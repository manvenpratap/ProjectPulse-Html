# Graph Report - ProjectPulse  (2026-07-22)

## Corpus Check
- 5 files · ~498,747 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 683 nodes · 1488 edges · 31 communities (26 shown, 5 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `071e883b`
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

## God Nodes (most connected - your core abstractions)
1. `$id()` - 151 edges
2. `save()` - 63 edges
3. `notify()` - 58 edges
4. `esc()` - 29 edges
5. `render()` - 28 edges
6. `renderSidebar()` - 26 edges
7. `setAdminActiveTab()` - 24 edges
8. `12 Change Log Baseline` - 21 edges
9. `renderTasksView()` - 18 edges
10. `renderTable()` - 18 edges

## Surprising Connections (you probably didn't know these)
- `renderBackupList()` --calls--> `warn()`  [EXTRACTED]
  temp_script_check.js → temp_script_check.js  _Bridges community 2 → community 21_
- `renderViewToggle()` --calls--> `$id()`  [EXTRACTED]
  temp_script_check.js → temp_script_check.js  _Bridges community 7 → community 2_
- `showViewHelp()` --calls--> `$id()`  [EXTRACTED]
  temp_script_check.js → temp_script_check.js  _Bridges community 7 → community 6_
- `syncFsDirectory()` --calls--> `$id()`  [EXTRACTED]
  temp_script_check.js → temp_script_check.js  _Bridges community 7 → community 1_
- `updateBulkBar()` --calls--> `$id()`  [EXTRACTED]
  temp_script_check.js → temp_script_check.js  _Bridges community 7 → community 24_

## Communities (31 total, 5 thin omitted)

### Community 0 - "Configuration & Reference & Status"
Cohesion: 0.01
Nodes (63): activeModal, allDone, anyStarted, blocked, bulkSelectedTasks, c, cache, CATEGORIES (+55 more)

### Community 1 - "Readme & State & Block"
Cohesion: 0.05
Nodes (73): addLog(), applyDashLayout(), applyReportLayout(), applyTemplate(), autoPopulateReport(), buildBoardPackContent(), captureAreaAsCanvas(), captureFullFeatureGantt() (+65 more)

### Community 2 - "Architecture & Audit & State"
Cohesion: 0.06
Nodes (52): addDDValueV(), addRelease(), clearProjectState(), closeRaidFlyout(), computeAlerts(), createNewGlobalSet(), deleteGlobalSet(), deleteRaidItem() (+44 more)

### Community 3 - "Manual & State & Md"
Cohesion: 0.04
Nodes (45): 1. Codebase Architecture & File Map, 2. Global State Schema (`P` Object), 3. Entity Schemas, 4. Core Function Registry, 5. Storage & Persistence Tiers, 6. Authoritative Business Rules, 7. Change Log (Milestones), 8. Modular Documentation Build System (+37 more)

### Community 4 - "Changelog & 2026 & 05"
Cohesion: 0.08
Nodes (39): autoResolveAllSchedulerConflicts(), autoSequenceAssignee(), changeSchedulerWeek(), clearMatrixFilter(), filterDashboardMetric(), filterRaid(), findScheduleConflicts(), generateIntelligentSuggestions() (+31 more)

### Community 5 - "Schedule & Manual & Check"
Cohesion: 0.07
Nodes (39): addEmptyState(), addGrid(), addST(), closeCtx(), downloadGanttAsHtml(), esc(), formatDateStringFriendly(), _matrixCellHover() (+31 more)

### Community 6 - "Readme & Typescript & Entity"
Cohesion: 0.1
Nodes (27): applyPvFilt(), cancelEditCw(), cap(), editCustomWidgetCtx(), editCw(), getFieldType(), _matrixCellClick(), moveDashSec() (+19 more)

### Community 7 - "Scheduler & The & Heuristic"
Cohesion: 0.09
Nodes (27): addDep(), addLeaveRow(), clearPvFilt(), closeCmdPalette(), closeEwsModal(), drawProgressRing(), $id(), openBulkDD() (+19 more)

### Community 8 - "Overview & Md & Executive"
Cohesion: 0.13
Nodes (27): applyBulkEdit(), autoFitCol(), doGridSort(), doSort(), finalizeColOrder(), getGridFiltered(), getGridPK(), getGridSorted() (+19 more)

### Community 9 - "Risks & Raid & Md"
Cohesion: 0.09
Nodes (20): 12 Change Log Baseline, 📅 [2026-05-14] - Baseline Documentation Established, 📅 [2026-05-17] - Dashboard Rendering Optimization (O(1) Caching & Batched Drawing), 📅 [2026-05-17] - Defect Categories Widget `undefined` Chart Label Fix, 📅 [2026-05-17] - Defect Hotspots Entity Resolution Fix, 📅 [2026-05-17] - Defect Intelligence Widget `Unlinked` Module Mapping Resolution, 📅 [2026-05-17] - Dynamic Dashboard Mini-Map Integration, 📅 [2026-05-17] - Premium Theme Expansion (User Request #3) (+12 more)

### Community 10 - "Readme & Md & Project"
Cohesion: 0.11
Nodes (17): 1. Global State Schema & Lifecycle, 1. In-place Mutation of Legacy Globals, 2. Core Subsystem Map, 2. High Mixing of Business Logic and DOM Operations, 3. Identified Code Smells, Redundancies, and Coupling, 3. Redundant / Brittle Script Utilities (`fix_orphan.py` bug), 4. Refactoring Strategy, A. Scheduling Engine (`recalcDatesAndStatus` & `recalcGUIScreen`) (+9 more)

### Community 11 - "Delivery & Md & Hierarchical"
Cohesion: 0.12
Nodes (18): addNewGUIScreen(), applyWorkflowTemplate(), commitWhatIfScenario(), fmtDate(), markAllGUIStepsDone(), openEwsModal(), openScreenFlyout(), renderGUIScreens() (+10 more)

### Community 12 - "Insights & Burn & Md"
Cohesion: 0.15
Nodes (13): addCustomFieldV(), cancelEditFeature(), closeAllFlyouts(), closeFeatFlyout(), closeTplFlyout(), finalizeTplUpdateV(), importScaffoldBulk(), propagateTemplateUpdate() (+5 more)

### Community 13 - "Team & Capacity & Role"
Cohesion: 0.17
Nodes (13): addScaffoldRow(), duplicateScaffoldRow(), generateFromScaffold(), loadScaffoldTemplate(), removeScaffoldRow(), renderAdminView(), renderScaffolder(), renderScaffoldStep1() (+5 more)

### Community 14 - "Defects & Defect & Bug"
Cohesion: 0.18
Nodes (11): deleteFeature(), initFeatGanttResizer(), initFeatScreenSearch(), renderFeatureGantt(), renderFeatureHub(), renderFeatureSwimlane(), renderTimeline(), setFeatGanttZoom() (+3 more)

### Community 15 - "Reports & Board & Md"
Cohesion: 0.22
Nodes (9): createBaselineSnapshot(), deleteBaselineSnapshot(), editReport(), openNewReport(), openRaidModal(), renderSettingsBaselines(), restoreBaselineSnapshot(), todayStr() (+1 more)

### Community 16 - "Activity & Md & Audit"
Cohesion: 0.33
Nodes (7): filterDefectLinkOptions(), getAllScreens(), openDefectModal(), raiseDefectForEntity(), renderDefectLinkOptionsList(), toggleDefectLinkDropdown(), updateDefectLinkOptions()

### Community 17 - "Project & Status & Md"
Cohesion: 0.33
Nodes (6): initApp(), initDesignSpells(), initGanttResizer(), load(), loadRecentProject(), renderRecentProjects()

### Community 18 - "User Manual & Architecture & Sync"
Cohesion: 0.4
Nodes (6): closeDefectFlyout(), closeDefectLinkDropdown(), handleDefectLinkClickOutside(), saveDefect(), selectDefectLinkOption(), setDefectLinkValue()

### Community 19 - "Delivery Matrix & Hierarchy & Edit"
Cohesion: 0.33
Nodes (6): featAddCustomScreen(), featAddScreen(), featRemoveScreen(), openFeatFlyout(), renderFeatScreenChips(), startEditFeature()

### Community 20 - "Capacity & Workload & Role"
Cohesion: 0.4
Nodes (5): autoFitAllCols(), closeDD(), _closeDDH(), executeAutofit(), getGridCols()

### Community 21 - "Defect Tracker & Bug Lifecycle"
Cohesion: 0.4
Nodes (5): listBackups(), renderAdminContent(), renderBackupList(), renderBackupListInline(), renderSettingsBackups()

### Community 22 - "Reports & Board & Export"
Cohesion: 0.67
Nodes (4): cancelTplConfirmV(), openTplFlyout(), startEditTplV(), updateTplImpactPreview()

### Community 23 - "Audit Log & Activity & Session"
Cohesion: 0.67
Nodes (3): bulkDeleteTasks(), resetProject(), showConfirm()

### Community 24 - "Widgets & Capture & Screenshot"
Cohesion: 0.67
Nodes (3): toggleAllBulkTasks(), toggleBulkTask(), updateBulkBar()

### Community 25 - "Status & Dashboard & Live"
Cohesion: 0.67
Nodes (3): closeFlyout(), confirmDeleteTask(), deleteTask()

## Knowledge Gaps
- **121 isolated node(s):** `icons`, `els`, `name`, `svg`, `PulseUtils` (+116 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `$id()` connect `Scheduler & The & Heuristic` to `Configuration & Reference & Status`, `Readme & State & Block`, `Architecture & Audit & State`, `Changelog & 2026 & 05`, `Schedule & Manual & Check`, `Readme & Typescript & Entity`, `Overview & Md & Executive`, `Delivery & Md & Hierarchical`, `Insights & Burn & Md`, `Team & Capacity & Role`, `Defects & Defect & Bug`, `Reports & Board & Md`, `Activity & Md & Audit`, `User Manual & Architecture & Sync`, `Delivery Matrix & Hierarchy & Edit`, `Defect Tracker & Bug Lifecycle`, `Reports & Board & Export`, `Widgets & Capture & Screenshot`, `Status & Dashboard & Live`, `Community 28`?**
  _High betweenness centrality (0.023) - this node is a cross-community bridge._
- **Why does `save()` connect `Architecture & Audit & State` to `Configuration & Reference & Status`, `Readme & State & Block`, `Changelog & 2026 & 05`, `Overview & Md & Executive`, `Delivery & Md & Hierarchical`, `Insights & Burn & Md`, `Team & Capacity & Role`, `Defects & Defect & Bug`, `Capacity & Workload & Role`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **What connects `icons`, `els`, `name` to the rest of the system?**
  _121 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Configuration & Reference & Status` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `Readme & State & Block` be split into smaller, more focused modules?**
  _Cohesion score 0.05 - nodes in this community are weakly interconnected._
- **Should `Architecture & Audit & State` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Manual & State & Md` be split into smaller, more focused modules?**
  _Cohesion score 0.04 - nodes in this community are weakly interconnected._