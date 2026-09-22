# DOUBLE_BLIND_COMPARISON — DEL-07-02 (F-07-02A vs F-07-02B)

> Script-derived by `R2/PKG-07/_scripts/double_blind.py` (R0 script adapted by path only). Agent measurement, not a ruling.

- A ledger: `DEL-07-02_A/DEL-07-02_claims.csv` sha256 `a085ae8197e01bc1fef106a0ce21c23964f2675c65e22c0e095310caf68b7b3e`; rows 53; base keys 35
- B ledger: `DEL-07-02_B/DEL-07-02_claims.csv` sha256 `ddea31e03f538b77d5e1f28b482a02507c3104010cc2971b84d19e139d9da0b1`; rows 53; base keys 37
- Base keys in both: 31; only A: []; only B: ['DEL-07-02#REGISTER-4', 'DEL-07-02#REGISTER-5']

- Indexed base keys compared: 31. Run-local keys (REGISTER-n/STATE-n) are numbered independently by each worker, so they are excluded from agreement and listed in §6.
Comparison unit: the base key (`.n` split suffix removed). Two readings agree on a field when the *set* of values across that base key's rows is identical; a secondary 'overlap' measure counts keys whose value sets intersect.

## 1. Field agreement on base keys

| Field | Exact agreement | Overlap agreement | Keys compared |
|---|---|---|---|
| ClaimType | 25/31 (81%) | 29/31 (94%) | 31 |
| Disposition | 19/31 (61%) | 24/31 (77%) | 31 |
| AuthorityTier | 21/31 (68%) | 25/31 (81%) | 31 |
| CauseTag | 15/31 (48%) | 19/31 (61%) | 31 |
| Confidence (secondary) | 25/31 | – | 31 |

## 2. Split rate

- A: 7/35 base keys split (20.0%); rows/base key 1.51
- B: 4/37 base keys split (10.8%); rows/base key 1.43
- Split-rate difference: 9.2 percentage points
- Keys split by both: 3; only A: ['DEL-07-02#CLM-013', 'DEL-07-02#CLM-020', 'DEL-07-02#CLM-021', 'DEL-07-02#CLM-025']; only B: ['DEL-07-02#CLM-011']

## 3. Histograms

**Disposition** (rows) — A: {'ALIGNED': 4, 'DOCUMENTED_UNIMPLEMENTED': 16, 'NOT_AUDITABLE': 5, 'PARTIALLY_IMPLEMENTED': 11, 'REMAINING_STATE_MISMATCH': 1, 'STALE_SPECIFICATION': 16}; B: {'ALIGNED': 1, 'DOCUMENTED_UNIMPLEMENTED': 19, 'NOT_AUDITABLE': 7, 'PARTIALLY_IMPLEMENTED': 11, 'REMAINING_STATE_MISMATCH': 2, 'STALE_SPECIFICATION': 13}

**CauseTag** (rows) — A: {'A2_TOPOLOGY': 21, 'CARRIER_PROPAGATION': 1, 'NONE': 9, 'PRE_V3_DRIFT': 22}; B: {'A2_TOPOLOGY': 22, 'CARRIER_PROPAGATION': 1, 'DOC_HYGIENE': 14, 'NONE': 8, 'PRE_V3_DRIFT': 8}

**ClaimType** (rows) — A: {'ACCEPTANCE': 2, 'CONTEXT_CLAIM': 12, 'REGISTER_DEFECT': 3, 'REQUIREMENT': 28, 'STATE_ASSERTION': 8}; B: {'ACCEPTANCE': 2, 'CONTEXT_CLAIM': 11, 'REGISTER_DEFECT': 5, 'REQUIREMENT': 28, 'STATE_ASSERTION': 7}

**AuthorityTier** (rows) — A: {'GOVERNANCE_INVARIANT': 23, 'LOCAL_DESIGN': 6, 'NOT_APPLICABLE': 22, 'PRD': 2}; B: {'GOVERNANCE_INVARIANT': 26, 'LOCAL_DESIGN': 2, 'NOT_APPLICABLE': 22, 'PRD': 3}

