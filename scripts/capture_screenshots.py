"""
capture_screenshots.py
Launches ProjectPulse in a headless Chromium browser, seeds rich demo data,
navigates to each view, and saves screenshots to docs/screenshots/.
"""

import os, json, time
from playwright.sync_api import sync_playwright

APP_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "projectpulse.html")
)
OUT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "docs", "screenshots")
)
os.makedirs(OUT_DIR, exist_ok=True)

# ── Rich demo state to seed into localStorage ──────────────────────────────
DEMO_STATE = {
    "name": "Phoenix Platform v2.0",
    "desc": "End-to-end rebuild of the core trading platform with modular GUI and API layers.",
    "settings": {
        "effortUnit": "hrs",
        "hoursPerDay": 8,
        "daysPerWeek": 5,
        "workDays": ["Mon","Tue","Wed","Thu","Fri"],
        "alertPrefs": {}
    },
    "dropdowns": {
        "status":    ["Not Started","In Progress","On Hold","Under Review","Completed","Cancelled"],
        "priority":  ["Critical","High","Medium","Low"],
        "category":  ["Feature","Bug","Improvement","Research","Documentation","DevOps","Testing","Design","Server Module","GUI Module","GUI Screen"],
        "module":    ["Account Management (AM)","Portfolio Management (PM)","Market Data","Shared Services","Core Engine","Authentication","User Interface","API Gateway","Analytics Service","Payment Module","Database Migration","Infrastructure"],
        "moduleType":["Server","GUI","Interface"],
        "role":      ["Engineering Manager","Lead Architect","Lead Frontend","Lead Design","Jr Lead UX","Jr Lead Research","Developer","Designer","QA","PM","DevOps","Analyst"],
        "memberStatus":["Active","On Leave","Other Assignment","Serving Notice Period","Departed"],
        "defectStatus":["New","Assigned","Fixed","Retest","Closed","Rejected","Deferred"],
        "defectPriority":["Critical","High","Medium","Low"],
        "defectSeverity":["S1 - Blocker","S2 - High","S3 - Medium","S4 - Low"],
        "defectType":["Functional Bug","UI/UX Issue","Performance","Security","Data Issue","Suggestion"],
        "complexity":["Easy","Medium","Complex"],
        "raidType":  ["Risk","Assumption","Issue","Dependency"],
        "raidImpact":["High","Medium","Low"],
        "raidProbability":["High","Medium","Low"],
        "raidSeverity":["S1 - Critical","S2 - Major","S3 - Moderate","S4 - Minor"],
        "raidStatus":["Identified","Active","Mitigated","Closed","Realized"],
        "decisionStatus":["Pending Sign-off","Approved","Rejected","Appealed"]
    },
    "complexityFactors": {"Easy": 0.5, "Medium": 1.0, "Complex": 1.5},
    "members": [
        {"id":"MEM-001","name":"Sarah Chen","role":"Engineering Manager","status":"Active","plannedLeaves":[]},
        {"id":"MEM-002","name":"Alex Rivera","role":"Lead Architect","status":"Active","plannedLeaves":[]},
        {"id":"MEM-003","name":"Jordan Kim","role":"Lead Frontend","status":"Active","plannedLeaves":[]},
        {"id":"MEM-004","name":"Maya Patel","role":"Lead Design","status":"Active","plannedLeaves":[]},
        {"id":"MEM-005","name":"Chris Thompson","role":"Developer","status":"Active","plannedLeaves":[]},
        {"id":"MEM-006","name":"Priya Sharma","role":"QA","status":"Active","plannedLeaves":[]},
        {"id":"MEM-007","name":"David Lee","role":"DevOps","status":"On Leave","plannedLeaves":[]},
        {"id":"MEM-008","name":"Emma Wilson","role":"Analyst","status":"Active","plannedLeaves":[]},
    ],
    "tasks": [
        {
            "id":"TASK-001","name":"Core Engine — Authentication Module","status":"Completed",
            "priority":"Critical","category":"Server Module","module":"Authentication","moduleType":"Server",
            "assignee":"Alex Rivera","release":"v1.0.0","startDate":"2026-01-06","dueDate":"2026-02-14",
            "actCompletionDate":"2026-02-12","baselineStartDate":"2026-01-06","baselineDueDate":"2026-02-14",
            "forecastDueDate":"2026-02-14","slippageReason":"","complexity":"Complex",
            "progress":100,"estEffort":120,"actEffort":110,"baselineEffort":120,"dependsOn":[],
            "notes":"JWT-based stateless auth, refresh token rotation, RBAC integration.","subtasks":[
                {"id":"ST-001","name":"JWT implementation","status":"Completed","category":"Feature","done":True,"effort":40,"actEffort":38,"progress":100,"type":"step","actCompletionDate":"2026-01-28"},
                {"id":"ST-002","name":"RBAC permission matrix","status":"Completed","category":"Feature","done":True,"effort":40,"actEffort":36,"progress":100,"type":"step","actCompletionDate":"2026-02-05"},
                {"id":"ST-003","name":"Refresh token rotation","status":"Completed","category":"Feature","done":True,"effort":40,"actEffort":36,"progress":100,"type":"step","actCompletionDate":"2026-02-12"},
            ],
            "guiScreens":[],"updatedAt":"2026-02-12T10:00:00Z","parentId":""
        },
        {
            "id":"TASK-002","name":"API Gateway — Rate Limiting & Routing","status":"Completed",
            "priority":"High","category":"Server Module","module":"API Gateway","moduleType":"Server",
            "assignee":"Alex Rivera","release":"v1.0.0","startDate":"2026-02-17","dueDate":"2026-03-14",
            "actCompletionDate":"2026-03-11","baselineStartDate":"2026-02-17","baselineDueDate":"2026-03-14",
            "forecastDueDate":"2026-03-14","slippageReason":"","complexity":"Complex",
            "progress":100,"estEffort":96,"actEffort":88,"baselineEffort":96,"dependsOn":["TASK-001"],
            "notes":"Kong-based gateway with Redis rate limiting, circuit breakers.","subtasks":[],"guiScreens":[],
            "updatedAt":"2026-03-11T10:00:00Z","parentId":""
        },
        {
            "id":"TASK-003","name":"Portfolio Management — Dashboard GUI","status":"In Progress",
            "priority":"Critical","category":"GUI Module","module":"Portfolio Management (PM)","moduleType":"GUI",
            "assignee":"Jordan Kim","release":"v1.1.0","startDate":"2026-03-17","dueDate":"2026-05-09",
            "actCompletionDate":"","baselineStartDate":"2026-03-17","baselineDueDate":"2026-04-25",
            "forecastDueDate":"2026-05-16","slippageReason":"Design revisions added 2 extra sprints.","complexity":"Complex",
            "progress":65,"estEffort":160,"actEffort":104,"baselineEffort":140,"dependsOn":["TASK-002"],
            "notes":"Real-time portfolio grid, P&L widgets, risk exposure charts.","subtasks":[
                {"id":"ST-004","name":"Portfolio grid component","status":"Completed","category":"GUI Screen","done":True,"effort":40,"actEffort":40,"progress":100,"type":"screen","actCompletionDate":"2026-04-04"},
                {"id":"ST-005","name":"P&L chart widget","status":"In Progress","category":"GUI Screen","done":False,"effort":48,"actEffort":32,"progress":67,"type":"screen","actCompletionDate":""},
                {"id":"ST-006","name":"Risk exposure heatmap","status":"Not Started","category":"GUI Screen","done":False,"effort":40,"actEffort":0,"progress":0,"type":"screen","actCompletionDate":""},
                {"id":"ST-007","name":"Responsive layout QA","status":"Not Started","category":"Feature","done":False,"effort":32,"actEffort":0,"progress":0,"type":"step","actCompletionDate":""},
            ],
            "guiScreens":["Portfolio Overview","P&L Dashboard","Risk Heatmap"],
            "updatedAt":"2026-06-10T10:00:00Z","parentId":""
        },
        {
            "id":"TASK-004","name":"Market Data — WebSocket Feed Integration","status":"In Progress",
            "priority":"High","category":"Feature","module":"Market Data","moduleType":"Interface",
            "assignee":"Chris Thompson","release":"v1.1.0","startDate":"2026-04-01","dueDate":"2026-05-30",
            "actCompletionDate":"","baselineStartDate":"2026-04-01","baselineDueDate":"2026-05-23",
            "forecastDueDate":"2026-05-30","slippageReason":"","complexity":"Complex",
            "progress":45,"estEffort":80,"actEffort":36,"baselineEffort":72,"dependsOn":["TASK-002"],
            "notes":"Live tick data streaming via WebSocket, Redis pub/sub.","subtasks":[],"guiScreens":[],
            "updatedAt":"2026-06-08T10:00:00Z","parentId":""
        },
        {
            "id":"TASK-005","name":"Analytics Service — Reporting Engine","status":"Not Started",
            "priority":"Medium","category":"Server Module","module":"Analytics Service","moduleType":"Server",
            "assignee":"Emma Wilson","release":"v1.2.0","startDate":"2026-06-01","dueDate":"2026-07-25",
            "actCompletionDate":"","baselineStartDate":"2026-06-01","baselineDueDate":"2026-07-25",
            "forecastDueDate":"2026-07-25","slippageReason":"","complexity":"Medium",
            "progress":0,"estEffort":64,"actEffort":0,"baselineEffort":64,"dependsOn":["TASK-003","TASK-004"],
            "notes":"Custom report builder, scheduled exports, BI connector APIs.","subtasks":[],"guiScreens":[],
            "updatedAt":"2026-06-01T10:00:00Z","parentId":""
        },
        {
            "id":"TASK-006","name":"Database Migration — Schema v2.0","status":"On Hold",
            "priority":"High","category":"DevOps","module":"Database Migration","moduleType":"Server",
            "assignee":"David Lee","release":"v1.1.0","startDate":"2026-04-14","dueDate":"2026-05-16",
            "actCompletionDate":"","baselineStartDate":"2026-04-14","baselineDueDate":"2026-05-16",
            "forecastDueDate":"2026-06-20","slippageReason":"Blocked on DBA resource availability (on leave).","complexity":"Complex",
            "progress":20,"estEffort":48,"actEffort":9,"baselineEffort":48,"dependsOn":["TASK-001"],
            "notes":"Flyway migrations, data integrity checks, rollback procedures.","subtasks":[],"guiScreens":[],
            "updatedAt":"2026-05-02T10:00:00Z","parentId":""
        },
        {
            "id":"TASK-007","name":"UI Design System — Component Library","status":"Completed",
            "priority":"High","category":"Design","module":"User Interface","moduleType":"GUI",
            "assignee":"Maya Patel","release":"v1.0.0","startDate":"2026-01-06","dueDate":"2026-03-07",
            "actCompletionDate":"2026-03-01","baselineStartDate":"2026-01-06","baselineDueDate":"2026-03-07",
            "forecastDueDate":"2026-03-07","slippageReason":"","complexity":"Medium",
            "progress":100,"estEffort":88,"actEffort":82,"baselineEffort":88,"dependsOn":[],
            "notes":"Figma token system, React component library, Storybook.","subtasks":[],"guiScreens":[],
            "updatedAt":"2026-03-01T10:00:00Z","parentId":""
        },
        {
            "id":"TASK-008","name":"Payment Module — PCI-DSS Integration","status":"Under Review",
            "priority":"Critical","category":"Feature","module":"Payment Module","moduleType":"Interface",
            "assignee":"Chris Thompson","release":"v1.2.0","startDate":"2026-05-04","dueDate":"2026-06-27",
            "actCompletionDate":"","baselineStartDate":"2026-05-04","baselineDueDate":"2026-06-27",
            "forecastDueDate":"2026-06-27","slippageReason":"","complexity":"Complex",
            "progress":80,"estEffort":120,"actEffort":96,"baselineEffort":120,"dependsOn":["TASK-001","TASK-002"],
            "notes":"Stripe integration, PCI tokenization, 3DS2 flows, webhook handler.","subtasks":[],"guiScreens":[],
            "updatedAt":"2026-06-11T10:00:00Z","parentId":""
        },
    ],
    "defects": [
        {"id":"DEF-001","title":"Login page fails on mobile Safari","type":"UI/UX Issue","severity":"S2 - High","priority":"High","status":"Assigned","linkedType":"task","linkedId":"TASK-001","assignee":"Jordan Kim","reporter":"Priya Sharma","desc":"Login form overflows viewport on iOS 17.","steps":"1. Open on iPhone 15\n2. Observe input overflow"},
        {"id":"DEF-002","title":"WebSocket drops after 30 min idle","type":"Functional Bug","severity":"S1 - Blocker","priority":"Critical","status":"In Progress","linkedType":"task","linkedId":"TASK-004","assignee":"Chris Thompson","reporter":"Priya Sharma","desc":"Connection lost after idle, no auto-reconnect.","steps":"1. Open market data feed\n2. Leave idle 30 min\n3. Observe disconnect"},
        {"id":"DEF-003","title":"Export PDF missing chart images","type":"Functional Bug","severity":"S2 - High","priority":"High","status":"Fixed","linkedType":"task","linkedId":"TASK-005","assignee":"Emma Wilson","reporter":"Sarah Chen","desc":"Charts are blank in exported PDF.","steps":"1. Generate report\n2. Export to PDF\n3. Open and inspect charts"},
        {"id":"DEF-004","title":"Portfolio grid sort flickers","type":"UI/UX Issue","severity":"S3 - Medium","priority":"Medium","status":"Retest","linkedType":"task","linkedId":"TASK-003","assignee":"Jordan Kim","reporter":"Priya Sharma","desc":"Column sort triggers visible re-render flash.","steps":"1. Open portfolio grid\n2. Click column header\n3. Observe flicker"},
        {"id":"DEF-005","title":"Payment webhook 502 on high load","type":"Performance","severity":"S1 - Blocker","priority":"Critical","status":"New","linkedType":"task","linkedId":"TASK-008","assignee":"","reporter":"Sarah Chen","desc":"Gateway returns 502 under 1000 rps stress test.","steps":"1. Run k6 load test\n2. Observe 502 spikes"},
    ],
    "raids": [
        {"id":"RAID-001","type":"Risk","title":"DBA resource dependency — single point of failure","status":"Active","probability":"High","impact":"High","severity":"S1 - Critical","owner":"Sarah Chen","mitigation":"Cross-train secondary DBA. Engage contractor.","targetDate":"2026-06-30","notes":""},
        {"id":"RAID-002","type":"Issue","title":"Market Data vendor API rate limits exceeded","status":"Active","probability":"High","impact":"High","severity":"S1 - Critical","owner":"Alex Rivera","mitigation":"Negotiate higher tier SLA. Implement local caching layer.","targetDate":"2026-06-20","notes":""},
        {"id":"RAID-003","type":"Assumption","title":"PCI audit window extends by 2 weeks","status":"Identified","probability":"Medium","impact":"High","severity":"S2 - Major","owner":"Sarah Chen","mitigation":"Pre-submit compliance documentation early.","targetDate":"2026-07-15","notes":""},
        {"id":"RAID-004","type":"Dependency","title":"Payment provider Stripe API v3 migration","status":"Active","probability":"Low","impact":"High","severity":"S2 - Major","owner":"Chris Thompson","mitigation":"Monitor Stripe changelog. Test against v3 sandbox.","targetDate":"2026-07-01","notes":""},
        {"id":"RAID-005","type":"Risk","title":"Team member attrition — Q3 hiring freeze","status":"Identified","probability":"Medium","impact":"Medium","severity":"S3 - Moderate","owner":"Sarah Chen","mitigation":"Knowledge transfer sessions. Document critical paths.","targetDate":"2026-08-01","notes":""},
    ],
    "baselines": [],
    "reports": [],
    "decisions": [],
    "releases": [
        {"id":"REL-001","version":"v1.0.0","name":"Foundation Release","status":"Released","date":"2026-03-15"},
        {"id":"REL-002","version":"v1.1.0","name":"Core Features","status":"In Progress","date":"2026-06-30"},
        {"id":"REL-003","version":"v1.2.0","name":"Analytics & Payments","status":"Planned","date":"2026-09-30"},
    ],
    "features": [],
    "log": [
        {"ts":"2026-06-14T04:00:00Z","user":"Sarah Chen","action":"Status Changed","taskId":"TASK-008","taskName":"Payment Module — PCI-DSS Integration","field":"status","oldVal":"In Progress","newVal":"Under Review","subtaskId":"","actCompletionDate":""},
        {"ts":"2026-06-13T09:30:00Z","user":"Alex Rivera","action":"Updated","taskId":"TASK-004","taskName":"Market Data — WebSocket Feed Integration","field":"progress","oldVal":"40","newVal":"45","subtaskId":"","actCompletionDate":""},
        {"ts":"2026-06-12T15:45:00Z","user":"Priya Sharma","action":"Created","taskId":"DEF-005","taskName":"Payment webhook 502 on high load","field":"status","oldVal":"","newVal":"New","subtaskId":"","actCompletionDate":""},
        {"ts":"2026-06-11T11:20:00Z","user":"Jordan Kim","action":"Status Changed","taskId":"TASK-003","taskName":"Portfolio Management — Dashboard GUI","field":"subtask.status","oldVal":"Not Started","newVal":"In Progress","subtaskId":"ST-005","actCompletionDate":""},
        {"ts":"2026-06-10T08:00:00Z","user":"Chris Thompson","action":"Updated","taskId":"TASK-008","taskName":"Payment Module — PCI-DSS Integration","field":"progress","oldVal":"72","newVal":"80","subtaskId":"","actCompletionDate":""},
    ],
    "cols": [],
    "defCols": [],
    "customFields": [],
    "defCustomFields": [],
    "stepTemplates": [],
    "fsHandle": None,
    "fsDirHandle": None,
    "fsDirName": "",
    "view": "dash",
    "theme": "nexus",
    "colorMode": "default",
    "filters": {},
    "sort": {},
    "defSort": {},
    "taskViewMode": "table",
    "cache": None,
}

