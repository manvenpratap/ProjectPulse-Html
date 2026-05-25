# 02 Functions & Views

## SECTION: Core Orchestration
| Function | ~Line | Purpose | Side Effects |
|:---|:---|:---|:---|
| `render()` | 28550 | Master UI dispatcher — calls view-specific render | Full DOM redraw of `#main-app` |
| `setView(v)` | ~28500 | Switch active view | Updates `P.view`, calls `render()` |
| `enterApp()` | ~28600 | Transition setup → main app | Shows `#main-app`, hides `#setup` |
| `resetToSetup()` | 10040 | Return to setup screen | Clears fsHandle, shows `#setup` |
| `withScroll(fn)` | 9431 | Wrap render in scroll-position preserver | Saves/restores scroll positions |

## SECTION: Rendering Functions
| View | Renderer | ~Line | Key Sub-functions |
|:---|:---|:---|:---|
| Tasks | `renderTasksView()` | 11744 | `renderTable()`, `renderGridHeader()`, `renderModuleRollups()` |
| Timeline | `renderTimeline()` | ~13200 | `drawGanttTasks()`, `drawDependencyLines()`, `initGanttResizer()` |
| Dashboard | `renderDash()` | ~19100 | `buildDashCache()` (~18000), `renderTopStats()`, `mkCC()` (16626) |
| Team | `renderTeam()` | ~13500 | `renderResourcesIntelligence()`, `renderTeamInspiration()` |
| Reports | `renderReports()` | ~15100 | `renderReportSection()`, `viewReport()` |
| Defects | `renderDefectsView()` | ~12600 | Defect grid + inline editing |
| Scaffolder | `renderScaffolder()` | 24886 | `renderScaffoldStep1()` (24904), `renderScaffoldStep2()` (25063), `renderScaffoldStep3()` |
| Features | `renderFeatureInsights()` | 17686 | Feature hub cards + progress |
| Registry | `renderFieldsView()` | ~26800 | `renderDropdownsView()`, `renderStepsView()` |
| Audit Log | `renderLog()` | ~12000 | Log table + filters |
| Sidebar | `renderSidebar()` | ~28200 | Filters, mini-map, module rollups |

## SECTION: CRUD Operations
| Entity | Create | Update | Delete | Other |
|:---|:---|:---|:---|:---|
| Task | `createTask()` 11177 | `updateField()` 11314 | `deleteTask()` 11446 | `duplicateTask()`, `confirmDeleteTask()` |
| Subtask | `addSubtask()` 11457 | `updateSubtask()` 11467 | `deleteSubtask()` 11502 | `toggleSubtask()` |
| Member | `saveMember()` | `—` | `deleteMember()` | `openMemberModal()` |
| Defect | `saveDefect()` | `—` | `deleteDefect()` | `openDefectModal()` |
| Report | `saveReport()` | `—` | `deleteReport()` | `viewReport()` |
| Feature | `saveFeature()` | `—` | `deleteFeature()` | `renderFeatureInsights()` |

## SECTION: Persistence & File System
| Function | ~Line | Purpose |
|:---|:---|:---|
| `save()` | 10048 | Debounced save to LS + optional FS write. 10s idle auto-save, `Ctrl+S` manual |
| `load()` | 10099 | Hydrate `P` from LS, run migrations, safe property checks |
| `getDB()` | 10237 | Open/create IndexedDB `ProjectPulseDB` |
| `saveHandle()` / `getHandle()` | 10261/10268 | Persist/retrieve FS handles in IDB |
| `createBackup()` | 10290 | JSON snapshot to IDB (10-min interval, keep last 10) |
| `createFileBackup()` | 10336 | Binary Excel blob backup to IDB (keep last 5) |
| `saveToFile()` | 10732 | Write workbook to linked Excel file via FS API |
| `loadFromFile()` | 10777 | Read workbook from linked file |
| `exportProjectExcel()` | ~22500 | Generate + download full Excel workbook |
| `generateProjectWorkbook()` | ~22600 | Build ExcelJS workbook with all sheets |
| `importProjectExcel()` | ~23800 | Upload + parse Excel file |
| `reconstructProjectFromBuffer()` | ~24000 | Rebuild hierarchical `P` from flat Excel rows |
| `exportProjectCSV()` | — | CSV export of tasks |
| `exportLogCSV()` | — | CSV export of audit log |

## SECTION: Dashboard Engine
| Function | Purpose |
|:---|:---|
| `buildDashCache(tasks, log)` | Single O(n) pass: groups tasks by status, priority, assignee, module, category; builds `taskById`, `subtaskById`, `screenByName`, `subtasksByScreen`, `statusLogsByTaskId` |
| `renderDash()` | Builds all widgets in DocumentFragment, uses dashCache for O(1) lookups, queues chart draws in `requestAnimationFrame` |
| `mkCC(title, subtitle, id, extra, type, hint, hintLabel, icon)` | Card Component Constructor — standardizes all widget cards |
| `renderCustomWidget()` | Pivot table / user-defined widget rendering |

