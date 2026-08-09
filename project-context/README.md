# ProjectPulse — High-Density AI Context Pack

This single document contains the authoritative architecture mapping, schema specifications, runtime business rules, and integration guidelines for **ProjectPulse**—a monolithic single-page project management suite (~70,000 lines of Vanilla HTML5/JS/CSS).

---

## 1. Codebase Architecture & File Map
The ProjectPulse repository consists of the monolithic core application, automated document compilers, and structured documentation assets.
```
ProjectPulse/
├── projectpulse.html            # Monolithic single-page application (~70,000 lines Vanilla HTML5/JS/CSS)
│   ├── CSS Stylesheet           # (Lines 110 – 13,428) 20 Curated Themes, Light/Dark modes, layout, animations
│   └── JavaScript Application   # (Lines 13,429 – 70,373) State, Persistence, CRUD, Gantt, Widgets, Scheduler
├── docs/                        # Authoritative product specifications and user guides
│   ├── user_manual/             # Compiled dynamic markdown user manuals
│   ├── screenshots/             # Cropped widget screenshot assets for manual illustrations
│   ├── stitch_projectpulse_design_assets/ # UI design components and specs
│   └── *.docx, *.pptx           # High-fidelity compiled Word documents and presentation decks
├── scripts/                     # Modular documentation compiler & maintenance toolchain
│   ├── build_all.py             # Master orchestrator for doc compilation
│   ├── build_fsd.py             # Functional Specification Document compiler
│   ├── build_pcd.py             # Product Capabilities Document compiler
│   ├── build_umi.py             # User Manual Index compiler
│   ├── build_user_manual_docx.py# User Manual docx compiler
│   ├── capture_screenshots.py   # Puppeteer-based automated page screenshot cropper
│   ├── capture_widgets.py       # Puppeteer-based automated widget screenshot cropper
│   ├── check_syntax.py          # AST syntax validator script for projectpulse.html
│   ├── docx_helpers.py          # Shared Word document styling, tables, XML helpers
│   ├── generate_diagrams.py     # Generates light-themed vector diagrams for document embedding
│   ├── patch_health_gauge.py    # Health gauge SVG animation patcher
│   ├── patch_steering_hero.py   # Steering hero component patcher
│   ├── schedule_manual_update.js# Scheduled task runner for documentation updates
│   └── update_manual.js         # Scrapes projectpulse.html dropdown configurations to update markdown docs
├── project-context/             # In-depth architectural & state schema context
│   ├── README.md                # Authoritative state schema mapping and business rules
│   ├── CHANGELOG.md             # Project milestones and release changelog
│   └── architecture_audit.md    # Codebase quality and refactoring assessment
└── graphify-out/                # Knowledge graph files for AST codebase navigation
    ├── GRAPH_REPORT.md          # Architecture report detailing god nodes and modular clusters
    ├── graph.html               # Interactive visual graph explorer
    ├── graph.json               # Graph structure dataset (nodes & edges)
    └── manifest.json            # Graph metadata manifest
```

---

## 2. Global State Schema (`P` Object)
The global state resides in `const P`. UI state is volatile, while core data and settings are persisted to **localStorage** (`pp-data`), **IndexedDB**, and **Excel**.

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
* `releases` (Release[]): Release version configurations (`id`, `name`, `startDate`, `date`, `status`).

