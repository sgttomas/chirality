# QA Report

`AUDIT = SCC-DECOMPOSE-SCA-APP-010` (1034, after the D-APP-110 decompose move)

## Input and schema coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Dependency-register discovery | PASS | 52 `Dependencies.csv` files under `PKG-*/1_Working/DEL-*/`; `Evidence/coverage.csv` has 52 rows; every row `HasDependencyCsv=Y`. No `MISSING_DEPENDENCIES_CSV` or `UNREADABLE` deliverable. |
| v3.1 column schema (registered analyzer) | PASS | 52 valid, 0 invalid; all rows declare `RegisterSchemaVersion=v3.1`. |
| v3.1 canonical validator (`tools/validation/validate_dependencies_schema.py`, every register) | WARNING | 50/52 pass; `DEL-05-01` and `DEL-05-05` fail on `TargetType` values `CODE` and `DECISION` (`Evidence/schema_validation.json`); both registers are byte-identical to the basis and outside every SCA-APP-010 and N14 write set; all ten N14 carriers pass, including the seven new `DOCUMENT`-typed rows with empty `TargetDeliverableID`. Same finding as the 0518 and 0807 runs. |
| Evidence population | PASS | 654/654 rows carry `EvidenceFile`. |
| `IMPLEMENTS_NODE` anchors | PASS | 52 present, 0 missing. |
| Active deliverable endpoints | PASS | 141/141 resolved; 0 unresolved; 0 invalid directions; 0 misplaced; 0 DELIVERABLE-typed rows without a target (`Evidence/core_checks.json`). |
| ID normalization | PASS | 0 normalizations (`Evidence/id_normalization.csv`). |
| Analyzer / supplement agreement | PASS | Independent re-derivation agrees with the analyzer on nodes, edges, isolates, SCC count and sizes, the header-only `scc_summary.csv`, bidirectional pairs, hubs, row counts, anchors, and evidence (`Evidence/core_checks.json` `analyzerAgreement`, all true). |
| Acyclicity witness | PASS | Supplement Tarjan finds 0 non-trivial SCCs; Kahn topological sort orders all 48 connected nodes (`Evidence/topological_order.csv`). `MAX_CYCLES=10000` is not exercised; `Evidence/cycles_sample.csv` is header only. |
| Parent live-check agreement | PASS | `Evidence/fanin_agreement.json`: `closure_summary.json` identical field for field to `Evidence/fanin_live_v1.3/closure_summary.json`; SCC summary, bidirectional pairs, isolates, and hubs identical; the brief's expected `scc_count = 0`, 48 nodes, 119 edges met. |

The analyzer's `execution_rows = 381` counts ACTIVE and RETIRED rows; its graph filter consumes 360 ACTIVE EXECUTION rows, of which 141 target deliverables and collapse to 119 distinct directed edges over 48 connected nodes.

## Post-move register identities (the ten N14 carriers)

All ten `Dependencies.csv`, `_DEPENDENCIES.md`, and `_run_records/TASK_RUN_2026-09-05_*.md` files hash to the identities pinned in `Evidence/n14_postwrite_identities.json` (`Evidence/refreshed_registers.json`, `_allMatch=true`). Exactly these ten registers differ from the basis `7eb4b0c7`; the other 42, including the four remaining 0807 carriers `DEL-04-04`, `DEL-07-01`, `DEL-07-03`, and `DEL-08-03`, are byte-identical to it.

