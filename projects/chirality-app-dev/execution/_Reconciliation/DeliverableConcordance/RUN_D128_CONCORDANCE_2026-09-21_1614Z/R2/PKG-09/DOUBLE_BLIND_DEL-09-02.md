# DOUBLE_BLIND_COMPARISON — DEL-09-02 (F-09-02A vs F-09-02B)

> Script-derived by `R2/PKG-09/_scripts/double_blind.py` (R0 script adapted by path only). Agent measurement, not a ruling.

- A ledger: `DEL-09-02_A/DEL-09-02_claims.csv` sha256 `3fa55fc71056ae01311b84316dc61015a065f6c4efec17251441c2ed8ba65cc7`; rows 53; base keys 35
- B ledger: `DEL-09-02_B/DEL-09-02_claims.csv` sha256 `b93c270a66911f33a9a4ba5d74829e7d07d19816a4848f10df145bb4f6fd065c`; rows 50; base keys 33
- Base keys in both: 29; only A: ['DEL-09-02#REGISTER-4', 'DEL-09-02#STATE-2']; only B: []

- Indexed base keys compared: 29. Run-local keys (REGISTER-n/STATE-n) are numbered independently by each worker, so they are excluded from agreement and listed in §6.
Comparison unit: the base key (`.n` split suffix removed). Two readings agree on a field when the *set* of values across that base key's rows is identical; a secondary 'overlap' measure counts keys whose value sets intersect.

## 1. Field agreement on base keys

| Field | Exact agreement | Overlap agreement | Keys compared |
|---|---|---|---|
| ClaimType | 18/29 (62%) | 20/29 (69%) | 29 |
| Disposition | 23/29 (79%) | 27/29 (93%) | 29 |
| AuthorityTier | 18/29 (62%) | 21/29 (72%) | 29 |
| CauseTag | 17/29 (59%) | 20/29 (69%) | 29 |
| HumanDecisionNeeded | 24/29 (83%) | 26/29 (90%) | 29 |
| Confidence (secondary) | 25/29 | – | 29 |

## 2. Split rate

- A: 3/35 base keys split (8.6%); rows/base key 1.51
- B: 3/33 base keys split (9.1%); rows/base key 1.52
- Split-rate difference: 0.5 percentage points
- Keys split by both: 2; only A: ['DEL-09-02#CLM-012']; only B: ['DEL-09-02#CLM-014']

## 3. Histograms

**Disposition** (rows) — A: {'ALIGNED': 9, 'AUTHORITY_CONFLICT': 2, 'DOCUMENTED_UNIMPLEMENTED': 4, 'IMPLEMENTED_DIFFERENTLY': 4, 'NOT_AUDITABLE': 5, 'PARTIALLY_IMPLEMENTED': 4, 'REMAINING_STATE_MISMATCH': 2, 'STALE_SPECIFICATION': 23}; B: {'ALIGNED': 6, 'DOCUMENTED_UNIMPLEMENTED': 4, 'IMPLEMENTED_DIFFERENTLY': 6, 'NOT_AUDITABLE': 4, 'PARTIALLY_IMPLEMENTED': 3, 'REMAINING_STATE_MISMATCH': 1, 'STALE_SPECIFICATION': 25, 'STALE_VERIFICATION': 1}

**CauseTag** (rows) — A: {'CODEX_SOLE_ENGINE': 11, 'DOC_HYGIENE': 15, 'LIFECYCLE_GATE_PENDING': 1, 'NATIVE_DELEGATION': 1, 'NONE': 14, 'PRE_V3_DRIFT': 10, 'RUNTIME_EXTRACTION': 1}; B: {'CARRIER_PROPAGATION': 13, 'CODEX_SOLE_ENGINE': 12, 'DOC_HYGIENE': 11, 'LIFECYCLE_GATE_PENDING': 1, 'NATIVE_DELEGATION': 1, 'NONE': 10, 'PRE_V3_DRIFT': 2}

**ClaimType** (rows) — A: {'ACCEPTANCE': 3, 'CONTEXT_CLAIM': 8, 'EXCLUSION': 1, 'REGISTER_DEFECT': 4, 'REMAINING_WORK': 1, 'REQUIREMENT': 24, 'STATE_ASSERTION': 12}; B: {'ACCEPTANCE': 4, 'CONTEXT_CLAIM': 14, 'EXCLUSION': 1, 'REGISTER_DEFECT': 3, 'REMAINING_WORK': 1, 'REQUIREMENT': 23, 'STATE_ASSERTION': 4}

