# Future Prompt Template

Copy and paste this into a new AI session to give it instant context.

---

**Task**: [DESCRIBE YOUR TASK HERE]

**Project Context**:
This is the ProjectPulse application, a local-first project management suite. 
Please read the following documentation files before proposing any changes:
- `/project-context/index.md`
- `/project-context/03-state-schema.md`
- `/project-context/04-function-index.md`
- `/project-context/08-persistence-and-compatibility.md`

**Constraints**:
1. Maintain full backward compatibility with the `P` state object.
2. Ensure any new features are reflected in the Excel Export/Import logic.
3. Use the established CSS variable system for all styling.
4. Stick to Vanilla JavaScript (no frameworks).
5. Update the project-context documents after completing the task.

---
