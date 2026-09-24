# DEL-01-03 obligation triage (O-1-1..O-1-10, O-2-1..O-2-8, O-3-1..O-3-14)

| Field | Value |
|---|---|
| Role | TASK (Type 2) under HELP_HUMAN, PEC loop; no delegation; instruction-asserted, not enforced |
| Serving model | `claude-opus-5-5[1m]`, as reported by the host; not independently verified |
| HEAD | `bc6d3459be778c7b2b4f8770cb830eb96b18a751` |
| Date | 2026-09-23 |
| Nature | A derivative triage of the three DEL-01-03 inquiry reports against accepted sources. It is not a ruling, acceptance, lifecycle act, production act or Remaining disposition. |

**Classes.**

- **A**: the repository already answers the obligation.
- **B**: an accepted decision, SOW clause, ADR or contract already settles it.
- **C**: a real defect or gap in the merged D-PEC-85 slice. Each one has a repair and a route.
- **D**: only the owner can settle it, because it needs a product choice, acceptance, lifecycle act or cross-loop request that no accepted source decides.

**Executions in this triage (all read-only).**

1. The O-2-2 reproduction command, as specified. Both calls returned `None`, which means both values were admitted.
2. One scratch script under the session scratchpad, outside the repository and using `tempfile` checkouts. It covered external deletion while a store handle is open, and multi-line text inside `RepositoryPath` passing the guard.
3. `git check-ignore -v --no-index` over five hypothetical `projects/pec/.pec-v2/` names.
4. The registered `v2-core-posture` command at HEAD.

`git status --short --ignored projects/pec` was identical before and after. It shows one pre-existing untracked file, `execution/_ScopeChange/SCA-005_2026-09-23_2139/Checkpoint1_Resolution_Note.md`, which belongs to another agent; this triage treats it as external state and did not touch it. None of these runs is a measurement, a VER discharge or an acceptance.

## 1. Triage table

Abbreviations:

- `SOW` = `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/ScopeOfWork.md`
- `R85` = `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-85_RULING_2026-09-08.md`
- `PROP` = `projects/pec/execution/_Coordination/P1_PRODUCTION_PREP_2026-09-07/CORRECTIONS/V2/PROPOSAL.md` (selected and incorporated by R85:8-12 and :38-42)
- `ADR` = `projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/artifacts/v2/ADRs.md` (ADR-PEC-V2-001, D-PEC-72 O-B)
- `S105` = `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/ScopeOfWork.md`
- `G` = `projects/pec/v2/src/pec_v2/core/content_minimal_guard.py`
- `A` = `projects/pec/v2/src/pec_v2/adapters/storage/sqlite_store.py`
- `PT` = `projects/pec/v2/src/pec_v2/core/ports/store.py`
- `SL` = `projects/pec/v2/tests/storage/test_store_lifecycle.py`
- `CG` = `projects/pec/v2/tests/storage/test_content_minimal_guard.py`
- `DOC` = `projects/pec/v2/docs/STORE_LIFECYCLE_AND_GUARD.md`
- `SWJ` = `projects/pec/software-workflow.json`
- `BC` = `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_01/children/VERIFY_BACKCHECK_02/REVIEW.md`

