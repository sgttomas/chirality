# DOUBLE_BLIND_COMPARISON — DEL-06-02 (F-06-02A vs F-06-02B)

> Script-derived by `R2/PKG-06/_scripts/double_blind.py` (R0 script adapted by path only). Agent measurement, not a ruling.

- A ledger: `DEL-06-02_A/DEL-06-02_claims.csv` sha256 `006bf3c885d30fee9ee8897a08bf608a50298956d0abae7f33aae8f0664a3a26`; rows 57; base keys 41
- B ledger: `DEL-06-02_B/DEL-06-02_claims.csv` sha256 `d1e1be6b220effd8bcbaa539872f3f4987b46100450a117a43a45d9cee55b186`; rows 56; base keys 43
- Base keys in both: 35; only A: []; only B: ['DEL-06-02#STATE-3', 'DEL-06-02#STATE-4']

- Indexed base keys compared: 35. Run-local keys (REGISTER-n/STATE-n) are numbered independently by each worker, so they are excluded from agreement and listed in §6.
Comparison unit: the base key (`.n` split suffix removed). Two readings agree on a field when the *set* of values across that base key's rows is identical; a secondary 'overlap' measure counts keys whose value sets intersect.

## 1. Field agreement on base keys

| Field | Exact agreement | Overlap agreement | Keys compared |
|---|---|---|---|
| ClaimType | 30/35 (86%) | 33/35 (94%) | 35 |
| Disposition | 19/35 (54%) | 23/35 (66%) | 35 |
| AuthorityTier | 28/35 (80%) | 31/35 (89%) | 35 |
| CauseTag | 27/35 (77%) | 30/35 (86%) | 35 |
| Confidence (secondary) | 25/35 | – | 35 |

## 2. Split rate

- A: 5/41 base keys split (12.2%); rows/base key 1.39
- B: 2/43 base keys split (4.7%); rows/base key 1.30
- Split-rate difference: 7.5 percentage points
- Keys split by both: 2; only A: ['DEL-06-02#CLM-004', 'DEL-06-02#CLM-015', 'DEL-06-02#CLM-021']; only B: []

## 3. Histograms

**Disposition** (rows) — A: {'ALIGNED': 2, 'AUTHORITY_CONFLICT': 3, 'DOCUMENTED_UNIMPLEMENTED': 1, 'IMPLEMENTED_DIFFERENTLY': 18, 'NOT_AUDITABLE': 8, 'PARTIALLY_IMPLEMENTED': 5, 'REMAINING_STATE_MISMATCH': 2, 'STALE_SPECIFICATION': 18}; B: {'ALIGNED': 3, 'AUTHORITY_CONFLICT': 4, 'IMPLEMENTED_DIFFERENTLY': 16, 'NOT_AUDITABLE': 7, 'PARTIALLY_IMPLEMENTED': 8, 'REMAINING_STATE_MISMATCH': 6, 'STALE_SPECIFICATION': 12}

**CauseTag** (rows) — A: {'CODEX_SOLE_ENGINE': 25, 'DOC_HYGIENE': 13, 'NONE': 10, 'PRE_V3_DRIFT': 7, 'RUNTIME_EXTRACTION': 2}; B: {'CODEX_SOLE_ENGINE': 29, 'DOC_HYGIENE': 11, 'NONE': 10, 'PRE_V3_DRIFT': 5, 'RUNTIME_EXTRACTION': 1}

**ClaimType** (rows) — A: {'ACCEPTANCE': 7, 'CONTEXT_CLAIM': 11, 'REGISTER_DEFECT': 4, 'REQUIREMENT': 22, 'STATE_ASSERTION': 13}; B: {'ACCEPTANCE': 7, 'CONTEXT_CLAIM': 9, 'REGISTER_DEFECT': 4, 'REQUIREMENT': 22, 'STATE_ASSERTION': 14}

**AuthorityTier** (rows) — A: {'GOVERNANCE_INVARIANT': 19, 'LOCAL_DESIGN': 12, 'NOT_APPLICABLE': 22, 'PRD': 4}; B: {'GOVERNANCE_INVARIANT': 17, 'LOCAL_DESIGN': 16, 'NOT_APPLICABLE': 19, 'PRD': 4}

**Confidence** (rows) — A: {'HIGH': 26, 'LOW': 1, 'MEDIUM': 30}; B: {'HIGH': 19, 'LOW': 1, 'MEDIUM': 36}

## 4. Reverse Response agreement

