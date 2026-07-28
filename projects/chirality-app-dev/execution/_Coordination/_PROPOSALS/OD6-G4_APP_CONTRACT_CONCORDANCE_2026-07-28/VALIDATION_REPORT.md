# D-APP-80 Validation Report

Date: 2026-07-28

Basis: `deb01644e324af2b39cff7b52abae43784cd071b`

Verdict: `PASS`

## Deterministic results

| Check | Result |
|---|---|
| Runnable contract-concordance validator | PASS |
| Complete contract population | PASS — 53 total |
| Decomposition-derived terminal-basis pins | PASS — 51 |
| PKG-00 controls preserved | PASS — 2 |
| Live `_CONTEXT.md` scope-ref equality | PASS — 53/53 |
| Explicit SCA-APP-006 downstream review set | PASS — 7/7 |
| Historical missing-basis relations preserved UNKNOWN | PASS — 6/6 |
| Missing historical object remains unresolvable | PASS |
| ScopeOfWork schema validation | PASS — 53/53 |
| APP-HOLD live tests | PASS — 14/14 |
| Current unresolved-basis scan | PASS — 0 scan-held |
| Active repair-validation register | PASS — 6 active and blocking |
| Missing repair-pending row negative test | PASS |
| Unaffected clear target positive test | PASS |
| Exact changed application surfaces | PASS — 56 |
| App receipt validator | PASS |
| Candidate whitespace validator | PASS |
| Path-anchor validator | PASS |
| `git diff --check` | PASS |

## Hold interpretation

The scan and register now answer different, compatible questions:

- the current-basis scan finds zero unresolvable contract declarations; and
- the register preserves six active `REPAIR_VALIDATION_PENDING` holds.

The guard requires all six D-APP-79 repair-pending IDs to remain in the
register even after basis repair. It also continues to require any future
scan-derived unresolvable target to appear in the register. Therefore a
successful repin is evidence for validation, not a hold release.

## Evidence identities

- `LIVE_SURFACE_MANIFEST.csv`:
  `6507828512e247f4cd96c1b2ae84cf72c7b1c1973bd2b69dfb21ef32206c7218`
- `CONTRACT_CONCORDANCE.csv`:
  `f3cf0588f50fcacc8d83aed24a758ef7d2e51b7dd2a488821044d218ce19f44b`
- `HISTORICAL_RELATIONS.csv`:
  `e4f3896b563a7ce822517cc3fae012101d6eb3a2a634f97e0da4f6ce0c46d1d8`
- `VALIDATION.json`:
  `7437f2ef4f047db27fba548c3f337260421f1d7e93702e6b397de6f8308819d0`
- `validate_contract_concordance.py`:
  `a525818c648f61e84e79667daee0b4d9b78dc48216fa1d9d1b2308ef9c1d0d28`

The package hash list is generated last after all narrative and ruling records
are stable.
