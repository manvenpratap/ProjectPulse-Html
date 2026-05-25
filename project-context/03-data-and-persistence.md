# 03 Data, Persistence & Business Rules

## SECTION: Startup Flow
1. `DOMContentLoaded` fires
2. `load()` hydrates `P` from `localStorage['pp-data']`
3. Runs migrations: hours→effort rename, safe property checks (`P.defects = P.defects || []`)
4. `syncDropdowns()` populates column option arrays
5. `setTheme(P.theme)` applies active theme
6. If valid project exists → `enterApp()` → `render()`
7. `checkAlerts()` starts background alert monitoring

## SECTION: Save/Load Lifecycle

### Save Pipeline (`save()` ~L10048)
```
User action → state mutation → addLog() → save() triggers:
  1. Serialize P → localStorage['pp-data']
  2. If 10min since last → createBackup() → IDB snapshot (keep 10)
  3. If P.fsHandle exists → saveToFile() → write Excel to disk
     └── createFileBackup() → IDB binary backup (keep 5)
```

### Save Behavior
- **Auto-save**: 10-second idle debounce timer (`_fileSaveTimer`)
- **Manual save**: `Ctrl+S` → immediate `save()` + "Data saved" notification
- **"Save to File" button**: Explicit save trigger in topbar (File Mode only)
- **Saving overlay**: GPU-accelerated "Saving..." indicator during Excel generation
- **Lock guard**: `_isSaving` flag prevents concurrent save operations

### Storage Tiers
| Tier | Store | Key/DB | Capacity | Purpose |
|:---|:---|:---|:---|:---|
| 1 | localStorage | `pp-data` | ~5MB | Primary state persistence |
| 2 | IndexedDB | `ProjectPulseDB` | ~50MB+ | Handles, backups, binary blobs |
| 3 | File System API | User's disk | Unlimited | Excel file sync |

### IndexedDB Stores
| Store | Contents | Retention |
|:---|:---|:---|
| `handles` | `FileSystemFileHandle` objects | Permanent |
| `backups` | JSON snapshots | Last 10 |
| `backups` (file) | Binary Excel blobs | Last 5 |

## SECTION: Excel Export/Import

### Export (`generateProjectWorkbook()` ~L22600)
Sheets generated:
1. **Executive_Dashboard** — calculated KPIs, health, velocity
2. **Data_Tasks** — flat task rows with dynamic effort headers
3. **Data_Subtasks** — exploded subtask rows with parent task ID
4. **Data_Members** — team directory
5. **Data_Defects** — defect registry
6. **Data_Features** — feature groupings
7. **Rel_TaskDependencies** — `taskId → dependsOnId` pairs
8. **Rel_GUIScreens** — `taskId → screenName` pairs
9. **Config_Dropdowns** — all registry values
10. **Config_GridColumns** — column definitions
11. **Config_Templates** — step template definitions
12. **Config_Layouts** — dashboard + report widget configs
13. **State_Filters** — active filter state
14. **Baseline_History** — baseline snapshots
15. **Activity Log** — audit log dump
16. **Reports** — saved report data
17. **Alert History** — alert archive

### Import (`reconstructProjectFromBuffer()` ~L24000)
- Maps sheet names → `P` properties
- Rebuilds relational arrays (dependencies, screens) by joining cross-reference sheets
- Validates against `PROJECT_SCHEMA`
- Runs effort key migration (legacy hours → effort)
- Dynamic column header parsing based on effort unit

### Critical Rule
> Any change to `PROJECT_SCHEMA` or `PROJECT_RELATIONAL_MODEL` MUST be reflected in BOTH export and import to prevent data loss on Excel round-trips.

## SECTION: Business Rules

### Status Transitions (`VALID_TRANSITIONS`)
| From | Allowed To |
|:---|:---|
| Not Started | In Progress, Completed, Cancelled |
| In Progress | On Hold, Under Review, Completed, Cancelled |
| On Hold | In Progress, Under Review, Cancelled |
| Under Review | In Progress, On Hold, Completed, Cancelled |
| Completed | In Progress, Under Review |
| Cancelled | Not Started |

> Moving to `On Hold`, `Cancelled`, or `Under Review` requires a mandatory comment (`COMMENT_REQUIRED`).
> Subtasks and workflow steps follow the **same** transitions as main tasks.

### Category Auto-Assignment
| Entity | Condition | Category |
|:---|:---|:---|
| Task | `moduleType === 'GUI'` | GUI Module |
| Task | `moduleType === 'Server'` | Server Module |
| Subtask | `type === 'screen'` | GUI Screen |

### Health Score (`getHealthScore()` ~L8983)
```
Base: 100
- (overdue_count / active_count) × 50
- (blocked_count / active_count) × 30
- (on_hold_count / active_count) × 20
= Score (0-100)
```
Active = tasks excluding Completed and Cancelled.

### Dependency Logic (`isBlocked()` ~L8974)
A task is **Blocked** if any task ID in `dependsOn` has status ≠ Completed.

### Effort Tracking System
- Unit configured in `P.settings.effortUnit`: `hrs`, `days`, or `months`
- Conversion: `hrs ÷ hoursPerDay = days`, `months × 4 × daysPerWeek = days`
- `convertEffortToDays(effort, unit)` / `convertDaysToEffort(days, unit)`
- Changing unit scales all tasks' estEffort, actEffort, baselineEffort proportionally
- `syncEffortColumnLabels()` renames grid column headers dynamically
- Excel headers also reflect active unit (e.g., "Estimated Days")

### Scheduling
- `addBusDays(date, days)` — adds working days, skips weekends per `daysPerWeek`
- `getBusinessDays(start, end)` — counts working days between dates
- Tasks cannot have `dueDate` before `startDate` (UI highlights mismatch)

### Progress Rollup
- **Manual**: User sets 0-100 directly
- **Subtask-driven**: If task has subtasks, parent progress = weighted % of completed subtasks
- Status `Completed` → `progress = 100`, `Not Started` → `progress = 0`
- Confetti animation on subtask completion

### Defect Severity/Priority
- **Severity (S1-S4)**: Technical impact (S1=Crash, S4=Cosmetic)
- **Priority**: Business urgency
- S1/S2 defects auto-flag linked task as "High Priority"

### Data Integrity
- Task IDs must be unique project-wide
- Cascade delete: deleting parent removes all children + subtasks
- Custom `dropdown` fields must map to `P.dropdowns` values if `source=global`

## SECTION: Schema Migrations (in `load()`)
| Migration | Trigger | Action |
|:---|:---|:---|
| Hours → Effort | `task.estHours` exists | Rename `estHours→estEffort`, `actHours→actEffort`, `baselineHours→baselineEffort`, `baseEstHours→baseEstEffort` |
| Column keys | `P.cols` has `estHours` key | Rename to `estEffort`, etc. |
| Safe defaults | Missing arrays | `P.defects = P.defects || []`, etc. |
| Sample screens | Known missing screens | Add to hierarchical sample tasks |
| Settings | Missing settings | Default `effortUnit:'days'`, `hoursPerDay:8`, `daysPerWeek:5` |
