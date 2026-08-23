# Activation — PR #632 UID and host-entanglement diagnosis

- Run: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`
- Parent: `WI-PKG09-R20-PR632-UID-MANAGER-01`
- Instance: `A2-PKG09-R20-PR632-UID-DIAGNOSE-01`
- Role: delegated-harness-native ephemeral generalist, explicit Agent 2 mode; role and non-delegation are instruction-asserted.
- Objective: independently trace the focused login-proof test's UID-to-`lstat()` metadata failure dataflow and inventory the whole test for host-entangled identity, path, symlink, homedir, process, and platform assumptions before any frontend write.
- Accepted basis: branch `codex/app-login-proof-r20-repair`; HEAD `4a48aeaede2d050631006f8ff23fb11736752bef`; parent `74525fb6b34f614c114e59a1bf09d20102fc6aac`; frontend tree `23315613d0d3e4d21580d928909816dc5aad92c7`.
- Read boundary: focused test, proof harness and directly called helpers, R19 never-exited fixture, relevant package/test utilities, Amendment 11, plan v12, graph v12, and applicable instructions. Owner Desktop evidence and private proof roots are excluded.
- Write boundary: this instance directory only.
- Prohibited actions: frontend/shared/product/fixture/operator/private-root edits; delegation; tests; builds; typecheck; supply; package; preflight; proof; network; Git stage/commit/fetch/push/PR/rebase/merge.
- Source state at activation: the accepted HEAD/tree match; the worktree contains only the parent's uncommitted run-control records listed by `git status --short`; no pre-existing frontend modification is present.
- Method: static source reading, deterministic text search, file metadata, and cryptographic hashing only. No local UID reproduction claim; CI remains the arbiter for host-identity portability classes.
- Status: `COMPLETE` — static diagnosis `PASS`; implementation may proceed only against the accepted inventory in this instance.
