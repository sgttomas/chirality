# Validation Evidence — APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05

All commands run from the repository root of worktree
`/Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2`
on branch `claude/sca-app-010-dependency-closure` (basis
`d66395d101143df68d956984f7ab93f5027418ec`, PR #713 merge). Raw outputs are
under `Evidence/validation/`.

## Node evidence

| Node | Evidence | Result |
| --- | --- | --- |
| N0 preflight | `Evidence/app_hold/DEL-*.json` (13, verdict `ALLOW`, contract `CLEAR`); `Evidence/baseline_closure/` (46 nodes, 99 edges, SCC-001 nine nodes, six isolates, one bidirectional pair); `Evidence/n1_preimages.json` | PASS |
| N1 previews (v1) | thirteen `instances/N1-TASK-*/` returns: every fence `NONE` per carrier; eight `WARNINGS` for held questions, five `PASS`; carrier bytes unchanged (pre-image re-hash) | returned |
| N1 fan-in simulation v1 | `Evidence/fanin_simulation_v1/` (all thirteen post-images substituted): 48 nodes, 124 edges, SCC-001 merged into a 20-node SCC plus a new two-node SCC; `edge_analysis.json`: 25 new edges, 15 on cycles collectively, none individually | stop condition handled by amendment v1.1 |
| Amendment v1.1 | `AMENDMENT_v1.1_N1_PREVIEWS.md`; `HELD_EDGE_PROPOSALS.csv` (19 rows, H-001 to H-019, reserved IDs); nine reruns with second run records; `Evidence/fanin_simulation_v1.1/`: 48 nodes, 109 edges, one SCC = the nine SCC-001 members, one bidirectional pair (baseline), no baseline edge removed | PASS |
| N2 review | `REVIEW.md` (SHA-256 `ece7d8ffae6f04efef337a98b675ec058d5713ecc60a426824e8e55d05bddd85`): PASS, BLOCKER 0 / MAJOR 0 / MINOR 9; fan-in parity reproduced independently; step-19 stop condition not triggered | PASS |
| N2-gate | `HANDOFF_STATE.md` N2-gate disposition: all thirteen `PROCEED`; MINORs carried as recorded | recorded |
| N3 reviewed write | thirteen `instances/N3-TASK-*/STATUS.json` `PASS`; every carrier's `Dependencies.csv` and `_DEPENDENCIES.md` hash equal to `Evidence/n3_reviewed_postimages.json`; one new carrier run record each (`_run_records/TASK_RUN_2026-09-05_051[3-5].md`); first fan-out lost to a session usage limit before any run record was written, two partial copies (DEL-02-01, DEL-02-05) reverted to pre-image with `git checkout --` and all thirteen re-dispatched from verified pre-images | PASS |
| Live closure after write | `analyze_dep_closure.py` over the live tree: 48 nodes, 109 edges, SCC-001 nine nodes, four isolates, one bidirectional pair (equal to `fanin_simulation_v1.1`) | PASS |
| N4 closure audit | `execution/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0518/` (25 files, `MANIFEST.sha256` verified): verdict `WARNINGS`, no blocker; 52 registers, 635 rows, 129/129 active endpoints resolved; 48 nodes, 109 edges; `SCC-001` membership identical to baseline and to the SCA-APP-008 audit, no SCC-internal edge added or retired, same ten elementary cycles, no new SCC; isolates 6 to 4; held proposals verified absent from every live register; new warnings DC-007/DC-008 (pre-existing legacy `TargetType` values in DEL-05-01 and DEL-05-05) and DC-009 (pre-existing `DEP-08-01-013` Root pointer); `_LATEST.md` not moved | WARNINGS (no blocker) |
| N5 reconciliation | `execution/_Reconciliation/RECON_SCA_APP_010_POST_ALIGNMENT_2026-09-05_0518/` (read-only R0/R1 posture, not an activated concordance run; `MANIFEST.sha256` verified): result `FINDINGS`, no BLOCKER or MAJOR; corpus v20 no drift; applied pair, companion (83/83 pins), and pointer parity PASS; `CARRIER_CONCORDANCE.csv` 489 claims: 470 ALIGNED, 17 MISMATCH, 2 UNKNOWN; lifecycle, approval SHA, fences, and the four working-surface files byte-identical to `origin/main`; findings F-1 (`_CONTEXT.md` Traceability `CoversScopeItems` row lags the applied refs on nine carriers), F-2 (SCA-APP-004 wording residue in three contexts), F-3 (stale row-line citations in three seated items), routed to WORKING_ITEMS; `_LATEST.md` not moved | FINDINGS (routed) |
| N6 decomposition audit | `execution/_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_ALIGNMENT_2026-09-05_0518/` (nine files plus `MANIFEST.sha256`, verified): `RUN_STATUS = WARNINGS`; 0 / 72 / 10 versus the Gate-5 post-change audit's 0 / 74 / 8; no new BLOCKER or MAJOR; G5-010-COV-005 resolved; G5-010-COV-004 partially resolved (prose aligned on all thirteen; the Traceability table, Anticipated Artifacts paragraph, and one DEL-08-03 ownership sentence still lag, outside the executed WI permitted effect); topology and companion expectations all met; thirteen refreshed registers valid and anchored; `_LATEST.md` not moved | WARNINGS (no new blocker or major) |

## Repository validators (tree after N3, before the audit snapshots)

| Validator | Result |
| --- | --- |
| `tools/scope_of_work/validate_scope_of_work.py` ×13 carriers | PASS ×13 (`scope_of_work_validator.txt`; `ScopeOfWork.md` untouched by this run) |
| `tools/validation/validate_dependencies_schema.py` over every `PKG-*/1_Working/DEL-*/Dependencies.csv` | 52 registers found; 50 VALID; two pre-existing failures unchanged versus `origin/main` and outside this run's write set (DEL-05-01 rows 006 and 009 use legacy `TargetType` values `CODE` and `DECISION`; DEL-05-05 likewise untouched, see `dependencies_schema_all.txt`); DEL-00-01 and DEL-00-02 carry no register (PKG-00 architecture basis) |
| `execution/_Reconciliation/References/reconcile_authority_corpus.py status` | corpus v20, no drift (`corpus_status.txt`) |
| `tools/practitioner_harness/harness.py self-check` | exit 0; no BLOCK, before the audit snapshots (`harness_self_check.txt`) and again after them (`harness_self_check_post.txt`); GEN-7 pointer currency raised nothing for the three new snapshots |
| G0 `validate_root_materialization_fence.py` | exit 0 |
| G1 `validate_root_harness_adapter.py` | exit 0 |
| G2 `validate_root_surface_ownership.py` | exit 0 |
| G3 `validate_root_work_graph_dispatch.py` | exit 0 |
| G4 `validate_instruction_tranche_manifest.py --base origin/main --head HEAD --added-manifests-only` | run after commit; recorded in the receipt |
| `tools/validation/validate_candidate_whitespace.py --base-ref origin/main` | PASS (`candidate_whitespace.txt`) |
| `tools/run_affected_tests.py --base origin/main` | 671 passed (`run_affected_tests.txt`) |
| `git diff --check` | clean |
| `tools/validation/validate_app_dev_loop_receipts.py` | VALID before the Receipt 239 append (`receipts_pre.txt`); rerun after the append and recorded in the receipt |
| Frontend gates | skipped: no product source changed (`frontend/**` untouched) |

## Scope backcheck

Changed paths versus the basis: the thirteen carriers' `Dependencies.csv` and
`_DEPENDENCIES.md` (26 modified) and one new `_run_records/TASK_RUN_2026-09-05_*.md`
each (13 untracked); this run folder; the three audit snapshots named in the
node table; `loop/LOOP_RECEIPTS.md` (append). No `frontend/**`, `docs/**`,
decomposition, companion register, pointer (`_ScopeChange/_LATEST.md`,
`_Reconciliation/DepClosure/_LATEST.md`, `_Reconciliation/_LATEST.md`,
`_Evaluation/DecompCoverage/_LATEST.md`), SCA snapshot, `_STATUS.md`,
`MEMORY.md`, `ScopeOfWork.md`, `_CONTEXT.md`, `_REFERENCES.md`, register, or
prior receipt changed.

## Attribution

HELP_HUMAN (Claude Fable 5.1, Anthropic, `claude-fable-5-1`) in an untyped
Claude Code session; thirteen N1 preview instances plus nine v1.1 reruns,
one N2 reviewer, thirteen N3 writers, and the N4, N5, N6 audit instances were
bounded Claude Code subagents (Claude Fable 5.1) under sealed briefs in this
folder; none launched a descendant. Role not mechanically enforced.

## v1.2 — owner ruling D-APP-109 (second commit on the same candidate)

| Node | Evidence | Result |
| --- | --- | --- |
| N8 ruling and context alignment | `_DECISIONS/D-APP-109_RULING_SCA_APP_010_HELD_EDGES_AND_CONTEXT_ALIGNMENT_2026-09-05.md` and one `_REGISTER.md` row; `build_context_fix.py` (freeze, apply, check) with `Evidence/context_fix/{pre_images,post_images}.json`: 39 files (thirteen carriers' `_CONTEXT.md`, `_STATUS.md`, `MEMORY.md`), post-image parity verified; every transformation keyed on exactly-once text; introduced lines whitespace-checked before any write | PASS |
| N9 held-row emission | nine `instances/N9-TASK-*/STATUS.json` `PASS`; all nineteen reserved rows present once with the D-APP-109 `CYCLE_PARTICIPATING` clause; every pre-existing register line byte-identical; one new run record per carrier; `Evidence/n9_postemission_identities.json` | PASS |
| Live closure after emission | `analyze_dep_closure.py` over the live tree: 48 nodes, 124 edges, two SCCs (twenty nodes; DEL-06-03/DEL-08-01), four bidirectional pairs, four isolates; identical to `Evidence/fanin_simulation_v1/` (the picture D-APP-109 accepted) | recorded |
| N10 review | `REVIEW_v1.2.md`: PASS, BLOCKER 0 / MAJOR 0 / MINOR 8 (RV-001 to RV-008; only RV-007, the CRLF-to-LF normalization of eighteen evidence CSVs, needs N12 action, absorbed by the manifest regeneration); fan-in reproduced independently and equal to `fanin_simulation_v1`; all thirteen `_CONTEXT.md` files equal the reviewer's own re-derivation from the basis pre-image and the applied rows | PASS |
| N11 closure audit | `execution/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0807/` (manifest verified): verdict `WARNINGS`, no blocker; 52 registers, 654 rows, 148/148 endpoints; 48 nodes, 124 edges; SCCs of size 2 (DEL-06-03, DEL-08-01) and 20, equal to `fanin_simulation_v1`; delta versus the 0518 snapshot exactly the fifteen held edges added and none removed; all nineteen emitted rows carry the D-APP-109 clause; posture checks unchanged; resolution options listed per SCC without a choice; `_LATEST.md` not moved | WARNINGS (recorded SCC change, no blocker) |
| N11 decomposition audit | `execution/_Evaluation/DecompCoverage/COV_SCA_APP_010_POST_D_APP_109_2026-09-05_0807/` (manifest verified): `RUN_STATUS = WARNINGS`; 0 / 59 / 25 versus the 0518 run's 0 / 72 / 10; no new BLOCKER or MAJOR; PA-010-COV-004 resolved on all thirteen carriers with no residual (context fidelity 48 MATCH / 4 carried PARTIAL outside D-APP-109); the thirteen registers valid, anchored, carrying the nineteen emitted rows once each; `_LATEST.md` not moved | WARNINGS (no new blocker or major) |

Repository validators on the v1.2 tree (`Evidence/validation/v1.2/`): Scope of Work validator PASS ×13 (`ScopeOfWork.md` untouched); dependency schema over 52 registers: 50 VALID, the same two pre-existing failures (DEL-05-01, DEL-05-05, untouched); corpus v20, no drift; receipts VALID before the receipt rewrite; G0 to G3 exit 0; harness self-check exit 0; routed tests pass; `git diff --check` clean; candidate whitespace passes on the committed range only once the second commit lands (the first commit carried the CRLF CSVs; the normalized bytes are in this commit); frontend gates skipped, no product source changed.

Scope backcheck, v1.2 additions: the nine holding carriers' `Dependencies.csv` and `_DEPENDENCIES.md` and one new run record each; thirteen carriers' `_CONTEXT.md`, `_STATUS.md` (one history line), `MEMORY.md` (one line); `_DECISIONS/D-APP-109_*.md` (new) and one register row; two new audit snapshots; this run folder; `loop/LOOP_RECEIPTS.md` (Receipt 239 re-authored on the candidate before merge). No `ScopeOfWork.md`, `_REFERENCES.md`, `frontend/**`, `docs/**`, decomposition, companion, pointer, or Root surface changed; no `_LATEST.md` moved.

## v1.3 — owner ruling D-APP-110, decompose the SCCs (third commit on the same candidate)

| Node | Evidence | Result |
| --- | --- | --- |
| N13 ruling and workbook | `_DECISIONS/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md` and one `_REGISTER.md` row; `SCC_DECOMPOSE_RULINGS.csv` (seven rows, five edges, three contract nodes); `Evidence/scc_decompose/{decompose_choice.json,search_log.txt,carrier_work.json}`: 43 cycle-participating edges, 33 eligible (no `PREREQUISITE` row), exhaustive search finds no acyclic-making set of size one to four and, on full enumeration, two of size five (the chosen one opens the two-node SCC from the anchored DEL-06-03 side; `REVIEW_v1.3.md` RW-001); simulated strict graph acyclic after the move | PASS |
| N14 decompose writes | ten `instances/N14-TASK-*/STATUS.json` `PASS`; the seven workbook rows re-targeted exactly (`ACTIVE`, `TargetType=DOCUMENT`, `TargetPackageID` and `TargetDeliverableID` empty, workbook `TargetRefID` and `TargetLocation`, D-APP-110 clause in `Notes`); the thirteen other D-APP-109 rows Notes-only; every other register line byte-identical to `7eb4b0c7`; schema VALID on all ten registers; one new run record per carrier; no CR bytes; `git diff --check` clean; `Evidence/n14_postwrite_identities.json` (post-write SHA-256 equal to every `STATUS.json`) | PASS |
| Live closure after decompose (parent check) | `analyze_dep_closure.py` over the live tree (`Evidence/fanin_live_v1.3/`): 52 registers, 654 rows, 48 nodes, 119 strict edges, `scc_count = 0`, zero bidirectional pairs, four isolates; the strict edge set equals the 0807 snapshot's minus exactly the five decomposed edges (`DEL-02-01->DEL-02-04`, `DEL-02-02->DEL-02-04`, `DEL-02-03->DEL-02-04`, `DEL-04-05->DEL-02-05`, `DEL-06-03->DEL-08-01`), nothing added | recorded |
| N15 review | `REVIEW_v1.3.md`: PASS, BLOCKER 0 / MAJOR 0 / MINOR 4 (RW-001 to RW-004); exhaustive search reproduced independently (two minimum sets of five, the chosen one anchored); every re-targeted and Notes-only row equal to the workbook and byte-identical elsewhere; all thirty identities equal the live bytes; fan-in reproduced at 48 nodes, 119 edges, `scc_count = 0`. RW-001 (uniqueness wording), RW-003 (three missing final newlines), and RW-004 (prose miscount "twelve", correct count thirteen) repaired by HELP_HUMAN before N16 in the ruling record, register row, plan, amendment, this file, `HANDOFF_STATE.md`, the N16 brief, and `search_log.txt`; the consumed N15 brief left as read; RW-002 (superseded pre-existing Notes sentences on DEL-02-04) carried for a later refresh | PASS |
| N16 closure audit | `execution/_Reconciliation/DepClosure/CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034/` (manifest verified, 30 entries): closure verdict `PASS` (`RUN_STATUS = WARNINGS` for carried pre-existing warnings only, no blocker); analyzer `e10abf21…` run once; 52 registers, 654 rows, 141/141 ACTIVE deliverable endpoints resolved; 48 nodes, 119 strict edges, `scc_count = 0`, zero bidirectional pairs, four isolates, Kahn order over all 48 nodes; delta versus 0807 exactly the five decomposed edges removed and nothing added; row-level diff 0 added / 0 removed / 7 re-targeted / 13 Notes-only / 0 other; "Move Basis" section in the `SCC-SAFE-MOVES-001` form with every re-targeted row `ACTIVE`, `DOCUMENT`, anchored, and necessary (restoring any one re-creates an SCC); warnings carried DC-002 to DC-008 (isolates, the two legacy enum registers, the `DEP-08-01-013` Root path); `_LATEST.md` not moved | PASS (closure) |

Repository validators on the v1.3 tree (`Evidence/validation/v1.3/`): Scope of Work validator PASS ×14 (`ScopeOfWork.md` untouched; DEL-04-05 added to the sweep as the seventh re-targeted row's carrier); dependency schema over 52 registers: 50 VALID, the same two pre-existing failures (DEL-05-01, DEL-05-05, untouched); corpus v20, no drift; receipts VALID before and after the receipt rewrite; G0 to G3 exit 0; harness self-check exit 0 before and after the snapshot; routed tests pass (671); `git diff --check` clean; no CR byte in the run folder or the snapshot; candidate whitespace passes on the committed range; frontend gates skipped, no product source changed.

Scope backcheck, v1.3 additions: the ten N14 carriers' `Dependencies.csv` and `_DEPENDENCIES.md` and one new run record each; `_DECISIONS/D-APP-110_*.md` (new) and one register row; one new closure snapshot `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`; this run folder (amendment v1.3, workbook, `REVIEW_v1.3.md`, `Evidence/scc_decompose/`, `Evidence/fanin_live_v1.3/`, `Evidence/n14_postwrite_identities.json`, `Evidence/validation/v1.3/`, instances N14 to N16); `loop/LOOP_RECEIPTS.md` (Receipt 239 re-authored on the candidate before merge). No `ScopeOfWork.md`, `_CONTEXT.md`, `_STATUS.md`, `MEMORY.md`, `_REFERENCES.md`, `frontend/**`, `docs/**`, decomposition, companion, pointer, or Root surface changed; no `_LATEST.md` moved.
