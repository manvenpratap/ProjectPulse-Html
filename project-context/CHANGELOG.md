# 12 Change Log Baseline

## 📅 [2026-05-14] - Baseline Documentation Established
- Created the `/project-context/` documentation pack.
- Documented full `P` state schema and `PROJECT_SCHEMA`.
- Mapped all primary `render` functions and data flows.
- Established rules for persistence, Excel sync, and business logic.
- **Current State**: Application is a monolithic HTML/JS/CSS file with advanced project management features, local-first persistence, and high-fidelity reporting.

## 📅 [2026-05-17] - Project Architect (Scaffolder) Workflow Modernization
- Completely redesigned the legacy Project Architect (`scaffolder`) view into a premium 3-step interactive workflow (Blueprint Modules, GUI Screens, Strategic Alignment).
- Replaced legacy static stepper with a universal interactive stepper component (`getScaffoldStepper`) featuring real-time sidebar mini-map synchronization (`renderSidebar()`).
- Upgraded Step 1 (Blueprint Modules) to feature 4 dynamic glassmorphic KPI cards tracking total modules, GUI screens, missing assignees, and unlinked modules.
- Modernized Step 2 (GUI Screens) with a bento-style card grid layout, monospace textareas, and integrated helper text for rapid UI sitemap mapping.
- Refined Step 3 (Strategic Alignment) with an interactive alignment matrix (`renderScaffoldFeatureMatrix`) allowing users to seamlessly toggle feature-to-module links (`toggleScaffoldFeatLink`), add/remove strategic features, and generate the full project.
- Enhanced `generateFromScaffold()` to auto-increment `P.nextFeatId`, generate `P.features`, create parent tasks, link GUI screens/workflow steps, and automatically transition the user to the `tasks` view upon completion.
- Ensured robust Lucide icon integration across all dynamic architect views, modals, and bulk import flyouts (`openBulkModuleFlyout`).

## 📅 [2026-05-17] - Dashboard Rendering Optimization (O(1) Caching & Batched Drawing)
- Refactored `renderDash()` into a non-blocking rendering pipeline using `DocumentFragment`.
- Implemented `buildDashCache()` to pre-compute task aggregations, status maps, and log indices in a single `O(n)` pass.
- Converted widget data queries to `O(1)` lookups against `dashCache`, eliminating thousands of inline `.filter()` calls.
- Replaced staggered widget `setTimeout` timers with a consolidated `requestAnimationFrame` drawing queue (`dashDrawQueue`).
- Scoped Lucide icon rendering to the dashboard container (`dashInnerContainer`) and prevented redundant global `lucide.createIcons()` scans during dashboard view updates.

## 📅 [2026-05-17] - Defect Hotspots Entity Resolution Fix
- Enhanced `buildDashCache()` to pre-compute `subtaskById` and `screenByName` lookup maps in a single `O(n)` pass.
- Resolved "Unknown Deliverable" display issues in Defect Hotspots, Defect Intelligence, Report Hotspots, Team Quality Champions, and PDF Export by enabling accurate `O(1)` entity resolution and parent task association.
- Enabled direct, contextual flyout navigation (`openScreenFlyout` for GUI screens, `openFlyout` for parent tasks) directly from defect hotspot listings.

## 📅 [2026-05-17] - Dynamic Dashboard Mini-Map Integration
- Refactored `renderSidebar()` to dynamically query active widget wrappers (`.dash-widget-wrapper`) instead of static `.sec-title` elements when in Dashboard view.
- Added `data-title` attributes to all widget wrappers in `renderDash()` to ensure accurate, human-readable titles (e.g. "Summary Cards", "Strategic Module Status") are displayed in the mini-map.
- Synchronized sidebar redraws (`renderSidebar()`) directly within `renderDash()` to ensure the mini-map instantly auto-adjusts to live configuration changes, drag-and-drop reordering (`ondrop`), and Apple Jiggle Mode.
- Implemented smooth scrolling and temporary visual blinking highlights (`.jump-highlight`) on target widgets upon mini-map navigation.
- Added drag-to-reorder functionality directly to the sidebar mini-map items (`.jump-nav-item`), enabling users to effortlessly reorder dashboard widgets (`P.dashLayout`) without having to scroll past large widgets in the main view.
- Fixed progress ring visual misalignment where inner centered text (e.g. "Avg Progress") extended outside the circle by updating `drawProgressRing()` to dynamically match canvas dimensions to parent container width.

