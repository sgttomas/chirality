# DOUBLE_BLIND_COMPARISON — DEL-01-03 (worker A vs worker B)

> Script-derived by `R2/PKG-01/_scripts/double_blind.py` (R0 script adapted by path only). Agent measurement, not a ruling.

- A ledger: `DEL-01-03_A/DEL-01-03_claims.csv` sha256 `509da4b44e91eed72d30f34299367ae180a9d2b69f1e676d7ff10390b106ba00`; rows 46; base keys 37
- B ledger: `DEL-01-03_B/DEL-01-03_claims.csv` sha256 `98da94b9763827825efeea1cf9c8cfd37a06777eaff05613cd4db7bcc785121c`; rows 45; base keys 36
- Base keys in both: 31; only A: ['DEL-01-03#REGISTER-3']; only B: []

- Indexed base keys compared: 31. Run-local keys (REGISTER-n/STATE-n) are numbered independently by each worker, so they are excluded from agreement and listed in §6.
Comparison unit: the base key (`.n` split suffix removed). Two readings agree on a field when the *set* of values across that base key's rows is identical; a secondary 'overlap' measure counts keys whose value sets intersect.

## 1. Field agreement on base keys

| Field | Exact agreement | Overlap agreement | Keys compared |
|---|---|---|---|
| ClaimType | 24/31 (77%) | 24/31 (77%) | 31 |
| Disposition | 25/31 (81%) | 26/31 (84%) | 31 |
| AuthorityTier | 28/31 (90%) | 28/31 (90%) | 31 |
| CauseTag | 20/31 (65%) | 21/31 (68%) | 31 |
| Confidence (secondary) | 27/31 | – | 31 |

## 2. Split rate

- A: 1/37 base keys split (2.7%); rows/base key 1.24
- B: 1/36 base keys split (2.8%); rows/base key 1.25
- Split-rate difference: 0.1 percentage points
- Keys split by both: 1; only A: []; only B: []

## 3. Histograms

**Disposition** (rows) — A: {'ALIGNED': 12, 'AUTHORITY_CONFLICT': 4, 'DOCUMENTED_UNIMPLEMENTED': 2, 'NOT_AUDITABLE': 8, 'PARTIALLY_IMPLEMENTED': 7, 'REMAINING_STATE_MISMATCH': 1, 'STALE_SPECIFICATION': 12}; B: {'ALIGNED': 25, 'AUTHORITY_CONFLICT': 3, 'NOT_AUDITABLE': 6, 'STALE_SPECIFICATION': 11}

**CauseTag** (rows) — A: {'CARRIER_PROPAGATION': 6, 'CODEX_SOLE_ENGINE': 8, 'DOC_HYGIENE': 8, 'LIFECYCLE_GATE_PENDING': 1, 'NONE': 20, 'SHELL_REDESIGN': 2, 'UNRECORDED_JUDGMENT': 1}; B: {'A2_TOPOLOGY': 1, 'CODEX_SOLE_ENGINE': 2, 'DOC_HYGIENE': 6, 'NONE': 31, 'PRE_V3_DRIFT': 5}

**ClaimType** (rows) — A: {'ACCEPTANCE': 4, 'CONTEXT_CLAIM': 12, 'EXCLUSION': 1, 'REGISTER_DEFECT': 3, 'REQUIREMENT': 22, 'STATE_ASSERTION': 4}; B: {'ACCEPTANCE': 4, 'CONTEXT_CLAIM': 10, 'EXCLUSION': 1, 'REGISTER_DEFECT': 2, 'REQUIREMENT': 19, 'STATE_ASSERTION': 9}

**AuthorityTier** (rows) — A: {'GOVERNANCE_INVARIANT': 19, 'LOCAL_DESIGN': 11, 'NOT_APPLICABLE': 16}; B: {'GOVERNANCE_INVARIANT': 21, 'LOCAL_DESIGN': 10, 'NOT_APPLICABLE': 14}

**Confidence** (rows) — A: {'HIGH': 21, 'LOW': 2, 'MEDIUM': 23}; B: {'HIGH': 20, 'LOW': 1, 'MEDIUM': 24}

## 4. Reverse Response agreement

- A sha256 `4c72d681609a8d7152313dc7fa638fd5bfb0ff6eb4b08760a5144e0d58b1133a`; B sha256 `cb29912d117c9952fafaaff569a500b017c8d1986b19eb01cbce68560f6eda61`
- Capabilities answered by both: 452
- Exact Response agreement: 438/452 (97%)
- Coarse agreement (mine vs NOT_MINE): 438/452 (97%)
- Same claiming base key where both CLAIMED_BY/PARTIAL agree: 9/9
- Response histogram A: {'NOT_MINE': 433, 'PARTIAL': 19}; B: {'NOT_MINE': 439, 'PARTIAL': 13}

