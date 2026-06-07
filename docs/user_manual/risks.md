# Unified RAID Register

The **RAID Register** is the risk mitigation control center of ProjectPulse. It consolidates Risk, Assumption, Issue, and Dependency elements into a searchable, categorized database.

---

## 1. RAID Classifications

Every RAID entry is categorized into one of four types:

| Type | Definition | Management Workflow |
| :--- | :--- | :--- |
| **Risk** | A potential future event that could impact the project negatively. | Mitigate or transfer before occurrence. |
| **Assumption** | Factors believed to be true for planning purposes without proof. | Validate assumptions to eliminate risk. |
| **Issue** | An active, current problem that is impacting timeline/scope/budget. | Resolve immediately using assigned owners. |
| **Dependency** | Reliances on external teams, systems, or deliverables. | Map to task schedules and monitor checkpoints. |

---

## 2. Threat Exposure Calculations

For **Risks**, exposure is computed using a $5 \times 5$ matrix:

$$\text{Exposure Score} = \text{Probability (1-5)} \times \text{Impact (1-5)}$$

### Scoring Reference:
- **`Score >= 15`**: **Critical (Red)**. Requires immediate mitigation strategies and executive visibility.
- **`Score 8-12`**: **Medium (Yellow)**. Monitored weekly; mitigation plans prepared.
- **`Score < 8`**: **Low (Green)**. Logged and reviewed bi-weekly.

---

## 3. Mitigation Plans and Owners

Every active RAID item must have:
- **Owner**: An active resource assigned from the Capacity Hub.
- **Mitigation/Resolution Strategy**: Detailed textual explanation of the action plan.
- **Target Closure Date**: The deadline for resolving the issue or validating the assumption.