## 📅 [2026-05-17] - Premium Theme Expansion (User Request #3)
- Audited the application theme architecture across `THEMES` JS registry, base `[data-theme]` CSS rules, and `html[data-color-mode]` overrides for light/dark mode toggling.
- Added 5 new premium curated theme presets inspired by user reference designs: `terracotta` (Executive Financial), `fintech` (Editorial Banking), `bento` (Vibrant Bento Grid), `codename` (Crimson SaaS), and `workflow` (Glassmorphism Violet).
- Configured complete light and dark mode CSS variable sets for all 5 new themes, ensuring perfect contrast, shadow rendering, and icon filtering regardless of system preference or manual toggle.
- Integrated new theme presets with curated typography pairings (`Inter`, `Fraunces`, `Satoshi`, `Outfit`) and detailed design descriptions in the `THEMES` registry for real-time preview in the Theme Flyout.

## 📅 [2026-05-17] - Widget Information Density Refinement (User Request #2)
- Redesigned the Defect Hotspots widget to eliminate repetitive `[Inspect Deliverable]` buttons and standalone legends, replacing them with a sleek, high-density interactive list container.
- Integrated an ultra-clean, slim 8px risk proportion bar where the table rows directly below serve as the live legend, featuring matching color indicator dots and Lucide icons.
- Drastically improved vertical and horizontal space utilization while maintaining premium SaaS dashboard aesthetics and full functional interactivity (`openFlyout`, `openScreenFlyout`).

## 📅 [2026-05-17] - Defect Categories Widget `undefined` Chart Label Fix
- Identified that the Defect Intelligence widget (`sec.id === 'defect_intel'`) was incorrectly aggregating defect counts using `d.category`, whereas the actual defect schema throughout the application defines this property as `d.type`.
- Replaced `d.category` with `d.type || 'Unclassified'`, instantly resolving the `undefined` x-axis bar chart label and restoring accurate root cause classifications (e.g., Functional Bug, UI/UX Issue, Performance).

## 📅 [2026-05-17] - Defect Intelligence Widget `Unlinked` Module Mapping Resolution
- Identified that sample defects (`DEF-006`, `DEF-008`, `DEF-011`) in the preset hierarchical sample project (`Investment Platform 2.0`) referenced valid GUI screen names (`Portfolio Overview`, `Settings Panel`, `Trade Confirmation`) that were omitted from `guiScreens` on the parent sample tasks, causing `dashCache.screenByName` lookups to return `undefined` and defaulting the module to `Unlinked`.
- Added `Portfolio Overview` and `Trade Confirmation` to `GUI: Trading Dashboard`, and `Settings Panel` to `GUI: User Profile Management` within both the preset `samples.hierarchical.tasks` definition and a dedicated migration block in `load()` for existing localStorage sessions. This completely eliminated the `Unlinked` bar in the module heatmap and restored accurate module-level defect distribution (e.g., Trading UI, Compliance).

## 📅 [2026-05-20] - Configurable Effort Tracking System & Generic Effort Migration
- Renamed legacy task and baseline properties (`baselineHours`, `estHours`, `actHours`, `baseEstHours`) to standard effort properties (`baselineEffort`, `estEffort`, `actEffort`, `baseEstEffort`) across all active project state and persistence layers.
- Added dynamic backward compatibility mapping logic in `load()` and `reconstructProjectFromBuffer()` to automatically migrate legacy objects on load.
- Added settings fields in `P.settings`: `effortUnit` (options: `hrs`, `days`, `months`), `hoursPerDay` (default: 8), and `daysPerWeek` (default: 5) to the General Settings panel in both the modal and inline Admin panel.
- Implemented `convertEffortToDays(effort, unit)` and `convertDaysToEffort(days, unit)` to handle dynamic effort conversion and scaled values proportionally when changing effort tracking units.
- Created `syncEffortColumnLabels()` to dynamically rename table column headers (e.g., `Est. Hrs`, `Act. Days`) in `P.cols` and the task grid based on the active tracking unit.
- Updated Excel export/import sheets (`Tasks`, `Subtasks`, `Baseline_History`) to write dynamic effort headers (e.g., `Estimated Days`) and preserve effort settings.
- Adapted Gantt and calendar scheduling logic to use the configured work week (`daysPerWeek`).