| Obligation | Class | Resolution or repair | Evidence path:line | Quote |
|---|---|---|---|---|
| O-1-1 | B | Placing the lifecycle adapter outside `core/` is the ruled hexagonal split: the core port is in `core/ports`, and SQLite lifecycle is in `adapters/storage`. R85 granted those exact paths. DEL-01-05's accepted contract scopes posture enforcement to `core/**` and excludes persistence adapters. REQ-007 is still evidenced for the adapter by `test_ver_007` (SL:152-169, stdlib-only import roots). Nothing further is owed. | `ADR:73-75`; `S105:72`; `R85:28-36` | "Store connection, schema migration, query dialect, transaction handling, and physical persistence are adapter concerns behind a core-owned persistence port." |
| O-1-2 | B | Hosting-checkout identity is ruled. The store is `projects/pec/.pec-v2/record_store.sqlite3`, the checkout root is `projects/pec`, and the rule is `projects/pec/.gitignore:17`. A non-mutating `check-ignore -v --no-index` at HEAD resolved every probed name to that line. R85 incorporated the proposal's verification, which deliberately keeps the store out of the live project during tests. | `R85:38-41`; `PROP:37`; `projects/pec/.gitignore:17` | R85: "Python standard-library SQLite and `projects/pec/.pec-v2/record_store.sqlite3` choices, finite verification ... are incorporated without enlargement." PROP: "No database is created in the live project during tests." |
| O-1-3 | A | `/.pec-v2/` is a directory rule, so it ignores every file beneath the directory whatever its name. At HEAD, `-journal`, `.lock`, `some-engine-index.idx` and a nested `sub/dir/tmp-123` all resolved to `.gitignore:17` (exit 0), and `git ls-files -- projects/pec/.pec-v2` returned 0 paths. | `projects/pec/.gitignore:17`; `DOC:6-8` | "the checked-in `/.pec-v2/` rule covers that database and its journal, WAL, shared memory, lock, index, and temporary neighbors." |
| O-1-4 | C | **Test gap.** The "running" case only calls the store's own `delete()`, which closes the handle first. The scratch run showed that `shutil.rmtree(<root>/.pec-v2)` while a handle is open, followed by `close()` and a new instance, gives an empty valid store. So the repair is test-only: extend `test_ver_002` in place with external deletion while open. A process-level PEC runtime case cannot exist yet, because R85 grants no runtime integration. **Doc note:** records admitted after an external delete but before the restart are lost with the deleted store and come back only through rebuild. The scratch run shows `accepted=1`, then empty after the restart. | `A:139-145`; `SL:112-134`; `R85:60-62` | "`delete()` first closes the handle" (DOC:21); R85: "grants no ... runtime integration" |
| O-1-5 | B | The kill test is ruled out of scope and assigned to DEL-10-02. DEL-10-02's own contract forbids it from defining store lifecycle, so DEL-01-03 owes nothing. | `SOW:69`; `projects/pec/execution/PKG-10_Validation_Measurement/1_Working/DEL-10-02_Kill_test_standing_release_gate/ScopeOfWork.md:319` | "This contract binds only the store-local property that makes that outside test possible; it neither runs nor discharges the kill test." |
| O-1-6 | B | The enforcing deliverable's accepted contract defines "runtime dependency" as an import reachable under the core target. A `git` subprocess in an adapter is neither. The ADR names Git as an adapter concern, and PEC-PRS-002 requires Git observation anyway. | `S105:71`; `ADR:48-49` | "a runtime dependency is an import reachable from a production Python module under the operative core target." |
| O-1-7 | A | The DEL-01-05 enforcement is registered and runs on every change through `always_checks`. At HEAD, `v2-core-posture` returned PASS for dependency, locality and registration, and `core_tree_sha256` `efebbdd8…` equals the D85 value. Its scope is `core/**` by contract. Acceptance of DEL-01-05's repaired bytes is DEL-01-05's own pending owner review (D-PEC-84) and does not block the DEL-01-03 re-run. | `SWJ:27`; `projects/pec/v2/config/service_core_posture.json:3` | `"always_checks": ["v2-api-contract", "v2-core-posture", "harness-self-check"]` |
| O-1-8 | C | **Map mislabel.** The signature-leakage inspection that VER-007 requires runs in `test_ver_003` but is mapped only to VER-003. Repair: change the SL:41 tuple to `("VER-003", "VER-007")`. The `test_ver_009` set equality is unaffected. DOC:87 already claims the link. | `SL:41`; `DOC:87` | `...test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface": ("VER-003",),` |
| O-1-9 | C | Adapter-class construction is composition and needs no change (ADR:65-66). **Real gap:** the port declares only `StoreClosedError`. Its methods `reopen`, `reset` and `read_all` raise adapter-defined `StoreConfigurationError` and `StoreDataError`, and `admit_batch` re-raises raw `sqlite3` errors. A consumer would have to import from `adapters.storage`, so swapping the engine (TBD-002) would change consumers. Repair: declare engine-neutral `StoreConfigurationError` and `StoreDataError` in PT. Have A import them and wrap `sqlite3.Error` from port methods (chained). Keep the re-export in `adapters/storage/__init__.py`. Assert in `test_ver_003` that raised types live in PT. The consumer counterfactual stays unexercised until the CLM-006 consumers integrate. | `PT:20-21`; `A:27-32,79-81`; `ADR:65-66` | PT: "class StoreClosedError(RuntimeError):" is the only port error. A:79-81: `except BaseException: connection.rollback() raise` |
| O-1-10 | D | Artifact acceptance, lifecycle promotion and disposition of the REM-001 row are reserved acts. See §4. | `projects/pec/execution/_Coordination/D85_PRODUCTION_CLOSEOUT_2026-09-08/FINAL_VALIDATION.json:39-41`; `docs/SPEC.md:296` | `"artifact_fitness_accepted": false, "checking_or_issued": false` |
| O-2-1 | C | **Test gap.** Structural privacy is not needed: Python convention plus a real call-graph assertion is proportionate. Repair: replace the SL:147-150 token counts with AST assertions. First, `_insert_guarded` is referenced exactly once, inside `admit_batch`, after `self._guard.guard`. Second, no `execute`, `executemany` or `executescript` outside `_insert_guarded` carries INSERT, UPDATE, DELETE or REPLACE; DDL is allowed only in `_create_schema`. Also add a record-write versus lifecycle-write inventory to DOC §Core interface. | `SL:144-150`; `A:63,249-267` | "`self.assertNotIn(\"INSERT \", source.split(\"def _insert_guarded\", 1)[0])`" is a token check, not a call graph |
| O-2-2 | C | **Content-boundary defect, reproduced.** `p('a\nb')` and `p('x/'+'y'*5000)` both return `None`. The scratch run also admitted a `RepositoryPath` carrying a multi-line file body and a diff header with hunk. Repair is in §3.1. | `G:288-296`; `projects/pec/docs/PRD.md:184` | PEC-K-10: "Paths, counts, SHAs, states, hashes — never file or diff content." |
| O-2-3 | C | **Test gap.** Residue is checked only through `read_all()`. Repair: add a helper to CG. After each rejection batch, it opens the database with a raw `sqlite3` connection, enumerates `sqlite_master`, and runs `SELECT *` on every table. It also reads the raw bytes of `record_store.sqlite3`, `-wal` and `-shm`. It asserts that no fixture byte string appears. Apply it to the VER-004 corpus, including a valid-wrapper multi-line `RepositoryPath` fixture that now fails under §3.1. | `CG:90-92` | `self.assertEqual(self.store.read_all(), ())` |
| O-2-4 | C | **Accounting and test gap.** First, extend `test_ver_005` in place to assert the nine guard codes, each located as (record, field). Second, in `admit_batch`, replace a `<unknown>` record id with `<input:{index}>` using `dataclasses.replace`, so RECORD_TYPE rejections are located. Third, compute `rejected` independently as failing decisions plus duplicates. Raise if `attempted != accepted + rejected`. | `A:83-91`; `G:133-145` | `rejected=attempted - accepted,` |
| O-2-5 | B | PEC-ORI-006 is a response-level duty owned by DEL-04-05 through SOW-009. Feed ingest belongs to DEL-03-01 and PKG-02 (CLM-008). The guard's share is already implemented: explicit, located, CON-001-labelled rejection. | `projects/pec/execution/_Decomposition/ScopeLedger.csv:10`; `projects/pec/docs/PRD.md:262` | "SOW-009,IN,State measurement limitations explicitly where a feed is unparseable or stale; prohibit silent omission,PEC-ORI-006,PKG-04,DEL-04-05" |
| O-2-6 | C | Real-path evidence is ruled deferred to consumer integration (PROP:43,49). **Test defect:** VER-006 requires "the same fixture corpus", but the three stand-ins use different STATE strings only. Repair: rewrite `test_ver_006` to send one shared corpus through three stand-in shapes. The corpus is the VER-004 fixtures plus the §3.1 multi-line PATH fixture, so it covers STATE, PATH and the unknown class. Assert identical `(field_name, code, constraint)` tuples per fixture. | `CG:111-125`; `SOW:114` | "Exercise reconciler-shaped, presence-shaped, and event-shaped ingest with the same fixture corpus and assert identical rejection behavior" |
| O-2-7 | D | Owner acceptance and REM-002 disposition. See §4. | `R85:60-62`; `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md:61` | "This ruling grants no `CHECKING`, `ISSUED`, artifact acceptance, full DEL-01-03 acceptance" |
| O-2-8 | B | The dependency is already recorded in the contract and implemented fail-closed: non-KnownState STATE values are rejected with `constraint="CON-001"` (G:217-224; DOC:48,56-58). Its resolution is ruled to be SCOPE_CHANGE or owner ruling, not production. REM-004 is HELD by the D83 disposition. | `SOW:97` | "A resolution that changes what the store may hold is a scope change, routed through SCOPE_CHANGE or an owner ruling, not a production choice." |
| O-3-1 | B | R85 incorporated the registration mode: a path-selected `v2-store-guard` with `always_checks` unchanged. The registered profile check is the ruled "service-core test run". Hosted CI runs none of the v2 Python checks, including `v2-core-posture`. That is repository-wide, outside R85's paths and a Root CI scope (note X-2). A separate low-severity path-rule gap is X-1. | `PROP:47`; `SWJ:14-17,41-44` | "Existing always checks remain `v2-api-contract`, `v2-core-posture`, `harness-self-check`" |
| O-3-2 | B | Each candidate assertion traces to a ruled source rather than defining a new criterion. `DUPLICATE_RECORD` → REQ-005 "silent substitution … prohibited" (SOW:79). The six `KnownState` values → Root SPEC §3.2 lifecycle states (`docs/SPEC.md:273`). The `CON-001` label → SOW:94,97. The digest and path formats → PEC-K-10 plus the TBD-002 production choices. The six-method surface → PROP:23 and REQ-002. R85 incorporates all of these. | `R85:38-41`; `SOW:71` | "These are chosen during production within the bounds of REQ-001, REQ-007, and REQ-008." |
| O-3-3 | B | Same as O-1-2. | `R85:38-41`; `PROP:37,49` | "checked-in ignore rule covers every scratch store artifact" |
| O-3-4 | C | Same repair as O-1-4 (one test extension). | `SL:112-134` | see O-1-4 |
| O-3-5 | C | Same repair as O-2-1. | `SL:144-150` | see O-2-1 |
| O-3-6 | C | Same repair as O-2-3. | `CG:90-92` | see O-2-3 |
| O-3-7 | C | Same repair as O-2-6. | `CG:111-125` | see O-2-6 |
| O-3-8 | A | There is no manifest because the accepted posture is Python stdlib only, so the bounded absence is itself the evidence. The adapter is excluded from posture scope by contract (O-1-1). The re-run passes at HEAD (O-1-7). `test_ver_007` checks import roots for all three files. | `S105:70`; `SL:152-169` | "the operative implementation posture is Python 3 plus the standard library." |
| O-3-9 | A | VER-008's declared method is a review, and the review record exists. `test_ver_008` is the mapped executing test. That review missed the PATH gap in O-2-2, so the §3.1 packet's verifier must re-review the PATH row. | `BC:43-44,63-65` | "PATH, COUNT, SHA, STATE, and HASH have closed runtime domains documented against PRD sections 7.1 and 7.2." |
| O-3-10 | A | The distinction is already stated in the product document and in every report. Nothing presents store-local evidence as kill-test evidence. | `DOC:100-101`; `SOW:110` | "Store-local deletion and recreation do not run or satisfy DEL-10-02's system kill test." |
| O-3-11 | D | Artifact fitness acceptance of the suite. See §4. | `projects/pec/execution/_Coordination/D85_PRODUCTION_CLOSEOUT_2026-09-08/FAN_IN.md:34-38` | "Artifact fitness acceptance, CHECKING, ISSUED, full DEL-01-03/P1 completion ... remain unopened." |
| O-3-12 | D | Disposition of the REM-003 row is reserved to the owner. See §4. | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md:61` | "`_STATUS.md` and the Remaining checkboxes are not edited; the return proposes their disposition." |
| O-3-13 | A | D-PEC-86 is now tracked. It was committed in `9c7ae80d0` and merged to `origin/main` by PR #882 (`bc6d3459b`), so the obligation is overtaken by publication. | `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md:61` | `git branch -r --contains 9c7ae80d0` → `origin/main` |
| O-3-14 | C | Same repair as O-2-4. | `A:88`; `CG:95-109` | see O-2-4 |

## 2. Summary count by class

| Class | Count | Obligations |
|---|---|---|
| A: resolved by evidence | 6 | O-1-3, O-1-7, O-3-8, O-3-9, O-3-10, O-3-13 |
| B: resolved by an existing ruling | 9 | O-1-1, O-1-2, O-1-5, O-1-6, O-2-5, O-2-8, O-3-1, O-3-2, O-3-3 |
| C: repair required | 13 (8 distinct repairs) | O-1-4, O-1-8, O-1-9, O-2-1, O-2-2, O-2-3, O-2-4, O-2-6, O-3-4, O-3-5, O-3-6, O-3-7, O-3-14 |
| D: owner decision required | 4 | O-1-10, O-2-7, O-3-11, O-3-12 |
| Total | 32 | |

## 3. Class-C repairs by file, and packet route

**Route for all of them.** D-PEC-85 P-A's nine-path grant is spent and closed (FAN_IN.md:34-38). `v2/**` is behind F-PEC-1, and `projects/pec/AGENTS.md:122-125` requires "an owner-ruled `D-PEC` packet naming the exact paths, acts, verification, and rollback". None of the repairs can be made documentation-only outside such a packet, because DOC is itself under `v2/**`.

The smallest route is **one successor D-PEC production packet**, a "D-PEC-85 follow-on correction slice" using the next free D-PEC number. Nothing is allocated here. The packet should:

- Name MODIFY acts only on existing files: G, PT, A, `v2/src/pec_v2/adapters/storage/__init__.py` (only for R8), SL, CG and DOC. Add `software-workflow.json` only if X-1 is taken.
- Set the administrative scope to `_run_records/P1_STORE_GUARD_02/**`, MEMORY and truthful `_STATUS.md` residuals. The state stays IN_PROGRESS.
- Keep the D85 pattern: one bounded TASK author (`software-bounded-implementation`), then a fresh read-only verifier (`software-code-review`).
- Run the selected checks for verification: `v2-store-guard`, `v2-core-posture`, `v2-loop-registry`, `v2-api-contract` and `harness-self-check`.
- Roll back by restoring the exact preimages.

Every new test ID must be added to `TEST_TO_VERIFICATION` (SL:30-44), because `test_ver_009` enforces set equality. Extending existing tests in place avoids that.

### 3.1 R1: PATH domain bound (O-2-2), the only production-code defect in the content boundary

**File G.** Replace the check at G:291-292. Add the following module constants and body checks, and keep the existing normalization check at G:293-295:

```python
_PATH_FORBIDDEN = re.compile(r"[\x00-\x1f\x7f-\x9f  \\]")
_MAX_PATH_BYTES = 4096      # PATH_MAX
_MAX_SEGMENT_BYTES = 255    # NAME_MAX
# inside _repository_path_problem, after the non-empty check:
if _PATH_FORBIDDEN.search(value):
    return "path must be single-line normalized POSIX text without control characters"
try:
    encoded = value.encode("utf-8")          # rejects lone surrogates
except UnicodeEncodeError:
    return "path must be valid UTF-8 text"
if len(encoded) > _MAX_PATH_BYTES or any(len(s.encode("utf-8")) > _MAX_SEGMENT_BYTES for s in value.split("/")):
    return "path exceeds the finite path bound"
```

**Why this is consistent.**

- It narrows only the PATH domain, not the set of classes. DOC:45 already excludes one legal Git path character (backslash), so this is the same kind of production choice and not a CON-001 or scope change.
- A multi-line file body or a diff hunk (a header plus lines) can no longer ride inside the PATH class. That is the purpose of PEC-K-10.
- Rejection stays explicit and located: INVALID_VALUE or SOURCE_CITATION, satisfying REQ-005.
- Across all 93,447 tracked paths at HEAD there are 0 control characters, a maximum of 388 bytes and a maximum segment of 118 bytes, so no real repository path is rejected.
- Spaces stay admitted, because 3,498 tracked paths contain them.

**Files CG and SL (tests).** Extend `test_ver_008_policy_is_fixed_finite_and_domain_checked` in place:

- In the bad-path loop (CG:148), add `"a\nb"`, `"a\rb"`, `"a\tb"`, `"a\x7fb"`, `"a b"`, `"x/" + "y"*256` and `"y/"*2049`.
- Add positive admissions for `"docs/a b.md"`, a 255-byte segment and a 4,096-byte total.
- In `test_ver_008_forged_wrappers…` (CG:169), add a forged `RepositoryPath` whose `value` is `"line one\n+line two"`, as both a field and a `source_path`. Assert located rejection and empty readback.

No map change is needed.

**File DOC (row 45).** Restate the PATH domain as: single-line, no C0 or C1 controls, DEL or U+2028/2029, at most 4,096 UTF-8 bytes, and at most 255 per segment.

**Documented residual.** A single-line, prose-like string with spaces cannot be told apart from a filename by syntax. The full closure is to check that the path exists at the cited source SHA. That belongs to the ingest caller (DEL-03-01 or the PKG-02 scanners), not to the policy-free guard, and DOC §Boundary should say so.

### 3.2 R2: accounting and located rejection (O-2-4, O-3-14)

- **File A:83-91.** Compute `rejected` from failing decisions plus duplicates, and raise if `attempted != accepted + rejected`. Replace a `<unknown>` record id with `<input:{index}>` using `dataclasses.replace`.
- **File CG.** Extend `test_ver_005` in place to assert all nine guard codes and the `<input:N>` location.

### 3.3 R3: write-surface call graph (O-2-1, O-3-5)

- **File SL:144-150.** Replace the token checks with AST assertions. `_insert_guarded` must have exactly one reference, inside `admit_batch`, and no DML may appear outside `_insert_guarded`.
- **File DOC §Core interface.** Add the inventory of record writes (`_insert_guarded`) and lifecycle writes (PRAGMA, DDL and unlink).

### 3.4 R4: raw persisted-field dump (O-2-3, O-3-6)

- **File CG.** Add a raw `sqlite_master` and all-table dump, plus a byte scan of the database, `-wal` and `-shm` files, after each VER-004 rejection batch. This can be a helper called from the existing tests, so no new ID is needed.

### 3.5 R5: shared-corpus uniform ingest (O-2-6, O-3-7)

- **File CG:111-125.** Send one shared corpus through three stand-in shapes and assert identical `(field, code, constraint)` tuples.

### 3.6 R6: external deletion while open (O-1-4, O-3-4)

- **File SL:112-134.** Extend `test_ver_002` with `shutil.rmtree(<root>/.pec-v2)` while the handle is open, then `close()`, a new instance, and `read_all() == ()`. The scratch run confirms this passes with no code change.
- **File DOC:19-24.** Add a note that writes made after an external delete are lost with the deleted store and come back only through rebuild.

### 3.7 R7: VER-007 map tag (O-1-8)

- **File SL:41.** Change the tuple to `("VER-003", "VER-007")`.

### 3.8 R8: engine-neutral port errors (O-1-9)

- **File PT.** Add `StoreConfigurationError` and `StoreDataError`.
- **File A.** Import them, and wrap `sqlite3.Error` raised from port methods.
- **File `adapters/storage/__init__.py`.** Keep the re-export.
- **File SL.** Add an assertion in `test_ver_003`.
- **File DOC.** Add one sentence.

### Additional findings (not among the 32; for the owner's packet choice)

- **X-1 (optional, low severity, `SWJ:42`).** Importing the store package also loads `pec_v2/__init__.py`, `core/__init__.py`, `core/ports/__init__.py`, `core/ports/loop_registry.py` and `adapters/__init__.py`. I confirmed this by listing `sys.modules`. The `v2-store-guard` path rule does not select on those files. Import breakage is partly caught by `v2-loop-registry` (SWJ:34-35). The smallest repair is to replace the four exact store source paths in SWJ:42 with `v2/src/pec_v2/**`. It belongs in the same packet.
- **X-2 (outside PEC).** Hosted CI (`.github/workflows/pec-tests.yml:80-82`, `tools/hosted-ci-routing.json`) runs only the frozen-corpus `npm test`. It runs no v2 Python check. This is a Root CI scope that needs its own authorized scope, and it is not a D-PEC-85 defect.

## 4. Class-D items and the exact owner choice

The four D items reduce to two owner choices.

**Choice 1: disposition of the three inquiry Remaining rows (O-1-10 in part, O-2-7 in part, O-3-12).** D-PEC-86 I-4 reserves this choice to the owner. The options are:

- **(a)** Treat REM-001..003 as discharged, because each inquiry ran exactly as worded and returned a verified report. Authorize WORKING_ITEMS to tick the three `_STATUS.md` checkboxes, with a history note citing the reports and this triage.
- **(b)** Keep them unchecked until the §3 correction packet lands.
- **(c)** Supersede them with the §3 packet's own Remaining rows.

The rows ask for inquiry, not for closure of the gaps. Option (a) is therefore consistent with their wording.

**Choice 2: artifact and lifecycle acceptance of the D-PEC-85 store/guard slice and its suite (O-1-10, O-2-7, O-3-11).** No accepted source decides this. Entry to CHECKING is a human act (`docs/SPEC.md:296,322`), and R85:60-62 withholds it. The options are:

- **(a)** Keep the slice IN_PROGRESS, approve the §3 correction packet first, then run REVIEW and decide on a CHECKING basis for the corrected bytes. This is the recommended option, because O-2-2 is a live content-boundary defect.
- **(b)** Declare CHECKING on the current D85 bytes, with §3 as recorded findings.
- **(c)** Accept artifact fitness of the bounded primitive only, and hold full DEL-01-03 acceptance until the CLM-006 consumers integrate.

In every option, approving the §3 packet is itself an owner ruling under `projects/pec/AGENTS.md:122-125`. Its contents are fully specified above and need no further product choice.
