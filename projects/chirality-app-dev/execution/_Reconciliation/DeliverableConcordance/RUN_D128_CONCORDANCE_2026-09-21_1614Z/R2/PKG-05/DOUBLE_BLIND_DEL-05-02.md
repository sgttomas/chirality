# DOUBLE_BLIND_COMPARISON — DEL-05-02 (F-05-02A vs F-05-02B)

> Script-derived by `R2/PKG-05/_scripts/double_blind.py` (R0 script adapted by path only). Agent measurement, not a ruling.

- A ledger: `DEL-05-02_A/DEL-05-02_claims.csv` sha256 `9f8a6a1f3b512e05bd38b657bd95a6c8546b606178f681bbdb8556208a759a99`; rows 51; base keys 37
- B ledger: `DEL-05-02_B/DEL-05-02_claims.csv` sha256 `801c5e9cab8575fc130b01ca3139637c9036e6ab2205cfc9292c2f7fd8c8ccd5`; rows 52; base keys 38
- Base keys in both: 33; only A: []; only B: ['DEL-05-02#REGISTER-4']

- Indexed base keys compared: 33. Run-local keys (REGISTER-n/STATE-n) are numbered independently by each worker, so they are excluded from agreement and listed in §6.
Comparison unit: the base key (`.n` split suffix removed). Two readings agree on a field when the *set* of values across that base key's rows is identical; a secondary 'overlap' measure counts keys whose value sets intersect.

## 1. Field agreement on base keys

| Field | Exact agreement | Overlap agreement | Keys compared |
|---|---|---|---|
| ClaimType | 31/33 (94%) | 31/33 (94%) | 33 |
| Disposition | 24/33 (73%) | 25/33 (76%) | 33 |
| AuthorityTier | 29/33 (88%) | 29/33 (88%) | 33 |
| CauseTag | 22/33 (67%) | 23/33 (70%) | 33 |
| Confidence (secondary) | 23/33 | – | 33 |

## 2. Split rate

- A: 1/37 base keys split (2.7%); rows/base key 1.38
- B: 1/38 base keys split (2.6%); rows/base key 1.37
- Split-rate difference: 0.1 percentage points
- Keys split by both: 1; only A: []; only B: []

## 3. Histograms

**Disposition** (rows) — A: {'ACCEPTED_DIVERGENCE': 3, 'ALIGNED': 11, 'DOCUMENTED_UNIMPLEMENTED': 1, 'IMPLEMENTED_DIFFERENTLY': 1, 'NOT_AUDITABLE': 1, 'PARTIALLY_IMPLEMENTED': 5, 'REMAINING_STATE_MISMATCH': 4, 'STALE_SPECIFICATION': 25}; B: {'ALIGNED': 11, 'DOCUMENTED_UNIMPLEMENTED': 2, 'IMPLEMENTED_DIFFERENTLY': 1, 'NOT_AUDITABLE': 1, 'PARTIALLY_IMPLEMENTED': 7, 'REMAINING_STATE_MISMATCH': 2, 'STALE_SPECIFICATION': 28}

**CauseTag** (rows) — A: {'A2_TOPOLOGY': 3, 'CARRIER_PROPAGATION': 3, 'CODEX_SOLE_ENGINE': 4, 'DOC_HYGIENE': 16, 'FACADE_DEPRECATION': 1, 'NONE': 12, 'PRE_V3_DRIFT': 1, 'RUNTIME_EXTRACTION': 11}; B: {'A2_TOPOLOGY': 4, 'CARRIER_PROPAGATION': 8, 'CODEX_SOLE_ENGINE': 1, 'DOC_HYGIENE': 13, 'FACADE_DEPRECATION': 1, 'LIFECYCLE_GATE_PENDING': 1, 'NONE': 12, 'RUNTIME_EXTRACTION': 12}

**ClaimType** (rows) — A: {'ACCEPTANCE': 4, 'CONTEXT_CLAIM': 8, 'REGISTER_DEFECT': 3, 'REMAINING_WORK': 2, 'REQUIREMENT': 26, 'STATE_ASSERTION': 8}; B: {'ACCEPTANCE': 5, 'CONTEXT_CLAIM': 9, 'REGISTER_DEFECT': 4, 'REMAINING_WORK': 2, 'REQUIREMENT': 25, 'STATE_ASSERTION': 7}

**AuthorityTier** (rows) — A: {'GOVERNANCE_INVARIANT': 27, 'LOCAL_DESIGN': 6, 'NOT_APPLICABLE': 18}; B: {'GOVERNANCE_INVARIANT': 23, 'LOCAL_DESIGN': 13, 'NOT_APPLICABLE': 16}

**Confidence** (rows) — A: {'HIGH': 23, 'LOW': 1, 'MEDIUM': 27}; B: {'HIGH': 18, 'LOW': 3, 'MEDIUM': 31}