## 📅 [2026-05-21] - Dashboard Layout Restoration
- Restored the **Advanced Analytics & Forecasting** widget (`analytics`) to the default dashboard layout (`defDashLay`) while retaining the existing basic widgets as requested.

## 📅 [2026-05-21] - Context Optimization & Help Sync
- Consolidated 17 project context files into 6 files for better token efficiency.
- Re-aligned all in-app `VIEW_HELP` guides and `mkCC` widget tooltips with current code behaviors (18 dashboard widgets, dynamic effort settings, drag-to-reorder, manual saves).

## 📅 [2026-05-27] - Sparklines, High-Fidelity Exports, Theme Alignment & Local Folder Persistence
- **Executive Overview Sparklines**: Replaced the static dashboard sparkline data with real dynamic tracking of composite project health scores over time, and upgraded `genspark` to plot smooth Bezier curves.
- **High-Fidelity Widget-to-Image Export**: Implemented custom canvas-based rendering with custom font configurations and direct DOM layout fallback styling to ensure exported widget images look identical to the active themes inside the app.
- **Theme-Aligned Status Toggles**: Restyled the filters on the *Screen Delivery Status* and *Module vs Type Status Matrix* widgets to align with the active theme's colors (`var(--color-primary)` for active background and `var(--color-surface)` for text/counters). Fixed the JS click handler bug on filter pills by removing the redundant innerHTML rewrite.
- **Defect Inflow Trend timescale**: Increased the Defect Inflow Trend widget's analysis period from 7 days to 7 weeks and updated descriptions.
- **Local Folder Sync Path in Excel**: Serialized the active directory sync path (`P.fsDirName`) to the Excel `System State` sheet, allowing the app to automatically reconstruct and restore directory sync handles from IndexedDB on Excel import.
- **Help Guide Calculations**: Added explanations of the dynamic **Health Index** (weighted penalty model) and **Delivery Confidence** (backlog volume vs 4-week velocity average) calculation systems to the "How this view works" Help Guide modal.

## 📅 [2026-06-04] - Retrospective Completion Tracking
- **Date Resolution & Normalization**: Implemented hoisted helper functions `getLogActivityDate(l)` and `getLogActivityDateStr(l)` to resolve actual completion dates retrospectively.
- **Log Entry Metadata**: Enhanced `addLog` to accept and serialize custom completion metadata (`subtaskId`, `actCompletionDate`).
- **Dashboard & Performance Timelines**: Updated 30-Day Activity timeline, recent activity widgets, member contribution heatmaps, weekly velocity dashboards, health metrics log replay (`calculateSparklineData`), and status reports (`autoPopulateReport`) to query log histories via resolved activity dates instead of log insertion timestamps.
- **Velocity & Confidence Fixes**: Corrected target log queries in Predictive AI ETA and Board Pack widgets to search by correct actions and newVal attributes, restoring historical velocity calculations.
- **Verification & Documentation**: Validated all changes via check_syntax.js and test_runtime.js, updated entity schemas and changelogs in the offline project context.

## 📅 [2026-06-05] - UI Layout & Icon Rendering Fixes
- **Dynamic Icon Binding**: Resolved invisible Lucide icons (specifically `trash-2` delete buttons in the reports list) by calling `lucide.createIcons()` immediately after dynamic toolbar and list injection.
- **Trash Icon Centering**: Fixed layout alignments and margin offsets for delete trash icons inside buttons and list item containers.

