# TASK: bounded library and folder UI repairs

Type 2 gpt-6-astra medium, no delegation. Read Root/App AGENTS, TASK and PLAN.md.
Owner approved first folder picker at home (remember explicit selections),
hiding Skills UI for this release while retaining background skill use, and
repairing workflow discovery after ordinary conversational creation. Parent
confirmed native folder dialog lacks defaultPath, stored folders are restored,
and library refresh only follows root/query/manual-refresh/runtime epoch.

Implement these three behaviors in the existing visual style. Do not make the
whole user home a project. Hide Skills entry points, redirect a saved Skills
view to Workflows, retain legacy/session data and background method capability.
Refresh catalog after completed work without flashing/resetting selection;
RightPanel already receives liveTurnActive. Check fresh workflow packages are
visible without closing/reopening panel. Do not assume a successful turn wrote
a workflow or claim invalid packages valid. Update existing six-central/old core
navigation fixtures for parent-authored create-workflow entry only when needed.

Allowed source: frontend/electron/main.ts; frontend/src/components/woven-dialogue/
right-panel.tsx, method-library-view.tsx; frontend/src/lib/woven-dialogue/
woven-workspace-state.ts; directly affected focused test files. Request expanded
scope for other source files. No chat-panel, supervisor, contracts, Runtime,
workflow packages, instructions, manifests, Git operations, builds, UI actions,
supplier execution or account/private-state access. Other authors own those.
Run focused behavioral tests and type checks proportionate to this slice; return
actual diff, tests and remaining integration issues. Preserve all unrelated work.
