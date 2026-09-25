<!--
Saved by WORKING_ITEMS. Source: the final report of the verifier child
(agent id a5eefcc3795adc090, subagent_type pec-reviewer, model opus), returned
directly to this manager by the host's foreground Agent call (not relayed by
HELP_HUMAN). Text reproduced verbatim; only the host's hand-back indentation
is removed.
-->

# VERIFIER_VERDICT_01: P1_STORE_GUARD_03 (D-PEC-89 A)

**Verdict: PASS.** There are no blocking findings. The six non-blocking notes below need no author repair. Two are small tasks for the manager (N-5, N-6).

The candidate implements R9–R14 as specified, with nothing added and nothing left out. My own probes show every routed residual open on the preimage and closed on the candidate. The one case still open is C2-4, which is the stated threat boundary. All nine reversals the proposal lists are caught by the tests it names.

- **Role:** TASK (Type 2) verifier, read-only. Dispatched by WORKING_ITEMS under HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node C3, slice `P1_STORE_GUARD_03`. No delegation, no repairs, no file edits in the checkout, no state-changing git.
- **Model:** the host reports Opus 5.5 (`claude-opus-5-5`). The role and the `high` reasoning effort are set by instruction; the host does not report them.
- **Method:** `.agents/skills/software-code-review/SKILL.md`.
- **Date:** 2026-09-25 (session date).

## Candidate

- **Checkout:** `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a18afc5a210fbbfb7`, branch `claude/pec-d89-exact-type-slice`.
- **Base:** HEAD and `origin/main` are both `9ffc54afcaa287d1b5fdc57dcda2194f6f1e0abf`.
- **What was reviewed:** the uncommitted working tree.
- **Interpreter:** `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3` (3.13.7), with `PYTHONDONTWRITEBYTECODE=1` for every run.

## Basis (SHA-256, recomputed)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| D-PEC-89 proposal | `962a7879788e75cac41bc73c8320eb2be11b65fe104fcbb163fff892b49f8a73` (matches the required value) |
| `D-PEC-89_RULING_2026-09-24.md` (A selected, R13 included) | `536b058873a011a4ef3df60f243fc55ecd389c2900132bfa30592ba414d263e3` |
| `.agents/skills/software-code-review/SKILL.md` | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` |
| `workflows/software-code-review/WORKFLOW.md` (listed, not loaded; the skill was enough) | `9054dfd47318a680e54fe390b00c67e2baf9595156487d4d1897a83458414810` |
| `projects/pec/docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |

**Preimages at `9ffc54afc`:** all five opened paths match the proposal's rollback table (`d63932c2…6b33`, `05b9846a…ae0a`, `c8e23563…1c29`, `edbd41df…cadf`, `e9d65fc7…ed35`).

**Postimages:**

| Path (relative to `projects/pec/`) | SHA-256 |
|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `2cb21e2d251eeffd164d68ad436cb0b9f0d4b8fdabd41358f33a0d7ed40122b3` |
| `v2/src/pec_v2/adapters/storage/sqlite_store.py` | `edb15e2b96eb3b5cdf918c05cf58fce128063b02475233649e30bcc92864ad5c` |
| `v2/tests/storage/test_content_minimal_guard.py` | `3a4c98b32b1e4e07f921d7b567120377c63b7e526e0322480216346828ae8cba` |
| `v2/tests/storage/test_store_lifecycle.py` | `96d9917d6283eeb8fd6310991cd0166ecd24bcf76afccae840afee508ec2fb64` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `1fc417fc6b5461bd0623780e751bf37354df491f3f28e713b98c7d29417130a3` |

The guard and adapter postimages are byte-identical to the proposal's prototype hashes. I judged them on their content (item 1 below).

## 1. Is the change what the specification asks for?

