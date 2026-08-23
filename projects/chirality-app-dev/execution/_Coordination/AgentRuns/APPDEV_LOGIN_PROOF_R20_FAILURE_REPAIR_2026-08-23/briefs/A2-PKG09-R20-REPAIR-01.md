# Sealed repair brief — A2-PKG09-R20-REPAIR-01

- RequestedBy: `WI-PKG09-R20-REPAIR-01`
- RunID: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23`
- ParentInstanceID: `WI-PKG09-R20-REPAIR-01`
- Executor: resume `A2-PKG09-R20-IMPLEMENT-01` as sole overlapping source write owner.
- Role/mechanism: delegated-harness-native explicit ephemeral-generalist Agent 2; `role not mechanically enforced`; evidence `instruction-asserted`; do not delegate.
- Objective: repair exactly F-01 through F-05 from immutable fresh review SHA-256 `0134c2db5a9255236171880b95f66a5d93292cd41f71be458dc853dc5636ef76`.
- AcceptedPredecessor: original candidate hashes script `604f2e189b167c9691eae33b28fc2b3a70352b6222abb1924f36252dd1493b45`, test `2d791913022671beb1c4f9e59cd104cba7f96521f784476a0798c9682511eab0`, fixture `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`.
- AllowedWriteTargets: the same exact script, test, and fixture targets from the original brief; plus `instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-1/**` only.
- RequiredRepairs:
  - F-01: adopt a fail-closed ordering/state machine so PASS-only failed-log removal cannot create a later FAIL after runtime destruction or leave a non-PASS without intact preserved evidence. Final PASS cannot be retroactively invalidated by post-destruction copy deletion. Add deterministic deletion-failure coverage.
  - F-02: eliminate nested-symlink and pathname TOCTOU hazards. Revalidate the owned runtime root; require safe contained non-symlink ancestors; read the actual token and both regular logs through safely opened, identity-bound snapshots without following final symlinks. Any identity/containment/ownership/mode ambiguity copies neither and retains runtime private-only. Add ancestor-symlink and final-file substitution/refusal coverage.
  - F-03: capture with either or both logs missing is an explicit preservation failure; report private-only/diagnostic preservation and prohibit runtime removal. Preserve any distinct install-attempt behavior only where source semantics prove the daemon may not have created logs. Add zero-log and one-log non-PASS coverage, including observation and later default-protection failures.
  - F-04: distinguish absent `last exit code` from a present empty/whitespace-only value; both empty forms throw. Exact `(never exited)` remains the only admitted noninteger sentinel.
  - F-05: add a distinct successful-bootout/job-still-loaded/process-absent test asserting refusal, report, no plist unlink, no runtime removal, and intact failed-log copies.
- Amendment01 remains binding: preserve across proof observation, cleanup, and later default-protection failures; copies exist before any allowed removal; no copied log contains the actual token.
- RequiredChecks: syntax; exact focused Vitest only; typecheck; fixture hash/cmp; candidate hashes and diff; `git diff --check`; App containment; empty index. No full suite/build/package/network/Git/proof/operator/private-root/Desktop action.
- ExpectedOutputs: repaired source/test/fixture; `repair-cycle-1/REPAIR.md`, `CHECKS.md`, `RETURN.md` with a finding-by-finding closure matrix, commands/exits/counts, hashes, exact inventory, attribution, and fences.
- Escalation: stop rather than broaden source scope, weaken token checks, infer private state, run a forbidden command, or accept a failed required check.
