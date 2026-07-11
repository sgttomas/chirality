# R2 Wave-1 Notes — DEL-02-02 Workbench and Pipeline Selection UX

- **Run:** `RUN_D55_CONCORDANCE_2026-07-11_1904Z` (D-APP-55, Option A), Wave 1 / PKG-02
- **Deliverable:** DEL-02-02, PKG-02 Desktop Shell, Navigation, and Operator State
- **Source state:** `frontend/` at `fac46e33f` (byte-identical to `4c8ed8907` / `61d70bdb0`); behavioral binding via `GATE-TRANSCRIPT(W1@fac46e33f)` (typecheck exit 0; Vitest 667 passed / 4 skipped)
- **Method:** pinned plan §§6-7 @ `551f84ef6`; `R2_METHOD_ADDENDUM.md` MR-1..MR-11; run-local `AUTHORITY_MAP.md`

> Epistemic status: evidence artifact, not authority. Dispositions are agent classifications for human review; every human-owned decision is flagged, not made.

## 1. Claim census

20 claim rows.

By ClaimType: REQUIREMENT 11; EXCLUSION 3; ACCEPTANCE 2; IMPLEMENTED_UNMAPPED 2; REMAINING_WORK 1; REGISTER_DEFECT 1.

By Disposition:

| Disposition | Count | Rows |
|---|---:|---|
| ALIGNED | 14 | REQ-001/003/004/005/006/007/008/009/010/011, EXC-001, EXC-003, ACC-002, REMAINING-1 |
| STALE_SPECIFICATION | 3 | REQ-002 (PRD/TYPES pre-pivot routing text), EXC-002 (dependency-deferral wording vs live 9-row register), ACC-001 (PRD hash-mismatch condition vs _REFERENCES MATCH) |
| IMPLEMENTED_UNDOCUMENTED | 2 | UNMAPPED-1 (execution-root scaffolding UI), UNMAPPED-2 (Pipeline contract/transition panel) |
| REMAINING_STATE_MISMATCH | 1 | REGISTER-1 (_DEPENDENCIES.md internal contradiction) |

Derived summary (not a deliverable verdict): the deliverable's four-document kit and implementation/tests agree for every behavioral requirement. Discordant surfaces are (a) the 2026-06-20 INSP-03 assessment (three PARTIAL ratings now overtaken), (b) pre-pivot routing wording still standing in the RATIFIED PRD §7.2/FR-008 and TYPES §4.1 (the same corpus text DEL-02-01 REQ-007/008 flagged), and (c) run-scoped kit statements (dependency-deferral, PRD hash warning) overtaken by later ruled work.

Notable assessment movement since INSP-03: REQ-004's two PARTIAL causes are both closed at `fac46e33f` — `workbench-surface.test.ts` now exists with an unsupported-agent read-only render test plus human-gated approval-SHA/actor-lock assertions (satisfying the D-APP-36 component/render-test bar), and Specification.md line 28 now names `canAgentTransitionLifecycle` as the implementation source (no longer "TBD registry").

## 2. Least-confident rows (mandatory self-flag) + the reading that would flip them

- **REQ-002 → STALE_SPECIFICATION (MEDIUM).** Flip reading: **ALIGNED.** The DEL-02-02 kit wording, implementation, and tests are loop-first-correct; the only stale artifact is the upstream PRD §7.2/FR-008 + TYPES §4.1 "open WORKBENCH" text, which is a corpus-amendment already owned by DEL-02-01 REQ-007/008. I followed the R0 exemplar precedent (identical PRD/TYPES text → STALE_SPECIFICATION routed to the corpus packet) rather than marking ALIGNED and deferring the upstream text entirely to DEL-02-01. A reviewer preferring no double-count would mark ALIGNED with a cross-reference note.
- **EXC-002 → STALE_SPECIFICATION (HIGH, but scope-boundary nuance).** Flip reading: **ALIGNED.** The Specification "Excluded" bullet, read as a scope boundary ("this UX slice performs no dependency extraction"), is still true. The disposition is STALE because the Datasheet/Procedure *declared-state* wording ("extraction deferred / Dependencies.csv not produced") is flatly false against the live 9-row register (MR-8). Directly parallel to R0 exemplar DEL-02-01-EXC-004.
- **EXC-003 → ALIGNED (MEDIUM).** Flip reading: **AUTHORITY_CONFLICT.** `_CONTEXT.md` lists SOW-007 under DEL-02-02 while the decomposition scope ledger marks PKG-08/DEL-08-03 as primary; two live surfaces touch the same scope item. I did not raise AUTHORITY_CONFLICT because "primary" leaves room for a UI-vs-dispatch split and the deliverable's own Guidance CONFLICT-003 + exclusion encode that split (compatible, pending ruling). HumanDecisionNeeded=NEW-PACKET carries the unresolved ownership question; a stricter reader could call it a live normative conflict.
- **UNMAPPED-2 → IMPLEMENTED_UNDOCUMENTED (MEDIUM).** Flip reading: **fold into REQ-003/004 as ALIGNED.** The Pipeline surface's deliverable-contract + transition panel duplicates the Workbench capability (REQ-003/004) rather than a wholly new behavior; it may be intended shared contract-review UI already understood as inside the "contract APIs" scope. Recorded as unmapped because no DEL-02-02 requirement scopes deliverable-contract review or lifecycle transitions to PIPELINE (only WORKBENCH).
- **UNMAPPED-1 → IMPLEMENTED_UNDOCUMENTED (MEDIUM).** Flip reading: out-of-scope-for-this-deliverable / belongs elsewhere. The scaffold-execution-root UI (`scaffoldHarnessExecutionRoot`, DECOMP BASE create-new) may be a PKG-00/PKG-08 harness feature that merely renders on the Pipeline surface; if so it is another deliverable's claim, not DEL-02-02's. Recorded here because it is material live behavior on this deliverable's named surface with no requirement mapping (plan §6).
- **REQ-010 → ALIGNED (MEDIUM).** Flip reading: **STALE_VERIFICATION.** The governance-negative property ("no UI state overrides project truth") is documentary; no named test asserts the negative. Marked ALIGNED because the positive evidence (summaries sourced only from contract routes; writes only through the governed transition endpoint) holds and INSP-03 rated it PASS.

