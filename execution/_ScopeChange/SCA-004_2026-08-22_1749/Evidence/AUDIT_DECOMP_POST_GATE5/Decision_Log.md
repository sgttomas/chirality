# AUDIT_DECOMP post-Gate-5 decision log

| ID | Decision | Basis / effect |
|---|---|---|
| AUD-POST-001 | Apply the owner-fenced output-location override. | All evidence is written only under `Evidence/AUDIT_DECOMP_POST_GATE5/`; no audit pointer or `_LATEST.md` is written. |
| AUD-POST-002 | Audit the applied authoritative package and synchronized companion/trace/telemetry surfaces. | This is the closure-lane backcheck after Gate 5, not a PREPARATION/folder-coverage act. |
| AUD-POST-003 | Treat intentionally deferred new folders as downstream propagation state. | R3-B and R5-A exclude INIT, SOW, lifecycle, dependency, estimate, schedule, graph, and dependency-closure acts from Gate 5. Their absence is not an applied-package mapping defect. |
| AUD-POST-004 | Compare topology to the immutable Gate-1 baseline. | Baseline SHA-256 `2210e77f…e9e45` is preserved; the exact delta is +7 deliverables, +6 in PKG-02, +1 in PKG-04, with package/scope/objective counts unchanged. |
| AUD-POST-005 | Return PASS for the Gate-5 applied package only. | All expected counts and mapping/trace invariants pass with zero findings; downstream derivative closure remains open. |