- A sha256 `1ade808ec20af9672af926c5f1b39d35d6a1f0e1b6f5a4efd0a5f88da679a9e7`; B sha256 `6dc63f0f0c67964ffcfc483fc17e293bf2366286c56ca3fa4c8c5a6f7eb6bc27`
- Capabilities answered by both: 326
- Exact Response agreement: 323/326 (99%)
- Coarse agreement (mine vs NOT_MINE): 323/326 (99%)
- Same claiming base key where both CLAIMED_BY/PARTIAL agree: 10/12
- Response histogram A: {'NOT_MINE': 314, 'CLAIMED_BY': 3, 'PARTIAL': 9}; B: {'NOT_MINE': 311, 'CLAIMED_BY': 3, 'PARTIAL': 12}

## 5. Every disagreement, both readings

### 5.1 Forward fields

| Base key | Field | A reading | B reading |
|---|---|---|---|
| DEL-06-02#CLM-001 | Disposition | STALE_SPECIFICATION | REMAINING_STATE_MISMATCH |
| DEL-06-02#CLM-004 | ClaimType | REQUIREMENT / STATE_ASSERTION | REQUIREMENT |
| DEL-06-02#CLM-004 | Disposition | IMPLEMENTED_DIFFERENTLY / STALE_SPECIFICATION | IMPLEMENTED_DIFFERENTLY |
| DEL-06-02#CLM-004 | AuthorityTier | GOVERNANCE_INVARIANT / NOT_APPLICABLE | GOVERNANCE_INVARIANT |
| DEL-06-02#CLM-004 | CauseTag | CODEX_SOLE_ENGINE / DOC_HYGIENE | CODEX_SOLE_ENGINE |
| DEL-06-02#CLM-005 | Disposition | STALE_SPECIFICATION | IMPLEMENTED_DIFFERENTLY |
| DEL-06-02#CLM-005 | CauseTag | PRE_V3_DRIFT | CODEX_SOLE_ENGINE |
| DEL-06-02#CLM-006 | AuthorityTier | GOVERNANCE_INVARIANT | LOCAL_DESIGN |
| DEL-06-02#CLM-008 | Disposition | STALE_SPECIFICATION | REMAINING_STATE_MISMATCH |
| DEL-06-02#CLM-010 | Disposition | AUTHORITY_CONFLICT / DOCUMENTED_UNIMPLEMENTED / IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED | AUTHORITY_CONFLICT / IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED |
| DEL-06-02#CLM-011 | Disposition | STALE_SPECIFICATION | NOT_AUDITABLE |
| DEL-06-02#CLM-011 | CauseTag | DOC_HYGIENE | NONE |
| DEL-06-02#CLM-013 | AuthorityTier | GOVERNANCE_INVARIANT | LOCAL_DESIGN |
| DEL-06-02#CLM-014 | ClaimType | REQUIREMENT | STATE_ASSERTION |
| DEL-06-02#CLM-015 | ClaimType | ACCEPTANCE / CONTEXT_CLAIM | ACCEPTANCE |
| DEL-06-02#CLM-015 | Disposition | IMPLEMENTED_DIFFERENTLY / NOT_AUDITABLE | IMPLEMENTED_DIFFERENTLY |
| DEL-06-02#CLM-015 | AuthorityTier | GOVERNANCE_INVARIANT / NOT_APPLICABLE | GOVERNANCE_INVARIANT |
| DEL-06-02#CLM-015 | CauseTag | CODEX_SOLE_ENGINE / NONE | CODEX_SOLE_ENGINE |
| DEL-06-02#CLM-016 | Disposition | STALE_SPECIFICATION | REMAINING_STATE_MISMATCH |
| DEL-06-02#CLM-019 | Disposition | IMPLEMENTED_DIFFERENTLY | PARTIALLY_IMPLEMENTED |
| DEL-06-02#CLM-020 | Disposition | PARTIALLY_IMPLEMENTED | IMPLEMENTED_DIFFERENTLY |
| DEL-06-02#CLM-020 | AuthorityTier | LOCAL_DESIGN | GOVERNANCE_INVARIANT |
| DEL-06-02#CLM-021 | ClaimType | ACCEPTANCE / STATE_ASSERTION | ACCEPTANCE |
| DEL-06-02#CLM-021 | Disposition | PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-06-02#CLM-021 | AuthorityTier | GOVERNANCE_INVARIANT / LOCAL_DESIGN | LOCAL_DESIGN |
| DEL-06-02#CLM-021 | CauseTag | CODEX_SOLE_ENGINE / PRE_V3_DRIFT | CODEX_SOLE_ENGINE |
| DEL-06-02#CLM-022 | Disposition | STALE_SPECIFICATION | REMAINING_STATE_MISMATCH |
| DEL-06-02#CLM-026 | Disposition | STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-06-02#CLM-029 | Disposition | STALE_SPECIFICATION | REMAINING_STATE_MISMATCH |
| DEL-06-02#CLM-031 | ClaimType | CONTEXT_CLAIM | REQUIREMENT |
| DEL-06-02#CLM-031 | Disposition | NOT_AUDITABLE | IMPLEMENTED_DIFFERENTLY |
| DEL-06-02#CLM-031 | AuthorityTier | NOT_APPLICABLE | LOCAL_DESIGN |
| DEL-06-02#CLM-031 | CauseTag | NONE | CODEX_SOLE_ENGINE |
| DEL-06-02#CLM-032 | Disposition | IMPLEMENTED_DIFFERENTLY | STALE_SPECIFICATION |
| DEL-06-02#CLM-032 | CauseTag | CODEX_SOLE_ENGINE | PRE_V3_DRIFT |
| DEL-06-02#CLM-033 | CauseTag | DOC_HYGIENE | CODEX_SOLE_ENGINE |