VIEWS = [
    ("overview",  "01_overview_dashboard"),
    ("dash",      "01b_insights_analytics"),
    ("tasks",     "02_delivery_matrix"),
    ("timeline",  "03_gantt_timeline"),
    ("scheduler", "04_weekly_scheduler"),
    ("raid",      "05_raid_register"),
    ("team",      "06_team_capacity_hub"),
    ("defects",   "07_defect_tracker"),
    ("reports",   "08_reports_boardpack"),
    ("log",       "09_activity_audit_log"),
    ("admin",     "10_configuration_settings"),
]

def seed_and_screenshot(page, view_id, filename):
    """Set localStorage state, navigate to view, wait and screenshot."""
    state_json = json.dumps(DEMO_STATE)
    # Set localStorage BEFORE navigating so the app hydrates it
    page.evaluate(f"""() => {{
        localStorage.setItem('pp-data', JSON.stringify({state_json}));
    }}""")
    # Re-navigate to apply fresh state
    page.reload(wait_until="networkidle")
    # Wait for app to mount
    page.wait_for_selector("#main-app, #landing-page", timeout=15000)

    # If landing page is shown, try to enter the app
    try:
        enter_btn = page.locator("button:has-text('Enter'), button:has-text('Open'), #enter-app-btn").first
        if enter_btn.is_visible(timeout=2000):
            enter_btn.click()
            page.wait_for_selector("#main-app", timeout=8000)
    except Exception:
        pass

    # Switch to target view by calling setView in JS
    page.evaluate(f"() => {{ if(typeof setView === 'function') setView('{view_id}'); else if(typeof P !== 'undefined') {{ P.view='{view_id}'; if(typeof render === 'function') render(); }} }}")
    page.wait_for_timeout(2500)

    # Take full screenshot
    out_path = os.path.join(OUT_DIR, f"{filename}.png")
    page.screenshot(path=out_path, full_page=False)
    print(f"  ✓  {filename}.png")
    return out_path

