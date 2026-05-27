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
