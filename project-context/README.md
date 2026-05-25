# ProjectPulse — AI Context Pack

> **Single-file project management suite** (28,800 lines). Vanilla JS/HTML5/CSS3.
> Local-first persistence (localStorage + IndexedDB + File System Access API + ExcelJS).
> 20 premium themes. Offline-capable via `./lib/` assets.

## CONTEXT FILES
| File | What to read it for |
|:---|:---|
| `01-state-and-schemas.md` | Adding/changing any `P` property, entity field, or setting |
| `02-functions-and-views.md` | Finding functions, understanding views, tracing features |
| `03-data-and-persistence.md` | Save/load, Excel import/export, business rules, migrations |
| `04-risks-and-backlog.md` | Architecture constraints, known issues, enhancement roadmap |
| `CHANGELOG.md` | History of all changes (append-only) |

## ARCHITECTURE AT A GLANCE
```
projectpulse.html (single file)
├── CSS (lines 1–8960)        — Theme vars, layout, animations, print styles
├── JS  (lines 8960–28800)    — All application logic
│   ├── Constants & Helpers    — STATUSES, PRIORITIES, THEMES, fmtDate, esc, etc.
│   ├── Global P object        — Single source of truth (~L9489)
│   ├── Persistence            — save/load/getDB/exportExcel (~L10048)
│   ├── CRUD                   — createTask/updateField/deleteTask (~L11177)
│   ├── View Renderers         — renderTasksView/renderDash/renderTeam (~L11744+)
│   ├── Dashboard Engine       — buildDashCache O(n) + renderDash O(1) (~L18000)
│   ├── Report Engine          — renderReportSection widgets (~L15200)
│   ├── Excel Engine           — generateProjectWorkbook/reconstructProjectFromBuffer (~L22000)
│   ├── Scaffolder             — 3-step Project Architect (~L24886)
│   └── Startup & Init         — DOMContentLoaded, enterApp, render (~L28500)
└── lib/ (offline assets)      — Lucide, Phosphor, ExcelJS, Google Fonts woff2
```

## GLOSSARY
| Term | Meaning |
|:---|:---|
| **P** | Global state object. All data + UI prefs. Persisted to `pp-data` in localStorage |
| **Module** | High-level task grouping (e.g., "Core Engine", "Admin GUI") |
| **Subtask** | Granular step within a task. Types: `step` or `screen` |
| **GUI Screen** | Subtask of type `screen` — represents a UI component |
| **Blueprint** | Reusable step template applied to tasks by category |
| **Scaffolder** | 3-step bulk task generator (Blueprint → Screens → Features) |
| **Flyout** | Drawer overlay (task flyout, theme flyout, alerts panel) |
| **Registry** | Global lookup lists (Statuses, Priorities, Modules, etc.) in `P.dropdowns` |
| **dashCache** | Pre-computed O(n) index built by `buildDashCache()` for O(1) widget rendering |
| **mkCC()** | Card Component Constructor — builds all dashboard/report widget cards |
| **LS/IDB/FS** | localStorage / IndexedDB / File System Access API |

## AI DEVELOPMENT RULES
1. **Never simplify** — the app is designed for high-density complex workflows
2. **Vanilla JS only** — no React/Vue/external frameworks
3. **Use CSS vars** — `var(--color-primary)` not hex values
4. **Persistence parity** — new `P` properties must appear in `save()`, Excel export, and `reconstructProjectFromBuffer()`
5. **Update this pack** — after any structural change, update `01-state-and-schemas.md` and append to `CHANGELOG.md`
6. **Don't break Excel round-trips** — changes to `PROJECT_SCHEMA` or `PROJECT_RELATIONAL_MODEL` must be reflected in export/import

## SEARCH PATTERNS
```bash
# Find a view renderer
grep "function render[ViewName]" projectpulse.html

# Find state mutations
grep "P\.\[property\] =" projectpulse.html

# Find persistence touchpoints
grep "save()" projectpulse.html

# Find widget definitions
grep "mkCC(" projectpulse.html

# Find keyboard shortcuts
grep "isMod &&" projectpulse.html

# Find all function definitions
grep -n "function [a-zA-Z]" projectpulse.html | head -50
```

## KEYBOARD SHORTCUTS
| Key | Action |
|:---|:---|
| `Cmd/Ctrl+K` | Command Palette |
| `Cmd/Ctrl+S` | Manual Save |
| `Cmd/Ctrl+,` | Settings |
| `Cmd/Ctrl+O` | Open Project Directory |
| `Cmd/Ctrl+N` | New Task |
| `1-7` | Switch views (Tasks, Timeline, Team, Log, Reports, Dash, Defects) |
| `?` | View-specific Help |
| `Esc` | Close active modal/flyout |
