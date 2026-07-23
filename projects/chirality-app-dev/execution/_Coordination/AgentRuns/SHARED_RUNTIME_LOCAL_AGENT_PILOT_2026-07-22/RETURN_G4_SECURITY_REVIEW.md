# G4 Return — Independent Security and Regression Review

Status: `ACCEPTED_AFTER_REMEDIATION`

The first review rejected the fan-in for forgeable required-tool evidence,
missing-exit success synthesis, an unhardened boot consumer, stale residency
state, and premature PEC terminal forwarding.

Remediation introduced in-process completion receipts set only by the
Chirality-owned tool handler, strict final engine `process:exit` requirements,
buffered boot validation before persistence, external residency reconciliation,
and terminal buffering through upstream exhaustion.

An independent second review returned `ACCEPT`. Focused regressions cover all
five findings, plus project-token containment, token revocation, redirects,
approval attribution, run-level locks, and browser routing denial.