## 📅 [2026-06-14] - Three-Document Suite & Modular Build System
- **Document Generation Suite**: Added python build scripts (`build_pcd.py`, `build_fsd.py`, `build_umi.py`, `build_user_manual_docx.py`) to generate three core documents: Product Capabilities Document (PCD), Functional Specification Document (FSD), and User Manual Index (UMI) in DOCX and Markdown formats.
- **Master Compiler Orchestration**: Implemented `build_all.py` as a central script to run all python doc compilers in sequence.
- **Dynamic Manual Updates**: Created `update_manual.js` to parse current system dropdown configurations from `projectpulse.html` and compile updated Markdown manual sheets.

## 📅 [2026-06-15] - Premium Document Styles & Visual Illustrations
- **Custom Diagrams**: Designed and embedded 10 custom workflow, lifecycle, and architecture diagrams into the PCD, FSD, and UMI suites.
- **High-Density Screenshots**: Automated widget capturing via `capture_screenshots.py` and `capture_widgets.py` to crop and embed screenshots of all 30 widgets in the User Manual.
- **Premium DOCX Styling**: Configured explicit Segoe UI styling, clean XML table structures, and theme-matching borders for professional document exports.

## 📅 [2026-06-16] - Graphify Navigation & Exclusions
- **Community Labels**: Added names for Graphify communities 18-25 mapping the User Manual index, delivery matrix, team capacity, and bug tracker components.
- **Graph Scope Reduction**: Excluded non-code resources `docs/` and `scripts/` from Graphify analysis via `.graphifyignore`, narrowing the codebase analysis to the monolithic single-page app core.

## 📅 [2026-06-21] - Project Steering & Health Widget Enhancement (ui-ux-pro-max)
- **Design & Layout Enhancement**: Upgraded the Project Steering & Health widget inside `projectpulse.html` to match premium Swiss design guidelines, custom color palettes, and theme-aligned CSS tokens.
- **Card 1: Project Steering Hero**: Restyled the horizontal release phases to use interactive glassmorphic phase node elements and dynamic connecting track highlights on top-level tracks. Configured counts and sub-stats inside spacious bento-grid cards.
- **Card 2: Project Health Gauge**: Redrawn the SVG gauge with a thin colored arc, rounded path tracks, and a tapered sweep-animated needle. Configured an interactive score breakdown overlay detailing positive/negative scoring parameters.
- **Card 3: Schedule & Status Overview**: Replaced standard button tabs with a unified segment control bar. Styled tables with custom layouts, borders, hover highlights, and warning badges.
## 📅 [2026-08-09] - Release Roadmap Date Alignment & Task Data Metric Reconciliation
- **Release Roadmap Date & Version Reconciliation**:
  - Configured explicit `startDate` and target date (`date`) fields for all release objects in `P.releases` across sample datasets, restoring full visibility of start and target dates in the Release Roadmap table.
  - Added missing `v2.1.0` release version to align strategic features, mapped tasks, and release roadmap asset trackers.
- **Task Status & Completion Metric Reconciliation**:
  - Performed a comprehensive data audit across all 143 sample tasks in both standard (`sampleTasks`) and hierarchical (`samples.hierarchical.tasks`) preset configurations.
  - Reconciled 22+ tasks with `"status": "Not Started"` that held logged actual hours (`actHours > 0`) or progress, resetting `actHours: 0`, `actEffort: 0`, `progress: 0`, and clearing stray actual completion dates.
  - Reconciled `"status": "Completed"` tasks to guarantee `progress: 100`, valid `actualStartDate` (or `actStartDate`), `actualEndDate` (or `actCompletionDate`), and logged actual effort.
  - Standardized `TASK-001` (`💎 Milestone: Project Kickoff`) and all 5 child subtasks to completed statuses with exact date tracking.
- **Subtask Sync & Scheduler Auto-Fixes**:
  - Enhanced `syncTaskToTemplate` (line ~16460) so generated subtasks inherit `status: 'Completed'`, `done: true`, `progress: 100`, and `actCompletionDate` when the parent task is marked completed.
  - Enhanced `PulseScheduler.recalcDatesAndStatus` (line ~21281) to automatically calculate `actCompletionDate` from subtasks (or target date) whenever a task transitions to `'Completed'`.
- **Project Directory Cleanup & Documentation**:
  - Removed temporary Office lock files (`~$*`) and scratch test scripts from workspace.
  - Synchronized AST knowledge graph (`graphify update .`).



