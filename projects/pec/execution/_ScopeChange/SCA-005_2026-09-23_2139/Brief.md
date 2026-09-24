---
amendment_id: SCA-005
doc_kind: scope_change.brief
decomp_variant: SOFTWARE
checkpoint_group: 1
created: 2026-09-23
status: awaiting_checkpoint_1_acceptance
authority: D-PEC-86 §3 I-1..I-3 (Gate 1 opened by owner direction 2026-09-23)
workflow: chirality-root:bundled:workflow:scope-change
---

# SCA-005 — PEC feed-model rebaseline (checkpoint-group-1 brief)

## Human initiation

SCA-005 was opened at Gate 1 by the owner's direction of 2026-09-23, recorded
verbatim in `execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md` §1:

> Proceed with SCA-005 and what follows in your recommendations.  You are
> Agent 0, so consider effective delegation to your Type 1 and Type 2
> instances.  Use `opus-5.5` models on `high` reasoning for all subagents.  You
> can continue working within your capacity of HELP_HUMAN, anticipating my
> needs and those of the agents under you.

The referent recommendation (Agent 0 text, D-PEC-86 §2 item 1, not owner
text): "Open SCA-005 to rebaseline PEC's feed model on the shared 2026-09-22
method and the A2 Runtime topology, producing a PRD v2.3 candidate,
decomposition revision 1.5 and a Scope of Work currency list; fold in the
adopted but unapplied PRD §16.3 postimage (D-PEC-79) and the nine TM-PEC-023
objective blanks."

The owner has **not** accepted checkpoint group 1. Opening Gate 1 is the only
owner act this package relies on.

## Normalized parameters

| Parameter | Value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `projects/pec/execution/` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` (revision 1.4 `current_basis`, SHA-256 `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`) |
| `SCOPE_CHANGE_ROOT` | `projects/pec/execution/_ScopeChange/` |
| `AMENDMENT_ID` | `SCA-005` (PEC-qualified; the ID also names Root and App/Piping amendments, A1 DR-18) |
| `ALLOW_RENUMBERING` | `false` |
| `ALLOWED_PROPAGATION_WRITES` | SOFTWARE default (decomposition + affected `_CONTEXT.md`/`_STATUS.md`), only after checkpoint-2 acceptance |
| Pointer posture for a later checkpoint 3 | `ACCEPTED_PREDECESSOR` (`_ScopeChange/_LATEST.md` names SCA-004) |
| Current stage | checkpoint group 1 (method parts A and B) prepared; awaiting owner |

## Semantic section binding (by heading text)

| Semantic section | Bound heading in `SOFTWARE_DECOMP.md` |
|---|---|
| Change Register | `## 11. Decision Log` and `## 12. Revision History (Phase 7 change summary)` (plus `## Gate Log`) |
| Unit Ledger | `## 6. Scope Ledger` → authoritative `ScopeLedger.csv` |
| Objectives | `## 3. Objectives (Phase 3)` and the ledger `ObjectiveIDs` column |
| Primary Partitions | `## 4. Packages (Phase 4)` |
| Secondary Entities | `## 5. Deliverables (Phase 5)` → authoritative `Deliverables.csv` |
| Vocabulary Map | `## 9. Vocabulary Map (seeded at Phase 2)` |
| Coverage basis / telemetry | `## 7. Coverage & Telemetry (Phase 6)`, `## 8. Context Budget QA (Phase 6)` → `ContextBudgetQA.csv`; pre-change `audit-decomp` output |
| Constraints / open issues | `### 1.3 Hard constraints`, `## 10. Open Issues` |

All bindings resolved at the first rank; none was resolved by position.

## The change as parsed (PROPOSED)

Evidence inputs (read, not modified): A1 survey `SURVEY_SISTER_LOOP_FILE_TRUTH.md`
(`ec3301c4…2ddb`) + `SURVEY_MANIFEST.json` (`4f84cde1…521c`); A2 inventory
`IMPACT_INVENTORY_PEC_BASIS.csv` (201 rows, `f0bba13a…e3bc`) + `.md`
(`b0ff8359…0484`); A4 design note `FEED_MODEL_V2_DESIGN_NOTE.md`
(`4b9ccb9f…12da`); D-PEC-79 postimage (`92627ee1…b5f0`); TM-PEC-023
`DECISION_SURFACE.md` (`3a61a24d…71ef`). Full hashes are in
`Impact_Assessment.md` §2 and `Handoff_State.md`.

`Amendment_Actions.csv` records **76 PROPOSED atomic actions** for the
recommended set (design-note O-B2 + P-β, with the manager's R1 deferral
representation, ADD-new feed items and Q6 re-expression):