### Dashboard Widgets (18 total, `defDashLay`)
| ID | Title | Type |
|:---|:---|:---|
| `summary` | Summary Cards | KPI cards (total, done, in-prog, overdue, blocked) |
| `module_status_matrix` | Strategic Module Status | Module×Type status heatmap |
| `health` | Project Health | Composite score gauge (0-100) |
| `defect_intel` | Defect Intelligence | Severity, priority, type, module charts + resolution rate |
| `feature_insights` | Feature Intelligence | Feature maturity & readiness tracker |
| `release_timeline` | Release Timeline | Upcoming 30-60 day milestone roadmap |
| `burndown` | Burndown Chart | Ideal vs actual remaining effort |
| `velocity` | Weekly Velocity | Completed effort + 3-week rolling average |
| `cfd` | Cumulative Flow | 8-week status distribution stacked area |
| `milestone-timeline` | Milestone Timeline | Interactive project milestone markers |
| `module_health` | Module & Release Health | Hierarchical progress by module side |
| `screen_status` | Screen Status Details | Per-screen delivery progress |
| `workload` | Team Workload | Stacked bar by assignee × status |
| `cat_hours` | Category & Effort | Category distribution + est/act effort comparison |
| `overdue` | Overdue Attention | Overdue task cards + details |
| `intelligence` | Predictive Intelligence | ETA forecast, aging, bottleneck, capacity, critical path |
| `activity` | Recent Activity | Latest audit log entries |
| `analytics` | Advanced Analytics | Consolidated burndown + velocity + CFD executive view |

## SECTION: Specialized Tools
| Function | Purpose |
|:---|:---|
| `openCmdPalette()` / `renderCmdResults()` | Command Palette (`Cmd+K`) |
| `checkAlerts()` / `renderAlertsPanel()` | Real-time alert system |
| `openBulkModuleFlyout()` | Scaffold bulk module import |
| `generateFromScaffold()` | Create tasks/features from scaffold state |
| `syncDropdowns()` | Cascade dropdown changes to existing entities |
| `syncEffortColumnLabels()` | Rename grid headers when effort unit changes |
| `convertEffortToDays()` / `convertDaysToEffort()` | Effort unit conversion |
| `triggerConfetti()` | Celebration animation on task completion |

## SECTION: Views & UI Map

### Persistent Shell
- **Sidebar `#sidebar`**: Nav links, search, multi-select filters (status/priority/assignee/module/feature), progress+date range sliders, module rollups, dashboard mini-map (drag-to-reorder)
- **Topbar `#topbar`**: Sidebar toggle, health indicator `#tb-health`, view title, stats (Total/Done), alert icon, theme toggle, `Cmd+K`

### View Panels (rendered in `#main-app`)
| View ID | Title | Container | Key State |
|:---|:---|:---|:---|
| `tasks` | Tasks Matrix | `#view-tasks` | `P.tasks`, `P.filters`, `P.sort`, `P.cols` |
| `timeline` | Project Timeline | `#view-timeline` | `P.tasks`, `P.ganttZoom` |
| `team` | Team Intelligence | `#view-team` | `P.members`, `P.tasks` |
| `dash` | Intelligence Dash | `#view-dash` | `P.tasks`, `P.defects`, `P.dashLayout` |
| `reports` | Reporting Suite | `#view-reports` | `P.reports`, `P.tasks` |
| `defects` | Defect Workshop | `#view-defects` | `P.defects`, `P.defCols` |
| `scaffolder` | Project Architect | `#view-scaffolder` | `P._scaffold`, `P._scaffoldStep` |
| `fields` | Registry Workshop | `#view-fields` | `P.customFields`, `P.defCustomFields` |
| `dropdowns` | Lookup Registry | `#view-dropdowns` | `P.dropdowns` |
| `steps` | Workflow Blueprints | `#view-steps` | `P.stepTemplates` |
| `features` | Feature Hub | `#feature-hub` | `P.features`, `P.tasks` |

### Modals & Flyouts
| Element | Purpose |
|:---|:---|
| `#modal` | Reused for Task/Member/Defect/Report CRUD |
| `#flyout` | Right-side task quick-edit drawer |
| `#cmd-palette` | Command Palette overlay |
| `#theme-flyout` | 20-theme selector with live preview |
| `#alerts-flyout` | Notification hub |
| `#snapshots-drawer` | Historical backup viewer |
| `#dash-builder-modal` | Dashboard widget layout editor |
| `#report-builder-modal` | Report widget layout editor |
| `#view-help-modal` | Context-sensitive help (`?` key) |

## SECTION: Hot Paths
1. `save()` — debounced 10s idle + `Ctrl+S` manual. Writes LS + optional FS
2. `render()` — global UI refresh after navigation or data changes
3. `syncDropdowns()` — ensures column options match `P.dropdowns`
4. `getHealthScore()` — calculated for topbar + dashboard + reports
5. `buildDashCache()` — pre-computes all dashboard metrics in one pass
