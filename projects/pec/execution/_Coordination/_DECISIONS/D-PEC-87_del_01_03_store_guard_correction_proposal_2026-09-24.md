# D-PEC-87 — DEL-01-03 store/guard correction slice proposal

Status: **PROPOSAL / AWAITING_RULING**. Prepared by a TASK (Type 2) under HELP_HUMAN for the PEC loop, 2026-09-24 (session date). This file is not approved by any earlier direction. It performs no production act, test run, lifecycle change, artifact acceptance or Remaining disposition. HELP_HUMAN owns the `_REGISTER.md` row. This file does not add it.

## Provenance

- **Inquiry authority.** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-86_sca_005_feed_model_rebaseline_2026-09-23.md`, SHA-256 `bf0046cb455e9ac335b620c0ba4d77bdd76f3f5b9dd85465a7258cff749e347f`, row I-4. It authorized the three read-only DEL-01-03 inquiries and reserves owner disposition of their obligations.
- **Inquiry reports.** Paths are under `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/`:
  - `REMAINING_EVIDENCE_DEL-01-03-REM-001/REPORT.md`, SHA-256 `8fcb3ff3c317a2819f0043fdd548f34b5558cb89136fdeaaa33544a19de3c312`
  - `REMAINING_EVIDENCE_DEL-01-03-REM-002/REPORT.md`, SHA-256 `b5d6632df94cd3cb7d3ba57b5ff8b0331e732cf9a0182040c8eefa6850364c60`
  - `REMAINING_EVIDENCE_DEL-01-03-REM-003/REPORT.md`, SHA-256 `ca1b7b3e03ad96e3eaa8aef32751be0945331bfe34f10c32ae54d0bdc69ca930`
- **Triage.** `projects/pec/execution/_Coordination/AgentRuns/HELP-HUMAN-PEC-20260923-SCA005/returns/OBLIGATION_TRIAGE_DEL-01-03.md`, SHA-256 `db335614da29883212ce653cc12b672c68c5d6639200c33280c78c7b466ae6ea`. It classifies the 32 returned obligations as follows:
  - 6 resolved by evidence;
  - 9 resolved by an existing ruling;
  - 13 needing repair, reduced to 8 distinct repairs (R1–R8), plus one registration finding, X-1;
  - 4 owner-only items, folded in below as L-1 and L-2.
- **Product basis.** `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-85_RULING_2026-09-08.md` and its incorporated V2 proposal. The D-PEC-85 P-A nine-path grant is spent at production closeout (`D85_PRODUCTION_CLOSEOUT_2026-09-08/FAN_IN.md:34-38`). F-PEC-1 and `projects/pec/AGENTS.md:122-125` require a new owner-ruled packet for any further write under `v2/**` or to `software-workflow.json`.
- **Source state.** Shared `origin/main` at `bc6d3459be778c7b2b4f8770cb830eb96b18a751`. DEL-01-03 is `IN_PROGRESS`.

## Options

- **C-A: approve the bounded correction slice as specified (recommended).** R1–R8 and X-1 are applied in one PKG-01 / DEL-01-03 slice. The grant covers the seven existing files below, followed by one author and one fresh verifier.
- **C-B: approve R1 only, as an urgent minimal fix.** Only the PATH-domain bound (O-2-2) is applied, touching only `content_minimal_guard.py`, `test_content_minimal_guard.py` and the PATH row of `STORE_LIFECYCLE_AND_GUARD.md`. R2–R8 and X-1 wait for a later packet.
- **Amend.** The owner changes the scope, the character classes or bounds, or the model steer, and the packet is re-prepared.
- **Defer.** Nothing is opened. O-2-2 stays a live content-boundary defect in the merged primitive. No consumer exists yet, so no ingest path currently reaches it.

**Why C-A.**

- It is one packet with one exact grant, and every edit is to an existing file already under D-PEC-85's slice.
- It needs one author/verifier cycle and one registered-check run instead of two. R2–R6 all edit the same two test files, so splitting them would make the second slice re-review R1's bytes.
- None of R2–R8 changes the admissible field classes, the store location or engine, or any consumer contract.

C-B is only worth choosing if the owner wants the content-boundary fix to land before the rest has been reviewed.

## Exact product and configuration grant (C-A)

After this ruling and its register row are merged and observed on fetched `origin/main`, WORKING_ITEMS may start one PKG-01 / DEL-01-03 correction slice. It may MODIFY only these seven existing paths, relative to `projects/pec/`:

1. `v2/src/pec_v2/core/content_minimal_guard.py`
2. `v2/src/pec_v2/core/ports/store.py`
3. `v2/src/pec_v2/adapters/storage/sqlite_store.py`
4. `v2/tests/storage/test_store_lifecycle.py`
5. `v2/tests/storage/test_content_minimal_guard.py`
6. `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`
7. `software-workflow.json`, limited to X-1's one-line `path_rules` change

The grant creates no new source, test, fixture or configuration file. Every fixture is in-test. `v2/src/pec_v2/adapters/storage/__init__.py` is **not** opened. Its existing `from .sqlite_store import SqliteMetadataStore, StoreConfigurationError, StoreDataError` keeps working unchanged once `sqlite_store.py` imports those names from the port (R8).

The grant opens no other source, test, contract, dependency, decomposition, SOW, Root, CI, sister-project, old PEC, registry or scanner path.

Test identity rule: `test_ver_009` requires the `TEST_TO_VERIFICATION` map (`test_store_lifecycle.py:30-44`) to equal the discovered suite. The preferred method is to extend existing tests in place. Any genuinely new test ID must be added to that map in the same change.

### Per-repair specification

| Repair | Closes | Exact behavioural change | Proving test | Files |
|---|---|---|---|---|
| **R1** PATH-domain bound | O-2-2 (the U-3 content channel) | `_repository_path_problem` (`content_minimal_guard.py:288-296`) rejects control and line-break characters, caps a path at 4,096 UTF-8 bytes and each `/`-segment at 255 bytes, and rejects text that cannot be encoded as UTF-8. Spaces and all other printable characters remain admitted. The same validator governs both field PATH values and record `source_path`, so both reject with the existing located codes `INVALID_VALUE` and `SOURCE_CITATION`. | Extend `test_ver_008_policy_is_fixed_finite_and_domain_checked` in place (bad-path loop at CG:148). Add rejections for `"a\nb"`, `"a\rb"`, `"a\tb"`, `"a\x7fb"`, `"a\x85b"`, `"a\u2028b", "a\u2029b"`, `"x/" + "y"*256` and `"y/"*2048 + "y"` (4,097 bytes). Add admissions for `"docs/a b.md"`, a 255-byte segment and a 4,096-byte path. Extend `test_ver_008_forged_wrappers…` (CG:169-209): add a forged `RepositoryPath` with `value="line one\n+line two"`, used both as a PATH field and as a `source_path`. Assert located rejection and empty readback. | 1, 5, 6 |
| **R2** Independent accounting and located rejection | O-2-4, O-3-14 | In `admit_batch` (`sqlite_store.py:45-91`), `rejected` becomes the count of failing guard decisions plus `DUPLICATE_RECORD` rollbacks, instead of `attempted - accepted`. A `RuntimeError` is raised if `attempted != accepted + rejected`. A guard failure whose `record_id` is `<unknown>` is re-located as `<input:{index}>` using `dataclasses.replace`. | Extend `test_ver_005_rejections_are_located…` in place. Assert each of the nine guard codes (`RECORD_TYPE`, `INVALID_IDENTIFIER`, `SOURCE_CITATION`, `EMPTY_RECORD`, `FIELD_TYPE`, `INVALID_FIELD_NAME`, `DUPLICATE_FIELD`, `UNKNOWN_FIELD_CLASS`, `INVALID_VALUE`) with its (record, field) location. Assert `<input:N>` for non-record candidates. Assert `rejected` equals the number of distinct failing inputs. | 3, 5 |
| **R3** Write-surface call graph | O-2-1, O-3-5 | No product change. The documentation adds an inventory of record writes (`_insert_guarded` only, reached from `admit_batch` after the guard) and lifecycle writes (PRAGMA, DDL in `_create_schema`, and unlink in `delete`). | In `test_ver_003_port_isolated…` (SL:144-150), replace the token counts with AST assertions. `_insert_guarded` must have exactly one call site, inside `admit_batch`, lexically after `self._guard.guard`. No `execute`, `executemany` or `executescript` outside `_insert_guarded` may carry `INSERT`, `UPDATE`, `DELETE` or `REPLACE`. DDL is allowed only in `_create_schema`. | 4, 6 |
| **R4** Raw persisted-field dump | O-2-3, O-3-6 | None; test only. | Add an in-file helper to `test_content_minimal_guard.py`, called from the existing VER-004 tests after each rejection batch. It opens a separate raw `sqlite3` connection, enumerates `sqlite_master`, and runs `SELECT *` on every table. It reads the raw bytes of `record_store.sqlite3`, `-wal` and `-shm`, if present. It asserts that no fixture string appears anywhere. The corpus includes R1's valid-wrapper multi-line PATH fixture. | 5 |
| **R5** Shared-corpus uniform ingest | O-2-6, O-3-7 | None; test only. Real-path evidence stays deferred to consumer integration under D-PEC-85's incorporated proposal. | Rewrite `test_ver_006_reconciler_presence_and_event_stand_ins…` in place. One shared corpus (the VER-004 fixtures plus R1's multi-line PATH fixture, covering STATE, PATH and the unknown class) is sent through three stand-in shapes. Assert identical `(field_name, code, constraint)` tuples per fixture across the three shapes, and empty readback. | 5 |
| **R6** External deletion while open | O-1-4, O-3-4 | No product change. A scratch run at `bc6d3459b` showed that external `rmtree` of `.pec-v2/` while a handle is open, followed by `close()` and a new instance, yields a valid empty store. The documentation records that records admitted after an external delete, and before restart, are lost with the deleted store and are restored only by rebuild (PEC-K-02). | Extend `test_ver_002_creation_restart…` in place with `shutil.rmtree(<checkout>/.pec-v2)` while a handle is open, then `close()`, a new `SqliteMetadataStore`, and `read_all() == ()`. | 4, 6 |
| **R7** VER-007 tag | O-1-8 | None. | Change the map entry at SL:41 to `("VER-003", "VER-007")`. `test_ver_009`'s set equality still holds. | 4 |
| **R8** Engine-neutral port errors | O-1-9 | Define `StoreConfigurationError` and `StoreDataError` (both `RuntimeError`) in `core/ports/store.py`, beside `StoreClosedError`. `sqlite_store.py` imports them instead of defining them. It wraps `sqlite3.Error` raised inside port methods (`admit_batch`, `read_all`, `reopen`, `delete`, `reset`) as `StoreDataError`, or `StoreConfigurationError` for open failures, chained with `from`. The public names stay importable from `pec_v2.adapters.storage`, whose `__init__.py` is unchanged. | Extend `test_ver_003…`: assert that both error classes are defined in `pec_v2.core.ports.store`, and that the adapter module's names are the same objects. Add one in-place assertion to `test_ver_002…`: a `read_all` on a deliberately corrupted scratch database raises the port-level `StoreDataError`, not a `sqlite3` exception. | 2, 3, 4, 6 |
| **X-1** Store-check selection | triage finding X-1 | Append `"v2/src/pec_v2/**"` to the existing `v2-store-guard` rule's `paths` array (`software-workflow.json:42`). No other key, command or rule changes. Evidence of the gap at `bc6d3459b`: `select_affected_checks.py projects/pec/software-workflow.json v2/src/pec_v2/core/__init__.py` selects `v2-loop-registry`, `v2-core-posture`, `v2-api-contract` and `harness-self-check`, but not `v2-store-guard`. The store's import chain loads `pec_v2/__init__.py`, `core/__init__.py`, `core/ports/__init__.py`, `core/ports/loop_registry.py` and `adapters/__init__.py`. | After the change, the same selector command also returns `v2-store-guard`. `v2-core-posture`'s registration assertion still returns PASS on the new workflow bytes. | 7 |

### R1 exact rule

The following is added to `content_minimal_guard.py`. It replaces the existing backslash/NUL test and keeps the existing normalization, absolute-path and `..` checks:

```python
_PATH_FORBIDDEN = re.compile(r"[\x00-\x1f\x7f-\x9f\u2028\u2029\\]")
_MAX_PATH_BYTES = 4096
_MAX_SEGMENT_BYTES = 255
```

The forbidden character classes are:

- C0 controls U+0000–U+001F, which include NUL, TAB, LF, VT, FF and CR;
- DEL U+007F;
- C1 controls U+0080–U+009F, which include NEL U+0085;
- LINE SEPARATOR U+2028 and PARAGRAPH SEPARATOR U+2029;
- backslash, which is already excluded at D-PEC-85.

Byte limits are measured on the strict UTF-8 encoding. A lone surrogate fails that encoding and is rejected.

**Evidence that the caps admit the whole repository.** A survey of all 93,447 paths tracked at `bc6d3459b` found:

- 0 paths containing a control character;
- a longest path of 388 bytes and a longest segment of 118 bytes, both well inside 4,096 and 255;
- 3,498 paths containing spaces, which is why spaces remain admitted.

**Why this is not a scope change.**

- It narrows the syntax of the existing PATH class only, the same kind of production choice as D-PEC-85's backslash exclusion.
- It adds, removes or re-decides no field class, so SOW CON-001's scope-change clause is not engaged.
- Rejection stays explicit and located (REQ-005).

**Documented residual.** A single-line, prose-like string with spaces remains syntactically indistinguishable from a filename. Closing that needs a check that the path exists at the cited source SHA. That check belongs to the ingest caller (DEL-03-01 or the PKG-02 scanners), not to the policy-free guard. The PATH row and the Boundary section of `STORE_LIFECYCLE_AND_GUARD.md` state this.

## Finite verification

Run every command from `projects/pec` (cwd `.`, as registered) with an explicit interpreter of Python 3.10 or later, and record the path and version. The last observed interpreter was 3.13.7. Record commands, exit codes and outputs under the run root.

| Check ID (software-workflow.json) | Command | Required for |
|---|---|---|
| `v2-store-guard` | `python3 -m unittest discover -s v2/tests/storage -p test_*.py` | All of R1–R8 and X-1. Record a verbose run listing every test ID with its VER mapping. |
| `v2-core-posture` | `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` | R1, R8 and X-1 (core and workflow bytes change). This check is also in `always_checks`. |
| `v2-loop-registry` | `python3 -m unittest discover -s v2/tests/config -p test_*.py` | Selected by the `v2/src/pec_v2/**` and `software-workflow.json` path rules. |
| `v2-api-contract` | `python3 -m unittest discover -s v2/tests/contracts/api -p test_*.py` | `always_checks`. |
| `harness-self-check` | `python3 tools/practitioner_harness/harness.py self-check` (cwd `../..`) | `always_checks`. |

The manager may run the same five checks through `python3 tools/software_workflow/run_registered_checks.py projects/pec/software-workflow.json --check <ID> --output <run-root>/checks/<ID>.json` from the repository root. For X-1, it should also run `python3 tools/software_workflow/select_affected_checks.py projects/pec/software-workflow.json v2/src/pec_v2/core/__init__.py` before and after the change.

Other required evidence:

- Changed-path containment must show exactly the seven granted paths plus the run root and `MEMORY.md`.
- Whitespace checks.
- A fresh reliance-hold preflight (`dispatch-for-production`, `rely-for-production`) before dispatch and before fan-in.
- An independent verifier who confirms substantive admissibility, not only passing tests.
- The verifier re-reviews the documented PATH row against PRD §7.1/§7.2. This is required because the D85 backcheck (`BC:43-44`) missed the unbounded PATH domain.

## Administrative grant

- **Scope.** WORKING_ITEMS owns PKG-01 / DEL-01-03 only.
- **Writes.** It may write `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_02/**` and that deliverable's `MEMORY.md`.
- **`_STATUS.md`.** The slice does not touch it. DEL-01-03 is already `IN_PROGRESS`, and no transition is needed or granted. Any `_STATUS.md` edit comes only through L-1 or L-2 below.
- **Work graph.** One bounded TASK author using `software-bounded-implementation` owns the seven product and configuration paths. One fresh read-only TASK verifier then applies `software-code-review`. Defects go back to the author; the verifier does not silently repair them.
- **Models.** The model steer follows the owner's current direction (D-PEC-86 I-8): Opus 5.5 (`claude-opus-5-5`) at `high` reasoning for manager, author and verifier, unless the owner states otherwise in this ruling. Role identity is instruction-asserted; serving identity is whatever the host reports.
- **Publication.** CHANGE owns commit, push, PR, merge and `origin/main` observation under the repository's standing Git authorization. Production waits for this ruling and its register row on fetched `origin/main`, then reruns the preimage checks (below) and the hold checks.

## Separately rulable lifecycle clauses

These fold in the triage's four owner-only items. They are independent of C-A and C-B and may be ruled, amended or deferred on their own.

**L-1: the three inquiry Remaining rows (REM-001..003).** This closes O-1-10 (in part), O-2-7 (in part) and O-3-12. The choices are:

- **L-1a (recommended).** Tick all three `_STATUS.md` checkboxes, with one history line citing the three reports and the triage by hash. Each row asked for a read-only inquiry and exact obligations. Each inquiry ran as worded, passed an independent verifier, and has had every obligation dispositioned here or in the triage. Closing the gaps is this packet's job, not the rows'. This grants WORKING_ITEMS that single `_STATUS.md` edit only.
- **L-1b.** Keep the rows open until the C-A slice lands, then tick them.
- **L-1c.** Replace the rows with new Remaining rows mirroring R1–R8 and X-1.

**L-2: acceptance route for the D-PEC-85 store/guard slice.** This closes O-1-10, O-2-7 (in part) and O-3-11. Entry to CHECKING is a human act (`docs/SPEC.md:296,322`). The choices are:

- **L-2a (recommended).** Land this packet first, then run a REVIEW against the corrected bytes, then the owner decides whether to declare a CHECKING basis. O-2-2 is a live content-boundary defect, so freezing the D85 bytes as a CHECKING candidate would freeze a known defect.
- **L-2b.** Declare CHECKING now on the D85 bytes, with R1–R8 recorded as findings. This requires a later reversal to IN_PROGRESS in order to apply them.
- **L-2c.** Accept artifact fitness of the bounded store primitive only, and hold full DEL-01-03 acceptance until the CLM-006 consumers integrate.

## Rollback

- **Before publication.** Discard the slice branch.
- **After merge.** CHANGE reverts the slice PR, restoring the exact preimages below and removing only the `P1_STORE_GUARD_02/**` records and the matching `MEMORY.md` entry. There is no schema migration.
- **Existing stores.** The slice changes no store DDL, so any existing scratch store remains readable. No user's live store is touched.

Preimage SHA-256 at `origin/main` `bc6d3459be778c7b2b4f8770cb830eb96b18a751` (fresh preimage verification must match these before the author starts):

| Path (relative to `projects/pec/`) | SHA-256 |
|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `3d66bb9131eee421c13fcf323bff59a646d5e17d9727e1ea4ef64142b3d54a01` |
| `v2/src/pec_v2/core/ports/store.py` | `2f5cdbf50bb1ed8b02ce8b7d820f81b749da4ca2d62e195afec39c78a035a4af` |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | `03cf799f02def3e9f3d5e20b26ba14607461b5ce5189eb1b0d9a643f2cdc10a8` |
| `v2/tests/storage/test_store_lifecycle.py` | `ed99fbc5a46587e364eed4cfb0521cf6fd4bce920e332714ec851f15ca6c4bef` |
| `v2/tests/storage/test_content_minimal_guard.py` | `2c4bfc3682710402a9374366dd3f89fb75508b21546e12ce458d75bc4cc46127` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `d1d69dcbf29a694ea62ada6b6502ffc379221415eb9a260b54fe095648cd1e48` |
| `software-workflow.json` | `247eb82715356e1e3f532c577ff0c9babf39c18912b14362bdfb4fc8412f5d3a` |

The unopened `v2/src/pec_v2/adapters/storage/__init__.py` must remain at `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540`. If any preimage differs at start, stop and route the exact discrepancy.

## Limits

This proposal, and any ruling selecting C-A or C-B, grants none of the following:

- `CHECKING`, `ISSUED`, artifact acceptance, full DEL-01-03 acceptance or full P1 completion. The only exceptions are what L-1 or L-2 separately rule.
- Runtime, consumer or daemon integration.
- A kill-test or parity conclusion. DEL-10-02 owns the kill test, and store-local evidence is never kill-test evidence.
- A hosted-CI or Root change. X-2, the absence of v2 Python checks in `.github/workflows/pec-tests.yml` and `tools/hosted-ci-routing.json`, stays a Root/CI concern needing its own scope.
- A change to the SOW, to the admissible field classes, to CON-001 or held REM-004, or to the store location or engine.
- Reopening or rewriting D-PEC-85's accepted evidence. The D85 run records, reviews and closeout stay immutable, and the new evidence is additive under `P1_STORE_GUARD_02/**`.

Existing reliance-hold, dependency, lifecycle and release boundaries survive unchanged.