All six non-ALIGNED-or-flagged rows above, plus every STALE_SPECIFICATION / IMPLEMENTED_UNDOCUMENTED / REMAINING_STATE_MISMATCH row, are offered for fan-in recheck.

## 3. Register-defect summary

- **REGISTER-1 (REMAINING_STATE_MISMATCH, HIGH):** `_DEPENDENCIES.md` contradicts itself — Declared Upstream (line 14) and Declared Downstream (line 18) say "no accepted dependency edges have been extracted yet," while the same file's Extracted Dependency Register (lines 33-47) and Run History (line 53) list 9 ACTIVE rows, matching the live `Dependencies.csv` (9 rows) and DepClosure D53A coverage `DEL-02-02,Y,9,Y,Y`. Repair is a `_DEPENDENCIES.md` prose update.

One dependency-currency observation NOT raised as a register-defect row (recorded here per the R0 exemplar's practice): all 9 `Dependencies.csv` rows carry `SatisfactionStatus=TBD` / `ProposedMaturity=TBD`, including EXECUTION rows whose targets are live-verified at `fac46e33f` (DEP-02-02-005 matrix routing → DEL-02-01; DEP-02-02-007/008 status/dependency APIs consumed by `workbench-surface.tsx`). This is the un-reconciled baseline (DepClosure `Y,9,Y,Y` certifies presence/schema, not satisfaction closure), consistent with the deliberately-open residual model, not a defect. Flagged for R3 in case a corpus-wide satisfaction-closure sweep is warranted.

## 4. Cross-reference / decision duties (MR-7)

- **D-APP-28/30/31** govern REQ-002 (loop-first routing supersession); cited as governing.
- **D-APP-36** governs REQ-004 (component/render-test bar for PKG-02 UI); the added `workbench-surface.test.ts` meets it. Context on UNMAPPED-2 (a Pipeline transition render test would be needed if that panel is adopted).
- **D-APP-35 / D-APP-38** govern ACC-001 (PRD hash refresh + versioned corpus v6 → REF-006 MATCH).
- **D-APP-53** context on EXC-002 and REGISTER-1 (dep reconciliation baseline).
- **No ruling found** naming SOW-007 ownership (EXC-003) — routed as NEW-PACKET, not decided here.
- Dependency/reference registers checked against the live tree: `Dependencies.csv` (9 rows) present and schema-valid; `_REFERENCES.md` all 7 refs MATCH (REF-006 now MATCH, contra the Datasheet/Guidance/Assessment hash-mismatch wording → ACC-001).

## 5. Post-fan-in corrections (2026-07-11, verifier-prompted, agent-verified and applied)

All 9 rechecked dispositions were CONFIRMED at fan-in; no disposition changed. Three evidence-cell corrections were applied after independently re-verifying the verifier's facts:

- **ACC-002 VerificationEvidence (defect fixed):** the original cell cited an `execution/_Coordination/WORKSPACE_MANIFEST.csv` row for DEL-02-02. Re-verified live: that file's schema is `Surface,Path,Role` and contains zero deliverable rows — the citation was factually wrong. Cell rewritten to `RUN-INSPECTION@fac46e33f` binding the valid elements (unique live folder path + `_CONTEXT.md` Identity block). Disposition ALIGNED unchanged.
- **EXC-001 and EXC-003 VerificationEvidence (token normalization):** free-text "Document/scope claim" phrasing prefixed with the MR-10 controlled token `RUN-INSPECTION@fac46e33f`; existing citations retained. Dispositions unchanged.
- **UNMAPPED-1 RemainingWork (candidate added, concurred):** PKG-07/DEL-07-02 Execution Root Scaffolding added to the candidate-owner list — re-verified that its Specification.md line 17 excludes "UI presentation beyond the scaffold API result surface," which both confirms the scaffold UI layer is currently unowned and makes DEL-07-02 the natural adjacency.

## 6. Method deviations

None. Datasheet restatements folded into REQ rows (MR-4); only datasheet-distinct conditions emitted as ACCEPTANCE rows (ACC-001 source warning, ACC-002 dispatch-path warning). No `DEFERRED_AGENT_WORKFLOW` row was required: the SOW-007 overlap (EXC-003) is a product scope/ownership question, not an agent-instruction or workflow-contract change. No test suites executed; behavioral evidence bound via `GATE-TRANSCRIPT(W1@fac46e33f)` plus named test cases (MR-3). No `AUTHORITY_CONFLICT` raised (see §2 EXC-003 nuance). No human decision represented as a ruling.
