# D-PEC-71 validation report

**Status:** PASS — candidate is complete and AWAITING_OWNER_RULING
**Basis:** `main@85ea0628fa4e57dd6aae53b06139b2b8734a9612`
**Date:** 2026-07-28

## Candidate checks (run at the frozen basis)

| Check | Result |
|---|---|
| D-PEC-69 evidence manifest | PASS — 766/766 verify, zero mismatches |
| D-PEC-69 post-validation summary | PASS — 32 active contracts, all tool exits zero |
| D-PEC-69 terminal independent verification | PASS — rerun 3 |
| D-PEC-70 packet manifest | PASS — 5/5 verify |
| Active reliance-hold register | PASS — header-only, zero active rows |
| Cited commits resolve and are ancestors of the basis | PASS — 8/8 |
| Abbreviated closeout commits disambiguate uniquely | PASS — 1 candidate each |
| Concordance method SHA-256 matches the D-PEC-69 citation | PASS |
| Strict decomposition registers | PASS — 64 registers / 254 rows, zero errors, zero warnings |
| No existing ruled record modified | PASS — diff is additive only |
| Ruling placeholders confined to the record | PASS — zero placeholders in any packet file |

## Exact resolutions recorded by this candidate

| Abbreviated pin (D-PEC-70 closeout) | Full 40-hex resolution |
|---|---|
| `5fdbf6572` | `5fdbf657268d06e1c0aaaab99740fa5c57f760fc` |
| `80d8c65c7` | `80d8c65c7b41242c95f403ebdce3f99bad0684bd` |

Both are unique at the frozen basis (`git rev-parse --disambiguate` returns
exactly one candidate each) and both are ancestors of
`85ea0628fa4e57dd6aae53b06139b2b8734a9612`. The D-PEC-70 closeout is not
edited; the restatement lives only in the D-PEC-71 record.

## Merges in scope

| PR | Merge commit | Author == merger | GitHub reviews |
|---|---|---|---|
| #399 | `404e47c16a88e7ffdc6d1fc5fac61ebb6864211e` | yes | 0 |
| #406 | `592ba2a3c2762009aeec275316722c64716a3938` | yes | 0 |
| #407 | `058b294c49fa2ddc760a520fe6b8a45dc82e7189` | yes | 0 |

Merge-provenance evidence for the program lane is cited content-addressed by
artifact manifest SHA-256
`53844bfdcedaf5bae4396241375deba5dd35cc5b6d483342efac4a28268fccc1`
(`execution/_Evaluation/MERGE_APPROVAL_MATRIX_2026-07-28_85EA0628/`), which is
produced outside this packet's write fence and is not present at the frozen
basis.

## Deferred to the post-completion run

`validate_od8_rat.py` is a post-completion validator. On this candidate it is
expected to report BLOCK — ruling placeholders are present by design, the
register state reads `AWAITING_RULING`, `EffectiveCommit` is `PENDING`, and
receipt 119 has not been appended. It must report PASS after the completion
commit that records the owner's verbatim rulings, appends receipt 119, and
creates the effective-state closeout.

## Effect fence

The validated effect of this candidate is limited to adding one decision
record, one register row, and this evidence packet. No ScopeOfWork contract,
decomposition, PRD, topology, dependency, lifecycle, implementation, runtime,
estimate, schedule, release, hold, or product source surface changes, and no
already-ruled record is edited.
