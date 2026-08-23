# SCA-004 decision log — Gates 1–4

Status: `AWAITING_OWNER_GATE_3_APPROVAL`

| Ref | Date | Status | Record |
|---|---|---|---|
| G1-DRAFT-001 | 2026-08-22 | RECORDED_INPUT | Ryan Tufts initiated SCA-004 Gate-1 assessment through the Root Phase-0 steer and attached G0 record. This is sufficient human initiation, not Gate-1 acceptance. |
| G1-DRAFT-002 | 2026-08-22 | MANAGER_PARSE | Existing accepted scope items SOW-104, SOW-041, and SOW-053 are sufficient; no PRD or new scope-item amendment is inferred. |
| G1-DRAFT-003 | 2026-08-22 | MANAGER_PARSE | Preserve DEL-02-06 as standing integration/release assurance. Propose six bounded PKG-02 implementation carriers because its accepted M envelope says implementation/client breadth must split when it exceeds M. |
| G1-DRAFT-004 | 2026-08-22 | MANAGER_PARSE | Propose a separate DEL-04-11 TEST_SUITE carrier for the Root receipt validator rather than changing DOC_UPDATE DEL-04-05 into a mixed artifact-kind deliverable. DEL-04-05 and DEL-05-02 remain doctrine/evidence predecessors. |
| G1-DRAFT-005 | 2026-08-22 | G0_AMENDMENT_CARRIED | A3 role parity and instruction-asserted evidence, A4 terminalize plus conditional `thread/resume`, and A7 three consented network postures supersede the conflicting Revision-3.1 planning text for this assessment. |
| G1-DRAFT-006 | 2026-08-22 | MANAGER_GRAPH_CALL | Cross-loop reciprocity is represented only as typed App notice edges. The non-trivial notice SCC is non-gating and proposed for `DECOMPOSE`; no cut/merge authority is inferred. |
| G1-DRAFT-007 | 2026-08-22 | NO_EFFECT | All ten DEL-02-06 bindings remain `HELD_UNAVAILABLE`; `_LATEST.md`, Task Management, deliverable status, decomposition truth, runtime, tools, and App truth remain unchanged. |
| G1-DRAFT-008 | 2026-08-22 | REQUIRED_BASELINE | Fresh scoped SOFTWARE AUDIT_DECOMP covered affected live carriers DEL-02-06, DEL-04-05, and DEL-05-02: 3/3 packages, deliverables, and contexts; 5/5 relevant objectives; 0 BLOCKER, 0 WARNING, 11 lifecycle-appropriate INFO. It is derivative evidence only and opens no later gate. |
| G1-ACCEPTED-001 | 2026-08-22 | `G1-ACCEPTED` | Ryan Tufts accepted the eight parsed actions against the exact three subject identities reproduced verbatim below. This opens Gate 2 impact refinement only. |
| G2-IMPACT-001 | 2026-08-22 | `PENDING_OWNER_ACCEPTANCE` | `Impact_Assessment.md` is the Gate-2 impact assessment. No Gate-3 exact amendment, decomposition write, companion-register write, folder/SOW creation, implementation authority, or hold lift is opened or inferred. |
| G2-ACCEPTED-001 | 2026-08-23 | `G2-ACCEPTED` | Ryan Tufts accepted the Gate-2 impact assessment against the exact three subject identities reproduced verbatim below. This opens Gate-3 and Gate-4 drafting only. |
| G3-AMENDMENT-001 | 2026-08-23 | `PENDING_OWNER_APPROVAL` | `Gate_3_Candidate/`, `Gate_3_Exact_Amendment.diff`, and `Amendment_Preview.md` carry the exact seven-surface amendment candidate. After review-cycle-1 through review-cycle-5 repairs, deterministic validation reports 98/98 PASS, including complete accepted socket controls and the exact closed HarnessEvent v2 terminal set. No live decomposition byte is changed. |
| G4-PROPAGATION-001 | 2026-08-23 | `PENDING_OWNER_APPROVAL` | `Propagation_Plan.md` and `Amendment_Actions.csv` carry the separately approvable propagation plan. No PREPARATION, SOW, dependency, estimate, schedule, graph, audit, pointer, implementation, lifecycle, or Gate-5 act is executed. |