**AuthorityTier** (rows) — A: {'GOVERNANCE_INVARIANT': 20, 'LOCAL_DESIGN': 9, 'NOT_APPLICABLE': 23, 'PRD': 1}; B: {'GOVERNANCE_INVARIANT': 13, 'LOCAL_DESIGN': 13, 'NOT_APPLICABLE': 17, 'PRD': 7}

**Confidence** (rows) — A: {'HIGH': 29, 'LOW': 1, 'MEDIUM': 23}; B: {'HIGH': 29, 'LOW': 2, 'MEDIUM': 19}

## 4. Reverse Response agreement

- A sha256 `f65175999437a2f59a8c17968c78c53e3ef11166e7472795e481c2771b9dfa2b`; B sha256 `dbe5e68dddeba5cc2eef30302516dbc798eb2f6e280a8cb6d08842972db943c9`
- Capabilities answered by both: 322
- Exact Response agreement: 307/322 (95%)
- Coarse agreement (mine vs NOT_MINE): 307/322 (95%)
- Same claiming base key where both CLAIMED_BY/PARTIAL agree: 3/3
- Response histogram A: {'NOT_MINE': 319, 'PARTIAL': 2, 'CLAIMED_BY': 1}; B: {'NOT_MINE': 304, 'PARTIAL': 17, 'CLAIMED_BY': 1}

## 5. Every disagreement, both readings

### 5.1 Forward fields

| Base key | Field | A reading | B reading |
|---|---|---|---|
| DEL-09-02#CLM-001 | ClaimType | STATE_ASSERTION | CONTEXT_CLAIM |
| DEL-09-02#CLM-003 | ClaimType | REQUIREMENT | CONTEXT_CLAIM |
| DEL-09-02#CLM-003 | AuthorityTier | GOVERNANCE_INVARIANT | NOT_APPLICABLE |
| DEL-09-02#CLM-004 | ClaimType | STATE_ASSERTION | CONTEXT_CLAIM |
| DEL-09-02#CLM-004 | CauseTag | DOC_HYGIENE | CARRIER_PROPAGATION |
| DEL-09-02#CLM-005 | AuthorityTier | GOVERNANCE_INVARIANT | PRD |
| DEL-09-02#CLM-005 | CauseTag | PRE_V3_DRIFT | CARRIER_PROPAGATION |
| DEL-09-02#CLM-007 | AuthorityTier | NOT_APPLICABLE | LOCAL_DESIGN |
| DEL-09-02#CLM-007 | HumanDecisionNeeded | R4-Q1 | NO |
| DEL-09-02#CLM-008 | ClaimType | STATE_ASSERTION | CONTEXT_CLAIM |
| DEL-09-02#CLM-009 | Disposition | ALIGNED | STALE_SPECIFICATION |
| DEL-09-02#CLM-009 | AuthorityTier | LOCAL_DESIGN | PRD |
| DEL-09-02#CLM-009 | CauseTag | NONE | CARRIER_PROPAGATION |
| DEL-09-02#CLM-010 | Disposition | ALIGNED / AUTHORITY_CONFLICT / DOCUMENTED_UNIMPLEMENTED / IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | ALIGNED / DOCUMENTED_UNIMPLEMENTED / IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION |
| DEL-09-02#CLM-010 | AuthorityTier | GOVERNANCE_INVARIANT / PRD | GOVERNANCE_INVARIANT / LOCAL_DESIGN / PRD |
| DEL-09-02#CLM-010 | CauseTag | CODEX_SOLE_ENGINE / NATIVE_DELEGATION / NONE / PRE_V3_DRIFT / RUNTIME_EXTRACTION | CARRIER_PROPAGATION / CODEX_SOLE_ENGINE / NATIVE_DELEGATION / NONE |
| DEL-09-02#CLM-012 | ClaimType | REQUIREMENT / STATE_ASSERTION | ACCEPTANCE |
| DEL-09-02#CLM-012 | Disposition | ALIGNED / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | STALE_SPECIFICATION |
| DEL-09-02#CLM-012 | AuthorityTier | LOCAL_DESIGN / NOT_APPLICABLE | LOCAL_DESIGN |
| DEL-09-02#CLM-012 | CauseTag | CODEX_SOLE_ENGINE / NONE / PRE_V3_DRIFT | CARRIER_PROPAGATION |
| DEL-09-02#CLM-012 | HumanDecisionNeeded | NO / R4-Q1 | NO |
| DEL-09-02#CLM-013 | ClaimType | STATE_ASSERTION | REQUIREMENT |
| DEL-09-02#CLM-013 | AuthorityTier | NOT_APPLICABLE | LOCAL_DESIGN |
| DEL-09-02#CLM-014 | ClaimType | ACCEPTANCE | ACCEPTANCE / STATE_ASSERTION |
| DEL-09-02#CLM-014 | Disposition | ALIGNED | ALIGNED / PARTIALLY_IMPLEMENTED |
| DEL-09-02#CLM-014 | AuthorityTier | GOVERNANCE_INVARIANT | LOCAL_DESIGN / PRD |
| DEL-09-02#CLM-014 | CauseTag | NONE | CODEX_SOLE_ENGINE / NONE |
| DEL-09-02#CLM-014 | HumanDecisionNeeded | NO | NO / R4-Q1 |
| DEL-09-02#CLM-015 | ClaimType | STATE_ASSERTION | CONTEXT_CLAIM |
| DEL-09-02#CLM-017 | ClaimType | STATE_ASSERTION | CONTEXT_CLAIM |
| DEL-09-02#CLM-018 | AuthorityTier | GOVERNANCE_INVARIANT | LOCAL_DESIGN |
| DEL-09-02#CLM-018 | CauseTag | PRE_V3_DRIFT | CARRIER_PROPAGATION |
| DEL-09-02#CLM-019 | Disposition | PARTIALLY_IMPLEMENTED | STALE_SPECIFICATION |
| DEL-09-02#CLM-019 | CauseTag | CODEX_SOLE_ENGINE | CARRIER_PROPAGATION |
| DEL-09-02#CLM-019 | HumanDecisionNeeded | R4-Q1 | NO |
| DEL-09-02#CLM-020 | ClaimType | ACCEPTANCE / STATE_ASSERTION | ACCEPTANCE / REQUIREMENT |
| DEL-09-02#CLM-020 | Disposition | PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | STALE_SPECIFICATION / STALE_VERIFICATION |
| DEL-09-02#CLM-020 | AuthorityTier | LOCAL_DESIGN / NOT_APPLICABLE | LOCAL_DESIGN |
| DEL-09-02#CLM-020 | CauseTag | PRE_V3_DRIFT | CARRIER_PROPAGATION / PRE_V3_DRIFT |
| DEL-09-02#CLM-021 | ClaimType | STATE_ASSERTION | CONTEXT_CLAIM |
| DEL-09-02#CLM-024 | CauseTag | PRE_V3_DRIFT | CARRIER_PROPAGATION |
| DEL-09-02#CLM-025 | CauseTag | PRE_V3_DRIFT | CARRIER_PROPAGATION |
| DEL-09-02#CLM-027 | CauseTag | DOC_HYGIENE | CARRIER_PROPAGATION |
| DEL-09-02#CLM-028 | AuthorityTier | NOT_APPLICABLE | LOCAL_DESIGN |
| DEL-09-02#CLM-028 | HumanDecisionNeeded | R4-Q1 | NO |

