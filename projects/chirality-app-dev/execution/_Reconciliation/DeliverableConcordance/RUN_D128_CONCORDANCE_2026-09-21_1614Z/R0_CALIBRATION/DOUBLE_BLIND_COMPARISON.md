# DOUBLE_BLIND_COMPARISON — DEL-03-01 (F-03A vs F-03B)

> Script-derived by `R0_CALIBRATION/_scripts/double_blind.py`. Agent measurement, not a ruling.

- A ledger: `DEL-03-01_A/DEL-03-01_claims.csv` sha256 `1c922fa150d1e8246028ee47f1b321cfc2492e20778bd10045a6c969109848ec`; rows 60; base keys 34
- B ledger: `DEL-03-01_B/DEL-03-01_claims.csv` sha256 `90dd4ce1bfb3e9a622d184b7ba4057699e3a39793ea2a1ee443e263722c0478d`; rows 65; base keys 36
- Base keys in both: 28; only A: []; only B: ['DEL-03-01#STATE-2', 'DEL-03-01#STATE-3']

- Indexed base keys compared: 28. Run-local keys (REGISTER-n/STATE-n) are numbered independently by each worker, so they are excluded from agreement and listed in §6.
Comparison unit: the base key (`.n` split suffix removed). Two readings agree on a field when the *set* of values across that base key's rows is identical; a secondary 'overlap' measure counts keys whose value sets intersect.

## 1. Field agreement on base keys

| Field | Exact agreement | Overlap agreement | Keys compared |
|---|---|---|---|
| ClaimType | 22/28 (79%) | 23/28 (82%) | 28 |
| Disposition | 23/28 (82%) | 27/28 (96%) | 28 |
| AuthorityTier | 18/28 (64%) | 22/28 (79%) | 28 |
| CauseTag | 18/28 (64%) | 24/28 (86%) | 28 |
| Confidence (secondary) | 22/28 | – | 28 |

## 2. Split rate

- A: 6/34 base keys split (17.6%); rows/base key 1.76
- B: 9/36 base keys split (25.0%); rows/base key 1.81
- Split-rate difference: 7.4 percentage points
- Keys split by both: 6; only A: []; only B: ['DEL-03-01#CLM-018', 'DEL-03-01#CLM-019', 'DEL-03-01#CLM-022']

## 3. Histograms

**Disposition** (rows) — A: {'ALIGNED': 14, 'DOCUMENTED_UNIMPLEMENTED': 2, 'IMPLEMENTED_DIFFERENTLY': 1, 'NOT_AUDITABLE': 7, 'PARTIALLY_IMPLEMENTED': 11, 'REMAINING_STATE_MISMATCH': 1, 'STALE_SPECIFICATION': 24}; B: {'ALIGNED': 14, 'AUTHORITY_CONFLICT': 6, 'IMPLEMENTED_DIFFERENTLY': 1, 'NOT_AUDITABLE': 8, 'PARTIALLY_IMPLEMENTED': 10, 'REMAINING_STATE_MISMATCH': 1, 'STALE_SPECIFICATION': 25}

**CauseTag** (rows) — A: {'A2_TOPOLOGY': 5, 'CARRIER_PROPAGATION': 2, 'CODEX_SOLE_ENGINE': 12, 'DOC_HYGIENE': 10, 'FACADE_DEPRECATION': 1, 'NONE': 21, 'PRE_V3_DRIFT': 5, 'RUNTIME_EXTRACTION': 3, 'UNRECORDED_JUDGMENT': 1}; B: {'CARRIER_PROPAGATION': 2, 'CODEX_SOLE_ENGINE': 26, 'DOC_HYGIENE': 9, 'FACADE_DEPRECATION': 2, 'NONE': 22, 'PRE_V3_DRIFT': 1, 'RUNTIME_EXTRACTION': 2, 'UNRECORDED_JUDGMENT': 1}

**ClaimType** (rows) — A: {'ACCEPTANCE': 4, 'CONTEXT_CLAIM': 12, 'REGISTER_DEFECT': 5, 'REMAINING_WORK': 2, 'REQUIREMENT': 30, 'STATE_ASSERTION': 7}; B: {'ACCEPTANCE': 2, 'CONTEXT_CLAIM': 16, 'EXCLUSION': 1, 'REGISTER_DEFECT': 5, 'REMAINING_WORK': 2, 'REQUIREMENT': 30, 'STATE_ASSERTION': 9}

**AuthorityTier** (rows) — A: {'GOVERNANCE_INVARIANT': 27, 'LOCAL_DESIGN': 19, 'NOT_APPLICABLE': 12, 'PRD': 2}; B: {'GOVERNANCE_INVARIANT': 13, 'LOCAL_DESIGN': 7, 'NOT_APPLICABLE': 30, 'PRD': 15}

**Confidence** (rows) — A: {'HIGH': 25, 'LOW': 2, 'MEDIUM': 33}; B: {'HIGH': 20, 'LOW': 3, 'MEDIUM': 42}

## 4. Reverse Response agreement

