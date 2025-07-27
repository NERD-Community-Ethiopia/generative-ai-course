# Meeting Notes & Task Automation

This folder is used to store weekly meeting updates and to trigger the task automation workflow for the project.

## How It Works
- After each Monday meeting (or any planning session), create a new meeting update file in this folder.
- The act of adding or updating a meeting note and pushing it to the `task-ops` branch will automatically trigger the GitHub Actions workflow for task generation, assignment, and sprint board creation.

## Naming Convention
- Use the format: `week-X-update.md` (e.g., `week-3-update.md`)
- This keeps notes organized and easy to reference.

## Example Workflow
1. **Create a new meeting note:**
   ```bash
   echo "# Week 3 Meeting Update\n\n- Summary of discussion\n- Decisions made\n- Action items\n" > meeting-notes/week-3-update.md
   git add meeting-notes/week-3-update.md
   git commit -m "Add Week 3 meeting update and trigger automation"
   git push origin task-ops
   ```

2. **Result:**
   - The push to `task-ops` triggers the automation workflow.
   - Tasks are generated, assigned, and the sprint board is updated as per the workflow.

## Best Practices
- Always summarize key points, decisions, and action items in each meeting note.
- Use clear, consistent formatting for easy review.
- Only push meeting notes to the `task-ops` branch if you want to trigger the automation.

---

_This process ensures that task management is always aligned with your team's latest discussions and decisions._ 