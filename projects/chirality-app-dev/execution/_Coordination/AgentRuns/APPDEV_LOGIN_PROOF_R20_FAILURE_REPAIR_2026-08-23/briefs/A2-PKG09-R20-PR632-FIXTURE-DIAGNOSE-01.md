# Sealed brief — PR #632 fixture-mode diagnosis

- RequestedBy: `WORKING_ITEMS` instance `/root/node3_pkg09` under HELP_HUMAN.
- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- ParentInstanceID: `WI-PKG09-R20-PR632-FIXTURE-MANAGER-01`.
- ChildInstanceID: `A2-PKG09-R20-PR632-FIXTURE-DIAGNOSE-01`.
- Role: delegated-harness-native ephemeral generalist in explicit Agent-2 mode; role/non-delegation instruction-asserted. Do not delegate.
- Objective: reproduce the focused login-proof fixture failure once under `umask 0002`, confirm its mechanism, and determine read-only whether product runtime directory/file creation relies on umask.
- AcceptedBasis: clean branch/tip `codex/app-login-proof-r20-repair` / `980f5951dbbfe88302514802384e4ffec33c38b9`; frontend tree `b4c73edda1fe3346815ce75449b2327c80c79bf8`; exact owner authority in `CHAT_TRANSCRIPTION.md`, Amendment 08, plan/graph v10.
- DeclaredReads: focused test `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`; proof harness `frontend/scripts/run-packaged-launchagent-login-proof.mjs`; directly imported helpers and runtime/daemon creation sites needed to classify fixture versus product behavior; package scripts; existing R20 evidence.
- AllowedTools: read-only filesystem/Git/source search/stat; exactly one focused Vitest invocation from frontend under `umask 0002`; no network.
- AllowedWriteTargets: only `instances/A2-PKG09-R20-PR632-FIXTURE-DIAGNOSE-01/` for activation, complete diagnostic log/evidence, source-site matrix, diagnosis, and return. Do not edit frontend or shared RunID files.
- Exact reproduction: from `projects/chirality-app-dev/frontend`, set `umask 0002` in the command shell and run the single test file once with the repo-pinned Vitest. Capture complete output, exit, counts, and first divergence. Do not rerun, even on failure.
- Source inspection: inventory all fixture-created runtime-data directories/files and their creation APIs/mode arguments; distinguish harness/product creation from test fixture setup; trace the rejected snapshot path and mode; identify every product directory/file creation relevant to this guard and whether each passes explicit mode or safely chmods before reliance. No prompt-only conclusion.
- ExpectedOutputs: `ACTIVATION.md`, complete reproduction log (normalize/gzip only if needed for whitespace), `SOURCE_SITE_MATRIX.md`, `DIAGNOSIS.md`, `RETURN.md`; exact counts/message; fixture/product conclusion; bounded implementation recommendations and file targets; blockers.
- AcceptanceCriteria: exact-once reproduction evidence; mechanism confirmed from output plus source; all relevant creation sites classified; product-umask reliance answered with evidence; frontend and index unchanged; App-only containment.
- Escalation: stop on inability to reproduce/inspect, source ambiguity, unexpected product behavior, scope need, or prohibited mutation. Do not implement.
- Git fence: no stage, commit, fetch, push, PR mutation, rebase, force-push, or merge.
