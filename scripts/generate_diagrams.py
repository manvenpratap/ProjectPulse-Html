#!/usr/bin/env python3
"""
generate_diagrams.py
====================
Uses Playwright to capture high-res cropped screenshots of each diagram
from lib/diagrams.html.
Saves them to docs/screenshots/diagrams/.
"""

import os
import shutil
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
HTML_PATH = os.path.join(BASE_DIR, "lib", "diagrams.html")
OUT_DIR = os.path.join(BASE_DIR, "docs", "screenshots", "diagrams")
os.makedirs(OUT_DIR, exist_ok=True)

DIAGRAM_IDS = [
    "system_architecture",
    "task_lifecycle",
    "defect_lifecycle",
    "raid_lifecycle",
    "evm_calculation",
    "sandbox_workflow",
    "gantt_dependencies",
    "scheduler_workflow",
    "baseline_workflow",
    "report_workflow"
]

OVERRIDE_MAP = {
    "system_architecture": "Browser-Native_Project_Intelligence_Overview.png",
    "evm_calculation": "Project_Management_EVM_Intelligence_Pipeline.png",
    "scheduler_workflow": "Automated_Schedule_Conflict_Resolution_Engine.png"
}

STITCH_MAP = {
    "system_architecture": "projectpulse_client_side_spa_system_architecture_diagram",
    "task_lifecycle": "task_lifecycle_state_machine_transition_guards_diagram",
    "defect_lifecycle": "defect_lifecycle_verification_pipeline_diagram",
    "raid_lifecycle": "raid_threat_register_mitigation_cycle_infographic",
    "evm_calculation": "earned_value_management_evm_performance_curves_chart",
    "sandbox_workflow": "executive_what_if_sandbox_lifecycle_process_flow",
    "gantt_dependencies": "gantt_bezier_dependencies_cascading_reschedule_diagram",
    "scheduler_workflow": "capacity_copilot_auto_resolve_cycle_diagram",
    "baseline_workflow": "schedule_baseline_snapshot_restorative_loop_diagram",
    "report_workflow": "report_compilation_board_pack_export_pipeline_diagram",
}

def main():
    print("Generating workflow and lifecycle diagrams...")
    file_url = f"file://{HTML_PATH}"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = browser.new_context(
            viewport={"width": 1200, "height": 1000},
            device_scale_factor=2  # High resolution / retina
        )
        page = context.new_page()
        page.goto(file_url, wait_until="networkidle")

        for diag_id in DIAGRAM_IDS:
            out_path = os.path.join(OUT_DIR, f"{diag_id}.png")
            
            # 1. Try to copy from stitch design assets first
            copied_from_stitch = False
            if diag_id in STITCH_MAP:
                stitch_prefix = STITCH_MAP[diag_id]
                stitch_dir = os.path.join(BASE_DIR, "docs", "stitch_projectpulse_design_assets")
                if os.path.exists(stitch_dir):
                    found_dir = None
                    for name in os.listdir(stitch_dir):
                        if name.startswith(stitch_prefix) and os.path.isdir(os.path.join(stitch_dir, name)):
                            found_dir = name
                            break
                    if found_dir:
                        src_path = os.path.join(stitch_dir, found_dir, "screen.png")
                        if os.path.exists(src_path):
                            try:
                                shutil.copy(src_path, out_path)
                                print(f"  ✓  Copied premium stitch design for {diag_id}.png")
                                copied_from_stitch = True
                                continue
                            except Exception as e:
                                print(f"  ✗  Failed to copy stitch asset for {diag_id}: {e}")
            
            if copied_from_stitch:
                continue

            # 2. Check if there is a premium custom override in the docs folder
            if diag_id in OVERRIDE_MAP:
                src_filename = OVERRIDE_MAP[diag_id]
                src_path = os.path.join(BASE_DIR, "docs", src_filename)
                if os.path.exists(src_path):
                    try:
                        shutil.copy(src_path, out_path)
                        print(f"  ✓  Copied premium custom infographic for {diag_id}.png")
                        continue
                    except Exception as e:
                        print(f"  ✗  Failed to copy override for {diag_id}: {e}")

            # 3. Fallback to Playwright screenshot
            try:
                elem = page.locator(f"#{diag_id}").first
                if elem.is_visible():
                    elem.screenshot(path=out_path)
                    print(f"  ✓  Captured {diag_id}.png")
                else:
                    print(f"  ✗  Element #{diag_id} not visible")
            except Exception as e:
                print(f"  ✗  Failed to capture #{diag_id}: {e}")

        context.close()
        browser.close()
    print("Diagram generation completed.\n")

if __name__ == "__main__":
    main()

