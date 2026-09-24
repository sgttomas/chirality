# DEL-01-03-REM-003: derivative evidence report

This is a read-only evidence inquiry. It creates no contract, implementation, test, measurement, acceptance, lifecycle or production act. It closes no Remaining item.

## 1. Header

| Field | Value |
|---|---|
| Item | `DEL-01-03-REM-003` |
| Date | 2026-09-23 (session date; UTC clock at the observation run read 2026-09-24T03:27Z) |
| HEAD | `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` |
| Author role | TASK (Type 2), instruction-asserted; no delegation used |
| Serving model | `claude-opus-5-5[1m]`, as stated in the host system context and not independently verified |
| Parent | WORKING_ITEMS manager for the PEC loop, dispatched by HELP_HUMAN under D-PEC-86 §3 I-4 |
| Brief | `OUT/CHILD_BRIEF.md` (sha256 `4487b8460d1c4a4bd69da25a7d6673e9115ec08f7ad83e49594a18fa83550df0`) |
| Reliance preflight | `OUT/PREFLIGHT_RELIANCE_HOLD.json`: `historical-read-only-inspection` returned `ALLOW` (copied into the manifest) |

Path abbreviations used below (all repository-relative):

- `DEL/` = `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/`
- `P1/` = `DEL/_run_records/P1_STORE_GUARD_01/`
- `OUT/` = `DEL/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-003/`
- `CO/` = `projects/pec/execution/_Coordination/`
- `SY/` = `projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/SYNTHESIS/`
- `D10/` = `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/`
- `D105/` = `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/`
- `V2/` = `projects/pec/v2/`

## 2. Scope and linked claims

The claim set is exact. It comes from `SY/APPLICATION_PREPARATION/FULL_01/PROPOSED_ITEMS.csv:9` and `SY/APPLICATION_PREPARATION/FULL_01/CLAIM_TO_PROPOSAL_MAP.json:3436-3614`, with per-claim baseline rows in `SY/FULL_02/CONSOLIDATED_CLAIMS.csv`.

| Claim | SOW locator (`DEL/ScopeOfWork.md`, sha256 `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341`) | D83 baseline row |
|---|---|---|
| `DEL-01-03::OUT-003` | line 61 (matrix row line 141) | `CONSOLIDATED_CLAIMS.csv:181` |
| `DEL-01-03::REQ-010` | line 84 | `CONSOLIDATED_CLAIMS.csv:200` |
| `DEL-01-03::AC-010` | line 95 | `CONSOLIDATED_CLAIMS.csv:210` |
| `DEL-01-03::VER-009` | line 117 (VER-001..008 at lines 109-116) | `CONSOLIDATED_CLAIMS.csv:220` |
| `DEL-01-03::CURRENT-REMAINING` | none. This is a documentary claim whose declared source is `DEL/_STATUS.md` (Remaining section at lines 12-24) | `CONSOLIDATED_CLAIMS.csv:229` |

The D83 baseline is historical. It was recorded at source commit `2be412cce` against `_STATUS.md` sha256 `c2f5ee7b…`, and every row carried `Disposition UNKNOWN`. The current SOW bytes (`986ef155…`) equal the baseline's SOW hash.

## 3. Method (read-only)

- **Read in full:** the DEL-01-03 SOW, `_STATUS.md`, `MEMORY.md`, `_CONTEXT.md`, `Dependencies.csv` and `_DEPENDENCIES.md`; all nine D85 product and configuration files; the D85 fan-in, check, author-ledger and review records named in §4; the D-PEC-83 and D-PEC-85 rulings; the D83 application return; and the DEL-10-02 `_STATUS.md` and run-record headings.
- **Targeted reads:** the D83 baseline rows for the five claims, `build_full_preparation.py:19,82-83`, the D-PEC-86 row I-4, `projects/pec/software-workflow.json`, the hosted CI wiring and the DEL-01-05 posture configuration and status.
- **Bounded searches.** Each search's scope and method is stated in the row that relies on it:
  - `grep -rn kill` over `V2/**` and `software-workflow.json`;
  - `find` for Python dependency manifests at depth 2 under `projects/pec` and `V2`;
  - `grep` for `service-core test run` over `projects/pec/**/*.md`;
  - `grep` for `v2-store-guard`, `v2/tests/storage` and `software-workflow.json` over `.github/`, `tools/hosted-ci-routing.json` and `projects/pec/tools/run-workspace-tests.ts`;
  - `grep` of `V2/tests/storage/**` for documentation or manifest references.
