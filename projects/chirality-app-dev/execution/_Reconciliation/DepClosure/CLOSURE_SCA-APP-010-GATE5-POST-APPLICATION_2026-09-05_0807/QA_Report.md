# QA Report

`AUDIT = SCA-APP-010-GATE5-POST-APPLICATION` (second run, 0807, post D-APP-109 emission)

## Input and schema coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Dependency-register discovery | PASS | 52 `Dependencies.csv` files under `PKG-*/1_Working/DEL-*/`; `Evidence/coverage.csv` has 52 rows; every row `HasDependencyCsv=Y`. No `MISSING_DEPENDENCIES_CSV` or `UNREADABLE` deliverable. |
| v3.1 column schema (registered analyzer) | PASS | 52 valid, 0 invalid; all rows declare `RegisterSchemaVersion=v3.1`. |
| v3.1 canonical validator (`tools/validation/validate_dependencies_schema.py`, every register) | WARNING | 50/52 pass; `DEL-05-01` and `DEL-05-05` fail on `TargetType` values `CODE` and `DECISION` (`Evidence/schema_validation.json`); both registers are byte-identical to `HEAD` and outside every SCA-APP-010 write set; all thirteen carriers pass, including the nine that received emitted rows. Same finding as the 0518 run. |
| Evidence population | PASS | 654/654 rows carry `EvidenceFile`. |
| `IMPLEMENTS_NODE` anchors | PASS | 52 present, 0 missing. |
| Active deliverable endpoints | PASS | 148/148 resolved; 0 unresolved; 0 invalid directions; 0 misplaced (`Evidence/core_checks.json`). |
| ID normalization | PASS | 0 normalizations (`Evidence/id_normalization.csv`). |
| Analyzer / supplement agreement | PASS | Independent re-derivation agrees with the analyzer on nodes, edges, isolates, SCC sizes and membership, bidirectional pairs, hubs, and row counts (`Evidence/core_checks.json` `analyzerAgreement`, all true). |
| Fan-in simulation agreement | PASS | `Evidence/fanin_agreement.json`: SCC set identical to `fanin_simulation_v1/scc_summary.csv`; `closure_summary.json` identical field for field; bidirectional pairs and isolates identical. |
| Cycle enumeration | PASS (complete) | Johnson enumeration inside each SCC terminated below `MAX_CYCLES=10000` (65 elementary cycles in total: 1 in the two-node SCC, 64 in the twenty-node SCC); an independent depth-first enumeration over `Evidence/edge_list.csv` reproduced both counts and length histograms (`Decision_Log.md` DEC-007). |

The analyzer's `execution_rows = 381` counts ACTIVE and RETIRED rows; its graph filter consumes 360 ACTIVE EXECUTION rows, of which 148 target deliverables and collapse to 124 distinct directed edges over 48 connected nodes.

## Post-emission register identities (check 2)

All thirteen `Dependencies.csv` and `_DEPENDENCIES.md` files hash to the identities pinned in the sealed brief (`Evidence/refreshed_registers.json`, `_allMatch=true`). Exactly nine of them differ from `HEAD` (`f38f1448`): the nine carriers that received emitted rows (`Evidence/delta_vs_0518.json` `registersChangedVsHEAD`). `DEL-04-04`, `DEL-07-01`, `DEL-07-03`, and `DEL-08-03` are byte-identical to `HEAD` and to their 0518 identities.

