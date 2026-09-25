---
amendment_id: SCA-005
doc_kind: scope_change.run_summary
decomp_variant: SOFTWARE
checkpoint_group: 3
created: 2026-09-25
status: checkpoint_3_prepared_awaiting_owner
---

# SCA-005 Run Summary — checkpoint-group-3 preparation

## Amendment

SCA-005 re-bases PEC's feed model on the shared development-loop method and
the application-owned Runtime topology (D-GOV-43 A2): decomposition revision
1.4 → 1.5 and PRD v2.2 → v2.3. It adds SOW-095/096 and DEL-02-08/09
(work-graph and MEMORY run-index parsers), re-sources the record-tier entity
model, receipts, run evidence, dependency and LOOP_INIT parsers, declares
per-loop feed profiles on registry rows, makes `adapter.yaml` a parity-peer
input, defers SOW-029/035/087 (trigger T-RT) and SOW-037 (cmux) to OUT, and
retires DEL-06-04, DEL-07-02, DEL-07-04 and DEL-07-05 non-destructively. 79
actions (8 ADD / 67 MODIFY / 4 REMOVE; `Amendment_Actions_CP2.csv`).

Authority: owner checkpoint-2 acceptance of 2026-09-25 ("CP2: accept; Q1 a; Q2 a; Q3 a; Q4 a with A4 deferred."),
recorded in `../checkpoint_snapshots/SCA-005_GROUP-2_2026-09-25/` with
register row `D-PEC-92`, which opens PEC's write fence for Lane A except A4.
Prepared by WORKING_ITEMS node B3 of HELP_HUMAN run
`HELP-HUMAN-PEC-20260923-SCA005` (brief `B3_SCA005_CHECKPOINT3.md`, SHA-256
`69c2296749cee727e1bd84b13f7a4ebcad93400f8ceb6267519e79601811b17f`; held by
HELP_HUMAN, to be committed at the run record's `briefs/B3_SCA005_CHECKPOINT3.md`)
under
`chirality-root:bundled:workflow:scope-change` (`WORKFLOW.md`
`58f5d1d53c655fdc5668d928f6087003590f40e321e25e3d9447805ee64a7a90`, `contract.md`
`4453a719f1588c4eba08bdb4a979140ff3541ed5a29f04477ea58a844f344d02`,
`method.md` `34187e83856853f655389625e3465e3c2cb9ff8ad38be1f4d138ee7470d167f5`).

Pointer posture: `ACCEPTED_PREDECESSOR` — `_ScopeChange/_LATEST.md` names
SCA-004 (`721a14dc…6280`, unchanged); `_Decomposition/_LATEST.md` names
revision 1.4 (`7abf65e6…d7a3`, unchanged). This folder is the candidate
snapshot; it is not active until the owner accepts checkpoint 3.

## Preconditions (all held before the first write)

Every live preimage in `Amendment_Preview.md` §"Byte preconditions" and
`Propagation_Plan.md` Lane A2/A3 matched; both pointer hashes matched; every
group-2 `ACCEPTED_MANIFEST.csv` hash matched except the two rows labelled "at
package publication" (`Decision_Log.md`, `Handoff_State.md`, updated
additively since, as the manifest allows); the `D-PEC-92` row is on `origin/main`
`2b0572fe0`; `pec_reliance_hold.py --operation dispatch-for-production`
returned `ALLOW` for every write target (register `f877d931…1cbc`, no rows).

## Actions taken (Lane A)

All 32 A1–A3 postimages were computed in memory, verified against their
planned SHA-256 and only then written (commit `5d2770350`). A2 applied the
plan's diff blocks as exact string replacements; A3 was a hand-authored exact
edit (Q-CP2-1 (a); `write_status.sh` not used; paired read: no `MEMORY.md` or
`_MEMORY.md` beside any of the four).

