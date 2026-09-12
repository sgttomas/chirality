# Launch brief — independent review of the frozen diff (TASK + software-code-review)

Role: TASK (Type 2), workflow `software-code-review` (`.agents/skills/software-code-review/SKILL.md`). Engine/model: Claude Fable 5.1 (Claude Code Agent tool), fresh session with no authorship of the diff. No delegation. Read-only: no file writes, no git write commands, no commits; the return travels back to the dispatching session, which records it under `returns/REVIEW_RETURN.md`.
Parent: implementing session for APP_V3_UI_REFINEMENT_20260912 (WORKING_ITEMS for this package).
Repository: /Users/ryan/dev/chirality/.claude/worktrees/project-first-impressions-06aed9 (git worktree, branch claude/chirality-ui-refinement-20260912). Frontend: projects/chirality-app-dev/frontend.

## Frozen diff

Basis 19bca4930 (main, merge of PR #774). Candidate 02ffa62b0. Review 100% of `git diff 19bca4930..02ffa62b0` (89 files). Commits, in order: 04f6e0e5c, e692c6c22, 85c552d3c, ca8e6935d, 4c792b1bc, 9d67e7987, 02ffa62b0.

## Scope the diff implements (owner brief, 19 items)

Items 1 to 12 (first pass): message distinction (operator bubbles, recorded role), single-action sign-in (browser opens on Sign in), compact turn activity, streaming follow with Jump to latest, account area (Account row, Sign-in and Runtime rows, popover with Settings, Appearance, Check for Updates, About), menus closing on selection, Plan tab in the right panel, update discovery (fail-closed feed checker in Electron main; Check for Updates; About panel; download opens in browser; no install), account icon, chat search heading, workflow navigation with Core (nine) / Specialist / Project Specific and a collapsed Superseded group, read-only Skills tab. The Core/Specialist/Project Specific naming is accepted direction and not under review.

Items 13 to 18 (second pass):
13. Per-chat working folder and context: persisted chat index (wovenWorkspace v1 additions chatIndex, foldersCollapsed, chatDocuments, lastActiveChat), navigator sections grouped by folder with the current folder first, opening a chat from another folder explicitly re-selects that folder then resumes, unavailable folder notice with Locate folder and Forget folder, per-chat drafts carrying permission and interaction mode for saved sessions, last active chat restored for the current folder only, document context per chat.
14. Authentication independent of folder: hosted bootstrap controller keeps the last account status across folder changes and reports the folder on its own axis (checking, registered, setup-required, conflict, unavailable); explicit selection of a folder that hydrates as a binding conflict (409) is set up once; model selectors keep the account catalog and name folder problems.
15. Interruption and recovery: turn phases (preparing, working, waiting, reconnecting, stopping) reported to the activity strip and status line; per-turn outcome chips (Completed, Stopped, Failed, Outcome unknown); unknown only after a lost connection with no recorded ending; message kept in the conversation so nothing is re-sent; text recorded after a drop appended; continuation note (closing the window keeps the turn running; quitting stops it); running sessions are continuable so reopening during work re-attaches.
16. Plan execution lifecycle: local per-session execution records (revision, attempt, started, running or outcome), Run again on executed revisions, Execute this revision on earlier ones, Execute plan still prepares the request in the composer for the user to send.
17. Preservation through updates: user-data inventory with renderer-storage snapshot, contract pins on electron/app-update.ts and main.ts, Download and About wording describing the manual install path, running-work note, acceptance checklist UPDATE_PRESERVATION_ACCEPTANCE.md.
18. Right panel tab strip wraps at narrow widths; keyboard and accessible names retained.

Verification recorded: frontend `npm run typecheck` PASS; frontend `npx vitest run` 2150 passed, 4 skipped (includes electron tests and contract pins); live checks on the dev instance in RUN_LOG.md (entries from 17:41Z to 20:04Z).

## What to check (in addition to the skill's own method)

- Correctness and regressions in `frontend/src/**` outside `__tests__` and `frontend/electron/**`: chat-panel.tsx turn observation (observeTurn, settleFromReplay, recoverActiveTurn, lostConnection, outcome derivation, plan execution records, per-session draft settings), woven-dialogue-shell.tsx (cross-folder open, pending folder chat, sessionsRoot gating, last-chat restore and persistence, document context), hosted-bootstrap-controller/view/context (account versus project axes, auto setup on conflict only for explicit selections), navigator folder sections, plan panel lifecycle, app-update modules and wording, live-work store.
- Security and privacy: no credentials, tokens, identity or private paths in logs or UI strings; app-update fail-closed behaviour unchanged (no fetch without a configured allowlisted https source; no install, relaunch, filesystem or userData surface); IPC handlers keep sender authorization; the operator-projection change (running sessions continuable) cannot cause a second submission or a write into a running turn.
- Contracts and persistence: wovenWorkspace v1 additions are additive and tolerate absent or malformed values; storage growth is bounded (chat index 500, chat documents 500); draft store keys unchanged for existing data.
- Tests: the new and changed tests actually pin the behaviour claimed; any behaviour in the brief without a test is named as missing verification.
- Scope: no expansion beyond the 19 items; no change to repository protections, release publication, skill creation or import.

## Constraints (verbatim from the owner's standing instructions)

Never enter credentials, passwords or codes. Never read live identity, auth, token, binding, keychain, trial Codex home or session/event files (this includes anything under the scratchpad spike userData directories and any `~/.codex` or `~/.chirality` runtime data). Filter desktop and daemon logs with `grep -v '@'` before quoting anything; the owner's account e-mail never appears in your return. No `security` commands. No cleanup of preserved trials or account resets. No publishing. Do not launch the App. Do not touch `projects/chirality-app-dev/intro-rehearsal/`.

You may run read-only checks: `npm run typecheck` and `npx vitest run <file>` in projects/chirality-app-dev/frontend, `git diff`, `git log`, `git show`. Do not run `git stash`, `git checkout`, `git commit`, or any command that writes to the repository.

## Return

Report: (1) verdict PASS or FAIL for publication under the App AGENTS.md independent-review rule (PASS requires no actionable finding); (2) findings ordered by severity, each with file:line, triggering condition, concrete impact, evidence, remediation direction; (3) residual risks and missing verification, separated from confirmed defects; (4) the checks you ran and their results; (5) confirmation that you read the whole diff (list any file you did not read).