## 5. Every disagreement, both readings

### 5.1 Forward fields

| Base key | Field | A reading | B reading |
|---|---|---|---|
| DEL-01-03#CLM-004 | Disposition | PARTIALLY_IMPLEMENTED | ALIGNED |
| DEL-01-03#CLM-004 | CauseTag | CODEX_SOLE_ENGINE | NONE |
| DEL-01-03#CLM-005 | ClaimType | REQUIREMENT | STATE_ASSERTION |
| DEL-01-03#CLM-008 | CauseTag | CARRIER_PROPAGATION | PRE_V3_DRIFT |
| DEL-01-03#CLM-009 | Disposition | ALIGNED / AUTHORITY_CONFLICT / DOCUMENTED_UNIMPLEMENTED / PARTIALLY_IMPLEMENTED | ALIGNED / AUTHORITY_CONFLICT |
| DEL-01-03#CLM-009 | CauseTag | CODEX_SOLE_ENGINE / DOC_HYGIENE / NONE / SHELL_REDESIGN | CODEX_SOLE_ENGINE / NONE |
| DEL-01-03#CLM-011 | CauseTag | CARRIER_PROPAGATION | PRE_V3_DRIFT |
| DEL-01-03#CLM-012 | ClaimType | REQUIREMENT | STATE_ASSERTION |
| DEL-01-03#CLM-012 | CauseTag | CARRIER_PROPAGATION | PRE_V3_DRIFT |
| DEL-01-03#CLM-016 | ClaimType | REQUIREMENT | STATE_ASSERTION |
| DEL-01-03#CLM-016 | CauseTag | CARRIER_PROPAGATION | PRE_V3_DRIFT |
| DEL-01-03#CLM-017 | Disposition | PARTIALLY_IMPLEMENTED | ALIGNED |
| DEL-01-03#CLM-017 | CauseTag | UNRECORDED_JUDGMENT | NONE |
| DEL-01-03#CLM-019 | ClaimType | REQUIREMENT | STATE_ASSERTION |
| DEL-01-03#CLM-019 | CauseTag | CARRIER_PROPAGATION | PRE_V3_DRIFT |
| DEL-01-03#CLM-020 | CauseTag | CARRIER_PROPAGATION | DOC_HYGIENE |
| DEL-01-03#CLM-022 | Disposition | PARTIALLY_IMPLEMENTED | ALIGNED |
| DEL-01-03#CLM-022 | CauseTag | LIFECYCLE_GATE_PENDING | NONE |
| DEL-01-03#CLM-024 | CauseTag | CODEX_SOLE_ENGINE | A2_TOPOLOGY |
| DEL-01-03#CLM-026 | ClaimType | CONTEXT_CLAIM | REQUIREMENT |
| DEL-01-03#CLM-026 | Disposition | NOT_AUDITABLE | ALIGNED |
| DEL-01-03#CLM-026 | AuthorityTier | NOT_APPLICABLE | GOVERNANCE_INVARIANT |
| DEL-01-03#CLM-027 | AuthorityTier | LOCAL_DESIGN | GOVERNANCE_INVARIANT |
| DEL-01-03#CLM-029 | ClaimType | CONTEXT_CLAIM | REQUIREMENT |
| DEL-01-03#CLM-029 | Disposition | NOT_AUDITABLE | ALIGNED |
| DEL-01-03#CLM-029 | AuthorityTier | NOT_APPLICABLE | GOVERNANCE_INVARIANT |
| DEL-01-03#CLM-031 | ClaimType | REQUIREMENT | STATE_ASSERTION |

### 5.2 Reverse responses

| CapabilityID | A | B |
|---|---|---|
| CAP-BUILD-018 | NOT_MINE  | PARTIAL DEL-01-03#CLM-009.1 |
| CAP-HARNESS-040 | PARTIAL DEL-01-03#CLM-009.4 | NOT_MINE  |
| CAP-HARNESS-053 | PARTIAL DEL-01-03#CLM-009.8 | NOT_MINE  |
| CAP-ROUTES-044 | PARTIAL DEL-01-03#CLM-009.2 | NOT_MINE  |
| CAP-RTCONTRACT-019 | PARTIAL DEL-01-03#CLM-024 | NOT_MINE  |
| CAP-SETTINGS-007 | PARTIAL DEL-01-03#CLM-009.3 | NOT_MINE  |
| CAP-SHELL-008 | PARTIAL DEL-01-03#CLM-009.1 | NOT_MINE  |
| CAP-SHELL-009 | NOT_MINE  | PARTIAL DEL-01-03#CLM-009.1 |
| CAP-SHELL-012 | PARTIAL DEL-01-03#CLM-009.1 | NOT_MINE  |
| CAP-SHELL-037 | NOT_MINE  | PARTIAL DEL-01-03#CLM-009.5 |
| CAP-SHELL-038 | PARTIAL DEL-01-03#CLM-009.5 | NOT_MINE  |
| CAP-WOVEN-033 | NOT_MINE  | PARTIAL DEL-01-03#CLM-009.3 |
| CAP-WOVEN-035 | PARTIAL DEL-01-03#CLM-009.6 | NOT_MINE  |
| CAP-WOVEN-042 | PARTIAL DEL-01-03#CLM-009.6 | NOT_MINE  |

