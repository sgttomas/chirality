# R14 combined independent source review

Verdict: **PASS** — no remaining actionable introduced finding after independent P2 backcheck. Native qualification pending.

Reviewer: independent delegated-harness-native Type 2 TASK, GPT-6 (exact deployment model identifier not exposed to this child); no delegation, implementation edits, commits, builds, supplier execution, downloads, packaging, native trials, or operational/auth-state access. Parent owns registered/full checks. Review used `.agents/skills/software-code-review/SKILL.md`.

## Resolved finding and backcheck

**Resolved P2 — Preserve the loaded conversation catalog when Files opens and closes before its read finishes.** Location: `frontend/src/lib/workspace/use-conversation-file-catalog.ts:9–11` together with `frontend/src/components/shell/file-tree-panel.tsx:131–138,198–206` (paths relative to App project). After the conversation hook has loaded a valid catalog, mounting Files unconditionally publishes `null`, and `acceptCatalog` erases the valid catalog. If the user closes Files before its fetch resolves, that panel's cleanup marks the request cancelled, so no catalog is published. The conversation hook's root/streaming/runtimeEpoch dependencies are unchanged and it does not reload. Previously working assistant links therefore stay inert until another turn, reconnect, or root change. Current tests separately verify hook loading and panel-unmount retention, but miss this composed lifecycle. Keep conversation-owned valid data during panel initialization (while still clearing on a real root change or an authoritative failed read), or trigger an independent refresh on invalidation. Add a composed regression: load hook, mount Files with deferred response, close Files, settle response, click README link.


Backcheck: parent added `catalogRootRef` initialized to the current project root. The mount/callback reset publishes null only on an actual root change. Thus mounting then unmounting before completion leaves the conversation-owned catalog intact; existing response cancellation still suppresses the late response. Actual root changes and failed reads continue to invalidate. Inspected the exact repair and new deferred-fetch/unmount regression; it asserts no callback occurs across the problematic sequence. Parent reports 11 focused file-tree/conversation-navigation tests passing; this reviewer did not duplicate that run. `git diff --check` and repeated DEL-09-04 reliance preflight passed. The original P2 is closed.

## Scope and evidence

Read all 46 changed Runtime/frontend product and test files, including seven untracked source/test files, against HEAD `05f11d5eb54a232b8b324e664fd59e3d500996af`. Covered native plan display/actions/save IPC and model choice; accepted user/attachment storage and reconstruction; direct history entry and guards; Codex settings and method-library cleanup; conversation catalog and Markdown rendering; native interruption/private IPC/adapter terminal projection/account-retirement composition. Read R14 findings and all four repair/cleanup returns. No additional introduced correctness/security finding confirmed.

Tracked product/test diff SHA-256: `3ec928c0d4fb9e53e1dadffac5e042abbd80f5a6fceafc13fdbd99de2df40c71`. Combined 46-file manifest hash (sorted repository path + space + file SHA-256, joined with newline): `d766144679ca5486dc928a2ff5868fb06cffc29ee1bd148004e5546132cbf34e`.

Executed reviewer reliance preflight `HELP_HUMAN:TRIAL:REPAIR`, DEL-09-04: ALLOW/CLEAR at that HEAD; hold-register hash `c08a2948201cfcc09a661750f45148f9555d1ce38b925eeacf987de89ac5cafc`. `git diff --check` passed. Source tracing and existing regression inspection only; no duplicate full test run.

Instruction context SHA-256: Root AGENTS `2f2e5ee53ab227936379ee47169c0e0ff19bf5fd3bcff9086f088f3568adfac7`; TASK `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7`; review skill `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a`; App AGENTS `47e11feeba9640caaaa5f7d45af7b5d3be5538fc7ab631213691d908f08244d7`; Runtime AGENTS `ca1b305c1fbc3ebc83e3718c6b2122170bbab3c1d1f616f744d0339f2a84691d`. Also consulted Runtime LOOP_INIT for bounded-entry limits.

## Limits and handoff

Electron export uses authorized sender checks and rejects static outside-root/symlink paths; Runtime remains the writer. **Pre-existing security residual, not an introduced diff finding:** `projects/chirality-runtime/packages/core/src/runtime-method-service.ts:357–392` checks ancestors/target with lstat then opens by pathname using `w`/`wx`; a concurrent target/ancestor symlink swap is not excluded. The added dialog does not make this race-proof. Parent was notified; do not claim adversarial concurrent path-containment qualification from these tests.

This is derivative review evidence against the named source basis, not accepted decomposition truth. Source review is suitable for manager fan-in; parent owns full deterministic integration and native retrial of save/export, history/drafts, links, settings, and interrupt-followed-by-resume. Supplier tool-host proposal is outside this review and owned by the separate reviewer. No authority snapshot or pointer updated.

## Final interrupted-exit UI backcheck

**PASS** for the two-file follow-up against commit `0ed1a1a7f1a6bf29ad761389e6f615c65efebcdb`. Lead identified an additional cross-layer gap after the initial combined review: ChatPanel treated the Runtime-normalized genuine interrupted exit (130 with `interrupted:true`) as failure. Inspected the exact frozen ChatPanel change and all five added test cases. Only that exact nonzero tuple now bypasses creation of a process failure. Bare 130, exit 1 with or without the interrupted flag, and an earlier fatal turn:error retain failure/draft-restoration behavior. The success fixture supplies turn.interrupted then the normalized exit and verifies a same-session successful follow-up without creating another session.

Contract tracing: delegated-engine-adapter requires a matching interrupted terminal before emitting that tuple; TurnCoordinator retains terminal evidence and projects it before process exit. The frontend test is a controlled normalized-stream fixture rather than an end-to-end native test. Together with the previously inspected Runtime production-composition regression, its coverage is adequate for this bounded source correction; native interruption/reuse remains pending. Author reports 39 focused tests and frontend typecheck passing; reviewer did not repeat those checks. Reviewer `git diff --check` passed and DEL-09-04 reliance preflight again returned ALLOW at this commit. No further actionable introduced finding.

Two-file follow-up diff SHA-256: `d9562b2b1f5f575a63b9b11b615b768331e85cc2cdcdf0c376eaf80e1a45b1dc`. The earlier 46-file hash identifies the earlier reviewed snapshot, not this follow-up. This remains derivative source-review evidence, with native qualification and the separately stated pre-existing export containment residual unchanged.
