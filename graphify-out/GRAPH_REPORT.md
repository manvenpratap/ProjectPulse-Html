# Graph Report - ProjectPulse  (2026-06-14)

## Corpus Check
- 25 files · ~413,370 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 300 nodes · 473 edges · 23 communities (22 shown, 1 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 28 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a2b1cd3c`
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
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]

## God Nodes (most connected - your core abstractions)
1. `build_fsd()` - 25 edges
2. `Active Dropdown Options` - 19 edges
3. `build_umi()` - 18 edges
4. `make_heading()` - 16 edges
5. `add_horizontal_rule()` - 15 edges
6. `add_data_table()` - 15 edges
7. `add_page_break()` - 15 edges
8. `12 Change Log Baseline` - 15 edges
9. `make_body()` - 14 edges
10. `add_screenshot()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `build_pcd()`  [INFERRED]
  scripts/build_all.py → scripts/build_pcd.py
- `build_fsd()` --calls--> `new_document()`  [INFERRED]
  scripts/build_fsd.py → scripts/docx_helpers.py
- `build_fsd()` --calls--> `add_footer()`  [INFERRED]
  scripts/build_fsd.py → scripts/docx_helpers.py
- `build_fsd()` --calls--> `add_document_control()`  [INFERRED]
  scripts/build_fsd.py → scripts/docx_helpers.py
- `build_fsd()` --calls--> `add_section_divider()`  [INFERRED]
  scripts/build_fsd.py → scripts/docx_helpers.py

## Communities (23 total, 1 thin omitted)

### Community 0 - "Configuration & Reference & Status"
Cohesion: 0.25
Nodes (33): add_callout(), add_data_table(), add_horizontal_rule(), add_page_break(), add_screenshot(), build_cover(), build_docx(), build_toc() (+25 more)

### Community 1 - "Readme & State & Block"
Cohesion: 0.06
Nodes (30): 1. Codebase Architecture & File Map, 2. Global State Schema (`P` Object), 3. Entity Schemas, 4. Core Function Registry, 5. Storage & Persistence Tiers, 6. Authoritative Business Rules, 7. Change Log (Milestones), A. Core Data Arrays (+22 more)

### Community 2 - "Architecture & Audit & State"
Cohesion: 0.12
Nodes (23): build_pcd(), ch_appendix(), ch_capabilities(), ch_capability_matrix(), ch_differentiators(), ch_exec_summary(), ch_gallery(), ch_product_overview() (+15 more)

### Community 3 - "Manual & State & Md"
Cohesion: 0.19
Nodes (24): build_fsd(), fsd_appendices(), fsd_audit(), fsd_baselines(), fsd_config(), fsd_defects(), fsd_delivery(), fsd_gantt() (+16 more)

### Community 4 - "Changelog & 2026 & 05"
Cohesion: 0.1
Nodes (20): Active Dropdown Options, Category, Complexity, Configuration Reference, Decision Status, Defect Priority, Defect Severity, Defect Status (+12 more)

### Community 5 - "Schedule & Manual & Check"
Cohesion: 0.17
Nodes (18): main(), build_all.py ============ Master build orchestrator for the ProjectPulse three-d, build_umi(), ch_audit(), ch_config(), ch_defects(), ch_delivery(), ch_gantt() (+10 more)

### Community 6 - "Readme & Typescript & Entity"
Cohesion: 0.11
Nodes (17): 1. Global State Schema & Lifecycle, 1. In-place Mutation of Legacy Globals, 2. Core Subsystem Map, 2. High Mixing of Business Logic and DOM Operations, 3. Identified Code Smells, Redundancies, and Coupling, 3. Redundant / Brittle Script Utilities (`fix_orphan.py` bug), 4. Refactoring Strategy, A. Scheduling Engine (`recalcDatesAndStatus` & `recalcGUIScreen`) (+9 more)

### Community 7 - "Scheduler & The & Heuristic"
Cohesion: 0.12
Nodes (16): CONFIG_MD_FILE, defaultTasksMatch, docsDir, dropdowns, evalStr, fs, HTML_FILE, htmlContent (+8 more)

### Community 8 - "Overview & Md & Executive"
Cohesion: 0.12
Nodes (15): 12 Change Log Baseline, 📅 [2026-05-14] - Baseline Documentation Established, 📅 [2026-05-17] - Dashboard Rendering Optimization (O(1) Caching & Batched Drawing), 📅 [2026-05-17] - Defect Categories Widget `undefined` Chart Label Fix, 📅 [2026-05-17] - Defect Hotspots Entity Resolution Fix, 📅 [2026-05-17] - Defect Intelligence Widget `Unlinked` Module Mapping Resolution, 📅 [2026-05-17] - Dynamic Dashboard Mini-Map Integration, 📅 [2026-05-17] - Premium Theme Expansion (User Request #3) (+7 more)

### Community 9 - "Risks & Raid & Md"
Cohesion: 0.14
Nodes (10): checkMode, { execSync }, fs, LAUNCH_AGENT_DIR, LOG_FILE, path, PLIST_FILE, PROJECT_ROOT (+2 more)

### Community 10 - "Readme & Md & Project"
Cohesion: 0.2
Nodes (9): 1. The Weekly Heatmap Grid, 2. Interactive Tooltips, 3. The Left Navigation Sidebar & "How this view works", 4. The Right-Side Diagnostics Cockpit, 5. Conflict Resolution Heuristics, Heuristic A: Auto-Sequence, Heuristic B: Smart Reassignment, Heuristic C: Cascading Date Shifting (+1 more)

### Community 11 - "Delivery & Md & Hierarchical"
Cohesion: 0.29
Nodes (6): 1. Key Performance Indicators (KPIs), 2. Dynamic Health Gauge, 3. What-If Predictive Sandbox, code:block1 ([   84%   ]), Executive Overview Dashboard, Operation

### Community 12 - "Insights & Burn & Md"
Cohesion: 0.29
Nodes (6): 1. What is a Baseline?, 2. Capturing a Baseline Snapshot, 3. Variance and Slippage Analysis, 4. Restoring and Deleting Snapshots, Schedule Baselines & Snapshot History, What happens when you capture a snapshot?

### Community 13 - "Team & Capacity & Role"
Cohesion: 0.33
Nodes (4): capture_screenshots.py Launches ProjectPulse in a headless Chromium browser, see, Set localStorage state, navigate to view, wait and screenshot., Set localStorage state, navigate to view, wait and screenshot., seed_and_screenshot()

### Community 14 - "Defects & Defect & Bug"
Cohesion: 0.33
Nodes (5): 1. RAID Classifications, 2. Threat Exposure Calculations, 3. Mitigation Plans and Owners, Scoring Reference:, Unified RAID Register

### Community 15 - "Reports & Board & Md"
Cohesion: 0.33
Nodes (5): Architecture Schematic, code:block1 ([LocalStorage/IndexedDB Backup Store]), Daily Automated Synchronization, Directory Navigation & Feature Guides, ProjectPulse User Manual — Master Index

### Community 16 - "Activity & Md & Audit"
Cohesion: 0.33
Nodes (5): 1. Parent-Child Hierarchies, 2. Spreadsheet-Style Inline Editing, 3. Complexity & Estimation Scaling, code:block1 ([Deliverable 1: Core API Setup]), Hierarchical Delivery Matrix

### Community 17 - "Project & Status & Md"
Cohesion: 0.4
Nodes (4): 1. Metric Caching (`buildDashCache`), 2. Earned Value Management (EVM), 3. Burn-up & Burn-down Projections, Live Project Insights & Analytics

### Community 18 - "Community 18"
Cohesion: 0.4
Nodes (4): 1. Capacity Modeling, 2. Dynamic Workload Balancing, 3. Role Assignments, Team Capacity Hub & Role Management

### Community 19 - "Community 19"
Cohesion: 0.4
Nodes (4): 1. Defect Severity Matrix, 2. Bug Lifecycle States, code:block1 ([New] ──► [Assigned] ──► [In Progress] ──► [Fixed] ──► [Veri), Defect Tracker & Bug Lifecycle

### Community 20 - "Community 20"
Cohesion: 0.5
Nodes (3): 1. Executive Board Pack Generator, 2. Spreadsheet Export Settings (ExcelJS), Reports & Stakeholder Board Packs

### Community 21 - "Community 21"
Cohesion: 0.5
Nodes (3): 1. Automated Action Logging, 2. Session Rollback Capability, Audit Log & Activity Streams

## Knowledge Gaps
- **138 isolated node(s):** `build_pcd.py ============ Builds the ProjectPulse Product Capabilities Document`, `build_fsd.py ============ Builds the ProjectPulse Functional Specification Docum`, `fs`, `path`, `PROJECT_ROOT` (+133 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `build_fsd()` connect `Manual & State & Md` to `Architecture & Audit & State`, `Schedule & Manual & Check`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `build_umi()` connect `Schedule & Manual & Check` to `Architecture & Audit & State`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Why does `build_pcd()` connect `Architecture & Audit & State` to `Schedule & Manual & Check`?**
  _High betweenness centrality (0.013) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `build_fsd()` (e.g. with `new_document()` and `add_footer()`) actually correct?**
  _`build_fsd()` has 5 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `build_umi()` (e.g. with `main()` and `new_document()`) actually correct?**
  _`build_umi()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `build_pcd.py ============ Builds the ProjectPulse Product Capabilities Document`, `build_fsd.py ============ Builds the ProjectPulse Functional Specification Docum`, `fs` to the rest of the system?**
  _138 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Readme & State & Block` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._