- A sha256 `ede7666f719b748b3a162baaf59382334ba10b1908e3028f6a7d254840a5f46f`; B sha256 `0a5997d1bc50f341f8591a842ec9065d8652192e4ab1c5945513ae5498082e8f`
- Capabilities answered by both: 60
- Exact Response agreement: 52/60 (87%)
- Coarse agreement (mine vs NOT_MINE): 52/60 (87%)
- Same claiming base key where both CLAIMED_BY/PARTIAL agree: 2/2
- Response histogram A: {'NOT_MINE': 57, 'PARTIAL': 2, 'CLAIMED_BY': 1}; B: {'NOT_MINE': 51, 'PARTIAL': 8, 'CLAIMED_BY': 1}

## 5. Every disagreement, both readings

### 5.1 Forward fields

| Base key | Field | A reading | B reading |
|---|---|---|---|
| DEL-03-01#CLM-003 | AuthorityTier | GOVERNANCE_INVARIANT | GOVERNANCE_INVARIANT / PRD |
| DEL-03-01#CLM-003 | CauseTag | A2_TOPOLOGY / CODEX_SOLE_ENGINE / NONE / PRE_V3_DRIFT | CODEX_SOLE_ENGINE / NONE / PRE_V3_DRIFT |
| DEL-03-01#CLM-004 | Disposition | ALIGNED / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | ALIGNED / AUTHORITY_CONFLICT / STALE_SPECIFICATION |
| DEL-03-01#CLM-004 | AuthorityTier | GOVERNANCE_INVARIANT / LOCAL_DESIGN / PRD | GOVERNANCE_INVARIANT / NOT_APPLICABLE / PRD |
| DEL-03-01#CLM-004 | CauseTag | A2_TOPOLOGY / DOC_HYGIENE / NONE / PRE_V3_DRIFT | CODEX_SOLE_ENGINE / DOC_HYGIENE / NONE |
| DEL-03-01#CLM-005 | AuthorityTier | GOVERNANCE_INVARIANT / LOCAL_DESIGN | NOT_APPLICABLE / PRD |
| DEL-03-01#CLM-008 | ClaimType | REQUIREMENT | EXCLUSION |
| DEL-03-01#CLM-009 | Disposition | ALIGNED / DOCUMENTED_UNIMPLEMENTED / IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | ALIGNED / AUTHORITY_CONFLICT / IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION |
| DEL-03-01#CLM-009 | CauseTag | A2_TOPOLOGY / CODEX_SOLE_ENGINE / DOC_HYGIENE / NONE / PRE_V3_DRIFT / UNRECORDED_JUDGMENT | CODEX_SOLE_ENGINE / DOC_HYGIENE / NONE / UNRECORDED_JUDGMENT |
| DEL-03-01#CLM-011 | ClaimType | ACCEPTANCE | REQUIREMENT |
| DEL-03-01#CLM-012 | AuthorityTier | LOCAL_DESIGN | LOCAL_DESIGN / NOT_APPLICABLE |
| DEL-03-01#CLM-012 | CauseTag | CARRIER_PROPAGATION / CODEX_SOLE_ENGINE | CODEX_SOLE_ENGINE |
| DEL-03-01#CLM-013 | AuthorityTier | GOVERNANCE_INVARIANT / LOCAL_DESIGN | GOVERNANCE_INVARIANT / NOT_APPLICABLE |
| DEL-03-01#CLM-016 | AuthorityTier | LOCAL_DESIGN | NOT_APPLICABLE |
| DEL-03-01#CLM-016 | CauseTag | DOC_HYGIENE | CODEX_SOLE_ENGINE |
| DEL-03-01#CLM-017 | ClaimType | REQUIREMENT | CONTEXT_CLAIM |
| DEL-03-01#CLM-017 | AuthorityTier | LOCAL_DESIGN | NOT_APPLICABLE |
| DEL-03-01#CLM-017 | CauseTag | RUNTIME_EXTRACTION | CODEX_SOLE_ENGINE |
| DEL-03-01#CLM-018 | ClaimType | ACCEPTANCE | REQUIREMENT |
| DEL-03-01#CLM-018 | Disposition | PARTIALLY_IMPLEMENTED | ALIGNED / AUTHORITY_CONFLICT / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION |
| DEL-03-01#CLM-018 | AuthorityTier | LOCAL_DESIGN | GOVERNANCE_INVARIANT / PRD |
| DEL-03-01#CLM-018 | CauseTag | CODEX_SOLE_ENGINE | CODEX_SOLE_ENGINE / NONE |
| DEL-03-01#CLM-019 | ClaimType | ACCEPTANCE | ACCEPTANCE / REQUIREMENT |
| DEL-03-01#CLM-021 | AuthorityTier | GOVERNANCE_INVARIANT | NOT_APPLICABLE |
| DEL-03-01#CLM-022 | ClaimType | REQUIREMENT | CONTEXT_CLAIM |
| DEL-03-01#CLM-022 | Disposition | PARTIALLY_IMPLEMENTED | ALIGNED / AUTHORITY_CONFLICT / PARTIALLY_IMPLEMENTED |
| DEL-03-01#CLM-022 | AuthorityTier | GOVERNANCE_INVARIANT | NOT_APPLICABLE |
| DEL-03-01#CLM-022 | CauseTag | CODEX_SOLE_ENGINE | CODEX_SOLE_ENGINE / NONE |
| DEL-03-01#CLM-025 | Disposition | STALE_SPECIFICATION | NOT_AUDITABLE |
| DEL-03-01#CLM-025 | CauseTag | A2_TOPOLOGY | NONE |
| DEL-03-01#REM-2 | CauseTag | A2_TOPOLOGY | CARRIER_PROPAGATION |

