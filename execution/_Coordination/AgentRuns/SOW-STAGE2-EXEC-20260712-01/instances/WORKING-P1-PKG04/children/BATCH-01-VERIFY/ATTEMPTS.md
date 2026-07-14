# Verifier Attempts

## Attempt 1 — retained harness-binding failure

The first invocation stopped during `DEL-04-01` fresh conversion because the
accepted P1 row stores multiple scope references as comma-plus-space text and
the inherited PKG-03 harness passed the second token without trimming it. The
converter therefore emitted three extra spaces and did not match the accepted
evidence hash. The failed workspace and command record are retained under
`attempts/attempt-001/DEL-04-01`.

Classification: `VERIFIER_HARNESS_BINDING`; reason code:
`MULTI_REF_TOKEN_WHITESPACE`. This was not a source, candidate, semantic, or
tool discrepancy. No candidate or project file was written.

## Remediation and attempt 2

The verifier-owned harness was corrected to strip each comma-separated scope
and objective reference before invoking the deterministic converter. The
negative clean-file probe was also bound to a visible verifier-only comment
mutation instead of an extra terminal blank line. Attempt 2 completed all five
members and all required checkpoints with no member failure, retry, repair, or
candidate change.
