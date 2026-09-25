# AUTHOR_RETURN_01 - P1_STORE_GUARD_03 (D-PEC-89 A), author cycle 1 (N2)

Role: TASK (Type 2) author, instruction-asserted. Dispatched by the
WORKING_ITEMS manager of this run (HELP_HUMAN run
`HELP-HUMAN-PEC-20260923-SCA005`, node C3). No delegation. Date: 2026-09-24/25
(session date; the host clock rolled over during the run). The host reports
the serving model as Opus 5.5 (`claude-opus-5-5`). The `high` reasoning effort
is instruction-asserted. I ran no state-changing git command; the only git
commands were `rev-parse`, `status`, `archive`, `diff` and `--version`.

Interpreter for every run:
`/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, Python
3.13.7 (CPython, SQLite library 3.50.4), with `PYTHONDONTWRITEBYTECODE=1`.
Checkout: `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a18afc5a210fbbfb7`,
branch `claude/pec-d89-exact-type-slice`, HEAD
`9ffc54afcaa287d1b5fdc57dcda2194f6f1e0abf`.

## Basis read

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-89_del_01_03_exact_type_closure_proposal_2026-09-24.md` | `962a7879788e75cac41bc73c8320eb2be11b65fe104fcbb163fff892b49f8a73` (matches the required value) |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-89_RULING_2026-09-24.md` (option A, R13 included) | `536b058873a011a4ef3df60f243fc55ecd389c2900132bfa30592ba414d263e3` |
| `workflows/software-bounded-implementation/WORKFLOW.md` (`chirality-root:bundled:workflow:software-bounded-implementation`) | `2ea0ddf4f53241fa94274e709b8042ad9de4d8beb9c82cd1ed1dcd0c6f8f0f7b` |
| `_run_records/P1_STORE_GUARD_02/VERIFIER_VERDICT_01.md` | `5871da78be6fd0c96320de2d1b9c8665347db217d42e589b85bc65d0e3349023` |
| `_run_records/P1_STORE_GUARD_02/VERIFIER_VERDICT_02.md` | `3208e75a5679a8eede155f8e71d41a70f08d1381414a3eaad63af86c2f79ba7a` |
| `_run_records/P1_STORE_GUARD_02/VERIFIER_VERDICT_03.md` | `30233584519ebb436337c583f092c8bda88c7b5c38de9445f8bd1285a8d89ffb` |
| `_run_records/P1_STORE_GUARD_02/AUTHOR_RETURN_02.md` | `a0c031df3edd41a2401575362d02dfbd1fbf2f9435704f47feb6454525485e7b` |
| `_run_records/P1_STORE_GUARD_03/RUN.md` (manager's; read, not written) | `6e64efd739da52c7ec562640d7ab3bb388bc05775a9a2726e83e3f7014db3c4f` |

The four P1_STORE_GUARD_02 hashes equal the proposal's provenance table. I
also read, but did not write, `v2/src/pec_v2/core/ports/store.py` and
`v2/src/pec_v2/adapters/storage/__init__.py` for context. I did not look for
or use HELP_HUMAN's scratch scripts or prototype files.

**Preimage verification at start.** All eight rollback-table paths matched
the proposal at HEAD `9ffc54afc`, both in the checkout and in the scratch
extraction (`git archive 9ffc54afc projects/pec/v2 projects/pec/software-workflow.json`
to `.../scratchpad/author/base/`): guard `d63932c2...6b33`, adapter
`05b9846a...ae0a`, guard tests `c8e23563...1c29`, lifecycle tests
`edbd41df...cadf`, doc `e9d65fc7...ed35`, `store.py` `d7544f71...05eb`,
`__init__.py` `c9d8b3e5...0880540`, `software-workflow.json` `8ec9ba6d...058a8b`.

## Per-repair status (postimage line locators, relative to `projects/pec/`)

| Repair | Status | Change (file:line) | Proving tests |
|---|---|---|---|
| R9 exact-type rule | DONE | `v2/src/pec_v2/core/content_minimal_guard.py`: `_is_identifier` added at `:286-287`; record ID `:144-145`; fields container `:161` (`type(candidate_fields) is not tuple or not candidate_fields`) and `:168` (`type(candidate_fields) is tuple`); field name `:175-176`; `_valid_hex` exact at `:291`; path check `:295-296` (`type(value) is not str or not value`, message "path must be a non-empty exact str"). No `isinstance(<x>, str/int/tuple)` call remains; the only `isinstance` left is `isinstance(guarded, AdmissionFailure)` at `:183`. No copying or coercion; no new failure code. | `test_ver_008_policy_is_fixed_finite_and_domain_checked`, `test_ver_008_forged_wrappers_are_revalidated_and_rejected_without_crashing` |
| R10 content-minimal failures | DONE | Same file: `:144` record ID becomes `<unknown>` unless `_is_identifier` (the adapter relocates it to `<input:N>`); `:175-176` an invalid field name is reported at `fallback` (`<field:N>`); the `field_name` echo variable is removed. | `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution`, forged-wrapper test (E-3 inputs 12 and 13 of the R9 batch) |
| R11 `close()` port error | DONE | `v2/src/pec_v2/adapters/storage/sqlite_store.py:141-147`: `sqlite3.Error` from `Connection.close()` re-raised as `StoreDataError("metadata store could not be closed")` with `from`; `_connection = None` only after a successful close. `delete()` `:174-175` now calls `self.close()` unwrapped, so the old "could not be closed for deletion" wrapper is gone. | `test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation` |
| R12 `reopen()` mkdir | DONE | `sqlite_store.py:153-156`: `OSError` from `mkdir(parents=True, exist_ok=True)` re-raised as `StoreConfigurationError("metadata store directory could not be created")` with `from`; the store stays closed (construction goes through `reopen()`). | `test_ver_002_...` |
| R13 `delete()` unlink | DONE | `sqlite_store.py:176-182`: `FileNotFoundError` is still ignored; any other `OSError` is re-raised as `StoreDataError("metadata store files could not be deleted")` with `from`, at the first failure. | `test_ver_002_...` |
| R14 doc | DONE (two interpretations, see "Discrepancies") | `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`: edit 1 `:41-47`; edit 2 `:59-64`; edit 3 `:89-90`; edit 4 `:94` (PATH domain and decision cell), `:95` (COUNT), `:96` (SHA), `:98` (HASH); edit 5 `:105-108`; edit 6 (deleted sentence after `:113`); edit 7 `:134` (REQ-002), `:136` (REQ-004), `:137` (REQ-005), `:140` (REQ-009); edit 8 `:152-186` (four paragraphs). The "Prose-like single-line paths" paragraph (now `:188-201`) and the closing kill-test paragraph are byte-unchanged. | Verifier review (per the proposal). My mechanical check: every quoted R14 sentence and all four blockquoted paragraphs are present verbatim after whitespace normalization, and all six replaced texts are absent (scratch `check_r14.py`, exit 0, 24 quoted strings and 4 paragraphs). |

### Test changes (in place; no new test ID; `TEST_TO_VERIFICATION` unchanged; 13 tests)

- `v2/tests/storage/test_content_minimal_guard.py`:
  - `import ast` at `:3`.
  - Module-level test helpers `SUBCLASS_PAYLOAD` (`"SECRET FILE BODY\n+diff line two"`), `SubclassPayload`, `MethodLiar`, `LengthLiar`, `LyingTuple`, `ClassSpoof` and `ConformingInt` at `:53-117`.
  - `test_ver_005`: the two tuples at `:261` and `:265` (see next section). No other expectation changed.
  - `test_ver_008_policy...`:
    - `ConformingInt(3)` added to `invalid_values` (`:369`).
    - `ValueError` asserted for `RepositoryPath(SubclassPayload(...))`, `RepositoryPath(MethodLiar("../../etc/passwd"))`, `ShaDigest(SHA1, SubclassPayload("b"*40))` and `ContentHash(..., SubclassPayload("c"*64))` (`:441-448`).
    - Syntax-tree assertion that `content_minimal_guard.py` has no `isinstance` call whose type argument names `str`, `int` or `tuple` (`:450-466`).
  - `test_ver_008_forged_wrappers...`: a second `admit_batch` of 14 inputs (`:546-639`) asserts the following:
    - `(14, 0, 14)` and the exact ordered `(record_id, field_name, code)` list;
    - each failure attribute is an exact `str` (`constraint` may be `None`) whose value, f-string and `repr` contain neither payload line;
    - `read_all() == ()`;
    - `assert_no_persisted_residue` for the payload, its two lines, `etc/passwd` and the 400-character digest.
- `v2/tests/storage/test_store_lifecycle.py`: `import threading` at `:11`. `test_ver_002` gains three blocks after the corrupted-database block (`:171-212`):
  - **R11:** close from a second `threading.Thread`, giving exactly one `port_module.StoreDataError` with a `sqlite3.Error` cause. Then `read_all() == ()`, which shows the handle was kept. The owning thread closes, and `read_all()` then raises `StoreClosedError`.
  - **R12:** `.pec-v2` is replaced by a regular file. Construction raises exactly `port_module.StoreConfigurationError` with an `OSError` cause, and the file is removed.
  - **R13:** `record_store.sqlite3-journal` is made a directory. `delete()` raises exactly `port_module.StoreDataError` with an `OSError` cause. The directory is removed, and after `reset()`, `read_all() == ()`.

### The two `test_ver_005` expected tuples (R10)

| Preimage line | Before | After (postimage line) |
|---|---|---|
| `:194` | `("bad id!", "<record_id>", "INVALID_IDENTIFIER")` | `("<input:2>", "<record_id>", "INVALID_IDENTIFIER")` (`:261`) |
| `:198` | `("field-name", "bad name", "INVALID_FIELD_NAME")` | `("field-name", "<field:0>", "INVALID_FIELD_NAME")` (`:265`) |

`rejected == len({record_id})` still holds (13), and `<unknown>` is still
absent.

## Commands (all with the interpreter above and `PYTHONDONTWRITEBYTECODE=1`)

| # | Command (cwd) | Exit | Result |
|---|---|---|---|
| 1 | `git -C <root> archive -o <scratch>/base.tar 9ffc54afc projects/pec/v2 projects/pec/software-workflow.json`; `tar -x` into `<scratch>/base` | 0 | Preimage copy; hashes equal the rollback table |
| 2 | `python3 probes/probe_d89.py <scratch>/base/projects/pec/v2` (run root) before any edit, saved to `probes/probe_BEFORE_preimage.out` | 0 | **28 / 33 open**, which equals the proposal's Base count |
| 3 | `python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v` (`projects/pec`), final bytes | 0 | `Ran 13 tests`, 13 `ok`, `OK`; the same 13 IDs as `TEST_TO_VERIFICATION` |
| 4 | `python3 probes/probe_d89.py <root>/projects/pec/v2`, saved to `probes/probe_AFTER_postimage.out` | 0 | **1 / 33 open: C2-4** (outside the threat boundary, as expected) |
| 5 | `python3 probes/mutate_d89.py <root>/projects/pec/v2`, saved to `probes/mutate_AFTER.out` | 0 | Baseline 13 ok; M1-M9 all caught by the named tests; `RESULT PASS` |
| 6 | `python3 <scratch>/check_r14.py <root>` | 0 | R14 verbatim check PASS |
| 7 | `python3 <scratch>/extra_mutation.py <root>/projects/pec/v2` (supplementary: `_connection` cleared before `close()`) | 0 (script); suite exit 1 | `test_ver_002` errors, so the handle-kept assertion catches it |
| 8 | `git -C <root> diff --check` | 0 | no output |
| 9 | `LC_ALL=C grep -c '[^ -~]'` on the 4 changed `.py` files and both probe scripts | - | 0 non-ASCII lines in each. Doc: the non-ASCII characters on added lines are only the pre-existing `§` (6) and en dash (2) carried by rewritten table rows, the same counts as on the removed lines. |
| 10 | `find <root>/projects/pec -name __pycache__` | 0 | none, so there was nothing to delete |

Every probe case and mutation ran in a `tempfile` directory (system temp),
never inside the checkout. The storage suite itself also uses `tempfile`
checkouts.

## Probe results (`probes/probe_d89.py`, 33 cases)

Classification: OPEN means a record was admitted, a needle was persisted, a
non-port exception escaped, a returned failure carried a non-exact `str` or
caller text, or a `DUPLICATE_RECORD` code was misreported. CLOSED means a
constructor `ValueError`, or a located rejection with clean failures and no
residue, or (E-2) a port error chained to the engine or OS error.

| Case | BEFORE (preimage) | AFTER (postimage) |
|---|---|---|
| E1-01 PATH field, public `RepositoryPath(Sneaky)` | OPEN: accepted, payload persisted | CLOSED: constructor `ValueError` |
| E1-02 `source_path`, public | OPEN: accepted, persisted | CLOSED: constructor `ValueError` |
| E1-03 PATH field, forged shell | OPEN: accepted, persisted | CLOSED: `locator` `INVALID_VALUE` |
| E1-04 `source_path`, forged shell | OPEN: accepted, persisted | CLOSED: `<source_path>` `SOURCE_CITATION` |
| E1-05 record ID `Sneaky` | OPEN: accepted, persisted | CLOSED: `<input:0>` `INVALID_IDENTIFIER` |
| E1-06 field name `Sneaky` | OPEN: accepted, persisted | CLOSED: `<field:0>` `INVALID_FIELD_NAME` |
| E1-07 source SHA, public | OPEN: accepted, persisted | CLOSED: constructor `ValueError` |
| E1-08 source SHA, forged | OPEN: accepted, persisted | CLOSED: `<source_sha>` `SOURCE_CITATION` |
| E1-09 SHA field, public | OPEN: accepted, persisted | CLOSED: constructor `ValueError` |
| E1-10 SHA field, forged | OPEN: accepted, persisted | CLOSED: `commit` `INVALID_VALUE` |
| E1-11 HASH field, public | OPEN: accepted, persisted | CLOSED: constructor `ValueError` |
| E1-12 HASH field, forged | OPEN: accepted, persisted | CLOSED: `snapshot` `INVALID_VALUE` |
| C2-2a public `Liar("../../etc/passwd")` | OPEN: accepted, `etc/passwd` persisted | CLOSED: constructor `ValueError` |
| C2-2b public `Liar("/etc/passwd")` | OPEN: accepted, persisted | CLOSED: constructor `ValueError` |
| C2-2c forged `Liar("a/../../etc/passwd")` | OPEN: accepted, persisted | CLOSED: `SOURCE_CITATION` + `INVALID_VALUE` |
| LEN-1 `HexLen` SHA1 digest | OPEN: accepted | CLOSED: `commit` `INVALID_VALUE` |
| CNT-1 `bool` count | CLOSED: `INVALID_VALUE` | CLOSED: `INVALID_VALUE` |
| CNT-2 `int` subclass with `__conform__` | CLOSED | CLOSED |
| ST-1 forged `KnownState` | CLOSED | CLOSED |
| ST-2 `Sneaky("IN_PROGRESS")` | CLOSED | CLOSED |
| FC-1 `Sneaky("path")` field class | CLOSED: `UNKNOWN_FIELD_CLASS` | CLOSED: `UNKNOWN_FIELD_CLASS` |
| TUP-1 lying tuple | OPEN: accepted with zero fields | CLOSED: `<record>` `EMPTY_RECORD` |
| DUP-1 never-equal field names | OPEN: misreported `DUPLICATE_RECORD` | CLOSED: `<field:0>`, `<field:1>` `INVALID_FIELD_NAME` |
| SPF-1 `__class__` spoof record ID | OPEN: `TypeError` escapes `admit_batch` | CLOSED: `<input:0>` `INVALID_IDENTIFIER` |
| E3-1 exact-`str` payload record ID | OPEN: echoed | CLOSED: `<input:0>` |
| E3-2 exact-`str` payload field name | OPEN: echoed | CLOSED: `<field:0>` |
| E3-3 invalid `Sneaky` record ID | OPEN: `Sneaky` object returned | CLOSED: `<input:0>` |
| E3-4 invalid `Sneaky` field name | OPEN: `Sneaky` object returned | CLOSED: `<field:0>` |
| C2-4 `sqlite3.register_adapter(str)` | OPEN: payload persisted | **OPEN** (outside the threat boundary by design) |
| E2-1 `close()` from a non-owning thread | OPEN: raw `sqlite3.ProgrammingError` | CLOSED: `StoreDataError`, cause `ProgrammingError`; handle kept; the owner closes; then `StoreClosedError` |
| E2-2 `.pec-v2` is a regular file | OPEN: raw `FileExistsError` | CLOSED: `StoreConfigurationError`, cause `FileExistsError` |
| E2-3 `reopen()` in a read-only checkout | OPEN: raw `PermissionError` | CLOSED: `StoreConfigurationError`, cause `PermissionError`; store closed |
| E2-4 sidecar name is a directory | OPEN: raw `PermissionError` | CLOSED: `StoreDataError`, cause `PermissionError`; `reset()` recovers `()` |
| **Total open** | **28 / 33** (proposal Base: 28 / 33) | **1 / 33 (C2-4)** (proposal Proto: 1 / 33) |

All seven required reproductions (E1-01, E1-05, E1-09, C2-2a, TUP-1, SPF-1,
E3-1) are OPEN on the preimage.

## Mutation results (`probes/mutate_d89.py`; each on a fresh temporary copy of the postimage `v2`)

| Mutation | Failing tests (suite exit 1 each) | Required by proposal | Verdict |
|---|---|---|---|
| Baseline (no mutation) | none (13 ok) | - | - |
| M1 `isinstance` in `_is_identifier` | `test_ver_008_forged_wrappers...`, `test_ver_008_policy...` | both VER-008 | caught |
| M2 `isinstance` in `_valid_hex` | both VER-008 | both VER-008 | caught |
| M3 `isinstance` in the path check | both VER-008 | both VER-008 | caught |
| M4 `isinstance` in the container check (both sites, i.e. the preimage form) | both VER-008 | both VER-008 | caught |
| M5 record-ID echo restored (A2 form: `... if type(candidate_record_id) is str else "<unknown>"`) | `test_ver_005...`, `test_ver_008_forged_wrappers...` | `test_ver_005` and forged-wrapper | caught |
| M6 field-name echo restored (A2 form: `candidate_name if type(candidate_name) is str else fallback`) | `test_ver_005...`, `test_ver_008_forged_wrappers...` | same | caught |
| M7 R11 removed | `test_ver_002...` | `test_ver_002` | caught |
| M8 R12 removed | `test_ver_002...` | `test_ver_002` | caught |
| M9 R13 removed | `test_ver_002...` | `test_ver_002` | caught |
| M4a (supplementary) first container site only | both VER-008 | - | - |
| M4b (supplementary) loop container site only | `test_ver_008_policy...` only (the syntax-tree check). It is behaviourally invisible because the first site already rejects. | - | - |

No test needed strengthening to catch M1-M9.

## Postimage SHA-256 (relative to `projects/pec/`)

| Path | SHA-256 |
|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `2cb21e2d251eeffd164d68ad436cb0b9f0d4b8fdabd41358f33a0d7ed40122b3` |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | `edb15e2b96eb3b5cdf918c05cf58fce128063b02475233649e30bcc92864ad5c` |
| `v2/tests/storage/test_content_minimal_guard.py` | `3a4c98b32b1e4e07f921d7b567120377c63b7e526e0322480216346828ae8cba` |
| `v2/tests/storage/test_store_lifecycle.py` | `96d9917d6283eeb8fd6310991cd0166ecd24bcf76afccae840afee508ec2fb64` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `1fc417fc6b5461bd0623780e751bf37354df491f3f28e713b98c7d29417130a3` |

The guard and adapter postimages hash exactly to the proposal's "Prototype
postimage" values. I observed this only after writing them from the
specification, and I never read the prototype files. The two test files
differ from the prototype hashes, as expected since the tests are my own
bytes.

**Unopened paths are unchanged:**

| Path | SHA-256 |
|---|---|
| `v2/src/pec_v2/core/ports/store.py` | `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb` |
| `v2/src/pec_v2/adapters/storage/__init__.py` | `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540` |
| `software-workflow.json` | `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b` |

**Containment.** `git diff --name-only` lists exactly the five granted
paths. The untracked files are only under `P1_STORE_GUARD_03/`: the
manager's `RUN.md` and `PREIMAGE.md` (not written by me), plus my `probes/*`
and this file. `RUN.md`, `PREIMAGE.md`, `checks/**`, `MEMORY.md`,
`_STATUS.md` and `_DECISIONS/**` were not written.

Run-root artifacts:

| File | SHA-256 |
|---|---|
| `probes/probe_d89.py` | `5dc3ac77782d414a15f98f065e20b50a7116d100987136aea718a68be9a6ecd5` |
| `probes/probe_BEFORE_preimage.out` | `62ba2cd4c6d751bd725c3190f15fa8d7edf4986a21ba6514dec8b272fc9318e6` |
| `probes/probe_AFTER_postimage.out` | `c51299614d5d96c1e1d61b7733546fd9299fdad958e37a8db26a58b1d4edbc05` |
| `probes/mutate_d89.py` | `98595ce1f895d13ba2875c803d94af0ed7c4eb0698e681ce606f1a17fcdf726a` |
| `probes/mutate_AFTER.out` | `33ce93f5f4a21dfb405c20454d5543875d0ebe2f45c2f78c4b12ec8f0082fb1d` |

## Discrepancies, interpretations and notes (routed, not worked around)

1. **R14 edit 4, SHA and HASH ("after 'lowercase hex', insert 'as an exact
   `str`'").**
   - The SHA cell contains "lowercase hex" twice. I inserted the phrase once,
     at the end of the cell: "`sha1`/40 lowercase hex or `sha256`/64
     lowercase hex as an exact `str`".
   - In the HASH cell, a literal insertion would split "lowercase hex
     characters". I inserted it after "characters": "exactly 64 lowercase hex
     characters as an exact `str`".
   - The verifier should confirm this reading, or the manager should route it.
2. **R14 edit 7, list connectors.** Each quoted item was inserted verbatim as
   a list item in its row.
   - REQ-002: the item was appended as the last list element. That meant
     dropping the pre-existing "and" before "a deliberately corrupted scratch
     database". No other words changed.
   - REQ-004, REQ-005 and REQ-009: each item was inserted before the final
     "and ..." element.
3. **R14 edit 5, rewrap.** The unchanged trailing sentence "A state rejection
   names its record and field and carries `constraint="CON-001"`. The
   implementation does not infer state tokens from source prose." was
   rewrapped (`:108-110`). The words are unchanged; only the wrapping moved.
4. **R11 test, one extra in-spec assertion.**
   - `threaded.read_all() == ()` runs after the failed cross-thread close and
     before the owner's close. It proves R11's "handle kept" statement.
   - Without it, a variant that clears `_connection` before closing would
     pass the specified assertions while leaking the handle (command 7
     above).
   - Beyond this assertion, the in-place tests follow the per-repair table
     exactly.
5. **R9 batch uses forged shells for the five subclass wrapper inputs.** These
   are source path, source SHA, PATH, SHA and HASH. The public constructors now
   reject subclasses, which the policy test asserts, so only a forged shell
   reaches the guard-level check. The record-ID and field-name subclass inputs
   need no shell.
6. **Syntax-tree check scope.** The check flags an `isinstance` call made by
   name or by attribute (for example `builtins.isinstance`), and also a call
   with fewer than two arguments, whenever its type argument names `str`,
   `int` or `tuple` anywhere, including inside a tuple of types. This is the
   same rule as the specification, stated so that it cannot be bypassed by
   spelling.
7. **Mutation spellings.**
   - M4 restores both container sites (the preimage form).
   - M5 and M6 use the A2 wording from the proposal, so they restore only the
     echo and not `isinstance`. This avoids a trivial catch by the
     syntax-tree check.
   - M4a and M4b are supplementary and labelled as such.
8. **Unchanged guard comment.** The comment at
   `content_minimal_guard.py:299` ("Unbound str methods: a forged str
   subclass cannot override the measurement.") is unchanged. It is still
   true, and now redundant. Changing it is outside the specification.
9. **Checks I did not run.** I ran no other registered check (`v2-core-posture`,
   `v2-loop-registry`, `v2-api-contract`, `harness-self-check`), no
   reliance-hold preflight and no `MEMORY.md` write. The run graph assigns
   these to the manager (N3/N5/N6), and the brief did not assign them to me.
10. **Platform note for E2-4 and the R13 test.** On macOS, unlinking a
    directory raises `PermissionError` (EPERM); Linux raises
    `IsADirectoryError`. The test asserts only an `OSError` cause, so it is
    portable.

Nothing here claims review, acceptance, CHECKING, merge or any lifecycle
change.
