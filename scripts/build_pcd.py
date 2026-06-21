"""
build_pcd.py
============
Builds the ProjectPulse Product Capabilities Document (PCD).
Audience: Executives, Sales, Prospects, Leadership.
Tone: Benefit-led, visual-first, outcome-focused.
Output: docs/ProjectPulse_Product_Capabilities.docx
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from docx_helpers import *

OUT_PATH = os.path.join(DOCS_DIR, "ProjectPulse_Product_Capabilities.docx")

# ── Chapter: Executive Summary ─────────────────────────────────────────────

def ch_exec_summary(doc):
    make_heading(doc, "Executive Summary", level=1, color=CLR_NAVY)
    add_horizontal_rule(doc, "00C2A8")
    make_body(doc,
        "ProjectPulse is a comprehensive, browser-based project intelligence "
        "workstation designed for modern software delivery teams. It combines "
        "real-time health monitoring, resource optimisation, risk governance, "
        "and stakeholder reporting into a single, zero-installation platform "
        "that runs entirely in the browser with no backend infrastructure required.",
        space_after=10)

    make_heading(doc, "Three Core Value Pillars", level=2, color=CLR_ACCENT)
    add_data_table(doc,
        ["Pillar", "Promise", "Key Capabilities"],
        [
            ["VISIBILITY",
             "Know the true state of your project at every moment — not just at the weekly status meeting.",
             "Real-time Health Index · EVM Analytics · 30-Day Heatmap · Burn-up Projections · Audit Trail"],
            ["CONTROL",
             "Act on problems before they become crises. Every risk, resource constraint, and dependency is surfaced and actionable.",
             "RAID Register · Weekly Scheduler · Conflict Resolver · Gantt Timeline · Defect Lifecycle"],
            ["INTELLIGENCE",
             "Make data-driven decisions with confidence. Simulate scenarios, forecast outcomes, and present board-ready insights in one click.",
             "Predictive Sandbox · Copilot Auto-Resolver · EVM Metrics · Executive Board Packs · Schedule Baselines"],
        ],
        col_widths=[1.3, 2.3, 2.8],
    )

    make_heading(doc, "Who Is ProjectPulse For?", level=2, color=CLR_ACCENT)
    add_data_table(doc,
        ["Persona", "Primary Use", "Key Views"],
        [
            ["Engineering Manager",     "Day-to-day project oversight, conflict resolution, resource management.", "Overview · Scheduler · Team Hub"],
            ["Product Manager",         "Delivery progress, stakeholder communication, risk governance.", "Delivery Matrix · RAID Register · Reports"],
            ["Executive / Sponsor",     "High-level health signals, milestone confidence, board reporting.", "Overview Dashboard · Board Packs"],
            ["QA Lead",                 "Defect lifecycle management, severity tracking, release readiness.", "Defect Tracker · Reports"],
            ["Lead Engineer",           "Task planning, dependency management, baseline tracking.", "Gantt Timeline · Delivery Matrix · Baselines"],
        ],
        col_widths=[1.8, 3.0, 1.6],
    )
    add_page_break(doc)


# ── Chapter 1: Product Overview ────────────────────────────────────────────

def ch_product_overview(doc):
    make_heading(doc, "1  Product Overview", level=1, color=CLR_NAVY)
    add_horizontal_rule(doc, "00C2A8")
    make_body(doc,
        "ProjectPulse is architected as a single-page application (SPA) that runs "
        "entirely within the browser. There is no server to configure, no database "
        "to provision, and no deployment to manage. All project data is persisted "
        "locally via the browser's localStorage API and can be exported at any time "
        "to a professionally formatted Excel workbook.",
        space_after=10)

    make_heading(doc, "1.1  The 12 Core Modules", level=2, color=CLR_ACCENT)
    add_data_table(doc,
        ["#", "Module", "One-Line Description"],
        [
            ["1",  "Executive Overview Dashboard",    "Real-time health signals, KPI cards, and the predictive what-if sandbox."],
            ["2",  "Live Insights & Analytics",       "Full EVM suite, burn-up projections, velocity tracking, and 30-day activity heatmap."],
            ["3",  "Hierarchical Delivery Matrix",    "Spreadsheet-style task grid with parent-child hierarchies, inline editing, and status workflows."],
            ["4",  "Gantt Timeline",                  "Interactive visual timeline with dependency arrows, drag-to-reschedule, and baseline overlay."],
            ["5",  "Weekly Scheduler",                "Resource capacity heatmap with over-allocation detection and Copilot auto-resolution."],
            ["6",  "RAID Register",                   "Unified Risk, Assumption, Issue, and Dependency register with exposure scoring."],
            ["7",  "Team Capacity Hub",               "Member profiles, capacity parameters, leave management, and utilisation tracking."],
            ["8",  "Defect Tracker",                  "Full bug lifecycle from logging through fix, retest, and closure — linked to tasks."],
            ["9",  "Reports & Board Packs",           "One-click Executive Board Pack and multi-sheet Excel workbook export."],
            ["10", "Audit Log",                       "Immutable activity stream with before/after diff payloads for traceability."],
            ["11", "Schedule Baselines",              "Snapshot-based baseline management with variance and slippage analysis."],
            ["12", "System Configuration",            "Flexible dropdown management, custom fields, 20 visual themes, and effort unit switching."],
        ],
        col_widths=[0.3, 2.1, 4.0],
    )

    make_heading(doc, "1.2  Architecture at a Glance", level=2, color=CLR_ACCENT)
    add_data_table(doc,
        ["Attribute", "Value"],
        [
            ["Deployment Model",    "Zero-backend — runs entirely in the browser"],
            ["Data Persistence",    "Browser localStorage (pp-data key) + Excel export"],
            ["Rendering Engine",    "Native HTML5, CSS3, SVG — no framework dependencies"],
            ["Analytics Engine",    "O(n) single-pass buildDashCache computation model"],
            ["Export Technology",   "ExcelJS (in-browser workbook generation)"],
            ["Theme System",        "20 curated visual themes with dark/light mode override"],
            ["Browser Support",     "Chrome 110+, Edge 110+, Firefox 115+, Safari 16+"],
        ],
        col_widths=[2.2, 4.2],
    )

    make_heading(doc, "1.3  System Architecture Design & Data Flow Lifecycle", level=2, color=CLR_ACCENT)
    make_body(doc,
        "ProjectPulse is built on a decentralized philosophy. Since the entire application runs "
        "client-side, data flows directly between the user interface, a fast local memory cache, "
        "and browser localStorage. The diagram below illustrates how data is modified in memory, "
        "automatically synchronized to browser storage, and exported to external Excel/JSON files on demand.",
        space_after=8)
    add_screenshot(doc, "diagrams/system_architecture", "Figure 1.1 — ProjectPulse Client-Side SPA System Architecture & Data Flow")
    add_page_break(doc)


# ── Chapter 2: The 12 Core Capabilities ───────────────────────────────────

def ch_capabilities(doc):
    make_heading(doc, "2  The 12 Core Capabilities", level=1, color=CLR_NAVY)
    add_horizontal_rule(doc, "00C2A8")
    make_body(doc,
        "Each of the 12 modules delivers a distinct, high-value capability. "
        "Together they form a complete project intelligence platform that eliminates "
        "the need for multiple disconnected tools.",
        space_after=10)

    caps = [
        ("2.1", "Executive Command Centre",
         "The Overview Dashboard gives project leadership an always-current, single-pane view of project health. "
         "The composite Health Index (0–100) aggregates overdue tasks, blocked items, critical risks, and "
         "open defects into a single RAG signal — so you know instantly whether to escalate or celebrate. "
         "The Predictive Sandbox lets managers simulate capacity reductions and scope expansions before "
         "committing to any plan change.",
         "01_overview_dashboard",
         "Figure 2.1 — Executive Overview Dashboard: Health Gauge, KPI Cards, and Predictive Sandbox"),

        ("2.2", "Live Analytics & EVM Intelligence",
         "The Insights module transforms raw task and effort data into the industry-standard Earned Value "
         "Management (EVM) metric suite — Planned Value, Earned Value, Schedule Variance, and Cost Performance "
         "Index — updated in real time. A burn-up chart projects the exact week of project completion based "
         "on rolling 3-week velocity, giving management an evidence-based delivery forecast.",
         "01b_insights_analytics", "Figure 2.2 — Live Insights: EVM Performance Metrics, Burn-up Chart, and Weekly Velocity"),

        ("2.3", "Hierarchical Delivery Matrix",
         "The Delivery Matrix is the operational backbone of ProjectPulse — a high-density, "
         "spreadsheet-style task grid supporting unlimited parent-child hierarchies. Every "
         "deliverable, epic, task, and subtask is managed here with inline editing, "
         "a controlled status workflow, dependency linking, and multi-dimensional filtering.",
         "02_delivery_matrix",
         "Figure 2.3 — Hierarchical Delivery Matrix: parent tasks, subtasks, status pills, inline editing"),

        ("2.4", "Visual Gantt & Dependency Graph",
         "The Gantt Timeline provides a time-anchored visual schedule with interactive task bars, "
         "dependency arrows (colour-coded by health: green=resolved, red=violated), baseline "
         "overlay ghost bars, and drag-to-reschedule with optional cascading date propagation. "
         "Four zoom levels (Day/Week/Month/Quarter) support both sprint-level and programme-level views.",
         "03_gantt_timeline",
         "Figure 2.4 — Gantt Timeline: dependency arrows, baseline overlay, and drag-to-reschedule"),

        ("2.5", "Smart Resource Scheduler",
         "The Weekly Scheduler maps every team member's allocated hours against their weekly capacity "
         "across a rolling 12-week horizon. Over-allocated cells glow crimson; optimal cells glow green. "
         "The Copilot engine applies three automated resolution heuristics — Auto-Sequence, Smart "
         "Reassignment, and Cascading Date Shift — to eliminate conflicts in a single click.",
         "04_weekly_scheduler",
         "Figure 2.5 — Weekly Scheduler: resource heatmap, over-allocation alerts, and Copilot Cockpit"),

        ("2.6", "RAID Risk Governance",
         "The RAID Register consolidates all Risks, Assumptions, Issues, and Dependencies into a "
         "single searchable register with a formal 5x5 exposure scoring matrix. Critical items "
         "(Exposure Score >= 15) automatically surface on the Executive Dashboard and deduct "
         "points from the Health Index until mitigated.",
         "05_raid_register",
         "Figure 2.6 — Unified RAID Register: risk matrix, RAID items, and exposure scoring"),

        ("2.7", "Team Capacity Hub",
         "The Capacity Hub maintains rich member profiles with role assignments, weekly hour caps, "
         "utilisation rates, and planned leave calendars. All scheduling calculations — from the "
         "Weekly Scheduler's heatmap to the Copilot's Smart Reassignment — draw their capacity "
         "data from this module in real time.",
         "06_team_capacity_hub",
         "Figure 2.7 — Team Capacity Hub: member utilisation bars and leave calendar integration"),

        ("2.8", "Defect Lifecycle Management",
         "The Defect Tracker provides a formal bug lifecycle from initial logging through "
         "assignment, fix, retest, and closure. S1 Blocker defects trigger dashboard alerts "
         "and SLA countdown timers. Every defect is linked to a specific task, subtask, or "
         "GUI screen for full traceability, and open defects automatically impact the Health Index.",
         "07_defect_tracker",
         "Figure 2.8 — Defect Tracker: severity cards, defect register, and lifecycle workflow"),

        ("2.9", "Stakeholder Board Packs & Reporting",
         "ProjectPulse generates a full Executive Board Pack — project narrative, health trend "
         "sparkline, top risks, velocity trend, and critical path highlights — and exports the "
         "complete project dataset to an 8-sheet Excel workbook with live formulas, colour-coded "
         "status cells, and executive-ready formatting. No spreadsheet maintenance required.",
         "08_reports_boardpack",
         "Figure 2.9 — Reports & Board Packs: export controls, preview panel, workbook sheet map"),

        ("2.10", "Immutable Audit Trail",
         "Every state mutation — task creation, status change, RAID update, member modification — "
         "is captured in an immutable, timestamped audit log with full before/after diff payloads. "
         "Teams can trace any change back to who made it, when, and why, allowing manual recovery "
         "if needed.",
         "09_activity_audit_log",
         "Figure 2.10 — Audit Log: chronological activity stream with diff payloads"),

        ("2.11", "Schedule Baseline History",
         "ProjectPulse tracks three parallel date sets per task (Planned, Baseline, Actual) and "
         "supports unlimited named baseline snapshots — taken at kickoff, phase gates, or "
         "re-scopes. Schedule variance and slippage analysis are calculated automatically, "
         "and any baseline can be restored in one click.",
         None, None),

        ("2.12", "Flexible Configuration & Theming",
         "All categorical dropdowns (Status, Priority, Module, Role, etc.) are fully configurable "
         "via the Dropdown Manager. Custom Fields extend the Task and Defect schemas with "
         "project-specific attributes. The effort unit (hrs/days/months) switches globally "
         "with one setting. Twenty curated visual themes with dark/light override ensure the "
         "interface matches your team's preference.",
         "10_configuration_settings",
         "Figure 2.12 — System Configuration: settings panel, dropdown manager, custom fields"),
    ]

    for num, title, desc, ss, cap in caps:
        make_heading(doc, f"{num}  {title}", level=2, color=CLR_ACCENT)
        make_body(doc, desc, space_after=8)
        if ss:
            add_screenshot(doc, ss, cap)
        if num == "2.9":
            add_screenshot(doc, "diagrams/report_workflow", "Figure 2.9b — Report Compilation and Board Pack Export Pipeline Flow")
        doc.add_paragraph()

    add_page_break(doc)


# ── Chapter 3: Key Differentiators ────────────────────────────────────────

def ch_differentiators(doc):
    make_heading(doc, "3  Key Differentiators", level=1, color=CLR_NAVY)
    add_horizontal_rule(doc, "00C2A8")
    make_body(doc,
        "ProjectPulse is purpose-built for software delivery teams who need more than "
        "a task list. The following capabilities set it apart from generic project "
        "management tools.",
        space_after=10)

    diffs = [
        ("Health Intelligence Engine",
         "Unlike tools that report status manually, ProjectPulse continuously computes "
         "a composite Health Index from four real signals: overdue tasks, blocked items, "
         "unmitigated critical risks, and open S1/S2 defects. The index degrades in "
         "real time as problems accumulate and recovers as they are resolved — giving "
         "leadership a live, truthful project health signal at all times."),
        ("What-If Predictive Sandbox",
         "The Predictive Sandbox is a non-destructive simulation environment that "
         "lets managers model capacity reductions (e.g., losing 20% of resource availability) "
         "or scope expansions (e.g., 1.2x complexity multiplier) and observe the projected "
         "impact on delivery dates — without touching the live schedule. Changes can be "
         "committed or discarded with a single click."),
        ("Automated Copilot Conflict Resolution",
         "When the Weekly Scheduler detects over-allocations or dependency violations, "
         "the Copilot engine can resolve all conflicts automatically using three heuristics: "
         "sequencing overlapping dependent tasks, redistributing work to role-matched "
         "resources with available capacity, and cascading date shifts across the critical "
         "path. The proposed resolution is previewed before any change is applied."),
        ("Zero-Backend Architecture",
         "ProjectPulse requires no server, no database, no deployment pipeline, and no "
         "DevOps overhead. It runs entirely in the browser. Teams can be operational "
         "in under five minutes with no IT involvement. Data lives locally and exports "
         "to Excel on demand — giving teams full data ownership and portability."),
    ]
    for title, desc in diffs:
        make_heading(doc, title, level=2, color=CLR_ACCENT)
        make_body(doc, desc, space_after=10)

    add_page_break(doc)


# ── Chapter 4: Capability Matrix ───────────────────────────────────────────

def ch_capability_matrix(doc):
    make_heading(doc, "4  Capability Matrix", level=1, color=CLR_NAVY)
    add_horizontal_rule(doc, "00C2A8")
    make_body(doc,
        "The table below maps each ProjectPulse module to the key capabilities it delivers. "
        "A tick indicates that the capability is fully supported within that module.",
        space_after=10)

    add_data_table(doc,
        ["Module", "Real-Time Data", "Inline Editing", "Export", "Analytics", "Scheduling", "Governance"],
        [
            ["Overview Dashboard",      "Yes", "—",   "—",   "Yes", "Yes",  "—"],
            ["Live Insights",           "Yes", "—",   "—",   "Yes", "—",    "—"],
            ["Delivery Matrix",         "Yes", "Yes", "Yes", "—",   "—",    "—"],
            ["Gantt Timeline",          "Yes", "Yes", "—",   "—",   "Yes",  "—"],
            ["Weekly Scheduler",        "Yes", "Yes", "—",   "—",   "Yes",  "—"],
            ["RAID Register",           "Yes", "Yes", "Yes", "—",   "—",    "Yes"],
            ["Team Capacity Hub",       "Yes", "Yes", "Yes", "—",   "Yes",  "—"],
            ["Defect Tracker",          "Yes", "Yes", "Yes", "—",   "—",    "Yes"],
            ["Reports & Board Packs",   "Yes", "—",   "Yes", "Yes", "—",    "—"],
            ["Audit Log",               "Yes", "—",   "Yes", "—",   "—",    "Yes"],
            ["Schedule Baselines",      "Yes", "—",   "Yes", "Yes", "—",    "—"],
            ["Configuration",           "Yes", "Yes", "—",   "—",   "—",    "—"],
        ],
        col_widths=[2.1, 0.8, 0.8, 0.7, 0.8, 0.9, 0.9],
    )
    add_page_break(doc)


# ── Chapter 5: Screenshots Gallery ────────────────────────────────────────

def ch_gallery(doc):
    make_heading(doc, "5  Application Screenshots Gallery", level=1, color=CLR_NAVY)
    add_horizontal_rule(doc, "00C2A8")
    make_body(doc,
        "The following screenshots show ProjectPulse loaded with a representative "
        "software delivery project ('Phoenix Platform v2.0'), demonstrating the "
        "application at full operational capacity.",
        space_after=12)

    gallery = [
        ("01_overview_dashboard",  "Executive Overview Dashboard — Health Gauge, KPI Cards, and Predictive Sandbox"),
        ("02_delivery_matrix",     "Hierarchical Delivery Matrix — parent tasks, subtasks, status pills, and inline controls"),
        ("03_gantt_timeline",      "Gantt Timeline — dependency arrows, baseline overlay, and today marker"),
        ("04_weekly_scheduler",    "Weekly Scheduler — resource heatmap, over-allocation detection, and Copilot Cockpit"),
        ("05_raid_register",       "RAID Register — risk classification, exposure scoring, and item lifecycle"),
        ("06_team_capacity_hub",   "Team Capacity Hub — member profiles, utilisation bars, and leave calendar"),
        ("07_defect_tracker",      "Defect Tracker — severity cards, defect register, and lifecycle workflow"),
        ("08_reports_boardpack",   "Reports & Board Packs — export builder and workbook preview"),
        ("09_activity_audit_log",  "Audit Log — chronological activity stream with diff payloads"),
        ("10_configuration_settings", "System Configuration — general settings, dropdown manager, and custom fields"),
    ]
    for fn, cap in gallery:
        add_screenshot(doc, fn, f"Screenshot: {cap}", width_inches=6.3)

    add_page_break(doc)


# ── Appendix: Technical Compatibility ─────────────────────────────────────

def ch_appendix(doc):
    make_heading(doc, "Appendix — Technical Compatibility & Deployment", level=1, color=CLR_NAVY)
    add_horizontal_rule(doc, "00C2A8")
    add_data_table(doc,
        ["Item", "Specification"],
        [
            ["Browser Support",     "Chrome 110+, Microsoft Edge 110+, Firefox 115+, Safari 16+"],
            ["Installation",        "None — open projectpulse.html in any supported browser"],
            ["Internet Connection", "Not required — fully offline-capable"],
            ["Data Storage",        "Browser localStorage (~5MB per origin, sufficient for 500+ tasks)"],
            ["Export Format",       "Microsoft Excel (.xlsx) — generated in-browser via ExcelJS"],
            ["File Sync",           "Optional file system sync via File System Access API (Chrome/Edge only)"],
            ["Screen Resolution",   "Minimum 1280 x 768px recommended for full grid views"],
            ["Mobile Support",      "Responsive layout for tablet (768px+). Limited functionality on mobile."],
        ],
        col_widths=[2.2, 4.2],
    )


# ── Main Build ─────────────────────────────────────────────────────────────

def build_pcd():
    print(f"\n{'='*60}")
    print("  ProjectPulse — Product Capabilities Document (PCD)")
    print(f"  Output: {OUT_PATH}")
    print(f"{'='*60}\n")

    doc = new_document()
    add_footer(doc, "Product Capabilities Document")

    build_cover(doc,
        product_name   = "ProjectPulse",
        subtitle       = "Product Capabilities Document",
        doc_type       = "Product Capabilities Document",
        version        = "v2.1.0",
        audience       = "Executives · Sales · Leadership · Prospects",
        confidentiality= "Commercial in Confidence",
    )

    toc_chapters = [
        ("—",   "Executive Summary",                    "3"),
        ("1",   "Product Overview",                     "4"),
        ("2",   "The 12 Core Capabilities",             "6"),
        ("3",   "Key Differentiators",                  "18"),
        ("4",   "Capability Matrix",                    "20"),
        ("5",   "Application Screenshots Gallery",      "21"),
        ("A",   "Appendix — Technical Compatibility",   "26"),
    ]
    build_toc(doc, toc_chapters)

    print("  Writing Executive Summary...")
    ch_exec_summary(doc)
    print("  Writing Chapter 1 — Product Overview...")
    ch_product_overview(doc)
    print("  Writing Chapter 2 — The 12 Core Capabilities...")
    ch_capabilities(doc)
    print("  Writing Chapter 3 — Key Differentiators...")
    ch_differentiators(doc)
    print("  Writing Chapter 4 — Capability Matrix...")
    ch_capability_matrix(doc)
    print("  Writing Chapter 5 — Screenshots Gallery...")
    ch_gallery(doc)
    print("  Writing Appendix...")
    ch_appendix(doc)

    print(f"\n  Saving document -> {OUT_PATH}")
    doc.save(OUT_PATH)
    print(f"\n  Done! PCD saved: {OUT_PATH}\n")
    return OUT_PATH


if __name__ == "__main__":
    build_pcd()