| Deliverable | `Dependencies.csv` SHA-256 | Match | `_DEPENDENCIES.md` SHA-256 | Match | Rows | ACTIVE | RETIRED | ACTIVE deliverable-target rows |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| `DEL-02-01` | `8d5315713a86732e44b4a9287e8632be03347d50ceb1d2ed7889c2b90cc8883e` | match | `f6a50a4513cc2d5895d81fe93a4b9ee45e43714f1a16234adf7c188b52e2c517` | match | 14 | 14 | 0 | 7 |
| `DEL-02-02` | `9feb11b0b1aa312eed09fa70de685c6a630f3b5fd717e2b6d774c75e336ec9a0` | match | `2b6d3b9935c857b089a80453e5b6f1c8b18162a30c15a79024ad47499610341d` | match | 22 | 21 | 1 | 14 |
| `DEL-02-04` | `abaf816695c2c6f13adfe03ad85b31ff0cbdef2db06b36873e519060f306bcb2` | match | `1cefdede31815de94d3f18b2e5033fbc1ebf17722f4a4d53c8e22f5eb0ec23ca` | match | 21 | 21 | 0 | 6 |
| `DEL-02-05` | `09aaacc8894bd4ffb1cdd48f09416d19dca368fe4e64f890234855af9bd9c703` | match | `5d93d935017bb99aa24834560488c753f73a825af6e97441e519229cf4b3a501` | match | 15 | 15 | 0 | 5 |
| `DEL-03-02` | `0e65c1a38383958ce83d4c77b6671efd24651ff6affc7d4694aaee4304c416ad` | match | `0144084fff0696e0854e919ca831cf2ea0c3779d1c95ff81fb24a00daad50051` | match | 15 | 15 | 0 | 6 |
| `DEL-04-04` | `1cb90e1ff30b50fb08c9f9f06aa65ad74ac63b92ab0ebbcecdf52ec93cde8034` | match | `1896ed236a76269842419a20021d9b1691da2e3b30dea3e5db9dbd2df42cb352` | match | 14 | 13 | 1 | 4 |
| `DEL-05-02` | `c26d4653b0eacd1eea65bd23ba3b14e59c4749bb18a853f82cc8e3fdf949879d` | match | `3c86ae3fbc52b5c84264c8656f58c7ba0decd3e52508cb07ca3aca041f4bdf51` | match | 16 | 15 | 1 | 6 |
| `DEL-06-03` | `15ea08e35b5d2dda40dfc417b3d0ff4e73318900ccab166f016b5dee3cb2f3cd` | match | `9e3faf5dcaf6c02a3f88c39006ff830e24b90057b50d1cd37ba3ba4fb0a32cb0` | match | 18 | 18 | 0 | 5 |
| `DEL-07-01` | `9c8e0405599f5077d450d92e8934c0664e25b5c193bb12e90d1c11b2af6a982f` | match | `b6b1fbb7436f9d1ef10fdad5af82e04c48bb9a0f5fe5db64fe4d3bb2847adac9` | match | 12 | 11 | 1 | 2 |
| `DEL-07-03` | `54d8dc8cff7338b164264eee9a7dd6a48e6bd364177a38e50ee4991e166715ed` | match | `8c8fe0324138c219493cae174545d6e5b4674f6db16ba8a6700059945fbfb297` | match | 14 | 14 | 0 | 4 |
| `DEL-08-01` | `e0e0102a6f743911d23c36892e8b6f7ff4d45c88820d705f1475c883d3836284` | match | `673460ea86ca6330067cdf7c5f30ef5fff35a308cdebb4beef2659394c33f7c4` | match | 21 | 21 | 0 | 2 |
| `DEL-08-03` | `7981ea6078052e96eebbaed06dade989e094260d659347e2eb8812f8a3fb7727` | match | `d8fbef7de157f70276c0cc90bd752802f4b8f61ba8f820a80c6a4620c8cf9294` | match | 10 | 10 | 0 | 0 |
| `DEL-08-04` | `3eb0f762ccb4a59d7a92f64f1589a41e390680de21289289ed08f89198590aef` | match | `b5123a21266a30b5e41892a2bc9bcc583f3fbebe3cbac481f3a4daff23ed6c2d` | match | 14 | 13 | 1 | 2 |

## Emitted rows (check 4)

`Evidence/emitted_rows.json`: each of the nineteen reserved `DependencyID`s (H-001 to H-019) is present exactly once, in its carrier's register, with `Status=ACTIVE`, `DependencyClass=EXECUTION`, `TargetType=DELIVERABLE`, and `Direction`, `DependencyType`, and `TargetDeliverableID` equal to `HELD_EDGE_PROPOSALS.csv`; the derived edge equals the held edge; every `Notes` field carries `CYCLE_PARTICIPATING`, the non-gating clause, and `D-APP-109`; the nineteen are exactly the `CYCLE_PARTICIPATING` rows in the corpus. Row-level diff against `HEAD` over all 52 registers: 19 rows added (the reserved IDs), 0 removed, 0 rows with any changed field (`Evidence/delta_vs_0518.json` `rowLevelTotals`).

## Posture checks (checks 3, 5, 6)

- SCC set: `SCC-001` = `DEL-06-03;DEL-08-01` (2), `SCC-002` = the twenty nodes listed in `Evidence/scc_summary.csv`; equal to the accepted fan-in simulation; the former nine-node SCC is a subset of `SCC-002` (`priorSCC001SubsetOfLiveSCC002=true`). Edges added versus 0518: 15, equal to the held-edge set; removed: 0; SCC-internal edges retired: 0; carrying rows of every pre-existing edge unchanged.
- Bidirectional pairs: `DEL-02-02/DEL-02-04`, `DEL-02-03/DEL-02-04`, `DEL-02-05/DEL-04-05`, `DEL-06-03/DEL-08-01` (expected four; `Evidence/fanin_agreement.json` `bidirectionalPairsEqualExpected=true`). Isolates: `DEL-01-01`, `DEL-09-07`, `DEL-10-04`, `DEL-10-05` (unchanged). Hubs: none.
- Descendant classes: DEL-08-04 managed `DEP-08-04-009`, native `DEP-08-04-010`; DEL-08-05 managed `DEP-08-05-004`, native `DEP-08-05-011`; each class once per carrier; the native rows deny Agent-role inference (`Evidence/posture_checks.json` `descendantClasses`).
- E-018, E-020, E-032: no live feedback row in either carrier; only the accepted gating orientations are materialized. New observation: the E-018 pair (`DEL-05-04`, `DEL-02-05`) and the E-020 pair (`DEL-08-05`, `DEL-08-04`) now both lie inside live `SCC-002` (they did not lie inside any live SCC in the 0518 run); E-032's pair does not. They remain objective-relative and non-gating; no row was invented and no mapping between the accepted DAG's SCCs and the live SCCs is asserted (DEC-010).
- EXTERNAL rows in the thirteen carriers: 18; 16 with `TargetLocation=TBD`; the two exceptions are the pre-existing descendant-class rows pointing at the repo-relative App decomposition; every Root-named EXTERNAL row has `TargetLocation=TBD`. Absolute path in the thirteen carriers: `DEP-08-01-013` only, byte-identical to `HEAD` (`identicalToHEAD_0518=true`).