## 6. Run-local rows (not key-comparable)

| Worker | Key | ClaimType | Disposition | CauseTag | DeclaredState (first 90 chars) |
|---|---|---|---|---|---|
| A | DEL-01-03#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | REF-002 CONTRACT, REF-003 SPEC, REF-006 PRD recorded MATCH with ExpectedSHA256 = ActualSHA |
| A | DEL-01-03#REGISTER-2 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | Dependency rows SATISFIED on the basis that _REFERENCES.md now records REF-006 (and REF-00 |
| A | DEL-01-03#REGISTER-3 | REGISTER_DEFECT | REMAINING_STATE_MISMATCH | DOC_HYGIENE | Authorization Basis: D-APP-19 Option D ruling 2026-06-20; Checking Approval SHA 8c6d55d3 |
| A | DEL-01-03#STATE-1 | STATE_ASSERTION | AUTHORITY_CONFLICT | CODEX_SOLE_ENGINE | _CONTEXT.md:48: Claude Agent SDK / Anthropic remains the first concrete/current path; Pi i |
| A | DEL-01-03#STATE-2 | STATE_ASSERTION | STALE_SPECIFICATION | DOC_HYGIENE | BOUNDARY_REVIEW_CHECKLISTS.md:9 and :78: REF-006 docs/PRD.md currently MATCH |
| A | DEL-01-03#STATE-3 | STATE_ASSERTION | AUTHORITY_CONFLICT | CODEX_SOLE_ENGINE | BOUNDARY_REVIEW_CHECKLISTS.md:25: absent an owner provider configuration, the Anthropic ke |
| B | DEL-01-03#REGISTER-1 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | REF-002 docs/CONTRACT.md, REF-003 docs/SPEC.md, REF-006 docs/PRD.md: ActualSHA256 = Expect |
| B | DEL-01-03#REGISTER-2 | REGISTER_DEFECT | STALE_SPECIFICATION | DOC_HYGIENE | DEP-01-03-011: '_REFERENCES.md now records REF-006 MATCH under the current D-APP-38 corpus |
| B | DEL-01-03#STATE-1 | STATE_ASSERTION | ALIGNED | NONE | IN_PROGRESS; ## Remaining empty; D-APP-108 copy-table note recorded as offered, not adopte |
| B | DEL-01-03#STATE-2 | STATE_ASSERTION | AUTHORITY_CONFLICT | CODEX_SOLE_ENGINE | 'Claude Agent SDK / Anthropic remains the first concrete/current path; Pi is pattern corpu |
| B | DEL-01-03#STATE-3 | STATE_ASSERTION | ALIGNED | NONE | Dated decision and evidence log; 2026-09-04: ScopeOfWork.md keeps its earlier pin and carr |

## 7. Row-level agreement where both split a key identically

- ClaimType: 10/10 sub-rows agree across 1 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- Disposition: 2/10 sub-rows agree across 1 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- AuthorityTier: 10/10 sub-rows agree across 1 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)
- CauseTag: 2/10 sub-rows agree across 1 identically split keys (sub-row numbering is worker-local; low agreement here may reflect different split boundaries)

## 8. Strict agreement on keys neither worker split

Keys unsplit by both: 30.

| Field | Agreement |
|---|---|
| ClaimType | 23/30 (77%) |
| Disposition | 25/30 (83%) |
| AuthorityTier | 27/30 (90%) |
| CauseTag | 20/30 (67%) |
| ALIGNED vs non-ALIGNED | 25/30 |

## 9. Brief-required measures (PKG-01 dispatch direction)

