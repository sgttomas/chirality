# N2 Validation Evidence — Phase-2 Companion Register Candidate

**Basis:** `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`
**Candidate SHA-256:** `f2d2e904d4f8b58da106fdcde7ed495146ea7d67de97f5b0535608879dab0079`

## Required ordering

1. Wrote the raw full-file CSV candidate.
2. Ran candidate whitespace against the exact basis: PASS.
3. Computed the candidate SHA-256 and byte count.
4. Authored the hash-pinning transaction and run records.

No pinning artifact existed before step 2.

## Mechanical checks

| Check | Result |
| --- | --- |
| CSV parse | `PASS` — 18 columns, 83 data rows |
| Unique invariant IDs | `PASS` — 83/83 unique |
| Unique invariant families | `PASS` — 50 |
| Pre→post accounting | `PASS` — 81/48 → 83/50, exactly +2/+2 |
| New IDs | `PASS` — exactly K-CONSENT-1 and K-UNTYPED-1 |
| Contract-source identity | `PASS` — all 83 rows equal `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8` |
| Decomposition basis | `PASS` — all 83 rows equal candidate `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f` |
| Source-anchor ID resolution | `PASS` — 83/83 exact against the reconstructed candidate contract line layout |
| K-CONTROL-1 coverage status | `PASS` — exactly `PENDING_ROOT_AMENDMENT` |
| K-CONTROL-1 open-issue state | `PASS` — exactly `PENDING_ROOT_AMENDMENT` |
| Consequential enforcement references | `PASS` — all six Gate-3 map rows represented on all referenced invariant rows |
| Duplicate IDs | `PASS` — none |
| Candidate byte count | `97803` |
| Candidate line count | `84` including header |

## Protected-surface checks

- live companion register remains SHA-256 `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`;
- live App contract remains SHA-256 `6d3a082c5f0821e11d22de37db2d65af950edbe30f403843534031b976a1e4d7`;
- `_ScopeChange/_LATEST.md` remains SHA-256 `a0298fdc5709181119d4c645b72b72f07b0c3b14904da67043d9de1f7ee01794`;
- App Task Management register remains SHA-256 `eb37fba1bdc46209bdbb576815c1161ffed81b375454a30b0022d5ef863320e6`;
- frontend tree remains `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`;
- N1 candidate remains SHA-256 `779d4874adc2fc3669078a0431f676fe50d31acbd2dd82c8c405714343fa1df0`.

The candidate makes no application, current implementation-coverage, Gate-5 eligibility, lifecycle, pointer, notice-routing, or release claim.
