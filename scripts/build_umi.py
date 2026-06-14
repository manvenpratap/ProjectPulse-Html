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
    add_page_break(doc)


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

    make_heading(doc,"3.2  Reading the Burn-Up Chart",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The burn-up chart shows your project's progress trajectory:",space_after=4)
    make_bullet(doc,"Blue Line (Scope): Total work to be done. A rising line means scope has been added.")
    make_bullet(doc,"Green Line (Completion): Cumulative work completed each week.")
    make_bullet(doc,"Dashed Amber Line (Projection): Where the green line is heading based on current velocity.")
    make_body(doc,
        "If the amber projection line crosses the blue scope line before your project end date, "
        "you are on track to deliver. If it projects past your end date, review your schedule.",space_after=8)

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

    make_heading(doc,"11.2  Rolling Back to a Prior State",level=2,color=CLR_ACCENT)
    make_body(doc,
        "If an incorrect change was made, you can restore your project to any prior state "
        "captured in the Audit Log:",space_after=4)
    make_numbered(doc,"Find the log entry immediately BEFORE the unwanted change in the Audit Log.")
    make_numbered(doc,"Click 'Restore to This Point' on that log entry.")
    make_numbered(doc,"A confirmation dialog explains what will be restored.")
    make_numbered(doc,"Click Confirm. The application restores all changes made after that point.")
    make_numbered(doc,"A 'Rollback' entry is added to the Audit Log recording what was restored.")
    doc.add_paragraph()
    add_callout(doc,
        "Rollback is a powerful but permanent operation. After rolling back, all changes made "
        "AFTER the restore point are lost. Ensure you have captured an Excel export before "
        "performing a rollback if you may need those records.",style="caution")
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
    make_bullet(doc,"Export before major changes: Always export to Excel before a rollback or baseline restore.")
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

    print(f"\n  Saving document -> {OUT_PATH}")
    doc.save(OUT_PATH)
    print(f"\n  Done! UMI saved: {OUT_PATH}\n")
    return OUT_PATH


if __name__ == "__main__":
    build_umi()