### 5.2 Reverse responses

| CapabilityID | A | B |
|---|---|---|
| CAP-BUILD-036 | CLAIMED_BY DEL-06-02#STATE-1 | CLAIMED_BY DEL-06-02#STATE-4 |
| CAP-HARNESS-019 | NOT_MINE  | PARTIAL DEL-06-02#CLM-010.1 |
| CAP-RTCONTRACT-043 | PARTIAL DEL-06-02#STATE-1 | PARTIAL DEL-06-02#STATE-4 |
| CAP-RTCORE-039 | NOT_MINE  | PARTIAL DEL-06-02#CLM-010.4 |
| CAP-RTCORE-041 | NOT_MINE  | PARTIAL DEL-06-02#CLM-010.12 |

## 6. Run-local rows (not key-comparable)

| Worker | Key | ClaimType | Disposition | CauseTag | DeclaredState (first 90 chars) |
|---|---|---|---|---|---|
| A | DEL-06-02#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | CONTRACT, SPEC and PRD ExpectedSHA256 = ActualSHA256, Status MATCH |
| A | DEL-06-02#REGISTER-2 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | Declared Upstream/Downstream 'TBD - no accepted dependency edges extracted'; register cite |
| A | DEL-06-02#REGISTER-3 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | Last Updated 2026-07-12 |
| A | DEL-06-02#REGISTER-4 | REGISTER_DEFECT | STALE_SPECIFICATION | CODEX_SOLE_ENGINE | Claude Agent SDK / Anthropic remains the first concrete/current path; verify daemon read-t |
| A | DEL-06-02#STATE-1 | STATE_ASSERTION | IMPLEMENTED_DIFFERENTLY | PRE_V3_DRIFT | frontend/scripts/generate-tool-catalog.mjs mapped to DEL-06-02 for the deterministic gener |
| A | DEL-06-02#STATE-2 | STATE_ASSERTION | IMPLEMENTED_DIFFERENTLY | RUNTIME_EXTRACTION | SOW-064 supported through App/project tool catalog, requested-tool validation and name-col |
| B | DEL-06-02#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | CONTRACT fa8fc9dc..., SPEC 01e1c75c..., PRD 8649ccba... recorded as MATCH |
| B | DEL-06-02#REGISTER-2 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | TBD - no accepted dependency edges have been extracted yet |
| B | DEL-06-02#REGISTER-3 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | DEP-06-02-011 (PRD constraint) SATISFIED because REF-006 is MATCH |
| B | DEL-06-02#REGISTER-4 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | Last Updated 2026-07-12 |
| B | DEL-06-02#STATE-1 | STATE_ASSERTION | STALE_SPECIFICATION | CODEX_SOLE_ENGINE | Claude Agent SDK / Anthropic remains the first concrete/current path; verify daemon read-t |
| B | DEL-06-02#STATE-2 | STATE_ASSERTION | PARTIALLY_IMPLEMENTED | CODEX_SOLE_ENGINE | SOW-064 supported through App/project tool catalog, requested-tool validation and name-col |
| B | DEL-06-02#STATE-3 | STATE_ASSERTION | STALE_SPECIFICATION | CODEX_SOLE_ENGINE | Runtime fingerprint is the accepted boot artifact for registry, policy, SDK and MCP versio |
| B | DEL-06-02#STATE-4 | STATE_ASSERTION | ALIGNED | NONE | frontend/scripts/generate-tool-catalog.mjs mapped to DEL-06-02 for the deterministic gener |

## 7. Row-level agreement where both split a key identically

- ClaimType: 15/15 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- Disposition: 10/15 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- AuthorityTier: 15/15 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- CauseTag: 15/15 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)

## 8. Strict agreement on keys neither worker split

Keys unsplit by both: 30.

| Field | Agreement |
|---|---|
| ClaimType | 28/30 (93%) |
| Disposition | 18/30 (60%) |
| AuthorityTier | 26/30 (87%) |
| CauseTag | 25/30 (83%) |
| ALIGNED vs non-ALIGNED | 30/30 |
