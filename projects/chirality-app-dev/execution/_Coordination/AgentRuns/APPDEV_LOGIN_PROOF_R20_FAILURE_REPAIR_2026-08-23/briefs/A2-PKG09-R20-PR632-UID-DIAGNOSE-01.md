# Sealed brief — PR #632 UID and host-entanglement diagnosis

- RequestedBy: `WORKING_ITEMS` instance `/root/node3_pkg09` under HELP_HUMAN.
- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`.
- ParentInstanceID: `WI-PKG09-R20-PR632-UID-MANAGER-01`.
- ChildInstanceID: `A2-PKG09-R20-PR632-UID-DIAGNOSE-01`.
- Role: delegated-harness-native ephemeral generalist in explicit Agent-2 mode; role/non-delegation instruction-asserted. Do not delegate.
- Objective: before any frontend write, independently confirm the exact UID-to-lstat failure dataflow and freeze a complete one-pass host-entanglement inventory across the focused login-proof test.
- AcceptedBasis: clean branch/HEAD `codex/app-login-proof-r20-repair` / `4a48aeaede2d050631006f8ff23fb11736752bef`; parent `74525fb6b34f614c114e59a1bf09d20102fc6aac`; frontend tree `23315613d0d3e4d21580d928909816dc5aad92c7`; Amendment 11 and plan/graph v12; exact owner transcription.
- DeclaredReads: focused test; proof harness and directly called helpers; R19 never-exited fixture; relevant package/test utilities. Do not read owner Desktop evidence or traverse a private proof root.
- AllowedWriteTargets: only `instances/A2-PKG09-R20-PR632-UID-DIAGNOSE-01/`. No frontend/shared write.
- Required analysis: trace hardcoded/mock UID through `deps.uid`, `deps.userInfo`, fixture launchctl/login-domain/securityUid parsing, `preserveFailureLogs`, expectedUid, `assertSafeSnapshotMetadata`, and real `lstat().uid`; distinguish semantically compared values from inert fixture text. Sweep the entire focused test for UID, GID, `gui/<uid>`, `uid =`, `/Users`, `/home`, real-state path comparisons, temporary-directory/symlink assumptions, homedir assumptions, process/platform assumptions, and deliberate mismatch values. Inspect product creation/guard paths only to confirm product correctness and scope.
- Fixed controls: independently hash/size the R19 never-exited fixture and require it remain byte-identical; hash the product proof script and require no write. Do not run the known failing CI, focused suite, full suite, typecheck, package, supply, preflight, proof, or network. Do not claim local UID reproduction; record that CI is the arbiter for host-identity classes.
- Outputs: `ACTIVATION.md`, `UID_DATAFLOW.md`, `HOST_ENTANGLEMENT_INVENTORY.md`, and `RETURN.md` with exact source/fixture hashes, accepted repair inventory, deliberate-mismatch inventory, non-findings, scope, and implementation acceptance criteria.
- AcceptanceCriteria: prompt diagnosis independently confirmed or rejected from source; inventory covers the whole test rather than one constant; each finding classified as change/retain/deliberate mismatch/inert text; R19 fixture and product script identities frozen; no frontend/product/private/operator/Git action.
- Escalation: stop on source disagreement, ambiguous real-state comparison, required product change, fixture drift, scope expansion, or missing coverage. No implementation.
- Git fence: no stage, commit, fetch, push, PR mutation, rebase, force-push, or merge.