def main():
    print(f"\n{'─'*60}")
    print("  ProjectPulse — Screenshot Capture")
    print(f"  App:    {APP_PATH}")
    print(f"  Output: {OUT_DIR}")
    print(f"{'─'*60}\n")

    file_url = f"file://{APP_PATH}"
    screenshots = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = browser.new_context(
            viewport={"width": 1600, "height": 900},
            device_scale_factor=2,  # Retina quality
        )
        page = context.new_page()

        # First navigate to load the app
        print("Loading app…")
        page.goto(file_url, wait_until="networkidle", timeout=30000)
        page.wait_for_timeout(2000)

        # Capture landing page
        try:
            out_path = os.path.join(OUT_DIR, "15_landing_page.png")
            page.screenshot(path=out_path)
            screenshots["15_landing_page"] = out_path
            print("  ✓  15_landing_page.png")
        except Exception as ex:
            print(f"  ✗  15_landing_page — {ex}")

        # Seed data once
        state_json = json.dumps(DEMO_STATE)
        page.evaluate(f"() => {{ localStorage.setItem('pp-data', JSON.stringify({state_json})); }}")
        page.reload(wait_until="networkidle")
        page.wait_for_timeout(3000)

        # Dismiss landing page if present
        try:
            btn = page.locator("button").filter(has_text="Enter").first
            if btn.is_visible(timeout=3000):
                btn.click()
                page.wait_for_timeout(1500)
        except Exception:
            pass
        try:
            btn = page.locator("[id*='enter'], [id*='start'], .enter-btn").first
            if btn.is_visible(timeout=1000):
                btn.click()
                page.wait_for_timeout(1500)
        except Exception:
            pass

        print("Capturing views…\n")
        for view_id, fname in VIEWS:
            try:
                page.evaluate(f"() => {{ try {{ setView('{view_id}') }} catch(e) {{ P.view='{view_id}'; render(); }} }}")
                page.wait_for_timeout(2800)
                out_path = os.path.join(OUT_DIR, f"{fname}.png")
                page.screenshot(path=out_path)
                screenshots[fname] = out_path
                print(f"  ✓  {fname}.png")
            except Exception as ex:
                print(f"  ✗  {fname} — {ex}")

        print("\nCapturing interactive flyouts…\n")

        # 11. Task Flyout
        try:
            page.evaluate("() => { try { setView('tasks'); openFlyout('TASK-003', 'edit'); } catch(e) { P.view='tasks'; openFlyout('TASK-003', 'edit'); } }")
            page.wait_for_timeout(1500)
            out_path = os.path.join(OUT_DIR, "11_add_task_flyout.png")
            page.screenshot(path=out_path)
            screenshots["11_add_task_flyout"] = out_path
            print("  ✓  11_add_task_flyout.png")
            # Close task flyout
            page.evaluate("() => { try { closeAddTask(); } catch(e) {} }")
        except Exception as ex:
            print(f"  ✗  11_add_task_flyout — {ex}")

        # 12. Defect Flyout
        try:
            page.evaluate("() => { try { setView('defects'); openDefectModal('DEF-001'); } catch(e) { P.view='defects'; openDefectModal('DEF-001'); } }")
            page.wait_for_timeout(1500)
            out_path = os.path.join(OUT_DIR, "12_add_defect_flyout.png")
            page.screenshot(path=out_path)
            screenshots["12_add_defect_flyout"] = out_path
            print("  ✓  12_add_defect_flyout.png")
            # Close defect flyout
            page.evaluate("() => { try { closeDefectFlyout(); } catch(e) {} }")
        except Exception as ex:
            print(f"  ✗  12_add_defect_flyout — {ex}")

        # 13. RAID Flyout
        try:
            page.evaluate("() => { try { setView('raid'); openRaidModal('RAID-001'); } catch(e) { P.view='raid'; openRaidModal('RAID-001'); } }")
            page.wait_for_timeout(1500)
            out_path = os.path.join(OUT_DIR, "13_add_raid_flyout.png")
            page.screenshot(path=out_path)
            screenshots["13_add_raid_flyout"] = out_path
            print("  ✓  13_add_raid_flyout.png")
            # Close RAID flyout
            page.evaluate("() => { try { closeRaidFlyout(); } catch(e) {} }")
        except Exception as ex:
            print(f"  ✗  13_add_raid_flyout — {ex}")

        # 14. Member Flyout
        try:
            page.evaluate("() => { try { setView('team'); openAddMember('MEM-001'); } catch(e) { P.view='team'; openAddMember('MEM-001'); } }")
            page.wait_for_timeout(1500)
            out_path = os.path.join(OUT_DIR, "14_add_member_flyout.png")
            page.screenshot(path=out_path)
            screenshots["14_add_member_flyout"] = out_path
            print("  ✓  14_add_member_flyout.png")
            # Close member flyout by removing class "on" or clicking close
            page.evaluate("() => { try { $id('member-flyout').classList.remove('on'); } catch(e) {} }")
        except Exception as ex:
            print(f"  ✗  14_add_member_flyout — {ex}")

        context.close()
        browser.close()

    print(f"\n✅  Done — {len(screenshots)} screenshots saved to:\n   {OUT_DIR}\n")
    return screenshots

if __name__ == "__main__":
    main()
