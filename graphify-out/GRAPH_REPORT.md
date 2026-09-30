# Graph Report - ProjectPulse  (2026-09-30)

## Corpus Check
- 4 files · ~384,041 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2405 nodes · 4964 edges · 61 communities (51 shown, 10 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `da0b6409`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Configuration & Reference & Status|Configuration & Reference & Status]]
- [[_COMMUNITY_Readme & State & Block|Readme & State & Block]]
- [[_COMMUNITY_Architecture & Audit & State|Architecture & Audit & State]]
- [[_COMMUNITY_Manual & State & Md|Manual & State & Md]]
- [[_COMMUNITY_Changelog & 2026 & 05|Changelog & 2026 & 05]]
- [[_COMMUNITY_Schedule & Manual & Check|Schedule & Manual & Check]]
- [[_COMMUNITY_Readme & Typescript & Entity|Readme & Typescript & Entity]]
- [[_COMMUNITY_Scheduler & The & Heuristic|Scheduler & The & Heuristic]]
- [[_COMMUNITY_Overview & Md & Executive|Overview & Md & Executive]]
- [[_COMMUNITY_Risks & Raid & Md|Risks & Raid & Md]]
- [[_COMMUNITY_Readme & Md & Project|Readme & Md & Project]]
- [[_COMMUNITY_Delivery & Md & Hierarchical|Delivery & Md & Hierarchical]]
- [[_COMMUNITY_Insights & Burn & Md|Insights & Burn & Md]]
- [[_COMMUNITY_Team & Capacity & Role|Team & Capacity & Role]]
- [[_COMMUNITY_Defects & Defect & Bug|Defects & Defect & Bug]]
- [[_COMMUNITY_Reports & Board & Md|Reports & Board & Md]]
- [[_COMMUNITY_Activity & Md & Audit|Activity & Md & Audit]]
- [[_COMMUNITY_Project & Status & Md|Project & Status & Md]]
- [[_COMMUNITY_User Manual & Architecture & Sync|User Manual & Architecture & Sync]]
- [[_COMMUNITY_Delivery Matrix & Hierarchy & Edit|Delivery Matrix & Hierarchy & Edit]]
- [[_COMMUNITY_Capacity & Workload & Role|Capacity & Workload & Role]]
- [[_COMMUNITY_Defect Tracker & Bug Lifecycle|Defect Tracker & Bug Lifecycle]]
- [[_COMMUNITY_Reports & Board & Export|Reports & Board & Export]]
- [[_COMMUNITY_Audit Log & Activity & Session|Audit Log & Activity & Session]]
- [[_COMMUNITY_Widgets & Capture & Screenshot|Widgets & Capture & Screenshot]]
- [[_COMMUNITY_Status & Dashboard & Live|Status & Dashboard & Live]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]

## God Nodes (most connected - your core abstractions)
1. `$id()` - 163 edges
2. `$id()` - 151 edges
3. `$id()` - 151 edges
4. `save()` - 64 edges
5. `save()` - 63 edges
6. `save()` - 63 edges
7. `notify()` - 58 edges
8. `notify()` - 58 edges
9. `notify()` - 58 edges
10. `renderSidebar()` - 35 edges

## Surprising Connections (you probably didn't know these)
- `renderBackupList()` --calls--> `warn()`  [EXTRACTED]
  temp_test.js → temp_test.js  _Bridges community 19 → community 27_
- `syncFsDirectory()` --calls--> `error()`  [EXTRACTED]
  temp_test.js → temp_test.js  _Bridges community 35 → community 27_
- `restoreFromFileBackup()` --calls--> `error()`  [EXTRACTED]
  temp_test.js → temp_test.js  _Bridges community 35 → community 7_
- `updateCxoEmailPreview()` --calls--> `error()`  [EXTRACTED]
  temp_test.js → temp_test.js  _Bridges community 35 → community 19_
- `showViewHelp()` --calls--> `$id()`  [EXTRACTED]
  temp_test.js → temp_test.js  _Bridges community 5 → community 7_

## Communities (61 total, 10 thin omitted)

### Community 0 - "Configuration & Reference & Status"
Cohesion: 0.0
Nodes (498): aCard, acCard, acPath, _act, active, activeEffortSum, activeIdx, activeModal (+490 more)