| Deliverable | `Dependencies.csv` SHA-256 | `_DEPENDENCIES.md` SHA-256 | Rows | ACTIVE | RETIRED | ACTIVE DOCUMENT rows | ACTIVE deliverable-target rows | Re-targeted | Notes-only |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| `DEL-02-01` | `b3fcca9e2ab6e5ee288a80fbf7e1b8f5869030b76edbb801070c27088808f2b1` | `58c4a9b24432d8b5af18015cefa7a6205c7b26ba881633ddbda11c44304f39f5` | 14 | 14 | 0 | 1 | 6 | `DEP-02-01-010` | - |
| `DEL-02-02` | `fd9b747956af24b6eba67ce670035aaf1b12d2d02e553f0ff504bfd2e0126dc4` | `29b2e46f990fd6683b46f2ee3e3ff4c37cad3f7dadc675a4730007a42c2763c5` | 22 | 21 | 1 | 1 | 13 | `DEP-02-02-022` | 015, 017, 018, 019, 020 |
| `DEL-02-04` | `29694c0953ecb6169cb245339803f72e7928c03378176efd4b46b0157450eb18` | `4f878d5e1096f3a2fac2116c96928c061515a11b2146ff65ad13862e3d8e9624` | 21 | 21 | 0 | 10 | 3 | 017, 018, 019 | 015, 016 |
| `DEL-02-05` | `1408edaa4cf79a1bf088cc187728eddf233f62112b35cdb770ea9a48fa50f9e7` | `9eec756b146b38560a75524e604fb5cea6c6448f3d0d30bf443ef71d86f340e0` | 15 | 15 | 0 | 1 | 5 | - | 014, 015 |
| `DEL-03-02` | `37dc1773fb3b55953167b9333187f7e6ebc486c43dafca3d899178181f0759d6` | `89d7f78298b0d58c4b85c19e0e97c89c39e6901d8d454b4c94c03a5548b05a4e` | 15 | 15 | 0 | 0 | 6 | - | 013 |
| `DEL-04-05` | `aec128ecb0369228520327eafe46a609facb6df3ec360bc5e3f3dcb42db2776a` | `d7ddb6c94f5366535362617891d2f0d41475ccd5e9229f1d9880aca7b1c1e695` | 13 | 11 | 2 | 2 | 3 | `DEP-04-05-010` | - |
| `DEL-05-02` | `090241fe899c9c57da14485b271fb3ed986ab2f9a12d8b95c87223b39023f4ca` | `3a48e72adb46dfa7164a817b3f0ef1b1d3dc7eaabdec9590f6e71d83089373b2` | 16 | 15 | 1 | 1 | 6 | - | 016 |
| `DEL-06-03` | `8b48a970881eb20460fc0d65db94d77f08d04a85cd2aaac3b90a9b9ba8b62135` | `3599bc1d55ae52e12a65b252179b0d7e142f31973f5d224db6b033a619da2e9f` | 18 | 18 | 0 | 3 | 4 | `DEP-06-03-014` | - |
| `DEL-08-01` | `3cdd199b1fffe1be2cb7985d563a2f1be154aecfdaec6b3657a23c99751b0d96` | `de76f73f3ecc9623013693ced29eed8f4e0efd71a5568a27c77887d1e9d1f7d8` | 21 | 21 | 0 | 8 | 2 | - | 018 |
| `DEL-08-04` | `8f482b56dd1e72cebf30615cb4104d8fbc8357a375cf29add648884d02e7e515` | `c5d1d094b06e4e65b0b239a9d46780adf4668d1de441143ff430442735ddd4d6` | 14 | 13 | 1 | 1 | 2 | - | 013 |

The ACTIVE deliverable-target row counts are 1, 1, 3, 0, 0, 1, 0, 1, 0, 0 lower than in the 0807 run for the ten carriers respectively (7 in total, the seven re-targeted rows); the ACTIVE DOCUMENT row counts are correspondingly higher.

## Move basis (check 3)

`Evidence/move_basis.json` (`allRowsPass=true`, `workbookEqualsDecomposeChoice=true`, `retargetedRowsInRegistersEqualWorkbook=true`, `edgesRemovedEqualWorkbookEdges=true`, `allDecomposedEdgesNecessary=true`, `allContractAnchorFragmentsFound=true`): the seven workbook rows are present exactly once in their carriers, `ACTIVE`, `EXECUTION`, `TargetType=DOCUMENT`, `TargetPackageID` and `TargetDeliverableID` empty, `TargetRefID`/`TargetName`/`TargetLocation` equal to the workbook, `Direction` and `DependencyType` unchanged and eligible (four `INTERFACE`, three `HANDOVER`; no `PREREQUISITE`), `Notes` carrying `DECOMPOSE 2026-09-05 under D-APP-110 (SD-nnn)` with the replaced edge and the preserved relation; basis `TargetType`/`TargetDeliverableID` equal the workbook `Previous*` fields; the basis-derived edge equals the workbook `GraphEdge`, is in the 0807 edge list under that `DependencyID`, and is absent from the live strict graph. Row-level diff over all 52 registers against the basis: 0 rows added, 0 removed, 0 `Status` changes (no row retired), 0 `Direction` changes (no row inverted), 0 `PREREQUISITE` rows re-targeted or changed in any field but `Notes` (four `PREREQUISITE` rows received the resolved clause; `Decision_Log.md` DEC-007), 0 rows changed outside the seven re-targeted and the thirteen Notes-only rows.

