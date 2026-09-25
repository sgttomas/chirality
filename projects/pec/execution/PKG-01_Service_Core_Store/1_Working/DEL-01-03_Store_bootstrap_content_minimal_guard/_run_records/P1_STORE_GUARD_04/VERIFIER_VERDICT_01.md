<!-- Saved verbatim by WORKING_ITEMS (node C4) from the final report of the
read-only verifier (Claude Code Agent tool, subagent_type pec-reviewer,
model opus, agent id aba7254fd920b8534, host-reported claude-opus-5-5),
returned directly to this manager (no HELP_HUMAN relay). The harness's
line indentation has been removed; the text is otherwise unchanged. -->

VERDICT: PASS

# VERIFIER_VERDICT_01: P1_STORE_GUARD_04 (D-PEC-91, option A-53), DEL-01-03

This review was done by a read-only TASK (Type 2) verifier under WORKING_ITEMS (HELP_HUMAN run `HELP-HUMAN-PEC-20260923-SCA005`, node C4). The host reports the model as `claude-opus-5-5`. The `high` reasoning level is instruction-asserted. The method was the project skill `.agents/skills/software-code-review/SKILL.md`. I did not delegate or repair anything, and wrote nothing to the checkout. This verdict makes no CHECKING, ISSUED or acceptance claim.

## Candidate reviewed

- **Candidate:** `d9dcb0126f3cb054ea542f62091d1fcf3122601c`. This is HEAD of `claude/pec-d91-count-domain-slice`, one commit on top of the base.
- **Base (preimage):** `origin/main` `8b6553850aa8a98cb44aed02e9fe91e23b1234bd`.
- **Checkout state:** `git status --short --untracked-files=all --ignored` was empty at the end, and HEAD had not changed.

## Basis read (SHA-256, `shasum -a 256`)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `.agents/skills/software-code-review/SKILL.md` | `06c27b1be5cfbd9e638570918a8f837d8439c8073c40d3ef708e53874f95570a` (matches the expected hash) |
| `D-PEC-91_RULING_2026-09-25.md` | `5d896204a0afcf39066f5aa56a9e043d199ed8fe7eb96397bcbe054f90ef3fbe` |
| `D-PEC-91_del_01_03_count_domain_encoding_residual_proposal_2026-09-25.md` | `5c044b095621bfb098bb3d4e69d55b5a0594a3c73322d58b440a767e2d2413ec` (matches the ruling) |
| `projects/pec/docs/PRD.md` | `6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba` |
| DEL-01-03 `ScopeOfWork.md` | `986ef15532cd65f17e8276ee9194b29469f559aca5616d2d3412fa3effca6341` |
| `RUN.md` | `8dc611e0082028307dbf4073df262ad65082dc1490718afd1d27dfa90227d65e` (context) |
| `PREIMAGE.md` | `92b0cfea095124d58414f9d577c491de20de5cd0974daffb06f13a6587c8522f` (context) |
| `AUTHOR_RETURN_01.md` | `c4c661ca7e7654aa9ec1796c3a68d01d44729401e31028888194e92f7d7fb0ae` (context) |
| `P1_STORE_GUARD_03/probes/mutate_d89.py` | `98595ce1f895d13ba2875c803d94af0ed7c4eb0698e681ce606f1a17fcdf726a` (copied into scratch and run there) |
| `execution/_Scripts/pec_reliance_hold.py` | `b1712e4b6e9f1476c577afd9170a4dd078beaa95878fa5f3b6c46a17b548cd0e` |
| `execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv` | `f877d9316c7da76218399838aa6b69f1bb51bbd3e59b5b1d19b31f69ad741cbc` (header only) |

**Host:** `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`, Python 3.13.7 (CPython), SQLite 3.50.4, `id -u` 501. The interpreter's default digit limit is 4300 and `str_digits_check_threshold` is 640. Every python run used `PYTHONDONTWRITEBYTECODE=1`.

**Reliance-hold preflight:** `pec_reliance_hold.py --register execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv --target <path> --operation candidate-validation`, run for each of the four opened paths, returned `ALLOW` with exit 0 each time.

## Per-check results

### 1. Containment: PASS

- **Changed paths.** `git diff --name-only 8b6553850 d9dcb0126` (exit 0) lists 26 paths:
  - the four granted product paths under `projects/pec/`: `v2/src/pec_v2/core/content_minimal_guard.py`, `v2/tests/storage/test_content_minimal_guard.py`, `v2/tests/storage/test_store_lifecycle.py` and `v2/docs/STORE_LIFECYCLE_AND_GUARD.md`;
  - 22 files under `_run_records/P1_STORE_GUARD_04/`;
  - nothing else.
