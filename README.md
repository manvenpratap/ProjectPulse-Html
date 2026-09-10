# ProjectPulse

ProjectPulse is a monolithic, local-first project management workstation built entirely using Vanilla HTML5, JavaScript, and CSS (~80,800 lines of code). It features a highly interactive and high-density interface with 20 curated themes, light/dark mode overrides, offline persistence, bi-directional Excel synchronization, and automated documentation compilation.

---

## 🚀 Quick Start

Since ProjectPulse is a self-contained single-page application, you can run it in multiple ways:

1. **Direct Execution**: Simply double-click and open [projectpulse.html](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/projectpulse.html) in any modern web browser.
2. **Local HTTP Server**:
   ```bash
   # Using Node.js
   npx serve .
   
   # Using Python
   python -m http.server 8000
   ```
   Then open `http://localhost:8000/projectpulse.html` in your browser.

---

## 📦 Repository Structure

The ProjectPulse repository is structured as follows:

```
ProjectPulse/
├── projectpulse.html            # Monolithic single-page application (~80,800 lines Vanilla HTML5/JS/CSS)
│   ├── CSS Stylesheet           # (Lines 88 – 14,600) 20 Curated Themes, layout, tokens, and animations
│   └── JavaScript Application   # (Lines 14,605 – 80,835) Global state, Excel sync, Deliveries, Gantt, Scheduler
├── docs/                        # Compiled high-fidelity Word documents, presentations, and guides
│   ├── user_manual/             # Dynamic markdown user manuals & configuration references
│   ├── screenshots/             # Cropped screenshots captured automatically by Puppeteer
│   ├── stitch_projectpulse_design_assets/ # UI design components and specs
│   └── *.docx, *.pptx           # Master product briefs, FSD, PCD, and presentation decks
├── scripts/                     # Modular documentation compiler & maintenance toolchain
│   ├── build_all.py             # Master orchestrator for doc compilation
│   ├── build_fsd.py             # Functional Specification Document (.docx) compiler
│   ├── build_pcd.py             # Product Capabilities Document (.docx) compiler
│   ├── build_umi.py             # User Manual Index (.docx) compiler
│   ├── build_user_manual_docx.py# User Manual (.docx) compiler
│   ├── capture_screenshots.py   # Puppeteer script for full-page screenshots
│   ├── capture_widgets.py       # Puppeteer script for individual widget screenshot crops
│   ├── check_syntax.py          # AST JavaScript syntax validator script
│   ├── docx_helpers.py          # Shared Word document styling, tables, XML helpers
│   ├── generate_diagrams.py     # Generates light-themed vector diagrams for document embedding
│   ├── patch_health_gauge.py    # Health gauge SVG animation patcher
│   ├── patch_steering_hero.py   # Steering hero component patcher
│   ├── schedule_manual_update.js# Scheduled task runner for documentation updates
│   └── update_manual.js         # Configuration parser and sync utility
├── project-context/             # In-depth architectural & state schema context
│   ├── README.md                # Authoritative state schema mapping and business rules
│   ├── CHANGELOG.md             # Project milestones and release changelog
│   └── architecture_audit.md    # Codebase quality and refactoring assessment
└── graphify-out/                # Knowledge graph files for AST codebase navigation
    ├── GRAPH_REPORT.md          # Architecture report detailing god nodes and modular clusters
    ├── graph.html               # Interactive visual graph explorer
    └── graph.json               # Graph structure dataset (nodes & edges)
```

---

## 🛠️ Key Features & 10 Operational Views

1. **Executive Overview Dashboard**: Health Index dial, Delivery Confidence meter, active RAID count, and What-If Predictive Sandbox for real-time scenario simulation.
2. **Live Insights & Velocity Analytics**: Performance cache (`buildDashCache`), 4-week moving velocity averages, Earned Value Management (EVM), and burn-up/down trajectories.
3. **Software Deliveries & Deployment Schedule**: Dedicated ALM / PDN release workstation, multi-entity linkage to parent tasks and screen specs, cycle lead time & variance metrics, smoke test sign-offs, and interactive visual perspective heatmaps (pivoting by Module, Target Version, or Phase).
4. **Reports & Board Packs**: One-click executive summaries, weekly stakeholder packs, milestone checklists, and filtered multi-tab Excel export.
5. **Intelligent Weekly Scheduler & Conflict Resolver**: Interactive resource heatmap grid, automated conflict detection, and heuristics (Auto-Sequence, Reassignment, Cascading Date Shifting).
6. **Unified RAID Register**: Risk, Assumption, Issue, and Dependency scoring, threat matrices, mitigation owners, and due dates.
7. **Hierarchical Task Matrix & Interactive Gantt Timeline**: Multi-tier WBS hierarchy, Fibonacci complexity estimation scaling, spreadsheet-style inline cell editing, and SVG Gantt chart with interactive dependency paths.
8. **Team Capacity Hub**: Real-time FTE load distribution, leave schedules, role quotas, and cross-project utilization balancing.
9. **Defect Tracker**: QA bug logging, severity/priority matrices, direct task linkage, and resolution lifecycle tracking.
10. **Audit & Activity Log**: Chronological change journaling, state transition tracking, and forensic project history.

### Core Capabilities:
- **Intelligent 5-Strategy Column Autofit Engine**: Instant layout adaptation across all data tables (`clip_wrap`, `clip_nowrap`, `wrap_balance`, `fill_distribute`, `natural_scroll`).
- **Offline-First Storage Tier**: LocalStorage (`pp-data`), IndexedDB (`ProjectPulseDB`) with automatic snapshot rotations, and File System Access API for local workbook sync.
- **Bi-Directional Excel Synchronization**: Production-grade ExcelJS engine generating multi-tab relational workbooks and round-trip state reconstruction.
- **High-Density Swiss UI Design**: 20 curated themes, dark/light mode toggle, and micro-interaction animations.

---

## 📖 Documentation Build System

ProjectPulse compiles its documentation suite directly from the source code configuration:

1. **Update Configurations**:
   ```bash
   node scripts/update_manual.js
   ```
2. **Build All Documents**:
   ```bash
   python scripts/build_all.py
   ```

---

## 🛠️ Developer Guidelines

- **Syntax Validation**: Before committing JavaScript or HTML changes, validate the file syntax:
  ```bash
  python scripts/check_syntax.py
  ```
- **Knowledge Graph Maintenance**: After modifying any code files, update the local AST knowledge graph:
  ```bash
  graphify update .
  ```

For full details on the `P` state object, entity schemas, and core function registry, please read the [Developer Context Pack](file:///Users/manvenpratapsingh/Downloads/ProjectPulse/project-context/README.md).
