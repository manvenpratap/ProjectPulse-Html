# 04 Architecture Risks & Backlog

## SECTION: Architecture Risks

### 1. Monolith Scalability
- **Risk**: The `projectpulse.html` file is ~28,800 lines. Manual editing is difficult, and risk of accidental regressions is high.
- **Mitigation**: Rely on this `project-context` pack for navigation. Future refactoring should consider splitting the file into logical modules (CSS, State, Views, Utils) if moving to a build-step environment.

### 2. LocalStorage Capacity Limit
- **Risk**: `localStorage` (5MB) can be exceeded by large project histories, high task volume, or thousands of log entries.
- **Mitigation**: Implemented an "Auto-Prune" for logs (preserving last 500), moved large blobs (like file handles and backups) to IndexedDB, and established direct File System Access API sync.

### 3. State Synchronization (Excel Roundtrips)
- **Risk**: When using Excel Sync, modifying the `.xlsx` file externally in ways that break the relational model (e.g., deleting a Task ID referenced by a Subtask) could corrupt state.
- **Mitigation**: `reconstructProjectFromBuffer()` includes strict validation logic. It skips orphaned children and notifies the user of "Broken Relationships". `PROJECT_SCHEMA` must always be accurately mapped to Excel logic.

### 4. UI Complexity & Render Performance
- **Risk**: Re-rendering the entire Task Matrix with thousands of DOM nodes on every minor change causes UI lag.
- **Mitigation**: Targeted sub-rendering where possible. Dashboard performance specifically is optimized via `buildDashCache()` (O(n) pass) and `requestAnimationFrame` drawing queues (`dashDrawQueue`) to avoid expensive layout thrashing.

### 5. Schema Drift
- **Risk**: Adding new features/properties to the `P` state but forgetting to account for them in the Excel Export/Import logic leads to silent data loss during file sync.
- **Mitigation**: Strict adherence to updating `01-state-and-schemas.md` and `reconstructProjectFromBuffer()` whenever state is expanded.

---

## SECTION: Enhancement Backlog

### 🔴 Critical / Bug Hardening
- [ ] **Log Pruning UI**: Implement a formal "Log Management" UI to allow users to clear history or set retention policies manually.
- [ ] **Excel Import Validation UI**: Enhance error reporting during Excel reconstruction to show specific row/cell errors instead of silent skipping.
- [ ] **Mobile Touch Optimization**: Improve drag-and-drop handles for the Dashboard on tablet/mobile devices.

### 🟡 UI / UX Polish
- [ ] **Dark Mode Transitions**: Add global CSS transitions for color variables to make theme switching smoother.
- [ ] **Skeleton Loaders**: Implement skeleton states for Dashboard widgets during initial project load (especially large files).
- [ ] **Command Palette Actions**: Add more context-aware "Quick Actions" to `Cmd+K` like "Log Defect on [Selected Task]".

### 🟢 Feature Enhancements
- [ ] **Multi-Project Support**: Allow switching between multiple project contexts saved in IndexedDB (currently 1 active project at a time).
- [ ] **Task Comments/Chat**: Add a threaded comment system within the Task Modal for collaboration.
- [ ] **Resource Forecasting**: A predictive view showing project end-date drift based on current team velocity.
- [ ] **Custom Field Formulas**: Support for calculated custom fields (e.g., `FieldC = FieldA * FieldB`).
- [ ] **Offline PWA**: Add a `manifest.json` and Service Worker to allow full offline installation to device homescreens.

### 🔵 Technical Debt
- [ ] **Function Decomposition**: Refactor `renderTable` (current monolithic function) into smaller, component-level renders.
- [ ] **CSS Variable Audit**: Consolidate redundant CSS variables across the 20 theme definitions.
- [ ] **Unit Testing Suite**: Create a `test-harness.html` to run core logic validations (Health Score, BusDays, Effort Conversion) in isolation.