**R9 and R10 (`content_minimal_guard.py`).**
- `_is_identifier` (`:286-287`) is written exactly as specified.
- The record ID is checked at `:144-145`: an invalid one becomes `<unknown>` and gets `INVALID_IDENTIFIER`.
- The fields container is checked at `:161` (`type(candidate_fields) is not tuple or not candidate_fields`) and `:168` (`type(candidate_fields) is tuple`).
- An invalid field name is reported at `fallback` (`<field:N>`) at `:175-176`. The old `field_name` echo variable is gone.
- `_valid_hex` is exact at `:291`.
- The path check is at `:295-296`, with the message `"path must be a non-empty exact str"` exactly as the specification words it.
- No value is copied or coerced, and no new failure code was added (still the nine codes).
- The only `isinstance` left is `isinstance(guarded, AdmissionFailure)` at `:183`, which does not test `str`, `int` or `tuple`.
- COUNT, STATE, field class and algorithm checks are unchanged.
- I found no other behaviour change. An accepted record containing all five field classes yields 19 output strings, and every one is an exact `str` (the persisted `field_class.value` included).

**E-2 wrapping (`sqlite_store.py`), against the specification's table:**
- **`close()` (`:141-147`):** catches `sqlite3.Error` and raises `StoreDataError("metadata store could not be closed") from error`. `_connection = None` runs only after a successful close.
- **`reopen()` (`:153-156`):** catches `OSError` from `mkdir` and raises `StoreConfigurationError("metadata store directory could not be created") from error`. Construction goes through the same path.
- **`delete()` (`:174-182`):** calls `self.close()` without wrapping it, so the old "closed for deletion" wrapper is gone. `FileNotFoundError` is still ignored. Any other `OSError` raises `StoreDataError("metadata store files could not be deleted") from error` at the first failure.

## 2. Do the tests prove each repair?

- **Test identity:** tests were extended in place. No test ID was added, `TEST_TO_VERIFICATION` is unchanged, and 13 tests are discovered and pass (`test_ver_009` passes).
- **`test_ver_005`:** exactly the two expected tuples changed. They are now at `:261` and `:265`, which were preimage `:194` and `:198`: `("<input:2>", "<record_id>", "INVALID_IDENTIFIER")` and `("field-name", "<field:0>", "INVALID_FIELD_NAME")`. Nothing else in that test changed.
- **R9 batch (`test_content_minimal_guard.py:546-639`):**
  - It has 14 inputs, matching the specification's list.
  - It asserts `(14, 0, 14)`, the exact ordered `(record_id, field_name, code)` list, `read_all() == ()` and `assert_no_persisted_residue`.
  - For every failure attribute it asserts an exact `str` whose value, f-string and `repr` do not contain the payload.
  - The subclass record ID and field name match the identifier pattern, so the test isolates the type check from the pattern check. The `MethodLiar`, `LengthLiar`, `LyingTuple` and `ClassSpoof` inputs would each be admitted, or would crash, if `isinstance` came back.
- **Policy test:** `ConformingInt(3)` was added. The four subclass constructor calls are asserted to raise `ValueError`. The syntax-tree check (`:450-466`) flags `isinstance` called by name or attribute whose type argument names `str`, `int` or `tuple`. Mutation M1 shows the syntax-tree check is doing real work in this test.
- **`test_ver_002` (`test_store_lifecycle.py:171-212`):** the three blocks follow the specification. The extra `threaded.read_all() == ()` after the cross-thread close is a legitimate proof that the handle was kept (it catches mutation X1 below).

## 3. Independent probes

My own script, `vprobe.py` (SHA-256 `7d776b09…eb0eb`), runs each case in a fresh temporary Git checkout under my scratch directory, outside the repository. The payload is `"VERIFIER-LEAK line A\n@@ -9 +9 @@ line B"`, and `Sneaky` overrides `__conform__`, `__format__`, `__str__` and `__repr__`.

- **Preimage:** `git archive 9ffc54afc` extracted to scratch. Output `probe_pre.out`, SHA-256 `99e35d13…d8f9`.
- **Candidate:** a copy of the working-tree `v2`. Output `probe_cand.out`, SHA-256 `9cf8021f…4e28`.

