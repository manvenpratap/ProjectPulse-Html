# Live Project Insights & Analytics

The **Insights Tab** analyzes execution telemetry and maps historical velocity trends to formulate predictive forecasts.

---

## 1. Metric Caching (`buildDashCache`)

To ensure smooth animations and instant navigation responses, ProjectPulse uses a consolidated cache mechanism (`P.cache`):
- Hydrated whenever project tasks or resource allocations change.
- Prevents expensive loop operations on every render cycle.
- Calculates time-series arrays for cumulative task completion.

---

## 2. Earned Value Management (EVM)

ProjectPulse evaluates scheduling efficiency using standard EVM equations:

*   **Planned Value ($PV$)**:
    $$PV = \text{Total Budget} \times \frac{\text{Time Elapsed}}{\text{Total Timeline}}$$
*   **Earned Value ($EV$)**:
    $$EV = \text{Total Budget} \times \% \text{ Completion}$$
*   **Actual Cost ($AC$)**:
    $$AC = \text{Sum of logged resource hours} \times \text{Average Blended Resource Rate}$$
*   **Schedule Variance ($SV$)**:
    $$SV = EV - PV$$
*   **Schedule Performance Index ($SPI$)**:
    $$SPI = \frac{EV}{PV}$$

---

## 3. Burn-Down & Burn-Up Projection Chart

The burndown widget renders four data series on a single canvas with a velocity-based **Projection Cone** for post-"Today" forecasting.

### Interactive Module Filtering
At the top of the chart widget, a **Module Multi-select Filter Bar** dynamically displays active project modules as selectable chips:
- **"All" Chip**: Resets the filter, displaying the cumulative burn-down/up calculations for the entire project.
- **Multi-select Chips**: Selecting one or more modules filters the task dataset on-the-fly, instantly recalculating the total scope, completed/remaining effort, ideal path, actual burndown/up curves, projection cone, and estimated completion metrics.

### Sub-Task & Screen-Aware Effort Decomposition
Rather than treating tasks as binary all-or-nothing units, ProjectPulse decomposes task effort (`estEffort`) down to the sub-task level for highly precise tracking:
1. **Tasks without Sub-tasks**: Evaluated as a single binary unit. The full `estEffort` is considered remaining until the task status is marked `Completed` (completion date defaults to `updatedAt`, `dueDate`, or `actCompletionDate`).
2. **Tasks with Sub-tasks**: Proportionally splits the parent task's `estEffort` across its sub-tasks. Each sub-task's weight is `(st.effort / total_raw_subtask_effort)`.
   - **Regular Sub-tasks**: Binary completed when `st.status === 'Completed'`, `st.done === true`, or `st.progress === 100`.
   - **Screen Sub-tasks**: Evaluated fractionally. If progress is between 0% and 100%, the effort is split into a **completed portion** (`progress / 100`) and a **remaining portion** (`1 - progress / 100`). This ensures that partial progress on UI screens is reflected incrementally in the burndown and burnup metrics rather than waiting for full task completion.

### Series Rendered

| Series | Colour | Description |
|---|---|---|
| **Actual Burndown** | Red solid | Remaining effort each week up to Today (includes partial sub-task and screen completions) |
| **Ideal Burndown** | Amber dashed | Linear target from total scope → 0 |
| **Burn-Up** | Green solid | Cumulative completed effort per week (reflects fractional progress) |
| **Projection Cone** | Red shaded zone | Optimistic / Most-Likely / Pessimistic after Today based on recent velocity |

### Key Visual Elements

- **"Today" Pill** — A dark pill label rendered *inside* the chart marks the current week. The dashed vertical line starts beneath the pill.
- **"Deadline" Line** — A subtle purple dashed line at the last week marks the project end date.
- **"Most Likely" Label** — A labelled pill inside the cone, y-clamped to always stay within the chart area.
- **Dual Y-Axes** — Left axis (red) = Remaining Work; Right axis (green) = Completed Work.
- **Smart Data Labels** — Value callouts appear only when the value changes ≥ 1.5 % of the scale, or at first / last / Today points, preventing crowding on flat segments.
- **Thinned Dots** — On dense charts, dots are rendered at computed step intervals rather than every week.

### Projection Cone Calculation

The cone uses the team's **recent average burn rate** from the last 2 weeks of actual data:

| Trajectory | Rate multiplier |
|---|---|
| Optimistic | × 1.35 of avg weekly burn |
| Most Likely | × 1.00 (average) |
| Pessimistic | × 0.65 of avg weekly burn |

### Summary Bar KPIs

| Metric | Description |
|---|---|
| Total Scope | Sum of all `estEffort` values for the filtered module scope |
| Completed | Effort of completed tasks and sub-tasks (shown in green, includes partial screen completions) |
| Remaining | Remaining effort of non-completed tasks and sub-tasks (shown in red) |
| Progress | Completed ÷ Total Scope × 100 % |
| Est. Finish | Weeks until Most-Likely projection reaches zero |

### Hover Tooltip

Snaps to the nearest week and shows Ideal, Remaining, Completed, and Proj. ML values. Height adapts to the number of valid rows and is clamped to stay within the canvas.

---

## 4. Weekly Velocity

Measures work completed per week. Two modes:

- **Subtask-Weighted** — Effort × (progress gained ÷ 100).
- **Binary Completed** — Full task effort when status reaches `Completed`.

A 3-week rolling average is overlaid to smooth fluctuations.

---

## 5. Cumulative Flow Diagram (CFD)

Stacked area chart showing task counts in each status over 8–100 weeks. **Flow Health** is flagged healthy when `Completed ≥ In Progress`.
