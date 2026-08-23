# Sealed brief — PR #632 fixture-mode implementation

- RequestedBy: `WORKING_ITEMS` instance `/root/node3_pkg09` under HELP_HUMAN.
- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- ParentInstanceID: `WI-PKG09-R20-PR632-FIXTURE-MANAGER-01`.
- ChildInstanceID: `A2-PKG09-R20-PR632-FIXTURE-IMPLEMENT-01`.
- Role: delegated-harness-native ephemeral generalist in explicit Agent-2 mode; role/non-delegation instruction-asserted. Do not delegate.
- Objective: implement the accepted test-only explicit-mode repair, prove normal and Linux-shaped focused behavior, and freeze the source candidate for fresh review.
- AcceptedBasis: branch/HEAD `codex/app-login-proof-r20-repair` / `980f5951dbbfe88302514802384e4ffec33c38b9`; frontend tree `b4c73edda1fe3346815ce75449b2327c80c79bf8`; exact owner authority, Amendment 08, plan/graph v10, and accepted diagnosis in `DISPOSITION_04_PR632_FIXTURE_DIAGNOSIS.md` plus diagnosis instance.
- Dependencies: diagnosis exact-once reproduction and product-site conclusion accepted. No product source change is indicated or authorized.
- AllowedWriteTargets: only `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` and `instances/A2-PKG09-R20-PR632-FIXTURE-IMPLEMENT-01/`. No other frontend/shared path.
- Implementation: inventory every fixture-created runtime-data directory/file in the suite; add explicit `{ mode: 0o700 }` to the diagnosed recursive directory creation calls and `{ mode: 0o600 }` to the diagnosed fixture file writes, preserving existing options/data/semantics. Add or adjust assertions only as needed to prove modes explicitly. Do not weaken/alter guard expectations or product source.
- Authorized checks, each at most once unless it is a pure read-only hash/diff check: APP-HOLD dispatch preflight; focused suite under ordinary host umask once; focused suite under `umask 0002` once after fix; typecheck once; syntax check of unchanged proof script once; exact mode/source assertions; `git diff --check`; frontend/App containment; empty index; candidate whitespace for current candidate. Do not run full suite, build, package, supply, daemon, precheck, proof, or network.
- Evidence: capture complete logs safely; if command output has whitespace defects, deterministically gzip it with preimage lineage before final candidate scan. Record exact commands/exits/counts, pre/post source hashes/diff, and test-mode coverage.
- ExpectedOutputs: `ACTIVATION.md`, implementation/mode inventory, check logs/summary, `RETURN.md`, exact changed inventory and hashes.
- AcceptanceCriteria: test-only minimal diff; every relevant fixture directory/file gets explicit private mode; normal focused PASS; exactly one post-fix `umask 0002` focused PASS; typecheck/syntax/APP-HOLD PASS; guard/product unchanged; frontend dirt only the focused test; App-only/index empty; no forbidden action.
- Escalation: stop on any failed gate, uncovered fixture creation, need for product change contrary to diagnosis, scope drift, or prohibited rerun. Do not repair beyond exact findings without manager disposition.
- Git fence: no stage, commit, fetch, push, PR mutation, rebase, force-push, or merge.