- **`MEMORY.md`.** It is not in the diff (hash `54f57151…2b14`, same as the preimage). That is expected, because the work graph schedules that entry at N6, after verification.
- **Preimage and postimage hashes.** I hashed git-archive exports of both revisions.
  - The four opened preimages equal the proposal's rollback table (`2cb21e2d…22b3`, `3a4c98b3…8cba`, `96d9917d…fb64`, `1fc417fc…30a3`).
  - The postimages equal the author's claims (`740a4a74…19ee9`, `d4655f2f…8ead`, `b51ca900…d3e7`, `89c3a5fc…2cadb`).
  - `sqlite_store.py` (`edb15e2b…ad5c`), `core/ports/store.py` (`d7544f71…05eb`), `adapters/storage/__init__.py` (`c9d8b3e5…0540`) and `software-workflow.json` (`8ec9ba6d…8a8b`) are identical in both revisions.
  - `_STATUS.md` is unchanged (`d9429b4e…555b`).
- **Test identity.** The sorted `def test_` sets are identical in both revisions, with 13 IDs. The `TEST_TO_VERIFICATION` block is byte-identical; only the `import os` line shifts it down by one line.
- **ASCII.** Of the 55 added `.py` lines, none contains a non-ASCII character (checked with a Python byte scan).
- **Whitespace.** `git diff --check 8b6553850 d9dcb0126` exited 0.

### 2. R15 code: PASS

- **Exact rule.** `content_minimal_guard.py:20` is `_MAX_COUNT = 2**53 - 1`. `:216` is `elif field_class is FieldClass.COUNT and type(value) is int and 0 <= value <= _MAX_COUNT:`. `rendered = str(value)` at `:217` is reached only after the comparison.
- **Comment (`:16-19`).** It cites the RFC 8259 JSON safe-integer range, says "16 decimal digits" and gives the 640-digit limit. It does not mention SQLite INTEGER, as the ruling requires.
- **Out-of-domain handling.** Values outside the domain fall to the existing `else` at `:224-231`. My probe shows the message is still "value does not satisfy the runtime domain for count" and the constraint is still `None`.
- **Exact-type rule (D-PEC-89) intact.** `type(value) is int` short-circuits before the comparison, so a `bool` or `int` subclass never reaches `<=`. The VER-008 check that the guard has no `isinstance` against `str`, `int` or `tuple` still passes. An `isinstance` reversal (my X2) is caught.
- **No other behaviour change.** The two lines above are the whole code diff.

### 3. Independent F-1 reproduction: PASS

I wrote my own probe (`vprobe.py`, scratch only). It ran on both exports at limits 4300, 640 and 0, with exit 0 for each tree.

**Preimage:**
- `guard()` on COUNT `10**5000` (and on `10**4300`) raises `ValueError` at 4300 and at 640. At 0 it is admitted as 5,001 characters.
- `admit_batch((good, 10**5000))` raises `ValueError` and persists nothing (`persisted=[]`) at 4300 and 640. At 0 the result is `(2,2,0)` and the 5,001-digit value is persisted.
- COUNT `2**63` is admitted at every limit, and so are `2**53` and `2**64`. The batch result is `(2,2,0)`.

**Candidate:**
- At every limit, `2**53`, `2**63`, `2**64`, `10**639`, `10**4300` and `10**5000` each give `[('r','c','INVALID_VALUE')]` from `guard()`.
- `admit_batch` gives `(2,1,1)`, with `ids=('good',)`, failure `('big','c','INVALID_VALUE')`, and only `good` persisted.
- The candidate output contains no `RAISES` line.

### 4. Boundary cases on the candidate, at 4300, 640 and 0: PASS

| Input | `guard()` and `admit_batch` result |
|---|---|
| `2**53 - 1` | admitted as `"9007199254740991"` (16 characters); batch `(2,2,0)` |
| `2**53` | located `INVALID_VALUE` |
| `0` | admitted as `"0"` |
| `-1`, `True`, `False` | located `INVALID_VALUE`; batch `(2,1,1)` |
| `SubInt(5)`, `SubInt(2**53 - 1)` (in range), `SubInt(10**5000)` | located `INVALID_VALUE`; batch `(2,1,1)` |
| `10**639`, `10**4300`, `10**5000` | located `INVALID_VALUE`; batch `(2,1,1)` |

Nothing raised, whether through `guard()` or through `admit_batch`.

### 5. Tests and mutations: PASS

**Suite runs:**
- Candidate: `python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v` in the scratch export ran 13 tests, all `ok`, exit 0.
- Preimage: the same command ran 13 tests, OK, exit 0.

