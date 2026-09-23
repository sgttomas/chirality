# PEC Task Management register review — 2026-09-22

**Invocation:** PEC WORKING_ITEMS register review under the owner's 2026-09-22 direction to review every Chirality Task Management register and make evidence-based closure/archive decisions. Selected method: bundled `workflows/task-management/WORKFLOW.md`, register-review mode (triage, staleness/closure echo, deferral review, row maintenance, archive). This is an agent application of that broad owner authorization, not a claim that the owner personally reviewed each row. This record changes no PEC product, SOW, SPEC, decision register, lifecycle, source, release, or reliance state.

**Basis:** `main@212564bc472fa56e232ef116d73f4065e32c111a`. Context origins and SHA-256: Root `AGENTS.md` `1bb670ca339a990b153cf033dac2d8e29ca71bdea0accee4200e6dd1feed3d57`; PEC `AGENTS.md` `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846`; `agents/AGENT_WORKING_ITEMS.md` `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665`; selected workflow `aefe4190ffd1b18cbebd9d7d9c3cfd76b0494bfbb3a89cb1e5b07bf76b6e932f`, contract `775148cc1ae65944e7a26b60b04bdeeb0266444c798b04ab06bed7e154e08290`, method `7f9e0d5ea7c2b74e7148faf3d2a35efc6ddd0552efd4b577a1c56895f75fe2f8`. Chirality change skill `2b490e172436417896c1cd25dbcd543c676e3473aa58b7663985d75785ff7dba`. No Type 2 child was dispatched for this PEC slice.

**Federation preflight:** `taskmgmt federation` wrote only the Git-ignored `.candidates/pec-audit-federation.json` projection. Coverage `COMPLETE`: four canonical tracked registers and archives parsed, zero invalid/unreadable/ambiguous inputs and zero register writes. It reported 27 typed cross-register status/notice findings, none presented as a PEC closure ground. It excludes untracked lookalikes, unsanctioned shapes, free-text Notes, and foreign-register acts. PEC evidence assessment below is bounded to its 18 live rows and seven pre-existing archived rows. PEC reliance-hold `candidate-validation` returned `ALLOW`.

## Applied decisions

| Row | Treatment and exact ground |
|---|---|
| TM-PEC-002 | `CLOSED / INFORMATIONAL_NO_ACTION`. Both cited App-to-PEC notices state no PEC scope, optionality, implementation or authority effect; this is PEC's informational acknowledgment only. Their current SHA-256 values are bound in the archive row. |
| TM-PEC-006 | `CLOSED / INFORMATIONAL_NO_ACTION`. The cited D-GOV-28 notice says no immediate PEC adoption is required and PEC remains an optional client. This does not adopt a runtime contract. |
| TM-PEC-011 | Already `CLOSED / RESOLVED_WITH_CHANGE` under the recorded 2026-08-09 owner ruling and exact accepted DEL-01-06 evidence. Mechanically archived unchanged. |
| TM-PEC-012 | `CLOSED / RESOLVED_WITH_CHANGE`. The SCA-004 PROJECT_SETUP handoff records 64/64 current context provenance blocks, 64/64 current reference packets and a current DEL-01-06 SOW-077 anchor. Its separate TM-PEC-023 mapping blocker survives. |
| TM-PEC-013 | `CLOSED / RESOLVED_WITH_CHANGE`. The 2026-08-09 currency closeout binds three successor SOW hashes, separate REVIEW snapshots, exact acceptance and zero open findings. Current SOW bytes reproduce those hashes. |
| TM-PEC-014 | `CLOSED / RESOLVED_WITH_CHANGE`. The same closeout binds the DEL-00-03 SPEC successor hash, REVIEW snapshot, exact acceptance and zero open findings. Current SPEC bytes reproduce that hash. |
| TM-PEC-015 | `CLOSED / RESOLVED_WITH_CHANGE`. The WORKING_ITEMS SCA-004 currency sweep records four current orientation maps corrected and validated. |
| TM-PEC-017 | `CLOSED / RESOLVED_WITH_CHANGE`. That sweep annotated four mutable handoffs and superseded three immutable historical handoffs through current coordination pointers; historical evidence was preserved. |

