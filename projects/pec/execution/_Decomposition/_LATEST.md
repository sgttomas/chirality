# Latest — revision pointer and handoff state

Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.5**
(**`current_basis`** — accepted 2026-09-25 as the SCA-005 successor under
the owner's checkpoint-group-3 audited-poststate acceptance; group-2
exact amendment and propagation plan accepted the same day, register row
`D-PEC-92`).

## Handoff state

- **Basis:** accepted PRD v2.3 (adopted 2026-09-25 through SCA-005
  checkpoint group 2); D-PEC-60 SOFTWARE_DECOMP revision 1.0; SCA-001
  directed bootstrap; SCA-002 objective mapping; SCA-003 consumer
  interface/ADR-014 concordance; SCA-004 loop-registry disposition; SCA-005
  feed-model rebaseline.
- **Package:** `SOFTWARE_DECOMP.md` revision 1.5 + `ScopeLedger.csv` +
  `Deliverables.csv` + `ContextBudgetQA.csv` + `Companion_Inventory.csv`,
  each equal to its accepted SCA-005 candidate.
- **Basis integrity:** decomposition SHA-256
  `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660`;
  Scope Ledger SHA-256
  `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df`;
  Deliverables SHA-256
  `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a`;
  `docs/PRD.md` SHA-256
  `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32`.
- **Semantic result:** feed model O-B2 with presence P-β; 96 scope items
  (`70 IN / 18 OUT / 8 TBD`), 11 packages, 66 deliverable rows (62 active,
  4 retired: DEL-06-04, DEL-07-02, DEL-07-04, DEL-07-05), six objectives,
  every IN item and active deliverable mapped to an objective; 10 open / 3
  resolved issues.
- **Closure verdict:** `CLOSED_FOR_SCOPE_CHANGE_ONLY` (owner Q-CP3-1 (a)).
- **Audit:**
  `_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/`;
  `BLOCKERS` by the method's count rule (2 / 6 / 74). Both blockers are the
  absent DEL-02-08/09 folders, an expected consequence of the owner's
  deferral of Lane A4; excluding expected consequences, 0 blockers / 4
  warnings. The audit folder's own `_LATEST.md` still names the SCA-004
  audit; moving it was not part of this act.
- **Scope-change snapshot:** `_ScopeChange/SCA-005_2026-09-23_2139/`.
- **Derivative state:** `INCOMPLETE`; `DownstreamRerunState = FROZEN`;
  `MetadataAlignmentState = IN_PROGRESS`; `ReadyForNextPhase = NO`. The
  SCA-004 downstream repairs closed on 2026-08-09
  (`_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md`).
  Open SCA-005 work, each separately gated, is listed in the SCA-005
  `Handoff_State.md` and `RUN_SUMMARY.md`: DEL-02-08/09 preparation with
  the dependency rerun (PROJECT_SETUP, own packet), context and reference
  re-pinning, SOW currency, derivative-artifact review, the registry source
  packet, fixtures, and the D-PEC-90 reliance amendment.
- **Authority fence:** no downstream repair, source, lifecycle beyond the
  four accepted retirements, artifact acceptance, release, professional
  reliance, or foreign-loop duty is implied by this pointer.
