# ProjectPulse Quick Reference

## 🚀 Common Commands
- `Cmd+K`: Open Command Palette.
- `Cmd+S`: Force save project state.
- `Cmd+,`: Open Settings/Registry.
- `Esc`: Close any active modal/flyout.

## 🎨 Design Tokens (CSS Variables)
Use these in any new component or style modification:
- `var(--color-primary)`: Main brand color.
- `var(--color-surface)`: Background for cards/modals.
- `var(--color-text)`: Primary text color.
- `var(--color-divider)`: Subtle border color.
- `var(--radius-lg)`: Standard rounded corner (16px).

## 📊 Core State (`P`)
- `P.tasks`: List of all tasks.
- `P.members`: Team members.
- `P.view`: Current view ID.
- `P.theme`: Active theme ID.

## 💾 Storage
- **Primary**: LocalStorage (`pp-data`).
- **Backup**: IndexedDB (Last 10 snapshots).
- **Sync**: Local Directory (if linked).

---
*For full details, see the [Project Context Pack](./project-context/index.md).*
