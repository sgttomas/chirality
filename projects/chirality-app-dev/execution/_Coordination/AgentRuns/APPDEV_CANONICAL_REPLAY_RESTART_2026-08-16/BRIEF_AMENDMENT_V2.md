# Brief amendment v2 — actual CLI façade

Integrated review found that a second `RuntimeClient` did not satisfy the
selected Desktop + CLI target. The test-only implementation node was reopened
to exercise Root `runtime/packages/cli` public `runCli` using `session replay
--project ... --session ... --json`, capture CLI output, decode it, and compare
the parsed canonical replay structurally with Desktop before and after restart.
Root remains read-only. Raw-byte equivalence is not claimed for parsed replay;
byte identity remains limited to raw legacy source-file preservation. Focused
test, typecheck, scope/whitespace checks, and fresh full-diff review are required
before renewed acceptance.
