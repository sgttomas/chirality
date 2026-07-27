# OD-7 Final Package Validation

Verdict: `PASS_WITH_ONE_RECORDED_SCHEMA_WAIVER`

- Accepted basis: `ef164c20c8a903a7ecff9450f677938a4111392f`;
  worktree `HEAD` matched exactly.
- Basis identity: 33/33 manifest paths existed and reproduced their SHA-256.
- Frozen return hashes: 4/4 reproduced the values in
  `FANIN_VALIDATION.md`.
- Return schema: 30/31 issue dispositions provided all twelve required
  fields. The single omitted `Unknowns` cell on the closed
  `PIP-EXISTING-AGENT-NOTICE` row is explicitly waived and treated as `None`;
  no frozen return was edited.
- CSV structure: `BASIS_MANIFEST.csv` 33 rows × 4 columns;
  `FINDINGS.csv` 22 rows × 10 columns; `ACTION_GRAPH.csv` 17 rows × 10
  columns.
- Evidence anchors: 132/132 return file-and-line references and 60/60
  synthesized references resolved.
- Scope containment: Git status showed only this evaluation package as
  untracked; no subject-state file was changed.
- Diff quality: `git diff --check` passed.
- Integrity: `ARTIFACT_HASHES.sha256` was generated last to cover all 13
  other package files and is required to verify 13/13 before handoff.

This validation closes only the derivative evaluation package. It authorizes
no remediation, ruling, notice, pointer update, SCOPE_CHANGE gate, or Git
action.