- **Git (read-only):** `git show --name-status 14f42e9ce`, `git log` on `_STATUS.md` and the SOW, and a diff of the Remaining section between `14f42e9ce` and HEAD. I also compared the Remaining section of `git show 14f42e9ce^:_STATUS.md` against the D83 baseline hash, and ran `git check-ignore --no-index -v` and `git ls-files -- .pec-v2` in `projects/pec`.
- **Hashes:** I recomputed the SHA-256 of all nine D85 postimages at HEAD. All nine equal the attempt-2 postimages in `P1/TECHNICAL_FAN_IN.md:12-22`.
- **One observation run:** the brief's exact storage-suite command, run once. It is recorded in `OUT/STORAGE_SUITE_OBSERVATION.json`. This observation is not a new measurement, acceptance or VER-discharge claim. `git status --short --untracked-files=all` was identical before and after the run.
- **Class conventions:** for the documentary claim `CURRENT-REMAINING` and for DEL-10-02 state, `OBSERVED_IMPLEMENTATION` means documentary bytes observed at HEAD, not product code. The evidence kinds are kept apart as follows:
  - (a) historical SOW format and documentary checks → `FINITE_METHOD_EXECUTION` (format only);
  - (b) D85 finite executions → `FINITE_METHOD_EXECUTION`;
  - (c) this observation run → `FINITE_METHOD_EXECUTION`;
  - (d) DEL-10-02 → recorded state only.

## 4. Evidence

### 4.1 VER method to executing-test map

"D85" means the verbose ledger `P1/children/AUTHOR/VERIFICATION_EXECUTION_REMEDIATION.json` together with the manager's final registered run. "Obs" means this inquiry's observation run. Test IDs are abbreviated. Their full IDs are the `TEST_TO_VERIFICATION` keys at `V2/tests/storage/test_store_lifecycle.py:30-44`, which are repeated verbatim in the observation file.

| VER | Executing test(s), module `test_store_lifecycle` (SL) or `test_content_minimal_guard` (CG) | Locator | D85 | Obs | Coverage against the declared method |
|---|---|---|---|---|---|
| VER-001 | SL `test_ver_001_database_journal_and_temp_artifacts_are_ignored`, `..._later_negation_of_the_rule_fails_before_store_creation`, `..._force_tracked_store_artifact_fails_before_any_write` | SL:68-110 | PASS | ok | **Partial.** The tests run in a temporary scratch checkout whose `/.pec-v2/` rule the test writes itself (SL:47-56). No test populates a store in the hosting checkout (SOW:86 wording). The PEC project checkout (`projects/pec`) carries the rule at `projects/pec/.gitignore:17`. Which directory is the hosting checkout is held UNKNOWN in REM-001 U-2 |
| VER-002 | SL `test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation` | SL:112-134 | PASS | ok | **Partial.** The "stopped" case is close-then-delete. The "running" case is `delete()` on an open handle, which closes the handle first (`sqlite_store.py:139-145`). No PEC process exists, and no deletion under a live connection is exercised. This is store-local only; it is not DEL-10-02 evidence |
| VER-003 | SL `test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface` | SL:136-150 | PASS | ok | **Partial.** It uses text and AST token counts (one `admit_batch`, one guard-call string, no `INSERT` before `_insert_guarded`) rather than an import or call graph |
| VER-004 | CG `test_ver_004_admission_and_readback_preserve_all_five_typed_classes`, `test_ver_004_content_diff_prose_unknown_classes_and_misleading_keys_are_rejected_atomically`, and also `test_ver_008_forged_wrappers_...` | CG:52-93, 157-209 | PASS | ok | **Partial.** Residue is checked through `read_all()`, not through a dump of every persisted table and field |
| VER-005 | CG `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution`, and also `test_ver_004_admission_...` | CG:95-109 | PASS | ok | **Partial.** The asserted `attempted = accepted + rejected` (CG:100) holds by construction, because `rejected` is computed as `attempted - accepted` (`sqlite_store.py:88`). Of the failure codes, only `DUPLICATE_RECORD` is asserted (CG:108). Nine codes are never asserted: `RECORD_TYPE`, `INVALID_IDENTIFIER`, `EMPTY_RECORD`, `FIELD_TYPE`, `INVALID_FIELD_NAME`, `DUPLICATE_FIELD`, `SOURCE_CITATION`, `UNKNOWN_FIELD_CLASS` and `INVALID_VALUE`. Nor is the `<unknown>` record location (`content_minimal_guard.py:132-224`) |
| VER-006 | CG `test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary` | CG:111-125 | PASS | ok | **Partial.** Three test-local stand-ins each carry different values, not one shared corpus. There is no by-construction assertion for a further ingest shape, and no real ingest path exists (`STORE_LIFECYCLE_AND_GUARD.md:93-98`) |
| VER-007 | SL `test_ver_007_runtime_imports_are_stdlib_or_pec_and_make_no_network_call` (interface leakage is asserted in the VER-003 test) | SL:152-169 | PASS | ok | **Partial.** No dependency manifest exists to inspect (bounded absence). The DEL-01-05 re-run has not been performed: DEL-01-05 is `IN_PROGRESS`, and its posture target is core-only, which excludes `adapters/storage` |
| VER-008 | CG `test_ver_008_policy_is_fixed_finite_and_domain_checked`, `test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing` | CG:127-209 | PASS | ok | **Partial.** The tests check the code policy. The declared method is a review of the documented rule (`STORE_LIFECYCLE_AND_GUARD.md:43-75`) against PRD §7.1 and §7.2, and no executing test reads that document |
| VER-009 | SL `test_ver_009_loaded_suite_has_exact_execution_mapping` | SL:171-189 | PASS | ok | **Partial.** The first clause is covered at the label level: discovered IDs equal the map keys, and the mapped set equals VER-001..009, with VER-009 mapped to itself. The second clause ("no test asserts a criterion absent from this contract") has no executing test and no recorded review |

