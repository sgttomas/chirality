# AUTHOR_RETURN_01 — P1_STORE_GUARD_02 (D-PEC-87 C-A), node N2

Role: TASK (Type 2) author, instruction-asserted. Dispatched by WORKING_ITEMS
run `P1_STORE_GUARD_02` (parent HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`,
node C2). No delegation was performed. Date: 2026-09-24 (session date).
Host: Claude Code agent in isolated worktree
`.claude/worktrees/agent-ad38112cce87e78c1`, HEAD `6b4a0f59d`. The host reports
the serving model as Opus 5.5, model ID `claude-opus-5-5`. The brief steered
`high` reasoning; this record cannot verify the effort level independently.

Method: bundled `workflows/software-bounded-implementation/WORKFLOW.md` (the
brief-cited `.agents/skills/software-bounded-implementation/SKILL.md` does not
exist; see RUN.md). Specification: `D-PEC-87_del_01_03_store_guard_correction_proposal_2026-09-24.md`
SHA-256 `ba3d3e64eab7c0488b7973a10e360479d9f34bb075113f821266aea4a4684569`
(re-hashed at start, match), selected by `D-PEC-87_RULING_2026-09-24.md`
SHA-256 `7da38e54508b913efba445e1968d5c86383ea6235719fb1dc908fd91717f66fe` (C-A,
no enlargement).

Interpreter: `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`,
`Python 3.13.7`.

## Preimage check at start

All seven granted paths and the unopened `adapters/storage/__init__.py` hashed
to the proposal preimages before any edit (same values as `PREIMAGE.md`).

## Per-repair status

Paths are relative to `projects/pec/`; line numbers are in the postimage.

| Repair | Status | Change locators | Proving tests |
|---|---|---|---|
| R1 PATH-domain bound | DONE | `v2/src/pec_v2/core/content_minimal_guard.py:13-15` (the three constants, byte-exact with the proposal's R1 rule); `:294-305` (the backslash/NUL test is replaced by `_PATH_FORBIDDEN`, strict UTF-8 encode, and the 4,096/255-byte caps; the normalization, absolute and `..` checks at `:306-309` are unchanged). The same `_repository_path_problem` still serves `RepositoryPath.__post_init__`, field PATH (`INVALID_VALUE`) and `source_path` (`SOURCE_CITATION`). Doc: PATH row `v2/docs/STORE_LIFECYCLE_AND_GUARD.md:83`; Boundary residual `:138-144`. | `test_ver_008_policy_is_fixed_finite_and_domain_checked` (`test_content_minimal_guard.py:308-363`): every listed rejection plus NUL, a lone surrogate and a 256-byte multibyte segment; each is asserted both as a `RepositoryPath` constructor `ValueError` and as a guard decision on a forged wrapper, with exactly `{("bad-path","<source_path>","SOURCE_CITATION"), ("bad-path","locator","INVALID_VALUE")}`. Admissions: `docs/a b.md`, a 255-byte segment, a 4,096-byte path and a 255-byte multibyte segment, each accepted as both source path and field. `test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing` (`:369-446`): forged `RepositoryPath("line one\n+line two")` as a PATH field (`:391`) and as `source_path` (`:411-415`), with a located rejection by code (`:431-442`), empty `read_all()`, and the R4 raw dump (`:443-445`). |
| R2 Independent accounting and located rejection | DONE | `v2/src/pec_v2/adapters/storage/sqlite_store.py:49-50` (independent counters); `:57-63` (guard-failure count; `<unknown>` is relocated to `<input:{index}>` with `dataclasses.replace`); `:73` (`DUPLICATE_RECORD` count); `:86-94` (`rejected = guard_rejected + duplicate_rejected` at `:88`; `RuntimeError` on mismatch, raised inside the transaction before commit so the batch rolls back). Doc `:44-56`. | `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution` (`test_content_minimal_guard.py:152-232`): a 14-input batch asserts the exact ordered `(record_id, field_name, code)` list covering all nine guard codes, `<input:1>` and `<input:10>` for non-record inputs, `<input:13>` for a non-string record ID, an in-batch `DUPLICATE_RECORD`, `rejected == 13 ==` the number of distinct failing inputs (and `!=` the 14 failures), and readback preservation. |
| R3 Write-surface call graph | DONE (test and documentation only; no product change) | `v2/tests/storage/test_store_lifecycle.py:181-253` replaces the token counts with AST assertions. Doc inventory: `STORE_LIFECYCLE_AND_GUARD.md:57-70`. | `test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface`: `_insert_guarded` is defined once, referenced exactly once (no bare-name or string reference), and called only in `admit_batch`, lexically after the single `self._guard.guard` call. Every `execute`, `executemany` and `executescript` statement must be statically inspectable. DML (`INSERT`/`UPDATE`/`DELETE`/`REPLACE`, with `ON DELETE`/`ON UPDATE` FK clauses excluded) occurs only in `_insert_guarded` (exactly two statements), and DDL only in `_create_schema`. |
| R4 Raw persisted-field dump | DONE (test only) | In-file helper `assert_no_persisted_residue` at `v2/tests/storage/test_content_minimal_guard.py:91-116`: a separate read-only raw `sqlite3` connection enumerates `sqlite_master` (asserting both tables exist), runs `SELECT *` on every table, and scans the raw bytes of `record_store.sqlite3` and any `-journal`, `-wal` or `-shm` file. | Called after the rejection batch in `test_ver_004_content_diff_prose_unknown_classes_and_misleading_keys_are_rejected_atomically` (`:150`) and in the VER-004/008 forged-wrapper test (`:443`). R5 also calls it (`:283`). The corpus includes the R1 multi-line PATH fixture. |
| R5 Shared-corpus uniform ingest | DONE (test only) | Module-level `rejection_corpus()` at `test_content_minimal_guard.py:52-70` (the VER-004 fixtures plus `multiline-path`, covering STATE, PATH and an unknown class), which the VER-004 rejection test also uses (`:145`). | `test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary` rewritten in place (`:234-285`). Three stand-in shapes, each with a distinct record-ID prefix, source path and SHA presence, admit the same corpus. The test asserts the per-fixture `(field_name, code, constraint)` tuples equal one explicit expected map for all three shapes, empty readback, and the R4 raw dump. |
| R6 External deletion while open | DONE (no product change) | `v2/tests/storage/test_store_lifecycle.py:142-150`; doc `STORE_LIFECYCLE_AND_GUARD.md:26-31`. | `test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation`: after one admission, `shutil.rmtree(<checkout>/.pec-v2)` with the handle open, then `close()`, a new `SqliteMetadataStore`, and `read_all() == ()`. |
| R7 VER-007 tag | DONE | `v2/tests/storage/test_store_lifecycle.py:47` → `("VER-003", "VER-007")`. | `test_ver_009_loaded_suite_has_exact_execution_mapping` passes (the map equals the discovered suite; VER-001..009 covered). |
| R8 Engine-neutral port errors | DONE | `v2/src/pec_v2/core/ports/store.py:24-29` (both classes are `RuntimeError` subclasses beside `StoreClosedError`). `sqlite_store.py:19-24` imports them; the local definitions are removed. Wrapping, chained with `from`: `admit_batch` at `:98-99` (`StoreDataError`); `read_all` at `:109-114` (body moved unchanged into the private static `_read_all` at `:116-139`); `reopen` at `:146-166` (wraps at `:153` and `:160`) (`StoreConfigurationError` for connect/PRAGMA/DDL failures); `delete` at `:168-172` (wrap at `:171`) (`StoreDataError`). `reset` inherits both. `adapters/storage/__init__.py` is not opened and its re-export still resolves. Doc `STORE_LIFECYCLE_AND_GUARD.md:33-42`. | `test_ver_003…` (`test_store_lifecycle.py:256-264`): both classes are defined in `pec_v2.core.ports.store`, subclass `RuntimeError`, are identical objects in `pec_v2.adapters.storage.sqlite_store` and `pec_v2.adapters.storage`, and no `ClassDef` of those names exists in the adapter. `test_ver_002…` (`:152-168`): every page after page 1 of a closed scratch database is overwritten; `read_all()` raises exactly the port `StoreDataError`, which is not a `sqlite3.Error` and has a `sqlite3.Error` `__cause__`; then `reset()` returns an empty store. |
| X-1 Store-check selection | DONE | `software-workflow.json:42`: `"v2/src/pec_v2/**"` appended as the last element of the `v2-store-guard` rule's `paths`. No other byte changed (`git diff` shows one line). | The selector AFTER returns `v2-store-guard` with reason `v2/src/pec_v2/core/__init__.py` (below). `v2-core-posture` registration assertion: PASS. |

No new test IDs were created. Every change extends an existing test in place,
so `TEST_TO_VERIFICATION` changed only at R7's entry.

## Verification (commands, exit codes)

From `projects/pec`:

| Check | Command | Exit | Result |
|---|---|---|---|
| v2-store-guard | `python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v` | 0 | `Ran 13 tests … OK` |
| v2-core-posture | `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` | 0 | `verdict: PASS`; dependency, locality and registration PASS; findings `[]`; `workflow_sha256 8ec9ba6d…8a8b`, `core_tree_sha256 ac1c02fe…914b`, `config_sha256 20d64ff3…09ed` |
| v2-loop-registry | `python3 -m unittest discover -s v2/tests/config -p 'test_*.py'` | 0 | `Ran 12 tests … OK` |
| v2-api-contract | `python3 -m unittest discover -s v2/tests/contracts/api -p 'test_*.py'` | 0 | `Ran 6 tests … OK` |

From the repository root:

| Check | Command | Exit | Result |
|---|---|---|---|
| harness-self-check | `python3 tools/practitioner_harness/harness.py self-check` | 0 | Summary INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124. No finding names any of the seven changed paths or this run root (grep of the full output). No pre-change baseline was run, so the counts are not compared. |
| X-1 selector AFTER | `python3 tools/software_workflow/select_affected_checks.py projects/pec/software-workflow.json v2/src/pec_v2/core/__init__.py` | 0 | checks `harness-self-check`, `v2-api-contract`, `v2-core-posture`, `v2-loop-registry`, `v2-store-guard`; reasons now include `v2-store-guard: [v2/src/pec_v2/core/__init__.py]` (BEFORE, per `checks/X-1_select_affected_checks_BEFORE.out`: no `v2-store-guard`) |
| whitespace | `git diff --check` | 0 | no output |
| containment | `git diff --name-only` | 0 | exactly the seven granted paths (below) |

Verbose storage-suite test IDs, each with its `TEST_TO_VERIFICATION` mapping (all `ok`):

| Test ID | VER mapping |
|---|---|
| `test_content_minimal_guard.ContentMinimalGuardTests.test_ver_004_admission_and_readback_preserve_all_five_typed_classes` | VER-004, VER-005 |
| `test_content_minimal_guard.ContentMinimalGuardTests.test_ver_004_content_diff_prose_unknown_classes_and_misleading_keys_are_rejected_atomically` | VER-004 |
| `test_content_minimal_guard.ContentMinimalGuardTests.test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution` | VER-005 |
| `test_content_minimal_guard.ContentMinimalGuardTests.test_ver_006_reconciler_presence_and_event_stand_ins_share_the_same_boundary` | VER-006 |
| `test_content_minimal_guard.ContentMinimalGuardTests.test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing` | VER-004, VER-008 |
| `test_content_minimal_guard.ContentMinimalGuardTests.test_ver_008_policy_is_fixed_finite_and_domain_checked` | VER-008 |
| `test_store_lifecycle.StoreLifecycleTests.test_ver_001_database_journal_and_temp_artifacts_are_ignored` | VER-001 |
| `test_store_lifecycle.StoreLifecycleTests.test_ver_001_force_tracked_store_artifact_fails_before_any_write` | VER-001 |
| `test_store_lifecycle.StoreLifecycleTests.test_ver_001_later_negation_of_the_rule_fails_before_store_creation` | VER-001 |
| `test_store_lifecycle.StoreLifecycleTests.test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation` | VER-002 |
| `test_store_lifecycle.StoreLifecycleTests.test_ver_003_port_isolated_and_adapter_has_one_guarded_record_write_surface` | VER-003, VER-007 |
| `test_store_lifecycle.StoreLifecycleTests.test_ver_007_runtime_imports_are_stdlib_or_pec_and_make_no_network_call` | VER-007 |
| `test_store_lifecycle.StoreLifecycleTests.test_ver_009_loaded_suite_has_exact_execution_mapping` | VER-009 |

### Supplementary evidence (scratch only; not registered checks)

- **Mutation pass.** The script and all copies lived in the session
  scratchpad or `tempfile` directories, never in the checkout. `v2/src` and
  `v2/tests/storage` were copied, one mutation was applied per copy, and the
  storage suite was run. Every mutation was caught (exit 1):
  - M1, old backslash/NUL-only PATH test: VER-004 rejection, VER-006, and both
    VER-008 tests fail.
  - M1b, byte caps disabled: `test_ver_008_policy…` fails.
  - M1c, segment cap measured in characters: `test_ver_008_policy…` fails.
  - M2, `<input:N>` relocation disabled: `test_ver_005…` fails.
  - M2b, duplicates omitted from `rejected`: `test_ver_005…` fails through the
    accounting `RuntimeError`.
  - M3, an extra `DELETE` in `read_all`: `test_ver_003…` fails, and so do
    `test_ver_002` and `test_ver_005`.
  - M3b, a second `_insert_guarded` call site: `test_ver_003…` fails.
  - M4, `read_all` wrapping removed: `test_ver_002…` fails.
  - M5, `StoreDataError` redefined in the adapter: `test_ver_002…` and
    `test_ver_003…` fail.
- **R6 and R8 behavior probe on the preimage bytes**, run in a tempfile
  checkout before editing. After an external `rmtree` with the handle open, a
  further admission returned `accepted=1` and was readable on the open
  handle. After `close()` and a new instance, `read_all()` was `()`. This
  matches the proposal's scratch evidence and the doc note. Overwriting the
  pages after page 1 left the store openable, and `read_all()` raised raw
  `sqlite3.DatabaseError: database disk image is malformed`, which the R8
  wrapping now converts.

## Postimage SHA-256

| Path (relative to `projects/pec/`) | Postimage SHA-256 |
|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `d63932c28dd346581deb0b04bb14841f00eff9481432a379ce67dd8e9d626b33` |
| `v2/src/pec_v2/core/ports/store.py` | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | `05b9846a2baa9a5fe2691196d83d35770b8227f8b653f39c3831dcd4b89eae0a` |
| `v2/tests/storage/test_store_lifecycle.py` | `edbd41df5e05573d9992ee9778aba053570b4de6d4a0bf392ff7a888ff42cadf` |
| `v2/tests/storage/test_content_minimal_guard.py` | `1a6cbcef7c7ff379de8914e966bd18934c81687da28c36dcca0dedf627d85ce3` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `5f8100cc2886840087fac61df458f38a43b3cb8e50eaa01798308bafb9b43094` |
| `software-workflow.json` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` |
| `v2/src/pec_v2/adapters/storage/__init__.py` (unopened; unchanged) | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` |

## Containment

`git diff --name-only` lists exactly the seven granted paths. The only
untracked path is the run root `P1_STORE_GUARD_02/`, which holds WORKING_ITEMS's
`PREIMAGE.md`, `RUN.md` and `checks/`, plus this file. Running the registered
checks created gitignored interpreter bytecode (`__pycache__/`) under `v2/src`
and `v2/tests`. It is not tracked or staged, and it was left in place for the
manager's disposition. No scratch store was created in the checkout: every
store lived under `tempfile` directories. No file or diff content is captured
in any artifact. The residue helper reads store bytes only to assert that
fixture strings are absent.

## Ambiguities, interpretations and routed items

1. **R1 regex transcription.** The brief's rendering of `_PATH_FORBIDDEN`
   shows two literal space-like characters where the proposal has
   `  `. I implemented the proposal's text byte-exactly, with escape
   sequences inside the raw string. Spaces remain admitted, as the rule
   requires.
2. **X-1 "append" vs "replace".** The triage (§Additional findings) suggested
   *replacing* the four exact store source paths with the glob. The governing
   proposal says *append* with no other change, so I appended. The four exact
   paths are now redundant under `v2/src/pec_v2/**`. That is harmless, but any
   cleanup would need its own scope.
3. **R2 raise point.** The proposal does not say when the `RuntimeError` is
   raised. I raise it inside the transaction before `commit()`, so a mismatch
   rolls the batch back instead of persisting writes behind an exception.
4. **R8 `close()`.** The enumerated wrap list (`admit_batch`, `read_all`,
   `reopen`, `delete`, `reset`) omits `close()`. I followed the list:
   - `delete()` wraps its internal close.
   - A direct `close()` can still surface a raw `sqlite3.Error`, for example
     `ProgrammingError` on a cross-thread close.
   - `reopen()`'s `mkdir` can still raise `OSError`, which is not a
     `sqlite3.Error` and so is not wrapped.

   Routing: if engine neutrality should cover `close()`, that needs a scope
   decision.
5. **Pre-existing hardening gap, reported but not fixed (outside R1's exact
   rule).** A forged `RepositoryPath` whose `value` is a `str` *subclass* can
   override `startswith`, `__ne__`, `split` or the methods that
   `posixpath.normpath` uses, and so evade the pre-existing normalization,
   absolute-path and `..` checks. The new R1 checks resist this: the regex runs
   on the string buffer, and the encode and split calls use unbound
   `str.encode`/`str.split`. So such a value is still single-line,
   control-free and byte-bounded. It is not a content channel. The residual is
   limited to normalization semantics. Routing: a one-line `type(value) is str`
   test in `_repository_path_problem` would close it, but it narrows the
   domain beyond the ruled rule and so needs a manager or owner decision.
6. **Returned (not persisted) echoes.** `INVALID_IDENTIFIER` and
   `INVALID_FIELD_NAME` failures echo the caller-supplied invalid record ID or
   field name in the returned `AdmissionResult`. This is pre-existing and never
   persisted. R2 relocates only `<unknown>`. This is noted for the verifier's
   PEC-K-10 reading. I made no change.
7. **Additions beyond the enumerated fixtures, all within the named tests in
   place.**
   - R1 adds NUL, a lone surrogate, and multibyte segment cases (256 bytes
     rejected, 255 admitted) to prove "strict UTF-8, byte-measured". The
     bad-path loop also asserts the guard codes on forged wrappers.
   - R3 additionally requires statically inspectable SQL arguments and forbids
     any bare-name or string reference to `_insert_guarded`.
   - R4's helper is also called from R5.
   - R6 does not assert the post-deletion admission itself, which depends on
     VFS and platform. The doc's loss statement rests on the proposal's and
     this run's scratch probe.
8. **`read_all` restructure.** To wrap `read_all` without re-indenting its
   body, the body moved unchanged into a private static `_read_all`. It
   carries only `SELECT` statements, and R3's AST assertions cover it.

Nothing in this return claims review, acceptance, CHECKING, merge, or any
lifecycle change. Git state is untouched: no commit, stage, stash or checkout.
