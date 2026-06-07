# Reports & Stakeholder Board Packs

ProjectPulse features an automated report generation utility that compiles real-time progress metrics into print-ready PDF formats or structured spreadsheets.

---

## 1. Executive Board Pack Generator

The Board Pack compiles status information across the entire project:
- **Project Summary Narrative**: High-level textual status updates.
- **Aggregated Health Indicators**: Trend graph of weekly health metrics.
- **Critical Path Highlights**: Tasks on the critical path that are nearing or past their due dates.
- **Top 5 Risks**: Ranked by risk exposure score ($Probability \times Impact$).

---

## 2. Spreadsheet Export Settings (ExcelJS)

Excel reports are generated using the `ExcelJS` client library. The exporter formats cells with professional colors and highlights:
- **Metadata Header**: Project Name, Export Date, and Author.
- **Color Coding**:
  - Green (`#0F5132` / `#D1E7DD`) for completed tasks and low risks.
  - Yellow (`#664D03` / `#FFF3CD`) for in-progress tasks or medium risks.
  - Red (`#842029` / `#F8D7DA`) for blocked tasks or critical issues.
- **Formulas**: Spreadsheet cells contain actual Excel formulas (e.g., `SUM`, `AVERAGE`) rather than static text where applicable, maintaining functional usability.
