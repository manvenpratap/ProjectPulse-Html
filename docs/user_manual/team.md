# Team Capacity Hub & Role Management

The **Team Capacity Hub** controls resource availability, role profiling, and assignment boundaries across all project phases.

---

## 1. Capacity Modeling

Each team member is profiled with specific capacity parameters:
- **Weekly Hour Cap**: The maximum standard hours they are expected to work per week (typically `40`).
- **Utilization Rate**: The percentage of standard time designated for project work (e.g., $80\%$ utilization means 32 project hours per week, with 8 hours reserved for administrative tasks).
- **Time Off / Leave Calendar**: Integrated directly into scheduling constraints to temporarily reduce available capacity.

---

## 2. Dynamic Workload Balancing

The Capacity Hub features a real-time capacity balance indicator:
- **Under-Utilized**: Resource is allocated $< 70\%$ of their capacity. The system suggests assignments based on their role profile.
- **Balanced**: Resource is allocated between $70\%$ and $100\%$ capacity.
- **Overallocated**: Resource is allocated $> 100\%$ capacity. A warning flag is displayed, and the **Weekly Scheduler Diagnostics** recommends reassigning tasks or extending deadlines.

---

## 3. Role Assignments

Roles dictate which tasks resources can be assigned to:
- **Standard Roles**: `Developer`, `Designer`, `QA Engineer`, `Product Owner`, `Project Manager`.
- **Assignment Logic**: When reassigning tasks to resolve scheduler conflicts, the automated resolver matches roles to ensure tasks are assigned to qualified personnel.
