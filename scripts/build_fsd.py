"""
build_fsd.py
============
Builds the ProjectPulse Functional Specification Document (FSD).
Audience: Product Managers, Developers, QA Engineers, Business Analysts.
Depth: Complete technical specification - every workflow, formula, state machine,
       data model, and business rule documented in full.
Output: docs/ProjectPulse_Functional_Specification.docx
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from docx_helpers import *

OUT_PATH = os.path.join(DOCS_DIR, "ProjectPulse_Functional_Specification.docx")

# ══════════════════════════════════════════════════════════════════════════════
#  PART I — SYSTEM ARCHITECTURE & FOUNDATIONS
# ══════════════════════════════════════════════════════════════════════════════

def part1_philosophy(doc):
    make_heading(doc,"1  Product Philosophy & Design Principles",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "ProjectPulse is built on five foundational design principles that govern every "
        "architectural and UX decision in the product.",space_after=8)
    principles = [
        ("Zero Friction",
         "The application must be usable immediately, without installation, configuration, "
         "or network connectivity. Every feature must be accessible within two clicks from "
         "any view. Complexity is hidden behind progressive disclosure."),
        ("Real-Time Truth",
         "All displayed metrics must reflect the current state of the data at all times. "
         "There are no 'refresh' or 'recalculate' buttons. Every state mutation triggers "
         "an immediate, synchronous UI update via the render pipeline."),
        ("Non-Destructive by Default",
         "All high-risk operations (sandbox mutations, baseline restores, bulk edits) operate "
         "on copies of the data or are reversible via the Audit Log. The user's live schedule "
         "is never modified without explicit confirmation."),
        ("Governance as a Feature",
         "Accountability is built into every workflow. Status transitions enforce mandatory "
         "comments. RAID items require owners. Defects are traced to tasks. Every mutation is "
         "permanently logged. The product treats governance as a first-class product requirement."),
        ("Performance at Scale",
         "The O(n) buildDashCache architecture ensures that analytics remain sub-millisecond "
         "regardless of task count. All SVG visualisations (Gantt, Health Gauge, heatmaps) "
         "are rendered natively without third-party charting libraries."),
    ]
    for title, desc in principles:
        make_heading(doc, title, level=2, color=CLR_ACCENT)
        make_body(doc, desc, space_after=8)
    add_page_break(doc)


def part1_architecture(doc):
    make_heading(doc,"2  Application Architecture",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")

    make_heading(doc,"2.1  Single-Page Application Model",level=2,color=CLR_ACCENT)
    make_body(doc,
        "ProjectPulse is implemented as a monolithic Single-Page Application (SPA) delivered "
        "as a single HTML file (projectpulse.html). All JavaScript logic, CSS styles, and "
        "SVG assets are inlined or bundled within this file. There is no module bundler, "
        "no build step, and no external CDN dependencies for core functionality.",space_after=6)
    make_bullet(doc,"Single file delivery: projectpulse.html contains all application logic.")
    make_bullet(doc,"No network requests at runtime (except optional file sync on supported browsers).")
    make_bullet(doc,"All state is maintained in a single JavaScript object P (the global state store).")
    make_bullet(doc,"The render pipeline is triggered by calling render() after every state mutation.")
    doc.add_paragraph()

    make_heading(doc,"2.2  Global State Object (P)",level=2,color=CLR_ACCENT)
    make_body(doc,
        "All application state is stored in a single JavaScript object P. The following "
        "top-level keys constitute the complete state topology:",space_after=6)
    add_data_table(doc,
        ["Key","Type","Contents"],
        [
            ["P.name",         "string",    "Project name. Displayed in the header and on exported documents."],
            ["P.desc",         "string",    "Project description. Shown on cover pages of exported reports."],
            ["P.tasks",        "Task[]",    "Array of all task objects (parent and child). The primary data entity."],
            ["P.members",      "Member[]",  "Array of all team member profiles."],
            ["P.raids",        "RAID[]",    "Array of all RAID register entries."],
            ["P.defects",      "Defect[]",  "Array of all defect records."],
            ["P.baselines",    "Baseline[]","Array of all captured baseline snapshot records."],
            ["P.log",          "LogEntry[]","Append-only array of all activity log entries (max 500)."],
            ["P.settings",     "object",    "Global settings: effortUnit, hoursPerDay, daysPerWeek, workDays, alertPrefs."],
            ["P.dropdowns",    "object",    "All configurable dropdown option arrays keyed by field name."],
            ["P.cache",        "object",    "Computed analytics cache (hydrated by buildDashCache). Never persisted directly."],
            ["P.sandboxTasks", "Task[]|null","In-memory sandbox clone. Null when sandbox is inactive."],
        ],
        col_widths=[1.5,0.8,4.1],
    )

    make_heading(doc,"2.3  localStorage Persistence Model",level=2,color=CLR_ACCENT)
    make_body(doc,
        "ProjectPulse persists all project data to the browser's localStorage under the "
        "key pp-data. Serialization uses JSON.stringify() with a custom replacer to ensure "
        "P.cache and P.sandboxTasks are excluded from persistence.",space_after=6)
    make_bullet(doc,"Key: pp-data — stores the full serialised P object minus cache and sandbox.")
    make_bullet(doc,"Save trigger: Every state mutation calls save() which debounces writes by 10 seconds.")
    make_bullet(doc,"Manual save: Ctrl+S forces an immediate synchronous localStorage write.")
    make_bullet(doc,"Storage limit: Browser localStorage is typically ~5MB per origin. Sufficient for 500+ tasks with full activity logs.")
    make_bullet(doc,"File sync: On Chrome/Edge, the File System Access API allows optional sync to a local .xlsx file.")
    doc.add_paragraph()

    make_heading(doc,"2.4  Auto-Save Mechanism",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The auto-save mechanism uses a debounce pattern to batch rapid successive mutations "
        "into a single localStorage write, preventing performance degradation during inline "
        "bulk editing operations.",space_after=6)
    make_code(doc,
        "function save() {\n"
        "  clearTimeout(P._saveTimer);\n"
        "  P._saveTimer = setTimeout(() => {\n"
        "    localStorage.setItem('pp-data', JSON.stringify(P, saveReplacer));\n"
        "  }, 10000);  // 10-second debounce\n"
        "}")
    add_callout(doc,
        "Ctrl+S bypasses the debounce timer and triggers an immediate synchronous save. "
        "This is recommended before closing the browser tab or switching networks.",style="tip")

    make_heading(doc,"2.5  Render Pipeline",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The render pipeline is the core update mechanism. It is called after every state "
        "mutation and follows this fixed execution sequence:",space_after=6)
    make_numbered(doc,"buildDashCache(P) — recomputes all analytics in O(n) single-pass.")
    make_numbered(doc,"renderActiveView() — re-renders the currently active module view.")
    make_numbered(doc,"updateNavBadges() — updates notification badges on the navigation bar.")
    make_numbered(doc,"updateHealthPulse() — refreshes the top-bar health pulse indicator.")
    doc.add_paragraph()
    add_page_break(doc)


def part1_schemas(doc):
    make_heading(doc,"3  Data Model & Full Schema Reference",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "This section documents the complete field-level schema for every primary data entity "
        "managed by ProjectPulse. All entities are stored as plain JavaScript objects within "
        "their respective arrays in the global state object P.",space_after=8)

    # Task Schema
    make_heading(doc,"3.1  Task Schema",level=2,color=CLR_ACCENT)
    make_body(doc,"The Task is the primary unit of work in ProjectPulse.",space_after=6)
    add_data_table(doc,
        ["Field","Type","Constraint","Default","Description"],
        [
            ["id",                "string",   "Unique, auto-gen", "TASK-NNN",  "Auto-generated unique identifier. Format: TASK-001."],
            ["name",              "string",   "Required",         "",          "Task title displayed in all views."],
            ["status",            "string",   "Enum (dropdowns)", "Not Started","Current workflow status. Must be a valid VALID_TRANSITIONS key."],
            ["priority",          "string",   "Enum",             "Medium",    "Critical / High / Medium / Low."],
            ["category",          "string",   "Enum",             "",          "Classification from configured Category dropdown."],
            ["module",            "string",   "Enum",             "",          "Associated module from Module dropdown."],
            ["moduleType",        "string",   "Enum",             "",          "Server / GUI / Interface."],
            ["assignee",          "string",   "Member name",      "",          "Assigned member. Must match a member in P.members."],
            ["release",           "string",   "",                 "",          "Target release label (e.g. v1.0.0)."],
            ["startDate",         "YYYY-MM-DD","",                "",          "Current planned start date."],
            ["dueDate",           "YYYY-MM-DD","",                "",          "Current planned due date."],
            ["actCompletionDate", "YYYY-MM-DD","",                "",          "Actual date work was completed (null if incomplete)."],
            ["baselineStartDate", "YYYY-MM-DD","Immutable post-capture","",   "Frozen baseline start date."],
            ["baselineDueDate",   "YYYY-MM-DD","Immutable post-capture","",   "Frozen baseline due date."],
            ["forecastDueDate",   "YYYY-MM-DD","System computed", "",          "Velocity-based projected completion date."],
            ["slippageReason",    "string",   "",                 "",          "Free-text explanation for schedule slippage beyond baseline."],
            ["complexity",        "string",   "Enum",             "Medium",    "Easy (0.5x) / Medium (1.0x) / Complex (1.5x)."],
            ["progress",          "number",   "0-100",            "0",         "Percentage completion. Aggregated from subtasks if present."],
            ["estEffort",         "number",   ">= 0",             "0",         "Estimated effort in active effort unit."],
            ["actEffort",         "number",   ">= 0",             "0",         "Actual logged effort in active effort unit."],
            ["baselineEffort",    "number",   ">= 0",             "0",         "Baseline effort captured at snapshot time."],
            ["dependsOn",         "string[]", "Task IDs",         "[]",        "Array of prerequisite Task IDs. Must be acyclic."],
            ["notes",             "string",   "",                 "",          "Multi-line task description and notes."],
            ["subtasks",          "Subtask[]","",                 "[]",        "Array of child step/screen items."],
            ["guiScreens",        "string[]", "",                 "[]",        "Linked GUI screen names (for GUI module tasks)."],
            ["updatedAt",         "ISO 8601", "",                 "now",       "Timestamp of last modification. Updated on every save."],
            ["parentId",          "string",   "",                 "",          "Parent task ID. Empty string for root-level tasks."],
        ],
        col_widths=[1.5,0.8,1.3,0.9,2.1],
    )

    # Subtask Schema
    make_heading(doc,"3.2  Subtask Schema",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Field","Type","Description"],
        [
            ["id",              "string",    "Unique identifier within parent task. Format: ST-NNN."],
            ["name",            "string",    "Subtask title."],
            ["status",          "string",    "Same valid statuses as parent Task."],
            ["category",        "string",    "Feature / Bug / Improvement / GUI Screen / etc."],
            ["done",            "boolean",   "True when status is Completed. Used for progress aggregation."],
            ["effort",          "number",    "Estimated effort in active effort unit."],
            ["actEffort",       "number",    "Actual effort logged."],
            ["progress",        "number",    "0-100. Contributes to parent task progress via weighted average."],
            ["type",            "string",    "step (development task) or screen (GUI screen)."],
            ["actCompletionDate","YYYY-MM-DD","Actual completion date. Used by Activity Heatmap date resolution."],
        ],
        col_widths=[1.8,0.9,3.9],
    )

    # Member Schema
    make_heading(doc,"3.3  Member Schema",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Field","Type","Description"],
        [
            ["id",            "string",  "Unique identifier. Format: MEM-NNN."],
            ["name",          "string",  "Full name. Used as assignee reference in tasks and defects."],
            ["role",          "string",  "Role from configured Role dropdown. Used by Copilot for Smart Reassignment."],
            ["status",        "string",  "Active / On Leave / Other Assignment / Serving Notice Period / Departed."],
            ["plannedLeaves", "object[]","Array of {start: YYYY-MM-DD, end: YYYY-MM-DD} leave date ranges."],
            ["weeklyHourCap", "number",  "Maximum standard hours per week. Default: 40."],
            ["utilisationRate","number", "0.0-1.0. Fraction of standard time dedicated to project work. Default: 1.0."],
        ],
        col_widths=[1.8,0.9,3.9],
    )

    # RAID Schema
    make_heading(doc,"3.4  RAID Item Schema",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Field","Type","Description"],
        [
            ["id",          "string",  "Unique identifier. Format: RAID-NNN."],
            ["type",        "string",  "Risk / Assumption / Issue / Dependency."],
            ["title",       "string",  "Short descriptive title."],
            ["description", "string",  "Full description of the item."],
            ["status",      "string",  "Identified / Active / Mitigated / Closed / Realized."],
            ["impact",      "string",  "High / Medium / Low (qualitative scale)."],
            ["probability", "string",  "High / Medium / Low (qualitative scale for Risks)."],
            ["severity",    "string",  "S1 Critical / S2 Major / S3 Moderate / S4 Minor."],
            ["exposureScore","number", "Computed: probability_int x impact_int using 1-3 scale. Max 9."],
            ["owner",       "string",  "Member name. Required for Active items."],
            ["mitigation",  "string",  "Mitigation / resolution strategy text. Required for Active items."],
            ["targetDate",  "YYYY-MM-DD","Target closure date. Required for Active items."],
            ["raisedDate",  "YYYY-MM-DD","Date the item was logged."],
            ["closedDate",  "YYYY-MM-DD","Date the item was closed or mitigated."],
        ],
        col_widths=[1.6,0.9,4.1],
    )

    # Defect Schema
    make_heading(doc,"3.5  Defect Schema",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Field","Type","Description"],
        [
            ["id",         "string",  "Unique identifier. Format: DEF-NNN."],
            ["title",      "string",  "Defect title. Required."],
            ["type",       "string",  "Functional Bug / UI/UX Issue / Performance / Security / Data Issue / Suggestion."],
            ["severity",   "string",  "S1 Blocker / S2 High / S3 Medium / S4 Low."],
            ["priority",   "string",  "Critical / High / Medium / Low."],
            ["status",     "string",  "New / Assigned / Fixed / Retest / Closed / Rejected / Deferred."],
            ["linkedType", "string",  "task / subtask / screen — type of linked entity."],
            ["linkedId",   "string",  "ID of the linked task (TASK-NNN) or subtask (ST-NNN)."],
            ["assignee",   "string",  "Developer assigned to fix. Must match a member name."],
            ["reporter",   "string",  "Person who logged the defect."],
            ["desc",       "string",  "Full defect description."],
            ["steps",      "string",  "Step-by-step reproduction instructions."],
            ["raisedDate", "YYYY-MM-DD","Date the defect was logged."],
            ["closedDate", "YYYY-MM-DD","Date the defect was resolved or closed."],
        ],
        col_widths=[1.5,0.9,4.2],
    )

    # Activity Log Entry Schema
    make_heading(doc,"3.6  Activity Log Entry Schema",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Field","Type","Description"],
        [
            ["ts",              "ISO 8601", "Timestamp of the log entry recorded at millisecond precision."],
            ["user",            "string",   "Name of the active team member who performed the action."],
            ["action",          "string",   "Created / Updated / Status Changed / Deleted."],
            ["taskId",          "string",   "ID of the primary entity affected."],
            ["taskName",        "string",   "Name of the primary entity at time of action."],
            ["field",           "string",   "The specific field that changed (e.g. status, dueDate)."],
            ["oldVal",          "any",      "Previous value before mutation."],
            ["newVal",          "any",      "New value after mutation."],
            ["subtaskId",       "string",   "Optional. References a specific subtask if the change was at subtask level."],
            ["actCompletionDate","YYYY-MM-DD","Optional. Retrospective actual completion date for activity date resolution."],
        ],
        col_widths=[1.8,0.9,3.9],
    )
    add_page_break(doc)


def part1_cache(doc):
    make_heading(doc,"4  Performance Caching: buildDashCache",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The buildDashCache(P) function is the analytics backbone of ProjectPulse. It performs "
        "a single O(n) pass over the entire task and log dataset to produce an O(1) lookup "
        "cache (P.cache) that powers every widget, chart, and KPI in the application.",space_after=8)

    make_heading(doc,"4.1  Cache Architecture",level=2,color=CLR_ACCENT)
    make_body(doc,"The cache object P.cache contains the following pre-computed structures:",space_after=6)
    add_data_table(doc,
        ["Cache Key","Type","Contents"],
        [
            ["totalTasks",     "number",   "Count of all non-cancelled, non-completed parent tasks."],
            ["completedTasks", "number",   "Count of tasks with status == Completed."],
            ["overdueTasks",   "number",   "Count of active tasks where dueDate < today and status != Completed/Cancelled."],
            ["blockedTasks",   "number",   "Count of tasks with status == On Hold or with unresolved dependency violations."],
            ["activeRaidCount","number",   "Count of RAID items with status in {Identified, Active}."],
            ["criticalRaids",  "number",   "Count of RAID items with exposureScore >= 15."],
            ["openDefects",    "Defect[]", "Array of defects with status not in {Closed, Rejected}."],
            ["s1Blockers",     "number",   "Count of open defects with severity == S1 Blocker."],
            ["s2Critical",     "number",   "Count of open defects with severity == S2 High."],
            ["velocityHistory","number[]", "Array of weekly complexity-points-completed for the past 12 weeks."],
            ["burnUpData",     "object",   "Time-series arrays for Scope and Completion lines on the burn-up chart."],
            ["heatmapData",    "object",   "30-day activity density map keyed by date string (YYYY-MM-DD)."],
            ["memberAlloc",    "object",   "Weekly allocation hours per member per week for the Scheduler grid."],
            ["evmMetrics",     "object",   "Pre-computed PV, EV, AC, SV, SPI, CV values."],
            ["depMap",         "object",   "Dependency lookup map: taskId -> [predecessorIds]. O(1) lookup."],
        ],
        col_widths=[1.8,0.9,3.9],
    )

    make_heading(doc,"4.2  Cache Invalidation Policy",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The cache has no TTL (time-to-live). It is fully rebuilt from scratch on every "
        "call to buildDashCache(), which is invoked as the first step of every render() "
        "call. Since render() is called after every state mutation, the cache is always "
        "perfectly consistent with the current state.",space_after=6)
    add_callout(doc,
        "P.cache is intentionally excluded from localStorage persistence. If the page is "
        "refreshed, the cache is rebuilt from the persisted P.tasks, P.members, etc. data "
        "on the first render() call after page load.",style="note")
    add_page_break(doc)


def part1_config(doc):
    make_heading(doc,"5  Global Configuration & Settings Model",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "All system-wide settings are stored in the P.settings object and P.dropdowns object. "
        "Changes to settings take effect immediately across all views without requiring a reload.",space_after=8)

    make_heading(doc,"5.1  P.settings Fields",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Field","Type","Valid Values","Effect"],
        [
            ["effortUnit",   "string",  "hrs / days / months",
             "Globally switches all effort labels and rescales displayed values."],
            ["hoursPerDay",  "number",  "1-24 (default: 8)",
             "Used to convert between hours and days when switching effort units."],
            ["daysPerWeek",  "number",  "1-7 (default: 5)",
             "Working week length. Affects capacity calculations and date math."],
            ["workDays",     "string[]","Subset of [Mon,Tue,Wed,Thu,Fri,Sat,Sun]",
             "Specifies which days are working days for date arithmetic."],
            ["alertPrefs",   "object",  "{}",
             "Future: alert threshold preferences per metric."],
        ],
        col_widths=[1.5,0.8,1.8,2.5],
    )

    make_heading(doc,"5.2  P.complexityFactors",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Complexity Level","Default Multiplier","Configurable?","Effect on Velocity"],
        [
            ["Easy",    "0.5x", "Yes", "Complexity points = estEffort x 0.5. Tasks count less toward velocity."],
            ["Medium",  "1.0x", "Yes", "Complexity points = estEffort x 1.0. Baseline multiplier."],
            ["Complex", "1.5x", "Yes", "Complexity points = estEffort x 1.5. Tasks count more toward velocity."],
        ],
        col_widths=[1.8,1.5,1.2,2.1],
    )
    add_callout(doc,
        "Changing complexity multipliers in Settings -> Complexity Factors triggers an immediate "
        "full cache rebuild, updating all velocity, EVM, and burn-up chart calculations across the application.",
        style="warning")
    add_page_break(doc)


# ══════════════════════════════════════════════════════════════════════════════
#  PART II — MODULE FUNCTIONAL SPECIFICATIONS
# ══════════════════════════════════════════════════════════════════════════════

def fsd_overview(doc):
    make_heading(doc,"6  Executive Overview Dashboard",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Executive Overview Dashboard is the primary health monitoring interface of "
        "ProjectPulse. It aggregates signals from all other modules into three composite "
        "KPI metrics and a radial health gauge. All calculations are computed in real time "
        "on every render cycle.",space_after=8)
    add_screenshot(doc,"01_overview_dashboard",
        "Figure 6.1 — Executive Overview Dashboard: KPI Cards, Health Gauge, and Predictive Sandbox")

    make_heading(doc,"6.1  Health Index — Formula Derivation",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The Health Index is a composite score (0-100) computed from four weighted drag factors:",space_after=6)
    make_formula(doc,
        "Health = 100 - (Overdue/Active * 50) - (Blocked/Active * 30) - (OnHold/Active * 20) "
        "- (criticalRaids * 5) - (s1Blockers * 10) - (s2Critical * 5)")
    make_body(doc,"Where:",space_after=4)
    add_data_table(doc,
        ["Variable","Source","Description"],
        [
            ["Overdue",      "P.cache.overdueTasks",  "Active tasks past their due date."],
            ["Blocked",      "P.cache.blockedTasks",  "Tasks on hold or with unresolved dependencies."],
            ["OnHold",       "computed inline",        "Tasks with status == On Hold."],
            ["Active",       "P.cache.totalTasks",    "Total non-Completed, non-Cancelled tasks."],
            ["criticalRaids","P.cache.criticalRaids", "RAID items with exposureScore >= 15."],
            ["s1Blockers",   "P.cache.s1Blockers",    "Open defects with severity == S1 Blocker."],
            ["s2Critical",   "P.cache.s2Critical",    "Open defects with severity == S2 High."],
        ],
        col_widths=[1.6,2.0,3.0],
    )
    add_callout(doc,
        "The Health Index is floored at 0 and capped at 100. "
        "Completed and Cancelled tasks are excluded from the Active denominator. "
        "The index cannot go negative.",style="rule")

    make_heading(doc,"6.2  Delivery Confidence — Velocity-Based Model",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Delivery Confidence is the probability of delivering all remaining work within the "
        "planned timeline, estimated from rolling velocity vs. remaining backlog.",space_after=6)
    make_formula(doc,
        "Confidence = MIN(100, MAX(30, (weeklyVelocity * weeksRemaining) / remainingPoints * 100))")
    add_data_table(doc,
        ["Variable","Calculation"],
        [
            ["weeklyVelocity",   "3-week rolling average of completed complexity points per week. Excludes holiday weeks."],
            ["weeksRemaining",   "Calendar weeks between today and the latest task due date in the active schedule."],
            ["remainingPoints",  "SUM(estEffort * complexityFactor) for all incomplete tasks."],
        ],
        col_widths=[2.0,4.4],
    )
    add_callout(doc,
        "Delivery Confidence is floored at 30% to prevent alarming users when no historical "
        "velocity data exists (e.g., a newly created project). The 30% floor communicates "
        "uncertainty rather than impossibility.",style="note")

    make_heading(doc,"6.3  Active RAID Count",level=2,color=CLR_ACCENT)
    make_formula(doc,
        "activeRAID = COUNT(P.raids WHERE status IN {Identified, Active})")
    make_body(doc,
        "This metric counts all RAID items not yet resolved. It is displayed as a KPI card "
        "and contributes to the Health Index via the criticalRaids sub-component.",space_after=8)

    make_heading(doc,"6.4  Dynamic Health Gauge — SVG Engine",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The Health Gauge is an animated radial SVG arc rendered natively in the browser. "
        "The arc angle maps the Health Index (0-100) to a 270-degree arc (range: 0 to 270 degrees).",space_after=6)
    make_formula(doc,"arcAngle = healthIndex / 100 * 270  (degrees)")
    make_body(doc,"Colour thresholds:",space_after=4)
    add_data_table(doc,
        ["Health Range","Gauge Colour","Glow Effect","Interpretation"],
        [
            ["80-100", "Green  (#27AE60)",  "Green neon glow",  "Project healthy. Maintain pace."],
            ["50-79",  "Amber  (#E67E22)",  "Amber glow",       "Warning. One or more risk factors active."],
            ["0-49",   "Red    (#C0392B)",  "Red pulsing glow", "Critical. Immediate intervention required."],
        ],
        col_widths=[1.3,1.6,1.5,2.2],
    )

    make_heading(doc,"6.5  What-If Predictive Sandbox — Full Workflow",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The Sandbox provides a non-destructive simulation environment. The following workflow "
        "governs sandbox activation, mutation, and resolution.",space_after=6)
    make_numbered(doc,"User clicks 'Enable Sandbox' toggle on the Overview Dashboard.")
    make_numbered(doc,"System deep-clones P.tasks into P.sandboxTasks. P.tasks remains unmodified.")
    make_numbered(doc,"All scheduler and Gantt views switch to render from P.sandboxTasks.")
    make_numbered(doc,"User adjusts Capacity Slider or Scope Multiplier to model the scenario.")
    make_numbered(doc,"System recalculates forecast dates across all P.sandboxTasks proportionally.")
    make_numbered(doc,"'Commit Changes' button: overwrites P.tasks with P.sandboxTasks, clears sandbox, triggers save().")
    make_numbered(doc,"'Discard' button: sets P.sandboxTasks = null, reverts all views to P.tasks.")
    doc.add_paragraph()
    add_data_table(doc,
        ["Sandbox Control","Input","Effect on P.sandboxTasks"],
        [
            ["Capacity Slider",   "-10% to -50%","Multiplies each task's duration by 1/(1-reduction). "
                                                 "E.g. -20% extends all task durations by 1.25x."],
            ["Scope Multiplier",  "1.1x to 2.0x","Multiplies estEffort of all Incomplete tasks by the factor. "
                                                 "Pushes forecast dates outward proportionally."],
            ["Commit Changes",    "—",           "Copies sandboxTasks to P.tasks. Logs a Sandbox Commit entry in P.log. Calls save()."],
            ["Discard",           "—",           "Sets P.sandboxTasks = null. Restores views to live P.tasks. No log entry created."],
        ],
        col_widths=[1.8,1.4,3.4],
    )
    add_callout(doc,
        "Always capture a Schedule Baseline (see Section 16) before clicking Commit. "
        "A Commit operation is irreversible without a baseline to restore from.",style="caution")
    add_page_break(doc)


def fsd_insights(doc):
    make_heading(doc,"7  Live Insights & Analytics",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Insights module is the analytical intelligence layer of ProjectPulse. It surfaces "
        "Earned Value Management metrics, velocity data, burn-up projections, and activity "
        "heatmaps — all computed in real time from the P.cache structures built by buildDashCache().",
        space_after=8)

    make_heading(doc,"7.1  Full EVM Metric Suite",level=2,color=CLR_ACCENT)
    make_body(doc,
        "ProjectPulse implements the full PMI-standard EVM framework. All six core EVM "
        "metrics are computed and displayed as live KPI cards.",space_after=6)
    add_data_table(doc,
        ["Metric","Abbr.","Formula","Green Threshold","Interpretation"],
        [
            ["Planned Value",              "PV",  "totalBudget x (daysElapsed / totalDays)",
             "N/A",        "Budget that should have been consumed by today per original plan."],
            ["Earned Value",               "EV",  "totalBudget x (completedPoints / totalPoints)",
             "EV >= PV",   "Value of work actually delivered relative to plan."],
            ["Actual Cost",                "AC",  "SUM(actEffort) x blendedRate",
             "AC <= EV",   "Real cost of resources consumed to date."],
            ["Schedule Variance",          "SV",  "EV - PV",
             "SV >= 0",    "Positive = ahead of schedule. Negative = behind schedule."],
            ["Schedule Performance Index", "SPI", "EV / PV",
             "SPI >= 1.0", "SPI < 1.0 = schedule slippage. SPI > 1.0 = ahead of schedule."],
            ["Cost Variance",              "CV",  "EV - AC",
             "CV >= 0",    "Positive = under budget. Negative = over budget."],
        ],
        col_widths=[1.8,0.5,2.2,1.0,1.9],
    )

    make_heading(doc,"7.2  Burn-Up Chart Rendering",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The burn-up chart displays three lines plotted on a weekly time axis:",space_after=6)
    make_bullet(doc,"Scope Line (Blue): SUM(estEffort x complexityFactor) for all tasks at each week. Rises when scope is added.")
    make_bullet(doc,"Completion Line (Green): Cumulative SUM of completed task complexity points per week, using actCompletionDate for attribution.")
    make_bullet(doc,"Projection Line (Dashed Amber): Linear extrapolation from current completion to 100% scope, based on rolling 3-week velocity.")
    make_body(doc,
        "Projection formula:",space_after=4)
    make_formula(doc,
        "weeksToComplete = remainingPoints / weeklyVelocity\n"
        "projectedEndDate = today + weeksToComplete weeks")
    add_callout(doc,
        "The projection line is only displayed when at least 3 weeks of velocity data exist. "
        "On newly created projects, only the Scope and Completion lines are shown.",style="note")

    make_heading(doc,"7.3  30-Day Activity Heatmap & Date Resolution",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The 30-Day Activity Heatmap is a calendar-style grid where each cell represents one "
        "calendar day. Cell colour intensity reflects the number of task state changes attributed "
        "to that day.",space_after=6)
    make_body(doc,"Date Resolution Algorithm:",bold=True,space_after=4)
    make_numbered(doc,"For each log entry in P.log, check if actCompletionDate is present and non-null.")
    make_numbered(doc,"If actCompletionDate is present: attribute the activity to that date.")
    make_numbered(doc,"If actCompletionDate is absent: attribute the activity to the log entry timestamp (ts).")
    make_numbered(doc,"Aggregate activity counts per date into heatmapData[dateString].")
    make_numbered(doc,"Render: lighter cells = fewer activities, darker teal cells = more activities.")
    add_callout(doc,
        "This retrospective date resolution is essential for teams who log completed work "
        "after the fact. Without it, all activity would cluster on the log entry dates "
        "rather than the actual completion dates, producing misleading velocity data.",style="rule")
    add_page_break(doc)


def fsd_delivery(doc):
    make_heading(doc,"8  Hierarchical Delivery Matrix",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Delivery Matrix is the operational backbone of ProjectPulse. It is a high-density, "
        "spreadsheet-style task grid that manages the full task hierarchy, inline editing, "
        "status workflows, dependency mapping, and effort tracking.",space_after=8)
    add_screenshot(doc,"02_delivery_matrix",
        "Figure 8.1 — Hierarchical Delivery Matrix: parent tasks, subtasks, status pills, inline editing")

    make_heading(doc,"8.1  Parent-Child Tree Rendering",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The task list is rendered as a flattened depth-first traversal of the task tree. "
        "Root tasks (parentId == '') are rendered at depth 0. Child tasks are rendered "
        "immediately after their parent, indented by 24px per depth level.",space_after=6)
    make_code(doc,
        "function flattenTree(tasks, parentId='', depth=0) {\n"
        "  return tasks\n"
        "    .filter(t => t.parentId === parentId)\n"
        "    .flatMap(t => [{ ...t, _depth: depth },\n"
        "                  ...flattenTree(tasks, t.id, depth+1)]);\n"
        "}")

    make_heading(doc,"8.2  Inline Edit Cell Lifecycle",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Every cell in the Delivery Matrix supports inline editing. The lifecycle is:",space_after=6)
    make_numbered(doc,"User double-clicks a cell. The cell renders an input control (text, number, date, or select).")
    make_numbered(doc,"The input is pre-populated with the current field value and focused automatically.")
    make_numbered(doc,"User modifies the value and either presses Enter or clicks outside (blur event).")
    make_numbered(doc,"The new value is validated against field constraints (type check, enum membership).")
    make_numbered(doc,"If valid: the task object in P.tasks is updated, a log entry is appended to P.log, render() is called.")
    make_numbered(doc,"If invalid: the input is highlighted in red and the original value is restored on blur.")
    doc.add_paragraph()

    make_heading(doc,"8.3  Task Status State Machine",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Status transitions follow the VALID_TRANSITIONS rule set. Not all transitions "
        "are permitted. Attempting an invalid transition displays an error toast.",space_after=6)
    add_transition_table(doc,[
        ["Not Started",  "In Progress",    "No guard",              "Log Status Changed entry."],
        ["Not Started",  "Cancelled",      "No guard",              "Log Status Changed entry."],
        ["In Progress",  "Under Review",   "No guard",              "Log Status Changed entry."],
        ["In Progress",  "On Hold",        "Comment required",      "Log Status Changed with comment."],
        ["In Progress",  "Cancelled",      "Comment required",      "Log Status Changed with comment."],
        ["Under Review", "Completed",      "No guard",              "Set actCompletionDate = today. Log entry."],
        ["Under Review", "In Progress",    "No guard",              "Log Status Changed entry."],
        ["Under Review", "Cancelled",      "Comment required",      "Log Status Changed with comment."],
        ["On Hold",      "In Progress",    "No guard",              "Log Status Changed entry."],
        ["On Hold",      "Under Review",   "No guard",              "Log Status Changed entry."],
        ["On Hold",      "Cancelled",      "Comment required",      "Log Status Changed with comment."],
        ["Completed",    "In Progress",    "No guard (re-open)",    "Clear actCompletionDate. Log re-open."],
        ["Cancelled",    "Not Started",    "No guard (re-activate)","Log Status Changed entry."],
    ])

    make_heading(doc,"8.4  Complexity Scoring Model",level=2,color=CLR_ACCENT)
    make_formula(doc,
        "complexityPoints(task) = task.estEffort * P.complexityFactors[task.complexity]")
    make_body(doc,
        "Complexity points are used for velocity calculation and EVM metrics. "
        "Changing the complexity level of a task immediately updates its point contribution.",space_after=6)

    make_heading(doc,"8.5  Progress Aggregation Formula",level=2,color=CLR_ACCENT)
    make_formula(doc,
        "parentProgress = SUM(subtask.progress * subtask.effort) / SUM(subtask.effort)")
    make_body(doc,
        "Parent task progress is the effort-weighted average of all child subtask progress values. "
        "If a parent task has no subtasks, progress is set directly on the parent.",space_after=6)

    make_heading(doc,"8.6  Multi-Dimensional Filter Engine",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The sidebar filter panel applies multiple simultaneous filters using AND logic. "
        "All active filters must be satisfied for a task to appear in the result set.",space_after=6)
    make_bullet(doc,"Module, Status, Priority, Assignee, Release, Category, Module Type — all support multi-select.")
    make_bullet(doc,"Full-text search scans: task ID, name, assignee, notes, and all subtask names.")
    make_bullet(doc,"Active filter pills are displayed above the task list for transparency. Each pill has an 'x' to remove it.")
    make_bullet(doc,"Filter state persists across view switches within the same session.")
    doc.add_paragraph()

    make_heading(doc,"8.7  Dependency Linking Model",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Task dependencies are stored as a string array (dependsOn[]) of predecessor task IDs. "
        "The dependency graph is enforced to be acyclic — the system prevents creation of "
        "circular dependencies.",space_after=6)
    make_bullet(doc,"Cycle detection: before adding task B to task A's dependsOn array, the system checks if A is already a transitive predecessor of B via BFS on the dependency graph.")
    make_bullet(doc,"Violated dependencies (successor scheduled before predecessor) are highlighted in red in the Gantt view and listed in the Scheduler's Diagnostics panel.")
    add_page_break(doc)


def fsd_gantt(doc):
    make_heading(doc,"9  Gantt Timeline",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Gantt Timeline provides a time-anchored visual schedule rendered as an SVG canvas "
        "within the browser. Task bars, dependency arrows, the today marker, and baseline "
        "overlay bars are all rendered as SVG elements.",space_after=8)
    add_screenshot(doc,"03_gantt_timeline",
        "Figure 9.1 — Gantt Timeline: dependency arrows, baseline overlay, and today marker")

    make_heading(doc,"9.1  SVG Canvas Coordinate Model",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The Gantt canvas is a single SVG element scaled to fit the current zoom level and task count.",space_after=6)
    make_formula(doc,"taskBarX = (startDate - viewStartDate) * pixelsPerDay")
    make_formula(doc,"taskBarWidth = (dueDate - startDate) * pixelsPerDay")
    make_formula(doc,"taskBarY = taskIndex * rowHeight")
    add_data_table(doc,
        ["Zoom Level","pixelsPerDay","Visible Horizon"],
        [
            ["Day",     "60px",  "4 weeks"],
            ["Week",    "12px",  "6 months"],
            ["Month",   "4px",   "18 months"],
            ["Quarter", "1.5px", "3 years"],
        ],
        col_widths=[1.5,1.5,3.4],
    )

    make_heading(doc,"9.2  Dependency Arrow Rendering",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Dependency arrows are rendered as cubic Bezier SVG <path> elements connecting the "
        "right edge of the predecessor bar to the left edge of the successor bar.",space_after=6)
    make_bullet(doc,"Green arrows: Predecessor status == Completed.")
    make_bullet(doc,"Blue arrows: Active dependency — predecessor in progress.")
    make_bullet(doc,"Red arrows: Violated dependency — successor.startDate < predecessor.dueDate.")
    make_body(doc,"Bezier path formula:",space_after=4)
    make_code(doc,
        "d = `M ${x1} ${y1}  C ${x1+40} ${y1}  ${x2-40} ${y2}  ${x2} ${y2}`")

    make_heading(doc,"9.3  Drag-to-Reschedule",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Task bars on the Gantt timeline are draggable. The drag-reschedule workflow:",space_after=6)
    make_numbered(doc,"mousedown on a task bar: stores initial mouse X position and task start/end dates.")
    make_numbered(doc,"mousemove: calculates deltaX in pixels, converts to deltaDays = deltaX / pixelsPerDay.")
    make_numbered(doc,"Visual preview: task bar moves with cursor. Ghost bar shows original position.")
    make_numbered(doc,"mouseup: applies deltaDays to task.startDate and task.dueDate. Calls render().")
    make_numbered(doc,"If cascade: propagates deltaDays to all downstream dependent tasks transitively.")
    add_callout(doc,
        "Drag-reschedule modifies the live P.tasks schedule. "
        "Use Sandbox Mode to experiment safely before applying changes to the live plan.",style="warning")
    add_page_break(doc)


def fsd_scheduler(doc):
    make_heading(doc,"10  Weekly Scheduler & Conflict Resolver",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Weekly Scheduler is the resource capacity management engine. It maps every active "
        "team member's allocation against their weekly capacity, detects conflicts, and offers "
        "automated resolution via the Copilot engine.",space_after=8)
    add_screenshot(doc,"04_weekly_scheduler",
        "Figure 10.1 — Weekly Scheduler: resource heatmap, conflict diagnostics, and Copilot Cockpit")

    make_heading(doc,"10.1  Weekly Capacity Formula",level=2,color=CLR_ACCENT)
    make_formula(doc,
        "weeklyCapacity(member, week) = hoursPerDay * daysPerWeek * utilisationRate - leaveHours(member, week)")
    make_body(doc,
        "where leaveHours(member, week) = number of work-day hours the member is on planned leave during that week.",space_after=8)

    make_heading(doc,"10.2  Weekly Allocation Calculation",level=2,color=CLR_ACCENT)
    make_formula(doc,
        "weeklyAllocation(member, week) = SUM(task.estEffort / task.durationWeeks\n"
        "  FOR EACH task WHERE task.assignee == member.name\n"
        "  AND task.startDate <= week.end AND task.dueDate >= week.start)")
    make_body(doc,
        "Task effort is spread evenly across its duration in weeks. "
        "A task spanning 4 weeks contributes estEffort/4 hours to each covered week.",space_after=6)

    make_heading(doc,"10.3  Heatmap Cell State Classification",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["State","Condition","Hex Colour","Cell Label","Action Required"],
        [
            ["On Leave",       "weeklyCapacity == 0 (leave recorded)",   "#374151","0h / 0h",    "No tasks should be assigned."],
            ["Over-allocated", "allocation > capacity",                  "#7F1D1D","XXh / YYh",  "Reassign tasks or extend dates."],
            ["Optimal",        "0.8 * capacity <= allocation <= capacity","14532D","XXh / YYh",  "No action required."],
            ["Under-utilised", "allocation < 0.7 * capacity",            "#374151","XXh / YYh",  "Consider additional assignments."],
        ],
        col_widths=[1.5,2.1,1.2,1.1,1.7],
    )

    make_heading(doc,"10.4  Conflict Detection Engine",level=2,color=CLR_ACCENT)
    make_body(doc,"The conflict detector scans for three types of scheduling conflicts:",space_after=6)
    add_data_table(doc,
        ["Conflict Type","Detection Condition","Severity"],
        [
            ["Over-Allocation",        "weeklyAllocation(member, week) > weeklyCapacity(member, week)", "High"],
            ["Dependency Violation",   "task.startDate < predecessor.dueDate for any predecessor in task.dependsOn", "High"],
            ["Scheduling Gap",         "A task has no assignee and its start date is within 7 days", "Medium"],
        ],
        col_widths=[2.0,3.0,1.4],
    )

    make_heading(doc,"10.5  Copilot — Three Resolution Heuristics",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The autoResolveAllSchedulerConflicts() engine evaluates tasks in sandbox state "
        "and applies heuristics sequentially until all conflicts are resolved:",space_after=6)
    add_data_table(doc,
        ["Heuristic","Name","Logic","Pre-condition","Post-condition"],
        [
            ["A","Auto-Sequence",
             "For each dependency violation (Task_A -> Task_B overlap): "
             "set Task_B.startDate = Task_A.dueDate + 1 day. "
             "Recalculate Task_B.dueDate = Task_B.startDate + originalDuration.",
             "Both tasks in sandbox.", "Task_B starts after Task_A ends."],
            ["B","Smart Reassignment",
             "For each over-allocated member M: find an active member M2 where "
             "M2.role == M.role AND weeklyAllocation(M2, week) + taskEffort/durationWeeks <= weeklyCapacity(M2, week). "
             "Reassign the smallest task from M to M2.",
             "Role-matched member with spare capacity exists.", "M's allocation drops below capacity."],
            ["C","Cascading Date Shift",
             "For each task on the critical path whose dueDate has shifted: "
             "collect all transitive dependents via BFS. For each dependent, "
             "push startDate and dueDate forward by the same delta, preserving durations.",
             "Dependency graph is acyclic.", "All dependent tasks are scheduled after their predecessors."],
        ],
        col_widths=[0.6,1.4,2.6,1.2,1.4],
    )
    add_callout(doc,
        "All Copilot resolutions are applied to P.sandboxTasks only. "
        "The Diagnostics panel shows the proposed changes in full before the user clicks Commit.",style="rule")

    make_heading(doc,"10.6  Sandbox Lifecycle — State Machine",level=2,color=CLR_ACCENT)
    add_transition_table(doc,[
        ["INACTIVE","ACTIVE (CLEAN)", "User enables Sandbox toggle", "Deep-clone P.tasks into P.sandboxTasks."],
        ["ACTIVE (CLEAN)","ACTIVE (DIRTY)", "User adjusts Capacity or Scope sliders", "Mutations applied to P.sandboxTasks only."],
        ["ACTIVE (DIRTY)","ACTIVE (DIRTY)", "User runs Copilot resolver", "Additional mutations applied to P.sandboxTasks."],
        ["ACTIVE (DIRTY)","COMMITTED",      "User clicks Commit Changes", "Copy P.sandboxTasks to P.tasks. Log entry. Call save(). Set P.sandboxTasks=null."],
        ["ACTIVE (CLEAN)","INACTIVE",       "User clicks Discard", "Set P.sandboxTasks=null. Views revert to P.tasks."],
        ["ACTIVE (DIRTY)","INACTIVE",       "User clicks Discard", "Set P.sandboxTasks=null. All sandbox changes lost."],
    ])
    add_page_break(doc)


def fsd_raid(doc):
    make_heading(doc,"11  RAID Register",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The RAID Register is the risk governance engine of ProjectPulse. It provides a "
        "structured framework for identifying, scoring, tracking, and mitigating project risks, "
        "assumptions, issues, and dependencies.",space_after=8)
    add_screenshot(doc,"05_raid_register",
        "Figure 11.1 — Unified RAID Register: risk matrix, RAID items, and exposure scoring")

    make_heading(doc,"11.1  Classification Model",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Type","Definition","Who Raises It","Management Action"],
        [
            ["Risk","A potential future event that could negatively impact timeline, scope, or quality.",
             "Any team member","Mitigate, transfer, or accept before the event occurs."],
            ["Assumption","A factor believed to be true for planning purposes without verified evidence.",
             "Project Manager / Analyst","Validate through testing or stakeholder confirmation."],
            ["Issue","An active, current problem impacting timeline, scope, or budget.",
             "Any team member","Resolve immediately via assigned owner with clear mitigation strategy."],
            ["Dependency","A reliance on an external team, system, vendor, or deliverable.",
             "Lead Engineer / PM","Map to task schedules. Monitor checkpoint dates. Escalate delays immediately."],
        ],
        col_widths=[1.3,2.2,1.5,1.6],
    )

    make_heading(doc,"11.2  Exposure Scoring Matrix (Risks)",level=2,color=CLR_ACCENT)
    make_formula(doc,"Exposure Score = Probability (1-3) x Impact (1-3)  [max = 9]")
    add_data_table(doc,
        ["Probability Label","Int Value","Impact Label","Int Value","Score Range","Rating"],
        [
            ["High",   "3", "High",   "3", "7-9", "Critical (Red)"],
            ["Medium", "2", "Medium", "2", "4-6", "Medium (Amber)"],
            ["Low",    "1", "Low",    "1", "1-3", "Low (Green)"],
        ],
        col_widths=[1.4,0.8,1.1,0.8,1.2,1.3],
    )
    add_data_table(doc,
        ["Score Range","Rating","Colour","Management Protocol"],
        [
            ["7-9", "Critical", "Red",   "Immediate mitigation plan required. Executive escalation mandatory. Contributes -5% to Health Index."],
            ["4-6", "Medium",   "Amber", "Weekly monitoring. Mitigation plan within 5 business days."],
            ["1-3", "Low",      "Green", "Logged and reviewed bi-weekly. No immediate action required."],
        ],
        col_widths=[1.0,1.0,0.9,3.7],
    )

    make_heading(doc,"11.3  RAID Item Status Lifecycle",level=2,color=CLR_ACCENT)
    add_transition_table(doc,[
        ["Identified","Active",    "Owner and mitigation plan assigned",    "Send notification to owner. Log status change."],
        ["Active",    "Mitigated", "Mitigation actions completed",          "Set closedDate. Log status change. Recalculate Health Index."],
        ["Active",    "Realized",  "Risk event has occurred (for Risks)",   "Convert to Issue. Log status change."],
        ["Mitigated", "Closed",    "Effectiveness confirmed over 2+ weeks", "Set closedDate. Permanently archived."],
        ["Mitigated", "Active",    "Mitigation proved ineffective",         "Clear closedDate. Reassign owner. Log re-activation."],
        ["Identified","Closed",    "Item found invalid upon triage",        "Set closedDate. Log closure."],
    ])

    make_heading(doc,"11.4  Dashboard Health Integration",level=2,color=CLR_ACCENT)
    make_formula(doc,
        "healthPenalty = criticalRaids * 5  (deducted from Health Index)")
    make_body(doc,
        "Only RAID items with exposureScore >= 7 (Critical) and status in {Identified, Active} "
        "contribute to the Health Index penalty. Mitigated, Closed, and Low/Medium items "
        "do not deduct from Health.",space_after=6)
    add_callout(doc,
        "Governance requirement: every Active RAID item must have an Owner, a Mitigation Strategy, "
        "and a Target Closure Date. The application enforces these three fields before allowing "
        "an item to transition from Identified to Active.",style="constraint")
    add_page_break(doc)


def fsd_team(doc):
    make_heading(doc,"12  Team Capacity Hub",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Team Capacity Hub manages all team resource profiles, capacity parameters, "
        "leave calendars, and utilisation data. It is the single source of truth for "
        "all resource-related calculations in the Scheduler, Copilot, and EVM modules.",space_after=8)
    add_screenshot(doc,"06_team_capacity_hub",
        "Figure 12.1 — Team Capacity Hub: member profiles, utilisation bars, and leave calendar")

    make_heading(doc,"12.1  Effective Weekly Capacity Formula",level=2,color=CLR_ACCENT)
    make_formula(doc,
        "effectiveCapacity(member, week) =\n"
        "  (hoursPerDay * daysPerWeek * member.utilisationRate)\n"
        "  - SUM(workHoursOnLeave(member, week))")
    make_body(doc,"where:",space_after=4)
    make_bullet(doc,"workHoursOnLeave: counts the number of configured working day hours within any overlap between member.plannedLeaves and the given week's date range.")
    make_bullet(doc,"Members with status != Active have effectiveCapacity = 0 for all weeks.")
    doc.add_paragraph()

    make_heading(doc,"12.2  Member Status Lifecycle",level=2,color=CLR_ACCENT)
    add_transition_table(doc,[
        ["Active",          "On Leave",              "Leave period starts",             "effectiveCapacity set to 0 for leave weeks."],
        ["On Leave",        "Active",                "Leave period ends",               "effectiveCapacity restored to normal."],
        ["Active",          "Other Assignment",      "Member temporarily reassigned",   "Excluded from Scheduler capacity. Tasks remain assigned."],
        ["Active",          "Serving Notice Period", "Resignation submitted",           "Excluded from future task assignments in Copilot."],
        ["Serving Notice",  "Departed",              "Employment ended",                "Excluded from all capacity and assignment logic."],
    ])

    make_heading(doc,"12.3  Role-Based Assignment Constraints",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The Copilot's Smart Reassignment heuristic (Section 10.5, Heuristic B) only "
        "swaps tasks between members with identical roles. This prevents incorrect "
        "cross-functional reassignments (e.g., a QA task being assigned to a Developer).",space_after=6)
    add_callout(doc,
        "Role names are configured in Settings -> Dropdown Manager -> Role. "
        "Ensure role names are consistent across all member profiles for Copilot to function correctly.",
        style="integration")
    add_page_break(doc)


def fsd_defects(doc):
    make_heading(doc,"13  Defect Tracker",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Defect Tracker manages the full software defect lifecycle from initial "
        "logging through assignment, fix, retest, and closure. Defect data is integrated "
        "into the Health Index and linked to tasks for full traceability.",space_after=8)
    add_screenshot(doc,"07_defect_tracker",
        "Figure 13.1 — Defect Tracker: severity cards, defect register, and lifecycle workflow")

    make_heading(doc,"13.1  Severity Matrix & SLA Targets",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Severity","Code","Definition","Health Index Impact","SLA Target"],
        [
            ["Blocker","S1",
             "Critical function completely broken. No workaround. Application unusable.",
             "-10% per active Blocker","24 hours"],
            ["High","S2",
             "Major functionality impaired. Temporary workaround exists but is impractical.",
             "-5% per active High","48 hours"],
            ["Medium","S3",
             "Significant issue. Clear and stable workaround available.",
             "-2% per active Medium","5 business days"],
            ["Low","S4",
             "Trivial cosmetic issue, spelling error, or minor UI inconsistency.",
             "-0.5% per active Low","10 business days"],
        ],
        col_widths=[1.1,0.6,2.3,1.6,1.4],
    )
    make_formula(doc,
        "healthDefectPenalty = (s1count*10) + (s2count*5) + (s3count*2) + (s4count*0.5)")

    make_heading(doc,"13.2  Defect Status Lifecycle",level=2,color=CLR_ACCENT)
    add_transition_table(doc,[
        ["New",      "Assigned",  "Owner allocated by Engineering Manager",     "Log Status Changed. Notify assignee."],
        ["Assigned", "Fixed",     "Developer applies code fix",                 "Log Status Changed. SLA timer stops."],
        ["Fixed",    "Retest",    "Fix deployed to test environment",           "Log Status Changed. Notify QA."],
        ["Retest",   "Closed",    "QA verifies fix is correct",                 "Set closedDate. Health penalty removed."],
        ["Retest",   "Assigned",  "QA finds fix incomplete (re-open)",          "Log Status Changed. Notify developer."],
        ["New",      "Rejected",  "Defect is by design or not reproducible",   "Set closedDate. Log rejection reason."],
        ["Assigned", "Rejected",  "Investigation reveals non-defect",           "Set closedDate. Log rejection reason."],
        ["Assigned", "Deferred",  "Fix postponed to future release",            "Log Status Changed with release target."],
    ])

    make_heading(doc,"13.3  S1 Blocker Escalation Workflow",level=2,color=CLR_ACCENT)
    make_numbered(doc,"S1 Blocker logged: Red alert banner immediately appears on Overview Dashboard.")
    make_numbered(doc,"24-hour SLA countdown timer starts from defect creation timestamp.")
    make_numbered(doc,"If defect remains in New or Assigned status after 24 hours: in-app notification sent to Engineering Manager.")
    make_numbered(doc,"SLA breach is flagged in the Defect Tracker with a red SLA badge.")
    make_numbered(doc,"Defect remains flagged until status transitions to Fixed or beyond.")
    add_page_break(doc)


def fsd_reports(doc):
    make_heading(doc,"14  Reports & Board Packs",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Reports module provides one-click generation of an Executive Board Pack "
        "and a professional multi-sheet Excel workbook export with live formulas.",space_after=8)
    add_screenshot(doc,"08_reports_boardpack",
        "Figure 14.1 — Reports & Board Packs: export builder, preview panel, workbook sheet map")

    make_heading(doc,"14.1  Executive Board Pack — Generation Workflow",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The Board Pack is assembled programmatically from live P.cache data:",space_after=6)
    make_numbered(doc,"Project Summary Narrative: auto-generated paragraph from health signals, milestone status, and top risks.")
    make_numbered(doc,"Health Trend Sparkline: 8-week history of Health Index from P.cache.velocityHistory.")
    make_numbered(doc,"Critical Path Tasks: all tasks on the critical path within 5 days of or past their due date.")
    make_numbered(doc,"Top 5 RAID Items: RAID items ranked by exposureScore descending, with owner and mitigation summary.")
    make_numbered(doc,"Team Velocity: 4-week rolling average from P.cache.velocityHistory.")
    doc.add_paragraph()

    make_heading(doc,"14.2  Excel Workbook Architecture — 8 Sheets",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Sheet","Contents","Live Formulas"],
        [
            ["System State",  "Project name, description, settings, effort unit, last saved timestamp, file sync path.", "No"],
            ["Tasks",         "Full task register: all fields, baseline dates, variance calculations, slippage reasons.", "Yes (variance)"],
            ["Team",          "Member directory: roles, statuses, capacity parameters, leave records.", "No"],
            ["RAID Register", "All RAID items: type, exposure score, owner, mitigation, status lifecycle.", "Yes (exposure)"],
            ["Defects",       "Complete defect log: severity, priority, status, SLA, linked tasks, repro steps.", "Yes (SLA)"],
            ["Activity Log",  "Last 500 audit log entries: timestamps, users, actions, diff payloads.", "No"],
            ["Baselines",     "All captured baseline snapshots with per-task variance calculations.", "Yes (variance)"],
            ["Releases",      "Release version registry with status and target dates.", "No"],
        ],
        col_widths=[1.5,3.5,1.4],
    )

    make_heading(doc,"14.3  Excel Cell Colour Coding Rules",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Colour","Background Hex","Text Hex","Applied When"],
        [
            ["Green",  "#D1E7DD","#0F5132","Status = Completed / Closed / Mitigated / Low RAID exposure."],
            ["Yellow", "#FFF3CD","#664D03","Status = In Progress / Under Review / Medium risk / Deferred."],
            ["Red",    "#F8D7DA","#842029","Status = Blocked / Overdue / Critical risk / S1-S2 Defect."],
            ["Grey",   "#F8F9FA","#6C757D","Status = Cancelled / Rejected / On Hold / Departed member."],
        ],
        col_widths=[1.0,1.5,1.2,2.9],
    )
    add_callout(doc,
        "Excel cells in the Tasks sheet contain live formulas for Variance Days and Effort Variance. "
        "Stakeholders can modify the workbook after export without breaking these calculations.",style="tip")
    add_page_break(doc)


def fsd_audit(doc):
    make_heading(doc,"15  Audit Log & Activity Streams",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Audit Log provides a complete, immutable, chronological record of every state "
        "mutation in the application. It is append-only and forms the basis for both "
        "accountability reporting and session rollback.",space_after=8)
    add_screenshot(doc,"09_activity_audit_log",
        "Figure 15.1 — Audit Log: chronological activity stream with diff payloads")

    make_heading(doc,"15.1  Immutability Model",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Log entries are appended to P.log using Array.push(). No update or delete "
        "operations are permitted on existing log entries. The application UI provides "
        "no mechanism to edit or remove a log entry — they are strictly immutable.",space_after=6)
    add_callout(doc,
        "The 500-entry auto-pruning policy removes the oldest entries when the log exceeds 500 records. "
        "Export the log to Excel before reaching this limit if a permanent audit record is required.",style="warning")

    make_heading(doc,"15.2  Session Rollback Algorithm",level=2,color=CLR_ACCENT)
    make_body(doc,
        "The rollback system computes the inverse of all log entries between the current "
        "state and the target restore point, then applies them in reverse chronological order.",space_after=6)
    make_numbered(doc,"User selects a target log entry (the desired restore point).")
    make_numbered(doc,"System collects all log entries with ts > target.ts in reverse chronological order.")
    make_numbered(doc,"For each collected log entry, the inverse operation is computed:")
    make_bullet(doc,"Created -> Deleted (remove entity from array).",level=1)
    make_bullet(doc,"Updated -> Updated (swap oldVal/newVal, restore previous value).",level=1)
    make_bullet(doc,"Status Changed -> Status Changed (restore previous status).",level=1)
    make_bullet(doc,"Deleted -> Created (restore entity from snapshot in log entry).",level=1)
    make_numbered(doc,"Inverse operations are applied sequentially to P.tasks/P.raids/P.defects/P.members.")
    make_numbered(doc,"render() is called after all inverses are applied.")
    make_numbered(doc,"A new 'Rollback' entry is appended to P.log describing what was restored.")
    make_numbered(doc,"save() is called to persist the restored state.")
    add_page_break(doc)


def fsd_baselines(doc):
    make_heading(doc,"16  Schedule Baselines",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "Schedule Baselines capture a named, timestamped snapshot of all task planned dates "
        "and efforts. They serve as the immutable reference for calculating schedule variance "
        "and enabling plan restoration.",space_after=8)

    make_heading(doc,"16.1  Three Date Set Model",level=2,color=CLR_ACCENT)
    add_data_table(doc,
        ["Date Set","Task Fields","Lifecycle","Purpose"],
        [
            ["Planned Dates",  "startDate, dueDate, estEffort",
             "Updated during execution","Current target dates that resources work towards."],
            ["Baseline Dates", "baselineStartDate, baselineDueDate, baselineEffort",
             "Frozen at capture; updated at each new snapshot",
             "Immutable reference for variance calculation."],
            ["Actual Dates",   "actCompletionDate, actEffort",
             "Set when task is completed",
             "Real completion dates used for EVM and velocity reporting."],
        ],
        col_widths=[1.4,2.0,1.5,1.7],
    )

    make_heading(doc,"16.2  Snapshot Capture Algorithm",level=2,color=CLR_ACCENT)
    make_numbered(doc,"User enters baseline name and description in Settings -> Schedule Baselines.")
    make_numbered(doc,"User clicks 'Capture Snapshot'.")
    make_numbered(doc,"System iterates over all tasks in P.tasks.")
    make_numbered(doc,"For each task: copies startDate -> baselineStartDate, dueDate -> baselineDueDate, estEffort -> baselineEffort.")
    make_numbered(doc,"A baseline record {id, name, description, timestamp, taskSnapshots[]} is appended to P.baselines.")
    make_numbered(doc,"The Activity Log records a 'Baseline Captured' entry.")
    make_numbered(doc,"save() is called.")
    doc.add_paragraph()

    make_heading(doc,"16.3  Variance Calculation Formulas",level=2,color=CLR_ACCENT)
    make_formula(doc,"varianceDays(task) = (task.dueDate - task.baselineDueDate) in calendar days")
    make_formula(doc,"effortVariance(task) = task.estEffort - task.baselineEffort")
    make_body(doc,
        "Positive varianceDays = behind schedule. "
        "Positive effortVariance = scope increase vs. baseline.",space_after=6)

    make_heading(doc,"16.4  Restore Workflow",level=2,color=CLR_ACCENT)
    make_numbered(doc,"User selects a historical baseline from Settings -> Schedule Baselines.")
    make_numbered(doc,"User clicks 'Restore'. Confirmation dialog shown.")
    make_numbered(doc,"System overwrites each task's startDate, dueDate, estEffort with values from the baseline snapshot.")
    make_numbered(doc,"System recalculates baselineStartDate, baselineDueDate, baselineEffort to match restored values.")
    make_numbered(doc,"Full cache rebuild and render() call.")
    make_numbered(doc,"'Baseline Restored' entry appended to P.log.")
    make_numbered(doc,"save() called.")
    add_callout(doc,
        "A restore operation overwrites all current planned dates. "
        "Always capture a 'Current State' snapshot before restoring a historical baseline, "
        "so you can return to the pre-restore position if needed.",style="caution")
    add_page_break(doc)


def fsd_config(doc):
    make_heading(doc,"17  System Configuration",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "The Administration panel (Settings icon in the navigation bar) centralises all "
        "system-wide configuration. Changes take effect immediately.",space_after=8)
    add_screenshot(doc,"10_configuration_settings",
        "Figure 17.1 — System Configuration: general settings, dropdown manager, and custom fields")

    make_heading(doc,"17.1  Dropdown Configuration Manager",level=2,color=CLR_ACCENT)
    make_body(doc,
        "All categorical dropdown option lists in ProjectPulse are stored in P.dropdowns "
        "and are fully configurable via the Dropdown Manager:",space_after=6)
    make_numbered(doc,"Navigate to Settings -> Dropdown Manager.")
    make_numbered(doc,"Select the dropdown to modify (e.g., Module, Category, Role).")
    make_numbered(doc,"Add new options, edit existing labels, or drag-and-drop to reorder.")
    make_numbered(doc,"Click Save. New options appear immediately in all inline edit selects.")
    doc.add_paragraph()
    add_callout(doc,
        "Removing a dropdown option that is currently assigned to active tasks will NOT delete "
        "those tasks or their data — the old value is preserved on existing records. "
        "However, the old value will not appear as a selectable option for new assignments.",style="warning")

    make_heading(doc,"17.2  Custom Fields Engine",level=2,color=CLR_ACCENT)
    make_body(doc,
        "Custom Fields extend the Task and Defect schemas with project-specific attributes:",space_after=6)
    add_data_table(doc,
        ["Attribute","Value"],
        [
            ["Supported Types",  "Text, Number, Date, Dropdown (with custom option list), Checkbox"],
            ["Scope",            "Custom fields are defined independently for Tasks and for Defects"],
            ["Visibility",       "Custom fields appear as additional columns in Delivery Matrix and Defect Tracker"],
            ["Persistence",      "Custom field values stored in task.customFields[fieldId] = value"],
            ["Export",           "Custom field columns are included in the Tasks and Defects sheets of the Excel workbook"],
        ],
        col_widths=[2.0,4.4],
    )

    make_heading(doc,"17.3  Theme Engine",level=2,color=CLR_ACCENT)
    make_body(doc,
        "ProjectPulse ships with 20 curated visual themes managed by a CSS custom property "
        "switching system. Theme selection is persisted in localStorage independently of the "
        "main project data (key: pp-theme).",space_after=6)
    make_bullet(doc,"Dark Themes (10): Nexus, Obsidian, Fintech, Codename, Workflow, Bento, and 4 additional dark palettes.")
    make_bullet(doc,"Light Themes (10): Emerald, Terracotta, Cloud, Daybreak, and 6 additional light palettes.")
    make_bullet(doc,"Dark/Light Override: Forces dark or light rendering mode regardless of theme selection.")
    make_bullet(doc,"Theme switch: applies immediately via document.documentElement.setAttribute('data-theme', themeName).")
    add_page_break(doc)


# ══════════════════════════════════════════════════════════════════════════════
#  PART III — CROSS-CUTTING CONCERNS
# ══════════════════════════════════════════════════════════════════════════════

def part3_concerns(doc):
    make_heading(doc,"18  Security & Data Privacy",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    make_body(doc,
        "As a zero-backend application, ProjectPulse does not transmit project data to "
        "any external server. All data remains within the browser's localStorage on the "
        "user's local device.",space_after=6)
    make_bullet(doc,"No server: no API endpoints, no authentication tokens, no network data transmission during normal operation.")
    make_bullet(doc,"localStorage isolation: data is scoped to the page origin and is not accessible by other websites.")
    make_bullet(doc,"Export security: Excel exports are generated in-browser and downloaded directly. No data passes through a server.")
    make_bullet(doc,"File sync: the optional File System Access API sync is initiated by explicit user gesture and requires user permission for each file access.")
    add_callout(doc,
        "Organizations with sensitive project data should ensure the projectpulse.html file "
        "is served from a secure, access-controlled web server rather than opened directly "
        "from the filesystem if multiple users share a device.",style="warning")

    make_heading(doc,"19  Performance & Scalability Limits",level=1,color=CLR_NAVY,space_before=18)
    add_horizontal_rule(doc,"00C2A8")
    add_data_table(doc,
        ["Resource","Practical Limit","Technical Reason"],
        [
            ["Tasks",            "Up to 500 tasks recommended", "localStorage 5MB cap. Above 500 tasks with full logs may approach limit."],
            ["Activity Log",     "500 entries (auto-pruned)",   "Fixed cap enforced in code. Older entries removed when limit reached."],
            ["Baselines",        "No hard limit",               "Each baseline snapshot stores per-task date triples. 20 baselines x 500 tasks = ~1MB."],
            ["Team Members",     "No hard limit (50 practical)","Scheduler grid becomes unwieldy beyond ~50 rows."],
            ["Render Performance","Smooth up to ~300 tasks",    "DOM virtualisation not implemented. Above 300 rows may cause perceptible render lag."],
        ],
        col_widths=[1.8,2.0,2.8],
    )

    make_heading(doc,"20  Browser Compatibility Matrix",level=1,color=CLR_NAVY,space_before=18)
    add_horizontal_rule(doc,"00C2A8")
    add_data_table(doc,
        ["Browser","Minimum Version","Full Support","File Sync API"],
        [
            ["Google Chrome",    "110+","Yes","Yes (File System Access API)"],
            ["Microsoft Edge",   "110+","Yes","Yes (File System Access API)"],
            ["Mozilla Firefox",  "115+","Yes","No (API not supported)"],
            ["Apple Safari",     "16+", "Yes","No (API not supported)"],
            ["Mobile Chrome",    "110+","Partial (grid views limited)","No"],
            ["Mobile Safari",    "16+", "Partial (grid views limited)","No"],
        ],
        col_widths=[1.8,1.5,1.5,2.6],
    )
    add_page_break(doc)


# ══════════════════════════════════════════════════════════════════════════════
#  APPENDICES
# ══════════════════════════════════════════════════════════════════════════════

def fsd_appendices(doc):
    make_heading(doc,"Appendix A — Keyboard Shortcuts Reference",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    add_data_table(doc,
        ["Shortcut","Action","Scope"],
        [
            ["Ctrl + S",     "Force immediate save to localStorage.",         "Global"],
            ["Ctrl + Z",     "Undo last inline cell edit.",                   "Delivery Matrix"],
            ["Ctrl + F",     "Focus the search / filter bar.",                "Delivery Matrix, Defects"],
            ["Escape",       "Close open modal, flyout, or dropdown.",         "Global"],
            ["Enter",        "Confirm inline cell edit.",                     "Delivery Matrix"],
            ["Tab",          "Move to next editable cell.",                   "Delivery Matrix"],
            ["Shift + Tab",  "Move to previous editable cell.",               "Delivery Matrix"],
            ["Arrow Keys",   "Navigate between grid cells.",                  "Delivery Matrix"],
            ["Ctrl + Click", "Multi-select tasks for bulk operations.",       "Delivery Matrix"],
            ["Space",        "Toggle expand/collapse on selected parent row.","Delivery Matrix"],
        ],
        col_widths=[1.5,3.1,1.8],
    )

    make_heading(doc,"Appendix B — Formula Reference Card",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
    add_data_table(doc,
        ["Formula","Module","Reference"],
        [
            ["Health = 100 - (Overdue/Active*50) - (Blocked/Active*30) - (OnHold/Active*20) - (critRaids*5) - (s1*10) - (s2*5)",
             "Overview","Section 6.1"],
            ["Confidence = MIN(100, MAX(30, velocity*weeksRemaining/remainingPoints*100))",
             "Overview","Section 6.2"],
            ["arcAngle = healthIndex/100*270",
             "Overview Gauge","Section 6.4"],
            ["PV = totalBudget * (daysElapsed/totalDays)",
             "Insights EVM","Section 7.1"],
            ["EV = totalBudget * (completedPoints/totalPoints)",
             "Insights EVM","Section 7.1"],
            ["SV = EV - PV",
             "Insights EVM","Section 7.1"],
            ["SPI = EV / PV",
             "Insights EVM","Section 7.1"],
            ["complexityPoints = estEffort * complexityFactor",
             "Delivery Matrix","Section 8.4"],
            ["parentProgress = SUM(st.progress * st.effort) / SUM(st.effort)",
             "Delivery Matrix","Section 8.5"],
            ["effectiveCapacity = hoursPerDay * daysPerWeek * utilisationRate - leaveHours",
             "Scheduler","Section 10.1"],
            ["ExposureScore = probability_int * impact_int",
             "RAID","Section 11.2"],
            ["healthDefectPenalty = s1*10 + s2*5 + s3*2 + s4*0.5",
             "Defects","Section 13.1"],
            ["varianceDays = dueDate - baselineDueDate",
             "Baselines","Section 16.3"],
            ["effortVariance = estEffort - baselineEffort",
             "Baselines","Section 16.3"],
        ],
        col_widths=[3.8,1.3,0.8],
    )

    make_heading(doc,"Appendix C — Glossary",level=1,color=CLR_NAVY)
    add_horizontal_rule(doc,"00C2A8")
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


# ══════════════════════════════════════════════════════════════════════════════
#  MAIN BUILD ORCHESTRATOR
# ══════════════════════════════════════════════════════════════════════════════

def build_fsd():
    print(f"\n{'='*60}")
    print("  ProjectPulse — Functional Specification Document (FSD)")
    print(f"  Output: {OUT_PATH}")
    print(f"{'='*60}\n")

    doc = new_document()
    add_footer(doc, "Functional Specification Document")

    build_cover(doc,
        product_name   = "ProjectPulse",
        subtitle       = "Functional Specification Document",
        doc_type       = "Functional Specification Document",
        version        = "v2.1.0",
        audience       = "Product Managers / Developers / QA Engineers / Business Analysts",
        confidentiality= "Internal - Restricted",
    )

    add_document_control(doc)

    toc_chapters = [
        # Part I
        ("I",   "PART I — System Architecture & Foundations",       "—"),
        ("1",   "Product Philosophy & Design Principles",           "5"),
        ("2",   "Application Architecture",                         "7"),
        ("3",   "Data Model & Full Schema Reference",               "10"),
        ("4",   "Performance Caching: buildDashCache",              "18"),
        ("5",   "Global Configuration & Settings Model",            "20"),
        # Part II
        ("II",  "PART II — Module Functional Specifications",       "—"),
        ("6",   "Executive Overview Dashboard",                     "23"),
        ("7",   "Live Insights & Analytics",                        "28"),
        ("8",   "Hierarchical Delivery Matrix",                     "32"),
        ("9",   "Gantt Timeline",                                   "38"),
        ("10",  "Weekly Scheduler & Conflict Resolver",             "42"),
        ("11",  "RAID Register",                                    "48"),
        ("12",  "Team Capacity Hub",                                "53"),
        ("13",  "Defect Tracker",                                   "57"),
        ("14",  "Reports & Board Packs",                            "62"),
        ("15",  "Audit Log & Activity Streams",                     "66"),
        ("16",  "Schedule Baselines",                               "70"),
        ("17",  "System Configuration",                             "74"),
        # Part III
        ("III", "PART III — Cross-Cutting Concerns",                "—"),
        ("18",  "Security & Data Privacy",                          "78"),
        ("19",  "Performance & Scalability Limits",                 "80"),
        ("20",  "Browser Compatibility Matrix",                     "81"),
        # Appendices
        ("A",   "Appendix A — Keyboard Shortcuts",                  "82"),
        ("B",   "Appendix B — Formula Reference Card",              "83"),
        ("C",   "Appendix C — Glossary",                            "85"),
    ]
    build_toc(doc, toc_chapters)

    # PART I
    add_section_divider(doc,"PART I","System Architecture & Foundations",
        "Application design, state model, data schemas, caching, and configuration.")
    print("  Writing Part I: Philosophy..."); part1_philosophy(doc)
    print("  Writing Part I: Architecture..."); part1_architecture(doc)
    print("  Writing Part I: Schemas..."); part1_schemas(doc)
    print("  Writing Part I: Cache..."); part1_cache(doc)
    print("  Writing Part I: Config..."); part1_config(doc)

    # PART II
    add_section_divider(doc,"PART II","Module Functional Specifications",
        "Complete specification of all 12 product modules — formulas, workflows, state machines, and business rules.")
    print("  Writing Ch 6: Overview..."); fsd_overview(doc)
    print("  Writing Ch 7: Insights..."); fsd_insights(doc)
    print("  Writing Ch 8: Delivery Matrix..."); fsd_delivery(doc)
    print("  Writing Ch 9: Gantt..."); fsd_gantt(doc)
    print("  Writing Ch 10: Scheduler..."); fsd_scheduler(doc)
    print("  Writing Ch 11: RAID..."); fsd_raid(doc)
    print("  Writing Ch 12: Team..."); fsd_team(doc)
    print("  Writing Ch 13: Defects..."); fsd_defects(doc)
    print("  Writing Ch 14: Reports..."); fsd_reports(doc)
    print("  Writing Ch 15: Audit Log..."); fsd_audit(doc)
    print("  Writing Ch 16: Baselines..."); fsd_baselines(doc)
    print("  Writing Ch 17: Config..."); fsd_config(doc)

    # PART III
    add_section_divider(doc,"PART III","Cross-Cutting Concerns",
        "Security, performance limits, browser compatibility, and error handling.")
    print("  Writing Part III: Cross-cutting concerns..."); part3_concerns(doc)

    # APPENDICES
    add_section_divider(doc,"APPENDICES","Reference Material",
        "Keyboard shortcuts, formula reference, and glossary.")
    print("  Writing Appendices..."); fsd_appendices(doc)

    print(f"\n  Saving document -> {OUT_PATH}")
    doc.save(OUT_PATH)
    print(f"\n  Done! FSD saved: {OUT_PATH}\n")
    return OUT_PATH


if __name__ == "__main__":
    build_fsd()
