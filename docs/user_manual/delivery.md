# Hierarchical Delivery Matrix

The **Delivery Matrix** is the operational database of project deliverables, milestones, and tasks. It supports complex task grouping, status tracking, and dependency linking.

---

## 1. Parent-Child Hierarchies

Tasks in ProjectPulse can be structured in a multi-level tree layout:
- **Parent Tasks (Deliverables / Epics)**: Summarize scope, aggregate duration, and roll up progress metrics from child tasks.
- **Subtasks (Actions / Deliverables)**: Individual items containing assignments, hours, complexity, and specific start/end dates.

```
[Deliverable 1: Core API Setup]
  ├── Subtask 1.1: Database Schema Definition (Completed)
  └── Subtask 1.2: Endpoints Integration (In Progress)
```

---

## 2. Spreadsheet-Style Inline Editing

For rapid entry and adjustment, the delivery matrix operates like a spreadsheet:
- **Double-Click Cell**: Activates inline input fields for fields like *Title*, *Hours*, *Complexity*, or *Due Date*.
- **Dropdown Enforcements**: Restricts inputs to valid system options (e.g., Status: "Not Started", "In Progress", "Blocked", "Completed"; Priority: "Low", "Medium", "High").
- **Auto-Save**: Changes propagate to state and persist to storage upon defocusing (`blur` event) or pressing `Enter`.

---

## 3. Complexity & Estimation Scaling

ProjectPulse utilizes a Fibonacci-based scale for estimating task complexity:

$$\text{Complexity Points} \in \{1, 2, 3, 5, 8, 13\}$$

- **Calculation**: These points are used in combination with assigned hours to compute the velocity index in the **Insights Tab**.
- **Rule**: High-complexity tasks (8 points or above) are automatically flagged with a recommendation to split them into smaller, lower-risk child tasks.