Totals are 13 test methods: D85 recorded 13 PASS (exit 0) and the observation recorded 13 ok (exit 0). Every one of VER-001..008 has at least one executing test that is labelled and mapped to it. Whether each such test *implements* its declared method is partial for VER-001, 002, 003, 004, 005, 006, 007 and 008, as the table shows. This inquiry does not decide that question.

### 4.2 Evidence table

| Row | Claim | Evidence class | Observation (one line) | Source path:lines | SHA-256 |
|---|---|---|---|---|---|
| E-01 | `OUT-003` | OBSERVED_IMPLEMENTATION | Storage suite: 2 modules, 13 test methods; `TEST_TO_VERIFICATION` binds each test ID to VER IDs | `V2/tests/storage/test_store_lifecycle.py:30-44` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| E-02 | `OUT-003` | OBSERVED_IMPLEMENTATION | VER-001: three tests run `git check-ignore`/`status` over five artifact shapes plus fail-closed cases, in a temp scratch checkout whose rule the test writes | `V2/tests/storage/test_store_lifecycle.py:47-56,68-110` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| E-03 | `OUT-003` | OBSERVED_IMPLEMENTATION | The PEC project checkout (`projects/pec`) carries checked-in rule `/.pec-v2/`; `git ls-files -- .pec-v2` returned 0 paths at HEAD; hosting-checkout identity held UNKNOWN (REM-001 U-2) | `projects/pec/.gitignore:17` | `352a305b5d6e002da80daa248a0d0bc330886685d039dbcfdf8b41897bfde9da` |
| E-04 | `OUT-003` | BOUNDED_LOCAL_ABSENCE | No test populates a store in the hosting checkout (SOW "in the hosting checkout"); scope `V2/tests/storage/**`, method: full read of both files | `V2/tests/storage/test_store_lifecycle.py:47-56` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| E-05 | `OUT-003` | OBSERVED_IMPLEMENTATION | VER-002: one test covers create, restart, close, reset, open-handle delete, closed delete, empty reopen | `V2/tests/storage/test_store_lifecycle.py:112-134` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| E-06 | `OUT-003` | OBSERVED_IMPLEMENTATION | `delete()` closes the connection before unlinking, so the open-handle case is close-then-delete, not deletion under a live connection | `V2/src/pec_v2/adapters/storage/sqlite_store.py:139-145` | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` |
| E-07 | `OUT-003` | BOUNDED_LOCAL_ABSENCE | No PEC service or daemon process and no deletion beneath a live connection; scope `find V2 -type f` plus both test files; the doc states no daemon | `V2/docs/STORE_LIFECYCLE_AND_GUARD.md:93-98` | `d1d69dcbf29a694ea62ada6b6502ffc379221415eb9a260b54fe095648cd1e48` |
| E-08 | `OUT-003` | OBSERVED_IMPLEMENTATION | VER-003: asserts protocol method list, no engine/path tokens in signatures, one `admit_batch`, one guard-call string, no `INSERT` before `_insert_guarded`; token check, not a call graph | `V2/tests/storage/test_store_lifecycle.py:136-150` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| E-09 | `OUT-003` | OBSERVED_IMPLEMENTATION | VER-004: typed readback plus five-fixture rejection; residue checked through `read_all()`, not a dump of every persisted table and field | `V2/tests/storage/test_content_minimal_guard.py:52-93` | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E-10 | `OUT-003` | OBSERVED_IMPLEMENTATION | VER-005 (partial): asserts located (record, field) failures and the `DUPLICATE_RECORD` code; `attempted = accepted + rejected` holds by construction (E-49); other codes unasserted (E-50) | `V2/tests/storage/test_content_minimal_guard.py:95-109` | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E-11 | `OUT-003` | OBSERVED_IMPLEMENTATION | VER-006: three test-local stand-ins with different values (no shared corpus); no by-construction assertion for a further shape | `V2/tests/storage/test_content_minimal_guard.py:111-125` | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E-12 | `OUT-003` | OBSERVED_IMPLEMENTATION | VER-007: AST import roots of three production files lie within stdlib and `pec_v2`, five network modules excluded; no manifest inspection; no DEL-01-05 re-run | `V2/tests/storage/test_store_lifecycle.py:152-169` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| E-13 | `OUT-003` | BOUNDED_LOCAL_ABSENCE | No Python dependency manifest (pyproject, requirements, setup, Pipfile) under `projects/pec` (depth 2) or `V2`, so VER-007's manifest has no object; method: `find` | `DEL/ScopeOfWork.md:115` | `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` |
| E-14 | `OUT-003` | OBSERVED_IMPLEMENTATION | DEL-01-05 posture target is `v2/src/pec_v2/core`; `adapters/storage/sqlite_store.py` lies outside it | `V2/config/service_core_posture.json:3` | `20d64ff38122fa2f7b4bbe6478e42450ce6f9c8b03dc91c90b5095393ef309ed` |
| E-15 | `OUT-003` | UNKNOWN | DEL-01-05 is `IN_PROGRESS` after the 2026-09-07 CHECKING-to-IN_PROGRESS reversal; its "available" status for the VER-007 re-run is unrecorded | `D105/_STATUS.md:3-13` | `7d3eeb9888f10f6e938c7a0c08ff22ee1907df89812064ee76a95e0fdaeae60c` |
| E-16 | `OUT-003` | OBSERVED_IMPLEMENTATION | VER-008: tests assert enum closure, six-state vocabulary, no policy constructor, domain rejections, forged wrappers | `V2/tests/storage/test_content_minimal_guard.py:127-209` | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E-17 | `OUT-003` | BOUNDED_LOCAL_ABSENCE | No storage test reads the documented admissibility rule or the PRD §7.1/§7.2 inventories; scope `V2/tests/storage/**`, method: full read plus grep for doc names | `V2/docs/STORE_LIFECYCLE_AND_GUARD.md:43-75` | `d1d69dcbf29a694ea62ada6b6502ffc379221415eb9a260b54fe095648cd1e48` |
| E-18 | `OUT-003` | FINITE_METHOD_EXECUTION | (a) Historical SOW INIT run, 2026-07-25: `PASS format=SOW_V1`, 10-item checklist, bound to earlier SOW `51850ed1…`; format check only | `DEL/_run_records/TASK_RUN_2026-07-25_1408.md:91-95` | `b7f1a04a1941c286c8c9375ad61a47a532ac8637ac548675fc2b49261be46b86` |
| E-19 | `REQ-010` | OBSERVED_IMPLEMENTATION | Doc maps REQ-001..010 to VER-001..009 to test IDs | `V2/docs/STORE_LIFECYCLE_AND_GUARD.md:77-89` | `d1d69dcbf29a694ea62ada6b6502ffc379221415eb9a260b54fe095648cd1e48` |
| E-20 | `REQ-010` | UNKNOWN | Assertions with an interpretive contract anchor: `DUPLICATE_RECORD` code, six-value `KnownState` set, `CON-001` label, digest and path format domains | `V2/tests/storage/test_content_minimal_guard.py:106-108,124,130-133,148-155` | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E-21 | `REQ-010` | UNKNOWN | Assertion of an exact six-method `MetadataStore` public surface, which the contract does not state | `V2/tests/storage/test_store_lifecycle.py:138-139` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| E-22 | `REQ-010` | FINITE_METHOD_EXECUTION | (a) Historical SOW revision, 2026-07-25: F7 removed the kill-test import from AC-002/VER-002; `PASS format=SOW_V1` bound to `d6423bd9…`, not current bytes | `DEL/_run_records/TASK_RUN_2026-07-25_1444.md:32,37-47` | `dc391380cb938415883795ae9853275a9eccf4392a4e2046378980b9003a3e0c` |
| E-23 | `AC-010` | OBSERVED_IMPLEMENTATION | `v2-store-guard` registered: cwd `.`, unittest discover over `v2/tests/storage` | `projects/pec/software-workflow.json:14-17` | `247eb82715356e1e3f532c577ff0c9babf39c18912b14362bdfb4fc8412f5d3a` |
| E-24 | `AC-010` | OBSERVED_IMPLEMENTATION | `v2-store-guard` is absent from `always_checks` and selected only by a path rule over the nine D85 paths | `projects/pec/software-workflow.json:27,41-44` | `247eb82715356e1e3f532c577ff0c9babf39c18912b14362bdfb4fc8412f5d3a` |
| E-25 | `AC-010` | BOUNDED_LOCAL_ABSENCE | "service-core test run" is undefined; grep over `projects/pec/**/*.md` finds the phrase only in SOW acceptance lines | `DEL/ScopeOfWork.md:95` | `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` |
| E-26 | `AC-010` | OBSERVED_IMPLEMENTATION | Hosted CI routes `projects/pec/v2/**` changes to the `pec` suite | `tools/hosted-ci-routing.json:74-94` | `1850e9a4477eb8198efe2a096f5059e7249230e14a72eb98d422e04a19a08b97` |
| E-27 | `AC-010` | BOUNDED_LOCAL_ABSENCE | Hosted `pec` job runs `npm test` for core, server and agent-sidecar only; no `v2-store-guard` or `v2/tests/storage` reference in `.github/`, `hosted-ci-routing.json` or the runner | `projects/pec/tools/run-workspace-tests.ts:17` | `ba5306cb181758c6277515b898df7cbcb0ea9648f685b370ecd740ff26511d01` |
| E-28 | `AC-010` | FINITE_METHOD_EXECUTION | (b) D85 manager final registered run, 2026-09-08: `v2-store-guard` exit 0, `Ran 13 tests` OK; no commit or timestamp field | `P1/checks/MANAGER_REGISTERED_CHECKS_FINAL.json:78-97` | `63392e5ca7e75c3160fe57da2ab991b358513e3dac0b1a5d46584367030ab118` |
| E-29 | `AC-010` | OBSERVED_IMPLEMENTATION | The nine D85 attempt-2 postimage hashes equal the current HEAD bytes (recomputed) | `P1/TECHNICAL_FAN_IN.md:12-22` | `0938c96726c869146f6603d59336ea829afdffb80f0c460d5e3af3b7f7ca9e8f` |
| E-30 | `AC-010` | FINITE_METHOD_EXECUTION | (c) This inquiry's read-only observation at HEAD `d61981ee`, 2026-09-24T03:27:21Z: 13 ok, exit 0; not a measurement or acceptance | `OUT/STORAGE_SUITE_OBSERVATION.json:1-92` | `bd22aad2867794ffbacf144fa9958a8273bbec3e33953509b0554ac21dd6c02c` |
| E-31 | `AC-010` | HISTORICAL_ACCEPTANCE | D-PEC-85 granted the nine paths, including tests and registration; it grants no CHECKING, ISSUED, artifact or full DEL-01-03 acceptance | `CO/_DECISIONS/D-PEC-85_RULING_2026-09-08.md:22-44,56-62` | `67167dc5ec68a3081a43a0b74084a3c6c7d7498d6b6698362ea313e9c9874851` |
| E-32 | `AC-010` | HISTORICAL_ACCEPTANCE | D85 common fan-in accepted the technical return; `artifact_fitness_accepted`, `checking_or_issued` and `full_deliverable_or_p1_complete` are all false | `CO/D85_PRODUCTION_CLOSEOUT_2026-09-08/FINAL_VALIDATION.json:27-42` | `3f2f7e0602429985e11ca5ae7a32ae4356671b6bf5a9ff64abeec9f654f046c2` |
| E-33 | `VER-009` | OBSERVED_IMPLEMENTATION | `test_ver_009` asserts discovered IDs equal the map keys and the mapped set equals VER-001..009 (self-mapped); label-level only | `V2/tests/storage/test_store_lifecycle.py:171-189` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| E-34 | `VER-009` | FINITE_METHOD_EXECUTION | (b) D85 author verbose ledger: 13 IDs with VER mapping, all PASS, Python 3.13.7; no timestamp in the file | `P1/children/AUTHOR/VERIFICATION_EXECUTION_REMEDIATION.json:1-24` | `73da805fcdd4ff455804b27f65e3394091efc385f536f0cfa03f812b94eba2e3` |
| E-35 | `VER-009` | FINITE_METHOD_EXECUTION | (b) D85 initial review V-F002: the earlier VER-009 test was a source-tag self-assertion (preserved FAIL) | `P1/children/VERIFY/REVIEW.md:37-54` | `cf4932c5c3d9469d332142c39b692aa377d83237aa89370b33bfda77c104e896` |
| E-36 | `VER-009` | FINITE_METHOD_EXECUTION | (b) D85 backcheck closed V-F002 and called the tests substantive; it records no per-assertion contract trace | `P1/children/VERIFY_BACKCHECK_02/REVIEW.md:28-36,63-65` | `be6cb4bf3379120f64d85bdb97a23669f2923c6b988b94a87f4455dc9f91f123` |
| E-37 | `VER-009` | MISSING_OR_UNMAPPED | No executing test or recorded review evidences "no test asserts a criterion absent from this contract" | `DEL/ScopeOfWork.md:117` | `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` |
| E-38 | `VER-009` | OBSERVED_IMPLEMENTATION | (d) DEL-10-02 state `INITIALIZED`; its REM-001 and REM-002 are unchecked | `D10/_STATUS.md:3,10-18` | `e04aef7be9a67c1616d56757bdb7387c643b795fae1980178c9176fb04479415` |
| E-39 | `VER-009` | FINITE_METHOD_EXECUTION | (d) DEL-10-02's only runs are 2026-07-25 SOW and register runs (`PASS format=SOW_V1`); no kill-test execution | `D10/_run_records/TASK_RUN_2026-07-25_scope_of_work_init.md:128` | `de968c6f2e048179121266deb00f986ef2b53ecf7714e02e4f6082dd0f5f8858` |
| E-40 | `VER-009` | BOUNDED_LOCAL_ABSENCE | No kill-test harness, run or verdict in the DEL-10-02 folder (full listing) or `V2/**` (`grep kill`); the only v2 hit is this disclaimer | `V2/docs/STORE_LIFECYCLE_AND_GUARD.md:100-103` | `d1d69dcbf29a694ea62ada6b6502ffc379221415eb9a260b54fe095648cd1e48` |
| E-41 | `CURRENT-REMAINING` | HISTORICAL_ACCEPTANCE | D83 baseline: "No ## Remaining section; not warranted NONE"; Disposition UNKNOWN; `_STATUS.md` `c2f5ee7b…`. R-A (`D-PEC-83_RULING_2026-09-07.md:13`) accepted the report as concordance evidence, not functional completion, lifecycle acceptance or replacement decomposition truth; the CSV is bound at `82e9b1cd…` by `SY/FULL_02/OUTPUT_MANIFEST.json:9` | `SY/FULL_02/CONSOLIDATED_CLAIMS.csv:229` | `82e9b1cd27325da2d1bfa6ccc9a1ee834e4c7714b87366bf2186883e2985464d` |
| E-42 | `CURRENT-REMAINING` | HISTORICAL_ACCEPTANCE | D-PEC-83 A-A authorized `APPEND_REMAINING_ONLY` for 57 entries; E UNSELECTED means applying a carrier executes nothing | `CO/_DECISIONS/D-PEC-83_RULING_2026-09-07.md:13-16` | `b002945953945ac11d78e1fe0eba516909fb58ba4659e9179d49607c15be2492` |
| E-43 | `CURRENT-REMAINING` | FINITE_METHOD_EXECUTION | D83 application return: 57 carriers, 89 items appended; no item executed; Remaining-state coherence only | `CO/D83_D84_EXECUTION_2026-09-07/ITERATION_02_APPLICATION_AND_REVERSAL/ACTUAL_RETURNS/D83_APPLICATION.md:8-17,32-33` | `c32a3a75fad709c4211f5ae82297955f77ae9db8bc41d82b9bf678db40ea546d` |
| E-44 | `CURRENT-REMAINING` | OBSERVED_IMPLEMENTATION | Commit `14f42e9ce` (2026-09-07) appended `## Remaining` REM-001..003; its preimage `_STATUS.md` hash equals the D83 baseline `c2f5ee7b…` | `DEL/_STATUS.md:12-24` | `73ae042e9204f1884642f74bced1a08a0c0166c6eeec321dbcf91ff08524e5a2` |
| E-45 | `CURRENT-REMAINING` | OBSERVED_IMPLEMENTATION | REM-003 unchecked at HEAD; the Remaining bytes are identical between `14f42e9ce` and HEAD; `c49bf7938` changed only state and history | `DEL/_STATUS.md:22-24` | `73ae042e9204f1884642f74bced1a08a0c0166c6eeec321dbcf91ff08524e5a2` |
| E-46 | `CURRENT-REMAINING` | FINITE_METHOD_EXECUTION | D85 fan-in check: `remaining_rows` `PASS_BYTES_UNCHANGED_FROM_ORIGIN_MAIN`; `acceptance_performed` false | `P1/FINAL_VALIDATION.json:42-45` | `ce37c9ed530b433ce3c5691cee2f0a0ae483c9cf0776a4e190ec54617a61e5bc` |
| E-47 | `CURRENT-REMAINING` | HISTORICAL_ACCEPTANCE | D-PEC-86 I-4 authorizes this read-only inquiry and reserves owner disposition; the file is untracked at HEAD and not yet effective on shared main | `CO/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md:61` | `7cc4dd0f9065f9a79e554aae6ddad5dfdb631a28556585e8d04a7e6a6bdb682b` |
| E-48 | `CURRENT-REMAINING` | FINITE_METHOD_EXECUTION | (a) Historical QA-20 run, 2026-07-26: matrix-row format disposition; no validator was executed in the run | `DEL/_run_records/TASK_RUN_2026-07-26_qa20_D-PEC-66.md:1-6` | `8c0ed35bf617b69a93431643eef3f1eef7fb11153b4361cb15f46a0ccf211108` |
| E-49 | `OUT-003` | OBSERVED_IMPLEMENTATION | VER-005: `rejected` is computed as `attempted - accepted`, so the asserted equality (CG:100) holds by construction | `V2/src/pec_v2/adapters/storage/sqlite_store.py:83-90` | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` |
| E-50 | `OUT-003` | BOUNDED_LOCAL_ABSENCE | Guard emits nine codes (`RECORD_TYPE`, `INVALID_IDENTIFIER`, `SOURCE_CITATION`, `EMPTY_RECORD`, `FIELD_TYPE`, `INVALID_FIELD_NAME`, `DUPLICATE_FIELD`, `UNKNOWN_FIELD_CLASS`, `INVALID_VALUE`) and the `<unknown>` record location; no storage test asserts any of them (only `DUPLICATE_RECORD`, CG:108); scope `V2/tests/storage/**`, method grep for `code` and `<unknown>` | `V2/src/pec_v2/core/content_minimal_guard.py:132-224` | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` |

Class counts:

| Class | Rows | Claims with class |
|---|---|---|
| OBSERVED_IMPLEMENTATION | 22 | 5 |
| BOUNDED_LOCAL_ABSENCE | 8 | 3 |
| MISSING_OR_UNMAPPED | 1 | 1 |
| FINITE_METHOD_EXECUTION | 11 | 5 |
| HISTORICAL_ACCEPTANCE | 5 | 2 |
| UNKNOWN | 3 | 2 |
| Total | 50 | 5 linked claims |

## 5. Per-claim summary

| Claim | Classes present | Still missing | Residual status |
|---|---|---|---|
| `OUT-003` | OBSERVED_IMPLEMENTATION, BOUNDED_LOCAL_ABSENCE, UNKNOWN, FINITE_METHOD_EXECUTION | Hosting-checkout VER-001 run (hosting-checkout identity is UNKNOWN per REM-001 U-2); non-derived count reconciliation and assertion of the unasserted failure codes and `<unknown>` location for VER-005; live-connection or running-process VER-002 case; call-graph VER-003; full persisted dump for VER-004; shared corpus and by-construction proof for VER-006; manifest inspection and DEL-01-05 re-run for VER-007; executing VER-008 document review; any artifact acceptance of the suite | `EVIDENCED_PARTIAL` |
| `REQ-010` | OBSERVED_IMPLEMENTATION, UNKNOWN, FINITE_METHOD_EXECUTION | Contract trace showing that no assertion defines scope, requirements or criteria (candidates are in E-20 and E-21) | `EVIDENCED_PARTIAL` / `UNKNOWN` on the "shall not define" clause |
| `AC-010` | OBSERVED_IMPLEMENTATION, BOUNDED_LOCAL_ABSENCE, FINITE_METHOD_EXECUTION, HISTORICAL_ACCEPTANCE | A definition of "the service-core test run"; evidence that the suite executes there (the suite is path-selected, absent from `always_checks` and not run by hosted CI); the "implements VER-001..008" fitness (§4.1); the no-new-criterion clause | `EVIDENCED_PARTIAL` / `UNKNOWN` on "executes in the service-core test run" |
| `VER-009` | OBSERVED_IMPLEMENTATION, FINITE_METHOD_EXECUTION, MISSING_OR_UNMAPPED, BOUNDED_LOCAL_ABSENCE | The second clause of VER-009; semantic, not label-level, correspondence for VER-001..008; any DEL-10-02 kill-test evidence (none exists, and none is expected from this deliverable) | `EVIDENCED_PARTIAL` (first clause, label level) / `NO_LOCAL_EVIDENCE` (second clause) |
| `CURRENT-REMAINING` | HISTORICAL_ACCEPTANCE, FINITE_METHOD_EXECUTION, OBSERVED_IMPLEMENTATION | An owner disposition of the REM-003 row. The D-PEC-86 authority for this inquiry is untracked at HEAD | `DOCUMENTARY_APPLIED_OPEN`: the Remaining section exists since `14f42e9ce`, and REM-003 is unchecked at HEAD |

## 6. UNKNOWN entries

- **U-1 (AC-010).** It is unknown whether the registered, path-selected `v2-store-guard` check is "the service-core test run". No accepted definition was found in the bounded search (E-25). *Resolved by* an owner or accepted-source definition of that run and of its trigger.
- **U-2 (REQ-010, VER-009, AC-010).** It is unknown whether any storage assertion states a criterion absent from the contract. The candidates are E-20 and E-21: `DUPLICATE_RECORD`, the six-value `KnownState` set, the `CON-001` label, the digest and path format domains, and the exact six-method `MetadataStore` surface. *Resolved by* an authorized independent assertion-by-assertion contract trace and an owner ruling on each candidate.
- **U-3 (OUT-003, VER-007).** It is unknown whether DEL-01-05 is "available" for the VER-007 re-run, and whether its core-only target would ever evaluate `adapters/storage` (E-14, E-15). *Resolved by* a DEL-01-05 lifecycle or owner determination, followed by a separately authorized run.
- **U-4 (OUT-003, VER-002).** It is unknown whether open-handle `delete()` satisfies "while it is running" when no PEC process exists (E-05 to E-07). *Resolved by* an owner interpretation. This overlaps REM-001.
- **U-5 (OUT-003, VER-006).** It is unknown whether test-local stand-ins with differing values satisfy "the same fixture corpus" and the "by construction" clause (E-11). *Resolved by* an owner interpretation. This overlaps REM-002.
- **U-6 (OUT-003, VER-008).** It is unknown whether VER-008, a documented-rule review, can have or needs an "executing automated test" under VER-009 (E-16, E-17). *Resolved by* an owner ruling.
- **U-7 (OUT-003, VER-001).** It is unknown whether the scratch-checkout test suffices for the "hosting checkout" wording (E-02 to E-04). Which directory is the hosting checkout is itself held UNKNOWN in REM-001 U-2. *Resolved by* an owner ruling, or by a separately authorized hosting-checkout measurement.
- **U-8 (AC-010, VER-009).** The D85 check and ledger records carry no commit or timestamp field (E-28, E-34). They bind to HEAD only through equality of the nine file hashes (E-29). Environment factors other than the Python version (Git version, OS) are unrecorded. *Resolved by* nothing further unless the owner requires an environment-bound run.
- **U-9 (VER-009, via the item text).** No DEL-10-02 kill-test evidence exists (E-38 to E-40). The system-level property of AC-002 and SOW-055 remains unknown, and nothing here bears on it. *Resolved by* DEL-10-02's own production and inquiries.
- **U-10 (CURRENT-REMAINING).** The publication and effectiveness state of D-PEC-86, the cited authority for this inquiry, is unknown at HEAD: the file is untracked (E-47). *Resolved by* the owner, or by CHANGE publication records.

## 7. Exact unresolved obligations for owner disposition

| ID | Claim(s) | Unresolved | Authority needed |
|---|---|---|---|
| O-3-1 | AC-010, OUT-003 | Define "the service-core test run" and decide whether the path-selected `v2-store-guard` check, which is not in `always_checks` and not in hosted CI, satisfies "executes in". Any wiring change is production | Owner ruling; separate production or CI scope if wiring changes |
| O-3-2 | REQ-010, VER-009, AC-010 | The "no test asserts a criterion absent from this contract" clause has no evidence. The candidate assertions are in E-20 and E-21 | An owner-authorized independent contract-trace review, then an owner ruling per candidate |
| O-3-3 | OUT-003, VER-009 (VER-001) | The hosting-checkout populated-store `git check-ignore`/`git status` run is absent; only a scratch checkout is tested. The hosting-checkout identity is UNKNOWN (REM-001 U-2) | Owner ruling on sufficiency, or a separate measurement run |
| O-3-4 | OUT-003, VER-009 (VER-002) | The "while it is running" case is covered only as open-handle close-then-delete; there is no running PEC process | Owner interpretation; any runtime test is later production (coordinate with REM-001) |
| O-3-5 | OUT-003, VER-009 (VER-003) | The test uses text and AST token checks, not an import or call-graph inspection | Owner ruling on sufficiency; any added test is production (coordinate with REM-002) |
| O-3-6 | OUT-003, VER-009 (VER-004) | "Dump every persisted field" is evidenced only through API readback | Owner ruling; any added test is production (coordinate with REM-002) |
| O-3-7 | OUT-003, VER-009 (VER-006) | There is no shared fixture corpus and no by-construction assertion; the three shapes are test-local stand-ins | Owner interpretation; real ingest paths belong to later deliverables (DEL-03-01, DEL-01-02, DEL-07-01) |
| O-3-8 | OUT-003, VER-009 (VER-007) | There is no dependency manifest. The DEL-01-05 re-run is not performed, and the posture target excludes `adapters/storage` | DEL-01-05 lifecycle and owner ruling; a separate authorized run |
| O-3-9 | OUT-003, VER-009 (VER-008) | The documented-rule review against PRD §7.1 and §7.2 is not an executing test; only the D85 backcheck statement exists | Owner ruling on the form VER-008 evidence must take |
| O-3-10 | VER-009 (via the item text) | Store-local delete and recreate must not be presented as kill-test evidence, and DEL-10-02 has no kill-test evidence (`INITIALIZED`, SOW-format runs only) | DEL-10-02 production and its REM-001/REM-002; owner |
| O-3-11 | OUT-003, AC-010 | There is no artifact or fitness acceptance of the test suite: D85 is technical fan-in only, with `artifact_fitness_accepted false` | Owner acceptance or a governed CHECKING route under a separate ruling |
| O-3-12 | CURRENT-REMAINING | The disposition of the unchecked REM-003 row, which was applied by `14f42e9ce` under D-PEC-83 A-A, given this report. No checkbox or `_STATUS.md` edit is made or proposed here | Owner disposition (D-PEC-86 I-4 reserves it) |
| O-3-13 | CURRENT-REMAINING | D-PEC-86, the authority cited for this inquiry, is untracked at HEAD | Owner or CHANGE publication decision |
| O-3-14 | OUT-003, VER-009 (VER-005) | VER-005 is partial. The count reconciliation is derived by construction (E-49), and nine failure codes (including `UNKNOWN_FIELD_CLASS` and `INVALID_VALUE`) plus the `<unknown>` record location are never asserted (E-50). Only `DUPLICATE_RECORD` is asserted | Owner ruling on sufficiency; any added test is production. Coordinate with REM-002 O-2-4 |

## 8. Limits

- No source, test, configuration, `_STATUS.md`, `MEMORY.md`, SOW or Git state was changed. The only writes are the three files in `OUT/`. Raw suite output was captured to the session scratchpad, which is outside the repository, and is not retained here.
- No review of the D85 correction chain beyond the cited records. No reproduction of the other four registered checks. No re-execution of D85 manifests or of the reverse-patch recovery.
- No reading of PRD §7.1 or §7.2, and no independent judgment of whether the documented rule matches those inventories.
- No reading of D-PEC-85's selected V2 proposal or of the D83 R5 application folder beyond the accepted return summary.
- No DEL-10-02 or DEL-01-05 execution. No interpretation of AC-002's system-level clause.
- The observation run is one execution, on one host with Python 3.13.7. It is not a measurement, acceptance or VER discharge.
- Search misses establish absence only within the stated scopes.

### Revision 1 (verifier cycle 1)

- **BLOCKING fix.** VER-005 is now marked **Partial** in §4.1, in the §4.1 summary sentence, in E-10, in the OUT-003 "Still missing" cell and in §7. Two rows are new: E-49 (the derived `rejected` count, `sqlite_store.py:88`) and E-50 (the unasserted failure codes and `<unknown>` location). O-3-14 is new and coordinates with REM-002 O-2-4.
- **E-41.** Added `D-PEC-83_RULING_2026-09-07.md:13` (R-A scope and what it did not accept) and `SY/FULL_02/OUTPUT_MANIFEST.json:9` (the binding at `82e9b1cd…`).
- **E-03 and §4.1 VER-001.** These now name the PEC project checkout (`projects/pec`) and record that hosting-checkout identity is UNKNOWN per REM-001 U-2. U-7 and O-3-3 were aligned to match.
- **E-47.** Added "not yet effective on shared main".
- The suite was not re-run. Class counts, manifest rows, sources, obligations and `report_sha256` were regenerated.

### Revision 2 (verifier cycle 2)

- E-50, the §4.1 VER-005 cell and O-3-14 now count nine unasserted codes, adding `UNKNOWN_FIELD_CLASS` (:206) and `INVALID_VALUE` (:224), plus the `<unknown>` location. The E-50 locator is extended to `content_minimal_guard.py:132-224`. The suite was not re-run.
