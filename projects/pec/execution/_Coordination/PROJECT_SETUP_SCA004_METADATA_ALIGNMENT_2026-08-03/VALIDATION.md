# Validation — SCA-004 PROJECT_SETUP Metadata Alignment

**Verdict:** PASS for the authorized PROJECT_SETUP live-effect set.

## Pre-write guards

- Clean branch `codex/pec-sca004-metadata-alignment-20260803` at exact HEAD
  `88e7590d3664d4f1daf91bed2a8899bda0748b92`: PASS.
- Accepted basis and SCA hashes matched `MANIFEST.md`: PASS.
- Deliverable directories / contexts / references: `64 / 64 / 64`.
- Live-target count: `128`; canonical grouped newline-terminated path-list hash
  (63 sorted contexts, 64 sorted references, DEL-01-06 dependency register last):
  `1d0ce82cee00d1e66b447eff6e32062eb4038fa0564eef95a6c580f1736b074e`.
- All context/reference lexical preimages matched exactly once per target.
- Context, reference, and dependency component aggregates matched with members
  sorted within each population; the combined preimage aggregate matched the
  canonical grouped order. Recorded combined pre/post aggregates use that same
  grouped order.

## Post-write structural checks

| Check | Result |
|---|---|
| Context provenance | 64/64 cite revision 1.4 / SCA-004 |
| Context semantic parity | 64/64 match `Deliverables.csv` for identity, scope, and objective fields |
| Reference basis | 64/64 cite revision 1.4 / SCA-004 in the accepted-basis bullet |
| DEL-01-06 reference coverage | exact `SOW-077;SOW-094` |
| DEL-01-06 context preservation | SHA-256 `24f357cc9746b1b0b24991995ed72067062dba9ce7b098b472a5d6eed2db94b2` |
| TM-PEC-023 semantic preservation | all nine blank `SupportsObjectives` values unchanged |
| Changed live paths | exactly 128/128 allowlisted; zero missing / zero unexpected |

## Dependency validation

Commands:

```text
python3 tools/validation/validate_dependencies_schema.py <DEL-01-06>/Dependencies.csv
python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict
python3 tools/coordination/analyze_dep_closure.py projects/pec/execution
```

Results:

- DEL-01-06 register: valid v3.1 schema, 29 columns, 3 data rows.
- Strict project registers: 64 registers / 255 rows / 0 errors / 0 warnings.
- Row classes: 136 ANCHOR / 119 EXECUTION; evidence coverage 255/255.
- Graph: 62 nodes / 119 edges / 2 known zero-edge nodes / 0 nontrivial
  SCCs / 0 bidirectional pairs / 0 ID normalizations.

## Diff hygiene

- `git -c core.whitespace=cr-at-eol diff --check`: PASS.
- The `cr-at-eol` mode is required because the accepted register and appended
  row use CRLF. Plain `git diff --check` otherwise reports the required CR byte
  on the added CSV row as trailing whitespace.
- No staging, commit, push, lifecycle, acceptance, release, reliance, or pointer
  act was performed.

## Protected-state result

Decomposition truth, accepted pointers, lifecycle files, ScopeOfWork/SPEC,
source/tests, `_DEPENDENCIES.md`, the other 63 dependency registers, maps,
historical handoffs, receipts, reviews, Task Management registers, and foreign
loops remained outside the changed-path set.