| Act | Path (under `projects/pec/`) | Preimage SHA-256 | Postimage SHA-256 |
|---|---|---|---|
| A1 decomposition (pre-acceptance variant) | `execution/_Decomposition/SOFTWARE_DECOMP.md` | `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81` | `37ea1084a8219943a69057be377646c69a609a76728241963045d7cfb015a6cc` |
| A1 register | `execution/_Decomposition/ScopeLedger.csv` | `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` |
| A1 register | `execution/_Decomposition/Deliverables.csv` | `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72` | `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` |
| A1 register | `execution/_Decomposition/ContextBudgetQA.csv` | `5c8d30994a99611b7023f8ac0995ee9a8efa0d2992f3c1a2683f4d2f9e8e2bef` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` |
| A1 register | `execution/_Decomposition/Companion_Inventory.csv` | `18793e150c537371f80d659af2784674d42bac0de37bf7128e484774a557ec23` | `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` |
| A1 PRD v2.3 | `docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| A2 DEL-00-02 | `execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-02_Event_contract_schema_v1/_CONTEXT.md` | `01cddc447f614885b23e6a7fe978b5cbf51803868acf52048e319389d2e699e2` | `beafd08c5112cf5f5b8edb81ecbfdb98128441b8c407eb7e1dc0ec07fe46bb58` |
| A2 DEL-01-01 | `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/_CONTEXT.md` | `d53e451a0e90a7ab2929ca3342dee740fbb6f26cc4c68b52efe663cd2febdf98` | `cab17da6dbdd6e086426813406fffa4b478f1607daf8c716ff38e2effb343975` |
| A2 DEL-01-06 | `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-06_Loop_registry_local_config_default/_CONTEXT.md` | `24f357cc9746b1b0b24991995ed72067062dba9ce7b098b472a5d6eed2db94b2` | `1362ed668436b5af79fe54dd5f7ab660dac9ddd29dad2a0d1b0adebb01ad5919` |
| A2 DEL-02-03 | `execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-03_Receipts_ledger_parser_per_loop_grammars/_CONTEXT.md` | `a787e6379cd1d099ce1237c603c1696f7e3d30b1fde1bb5f3759c6c848d0be46` | `aafac18687dae3703e2ea0e903fc790df5123ea78cbba5682a532b54422f1d12` |
| A2 DEL-02-04 | `execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-04_Run_evidence_JSON_parser/_CONTEXT.md` | `e5460afb03737fcc61594fb17a769d8b5d5de1faa40f4769c855d282b407f48d` | `7f72f6d7304254cb05cf22eb941341627ea2372e549426722311da13595666c2` |
| A2 DEL-02-05 | `execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_CONTEXT.md` | `c4eee6211db66a8d5305741a999ee5b054f40b79d83ecefd2e29964a3c604156` | `6c3ffcff5cb13773bbac24b821ac7d0e101f99ee414b1806a5bd6006b5e38899` |
| A2 DEL-02-06 | `execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-06_Workplan_LOOP_INIT_parser/_CONTEXT.md` | `ff59149c1f01bf47976f412d585481e421c1453134ac6a8e9f6c3d97c3632da0` | `3a09d9792f1a025f807ca63239b7a7c9622226880bb9706a62a10d6e093c1ec1` |
| A2 DEL-02-07 | `execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer/_CONTEXT.md` | `5f2647cf1e65f29e9ce539707891e7b3259d1f9f7e3da8702eb803826b5a7f81` | `fdad5d912567281dabcc61713175a75bed477e225507310f7458b72d698f04c8` |
| A2 DEL-03-03 | `execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-03_Drift_classification/_CONTEXT.md` | `215f30967b8ea683eaba6b0e43d1f4be44838b76ab927481a79e15ec03c94a4e` | `0181f52d5a1c4199f3a29eb61c286d4fb916c91833d47f1a5c90c026d6d08a4b` |
| A2 DEL-03-05 | `execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-05_Stream_loss_recovery_guarantee/_CONTEXT.md` | `912abd1d8b18a166d324deec0f8f2780243d3d5dda95d684c1fcca04eef95ef9` | `4e89162e0c483b34afc4a0e954263c9929ef333a228f656075638c93a7116a17` |
| A2 DEL-04-01 | `execution/PKG-04_Orientation_Services/1_Working/DEL-04-01_Loop_orientation_return/_CONTEXT.md` | `b6816f9a2878d057d28b182c16ae64d6ec3385e6d44cc71e8062ff76128986ea` | `107a293ff8de3b127d2ee2c8c2c71171ee1578ca0d1aaa36842e9c90314aa85f` |
| A2 DEL-05-01 | `execution/PKG-05_Gate_Evaluation_Decision_Slate/1_Working/DEL-05-01_Gate_precondition_evaluators_Explain_shaped/_CONTEXT.md` | `83230f78ef5e98bfaff1ecd0bb326220a8974fcc2d3f1c945458013955410989` | `142528619a8d497437fbd0232b0bda28d3c720a9356b180455265f325b8cbe15` |
| A2 DEL-06-01 | `execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records/_CONTEXT.md` | `8d867899d0facb0e8ecd79538ac3dd9cc5ed3f32ee61c9dd187dc77f6c3e9d5d` | `c9dbe25c44ab78d4e970a94c792865f5b028a905c789111a2c80c9759350d412` |
| A2 DEL-06-04 | `execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_CONTEXT.md` | `2df7d3d4d569ab828c13dcb8c85c62db89519e807e599a4f895610a9cb393cbf` | `a0aee56bc26a769f3ef617ed2f836050c8634b4b7ca3df14554ecee33b47fc30` |
| A2 DEL-07-02 | `execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_CONTEXT.md` | `8aadd01be7375624c26989163d4f7e72cb22ad608c1fcea56538fe100fd97e1d` | `0bb820ded2fe598b8484ee37ae11ae35a81720f8088b490e5c438725cf6af3f0` |
| A2 DEL-07-03 | `execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-03_Hooks_CLI_bridge/_CONTEXT.md` | `984841782d524e77c912e03fb8ce9a6a0231b69ffe1ca660d7441e71327c894a` | `508bd1de276c4235ecadadb2261ed7be470c78e87bdf2c32d45f774103215431` |
| A2 DEL-07-04 | `execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_CONTEXT.md` | `805a32c90214b9c3f401e06399d9e205207c629696e432829195975ab03097f9` | `5ac0787f665f6603fdc461e5816681584431715019937f292f26c9242dc81b43` |
| A2 DEL-07-05 | `execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_CONTEXT.md` | `b32196a0e7bdbbd44de79916f97d63ce68cf75d7f5350fc1f6d5ac823ce90f4b` | `1adc79cd3779b756d80ff681e975adb52e776d612081e52bd0ad5acc618de12e` |
| A2 DEL-08-01 | `execution/PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md` | `3393b45003a6ab0ae3e54e36831f7bb32399be4fa8aa1b15bbdc213ebed4dc15` | `151e1e34330a58467ef0f9aa28a3283b50b84bf5f563b03039f5c6bcd9273985` |
| A2 DEL-08-05 | `execution/PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/_CONTEXT.md` | `d1bbae9720e13b66b9ab2267657b10910e134564dfcb1c4fc616637817ef8daa` | `ba3f7d6e10d52c9b6fc1185538d891ccad0833afea16107fd1b060d5cd4ae31d` |
| A2 DEL-09-05 | `execution/PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board/_CONTEXT.md` | `6c5455c38b85003e3632e52a961e0aae150eb4e25567bd6378d0c05207085569` | `cd2b2f6b4e14c2b47d9ee98f545cdc27f006275c92d3b01ef1d3142c6b52cab9` |
| A2 DEL-10-08 | `execution/PKG-10_Validation_Measurement/1_Working/DEL-10-08_Stream_loss_recovery_demonstration/_CONTEXT.md` | `9c320e3795b874819dde7db11e0a4c3550dad32b3488ef1ba70b347ffaa7a51c` | `d08c2b9050b93b1ca0581b5b08b39334c129e2dc47ad2b72bad9485ab6ae18d0` |
| A3 DEL-06-04 RETIRED | `execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-04_Live_hierarchy_edges/_STATUS.md` | `8cfb8b8800a591124cc0e24aeae9d643f278e8845bf99cd1bb90170a471d4726` | `eeae22fbd49a8f4105139480e45db6c9c1147d343cfa2b8a83bd8bad039724bc` |
| A3 DEL-07-02 RETIRED | `execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-02_Daemon_SSE_subscriber_bridge/_STATUS.md` | `b05edcc916edf44db252bcd8ca055391ec9d48525e23aaead17f962af4f0f45f` | `8eda30e178b6164c3caa4a5afd97271e49cbec2f1232a0ffc4c4fe4ccbc93b8a` |
| A3 DEL-07-04 RETIRED | `execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-04_cmux_socket_adapter_optional/_STATUS.md` | `10905472a88d4e3d6ca96cfe22769106fa408b79097e403b0fb65b499a34b726` | `2aaec8fd5ba027c5a7cc34d1a94a972ca8ddb2c7a1a59db52e53be8d12f2de5e` |
| A3 DEL-07-05 RETIRED | `execution/PKG-07_Event_Ingest_Bridges/1_Working/DEL-07-05_Shared_runtime_client_seam_v2/_STATUS.md` | `4fb85e33b8c28cc220f8c0e40a66705929f96aa0abcbe793d07be731731d30df` | `19123cf8a3ca8e19a60bac8849c9008d33a025e245dabffb4bd82f4cc8383ded` |