**Do the new assertions prove R15 and R16?**
- **They fail on the preimage.** Running the candidate tests with the preimage guard file (my "PRE" run) exits 1:
  - `test_ver_005` errors;
  - `test_ver_008_policy` has 4 failures and 1 error.
- **The digit limit is restored.**
  - I ran `test_ver_008_policy` alone with the process limit set to 5000 beforehand.
  - Afterwards the limit was 5000 again, on the candidate (test passing), on M2 (failing) and on M5 (erroring).
  - The `addCleanup` plus the explicit `finally` restore the saved value, not a hard-coded default. `default_max_str_digits` is used only as one of the three loop values (judgment call J1). That is sound.
- **`subTest` cannot hide a failure.**
  - Each subTest failure or error was reported by name, for example `(digit_limit=640)` and `(field='over_max')`, and made the run exit 1.
  - A failed `assertTrue(at_max.accepted)` ends only that subTest. The failure is still recorded, and the next limit still runs.
  - Failure messages contain no large integers, so formatting them cannot raise under the reduced limits.

**My own mutations.** Each one was applied by my own edits to a separate scratch copy of the candidate `v2` tree, then the full storage suite was run.

| ID | Mutation | Exit | Failing tests |
|---|---|---|---|
| M1 | preimage branch `value >= 0` | 1 | `test_ver_005`, `test_ver_008_policy` |
| M2 | `< _MAX_COUNT` | 1 | `test_ver_008_policy` (all three limits) |
| M3 | `<= _MAX_COUNT + 1` | 1 | `test_ver_008_policy` |
| M4 | bound replaced by a helper that returns `None` when `str()` raises `ValueError` | 1 | `test_ver_008_policy` |
| M5 | `len(str(value)) > 0` evaluated before the bound | 1 | `test_ver_005`, `test_ver_008_policy` |
| M6 | `_MAX_COUNT = 10**4000` | 1 | `test_ver_008_policy` |
| M7 | R12 narrowed to `except FileExistsError` | 1 | `test_ver_002` (raw `PermissionError` escapes) |
| X1 | M7 plus the R16 condition replaced by `if False:` | 0 | none; **survives**, as expected |
| X2 | `isinstance(value, int)` reversal | 1 | `test_ver_005`, `test_ver_008_policy` |
| X3 | `_MAX_COUNT = 2**53 - 2` | 1 | `test_ver_008_policy` |

Every mutation is caught by the tests the specification names.

**D-PEC-89 reversals.** I copied `mutate_d89.py` into scratch and ran it against my candidate export (exit 0). The baseline ran 13 tests, OK. M1 to M9 were each "CAUGHT by all named tests", and M4a and M4b also failed tests. It printed `RESULT PASS`. This agrees with `checks/mutate_d89_manager_run.out`.

### 6. R16 host condition: PASS. The read-only block ran on this host.

- `id -u` is 501.
- My own probe (`r16_check.py`, candidate export) did the following:
  - it made a scratch checkout mode `0o555`;
  - `os.access(checkout, W_OK)` returned `False`;
  - `SqliteMetadataStore(checkout)` raised `pec_v2.core.ports.store.StoreConfigurationError`, and `type(e) is port.StoreConfigurationError` was True;
  - the message was "metadata store directory could not be created" and the cause was `PermissionError`;
  - `.pec-v2` did not exist afterwards.
- The mutation results show that the block's assertions are what catch M7. M7 is caught by `test_ver_002`. X1 is M7 with the block disabled, and it survives.

### 7. R17 documentation: PASS

**Exact text.** I rebuilt the expected postimage from the preimage doc by applying D1 to D10, taking the text from the proposal bytes:
- D1 from L151, the A-53 rationale sentence from L169, D6 from L159 and D10 from L167;
- with the A-53 substitutions: `2**53 - 1` (9,007,199,254,740,991), "At 16 digits", the over list `2**53`, `2**63`, `10**639`, `10**5000`, and "(at most `2**53 - 1` each)".

After collapsing whitespace, the rebuilt text equals the candidate exactly. The only byte differences are where line breaks fall at D7 (`:154-155`) and D9 (`:184-185`): the candidate keeps the original breaks rather than re-wrapping. The diff hunks touch only preimage lines 95, 100, 134, 137, 140, 141, 154, 155, 174, 184 and 185, and add 2 lines (D10 and a blank line). Every other line is byte-unchanged, including the "Exact-type rule" paragraph, the threat-boundary paragraph apart from its two insertions, and the kill-test paragraph.

