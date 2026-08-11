# Stage 2 — historical command-identity scan

Status: `PASS — ZERO MATCHES`

Frozen form F02 was executed against the six explicit paths in
`allowlists/SALVAGE_FILES.txt` with the manager's full pattern set:

```text
C[0-9]{3,}|A3-OP-[0-9]{3}|R[0-9]+-C[0-9]{3,}|ATTEMPT[-_ ]?[0-9]+[-_ ]?CMD[-_ ]?[0-9]+
```

Observed result: exit `1`, stdout `0` bytes. Under the frozen form contract,
that is the required clean zero-hit result. The command named all six files
explicitly; it did not list, glob, search, or walk any historical root.

The exact F02 invocation was executed twice because the first orchestration
wrapper failed while formatting the already-completed command result. Both
executions used identical explicit operands. The retained second observation
was exit `1`, stdout `0` bytes. Native context telemetry: unavailable.
