# Graph Report - ProjectPulse  (2026-06-21)

## Corpus Check
- 3 files · ~220,042 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 72 nodes · 69 edges · 8 communities
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `198a5d9b`
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

## God Nodes (most connected - your core abstractions)
1. `12 Change Log Baseline` - 19 edges
2. `ProjectPulse — High-Density AI Context Pack` - 9 edges
3. `3. Entity Schemas` - 6 edges
4. `Architecture Audit & Refactoring Strategy — ProjectPulse` - 5 edges
5. `2. Core Subsystem Map` - 5 edges
6. `2. Global State Schema (`P` Object)` - 5 edges
7. `4. Core Function Registry` - 5 edges
8. `3. Identified Code Smells, Redundancies, and Coupling` - 4 edges
9. `4. Refactoring Strategy` - 4 edges
10. `1. Global State Schema & Lifecycle` - 3 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities (8 total, 0 thin omitted)

### Community 0 - "Configuration & Reference & Status"
Cohesion: 0.1
Nodes (19): 12 Change Log Baseline, 📅 [2026-05-14] - Baseline Documentation Established, 📅 [2026-05-17] - Dashboard Rendering Optimization (O(1) Caching & Batched Drawing), 📅 [2026-05-17] - Defect Categories Widget `undefined` Chart Label Fix, 📅 [2026-05-17] - Defect Hotspots Entity Resolution Fix, 📅 [2026-05-17] - Defect Intelligence Widget `Unlinked` Module Mapping Resolution, 📅 [2026-05-17] - Dynamic Dashboard Mini-Map Integration, 📅 [2026-05-17] - Premium Theme Expansion (User Request #3) (+11 more)

### Community 1 - "Readme & State & Block"
Cohesion: 0.14
Nodes (13): 1. Codebase Architecture & File Map, 2. Global State Schema (`P` Object), 5. Storage & Persistence Tiers, 7. Change Log (Milestones), 8. Modular Documentation Build System, A. Core Data Arrays, A. Dynamic Configuration Extraction, B. Configurations (+5 more)

### Community 2 - "Architecture & Audit & State"
Cohesion: 0.18
Nodes (11): 3. Entity Schemas, code:typescript ({), code:typescript ({), code:typescript ({), code:typescript ({), code:typescript ({), Defect, Log (+3 more)

### Community 3 - "Manual & State & Md"
Cohesion: 0.2
Nodes (9): 1. Global State Schema & Lifecycle, 2. Core Subsystem Map, A. Scheduling Engine (`recalcDatesAndStatus` & `recalcGUIScreen`), Architecture Audit & Refactoring Strategy — ProjectPulse, B. Dashboard / Analytics Cache (`buildDashCache`), C. Persistence & Backup Tier, D. Excel Import / Export Engine, State Mutation & Splicing Side Effects (+1 more)

### Community 4 - "Changelog & 2026 & 05"
Cohesion: 0.4
Nodes (5): 4. Core Function Registry, A. View Rendering (Orchestration & Target Containers), B. CRUD Operations, C. Data Operations & Caching, D. Persistence Lifecycle

### Community 5 - "Schedule & Manual & Check"
Cohesion: 0.5
Nodes (4): 1. In-place Mutation of Legacy Globals, 2. High Mixing of Business Logic and DOM Operations, 3. Identified Code Smells, Redundancies, and Coupling, 3. Redundant / Brittle Script Utilities (`fix_orphan.py` bug)

### Community 6 - "Readme & Typescript & Entity"
Cohesion: 0.5
Nodes (4): 4. Refactoring Strategy, code:mermaid (graph TD), Migration Path (Phase 2: Restructure), Namespace Definitions

### Community 7 - "Scheduler & The & Heuristic"
Cohesion: 0.5
Nodes (4): 6. Authoritative Business Rules, A. Task Status Transitions, B. Calculated Metrics, code:block7 ([Not Started] ──> [In Progress] ──> [Under Review] ──> [Comp)

## Knowledge Gaps
- **50 isolated node(s):** `State Storage & Memory Registry`, `State Mutation & Splicing Side Effects`, `A. Scheduling Engine (`recalcDatesAndStatus` & `recalcGUIScreen`)`, `B. Dashboard / Analytics Cache (`buildDashCache`)`, `C. Persistence & Backup Tier` (+45 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `ProjectPulse — High-Density AI Context Pack` connect `Readme & State & Block` to `Architecture & Audit & State`, `Changelog & 2026 & 05`, `Scheduler & The & Heuristic`?**
  _High betweenness centrality (0.178) - this node is a cross-community bridge._
- **Why does `3. Entity Schemas` connect `Architecture & Audit & State` to `Readme & State & Block`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **What connects `State Storage & Memory Registry`, `State Mutation & Splicing Side Effects`, `A. Scheduling Engine (`recalcDatesAndStatus` & `recalcGUIScreen`)` to the rest of the system?**
  _50 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Configuration & Reference & Status` be split into smaller, more focused modules?**
  _Cohesion score 0.1 - nodes in this community are weakly interconnected._
- **Should `Readme & State & Block` be split into smaller, more focused modules?**
  _Cohesion score 0.14 - nodes in this community are weakly interconnected._