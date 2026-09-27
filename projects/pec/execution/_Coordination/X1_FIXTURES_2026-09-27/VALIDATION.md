# VALIDATION — D-PEC-106 X1 act (run root `X1_FIXTURES_2026-09-27`)

Finite verification of the proposal (`D-PEC-106_x1_parser_fixture_suites_proposal_2026-09-26.md`, §"Finite verification"), run by WORKING_ITEMS on 2026-09-27 (UTC). Every command, exit code and output is saved under `evidence/`; each output file opens with its `date -u` line and the command line.

## Environment

- Worktree `/Users/ryan/ai-env/projects/chirality/.claude/worktrees/pec-d106-act`, a `git worktree` of the full clone `/Users/ryan/ai-env/projects/chirality` (common dir `.git`), branch `claude/pec-d106-x1-fixtures-act`, cut from fetched `origin/main` `c5d852c4a`.
- Clone: `git rev-parse --is-shallow-repository` `false`; `extensions.partialclone`, `remote.origin.partialclonefilter` and `remote.origin.promisor` all unset (`evidence/row1_basis.out`).
- Git 2.54.0 (Apple Git-157), which honours `GIT_NO_LAZY_FETCH` (2.44 or later). Python 3.13.7 at `/Library/Frameworks/Python.framework/Versions/3.13/bin/python3`. `PYTHONDONTWRITEBYTECODE=1` throughout.
- `TMPDIR` exported in every shell that ran an aid, to `/private/tmp/claude-501/-Users-ryan-ai-env-projects-chirality--claude-worktrees-pec-project-assessment-6106d5/978bf4ac-7408-4c14-9b91-74754c7e380f/scratchpad/x1a-mgr.1PYo3d` (outside the repository). Disclosure: in one early shell, before `TMPDIR` was exported, the manager wrote one scratch file (`bound.sums`, a filtered copy of the prep `SHA256SUMS`) into the system temp directory under `/var/folders`; it was removed at once and recreated under the scratch `TMPDIR`. No aid ran in that shell, and nothing was written in the repository.

## Results

