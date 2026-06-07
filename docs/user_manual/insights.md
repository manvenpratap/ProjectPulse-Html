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

## 3. Burn-up & Burn-down Projections

Dynamic charts depict:
1.  **Scope Line (Burn-up)**: Total planned complexity points over time.
2.  **Completion Line**: Accumulated complexity points of "Completed" tasks.
3.  **Dynamic Projection**: A linear extrapolation based on the rolling 3-week velocity, estimating the exact calendar week of project completion.
