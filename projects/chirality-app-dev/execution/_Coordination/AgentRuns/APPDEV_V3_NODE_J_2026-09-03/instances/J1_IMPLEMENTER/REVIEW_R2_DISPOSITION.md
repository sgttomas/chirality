# Node J round-2 review disposition

- Reviewed freeze: `26a1e43cd3177bb1fef9eff7ddf02310e413fb89`
- Review verdict: `FAIL` — 0 BLOCKER, 3 MAJOR, 0 MINOR, 0 NOTE
- Review report: `/private/tmp/chirality-app-v3-slate3-20260903/reviews/nodeJ/REVIEW_02_2026-09-03_over_26a1e43cd.md`
- Review SHA-256: `e48e5c6e86698c32d778224a0ff65d813a2b8c05b6672846efb5775dca9a4601`
- Scope response: remediation only; no product, status, receipt, Root, plan, register, or decision-record byte added

| Finding | Disposition | Implementation and proof |
|---|---|---|
| J2-F1 — non-unique identity and signal-boundary race | REMEDIATED IN RUNNER | Replaced individual-PID signalling with retained POSIX session/process-group controllers. Each controller is the unreaped group leader through the final atomic group signal, so its PID/PGID cannot be reallocated during the controlled lifetime. Recursive descendants inherit the group, TERM reaches the whole group, and KILL reaches verified survivors plus the controller without a PID check-to-signal interval. The deterministic proof launches two same-command processes in the same start-second outside the controlled group, proves both survive controlled TERM/KILL, and proves a TERM-resistant controlled descendant is removed. |
| J2-F2 — observation failures inferred as clean | REMEDIATED IN RUNNER | Process-table and port-listener observations are tri-state. Any observation failure records `UNKNOWN`, sets cleanup failure, and prevents a zero-count inference. The deterministic proof forces process inspection failure while a controlled child is live and forces `lsof` failure; both cleanup paths exit 74 and retain verifying manifests. A simultaneous incoming status 23 remains authoritative. |
| J2-F3 — false exact-HEAD provenance | IN PROGRESS: TWO-PHASE METHOD | This first phase freezes only the final runner, helper, deterministic regression, and review-control bytes. The retained live proof will run from this clean runner commit into an external run root. The evidence commit will record application/product snapshot basis `ede175910c67b384332324622b17695f69e6a715`, the exact clean runner commit SHA, the clean pre-run status, and an explicit superseded-candidate disposition before round-3 review. |

The original TASK stop and HELP_HUMAN execution-form amendment remain unchanged. A1 and F-APP-2 boundaries remain unchanged. Fresh round-3 independent review is required after the evidence commit.
