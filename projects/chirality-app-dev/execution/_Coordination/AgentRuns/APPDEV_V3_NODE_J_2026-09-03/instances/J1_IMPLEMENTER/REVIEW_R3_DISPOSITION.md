# Node J round-3 review disposition

- Reviewed freeze: `2c42f919aa38546c5a4ad9eb692b450aa5c13d06`
- Review verdict: `FAIL` — 0 BLOCKER, 1 MAJOR, 0 MINOR, 0 NOTE
- Review report: `/private/tmp/chirality-app-v3-slate3-20260903/reviews/nodeJ/REVIEW_03_2026-09-03_over_2c42f919a.md`
- Review SHA-256: `3b66f126fb9270206b201306ff1bfbbaf56e81543996ffe5ea78affc1555de83`
- Scope response: remediation only; no product, status, receipt, Root, plan, register, or decision-record byte added

| Finding | Disposition | Implementation and proof |
|---|---|---|
| J3-F1 — a controlled descendant can leave an anchored PGID with `setsid()` and survive while group cleanup reports zero | REMEDIATED; ROUND-4 REVIEW PENDING | The outer supervisor now runs the proof as one uniquely labelled transient per-user LaunchAgent and remains outside that job. The job's distinct resource-and-jetsam coalition pair is inherited across fork, exec, process-group changes, and `setsid()`. PGID TERM/KILL remains the inner graceful first line; the authoritative outer cleanup enumerates both coalition IDs and uses `proc_signal_with_audittoken`, which atomically validates PID plus kernel pidversion, for repeated TERM then STOP/KILL sweeps until three consecutive scans are empty. No bare PID or command match is signal authority. The pre-build behavioral probe proves a TERM-resistant `setsid()` child and a forker-created `setsid()` grandchild survive ordinary bootout and are removed by the coalition sweep, a same-command/same-second foreign process survives, and stale pidversion is rejected with ESRCH. Forced enumeration, unique-ID, coalition, signal, bootstrap, and bootout failures all exit 74 and remove probe state. The retained premerge proof and separate release-quality lifecycle both passed from final clean runner `9dfbb7962`; their final coalitions were empty and manifests verified. |

## Host-pinned boundary and claim calibration

The remediation is based on the verified host prototype at `/private/tmp/chirality-app-v3-slate3-20260903/reviews/nodeJ/CONTAINMENT_PROTOTYPE_2026-09-04.md`, SHA-256 `6ccc89b1e4e3a7be196b208624f3b8e298c7d62d5f8f43a08885025e4ef4c5e6`. On this macOS host, `PROC_PIDUNIQIDENTIFIERINFO` (flavor 17), `PROC_PIDCOALITIONINFO` (flavor 20), and `proc_signal_with_audittoken` were experimentally verified. Direct coalition creation and Mach task control remain unavailable without privilege; ordinary launchd bootout alone is insufficient because a TERM-resistant `setsid()` child survives it.

This is a host-pinned evidence helper, not a product/runtime containment claim. Before any build or daemon launch it verifies the private ABI sizes and behavior, per-user launchd access, a distinct nonzero coalition pair, pair inheritance across `setsid()`, exact audit-token signaling, stale-token rejection, and absence of the private coalition-spawn entitlement from every target binary. Any unavailable, ambiguous, or failed observation/launch/signal operation stops or fails cleanup; there is no PGID-only or bare-PID fallback. The application's GUI-spawn route remains disabled as defense in depth, not as the containment mechanism.

The earlier reviewed candidate at clean runner `b1f0d71f128e31fb2f0d10b579abf6523bae7d3c` and the unaccepted restricted-contract run at `0c668f233ad5c44e2c12bbbd80b3ac517fc084d0` are superseded for H2-F1. The latter run remains external and is not imported as accepted evidence. The final two-phase provenance is runner/helper/test/control commits through `9dfbb7962cd22b56b1899d10c05c3e97f2a10d2f`, then the generated-evidence freeze. A fresh round-4 independent review is still required.

The original TASK stop and HELP_HUMAN execution-form amendment remain unchanged. A1 and F-APP-2 boundaries remain unchanged.
