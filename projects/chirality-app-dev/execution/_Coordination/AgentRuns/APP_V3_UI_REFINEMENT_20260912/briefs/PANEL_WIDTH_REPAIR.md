# TASK: panel width accessibility correction

Agent 0 dispatch, 2026-09-12. Type 2, gpt-6-astra, medium. No delegation.

Work only in `/Users/ryan/.codex/worktrees/chirality-ui-refinement-packaged-20260912/chirality`.
Read Root and App AGENTS.md and the active TASK instructions. Parent directly
tested the merged 85f19f019 product at 1000 x 900 and 760 x 900. Dragging,
collapse/reopen, expand/return, and six-tab keyboard navigation worked. At 1000
with Navigator open the right panel rendered at 280 px while its separator
announced aria-valuenow=480, aria-valuemin=280, aria-valuemax=280. Its saved
preferred width was being announced instead of the constrained rendered width.

Fix only this observed accessibility mismatch and any directly coupled resize
start calculation necessary to prevent a drag starting from an invisible width.
Preserve preferred per-tab widths and expansion return. Do not redesign the
responsive layout, catalog, chat binding, or other panel behavior. Write targets:
`frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx` and its
`frontend/src/__tests__/components/woven-dialogue-shell.test.tsx` under the App
project. Add a regression that models a constrained viewport and demonstrates
the announced width agrees with the rendered layout, with preferred width
restored when space returns. Check focused tests. Do not run full suites, commit,
launch apps, inspect any live profile/credential/trial files, or signal processes.

Return exact files, behavior, checks and residual concerns. Another agent is
editing Runtime/chat recovery in distinct files; do not touch those changes.
Parent validates the return and obtains a fresh independent full-diff review.