| Row | Check | Command (see evidence file for the exact line) | Result | Evidence |
|---|---|---|---|---|
| 0 | Bound copies | copy of `apply_x1p.py`, 35 candidates and 9 aids from `PEC_X1_FIXTURES_PREP_2026-09-26/`; `shasum -a 256 -c` against the prep `SHA256SUMS` lines; prep `SHA256SUMS` 112/112 | exit 0; 45/45 OK; `apply_x1p.py` `452ff66a…2428` | `evidence/row0_bound_copy.out`, `evidence/bound_copy.sums` |
| 1 | Basis | `git fetch`; ruling and proposal hashes at `origin/main`; register row | `c5d852c4a` contains ruling `5161630b…96fe`, proposal `677b59f6…d279`, row `D-PEC-106` `RULED A / FX-PEC-0 AND THRESHOLDS CONFIRMED / L / M / EFFECTIVE ON MERGE` | `evidence/row1_basis.out` |
| 1 | Preimages | `write_status.sh`, three `_STATUS.md`, holds register and script, `docs/SPEC.md`; `MEMORY.md` and `v2/tests/parsers` absent | `write_status.sh` `0bf835f5…ece3` recomputed; `_STATUS.md` `6f94c04f…cf06f`, `4341d6b2…04fe`, `e67be587…1056` as tabled, all `INITIALIZED` | `evidence/row1_preimages.out` |
| 1 | Dependencies | `evidence/deps_read.py` over every PEC `Dependencies.csv` | 10/10 named rows ACTIVE `PREREQUISITE` `PENDING` as tabled; the only ACTIVE `PREREQUISITE` rows from the three deliverables are the three on DEL-01-01, which the fixtures do not need (proposal §"Scope, lifecycle and dependencies") | `evidence/row1_dependencies.out` |
| 1 | Holds, dispatch | `pec_reliance_hold.py --operation dispatch-for-production` on 41 targets (35 act paths, three `_STATUS.md`, three `MEMORY.md`), cwd `projects/pec` | ALLOW, exit 0, 41/41; `date -u` 17:37 UTC | `evidence/row1_hold_dispatch_for_production.out`, `evidence/hold_targets.txt` |
| 1 | Check-only | `apply_x1p.py --check-only` from the run root | exit 0; `CHECK preflight passed` (12 pins, preimage, absences) | `evidence/row1_apply_check_only.out` |
| 1 | Pins | `report_x1p_pins.py <repo> origin/main <manifest>` | `RESULT PASS 19/19` (FX-PEC-0.graph path drift informational; pin is by blob) | `evidence/row1_pins.out` |
| 1 | Full prep suite | `run_x1p_checks.sh <repo> c5d852c4a <prep dir> <out>` on `git archive` exports | `OVERALL PASS` (act, containment, six checks, 10 tests, 442/442, 19/19, 67/67, strict/harness/receipts identical, hygiene, fault injection 11/11, negative controls 20/20) | `evidence/pre_act_checks_c5d852c4a/SUMMARY.out`, `evidence/pre_act_checks.cmd` |
| 1 | Fixture suite | `run_fixture_suite.sh <repo> HEAD <run-root candidates> -v` | 10 tests OK, exit 0 | `evidence/row1_fixture_suite_pre_act.out` |
| 1a | Add-on L | three tabled `write_status.sh … IN_PROGRESS "…X1_FIXTURES_2026-09-27/"` from the repository root | exit 0 ×3; postimages `84b238d2…9b5e`, `bfc99586…1ff6`, `50bc10f4…372a`; slot rule 3/3 (`check_addon_L_slots.py` rebuilds each postimage from the preimage at `c5d852c4a`); committed as `3f1e1a4d7` before the act | `evidence/row1a_addon_L.out`, `evidence/row1a_addon_L_slots.out` |
| 2 | Act | `apply_x1p.py --check-only`, then one real run, from the repository root with HEAD `3f1e1a4d7` | check-only exit 0; act **exit 0**, `CHECK targets 35/35 byte-exact; write set = grant (34 created, 1 modified, 0 removed under projects/pec outside the run root); pinned 12/12 unchanged`. The grant is consumed. No rolled-back or refused run occurred | `evidence/row2_apply_check_only.out`, `evidence/row2_apply.out` |
| 2b | Bytes and hygiene | `evidence/check_bytes_hygiene.py` | 35/35 targets equal tabled postimages and candidates; 0 extra files; hygiene 35/35 | `evidence/row2b_bytes_hygiene.out` |
| 3 | Registered checks | `run_registered_checks.py software-workflow.json --check` ×6, cwd `projects/pec`; `unittest discover -v`; posture | all six exit 0; `v2-parsers` ran the 10 tests of `TEST_TO_VERIFICATION` (names compared); `core_tree_sha256` `dd7e1dda…6e5a` unchanged, `workflow_sha256` `8ec9ba6d…` → `d55fff77…` | `evidence/row3_*` |
| 4 | Selection | `select_affected_checks.py software-workflow.json <35 changed paths>` | the six checks of row 3 | `evidence/row4_select_affected.out` |
| 5 | Bindings and pins | `verify_x1p_bindings.py <repo> HEAD <candidates>`; `report_x1p_pins.py <repo> HEAD <manifest>` | `RESULT PASS 442/442`; `RESULT PASS 19/19` | `evidence/row5_*` |
| 6 | Every-PR and registers | strict registers, harness self-check, receipts validator, before (HEAD `c5d852c4a`, before L) and after the act | identical: strict exit 1 with 0 errors and 26 `XRG-013` warnings; harness exit 0; receipts exit 0 | `evidence/row6_*` |
| 7 | Lifecycle | `git diff --name-status origin/main...HEAD -- '**/_STATUS.md'` | exactly the three tabled `_STATUS.md` (A + L) | `evidence/row7_lifecycle_final.out` (at the head carrying verdict 02 and the return, against the then-current `origin/main`); intermediate capture `evidence/row7_lifecycle.out` (at `7ff6eb7bb`, against `c5d852c4a`) |
| 8 | Containment | `git diff --name-status origin/main...HEAD` | the 34 creates; `software-workflow.json`; the three `_STATUS.md`; the run root; the brief copy and the return under `AgentRuns/HELP-HUMAN-PEC-20260925-POST-SCA005/`; nothing else | `evidence/row8_containment_final.out` (same head as row 7 final); intermediate capture `evidence/row8_containment.out` (at `7ff6eb7bb`, against `c5d852c4a`) |
| 9 | Whitespace | `git diff --check origin/main...HEAD` | clean | `evidence/row9_diff_check.out` (same head as row 7 final); two earlier failed attempts below |
| Fan-in | Holds, reliance | `pec_reliance_hold.py --operation rely-for-production` on the same 41 targets, before fan-in of the verifier's verdict | ALLOW, exit 0, 41/41 | `evidence/fanin_hold_rely_for_production.out` |

