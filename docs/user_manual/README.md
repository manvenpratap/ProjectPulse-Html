# ProjectPulse User Manual — Master Index

Welcome to the official documentation for **ProjectPulse**, the monolithic, single-page, high-performance project management workstation. 

This user manual directory serves as the definitive reference guide for project leads, executives, developers, and QA engineers utilizing ProjectPulse to plan deliverables, mitigate RAID elements, monitor resource allocation, and track defects.

---

## Directory Navigation & Feature Guides

Explore the detailed functional specifications and operating procedures for each system module:

1. **[Executive Overview Dashboard](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/overview.md)**
   - Core KPIs: Health Index, Delivery Confidence, and RAID count.
   - What-If Predictive Sandbox: Simulating schedule variations in real-time.
2. **[Live Project Insights](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/insights.md)**
   - Performance metrics caching (`buildDashCache`).
   - Earned Value Management (EVM) and velocity pacing equations.
3. **[Software Deliveries & Deployment Schedule](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/delivery.md)**
   - Release governance, ALM/PDN change tracking, multi-entity task & screen linkage.
   - Dual perspectives: Table Grid View and Visual Perspective Heatmaps (Module, Version, Phase).
   - 5-strategy Column Autofit Engine and bi-directional Excel telemetry synchronization.
4. **[Reports & Board Packs](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/reports.md)**
   - Generating stakeholder reports, status updates, and export parameters.
5. **[Intelligent Weekly Scheduler & Conflict Resolver](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/scheduler.md)**
   - Operating the Weekly Heatmap Grid, Diagnostics, and Copilot.
   - Detailed heuristics: Auto-Sequence, Reassignment, and Cascading Date Shifting.
6. **[Unified RAID Register](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/risks.md)**
   - Risks, Assumptions, Issues, and Dependencies management.
   - Threat assessment matrix scoring.
7. **[Hierarchical Task Matrix & Interactive Gantt Timeline](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/tasks.md)**
   - Work Breakdown Structure (WBS), subtask checklists, and screen subtask scaling.
   - Spreadsheet-style inline cell editing and Fibonacci complexity multipliers.
   - Interactive SVG Gantt chart, critical path calculation, and dependency links (FS, SS, FF).
8. **[Team Capacity Hub](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/team.md)**
   - Resource loading, roles assignment, and workload balancing.
9. **[Defect Tracker](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/defects.md)**
   - Bug lifecycle, severity metrics, and QA validation workflows.
10. **[Audit & Activity Log](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/activity.md)**
    - Historic logging, change tracking, and state reconstruction.
11. **[Schedule Baselines & Snapshot History](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/baselines.md)**
    - Capturing baseline snapshots, calculating schedule variance, slippage rationales, and restoring history.

---

## Architecture Schematic

The diagram below represents the single-page state flow of ProjectPulse:

```
[LocalStorage/IndexedDB Backup Store] 
                 │ (Hydrates on Init)
                 ▼
          [Global State P] ◄──────┐
                 │                │ (State Updates)
                 ▼                │
     [recalcDatesAndStatus] ──────┘
                 │
                 ▼
          [buildDashCache]
                 │
                 ▼
      [renderView(ActiveView)]
                 │
  ┌──────────────┼──────────────┬──────────────┐
  ▼              ▼              ▼              ▼
[Overview]  [Deliveries]   [Scheduler]   [Tasks / Gantt] ... (Other Views)
```

---

## Daily Automated Synchronization

To ensure the documentation remains dynamically synchronized with the actual system configurations, active team sizes, dropdown options, and complexity multipliers, a background task compiles this folder daily.
- If a local directory handle is configured in the browser, the app updates this folder on page load.
- If working via the CLI, the macOS LaunchDaemon executes `node scripts/update_manual.js` daily at **00:00 AM**.
