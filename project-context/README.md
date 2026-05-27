# ProjectPulse — High-Density AI Context Pack

This single document contains the authoritative architecture mapping, schema specifications, runtime business rules, and integration guidelines for **ProjectPulse**—a monolithic single-page project management suite (~35,000 lines of Vanilla HTML5/JS/CSS).

---

## 1. Codebase Architecture & File Map
The entire application resides within [projectpulse.html](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html).
```
projectpulse.html
├── CSS Stylesheet (lines 1 – 8,960)
│   └── 20 Curated Themes, Dark/Light color modes, layout, components, and animations.
└── JavaScript Application (lines 8,960 – 35,000+)
    ├── Core Constants (STATUSES, VALID_TRANSITIONS, THEMES, CC colors)
    ├── State Definition: const P = { ... } (~L9489)
    ├── Storage & Backups (localStorage, IndexedDB ProjectPulseDB, File System Access API)
    ├── CRUD & Operations (createTask, updateField, addSubtask, saveMember, saveDefect)
    ├── View Renderers (renderTasksView, renderTimeline, renderDash, renderTeam, etc.)
    ├── Dashboard Aggregation Engine (buildDashCache, renderDash)
    ├── Excel Import/Export Engine (generateProjectWorkbook, reconstructProjectFromBuffer)
    ├── Project Scaffolder / Architect (renderScaffolder, generateFromScaffold)
    └── App Initialization (DOMContentLoaded, enterApp)
```

---

## 2. Global State Schema (`P` Object)
The global state resides in `const P`. UI state is volatile, while core data and settings are persisted to **localStorage** (`pp-data`) and **Excel**.

### A. Core Data Arrays
* `name` (string): Project name.
* `desc` (string): Project description.
* `tasks` (Task[]): Master task list.
* `members` (Member[]): Team member directory.
* `defects` (Defect[]): Defect tracking registry.
* `reports` (Report[]): Saved custom report layouts.
* `log` (Log[]): Audit history log (auto-pruned to last 500 entries).
* `features` (Feature[]): Strategic business feature alignments.
* `raids` (RAID[]): Risk, Assumption, Issue, and Dependency items.
* `decisions` (Decision[]): Project steering decisions.
* `baselines` (Baseline[]): Saved performance baselines.
* `releases` (Release[]): Release version configurations.

### B. Configurations
* `dropdowns` (object): System registries (`status`, `priority`, `category`, `module`, etc.).
* `customFields` / `defCustomFields` (Field[]): Custom task/defect attribute definitions.
* `stepTemplates` (Template[]): Workflow blueprints for subtask generation.
* `settings` (object): General system preferences (`effortUnit`, `hoursPerDay`, `daysPerWeek`, `workDays`, `alertPrefs`).
* `cols` / `defCols` (ColDef[]): Column layouts, sizes, and visibilities.
* `complexityFactors` (object): Effort multipliers (`{Easy: 0.5, Medium: 1.0, Complex: 1.5}`).

### C. Persistent File System State
* `fsHandle` (FileHandle): Linked Excel file handle (stored in IndexedDB).
* `fsDirHandle` (DirHandle): Linked Backup directory handle (stored in IndexedDB).
* `fsDirName` (string): Directory display name. Saved to Excel as `'Local Folder Sync Path'`.

### D. Volatile UI State
* `view` (string): Current view ID (`tasks`, `dash`, `team`, `defects`, `reports`, `admin`, `log`, etc.).
* `theme` (string): Selected theme ID (`nexus`, `obsidian`, `emerald`, `fintech`, `bento`, `workflow`, etc.).
* `colorMode` (string): Dark/Light mode overrides (`default`, `light`, `dark`).
* `filters` (object): Selected sidebar multi-filters.
* `sort` / `defSort` (object): Sorting columns and directions.
* `taskViewMode` (string): Tasks presentation (`table` or `timeline`).

---

## 3. Entity Schemas

