# Node J round-3 review disposition

- Reviewed freeze: `2c42f919aa38546c5a4ad9eb692b450aa5c13d06`
- Review verdict: `FAIL` — 0 BLOCKER, 1 MAJOR, 0 MINOR, 0 NOTE
- Review report: `/private/tmp/chirality-app-v3-slate3-20260903/reviews/nodeJ/REVIEW_03_2026-09-03_over_2c42f919a.md`
- Review SHA-256: `3b66f126fb9270206b201306ff1bfbbaf56e81543996ffe5ea78affc1555de83`
- Scope response: remediation only; no product, status, receipt, Root, plan, register, or decision-record byte added

| Finding | Disposition | Implementation and proof |
|---|---|---|
| J3-F1 — a controlled descendant can leave an anchored PGID with `setsid()` and survive while group cleanup reports zero | REMEDIATED IN RUNNER; CLEAN PROOF PENDING | The runner now explicitly disables the application's known daemon GUI-detach route with `CHIRALITY_DAEMON_GUI_SPAWN=0` and records the prohibited activation policy. Each retained controller continuously inventories its owned descendant relation through macOS `libproc`, keyed by PID plus kernel start timestamp. Every observed descendant must remain in the controller's anchored PGID for the complete proof lifecycle. A PGID escape, malformed/missing audit, or inspection error is permanent fail-closed state and makes an otherwise successful run exit 74. No individual PID becomes signal authority. The deterministic adversarial proof makes a child call `setsid()`: the audit records `violation`, automatic anchored-group cleanup returns 74 rather than success, the escapee remains explicitly identified as requiring manual escalation, and the test then removes only the disposable escapee's own process group. Existing same-command/same-second foreign processes remain alive across controlled TERM/KILL. |

## Platform boundary and claim calibration

macOS supplies no unprivileged cgroup/pidfd-style primitive that forcibly contains an arbitrary descendant after `setsid()`. Launchd job cleanup is process-group based; Mach task/coalition control is privilege-gated; complete lineage enforcement would require a stronger host facility such as Endpoint Security. This runner therefore does not claim generic containment or automatic termination of a hostile escapee.

The supported proof lifecycle is narrower and fail closed: the actual daemon's known detach route is disabled before launch, daemon and Next descendants are continuously audited, every observed actual descendant must stay in its anchored group, and only those kernel-owned groups are signalled atomically. Any escape prevents evidence acceptance and requires explicit host cleanup. The new retained run must show both daemon and Next audits remained `ok`, their violations arrays stayed empty, all group members were removed, and the port/socket/state invariants passed.

The earlier accepted-run candidate at clean runner `b1f0d71f128e31fb2f0d10b579abf6523bae7d3c` is superseded for H2-F1 because it did not enforce or record this contract. Its raw bytes remain dated candidate history and are excluded from the replacement comparison. The two-phase provenance rule remains: commit the final runner/helper/test/control bytes first; execute the proof from that clean commit; import generated evidence separately; then require a fresh round-4 independent review.

The original TASK stop and HELP_HUMAN execution-form amendment remain unchanged. A1 and F-APP-2 boundaries remain unchanged.
