# ProjectPulse

ProjectPulse is a monolithic, local-first project management suite built entirely using Vanilla HTML5, JavaScript, and CSS (~35,000 lines of code). It features a highly interactive and high-density interface with 20 curated themes, light/dark mode overrides, offline persistence, and automated documentation compilation.

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
├── projectpulse.html            # Monolithic single-page application (UI & Business Logic)
│   ├── CSS Stylesheet           # (Lines 1 – 8,960) 20 Curated Themes, layout, and animations
│   └── JavaScript Application   # (Lines 8,960 – 35,000+) Global state, Excel sync, Gantt chart, Widgets
├── docs/                        # Compiled high-fidelity Word documents, presentations, and guides
│   ├── user_manual/             # Markdown user manuals and configuration guides
│   ├── screenshots/             # Cropped screenshots taken automatically by Puppeteer
│   └── *.docx, *.pptx           # Master product briefs and specifications
├── scripts/                     # Python/JS compilers and automation tools
│   ├── build_all.py             # Master compiler orchestrator
│   ├── build_fsd.py             # Functional Specification Document (.docx) compiler
│   ├── build_pcd.py             # Product Capabilities Document (.docx) compiler
│   ├── build_umi.py             # User Manual Index (.docx) compiler
│   ├── build_user_manual_docx.py# User Manual (.docx) compiler
│   ├── capture_screenshots.py   # Puppeteer script for page screenshots
│   ├── capture_widgets.py       # Puppeteer script for individual widget screenshot crops
│   ├── check_syntax.py          # Syntax validator script
│   └── update_manual.js         # Configuration parser and sync utility
├── project-context/             # In-depth architectural & state schema context
│   ├── README.md                # Authoritative state schema mapping and business rules
│   ├── CHANGELOG.md             # Project milestones and release changelog
│   └── architecture_audit.md    # Codebase quality and refactoring assessment
└── graphify-out/                # Knowledge graph files for codebase navigation
```

---

## 🛠️ Key Features

- **High-Density Swiss UI Design**: Modular dashboard widgets, interactive Gantt charts, customized bento-grid layouts, and custom-drawn themes.
- **Offline-First Storage System**:
  - **Tier 1 (LocalStorage)**: Primary application state, tables, and settings.
  - **Tier 2 (IndexedDB)**: State snapshots, backups, and file handle tracking.
  - **Tier 3 (File System Access API)**: Synchronized local Excel workbooks and background file backups.
- **Calculated Metric Engine**: Real-time project health scores, delivery confidence meters, and dependency path tracking.
- **Defect and RAID Logs**: Embedded trackers mapping defects directly to tasks, features, and team members.

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