**Truthfulness against the code:**
- The COUNT row states the domain `0..2**53 - 1` and the rejections that the code makes.
- D1's rationale is correct: IEEE-754 doubles are exact up to `2**53 - 1`, and SQLite stores that value exactly. The row also correctly says the value is stored as decimal text in the `TEXT` `value` column.
- "16 digits, below 640" is correct, so admission does not depend on `sys.set_int_max_str_digits` (demonstrated in item 3).
- The D8 relocation of `<unknown>` to `<input:N>` matches `sqlite_store.py:59-60`.
- The D6 file `P1_STORE_GUARD_01/children/AUTHOR/VERIFICATION_EXECUTION_REMEDIATION.json` exists. This slice's verbose runs are recorded under the run root, with 13 `ok` lines each.
- The D4 and D5 test-map text matches the actual tests.

**Truthfulness against the product basis:**
- PEC-K-10 (PRD §6) still admits counts, now with a stated bound.
- The §7.2 ahead/behind and dirty counts are covered.
- PEC-SVC-005 holds: the guard is still enforced at ingest.
- REQ-005 and AC-005 hold: rejections are explicit and located, with no silent drop or substitution.
- AC-009 holds: the COUNT decision cites D-PEC-91.
- AC-004's residual is stated honestly in D7 and D10.
- The threat boundary is kept, with the D9 additions only.

**Judgment calls:**
- **J2 (no re-wrap, long lines at `:100`, `:174`, `:184-185`, `:203`) is not a defect.** D2 explicitly allows the line to wrap, the table rows are already long, Markdown rendering is unaffected, and `git diff --check` is clean.
- **J5 (`:122` "nonnegative counts … fit the finite classes" left unchanged) is not a defect.** The specification requires every other line to stay byte-unchanged, so editing it would have enlarged the grant. It remains true as a statement about which §7.2 kinds of value fit which class. See N-1 below.
- **J7 (the author read `sqlite_store.py`) is not a defect.** The grant limits which paths may be modified; the file's hash is unchanged.

### 8. Registered checks: PASS

- `v2-core-posture` re-run in the scratch candidate export (the tool only reads files and prints JSON): exit 0, `"verdict": "PASS"`, `core_tree_sha256` `88f590c019eb67febfbb569a34ec688831edc7e867f251376ecebe3f7799c016`. This is identical to `checks/v2-core-posture.json`.
- `v2-loop-registry` in scratch: ran 12, OK.
- `v2-api-contract` in scratch: ran 6, OK.
- The manager's `checks/*.json` files report PASS with exit 0 for all five check IDs, including `harness-self-check`.

## Findings

There are no blocking findings.

- **N-1. NON-BLOCKING, severity INFO. Location: `projects/pec/v2/docs/STORE_LIFECYCLE_AND_GUARD.md:122`.**
  - **Issue:** "nonnegative counts … fit the finite classes" is broader than the COUNT domain now stated at `:95`. Read alone, it could suggest that any nonnegative `int` is admitted.
  - **Not an author defect:** the specification requires this line to stay byte-unchanged.
  - **Required repair:** none in this slice. If a later granted doc edit opens this file, qualify it, for example "nonnegative counts within the COUNT bound".
- **N-2. NON-BLOCKING, severity INFO (administrative). Location: `_run_records/P1_STORE_GUARD_04/RUN.md` §"Progress log".**
  - **Issue:** at this revision the log records only "N1 complete". The N2 author return and the N3 check outputs are already committed but not logged. The basis table also has no `agents/AGENT_TASK.md` hash (the author's D-1).
  - **Required repair (manager, within the run-root grant):** record N2 and N3, and this N4 verdict, before N7.
- **Recorded but ruled, not a finding.** D3's "is skipped" describes a conditional block that passes silently where directory permissions are not enforced. Clarification N-4 in the ruling covers this. On this host the block ran (item 6).

**Residual risk.** R16 is proven only on hosts that enforce directory permissions. On a root runner or a filesystem without permissions, the block does not run and M7 would survive there. This is the known, stated condition.

**Suitability for fan-in.** The implementation is suitable for manager fan-in (N5). This verdict makes no lifecycle acceptance.

## Scratch

- **Created:** `/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T/d91_verifier.2T1xJ5` (from `mktemp -d`, outside the checkout).
- **Contents:** git-archive exports of both revisions (`projects/pec/v2` and `projects/pec/software-workflow.json`), my probe, mutation, restore and doc-check scripts, and eleven mutation copies.
- **Removed:** with `rm -rf` at the end, then confirmed absent.
- **Checkout:** nothing was written to it, and there is no `__pycache__` or `.pec-v2` under `projects/pec`.
