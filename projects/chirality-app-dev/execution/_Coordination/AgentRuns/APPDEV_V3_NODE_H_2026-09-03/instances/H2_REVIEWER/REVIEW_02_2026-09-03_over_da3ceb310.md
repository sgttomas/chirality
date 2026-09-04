# REVIEW — Node H round 2 (DEL-09-01-V3-01, Section 8 preservation evidence)

- **Reviewer:** Claude Fable 5.1 (`claude-fable-5-1`), fresh read-only ephemeral Agent 2, `TASK + software-code-review` pattern, own detached worktree `wt-reviewH2` at `da3ceb310` (removed at the end of this review).
- **Basis:** `e59efa4830fb54143c86e511ec35a6d1a476f72e`.
- **Round-1 head:** `021e1f1863670f30cf81df909a417bf550cbc370` (reviewed FAIL, H1-F1 MAJOR).
- **Round-2 head:** `da3ceb310ebf4bcf4cc51f3e493467c45bfd201f` (`evidence(app): node H round-1 review remediation (H1-F1..F8, F10, F12)`).
- **Remediation diff `021e1f186..da3ceb310`:** 58 files, +1,862 −29 — 47 added (44 under `run-head-e59efa483-round2/`, `COMPARE_RESULT_round2.txt`, `probe/RUNNER.md`, `instances/H2_REVIEWER/REVIEW_01_2026-09-03_over_021e1f186.md`), 11 modified (`EVIDENCE.md`, `MANIFEST.sha256` ×3, `compare-section8-summaries.py`, `rerun-section8-local.sh`, `TASK_RUN_2026-09-03_NODE_H.md`, `CHECKS.json`, `COORDINATOR_DECISIONS.md`, `ORCHESTRATION_PLAN.md`, `RETURN.md`). Every path is under `DEL-09-01…` or `APPDEV_V3_NODE_H_2026-09-03` — `git diff --name-only 021e1f186..da3ceb310 | grep -vE 'DEL-09-01|APPDEV_V3_NODE_H'` is empty. No product source, script, fixture, workflow, `runtime/**`, `package.json`, or lockfile path. 100% of the remediation diff read; every authored file read in full; every new captured byte scanned mechanically.
- Selectability flip not re-litigated (ruled `WITHIN_AUTHORITY` in round 1). `_STATUS.md` is byte-unchanged since `021e1f186`; its only delta from basis is still the one flip line.

## Commands run (cwd = review worktree unless stated) and exit codes

