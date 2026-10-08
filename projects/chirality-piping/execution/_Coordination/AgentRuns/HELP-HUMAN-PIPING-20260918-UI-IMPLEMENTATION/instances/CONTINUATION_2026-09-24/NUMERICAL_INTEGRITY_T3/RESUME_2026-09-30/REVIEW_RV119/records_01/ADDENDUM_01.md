# RV119 ADDENDUM_01: #1114's new head `8568fb2053` (the S-1 delta)

**Reviewer:** RV119, TASK (Type 2), for ROOT (HELP_HUMAN, Agent 0), the return path. No descendants. 2026-10-08 UTC.

**The request.** The coordinator asked me to confirm #1114's new head. Its rulings on my review are in RR "RV119 passes #1114 with S-1; the owner has ROOT's two hostname lines reworded (E-18); a run-time host screen; errata to E-16's account" (NUM `dc4ffdc7c8`). My sealed `REVIEW.md` (`ef2c9538…`) and `SHA256SUMS` are unchanged. This file, `SHA256SUMS.addendum_01` and `_run_records/addendum_01/` are new.

**Placeholders** as in REVIEW.md. H = `57f078b4c8` (the reviewed head); **H2 = `8568fb2053f6750e4d09aa00d1791f9f3757f7e1`** (the new head); N2 = NUM `dc4ffdc7c8d8d7adbefe05127c9c8817973e57be`; M = `f4358eb0be` (the PR's base); M2 = `0e62b8e36b` (main now, #1115). Host-name forms are described, never written.

## Verdict: **CONFIRMED** (PASS at H2; no blocking finding)

| Severity | Count |
|---|---|
| BLOCKING | 0 |
| SHOULD-FIX | 1 |
| NOTE | 2 |

All six requested confirmations hold. They are qualified by A-S1, on what stays public outside main.

| ID | Sev. | Path | Evidence | Remedy |
|---|---|---|---|---|
| A-S1 | SHOULD-FIX | The PR's first commit `57f078b4c8`; NUM's branch on origin; RR:15636, RR "Erratum E-16: …" and `REDACTION_E16/RECORD.md` | **The squash keeps the earlier form off main's tree and history. It does not keep it from being public.** `sgttomas/chirality` is a public repository.<br>- **#1114's first commit `57f078b4c8`** spells the earlier form in its two lines. GitHub serves that commit from the PR (`refs/pull/1114/head`'s history and the PR's commit list), and a squash leaves it there.<br>- **NUM's branch is pushed to origin** (tip `dc4ffdc7c8`; GitHub's activity log shows a push per NUM commit, including `592f487abe` at 02:20:10Z and `c8e54918cd` at 02:33:31Z, before E-16's redaction). Its history carries:<br>&nbsp;&nbsp;- the earlier form, from `592f487abe` until E-18;<br>&nbsp;&nbsp;- **E-16's 42 pre-redaction junit files** (`c8e54918cd`, an ancestor of the pushed tip), whose attribute is the network name;<br>&nbsp;&nbsp;- **E-10's pre-redaction files** (`bc37d43a0a`, also an ancestor).<br>- **So two statements hold only for main:** RR:15636 ("So main carries the form only inside that one regex"), and E-10's and E-16's "the original bytes stay only in NUM's history, which is never merged into main". Main's tree is as stated; what is publicly retrievable is wider.<br>- **The exposure is low.** The network name and home-path forms are already on main in older records, and only the earlier form is a new kind. But the owner chose "Redact my two lines" on ROOT's account, and that account did not say this. (`_run_records/addendum_01/public_history.txt`) | **Before the squash:** tell the owner that the earlier form, and E-16's and E-10's originals, stay publicly retrievable from NUM's pushed branch and #1114's first commit, whatever the squash does. Anything further is the owner's call.<br>**At the next RR append:** reword the "only in NUM's history" statements to say that history is public. |
| A-N1 | NOTE | WG:602 | **The work graph quotes owner words that RR does not record:** "I choose 1", for E-16's redaction. RR:15521 says only "The owner chose redaction in place on NUM (option 1 of three)", with no quotation, and neither RR nor `REDACTION_E16/RECORD.md` contains the phrase. Every other quoted owner phrase in WG's block, including "Redact my two lines" (RR:15636), is verbatim in RR (`owner_quotes_check.txt`). | Record the owner's words in RR at the next append, or drop the quotation marks in WG. |
| A-N2 | NOTE | `R/BRIEFS/B2C_REVISION_02.md:41`; RR:15640; WG's next safe action 3; RR:15598 | **Precision points; none changes a ruling:**<br>- **The reworded brief line** sends the reader to "the machine's earlier host-name form named in RR". After E-18, RR no longer names it; it describes it, and ROOT's private list holds the name.<br>- **E-18 (RR:15640) lists two records that cite the brief's old sha256 `d82dba65…`:** RR:15492 and I97's REVISION_02:5. Two more do: RV118's `ADDENDUM_02.md:9` and its `addendum_02/checks_addendum_02.txt:5`. The mapping covers them equally (`brief_hash_citations.txt`).<br>- **WG's next safe action 3** says #1114 "carries NUM's records through `96cf68289f`". With this delta it carries them through `dc4ffdc7c8`.<br>- **RR:15598** says RV109's 52 files screened clean "decompressed `.gz` … included". There is no `.gz` among them.<br>- **The leak check's count:** ROOT's "1,111 files" matches a run against main now (`0e62b8e36b`), where the two-dot diff also counts 2 of #1115's App v4 run records that H2 lacks. Against the PR's base `f4358eb0be`, the PR's own count is **1,109**. Both PASS. | The merge record states the base used for the leak check. The rest goes in the next RR append or WG touch. |

## 1. The delta is exactly NUM's `execution/` at `dc4ffdc7c8`: CONFIRMED

Evidence: `_run_records/addendum_01/delta_scope.txt`.
- **H2's only parent is H.** The PR is now two commits on M (`57f078b4c8`, `8568fb2053`). No commit of NUM's history is in H2's ancestry, and origin's branch = H2.
- **P/execution at H2 equals N2's** (tree `d44512e129…`).
- **Nothing outside `P/execution/` changed in H..H2** (0 paths), and `P/validation/portability_policy.json` is H's blob.
- **H..H2 is 56 paths: 53 A and 3 M, 0 D, all mode 100644.**
  - Added: RV109's ADDENDUM_01 to round 2 with its evidence (52 files), and the RV119 brief (`R/BRIEFS/RV119_RECORDS_PR8_REVIEW.md`, which RR:15594 cites as `62078533…`).
  - Modified: RR, WG and `R/BRIEFS/B2C_REVISION_02.md`.
  - **My own records are not in H2**, as RR:15658 says.
- **The whole PR (M..H2)** is 1,108 A and 2 M under `P/execution/`, plus the policy file: 1,111 paths, as GitHub reports.
- **Main's move to M2** (#1115) is 207 paths, all under `projects/chirality-app-v4/`. It shares no path with M..H2. CI's merge ref is M2 + H2. Main then moved again, to `7b0170ed4d` (#1116: 27 App v4 files, nothing under P).

## 2. The earlier host-name form, across the whole PR: CONFIRMED for the PR's net content (A-S1 for its history)

The form is read at run time from **RR at H** (the reviewed head's "Screen widened" line), so no file of mine carries it. The scripts take that rev as their last argument.
- **Plain form:** 0 lines in M..H2. That covers every added file in full, all 156 `.gz` files decompressed, and the `+` lines of RR, WG and the policy file. Its domain alone also gives 0 (`whole/publication_scan_summary.txt`, `whole/gz_check.txt`).
- **Split, escaped or character-class forms** (`whole/host_variants_scan.txt`): exactly 1 line, **I90's `_run_records/repair_02/scripts/write_records_r2.sh:35`**. It is the only hit for the full form with any joiners and for the split domain. Its first-name and laptop-model split forms are on the same line.
- **H2's RR and brief** contain the form nowhere, in any case (`e18_check.txt`).
- **ROOT's report agrees:** its run-time screen's one earlier-form hit on the whole PR is the same regex.

**The rest of the host screen on M..H2:**
- the network name, the local host name and the computer name: 0;
- the strict pattern: 1, B2W_B3W_PROBES.md:59, registered by E-17;
- the junit `hostname` attribute: 0 in any junit document, and 13 text lines (rule text and RV117's records), as at H;
- the laptop-model form: 8 rule-text lines (RR:15286, the owner's words; RR:15500 and :15530; WG:572; REDACTION_E16 RECORD:22; RV117's two script patterns; and the RV119 brief:31);
- the dot-local suffix: 24 lines, all product identifiers or rule text.

**The delta alone** (`delta/`):
- 6,378 lines, with 0 hits for credentials, e-mails, names, host names, the strict pattern, machine paths, IPs or MAC addresses;
- 1 laptop-model rule-text line (the RV119 brief:31) and 2 dot-local rule-text lines (B2C_REVISION_02:41, the RV119 brief:32);
- 0 `.gz` files and 0 split forms other than the brief's rule text.

## 3. E-18's two rewordings: CONFIRMED (A-N2 for two citations)

Evidence: `e18_check.txt`, with old and new lines printed with the host forms masked.
- **RR: exactly one line changed**, H:15496 = H2:15496. Everything else in H's RR is unchanged, and 79 lines are appended after H's end (15581 → 15660 lines).
  - **Main's RR is still an exact byte prefix of H2's.** Line 15496 is past main's 14,962 lines, as RR:15639 says, and E-2's precedent (RR:12036) is as cited.
  - RR's sha256 goes `cba01040…` → `137c622b…`.
- **The brief: exactly one line changed** (41). Its sha256 goes **`d82dba65f45a…` → `d1d213d8d27e…`**, as E-18 records.
- **The meaning is unchanged:**
  - **RR:** "any [laptop-model] form" becomes "the laptop-model form", and the spelled-out earlier form becomes "the machine's earlier host-name form", with a pointer to ruling 4.
  - **The brief:** the list becomes "the machine's earlier host-name form …, its network name, and the laptop-model form". Naming the network name only makes explicit what the laptop-model term already caught, since the network name contains that form.
  - The screen's terms are the same set.
- **No other file present at H changed** (the only non-added changes are RR, WG and the brief).

## 4. The new RR sections and WG lines (N-1, N-2): CONFIRMED (A-N1, A-N2)

**RR:15583–15660** (3 sections):
- **"Records PR #1114 opened; …"** matches the PR at H and my review's §1.
- **"RV109 confirms SP's I3 step; …"** matches RV109's ADDENDUM_01: `f065a1f6…`; 0/0/2; 51 sums; 124 of 132 probe rows; 86 hex pins.
  - Its PP Stale 568/5 → 575/1 is RV109's `--lib` count. ADDENDUM_01:107 says so; I85's 731 → 738 counts all targets.
- **"RV119 passes #1114 with S-1; …"** matches my review: `ef2c9538…`, 67 of 67, 0/1/3. "228 citations" = 88 + 67 + 73.
  - **E-18 and the N-2 errata are exact:** RV76's path is home-rooted absolute and registered; I91's five junit files sit three in `suites/` and two in `repair_01/suites/`.
  - **N-3 is routed to the squash body.**
- **The citations resolve:**
  - 12 hash citations: 8 match files at H2. The others are my REVIEW.md (untracked in NUM, its hash `ef2c9538…` correct, to reach main with the next records PR) and the brief's old hash (verified at H). WG:569's two canonical H values were checked in my review.
  - 33 of 34 paths resolve; the missing one is my REVIEW.md, for the same reason.
  - 77 of 79 quotations resolve to headings; the other 2 are not heading citations.

**WG** (`wg_delta.diff`, `owner_quotes_check.txt`). N-1's points are addressed:
- **The position header** reads 2026-10-08.
- **The T3-B1/B6 row** says I85 landed the I3 step at `03f55e7178`, RV109 confirmed it, and SP is complete.
- **The estimate** now says that B3-D's and B2-C's revisions and option (ii) add to the PLAN figure.
- **The owner-held list** gains the cleanup of main's historical host-name exposure.
- **The owner decisions in force** gain the 2026-10-08 host-name redactions. Their "I choose 1" is A-N1.
- **The rulings in force** cite every 2026-10-08 section, from "I90's SR-RS repair round 2 verified; …" to "RV119 passes #1114 with S-1; …".
- **Running:** RV113 and RV119; RV109 is idle; **the next unused IDs are I100 and RV120** (RV119 is used).
- **The only line stale at N2** is next safe action 3's "through `96cf68289f`" (A-N2).

## 5. RV109's ADDENDUM_01: CONFIRMED

- **The sums verify:** `SHA256SUMS.addendum_01` is 51/51 OK. Round 2's sealed `SHA256SUMS` is 125/125, and its REVIEW.md is unchanged. The folder has 178 files, all covered (`sums_folders.tsv`). I85's `SHA256SUMS.i3_01` is 120/120.
- **The whole PR at H2** has 29 added sum files, 1,065 entries, all OK (`sums_committed_tree.tsv`).
- **The screens are clean** in text: all 52 files, 0 hits for credentials, names, e-mails, host names (plain and split), the strict pattern, machine paths, IPs or process data.
  - **There is no `.gz` file** among them, so nothing needed decompressing.
  - **The lock log** (`cargo_jobs_rv109_a1.log`, 75 lines) is RV109's own lines only: `WT/rv109/a1_head`, `a1_i3` and `a1_mut` (`delta/lock_log_cwds.txt`).
  - There are no links, no `build` folder, nothing ignored, and NUM's disk matches N2's tree (178 files). The largest file is 230,862 B.
- **The redacted originals are still absent at H2:** E-16's 42, E-10's 47 and REDACTIONS.json's 13 (`whole/redactions_*.txt`). `rvr_sr_py_01/SHA256SUMS` is 245/245.

## 6. Gates at H2

| Gate | Evidence | Result |
|---|---|---|
| GEN-8 (RV119) | `WT/rv119`, a detached worktree of H2, through `WT/tools/t3_slot.sh` (slot 2): **1 passed, 10 deselected in 32.85s**, exit 0. HEAD was H2 before and after, with 0 status entries (`gen8_pytest.log`, `gen8_prepost.txt`) | **pass** |
| `validate_run_record_leaks.py` (RV119) | `--base f4358eb0be --head 8568fb2053`: PASS, 1,109 files, 0, 0, one 8.1 MB warning. The delta alone (`--base H`): PASS, 55 files. Against M2: PASS, 1,111 (A-N2) | **pass** |
| governance-harness | 37724855363, on the merge ref `1f8846377c` (parents M2 and H2), with `CHIRALITY_REQUIRE_LIVE_TESTS: 1`: "1161 passed, 48 subtests passed" | **success** |
| Harness Pre-merge Validation | 37724855268 | **success** |
| pec-tests | 37724855435 | **success** |
| Piping Desktop E2E | 37724855398: Select source coverage, the Numerical cargo suite and Desktop E2E (source mode) succeeded (completed 04:22Z); remainder and accessibility skipped by selection (`ci_runs_H2.txt`) | **success** |

## What ROOT must rule on

1. **A-S1, before the squash:** tell the owner that the earlier form, E-16's 42 originals and E-10's originals stay publicly retrievable from NUM's pushed branch and #1114's first commit. Whether anything more is done is the owner's call. Then reword the "only in NUM's history" statements at the next RR append.
2. **The merge, unchanged in form:**
   - check main: it moved again during this addendum, to `7b0170ed4d` (#1116: 27 files, all under `projects/chirality-app-v4/`, nothing under P). The PR is MERGEABLE and CLEAN against it;
   - `gh pr merge 1114 --squash --match-head-commit 8568fb2053f6750e4d09aa00d1791f9f3757f7e1`, with N-3's squash body;
   - the merge record carries GEN-8 at H2, the leak check with its base named (A-N2), and H2's CI run IDs.
3. **A-N1 and A-N2:** the next RR append and WG touch.

## Host and method

- **My copy:** a detached worktree of H2 at `WT/rv119`, created from NUM's repository and removed at the end with its registration. I wrote nothing in it. Logs are in `WT/scratch/rv119_records_01/`, with `TMPDIR` there.
- **What I ran:**
  - one GEN-8 pytest through `t3_slot.sh`, with one wait (its completion notice, after the job's process had gone);
  - three `validate_run_record_leaks.py` runs in my copy;
  - read-only VENV Python scans with `PYTHONDONTWRITEBYTECODE=1`;
  - read-only Git with `GIT_OPTIONAL_LOCKS=0`;
  - `gh` reads (the PR, CI runs and one job log, commit and branch-activity API reads, and the repository's visibility);
  - one background wait on the E2E run's completion, which ended when that run completed.

  No cargo, no install, no other test, and no Git write beyond my worktree. No process or wait of mine remains.
- **The earlier form** is read at run time from RR at H, the reviewed head, never written.
- **The scripts** are in `_run_records/addendum_01/scripts/`. They are my REVIEW's scripts, with an optional last argument naming that rev, plus `e18_check.py`.
- **Records:** this file, `SHA256SUMS.addendum_01` and `_run_records/addendum_01/`. They were screened with my `self_screen.py` before return, with 0 hits. There are no links, no `build` folder, no `.gz` and no junit output, and `git status --ignored` shows nothing ignored.
