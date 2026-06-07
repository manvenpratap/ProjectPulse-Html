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

## 2. Session Rollback Capability

From the Activity Log UI:
- **Reversion**: Managers can select a historical log entry and click "Revert State".
- **Execution**: ProjectPulse computes the inverse operations from the diff payload and applies them sequentially back to the target index.
- **State Save**: Following reversion, `save()` is automatically called to persist the restored state in browser storage.