| Command | Exit | Result |
|---|---|---|
| `git worktree add --detach <scratch>/wt-reviewH2 da3ceb310…` | 0 | HEAD = `da3ceb310` |
| `git diff --stat 021e1f186..da3ceb310` | 0 | 58 files, +1862 −29 (matches the implementer's claim) |
| `git diff --check e59efa483..da3ceb310` | 0 | clean |
| `git diff --check 021e1f186..da3ceb310` | 0 | clean |
| `git diff --check 021e1f186..da3ceb310 -- ':!*.sse' ':!*.log'` | 0 | clean without the folder-local exemption |
| Python whitespace-class scan over all 44 round-2 files | — | blank-line-at-EOF in the 5 new `.sse` (hidden by the existing `.gitattributes`); `logs/harness-ready.json` has no trailing newline (not a `--check` class). No CR/tab/NUL/non-UTF-8 |
| `python3 tools/software_workflow/validate_change_scope.py . --base e59efa483… --head da3ceb310… --allowed <DEL-09-01> --allowed <node H run record>` | 0 | `status: PASS`, `violations: []` |
| Retained-bytes check: `git diff --quiet 021e1f186 da3ceb310 -- <f>` for each of the 99 files under `run-head-e59efa483/` + `run-base-0c683fb16/` excl. `MANIFEST.sha256`; `git ls-tree` listing diff of both folders between heads | 0 | `total=99 changed=0`; no file added or removed in either folder |
| `shasum -a 256 -c MANIFEST.sha256` (cwd `…/run-head-e59efa483/`) | **0** | 56/56 OK; 56 files on disk excl. manifest; `LC_ALL=C sort -c` sorted |
| `shasum -a 256 -c MANIFEST.sha256` (cwd `…/run-base-0c683fb16/`) | **0** | 43/43 OK; 43 files on disk; sorted |
| `shasum -a 256 -c MANIFEST.sha256` (cwd `…/run-head-e59efa483-round2/`) | **0** | 43/43 OK; 43 files on disk; sorted; includes `logs/teardown.txt`, `logs/cleanup.txt`, `logs/driver.log` |
| `shasum -a 256 -c MANIFEST.sha256` (cwd bundle `Evidence/Node_H_Section8_Preservation_2026-09-03/`) | **0** | 161/161 OK; 162 files on disk; `comm` of disk vs manifest: only `MANIFEST.sha256` itself is absent from the manifest, nothing in the manifest is missing on disk; the three per-run `MANIFEST.sha256` are pinned (`6d7216c4…` base, `374c8a41…` head, `956e7af9…` round2); sorted |
| `git diff 021e1f186..da3ceb310 -- run-*/MANIFEST.sha256` | 0 | each per-run manifest changed exactly in the three logs round 1 flagged (`daemon.log`, `driver.log`, `next-dev.log`) and gained `logs/cleanup.txt` + `logs/teardown.txt`; no other hash line changed |
| `shasum -a 256` of `instances/H2_REVIEWER/REVIEW_01_2026-09-03_over_021e1f186.md` vs scratchpad `REVIEW_NODE_H_R1.md`; `cmp` | 0 | both `6be44efc895d7f9a69e5e6b400bb7ac08841ed1cc9c7cdcf29f96e3ba8405acb`; IDENTICAL (filed verbatim) |
| `bash -n rerun-section8-local.sh`; `shellcheck -S warning rerun-section8-local.sh` | 0 / 0 | syntax OK; no warnings |
| `grep -nE 'lsof.*kill\|xargs kill\|kill.*lsof' rerun-section8-local.sh` | 1 | no port-based kill remains (the only `lsof` uses are the fail-fast probe at :236 and the observation lines at :127, :266) |
| `python3 compare-section8-summaries.py <HEAD-local> <basis-local> <CI 681> <CI 686>` (cwd bundle; script imports only `json`, `sys`) | 0 | stdout `cmp`-identical to `COMPARE_RESULT.txt`; `BEHAVIOUR_PROJECTIONS_EQUAL=true` |
| `python3 compare-section8-summaries.py <HEAD-local> <round2-local> <basis-local> <CI 681> <CI 686>` | 0 | stdout `cmp`-identical to `COMPARE_RESULT_round2.txt`; `EQUAL=true` |
| Comparator negative: two identical *failing* summaries (overall `fail` + one row `fail`) | **1** | `PROBLEM: summary status is 'fail'…`, `PROBLEM: row section8.smoke_stream status is 'fail'…` (H1-F6 fixed) |
| Comparator negative: overall `pass` but one row `fail`, compared with itself | 1 | row-level `PROBLEM`; exit 1 |
| Comparator negative: mutated `eventCount` vs original | 1 | `EQUAL=false` |
| `python3 -m json.tool CHECKS.json` | 0 | valid JSON |
| Secrets scan over the 44 round-2 files (`sk-ant`, `Bearer `, `api_key`, `token=`, `password`, `"token":`, base64 ≥ 80) | — | zero hits |
| `/Users/` scan over the 44 round-2 files | — | zero hits (paths present are `…/scratchpad/wt-nodeH` ×32 and `/private/tmp/chirality-s8.F8ehog/…` ×14 only — both classes declared in `EVIDENCE.md:108`/`:104`) |
| Secrets + `/Users/` scan over the 14 non-run files in the remediation diff | — | only the sentences describing the scans (`EVIDENCE.md:103`, `:108`; the filed round-1 review) |
| F-APP-2 grep (`notariz\|codesign\|signed\|release[- ]ready\|publish`) over all 58 changed files | — | 9 hits: the F-APP-2 disclaimer (`EVIDENCE.md:6`), "unsigned development Electron.app" descriptive uses (`EVIDENCE.md:35`, `RUNNER.md:24`, script `:194`, `RETURN.md:23`), the A1/write-locus sentence (`ORCHESTRATION_PLAN.md:31`), the TASK_RUN state line, and the filed round-1 review quoting the grep. `ORCHESTRATION_PLAN.md` no longer contains "publish". No claim |

Not run (per brief): `rerun-section8-local.sh` itself. Judged by reading, by the diff, and by the retained round-2 outputs.

## Round-1 disposition table

| ID | Sev (R1) | Disposition | Evidence |
|---|---|---|---|
| H1-F1 | MAJOR | **FIXED** | Script: the manifest write moved from the old `:295` (deleted in the diff) into `teardown()` at `rerun-section8-local.sh:146–150`, after `teardown.txt` (`:122–128`), `cleanup.txt` (`:129–144`) and the final `log "teardown done"` (`:145`); trap installed at `:152`. Retained round-1 manifests regenerated from unchanged bytes: 0/99 retained files changed; `shasum -c` now 56/56 and 43/43 OK; each manifest diff is exactly the three flagged logs plus `teardown.txt`/`cleanup.txt`. Round-2 run: script-written manifest 43/43 OK, `driver.log` ends `[02:05:38] teardown done` and its hash in the manifest verifies. Bundle manifest 161/161 OK, excludes only itself, pins all three per-run manifests. `EVIDENCE.md:107` and `RETURN.md` §1 item 1 corrected with an explicit provenance note |
| H1-F2 | MINOR | **FIXED** | Fail-fast at `:236–238` (`exit 72`) before the `next dev` launch at `:240`; teardown signals only `$NEXT_PID` + direct children (`:99–101`, `:117–120`) and processes whose command line carries `--user-data-dir=$USER_DATA` (`:116`); the `lsof -t -i:$PORT … kill -9` loop is gone (grep exit 1). `CHECKS.json` `rerun-script-port-fail-fast`: exit 72, foreign listener on 51843 survived. See H2-F1 for the one residual (grandchildren) |
| H1-F3 | MINOR | **FIXED** | `:69–74` sets `USER_DATA_CREATED`; `:130` removes `USER_DATA` only when `=1`; `:133–137` records `user_data_retained=caller-supplied` otherwise; header `:33–43` documents the shared `HARNESS_TMP_ROOT` and the no-concurrency rule. Round-2 `environment.txt:13` `user_data_created_by_script=1`, `cleanup.txt:1` `user_data_removed=yes` |
| H1-F4 | NOTE | **FIXED** | `:140` `checkout_leftovers=` line; present in round-2 `cleanup.txt:4` naming both gitignored paths. `EVIDENCE.md:106` declares that the round-1 trees predate the line |
| H1-F5 | NOTE | **FIXED** | `EVIDENCE.md:108` "Host-identifying strings in retained bytes" names the scratch-worktree path (embedding `-Users-ryan-`), the lsof username, and `LAUNCH_BRIEF.md`'s `REPO=/Users/ryan/dev/chirality` |
| H1-F6 | NOTE | **FIXED** | `compare-section8-summaries.py:51–55` asserts `status == "pass"` overall and per row; docstring `:15–17` updated; negative case exits 1 (my rerun); `COMPARE_RESULT.txt` byte-identical after regeneration; `COMPARE_RESULT_round2.txt` reproduces |
| H1-F7 | NOTE | **FIXED** | `probe/RUNNER.md` (24 lines): exact `spawnSync` wrapper (`timeout:20000`, `killSignal:'SIGKILL'`, `--user-data-dir=/private/tmp/chirality-s8-probe`), per-log `<ARGS>` and sandbox-state table, the unretained first attempt named, Electron version. Log first lines (`status null signal SIGKILL error ETIMEDOUT`, `status 0 signal null error undefined`) match the wrapper's `console.log` format. Probe logs unchanged |
| H1-F8 | NOTE | **FIXED** | `TASK_RUN_2026-09-03_NODE_H.md:3` DRAFT banner naming exactly the anticipatory items (review pointer, `_STATUS.md` revision, receipt number) |
| H1-F9 | NOTE | **N/A (carried)** | Coordinator D1 (`COORDINATOR_DECISIONS.md:38–41`) carries the History-line quotation to the closeout commit; `_STATUS.md` unchanged this round, as required |
| H1-F10 | NOTE | **FIXED** | `ORCHESTRATION_PLAN.md:8` "Required verdict to push" |
| H1-F11 | NOTE | **N/A** | No change required in round 1; `.gitattributes` unchanged; authored files still pass `--check` without the exemption |
| H1-F12 | NOTE | **FIXED** | `CHECKS.json` `validate-change-scope` entry records the `--head 021e1f186…` form; `scope_validation_command.note` amended. The `--head da3ceb310` form cannot be inside the commit it names; my rerun of it passes |
| H1-F13 | NOTE | **N/A** | No change required; the workflow-mirroring steps 1–6 are untouched by the diff |

## New findings (round 2)

| ID | Severity | File:line | Claim under test | Evidence | Fix / suggestion |
|---|---|---|---|---|---|
| H2-F1 | NOTE | `rerun-section8-local.sh:100`, `:117–120` | H1-F2 "teardown signals only `$NEXT_PID` + children" | The SIGTERM (`pkill -P`) and SIGKILL (`pgrep -P`) fallbacks reach only *direct* children of `$NEXT_PID` (the `npm run` process). The listener is a grandchild: round-2 `containment-before.txt:11` shows `node 84306` on the port while `teardown.txt:3` gives `next_pid=84274`. Normal shutdown works because `next` forwards SIGTERM to its server child (round-2 `teardown.txt:5` `port_51842_listeners_after_stop=0`), but the round-1 port-kill backstop that would have caught a wedged `next` is gone, so a hung dev server would now survive teardown. The condition is observable (`port_<PORT>_listeners_after_stop` would be non-zero) and the script has already demonstrated a clean run, so this is a robustness note, not a defect in the evidence | Walk the tree recursively (e.g. a small `descendants()` helper over `pgrep -P`) before the SIGKILL pass, keeping the by-pid scoping |
| H2-F2 | NOTE | `run-head-e59efa483-round2/logs/environment.txt:3` (`head=021e1f186…`); `EVIDENCE.md:73` ("run of the corrected script at HEAD"); `CHECKS.json` `rerun-script-round2-smoke` ("fixed script at HEAD e59efa483") | Round-2 run provenance | The round-2 run was executed in `wt-nodeH` checked out at `021e1f186` with the remediation edits still uncommitted (`git-status-before.txt`: 10 dirty paths, all under DEL-09-01 / the run record), not at `e59efa483` as the folder name and narrative say. Product bytes are identical: `git diff --name-only e59efa483..021e1f186` outside the two evidence roots is empty, and round-2 `built-bundles.sha256` is byte-identical to the round-1 head run's. The retained bytes are truthful; only the narrative label elides one evidence-only commit. Corollary: the exact script bytes that produced the round-2 run are the uncommitted working-tree version, whose observable behaviour (`user_data_created_by_script` line, `checkout_leftovers` line, manifest last) matches the committed `080b9205…` script | One clause in `EVIDENCE.md:73` and the `CHECKS.json` summary: "checkout at `021e1f186` (product bytes identical to `e59efa483`; same `built-bundles.sha256` as `run-head-e59efa483/`)" |
| H2-F3 | NOTE | `rerun-section8-local.sh:236` | Fail-fast "before step 4" | The port check sits after the build (step 1), daemon start (step 2) and project registration (step 3), so an occupied port still costs a daemon start + teardown before `exit 72` (as the `CHECKS.json` fail-fast test shows: daemon torn down, manifest written). Correct as claimed; merely late | Move the check above step 1 (it depends only on `$PORT`) |
| H2-F4 | NOTE | `rerun-section8-local.sh:116`, `:123`, `:215`, `:260` | Kill scoping by `pgrep -f -- "--user-data-dir=$USER_DATA"` | `pgrep -f` is an unanchored regex substring match, so a caller-supplied `USER_DATA` that is a prefix of another daemon's user-data path (e.g. `/private/tmp/s8` vs `/private/tmp/s8-other`) would match that daemon too. Unreachable with the mktemp default (`chirality-s8.XXXXXX`) and only relevant to the caller-supplied path the script now protects from `rm -rf` | Anchor the pattern (`--user-data-dir=$USER_DATA( |$)`) or match on `$DAEMON_ELECTRON_PID` + `$DAEMON_PID` |
| H2-F5 | NOTE | `EVIDENCE.md:106`; `_run_records/TASK_RUN_2026-09-03_NODE_H.md:5`; `RETURN.md` §2 second paragraph | Narrative currency | `EVIDENCE.md:106` says "the retained runs predate that line" — true of the two round-1 trees, not of `run-head-e59efa483-round2/` (whose `cleanup.txt:4` has it). The DRAFT `TASK_RUN` Evidence list and the older `RETURN.md` §2 file list omit `run-head-e59efa483-round2/**` and `COMPARE_RESULT_round2.txt` (the new §2 paragraph above them lists both). Both are closeout-rewritten documents | "the round-1 retained runs predate that line"; add the two round-2 artefacts to the TASK_RUN list at closeout |

No BLOCKER. No MAJOR. No MINOR.

## Round-2 run tree consistency (`run-head-e59efa483-round2/`, 44 files)

- `premerge.machine-lines.txt`: `HARNESS_PREMERGE_STATUS=pass`, `HARNESS_PREMERGE_TEST_COUNT=8`, `HARNESS_SECTION9_STATUS=pass` 16 (`REPORT_ONLY=true`); `result.txt`: `premerge_exit=0`, `release_quality_exit=not-run`, `git_status_after=10 dirty paths` (identical to before); `premerge.stderr.log` empty.
- `section8-run/summary.json` and `stable/section8-latest-summary.json` both `pass` 8/8, SHA-256 `50391877…` (matches `EVIDENCE.md:73` and the bundle manifest); all 8 per-check logs `pass`; `cleanup/sessions.json` 7 cleaned / 0 failures; `generatedAt 02:05:29Z` lies between `harness API ready 02:05:27` and `premerge exit 02:05:36` in `driver.log`.
- Containment: daemon (`Electron 84252`) holds only `control.sock` (`srw-------`), runtime dir `drwx------`, no TCP socket before or after, only `node 84306` listens on 51842; `daemon.log` ends `desktop.shutdown.completed {"reason":"runtime-daemon-signal","exitCode":0}`.
- Teardown/cleanup: `daemon_process_tree_remaining=0`, both pids `alive=no`, socket absent, `port_51842_listeners_after_stop=0`; `user_data_removed=yes`, `harness_tmp_root_removed=yes`, `private_dir_removed=yes`, `checkout_leftovers=` present.
- `registration.redacted.json` retains only `projectId`, `clientId`, `tokenFile` (path), `manifestHash`; `harness-ready.json` `{"sessions":[]}`.
- Toolchain identical to round 1 (Node v24.18.0, Electron 43.2.0, Next 15.5.21, Vitest 4.1.10); `built-bundles.sha256` identical to the round-1 head run.
- Secrets/host scan: zero hits; only the declared scratch-worktree and `chirality-s8.*` paths (see H2-F2 for the `head=` line).

## Script review (`rerun-section8-local.sh`, 333 lines, read in full)

- **Manifest-in-teardown ordering:** `trap teardown EXIT` (`:152`) fires on `exit 0/70/71/72`, on the premerge/RQ exit at `:331–332`, and on any `set -e` abort after `:152`; `teardown` first does `set +e` (`:97`), so nothing inside it can abort before the manifest at `:148–150`. The write follows the last `log` call (`:145`), so `driver.log` is final when hashed; `RUN_ROOT/private` is deleted first (`:139`) and is outside the `find artifacts logs` set anyway. Both `artifacts/` and `logs/` exist from `:65` before the trap is armed, so the guard at `:148` is always true on a normal path. Verified empirically by the round-2 manifest (43/43 incl. `teardown.txt`, `cleanup.txt`, `driver.log`).
- **`set -e` / trap interplay:** no `return`/`exit` inside `teardown`; `local status=$?` captured before `set +e`; the `xargs shasum` subshell's status is not tested. Exit status of the script is preserved (the EXIT trap does not alter `$?` unless it calls `exit`, which it does not).
- **Fail-fast port check:** `:236–238`, before the `next dev` launch; `exit 72` with the trap handling `NEXT_PID` empty.
- **Scoped kill:** `:99–101` SIGTERM `$NEXT_PID` + direct children and `$DAEMON_PID`; `:105–111` wait; `:116` SIGKILL processes whose cmdline carries the disposable `--user-data-dir`; `:117–120` SIGKILL `$NEXT_PID` + direct children. No port-based kill (H2-F1, H2-F4 residuals are NOTEs).
- **mktemp guard:** `:69–74`, `:130`, `:133–137`.
- **`--use-mock-keychain`:** appears only at the disposable daemon launch (`:201`) and in the `environment.txt` record (`:177`) and comments; not applied to `next dev`, the CLI, or the wrappers.
- **No new defect** introduced: `shellcheck -S warning` clean; the removed `:295` write has no other reader; `USER_DATA_CREATED` is defined before any use under `set -u`.

## Verdict

**PASS** — H1-F1 FIXED (per-run manifests now written last in teardown, both round-1 manifests regenerated from byte-unchanged trees and verifying 56/56 and 43/43, a fresh round-2 run whose script-written manifest verifies 43/43, bundle manifest 161/161 pinning all three); H1-F2/F3 FIXED; NOTEs F4–F8, F10, F12 FIXED; F9 carried to closeout by coordinator decision D1; F11/F13 needed no change. Zero BLOCKER, zero MAJOR, zero MINOR; five new NOTEs (H2-F1..F5), none actionable before push — H2-F2 and H2-F5 are one-clause narrative corrections that can ride the closeout commit.