### Community 1 - "Readme & State & Block"
Cohesion: 0.01
Nodes (89): activeModal, allDone, anyStarted, autoFitAllCols(), blocked, bulkDeleteTasks(), bulkSelectedTasks, c (+81 more)

### Community 2 - "Architecture & Audit & State"
Cohesion: 0.01
Nodes (82): activeModal, allDone, anyStarted, autoFitAllCols(), blocked, bulkDeleteTasks(), bulkSelectedTasks, c (+74 more)

### Community 3 - "Manual & State & Md"
Cohesion: 0.04
Nodes (92): addDDValueV(), addLog(), addRelease(), applyDashLayout(), applyReportLayout(), applyTemplate(), autoPopulateReport(), buildBoardPackContent() (+84 more)

### Community 4 - "Changelog & 2026 & 05"
Cohesion: 0.04
Nodes (81): addDDValueV(), addLog(), addNewGUIScreen(), addRelease(), applyDashLayout(), applyReportLayout(), applyTemplate(), applyWorkflowTemplate() (+73 more)

### Community 5 - "Schedule & Manual & Check"
Cohesion: 0.05
Nodes (72): addCustomFieldV(), addDep(), addLeaveRow(), autoInferCategory(), autoInferRelease(), cancelTplConfirmV(), clearPvFilt(), closeCmdPalette() (+64 more)

### Community 6 - "Readme & Typescript & Entity"
Cohesion: 0.05
Nodes (71): addCustomFieldV(), addDep(), addLeaveRow(), cancelTplConfirmV(), clearPvFilt(), closeCmdPalette(), closeCtx(), closeDefectLinkDropdown() (+63 more)

### Community 7 - "Scheduler & The & Heuristic"
Cohesion: 0.06
Nodes (68): addDDValueV(), addLog(), applyBulkEdit(), applyDashLayout(), applyReportLayout(), applyTemplate(), autoPopulateReport(), buildBoardPackContent() (+60 more)

### Community 8 - "Overview & Md & Executive"
Cohesion: 0.05
Nodes (68): addDep(), addLeaveRow(), cancelTplConfirmV(), clearPvFilt(), closeCmdPalette(), closeCtx(), closeDefectFlyout(), closeDefectLinkDropdown() (+60 more)

### Community 9 - "Risks & Raid & Md"
Cohesion: 0.05
Nodes (57): addCustomFieldV(), addScaffoldRow(), autoPopulateReport(), cancelEditFeature(), captureAreaAsCanvas(), captureFullFeatureGantt(), captureFullGanttChart(), closeAllFlyouts() (+49 more)

### Community 10 - "Readme & Md & Project"
Cohesion: 0.06
Nodes (51): autoResolveAllSchedulerConflicts(), autoSequenceAssignee(), changeSchedulerWeek(), clearMatrixFilter(), closeRaidFlyout(), deleteRaidItem(), deleteRaidItemById(), filterDashboardMetric() (+43 more)

### Community 11 - "Delivery & Md & Hierarchical"
Cohesion: 0.07
Nodes (47): clearMatrixFilter(), closeRaidFlyout(), deleteFeature(), deleteRaidItem(), deleteRaidItemById(), filterDashboardMetric(), filterDefectsBy(), filterRaid() (+39 more)

### Community 12 - "Insights & Burn & Md"
Cohesion: 0.07
Nodes (41): autoResolveAllSchedulerConflicts(), autoSequenceAssignee(), changeSchedulerWeek(), clearMatrixFilter(), filterRaid(), filterTasksByAssignee(), findScheduleConflicts(), generateIntelligentSuggestions() (+33 more)

### Community 13 - "Team & Capacity & Role"
Cohesion: 0.1
Nodes (36): autoFitCol(), doGridSort(), doSort(), downloadGanttAsHtml(), finalizeColOrder(), getFiltered(), getGridFiltered(), getGridPK() (+28 more)

### Community 14 - "Defects & Defect & Bug"
Cohesion: 0.07
Nodes (35): applyPvFilt(), cancelEditCw(), cap(), createBaselineSnapshot(), deleteBaselineSnapshot(), editCustomWidgetCtx(), editCw(), editReport() (+27 more)