## Analyzer limitations and supplements

- The registered analyzer does not emit `cycles_sample.csv`; the bounded enumeration in `Evidence/cycles_sample.csv` is a deterministic supplement over the analyzer's own edge set (see `Decision_Log.md` DEC-003, DEC-007).
- The analyzer labels isolated deliverables as orphans in `orphans.csv`; with zero unresolved endpoints the entries are isolates, not dangling targets (DEC-004).
- The analyzer numbers SCCs in Tarjan discovery order; in this run `SCC-001` is the two-node component and `SCC-002` the twenty-node component, the same labels the fan-in simulation used (DEC-006).
- The analyzer's CSVs use CRLF line endings and its JSON lacks a final newline; both were normalized after parsing with recorded lineage (DEC-003):

| File | Analyzer SHA-256 | Normalized SHA-256 | Change |
| --- | --- | --- | --- |
| `Evidence/bidirectional_pairs.csv` | `0af238afab0ce61496b62d3f60c61d673adeb26ec098bb238e2dfe50ee1888a7` | `f9f6216b2b3aa8a58fa93cb0ecc2642aa2c98a722b87b8fffa7f548791892b42` | 5 CRLF -> LF |
| `Evidence/coverage.csv` | `0586c5b5b054682f218bf85f001ae668ac0217f79b0f86b8f18c6ddd96f4d644` | `e16517aced3fe9b0a3d6003790ce7b5147da5105fa49db61a560637d2970ea78` | 53 CRLF -> LF |
| `Evidence/hubs.csv` | `461b09cff46fadec5ae392e5feae820b87bd608ec22935ff7eb4e33c5fb9b5c0` | `2a8f48c7ddbe9ae0266d826695bd86419362cb584f503b09d373e0128c49b955` | 1 CRLF -> LF |
| `Evidence/id_normalization.csv` | `1e1dc4b14515b25fd32c69e7b965d4e9ba4f5489ce3ea5d46fad2e9c938dd2f3` | `24820fc7cf0c53df91c2616321418bd6684c723bc71109267ef98a25ca94fd9c` | 1 CRLF -> LF |
| `Evidence/orphans.csv` | `fb160cb2f4f9c22aa6a44817bc820014fa09278be09e4adda115972297a6dd27` | `e5d2eb60afa8e92ac95e0798462a7d52edb6cff69059f1aa12270c6f7ca7728f` | 5 CRLF -> LF |
| `Evidence/scc_summary.csv` | `fcbc6d22f8cee554212ccffd67034a05519e49cb61afede23ca00739af8820e7` | `d93746d9434ccc347625c048088b2e90fd683ea58d6e92210e0cad7854fd05eb` | 3 CRLF -> LF |
| `Evidence/closure_summary.json` | `c7f934068b02bf3bee76196a4bbe914c87c06515d56c4b18b579e48119955920` | `5857a6f33ace955c0b5708057da319738ef1ebc50f6d114133649bd9ad87fab6` | 0 CRLF -> LF; final LF added |

- The analyzer's schema check is column-level; enum conformance was checked separately with the canonical validator (DEC-008).

## Write containment

This dedicated auditor modified no register, deliverable file, decomposition, snapshot, `docs/**`, `frontend/**`, or Root surface. It wrote only this snapshot and the two control files `RETURN.md` and `STATUS.json` under `instances/N11-AUDIT-DEP-CLOSURE/`. No `_Evaluation/DepClosure/` path was created and no `_LATEST.md` pointer was created or moved (`_Reconciliation/DepClosure/_LATEST.md` still names `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`). No Git state-changing command (only `git rev-parse`, `git status`, `git log`, and `git show HEAD:<register>`) and no network access was used. The two helper scripts lived only in a private scratchpad subfolder (supplement SHA-256 `520d4a100a46867ae4a447bf6e99c8d9df8a8d3a8e90352cbed6a8ad66747063`; cycle-participation helper SHA-256 `55d9274d26b1178cb77232f8282f6896d697d02ac44eb04f0190d2b630644d16`). Working-tree observation only: untracked `_run_records/TASK_RUN_2026-09-05_*.md` files exist under the nine N9 carriers and the run folder's baseline and simulation CSVs show as modified in `git status`; none is an analyzer input and none was read for this audit beyond the simulation files named in the brief.