## 4. Reverse Response agreement

- A sha256 `a88ab59d28ecfaa17c6337ada46656f716baa2bbcb755f6cb1e914205ba4408d`; B sha256 `3f93fa0d75948cbdd72b45e87017431eec0c2b9b3110058d351d4eb2dae03ee0`
- Capabilities answered by both: 413
- Exact Response agreement: 404/413 (98%)
- Coarse agreement (mine vs NOT_MINE): 404/413 (98%)
- Same claiming base key where both CLAIMED_BY/PARTIAL agree: 11/12
- Response histogram A: {'NOT_MINE': 395, 'PARTIAL': 15, 'CLAIMED_BY': 3}; B: {'NOT_MINE': 398, 'CLAIMED_BY': 3, 'PARTIAL': 12}

## 5. Every disagreement, both readings

### 5.1 Forward fields

| Base key | Field | A reading | B reading |
|---|---|---|---|
| DEL-05-02#CLM-002 | CauseTag | DOC_HYGIENE | CARRIER_PROPAGATION |
| DEL-05-02#CLM-003 | CauseTag | RUNTIME_EXTRACTION | A2_TOPOLOGY |
| DEL-05-02#CLM-004 | Disposition | STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-05-02#CLM-005 | Disposition | ACCEPTED_DIVERGENCE | PARTIALLY_IMPLEMENTED |
| DEL-05-02#CLM-007 | Disposition | REMAINING_STATE_MISMATCH | STALE_SPECIFICATION |
| DEL-05-02#CLM-007 | CauseTag | DOC_HYGIENE | CARRIER_PROPAGATION |
| DEL-05-02#CLM-009 | Disposition | ACCEPTED_DIVERGENCE | STALE_SPECIFICATION |
| DEL-05-02#CLM-009 | AuthorityTier | GOVERNANCE_INVARIANT | LOCAL_DESIGN |
| DEL-05-02#CLM-010 | Disposition | ALIGNED / DOCUMENTED_UNIMPLEMENTED / IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED | ALIGNED / DOCUMENTED_UNIMPLEMENTED / IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION |
| DEL-05-02#CLM-010 | CauseTag | CODEX_SOLE_ENGINE / NONE / PRE_V3_DRIFT | A2_TOPOLOGY / CODEX_SOLE_ENGINE / NONE / RUNTIME_EXTRACTION |
| DEL-05-02#CLM-015 | Disposition | ACCEPTED_DIVERGENCE | STALE_SPECIFICATION |
| DEL-05-02#CLM-016 | ClaimType | STATE_ASSERTION | CONTEXT_CLAIM |
| DEL-05-02#CLM-017 | CauseTag | RUNTIME_EXTRACTION | A2_TOPOLOGY |
| DEL-05-02#CLM-021 | AuthorityTier | GOVERNANCE_INVARIANT | LOCAL_DESIGN |
| DEL-05-02#CLM-022 | Disposition | STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-05-02#CLM-022 | CauseTag | CODEX_SOLE_ENGINE | RUNTIME_EXTRACTION |
| DEL-05-02#CLM-025 | CauseTag | RUNTIME_EXTRACTION | A2_TOPOLOGY |
| DEL-05-02#CLM-027 | Disposition | REMAINING_STATE_MISMATCH | STALE_SPECIFICATION |
| DEL-05-02#CLM-027 | CauseTag | DOC_HYGIENE | CARRIER_PROPAGATION |
| DEL-05-02#REM-2 | Disposition | STALE_SPECIFICATION | DOCUMENTED_UNIMPLEMENTED |
| DEL-05-02#REM-2 | CauseTag | CARRIER_PROPAGATION | LIFECYCLE_GATE_PENDING |
| DEL-05-02#SEC-1 | CauseTag | A2_TOPOLOGY | CARRIER_PROPAGATION |
| DEL-05-02#SEC-2 | ClaimType | REQUIREMENT | ACCEPTANCE |
| DEL-05-02#SEC-2 | AuthorityTier | GOVERNANCE_INVARIANT | LOCAL_DESIGN |
| DEL-05-02#SEC-2 | CauseTag | A2_TOPOLOGY | CARRIER_PROPAGATION |
| DEL-05-02#SEC-3 | AuthorityTier | NOT_APPLICABLE | LOCAL_DESIGN |

### 5.2 Reverse responses