### Community 15 - "Reports & Board & Md"
Cohesion: 0.07
Nodes (32): addScaffoldRow(), createBaselineSnapshot(), createFileBackup(), deleteBaselineSnapshot(), duplicateScaffoldRow(), editReport(), generateFromScaffold(), generateProjectWorkbook() (+24 more)

### Community 16 - "Activity & Md & Audit"
Cohesion: 0.08
Nodes (31): addEmptyState(), addGrid(), addST(), esc(), formatDateStringFriendly(), getModuleMilestones(), _matrixCellHover(), _matrixStateChange() (+23 more)

### Community 17 - "Project & Status & Md"
Cohesion: 0.08
Nodes (31): addEmptyState(), addGrid(), addST(), esc(), formatDateStringFriendly(), getModuleMilestones(), _matrixCellHover(), _matrixStateChange() (+23 more)

### Community 18 - "User Manual & Architecture & Sync"
Cohesion: 0.12
Nodes (29): applyBulkEdit(), autoFitCol(), doGridSort(), doSort(), finalizeColOrder(), getGridFiltered(), getGridPK(), getGridSorted() (+21 more)

### Community 19 - "Delivery Matrix & Hierarchy & Edit"
Cohesion: 0.15
Nodes (28): closeCxoEmailFlyout(), closeCxoEmailModal(), computeCxoStatusBreakdown(), computeGlobalStats(), copyCxoEmailToClipboard(), copyCxoPlainTextToClipboard(), copyCxoRichTextToClipboard(), escapeHTML() (+20 more)

### Community 20 - "Capacity & Workload & Role"
Cohesion: 0.13
Nodes (27): applyBulkEdit(), autoFitCol(), doGridSort(), doSort(), finalizeColOrder(), getGridFiltered(), getGridPK(), getGridSorted() (+19 more)

