# 01 State & Schemas

## SECTION: Global P Object (~L9489)

All app state lives in `const P = {...}`. Persisted to `localStorage` key `pp-data`.

### Core Data Arrays
| Key | Type | Persisted | Description |
|:---|:---|:---|:---|
| `name` | `string` | LS | Project name |
| `desc` | `string` | LS | Project description |
| `tasks` | `Task[]` | LS+Excel | Master task list |
| `members` | `Member[]` | LS+Excel | Team directory |
| `defects` | `Defect[]` | LS+Excel | Bug/quality tracker |
| `reports` | `Report[]` | LS+Excel | Saved report configs |
| `log` | `Log[]` | LS+Excel | Immutable audit trail |
| `features` | `Feature[]` | LS+Excel | Business feature groupings |
| `raids` | `RAID[]` | LS | Risk/Assumption/Issue/Dependency items |
| `decisions` | `Decision[]` | LS | Logged decisions with approval status |
| `baselines` | `Baseline[]` | LS+Excel | Historical baseline snapshots |
| `healthHistory` | `HealthEntry[]` | LS | Periodic health score log |
| `releases` | `Release[]` | LS+Excel | Release version configs |
| `alertHistory` | `Alert[]` | LS+Excel | Triggered alert archive |

### Configuration
| Key | Type | Persisted | Description |
|:---|:---|:---|:---|
| `dropdowns` | `Object` | LS+Excel | Registry: `status`, `priority`, `category`, `module`, `moduleType`, `role`, `memberStatus`, `defectStatus`, `defectPriority`, `defectSeverity`, `defectType`, `complexity`, `raidType/Impact/Probability/Severity/Status`, `decisionStatus` |
| `customFields` | `Field[]` | LS+Excel | Custom task metadata definitions |
| `defCustomFields` | `Field[]` | LS+Excel | Custom defect metadata definitions |
| `stepTemplates` | `Template[]` | LS+Excel | Reusable subtask workflow blueprints |
| `settings` | `Settings` | LS+Excel | Effort unit, work week, alert prefs |
| `cols` | `ColDef[]` | LS+Excel | Task grid column definitions (key, label, width, type) |
| `defCols` | `ColDef[]` | LS+Excel | Defect grid column definitions |
| `complexityFactors` | `Object` | LS | `{Easy:0.5, Medium:1.0, Complex:1.5}` |

### UI State (volatile — not in Excel export)
| Key | Type | Description |
|:---|:---|:---|
| `view` | `string` | Current view ID (`tasks`, `dash`, `team`, etc.) |
| `theme` | `string` | Active theme ID (20 themes) |
| `colorMode` | `string` | `default`, `light`, `dark` |
| `search` | `string` | Active search query |
| `filters` | `{status:Set, priority:Set, assignee:Set, module:Set, feature:Set}` | Active sidebar filters |
| `sort` | `{col:string, dir:'asc'|'desc'}` | Task grid sort state |
| `sbOpen` | `boolean` | Sidebar visibility |
| `ganttZoom` | `string` | Timeline zoom level: `day`, `week`, `month` |
| `taskViewMode` | `string` | `table` or `timeline` |
| `dashLayout` | `Widget[]|null` | Dashboard widget order & visibility |
| `reportLayout` | `Widget[]|null` | Report widget order & visibility |
| `widgetSpans` | `Object` | Per-widget column span overrides |
| `colOrder` | `string[]|null` | Custom column ordering |
| `colWidths` | `Object|null` | Custom column widths |
| `colFilters` | `Object` | Per-column inline filter values |
| `hiddenCols` | `string[]` | Hidden task grid columns |
| `defHiddenCols` | `string[]` | Hidden defect grid columns |
| `readonly` | `boolean` | View-Only mode flag |
| `showExplanations` | `boolean` | Toggle widget hint tooltips globally |
| `displayLevel` | `number` | Task hierarchy display depth (1=flat) |
| `collapsedNodes` | `Set` | Collapsed parent task IDs in grid |
| `expanded` | `Set` | Expanded task IDs |
| `dismissedAlerts` | `Set` | Alert fingerprints user has dismissed |
| `sidebarCollapsed` | `Object` | Sidebar section collapse state |
| `quickTipsCollapsed` | `boolean` | Quick Tips section state |
| `showInlineFilters` | `boolean` | Show column-level filter row |
| `showGanttDeps` | `boolean` | Show dependency lines in Gantt |
| `showGanttActuals` | `boolean` | Show actual dates overlay in Gantt |

### Scaffolder State
| Key | Type | Description |
|:---|:---|:---|
| `_scaffold` | `Object[]` | Active module definitions |
| `_scaffoldStep` | `number` | Current step (1-3) |
| `_scaffoldFeatures` | `Object[]` | Strategic feature alignment groups |
| `nextFeatId` | `number` | Auto-increment counter for `FEAT-001` |