## Closure (check 4)

- Strict graph: 48 nodes, 119 edges, `scc_count = 0`, `Evidence/scc_summary.csv` header only, 0 bidirectional pairs (the analyzer reports none), 4 isolates (`DEL-01-01`, `DEL-09-07`, `DEL-10-04`, `DEL-10-05`, unchanged), 0 hubs at degree 20 (highest degree `DEL-09-02` at 15).
- Delta versus 0807 (`Evidence/delta_vs_0807.json`): the basis registers reproduce the 0807 edge list exactly; edges removed = exactly the five workbook edges; edges added = 0; common edges with changed carrying rows = 0; the four 0807 bidirectional pairs all dissolved; isolates and hubs unchanged.
- Delta versus the pre-extraction baseline (`Evidence/delta_vs_baseline.json`): 46 -> 48 nodes, 99 -> 119 edges, 6 -> 4 isolates, SCC [9] -> [].
- The thirteen other D-APP-109 rows (`Evidence/resolved_rows.json`, `allRowsPass=true`): each `ACTIVE EXECUTION DELIVERABLE`, changed in `Notes` only, carrying the `RESOLVED 2026-09-05` clause naming D-APP-110 and "gates per its SatisfactionStatus", each a strict edge of the live graph inside no SCC; `SatisfactionStatus` PENDING x10, TBD x3. Six re-targeted emitted rows plus the thirteen are exactly the nineteen H-001 to H-019 (`retargetedFromEmittedPlusResolvedEqualsNineteen=true`); `DEP-04-05-010` is pre-existing.

## Posture checks (check 5)

- Descendant classes: DEL-08-04 managed `DEP-08-04-009`, native `DEP-08-04-010`; DEL-08-05 managed `DEP-08-05-004`, native `DEP-08-05-011`; each class once per carrier; the native rows deny Agent-role inference (`Evidence/posture_checks.json` `descendantClasses`).
- E-018, E-020, E-032: no live feedback row in either carrier; only the accepted gating orientations are materialized (E-020 by `DEP-08-04-006`, `DEP-08-05-004`, `DEP-08-05-011`; E-032 by `DEP-09-05-009`; E-018 by no row). The E-018 and E-020 node pairs, enclosed by the 0807 `SCC-002`, now lie inside no live SCC. `DAG.md` SHA-256 `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996` verified live.
- EXTERNAL rows in the fourteen swept carriers (the 0807 thirteen plus `DEL-04-05`): 18; 16 with `TargetLocation=TBD`; the two exceptions are the pre-existing descendant-class rows pointing at the repo-relative App decomposition; every Root-named EXTERNAL row has `TargetLocation=TBD`; no re-targeted row is EXTERNAL or carries an absolute path. Absolute path in the swept carriers: `DEP-08-01-013` only, byte-identical to the basis in every field (`identicalToBasis=true`).

## Analyzer limitations and supplements

- The registered analyzer does not emit an edge list or `cycles_sample.csv`; `Evidence/edge_list.csv` and the header-only `Evidence/cycles_sample.csv` are deterministic supplements over the analyzer's own filters (`Decision_Log.md` DEC-003, DEC-006).
- The analyzer labels isolated deliverables as orphans in `orphans.csv`; with zero unresolved endpoints the entries are isolates, not dangling targets (DEC-004).
- The analyzer's CSVs use CRLF line endings and its JSON lacks a final newline; both were normalized after parsing with recorded lineage (DEC-003):

