# DEL-00-01 — forward-pass notes (R2, PKG-00)

Ledger: `DEL-00-01_claims.csv`, 41 rows. Validator: `RESULT PASS errors=0 warnings=0`.
Sealed SHA-256: `d87cf0978d2f2d9b4a0db7b43ad5f0fac97db963b136f8b96778e762fb815209`.

## 1. Census

| ClaimType | ALIGNED | STALE_SPECIFICATION | NOT_AUDITABLE | DOCUMENTED_UNIMPLEMENTED | REMAINING_STATE_MISMATCH | Total |
|---|---:|---:|---:|---:|---:|---:|
| REQUIREMENT | 14 | 4 | 0 | 0 | 0 | 18 |
| STATE_ASSERTION | 4 | 5 | 0 | 0 | 0 | 9 |
| CONTEXT_CLAIM | 0 | 0 | 7 | 0 | 0 | 7 |
| ACCEPTANCE | 2 | 1 | 0 | 1 | 0 | 4 |
| REGISTER_DEFECT | 0 | 1 | 0 | 0 | 1 | 2 |
| EXCLUSION | 1 | 0 | 0 | 0 | 0 | 1 |
| **Total** | **21** | **11** | **7** | **1** | **1** | **41** |

- Indexed units: 26, all covered. Run-local rows: 4 (`REGISTER-1`, `REGISTER-2`, `STATE-1`, `STATE-2`).
- Split rate: 4 of 26 units split (15%). The splits are CLM-009 into 8 rows (a REQ table), CLM-010 into 3 (a standards table whose rows take different dispositions), CLM-012 into 2 (prose plus AC-001) and CLM-018 into 2 (prose plus VER-001). CLM-011 (the verification table) and CLM-016 (numbered steps) were not split: only one row or step of each is defective.
- SEE rows (MR-4), counted separately: 8, all `SEE:DEL-00-01#CLM-003`: CLM-009.1, CLM-010.2, CLM-011, CLM-015, CLM-016, CLM-022, REGISTER-1 and STATE-1. Excluding them leaves 33 rows, of which 3 are STALE_SPECIFICATION (CLM-003, CLM-025, STATE-2).
- No errata file yet (pass 1).
- Confidence: 36 HIGH, 4 MEDIUM, 1 LOW.
- R4-Qn counts: 0. HumanDecisionNeeded is `NO` on every row. No code evidence was cited, so no REACH tags apply and no R4-Q1 citations follow.
- PostReleaseBasis: `NO` on every row. No cited file appears in pack item 1 (`TOUCHED_PATHS.csv` has no PKG-00 or DepClosure paths).

## 2. Least-confident rows

- **DEL-00-01#CLM-018.2 (VER-001), LOW, DOCUMENTED_UNIMPLEMENTED.** The evidence roots hold no claim map, parity report or checklist for DEL-00-01. The SOW-v1 migration commits `7f1b8f746` and `bbe25006f` touch only the SoW and the four retired documents. *Alternative:* the migration's parity output was produced by a Root tool outside the evidence roots, which would make the row `UNKNOWN`. The D-APP-55 and D-APP-68 concordance records also partly serve as claim mapping.
- **CLM-011, MEDIUM.** The verification table is judged `STALE_SPECIFICATION` as a whole because its REQ-001 row verifies a now-false "current" fact. The other rows pass. *Alternative:* split per REQ, giving 7 ALIGNED rows and 1 stale row.
- **CLM-012.2 (AC-001), MEDIUM, ALIGNED.** Preservation is judged from the CLM-block structure and the commit history, not from a byte comparison with the retired Datasheet, Specification, Procedure and Guidance.
- **CLM-021, MEDIUM, ALIGNED.** The principles use pre-ruling conditional wording ("may need conversion") but make no present-fact claim. *Alternative:* STALE_SPECIFICATION, on the same reasoning as CLM-025 and STATE-2.
- **STATE-2, MEDIUM.** The README Working Rule "requiring reconciliation" is read as a present-tense false statement. *Alternative:* a standing rule of thumb, which would make it NOT_AUDITABLE.

## 3. Register-defect summary

- **REGISTER-1** (`_REFERENCES.md`), STALE_SPECIFICATION. REF-007 (D53A) is still marked `CURRENT` and described as the "Current accepted DepClosure snapshot". The accepted pointer is `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034` (D-APP-111), and that snapshot is not listed.
- **REGISTER-2** (`_STATUS.md`), REMAINING_STATE_MISMATCH. `Last Updated` reads 2026-07-12, but the History section has a 2026-07-19 entry (D-APP-68). This is metadata lag only (tie-break rule 2b).
- No MATCH-hash REGISTER rows. Pack item 3 records CONTRACT, SPEC and PRD as `NOT_RECORDED` for this deliverable.
- Not counted as a defect: the `_STATUS.md` header still names D-APP-19 and the Checking Approval SHA. D-APP-54 (`D-APP-54_RULING_2026-07-11.md`, lines 48–54) preserves both as history.

## 4. Direction and cause

