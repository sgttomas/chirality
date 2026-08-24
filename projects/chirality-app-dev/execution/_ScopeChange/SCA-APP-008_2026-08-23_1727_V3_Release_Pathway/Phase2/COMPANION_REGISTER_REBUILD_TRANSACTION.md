# SCA-APP-008 Phase 2 — Companion Invariant-Coverage Register Rebuild

**State:** `AWAITING_OWNER_APPROVAL`
**Authority effect:** `CANDIDATE_ONLY — NOT_APPLIED`
**ReadyForNextPhase:** `NO`
**Basis commit:** `4c9fdb4cc9031b376f220ceb5c34afa3874eacb7`
**N1 input:** `K_EVENT_4_RESOLVED_CONTRACT_ROW_CANDIDATE.md`, SHA-256 `779d4874adc2fc3669078a0431f676fe50d31acbd2dd82c8c405714343fa1df0`
**Resolved full App-contract candidate:** SHA-256 `a79282970bbd96d27e28846605be2ce0b3433c0f6c991bbc5911548c6f7e56c8`

## Boundary and effect

This additions-only artifact describes the exact full-file companion-register post-image candidate at `CONTRACT_INVARIANT_COVERAGE_REGISTER_RESOLVED_CANDIDATE.csv`. It does not edit or replace the live companion register, apply the contract or decomposition candidates, move `_LATEST.md`, create Gate-5 eligibility, route a notice, or confer implementation, lifecycle, release, or foreign-loop authority.

A4-B/A5-B sequence Root's K-CONTROL-1 design amendment ahead of App application. Accordingly, the candidate row for K-CONTROL-1 is marked exactly `CoverageStatus = PENDING_ROOT_AMENDMENT` and `OpenIssueIDs = PENDING_ROOT_AMENDMENT`. The candidate makes no current coverage or Gate-5 eligibility claim for that row. A5-C retains one Gate-5 act for the decomposition and contract groups after all eligibility conditions and exact owner approvals are satisfied.

## Exact full-file transaction

| Field | Exact value |
| --- | --- |
| Target | `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` |
| Target full-file pre-image SHA-256 | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` |
| Target pre-image bytes | `88985` |
| Target pre-image rows | `81` data rows plus one header |
| Target pre-image invariant IDs | `81` unique |
| Target pre-image invariant families | `48` unique |
| Candidate full-file post-image SHA-256 | `f2d2e904d4f8b58da106fdcde7ed495146ea7d67de97f5b0535608879dab0079` |
| Candidate post-image bytes | `97803` |
| Candidate post-image rows | `83` data rows plus one header |
| Candidate post-image invariant IDs | `83` unique |
| Candidate post-image invariant families | `50` unique |
| ID/family delta | `+2 IDs / +2 families`: K-CONSENT-1/K-CONSENT and K-UNTYPED-1/K-UNTYPED |

The 81-ID/48-family baseline accounting discipline is preserved by a complete census, collision check, and explicit delta. It is not preserved by falsely reporting the post-image as 81 IDs: the two owner-approved, collision-free candidate IDs make the accountable post-state 83 IDs across 50 families.

Application grammar for a later owner-approved Gate-5 act:

1. require the live target SHA-256 to equal the pre-image above;
2. require the resolved full App-contract candidate SHA-256 and exact decomposition candidate SHA-256 `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f`;
3. require the raw candidate file SHA-256 to equal the post-image above;
4. require 83 unique invariant IDs, 50 unique families, no duplicate ID, and exactly one row each for K-CONSENT-1 and K-UNTYPED-1;
5. require every `ContractSourceSHA256` cell to equal the resolved contract candidate and every `AppDecompositionBasis` cell to name the exact decomposition candidate;
6. require every `SourceAnchor` to resolve to the same invariant ID in the exact contract candidate;
7. require K-CONTROL-1 to remain `PENDING_ROOT_AMENDMENT` unless the ratified Root amendment and a later exact owner-approved candidate supersede these bytes;
8. apply the full file atomically; never mix rows from this candidate with the live pre-image.

## Rebuild inventory

All 81 existing rows are mechanically rebased to the resolved full-contract candidate SHA-256 and the approved full decomposition candidate SHA-256. Source line anchors are deterministically shifted for the two new invariant rows, six new enforcement-map rows, and one new accepted-scope-change row.

The substantive row set is:

- amended invariant rows: K-ROLE-2, K-NET-1, K-KEY-1, K-EVENT-3, K-EVENT-4, K-EVENT-6;
- held invariant row: K-CONTROL-1 (`PENDING_ROOT_AMENDMENT`);
- new invariant rows: K-CONSENT-1 and K-UNTYPED-1;
- consequential enforcement-map references: K-AUTH-1, K-CONTROL-1, K-EVENT-3, K-EVENT-4, K-EVENT-6, K-KEY-1, K-NET-1, K-PACKAGE-1, K-PATH-2, K-RELEASE-1, K-ROLE-2, K-ROOT-1, K-SDK-1, K-SUBAGENT-1, K-SUBAGENT-2, K-SUBAGENT-3, K-VALIDATE-1, plus the two new rows.

The six exact Gate-3 enforcement-point names are added to every referenced row's `EnforcementSurfaces` field:

1. `Delegated-harness process supervisor and control sockets`;
2. `` `HostedEngineConsentPort` and account/root continuity ``;
3. `Role entry and managed/native descendant classification`;
4. `Event codec, coordinator, persistence, SSE, replay, diagnostics, and support sinks`;
5. `Renderer credential IPC`;
6. `Exact-candidate release validation`.

## Exact anchor accounting

The candidate contract inserts K-UNTYPED-1 at line 119 and K-CONSENT-1 at line 127. Existing live source anchors are shifted by this deterministic rule:

| Live line interval | Candidate-line delta |
| --- | ---: |
| `<119` | `0` |
| `119..125` | `+1` |
| `126..167` | `+2` |
| `168..193` | `+8` |
| `>=194` | `+9` |

Consequently K-CONTROL-1 resolves at line 209 and K-ROLE-2 at line 213. The six enforcement-map additions occupy lines 170–175, and the accepted SCA-APP-008 row occupies line 202. Anchor validation uses exact invariant IDs rather than positional inference.

## Validation boundary

The raw CSV candidate was written before this hash-pinning artifact. The N2 SCOPE_CHANGE manager then ran:

```text
python3 tools/validation/validate_candidate_whitespace.py --base-ref 4c9fdb4cc9031b376f220ceb5c34afa3874eacb7
PASS: candidate whitespace is clean (untracked binary/symlink paths safely skipped: 0).
```

Only after that PASS were the post-image SHA-256 and this transaction record generated.

## Candidate handoff

| State | Value |
| --- | --- |
| `CandidateState` | `COMPLETE_AWAITING_OWNER_APPROVAL` |
| `AuthorityState` | `NO_NEW_AUTHORITY` |
| `TruthState` | `AUTHORITATIVE_SURFACES_UNCHANGED` |
| `NextGateState` | `N3_FRESH_INDEPENDENT_REVIEW_REQUIRED` |

`ReadyForNextPhase = NO`.
