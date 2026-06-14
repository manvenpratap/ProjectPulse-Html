# Schedule Baselines & Snapshot History

Schedule Baselines allow you to capture a static snapshot of your project's planned schedule. This helps you track deviations, measure schedule variance, identify slippage reasons, and restore past versions if planning assumptions change.

---

## 1. What is a Baseline?

A **Baseline** is the approved version of a project schedule. It consists of the planned start dates, due dates, and efforts (in hours/days/months) for all tasks.

In ProjectPulse, schedule tracking uses three sets of dates/efforts:
1. **Planned Dates (`startDate`, `dueDate`, `estEffort`)**: The current target dates that resources are working towards. These can be adjusted during execution.
2. **Baseline Dates (`baselineStartDate`, `baselineDueDate`, `baselineEffort`)**: The frozen target dates captured at a specific milestone (e.g., project kick-off). These serve as the reference point for calculating variance.
3. **Actual Dates (`actCompletionDate`, `actEffort`)**: The actual dates and efforts recorded when a task is completed.

---

## 2. Capturing a Baseline Snapshot

To capture a baseline snapshot:
1. Open **Project Settings** (by clicking the gear icon in the topbar).
2. Select **Schedule Baselines** from the sidebar.
3. Enter a **Baseline Name** (e.g., `Initial Kick-off Plan`) and a **Description** detailing the scope or milestones captured.
4. Click **Capture Snapshot**.

### What happens when you capture a snapshot?
- All active tasks' baseline fields (`baselineStartDate`, `baselineDueDate`, `baselineEffort`) are updated to match their current planned values (`startDate`, `dueDate`, `estEffort`).
- A snapshot record for every task is generated and appended to the flat `P.baselines` history array.
- This creates a historical record of the plan at that specific moment in time.

---

## 3. Variance and Slippage Analysis

Once a baseline is set:
- **Variance Days**: The difference (in days) between the current planned/actual date and the baseline date.
  - A positive variance (e.g., `+5d`) indicates the task is running late (slippage).
  - A negative variance indicates the task is ahead of schedule.
- **Slippage Rationale**: If a task slips, you can document the reason in the task editing flyout. This rationale is captured in subsequent baseline snapshots and is exported to Excel.

---

## 4. Restoring and Deleting Snapshots

From the **Schedule Baselines** panel, you can manage your captured snapshots:
- **Restore**: Overwrite your current active planned schedule and active baseline dates with the values saved in the snapshot. This provides a complete rollback capability.
- **Delete**: Permanently remove a baseline snapshot from the history log.
