# Architecture Audit & Refactoring Strategy — ProjectPulse

This document details the architectural findings, structural dependencies, code smells, and the refactoring strategy for **ProjectPulse**, a monolithic single-page project management suite.

---

## 1. Global State Schema & Lifecycle

### State Storage & Memory Registry
* **Memory Reference**: The primary runtime state is registered under `const P` and exposed to the environment via `window.P`.
* **Dynamic Registries**: `P.dropdowns` holds lists of standard fields (status, priority, categories, complex etc.).
* **State Lifecycle**: 
  - **Tier 1 (LocalStorage)**: `pp-data` is used for auto-saving standard state.
  - **Tier 2 (IndexedDB)**: `ProjectPulseDB` is used for caching file system access handles, JSON backups (last 10 snapshots), and binary Excel backups (last 5).
  - **Tier 3 (Local Disk)**: Excel binary file writes via File System Access API.

### State Mutation & Splicing Side Effects
* **Legacy Globals Coupling**: Global arrays like `STATUSES`, `PRIORITIES`, `CATEGORIES`, `MODULES`, `MODULE_TYPES`, `VERSIONS`, `ROLES`, and `MEMBER_STATUSES` are declared globally.
* **Syncing System**: Every time dropdown structures change, `syncDropdowns()` is executed. It uses `.splice(0, arr.length, ...newValues)` to mutate these legacy arrays in-place to ensure backward compatibility with old script blocks that reference the global arrays directly instead of checking `P.dropdowns`.
* **Column Options Updates**: `syncDropdowns()` also updates the options arrays (`opts`) inside task grid columns (`P.cols`) and defect columns (`P.defCols`) dynamically.

---

## 2. Core Subsystem Map

### A. Scheduling Engine (`recalcDatesAndStatus` & `recalcGUIScreen`)
Governs task, subtask, and step date propagation, effort scaling, and status rollups:
1. **Effort Scaling**:
   - Task estimates scale according to task complexity factors configured in `P.complexityFactors` (`Easy: 0.5`, `Medium: 1.0`, `Complex: 1.5`).
   - If a task has checklist subtasks, effort and progress are rolled up from them. Screen subtasks are scaled on their own steps; non-screen subtasks are scaled by the parent task complexity multiplier.
2. **Assignee-based GUI Scheduling**:
   - For GUI modules, screen subtasks under the same assignee are calculated sequentially.
   - Screen subtasks under different assignees are processed in parallel (independent timeline tracks starting from the task start date).
   - Screens are ordered sequentially by priority (Critical first) to schedule resources.
3. **Sequential Non-GUI Scheduling**:
   - For server modules or interface categories, subtask dates propagate sequentially from step to step, regardless of assignee.

### B. Dashboard / Analytics Cache (`buildDashCache`)
* **Purpose**: Replaces expensive filter operations during view rendering with `O(1)` lookups.
* **Performance Path**: Computes team utilization, defect inflow trends, milestones, task counts, and audit logs history in a single $O(n)$ iteration, storing aggregates in a cached dictionary before rendering the UI widgets.
* **Health Scoring**: Dynamically calculates composite metrics:
  - **Health Index**: Penalizes project status for Overdue, Blocked, and On-Hold tasks.
  - **Delivery Confidence**: Compares pacing against velocity calculations extracted from status logs.

### C. Persistence & Backup Tier
* **Debounced Auto-Save**: Triggers auto-save of state to localStorage and IndexedDB after a 10-second idle timer, or immediately on critical edits (CRUD, deletes, state transitions).
* **Backup Rotations**: Stores rotating JSON snapshots and full binary buffers in IndexedDB, and propagates files to local directory structures when a local backup path is connected.

### D. Excel Import / Export Engine
* **Export (`generateProjectWorkbook`)**: Generates an Excel workbook file containing structured sheets mapping task parent/child relationships, dependencies, RAID registries, custom columns, and project metadata.
* **Import (`reconstructProjectFromBuffer`)**: Rebuilds the nested task hierarchy from tabular Excel buffers, validates schemas against `window.PROJECT_SCHEMA`, resolves missing columns, and repairs data integrity.