| Case | Preimage | Candidate |
|---|---|---|
| E1-01 PATH field, public `RepositoryPath(Sneaky)` | OPEN: accepted, payload in the database | CLOSED: constructor `ValueError` |
| E1-02 source path, public | OPEN: payload persisted | CLOSED: `ValueError` |
| E1-03 PATH field, forged shell | OPEN | CLOSED: `locator` `INVALID_VALUE` |
| E1-04 source path, forged shell | OPEN | CLOSED: `<source_path>` `SOURCE_CITATION` |
| E1-05 record ID `Sneaky` | OPEN: payload persisted | CLOSED: `<input:0>` `INVALID_IDENTIFIER` |
| E1-06 field name `Sneaky` | OPEN | CLOSED: `<field:0>` `INVALID_FIELD_NAME` |
| E1-07 / E1-08 source SHA digest, public / forged | OPEN / OPEN | CLOSED: `ValueError` / `<source_sha>` `SOURCE_CITATION` |
| E1-09 / E1-10 SHA field digest, public / forged | OPEN / OPEN | CLOSED: `ValueError` / `commit` `INVALID_VALUE` |
| E1-11 / E1-12 HASH digest, public / forged | OPEN / OPEN | CLOSED: `ValueError` / `snap` `INVALID_VALUE` |
| C2-2a public `Liar("../../etc/passwd")` as source path | OPEN: `etc/passwd` persisted | CLOSED: `ValueError` |
| C2-2b public `Liar("/etc/passwd")` as PATH | OPEN | CLOSED: `ValueError` |
| C2-2c forged `Liar("a/../../etc/passwd")` as both | OPEN | CLOSED: `SOURCE_CITATION` and `INVALID_VALUE` |
| LEN-1 `HexLen` (300 hex characters, reports length 40) | OPEN: 300-character digest persisted | CLOSED: `INVALID_VALUE` |
| TUP-1 lying tuple | OPEN: accepted with zero fields | CLOSED: `<record>` `EMPTY_RECORD` |
| DUP-1 field names that never compare equal | OPEN: misreported `DUPLICATE_RECORD` | CLOSED: `<field:0>` and `<field:1>` `INVALID_FIELD_NAME` |
| SPF-1 record ID with a spoofed `__class__` | OPEN: `TypeError` escapes `admit_batch` | CLOSED: `<input:0>` `INVALID_IDENTIFIER` |
| E3-1 exact-`str` payload as record ID | OPEN: echoed | CLOSED: `<input:0>` |
| E3-2 exact-`str` payload as field name | OPEN: echoed | CLOSED: `<field:0>` |
| E3-3 / E3-4 invalid `Sneaky` record ID / field name | OPEN: `Sneaky` object returned | CLOSED: placeholders |
| E2-1 `close()` from a thread that does not own the connection | OPEN: raw `ProgrammingError` | CLOSED: `StoreDataError`, cause `ProgrammingError`; handle kept; owner closes; then `StoreClosedError` |
| E2-2 `.pec-v2` is a regular file | OPEN: raw `FileExistsError` | CLOSED: `StoreConfigurationError`, cause `FileExistsError` |
| E2-3 construction in a read-only checkout | OPEN: raw `PermissionError` | CLOSED: `StoreConfigurationError`, cause `PermissionError` |
| E2-3b `reopen()` in a read-only checkout | OPEN: raw `PermissionError` | CLOSED: `StoreConfigurationError`; store stays closed |
| E2-4 sidecar name is a directory, on `delete()` | OPEN: raw `PermissionError` (EPERM) | CLOSED: `StoreDataError`, cause `PermissionError`; `reset()` recovers `()` |
| C2-4 `sqlite3.register_adapter(str, …)` | OPEN | **OPEN (expected: the stated threat boundary)** |
| **Total open** | **29 / 29** | **1 / 29 (C2-4 only)** |