## G1-ACCEPTED owner record (verbatim)

Source:
`plans/steers/chirality_app_v3_root_ruling_record_r1_2026-08-22.md`,
SHA-256
`a9879a87faaeb4cd4d5f16b2b4b0364543dff117e1b51c7e17d1efdcb20f377d`.

<!-- BEGIN R1-C VERBATIM -->
R1-C — SCA-004 Gate 1 (v3 release-pathway Root carrier intake): [click]
  "Accept as parsed".
  Subject bytes: `execution/_ScopeChange/SCA-004_2026-08-22_1749/Brief.md`
  SHA-256 `cdd14b18bd865060398bd8aa22157a6b86d91d7906cdf6d0f68e7ade7d559126`;
  `Gate_1_Validation.md` SHA-256
  `812d0d3a33f0c2740dc89be31566a7b1f30ec833bfd99f3afe45f7bc11c99c14`;
  `WORK_GRAPH.json` SHA-256
  `86159f1eb56fd6dbe08e4133298b0a24aa35e30e443f1965579c229cfbbe78e9`.
  Recorded form: the owner accepts the eight parsed actions — MODIFY
  DEL-02-06 as the standing integration/release-assurance carrier; ADD
  DEL-02-07 through DEL-02-12 under PKG-02; ADD DEL-04-11 under PKG-04 — with
  all ten DEL-02-06 bindings held and App coupling as notice edges only.
  Acceptance opens Gate 2 impact refinement only; it creates no folder, SOW,
  mapping, or implementation authority, and no later gate is inferred.
<!-- END R1-C VERBATIM -->

## G2-ACCEPTED owner record (verbatim)

Source:
`plans/steers/chirality_app_v3_root_ruling_record_r2_2026-08-23.md`,
SHA-256
`63b174f00860cd31dbdde1f734a9e1ca08c44f7cd2ed51f7716612f3847a6bce`.

<!-- BEGIN R2-A VERBATIM -->
R2-A — SCA-004 Gate 2 (impact assessment): [click] "Accept".
  Subject bytes: `execution/_ScopeChange/SCA-004_2026-08-22_1749/Impact_Assessment.md`
  SHA-256 `ff370baaa72a871c2bf7f4c0ade0b41966f414ab8e3f1fb5ae1efe4ba91ed3d3`
  (status `AWAITING_OWNER_GATE_2_ACCEPTANCE`, conclusion
  `PASS_TO_OWNER_GATE_2_WITH_EXACT_GATE_3_REQUIREMENTS`), read against
  `Decision_Log.md` SHA-256
  `bfc184ff50af1f2ba9b9d18ab9d035f9abbaaadd41eae9e99660fcbb51f494dc` and
  `Handoff_State.md` SHA-256
  `971c63bbda66c420f3ffaf581967a9675ae82260a081e3caaaa373cb73e4947c`.
  Recorded form: the owner accepts the Gate-2 impact assessment for the eight
  Gate-1 actions (MODIFY DEL-02-06; ADD DEL-02-07..DEL-02-12; ADD DEL-04-11),
  including its projected topology (46→53 deliverables; PKG-02 6→12; PKG-04
  10→11; packages, objectives, and scope items unchanged), its G0 A3/A4/A7
  carriage, the unchanged ten-binding hold matrix, and its derivative
  classifications. Acceptance opens Gate 3 and Gate 4 *drafting* only: the
  exact synchronized decomposition, companion-register, trace, and telemetry
  bytes, and the propagation plan, return to the owner for approval. No
  decomposition truth, register, pointer, folder, SOW, lifecycle, dependency,
  estimate, schedule, tool, runtime, or App surface changes; Gate 5 is not
  opened; all ten DEL-02-06 bindings remain `HELD_UNAVAILABLE`.
<!-- END R2-A VERBATIM -->

## Pending owner decisions

1. Approve, correct, or decline the exact Gate-3 candidate bytes identified in
   `Amendment_Preview.md` and `Gate_3_Validation.json`.
2. Separately approve, correct, or decline `Propagation_Plan.md` and
   `Amendment_Actions.csv`.

Gate 5 is not open. Neither approval may be inferred from R2-A or from the
existence of these drafts.