### B. Configurations
* `dropdowns` (object): System registries (`status`, `priority`, `category`, `module`, `moduleType`, `role`).
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
* `view` (string): Current view ID (`tasks`, `dash`, `team`, `defects`, `reports`, `admin`, `log`, `releases`, `architect`).
* `theme` (string): Selected theme ID (`nexus`, `obsidian`, `emerald`, `fintech`, `bento`, `workflow`, `terracotta`, `codename`, etc.).
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
  category: string,           // Feature, Bug, Server Module, GUI Screen, DevOps, Backend, Frontend, etc.
  module: string,             // Dropdown module name
  moduleType: string,         // "Server" | "GUI" | "Interface" | "Service"
  assignee: string,           // Member name
  releaseVersion: string,     // Mapped version (e.g. "v1.0.0", "v2.0.0-Beta")
  startDate: string,          // YYYY-MM-DD
  dueDate: string,            // YYYY-MM-DD
  actualStartDate: string,    // YYYY-MM-DD
  actCompletionDate: string,  // YYYY-MM-DD (null if incomplete)
  baselineStartDate: string,  // YYYY-MM-DD
  baselineDueDate: string,    // YYYY-MM-DD
  forecastDueDate: string,    // YYYY-MM-DD
  slippageReason: string,     // Free text explanation
  complexity: string,         // "Easy" | "Medium" | "Complex"
  confidence: string,         // "High" | "Medium" | "Low"
  progress: number,           // 0 - 100
  estEffort: number,          // Estimated effort (in active effortUnit)
  actEffort: number,          // Actual logged effort (in active effortUnit)
  baselineEffort: number,     // Baseline effort (in active effortUnit)
  baseEstEffort: number,      // Unscaled base estimated effort
  dependsOn: string[],        // Mapped Task IDs
  notes: string,              // Multi-line description
  subtasks: Subtask[],        // Array of child steps/screens
  guiScreens: string[],       // Array of linked screen names
  createdAt: string,          // ISO timestamp
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
  status: string,             // "Not Started" | "In Progress" | "Completed"
  category: string,           // "GUI Screen" or step type
  done: boolean,              // status === 'Completed'
  effort: number,             // Estimated effort
  actEffort: number,          // Logged actual effort
  progress: number,           // 0 - 100
  type: string,               // "step" | "screen"
  startDate: string,          // YYYY-MM-DD
  dueDate: string,            // YYYY-MM-DD
  actCompletionDate: string   // YYYY-MM-DD (populated when status === 'Completed')
}
```

### Release
```typescript
{
  id: string,                 // "rel-1"
  name: string,               // "v2.0.0-Alpha", "v2.0.0-Beta", "v2.1.0"
  startDate: string,          // YYYY-MM-DD (Release start date)
  date: string,               // YYYY-MM-DD (Target release date)
  status: string              // "Released" | "Active" | "Planned"
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

### Log
```typescript
{
  ts: string,                 // ISO Timestamp (e.g. "2026-06-04T12:00:00Z")
  user: string,               // Member name who performed the action
  action: string,             // "Created" | "Updated" | "Status Changed" | "Deleted"
  taskId: string,             // Associated Task ID
  taskName: string,           // Associated Task name
  field: string,              // Mapped field name (e.g. "status", "dueDate", "actCompletionDate", "subtask.status")
  oldVal: string,             // Old value
  newVal: string,             // New value
  subtaskId: string,          // Optional. Associated Subtask ID
  actCompletionDate: string   // Optional. Retrospective actual completion date (YYYY-MM-DD)
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
* `renderReleases()` (~L54922): Renders the Release Roadmap table with version start dates, target dates, status badges, and mapped asset counts.

### B. CRUD Operations & Scheduling
* `createTask()` / `updateField()` / `deleteTask()` (~L11177-L11446): Manages task CRUD lifecycle.
* `addSubtask()` / `updateSubtask()` / `deleteSubtask()` (~L11457-L11502): Manages task checklist sub-steps.
* `syncTaskToTemplate(task)` (~L16460): Auto-generates or updates subtasks based on workflow step templates, inheriting completion states when parent tasks are complete.
* `PulseScheduler.recalcDatesAndStatus(task)` (~L21192): Recalculates effort rollups, parent task progress, auto-maps baseline dates from release roadmaps, and computes `actCompletionDate` fallbacks.

### C. Data Operations & Caching
* `buildDashCache(tasks, log)` (~L18000): **O(n) hot path.** Computes task stats, dependency lookups, entity resolution maps, and log frequencies in a single pass to power dashboard widgets at `O(1)`.
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
* **📅 [2026-06-04] Retrospective Completion Tracking**:
  - Implemented activity date normalization helpers (`getLogActivityDate`) using `actCompletionDate` fields.
  - Rewrote performance widgets, velocity metrics, and timelines to query activity dates retrospectively.
* **📅 [2026-06-14] Three-Document Suite & Build System**:
  - Implemented modular compilers (`build_pcd.py`, `build_fsd.py`, `build_umi.py`, `build_user_manual_docx.py`) orchestrated by `build_all.py` to compile core technical documents.
  - Developed `update_manual.js` to dynamically compile Markdown system configurations.
* **📅 [2026-06-15] Styling & Visual Enhancements**:
  - Added 10 custom architectural/workflow diagrams and 30 screenshot glossary mappings.
  - Upgraded docx designs to professional Segoe UI typography and grid layout guidelines.
* **📅 [2026-06-16] Knowledge Graph Exclusions**:
  - Excluded `docs/` and `scripts/` from Graphify analysis to focus graph navigation strictly on the code codebase.
* **📅 [2026-06-21] Project Steering & Health Widget Enhancement (ui-ux-pro-max)**:
  - Upgraded the Project Steering & Health widget inside `projectpulse.html` to match premium Swiss design guidelines.
  - Implemented an interactive horizontal timeline, bento-grid KPI cards, and custom gauge needle animations.
  - Styled overdue and blocked tables with clean layouts, segment tabs, and warning badges.
  - Added `scripts/check_syntax.py` to validate JavaScript syntax.
* **📅 [2026-08-09] Release Roadmap Date Alignment & Task Data Metric Reconciliation**:
  - Reconciled Release Roadmap start and target dates (`startDate`, `date`) across sample presets and added the missing `v2.1.0` release.
  - Performed data audit and reconciled all 143 sample tasks in `sampleTasks` and `samples.hierarchical.tasks` to eliminate discrepancies between task status and logged completion actuals.
  - Enhanced `syncTaskToTemplate` for completed subtask inheritance and `PulseScheduler.recalcDatesAndStatus` for `actCompletionDate` fallback calculation.
  - Cleaned temporary files and synchronized AST knowledge graph via `graphify update .`.

---

## 8. Modular Documentation Build System

ProjectPulse uses an automated document generation system that translates codebase configuration registries, schemas, and screenshots into formatted specifications:

### A. Dynamic Configuration Extraction
* **Source**: The script blocks inside [projectpulse.html](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html) define the authoritative UI states and database dropdown configurations.
* **Extraction**: `scripts/update_manual.js` loads the HTML page structure, parses JavaScript runtime settings (e.g. system dropdown categories, complexities), and rewrites them into [configuration_reference.md](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/configuration_reference.md) dynamically.

### B. High-Fidelity Word (.docx) Compilation
* **Layout Engines**: Individual python compilers (`build_pcd.py`, `build_fsd.py`, `build_umi.py`, `build_user_manual_docx.py`) load text data, markdown chapters, and diagram configurations.
* **Styling & Rendering**: Powered by `scripts/docx_helpers.py`, which provides XML abstractions for custom background borders, Margins (padding) in twentieths of a point (dxa), tables, callout blocks, headers/footers, and custom Segoe UI font properties to render documents match-themed to the ProjectPulse aesthetics.
* **Screenshots Automation**: Heads-up automated browsers (`capture_screenshots.py`, `capture_widgets.py`) spin up the single-page application in headless mode, inject project states, wait for animations to settle, take screenshots of interactive modules, and crop them directly to place inside user manual documents.