All seven required reproductions (E1-01, E1-05, E1-09, C2-2a, TUP-1, SPF-1, E3-1) are open on the preimage and closed on the candidate.

## 4. Mutations

My own runner, `vmutate.py` (SHA-256 `16330524…0650`), applies each reversal to a fresh scratch copy of the candidate and runs the storage suite. Output `mutate.out`, SHA-256 `94d5db07…c58`.

| Mutation | Suite exit | Failing tests | Required tests caught? |
|---|---|---|---|
| Baseline | 0 | none | — |
| M1 `isinstance` in `_is_identifier` | 1 | both VER-008 tests | yes |
| M2 `isinstance` in `_valid_hex` | 1 | both VER-008 tests | yes |
| M3 `isinstance` in the path check | 1 | both VER-008 tests | yes |
| M4 `isinstance` in the container check (both sites) | 1 | both VER-008 tests | yes |
| M5 record-ID echo restored | 1 | `test_ver_005`, forged-wrapper test | yes |
| M6 field-name echo restored | 1 | `test_ver_005`, forged-wrapper test | yes |
| M7 R11 removed | 1 | `test_ver_002` | yes |
| M8 R12 removed | 1 | `test_ver_002` | yes |
| M9 R13 removed | 1 | `test_ver_002` | yes |
| X1 (extra) handle cleared before `close()` | 1 | `test_ver_002` | extra, caught |
| X2 (extra) R13 swallows the `OSError` | 1 | `test_ver_002` | extra, caught |
| X3 (extra) only the first container site reverted | 1 | both VER-008 tests | extra, caught |
| X4 (extra) `issubclass(type(v), str)` in `_valid_hex`, which dodges the syntax-tree check | 1 | both VER-008 tests (by behaviour) | extra, caught |
| X5 (extra) R12 catches only `FileExistsError` | 0 | none | **survives** (see N-1) |

## 5. Documentation (R14)

My script `vdoc.py` (SHA-256 `07f5236a…f9`) pulled the quoted text out of proposal lines 204-231 and compared it with the whitespace-normalized preimage and postimage.
- Every new string from edits 1-7 and all four paragraphs of edit 8 are present in the postimage and absent from the preimage.
- Every text the edits replace or delete is absent from the postimage.
- The document from "**Prose-like single-line paths.**" to the end is byte-identical to the preimage, which covers that paragraph and the kill-test paragraph.
- The threat-boundary paragraph, including C2-4, is present.
- No "routed for a separate owner ruling" or "`str`-subclass channel under …" pointer remains.

**The author's three placement judgements are all faithful:**
- **(a) SHA and HASH ("as an exact `str`").** In the SHA row, putting the phrase after the second "lowercase hex" covers both algorithms and reads correctly. Putting it after the first would qualify only `sha1`. In the HASH row, a literal insertion after "lowercase hex" would split "lowercase hex characters", so placing it after "characters" keeps the specified meaning.
- **(b) The list item in edit 7.** Dropping the "and" in REQ-002 is the grammar a list append needs; no other word changed. REQ-004, REQ-005 and REQ-009 were each inserted before the final "and …" item.
- **(c) The rewrap in edit 5.** The sentence about state rejections and `constraint="CON-001"` is word-for-word intact after normalization.

**Against the code and the PRD:**
- Each new claim holds against the code: the close error keeps the handle open for a retry, directory creation maps to the configuration error, the unlink error maps to the data error, a failure never echoes an invalid identifier, and only exact types are admitted.
- The text is consistent with PRD §6 PEC-K-10 (content-minimal), §7.1 and §7.2 (those inventory paragraphs only lose the stale caveat), PEC-SVC-005 (enforced at ingest) and PEC-SVC-006 (consumers may log failures without carrying caller text).
- I found no overclaim that the author could correct. The precision notes N-2 to N-4 concern the specification's own verbatim wording.

## 6. Containment