### Community 21 - "Defect Tracker & Bug Lifecycle"
Cohesion: 0.08
Nodes (24): 12 Change Log Baseline, 📅 [2026-05-14] - Baseline Documentation Established, 📅 [2026-05-17] - Dashboard Rendering Optimization (O(1) Caching & Batched Drawing), 📅 [2026-05-17] - Defect Categories Widget `undefined` Chart Label Fix, 📅 [2026-05-17] - Defect Hotspots Entity Resolution Fix, 📅 [2026-05-17] - Defect Intelligence Widget `Unlinked` Module Mapping Resolution, 📅 [2026-05-17] - Dynamic Dashboard Mini-Map Integration, 📅 [2026-05-17] - Premium Theme Expansion (User Request #3) (+16 more)

### Community 22 - "Reports & Board & Export"
Cohesion: 0.09
Nodes (26): addNewGUIScreen(), aggregateCustomData(), animateCounter(), applyWorkflowTemplate(), commitWhatIfScenario(), entries, fmtDate(), getFilteredLogs() (+18 more)

### Community 23 - "Audit Log & Activity & Session"
Cohesion: 0.11
Nodes (24): applyPvFilt(), cancelEditCw(), cap(), editCustomWidgetCtx(), editCw(), getFieldType(), _matrixCellClick(), moveDashSec() (+16 more)

### Community 24 - "Widgets & Capture & Screenshot"
Cohesion: 0.09
Nodes (23): addRelease(), addScaffoldRow(), createBaselineSnapshot(), deleteBaselineSnapshot(), deleteRelease(), duplicateScaffoldRow(), generateFromScaffold(), loadScaffoldTemplate() (+15 more)

### Community 25 - "Status & Dashboard & Live"
Cohesion: 0.12
Nodes (22): autoResolveAllSchedulerConflicts(), autoSequenceAssignee(), changeSchedulerWeek(), findScheduleConflicts(), formatDateStringFriendly(), generateIntelligentSuggestions(), getTeamNames(), getWorkDaysForWeekOffset() (+14 more)

### Community 26 - "Community 26"
Cohesion: 0.1
Nodes (19): 1. Global State Schema & Lifecycle, 1. In-place Mutation of Legacy Globals, 2. Core Subsystem Map, 2. High Mixing of Business Logic and DOM Operations, 3. Identified Code Smells, Redundancies, and Coupling, 3. Redundant / Brittle Script Utilities (`fix_orphan.py` bug), 4. Refactoring Strategy, A. Scheduling Engine (`recalcDatesAndStatus` & `recalcGUIScreen`) (+11 more)

### Community 27 - "Community 27"
Cohesion: 0.12
Nodes (20): addEmptyState(), createFileBackup(), esc(), listBackups(), _matrixCellClick(), mkPill(), openAddTask(), openFlyout() (+12 more)

### Community 28 - "Community 28"
Cohesion: 0.12
Nodes (18): addNewGUIScreen(), applyWorkflowTemplate(), commitWhatIfScenario(), fmtDate(), markAllGUIStepsDone(), openEwsModal(), openScreenFlyout(), renderGUIScreens() (+10 more)

### Community 29 - "Community 29"
Cohesion: 0.16
Nodes (17): applyPvFilt(), cancelEditCw(), cap(), editCustomWidgetCtx(), editCw(), getFieldType(), moveDashSec(), moveRptSec() (+9 more)

### Community 30 - "Community 30"
Cohesion: 0.18
Nodes (17): clearProjectState(), computeAlerts(), dismissAlert(), dismissAllAlerts(), enterApp(), loadSample(), moveViewOrder(), nowISO() (+9 more)

### Community 31 - "Community 31"
Cohesion: 0.18
Nodes (17): clearProjectState(), computeAlerts(), dismissAlert(), dismissAllAlerts(), enterApp(), loadSample(), moveViewOrder(), nowISO() (+9 more)

### Community 32 - "Community 32"
Cohesion: 0.13
Nodes (14): code:bash (# Using Node.js), code:block2 (ProjectPulse/), code:bash (node scripts/update_manual.js), code:bash (python scripts/build_all.py), code:bash (python scripts/check_syntax.py), code:bash (graphify update .), Core Capabilities:, 🛠️ Developer Guidelines (+6 more)

### Community 33 - "Community 33"
Cohesion: 0.14
Nodes (15): clearProjectState(), enterApp(), initApp(), initDesignSpells(), initGanttResizer(), load(), loadCustomLayouts(), loadRecentProject() (+7 more)

### Community 34 - "Community 34"
Cohesion: 0.16
Nodes (14): captureAreaAsCanvas(), captureFullGanttChart(), copyAllShares(), copyChart(), copyWidgetAsImage(), downloadGanttAsHtml(), exportFeatureMatrixExcel(), exportLogCSV() (+6 more)

### Community 35 - "Community 35"
Cohesion: 0.22
Nodes (13): captureAreaAsCanvas(), captureFullFeatureGantt(), captureFullGanttChart(), copyAllShares(), copyChart(), copyWidgetAsImage(), error(), exportProjectExcel() (+5 more)

### Community 36 - "Community 36"
Cohesion: 0.24
Nodes (13): closeRaidFlyout(), computeAlerts(), deleteRaidItem(), deleteRaidItemById(), dismissAlert(), dismissAllAlerts(), nowISO(), pruneAlertHistory() (+5 more)

### Community 37 - "Community 37"
Cohesion: 0.17
Nodes (12): cancelEditFeature(), closeAllFlyouts(), closeFeatFlyout(), closeTplFlyout(), finalizeTplUpdateV(), getRaidAgeDays(), getRaidDateSince(), importScaffoldBulk() (+4 more)

### Community 38 - "Community 38"
Cohesion: 0.2
Nodes (12): draw(), drawAgeBars(), drawBarChart(), drawDonut(), drawGroupedBar(), drawHBar(), drawMiniHistory(), drawSpark() (+4 more)

### Community 39 - "Community 39"
Cohesion: 0.22
Nodes (11): 3. Entity Schemas, code:typescript ({), code:typescript ({), code:typescript ({), code:typescript ({), code:typescript ({), Defect, Member (+3 more)

### Community 40 - "Community 40"
Cohesion: 0.2
Nodes (11): addGrid(), addST(), mkCC(), mkCvs(), pivotTasks(), renderCustomWidget(), renderPivotGrid(), renderResourcesIntelligence() (+3 more)

### Community 41 - "Community 41"
Cohesion: 0.18
Nodes (11): commitWhatIfScenario(), fmtDate(), openEwsModal(), openScreenFlyout(), renderOverviewView(), renderWhatIfSandbox(), resetWhatIfSandbox(), runEarlyWarningScanners() (+3 more)

### Community 42 - "Community 42"
Cohesion: 0.22
Nodes (8): 1. Codebase Architecture & File Map, 5. Storage & Persistence Tiers, 7. Change Log (Milestones), 8. Modular Documentation Build System, A. Dynamic Configuration Extraction, B. High-Fidelity Word (.docx) Compilation, code:block1 (ProjectPulse/), ProjectPulse — High-Density AI Context Pack

### Community 43 - "Community 43"
Cohesion: 0.25
Nodes (8): 4. Core Function Registry, A. View Rendering (Orchestration & Target Containers), B. CRUD Operations, B. CRUD Operations, Delivery Governance & Scheduling, B. CRUD Operations & Scheduling, C. Data Operations & Caching, D. Persistence & Excel Lifecycle, D. Persistence Lifecycle

### Community 44 - "Community 44"
Cohesion: 0.29
Nodes (8): 6. Authoritative Business Rules, A. Task Status Transitions, B. Calculated Metrics, code:typescript ({), code:typescript ({), code:block9 ([Not Started] ──> [In Progress] ──> [Under Review] ──> [Comp), Delivery, Log

### Community 45 - "Community 45"
Cohesion: 0.33
Nodes (6): initApp(), initDesignSpells(), initGanttResizer(), load(), loadRecentProject(), renderRecentProjects()

### Community 46 - "Community 46"
Cohesion: 0.4
Nodes (5): 2. Global State Schema (`P` Object), A. Core Data Arrays, B. Configurations, C. Persistent File System State, D. Volatile UI State

### Community 47 - "Community 47"
Cohesion: 0.4
Nodes (5): autoFitAllCols(), closeDD(), _closeDDH(), executeAutofit(), getGridCols()

### Community 48 - "Community 48"
Cohesion: 0.67
Nodes (3): bulkDeleteTasks(), resetProject(), showConfirm()

### Community 49 - "Community 49"
Cohesion: 0.67
Nodes (3): closeFlyout(), confirmDeleteTask(), deleteTask()

### Community 50 - "Community 50"
Cohesion: 0.67
Nodes (3): toggleAllBulkTasks(), toggleBulkTask(), updateBulkBar()

## Knowledge Gaps
- **684 isolated node(s):** `code:bash (# Using Node.js)`, `code:block2 (ProjectPulse/)`, `Core Capabilities:`, `code:bash (node scripts/update_manual.js)`, `code:bash (python scripts/build_all.py)` (+679 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **10 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `$id()` connect `Readme & Typescript & Entity` to `Community 33`, `Architecture & Audit & State`, `Manual & State & Md`, `Community 34`, `Community 36`, `Insights & Burn & Md`, `Reports & Board & Md`, `Activity & Md & Audit`, `Capacity & Workload & Role`, `Audit Log & Activity & Session`, `Community 28`?**
  _High betweenness centrality (0.003) - this node is a cross-community bridge._
- **Why does `$id()` connect `Schedule & Manual & Check` to `Configuration & Reference & Status`, `Community 35`, `Community 37`, `Scheduler & The & Heuristic`, `Community 40`, `Delivery & Md & Hierarchical`, `Team & Capacity & Role`, `Community 49`, `Community 50`, `Delivery Matrix & Hierarchy & Edit`, `Reports & Board & Export`, `Widgets & Capture & Screenshot`, `Status & Dashboard & Live`, `Community 27`, `Community 29`, `Community 30`?**
  _High betweenness centrality (0.003) - this node is a cross-community bridge._
- **Why does `$id()` connect `Overview & Md & Executive` to `Readme & State & Block`, `Changelog & 2026 & 05`, `Risks & Raid & Md`, `Readme & Md & Project`, `Community 41`, `Defects & Defect & Bug`, `Project & Status & Md`, `User Manual & Architecture & Sync`, `Community 31`?**
  _High betweenness centrality (0.001) - this node is a cross-community bridge._
- **What connects `code:bash (# Using Node.js)`, `code:block2 (ProjectPulse/)`, `Core Capabilities:` to the rest of the system?**
  _684 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Configuration & Reference & Status` be split into smaller, more focused modules?**
  _Cohesion score 0.0 - nodes in this community are weakly interconnected._
- **Should `Readme & State & Block` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `Architecture & Audit & State` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._