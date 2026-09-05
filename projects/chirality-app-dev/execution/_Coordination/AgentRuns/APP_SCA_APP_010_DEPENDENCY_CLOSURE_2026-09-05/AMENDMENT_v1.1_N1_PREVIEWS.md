# Brief amendment v1.1 — N1 previews (issued by HELP_HUMAN after fan-in of the thirteen returns)

**RunID:** `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` · **Applies to:** every `instances/N1-TASK-*/LAUNCH_BRIEF.md` (v1) · **Version:** 1.1 · **Authority:** HELP_HUMAN's supervisory disposition under `agents/AGENT_HELP_HUMAN.md` Phase 4 (versioned brief amendment). This amendment narrows the previews; it widens no authority and changes no fence. Nothing here is an owner ruling.

## Why

The thirteen previews each passed their own fences, but the fan-in simulation with all thirteen post-images substituted at once (`Evidence/fanin_simulation_v1/`) shows that 15 of the 25 newly proposed deliverable edges lie on cycles collectively: together they would merge `SCC-001` (nine nodes) into a 20-node SCC and create a new two-node SCC (DEL-06-03 / DEL-08-01), while any one of them alone changes nothing (`edge_analysis.json`). SCA-APP-010 `DOWNSTREAM_HANDOFFS.csv` row 3 requires "SCC unchanged unless separately ruled", and `docs/CYCLE_DRIVEN_RESOLUTION.md` makes cut and merge human-gated and holds cycle-participating edges non-gating until resolved. Choosing which of the fifteen to keep would be a cut. Therefore all fifteen are **held**: recorded as non-emitted proposals in `HELD_EDGE_PROPOSALS.csv` (H-001 to H-019 rows, one per register row; reciprocal rows of one edge appear twice) for the owner's separate transaction, and removed from the post-images. The acyclic remainder proceeds.

## A. Held rows to remove from the post-image (IDs stay reserved)

| Carrier | Rows to remove from `POSTIMAGE_Dependencies.csv` | Reserved for |
|---|---|---|
| DEL-02-01 | DEP-02-01-010 | H-001 |
| DEL-02-02 | DEP-02-02-015, DEP-02-02-017, DEP-02-02-018, DEP-02-02-019, DEP-02-02-020, DEP-02-02-022 | H-002 to H-007 |
| DEL-02-04 | DEP-02-04-015, DEP-02-04-016, DEP-02-04-017, DEP-02-04-018, DEP-02-04-019 | H-008 to H-012 |
| DEL-02-05 | DEP-02-05-014, DEP-02-05-015 | H-013, H-014 |
| DEL-03-02 | DEP-03-02-013 | H-015 |
| DEL-05-02 | DEP-05-02-016 | H-016 |
| DEL-06-03 | DEP-06-03-014 | H-017 |
| DEL-08-01 | DEP-08-01-018 | H-018 |
| DEL-08-04 | DEP-08-04-013 | H-019 |

Rules: delete exactly these rows from the post-image CSV (they were never written to the carrier, so this is not a register deletion); do **not** renumber the remaining rows (the removed IDs stay reserved for the held proposals and are listed as such); in `POSTIMAGE__DEPENDENCIES.md` add one Run Notes bullet per held row in the form `HELD (non-emitted proposal, pending owner ruling): DEP-xx-yy-0nn reserved — <edge> — see AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/HELD_EDGE_PROPOSALS.csv H-nnn`, remove the row from the extracted-register table, and reconcile every count (register summary, Run History ACTIVE count, lifecycle, satisfaction). In `PREVIEW.md` move each held row from the diff table to a new section `## Held proposals (amendment v1.1)` listing the H-id, the edge, and the evidence it would have cited. Carriers not listed (DEL-04-04, DEL-07-01, DEL-07-03, DEL-08-03) are unchanged by this amendment.

## B. SCC-internal rows: evidence-field refresh is permitted (clarifies v1 rule F1)

v1 said SCC-internal rows are "preserved byte-identically except `LastSeen`". That was read as forbidding evidence-field changes and left rows citing files that no longer exist. Clarification: for a row whose `FromDeliverableID` and `TargetDeliverableID` are both SCC-001 members, the fields `EvidenceFile`, `SourceRef`, `EvidenceQuote`, `TargetLocation` (line pointer only), and `LastSeen` **may** be refreshed to live bytes when the relation is still stated; `DependencyClass`, `AnchorType`, `Direction`, `DependencyType`, `TargetType`, `TargetDeliverableID`, `Status`, `Statement`, `SatisfactionStatus`, `Origin`, and `FirstSeen` stay frozen. A row still not evidenced after that stays ACTIVE and unchanged and remains listed under `NEEDS_HUMAN_GRAPH_DECISION`. Apply to: DEL-03-02 rows 007, 008, 009; DEL-05-02 rows 009, 010, 012; DEL-02-05 rows 004 and 006 (line pointers). Change class in the diff table: `RE-EVIDENCED (SCC-internal, evidence fields only)`.

## C. Dispositions of the other held questions (HELP_HUMAN, disposition-class; recorded here, not rulings)

1. DEL-02-02 `DEP-02-02-021` (Workflows view host): keep target DEL-02-03 with `Confidence=MEDIUM` and a `Notes` ASSUMPTION citing the owner-adopted `_STATUS.md` Depends line (`DEL-02-03-V3-01`, D-APP-108) as the evidence and the applied row L307/L309 silence as the reason for MEDIUM. Same treatment for DEL-02-05 `DEP-02-05-015` would have applied, but that row is held under A.
2. DEL-04-04 `DEP-04-04-004`: stays RETIRED (RUL-SCC-001-TRANCHE-001); no change.
3. DEL-08-01 `DEP-08-01-013` (pre-existing absolute Root pointer in `TargetLocation`): preserved unchanged; outside DEP-021's permitted effect; carried to the owner slate in `HANDOFF_STATE.md`.
4. DEL-08-01 reciprocal edge to DEL-04-04: not invented; no change.
5. DEL-02-01 HGD-1 (direction of `DEP-02-01-006`), HGD-2 (`DEP-02-01-007/008` after DEC-025), HGD-3 (`DEL-02-02-V3-03` prerequisite): unchanged in the post-image; carried to the owner slate.
6. DEL-06-03 H-1 (DEL-06-02 catalog validation): stays non-emitted; carried to the owner slate. The disclosed read-only import of the analyzer for the SCC replay is accepted as disclosed and non-load-bearing; record it in the rerun record as well.
7. `TargetType=UNKNOWN` for objective anchors: keep the brief's convention (matches the pre-existing rows in these carriers).

## D. Rerun contract (for the nine carriers in A, plus B where it applies)

A fresh instance rewrites, in place under its own `instances/N1-TASK-<carrier>/`, the files `POSTIMAGE_Dependencies.csv`, `POSTIMAGE__DEPENDENCIES.md`, `PREVIEW.md`, `RETURN.md`, `STATUS.json` (`STATUS.json` gains `"amendment": "v1.1"`), and appends a **new** run record `_run_records/TASK_RUN_2026-09-05_<HHmm>.md` (the v1 record stays). Re-run Function 5 on the revised post-image (schema, enums, one parent anchor, evidence resolves to live bytes, counts reconciled, unique IDs, `FromDeliverableID`). Change nothing else anywhere; the carrier stays untouched. Record the new post-image hashes in `RETURN.md`. `STATUS.json.status` is `PASS` when no `NEEDS_HUMAN_GRAPH_DECISION` row remains, else `WARNINGS`.
