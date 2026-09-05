# QA Report

`AUDIT = SCA-APP-010-GATE5-POST-APPLICATION`

## Input and schema coverage

| Check | Result | Evidence |
| --- | --- | --- |
| Dependency-register discovery | PASS | 52 `Dependencies.csv` files under `PKG-*/1_Working/DEL-*/`; `Evidence/coverage.csv` has 52 rows; every row `HasDependencyCsv=Y`. No `MISSING_DEPENDENCIES_CSV` or `UNREADABLE` deliverable. |
| v3.1 column schema (registered analyzer) | PASS | 52 valid, 0 invalid; all rows declare `RegisterSchemaVersion=v3.1`. |
| v3.1 canonical validator (`tools/validation/validate_dependencies_schema.py`, every register) | WARNING | 50/52 pass; `DEL-05-01` and `DEL-05-05` fail on `TargetType` values `CODE` and `DECISION` (`Evidence/schema_validation.json`); both registers are byte-identical to the basis and outside the refresh; all thirteen refreshed registers pass. |
| Evidence population | PASS | 635/635 rows carry `EvidenceFile`. |
| `IMPLEMENTS_NODE` anchors | PASS | 52 present, 0 missing. |
| Active deliverable endpoints | PASS | 129/129 resolved; 0 unresolved; 0 invalid directions (`Evidence/core_checks.json`). |
| Misplaced fields | PASS | 0 ACTIVE EXECUTION rows with a non-DELIVERABLE `TargetType` and a populated `TargetDeliverableID`. |
| ID normalization | PASS | 0 normalizations (`Evidence/id_normalization.csv`). |
| Analyzer / supplement agreement | PASS | Independent re-derivation agrees with the analyzer on nodes, edges, isolates, SCC sizes, bidirectional pairs, hubs, and row counts (`Evidence/core_checks.json` `analyzerAgreement`). |
| Baseline reproduction | PASS | Basis graph reconstructed from `git show HEAD:` for all 52 registers reproduces the baseline snapshot's nodes, edges, isolates, and SCC (`Evidence/delta_vs_baseline.json` `baselineSnapshotAgreement`). |

The analyzer's `execution_rows = 362` counts ACTIVE and RETIRED rows; its graph filter consumes 341 ACTIVE EXECUTION rows, of which 129 target deliverables and collapse to 109 distinct directed edges over 48 connected nodes.

## Refreshed-register identities (check 4)

All thirteen `Dependencies.csv` and `_DEPENDENCIES.md` files hash to the identities pinned in the sealed brief (`Evidence/refreshed_registers.json`, `_allMatch=true`). They are exactly the registers that differ from `HEAD` in the working tree (`Evidence/delta_vs_baseline.json` `changedRegisters`).

