# Software Deliveries & Deployment Schedule

The **Software Deliveries & Deployment Schedule** (View 3) is ProjectPulse's dedicated release governance workstation. It provides complete lifecycle visibility into software deliverables, Application Lifecycle Management (ALM) / Production Deployment Notification (PDN) tracking, multi-entity task and screen linkage, verification sign-offs, and deployment cycle lead times.

---

## 1. Overview & Core Mission

While the [Task Matrix & Gantt Timeline](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/docs/user_manual/tasks.md) manages internal work breakdown structures and hours, the **Deliveries Module** governs external and production deployment milestones. It bridges the gap between engineering tasks and release management:

- **Deployment Tracking**: Monitor releases across multi-tier deployment environments (Development, UAT, Staging, Production).
- **ALM / PDN Change Governance**: Directly record and track enterprise ALM identifiers and PDN ticket numbers.
- **Verification Sign-Offs**: Enforce strict approval gates, designated approvers, and smoke test outcomes prior to release closure.
- **Cycle Lead Time & Variance**: Automatically measure the duration from scheduled target date to actual deployment completion date.

---

## 2. Core Delivery Entity Schema

Each delivery record in the system contains the following standardized attributes:

| Field | Key | Type | Description |
| :--- | :--- | :--- | :--- |
| **Delivery ID** | `id` | String | Unique identifier (e.g., `DEL-001`). |
| **Delivery Name** | `name` | String | Descriptive title of the deliverable or release package. |
| **Module** | `module` | Dropdown | Functional project module (e.g., `Core`, `Auth`, `Billing`, `Reporting`). |
| **Target Version** | `version` | Dropdown | Release version milestone (e.g., `v1.0.0`, `v1.1.0-RC1`). |
| **Release Date** | `targetDate` | Date | Scheduled delivery or deployment date. |
| **Actual Date** | `actualDate` | Date | Actual completion date in production or staging. |
| **Environment** | `environment` | Dropdown | Deployment environment (`Dev`, `UAT`, `Staging`, `Production`). |
| **Status** | `status` | Dropdown | Release lifecycle state: `Draft`, `Scheduled`, `Ready for Staging`, `Staged`, `In Production`, `Verified`, `Deferred`, `Cancelled`. |
| **Risk Level** | `risk` | Dropdown | Qualitative delivery risk assessment: `Low`, `Medium`, `High`, `Critical`. |
| **Approver** | `approver` | Dropdown | Lead engineer, release manager, or QA sign-off authority. |
| **Smoke Test** | `smokeTest` | Dropdown | Post-deployment smoke test result: `Passed`, `Failed`, `Pending`, `Skipped`. |
| **ALM / PDN #** | `almNumber` | String | Enterprise change request or tracking ticket ID. |
| **Linked Tasks** | `linkedTaskIds` | Array | References to parent tasks implementing this release. |
| **Linked Screens**| `linkedScreenIds`| Array | References to granular UI screen subtasks included in this deliverable. |
| **Notes** | `notes` | Text | Deployment remarks, release notes, and deployment runbook links. |

---

## 3. Multi-Entity Linkage

ProjectPulse provides bi-directional linkage between software deliveries and implementation artifacts:

1. **Parent Task Linkage (`linkedTaskIds`)**:
   - Associate one or multiple parent tasks (WBS items) with a single deployment package.
   - The delivery row renders interactive badge chips linking directly to the underlying tasks.
2. **Granular Screen Linkage (`linkedScreenIds`)**:
   - Link specific screen IDs (e.g., `SCR-01`, `SCR-02`) to ensure that all UI screens required for a release are accounted for.
3. **Automated Linkage Engine (`autoIdentifyDeliveryLink`)**:
   - ProjectPulse includes an automated inference engine that scans task names, module codes, and screen specifications to automatically propose or create linkages between unlinked deliveries and matching project tasks.

---

## 4. Visual Perspectives: Grid vs. Heatmap

The workstation features two synchronized operational perspectives toggled via the toolbar:

### A. Table Grid View (`renderDeliveriesTable`)
- High-density data grid with color-coded status badges, risk pills, and date indicators.
- Quick inline cell editing for instant attribute adjustment.
- Visual status indicators:
  - 🟢 **Verified / In Production**: Active in production environments.
  - 🔵 **Ready for Staging / Staged**: Under active QA/UAT validation.
  - 🟡 **Scheduled / Draft**: Upcoming pipeline deliverables.
  - 🔴 **Deferred / Cancelled / Critical Risk**: Blocked or high-attention releases.

### B. Visual Perspective Heatmap (`renderDeliveryHeatmapView`)
- Visual distribution matrix grouping deliveries into interactive swimlanes.
- **Dynamic Pivots**:
  - **By Module**: Groups releases horizontally across functional modules.
  - **By Target Version**: Groups releases by upcoming sprint releases and milestone roadmaps.
  - **By Deployment Phase**: Visualizes delivery flow across lifecycle stages (`Draft` $\rightarrow$ `Staging` $\rightarrow$ `Production` $\rightarrow$ `Verified`).
- Includes delivery count chips, risk density badges, and overdue release warnings.

---

## 5. Row Actions, Context Menus & Detail Flyout Drawer

The Deliveries table is designed for maximum efficiency:

1. **3-Dot Action Menu**:
   - Positioned cleanly at the end of each row, providing instant access to actions on both desktop and mobile touchscreens.
2. **Right-Click Context Menu (`showDeliveryCtx`)**:
   - Right-clicking any row activates a quick context menu with direct status transitions (`Mark Verified`, `Stage Release`, `Defer`), instant deletion, and task association tools.
3. **Slide-Out Detail Flyout Drawer (`openDeliveryFlyout`)**:
   - Clicking a delivery row opens a comprehensive slide-out panel featuring:
     - Full delivery telemetry and status history.
     - Interactive linked task badges with progress indicators.
     - Verification sign-off details and smoke test execution notes.
     - ALM/PDN tracking numbers and release documentation links.

---

## 6. Intelligent 5-Strategy Column Autofit Engine

To support various monitor aspect ratios, tablet layouts, and data densities, the deliveries table supports ProjectPulse's 5-strategy autofit engine (`P.autofitStrategy`):

- **Clip & Wrap (`clip_wrap`)**: Standard table layout with soft text-wrapping on titles and remarks.
- **Clip & No-Wrap (`clip_nowrap`)**: High-density single-line layout with ellipsis truncation.
- **Wrap & Balance (`wrap_balance`)**: Multi-line expansion optimized for lengthy release notes.
- **Fill & Distribute (`fill_distribute`)**: Proportionally stretches columns across 100% of widescreen displays.
- **Natural Scroll (`natural_scroll`)**: Content-measured natural column widths with a smooth horizontal scroll container.

---

## 7. Excel Telemetry Import & Export Synchronization

The Deliveries subsystem is fully integrated with the ProjectPulse Excel engine (`PulseExcel`):

- **Worksheet Export (`PulseExcel.buildDeliveriesSheet`)**: Automatically exports a dedicated, styled `Deliveries` worksheet containing all delivery records, linked tasks, ALM/PDN numbers, approval signatures, and test statuses.
- **Worksheet Import**: The import engine dynamically maps incoming Excel columns with normalized header resolution (supporting variations like `ALM #`, `ALM Number`, `PDN`, `Linked Tasks`, `Smoke Test Result`), ensuring flawless two-way data round-trips without data loss.