| CapabilityID | A | B |
|---|---|---|
| CAP-HARNESS-006 | PARTIAL DEL-05-02#SEC-1 | NOT_MINE  |
| CAP-HARNESS-030 | PARTIAL DEL-05-02#CLM-010.6 | NOT_MINE  |
| CAP-HARNESS-048 | PARTIAL DEL-05-02#CLM-010.10 | NOT_MINE  |
| CAP-HARNESS-057 | NOT_MINE  | PARTIAL DEL-05-02#CLM-028 |
| CAP-RTCONTRACT-025 | NOT_MINE  | PARTIAL DEL-05-02#CLM-010.13 |
| CAP-RTCORE-017 | CLAIMED_BY DEL-05-02#CLM-010.5 | CLAIMED_BY DEL-05-02#CLM-005 |
| CAP-RTCORE-018 | PARTIAL DEL-05-02#CLM-010.7 | NOT_MINE  |
| CAP-RTCORE-025 | NOT_MINE  | PARTIAL DEL-05-02#REM-1 |
| CAP-WOVEN-019 | PARTIAL DEL-05-02#CLM-010.8 | NOT_MINE  |
| CAP-WOVEN-033 | PARTIAL DEL-05-02#REM-1 | NOT_MINE  |

## 6. Run-local rows (not key-comparable)

| Worker | Key | ClaimType | Disposition | CauseTag | DeclaredState (first 90 chars) |
|---|---|---|---|---|---|
| A | DEL-05-02#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | CONTRACT, SPEC and PRD recorded with ActualSHA256 = Expected and Status MATCH |
| A | DEL-05-02#REGISTER-2 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | REF-009 and REF-010 each used twice (software-decomp resources and SCA-APP-010 Gate3/Propa |
| A | DEL-05-02#REGISTER-3 | REGISTER_DEFECT | STALE_SPECIFICATION | CARRIER_PROPAGATION | DEP-05-02-013 closed schema v2 gates v3 consumption; DEP-05-02-015 PENDING Root DEL-02-10  |
| A | DEL-05-02#STATE-1 | STATE_ASSERTION | STALE_SPECIFICATION | A2_TOPOLOGY | Consume Root-owned daemon HarnessEvent records; proposal.* once Root accepts; daemon evide |
| B | DEL-05-02#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | CONTRACT, SPEC and PRD ExpectedSHA256 = ActualSHA256, Status MATCH |
| B | DEL-05-02#REGISTER-2 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | REF-009 and REF-010 each name two different sources (software-decomp resources and SCA-APP |
| B | DEL-05-02#REGISTER-3 | REGISTER_DEFECT | STALE_SPECIFICATION | CARRIER_PROPAGATION | DEP-05-02-013 (Root closed schema v2) and DEP-05-02-015 (Root DEL-02-10 acceptance, PREREQ |
| B | DEL-05-02#REGISTER-4 | REGISTER_DEFECT | STALE_SPECIFICATION | CARRIER_PROPAGATION | Consume Root-owned daemon HarnessEvent records; proposal.* once Root accepts them; daemon  |
| B | DEL-05-02#STATE-1 | STATE_ASSERTION | STALE_SPECIFICATION | RUNTIME_EXTRACTION | OUT-001 is a provider-neutral HarnessEvent schema and append-only JSONL persistence surfac |

## 7. Row-level agreement where both split a key identically

- ClaimType: 15/15 sub-rows agree across 1 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- Disposition: 13/15 sub-rows agree across 1 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- AuthorityTier: 15/15 sub-rows agree across 1 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- CauseTag: 11/15 sub-rows agree across 1 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)

## 8. Strict agreement on keys neither worker split

Keys unsplit by both: 32.

| Field | Agreement |
|---|---|
| ClaimType | 30/32 (94%) |
| Disposition | 24/32 (75%) |
| AuthorityTier | 28/32 (88%) |
| CauseTag | 22/32 (69%) |
| ALIGNED vs non-ALIGNED | 32/32 |

## 9. Addendum 5 tie-break test (STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH)

> Script-derived by `R2/PKG-05/_scripts/tiebreak_split.py`. Same comparison unit as §1 (Disposition value set per indexed base key). PKG-06 DEL-06-02 (pre-Addendum-5 baseline) is recomputed read-only from its two sealed ledgers. Agent measurement, not a ruling.

| Measure | DEL-05-02 (wave 2, tie-break given to A and B verbatim before dispatch) | DEL-06-02 (wave 1, before the tie-break) |
|---|---|---|
| Disposition exact agreement, indexed base keys | 24/33 (73%) | 19/35 (54%) |
| Disagreements that are pure SS vs RSM splits | 2 | 5 |
| Disagreements involving SS or RSM plus another verdict | 6 | 6 |
| Other disagreements | 1 | 5 |
| Agreement on keys where either worker used SS or RSM | 20/28 (71%) | 6/17 (35%) |
| Agreement if pure SS-vs-RSM splits were counted as agreement | 26/33 (79%) | 24/35 (69%) |
| Rows STALE_SPECIFICATION (A / B) | 25 / 28 | 18 / 12 |
| Rows REMAINING_STATE_MISMATCH (A / B) | 4 / 2 | 2 / 6 |

