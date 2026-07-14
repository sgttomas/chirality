# Independent Reconciliation Checks

Verdict: `PASS_WITH_LIMITS`.

## Reproduced quality

- Basis remains exact `main@ef461cfdb3a4b135dc670b04f646eca3eac47712`; the accepted Stage-2 plan/run and all three live deliverable paths have zero tracked diff from that basis.
- Exact scope is `DEL-01-02`, `DEL-01-03`, and `DEL-01-04`; all 27 frozen source/status/control/dependency hashes reproduce against both the accepted P1 rows and live bytes. Lifecycle is still `IN_PROGRESS`, format is still complete `LEGACY_FOUR_DOC`, and no live `ScopeOfWork.md` exists.
- Corrected package manifest `68ef7561011b2ba8a3abf69e3dc00ab0a4f4cf69b18beb982c1e1a1bd31bb72c`: 133/133 rows rehashed. Corrected manager manifest `bbc5bddc118e2138a92fd0b465b19ad0803afea38339aefbbb9bcbfb9d56347a`: 29/29 rows rehashed. Author and verifier manifests remain respectively 265/265 and 317/317 at their recorded hashes. Every path is portable and every byte/line binding reproduces.
- Independent duplicate conversions equal each other and the accepted candidates byte-for-byte. All three candidates validate as standalone `SOW_V1`; all six isolated workspaces validate as authorized `MIGRATION_DUAL`.
- Claim map, parity, checklist, and render pairs are byte-identical for every member. All 88 mappings are `PRESERVED`; continuous first-to-last line disposition covers exactly 727/727 source lines with current source hashes, defined target IDs, no issue, mismatch, gap, or silent loss.
- Each deterministic checklist contains exactly `AC-001`, exact text, candidate/source identity, `OUT-001`, and matrix-linked `VER-001`. Each render is source-hash-bound, deterministic, script/form/iframe-free, and has no external resource reference.
- Every member independently fails closed for partial legacy conversion, unauthorized dual validation, unauthorized dual checklist derivation, and legacy-only checklist derivation; failed checklist probes emit no artifact.
- Live four-document and dependency-schema checks pass 3/3. Exact 15-row replacement equals the package manifest and exact 15-row rollback is its action/hash inverse. Apply, target `SOW_V1` validation, and exact legacy rollback pass 3/3 in run-local scratch with all nine source/control hashes restored.
- Conservative content judgment passes: the converter-generated `OUT-001`, `AC-001`, and `VER-001` for each member are grounded in the preserved source kit and do not resolve retained TBDs, invent legal/professional authority, or change lifecycle meaning. This is faithful representation evidence only, not substantive approval of the policy or engineering content.

## Repository substrate

- Practitioner self-check independently exits 0 with the unchanged baseline: `INFO=15`, `NOT_APPLICABLE=2`, `REVIEW=27`, `WARN=6`, no `BLOCK`.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider tools/practitioner_harness` independently passes `264 passed in 69.09s`.
- DEC-025 remains not applicable because the experiment changes no project code path.

## App comparison

The accepted App ordinary waves were reopened at their immutable member and simulation ledgers, not accepted from narrative alone:

| Evidence | Members | Mappings | Source lines | Replacement rows | Simulations | Manifest SHA-256 |
|---|---:|---:|---:|---:|---:|---|
| App A1 | 15 | 456 | 4,817 | 75 | 15 | `c8ae005ca8d1007ccf7f7ee12dc81f441ad65ae3fa094d7314249e747831a5eb` |
| App A2 | 16 | 491 | 5,584 | 80 | 16 | `0dbf05dec12668517f3b34097d15afdb5bff3a9bfa9f73569f614883238b000d` |
| App A3 | 16 | 481 | 4,985 | 80 | 16 | `53fbec09f4d174f4de1744fdaf38b88f3d28ba2936b10cdc83087d1bbb76f10f` |
| App total | 47 | 1,428 | 15,386 | 235 | 47 | three accepted manifests above |
| PKG-01 experiment | 3 | 88 | 727 | 15 | 3 | corrected package manifest above |

PKG-01 preserves the same representation-migration gates and separation of schema, content authority, preservation, and substrate verdicts. App-specific frontend/typecheck/build checks have no Piping-content analogue; the applicable shared harness and Piping package checks pass. The migration-quality result is therefore `PASS_EQUIVALENT` for this three-member scope.

## Limits

Native token occupancy and context-window utilization were unavailable. No comparable wall-clock or token-cost baseline was captured, so session-count reduction is observable but time/token savings are not established. This experiment cannot set a safe larger-package size.