### File System State
| Key | Type | Description |
|:---|:---|:---|
| `fsHandle` | `FileHandle` | Browser FS handle for Excel sync (stored in IDB) |
| `fsDirHandle` | `DirHandle` | Directory handle for folder sync |
| `fsDirName` | `string` | Directory name display |
| `lastSynced` | `ISO string` | Last successful file write |
| `lastBackup` | `ISO string` | Last successful IDB backup |
| `_isSaving` | `boolean` | Save lock flag |
| `_isLoading` | `boolean` | Load lock flag |
| `_fsPermissionError` | `boolean` | FS permission denied flag |

### Internal/Transient
| Key | Type | Description |
|:---|:---|:---|
| `_editingTaskId` | `string|null` | Task being edited in modal |
| `_editingMemberId` | `string|null` | Member being edited |
| `_editingReportId` | `string|null` | Report being edited |
| `_editingCfIdx` | `number|null` | Custom field being edited |
| `_pendingComment` | `string|null` | Comment awaiting submission |
| `_pvS` | `{rows:[], cols:[], vals:[]}` | Pivot table field selections |
| `activeReportId` | `string|null` | Currently viewed report ID |
| `lastView` | `string|null` | Previous view (for scroll restoration) |
| `_fieldsActiveTab` | `string` | Active tab in Registry view |

---

## SECTION: Entity Schemas

### Task
```
id: string               "TASK-001"
name: string              Title
status: string            Dropdown value
priority: string          Dropdown value
category: string          Dropdown value (Feature, Bug, Server Module, GUI Screen, etc.)
module: string            Dropdown value (e.g., "Core Engine")
moduleType: string        "Server" | "GUI" | "Interface"
assignee: string          Member name
release: string           Release version
startDate: string         YYYY-MM-DD
dueDate: string           YYYY-MM-DD
actCompletionDate: string YYYY-MM-DD (null if not done)
baselineStartDate: string YYYY-MM-DD
baselineDueDate: string   YYYY-MM-DD
forecastDueDate: string   YYYY-MM-DD
slippageReason: string    Free text
complexity: string        "Easy" | "Medium" | "Complex"
progress: number          0-100
estEffort: number         Estimated effort in active unit (hrs/days/months)
actEffort: number         Actual effort in active unit
baselineEffort: number    Baseline effort in active unit
dependsOn: string[]       Task IDs this depends on
notes: string             Multi-line text
subtasks: Subtask[]       Nested steps/screens
guiScreens: string[]      Linked screen names
updatedAt: string         ISO timestamp
parentId: string          Parent task ID (for hierarchy)
[customKey]: any          Custom field values
```

### Subtask
```
id: string           "ST-001"
name: string          Step title
status: string        Full status list
category: string      e.g., "GUI Screen"
done: boolean         (status === 'Completed')
effort: number        Estimated effort
actEffort: number     Actual effort
progress: number      0-100
type: string          "step" | "screen"
actCompletionDate: string
```

### Member
```
id: string            "MEM-001"
name: string          Full name
role: string          Job title
status: string        Active, On Leave, etc.
reportsTo: string     Manager name
email: string
phone: string
birthday: string      "DD MMM"
plannedLeaves: [{start: ISO, end: ISO, type: string}]
```

### Defect
```
id: string            "DEF-001"
title: string
type: string          Functional Bug, UI/UX Issue, Performance, Security, Data Issue, Suggestion
severity: string      S1-S4
priority: string
status: string        New, Assigned, Fixed, Retest, Closed, Rejected, Deferred
linkedType: string    "task" | "subtask" | "screen"
linkedId: string      ID of linked entity
assignee: string
reporter: string
desc: string
steps: string         Reproduction steps
createdAt: string     ISO
updatedAt: string     ISO
[customKey]: any      Custom defect field values
```

### Settings
```
effortUnit: "hrs" | "days" | "months"   Default: "days"
hoursPerDay: number                     Default: 8
daysPerWeek: number                     Default: 5
hoursPerWeek: number                    Default: 40
alertPrefs: {
  overdue: boolean, dueSoon: boolean, blocked: boolean,
  overloaded: boolean, leave: boolean, stale: boolean,
  milestone: boolean, daysUntilDue: number, staleDays: number
}
```

### Custom Field Definition
```
name: string
type: "text" | "number" | "date" | "dropdown" | "checkbox"
source: "local" | "global"        For dropdown fields
globalKey: string                  Maps to P.dropdowns[key]
options: string[]                  Manual options if source=local
required: boolean
```

### Dashboard/Report Layout Widget
```
id: string       Widget type ID (e.g., "burndown", "health")
t: string        Display title
on: boolean      Visible or hidden
span: number     Column span (2 or 4)
type: string     "standard" | "pivot" | "custom"
```

### Step Template (Blueprint)
```
name: string
category: string
steps: [{name: string, effort: number}]
```