| Deliverable | `Dependencies.csv` SHA-256 | Match | `_DEPENDENCIES.md` SHA-256 | Match | Rows | ACTIVE | RETIRED | ACTIVE deliverable-target rows |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: |
| `DEL-02-01` | `4af3d115b79d403c190661ba57050abe9bda04539cadf09cf9b07edf2d49c254` | match | `26a99f29ef68e00a9cc02839802142f099f67f7c5816cb461971a9ccb9a3ef49` | match | 13 | 13 | 0 | 6 |
| `DEL-02-02` | `d4f6dad83cc9538186214b6ab9a116c85c6ae2a8578acfb5a65acd56e61c3cff` | match | `adeb89260b62b2a86268b99505f08a6df2ea2eb98a22185961767fbad09b1df0` | match | 16 | 15 | 1 | 8 |
| `DEL-02-04` | `c6bdffd1aef83f0c04764a8f8f01d5f67abc1928c9630866f6f48dd83d16ac62` | match | `1fffa1ec5e37709dcb26f0c1b0cd611e3ae474690db63593a85e6bd2c50ba35e` | match | 16 | 16 | 0 | 1 |
| `DEL-02-05` | `03d3d7bcf405e98e7096d24f6322b2a7bc0fd68a239e620f8d27191616c66f17` | match | `5dfb3da66a0c128569e0fd9714a65a14df28c3d2ffa5cedf710cc3b40d21fcc9` | match | 13 | 13 | 0 | 3 |
| `DEL-03-02` | `be877cffd700069afae17a3f604af28bc2e666c5608b833aff814ce51c291458` | match | `dffe9d126bebeb967dc9e0a109c528b44b22b7daf374cda4079f3fc349da7eb8` | match | 14 | 14 | 0 | 5 |
| `DEL-04-04` | `1cb90e1ff30b50fb08c9f9f06aa65ad74ac63b92ab0ebbcecdf52ec93cde8034` | match | `1896ed236a76269842419a20021d9b1691da2e3b30dea3e5db9dbd2df42cb352` | match | 14 | 13 | 1 | 4 |
| `DEL-05-02` | `7a6da98003c9fc93caf3c602c09e242abb6105e90a1e45cff25e67d4a18f5380` | match | `8823be430d59a5060bff63a17d1474ff48c09ddc77a2ee7006dec0c7a91539a0` | match | 15 | 14 | 1 | 5 |
| `DEL-06-03` | `89a579e740656560f565c41c9f536dbfe99038d86d65faae93f882134f682d02` | match | `d9140c2f599150cd3f7ab82124b12a3aad6b0a137a6c5636d4cf37f89bba3800` | match | 17 | 17 | 0 | 4 |
| `DEL-07-01` | `9c8e0405599f5077d450d92e8934c0664e25b5c193bb12e90d1c11b2af6a982f` | match | `b6b1fbb7436f9d1ef10fdad5af82e04c48bb9a0f5fe5db64fe4d3bb2847adac9` | match | 12 | 11 | 1 | 2 |
| `DEL-07-03` | `54d8dc8cff7338b164264eee9a7dd6a48e6bd364177a38e50ee4991e166715ed` | match | `8c8fe0324138c219493cae174545d6e5b4674f6db16ba8a6700059945fbfb297` | match | 14 | 14 | 0 | 4 |
| `DEL-08-01` | `1f616ed9ed997a5cbd6e19114930e9c9055bd44313be7fe5954ac93d03c768f6` | match | `09321d20219a27017c74f99da5d84f8c2f8bed10832b008304bf09d38ca3e57a` | match | 20 | 20 | 0 | 1 |
| `DEL-08-03` | `7981ea6078052e96eebbaed06dade989e094260d659347e2eb8812f8a3fb7727` | match | `d8fbef7de157f70276c0cc90bd752802f4b8f61ba8f820a80c6a4620c8cf9294` | match | 10 | 10 | 0 | 0 |
| `DEL-08-04` | `902678b137b5600f0cd2202519b7906122c29168d74ab48846ca99b2f41d84e5` | match | `8d66e9dd97d16e2746ca295f01dab051fb9ac981accced36ef76855e9cd074c0` | match | 13 | 12 | 1 | 1 |

## Posture checks (checks 5 to 7)

- SCC-001 membership identical to baseline and SCA-APP-008; SCC-internal edges added: 0; retired: 0; new SCCs: 0; new cycles: 0 (`Evidence/delta_vs_baseline.json`, `Evidence/delta_vs_sca_app_008.json`, `Evidence/cycles_sample.csv`).
- Descendant classes: DEL-08-04 managed `DEP-08-04-009`, native `DEP-08-04-010`; DEL-08-05 managed `DEP-08-05-004`, native `DEP-08-05-011`; the native rows state that no Agent 0/1/2 role is assigned (`Evidence/posture_checks.json` `descendantClasses`). The text heuristic also lists DEP-08-05-004 under `nativeClassRows` because its Notes contrast the managed class with native descent; the row itself is the managed-class row.
- E-018, E-020, E-032: no live feedback row in either carrier; only the accepted gating orientations are materialized (`Evidence/posture_checks.json` `acceptedObjectiveEdges`).
- EXTERNAL rows in the thirteen carriers: 18; 16 with `TargetLocation=TBD`; the two exceptions are the pre-existing descendant-class rows pointing at the repo-relative App decomposition. Absolute Root path in the thirteen carriers: `DEP-08-01-013` only, pre-existing and byte-identical at basis.
- Held proposals: 19 rows / 15 edges non-emitted; reserved IDs absent from all live registers; held edges absent from the live graph.