| File | Analyzer SHA-256 | Normalized SHA-256 | Change |
| --- | --- | --- | --- |
| `Evidence/bidirectional_pairs.csv` | `e0fcf0084fce3ec4ebb162e6d9e7430e6bde0eeb759307d8b6716301cf950c59` | `96763837f083b613c05053bee7e700c98f7abff516e73ecc31d7ba6589143243` | 1 CRLF -> LF |
| `Evidence/coverage.csv` | `0586c5b5b054682f218bf85f001ae668ac0217f79b0f86b8f18c6ddd96f4d644` | `e16517aced3fe9b0a3d6003790ce7b5147da5105fa49db61a560637d2970ea78` | 53 CRLF -> LF |
| `Evidence/hubs.csv` | `461b09cff46fadec5ae392e5feae820b87bd608ec22935ff7eb4e33c5fb9b5c0` | `2a8f48c7ddbe9ae0266d826695bd86419362cb584f503b09d373e0128c49b955` | 1 CRLF -> LF |
| `Evidence/id_normalization.csv` | `1e1dc4b14515b25fd32c69e7b965d4e9ba4f5489ce3ea5d46fad2e9c938dd2f3` | `24820fc7cf0c53df91c2616321418bd6684c723bc71109267ef98a25ca94fd9c` | 1 CRLF -> LF |
| `Evidence/orphans.csv` | `fb160cb2f4f9c22aa6a44817bc820014fa09278be09e4adda115972297a6dd27` | `e5d2eb60afa8e92ac95e0798462a7d52edb6cff69059f1aa12270c6f7ca7728f` | 5 CRLF -> LF |
| `Evidence/scc_summary.csv` | `1cd736c87b44cb483cf3cd64a2376a19821a7f50fe6b6dbaadb842ba21b20e7d` | `2951a8e40268d483dba0101bd83e04c53ccf3236818353af6b3039c68d896578` | 1 CRLF -> LF |
| `Evidence/closure_summary.json` | `180ff9d2bf5e805e0c9757456b9b0704fe75a4880321b19a7a6a9b5ebf23dbd6` | `8ef85cb14932831860d951af6afdd70737fe688593a3e1ce2cf6cd93d20b3253` | 0 CRLF -> LF; final LF added |

`coverage.csv`, `hubs.csv`, `id_normalization.csv`, and `orphans.csv` are byte-identical to their 0807 counterparts after normalization (same analyzer and normalized hashes), as the unchanged register count, isolates, and hub result imply.

- The analyzer's schema check is column-level; enum conformance was checked separately with the canonical validator (DEC-008).

## Observations for the parent (outside this audit's write scope)

- The RW-001, RW-003, and RW-004 repairs named in the dispatch are present in the run folder: `search_log.txt` carries the full-enumeration line; `carrier_work.json`, `decompose_choice.json`, and `fanin_live_v1.3/closure_summary.json` end with a final LF; the D-APP-110 ruling, the amendment, `HANDOFF_STATE.md`, and `ORCHESTRATION_PLAN.md` no longer say "twelve". The one remaining occurrence of "twelve" in `VALIDATION_EVIDENCE.md` (line 86) is the RW-004 repair description quoting the corrected miscount ("prose miscount \"twelve\", correct count thirteen"), not an uncorrected count.
- `HANDOFF_STATE.md` carries the placeholder for this snapshot's name; the name is `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`.

## Write containment

This dedicated auditor modified no register, deliverable file, decomposition, prior snapshot, `docs/**`, `frontend/**`, or Root surface. It wrote only this snapshot and the two control files `RETURN.md` and `STATUS.json` under `instances/N16-AUDIT-DEP-CLOSURE/`. No `_Evaluation/DepClosure/` path was created and no `_LATEST.md` pointer was created or moved (`_Reconciliation/DepClosure/_LATEST.md` still names `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`). No Git state-changing command (only `git rev-parse`, `git branch --show-current`, `git status`, `git diff` and `git diff --stat` against the basis, `git check-ignore`, and `git show 7eb4b0c7:<register>`) and no network access was used. The single helper script lived only in a private scratchpad subfolder (supplement SHA-256 `cf61f8f4b2bac7f91f614c2e9e2afb63affb9e6c3f454231e228fa901527c9de`). No `__pycache__` was created under `tools/` by this audit (`Decision_Log.md` DEC-016). Working-tree observation only: the ten N14 carriers' untracked `_run_records/TASK_RUN_2026-09-05_*.md` files and the run folder's v1.3 files show in `git status`; none is an analyzer input and none was read beyond the files named in the brief and the dispatch.