---

## 3. Identified Code Smells, Redundancies, and Coupling

### 1. In-place Mutation of Legacy Globals
* **Smell**: Splicing array contents in `syncDropdowns` creates implicit side effects. Functions that query `STATUSES` or `PRIORITIES` read mutated lists without dynamic getters, which can lead to layout desyncs or reference errors if not called in the exact lifecycle order.
* **Coupling**: High coupling between the settings page, task grid dropdown columns, and independent modal components.

### 2. High Mixing of Business Logic and DOM Operations
* **Smell**: Functions that execute calculations or data mutations often perform direct DOM manipulation (e.g., changing innerHTML of task rows, triggering Lucide icon updates, or calling view rendering functions).
* **Impact**: Recalculating task dates triggers direct saves and UI repaints, making it difficult to write tests or run calculations in memory (such as during What-If simulations) without visual side effects.

### 3. Redundant / Brittle Script Utilities (`fix_orphan.py` bug)
* **Finding**: The utility script `fix_orphan.py` was created to clean up an "orphan block". However, it uses fragile line-offset indexes and broad substring matches. 
* **Bug**: Running `fix_orphan.py` cuts out over 1000 lines of functional JavaScript code (the Activity Log view, the What-If predictive sandbox, etc.) and leaves unfinished brace blocks, causing syntax errors in script compiling.
* **Remedy**: We should deprecate or fix the pattern matching in `fix_orphan.py` to prevent accidental execution by developers or automated systems.

---

## 4. Refactoring Strategy

Since the codebase must remain a **single-file monolith** (`projectpulse.html`), we cannot split script blocks into external files. Instead, we will refactor by encapsulating code into structured, namespace-based objects on `window` or local closures to separate concerns:

```mermaid
graph TD
    subgraph Single-File Monolith (projectpulse.html)
        A[HTML Document Structure]
        B[CSS Custom Themes & Tokens]
        subgraph Encapsulated JavaScript Namespace
            C[PulseConfig / PulseConstants]
            D[PulseState]
            E[PulseScheduler]
            F[PulsePersistence]
            G[PulseDashboard]
            H[PulseExcel]
            I[PulseUI & Renderers]
        end
    end
    
    PulseState --> PulseScheduler
    PulseState --> PulsePersistence
    PulseScheduler --> PulseDashboard
    PulseDashboard --> PulseUI
    PulseExcel --> PulseState
```

### Namespace Definitions

1. **`PulseConstants`**: Contains core configurations, valid transitions mapping, theme listings, category mappings, and column metadata blueprints.
2. **`PulseState`**: Governs core state variables (`P` registry), handles validation rules, coordinates custom fields schema, and wraps dropdown sync processes.
3. **`PulseScheduler`**: Contains pure scheduling logic, including complexity factor scaling, date propagation rules, assignee sequence processing, and What-If sandbox calculations.
4. **`PulsePersistence`**: Handles LocalStorage serialization, IndexedDB queries/backups, and File System API file handle bindings.
5. **`PulseDashboard`**: Contains logic for aggregation cache compilation, health metrics calculation, and delivery confidence pacing.
6. **`PulseExcel`**: Manages ExcelJS workbook configuration, relational sheets mapping, and import verification logic.
7. **`PulseUI`**: Manages view state routes, rendering dispatchers, modal bindings, event listeners, and layout transitions.

### Migration Path (Phase 2: Restructure)
We will carry out the restructuring step-by-step in the main script block of `projectpulse.html` to keep the app compiling and functional at all stages:
- **Step 1**: Consolidate core constant definitions and transitions under `PulseConstants`.
- **Step 2**: Wrap state initialization and dropdown sync helpers into `PulseState` while keeping legacy references for backwards compatibility.
- **Step 3**: Extract scheduling routines (`recalcDatesAndStatus`, `recalcGUIScreen`, date helpers) into `PulseScheduler`.
- **Step 4**: Extract caching, metrics computation (`buildDashCache`, health/confidence scores) into `PulseDashboard`.
- **Step 5**: Verify code integrity at each step using the `check_syntax.js` verification suite.