## Analyzer limitations and supplements

- The registered analyzer does not emit `cycles_sample.csv`; the bounded enumeration in `Evidence/cycles_sample.csv` is a deterministic supplement over the analyzer's own edge set (see `Decision_Log.md` DEC-003).
- The analyzer labels isolated deliverables as orphans in `orphans.csv`; with zero unresolved endpoints the entries are isolates, not dangling targets (DEC-004).
- The analyzer's CSVs use CRLF line endings and its JSON lacks a final newline; both were normalized after parsing with recorded lineage (DEC-003):

| File | Analyzer SHA-256 | Normalized SHA-256 | Change |
| --- | --- | --- | --- |
| `Evidence/bidirectional_pairs.csv` | `93fea38e2e8f109b4213960c3f1429988f16646ca385d6668597441f026d7dd8` | `fc8d468c5226c825760791d6e4811226fa1fe6b260e456131f80dcaba2ea55f5` | 2 CRLF -> LF |
| `Evidence/coverage.csv` | `00cb9b9ce1dd4b7de01b09cb2717213ef3856fa0945c709880d1b68e6e3f0c9f` | `8f86a528e35b27d083868f13838ba7edd922d8375ba8bbb6e133faf0acb3ce61` | 53 CRLF -> LF |
| `Evidence/hubs.csv` | `461b09cff46fadec5ae392e5feae820b87bd608ec22935ff7eb4e33c5fb9b5c0` | `2a8f48c7ddbe9ae0266d826695bd86419362cb584f503b09d373e0128c49b955` | 1 CRLF -> LF |
| `Evidence/id_normalization.csv` | `1e1dc4b14515b25fd32c69e7b965d4e9ba4f5489ce3ea5d46fad2e9c938dd2f3` | `24820fc7cf0c53df91c2616321418bd6684c723bc71109267ef98a25ca94fd9c` | 1 CRLF -> LF |
| `Evidence/orphans.csv` | `fb160cb2f4f9c22aa6a44817bc820014fa09278be09e4adda115972297a6dd27` | `e5d2eb60afa8e92ac95e0798462a7d52edb6cff69059f1aa12270c6f7ca7728f` | 5 CRLF -> LF |
| `Evidence/scc_summary.csv` | `bdb6da3782a576c602072c9b40574b5f2c2112619b5ab02973ff8a381dcb8226` | `348508f92d0033220fd7cfbc8770f47df35af8218ff0f1bd7aa246016d3dc8e3` | 2 CRLF -> LF |
| `Evidence/closure_summary.json` | `8b3204880da234ac7f331f440ce02e59e825dd22e565d1c3f9422615dd3bcdcf` | `26b9885cf350fae02473d6fddeb1d09e5b362d536e691869e061f8be3ab8c84a` | 0 CRLF -> LF; final LF added |

- The analyzer's schema check is column-level; enum conformance was checked separately with the canonical validator (DEC-007).

## Write containment

This dedicated auditor modified no register, deliverable file, decomposition, snapshot, `docs/**`, `frontend/**`, or Root surface. It wrote only this snapshot and the two control files `RETURN.md` and `STATUS.json` under `instances/N4-AUDIT-DEP-CLOSURE/`. No `_Evaluation/DepClosure/` path was created and no `_LATEST.md` pointer was created or moved. No Git state-changing command and no network access was used. Working-tree observation only: untracked `_run_records/TASK_RUN_2026-09-05_*.md` files exist under the thirteen refreshed carriers from the N3 writes; they are not inputs to the analyzer and were not read for this audit.
