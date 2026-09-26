# Latest — revision pointer and handoff state

Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.6**
(**`current_basis`** — accepted 2026-09-26 as the SCA-006 successor under
the owner's checkpoint-group-3 audited-poststate acceptance; group-2
exact amendment and propagation plan accepted 2026-09-25, register row
`D-PEC-97`).

## Handoff state

- **Basis:** accepted PRD v2.4 (adopted 2026-09-25 through SCA-006
  checkpoint group 2, settled at checkpoint 3 on 2026-09-26); D-PEC-60
  SOFTWARE_DECOMP revision 1.0; SCA-001 directed bootstrap; SCA-002
  objective mapping; SCA-003 consumer interface/ADR-014 concordance; SCA-004
  loop-registry disposition; SCA-005 feed-model rebaseline; SCA-006
  operational reliance on PEC data (`D-PEC-90` R-A).
- **Package:** `SOFTWARE_DECOMP.md` revision 1.6 + `ScopeLedger.csv` +
  `Deliverables.csv` + `ContextBudgetQA.csv` + `Companion_Inventory.csv`,
  at the hashes accepted in
  `_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-3_2026-09-26/ACCEPTED_MANIFEST.csv`.
- **Basis integrity:** decomposition SHA-256
  `9374c21fb87b02e5f842af9407caf65690d73f3067f86ce6c7dba0a3a7908eb1`;
  Scope Ledger SHA-256
  `1d24a4b86f05dc6fd57028c08e202d33f9f317b148821f9c61246c6e91ee916e`;
  Deliverables SHA-256
  `94ee5d182ae99092324505a72bf2f3b0581f85c0bae6c693214cfef709179805`;
  `docs/PRD.md` SHA-256
  `ae49b8065698f003001b2183f550b814cded5cd5ea06f940b81dd5c287483fbe`.
- **Semantic result:** operational reliance within the declared pin,
  coverage and tier (C3 re-expressed; PEC output stays never citable as
  authority); 100 scope items (`74 IN / 18 OUT / 8 TBD`), 11 packages, 68
  deliverable rows (64 active, 4 retired: DEL-06-04, DEL-07-02, DEL-07-04,
  DEL-07-05), six objectives, every IN item and active deliverable mapped
  to an objective; 10 open / 3 resolved issues. New in revision 1.6:
  SOW-097..100 and the register rows DEL-08-06 and DEL-10-13 (no folders
  yet; SCA-006 Lane B1).
- **Closure verdict:** `CLOSED_FOR_SCOPE_CHANGE_ONLY` (owner acceptance of
  2026-09-26).
- **Audit:**
  `_Evaluation/DecompCoverage/COV_SCA006_POSTCHANGE_2026-09-26_0051/`, which
  the audit folder's `_LATEST.md` names (owner Q-CP3-2 (a)): `WARNINGS`,
  0 blockers / 3 pre-existing warnings / 71 info / 12 expected
  consequences, run on the pre-acceptance form of the same poststate. The
  three warnings are pre-existing (v2 artifacts held outside their
  deliverable folders). COV-083 (the `remaining-loop` design text in
  SOW-094, the DEL-01-06 Description and the §9 example) is carried
  knowingly for a later PEC scope change (owner Q-CP3-1 (a)).
- **Scope-change snapshot:** `_ScopeChange/SCA-006_2026-09-25_1912/`.
- **Derivative state:** `INCOMPLETE`; `DownstreamRerunState = FROZEN`;
  `MetadataAlignmentState = IN_PROGRESS`; `ReadyForNextPhase = NO`. The
  three direct `_CONTEXT.md` mirrors were written with the amendment;
  `projects/pec/AGENTS.md` carries the SCA-006 instruction tranche. Open,
  each separately gated (SCA-006 `RUN_SUMMARY.md` §6): B1 folders for
  DEL-08-06 and DEL-10-13, B2 and B3 dependency work, B4 SOW currency, B5
  the DEL-00-03 SPEC premise, B6 the tier-0 profile entry, B7 the
  revision-1.6 re-pin, B8 the API schema fields, and the COV-083
  correction. Undertaking `HELP-HUMAN-PEC-20260925-POST-SCA005` plans the
  open items in
  `_Coordination/WorkGraphs/HELP-HUMAN-PEC-20260925-POST-SCA005/WORK_GRAPH.md`.
- **Authority fence:** no downstream repair, source, lifecycle beyond the
  four accepted retirements, artifact acceptance, release, professional
  reliance, or foreign-loop duty is implied by this pointer.