- `git diff --name-only 9ffc54afc` lists exactly the five granted paths.
- Untracked files are only under `…/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_03/`: `AUTHOR_RETURN_01.md`, `PREIMAGE.md`, `RUN.md`, the five `checks/*.json` files plus `mutation_manager_run.out` and `v2-store-guard_verbose.out`, and `probes/{probe_d89.py,probe_BEFORE_preimage.out,probe_AFTER_postimage.out,mutate_d89.py,mutate_AFTER.out}`.
- `validate_change_scope.py --base 9ffc54afc` with the five paths and the run root as allowed roots gives `"status": "PASS"`, `"violations": []`.
- The three unopened paths are unchanged:
  - `store.py`: `d7544f7191c38a40df49e55c8aaadbb54ea122003be5eb6ab7a2a1d6400a05eb`
  - `__init__.py`: `c9d8b3e5a1338ecf9dbc5a7405c47c69956e3c68e3219f60e3c988c1f1880540`
  - `software-workflow.json`: `8ec9ba6dcba7ea6b935923f5b4d846b2a9ac3f3d5cc43f5e160abe0971058a8b`
- The administrative files are unchanged: `_STATUS.md` `d9429b4e…555b` and `MEMORY.md` `4e16a24b…0395`, both matching `PREIMAGE.md`.
- `git diff --check 9ffc54afc` gives no output. The four changed `.py` files are ASCII-only.
- There is no `__pycache__` under `projects/pec`. There is one untracked, git-ignored `__pycache__` elsewhere in the checkout (N-5).
- `git status --short` was identical before and after all my runs.

## Commands run

| Command (working directory) | Exit | Result |
|---|---|---|
| `git status --short`; `git diff --name-only 9ffc54afc`; `git ls-files --others --exclude-standard`; `git rev-parse HEAD origin/main` (checkout root) | 0 | as in section 6 |
| `git diff --check 9ffc54afc` (checkout root) | 0 | no output |
| `git archive -o <scratch>/pre.tar 9ffc54afc projects/pec/v2 projects/pec/software-workflow.json`, then `tar -x` | 0 | preimage copy; hashes match |
| `python3 vprobe.py pre/projects/pec/v2` (scratch) | 0 | 29 / 29 open |
| `python3 vprobe.py cand/projects/pec/v2` (scratch) | 0 | 1 / 29 open (C2-4) |
| `python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v` (`projects/pec`) | 0 | Ran 13, OK; the same 13 IDs as the map |
| `python3 v2/tools/check_service_core_posture.py --config v2/config/service_core_posture.json --workflow software-workflow.json` (`projects/pec`) | 0 | `"verdict": "PASS"` |
| `python3 -m unittest discover -s v2/tests/config -p 'test_*.py'` (`projects/pec`) | 0 | Ran 12, OK |
| `python3 -m unittest discover -s v2/tests/contracts/api -p 'test_*.py'` (`projects/pec`) | 0 | Ran 6, OK |
| `python3 tools/practitioner_harness/harness.py self-check` (checkout root) | 0 | INFO=14, NOT_APPLICABLE=1, REVIEW=4, WARN=124 (same as the D-PEC-87 baseline) |
| `python3 vmutate.py cand/projects/pec` (scratch) | 0 | M1–M9 all caught; X5 survives |
| `python3 vdoc.py <proposal> <pre doc> <post doc>` | 0 | R14 verbatim; tail byte-identical |
| `python3 tools/software_workflow/validate_change_scope.py . --base 9ffc54afc --allowed …` | 0 | PASS |
| `python3 execution/_Scripts/pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <each of the five paths> --operation candidate-validation` (`projects/pec`) | 0 ×5 | `ALLOW`; register `f877d931…cbc` has no rows. (A first attempt with `--operation review` exited 2 with "invalid choice", which is my own argument error.) |

The manager's evidence matches my results: the five `checks/*.json` files all report `"status": "PASS"`, the verbose run has 13 `ok`, and `mutation_manager_run.out` shows M1–M9 caught.

