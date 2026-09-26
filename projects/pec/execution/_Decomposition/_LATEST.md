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
  `_Evaluation/DecompCoverage/COV_SCA005_POSTSETUP_2026-09-25_1606/`, which
  the audit folder's `_LATEST.md` names: `WARNINGS`, 0 blockers / 3
  warnings / 70 info, run after PROJECT_SETUP created DEL-02-08/09 and
  applied the dependency rerun under `D-PEC-93`. The three warnings are
  pre-existing (v2 artifacts held outside their deliverable folders). Its
  INFO findings COV-068/069 (context and reference pins), COV-072
  (evidence-quote currency) and COV-073 (stale handoff text) were addressed
  on 2026-09-25 under `D-PEC-95` without a further audit. The checkpoint-3 audit
  `COV_SCA005_POSTCHANGE_2026-09-25_1344/` is superseded.
- **Scope-change snapshot:** `_ScopeChange/SCA-005_2026-09-23_2139/`.
- **Derivative state:** `INCOMPLETE`; `DownstreamRerunState = IN_PROGRESS`;
  `MetadataAlignmentState = COMPLETE`; `ReadyForNextPhase = NO`. Done under
  their own packets: DEL-02-08/09 preparation with the dependency rerun, the
  re-audit and the audit-pointer move (`D-PEC-93`; closeout
  `_Coordination/PROJECT_SETUP_SCA005_A4_B3_2026-09-25/HANDOFF_STATE.md`);
  context and reference re-pinning and the evidence-quote refresh
  (`D-PEC-95`). `projects/pec/AGENTS.md` names PRD v2.3 and the D-GOV-43
  Runtime boundary since `D-PEC-94`. Open, each separately gated: SOW
  currency, derivative-artifact review, the registry source packet,
  fixtures and the D-PEC-90 reliance amendment; TM-PEC-023's state is in
  the Task Management register. Undertaking
  `HELP-HUMAN-PEC-20260925-POST-SCA005` plans the open items in
  `_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`.
  The SCA-004 downstream repairs closed on 2026-08-09
  (`_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md`).
- **Authority fence:** no downstream repair, source, lifecycle beyond the
  four accepted retirements, artifact acceptance, release, professional
  reliance, or foreign-loop duty is implied by this pointer.
