# N2 SCOPE_CHANGE Return — Phase-2 Companion Register Candidate

**Verdict:** `PASS — COMPLETE_AWAITING_OWNER_APPROVAL`
**Basis:** `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`
**Authority effect:** none; exact candidate only
**ReadyForNextPhase:** `NO`
**Next node:** `N3-REVIEW-01`

## Outcome

N2 produced the exact additions-only full-file post-image candidate for the App companion invariant-coverage register and a transaction record. The live register and every authoritative surface remain unchanged.

## Output identities

| Path | SHA-256 | State |
| --- | --- | --- |
| `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase2/CONTRACT_INVARIANT_COVERAGE_REGISTER_RESOLVED_CANDIDATE.csv` | `f2d2e904d4f8b58da106fdcde7ed495146ea7d67de97f5b0535608879dab0079` | `COMPLETE_AWAITING_OWNER_APPROVAL` |
| `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-008_2026-08-23_1727_V3_Release_Pathway/Phase2/COMPANION_REGISTER_REBUILD_TRANSACTION.md` | `ace737e599d8f7ec5bdefa47192e30a83f4c12112a032ffe0e0df834dda7ca84` | `TRANSACTION_EVIDENCE` |

The live full-file pre-image is SHA-256 `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1`, 88,985 bytes, with 81 unique IDs across 48 families. The candidate is 97,803 bytes, with 83 unique IDs across 50 families. The exact +2/+2 delta is K-CONSENT-1/K-CONSENT and K-UNTYPED-1/K-UNTYPED; no ID is duplicated or removed.

## N1 and full-candidate binding

- N1 candidate consumed only at SHA-256 `779d4874adc2fc3669078a0431f676fe50d31acbd2dd82c8c405714343fa1df0`.
- All 83 rows bind `ContractSourceSHA256` to resolved full App-contract candidate `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8`.
- All 83 rows bind `AppDecompositionBasis` to approved candidate `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f`.
- Every source line anchor resolves to the same invariant ID in the reconstructed candidate contract layout.

## K-CONTROL-1 hold proof

The K-CONTROL-1 row has both:

```text
OpenIssueIDs=PENDING_ROOT_AMENDMENT
CoverageStatus=PENDING_ROOT_AMENDMENT
```

Its authority references cite A4-B/A5-B. This is an explicit ineligibility state, not stale mapped coverage. The candidate does not claim Root has amended K-CONTROL-1 and does not claim the atomic contract group is eligible for Gate 5.

## Gate-3 amendment coverage

The candidate includes:

- resolved K-EVENT-4;
- K-CONSENT-1 and K-UNTYPED-1;
- confirmed K-ROLE-2;
- K-NET-1, K-KEY-1, K-EVENT-3, and K-EVENT-6;
- the held K-CONTROL-1 row;
- all six consequential enforcement-map relationships across the 19 affected/new invariant rows.

## Validation and sequencing

The raw candidate was written before any output artifact pinned its hash. Candidate whitespace then passed against exact basis `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`. Subsequent CSV parse, uniqueness, count, anchor, source-identity, K-CONTROL state, enforcement-map completeness, protected-identity, containment, candidate-whitespace, and `git diff --check` checks passed.

## N3 review handoff

N3 must review exactly:

1. N1 resolved K-EVENT-4 candidate SHA-256 `779d4874adc2fc3669078a0431f676fe50d31acbd2dd82c8c405714343fa1df0`;
2. resolved full App-contract candidate SHA-256 `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8`;
3. N2 raw companion-register candidate SHA-256 `f2d2e904d4f8b58da106fdcde7ed495146ea7d67de97f5b0535608879dab0079`;
4. the 81/48 → 83/50 accounting proof and exact +2/+2 delta;
5. K-CONTROL-1's exact `PENDING_ROOT_AMENDMENT` state and the absence of any stale coverage or Gate-5 eligibility claim;
6. every Gate-3 changed/new row and all six consequential enforcement-map relationships.

| State | Value |
| --- | --- |
| `CandidateState` | `COMPLETE_AWAITING_OWNER_APPROVAL` |
| `AuthorityState` | `NO_NEW_AUTHORITY` |
| `TruthState` | `AUTHORITATIVE_SURFACES_UNCHANGED` |
| `NextGateState` | `N3_FRESH_INDEPENDENT_REVIEW_REQUIRED` |

`ReadyForNextPhase = NO`.