## Blocking findings

None.

## Non-blocking findings

- **N-1 (test coverage; not a deviation from the specification).** `test_store_lifecycle.py:191-199`.
  - R12 is proved only with a regular file at `.pec-v2`, which raises `FileExistsError`. Mutation X5, which narrows the catch to `FileExistsError`, passes the whole suite. The permission-denied path (E2-3 and E2-3b) is proved only by probes.
  - The specification's proving test was followed exactly, so no correction is required in this slice.
  - Optional, if the manager wants it: extend `test_ver_002` in place with a `reopen()` on a read-only checkout, asserting `StoreConfigurationError` with an `OSError` cause.
- **N-2 (precision of the specification's text; the author must not change it).** `STORE_LIFECYCLE_AND_GUARD.md`, "Returned failures are content-minimal".
  - The placeholder list leaves out `<unknown>`, which `ContentMinimalGuard.guard()` returns to a caller that is not the store (`content_minimal_guard.py:139`, `:144`). Only the store relocates it to `<input:N>`.
  - The claim itself stays true: `<unknown>` is a fixed literal. No action in this slice; the spec owner may adjust the wording later.
- **N-3 (precision of the specification's text).** Doc, "Exact-type rule" paragraph.
  - "Every string in a `GuardedRecord` is … an exact `str`" does not strictly cover `GuardedField.field_class`, which is a `FieldClass` member, a str-based enum.
  - The store persists `.value`, which is an exact `str` (verified), and the same paragraph explains that enum members are identity-checked. No action.
- **N-4 (residual risk in verbatim text).** Doc edit 1: "None of the adapter's own engine or filesystem operations lets a raw `sqlite3` or `OSError` exception escape a port method."
  - `connection.close()` inside the error handlers in `reopen()` (`sqlite_store.py:167`, `:170`) is not wrapped. A raw error could escape only if that close also failed during an open that was already failing. This is theoretical and outside the specification's wrapping table.
  - No action.
- **N-5 (manager housekeeping).**
  - An untracked, git-ignored `tools/software_workflow/__pycache__/software_workflow_common.cpython-313.pyc` exists (mtime 2026-09-25 00:10, ignored by `.gitignore:26`). It predates my commands, all of which ran with `PYTHONDONTWRITEBYTECODE=1`. It is probably left over from a `run_registered_checks.py` run.
  - It is not in the diff, but the brief requires no `__pycache__` in the checkout.
  - Correction: the manager deletes that directory before closeout.
  - The two `.pyc` files under `execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/**` are tracked on `main` and are not part of this slice.
- **N-6 (evidence record).**
  - `checks/mutation_manager_run.out` is byte-identical to the author's `probes/mutate_AFTER.out` (both `33ce93f5f4a21dfb405c20454d5543875d0ebe2f45c2f78c4b12ec8f0082fb1d`). That fits a deterministic rerun of the same script, but nothing in the records says whether it was rerun or copied.
  - `RUN.md` (`6e64efd7…3c4f`) records nothing after "N1 complete."
  - Correction: the manager records in `RUN.md` the exact command, working directory and exit code that produced `checks/mutation_manager_run.out`, and completes the progress log.

## Is the return ready for fan-in?

Yes, it is suitable for manager fan-in. Two risks remain:
- **By design:** C2-4, meaning in-process code that registers a global `sqlite3` adapter. The document now states this boundary.
- **Test coverage:** N-1, the permission-denied `mkdir` path, which only probes cover.

This verdict does not grant CHECKING, acceptance, merge or any lifecycle change.

## Verifier scratch artifacts

These are outside the checkout. None were written into the repository.

`/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/verifier/`:
- `vprobe.py`, `vmutate.py`, `vdoc.py`
- `probe_pre.out`, `probe_cand.out`, `mutate.out`
- `storage.out`, `posture.out`, `registry.out`, `api.out`, `harness.out`
- `pre/` (preimage extraction) and `cand/` (candidate copy)
