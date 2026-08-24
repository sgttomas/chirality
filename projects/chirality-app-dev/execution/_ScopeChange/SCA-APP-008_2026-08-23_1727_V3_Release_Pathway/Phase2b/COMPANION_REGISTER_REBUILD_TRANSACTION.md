# SCA-APP-008 Phase 2b — Companion Invariant-Coverage Register Rebuild

**State:** `AWAITING_OWNER_APPROVAL`
**Authority effect:** `CANDIDATE_ONLY — NOT_APPLIED`
**ReadyForNextPhase:** `NO`
**Basis commit:** `ef92fab10f40aa95da484701982d83fa1abca874`
**Resolved full App-contract candidate:** SHA-256 `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`

## Boundary and effect

This additions-only artifact describes the exact full-file companion-register
post-image candidate at
`CONTRACT_INVARIANT_COVERAGE_REGISTER_REGENERATED_CANDIDATE.csv`. It does not
edit or replace the live companion register, apply a contract or decomposition
candidate, move `_LATEST.md`, activate DEL-02-07/WP-03, route a notice, or
confer implementation, lifecycle, release, publication, or foreign-loop
authority.

Root's K-CONTROL-1 design amendment is ratified. The K-CONTROL-1 row is now
design-mapped to Root `docs/CONTRACT.md` line 162 at SHA-256 `ad0a4e6a…`
under external Root authority. Its coverage remains explicitly open for the
separately gated DEL-02-07/WP-03 implementation: it claims one live control
socket and design-gated supervisor-socket and two-listener tests, never a live
second socket or implementation coverage.

## Exact full-file transaction

| Field | Exact value |
| --- | --- |
| Target | `projects/chirality-app-dev/execution/_Decomposition/contract_invariant_coverage_register.csv` |
| Target full-file pre-image SHA-256 | `84d6fe0008c5ef210f8e70e583bb45251bf3170c01a5bbaea0c7bf752b88f5a1` |
| Target pre-image bytes | `88985` |
| Target pre-image rows | `81` data rows plus one header |
| Target pre-image invariant IDs | `81` unique |
| Target pre-image invariant families | `48` unique |
| Superseded Phase-2 candidate SHA-256 | `f2d2e904d4f8b58da106fdcde7ed495146ea7d67de97f5b0535608879dab0079` |
| Raw Phase-2b candidate SHA-256 | `69abc8859cc10596f959527eb35a6620d7d4c536e8b415644a26e83cf74534a0` |
| Raw Phase-2b candidate bytes | `98230` |
| Candidate rows | `83` data rows plus one header |
| Candidate invariant IDs | `83` unique |
| Candidate invariant families | `50` unique |
| ID/family delta from live | `+2 IDs / +2 families`: K-CONSENT-1/K-CONSENT and K-UNTYPED-1/K-UNTYPED |

Application grammar for a later exact owner-approved Gate-5 act:

1. require the live target SHA-256 to equal the pre-image above;
2. require the resolved full App-contract candidate SHA-256
   `842bf170e6737adf8eaa7a4a1acfd74e22390bc6e14c64eed9502195c68dbed9`
   and exact decomposition candidate SHA-256
   `932b890e4de38c0fc59d1fcffeb75d9d436c74aeac6b2535a7d4f5185168716f`;
3. require the raw candidate SHA-256 to equal `69abc885…`;
4. require 83 unique invariant IDs, 50 unique families, no duplicate ID, and
   exactly one row each for K-CONSENT-1 and K-UNTYPED-1;
5. require every `ContractSourceSHA256` cell to equal `842bf170…`, every
   `AppDecompositionBasis` cell to name `932b890e…`, and every source anchor
   to resolve to its exact invariant ID in the reconstructed candidate;
6. require K-CONTROL-1 to remain design-mapped under external Root authority
   with `CoverageStatus = MAPPED_WITH_OPEN_ISSUE` and
   `OpenIssueIDs = RUNTIME-OPEN-005;DEL-02-07;WP-03` unless a later exact
   owner-approved candidate supersedes these bytes; and
