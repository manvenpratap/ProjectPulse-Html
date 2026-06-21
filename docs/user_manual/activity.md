# Audit Log & Activity Streams

ProjectPulse maintains an immutable log of state modifications within the active browser session, helping managers track history and audit changes.

---

## 1. Automated Action Logging

Any CRUD action on tasks, resources, RAID items, or defects triggers an entry in the Activity Stream:
- **Timestamp**: Recorded down to the millisecond.
- **User Identifier**: The active profile committing the change.
- **Entity Reference**: The ID and Type of modified entity (e.g., `Task-104`).
- **Diff payload**: A structured object detailing the old values and new values.

---

## 2. Traceability & Historical Audit

The Activity Log is designed as a read-only, immutable history ledger. 
- **Auditing**: Managers can trace who made what change, which fields were updated, and when.
- **State Reconstruction**: While there is no automated rollback feature directly in the Activity Log view, the detailed diff payload provides a record that allows managers to manually reconstruct prior states or values if necessary (e.g., in case of accidental deletions or overwrites).

