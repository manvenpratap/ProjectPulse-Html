# Defect Tracker & Bug Lifecycle

The **Defect Tracker** enables QA teams and developers to log, categorize, prioritize, and verify issues identified during testing cycles.

---

## 1. Defect Severity Matrix

Defects are assigned a severity level that determines their impact on the project health score:

| Severity Level | Definition | Impact on Health Index | Target SLA |
| :--- | :--- | :--- | :--- |
| **Blocker** | Critical function completely broken; no workaround. | `-10%` per active blocker | 24 Hours |
| **Critical** | Major functionality affected; temporary workaround exists. | `-5%` per active critical | 48 Hours |
| **Major** | Significant issue with clear, stable workarounds. | `-2%` per active major | 5 Days |
| **Minor** | Trivial issue (cosmetic, spelling error, etc.). | `-0.5%` per active minor | 10 Days |

---

## 2. Bug Lifecycle States

ProjectPulse logs defects through the following lifecycle flow:

```
[New] ──► [Assigned] ──► [In Progress] ──► [Fixed] ──► [Verified] ──► [Closed]
                                            │
                                            └─► [Failed QA Re-test] ──┐
                                                      ▲               │
                                                      └───────────────┘
```

- **New**: Logged but not yet triaged.
- **Assigned**: Owner allocated from the Capacity Hub.
- **Fixed**: Remediated by development; awaiting validation.
- **Verified**: QA confirmed resolution.
- **Closed**: Permanently closed.
- **Re-opened**: Failed verification; sent back to development.
