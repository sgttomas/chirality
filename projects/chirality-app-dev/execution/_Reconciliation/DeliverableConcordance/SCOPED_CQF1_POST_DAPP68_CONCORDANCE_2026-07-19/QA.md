# QA — Activation-Failure Package

## Checks

- Requested basis SHA equals live `HEAD`: PASS.
- Requested branch equals live branch: PASS.
- Scope manifest has 22 data rows, 22 unique paths, and five Remaining
  containers: PASS.
- Ordered scope-path SHA-256 matches
  `2e314f3f601350736032ace2730492c2afa6ab5b21fe26465d799470a195fc36`:
  PASS.
- Activation ruling with exact RunID, scope, method, and committed run pointer:
  **FAIL**.
- Subject corpus writes: NONE.
- Subagent dispatch: NONE.
- Derivative ledger scope accounting: 22 rows, each exactly once, all
  `BLOCKED_INPUT`.
- Candidate mappings: 0.
- Owner slate: absent because no path-level owner classification was validly
  produced.
- Waivers: none.

## Validation limit

Source, test, documentation, affinity, and mapping validation was not run; it
would be invalid after the activation preflight failure. Structural CSV,
Markdown, path-containment, and diff-hygiene checks are the only applicable
R1 validations.
