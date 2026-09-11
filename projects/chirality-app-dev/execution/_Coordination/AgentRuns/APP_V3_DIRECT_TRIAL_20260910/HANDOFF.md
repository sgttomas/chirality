# Final-phase handoff

The owner explicitly directed PR #765 to merge as unfinished source integration. This is not functional trial acceptance or publishing approval. Once merged, begin new work from main containing that merge; preserve the existing implementation checkout and all local trial evidence.

## Read first

Read the active checkout's Root and applicable project AGENTS.md and HELP_HUMAN role. Read the final sections of adjacent TRIAL_FINDINGS.md for the actual blocker and proposed repair. Adjacent REBUILD_PLAN.md contains historical packaging procedures and completed Stage12 evidence; do not rerun completed commands verbatim.

The release plan and Trial Checklist remain in the preserved local continuity directory:
`/Users/ryan/.codex/worktrees/aed8/chirality/execution/_Coordination/AgentRuns/APP_V3_CONTINUITY_20260910/`.
Its older status/merge-authority entries are superseded by this handoff and PR765's actual merge state.

## Current state and next work

R3 is built from a120bd6b36a27b8fd83d49e6e1947c6a0708bdcb. App, Root and PEC CI passed. Actual signed Runtime startup and account-host connection succeeded; project initialization fails with “Complete App account host proof is required.” No actual OAuth, model turn, or complete functional checklist item has passed.

Latest diagnosis: App runtime-client/runtime-daemon-harness-port.ts initializeProject calls registeredStatus through an ordinary client lacking account proof. Other GUI account actions use authenticated Electron IPC. Proposed repair, not implemented: return verified registration/binding from initialization, then obtain status through existing authenticated IPC; retain cancellation/generation protections and daemon authorization. Validate the whole setup, consent, login, status, cancellation and sign-out connecting path before the next consolidated signed build.

Do not perform full signing for each isolated repair. Use production-code integration tests with controlled external effects, without bypassing the guards under test. Native identity/XPC verification still requires the appropriately signed package. No signed-bundle mutation, authority weakening, or mock-based native qualification.

## Local operational details

- Preserved implementation checkout: `/Users/ryan/.codex/worktrees/chirality-change-lessons-20260910/chirality`.
- R3 launcher: `/Users/ryan/Applications/Launch Chirality Trial 20260910 R3.command`.
- R3 userdata: `/Users/ryan/Library/Application Support/Chirality Trial 20260910 R3`.
- Stage12 recipes/evidence: `/private/tmp/chirality-local-human-trial-20260910-12`.
- Synthetic workspace: `/Users/ryan/Chirality Trial Workspace 20260910`.
- Trial authority expires 2026-10-10T22:43:56.184Z. Prior bundles and data are preserved.

At handoff GUI/daemon were idle and running; workers were completed/interrupted. Recheck live state. CUA getApp can launch an absent App with unprovisioned default userdata: select the actual launcher in Finder, open it, verify startup userdata, then attach CUA. Refresh CUA binding when native dialogs are not represented correctly.

This checkout's node_modules/.bin and react-test-renderer include foreign symlinks. Use canonical local CLI entrypoints and verify emitted Runtime consumer resolution; do not misdiagnose duplicate React as product failure. Exact working commands are in REBUILD_PLAN.md.

Direct Type2 dispatch is authorized for this testing phase: gpt-5.6-sol medium, separate independent reviewers. Rare gpt-6-astra high escalation is authorized. If Type1 managers are needed, use gpt-6-astra medium. Maintain direct oversight while workers run. Former workers are clarification only.

No UI logo work remains: website art is native icon only. Final milestones are usable trial, system-prompt discussion, and explicit publishing approval.
