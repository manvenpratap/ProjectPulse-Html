#!/usr/bin/env python3
"""
generate_diagrams.py
====================
Uses Playwright to capture high-res cropped screenshots of each diagram
from lib/diagrams.html.
Saves them to docs/screenshots/diagrams/.
"""

import os
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
            try:
                elem = page.locator(f"#{diag_id}").first
                if elem.is_visible():
                    out_path = os.path.join(OUT_DIR, f"{diag_id}.png")
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
