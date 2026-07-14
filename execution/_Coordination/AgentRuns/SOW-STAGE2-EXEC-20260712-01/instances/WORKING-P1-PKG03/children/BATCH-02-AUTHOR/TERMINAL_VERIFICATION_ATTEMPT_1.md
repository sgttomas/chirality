# Retained terminal-verification finding

After the complete author harness and terminal package generation passed, an
additional read-only binding check guessed the finalization report field name
as `production_sha256`. The registered report schema uses
`production_scope_of_work_sha256`, so that supplemental check raised
`KeyError` before completing its three-member loop.

Reason code: `SUPPLEMENTAL_CHECK_SCHEMA_KEY_GUESS`.

The check did not modify candidates, live inputs, or project state. The
remediation re-read the registered report, used its exact schema field, and
re-ran the manifest, finalization-binding, and wrong-member checks over all
three members. No registered Scope-of-Work tool failed or retried.