### 5.2 Reverse responses

| CapabilityID | A | B |
|---|---|---|
| CAP-HARNESS-025 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.8 |
| CAP-HARNESS-030 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.3 |
| CAP-HARNESS-031 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.5 |
| CAP-HARNESS-032 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.3 |
| CAP-HARNESS-038 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.4 |
| CAP-HARNESS-043 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.6 |
| CAP-HARNESS-045 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.8 |
| CAP-HARNESS-047 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.8 |
| CAP-HARNESS-048 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.9 |
| CAP-HARNESS-050 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.7 |
| CAP-HARNESS-053 | NOT_MINE  | PARTIAL DEL-09-02#CLM-007 |
| CAP-HARNESS-058 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.11 |
| CAP-RTCONTRACT-021 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.4 |
| CAP-RTCONTRACT-039 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.2 |
| CAP-RTCONTRACT-044 | NOT_MINE  | PARTIAL DEL-09-02#CLM-010.7 |

## 6. Run-local rows (not key-comparable)

| Worker | Key | ClaimType | Disposition | CauseTag | DeclaredState (first 90 chars) |
|---|---|---|---|---|---|
| A | DEL-09-02#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | CONTRACT fa8fc9dc..., SPEC 01e1c75c..., PRD 8649ccba... recorded MATCH |
| A | DEL-09-02#REGISTER-2 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | Last Updated 2026-09-03 |
| A | DEL-09-02#REGISTER-3 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | [WARNING] TBD_SURFACES: registry path, runner entrypoint, command, summary schema path and |
| A | DEL-09-02#REGISTER-4 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | All 25 rows SatisfactionStatus TBD; execution targets DEL-04-02 SdkOptionsBuilder, DEL-04- |
| A | DEL-09-02#STATE-1 | STATE_ASSERTION | STALE_SPECIFICATION | CODEX_SOLE_ENGINE | Claude Agent SDK / Anthropic remains the first concrete/current path; validation must prov |
| A | DEL-09-02#STATE-2 | CONTEXT_CLAIM | NOT_AUDITABLE | NONE | Dated semantic lens over Datasheet/Specification/Guidance/Procedure; STATUS_POLICY PRESERV |
| B | DEL-09-02#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | CONTRACT, SPEC and PRD ExpectedSHA256 = ActualSHA256, Status MATCH |
| B | DEL-09-02#REGISTER-2 | REGISTER_DEFECT | STALE_SPECIFICATION | CARRIER_PROPAGATION | [WARNING] TBD_SURFACES: registry path, runner entrypoint, command, summary schema path and |
| B | DEL-09-02#REGISTER-3 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | Last Updated 2026-09-03; Checking Approval SHA 8c6d55d3… on an IN_PROGRESS item; no D-GOV- |
| B | DEL-09-02#STATE-1 | STATE_ASSERTION | STALE_SPECIFICATION | CODEX_SOLE_ENGINE | Claude Agent SDK / Anthropic remains the first concrete/current path; runtime validation m |