### 5.2 Reverse responses

| CapabilityID | A | B |
|---|---|---|
| CAP-HARNESS-002 | NOT_MINE  | PARTIAL DEL-03-01#CLM-004.2 |
| CAP-HARNESS-027 | NOT_MINE  | PARTIAL DEL-03-01#CLM-018.1 |
| CAP-HARNESS-028 | NOT_MINE  | PARTIAL DEL-03-01#CLM-009.8 |
| CAP-HARNESS-031 | NOT_MINE  | PARTIAL DEL-03-01#CLM-005.1 |
| CAP-HARNESS-032 | NOT_MINE  | PARTIAL DEL-03-01#CLM-009.10 |
| CAP-HARNESS-034 | NOT_MINE  | PARTIAL DEL-03-01#CLM-009.10 |
| CAP-HARNESS-039 | NOT_MINE  | PARTIAL DEL-03-01#CLM-009.11 |
| CAP-HARNESS-059 | PARTIAL DEL-03-01#CLM-019 | NOT_MINE  |

## 6. Run-local rows (not key-comparable)

| Worker | Key | ClaimType | Disposition | CauseTag | DeclaredState (first 90 chars) |
|---|---|---|---|---|---|
| A | DEL-03-01#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | Table lists DEP-03-01-006 ACTIVE/PENDING; P45 block says ACTIVE 7, PENDING 4; Lifecycle su |
| A | DEL-03-01#REGISTER-2 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | Evidence files Datasheet.md, Specification.md, Procedure.md, Guidance.md |
| A | DEL-03-01#REGISTER-3 | REGISTER_DEFECT | STALE_SPECIFICATION | CODEX_SOLE_ENGINE | Active prerequisite on Claude SDK probe |
| A | DEL-03-01#REGISTER-4 | REGISTER_DEFECT | STALE_SPECIFICATION | CARRIER_PROPAGATION | Gate interface is Root API v2 and event schema v2 |
| A | DEL-03-01#REGISTER-5 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | All refs MATCH |
| A | DEL-03-01#STATE-1 | STATE_ASSERTION | STALE_SPECIFICATION | DOC_HYGIENE | blocked-on: D-APP-47, D-APP-48, D-T0-09, D-30 |
| B | DEL-03-01#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | _DEPENDENCIES.md: Declared Upstream/Downstream TBD; table lists DEP-03-01-006 ACTIVE PENDI |
| B | DEL-03-01#REGISTER-2 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | Rows 001-008 cite Datasheet.md, Specification.md, Procedure.md, Guidance.md |
| B | DEL-03-01#REGISTER-3 | REGISTER_DEFECT | STALE_SPECIFICATION | CARRIER_PROPAGATION | DEP-009 targets Root-owned runtime contracts API v2 and event schema v2 (PENDING); V3-01 c |
| B | DEL-03-01#REGISTER-4 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | REF-002, REF-003, REF-006 Status MATCH |
| B | DEL-03-01#REGISTER-5 | REGISTER_DEFECT | STALE_SPECIFICATION | CODEX_SOLE_ENGINE | DEP-003 PENDING on DEL-04-01 SDK probe; DEP-008 PENDING Section 9 linkage |
| B | DEL-03-01#STATE-1 | STATE_ASSERTION | STALE_SPECIFICATION | CODEX_SOLE_ENGINE | SDK-backed live query conformance has D-APP-17 proof and D-APP-18 key-aware default; resid |
| B | DEL-03-01#STATE-2 | STATE_ASSERTION | STALE_SPECIFICATION | DOC_HYGIENE | blocked-on: D-APP-47, D-APP-48, D-T0-09, D-30 |
| B | DEL-03-01#STATE-3 | STATE_ASSERTION | STALE_SPECIFICATION | FACADE_DEPRECATION | Doc names frontend/packages/harness-contract/src/agent-engine-port.ts as the product bound |

## 7. Row-level agreement where both split a key identically

- ClaimType: 23/23 sub-rows agree across 4 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- Disposition: 17/23 sub-rows agree across 4 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- AuthorityTier: 11/23 sub-rows agree across 4 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- CauseTag: 16/23 sub-rows agree across 4 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)

## 8. Strict agreement on keys neither worker split

Keys unsplit by both: 19.

| Field | Agreement |
|---|---|
| ClaimType | 16/19 (84%) |
| Disposition | 18/19 (95%) |
| AuthorityTier | 16/19 (84%) |
| CauseTag | 15/19 (79%) |
| ALIGNED vs non-ALIGNED | 19/19 |