**Confidence** (rows) — A: {'HIGH': 37, 'MEDIUM': 16}; B: {'HIGH': 38, 'MEDIUM': 15}

## 4. Reverse Response agreement

- A sha256 `f654bdc041ceb63efeb96310f2fe4c227d365d87c01db6787b5e1b04be27ed23`; B sha256 `95681f6ade6bbb27a5f712c73aad3ea4b669089a2ec5077f22702e72a0a09cc0`
- Capabilities answered by both: 364
- Exact Response agreement: 362/364 (99%)
- Coarse agreement (mine vs NOT_MINE): 363/364 (100%)
- Same claiming base key where both CLAIMED_BY/PARTIAL agree: 6/6
- Response histogram A: {'NOT_MINE': 356, 'PARTIAL': 4, 'CLAIMED_BY': 4}; B: {'NOT_MINE': 357, 'PARTIAL': 4, 'CLAIMED_BY': 3}

## 5. Every disagreement, both readings

### 5.1 Forward fields

| Base key | Field | A reading | B reading |
|---|---|---|---|
| DEL-07-02#CLM-001 | CauseTag | PRE_V3_DRIFT | DOC_HYGIENE |
| DEL-07-02#CLM-004 | Disposition | PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | DOCUMENTED_UNIMPLEMENTED / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION |
| DEL-07-02#CLM-004 | CauseTag | A2_TOPOLOGY / PRE_V3_DRIFT | A2_TOPOLOGY / DOC_HYGIENE / PRE_V3_DRIFT |
| DEL-07-02#CLM-005 | Disposition | DOCUMENTED_UNIMPLEMENTED | PARTIALLY_IMPLEMENTED |
| DEL-07-02#CLM-005 | CauseTag | A2_TOPOLOGY | PRE_V3_DRIFT |
| DEL-07-02#CLM-006 | CauseTag | PRE_V3_DRIFT | DOC_HYGIENE |
| DEL-07-02#CLM-007 | CauseTag | PRE_V3_DRIFT | DOC_HYGIENE |
| DEL-07-02#CLM-009 | AuthorityTier | GOVERNANCE_INVARIANT | GOVERNANCE_INVARIANT / PRD |
| DEL-07-02#CLM-011 | Disposition | STALE_SPECIFICATION | NOT_AUDITABLE / STALE_SPECIFICATION |
| DEL-07-02#CLM-011 | CauseTag | PRE_V3_DRIFT | DOC_HYGIENE / NONE |
| DEL-07-02#CLM-012 | AuthorityTier | LOCAL_DESIGN | PRD |
| DEL-07-02#CLM-013 | ClaimType | CONTEXT_CLAIM / REQUIREMENT | REQUIREMENT |
| DEL-07-02#CLM-013 | Disposition | ALIGNED / STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-07-02#CLM-013 | AuthorityTier | LOCAL_DESIGN / NOT_APPLICABLE | LOCAL_DESIGN |
| DEL-07-02#CLM-013 | CauseTag | NONE / PRE_V3_DRIFT | PRE_V3_DRIFT |
| DEL-07-02#CLM-014 | Disposition | DOCUMENTED_UNIMPLEMENTED / STALE_SPECIFICATION | DOCUMENTED_UNIMPLEMENTED / NOT_AUDITABLE |
| DEL-07-02#CLM-014 | CauseTag | A2_TOPOLOGY / PRE_V3_DRIFT | A2_TOPOLOGY / NONE |
| DEL-07-02#CLM-015 | CauseTag | PRE_V3_DRIFT | DOC_HYGIENE |
| DEL-07-02#CLM-019 | Disposition | PARTIALLY_IMPLEMENTED | DOCUMENTED_UNIMPLEMENTED |
| DEL-07-02#CLM-019 | AuthorityTier | LOCAL_DESIGN | GOVERNANCE_INVARIANT |
| DEL-07-02#CLM-019 | CauseTag | PRE_V3_DRIFT | A2_TOPOLOGY |
| DEL-07-02#CLM-020 | ClaimType | CONTEXT_CLAIM / REQUIREMENT | REQUIREMENT |
| DEL-07-02#CLM-020 | Disposition | ALIGNED / STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-07-02#CLM-020 | AuthorityTier | LOCAL_DESIGN / NOT_APPLICABLE | LOCAL_DESIGN |
| DEL-07-02#CLM-020 | CauseTag | NONE / PRE_V3_DRIFT | PRE_V3_DRIFT |
| DEL-07-02#CLM-021 | ClaimType | ACCEPTANCE / STATE_ASSERTION | ACCEPTANCE |
| DEL-07-02#CLM-021 | Disposition | PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-07-02#CLM-021 | AuthorityTier | LOCAL_DESIGN / NOT_APPLICABLE | PRD |
| DEL-07-02#CLM-022 | CauseTag | PRE_V3_DRIFT | DOC_HYGIENE |
| DEL-07-02#CLM-024 | Disposition | PARTIALLY_IMPLEMENTED | DOCUMENTED_UNIMPLEMENTED |
| DEL-07-02#CLM-025 | ClaimType | CONTEXT_CLAIM / REQUIREMENT | CONTEXT_CLAIM |
| DEL-07-02#CLM-025 | Disposition | ALIGNED / STALE_SPECIFICATION | STALE_SPECIFICATION |
| DEL-07-02#CLM-025 | AuthorityTier | LOCAL_DESIGN / NOT_APPLICABLE | NOT_APPLICABLE |
| DEL-07-02#CLM-025 | CauseTag | NONE / PRE_V3_DRIFT | DOC_HYGIENE |
| DEL-07-02#CLM-026 | ClaimType | REQUIREMENT | CONTEXT_CLAIM |
| DEL-07-02#CLM-026 | Disposition | PARTIALLY_IMPLEMENTED | NOT_AUDITABLE |
| DEL-07-02#CLM-026 | AuthorityTier | PRD | NOT_APPLICABLE |
| DEL-07-02#CLM-026 | CauseTag | PRE_V3_DRIFT | NONE |
| DEL-07-02#CLM-028 | ClaimType | CONTEXT_CLAIM | REQUIREMENT |
| DEL-07-02#CLM-028 | Disposition | NOT_AUDITABLE | DOCUMENTED_UNIMPLEMENTED |
| DEL-07-02#CLM-028 | AuthorityTier | NOT_APPLICABLE | GOVERNANCE_INVARIANT |
| DEL-07-02#CLM-028 | CauseTag | NONE | A2_TOPOLOGY |
| DEL-07-02#CLM-029 | AuthorityTier | PRD | GOVERNANCE_INVARIANT |
| DEL-07-02#CLM-031 | CauseTag | PRE_V3_DRIFT | DOC_HYGIENE |

