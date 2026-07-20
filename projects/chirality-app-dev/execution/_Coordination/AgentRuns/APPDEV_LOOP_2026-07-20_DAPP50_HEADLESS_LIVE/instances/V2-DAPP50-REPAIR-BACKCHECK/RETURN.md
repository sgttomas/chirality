# V2 D-APP-50 Repair Backcheck Return

## Terminal result

`BLOCK`

Fresh independent EVALUATION completed all nine released adversarial questions.
V1 F-002 is cured, but F-001 remains incompletely cured because the repaired
adapter accepts an exit-0 runner result whose declared result envelope has no
matching checksum reference. Final CHANGE publication remains held.

## Finding

`V2-F-001` is a deterministic result-contract blocker. The focused positive
fixture declares `result_envelope_ref` but its only checksum targets
`runner_request`; the real configured transport accepts it and the focused
suite passes 48/48. The app validates individual checksum shape but not the
required cross-reference. Piping's final `validate_result` emits
`HEADLESS_RUNNER_RESULT_ENVELOPE_CHECKSUM_MISSING` for this condition, and the
committed TP-RUNNER-015 exit-0 witness contains the required matching checksum.
This is nested transport/result correlation, not an exhaustive solver-semantic
claim.

The separately examined `TBD` diagnostic-class token is authorized by the
frozen headless-runner schema and is not a finding.

## Coverage and checks

- G0 exact 14 paths/hashes and G1 exact two paths/hashes/topology: PASS.
- Frontend clean at G1; empty index; expected closeout/control/evaluation dirt
  contained: PASS.
- Original runner path/hash/process/stdin/stdout/timeout/cap/error and
  `runnerInputRef` containment controls: PASS.
- Exact `open_pipe_stress` registry/profile gate; read-only/exclusive
  descriptor; normal permission/event/redaction/budget/evidence/artifact path;
  no boundary expansion: PASS.
- Focused repaired suite 48/48; catalog 2/2; typecheck; full frontend 776 pass
  / 4 skipped; production build: PASS.
- Managed premerge Section 8 8/8 and Section 9 16/16: PASS. The evaluator-owned
  server was stopped. The initial absent-server attempt ran zero checks and was
  superseded by the complete managed rerun.
- Pull-contract validator, dependency lint, receipt validator, authority corpus
  v9 8/8, repository self-check baseline, validation pytest 123/123, and
  practitioner-harness pytest 311/311: PASS.
- D-APP-48 final pin/version/exports/false boundaries, DEL-10-01 lifecycle/
  Remaining/Checking SHA, W2/W4 history/run records, Receipt-83 prefix,
  Receipt-84 cursor, decision register, and unrelated-state containment: PASS.
- F-002: PASS — `frontend/dist` absent; no material distribution artifact or
  relevant process remains. Normal ignored `.next` and `dist-electron` remain
  distinct.

Coverage limitations: none. Blockers: 1. Unknowns: 0. Conflicts: 0. Waivers:
0. Final CHANGE is not released. Required route is bounded WORKING_ITEMS
repair, reachable CHANGE commit, append-only repin/correction, then fresh
independent EVALUATION.

## Evaluation outputs

The evaluation manifest binds the four narrative/register files. Exact hashes
for the complete five-file package and all three terminal records are returned
to the parent after terminal write verification.

## Subject preservation

No source, contract, receipt, decision, deliverable, Git, packaging, or cleanup
mutation was performed. Durable V2 writes are confined to the released
evaluation root and terminal instance. Required checks refreshed only ignored
ordinary build/harness outputs; `frontend/dist` remains absent.
