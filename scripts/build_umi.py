"""
build_umi.py
============
Builds the ProjectPulse User Manual with Illustrations (UMI).
Audience: End users — Project Managers, Team Leads, Engineers, QA.
Tone: Procedural, step-numbered, conversational.
Output: docs/ProjectPulse_User_Manual.docx
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from docx_helpers import *

OUT_PATH = os.path.join(DOCS_DIR, "ProjectPulse_User_Manual.docx")


def ch_getting_started(doc):
    make_heading(doc,"Chapter 1 — Getting Started",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "This chapter explains how to open ProjectPulse for the first time, load your project, "
        "and navigate the main interface.",space_after=8)

    make_heading(doc,"1.1  Opening ProjectPulse",level=2,color=CLR_ACCENT)
    make_body(doc,"ProjectPulse requires no installation. Follow these steps:",space_after=4)
    make_numbered(doc,"Locate the projectpulse.html file on your computer or shared drive.")
    make_numbered(doc,"Double-click the file to open it in your default web browser.")
    make_numbered(doc,"ProjectPulse loads with a welcome landing page. Click 'Enter' or 'Open App' to enter the main dashboard.")
    make_numbered(doc,"To start a fresh project: click Settings (gear icon) -> General -> 'Reset Project'. Enter your project name and click Save.")
    add_screenshot(doc,"15_landing_page",
        "Figure 1.1 — The Welcome/Landing page of ProjectPulse before entering the main workspace.")
    doc.add_paragraph()
    add_callout(doc,
        "For the best experience, use Google Chrome or Microsoft Edge version 110 or later. "
        "Firefox and Safari are also fully supported.",style="tip")
    
    make_heading(doc,"1.2  The Navigation Bar",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The left-side navigation bar is your primary way to move between modules. "
        "Each icon represents one module:",space_after=4)
    add_data_table(doc,
        ["Icon","Module","When to Use"],
        [
            ["Home/Gauge",    "Executive Overview Dashboard",  "Morning stand-up health check. Exec reporting."],
            ["Chart Bar",     "Live Insights & Analytics",     "Weekly velocity reviews. EVM reporting."],
            ["Table Grid",    "Delivery Matrix",               "Daily task management. Inline editing."],
            ["Bars (Gantt)",  "Gantt Timeline",                "Schedule planning. Dependency visualisation."],
            ["Calendar",      "Weekly Scheduler",              "Resource allocation. Conflict resolution."],
            ["Shield",        "RAID Register",                 "Risk tracking. Issue management."],
            ["People",        "Team Capacity Hub",             "Member management. Leave planning."],
            ["Bug",           "Defect Tracker",                "Bug logging. QA lifecycle management."],
            ["Document",      "Reports & Board Packs",         "Stakeholder reporting. Excel export."],
            ["Clock",         "Audit Log",                     "Activity review. Change investigation."],
            ["Gear",          "Settings / Configuration",      "System administration. Theme selection."],
        ],
        col_widths=[1.2,2.0,3.2],
    )

    make_heading(doc,"1.3  Saving Your Work",level=2,color=CLR_ACCENT)
    make_body(doc,
        "ProjectPulse saves your work automatically every 10 seconds. You will see a "
        "brief 'Saving...' indicator in the top bar. You can force an immediate save "
        "at any time by pressing Ctrl + S.",space_after=6)
    add_callout(doc,
        "Never close the browser tab while the 'Saving...' indicator is active. "
        "Wait for it to disappear before closing to ensure your last changes are saved.",style="caution")



def ch_overview(doc):
    make_heading(doc,"Chapter 2 — Executive Overview Dashboard",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Overview Dashboard is your project's health health command centre. "
        "It gives you an instant read on how your project is performing across "
        "four critical dimensions: schedule, risk, quality, and delivery confidence.",space_after=8)
    add_screenshot(doc,"01_overview_dashboard",
        "Figure 2.1 — The Executive Overview Dashboard showing the Health Gauge, KPI cards, and Predictive Sandbox.")

    make_heading(doc,"2.1  Reading the Health Gauge",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The large radial gauge in the top-left is your project's Health Index (0-100). "
        "The arc colour tells you the overall status at a glance:",space_after=4)
    add_data_table(doc,
        ["Colour","Health Range","What It Means","Recommended Action"],
        [
            ["Green", "80-100","Project is healthy. Risks and issues are under control.","Continue current pace."],
            ["Amber", "50-79", "One or more risk factors are active. Attention needed.","Review RAID register. Address overdue tasks."],
            ["Red",   "0-49",  "Critical situation. Multiple problems require immediate resolution.","Escalate to leadership. Resolve S1 defects and critical risks."],
        ],
        col_widths=[1.0,1.2,2.4,2.0],
    )

    make_heading(doc,"2.2  Understanding the Three KPI Cards",level=2,color=CLR_ACCENT)
    make_body(doc,"Below the gauge are three key performance indicator cards:",space_after=4)
    make_bullet(doc,"Delivery Confidence (%): The probability of delivering all remaining work on time based on current velocity. 80%+ is green.")
    make_bullet(doc,"Schedule Performance Index (SPI): Industry standard EVM metric. 1.0 = exactly on schedule. Below 1.0 = behind schedule.")
    make_bullet(doc,"Active RAID Items: Total count of open Risks, Assumptions, Issues, and Dependencies. Lower is better.")
    doc.add_paragraph()

    make_heading(doc,"2.3  Using the What-If Predictive Sandbox",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The Sandbox lets you safely model scenarios — like losing a team member or adding "
        "scope — without touching your live schedule. Here is how to use it:",space_after=4)
    make_numbered(doc,"Click the 'Enable Sandbox' toggle on the right side of the Dashboard.")
    make_numbered(doc,"The Sandbox indicator banner appears, confirming you are in simulation mode.")
    make_numbered(doc,"Use the Capacity Slider to model a reduction (e.g., slide to -20% to simulate losing one of five team members).")
    make_numbered(doc,"Use the Scope Multiplier to model scope growth (e.g., 1.2x if 20% more work has been discovered).")
    make_numbered(doc,"Watch the projected completion date update instantly.")
    make_numbered(doc,"If happy with the simulation: click 'Commit Changes' to apply. Otherwise, click 'Discard' to cancel.")
    doc.add_paragraph()
    add_callout(doc,
        "The Sandbox never modifies your live schedule unless you click 'Commit Changes'. "
        "Discarding has no effect on your actual project data.",style="tip")


    make_heading(doc,"2.4  Interactive Dashboard Widgets Reference Guide",level=2,color=CLR_ACCENT)
    make_body(doc,
        "ProjectPulse is built around an interactive, highly-customisable widget ecosystem. "
        "Each widget acts as an information radiator, providing transparency on specific metrics.",space_after=8)

    # Widget Catalog
    make_heading(doc,"2.4.1  Schedule Pacing & Milestones Widget",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Purpose: Shows upcoming delivery demands and recently achieved milestones.\n"
        "• How to Read: Displays upcoming tasks due in 7, 14, and 30 days as badge counters. "
        "Red badges indicate immediate pressure, amber shows moderate volume, and green indicates a light schedule. "
        "A checklist below lists completed milestone tasks marked with green check circles.\n"
        "• Actionable Insight: If the 7-day badge is Red, ensure the assignee list is fully staffed and no team member has planned leaves.",space_after=6)

    make_heading(doc,"2.4.2  High-Priority RAID Risks Widget",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Purpose: Surface the most critical threats to project execution.\n"
        "• How to Read: Lists the top three active risks from the RAID register sorted by highest exposure score. "
        "Each risk shows its ID, title, impact level, and designated owner.\n"
        "• Actionable Insight: Assign owners immediately to any risk flagged with High impact to ensure mitigation activities are underway.",space_after=6)

    make_heading(doc,"2.4.3  Strategic Module Status Matrix Widget",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Purpose: Summarise software engineering progress across architectural modules.\n"
        "• How to Read: A grid displaying modules (e.g., Core Engine, API Gateway) on rows and statuses on columns. "
        "Numbers inside cells show the count of tasks, with a horizontal progress bar indicating completion percentage. "
        "Hovering over elements reveals release mappings.\n"
        "• Actionable Insight: Check for modules with 0% progress when close to their target release versions to prevent release slippage.",space_after=6)

    make_heading(doc,"2.4.4  Team Capacity Allocation Widget",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Purpose: Visualise the distribution of effort across roles and disciplines.\n"
        "• How to Read: Features a progress grid representing total planned hours allocated to each role (e.g., Lead Architect, QA, PM). "
        "Shows percentage bars indicating resource utilisation ratios.\n"
        "• Actionable Insight: A high QA utilization combined with low Developer progress implies QA resources are idle, suggesting tasks need sequencing adjustments.",space_after=6)

    make_heading(doc,"2.4.5  High Impact Entities & Overdue Attention Widget",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Purpose: Identify tasks blocking downstream work or lagging past their deadlines.\n"
        "• How to Read: Lists critical path items with high follower counts, and overdue items. "
        "Red badges indicate tasks past their due date, while warning icons highlight blockers with multiple dependents.\n"
        "• Actionable Insight: Allocate senior developers to resolve overdue blocking tasks immediately to prevent compounding delays.",space_after=6)

    make_heading(doc,"2.4.6  Defect Intelligence Bento Grid Widget",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Purpose: Track product quality metrics and defect density.\n"
        "• How to Read: A collection of indicators presenting defects grouped by S1-S4 Severity (e.g. Blocker, High), "
        "priority distribution, and resolution rate (Closed vs. Open). Displays defect counts linked per code module.\n"
        "• Actionable Insight: An S1 Blocker count above zero triggers a high-severity red alert. QA testing should pause on that module until resolved.",space_after=6)

    make_heading(doc,"2.4.7  Predictive Intelligence Widget",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Purpose: Machine learning-driven forecast of final delivery timelines.\n"
        "• How to Read: Displays an estimated completion date and a risk factor score. "
        "Accounts for historically logged actual effort versus baseline schedules to project delays.\n"
        "• Actionable Insight: If the predictive completion date drifts past the project deadline, trigger a re-scoping exercise or utilize the Sandbox to model capacity shifts.",space_after=6)

    make_heading(doc,"2.4.8  Advanced Analytics: Burn-up & Velocity Widgets",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Purpose: Monitor long-term pacing and team output.\n"
        "• How to Read: The Burn-up chart plots scope lines alongside completed hours. "
        "The Weekly Velocity widget shows a bar chart of effort completed week-over-week. "
        "The Cumulative Flow diagram highlights task volume by state over time.\n"
        "• Actionable Insight: Flat weekly velocity indicates operational bottlenecks or unlogged work, requiring status reviews.",space_after=6)

    add_page_break(doc)


def ch_insights(doc):
    make_heading(doc,"Chapter 3 — Live Insights & Analytics",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Insights module gives you deep visibility into project performance through "
        "EVM metrics, velocity trends, burn-up projections, and activity patterns.",space_after=8)
    add_screenshot(doc,"01b_insights_analytics",
        "Figure 3.1 — The Project Insights Dashboard showing EVM parameters, Burn-Up projection, and Weekly Velocity tracking.")

    make_heading(doc,"3.1  Reading EVM Metrics",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The EVM (Earned Value Management) cards show the financial health of your project. "
        "You do not need to enter cost data — ProjectPulse uses effort hours as the cost proxy.",space_after=4)
    make_bullet(doc,"SPI (Schedule Performance Index): 1.0 = on schedule. Above 1.0 = ahead. Below 1.0 = behind.")
    make_bullet(doc,"SV (Schedule Variance): Positive = delivering ahead of plan. Negative = behind plan.")
    make_bullet(doc,"Green cards = healthy. Amber = watch. Red = needs action.")
    doc.add_paragraph()
    add_callout(doc,
        "EVM metrics are most meaningful after 2+ weeks of task completions. "
        "On new projects, give the analytics a week to calibrate.",style="note")


    make_heading(doc,"3.2  Reading the Burn-Down & Burn-Up Chart",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The chart widget renders four series on a single canvas to track remaining and completed work:",space_after=4)
    make_bullet(doc,"Actual Burndown (Red solid): Remaining effort to date, reflecting detailed sub-task and screen progress.")
    make_bullet(doc,"Ideal Burndown (Amber dashed): A linear baseline from total project scope down to zero remaining work.")
    make_bullet(doc,"Burn-Up (Green solid): Cumulative completed effort, including partial progress from screen sub-tasks.")
    make_bullet(doc,"Projection Cone (Red shaded zone): The range of possible outcomes (Optimistic, Most-Likely, and Pessimistic) after Today based on recent burn rates.")
    add_callout(doc,
        "Use the Module Filter Chips at the top of the card to filter the dataset. "
        "Selecting specific modules instantly recalculates all metrics and trajectories for that subset of work.",style="note")

    make_heading(doc,"3.3  Interpreting the 30-Day Activity Heatmap",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The heatmap shows how active your team has been each day over the past 30 days. "
        "Darker teal cells = more task state changes. Lighter cells = quiet days.",space_after=4)
    make_bullet(doc,"Gaps (white days) may indicate blockers or weekend/holidays.")
    make_bullet(doc,"Uniform activity is a sign of a well-paced team.")
    make_bullet(doc,"Activity spikes at the end of weeks may indicate date-driven completion behaviour.")
    add_page_break(doc)


def ch_delivery(doc):
    make_heading(doc,"Chapter 4 — Hierarchical Delivery Matrix",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Delivery Matrix is where the day-to-day work happens. "
        "Every task, subtask, assignee, date, status, and effort is managed here.",space_after=8)
    add_screenshot(doc,"02_delivery_matrix",
        "Figure 4.1 — The Delivery Matrix showing parent tasks, subtasks, status pills, and inline editing controls.")

    make_heading(doc,"4.1  Creating Your First Task",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click the '+ Add Task' button in the top-right of the Delivery Matrix.")
    make_numbered(doc,"Alternatively, open the Task Flyout detailed panel by clicking the task detail/edit button.")
    make_numbered(doc,"A comprehensive form appears with fields for name, assignee, status, priority, complexity, dates, and dependencies.")
    make_numbered(doc,"Fill in the details and click 'Save Task'.")
    add_screenshot(doc,"11_add_task_flyout",
        "Figure 4.2 — The interactive Task Details flyout panel showing comprehensive fields and subtask lists.")
    doc.add_paragraph()

    make_heading(doc,"4.2  Adding Subtasks",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click the expand arrow ▶ on any parent task row to reveal the subtask area.")
    make_numbered(doc,"Click '+ Add Subtask'.")
    make_numbered(doc,"Enter the subtask name and category (e.g., Feature / GUI Screen / Test Case).")
    make_numbered(doc,"Set the subtask status and effort estimate.")
    make_numbered(doc,"The parent task's progress bar automatically updates based on subtask completion.")
    doc.add_paragraph()

    make_heading(doc,"4.3  Updating Task Status",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Double-click the Status cell on any task row.")
    make_numbered(doc,"A dropdown appears with the available next statuses (invalid transitions are hidden).")
    make_numbered(doc,"Select the new status.")
    make_numbered(doc,"If the transition requires a comment (e.g., moving to On Hold or Cancelled), a dialog appears.")
    make_numbered(doc,"Enter your comment and click Confirm.")
    make_numbered(doc,"The status pill updates immediately and the change is recorded in the Audit Log.")
    doc.add_paragraph()


    make_heading(doc,"4.4  Filtering Tasks",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click the Filter icon in the top-right toolbar to open the filter panel.")
    make_numbered(doc,"Select one or more values in any filter category (Status, Assignee, Module, Priority, etc.).")
    make_numbered(doc,"The task list updates immediately to show only matching tasks.")
    make_numbered(doc,"Active filters appear as coloured pills above the task list. Click the 'x' on any pill to remove that filter.")
    make_numbered(doc,"Use the Search box to find tasks by name, ID, notes, or assignee.")
    doc.add_paragraph()
    add_callout(doc,
        "Multiple filters are combined with AND logic — only tasks matching ALL active filters appear. "
        "To reset all filters at once, click the 'Clear All' button in the filter panel.",style="tip")

    make_heading(doc,"4.5  Linking Task Dependencies",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Open a task by clicking the task name to open the Task Detail panel.")
    make_numbered(doc,"Scroll to the 'Depends On' section.")
    make_numbered(doc,"Click '+ Add Dependency'.")
    make_numbered(doc,"Search for and select the predecessor task.")
    make_numbered(doc,"Click Confirm. The dependency is added and visible in the Gantt view.")
    doc.add_paragraph()
    add_callout(doc,
        "ProjectPulse prevents circular dependencies. If you attempt to add a dependency "
        "that would create a loop (e.g., Task A depends on Task B which already depends on Task A), "
        "an error message is shown and the dependency is not saved.",style="warning")

    make_heading(doc, "4.6  Field Reference: Task & Subtask Business Objects", level=2, color=CLR_ACCENT)
    make_body(doc,
        "This section provides an authoritative data glossary for all attributes of the Task and Subtask business objects. "
        "Every field must be entered exactly as defined below to ensure downstream calculations function correctly.", space_after=6)
    
    make_heading(doc, "4.6.1  Task Object Attributes", level=3, color=CLR_NAVY)
    add_data_table(doc,
        ["Field Name", "Type / Format", "UI Required?", "Validation / Allowed Values", "Description / Cross-Module Effect"],
        [
            ["Task Title", "String", "Yes", "Non-empty. Max 100 chars.", "Human-readable label shown in the Gantt bar and list views."],
            ["Assignee", "String (Enum)", "No", "Selected from active members.", "Designated worker. Used by Scheduler for weekly capacity loading."],
            ["Status", "String (Enum)", "Yes", "VALID_TRANSITIONS key.", "Current state (e.g. Not Started, In Progress, QA, Completed). Triggers log."],
            ["Priority", "String (Enum)", "Yes", "Critical / High / Medium / Low.", "Qualitative severity. Used to prioritize tasks in lists and reports."],
            ["Category", "String (Enum)", "Yes", "Active category list.", "Classification (e.g. Feature, Bug, DevOps). Used for effort distribution."],
            ["Module", "String (Enum)", "Yes", "Active module list.", "System component linked to this task. Recalculates module maturity matrix."],
            ["Start Date", "Date (YYYY-MM-DD)", "Yes", "Must be <= Due Date.", "Planned start. Shifts downstream tasks if Cascade is enabled."],
            ["Due Date", "Date (YYYY-MM-DD)", "Yes", "Must be >= Start Date.", "Planned deadline. Used for overdue badges and slippage calculation."],
            ["Est. Effort", "Number", "Yes", ">= 0 hours (or active unit).", "Expected effort. Used to load the resource Scheduler heatmap."],
            ["Act. Effort", "Number", "No", ">= 0 hours (or active unit).", "Logged work to date. Increments actuals in EVM analytics calculations."],
            ["Depends On", "String List", "No", "Task IDs. Must be acyclic.", "Prerequisite task dependencies. Circular dependencies are rejected in form."],
            ["Complexity", "String (Enum)", "Yes", "Easy / Medium / Complex.", "Point multiplier (0.5x, 1.0x, 1.5x) used to calculate weekly velocity."],
            ["Progress (%)", "Number", "No", "0 to 100.", "Completions. Derived as weighted average of subtasks if present."],
            ["Notes", "String", "No", "Free text.", "Additional instructions, specifications, or development comments."]
        ],
        col_widths=[1.1, 1.1, 0.8, 1.5, 2.2]
    )

    make_heading(doc, "4.6.2  Subtask Object Attributes", level=3, color=CLR_NAVY)
    add_data_table(doc,
        ["Field Name", "Type / Format", "UI Required?", "Validation / Allowed Values", "Description / Cross-Module Effect"],
        [
            ["Subtask Title", "String", "Yes", "Non-empty.", "Detailed step description (e.g. 'Build login controller')."],
            ["Category", "String (Enum)", "Yes", "Step / GUI Screen / Test.", "Subtask type. Linked GUI Screen types auto-update design states."],
            ["Status", "String (Enum)", "Yes", "Not Started / In Progress / Completed.", "Subtask status. Setting to Completed sets 'done' to true."],
            ["Effort (Hrs)", "Number", "Yes", ">= 0.", "Estimated effort. Aggregates to parent task's total estimates."],
            ["Act. Effort", "Number", "No", ">= 0.", "Logged effort. Propagates actuals to parent task and EVM metrics."]
        ],
        col_widths=[1.1, 1.1, 0.8, 1.5, 2.2]
    )
    add_page_break(doc)


def ch_gantt(doc):
    make_heading(doc,"Chapter 5 — Gantt Timeline",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Gantt Timeline gives you a visual, time-anchored view of your entire schedule. "
        "Use it for planning, identifying bottlenecks, and communicating timelines to stakeholders.",
        space_after=8)
    add_screenshot(doc,"03_gantt_timeline",
        "Figure 5.1 — The Gantt Timeline with task bars, dependency arrows, baseline overlay, and today marker.")

    make_heading(doc,"5.1  Navigating the Timeline",level=2,color=CLR_ACCENT)
    make_bullet(doc,"Use the Zoom controls (Day / Week / Month / Quarter) in the toolbar to adjust the visible time horizon.")
    make_bullet(doc,"Scroll horizontally to move forward or backward in time.")
    make_bullet(doc,"Click 'Today' to jump the view to the current date.")
    make_bullet(doc,"The red vertical line marks today's date.")
    doc.add_paragraph()

    make_heading(doc,"5.2  Reading Dependency Arrows",level=2,color=CLR_ACCENT)
    make_body(doc,"Arrows connecting task bars represent dependencies. Colour indicates health:",space_after=4)
    make_bullet(doc,"Green arrow: The predecessor task is complete. Dependency is resolved.")
    make_bullet(doc,"Blue arrow: The predecessor task is in progress. Dependency is active.")
    make_bullet(doc,"Red arrow: VIOLATION — the successor task starts before the predecessor finishes. Needs attention.")
    doc.add_paragraph()


    make_heading(doc,"5.3  Rescheduling Tasks by Drag",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click and hold on a task bar.")
    make_numbered(doc,"Drag it left (earlier) or right (later) to the new start date.")
    make_numbered(doc,"A ghost bar shows the original position while you drag.")
    make_numbered(doc,"Release to confirm. The task's Start and Due dates are updated automatically.")
    make_numbered(doc,"If 'Cascade Dependents' is enabled, all downstream tasks shift by the same number of days.")
    doc.add_paragraph()

    make_heading(doc,"5.4  Enabling Baseline Overlay",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click the 'Show Baseline' toggle in the Gantt toolbar.")
    make_numbered(doc,"Semi-transparent ghost bars appear behind the current task bars showing the captured baseline dates.")
    make_numbered(doc,"Tasks ahead of baseline: current bar is to the left of the ghost bar.")
    make_numbered(doc,"Tasks behind baseline: current bar is to the right of the ghost bar (schedule slippage).")
    add_page_break(doc)


def ch_scheduler(doc):
    make_heading(doc,"Chapter 6 — Weekly Scheduler & Conflict Resolution",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Weekly Scheduler shows you exactly how much work is assigned to each team member "
        "each week — and alerts you immediately when someone is over-allocated.",space_after=8)
    add_screenshot(doc,"04_weekly_scheduler",
        "Figure 6.1 — The Weekly Scheduler heatmap showing member allocations, over-allocation (red), and the Copilot panel.")

    make_heading(doc,"6.1  Reading the Resource Heatmap",level=2,color=CLR_ACCENT)
    make_body(doc,"Each row is a team member. Each column is a week. Each cell shows:",space_after=4)
    make_bullet(doc,"Allocated hours / Available capacity (e.g., 38h / 40h).")
    make_bullet(doc,"Green cells: Allocation is within capacity. No action needed.")
    make_bullet(doc,"Red cells: Over-allocation. More hours assigned than the member can work that week.")
    make_bullet(doc,"Grey cells: The member is on leave. No capacity available that week.")
    doc.add_paragraph()

    make_heading(doc,"6.2  Resolving Conflicts Manually",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click on a red (over-allocated) cell to see which tasks are causing the conflict.")
    make_numbered(doc,"A panel appears listing all tasks assigned to that member in that week.")
    make_numbered(doc,"Click any task to open it in the Delivery Matrix inline editor.")
    make_numbered(doc,"Adjust the task dates, reassign to another team member, or reduce estimated effort.")
    make_numbered(doc,"The heatmap refreshes automatically to reflect your changes.")
    doc.add_paragraph()

    make_heading(doc,"6.3  Using the Copilot — Automated Conflict Resolution",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The Copilot can automatically resolve all resource conflicts in one click. "
        "It works safely in Sandbox mode so you can review the changes before committing them.",space_after=4)
    make_numbered(doc,"Click 'Enable Sandbox' at the top of the Scheduler.")
    make_numbered(doc,"Click 'Open Copilot Cockpit'. The diagnostics panel shows all detected conflicts.")
    make_numbered(doc,"Review the list of conflicts: over-allocations, dependency violations, unassigned tasks.")
    make_numbered(doc,"Click 'Resolve All Conflicts'. The Copilot analyses each conflict and applies one of three fixes:")
    make_bullet(doc,"Auto-Sequence: Pushes conflicting tasks end-to-end so dependencies are not violated.",level=1)
    make_bullet(doc,"Smart Reassign: Moves a task to a role-matched team member with spare capacity.",level=1)
    make_bullet(doc,"Cascade Date Shift: Adjusts all downstream dependent tasks to maintain schedule coherence.",level=1)
    make_numbered(doc,"Review the 'Proposed Changes' summary in the Copilot panel.")
    make_numbered(doc,"Click 'Commit' to apply changes to your live schedule, or 'Discard' to cancel.")
    doc.add_paragraph()
    add_callout(doc,
        "The Copilot is designed to make smart, conservative choices. "
        "It will never reassign a task to a member with a different role, "
        "and it always preserves task durations when shifting dates.",style="rule")

    add_page_break(doc)


def ch_raid(doc):
    make_heading(doc,"Chapter 7 — RAID Register",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The RAID Register is your project's formal risk and issue management system. "
        "Use it to track all Risks, Assumptions, Issues, and Dependencies throughout the project lifecycle.",
        space_after=8)
    add_screenshot(doc,"05_raid_register",
        "Figure 7.1 — The RAID Register showing the risk exposure matrix and the item list.")

    make_heading(doc,"7.1  Logging a New RAID Item",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Navigate to the RAID Register module.")
    make_numbered(doc,"Click '+ Add Item'.")
    make_numbered(doc,"The RAID logging flyout panel appears, allowing comprehensive details to be set.")
    make_numbered(doc,"Select the Type: Risk / Assumption / Issue / Dependency.")
    make_numbered(doc,"Enter a clear, specific title (e.g., 'Key backend developer may leave before Phase 2 completion').")
    make_numbered(doc,"Fill in Description, Impact, Probability (for Risks), and Severity.")
    make_numbered(doc,"Assign an Owner from the team member list.")
    make_numbered(doc,"Enter a Mitigation Strategy and a Target Closure Date.")
    make_numbered(doc,"Click Save. The Exposure Score is calculated automatically.")
    add_screenshot(doc,"13_add_raid_flyout",
        "Figure 7.2 — Logging/Editing a RAID item with mitigation strategy, owner select, and auto-exposure calculation.")
    doc.add_paragraph()

    make_heading(doc,"7.2  Understanding the Exposure Score",level=2,color=CLR_ACCENT)
    make_body(doc,"Exposure Score = Probability x Impact. Both use a 1-3 scale:",space_after=4)
    add_data_table(doc,
        ["Score","Label","Recommended Action"],
        [
            ["7-9", "Critical (Red)",  "Immediate action required. Escalate to project sponsor. Report weekly."],
            ["4-6", "Medium (Amber)", "Active monitoring required. Mitigation plan must be agreed within 5 days."],
            ["1-3", "Low (Green)",    "Log and review bi-weekly. No immediate action unless score increases."],
        ],
        col_widths=[0.8,1.8,4.0],
    )

    make_heading(doc,"7.3  Managing Item Lifecycle",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Each RAID item has a status that reflects where it is in the management lifecycle:",space_after=4)
    make_bullet(doc,"Identified: Newly logged. Awaiting owner assignment and mitigation planning.")
    make_bullet(doc,"Active: Owner assigned. Mitigation in progress. Monitored weekly.")
    make_bullet(doc,"Mitigated: Mitigation actions completed. Monitoring for recurrence over 2 weeks.")
    make_bullet(doc,"Realized (Risks only): The risk event occurred. Item should be converted to an Issue.")
    make_bullet(doc,"Closed: Item fully resolved. Archived for reporting purposes.")

    make_heading(doc, "7.4  Field Reference: RAID Item Business Object", level=2, color=CLR_ACCENT)
    make_body(doc,
        "This section defines the data fields that govern RAID register entries. "
        "RAID items dictate project threat metrics and impact the overall Health Index.", space_after=6)
    
    add_data_table(doc,
        ["Field Name", "Type / Format", "UI Required?", "Validation / Allowed Values", "Description / Cross-Module Effect"],
        [
            ["Type", "String (Enum)", "Yes", "Risk / Assumption / Issue / Dependency.", "Entity class. Risks compute exposure; Issues track active blocks."],
            ["Title", "String", "Yes", "Non-empty. Max 100 chars.", "Short descriptive title shown in lists and executive widgets."],
            ["Description", "String", "Yes", "Free text description.", "Detailed background of the threat, assumption, or blocker."],
            ["Status", "String (Enum)", "Yes", "Identified / Active / Mitigated / Closed / Realized.", "Active items require Owner. Reaching Realized converts Risks to Issues."],
            ["Impact", "String (Enum)", "Yes", "High (3) / Medium (2) / Low (1).", "Severity multiplier. Used in Risk Exposure calculations."],
            ["Probability", "String (Enum)", "Yes (Risks)", "High (3) / Medium (2) / Low (1).", "Probability multiplier (Risks only). Multiplied by impact for Exposure."],
            ["Exposure Score", "Number", "No", "Calculated: 1 to 9.", "Risk priority. Probability x Impact. Scores >= 7 flag red alerts."],
            ["Owner", "String", "Yes (Active)", "Member name.", "Responsible person for mitigation. Must match active team members."],
            ["Mitigation", "String", "Yes (Active)", "Free text.", "Mitigation plan or resolution step to manage or close the item."],
            ["Target Date", "Date (YYYY-MM-DD)", "Yes (Active)", "Must be future date.", "Committed resolution date. Overdue targets trigger warning alerts."],
            ["Raised Date", "Date (YYYY-MM-DD)", "Yes", "Defaults to today.", "Date logged. Tracks aging of RAID risks and issues."]
        ],
        col_widths=[1.1, 1.1, 0.8, 1.5, 2.2]
    )
    add_page_break(doc)


def ch_team(doc):
    make_heading(doc,"Chapter 8 — Team Capacity Hub",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Team Capacity Hub is where you manage your team — adding members, "
        "setting their work capacity, and recording planned leave.",space_after=8)
    add_screenshot(doc,"06_team_capacity_hub",
        "Figure 8.1 — The Team Capacity Hub showing member cards, utilisation bars, and the add member form.")

    make_heading(doc,"8.1  Adding a Team Member",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click '+ Add Member' in the Team Capacity Hub.")
    make_numbered(doc,"Enter the member's full name, role (e.g., Backend Developer, QA Engineer), and current status (Active).")
    make_numbered(doc,"Set their Weekly Hour Cap (default: 40 hours) and Utilisation Rate (1.0 = full time, 0.5 = part time).")
    make_numbered(doc,"Click Save. The member now appears in all assignee dropdowns and the Scheduler heatmap.")
    add_screenshot(doc,"14_add_member_flyout",
        "Figure 8.2 — Add/Edit Team Member form showing capacity hour caps, utilization rates, and planned leaves scheduler.")
    doc.add_paragraph()

    make_heading(doc,"8.2  Recording Planned Leave",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click on a team member's card to open their profile.")
    make_numbered(doc,"Click '+ Add Leave' in the Leave Calendar section.")
    make_numbered(doc,"Select the leave start date and end date.")
    make_numbered(doc,"Click Save. The Scheduler will show the member's cells for that period as 'On Leave' (grey, zero capacity).")
    doc.add_paragraph()

    make_heading(doc,"8.3  Member Status Management",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Updating a member's status affects their availability across all scheduling calculations:",space_after=4)
    make_bullet(doc,"Active: Normal capacity available. Can be assigned to tasks.")
    make_bullet(doc,"On Leave: Zero capacity for leave period. Scheduler shows grey cells.")
    make_bullet(doc,"Other Assignment: Temporarily excluded from capacity. Existing task assignments remain.")
    make_bullet(doc,"Serving Notice Period: Cannot be assigned to new tasks. Copilot will not reassign work to them.")
    make_bullet(doc,"Departed: Fully removed from capacity calculations. Existing assignments remain for record.")

    make_heading(doc, "8.4  Field Reference: Team Member Business Object", level=2, color=CLR_ACCENT)
    make_body(doc,
        "This section documents the configuration fields for team members. "
        "Member capacity settings directly drive the resource Scheduler heatmap.", space_after=6)
    
    add_data_table(doc,
        ["Field Name", "Type / Format", "UI Required?", "Validation / Allowed Values", "Description / Cross-Module Effect"],
        [
            ["Full Name", "String", "Yes", "Unique name.", "Identifier. Used in all assignee selectors and scheduler rows."],
            ["Role", "String (Enum)", "Yes", "Active roles list.", "Specialty (e.g. QA, Dev). Copilot limits reassignments to matched roles."],
            ["Status", "String (Enum)", "Yes", "Active / On Leave / notice / notice notice / Departed.", "Availability state. Non-Active status removes them from allocation pools."],
            ["Weekly Hour Cap", "Number", "Yes", ">= 0. Defaults to 40.", "Standard weekly work capacity limit. Red flags appear if exceeded."],
            ["Utilisation Rate", "Number", "Yes", "0.0 to 1.0. Default 1.0.", "Fractions (e.g. 0.5 for part-time). Multiplies hour cap for net capacity."],
            ["Planned Leaves", "Date Ranges", "No", "Pairs of {start, end}.", "Planned vacation blocks. Sets capacity to zero for those calendar weeks."]
        ],
        col_widths=[1.1, 1.1, 0.8, 1.5, 2.2]
    )
    add_page_break(doc)


def ch_defects(doc):
    make_heading(doc,"Chapter 9 — Defect Tracker",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Defect Tracker manages all software defects from initial discovery "
        "through resolution and closure. Use it to ensure all bugs are tracked, "
        "assigned, and resolved within agreed SLA timeframes.",space_after=8)
    add_screenshot(doc,"07_defect_tracker",
        "Figure 9.1 — The Defect Tracker showing severity summary cards, the defect register, and the log defect form.")

    make_heading(doc,"9.1  Logging a Defect",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click '+ Log Defect' in the Defect Tracker.")
    make_numbered(doc,"Enter a clear, descriptive title (e.g., 'Gantt timeline fails to load with 200+ tasks').")
    make_numbered(doc,"Select the Defect Type: Functional Bug / UI-UX Issue / Performance / Security / Data Issue / Suggestion.")
    make_numbered(doc,"Select Severity: S1 Blocker / S2 High / S3 Medium / S4 Low. This affects the Health Index and SLA timer.")
    make_numbered(doc,"Select Priority: Critical / High / Medium / Low.")
    make_numbered(doc,"Link to a Task: select the task or subtask the defect was found in.")
    make_numbered(doc,"Enter detailed Reproduction Steps so the developer can replicate the bug.")
    make_numbered(doc,"Click Save.")
    add_screenshot(doc,"12_add_defect_flyout",
        "Figure 9.2 — Log Defect form linking the bug to a parent task, specifying severity, and listing reproduction steps.")
    doc.add_paragraph()
    add_callout(doc,
        "S1 Blocker defects trigger an immediate red alert banner on the Overview Dashboard "
        "and a 24-hour SLA countdown. Assign an S1 immediately after logging.",style="caution")

    make_heading(doc,"9.2  Managing the Defect Lifecycle",level=2,color=CLR_ACCENT)
    make_body(doc,"Move defects through their lifecycle using the Status dropdown:",space_after=4)
    make_bullet(doc,"New -> Assigned: Engineering Manager assigns a developer.")
    make_bullet(doc,"Assigned -> Fixed: Developer resolves the bug and logs fix details.")
    make_bullet(doc,"Fixed -> Retest: QA is notified and retests the fix in the test environment.")
    make_bullet(doc,"Retest -> Closed: QA confirms the fix is correct. Defect removed from Health Index.")
    make_bullet(doc,"Retest -> Assigned (re-open): QA finds the fix incomplete. Developer is reassigned.")
    make_bullet(doc,"Any -> Rejected: Defect is by design or cannot be reproduced. Requires a rejection reason.")

    make_heading(doc, "9.3  Field Reference: Defect Business Object", level=2, color=CLR_ACCENT)
    make_body(doc,
        "This section details defect fields. Defect tracking is tightly linked to "
        "task deliverables and heavily impacts the quality rating of product modules.", space_after=6)
    
    add_data_table(doc,
        ["Field Name", "Type / Format", "UI Required?", "Validation / Allowed Values", "Description / Cross-Module Effect"],
        [
            ["Defect Title", "String", "Yes", "Non-empty.", "Title detailing the failure (e.g., 'Chart axis overflow')."],
            ["Type", "String (Enum)", "Yes", "Bug / UI-UX / Perf / Sec / Data.", "Defect type classification for metrics donut charts."],
            ["Severity", "String (Enum)", "Yes", "S1 Blocker / S2 High / S3 Med / S4 Low.", "Severity grading. S1 blocker triggers immediate Dashboard red banner."],
            ["Priority", "String (Enum)", "Yes", "Critical / High / Medium / Low.", "Resolution urgency. Dictates SLA timers for developers."],
            ["Status", "String (Enum)", "Yes", "New / Assigned / Fixed / Retest / Closed / Rejected / Deferred.", "Bug state. Re-opening triggers transition back to Assigned."],
            ["Linked Task ID", "String", "No", "Valid TASK-NNN or ST-NNN.", "Prerequisite task. Attributes bugs directly to code modules in matrix."],
            ["Assignee", "String", "No", "Active developer.", "Assigned developer. Must have development roles to receive assignments."],
            ["Reproduction Steps", "String", "Yes", "Detailed text.", "Step-by-step description to reproduce defect. Required to start work."]
        ],
        col_widths=[1.1, 1.1, 0.8, 1.5, 2.2]
    )
    add_page_break(doc)


def ch_reports(doc):
    make_heading(doc,"Chapter 10 — Reports & Board Packs",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Reports module lets you generate professional stakeholder deliverables "
        "in one click — an Executive Board Pack for leadership, "
        "and a comprehensive Excel workbook for detailed project records.",space_after=8)
    add_screenshot(doc,"08_reports_boardpack",
        "Figure 10.1 — The Reports module with export options, workbook sheet map, and Board Pack preview.")

    make_heading(doc,"10.1  Generating the Executive Board Pack",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Navigate to the Reports module.")
    make_numbered(doc,"Click 'Generate Board Pack'.")
    make_numbered(doc,"The Board Pack is assembled automatically from live project data and displayed in the preview panel.")
    make_numbered(doc,"Review the Board Pack contents: Project Summary, Health Trend, Critical Path, Top Risks, and Team Velocity.")
    make_numbered(doc,"Click 'Print' to send to a printer or 'Save as PDF' to generate a PDF file.")
    doc.add_paragraph()


    make_heading(doc,"10.2  Exporting to Excel",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Click 'Export to Excel' in the Reports module.")
    make_numbered(doc,"A file download is triggered. Save the file to your preferred location.")
    make_numbered(doc,"The Excel workbook contains 8 sheets: System State, Tasks, Team, RAID Register, Defects, Activity Log, Baselines, and Releases.")
    make_numbered(doc,"Each sheet uses colour-coded cells: Green = complete/healthy, Yellow = in progress, Red = blocked/overdue, Grey = cancelled.")
    doc.add_paragraph()
    add_callout(doc,
        "The Excel workbook is a live snapshot of your project data at the moment of export. "
        "For an up-to-date workbook, always export immediately before sharing with stakeholders.",style="note")
    add_page_break(doc)


def ch_audit(doc):
    make_heading(doc,"Chapter 11 — Audit Log",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Audit Log maintains a complete, immutable record of every change made to your project. "
        "Use it to investigate unexpected changes, track accountability, or roll back to a prior state.",
        space_after=8)
    add_screenshot(doc,"09_activity_audit_log",
        "Figure 11.1 — The Audit Log showing the chronological activity stream with timestamps and change details.")

    make_heading(doc,"11.1  Reading the Audit Log",level=2,color=CLR_ACCENT)
    make_body(doc,"Each entry in the Audit Log shows:",space_after=4)
    make_bullet(doc,"Timestamp: Exact date and time of the change.")
    make_bullet(doc,"User: The team member who made the change (set via the active user indicator in the top bar).")
    make_bullet(doc,"Action: Created / Updated / Status Changed / Deleted.")
    make_bullet(doc,"Entity: The task, defect, RAID item, or member that was changed.")
    make_bullet(doc,"Change Details: Old value -> New value (e.g., 'Status: In Progress -> Under Review').")
    doc.add_paragraph()

    make_heading(doc,"11.2  Reviewing & Reconstructing State",level=2,color=CLR_ACCENT)
    make_body(doc,
        "If an incorrect change was made or a task was accidentally deleted, the detailed "
        "diff payload in the Audit Log can be used to manually reconstruct the prior state:",space_after=4)
    make_numbered(doc,"Locate the log entry in the Audit Log representing the incorrect modification or deletion.")
    make_numbered(doc,"View the details of the change to identify the 'Old Value' of the updated fields.")
    make_numbered(doc,"Open the target view (e.g., Delivery Matrix or RAID Register) and edit the fields back to their original values.")
    doc.add_paragraph()
    add_callout(doc,
        "For project-wide rollbacks, you can also use captured baseline snapshots (Settings -> Schedule Baselines) "
        "or restore database backups (Settings -> Data Recovery / Backups) to revert to previous saved states.",style="tip")
    add_page_break(doc)


def ch_config(doc):
    make_heading(doc,"Chapter 12 — System Configuration",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Settings panel (gear icon in the navigation bar) lets you customise "
        "ProjectPulse to match your project's terminology, working calendar, and visual style.",
        space_after=8)
    add_screenshot(doc,"10_configuration_settings",
        "Figure 12.1 — The Settings panel showing General Settings, Dropdown Manager, and Theme Selector.")

    make_heading(doc,"12.1  Configuring the Working Calendar",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Navigate to Settings -> General.")
    make_numbered(doc,"Set Hours Per Day (default: 8) — how many work hours constitute a working day.")
    make_numbered(doc,"Set Days Per Week (default: 5) — your team's standard working week length.")
    make_numbered(doc,"Toggle specific days on/off under 'Working Days' to mark non-working days.")
    make_numbered(doc,"Set your preferred Effort Unit: hours (hrs), days, or months.")
    make_numbered(doc,"Click Save. All effort displays and capacity calculations update immediately.")
    doc.add_paragraph()

    make_heading(doc,"12.2  Customising Dropdowns",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Navigate to Settings -> Dropdown Manager.")
    make_numbered(doc,"Select the dropdown you want to customise (e.g., Module, Category, Role).")
    make_numbered(doc,"Click '+ Add Option' to add a new value.")
    make_numbered(doc,"Drag items to reorder them. Click 'Edit' to rename. Click the trash icon to remove.")
    make_numbered(doc,"Click Save. New options appear immediately in all relevant selects.")
    doc.add_paragraph()

    make_heading(doc,"12.3  Changing the Visual Theme",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Navigate to Settings -> Appearance.")
    make_numbered(doc,"Browse the 20 available themes in the theme gallery.")
    make_numbered(doc,"Click any theme to preview it instantly.")
    make_numbered(doc,"Toggle 'Force Dark Mode' or 'Force Light Mode' to override the theme's default mode.")
    make_numbered(doc,"Theme selection is saved automatically.")
    doc.add_paragraph()

    make_heading(doc,"12.4  Managing Schedule Baselines",level=2,color=CLR_ACCENT)
    make_numbered(doc,"Navigate to Settings -> Schedule Baselines.")
    make_numbered(doc,"Click 'Capture Current Snapshot'. Enter a name (e.g., 'Phase 1 Kickoff') and description.")
    make_numbered(doc,"Click Save. The snapshot records all task planned dates and effort values at this moment.")
    make_numbered(doc,"To view baseline overlay on the Gantt, enable 'Show Baseline' in the Gantt toolbar.")
    make_numbered(doc,"To restore a historical baseline: click Restore next to the snapshot. Confirm the dialog.")
    add_callout(doc,
        "Best practice: Capture a baseline at project kickoff and again at each major phase gate or re-scope. "
        "This gives you a clear record of schedule evolution over the project lifetime.",style="tip")

    add_page_break(doc)


def ch_tips(doc):
    make_heading(doc,"Chapter 13 — Tips, Best Practices & Troubleshooting",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")

    make_heading(doc,"13.1  Daily Recommended Workflow",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Time","Action","Module"],
        [
            ["Morning Stand-up",  "Check Health Index and KPI cards. Review overdue tasks and blocked items.",  "Overview Dashboard"],
            ["Task Updates",      "Update task statuses and log actual effort.",                                "Delivery Matrix"],
            ["Scheduler Check",   "Scan the heatmap for new over-allocations introduced by date changes.",     "Weekly Scheduler"],
            ["RAID Review",       "Update RAID item statuses. Log any new risks or issues.",                   "RAID Register"],
            ["Weekly (Friday)",   "Capture a baseline snapshot. Generate and review the Board Pack.",          "Settings / Reports"],
        ],
        col_widths=[1.8,3.2,1.8],
    )

    make_heading(doc,"13.2  Pro Tips",level=2,color=CLR_ACCENT)
    make_bullet(doc,"Ctrl+S: Save your project immediately at any time without waiting for the 10-second auto-save.")
    make_bullet(doc,"Ctrl+F: Jump directly to the search bar in the Delivery Matrix or Defect Tracker.")
    make_bullet(doc,"Tab navigation: Use Tab and Shift+Tab to move between cells in the Delivery Matrix.")
    make_bullet(doc,"Bulk status update: Ctrl+Click multiple tasks, then right-click to bulk-change status.")
    make_bullet(doc,"Export before major changes: Always export to Excel before a baseline restore or backups restore.")
    doc.add_paragraph()

    make_heading(doc,"13.3  Troubleshooting Common Issues",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Symptom","Likely Cause","Resolution"],
        [
            ["Data disappeared after page refresh",
             "localStorage was cleared by browser privacy settings.",
             "Export to Excel regularly. Enable File Sync in Settings to maintain a file backup."],
            ["Gantt bars not visible",
             "Tasks have no start/due dates set, or all dates are outside the current view window.",
             "Ensure tasks have start and due dates. Click 'Today' to re-centre the Gantt view."],
            ["Health Index stays at 0",
             "All tasks are Completed or Cancelled (no active tasks for denominator).",
             "Expected behaviour for completed projects. Add new tasks to reset the denominator."],
            ["Copilot greyed out",
             "Sandbox mode is not enabled.",
             "Click 'Enable Sandbox' before opening the Copilot Cockpit."],
            ["EVM metrics show '--'",
             "No tasks have been completed yet (EV = 0).",
             "EVM metrics calculate once at least one task is marked Completed."],
            ["Member not appearing in Scheduler",
             "Member status is not 'Active'.",
             "Navigate to Team Capacity Hub and set the member's status to Active."],
        ],
        col_widths=[1.8,2.0,2.8],
    )

def ch_widgets_glossary(doc):
    make_heading(doc,"Chapter 14 — Complete Widget Directory & Glossary",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "ProjectPulse uses a highly modular component architecture across its interactive views. "
        "This chapter lists every widget available in the Dashboard and Report Builder layouts, "
        "explaining their indicators, calculation mechanisms, and target audiences.",space_after=8)

    make_heading(doc,"14.1  Global Widget Directory Matrix",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Widget ID", "Human-Readable Name", "Target View(s)", "Type", "Core Data Source"],
        [
            ["summary", "Executive Summary", "Dashboard / Report", "Metrics Cards", "Task status, RAID count"],
            ["health", "Project Health & Quality", "Dashboard / Report", "Charts", "Active vs overdue tasks"],
            ["mgmt_insights", "Management Insights", "Dashboard", "Multi-Card", "Pacing, risks, workloads"],
            ["exec_reporting", "Executive Reporting", "Dashboard", "Multi-Card", "Milestones & critical items"],
            ["exec_capacity", "Team Capacity Allocation", "Dashboard / Report", "Grid / Heatmap", "Member weekly caps"],
            ["module_matrix", "Strategic Module Status", "Dashboard / Report", "Matrix Grid", "Task counts per module"],
            ["module_health", "Module & Release Health", "Dashboard / Report", "Table", "Bugs & defects by module"],
            ["feature_insights", "Feature Intelligence", "Dashboard / Report", "Bento Grid", "Feature matrix progress"],
            ["screen_status", "Screen Status Details", "Dashboard / Report", "Table", "GUI Screen completions"],
            ["release_timeline", "Release Timeline", "Dashboard / Report", "Visual Chart", "Version releases"],
            ["milestone_timeline", "Milestone Timeline", "Dashboard / Report", "Visual List", "Milestone tasks"],
            ["burndown", "Burndown Chart", "Dashboard / Report", "SVG Chart", "Task baseline vs actuals"],
            ["velocity", "Weekly Velocity", "Dashboard / Report", "Bar Chart", "Weekly completed effort"],
            ["cfd", "Cumulative Flow", "Dashboard / Report", "Area Chart", "Task status transition log"],
            ["overdue", "Overdue Attention", "Dashboard / Report", "List", "Overdue tasks list"],
            ["high_impact_entities", "High Impact Entities", "Dashboard", "Bubble Heatmap", "Force-directed bubble risk visualization"],
            ["workload", "Team Workload", "Dashboard / Report", "Bar Chart", "Assigned task effort"],
            ["cat_hours", "Category & Effort", "Dashboard / Report", "Donut Chart", "Task category distribution"],
            ["defect_intel", "Defect Intelligence", "Dashboard / Report", "Bento Statistics", "Defects registry log"],
            ["intelligence", "Predictive Intelligence", "Dashboard / Report", "ML Forecast", "EVM velocity projection"],
            ["analytics", "Advanced Analytics", "Dashboard / Report", "Metric Grid", "EVM variables"],
            ["activity", "Recent Activity / Audit", "Dashboard / Report", "Activity Stream", "System audit log trail"],
            ["kpi_summary", "Executive Metrics", "Report Only", "Text Cards", "Key status summaries"],
            ["activities", "Key Activities", "Report Only", "Editable List", "User text entry"],
            ["achievements", "Achievements", "Report Only", "Highlights Card", "User text entry"],
            ["risks", "Risks & Issues", "Report Only", "Table", "Active RAID registers"],
            ["plans", "Upcoming Plans", "Report Only", "Text Block", "User sprint plans"],
            ["team", "Team Workload Table", "Report Only", "Data Table", "Team allocations log"],
            ["util", "Resource Utilization Summary", "Report Only", "Metrics Cards", "Team capacity percentages"],
            ["overdue_tbl", "Overdue Table Detail", "Report Only", "Detailed Table", "Task delay register"]
        ],
        col_widths=[1.3, 1.8, 1.4, 0.9, 1.6]
    )

    doc.add_paragraph()

    make_heading(doc,"14.2  Detailed Widget Descriptions & Usage Instructions",level=2,color=CLR_ACCENT)

    # 1. summary
    make_heading(doc,"14.2.1  Executive Summary (summary)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: The flagship dashboard widget combining the Health Index gauge with three KPI metrics cards.\n"
        "• Interpretation: The radial gauge arc transitions from Green (80-100: healthy) to Amber (50-79: warning) to Red (0-49: critical). "
        "It evaluates delivery confidence, Schedule Performance Index (SPI), and active RAID issues.\n"
        "• How to Use: Leadership uses this widget at startup to determine if a project requires recovery planning.",space_after=4)
    add_screenshot(doc, "widgets/summary", "Figure 14.1 — Executive Summary Widget (summary)", width_inches=5.5)

    # 2. health
    make_heading(doc,"14.2.2  Project Health & Quality (health)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Two high-fidelity charts breaking down active project tasks by priority level and execution status.\n"
        "• Interpretation: Displays status splits (Not Started, In Progress, QA, Completed) in a stacked bar chart. "
        "A separate donut chart maps tasks by priority (Critical, High, Medium, Low).\n"
        "• How to Use: Project managers use this to check task distributions and ensure there isn't a bottleneck in the QA state.",space_after=4)
    add_screenshot(doc, "widgets/health", "Figure 14.2 — Project Health & Quality Widget (health)", width_inches=5.5)

    # 3. mgmt_insights
    make_heading(doc,"14.2.3  Management Insights (mgmt_insights)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: A compound widget surfacing schedule pacing, high-priority risks, workload thresholds, and developer friction.\n"
        "• Interpretation: Flags tasks due within immediate (7d), mid-term (14d), and long-term (30d) horizons. Highlight cells turn red when overdue volume accumulates.\n"
        "• How to Use: Scrum masters check this daily to align task workloads with sprint capacity.",space_after=4)
    add_screenshot(doc, "widgets/mgmt_insights", "Figure 14.3 — Management Insights Widget (mgmt_insights)", width_inches=5.5)

    # 4. exec_reporting
    make_heading(doc,"14.2.4  Executive Reporting (exec_reporting)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: High-density card presentation summarizing milestone achievements, critical path milestones, and RAID exposure levels.\n"
        "• Interpretation: Formatted with large text metrics and badge indicators, omitting technical logs for presentation cleanliness.\n"
        "• How to Use: Use this view to capture quick status screenshots for monthly steering committee slides.",space_after=4)
    add_screenshot(doc, "widgets/exec_reporting", "Figure 14.4 — Executive Reporting Widget (exec_reporting)", width_inches=5.5)

    # 5. exec_capacity
    make_heading(doc,"14.2.5  Team Capacity Allocation (exec_capacity)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Discloses planned working hours mapped against role capabilities.\n"
        "• Interpretation: Shows grid items per role (e.g. Lead Frontend) with a horizontal bar highlighting planned effort vs capacity.\n"
        "• How to Use: Use this to detect capacity shortfalls. If QA capacity is exceeded, adjust incoming feature scopes.",space_after=4)
    add_screenshot(doc, "widgets/exec_capacity", "Figure 14.5 — Team Capacity Allocation Widget (exec_capacity)", width_inches=5.5)

    # 6. module_matrix
    make_heading(doc,"14.2.6  Strategic Module Status Matrix (module_matrix)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Grid mapping code modules against development statuses.\n"
        "• Interpretation: Intersecting cells contain task counts. Features a progress bar reflecting completed vs total tasks per module.\n"
        "• How to Use: Evaluates module maturity. Ensure gateway or authentication modules are completed before starting GUI components.",space_after=4)
    add_screenshot(doc, "widgets/module_matrix", "Figure 14.6 — Strategic Module Status Matrix Widget (module_matrix)", width_inches=5.5)

    # 7. module_health
    make_heading(doc,"14.2.7  Module & Release Health (module_health)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Quality index chart correlating active defects against code modules.\n"
        "• Interpretation: Assigns a health grade (A to F) to modules based on S1-S4 defect densities.\n"
        "• How to Use: Engineering managers check this to schedule technical debt refactoring sprints on modules with D/F grades.",space_after=4)
    add_screenshot(doc, "widgets/module_health", "Figure 14.7 — Module & Release Health Widget (module_health)", width_inches=5.5)

    # 8. feature_insights
    make_heading(doc,"14.2.8  Feature Intelligence (feature_insights)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Bento grid showing delivery progress of functional user features.\n"
        "• Interpretation: Shows completion percentages, feature complexity scores, and associated risks.\n"
        "• How to Use: Product Owners use this to report feature release readiness to marketing stakeholders.",space_after=4)
    add_screenshot(doc, "widgets/feature_insights", "Figure 14.8 — Feature Intelligence Widget (feature_insights)", width_inches=5.5)

    # 9. screen_status
    make_heading(doc,"14.2.9  Screen Status Details (screen_status)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Detailed tracker logging progress of frontend UI screens.\n"
        "• Interpretation: Grid lists screen names, linked module, and current design/development states.\n"
        "• How to Use: UI/UX designers check this to coordinate screen sign-offs with developers.",space_after=4)
    add_screenshot(doc, "widgets/screen_status", "Figure 14.9 — Screen Status Details Widget (screen_status)", width_inches=5.5)

    # 10. release_timeline
    make_heading(doc,"14.2.10  Release Timeline (release_timeline)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Visual roadmap showing target dates and completion status of version releases.\n"
        "• Interpretation: Chronological timeline bar showing milestones (e.g. v1.0.0, v1.1.0) and status badges (Released, In Progress).\n"
        "• How to Use: Release managers use this to coordinate deployment windows and release notes.",space_after=4)
    add_screenshot(doc, "widgets/release_timeline", "Figure 14.10 — Release Timeline Widget (release_timeline)", width_inches=5.5)

    # 11. milestone_timeline
    make_heading(doc,"14.2.11  Milestone Timeline (milestone_timeline)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: List tracking critical milestone deliverables.\n"
        "• Interpretation: Maps target dates against milestone completions. Completed milestones show green indicators.\n"
        "• How to Use: Program coordinators review this weekly to verify key phase gate completions.",space_after=4)
    add_screenshot(doc, "widgets/milestone_timeline", "Figure 14.11 — Milestone Timeline Widget (milestone_timeline)", width_inches=5.5)

    # 12. burndown
    make_heading(doc,"14.2.12  Burndown Chart (burndown)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: SVG chart plotting total scope baseline against actual task completions.\n"
        "• Interpretation: X-axis represents weeks; Y-axis shows effort hours. The projection line forecast final dates.\n"
        "• How to Use: PMs use the burn-down projection to detect early signs of schedule slippage.",space_after=4)
    add_screenshot(doc, "widgets/burndown", "Figure 14.12 — Burndown Chart Widget (burndown)", width_inches=5.5)

    # 13. velocity
    make_heading(doc,"14.2.13  Weekly Velocity (velocity)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Bar chart tracking effort completed week-over-week.\n"
        "• Interpretation: Each bar represents a week's total completed effort. Steady height shows stable throughput.\n"
        "• How to Use: PMs use average velocity to estimate capacity for future planning cycles.",space_after=4)
    add_screenshot(doc, "widgets/velocity", "Figure 14.13 — Weekly Velocity Widget (velocity)", width_inches=5.5)

    # 14. cfd
    make_heading(doc,"14.2.14  Cumulative Flow Diagram (cfd)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Multi-mode stacked area chart showing work items across lifecycle status stages over time.\n"
        "• Controls & Customization: Features a Mode Selector dropdown (Count vs Effort (Days)), a Sub-tasks level checkbox toggle (evaluating individual sub-tasks vs parent task items), and a timeframe selector (8 to 100 weeks).\n"
        "• Interpretation: Band heights display item counts or effort in Not Started, In Progress, On Hold, Under Review, and Completed. Bulging bands indicate process bottlenecks.\n"
        "• How to Use: Identifies bottleneck areas and flow health. Toggle between Count and Effort (Days) or enable Sub-tasks mode for granular status lifecycle tracking.",space_after=4)
    add_screenshot(doc, "widgets/cfd", "Figure 14.14 — Cumulative Flow Diagram Widget (cfd)", width_inches=5.5)

    # 15. overdue
    make_heading(doc,"14.2.15  Overdue Attention (overdue)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: List of tasks that have missed their due dates.\n"
        "• Interpretation: Displays task ID, name, assignee, and days overdue in red highlight.\n"
        "• How to Use: Team leads review this in stand-ups to assign help to delayed items.",space_after=4)
    add_screenshot(doc, "widgets/overdue", "Figure 14.15 — Overdue Attention Widget (overdue)", width_inches=5.5)

    # 16. high_impact_entities
    make_heading(doc,"14.2.16  High Impact Entities (high_impact_entities)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: An interactive Canvas-based force-directed bubble heatmap widget that visualizes project risk density and dependency gravity.\n"
        "• Interpretation: Bubble sizes correspond to the composite risk impact score of the entity (integrating delays, priority, blockers, defect counts, and progress). Bubble colors represent risk categories: Green for OK (Low Risk), Amber for Warning (Medium), and Red for Critical (High Risk). Hovering reveals detailed metadata tooltips, and clicking navigates directly to the target item.\n"
        "• How to Use: Managers and leads monitor bubble clusters and sizes to identify and resolve high-risk bottleneck nodes before they block downstream paths.",space_after=4)
    add_screenshot(doc, "widgets/high_impact_entities", "Figure 14.16 — High Impact Entities Widget (high_impact_entities)", width_inches=5.5)

    # 17. workload
    make_heading(doc,"14.2.17  Team Workload (workload)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Mapped chart showing workload hours assigned per team member.\n"
        "• Interpretation: Mapped against standard capacity limits (e.g. 40h). Highlights overallocated members.\n"
        "• How to Use: Balance assignments in scheduler to prevent burnout.",space_after=4)
    add_screenshot(doc, "widgets/workload", "Figure 14.17 — Team Workload Widget (workload)", width_inches=5.5)

    # 18. cat_hours
    make_heading(doc,"14.2.18  Category & Effort (cat_hours)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Donut chart showing effort hours distributed across task categories.\n"
        "• Interpretation: Segments show percentages spent on Feature, Bug, DevOps, Design, etc.\n"
        "• How to Use: Product Owners ensure focus aligns with goals, e.g., keeping bug effort below 20%.",space_after=4)
    add_screenshot(doc, "widgets/cat_hours", "Figure 14.18 — Category & Effort Widget (cat_hours)", width_inches=5.5)

    # 19. defect_intel
    make_heading(doc,"14.2.19  Defect Intelligence (defect_intel)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: High density bento statistics card focusing on defect status and density metrics.\n"
        "• Interpretation: Features counts of active S1-S4 bugs and resolution rates.\n"
        "• How to Use: QA leads check this before release to ensure no S1 blocker defects are open.",space_after=4)
    add_screenshot(doc, "widgets/defect_intel", "Figure 14.19 — Defect Intelligence Widget (defect_intel)", width_inches=5.5)

    # 20. intelligence
    make_heading(doc,"14.2.20  Predictive Intelligence (intelligence)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Forecast analytics widget displaying projected completion dates.\n"
        "• Interpretation: Evaluates actual effort velocities against baselines to predict delays.\n"
        "• How to Use: PMs use predictions for re-scoping before timelines are compromised.",space_after=4)
    add_screenshot(doc, "widgets/intelligence", "Figure 14.20 — Predictive Intelligence Widget (intelligence)", width_inches=5.5)

    # 21. analytics
    make_heading(doc,"14.2.21  Advanced Analytics (analytics)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: high-density table presenting Earned Value Management (EVM) values.\n"
        "• Interpretation: Tracks Earned Value (EV), Planned Value (PV), Schedule Variance (SV), and Schedule Performance Index (SPI).\n"
        "• How to Use: Finance and program managers review this for status reports.",space_after=4)
    add_screenshot(doc, "widgets/analytics", "Figure 14.21 — Advanced Analytics Widget (analytics)", width_inches=5.5)

    # 22. activity
    make_heading(doc,"14.2.22  Recent Activity (activity)",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Chronological audit trail showing system events.\n"
        "• Interpretation: Lists action events with timestamps and author details.\n"
        "• How to Use: Track accountability and audit changes in the workspace.",space_after=4)
    add_screenshot(doc, "widgets/activity", "Figure 14.22 — Recent Activity Widget (activity)", width_inches=5.5)

    # 23. kpi_summary
    make_heading(doc,"14.2.23  Executive Metrics (kpi_summary) [Report Only]",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Report card presenting key health indexes and delivery ratios.\n"
        "• Interpretation: Displays delivery confidence, SPI index, and RAID count in a structured print block.\n"
        "• How to Use: Pre-formatted block for steering committee reports.",space_after=4)
    add_screenshot(doc, "widgets/kpi_summary", "Figure 14.23 — Executive Metrics Widget (kpi_summary)", width_inches=5.5)

    # 24. activities
    make_heading(doc,"14.2.24  Key Activities (activities) [Report Only]",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Text-editable widget to log key activities.\n"
        "• Interpretation: Users type text summary bullet points directly into the PDF preview panel.\n"
        "• How to Use: PMs write comments to explain anomalies.",space_after=4)
    add_screenshot(doc, "widgets/activities", "Figure 14.24 — Key Activities Widget (activities)", width_inches=5.5)

    # 25. achievements
    make_heading(doc,"14.2.25  Achievements (achievements) [Report Only]",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Showcase widget to highlight successes.\n"
        "• Interpretation: Editable text list formatted for callouts.\n"
        "• How to Use: Highlight milestones met in the reporting period.",space_after=4)
    add_screenshot(doc, "widgets/achievements", "Figure 14.25 — Achievements Widget (achievements)", width_inches=5.5)

    # 26. risks
    make_heading(doc,"14.2.26  Risks & Issues (risks) [Report Only]",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Detailed RAID table for stakeholder reports.\n"
        "• Interpretation: Lists top active risks, mitigation plans, and owners.\n"
        "• How to Use: Simplifies presenting risk registers to stakeholders.",space_after=4)
    add_screenshot(doc, "widgets/risks", "Figure 14.26 — Risks & Issues Widget (risks)", width_inches=5.5)

    # 27. plans
    make_heading(doc,"14.2.27  Upcoming Plans (plans) [Report Only]",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Text-editable section for upcoming plans.\n"
        "• Interpretation: Formatted text block for future objectives.\n"
        "• How to Use: Outline plans for the next reporting period.",space_after=4)
    add_screenshot(doc, "widgets/plans", "Figure 14.27 — Upcoming Plans Widget (plans)", width_inches=5.5)

    # 28. team
    make_heading(doc,"14.2.28  Team Workload Table (team) [Report Only]",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Capacity overview table for reports.\n"
        "• Interpretation: Lists team member names, roles, and allocated hours.\n"
        "• How to Use: Verify workloads in stakeholder reports.",space_after=4)
    add_screenshot(doc, "widgets/team", "Figure 14.28 — Team Workload Table Widget (team)", width_inches=5.5)

    # 29. util
    make_heading(doc,"14.2.29  Resource Utilization Summary (util) [Report Only]",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: High-level utilization stats.\n"
        "• Interpretation: Displays utilization percentages per role.\n"
        "• How to Use: Report resource efficiency to stakeholders.",space_after=4)
    add_screenshot(doc, "widgets/util", "Figure 14.29 — Resource Utilization Summary Widget (util)", width_inches=5.5)

    # 30. overdue_tbl
    make_heading(doc,"14.2.30  Overdue Table Detail (overdue_tbl) [Report Only]",level=3,color=CLR_NAVY)
    make_body(doc,
        "• Description: Table of overdue tasks for reports.\n"
        "• Interpretation: Lists task name, assignee, and delay details.\n"
        "• How to Use: Highlight delayed tasks in stakeholder updates.",space_after=4)
    add_screenshot(doc, "widgets/overdue_tbl", "Figure 14.30 — Overdue Table Detail Widget (overdue_tbl)", width_inches=5.5)

    make_heading(doc,"14.3  Glossary of Terms",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Term","Definition"],
        [
            ["actCompletionDate","The actual date work was finished, used for retrospective activity attribution."],
            ["Baseline","A named, timestamped snapshot of planned task dates and efforts."],
            ["buildDashCache","The O(n) single-pass analytics aggregation function that populates P.cache."],
            ["Complexity Factor","A multiplier (0.5x / 1.0x / 1.5x) applied to task effort for velocity scoring."],
            ["Copilot","The automated conflict resolution engine in the Weekly Scheduler."],
            ["Delivery Confidence","The velocity-based probability of delivering all remaining work on schedule."],
            ["EVM","Earned Value Management — a PMI-standard project performance measurement framework."],
            ["Exposure Score","RAID risk score: probability_int x impact_int. Ranges 1-9."],
            ["Health Index","Composite project health score (0-100) derived from overdue tasks, risks, and defects."],
            ["localStorage","Browser-native key-value storage used to persist project data."],
            ["P","The global JavaScript state object containing all project data."],
            ["pp-data","The localStorage key under which the serialised P object is stored."],
            ["RAID","Risks, Assumptions, Issues, and Dependencies — the four governance entity types."],
            ["Sandbox","The non-destructive simulation environment for what-if scenario modelling."],
            ["SPI","Schedule Performance Index: EV / PV. < 1.0 = schedule slippage."],
            ["SV","Schedule Variance: EV - PV. Negative = behind schedule."],
            ["VALID_TRANSITIONS","The authoritative map of permitted task status transitions enforced by the state machine."],
            ["Velocity","Rolling 3-week average of completed complexity points per week."],
        ],
        col_widths=[2.0,4.4],
    )

    add_page_break(doc)


def ch_project_intelligence(doc):
    make_heading(doc,"Chapter 15 — Project Intelligence & Training Resources",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "To maximize efficiency and operational insight, ProjectPulse incorporates several high-level "
        "visual blueprints and training resources generated to support executive reviews and new team member onboarding.",space_after=8)

    make_heading(doc,"15.1  Interactive Workstation Blueprint",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The ProjectPulse workspace coordinates state change across a highly integrated set of "
        "interactive cards, tables, and analytics modules in the client-side UI, allowing users "
        "to manage all tasks and capacity from a single workstation interface.",space_after=8)

    make_heading(doc,"15.2  Software Delivery Ecosystem Mind Map",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The delivery ecosystem encompasses the relationships between the state machine variables "
        "(contained within the global P object) and active management modules. This structure helps "
        "developers and managers trace data propagation paths across the system.",space_after=8)

    make_heading(doc,"15.3  Stakeholder Training Slide Deck Outline",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The project file directory contains the official onboarding and presentation slide deck "
        "(ProjectPulse_Intelligence_Workstation.pptx). Below is the structured outline of the 15 presentation slides "
        "designed for team training:",space_after=6)

    add_data_table(doc,
        ["Slide","Title","Visual Concept & Presentation Key points"],
        [
            ["1","Executive Cover Slide","Title: ProjectPulse — Browser-Native Project Intelligence Workstation. Core theme: Serverless, Local-First, Zero-Backend operational management."],
            ["2","Product Concept","Visual: Mockup of the local-first UI. Concept: Operational workstation delivering zero-dependency planning for agile teams."],
            ["3","Client-Side SPA Architecture","Visual: Component mapping of projectpulse.html. Focus: Inlined JS/CSS, localStorage data model, and memory caches."],
            ["4","Global State topology (P)","Visual: Interactive JSON tree diagram. Focus: Schema reference for tasks, team capacity, RAID register, and logs."],
            ["5","Interactive Delivery Matrix","Visual: Gantt + spreadsheet layout. Focus: In-place cell editing, custom sorting/filtering, and row expansion."],
            ["6","Earned Value Management (EVM)","Visual: S-Curves showing PV, EV, AC. Focus: Schedule Performance Index (SPI) and Cost Performance Index (CPI) metrics."],
            ["7","Weekly Capacity Heatmap","Visual: Color-coded grid per resource. Focus: Under/over-allocation alerts and automated leveling diagnostics."],
            ["8","Copilot Heuristic Resolver","Visual: Decision flowchart. Focus: Automatic sequencing and conflict resolution logic rules."],
            ["9","Defect Verification Pipeline","Visual: Pipeline of defect states. Focus: S1-S4 severities, SLAs, and retesting loops."],
            ["10","RAID Governance Matrix","Visual: 5x5 threat matrix. Focus: Exposure scoring, owner assignments, and action items."],
            ["11","Schedule Baselines","Visual: Drift timeline overlays. Focus: Freeze snapshots, variance tracking, and recovery loops."],
            ["12","Custom Report Builder","Visual: Checklist config panel. Focus: Generating board packs, custom filters, and printing."],
            ["13","Keyboard Shortcuts","Visual: Command cheatsheet card. Focus: Power-user hotkeys for navigation and saving."],
            ["14","Business Value & Security","Visual: Security architecture card. Focus: 100% data ownership, zero database leaks, offline operation."],
            ["15","Summary & Roadmaps","Visual: Future release milestones. Focus: Offline-first advancements and next-generation UI updates."]
        ],
        col_widths=[0.6,2.0,3.7]
    )
    add_page_break(doc)


# ── Main Build ─────────────────────────────────────────────────────────────

def build_umi():
    print(f"\n{'='*60}")
    print("  ProjectPulse — User Manual with Illustrations (UMI)")
    print(f"  Output: {OUT_PATH}")
    print(f"{'='*60}\n")

    doc = new_document()
    add_footer(doc,"User Manual with Illustrations")

    build_cover(doc,
        product_name   = "ProjectPulse",
        subtitle       = "User Manual with Illustrations",
        doc_type       = "User Manual with Illustrations",
        version        = "v2.1.0",
        audience       = "End Users  |  Project Managers  |  Team Leads  |  QA Engineers",
        confidentiality= "Internal Use",
    )

    toc_chapters = [
        ("1",  "Getting Started",                          "3"),
        ("2",  "Executive Overview Dashboard",             "5"),
        ("3",  "Live Insights & Analytics",               "8"),
        ("4",  "Hierarchical Delivery Matrix",            "11"),
        ("5",  "Gantt Timeline",                          "17"),
        ("6",  "Weekly Scheduler & Conflict Resolution",  "21"),
        ("7",  "RAID Register",                           "26"),
        ("8",  "Team Capacity Hub",                       "30"),
        ("9",  "Defect Tracker",                          "33"),
        ("10", "Reports & Board Packs",                   "37"),
        ("11", "Audit Log",                               "40"),
        ("12", "System Configuration",                    "43"),
        ("13", "Tips, Best Practices & Troubleshooting",  "47"),
        ("14", "Complete Widget Directory & Glossary",    "50"),
        ("15", "Project Intelligence & Training Resources", "55"),
    ]
    build_toc(doc, toc_chapters)

    print("  Writing Ch 1: Getting Started...")
    ch_getting_started(doc)
    print("  Writing Ch 2: Overview Dashboard...")
    ch_overview(doc)
    print("  Writing Ch 3: Insights...")
    ch_insights(doc)
    print("  Writing Ch 4: Delivery Matrix...")
    ch_delivery(doc)
    print("  Writing Ch 5: Gantt...")
    ch_gantt(doc)
    print("  Writing Ch 6: Scheduler...")
    ch_scheduler(doc)
    print("  Writing Ch 7: RAID...")
    ch_raid(doc)
    print("  Writing Ch 8: Team...")
    ch_team(doc)
    print("  Writing Ch 9: Defects...")
    ch_defects(doc)
    print("  Writing Ch 10: Reports...")
    ch_reports(doc)
    print("  Writing Ch 11: Audit Log...")
    ch_audit(doc)
    print("  Writing Ch 12: Config...")
    ch_config(doc)
    print("  Writing Ch 13: Tips...")
    ch_tips(doc)
    print("  Writing Ch 14: Widgets Directory...")
    ch_widgets_glossary(doc)
    print("  Writing Ch 15: Project Intelligence...")
    ch_project_intelligence(doc)

    print(f"\n  Saving document -> {OUT_PATH}")
    doc.save(OUT_PATH)
    print(f"\n  Done! UMI saved: {OUT_PATH}\n")
    return OUT_PATH


if __name__ == "__main__":
    build_umi()