### 5.2 Reverse responses

| CapabilityID | A | B |
|---|---|---|
| CAP-RTCONTRACT-004 | PARTIAL DEL-07-02#CLM-009.9 | NOT_MINE  |
| CAP-RTCORE-023 | CLAIMED_BY DEL-07-02#CLM-009.9 | PARTIAL DEL-07-02#CLM-003 |

## 6. Run-local rows (not key-comparable)

| Worker | Key | ClaimType | Disposition | CauseTag | DeclaredState (first 90 chars) |
|---|---|---|---|---|---|
| A | DEL-07-02#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | PRE_V3_DRIFT | CONTRACT, SPEC and PRD recorded MATCH |
| A | DEL-07-02#REGISTER-2 | REGISTER_DEFECT | STALE_SPECIFICATION | PRE_V3_DRIFT | RequiredMaturity counts SEMANTIC_READY 4, TBD 7; annotation says counts reflect Dependenci |
| A | DEL-07-02#REGISTER-3 | REGISTER_DEFECT | STALE_SPECIFICATION | PRE_V3_DRIFT | Evidence rows cite Datasheet.md, Procedure.md and Specification.md in this folder |
| A | DEL-07-02#STATE-1 | STATE_ASSERTION | REMAINING_STATE_MISMATCH | CARRIER_PROPAGATION | IN_PROGRESS, Last Updated 2026-07-12, no Remaining items, no D-GOV-43/D-APP-127 note |
| B | DEL-07-02#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | REF-002 CONTRACT fa8fc9dc..., REF-003 SPEC 01e1c75c..., REF-006 PRD 8649ccba... recorded M |
| B | DEL-07-02#REGISTER-2 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | Last Updated 2026-07-12; Authorization Basis D-APP-19 Option D; Checking Approval SHA 8c6d |
| B | DEL-07-02#REGISTER-3 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | RequiredMaturity counts SEMANTIC_READY 4 and TBD 7; annotation says the summary counts ref |
| B | DEL-07-02#REGISTER-4 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | EvidenceFile/SourceRef cite Datasheet.md, Procedure.md, Specification.md; DEP-07-02-004 Ta |
| B | DEL-07-02#REGISTER-5 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | Register text restates 'REF-006 is MATCH under D-APP-38' as current |
| B | DEL-07-02#STATE-1 | STATE_ASSERTION | REMAINING_STATE_MISMATCH | CARRIER_PROPAGATION | No Remaining items; R6 closeout 'surviving deliverable-local items retained' |