- **Main finding.** On 2026-09-05, D-APP-111 moved the DepClosure pointer from D53A to the 1034 snapshot. D-APP-114 then repointed `DAG_CLOSURE_CONTROL.md` only; its scope was "named files only". Every DEL-00-01 carrier still calls D53A the current snapshot: SoW CLM-003, 009 REQ-001, 010, 011, 015, 016 and 022, plus `_REFERENCES.md` REF-007 and `CONTROL.md`. The substance still holds, since the 1034 snapshot is strict acyclic with `scc_count = 0`. Only the pointer name is stale.
  - CauseTag `CARRIER_PROPAGATION`, with `CAUSE2:DOC_HYGIENE`.
  - DirectionEvidence `GOV:D-APP-111; GOV:D-APP-114`.
  - LatestDecision `D-APP-111 (context)`, because neither ruling names DEL-00-01, so MR-11 is not applied.
- **CLM-025 and STATE-2.** Pre-ruling rationale text from May 2026 is still written in the present tense. It says the rationale is "provisional", that decision authority "remains unresolved", and that the rows are PENDING and TBD. This contradicts the six Human-APPROVED rulings (`Ruling_Register.csv`), the CHANGE handoff, and the same SoW's CLM-015 and CLM-022. D-APP-56 P42 (UPD-082) repaired the Considerations and README Source Rows descriptors but not this text.
  - CauseTag `PRE_V3_DRIFT`; DirectionEvidence `NONE_FOUND`.
- **CLM-018.2.** CauseTag `PRE_V3_DRIFT`: the migration dates from 2026-07-13, before 2026-08-22.
- **CONTEXT records used:** none. No RUN_BASIS §5 CONTEXT source addresses PKG-00 or DepClosure pointers.
- **Searches behind each `NONE_FOUND`:**
  - `_REGISTER.md`: grep for DEL-00-01, SCC-002 and the rows D-APP-53, 54, 55, 56, 68, 110, 111 and 114.
  - The RUN_BASIS §5 CONTEXT list: v3 plan and steers, SCA-APP-008, and the `APP_V3_*` and `APPDEV_V3_NODE_*` AgentRuns. They were checked by name for PKG-00 or DepClosure relevance; none applies.
  - AgentRuns, `_Evaluation` and `_Scripts`: grep for DEL-00-01 together with sow, migrat, parity or claim (for VER-001).

## 5. Method friction

- **Owning registers out of bounds.** The PKG-10 `Dependencies.csv` files that the deliverable treats as its source registers are inside another package's deliverable folder, which is outside the evidence roots. Row states were therefore established from in-bounds evidence:
  - the 1034 snapshot's `Evidence/edge_list.csv`, where DEP-10-03-006 is an active edge and DEP-10-02-004 is absent;
  - the historical R6 backcheck (`R6_D55_BACKCHECK_2026-07-12_1903Z/CHANGED_CLAIM_REEXTRACTION.csv` rows UPD-081 and UPD-082, CONFIRMED);
  - the SCC-002 case Ruling_Register.
  - **Accidental read.** One of my greps (`grep -rn … execution/ | grep -v '^./PKG-'`) had a filter that did not match the output's path form. It surfaced a few lines from the PKG-10 deliverable folders (DEL-10-02 and DEL-10-03 `Dependencies.csv`, `_DEPENDENCIES.md` and `Evidence_D53A_*`). No row relies on those lines, and none cites them.
  - *Proposal:* for control packages, allow read-only access to the specific foreign register rows the control deliverable names.
- **Package-level control records.** `DAG_CLOSURE_CONTROL.md`, `CONTROL_REGISTER.csv` and the PKG-00 `README.md` belong to PKG-00 but to no single deliverable. They are cited as evidence only; see the coverage gaps below.
- **REACH.** The deliverable has no code surface, so the REACH and R4-Q1 subject tests had no application.

## Coverage gaps for the manager

These PKG-00 package-level control records have no indexed unit in either DEL-00-* deliverable. All four are stale at the frozen basis:

- `CONTROL_REGISTER.csv` **PKG-00-CTRL-004** (`CURRENT_DEPCLOSURE_SNAPSHOT`) still names `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z` as the accepted current snapshot. It was not moved for either D53A (D-APP-56/68) or the 1034 snapshot (D-APP-111).
- `CONTROL_REGISTER.csv` **PKG-00-CTRL-005/006** (`CONTROL_DELIVERABLE_SEMANTIC_READY`, ACTIVE) and the `DAG_CLOSURE_CONTROL.md` §Control Deliverable Readiness table (lines 33–36) record DEL-00-01 and DEL-00-02 as `SEMANTIC_READY`. `_STATUS.md` records `IN_PROGRESS` (D-APP-54).
- The PKG-00 `README.md` §Current Readiness (lines 23–27) says both control deliverables are `SEMANTIC_READY` and that the work "does not make the strict product graph acyclic". Both statements are now false.
- `DAG_CLOSURE_CONTROL.md:64` (Current Queue) says to "proceed with the D-APP-19 inspection queue". D-APP-54 superseded that convention.

## 6. Effort

- About 30 files read, mostly line ranges: the deliverable folder, the PKG-00 control files, 5 DepClosure snapshots, the D-APP-54 and D-APP-111 ruling records, register rows, and the R6 backcheck rows.
- Git use was read-only `log`, `show --stat` and `show --format` against the frozen tree only.
- The context budget was not tight.
