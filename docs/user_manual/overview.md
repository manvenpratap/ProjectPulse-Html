# Executive Overview Dashboard

The **Executive Overview Dashboard** is the commanding portal of ProjectPulse, displaying immediate health signals and facilitating schedule simulations.

---

## 1. Key Performance Indicators (KPIs)

The top ribbon hosts three primary, dynamically calculated status metrics:

| Metric | Calculation Heuristic / Logic | Target |
| :--- | :--- | :--- |
| **Health Index** | Integrates task completion ratios, unmitigated critical risks, and active high-severity defects. | `> 80%` (Green) |
| **Delivery Confidence** | Measures the schedule variance ($SV$) against the target milestones, factoring in team velocity. | `> 85%` (Green) |
| **Active RAID Elements** | Count of all items categorized as *Risk*, *Assumption*, *Issue*, or *Dependency* with status "Active". | `0` (Goal) |

---

## 2. Dynamic Health Gauge

The Health Gauge is a premium SVG radial visualization showing real-time health levels. Hovering over sections reveals a breakdown of underlying drag factors (e.g., "Defects: -12%", "Overdue Tasks: -8%").

```
      [   84%   ]
    /  Health   \
   |  Indicator  |  <-- Radial SVG Gauge (Green Neon Glow)
    \  Status   /
      `-------`
```

---

## 3. What-If Predictive Sandbox

The **Predictive Sandbox** allows managers to simulate schedule slips, capacity reductions, and scope expansions without mutating the active database.

### Operation
- **Toggle Sandbox Mode**: Shifts state from the master schedule (`P.tasks`) to a memory-based sandbox clone (`P.sandboxTasks`).
- **Simulate Resource Reductions**: Adjust available Capacity dynamically and observe the projected date drift.
- **Simulate Scope Expansion**: Artificially increase Task Complexity by a factor (e.g., $1.2\times$) to test schedule robustness.
- **Commit/Reset**: Click "Commit Changes" to override the active schedule, or "Discard" to revert the sandbox.