## 7. Row-level agreement where both split a key identically

- ClaimType: 13/15 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- Disposition: 13/15 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- AuthorityTier: 12/15 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- CauseTag: 13/15 sub-rows agree across 2 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)

## 8. Strict agreement on keys neither worker split

Keys unsplit by both: 23.

| Field | Agreement |
|---|---|
| ClaimType | 21/23 (91%) |
| Disposition | 18/23 (78%) |
| AuthorityTier | 18/23 (78%) |
| CauseTag | 13/23 (57%) |
| ALIGNED vs non-ALIGNED | 23/23 |

## 9. Addenda 5 and 6 effects (manager supplement, `_scripts/double_blind_addenda.py`)

Both workers received the Addendum 5 tie-break and the Addendum 6 subject test verbatim and identically (`BRIEFS/WORKER_BRIEF.md`).

| Measure | Result |
|---|---|
| Disposition, exact (value sets per base key) | 19/31 (61%) |
| Disposition, overlap | 24/31 (77%) |
| Keys where either worker used STALE_SPECIFICATION or REMAINING_STATE_MISMATCH | 13 |
| …of which the workers disagree on Disposition | 7 |
| …of which the disagreement is purely STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH | 0 (none) |
| HumanDecisionNeeded, exact | 19/31 (61%) |
| R4-Q1 presence (either row of the base key cites it), agreement | 19/31 (61%) |
| Base keys citing R4-Q1: A / B / both | 0 / 12 / 0 |
| Rows citing R4-Q1: A / B | 0 / 22 |
| Rows with `ALSO_MODULE:` in Notes: A / B | 18 / 19 |
| Rows with `ALSO:` in Notes: A / B | 3 / 0 |

### 9.1 Disposition disagreements with STALE_SPECIFICATION / REMAINING_STATE_MISMATCH

| Base key | A | B |
|---|---|---|
| DEL-07-02#CLM-004 | PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | DOCUMENTED_UNIMPLEMENTED / PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION |
| DEL-07-02#CLM-011 | STALE_SPECIFICATION | NOT_AUDITABLE / STALE_SPECIFICATION |
| DEL-07-02#CLM-013 | ALIGNED / STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-07-02#CLM-014 | DOCUMENTED_UNIMPLEMENTED / STALE_SPECIFICATION | DOCUMENTED_UNIMPLEMENTED / NOT_AUDITABLE |
| DEL-07-02#CLM-020 | ALIGNED / STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-07-02#CLM-021 | PARTIALLY_IMPLEMENTED / STALE_SPECIFICATION | PARTIALLY_IMPLEMENTED |
| DEL-07-02#CLM-025 | ALIGNED / STALE_SPECIFICATION | STALE_SPECIFICATION |

### 9.2 R4-Q1 splits, with each worker's REACH tags