- DEL-05-02 SS_vs_RSM: CLM-007 (A REMAINING_STATE_MISMATCH; B STALE_SPECIFICATION), CLM-027 (A REMAINING_STATE_MISMATCH; B STALE_SPECIFICATION)
- DEL-05-02 SS_or_RSM_other: CLM-004 (A STALE_SPECIFICATION; B PARTIALLY_IMPLEMENTED), CLM-009 (A ACCEPTED_DIVERGENCE; B STALE_SPECIFICATION), CLM-010 (A ALIGNED/DOCUMENTED_UNIMPLEMENTED/IMPLEMENTED_DIFFERENTLY/PARTIALLY_IMPLEMENTED; B ALIGNED/DOCUMENTED_UNIMPLEMENTED/IMPLEMENTED_DIFFERENTLY/PARTIALLY_IMPLEMENTED/STALE_SPECIFICATION), CLM-015 (A ACCEPTED_DIVERGENCE; B STALE_SPECIFICATION), CLM-022 (A STALE_SPECIFICATION; B PARTIALLY_IMPLEMENTED), REM-2 (A STALE_SPECIFICATION; B DOCUMENTED_UNIMPLEMENTED)
- DEL-05-02 other: CLM-005 (A ACCEPTED_DIVERGENCE; B PARTIALLY_IMPLEMENTED)
- DEL-06-02 SS_vs_RSM: CLM-001 (A STALE_SPECIFICATION; B REMAINING_STATE_MISMATCH), CLM-008 (A STALE_SPECIFICATION; B REMAINING_STATE_MISMATCH), CLM-016 (A STALE_SPECIFICATION; B REMAINING_STATE_MISMATCH), CLM-022 (A STALE_SPECIFICATION; B REMAINING_STATE_MISMATCH), CLM-029 (A STALE_SPECIFICATION; B REMAINING_STATE_MISMATCH)
- DEL-06-02 SS_or_RSM_other: CLM-004 (A IMPLEMENTED_DIFFERENTLY/STALE_SPECIFICATION; B IMPLEMENTED_DIFFERENTLY), CLM-005 (A STALE_SPECIFICATION; B IMPLEMENTED_DIFFERENTLY), CLM-011 (A STALE_SPECIFICATION; B NOT_AUDITABLE), CLM-021 (A PARTIALLY_IMPLEMENTED/STALE_SPECIFICATION; B PARTIALLY_IMPLEMENTED), CLM-026 (A STALE_SPECIFICATION; B PARTIALLY_IMPLEMENTED), CLM-032 (A IMPLEMENTED_DIFFERENTLY; B STALE_SPECIFICATION)
- DEL-06-02 other: CLM-010 (A AUTHORITY_CONFLICT/DOCUMENTED_UNIMPLEMENTED/IMPLEMENTED_DIFFERENTLY/PARTIALLY_IMPLEMENTED; B AUTHORITY_CONFLICT/IMPLEMENTED_DIFFERENTLY/PARTIALLY_IMPLEMENTED), CLM-015 (A IMPLEMENTED_DIFFERENTLY/NOT_AUDITABLE; B IMPLEMENTED_DIFFERENTLY), CLM-019 (A IMPLEMENTED_DIFFERENTLY; B PARTIALLY_IMPLEMENTED), CLM-020 (A PARTIALLY_IMPLEMENTED; B IMPLEMENTED_DIFFERENTLY), CLM-031 (A NOT_AUDITABLE; B IMPLEMENTED_DIFFERENTLY)

## 10. Addendum 6 (R4-Q1 subject test) — stage difference between A and B

- RUN_BASIS Addendum 6 was adopted while both DEL-05-02 workers were in pass 1. The PKG-05 manager sent the identical notice (`BRIEFS/RULE_NOTICE_ADDENDUM6.md`) to A and B by SendMessage at the same moment (STATE.jsonl `rule_adopted`, 2026-09-21T20:25Z).
- **Worker A received it before sealing and applied it. Worker B had already sealed** (its claims file hash at send time equals its sealed hash) and left the ledger unchanged, listing the rows the test would touch in its notes §6a. The two ledgers are therefore not at the same rule stage for R4-Q1; R3 re-derives R4-Q1 on B's sealed rows by script from the REACH tags (Addendum 6 scope).
- Base keys citing R4-Q1: A 1 (CLM-010); B 0 (none).
- HumanDecisionNeeded exact agreement on indexed base keys: 31/33 (94%). Disposition is unaffected by the test's rule 3 (R4-Q1 citation) but rules 1–2 can move a row between module-level and live-path readings.
- RUN_BASIS Addendum 7 (R4-Q5) was adopted after **both** A and B had sealed their forward ledgers (STATE.jsonl `rule_adopted` Addendum 7), so neither received it and both are at the same stage for R4-Q5; any plain `R4` rows on the stored-as-received vs translated question are mapped by R3.