7. apply the full file atomically; never mix rows from this candidate with the
   live pre-image or superseded Phase-2 candidate.

## Rebuild inventory

All 83 Phase-2 rows are rebound from `a7928297…` to the Phase-2b resolved
contract `842bf170…`. The 83-ID/50-family set, exact +2/+2 delta, source
anchors, approved decomposition candidate pin, consequential enforcement
relationships, and N3-RF-001 DEL-03-04 repair are preserved.

For the 82 non-K-CONTROL-1 rows, the only byte-level field change from the
Phase-2 candidate is `ContractSourceSHA256`. K-CONTROL-1 changes exactly six
fields:

1. `ContractSourceSHA256` rebinds to `842bf170…`;
2. `OwnerAuthorityRef` cites ratified Root `docs/CONTRACT.md` line 162 at
   `ad0a4e6a…` plus A4-B, A5-B, and A6-A;
3. `EnforcementSurfaces` distinguishes live single-socket checks from
   design-gated supervisor-socket and two-listener checks;
4. `OpenIssueIDs` becomes `RUNTIME-OPEN-005;DEL-02-07;WP-03`;
5. `CoverageStatus` becomes `MAPPED_WITH_OPEN_ISSUE`; and
6. `RationaleEvidenceAnchor` binds the ratified Root row and regenerated C-01
   transaction.

The K-CONTROL-1 authority fields remain:

| Field | Exact value |
| --- | --- |
| `SemanticOwnerProduct` | `ROOT` |
| `OwnerAuthorityBasis` | `ROOT_RULED_CONTINUING_STEWARDSHIP` |
| `AppObligationClass` | `APP_CLIENT_CONFORMANCE` |
| `ProvenanceStatus` | `EXTERNAL_ROOT_AUTHORITY` |
| `CoverageStatus` | `MAPPED_WITH_OPEN_ISSUE` |
| `OpenIssueIDs` | `RUNTIME-OPEN-005;DEL-02-07;WP-03` |

This is design mapping, not implementation coverage. No row asserts a live
supervisor socket, a two-listener runtime, Gate-5 application, or completion
of DEL-02-07/WP-03.

## Deterministic validation

| Check | Result |
| --- | --- |
| CSV parse | `PASS` — 18 columns, 83 data rows |
| Unique invariant IDs / families | `PASS` — `83 / 50` |
| Live pre-image accounting | `PASS` — `81 / 48` |
| Exact delta | `PASS` — only K-CONSENT-1/K-CONSENT and K-UNTYPED-1/K-UNTYPED, `+2 / +2` |
| Contract-source identity | `PASS` — all 83 rows equal `842bf170…` |
| Decomposition basis | `PASS` — all 83 rows equal `932b890e…` |
| Source-anchor ID resolution | `PASS` — 83/83 against the 214-line reconstructed candidate |
| Contract/register ID parity | `PASS` — exact 83-ID set equality |
| Phase-2 semantic preservation | `PASS` — 82 rows change only the global contract pin; K-CONTROL-1 changes only the six declared fields |
| DEL-03-04 repair retention | `PASS` — K-EVENT-3 retains DEL-03-04 in both carrier cells |
| K-CONTROL-1 Root ownership/provenance | `PASS` — ROOT / EXTERNAL_ROOT_AUTHORITY |
| K-CONTROL-1 design-only calibration | `PASS` — one live socket; second-socket/two-listener checks design-gated |
| Duplicate IDs | `PASS` — none |

## Validation boundary

The raw CSV candidate was written before this hash-pinning transaction.
Candidate whitespace then passed against exact basis
`ef92fab10f40aa95da484701982d83fa1abca874` before its SHA-256 and byte count
were pinned here.

## Candidate handoff

| State | Value |
| --- | --- |
| `CandidateState` | `COMPLETE_AWAITING_OWNER_APPROVAL` |
| `AuthorityState` | `NO_NEW_AUTHORITY` |
| `TruthState` | `AUTHORITATIVE_SURFACES_UNCHANGED` |
| `NextGateState` | `N4_FRESH_INDEPENDENT_REVIEW_REQUIRED` |

`ReadyForNextPhase = NO`.