## 7. Row-level agreement where both split a key identically

- ClaimType: 17/18 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- Disposition: 14/18 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- AuthorityTier: 13/18 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- CauseTag: 13/18 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- HumanDecisionNeeded: 15/18 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)

## 8. Strict agreement on keys neither worker split

Keys unsplit by both: 25.

| Field | Agreement |
|---|---|
| ClaimType | 17/25 (68%) |
| Disposition | 23/25 (92%) |
| AuthorityTier | 18/25 (72%) |
| CauseTag | 17/25 (68%) |
| HumanDecisionNeeded | 22/25 (88%) |
| ALIGNED vs non-ALIGNED | 24/25 |

## 9. Disposition agreement, STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH splits, and HumanDecisionNeeded (R4-Qn)

> Script-derived by `R2/PKG-09/_scripts/tiebreak_split.py`. Both workers received the Addendum 5 tie-break, the Addendum 6 subject test, the HELP_HUMAN rule-3 clarification and the R4-Q4/R4-Q5 vocabulary verbatim in the same brief, before dispatch (STATE.jsonl). Baselines are the figures given at dispatch. Agent measurement, not a ruling.

| Measure | DEL-09-02 (wave 5) | DEL-05-02 (wave 2) | DEL-06-02 (wave 1, pre-tie-break) |
|---|---|---|---|
| Disposition exact agreement, indexed base keys | 23/29 (79%) | 24/33 | 19/35 |
| Disagreements that are pure SS vs RSM splits | 0 | – | – |
| Disagreements involving SS or RSM plus another verdict | 5 | – | – |
| Other disagreements | 1 | – | – |
| Agreement on keys where either worker used SS or RSM | 16/21 (76%) | – | – |
| Rows STALE_SPECIFICATION (A / B) | 23 / 25 | – | – |
| Rows REMAINING_STATE_MISMATCH (A / B) | 2 / 1 | – | – |
| HumanDecisionNeeded exact agreement (value set) | 24/29 (83%) | – | – |
| R4/R4-Qn token-set agreement on keys where either cites R4 | 1/6 (17%) | – | – |
| Cites any R4 token vs none (coarse) | 24/29 (83%) | – | – |
| Base keys citing R4-Q1 (A / B / both) | 5 / 2 / 1 | – | – |

- SS_vs_RSM: none
- SS_or_RSM_other: CLM-009 (A ALIGNED; B STALE_SPECIFICATION), CLM-010 (A ALIGNED/AUTHORITY_CONFLICT/DOCUMENTED_UNIMPLEMENTED/IMPLEMENTED_DIFFERENTLY/PARTIALLY_IMPLEMENTED/STALE_SPECIFICATION; B ALIGNED/DOCUMENTED_UNIMPLEMENTED/IMPLEMENTED_DIFFERENTLY/PARTIALLY_IMPLEMENTED/STALE_SPECIFICATION), CLM-012 (A ALIGNED/PARTIALLY_IMPLEMENTED/STALE_SPECIFICATION; B STALE_SPECIFICATION), CLM-019 (A PARTIALLY_IMPLEMENTED; B STALE_SPECIFICATION), CLM-020 (A PARTIALLY_IMPLEMENTED/STALE_SPECIFICATION; B STALE_SPECIFICATION/STALE_VERIFICATION)
- other: CLM-014 (A ALIGNED; B ALIGNED/PARTIALLY_IMPLEMENTED)
- R4 token disagreements: CLM-007 (A R4-Q1; B none), CLM-012 (A R4-Q1; B none), CLM-014 (A none; B R4-Q1), CLM-019 (A R4-Q1; B none), CLM-028 (A R4-Q1; B none)
