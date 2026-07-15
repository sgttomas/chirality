# ORCHESTRATOR-P4-B0 Attempts and Mechanical Disposition

## Attempt 1 — predecessor-transform guard

The first builder execution stopped before snapshot creation because the new
P4 delta initially targeted the W-P3 wrapper rather than its accepted W-P2
base builder and therefore could not match the generated manager expression.
No snapshot, project, candidate, lifecycle, Git, or authority state was
written. Inspection identified this as a mechanical transform-source defect.

## Attempt 2 — completed and rebound

The builder was rebound directly to the accepted W-P2 deterministic base with
audited cumulative P3/P4 deltas. It completed the exact 22-member census and
wrote the owned derivative snapshot. Population, binding, lifecycle, format,
batch, dependency-direction, method, predecessor, ref, and containment gates
passed. Registered command checks then passed: 22/22 dependency schemas,
self-check exit 0 with unchanged cross-root baseline findings outside this
preflight scope, and 264/264 practitioner harness tests. Finalization rebuilt
all direct snapshot bindings and produced manifest SHA-256
`e3c0ba738b4109fe8ab3eccaaab1e76e82e213b5e6b27f9dd6632c7716682faf`.
The final integrity scan found 21/21 bindings exact, valid JSON, and zero
terminal-LF defects. A final live recheck found 198/198 live bindings and
29/29 method bindings unchanged.