## Rerun after `origin/main` moved

`origin/main` moved during the run from `c5d852c4a` to `0adfbc747` (PR #1009, App SCA-APP-011 records only; 312 paths, none under `projects/pec`). The branch merged it without a rebase (merge `0040299f6`). None of the 12 act pins, the 35 targets, the three `_STATUS.md`, `write_status.sh`, the holds register or script, the three deliverables' `Dependencies.csv`, the prep folder or `v2/**` changed. Reruns at the merged head, in `evidence/rerun_after_merge_0adfbc747/`:

- `act_pins_and_targets.py`: 12 pins, 35 target postimages, three add-on L postimages, `write_status.sh`, register and script: `RESULT PASS 53/53`;
- `report_x1p_pins.py … HEAD`: `RESULT PASS 19/19`; dependency rows identical to row 1;
- `run_x1p_checks.sh <repo> origin/main <prep dir> <out>` on exports of `0adfbc747`: `OVERALL PASS` (same lines as row 1);
- fixture suite at HEAD: 10 tests OK; the six registered checks exit 0; bindings 442/442;
- strict, harness and receipts at HEAD identical to the pre-act export of `0adfbc747` after normalizing the root path (`row6_compare.out`).

## Independent verification

`VERIFIER_VERDICT_01.md`: fresh read-only `pec-reviewer` applying `software-code-review` (`ee085d58…8bca`) to head `f4ab6c307`. **PASS WITH NOTES**; three non-blocking evidence-recording findings, dispositioned in that file. Backcheck: `VERIFIER_VERDICT_02.md` at head `04a333f73`, **PASS WITH NOTES** (final row 7/8/9 captures then pending; one inferred HEAD stated as fact; one observation), dispositioned in that file.

## Evidence-handling notes (verdict 01 findings 1–3)

- **Whitespace normalization after commit.** `git diff --check` flagged trailing whitespace inside two captured outputs. Only trailing whitespace was removed, in commit `f657822b2`:
  - `evidence/row1_basis.out`: raw capture at `2886540c0` (`86476cb8…5b3a`), normalized `4bc0e8ce…8a89` (the register-row line lost one trailing blank).
  - `evidence/row1a_addon_L.out`: raw capture at `3f1e1a4d7` (`eebeb32c…5ca5925`), normalized `7597dafa…0906`. Blank unified-diff context lines `" "` became `""`, so the captured diff text is no longer patch-applicable. The binding add-on L evidence is the postimage hashes and `row1a_addon_L_slots.out`, which is unchanged.
- **Row 9 attempts.** Attempt 1 (17:46:19 UTC, exit 2; HEAD inferred as `7ff6eb7bb` from its commit time, since the capture has no HEAD line) flagged those two files; it is kept as `evidence/row9_diff_check_attempt1.out`, restored from `f657822b2`, with each trailing-whitespace run replaced by a visible marker. Attempt 2 (17:46:34 UTC, HEAD `f657822b2`, exit 2) flagged the whitespace inside attempt 1's own captured output; it is kept as `evidence/row9_diff_check_attempt2.out` (marked the same way). The final clean capture is `evidence/row9_diff_check.out`.
- **Composite command.** The last line of `evidence/row1_basis.out` was produced by `git log -1 --format='%H %s %P' c5d852c4a`; the echoed label reads `--format='%H %s'` and omits `%P`. The file is not rewritten.

No check was weakened, skipped or re-pinned.
