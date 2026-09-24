# DEL-01-03-REM-002 — Derivative evidence report (read-only inquiry)

## 1. Header

| Field | Value |
|---|---|
| Item | DEL-01-03-REM-002 |
| Date | 2026-09-23 (local; suite observation UTC 2026-09-24T03:25:48Z) |
| HEAD | `d61981ee2b9e36c82c6cdd28d4f3c12d3d32a69b` |
| Author role | TASK (Type 2), instruction-asserted |
| Serving model | `claude-opus-5-5[1m]`, as reported by the host system prompt; not independently verified |
| Parent | WORKING_ITEMS manager for the PEC loop (dispatched by HELP_HUMAN under D-PEC-86 §3 I-4) |
| Brief | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-002/CHILD_BRIEF.md` `a1d49b7f47eb9d443d4e876319d6076831ec5172230368b23e67fde6d100be9a` |
| Preflight | `historical-read-only-inspection` ALLOW (manager-run; copied into the manifest) |

This report is derivative evidence. It is not a contract, implementation, test, measurement, acceptance, or lifecycle or production act. It does not dispose of any Remaining item.

## 2. Scope and linked claims

13 claims from the D83 `PROPOSED_ITEMS.csv` row 8 and `CLAIM_TO_PROPOSAL_MAP.json`. SOW = `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/ScopeOfWork.md` (`986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341`, matching the preflight hash). The D83 baseline (`CONSOLIDATED_CLAIMS.csv`, source commit `2be412cc`, before D85 production) records Disposition `UNKNOWN` for all 13. That baseline is historical only.

| Claim | SOW line | D83 baseline row (CONSOLIDATED_CLAIMS.csv) |
|---|---|---|
| DEL-01-03::OUT-002 | ScopeOfWork.md:60 | line 180 (UNKNOWN) |
| DEL-01-03::REQ-003 | ScopeOfWork.md:77 | line 193 (UNKNOWN) |
| DEL-01-03::REQ-004 | ScopeOfWork.md:78 | line 194 (UNKNOWN) |
| DEL-01-03::REQ-005 | ScopeOfWork.md:79 | line 195 (UNKNOWN) |
| DEL-01-03::REQ-006 | ScopeOfWork.md:80 | line 196 (UNKNOWN) |
| DEL-01-03::AC-003 | ScopeOfWork.md:88 | line 203 (UNKNOWN) |
| DEL-01-03::AC-004 | ScopeOfWork.md:89 | line 204 (UNKNOWN) |
| DEL-01-03::AC-005 | ScopeOfWork.md:90 | line 205 (UNKNOWN) |
| DEL-01-03::AC-006 | ScopeOfWork.md:91 | line 206 (UNKNOWN) |
| DEL-01-03::VER-003 | ScopeOfWork.md:111 | line 214 (UNKNOWN) |
| DEL-01-03::VER-004 | ScopeOfWork.md:112 | line 215 (UNKNOWN) |
| DEL-01-03::VER-005 | ScopeOfWork.md:113 | line 216 (UNKNOWN) |
| DEL-01-03::VER-006 | ScopeOfWork.md:114 | line 217 (UNKNOWN) |

Out of scope (held REM-004): CON-001, REQ-009, AC-009, VER-008. They are cited only where REQ-004/AC-004 depend on CON-001.

## 3. Method (read-only)

- Read the deliverable context files, the P1_STORE_GUARD_01 run records (activation, fan-in, handoff, final validation, check registration, work graph, final registered-check evidence, author verbose execution ledger, initial review, backcheck review), the D85 authorized scope, the fan-in and handoff, the D-PEC-85 ruling, the D-PEC-86 dispatch basis, the store port, guard, adapter, storage tests and doc, `software-workflow.json` (`v2-store-guard` at lines 14-17 and 41-44), `.gitignore` line 17, the DEL-10-02 `_STATUS.md` and `_DEPENDENCIES.md`, the D83 baseline files, and PRD passages by locator only (PEC-K-10:184, §7.1:199-214, §7.2:215-224, PEC-ORI-006:262, PEC-RCN-002:269, PEC-PRS-002:289, PEC-STR-001:300, PEC-SVC-005:338).
- Confirmed that all nine D85 product and configuration files hash identically at HEAD to the postimages in `TECHNICAL_FAN_IN.md` lines 12-22 (no drift).
- Ran bounded `grep` searches, with the scopes and patterns stated in the rows marked BOUNDED_LOCAL_ABSENCE.
- Ran the registered storage suite once, read-only, as the brief permits. The result is in `STORAGE_SUITE_OBSERVATION.json`: 13 ok, exit 0. `git status --short --ignored projects/pec` was identical before and after the run. The observation is not a new measurement, an acceptance or a VER discharge.
- No other program was executed against the product. No ad hoc probe was run, including for U-3.

## 4. Evidence table

| Row | Claim | Evidence class | Observation (one line) | Source path:lines | SHA-256 |
|---|---|---|---|---|---|
| E01 | OUT-002 | OBSERVED_IMPLEMENTATION | Fixed, policy-free `ContentMinimalGuard.guard` admits only the five `FieldClass` members; any failure yields no guarded record. | `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py`:15-20;129-197 | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` |
| E02 | OUT-002 | OBSERVED_IMPLEMENTATION | `SqliteMetadataStore` holds one guard; `admit_batch` guards every candidate before `BEGIN IMMEDIATE` and inserts only accepted decisions. | `projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py`:42;45-63 | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` |
| E03 | OUT-002 | HISTORICAL_ACCEPTANCE | D-PEC-85 owner ruling granted production of the nine paths only; it grants no CHECKING, ISSUED, artifact acceptance or full DEL-01-03 acceptance. | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-85_RULING_2026-09-08.md`:22-44;56-62 | `67167dc5ec68a3081a43a0b74084a3c6c7d7498d6b6698362ea313e9c9874851` |
| E04 | OUT-002 | HISTORICAL_ACCEPTANCE | D85 common fan-in accepted the technical return only; artifact fitness acceptance, CHECKING, ISSUED and full DEL-01-03/P1 completion remain unopened. | `projects/pec/execution/_Coordination/D85_PRODUCTION_CLOSEOUT_2026-09-08/FAN_IN.md`:1-8;34-39 | `bf0706c2dac1a9aaba2829ffc940983e8958e57a3c7aade9215dcd43fc7d9a32` |
| E05 | REQ-003 | OBSERVED_IMPLEMENTATION | Record writes: the only `INSERT` statements are in `_insert_guarded`, whose single call site is inside `admit_batch` after a guard acceptance. | `projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py`:54-63;248-267 | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` |
| E06 | REQ-003 | OBSERVED_IMPLEMENTATION | Lifecycle writes (no record rows): `reopen` does mkdir, connect, two PRAGMAs, `CREATE TABLE IF NOT EXISTS` DDL and commit; `delete` unlinks four fixed files; `reset` = delete + reopen. | `projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py`:123-149;225-246 | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` |
| E07 | REQ-003 | OBSERVED_IMPLEMENTATION | Bypass resistance is by naming convention, not enforced: `_insert_guarded` is a staticmethod accepting any `GuardedRecord` (a public dataclass, G:101-107) and `_connection` is a plain attribute. | `projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py`:41;248-249 | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` |
| E08 | REQ-003 | BOUNDED_LOCAL_ABSENCE | Grep for store-module imports and store-path literals (`pec_v2.adapters.storage`, `content_minimal_guard`, `SqliteMetadataStore`, `pec-v2/record_store`) and, in v2, for `sqlite3`, `.execute(`, INSERT/UPDATE/DELETE/REPLACE: no other store writer; SQL only in sqlite_store.py. | `projects/pec (excluding execution/ and .git)`:n/a | `n/a (search scope)` |
| E09 | REQ-003 | FINITE_METHOD_EXECUTION | Independent backcheck (2026-09-08, technical-fan-in PASS) records `admit_batch()` as the sole record-write surface; a review record, not acceptance. | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/children/VERIFY_BACKCHECK_02/REVIEW.md`:47-50 | `be6cb4bf3379120f64d85bdb97a23669f2923c6b988b94a87f4455dc9f91f123` |
| E10 | AC-003 | FINITE_METHOD_EXECUTION | D85 author verbose run (Python 3.13.7, 13 tests OK) records `test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface` PASS. | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/children/AUTHOR/VERIFICATION_EXECUTION_REMEDIATION.json`:20 | `73da805fcdd4ff455804b27f65e3394091efc385f536f0cfa03f812b94eba2e3` |
| E11 | AC-003 | MISSING_OR_UNMAPPED | `test_ver_003` is a textual/AST heuristic (one `admit_batch` def, one guard-call string, no `INSERT ` before `_insert_guarded`); it does not enumerate every persistence call or prove a single caller of `_insert_guarded`. | `projects/pec/v2/tests/storage/test_store_lifecycle.py`:144-150 | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| E12 | VER-003 | FINITE_METHOD_EXECUTION | This inquiry's observation run: `test_ver_003...` ok (not a VER discharge). | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-002/STORAGE_SUITE_OBSERVATION.json`:23 | `c2460fc0f4934f72b2cf37ddf5b60e8a3f39119dae7d1bcd1981fb1c7c0317f9` |
| E13 | VER-003 | MISSING_OR_UNMAPPED | VER-003 names inspection of the write surface and import/call graph; no recorded call-graph or write-surface inventory artifact was located. | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/ScopeOfWork.md`:111 | `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` |
| E14 | REQ-004 | OBSERVED_IMPLEMENTATION | Each class has an exact runtime domain (RepositoryPath; non-bool int >= 0; sha1/sha256 ShaDigest; six KnownState values; blake2b-256 ContentHash); wrappers are revalidated at admission; unknown class rejected. | `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py`:199-225;241-285 | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` |
| E15 | REQ-004 | OBSERVED_IMPLEMENTATION | Schema `CHECK` limits `field_class` to the five labels; the records table holds only id, source path and optional SHA pair. | `projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py`:229-244 | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` |
| E16 | REQ-004 | OBSERVED_IMPLEMENTATION | PATH domain checks non-empty, no backslash/NUL, normalized, relative, no `..`; no length bound and no whitespace/newline restriction; same validator applies to record `source_path`. | `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py`:288-296 | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` |
| E17 | REQ-004 | OBSERVED_IMPLEMENTATION | Every non-KnownState STATE value is rejected with constraint `CON-001`; the prose-versus-state separation rule itself belongs to held REM-004. | `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py`:217-224 | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` |
| E18 | REQ-004 | FINITE_METHOD_EXECUTION | Initial review V-F001 (forged wrappers persisted arbitrary text; VR:17-35) was preserved; the corrected-candidate backcheck closed it and recorded content-boundary PASS. | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/children/VERIFY_BACKCHECK_02/REVIEW.md`:11-26;40-42 | `be6cb4bf3379120f64d85bdb97a23669f2923c6b988b94a87f4455dc9f91f123` |
| E19 | AC-004 | FINITE_METHOD_EXECUTION | D85 run records `test_ver_004_content_diff_prose_unknown_classes_and_misleading_keys_are_rejected_atomically` PASS (fixtures TG:77-93: 5 attempted, 0 accepted, 5 rejected, empty readback). | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/children/AUTHOR/VERIFICATION_EXECUTION_REMEDIATION.json`:11 | `73da805fcdd4ff455804b27f65e3394091efc385f536f0cfa03f812b94eba2e3` |
| E20 | AC-004 | MISSING_OR_UNMAPPED | Two mechanisms, neither inspects content: file-body and diff-hunk (TG:80-81) are raw `str` STATE values failing the KnownState identity check (G:213,270-281); register-prose (TG:82) is a raw `str` PATH value failing the wrapper-type check (G:242). No fixture places content-shaped text in a validly constructed `RepositoryPath` (forged cases TG:170,189 use `..`). | `projects/pec/v2/tests/storage/test_content_minimal_guard.py`:80-82 | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E21 | AC-004 | MISSING_OR_UNMAPPED | "No residue" is asserted only as `read_all()` returning empty, i.e. through the adapter's own two-table reader (A:93-116); no raw dump of the database file, WAL/journal sidecars or `sqlite_master`. | `projects/pec/v2/tests/storage/test_content_minimal_guard.py`:92 | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E22 | VER-004 | FINITE_METHOD_EXECUTION | This inquiry's observation run: both `test_ver_004...` tests and the forged-wrapper test ok (not a VER discharge). | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-002/STORAGE_SUITE_OBSERVATION.json`:13-14;17 | `c2460fc0f4934f72b2cf37ddf5b60e8a3f39119dae7d1bcd1981fb1c7c0317f9` |
| E23 | VER-004 | FINITE_METHOD_EXECUTION | D85 registered check `v2-store-guard` PASS, 13 tests, exit 0 (2026-09-08). | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/checks/MANAGER_REGISTERED_CHECKS_FINAL.json`:78-97 | `63392e5ca7e75c3160fe57da2ab991b358513e3dac0b1a5d46584367030ab118` |
| E24 | VER-004 | BOUNDED_LOCAL_ABSENCE | Case-insensitive grep for `dump` over all 53 files of the P1 run records: zero hits; no persisted-field dump or per-fixture outcome artifact located. | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/** (53 files)`:n/a | `n/a (search scope)` |
| E25 | REQ-005 | OBSERVED_IMPLEMENTATION | `AdmissionFailure` carries record_id, field_name, code, message and optional constraint; one failure per offending element; duplicate insert yields `DUPLICATE_RECORD` (A:64-73); unexpected errors roll back and re-raise (A:78-81). | `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py`:110-116;139-187 | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` |
| E26 | REQ-005 | OBSERVED_IMPLEMENTATION | A non-`MetadataRecord` candidate or non-string record id is reported as record `<unknown>`, and `AdmissionFailure` carries no input index, so such a rejection is not located to a specific input. | `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py`:133-145 | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` |
| E27 | REQ-005 | BOUNDED_LOCAL_ABSENCE | Grep `-i` for `PEC-ORI-006` and `feed` over all of v2: zero hits; v2/src has no ingest/feed code. No feed exists for which a limitation could be stated. | `projects/pec/v2 (all files)`:n/a | `n/a (search scope)` |
| E28 | REQ-005 | UNKNOWN | The PEC-ORI-006 clause (feed limitation stated, not omitted) has no evidence either way. | `projects/pec/docs/PRD.md`:262 | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| E29 | AC-005 | OBSERVED_IMPLEMENTATION | `AdmissionResult.rejected` is computed as attempted minus accepted, so attempted = accepted + rejected holds by construction; it is not an independent reconciliation. | `projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py`:83-91 | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` |
| E30 | AC-005 | FINITE_METHOD_EXECUTION | D85 run records `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution` PASS (one accepted, one rejected at (record, field); duplicate reported, original preserved). | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/children/AUTHOR/VERIFICATION_EXECUTION_REMEDIATION.json`:12 | `73da805fcdd4ff455804b27f65e3394091efc385f536f0cfa03f812b94eba2e3` |
| E31 | AC-005 | MISSING_OR_UNMAPPED | Only the adapter code `DUPLICATE_RECORD` is asserted (TG:108); none of the nine guard codes (RECORD_TYPE, INVALID_IDENTIFIER, SOURCE_CITATION, EMPTY_RECORD, FIELD_TYPE, INVALID_FIELD_NAME, DUPLICATE_FIELD, UNKNOWN_FIELD_CLASS, INVALID_VALUE; G:136-224) is asserted, nor the `<unknown>` record-location path; no-truncation evidence is readback of short values (TG:52-75). | `projects/pec/v2/tests/storage/test_content_minimal_guard.py`:95-109 | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E32 | VER-005 | FINITE_METHOD_EXECUTION | This inquiry's observation run: `test_ver_005...` ok (not a VER discharge). | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-002/STORAGE_SUITE_OBSERVATION.json`:15 | `c2460fc0f4934f72b2cf37ddf5b60e8a3f39119dae7d1bcd1981fb1c7c0317f9` |
| E33 | VER-005 | MISSING_OR_UNMAPPED | The count equality asserted at TG:100 compares derived quantities; the independent per-record reconciliation is limited to accepted IDs (TG:102) and failure locations (TG:103; set equality at TG:93). | `projects/pec/v2/tests/storage/test_content_minimal_guard.py`:100-103 | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E34 | REQ-006 | OBSERVED_IMPLEMENTATION | By-construction reasoning only: the guard takes no policy parameter and the port exposes one admission method (PT:24-28), so any caller reaches the same guard. | `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py`:129-132 | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` |
| E35 | REQ-006 | BOUNDED_LOCAL_ABSENCE | Grep `-i` for reconcil, presence, event, ingest, feed over v2/src: zero hits. No real P1 reconciler, P3 presence/Git or event ingest path exists. | `projects/pec/v2/src (11 .py files)`:n/a | `n/a (search scope)` |
| E36 | REQ-006 | HISTORICAL_ACCEPTANCE | D85 authorized scope excluded reconciler and orientation/runtime/network integration; uniform ingest over real paths was outside the ruled slice. | `projects/pec/execution/_Coordination/D85_EXECUTION_2026-09-08/AUTHORIZED_SCOPE.md`:20-25 | `301fd94e3fd054f21e429319dbe38d676ada694eb433035324b1cf3d80995743` |
| E37 | AC-006 | FINITE_METHOD_EXECUTION | D85 run records `test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary` PASS. | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/children/AUTHOR/VERIFICATION_EXECUTION_REMEDIATION.json`:13 | `73da805fcdd4ff455804b27f65e3394091efc385f536f0cfa03f812b94eba2e3` |
| E38 | AC-006 | MISSING_OR_UNMAPPED | Stand-ins are one `MetadataRecord` type with different record ids and different single STATE strings: not the same fixture corpus, not distinct shapes, STATE class only. | `projects/pec/v2/tests/storage/test_content_minimal_guard.py`:111-125 | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| E39 | VER-006 | FINITE_METHOD_EXECUTION | This inquiry's observation run: `test_ver_006...` ok (not a VER discharge). | `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/REMAINING_EVIDENCE_DEL-01-03-REM-002/STORAGE_SUITE_OBSERVATION.json`:16 | `c2460fc0f4934f72b2cf37ddf5b60e8a3f39119dae7d1bcd1981fb1c7c0317f9` |
| E40 | VER-006 | UNKNOWN | "Further shape needs no new content check" rests on design text (DOC:70-75) and stand-ins; no executing evidence over a real path exists. | `projects/pec/v2/docs/STORE_LIFECYCLE_AND_GUARD.md`:93-98 | `d1d69dcbf29a694ea62ada6b6502ffc379221415eb9a260b54fe095648cd1e48` |

Cross-reference paths cited inline in the table: `G` = `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py` (`3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01`); `A` = `projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py` (`03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8`); `TG` = `projects/pec/v2/tests/storage/test_content_minimal_guard.py` (`2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127`); `PT` = `projects/pec/v2/src/pec_v2/core/ports/store.py` (`2f5cdbf50bb1ed8b02ce8b7d820f81b749da4ca2d62e195afec39c78a035a4af`); `VR` = `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/children/VERIFY/REVIEW.md` (`cf4932c5c3d9469d332142c39b692aa377d83237aa89370b33bfda77c104e896`); `DOC` = `projects/pec/v2/docs/STORE_LIFECYCLE_AND_GUARD.md` (`d1d69dcbf29a694ea62ada6b6502ffc379221415eb9a260b54fe095648cd1e48`).

## 5. Per-claim summary

| Claim | Classes present | Still missing | Residual status |
|---|---|---|---|
| OUT-002 | OBSERVED_IMPLEMENTATION, HISTORICAL_ACCEPTANCE | Artifact/lifecycle acceptance; items under REQ-003..006. | EVIDENCED_PARTIAL |
| REQ-003 | OBSERVED_IMPLEMENTATION, BOUNDED_LOCAL_ABSENCE, FINITE_METHOD_EXECUTION | Enforced (non-conventional) boundary; future in-process callers. | EVIDENCED_PARTIAL |
| REQ-004 | OBSERVED_IMPLEMENTATION, FINITE_METHOD_EXECUTION | PATH domain has no content-shape bound; CON-001 rule held in REM-004. | EVIDENCED_PARTIAL_WITH_OPEN_GAP |
| REQ-005 | OBSERVED_IMPLEMENTATION, BOUNDED_LOCAL_ABSENCE, UNKNOWN | Location for `<unknown>` candidates; PEC-ORI-006 feed-level statement. | EVIDENCED_PARTIAL_WITH_UNKNOWN |
| REQ-006 | OBSERVED_IMPLEMENTATION, BOUNDED_LOCAL_ABSENCE, HISTORICAL_ACCEPTANCE | Any real ingest path (bounded local absence). | NO_LOCAL_EVIDENCE_FOR_REAL_PATHS |
| AC-003 | MISSING_OR_UNMAPPED, FINITE_METHOD_EXECUTION | Inspection covering every persistence call. | EVIDENCED_PARTIAL |
| AC-004 | MISSING_OR_UNMAPPED, FINITE_METHOD_EXECUTION | Content inside valid wrappers; full persisted-field inspection. | EVIDENCED_PARTIAL_WITH_UNKNOWN |
| AC-005 | OBSERVED_IMPLEMENTATION, MISSING_OR_UNMAPPED, FINITE_METHOD_EXECUTION | Independent count reconciliation; untested failure codes; truncation on long values. | EVIDENCED_PARTIAL |
| AC-006 | MISSING_OR_UNMAPPED, FINITE_METHOD_EXECUTION | Same corpus across distinct shapes; real paths. | EVIDENCED_PARTIAL |
| VER-003 | MISSING_OR_UNMAPPED, FINITE_METHOD_EXECUTION | Call-graph inspection artifact. | METHOD_PARTIALLY_EXECUTED |
| VER-004 | BOUNDED_LOCAL_ABSENCE, FINITE_METHOD_EXECUTION | Persisted-field dump; per-fixture outcome record. | METHOD_PARTIALLY_EXECUTED |
| VER-005 | MISSING_OR_UNMAPPED, FINITE_METHOD_EXECUTION | Non-derived input-versus-outcome count reconciliation. | METHOD_PARTIALLY_EXECUTED |
| VER-006 | FINITE_METHOD_EXECUTION, UNKNOWN | Same-corpus run; by-construction claim unexecuted. | METHOD_PARTIALLY_EXECUTED_WITH_UNKNOWN |

No status above means satisfied, accepted or closed.

## 6. UNKNOWN entries

- **U-1** (REQ-005, AC-005): Whether a feed that cannot be admitted is stated as a limitation (PEC-ORI-006). No feed exists in v2. Would be resolved by: A real feed ingest path with its limitation reporting and executing evidence (e.g. DEL-03-01 reconciler).
- **U-2** (REQ-006, AC-006, VER-006): Whether real reconciler, presence/Git and event ingest paths route through admit_batch and reject identically. Would be resolved by: Integration evidence from DEL-03-01, the presence/Git owner and DEL-07-01 when those paths exist.
- **U-3** (REQ-004, AC-004): Whether file-content, diff or register-prose text wrapped in a validly constructed RepositoryPath is admitted. Code reading shows no rule that would reject it; no execution exercised it. Would be resolved by: A separately authorized test or measurement, or a production ruling on the PATH domain.
- **U-4** (AC-004, VER-004): Whether any content residue exists outside the adapter read path (sidecars, free pages, other tables) after rejection. Would be resolved by: A separately authorized full persisted-field and file-level dump.
- **U-5** (REQ-003, AC-003): Whether any future in-process caller bypasses the guard through private members; the boundary is conventional. Would be resolved by: Per-consumer call-graph inspection, or a production ruling on structural enforcement.
- **U-6** (REQ-004): The test separating a state token from prose (CON-001) is unresolved; it belongs to held REM-004. Would be resolved by: The owner disposition of REM-004 (CON-001), or SCOPE_CHANGE.

## 7. Exact unresolved obligations for owner disposition

- **O-2-1**. Claims: REQ-003, AC-003, VER-003. Unresolved: Decide whether the heuristic test_ver_003 and conventional privacy suffice for the single boundary, or whether a recorded write-surface/call-graph inventory (record writes versus lifecycle writes) and/or structural enforcement is required. Authority needed: Owner ruling; any new artifact, test or code change needs a separate DEL-01-03 production ruling.
- **O-2-2**. Claims: REQ-004, AC-004. Unresolved: Decide the PATH-domain gap: no length or whitespace/newline bound, so content-shaped text in a valid RepositoryPath is not rejected by any inspected rule (U-3). Authority needed: Production ruling; SCOPE_CHANGE or REM-004/CON-001 routing if it changes what the store may hold.
- **O-2-3**. Claims: AC-004, VER-004. Unresolved: Decide whether raw-str fixtures and read_all-based residue checking meet "dump every persisted field", or whether a realistic corpus and full persisted-field dump are required (U-4). Authority needed: Separate measurement run, or production ruling for a test change.
- **O-2-4**. Claims: REQ-005, AC-005, VER-005. Unresolved: Decide whether `<unknown>` record location with no input index, nine unasserted guard failure codes (including UNKNOWN_FIELD_CLASS and INVALID_VALUE), and a derived rejected count satisfy located rejection and no-silent-loss accounting. Authority needed: Owner acceptance of the current accounting, or production ruling for a change.
- **O-2-5**. Claims: REQ-005. Unresolved: Route the PEC-ORI-006 feed-limitation clause, which stays UNKNOWN (U-1), to the deliverables that will own feeds. Authority needed: Owner routing decision; later production in DEL-03-01 or orientation owners.
- **O-2-6**. Claims: REQ-006, AC-006, VER-006. Unresolved: Decide whether stand-ins suffice for this deliverable, given the bounded local absence of real ingest paths. They use different strings, only the STATE class and one record type, and the by-construction claim is not executed (U-2). Authority needed: Owner ruling; integration evidence in DEL-03-01, the presence/Git owner and DEL-07-01; any test revision needs a production ruling.
- **O-2-7**. Claims: OUT-002. Unresolved: No artifact or lifecycle acceptance of the guard exists (D85 technical fan-in only). Decide the disposition of DEL-01-03-REM-002 and of any reliance beyond technical fan-in. Authority needed: Owner acceptance / owner Remaining disposition.
- **O-2-8**. Claims: REQ-004, AC-004. Unresolved: Record that prose-versus-state rejection depends on CON-001 (REQ-009, AC-009, VER-008 in held REM-004); the in-scope claims cannot resolve that dependency (U-6). Authority needed: Owner ruling on REM-004 or SCOPE_CHANGE.

## 8. Limits

- This inquiry made no product, test, contract, status, MEMORY, register or git change. It wrote only REPORT.md, EVIDENCE_MANIFEST.json and STORAGE_SUITE_OBSERVATION.json in this folder. Transient `git status` snapshots and the suite console output were kept in the session scratchpad outside the repository.
- It did not probe guard behaviour beyond the registered suite. U-3 is a code-reading observation and has not been executed.
- It did not search the frozen old PEC tree for ingest behaviour. The REQ-003 scope covered projects/pec outside execution/ for store-module users only.
- It did not review D85 files beyond those listed in the manifest `sources`. The D85 `VERIFICATION/**` files under `D85_EXECUTION_2026-09-08` concern ruling publication and were scanned by keyword only.
- Store-local delete/recreate (VER-002) is not DEL-10-02 kill-test evidence and is not used here. DEL-10-02 remains INITIALIZED with its own open inquiries.
- It does not decide or propose the closure of DEL-01-03-REM-002.
- Revision 1 (verifier cycle 1): row E20 reworded after the independent verifier backcheck to separate the STATE identity check (TG:80-81) from the PATH wrapper-type check (TG:82). Its conclusion and the U-3 and O-2-2 entries are unchanged. The suite was not re-run.
- Revision 2 (verifier cycle 2): E31 and O-2-4 now list all nine unasserted guard failure codes, adding UNKNOWN_FIELD_CLASS (G:206) and INVALID_VALUE (G:224); the count wording is corrected; the suite was not re-run.
