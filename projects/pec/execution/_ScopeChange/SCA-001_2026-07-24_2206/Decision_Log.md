---
amendment_id: SCA-001
doc_kind: scope_change.decision_log
decomp_variant: SOFTWARE
created: 2026-07-24
status: closed_for_scope_change_only
---

# SCA-001 Decision Log

| Ref | Gate | Decision or state | Authority / disposition |
|---|---|---|---|
| DL-SCA-001 | Opening | Human initiated `PEC SCA-001 — Directed Full-DAG Self-Bootstrap`; PRD v2.1 is adopted, `FULL_GRAPH` is selected, and SCA-001 opens against accepted decomposition revision 1.0. | `D-PEC-61`; ruled. |
| DL-SCA-002 | Opening | The owner packet authorizes the session and its documentation surfaces but does not pre-approve SCOPE_CHANGE Gates 1–5. | `D-PEC-61`; binding gate boundary. |
| DL-SCA-003 | Gate 1 | Resolve `DECOMP_VARIANT=SOFTWARE`, accepted basis revision 1.0, `AMENDMENT_ID=SCA-001`, and `ALLOW_RENUMBERING=false`. | Protocol/defaults; resolved. |
| DL-SCA-004 | Gate 1 | Parse exactly four actions A001–A004 as `MODIFY`; treat A001 as modification of the existing Hard Constraints semantic section, with C16 as its new non-topological row. | Owner plan + semantic section binding; validated. |
| DL-SCA-005 | Gate 1 | Dispatch read-only `AUDIT_DECOMP` against the unscaffolded execution root. Preserve `FAILED_INPUTS` rather than interpreting absent folders as negative coverage. | `AGENT_SCOPE_CHANGE` Gate 1 + `AGENT_AUDIT_DECOMP` Step 0; completed. |
| DL-SCA-006 | Gate 1 | Use a deterministic register-integrity baseline because filesystem coverage is not yet available. | OI-013 limitation + owner plan; completed in `Pre_Change_Coverage.json`. |
| DL-SCA-007 | Gate 1 | Do not create `Dependencies.csv`; full-DAG dependency materialization belongs to downstream `PROJECT_SETUP`. | `D-PEC-61` exact fence; binding. |
| DL-SCA-008 | Gate 1 | Hold all Gate 2 work until the owner answers the exact Gate 1 confirmation question. | `AGENT_SCOPE_CHANGE` protocol; satisfied by owner confirmation. |
| DL-SCA-009 | Gate 1 | Owner confirmed the parsed change and Gate 1 baseline: “Yes that's what I intend.  Proceed accordingly.” | Verbatim in-session owner confirmation; Gate 1 confirmed. |
| DL-SCA-010 | Gate 2 | Assess A001–A004 as a non-topological clarification: no ID/count/lineage change; direct eventual writes are limited to the approved decomposition package surfaces; dependency/scaffold work remains downstream. | `Impact_Assessment.md`; awaiting owner acceptance. |
| DL-SCA-011 | Gate 2 | Preserve the pre-scaffold `AUDIT_DECOMP FAILED_INPUTS` result as a limitation and require deterministic post-change register comparison because OI-013 remains open. | `Impact_Assessment.md`; awaiting owner acceptance. |
| DL-SCA-012 | Gate 2 | Hold all Gate 3 work until the owner answers the exact Gate 2 confirmation question. | `AGENT_SCOPE_CHANGE` protocol; satisfied by owner acceptance. |
| DL-SCA-013 | Gate 2 | Owner accepted the impact assessment: “I accept this impact assessment.  Proceed accordingly.” | Verbatim in-session owner confirmation; Gate 2 confirmed. |
| DL-SCA-014 | Gate 3 | Draft the complete exact revision 1.0→1.1 amendment across the working surface, three affected authoritative companion rows, and decomposition handoff pointer; classify `Companion_Inventory.csv` as `NO_CHANGE`. | `Amendment_Preview.md`; awaiting owner approval. |
| DL-SCA-015 | Gate 3 | Hold all Gate 4 work until the owner answers the exact Gate 3 approval question. | `AGENT_SCOPE_CHANGE` protocol; satisfied by owner approval. |
| DL-SCA-016 | Gate 3 | Owner approved the exact amendment preview: “I approve these amendments to the decomposition document.  Proceed accordingly.” | Verbatim in-session owner confirmation; Gate 3 approved. |
| DL-SCA-017 | Gate 4 | Bind A001–A004 to the exact direct-write quarantine, deterministic recomputations, audit attempt, no-change surfaces, rollback, closure state, and downstream handoffs in `Propagation_Plan.md`; register the four actions in `Amendment_Actions.csv`. | Awaiting owner approval. |
| DL-SCA-018 | Gate 4 | Record no admitted authority fact override: all four actions use `SupersessionBindingPresent=NO`; Gate 5 creates a header-only cumulative `Supersession_Map.csv` and no `Supersession_Delta.csv`. | `D-PEC-61` + approved Gate 3 preview; awaiting owner approval. |
| DL-SCA-019 | Gate 4 | Hold all Gate 5 execution until the owner answers the exact Gate 4 confirmation question. | `AGENT_SCOPE_CHANGE` protocol; satisfied by owner approval. |
| DL-SCA-020 | Gate 4 | Owner approved the propagation plan: “I approve this propagation plan.  Proceed.” | Verbatim in-session owner confirmation; Gate 4 approved. |
| DL-SCA-021 | Gate 5 | Verify all six accepted revision 1.0 hashes before applying any amendment. | PASS, 6/6; `Pre_Change_Coverage.json`. |
| DL-SCA-022 | Gate 5 | Apply only the approved Gate 3 diff to the five authorized decomposition surfaces and keep `Companion_Inventory.csv` byte-identical. | Completed; deterministic postcheck PASS. |
| DL-SCA-023 | Gate 5 | Generate a header-only cumulative `Supersession_Map.csv`; omit `Supersession_Delta.csv` because no admitted authority fact is overridden. | Registered accumulator PASS, 0 rows, 0 findings. |
| DL-SCA-024 | Gate 5 | Dispatch post-change `AUDIT_DECOMP`; preserve its expected pre-scaffold `FAILED_INPUTS` result as `AuditState=WARNINGS`, not filesystem coverage. | Completed; `COV_SCA001_POSTCHANGE_2026-07-24_2230`. |
| DL-SCA-025 | Gate 5 | Hold final closure, `current_basis`, `CHANGE`, and `PROJECT_SETUP` handoffs until the owner confirms the post-change state. | Satisfied by owner confirmation. |
| DL-SCA-026 | Gate 5 | Owner confirmed the post-change state and accepted the successor: “I confirm the post-change state and accept decomposition revision 1.1 as the current basis.” | Verbatim in-session owner confirmation; Gate 5 confirmed. |
| DL-SCA-027 | Closure | Set revision 1.1 to `current_basis`, close `CLOSED_FOR_SCOPE_CHANGE_ONLY`, release `PROJECT_SETUP` with `FULL_GRAPH` selected and Phase 1.3 choices pending, and authorize the `CHANGE` handoff without invoking either workflow. | SCA-001 closed. |

## Gate status

| Gate | State | Owner confirmation |
|---|---|---|
| Gate 1 — Change intake and validation | `CONFIRMED` | “Yes that's what I intend.  Proceed accordingly.” |
| Gate 2 — Impact assessment | `CONFIRMED` | “I accept this impact assessment.  Proceed accordingly.” |
| Gate 3 — Amendment approval | `APPROVED` | “I approve these amendments to the decomposition document.  Proceed accordingly.” |
| Gate 4 — Propagation plan approval | `APPROVED` | “I approve this propagation plan.  Proceed.” |
| Gate 5 — Execute and validate | `CONFIRMED` | “I confirm the post-change state and accept decomposition revision 1.1 as the current basis.” |

Revision 1.1 is the accepted `current_basis`. SCA-001 is
`CLOSED_FOR_SCOPE_CHANGE_ONLY`; downstream workflows are released but have
not been invoked.