The seven new closure rows and the one previously closed row moved through `taskmgmt archive`. The live register moves from 18 to 10 rows (`OPEN=9`, `DEFERRED=1`, `CLOSED=0`); the archive moves from seven to 15. Closure EvidenceRef, EvidenceSha and EvidenceQuote are in each archived row. No priority, assignment or receiving-loop obligation was added.

## Retained live rows — row-complete review

| Row | Current treatment and reason |
|---|---|
| TM-PEC-001 | `OPEN`. The D-GOV-31 notice still requests a PEC-local disposition of the merge-policy succession; Root policy evolution alone does not decide PEC's local adoption/acknowledgment. |
| TM-PEC-003 | `OPEN`. The governing D-PEC-02 register row remains `NOT_PREPARED`; retired product framing does not itself amend that decision record. |
| TM-PEC-004 | `OPEN`. DEL-04-01 feed-grammar ownership remains a boundary choice; accepted current SOW currency did not name its owner. |
| TM-PEC-005 | `OPEN`. Limitation inventory, absent-feed ownership, rendering and trigger-set questions still require an owning choice across the cited contracts. |
| TM-PEC-018 | `OPEN`. Batch-B8 fan-in explicitly ruled F7 `NO-ACTION`, but the paired E-P26 evidence gap in the DEL-03-02 run record remains without a documented completion or retirement. One resolved limb does not close the combined row. |
| TM-PEC-019 | `OPEN`. D-PEC-66 closed the E-N13, REQ-011 and QA-item-20 limbs, while its residual account still carries DEL-08-02 provenance, DEL-08-01 AC-005 method coverage and DEL-00-03 CLM-001 matrix linkage. The combined row is only partly discharged. |
| TM-PEC-021 | `OPEN`. The cited reconciliation handoff still routes the ADR-014 PRD §13 wording discrepancy to PRD authority; the live PRD text still contains the referenced wording. |
| TM-PEC-022 | `DEFERRED`. COV-040 remains a recorded warning; the later D-PEC-81 ruling expressly keeps it deferred until the next DEL-08-02 lifecycle act. No such act is established here. |
| TM-PEC-023 | `OPEN / held`. The SCA-004 metadata handoff and D-PEC-81 expressly retain nine blank objective mappings pending a dedicated owner mapping or typed non-mapping ruling and SCOPE_CHANGE mechanics. This gate is not discharged by metadata completion. |
| TM-PEC-024 | `OPEN`. Receipt 146 and the D-PEC-77 handoff establish the inherited generated-output-labeling failure, but the row asks for a named repair owner or deliberate no-action. A current harness run without that generated scratch file is insufficient to establish either disposition. |

## Pre-existing archive closure echo

| Row | Retained closure ground |
|---|---|
| TM-PEC-007 | Informational shared instruction succession; prior owner disposition and notice evidence retained. |
| TM-PEC-008 | Informational Root harness scope-correction notice; prior owner disposition retained. |
| TM-PEC-009 | DEL-01-06 RF-001/VER-005 exact rerun and prior owner closure retained. |
| TM-PEC-010 | D-PEC-78 O-A resolved the registry home/shape decision; separate propagation remained with its owning instrument. |
| TM-PEC-016 | Five individual notice dispositions are recorded by the cited ledger; prior owner closure retained. |
| TM-PEC-020 | Prior owner no-action after the SCA-004 corpus-wide dispatch; no historical normalization inferred. |
| TM-PEC-025 | Prior owner `OBE` ruling cites separate successor acts discharging all three carried gates. |

Those seven archive rows remain byte-identical. Four retain `_DomainEngines/pec/_TaskManagement/` evidence locators from before D-PEC-80's relocation; each maps to the current PEC Task Management home with the recorded SHA-256 unchanged. Their historical paths and closure citations remain in the archived records. This review found no new PEC evidence that reverses a closure. The relevant current records also preserve TM-PEC-022 and TM-PEC-023 as live gates. A later source change should be handled as staleness against that row's actual source, not by silently re-closing it.