| Base key | A HDN | A REACH | B HDN | B REACH |
|---|---|---|---|---|
| DEL-07-02#CLM-003 | NO | LIVE,TEST_ONLY | R4-Q1 | LEGACY_ONLY,LIVE |
| DEL-07-02#CLM-004 | NO | LIVE,TEST_ONLY | NO / R4-Q1 | LEGACY_ONLY,LIVE |
| DEL-07-02#CLM-005 | NO | LIVE,TEST_ONLY | R4-Q1 | LEGACY_ONLY |
| DEL-07-02#CLM-008 | NO | LIVE,TEST_ONLY | R4-Q1 | LEGACY_ONLY,LIVE |
| DEL-07-02#CLM-009 | NO | LIVE,TEST_ONLY | NO / R4-Q1 | LEGACY_ONLY,LIVE |
| DEL-07-02#CLM-010 | NO | LIVE,TEST_ONLY | R4-Q1 | LEGACY_ONLY,LIVE |
| DEL-07-02#CLM-013 | NO | LIVE,TEST_ONLY | R4-Q1 | LEGACY_ONLY,TEST_ONLY |
| DEL-07-02#CLM-018 | NO | LIVE,TEST_ONLY | R4-Q1 | LEGACY_ONLY,LIVE |
| DEL-07-02#CLM-019 | NO | TEST_ONLY | R4-Q1 | LEGACY_ONLY,LIVE |
| DEL-07-02#CLM-024 | NO | LIVE,TEST_ONLY | R4-Q1 | LEGACY_ONLY,LIVE |
| DEL-07-02#CLM-028 | NO | no-code | R4-Q1 | LEGACY_ONLY,LIVE |
| DEL-07-02#CLM-029 | NO | LIVE,TEST_ONLY | R4-Q1 | LEGACY_ONLY,LIVE |

REACH tag counts (all rows): A {'LIVE': 111, 'TEST_ONLY': 34}; B {'LIVE': 113, 'LEGACY_ONLY': 31, 'TEST_ONLY': 7}.

## 10. Reading (hand-written by the PKG-07 manager; agent measurement, not a ruling)

- **Disposition overall:** exact 19/31 (61%), overlap 24/31 (77%); on the 23 keys neither worker split,
  18/23 (78%), and ALIGNED-vs-non-ALIGNED 23/23. Most exact-set disagreements come from worker A
  splitting a key into an ALIGNED/PARTIAL row plus a STALE_SPECIFICATION row (CLM-013, 020, 021, 025)
  where B wrote one row, and from DOCUMENTED_UNIMPLEMENTED vs PARTIALLY_IMPLEMENTED on the 501 scaffold
  route (CLM-005, 019, 024: whether the served route counts as partial delivery).
- **STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH (Addendum 5):** no key splits purely between the two.
  Both workers put the REF-006 MATCH restatements and the stale register text in STALE_SPECIFICATION and
  kept REMAINING_STATE_MISMATCH for Remaining/metadata lag (A 1 row, B 2). Compared with DEL-06-02
  (19/35, most splits between these two verdicts), the tie-break removed this source of variance here.
- **HumanDecisionNeeded / R4-Q1 (Addendum 6):** agreement 19/31 (61%); A cites R4-Q1 on 0 rows, B on 22
  (12 base keys). Both workers read the claims as product behaviour and both wrote `ALSO_MODULE:` on
  ~18–19 rows, so the subject test was applied the same way. The split comes from **REACH tagging of
  `scaffold.ts`**: A tagged the parser/plan code TEST_ONLY (only tests call `scaffoldExecutionRoot`), B
  tagged it LEGACY_ONLY (reached via the legacy `scaffold_preview` tool). The verifier of A's ledger
  sided with B's tag on those lines (CORRECTIONS.csv) but held that mixed TEST_ONLY + LEGACY_ONLY
  evidence does not meet rule 3's "only code meeting the claim is LEGACY_ONLY". Addendum 6 therefore
  stabilised the subject reading; the remaining variance is in symbol-level reach and in how rule 3
  treats mixed legacy/test-only evidence.
- **Reverse:** Response agreement 362/364 (99%); same claiming base key 6/6.
- **CauseTag** agreement stays low (15/31): A used PRE_V3_DRIFT for the REF-006 drift (refuted by its
  verifier: the drift is 2026-09-12, DOC_HYGIENE) and A2_TOPOLOGY for the scaffold gap; B spread the same
  rows differently.