- **Disposition agreement overall** (exact value-set per indexed base key): 25/31. Comparators: DEL-06-02 19/35 (before the Addendum 5 tie-break); DEL-05-02 24/33.
- **STALE_SPECIFICATION vs REMAINING_STATE_MISMATCH splits:** pure SS/RSM splits (both readings only SS/RSM, and they differ) 0: []; other disagreements involving SS or RSM on one side 0: []; agreement on keys where either worker used SS or RSM 9/9.
- Disposition disagreements not involving SS/RSM: 6: ['DEL-01-03#CLM-004', 'DEL-01-03#CLM-009', 'DEL-01-03#CLM-017', 'DEL-01-03#CLM-022', 'DEL-01-03#CLM-026', 'DEL-01-03#CLM-029']
- **HumanDecisionNeeded agreement** (full token set per base key): 29/31; **R4/R4-Qn token agreement** (R4* tokens only): 29/31; on keys where either cited an R4 token: 0/2.
- R4 token counts over indexed base keys — A: {'R4-Q1': 2}; B: {'R4': 1, 'R4-Q1': 1, 'R4-Q5': 1}

| Base key | A HumanDecisionNeeded | B HumanDecisionNeeded |
|---|---|---|
| DEL-01-03#CLM-009 | NO; R4-Q1 | NO; R4-Q1; R4-Q5 |
| DEL-01-03#CLM-024 | R4-Q1 | R4 |

## 10. Reading (hand-written by the PKG-01 manager; agent measurement, not a ruling)

- **Rule stage.** A and B received the same brief (`BRIEFS/WORKER_BRIEF.md`, carrying the Addendum 5 and
  Addendum 6 texts verbatim) in the same dispatch round. Their pass-2 messages were identical except for the
  folder and seal values, and both received the same 10 capability files (the union of both ledgers' areas).
  Neither worker received HELP_HUMAN's `OTHER:V3_ROLE_ADOPTION` note or the Addendum 6 rule-3 clarification
  before sealing: both had already sealed, so the stage was identical.
- **Disposition agreement 25/31 (81%)** on indexed base keys, against DEL-06-02's 19/35 (54%; before the
  Addendum 5 tie-break) and DEL-05-02's 24/33 (73%).
  - **No split falls between STALE_SPECIFICATION and REMAINING_STATE_MISMATCH.** Both workers agree on all 9
    keys where either used SS or RSM. The Addendum 5 tie-break appears to have closed the DEL-06-02 variance
    source for this deliverable.
  - **All 6 Disposition disagreements are about how much of the claim is met.**
    - A reads 4 as PARTIALLY_IMPLEMENTED or DOCUMENTED_UNIMPLEMENTED where B reads ALIGNED: CLM-004, CLM-017
      (no boundary review record for the shipped v3.0.x release), CLM-022, and the CLM-009 sub-rows.
    - On CLM-026 and CLM-029, A reads a CONTEXT_CLAIM (NOT_AUDITABLE) where B reads a REQUIREMENT (ALIGNED).
  - **CLM-009 sub-rows (REQ-01..10).** Both workers split them identically, but agree on the Disposition of
    only 2 of 10 sub-rows. A found missing live copy for REQ-01 (governed-work posture), REQ-04 (draft notice)
    and REQ-06 (runtime records are not approvals); B judged these ALIGNED.
- **A factual disagreement for R3 (reach, not interpretation).**
  - A's erratum on CLM-009.2 says the "Anthropic API Key" settings panel is reachable live, because the 404
    page (`not-found.tsx`) renders the legacy ShellFrame.
  - B's erratum on the same row says the panel is never rendered.
  - V-DEL-01-03_A CONFIRMED A's erratum, and B's ledger is not verified. The capability file
    (CAP-SETTINGS-009, STATE=DISABLED) misses the 404 path, according to A.
- **HumanDecisionNeeded 29/31.** R4 tokens agree on 0 of the 2 keys where either worker cited one.
  - On CLM-009, B adds R4-Q5 for the live "Codex" notification tab.
  - On CLM-024, A cites R4-Q1 and B cites plain R4. Both mark the row AUTHORITY_CONFLICT against the
    unamended DIRECTIVE §2.8.
  - On the run-local rows, both workers independently raised AUTHORITY_CONFLICT on `_CONTEXT.md` "Claude
    Agent SDK / Anthropic remains the current path" (A STATE-1, B STATE-2).
- **Metadata columns.** CauseTag 20/31 (65%). The main split is CARRIER_PROPAGATION (A) against PRE_V3_DRIFT
  (B) on the stale dependency and TBD text (CLM-008, 011, 012, 016, 019). That matches the R0 finding that cause precedence is
  weakly reproducible. ClaimType 24/31: B reads SoW state prose as STATE_ASSERTION where A reads it as
  REQUIREMENT.
- **Reverse Response agreement 438/452 (97%).** Where both workers answered PARTIAL, they named the same base
  key 9/9 times.
