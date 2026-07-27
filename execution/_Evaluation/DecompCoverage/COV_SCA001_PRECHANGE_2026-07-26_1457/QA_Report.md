# QA Report

## Input and section resolution

- Decomposition readable: PASS (`/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`; 615 lines).
- `Packages` semantic section: exact heading match at line 246.
- `Deliverables` semantic section: exact heading match at line 271.
- `Scope Ledger` semantic section: exact heading match at line 364; authoritative rows loaded from `/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`.
- SOFTWARE objective binding: unique objective IDs resolved from the Scope Ledger `ObjectiveIDs` column; the dedicated `Objectives` section and `/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Decomposition/chirality_root_objective_register_v1_0.csv` were also used for cross-surface support-count validation.
- Companion inventory: explicit at decomposition §3; authoritative roles are discoverable.
- Parse ambiguities: none.

## Scan coverage

- Package folders scanned: 6.
- Deliverable folders scanned: 45.
- `_CONTEXT.md` files read: 45.
- `_STATUS.md` files read: 45.
- `ScopeOfWork.md` contracts validated by `tools/scope_of_work/validate_scope_of_work.py`: 45.
- Scope-ledger rows checked: 103 total, 94 IN.
- Objective support surfaces compared: deliverable register against objective register for 7 objectives.

## Deterministic limits

- Artifact presence is filename-based and folder-local, as required by Check 6. Control files (`_*.md`) and the `ScopeOfWork.md` production contract are not counted as produced anticipated outputs.
- An anticipated path outside its deliverable folder (for example `execution/_harness/root_guards.yaml`) remains INFO-not-present for Check 6 even if a file exists elsewhere, because the protocol directs the scan to the deliverable folder.
- Semantic similarity for descriptions was not needed: all normalized descriptions matched exactly.
- No prior-run comparison was requested.
- `_ScopeChange/_LATEST.md` was absent. Check 10 is therefore SKIPPED for this pre-change baseline; no active SCOPE_CHANGE snapshot was claimed or inferred.

## Output validation

- Required artifact count: 8/8.
- Issue-log schema: valid, including string check number `9b` support (no 9b issue emitted).
- Coverage-matrix schema: valid.
- Summary JSON: parseable and schema fields present.
- Evidence pointers: every emitted issue names both a decomposition/register reference and a filesystem path.