### Task
```typescript
{
  id: string,                 // "TASK-001" (Unique)
  name: string,               // Title
  status: string,             // Not Started, In Progress, On Hold, Under Review, Completed, Cancelled
  priority: string,           // Critical, High, Medium, Low
  category: string,           // Feature, Bug, Server Module, GUI Screen, etc.
  module: string,             // Dropdown module name
  moduleType: string,         // "Server" | "GUI" | "Interface"
  assignee: string,           // Member name
  release: string,            // Mapped version (e.g. "v1.0.0")
  startDate: string,          // YYYY-MM-DD
  dueDate: string,            // YYYY-MM-DD
  actCompletionDate: string,  // YYYY-MM-DD (null if incomplete)
  baselineStartDate: string,  // YYYY-MM-DD
  baselineDueDate: string,    // YYYY-MM-DD
  forecastDueDate: string,    // YYYY-MM-DD
  slippageReason: string,     // Free text explanation
  complexity: string,         // "Easy" | "Medium" | "Complex"
  progress: number,           // 0 - 100
  estEffort: number,          // Estimated effort (in active effortUnit)
  actEffort: number,          // Actual logged effort (in active effortUnit)
  baselineEffort: number,     // Baseline effort (in active effortUnit)
  dependsOn: string[],        // Mapped Task IDs
  notes: string,              // Multi-line description
  subtasks: Subtask[],        // Array of child steps/screens
  guiScreens: string[],       // Array of linked screen names
  updatedAt: string,          // ISO timestamp
  parentId: string,           // Parent task ID (for sub-rows)
  [customKey]: any            // Dynamic custom fields
}
```

### Subtask
```typescript
{
  id: string,                 // "ST-001"
  name: string,               // Title
  status: string,             // Transition states
  category: string,           // "GUI Screen" or step type
  done: boolean,              // status === 'Completed'
  effort: number,             // Estimated effort
  actEffort: number,          // Actual effort
  progress: number,           // 0 - 100
  type: string,               // "step" | "screen"
  actCompletionDate: string   // YYYY-MM-DD
}
```

### Member
```typescript
{
  id: string,                 // "MEM-001"
  name: string,               // Display name
  role: string,               // Job title
  status: string,             // "Active" | "On Leave"
  plannedLeaves: Array<{start: string, end: string, type: string}>
}
```

### Defect
```typescript
{
  id: string,                 // "DEF-001"
  title: string,              // Title
  type: string,               // Functional Bug, UI/UX Issue, Performance, Security, etc.
  severity: string,           // S1 (Crash) - S4 (Cosmetic)
  priority: string,           // High, Medium, Low
  status: string,             // New, Assigned, Fixed, Retest, Closed, Rejected, Deferred
  linkedType: string,         // "task" | "subtask" | "screen"
  linkedId: string,           // ID of the target entity
  assignee: string,           // Assigned developer
  reporter: string,           // Reporter name
  desc: string,               // Description
  steps: string               // Repro steps
}
```

---

## 4. Core Function Registry

### A. View Rendering (Orchestration & Target Containers)
* `render()` (~L28550): Global dispatcher matching `P.view` to draw views into `#main-app`.
* `setView(v)` (~L28500): Sets active view, triggers scroll restoration, and executes `render()`.
* `renderTasksView()` (~L11744): Draws the task grid table, filters, and module rollups.
* `renderTimeline()` (~L13200): Draws the Gantt chart, dependency lines, and resize handlers.
* `renderDash()` (~L19100): Compiles the analytics dashboard in an off-screen `DocumentFragment` using cached values.

### B. CRUD Operations
* `createTask()` / `updateField()` / `deleteTask()` (~L11177-L11446): Manages task CRUD lifecycle.
* `addSubtask()` / `updateSubtask()` / `deleteSubtask()` (~L11457-L11502): Manages task checklist sub-steps.