| Change element (brief item) | Seq | Summary |
|---|---|---|
| (a) premises naming retired surfaces | 1–7, 12–18, 22–45 | SOW/DEL/PKG/constraint rows citing `WORK_GRAPH.json`/`STATUS.json`/`RUNTIME_SUMMARY.json`, per-loop ledgers/D-APP-57, `## Remaining`, workplans, the per-user daemon (D-GOV-20) or `adapter.yaml` as manifest are re-expressed |
| (b) ADD candidates the drift implies | 8–11, 19–21, 56–59 | SOW-095 + DEL-02-08 (Markdown work graphs, discovery, PR→merge join inputs); SOW-096 + DEL-02-09 (MEMORY run index); central receipts folded into SOW-013/DEL-02-03; registry feed profiles (SOW-077/094, DEL-01-06); vocabulary terms — each a proposal with stated parent and design-note option, never accepted scope |
| (c) nine TM-PEC-023 carry-ins | 63–71 | owner-selectable options exactly as prepared; no option pre-selected; rows 1/4/7 sequenced behind Q3 |
| (d) D-PEC-79 postimage | 75–76 | adopted exact input; PRD is product authority outside the decomposition; application rides the propagation plan only with checkpoint-2 acceptance |
| (e) telemetry / coverage | 60–62, 73–74 | objective views, §7/§8 recomputation, traceability after checkpoint 3 |
| presence under A2 (Q3) | 26–45 | P-β: Git + hooks presence; SOW-029/035/087 Deferred OUT behind trigger T-RT; DEL-06-04/07-02/07-05 retired non-destructively |
| §16 TBD items (Q6) | 46–53 | re-expressed, decisions still open |
| Q9 (conditional) | 72 | SOW-058 supplementary comparison baseline |

Counts: 8 ADD, 65 MODIFY, 3 REMOVE; 27 DELIVERABLE, 36 OTHER, 6 VOCAB_TERM,
4 PACKAGE, 3 OBJECTIVE. Part-A validation: 76/76 PASS (Impact Assessment
Annex A). Delta tables for O-A, O-B1, O-C, P-α, P-δ, R2 and the other options
are in Impact Assessment §12.

Exact amendment prose is deliberately absent; it belongs to checkpoint
group 2.

## Write boundary of this run

Written: this snapshot folder (`Brief.md`, `Impact_Assessment.md`,
`Amendment_Actions.csv`, `Pre_Change_Coverage.json`, `Decision_Log.md`,
`Handoff_State.md`) and, by a dispatched TASK child, the pre-change audit
snapshot `_Evaluation/DecompCoverage/COV_SCA005_PRECHANGE_2026-09-23_2139/`.

Not written: `_ScopeChange/_LATEST.md`, `_Evaluation/DecompCoverage/_LATEST.md`,
`_ScopeChange/checkpoint_snapshots/`, any decomposition file or register,
`docs/PRD.md`, any `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `v2/**`,
`_DomainEngines/**`, or any App, Piping, Runtime, Root or bridge path. The
checkpoint-1 decision snapshot is not created; it follows owner acceptance.

## Instruction and method basis

| File | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_WORKING_ITEMS.md` | `9ae4bea25bd95750a6878a9d53fbbbd7cd058d72c652a36baf4aa90601799665` |
| `workflows/scope-change/WORKFLOW.md` | `58f5d1d53c655fdc5668d928f6087003590f40e321e25e3d9447805ee64a7a90` |
| `workflows/scope-change/resources/contract.md` | `4453a719f1588c4eba08bdb4a979140ff3541ed5a29f04477ea58a844f344d02` |
| `workflows/scope-change/resources/method.md` | `34187e83856853f655389625e3465e3c2cb9ff8ad38be1f4d138ee7470d167f5` |
| `workflows/audit-decomp/WORKFLOW.md` | `4aaa7e10990ddd1b769ba09da78a03f9f491a6b6f3be6df08a1a8de93c26e3e6` |
| `workflows/audit-decomp/resources/contract.md` | `70a5abebc8ff34826415e1566715373a322baded2939325b5b73828d78401a0c` |
| `workflows/audit-decomp/resources/method.md` | `97df84022ccbec434aea9745296b93b6e549ef840acc0ca9df0a215e634d79c2` |
| `workflows/audit-decomp/execution.json` | `5183e34217c8d68e63456eb698531882b8c9aebdf083a2fc1a705e27f540d8d1` |
| Brief B1 with both addenda | `126f8c951307c49a84d4e8811f67364aa52e403c2ebf3418950f0c0ff139819e` |
| D-PEC-86 | `7cc4dd0f9065f9a79e554aae6ddad5dfdb631a28556585e8d04a7e6a6bdb682b` |

The scope-change hashes equal those recorded in `SUPPLIED_BASIS.json`. The
manager read only its own role file; the audit-decomp workflow files were
read to brief the TASK child (that child ran them). SCA-004's snapshot form
was mirrored where the method is silent; SCA-004 used the older five-gate
vocabulary, while this run follows the current three checkpoint groups.

## Gate boundary

This package changes no decomposition truth, companion register, accepted
pointer, deliverable metadata or content, dependency register, PRD, source,
lifecycle, Task Management row, decision, receipt or foreign-loop surface.