**Slot values (hash rule of `Amendment_Preview.md` §"Acceptance-bound
tokens").** Application date 2026-09-25. `SOFTWARE_DECOMP.md` front matter
`date:` = `2026-09-25`; §7 `Revision` row = `1.5, 2026-09-25 (SCA-005)`;
§11 DL-20 date cell = `2026-09-25`; front matter `status:` and `accepted:`
carry the two pre-acceptance lines exactly as the preview gives them. The
PRD's Date row, Status-row date, epistemic-paragraph date (`2026-09-25`) and
snapshot token (`SCA-005_GROUP-2_2026-09-25`) equal the group-2 act. The four
`_STATUS.md` `**Last Updated:**` and History-line dates are `2026-09-25`.
Every slot equals the package default, so the slot-substituted hash equals
the accepted hash in each case: decomposition pre-acceptance variant
`37ea1084…a6cc` (accepted final-form candidate `dc2b8479…9660`, differing in
front-matter lines 5 and 8 only); PRD `fff27a66…fdc32`.

**A4 not opened** (no DEL-02-08/09 folder, no `Dependencies.csv` row). **A6
not performed**: no pointer moved.

**A5 snapshot completion (this folder).**

| File | SHA-256 | Source |
|---|---|---|
| `Supersession_Map.csv` | `4ca705ba090cafb9a74870a0095be490c1d507149767dac32ec52879c487240c` | `python3 tools/coordination/accumulate_supersession_map.py --prior-map …/SCA-004_2026-08-02_2325/Supersession_Map.csv --delta …/SCA-005_2026-09-23_2139/Supersession_Delta.csv --output-map …/SCA-005_2026-09-23_2139/Supersession_Map.csv`: exit 0, 29 rows, 0 findings (SCA-004 prior map is header-only, `9b62e987…fcb9`) |
| `Post_Change_Coverage.json` | `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` | byte copy of the C4 audit `coverage_summary.json` (`cmp` identical) |
| `RUN_SUMMARY.md` | this file | — |
| `Decision_Log.md`, `Handoff_State.md` | recorded in `Handoff_State.md` | additive sections, with the front matter, `Handoff_State.md` heading, the SCA005-CP3 row and the hash-table row updated in place (disclosed in the ninth amendment) |

## Validation (Lane C)

**C1 containment.** Against `origin/main` `2b0572fe0`: every changed path is on
the allowlist (the decomposition and four registers, `docs/PRD.md`, the 22
`_CONTEXT.md`, the four `_STATUS.md`, this snapshot folder, the new
`COV_SCA005_POSTCHANGE_2026-09-25_1344/`, and the run-record `returns/` B3
files); all 32 A1–A3 postimages equal their planned hashes (slot rule
applied); no checkpoint-1/2 artifact in this folder, no `checkpoint_snapshots/**`
file, no pointer, no other `_STATUS.md` or `_CONTEXT.md`, no SOW,
`Dependencies.csv`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `v2/**` or foreign
path changed. `git diff --check 2b0572fe0..HEAD` flags 30 lines, all in
`Supersession_Map.csv`: the deterministic accumulator writes CRLF line endings
(`csv.DictWriter` default); the file is byte-identical to a fresh accumulator
run and A5 forbids hand-writing it (10 of 29 committed `Supersession_Map.csv`
files in the repository are CRLF). No other path is flagged. Final figures
are in the B3 return.

**C2 structure.**
`python3 tools/validation/validate_decomposition_registers.py projects/pec/execution --strict`:
64 registers, 255 dependency rows, **0 errors, exactly 2 warnings (DRB-008
DEL-02-08, DRB-008 DEL-02-09)**; exit 1 because `--strict` fails on warnings.
`python3 tools/coordination/analyze_dep_closure.py projects/pec/execution --output-dir <scratch>`:
`COMPLETE`, 119 EXECUTION edges over 64 nodes, **0 SCCs, 0 bidirectional
pairs**, isolated **DEL-00-03 and DEL-01-05**, `DEP-09-05-005` (DEL-09-05 →
retired DEL-06-04) present. Both are the pre-A4/pre-B3 expectations in the
group-2 `DECISION.md`, not defects.

**C3 exact successor assertions: 31/31 PASS.** 96 scope items (70 IN / 18 OUT /
8 TBD); 11 packages; 66 deliverable rows (62 active / 4 RETIRED: DEL-06-04,
DEL-07-02, DEL-07-04, DEL-07-05); 6 objectives; 66 ContextBudgetQA rows over
the same deliverable set; 0 IN items without package, deliverable or
objective; 0 active deliverables without objectives; union rule
`SupportsObjectives = union(ObjectiveIDs)` on 62/62 active rows; retired rows
carry blank coverage and objectives; active envelopes S 28 / M 32 / L 2 / XL
0; PKG-02 / 06 / 07 assigned 9 / 6 / 3 and PKG-06 / 07 active children 5 / 2;
open / resolved issues 10 / 3; 26 vocabulary terms; every revision-1.4 SOW
and DEL ID, name and package retained, new IDs exactly SOW-095/096 and
DEL-02-08/09; every revision-1.4 deliverable folder present.
SOFTWARE-specific: no package change left a deliverable or IN Scope Ledger row
parentless. **Package-discipline isolation (DL-3, DL-12) and artifact-kind
granularity (DL-4, DL-13) for DEL-02-08/09:** both are PKG-02
`BACKEND_FEATURE_SLICE` read-side grammar parsers that write nothing, one
grammar each (work graph; MEMORY run index), P1, `OBJ-001;OBJ-002`, covering
SOW-095 and SOW-096 respectively — the rules hold.

**C4 post-change audit.** TASK `audit-decomp` →
`_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/`
(`coverage_summary.json` `912610ff…4deb`), compared with
`COV_SCA005_PRECHANGE_2026-09-23_2139` in its `PrePost_Comparison.md`.

- **Verdict by the method's count rule: `overall_status = BLOCKERS`,
  `closure_readiness = FAIL`** — 2 blockers / 6 warnings / 74 info.
- Classification-adjusted reading (the child's, checked here): excluding
  expected consequences, 0 blockers / 4 warnings (3 pre-existing, 1 defect),
  which would read `WARN`.
- Blockers COV-001/COV-002 (Check 2): the DEL-02-08 and DEL-02-09 folders are
  absent — EXPECTED_CONSEQUENCE of the owner's A4 deferral (group-2
  `DECISION.md`: such findings are "reported as a consequence of this
  decision, not repaired").
- Warnings: COV-070/071 (SOW-095/096 point at units without folders) —
  expected, same clause; COV-006/008/042 (DEL-01-03, DEL-01-05, DEL-08-02
  artifacts live under `v2/`) — pre-existing (PRECHANGE COV-004/006/040);
  **COV-072 — DEFECT in the accepted plan's stated count** (below).
- Retired-row representation: confirmed on the real files — no blocker and no
  warning (4 Check-6 and 4 Check-7 INFO only).
- Pre/post: forward deliverable coverage 100 % → 96.97 % (2 declared units
  without folders, A4); context fidelity 100 % both; unmapped IN rows / active
  deliverables 11 / 9 → 0 / 0; lifecycle 26 INITIALIZED / 28 OPEN / 4 CHECKING
  / 2 IN_PROGRESS / 4 RETIRED; 62 findings carried, 6 resolved, 4 changed, 16
  new (15 expected, 1 defect).
- Audit containment verified by the manager: only the COV folder was added;
  its nine files hash as the child reported; `DecompCoverage/_LATEST.md`
  unchanged (`0084d218…7432`).
- COV-075 (snapshot mid-A5; `Handoff_State.md` heading still
  "Checkpoint-group-1") is superseded by this A5 completion; the immutable
  audit keeps it as observed.
- The plan's §C4 expectation of closure-tool isolated-node warnings for the
  four retired deliverables cannot be observed before B3: their registers
  still hold 18 ACTIVE rows (audit COV-080). That sub-expectation is deferred
  with B3.

**Evidence correction (COV-072), not a plan change.** `Propagation_Plan.md`
(package-role table L45, B1 L802, derivative-status table L904) and brief B3
state that 40 `_CONTEXT.md` files are not written in A2 and await the B1
re-pin. The census is **42** (64 deliverable folders − 22 A2 mirrors;
`context_provenance_revision` 1.5: 22 / 1.4: 42). B1's selection rule ("the
`_CONTEXT.md` files not written in A2") is unchanged and selects all 42; the
accepted plan's bytes are not edited. No C3 assertion and no closure field
depends on the number: `MetadataAlignmentState = IN_PROGRESS` rests on "22
mirrors done; B1 open". Every statement of that population in this snapshot
from here on uses 42.

**C5 snapshot completeness.** Present with hashes: `Brief.md`,
`Impact_Assessment.md`, `Amendment_Preview.md`, `Propagation_Plan.md`,
`Amendment_Actions.csv`, `Amendment_Actions_CP2.csv`, `Supersession_Delta.csv`,
`Supersession_Map.csv`, `Pre_Change_Coverage.json`,
`Post_Change_Coverage.json`, `Decision_Log.md`, `Handoff_State.md`,
`RUN_SUMMARY.md`, `PRD_V2_3_SUCCESSOR_DIFF.md`, `CP2_CANDIDATE/` (6 files).
Checkpoint-1 and checkpoint-2 artifacts are byte-unchanged (hash table in
`Handoff_State.md`).

**Independent review.** A fresh read-only `pec-reviewer` audits this poststate;
its verdicts are saved as `returns/B3_VERIFIER_VERDICT_NN.md` in the run
record and summarized in the B3 return.

## State fields

| Field | Value |
|---|---|
| `DecompositionTruthState` | `COMPLETE` — revision 1.5 applied; its two front-matter lines stay in pre-acceptance form until checkpoint-3 acceptance |
| `DerivativePackageState` | `INCOMPLETE` — Lane B open; A4 deferred |
| `ContentRemediationState` | `NOT_REQUIRED` — SOFTWARE variant |
| `DownstreamRerunState` | `FROZEN` — no Lane B item authorized |
| `MetadataAlignmentState` | `IN_PROGRESS` — 22 direct mirrors and 4 retirements done; B1 re-pin of 42 `_CONTEXT.md` and 64 `_REFERENCES.md` open; 2 new folders `NOT_CREATED` |
| `AuditState` | **`BLOCKED`** — the C4 audit reads `BLOCKERS` / `FAIL` by the method's count rule (2 / 6 / 74). Beside it, the classification-adjusted reading: both blockers are EXPECTED_CONSEQUENCE of the A4 deferral; excluding them the audit has 0 blockers / 4 warnings (3 pre-existing, 1 plan-count defect) and would read `WARN` |
| `ReadyForNextPhase` | `NO` |
| Closure verdict | `OPEN_PENDING_DERIVATIVE_CLOSURE` now; `CLOSED_FOR_SCOPE_CHANGE_ONLY` only on the owner's checkpoint-3 acceptance (Q-CP3-1) |

## Recommended downstream reruns (not executed)

| Item | Owner | Trigger |
|---|---|---|
| A4 — DEL-02-08/09 folders (`_CONTEXT.md`, `_STATUS.md` `OPEN`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv` ANCHOR rows); clears COV-001/002/070/071 and the two DRB-008 warnings | PROJECT_SETUP under its own packet, with B3 | owner packet |
| B1 — re-pin 42 `_CONTEXT.md` and 64 `_REFERENCES.md` to revision 1.5 | PROJECT_SETUP | after checkpoint 3 |
| B3 — dependency retirements (18 rows owned by retired registers, `DEP-09-05-005`, `DEP-03-01-014`), new-deliverable edges, mirror refresh; planned 119 → 108 → 107 → 111/112 edges | dependency-extract / PROJECT_SETUP | with A4 |
| B4 — 23 Scope of Work contracts needing currency work, 5 housekeeping-only | WORKING_ITEMS + artifact gates | per deliverable |
| B5 — DEL-00-01 ADRs, DEL-00-03 SPEC stale-premise review | owning workflows | per deliverable |
| B6 — registry source packet (`loops.schema.json` v2, feed profiles, `RegisteredLoop`) | later D-PEC packet | owner packet |
| B7 — P1 fixture suites | DEL-02-08/09/03 SOWs | after A4 |
| B8 — TM-PEC-023 `RESOLVED_BY_DECISION`; D-PEC-90 reliance amendment; README/STATUS refresh; `projects/pec/AGENTS.md` L28/L170 and Shared Runtime Boundary instruction tranche | task-management; next PEC scope change; HELP_HUMAN; instruction tranche | after checkpoint 3 |
| Foreign notices (RETIRED method/tool mismatch and `LOOP_INIT` to Root; `adapter.yaml` to App and Piping) | HELP_HUMAN (outside B3's write boundary) | checkpoint-3 preparation, before or with the presentation of checkpoint 3 (group-2 `DECISION.md` §Notices); drafts in the B3 return; not written when B3 handed back — HELP_HUMAN states their status when it asks the owner |
| Re-audit (`audit-decomp`) after A4 and B3 | TASK | after A4/B3 |

## Rollback on refusal

If the owner returns checkpoint 3, pointers stay on revision 1.4 / SCA-004 and
this candidate becomes non-current evidence. Restoring the accepted basis
means returning every Lane A path to its preimage hash in the table above.
**That includes the 22 A2 `_CONTEXT.md` mirrors (audit COV-076)**: they carry
the accepted exact bytes, whose provenance already reads "then by revision 1.5
(`current_basis`, SCA-005 successor)", while the decomposition itself says
`candidate_pending_checkpoint_3`. They become true on acceptance; on refusal
they are wrong and must be restored with the rest. The four `_STATUS.md`
retirements, the four registers and `docs/PRD.md` are likewise restored to
their preimages. The rollback is a new, recorded exact-bytes act from the
preimages at `origin/main` `2b0572fe0` — not a Git reset or deletion — and is
repaired only through a refreshed accepted plan.

## Repository-change evidence

Modified: the 32 Lane A paths above; `_ScopeChange/SCA-005_2026-09-23_2139/`
(`Supersession_Map.csv`, `Post_Change_Coverage.json`, `RUN_SUMMARY.md` new;
`Decision_Log.md`, `Handoff_State.md` updated as disclosed above); new
`_Evaluation/DecompCoverage/COV_SCA005_POSTCHANGE_2026-09-25_1344/`; run-record
returns `B3_SCA005_CHECKPOINT3.md` and `B3_VERIFIER_VERDICT_NN.md`. Branch
`claude/pec-sca005-cp3-execution` under the owner's standing Git authorization
of 2026-09-12; the PR is not merged by B3.

Recommended commit message:

```text
scope: SCA-005 — feed-model rebaseline, revision 1.5 candidate (checkpoint-3 preparation)

Variant: SOFTWARE
Actions: 79 (ADD:8, MODIFY:67, REMOVE:4)
Affected entities: SOW-001/004/013..017/026/029/033..035/037/049/074/076/077/080/082/083/087/092/094/095/096; DEL-00-02, DEL-01-01, DEL-01-06, DEL-02-03..09, DEL-03-03, DEL-03-05, DEL-04-01, DEL-05-01, DEL-06-01, DEL-06-04, DEL-07-02..05, DEL-08-01, DEL-08-05, DEL-09-05, DEL-10-08; PKG-00/02/06/07; OBJ-001..004
```

## Checkpoint-3 owner question

**Q-CP3-A — accept the audited poststate.** Accept, as the SCA-005
checkpoint-group-3 decision, the applied revision-1.5 poststate:

| Artifact | SHA-256 |
|---|---|
| live `_Decomposition/SOFTWARE_DECOMP.md` (pre-acceptance form) | `37ea1084a8219943a69057be377646c69a609a76728241963045d7cfb015a6cc` (becomes accepted candidate `dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660` when its two front-matter lines and date slots are set in A6; slot rule applies if the acceptance date is not 2026-09-25) |
| `ScopeLedger.csv` / `Deliverables.csv` | `83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df` / `b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a` |
| `ContextBudgetQA.csv` / `Companion_Inventory.csv` | `2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df` / `7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8` |
| `docs/PRD.md` v2.3 | `fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32` |
| audit snapshot `COV_SCA005_POSTCHANGE_2026-09-25_1344/coverage_summary.json` | `912610ff55e7e53788cb07c972a5a27afe5e246ecadb042932d57776cc0c4deb` |

with these facts in view:

- **Audit verdict:** `BLOCKERS` / `FAIL` by the method's count rule (2 / 6 /
  74). Both blockers, COV-001/002, are the absent DEL-02-08/09 folders — the
  consequence of your A4 deferral. Excluding expected consequences: 0
  blockers / 4 warnings (3 pre-existing v2-artifact locations; 1 plan-count
  defect, COV-072, recorded as an evidence correction: 42, not 40, contexts
  await B1). Retired rows raise nothing above INFO.
- **Closure state fields:** `DecompositionTruthState COMPLETE`;
  `DerivativePackageState INCOMPLETE`; `ContentRemediationState NOT_REQUIRED`;
  `DownstreamRerunState FROZEN`; `MetadataAlignmentState IN_PROGRESS`;
  `AuditState BLOCKED` (adjusted reading `WARN`); `ReadyForNextPhase NO`.
- **Known consequences of the A4/B3 deferral:** DEL-02-08/09 have register
  rows but no folders (audit blockers COV-001/002, warnings COV-070/071, two
  DRB-008 validator warnings); dependency topology is still pre-B3 (119
  edges, isolated DEL-00-03 and DEL-01-05, `DEP-09-05-005` pointing at the
  retired DEL-06-04, 18 ACTIVE rows in the retired deliverables' registers).
  All clear only when PROJECT_SETUP runs A4 with B3 under its own packet.
- **COV-076:** the 22 A2 `_CONTEXT.md` mirrors already name revision 1.5 as
  `current_basis`. Acceptance makes that true; refusal requires restoring them
  with the rest (§Rollback on refusal).
- **On acceptance, HELP_HUMAN performs A6** with the checkpoint-3 acceptance
  date: `_ScopeChange/_LATEST.md` names SCA-005; `_Decomposition/_LATEST.md`
  becomes the revision-1.5 handoff (citing the 2026-08-09 SCA-004 repair
  closeout rather than its stale populations); the decomposition's
  `status:`/`accepted:` lines return to their accepted values and its four
  date slots take the acceptance date (slot hash rule); the Decision_Log
  records the act. Lane B stays open work.

**Recommendation: accept.**

Genuinely open choice:

| # | Choice | Options | Recommendation |
|---|---|---|---|
| Q-CP3-1 | Closure verdict recorded on acceptance, given the audit's by-rule `BLOCKERS` come only from the deferred A4 folders | (a) `CLOSED_FOR_SCOPE_CHANGE_ONLY`, the plan's planned value and the SCA-004 precedent: the decomposition amendment is closed; A4, B1–B8 and a re-audit are recorded open in `Handoff_State.md`; (b) `OPEN_PENDING_DERIVATIVE_CLOSURE` until A4 and B3 land and a re-audit clears COV-001/002 (pointers still move on acceptance) | **(a)** — the blockers measure derivative scaffolding you deferred on purpose, not the amendment; (a) keeps them visible as open obligations without holding the scope change open |
