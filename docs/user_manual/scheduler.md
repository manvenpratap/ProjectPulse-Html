# Intelligent Weekly Scheduler & Conflict Resolver

The **Weekly Scheduler** is the resource-levelling engine of ProjectPulse. It maps resource capacity against assigned task efforts in a dynamic weekly view, identifying allocation constraints and conflicts.

---

## 1. The Weekly Heatmap Grid

The grid displays a list of team resources vertically and calendar weeks horizontally. Cells are styled to reflect resource allocations:

- **Monospace Grid Design**: Displays allocated hours vs. maximum weekly capacity.
- **Dynamic Heatmap Colorization**:
  - **Over-allocation (Red Alert)**: Hours allocated exceed Capacity (e.g., `45h / 40h`). The cell glows with a neon crimson border.
  - **Optimal (Green)**: Allocation is between $80\%$ and $100\%$ capacity.
  - **Under-allocated (Grey/Slate)**: Resource has significant idle capacity.

---

## 2. Interactive Tooltips

Hovering over elements on the grid displays live data details:
- **Grid Cells**: Shows list of tasks assigned to the resource for that week, total hours, and remaining available hours.
- **Task Chips**: Shows the task status, parent deliverables, priority level, and start/end dates.

---

## 3. The Diagnostics Cockpit & "Quick Tips"

On the right side of the scheduler layout, a multi-tab cockpit provides real-time information:
- **Tab 1: Diagnostics**: Displays a list of active conflicts (e.g., "Overallocated", "Task Dependency Violations").
- **Tab 2: Copilot Actions**: Offers automated quick actions.
- **Tab 3: Quick Tips**: Shows shortcuts, operation guides, and sandbox reminders.

---

## 4. Conflict Resolution Heuristics

ProjectPulse features an automated conflict resolver (`autoResolveAllSchedulerConflicts`) that evaluates tasks in the sandbox state:

### Heuristic A: Auto-Sequence
If two tasks with dependency relationships ($Task_A \to Task_B$) overlap, the resolver shifts $Task_B$ to start immediately after $Task_A$ ends.

### Heuristic B: Smart Reassignment
If Resource $R_1$ is overallocated and Resource $R_2$ shares the same Role and has available capacity, tasks are re-assigned to $R_2$.

### Heuristic C: Cascading Date Shifting
If a delay occurs on a critical path task, the resolver shifts all dependent future tasks forward, maintaining established buffer periods.
