# AUTHOR_RETURN_01 — P1_STORE_GUARD_04 (D-PEC-91 A-53), author cycle 1

Role: TASK (Type 2) author under WORKING_ITEMS (node N2 of this run; HELP_HUMAN
run `HELP-HUMAN-PEC-20260923-SCA005`, node C4), PKG-01 / DEL-01-03. No
delegation. Method: bundled workflow
`chirality-root:bundled:workflow:software-bounded-implementation`. Host reports
the serving model as `claude-opus-5-5`; the `high` reasoning level is
instruction-asserted. Date 2026-09-25 (session date).

Worktree `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a4acca0ffd3953d47`,
branch `claude/pec-d91-count-domain-slice`, HEAD
`8b6553850aa8a98cb44aed02e9fe91e23b1234bd`. No state-changing git command was
run. This return makes no CHECKING, ISSUED or acceptance claim.

## Basis read (SHA-256)

| Source | SHA-256 |
|---|---|
| `AGENTS.md` (Root) | `c8ce87ef342902cb081bc659b26fc9a4edda1b6dba513814e5cb1e14e0b1dffd` |
| `projects/pec/AGENTS.md` | `46689c36d5379029a34a5c5d26f109445e338fca82b86e590826bcbc39ad3846` |
| `agents/AGENT_TASK.md` | `1a13a5b00b3ce01ff8519efe6b46bcbe0cd6a5b7985e24282fa7efa2c57c8fb7` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-91_RULING_2026-09-25.md` | `5d896204a0afcf39066f5aa56a9e043d199ed8fe7eb96397bcbe054f90ef3fbe` |
| `projects/pec/execution/_Coordination/_DECISIONS/D-PEC-91_del_01_03_count_domain_encoding_residual_proposal_2026-09-25.md` | `5c044b095621bfb098bb3d4e69d55b5a0594a3c73322d58b440a767e2d2413ec` (matches the ruling and the brief) |
| `workflows/software-bounded-implementation/WORKFLOW.md` | `2ea0ddf4f53241fa94274e709b8042ad9de4d8beb9c82cd1ed1dcd0c6f8f0f7b` |
| `_run_records/P1_STORE_GUARD_03/probes/mutate_d89.py` (context, run read-only) | `98595ce1f895d13ba2875c803d94af0ed7c4eb0698e681ce606f1a17fcdf726a` |
| `_run_records/P1_STORE_GUARD_04/RUN.md` (context, not written) | `8dc611e0082028307dbf4073df262ad65082dc1490718afd1d27dfa90227d65e` |
| `_run_records/P1_STORE_GUARD_04/PREIMAGE.md` (context, not written) | `92b0cfea095124d58414f9d577c491de20de5cd0974daffb06f13a6587c8522f` |

Also read for context, not written: `P1_STORE_GUARD_03/probes/probe_BEFORE_preimage.out`
and `mutate_AFTER.out`; lines 140-170 of `v2/src/pec_v2/adapters/storage/sqlite_store.py`
(read only, to take M7's exact R12 pattern; see judgment call J7).

Preimage re-verification at start (before any edit), `shasum -a 256` from
`projects/pec/`: all four opened paths and all four unopened paths equal the
proposal's rollback table and `PREIMAGE.md` (guard `2cb21e2d…22b3`, guard tests
`3a4c98b3…8cba`, lifecycle tests `96d9917d…fb64`, doc `1fc417fc…30a3`,
`sqlite_store.py` `edb15e2b…ad5c`, `ports/store.py` `d7544f71…05eb`,
`adapters/storage/__init__.py` `c9d8b3e5…0540`, `software-workflow.json`
`8ec9ba6d…8a8b`). `git status --short --ignored` at start showed only the
untracked run root.

## Host

- Interpreter `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`,
  Python 3.13.7 (CPython, `v3.13.7:bcee1c32211`); `python3` on PATH resolves to it.
- SQLite library 3.50.4.
- `id -u` 501 (not root). Default `sys.get_int_max_str_digits()` 4300;
  `sys.int_info.str_digits_check_threshold` 640.
- Every python run used `PYTHONDONTWRITEBYTECODE=1`; every probe script also sets
  `sys.dont_write_bytecode = True`.

## Per-repair status

| Repair | Status | Change | Proving test (in place) |
|---|---|---|---|
| R15 COUNT domain (A-53) | Applied | `_MAX_COUNT = 2**53 - 1` after `_MAX_SEGMENT_BYTES`, with a 4-line comment citing the JSON safe-integer range (RFC 8259), 16 digits, and the 640-digit smallest nonzero limit. COUNT branch is now `field_class is FieldClass.COUNT and type(value) is int and 0 <= value <= _MAX_COUNT`; `rendered = str(value)` unchanged and reached only after the comparison. Out-of-domain falls to the existing `else`: `INVALID_VALUE` at the field name, message "value does not satisfy the runtime domain for count", constraint `None` (evidenced by `probe_d91_failure_shape_AFTER.out`). No other code change. | `test_ver_008_policy_is_fixed_finite_and_domain_checked`; `test_ver_005_rejections_are_located_and_accounting_has_no_silent_loss_or_substitution` |
| R16 read-only checkout | Applied | `test_ver_002`: `import os`; after `store_directory.unlink()`, saves the checkout mode, sets `0o555`, and if `os.access(checkout, os.W_OK)` is false asserts `SqliteMetadataStore(checkout)` raises `StoreConfigurationError`, `type(...) is port_module.StoreConfigurationError`, `__cause__` is a `PermissionError`, and `.pec-v2` was not created; restores the saved mode in `finally`. No product change. | `test_ver_002_creation_restart_closed_delete_open_reset_and_empty_recreation` |
| R17 documentation D1-D10 (A-53) | Applied | D1-D10 as quoted, with the A-53 substitutions (see Diff summary). | Verifier text review (not a test) |

Test identity: no test ID added; `TEST_TO_VERIFICATION` unchanged; the storage
suite discovers the same 13 IDs and `test_ver_009` passes.

## Diff summary (`git diff --stat`: 4 files, 68 insertions, 13 deletions)

- `v2/src/pec_v2/core/content_minimal_guard.py` (+6/-1): the constant and comment
  (lines 16-20), and the COUNT branch (line 216).
- `v2/tests/storage/test_content_minimal_guard.py` (+34/-1):
  - `test_ver_005`: input 14 `self.record("over-count", MetadataField("count", FieldClass.COUNT, 10**5000))`;
    expected failure list gains `("over-count", "count", "INVALID_VALUE")` last;
    counts `(15, 1, 14)`. `accepted_record_ids == ("fresh",)` and the readback
    assertions are unchanged.
  - `test_ver_008_policy`: `invalid_values` gains `over_max` (COUNT `2**53`) and
    `over_digit_limit` (COUNT `10**5000`). New block: saves
    `sys.get_int_max_str_digits()`, registers `addCleanup(sys.set_int_max_str_digits, original)`,
    and in `try/finally` (explicit restore) loops over
    `(sys.int_info.default_max_str_digits, 640, 0)`; in a `subTest(digit_limit=…)`
    asserts `2**53 - 1` admitted and rendered `"9007199254740991"`, and each of
    `2**53`, `2**63`, `10**639`, `10**5000` yields exactly
    `[("count-over", "n", "INVALID_VALUE")]`.
- `v2/tests/storage/test_store_lifecycle.py` (+15/-0): `import os`; the R16 block.
- `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` (+13/-11 lines; preimage line numbers):
  - D1 `:95` COUNT row: bound `2**53 - 1` (9,007,199,254,740,991); the proposal's
    A-53 rationale sentence (proposal L169) replaces the SQLite-INTEGER sentence;
    "At 16 digits". Verified by script: equals proposal L151 after exactly those
    three substitutions.
  - D2 `:100`: "counts above `2**53 - 1`," inserted.
  - D3 `:134`: "a read-only checkout," inserted; sentence appended.
  - D4 `:137`: inserted as quoted.
  - D5 `:140`: "the COUNT boundary (`2**53 - 1` admitted; `2**53`, `2**63`, `10**639`, and `10**5000` rejected) under the default, smallest (640), and unlimited (0) interpreter digit limits" inserted.
  - D6 `:141`: replaced as quoted.
  - D7 `:154-155`: "verbatim" and "or the deliberate-encoding residual" inserted.
  - D8 `:174`: placeholder text replaced as quoted.
  - D9 `:184-185`: both insertions as quoted.
  - D10: new paragraph after `:201` (new line 203, blank lines either side),
    "(at most `2**53 - 1` each)" in place of "(at most 63 bits each)". Verified
    by script: equals proposal L167 after exactly that substitution.
  - Every other line is byte-unchanged (the diff touches only preimage lines
    95, 100, 134, 137, 140, 141, 154, 155, 174, 184, 185 and inserts 2 lines).
    The only non-ASCII characters on changed doc lines are 3 pre-existing `§`.

## F-1 before / after (`probe_d91.py`; per limit)

Guard outcome for `guard()` on COUNT, and `admit_batch((good, big))` as
`(attempted, accepted, rejected)` with what persisted.

BEFORE (preimage bytes, `probe_BEFORE_preimage.out`):

| COUNT | limit 4300 | limit 640 | limit 0 |
|---|---|---|---|
| `2**53 - 1` | admitted `"9007199254740991"`; batch (2,2,0) | same | same |
| `2**53` | admitted; batch (2,2,0), both persisted | same | same |
| `2**63`, `2**64` | admitted; batch (2,2,0), both persisted | same | same |
| `10**639` | admitted (640 chars); batch (2,2,0) | same | same |
| `10**4300`, `10**5000` | **guard raises ValueError; admit_batch raises ValueError; nothing persisted** | **same** | admitted (4,301 / 5,001 chars); batch (2,2,0), persisted |
| `-1`, `True`, `SubInt(5)` | located INVALID_VALUE; batch (2,1,1), good only | same | same |

F-1 minimum set reproduced: `guard()` on `10**5000` raises `ValueError` at 4300
and 640 and is admitted at 0; `admit_batch((good, 10**5000))` raises and
persists nothing at 4300; COUNT `2**63` (and `2**53`) admitted.

AFTER (postimage, `probe_AFTER_postimage.out`):

| COUNT | limit 4300 | limit 640 | limit 0 |
|---|---|---|---|
| `2**53 - 1` | admitted `"9007199254740991"`; batch (2,2,0) | same | same |
| `2**53`, `2**63`, `2**64`, `10**639`, `10**4300`, `10**5000` | `[('r','items','INVALID_VALUE')]`; batch (2,1,1), failure `('big','items','INVALID_VALUE')`, only `good` persisted | same | same |
| `-1`, `True`, `SubInt(5)` | unchanged: located INVALID_VALUE; batch (2,1,1) | same | same |

No case raises on the postimage at any limit.

## Commands and exit codes (cwd `projects/pec/` unless stated)

| # | Command | Exit | Output |
|---|---|---|---|
| 1 | `PYTHONDONTWRITEBYTECODE=1 python3 <RR>/probes/probe_d91.py v2` (preimage, before any edit) | 0 | `probes/probe_BEFORE_preimage.out` |
| 2 | `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s v2/tests/storage -p 'test_*.py' -v` (postimage) | 0 | `probes/storage_suite_verbose_AFTER.out`: Ran 13, 13 `ok`, same IDs as the map; `test_ver_009` ok |
| 3 | `PYTHONDONTWRITEBYTECODE=1 python3 <RR>/probes/probe_d91.py v2` (postimage) | 0 | `probes/probe_AFTER_postimage.out` |
| 4 | `PYTHONDONTWRITEBYTECODE=1 python3 <RR>/probes/probe_d91_failure_shape.py v2` (postimage) | 0 | `probes/probe_d91_failure_shape_AFTER.out` |
| 5 | `PYTHONDONTWRITEBYTECODE=1 python3 <RR>/probes/r16_block_probe.py v2` (postimage) | 0 | `probes/r16_block_probe_AFTER.out` |
| 6 | `PYTHONDONTWRITEBYTECODE=1 python3 <RR>/probes/mutate_d91.py v2` | 0 | `probes/mutate_d91_AFTER.out`, `RESULT PASS` |
| 7 | `PYTHONDONTWRITEBYTECODE=1 python3 <P1_STORE_GUARD_03>/probes/mutate_d89.py v2` (runner run read-only in place) | 0 | `probes/mutate_d89_on_postimage.out`, `RESULT PASS` |
| 8 | `git -C <REPO> diff --stat` | 0 | 4 product files only |
| 9 | `git -C <REPO> diff --check` | 0 | clean |
| 10 | ASCII scan of added `.py` diff lines (`grep -P '[^\x00-\x7F]'`) | — | 0 non-ASCII lines |

`python3` = `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3` throughout.
`<RR>` = `execution/PKG-01_Service_Core_Store/1_Working/DEL-01-03_Store_bootstrap_content_minimal_guard/_run_records/P1_STORE_GUARD_04`.
The other registered checks (`v2-core-posture`, `v2-loop-registry`,
`v2-api-contract`, `harness-self-check`) were not run by the author; the work
graph assigns them to WORKING_ITEMS (N3).

## Did R16's read-only block run?

Yes, on this host (uid 501). Evidence, not assertion:

1. `r16_block_probe.py` copies the postimage v2 tree to a temporary directory
   outside the checkout, inserts one marker-writing line as the first statement
   inside `if not os.access(self.checkout, os.W_OK):`, and runs only
   `test_ver_002` there: exit 0, "Ran 1 test … OK", marker written = `True`.
2. `mutate_d91.py` reports "host enforces directory permissions (0o555 dir not
   writable): True", and M7 (R12 narrowed to `except FileExistsError`) is caught
   by `test_ver_002` alone. Without the block, M7 survives the suite (D-PEC-89
   verifier X5; proposal L274), so the catch shows the block's assertions ran.

## Mutation results (all 16 caught)

D-PEC-91 (`mutate_d91_AFTER.out`; baseline exit 0, ran 13, no failures):

| ID | Mutation | Failing tests | Verdict |
|---|---|---|---|
| M1 | upper bound removed (preimage `value >= 0`) | test_ver_005, test_ver_008_policy | CAUGHT by all named |
| M2 | `0 <= value < _MAX_COUNT` | test_ver_008_policy | CAUGHT |
| M3 | `0 <= value <= _MAX_COUNT + 1` | test_ver_008_policy | CAUGHT |
| M4 | bound replaced by catching `ValueError` from `str()` | test_ver_008_policy | CAUGHT |
| M5 | `str()` evaluated before the bound | test_ver_005, test_ver_008_policy | CAUGHT by all named |
| M6 | `_MAX_COUNT = 10**4000` | test_ver_008_policy | CAUGHT |
| M7 | R12 narrowed to `except FileExistsError` (scratch copy of `sqlite_store.py` only) | test_ver_002 | CAUGHT |

D-PEC-89 regression (`mutate_d89_on_postimage.out`; baseline exit 0, ran 13):
M1-M9 each "CAUGHT by all named tests" (M1-M4 by both VER-008 tests; M5-M6 by
test_ver_005 and the forged-wrapper test; M7-M9 by test_ver_002); supplementary
M4a/M4b also fail tests. `RESULT PASS`.

Every mutation ran in a `tempfile.TemporaryDirectory` copy under
`/var/folders/0s/50y7rb796d1bqdxmpcz6qg800000gn/T/`; the checkout tree was only read.

## Postimage SHA-256

| Path (relative to `projects/pec/`) | SHA-256 |
|---|---|
| `v2/src/pec_v2/core/content_minimal_guard.py` | `740a4a74122178cc31947bb69c23d6aa55abc15b87c523dcf1c551dee3e19ee9` |
| `v2/tests/storage/test_content_minimal_guard.py` | `d4655f2f95e953b2f27ce43e1d622260be86d883fa6050fa7b3e2e6fe9468ead` |
| `v2/tests/storage/test_store_lifecycle.py` | `b51ca900667d38b47de3dfc514a350d7aabff157f447bb05e6ada9c0edc6d3e7` |
| `v2/docs/STORE_LIFECYCLE_AND_GUARD.md` | `89c3a5fcc722a232a587a721949cb3ec0ef69825f6e266ef36b29fa69d32cadb` |

Unchanged after the work (same as preimage): `sqlite_store.py` `edb15e2b…ad5c`,
`ports/store.py` `d7544f71…05eb`, `adapters/storage/__init__.py` `c9d8b3e5…0540`,
`software-workflow.json` `8ec9ba6d…8a8b`, DEL-01-03 `_STATUS.md` `d9429b4e…555b`,
`MEMORY.md` `54f57151…2b14`. Full `git diff` SHA-256
`9e596f856758e361246e7bd597e11c5352a483c3b954193cb5bf183c720ef4e4`.

Run-root files created by the author (all under `<RR>/`):

| File | SHA-256 |
|---|---|
| `probes/probe_d91.py` | `b8f7d945e0327c23eafb7260c6eb9aaa3bbd0a10e3dd393759678e0eee91b64f` |
| `probes/probe_BEFORE_preimage.out` | `ff2263ea39a2073bd23472545b40b9c53f2b4a56dd04230bb8401763ed589a6a` |
| `probes/probe_AFTER_postimage.out` | `5984a5b6f18a0abe84285b915a7abd08ffcf147cd10caff7ff02f274d5af1723` |
| `probes/probe_d91_failure_shape.py` | `96ae13beb990fac6b8c93eb652bf0c8ac845569c8a199ebd0a3b18232474dd20` |
| `probes/probe_d91_failure_shape_AFTER.out` | `a2e2657cbed046d94c92566d3c9a2a89d0f6ea95b14c73b124d534795651d194` |
| `probes/r16_block_probe.py` | `474fecd791b8e79742d0d66b801fd0ab168f0c10b40a9c4ea49e531034b2ade9` |
| `probes/r16_block_probe_AFTER.out` | `9beecb449a112dc616390b056363cddc025f7c96d0424793d7014e14ea3e7e48` |
| `probes/mutate_d91.py` | `1f0827a63fc0d59f79dae73d80a39013a90596d56f5117ee51837dbf9f00b79e` |
| `probes/mutate_d91_AFTER.out` | `47cd594031370dbe7a8fb0b28331d082d6d72604c0c4911a38d8b20e49be0ccb` |
| `probes/mutate_d89_on_postimage.out` | `e355c2be8ab4f519ceb83df134b36a1bb4a8ba95352a96cf833c76dc0e75b2ca` |
| `probes/storage_suite_verbose_AFTER.out` | `94cc35f2c00678c3f48c6119d45be77e060bdd7a693b8cbbcbe04d7d934e4b02` |
| `AUTHOR_RETURN_01.md` | this file |

## Containment and cleanup

- `git status --short --untracked-files=all`: exactly the four product paths
  modified, plus untracked files under `P1_STORE_GUARD_04/` (the manager's
  `RUN.md`, `PREIMAGE.md`, empty `checks/`, and the author files above).
- No `__pycache__` anywhere under `projects/pec` (`find` empty). The only
  `__pycache__` directories in the worktree are two tracked Root files under
  `execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/`,
  present at HEAD and untouched.
- Files deleted: none by hand. No `<RR>/probes/_scratch/` was created. Every
  scratch tree copy and SQLite store lived in a `tempfile.TemporaryDirectory`
  (prefixes `probe_d91_`, `mutate_d91_`, `mutate_d89_`, `r16_block_`, plus the
  suite's own temporary checkouts) outside the checkout and was removed on exit;
  a post-run `find` in `$TMPDIR` found 0 directories with those prefixes.

## Judgment calls and discrepancies (for the manager and verifier)

- **J1. "default" digit limit in the test.** The R15 loop uses
  `sys.int_info.default_max_str_digits` (the interpreter default, 4300), not the
  process's current setting. The current setting is saved and restored by
  `addCleanup` and explicitly in `finally`. The probe's "default" is the current
  setting at start, which was 4300 on this host.
- **J2. Doc line wrapping.** No paragraph was re-wrapped. Replacements confined
  to one line stay on that line, which lengthens lines 100 (D2), 174 (D8), 184
  and 185 (D9) past the doc's usual width. D7 keeps the original break after
  "prose-like". D10 is inserted as one line, as quoted. `git diff --check` is
  clean. Markdown rendering is unaffected.
- **J3. Wording that the proposal does not fix.** The four-line R15 code comment
  and the two-line R16 comment in `test_ver_002` are my own words. They meet the
  ruling's requirements: RFC 8259 / JSON safe-integer range, 16 digits, and 640.
  They do not mention SQLite INTEGER.
- **J4. R16 mode restore** uses the saved `st_mode & 0o7777`, not a fixed mode.
  The test adds no import besides `os`.
- **J5. No other A-53 consequential edit was made.** The ruling's list includes
  a proposal L213 rollback note. That note is in the proposal, not in any of the
  four paths, so nothing here needs it. Doc line 122 ("nonnegative counts … fit
  the finite classes") was left byte-unchanged. It still reads true as a class
  statement, but a verifier may want to consider it next to the new bound. I
  did not change it because it is not clearly implied by the ruling's
  consequential-wording list.
- **J6. Mutation forms.** M4 is implemented as
  `… type(value) is int and value >= 0 and _m4_render(value) is not None:`,
  with a module helper that returns `None` on `ValueError` (appended in the
  scratch copy). M5 is `… type(value) is int and (early := str(value)) is not None and 0 <= value <= _MAX_COUNT:`.
  M1 is the exact preimage branch, so M1 being caught also shows that the new
  assertions fail on the preimage guard.
- **J7. Reading the unopened adapter.** I read part of `sqlite_store.py` (R12
  region, lines 140-170). This was a read only, used to take M7's exact pattern;
  its hash is unchanged. If "stay unopened" is meant to forbid reading too, the
  manager should record this.
- **D-1 (information).** The manager's `RUN.md` basis lists no hash for
  `agents/AGENT_TASK.md`; this return records it above.
