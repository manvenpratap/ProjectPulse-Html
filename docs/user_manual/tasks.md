# Hierarchical Task Matrix & Interactive Gantt Timeline

The **Task Matrix & Gantt Timeline** serves as the central operational engine of ProjectPulse. It combines high-density spreadsheet data entry with an interactive, responsive SVG Gantt chart to govern work breakdown structures, multi-tiered dependencies, resource scheduling, and progress rollups.

---

## 1. Work Breakdown Structure (WBS) & Hierarchies

Tasks in ProjectPulse can be structured in a multi-level tree layout:

- **Parent Tasks (Epics / Functional Deliverables)**: High-level scopes of work that aggregate duration, calculate total estimated vs. actual hours, and roll up progress percentages from child tasks.
- **Subtasks (Action Items / Components)**: Work items assigned to specific team members with explicit start/end dates, complexity points, hourly estimates, and checklist steps.
- **GUI Screen Subtasks**: Specialized subtasks marked with a Screen ID (e.g., `SCR-101`) that automatically scale according to screen step counts and serialize through assignee-based GUI scheduling rules.
- **Checklist Steps**: Atomic verification items within subtasks that drive fractional progress completion.

```
[Parent Task: T-100 User Authentication Subsystem]
  ├── [Subtask: T-101 OAuth 2.0 Integration] (8 pts / 40 hrs - In Progress)
  │     ├── [Step 1: Provider Configuration] (Completed)
  │     └── [Step 2: Token Refresh Flow] (In Progress)
  └── [Subtask: T-102 Multi-Factor Authentication Screen] (SCR-04, 5 pts / 24 hrs - Scheduled)
```

---

## 2. Spreadsheet-Style Inline Editing

The Task Matrix functions as an ultra-fast spreadsheet:

- **Double-Click Cell**: Activates inline editors tailored to each column type (Text, Date Picker, Number Input, or Dropdown Select).
- **Keyboard Navigation**:
  - `Tab` / `Shift+Tab`: Move to the next or previous editable cell in the row.
  - `Enter`: Commit the value, trigger date recalculations, and move to the cell below.
  - `Escape`: Cancel editing and revert to the previous value.
- **Auto-Save & Validation**: Edits are committed immediately on `blur` or `Enter`, triggering debounced background persistence to LocalStorage and IndexedDB.
- **Context Menus**: Right-clicking any task row reveals an action menu:
  - Add Child Subtask
  - Duplicate Task / Subtask Tree
  - Convert to Milestone
  - Reassign Resource
  - View Activity Audit Log
  - Delete Task

---

## 3. Complexity & Estimation Scaling

ProjectPulse utilizes a Fibonacci-based point system combined with modular complexity multipliers:

$$\text{Estimated Hours} = \text{Base Step Hours} \times \text{Complexity Multiplier}$$

- **Complexity Tiers**:
  - **Easy** ($0.5\times$ multiplier): Routine or well-understood implementations.
  - **Medium** ($1.0\times$ multiplier): Standard development effort.
  - **Complex** ($1.5\times$ multiplier): High-risk, architectural, or multi-system integrations.
- **Fibonacci Point Weighting**: Tasks use Fibonacci story points ($1, 2, 3, 5, 8, 13$). Tasks with $\ge 8$ points trigger a splitting recommendation in the Insights diagnostic panel.
- **Automated Rollups**: Modifying a subtask's hours, dates, or progress automatically propagates upward to recompute the parent task's overall progress percentage and date boundaries.

---

## 4. Interactive Gantt Timeline

The integrated Gantt Timeline visualizes the temporal layout and relationship network of all tasks:

- **SVG Dynamic Rendering**: High-performance vector timeline rendering hundreds of tasks with zero lag.
- **Zoom Levels**: Toggle between **Day**, **Week**, and **Month** viewing scales.
- **Dependency Paths**: Visual bezier connector lines representing task dependencies:
  - **Finish-to-Start (FS)**: Task B starts after Task A finishes.
  - **Start-to-Start (SS)**: Task B starts alongside Task A.
  - **Finish-to-Finish (FF)**: Task B finishes alongside Task A.
- **Critical Path Highlighting**: Highlights the sequence of dependent tasks that directly dictates the overall project completion date.
- **Drag-to-Schedule**: Dragging a timeline bar shifts the task's start and end dates, automatically adjusting all dependent downstream tasks in real-time.

---

## 5. Automated Scheduling Rules (`recalcDatesAndStatus`)

ProjectPulse features an automated scheduling engine that prevents over-allocation and maintains chronological integrity:

1. **Assignee-based GUI Serialization**:
   - For GUI modules, screen subtasks assigned to the *same engineer* are automatically scheduled sequentially according to priority (Critical $\rightarrow$ High $\rightarrow$ Medium $\rightarrow$ Low).
   - Screen subtasks under *different engineers* are scheduled in parallel, branching from the parent task start date.
2. **Non-GUI Sequential Scheduling**:
   - For backend, database, and infrastructure tasks, steps propagate sequentially from step to step regardless of assignee.
3. **Auto-Completion Inheritance**:
   - When all child subtasks reach `Completed`, the parent task automatically transitions to `Completed`.
   - If any subtask is marked `Blocked`, the parent task displays a warning badge indicating a blocked dependency.

---

## 6. Intelligent Column Autofit Integration

The Task Matrix integrates with the ProjectPulse 5-strategy autofit engine (`applyAutofitStrategy`):

- **Clip & Wrap (`clip_wrap`)**: Standard table layout with soft text-wrapping on titles and remarks.
- **Clip & No-Wrap (`clip_nowrap`)**: Maximizes row density with single-line ellipsis clipping.
- **Wrap & Balance (`wrap_balance`)**: Multi-line expansion designed for thorough task descriptions.
- **Fill & Distribute (`fill_distribute`)**: Proportionally stretches columns to utilize 100% of widescreen displays.
- **Natural Scroll (`natural_scroll`)**: Preserves natural column widths with a smooth horizontal scroll container.