### C. Data Operations & Caching
* `buildDashCache(tasks, log)` (~L18000): **O(n) hot path.** Computes task stats, dependency lookups, and log frequencies in a single pass to power dashboard widgets at `O(1)`.
* `getHealthScore()` (~L8983): Computes composite project health based on overdue, blocked, and on-hold tasks.
* `convertEffortToDays(eff, unit)` / `convertDaysToEffort(days, unit)` (~L11100): Dynamic scaling between `hrs`, `days`, and `months`.

### D. Persistence Lifecycle
* `save()` (~L10048): Debounced auto-save (10s idle) or immediate save via `Ctrl+S` or manual triggers. Writes to `localStorage` and triggers background directory/file backup writes.
* `saveToFile()` (~L10732): Generates and writes the ExcelJS binary buffer to the linked `P.fsHandle` file.
* `reconstructProjectFromBuffer(buf)` (~L28286): Parses import buffers, matches structures against `PROJECT_SCHEMA`, reconstructs task nesting, resolves missing fields, and runs migrations.

---

## 5. Storage & Persistence Tiers

| Tier | Engine | Store Key / Location | Capacity | Retention & Scope |
|:---|:---|:---|:---|:---|
| **Tier 1** | LocalStorage | `pp-data` | ~5MB | Primary application state, settings, and tables |
| **Tier 2** | IndexedDB | `ProjectPulseDB` | ~50MB+ | File handles, JSON state snapshots (last 10), and Excel Binary backups (last 5) |
| **Tier 3** | File System API | Connected Local Disk | Unlimited | Synchronized project Excel sheets and background directory backups |

---

## 6. Authoritative Business Rules

### A. Task Status Transitions
Status transitions must strictly match the following mapping. Comment logging is mandatory when entering `On Hold`, `Cancelled`, or `Under Review`.
```
[Not Started] ──> [In Progress] ──> [Under Review] ──> [Completed]
      │               │                   │
      └──> [Cancelled]◄───────────────────┘
              ▲
              └─── [On Hold] (reversible to In Progress / Under Review)
```

### B. Calculated Metrics
* **Health Index**:
  $$\text{Health} = 100 - \left( \frac{\text{Overdue}}{\text{Active}} \times 50 \right) - \left( \frac{\text{Blocked}}{\text{Active}} \times 30 \right) - \left( \frac{\text{On Hold}}{\text{Active}} \times 20 \right)$$
  *(Active refers to all tasks excluding Completed and Cancelled)*
* **Delivery Confidence**: Project pacing calculated by matching remaining active task backlog count against the team's 4-week moving average completion velocity (extracted from status logs). Pacing deficits linearly degrade confidence down to a minimum floor of 30%.
* **Blocking Dependencies**: A task is flagged as **Blocked** if any ID registered in its `dependsOn` array has a status other than `Completed`.

---

## 7. Change Log (Milestones)

* **📅 [2026-05-17] Dashboard & Themes**:
  - Implemented `buildDashCache()` to optimize rendering from $O(n)$ filters to $O(1)$ lookups.
  - Expanded themes registry with `terracotta`, `fintech`, `bento`, `codename`, and `workflow`.
* **📅 [2026-05-20] Configurable Effort System**:
  - Migrated legacy `Hours` variables to generic `Effort` variables with settings-based scaling support (`hrs`/`days`/`months`).
* **📅 [2026-05-27] Sparklines, High-Fidelity Exports, Theme Alignment & Local Folder Persistence**:
  - Replaced static sparklines with live dynamic health index datasets over time, rendering smooth Bezier curves.
  - Built custom canvas-based image copy rendering to ensure exported widget images exactly match active themes.
  - Restyled Screen Delivery filter pills/counters and Module matrix toggles to align with active theme CSS variables.
  - Increased Defect Inflow Trend widget analysis scale to 7 weeks and updated metric guides in the Help Modal.
  - Persisted Local Folder Sync Path directory name to the Excel System State sheet, allowing auto-restoration of File System Access directory handles on workbook import.
  - Added calculations for Health Index and Delivery Confidence to "How this view works" Help Guide modal.
