# RV119: independent review of the T3 records-only PR after #1111 (#1114)

**Reviewer:** RV119, TASK (Type 2), dispatched directly by ROOT (HELP_HUMAN, Agent 0). ROOT is the return path. No descendants. I wrote none of these records. 2026-10-08 UTC.

**Brief:** `R/BRIEFS/RV119_RECORDS_PR8_REVIEW.md` (sha256 `62078533…`, verified before use), read in full. Its method is `R/BRIEFS/RV103_RECORDS_PR4_REVIEW.md` items 1–6 with the brief's substitutions and its item-3 to item-5 checks. Precedents read first: RV117's brief and `REVIEW.md` (#1111), RV110's brief and records (#1108), then RV103's brief. `R/BRIEFS/B1_COMMON.md` (`2d170307…`) and the strict pattern as RV117's scripts assemble it.

**Placeholders.** WT = the t3 workspace; NUM = WT/numerics; P = `projects/chirality-piping`; T = P/execution/…/NUMERICAL_INTEGRITY_T3 (written `T3/` in the run records); R = T/RESUME_2026-09-30; RR = T/ROOT_RULINGS_V1.md; WG = P/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md; VENV = the piping venv's Python 3.13.14. `RR:n` and `WG:n` are line numbers at the PR head. Host-name forms are described, never written: "the network name", "the laptop-model form", "the earlier form" (the one RR:15496 names) and "the dot-local suffix".

**NUM moved after N.** At dispatch NUM was `7e6a5ba7ea` (#1114 opened; this brief). During the review it moved to `180314cf18` (RV109 confirms SP's I3 step). Neither is in #1114. Every check below is against N = `96cf68289f` and the PR head H.

## The candidate

| Item | Value |
|---|---|
| PR | #1114, `codex/piping-t3-records-20261008` → `main`, ready (not draft), MERGEABLE, merge state CLEAN after CI |
| H (head) | `57f078b4c8a87756d3d0985f58a67e15bbeda476`, one commit, sole parent M; origin's branch = H |
| M (base, main) | `f4358eb0be945bc98677d05b526bb4a1b0b1d5cf` (#1113's merge, App v4); origin's main is still M |
| N (source, NUM) | `96cf68289fbac2fe3f4919d1b2e55bcfa0a2b6cd` |
| Author and committer | the owner's configured Git identity; the only other identity is the agent co-author trailer |

## Verdict: **PASS** (no blocking finding)

| Severity | Count |
|---|---|
| BLOCKING | 0 |
| SHOULD-FIX | 1 |
| NOTE | 3 |

The following pass:
- **Scope.** H is M plus one commit, not from NUM's history. **P/execution at H equals N's** (tree `4619994e3d…`), and so does the policy file. 1,058 paths change: **1,055 A and 2 M under `P/execution/`, 0 D**, plus `P/validation/portability_policy.json` (M). The modified execution paths are exactly RR and WG. H differs from N only by #1113's 209 App v4 paths, which main gained after NUM's merge base `0b6c5d7362`; #1113 touches nothing under P. No open product PR shares a path with H.
- **Publication screen.** No credentials, whole-host data, binaries or large files; no symlink; no `build` folder. Main's `validate_run_record_leaks.py` passes on M..H (1,056 files; 0 credentials; 0 machine-local symlinks; one size warning, 8.1 MB). **All 156 `.gz` files decompress, parse and screen clean,** and none of their 44 junit documents has a `hostname` attribute. The network name, the local host name and the computer name occur nowhere in the PR. **S-1:** the earlier host-name form is new to main.
- **E-16, E-10 and the 13 originals.** E-16's 42 old sha256s are absent; each file has its new sha256 and differs from its original only by the removed attribute (whose value was the network name). `rvr_sr_py_01/SHA256SUMS` is 245/245 and REVIEW.md is `d8611e59…`, unchanged. None of E-10's 47 pre-redaction blobs and none of REDACTIONS.json's 13 originals is in H.
- **E-17.** The policy file's only change is the two appended entries (+16/−0); each path exists at H with the registered sha256, with the roles RR rules (CONTROL for the brief, EVIDENCE for RV117's review).
- **Portability.** GEN-8 passes on the exact head (1 passed, 10 deselected). No machine-absolute path is in the changed files beyond B2W_B3W_PROBES.md's screen pattern, which E-17 registers.
- **Integrity.** All 28 sum files the PR adds verify in the committed tree (1,014 entries), and so do the 12 on main in the same folders (40 files, 1,523 entries). The superseded sealed files are byte-unchanged since their first commit. RR is append-only.
- **Gates.** The four automatic CI runs succeeded on H.
- **The living documents.** #1111's squash, #1112's merge and NUM's two absorbs; the 22 appended RR sections (88 hash citations, 67 path citations and 73 heading citations all resolve); the I3 step and the three readers' rounds (branch facts and the nine transport changes recomputed from the census files); B2-C's path to final for J1; the next unused IDs (I100 and RV119). **ROOT took no owner-held decision, and every owner quotation is verbatim.** WG lags RR in places (N-1).

Nothing blocks the squash. S-1 needs ROOT's ruling before it.

## Findings

| ID | Sev. | Path | Evidence | Remedy |
|---|---|---|---|---|
| S-1 | SHOULD-FIX | RR:15496; `R/BRIEFS/B2C_REVISION_02.md:41`; `R/I90/b1_sr_rs_01/_run_records/repair_02/scripts/write_records_r2.sh:35` | **The PR publishes the machine's earlier host-name form on main for the first time.**<br>- **RR:15496** ("Screen widened (E-16 …)") and **B2C_REVISION_02.md:41** (its host rules) spell it out literally as a screen term. **I90's `write_records_r2.sh:35`** carries it in character-class form, in I90's own screen pattern.<br>- **Main carries it nowhere**, in any form (`host_variants_scan.txt`, `main_host_exposure.txt`). RR's E-16 calls it "the machine's other host-name form", and ruling 4 has a record carrying the machine's full host name redacted before its first commit.<br>- **The brief's test:** pattern or rule text is acceptable, and a machine datum is not. These three lines are both. ROOT's PR body files them under "pattern or rule text". I judge the text itself a machine datum. Its sensitivity is low: a generic machine label and a home-network domain, with no personal name.<br>- **A gap in the literal screens:** the same line of I90's script also spells the local host name's first-name prefix and the laptop-model form split by quotes and brackets, and the home root split by quotes. A literal host-name screen misses them (my literal terms find 0 there); only an owner-name pattern and a split-form scan find them. That exposure (the network name) is already on main in 12 text files and I91's five junit `.gz`, so it adds no new kind. (`publication_hits.tsv`, `host_variants_scan.txt`) | **A ruling before the squash**, one of:<br>(a) **accept** the three lines as screen text, recording that main gains the earlier form; or<br>(b) **redact them in place on NUM** by E-16's method before the merge. That would be the owner's call, as E-16's was.<br>**From now on:** describe the earlier form, as RR:15530 does, and add a split-form check (for example `scripts/host_variants_scan.py`) to the commit-time screen. |
| N-1 | NOTE | WG:548, WG:582 (T3-B1/B6), WG:583 (T3-B2/B3/B4), WG:589–598 (owner-held), WG:600–614 (owner decisions), WG:621–677 (rulings in force) | **WG's T3 section lags RR at N where RV117 N-1's ruling does not reach.** That ruling covers positions, the next IDs and the next safe action, and those are current. The rest is not:<br>- **Rulings in force** cite none of the nine 2026-10-08 sections from RR:15329 to RR:15541:<br>&nbsp;&nbsp;- E-15;<br>&nbsp;&nbsp;- the census rule with the nine transport changes, and TS's G3 conjunct to G8;<br>&nbsp;&nbsp;- the restated rule for jobs in flight at a host change;<br>&nbsp;&nbsp;- SA3-1's option (ii), and A-1's formation in B2-K;<br>&nbsp;&nbsp;- B2-C final for J1, with SA4-1, B-2 and B-1 routed;<br>&nbsp;&nbsp;- E-16's widened screen and its stop rule;<br>&nbsp;&nbsp;- E-17 (briefs never spell out the strict pattern).<br>- **The T3-B1/B6 row** still says "At I3, I85 lands W-C2's pins, SF-1 … and SF-2". The position bullets and RR:15404 record that step as done.<br>- **The position header** reads "(2026-10-07 UTC)".<br>- **"About 206–329 h agent"** (T3-B2/B3/B4) predates three changes: B3b's +3–4 h (RR:14861), B2-C's +12–19 h (RR:15079) and B2-K's +2.5–3.5 h (RR:15507).<br>- **The owner-held list** lacks the cleanup of main's tree (RR:15055, RR:15534).<br>- **The owner decisions in force** lack E-16's redaction-in-place choice (2026-10-08).<br>(`wg_staleness.txt`) | At the next WG touch. Consider extending ruling 1 to the rulings-in-force list. |
| N-2 | NOTE | RR:15534 and `IMPLEMENTATION/REDACTION_E16/RECORD.md` ("Main's earlier records"); RR:15538 | **E-16's account of main's exposure has two precision slips:**<br>- **"one home-relative path in RV76's REVIEW.md":** the path on main (`REVIEW_RV76/summary_coverage_01/REVIEW.md:5`) is home-rooted absolute. It has no home-relative form, and it is registered in the portability policy. The same line carries the network name; it is one of the 11.<br>- **RR:15538** places I91's five junit `.gz` files in `R/I91/b1_sr_py_01/_run_records/suites/`. Three are there, and two are under `_run_records/repair_01/suites/`, as RV117 N-4 listed them.<br>The counts hold: 11 T3 text records plus one App runtime record carry the network name, and the five `.gz` files carry the attribute. (`main_host_exposure.txt`) | One RR erratum at the next append. If the owner was told "home-relative", correct that too. |
| N-3 | NOTE | PR #1114 description (`_run_records/pr1114_body.md`) | **Two wording points:**<br>- **"every remaining hit is pattern or rule text, or an already-redacted placeholder."** It leaves out the owner's own words: RR:15286 quotes the owner naming the hardware model, a category RR:15539 itself lists. It also files the earlier form under pattern text (S-1).<br>- **"the I3 step: I85's SP pins and the nodal-term ordinal fix, with RV109's round 2."** RV109's round 2 reviewed SP at `603e238517`, before I3. RV109's confirmation of the I3 step is after N and not in this PR.<br>**The rest is accurate:**<br>- the counts, 1,055/2/0 plus the policy file;<br>- the two merge records; I85's I3 step; the three readers' rounds; RV113's SR-PY and SR-TS reviews and its SR-RS ADDENDUM_01; SC's brief;<br>- I97's contract and revisions 01–02, with RV118's review and addenda and RV115's addenda 02–04;<br>- I98 and I99; RV111's ADDENDUM_02–04; RV117's review;<br>- E-15 (8 `out/` files), E-16 and E-17;<br>- "Not in this PR";<br>- the screening, leak-check and GEN-8 claims.<br>The commit message is accurate. | Word the explicit squash body to match. Keep the agent co-author trailer. |

## 1. Scope: PASS

Evidence: `_run_records/scope_checks.txt`, `changed_paths_name_status.tsv`, `added_by_folder.txt`, `pr1114_view.json`, `pr1114_body.md` and `open_prs.txt`.

**Parentage:**
- H's only parent is M, and `rev-list --count M..H` = 1. `ls-remote`: main = M, and the PR branch = H.
- H is not an ancestor of N. **None of NUM's 892 commits in `M..N` is in H's ancestry.**
- NUM's merge base with main is `0b6c5d7362` (#1112's merge). Main then moved only by #1113 (`f4358eb0be`, 209 App v4 paths, 0 under P), as RR's "Records PR #1114 opened" (after N) says.

**Equality with NUM:**
- **P/execution at H equals N's** (`4619994e3d…`), and `portability_policy.json` at H equals N's (`5bff4b2498`).
- `git diff N H` lists only #1113's 209 App v4 paths. So H = M + N's P/execution and policy file.

**Changed paths** (`git diff --no-renames M H`):
- **1,058 paths:** 1,055 A and 2 M under `P/execution/`, and 1 M under `P/validation/`; 0 D. GitHub reports 1,058 files, +490,110/−29.
- **Modes:** 1,042 regular and 16 executable: RV109's seven tools, RV113's seven SR-PY harness scripts, and I98's and I99's run scripts. **No mode `120000`,** and no link under P/execution at H.
- Added by folder:

  | Folder (T-relative) | Files |
  |---|---|
  | `IMPLEMENTATION/RECORDS_MERGE_2026-10-07C/` | 7 |
  | `IMPLEMENTATION/REDACTION_E16/` | 2 |
  | `IMPLEMENTATION/SI1C_MERGE/` | 29 |
  | `R/BRIEFS/` (B1_SC, B1_SP_I3, B1_SR_PY_REPAIR_02, B1_SR_RS_REPAIR_02, B1_SR_TS_REPAIR_01, B2C_CONTRACT, B2C_REVISION_01, B2C_REVISION_02, B2W_B3W_PROBES, RV117, RV118) | 11 |
  | `R/I85/b1_sp_01/` (I3_01) | 121 |
  | `R/I90/b1_sr_rs_01/` (repair 02) | 76 |
  | `R/I91/b1_sr_py_01/` (repair 02, item 4) | 101 |
  | `R/I92/b1_sr_ts_01/` (repair 01, item 3) | 51 |
  | `R/I97/b2_c_01/` | 35 |
  | `R/I98/b2_w_probe_01/` | 63 |
  | `R/I99/b3_w_probe_01/` | 39 |
  | `R/REVIEW_RV109/rvp_round2_01/` | 126 |
  | `R/REVIEW_RV111/si1c_01/` (ADDENDUM_02–04) | 23 |
  | `R/REVIEW_RV113/rvr_sr_py_01/` | 246 |
  | `R/REVIEW_RV113/rvr_sr_rs_01/` (ADDENDUM_01) | 10 |
  | `R/REVIEW_RV113/rvr_sr_ts_01/` | 32 |
  | `R/REVIEW_RV115/b2_kd_01/` (ADDENDUM_02–04) | 15 |
  | `R/REVIEW_RV117/records_01/` | 46 |
  | `R/REVIEW_RV118/b2_c_01/` | 22 |

**The modified paths:**

| Path | Main blob → head blob | Change | Lineage |
|---|---|---|---|
| RR | `0eec737e55` → `2de0290b2e` | +619 / −0 | Byte prefix (§5) |
| WG | `5d0107fce6` → `a2ca26598d` | +41 / −29 | Main's blob = NUM's at `0b8299e496` (#1111's delta), and main last touched it in `54f1ba1f6d`. **No change of main's is reverted** |
| `P/validation/portability_policy.json` | `9fb269d2a0` → `5bff4b2498` | +16 / −0 | E-17's two entries only (§3) |

**A1-S-1 (no open product PR's package):** the only other open PR is #885 (a draft from 2026-09-24, not T3's), which shares 0 of its 100 paths. No T3 product PR is open, and no `IMPLEMENTATION/` package of an unmerged slice is in H.

## 2. Nothing that must not be published: PASS (S-1 for ROOT's ruling)

**What the screen covers:** every line of the 1,055 added files, including the decompressed contents of the 156 `.gz` files, and the `+` lines of RR, WG and the policy file. That is 533,148 lines, screened with RV117's patterns plus the brief's terms, assembled at run time in my scripts:
- the strict pattern of B1_COMMON;
- the network name, the local host name and the computer name, read at run time;
- the laptop-model form, case-insensitive;
- the earlier form, read from RR at H;
- the dot-local suffix;
- the junit `hostname` attribute.

Evidence: `_run_records/publication_scan_summary.txt` and `publication_hits.tsv` (host data written as placeholders, home roots hyphenated); `host_variants_scan.txt`, `extra_host_scan.txt`, `token_shape_scan.txt`, `gz_check.txt`, `leak_validator.txt`, `lock_log_cwds.txt`, `size_type_summary.txt` and `size_ignored_checks.txt`; with `scripts/`.

**Credentials: none.**
- **Token-shaped patterns** over every changed file in full, `.gz` decompressed, find **0** of each: GitHub tokens, `github_pat_` bodies, `sk-` keys, AKIA keys, PEM blocks, password and token values, Authorization values, Slack tokens and JWTs.
- **Main's `validate_run_record_leaks.py --base f4358eb0be --head 57f078b4c8`**, run in my copy: "PASS: 1056 changed run-record file(s) scanned; 0 possible credential(s); 0 machine-local symlink(s)", exit 0. 1,056 = the 1,055 added files plus RR. Its one WARN is the 8.1 MB `REVIEW_RV113/rvr_sr_py_01/evidence/probes/probes_v5.json` (8,081,676 B), under the 50 MB limit.
- **The name-pattern hits** are all scan vocabulary in RV117's records (its scripts and summaries).

**The 156 gzipped files** (2 of I91's, 154 of RV113's SR-PY evidence; `gz_check.txt`):
- every file decompresses (0 failures);
- each parses by type: 44 junit XML, 74 JSON Lines and 38 text;
- across their 43,038 lines, **0 hits** for home or temp paths, e-mails, token shapes, credential words, any host name (run-time names and the earlier form), the laptop-model form, the dot-local suffix, other host data, the `hostname` attribute, the strict pattern and the owner's name;
- **0 of the 44 junit documents carries a `hostname` attribute.** That includes I91's two new junit files and E-16's 42.

**Host data (the brief's host screen):**

| Term | Hits | Judgement |
|---|---|---|
| The network name, the local host name, the computer name | **0** | — |
| The laptop-model form | 9 lines in 6 files | Rule text in RR:15496, :15500, :15530, WG:572, REDACTION_E16 RECORD:22 and B2C_REVISION_02:41; RV117's two script patterns; **RR:15286, the owner's quoted words** (naming the hardware model). **Acceptable** |
| The earlier form | 2 lines (RR:15496, B2C_REVISION_02.md:41), plus 1 character-class line in I90's `write_records_r2.sh:35` | Rule or pattern text whose content is the machine datum, **new to main: S-1** |
| The dot-local suffix | 23 lines in 14 files | The product schema's `$id` in I97's statics (a product domain, accepted at RR:15063); RV113's sanitizer, which maps a tool-install folder under the home's dot-local directory to a placeholder; and rule text (briefs, RR, WG, I85's screen script, RV118's addendum, RV117's records). **Acceptable** |
| The `hostname` attribute | 13 lines in 4 files, all text | REDACTION_E16's rule text; RV117's REVIEW N-4, its hits file (written `<host>`) and its script pattern. **No junit document carries it** |
| Split forms (quotes, brackets or joiners inside a host name) | 1 line (I90's `write_records_r2.sh:35`) | The earlier form, the local host name's first-name prefix, and the laptop-model form, in I90's own screen pattern. **S-1** |

**Personal data: the owner's configured Git identity only.**
- **The owner's e-mail** occurs on 4 lines, in I91's two `commits.txt` (git log output of its own commits: `repair_02/diff/` 3, `repair_02_item4/diff/` 1). That is the configured Git identity, which the brief allows, and main already carries it in 3 T3 files.
- **The owner's name** occurs as the Git author in those files and in RV117's `pr1111_view.json`. It also occurs, split, in I90's screen pattern (S-1).
- The only other address is the agent's no-reply attribution.

**Whole-host data: none.**
- **0** UUIDs, tool-call or message ids, session ids, transcript paths, private IPv4 or MAC addresses, URL-encoded or Windows home roots, keychain paths, or process-table headers. The only session-id, transcript, process-header and application-folder hits are RV117's own scan patterns.
- **`pgrep` occurs only in memguard and lock-count checks** whose output goes nowhere or is only counted (I85, I90, I98 and I99 scripts; B2W_B3W's host rule).
- "slack" (RV115 ADDENDUM_03, RV112's words quoted by RV117) is the word, not the application.
- **The 10 lock-log excerpts are each agent's own lines** (`lock_log_cwds.txt`). I85: `WT/b1` and `WT/scratch/i85_b1_st`; I90: `WT/b1-r` and its scratch; I91: `WT/b1-p` and its scratch; I98 and I99: their own archive (`ARCH`); RV109: `WT/rv109/…`; RV113: `WT/rv113/…`.
  - Three of I91's item-4 lines have `cwd=WT/scratch/root_si1c_pr`. They are I91's own census job, whose cwd was its session's working folder, as the log's own header says.
  - There is no other agent's line and no process listing.
- **RR:15322 names two memory-guard PIDs** (ROOT's own guard processes). That is not a process listing. Acceptable.

**Size and type** (`size_type_summary.txt`, `size_ignored_checks.txt`):
- **The sizes:** the 1,058 changed files total 31,373,904 B. The largest are `probes_v5.json` (8,081,676 B), RV113's two SR-TS vitest logs (about 1.49 MB each) and RR (1,349,177 B). **No file is over 50 MB**, and one is over 2 MB.
- **The types** (`file --mime-type`): 651 plain text, 156 gzip, 151 JSON, 45 shell, 32 Python, 17 diffs, 1 CSV, and 5 sources misread as Algol or Java. No other binary.
- **No build output** (no `target/`, `node_modules/`, `dist/`, `__pycache__`, `.pyc`, `.so`, `.wasm`, `.dylib`, `.rlib` or object file) and **no path component named `build`**.
- **Nothing ignored is left behind** in the PR's added folders (`git status --ignored` in NUM: 0 `!!` entries in each). The added folders I counted on disk match N's tree file for file. NUM's working tree under T holds:
  - 202 symlinks, all in RV56's two ignored `imported/` folders (known, untracked, not in H);
  - RV113's two untracked addenda (SR-RS ADDENDUM_02, SR-TS ADDENDUM_01), which "Not in this PR" names.

## 3. Portability and the brief's item-3 checks: PASS

**GEN-8 by E-4's method** (`_run_records/gen8_pytest.log`, `gen8_prepost.txt`):
- My own detached worktree of H at `WT/rv119` (created for this review and removed after it), read-only: `PYTHONDONTWRITEBYTECODE=1`, `GIT_OPTIONAL_LOCKS=0`, `-p no:cacheprovider`, `TMPDIR` in my scratch. It ran through `WT/tools/t3_slot.sh` (slot 3).
- HEAD was H before and after, with 0 status entries (including ignored) before and after.

  ```
  WT/tools/t3_slot.sh env TMPDIR=… VENV -m pytest -q -p no:cacheprovider -rA tools/practitioner_harness/test_live_baseline.py -k gen8
  ```

- **The result: 1 passed, 10 deselected in 36.77s**, exit 0, 02:50:55–02:51:32Z.

**No symlink:** 0 mode-`120000` entries in M..H, and 0 links under P/execution at H. The tree's only 2 links are main's, under `execution/_Evaluation/`, outside the PR.

**Machine-absolute paths** in the 1,058 changed files (`abs_paths_by_file.tsv`, `.gz` decompressed; GEN-8's own detector and a broad pattern):

| Check | Result |
|---|---|
| GEN-8's detector (`surface_roles.iter_machine_path_lines`), added lines | 11 lines, none a machine path:<br>- B2W_B3W_PROBES.md:59, the strict pattern, registered by E-17;<br>- RV117's REVIEW.md:154, quoting temp snippets, registered by E-17;<br>- four mutant drivers of I91 and I92, which build a temp folder from the agent's scratch variable;<br>- five lines of RV117's own `abs_paths_by_file.tsv` samples.<br>GEN-8 passes |
| Broad pattern | 2 more lines: RR:15579's text quoting the temp snippets (E-17), and one more sample line in RV117's records |
| **Machine-absolute paths in total** | **0** |

**The living documents carry none:** RR's 619 appended lines, WG's diff and the 11 briefs. B2W_B3W_PROBES.md spells out the strict pattern, and E-17 registers it as an as-issued CONTROL brief. No other brief, and nothing in RR's or WG's added lines, matches the strict pattern.

**E-16's redaction** (`redactions_e16_check.txt`; pre-redaction rev `c8e54918cd`):
- The RECORD's table has 42 rows. Each blob at `c8e54918cd` hashes to its old sha256 (42/42), and each H blob to its new sha256 (42/42).
- **Each of the 42 parses as XML and carries no `hostname` attribute.** Each decompresses to its original with exactly one `hostname` attribute removed and nothing else changed (42/42). At `c8e54918cd`, all 42 attribute values were the network name, so E-16's description is exact.
- **0 pre-redaction blobs** are in H's or M's tree. 0 of the 240 `.gz` files under T at H, and 0 of the 1,058 changed files, hash to an old sha256.
- **`rvr_sr_py_01/SHA256SUMS` at H is 245/245 OK**, and it lists all 42 new sha256s. It differs from the pre-redaction file in exactly 42 lines. **REVIEW.md is `d8611e59f67f…` at H and at `c8e54918cd`.**
- The RECORD's own sum file verifies (`e3af69ba…`, as RR:15527 cites).

**E-10's originals** (`redactions_e10_check.txt`, RV117's script; pre-redaction rev `bc37d43a0a`):
- REDACTION_01's tables list 50 files. The 47 committed at `bc37d43a0a` hash there to the old sha256, and all 50 of H's blobs hash to the new sha256.
- **0 pre-redaction blob ids are in H or M**, and 0 changed files hash to any old sha256, which covers the three never committed.

**REDACTIONS.json's 13** (`redactions_check.txt`): each original at `dfa5e2dc44` matches its `original_sha256`, and each H blob its `redacted_sha256`. 0 originals are in H's tree (68,532 distinct blobs) or M's, and 0 changed files hash to an original.

**E-17's portability entries** (`e17_policy_check.txt`):
- M's two lists are exact prefixes of H's: `control_path_exceptions` 92 → 93 and `historical_role_overrides` 740 → 741. Nothing else in the file changed (parsed equality, and numstat +16/−0).
- **`T3/RESUME_2026-09-30/BRIEFS/B2W_B3W_PROBES.md`:** a `control_path_exception`, role **CONTROL**, sha256 `b7e2fdc726f8…`, which equals H's bytes.
- **`T3/RESUME_2026-09-30/REVIEW_RV117/records_01/REVIEW.md`:** a `historical_role_override`, role **EVIDENCE**, sha256 `fb368f741d15…`, which equals H's bytes (and RR:15030's `fb368f74…`).
- **Both authorities cite RR's heading verbatim** ("RV115 and RV118 confirm B2-C revision 02: …; E-17 and two portability registrations", RR:15541), with the owner's standing authorization and the #1084 and `f9ff31f163` precedents, as the section states. The roles and entry types match it.
- **E-17's two reasons are exact:** my scan finds the strict pattern at B2W_B3W_PROBES.md:59 and the temp snippets at RV117's REVIEW.md:154. GEN-8 passes with the two registrations.

## 4. The living documents against the records and Git

Evidence: `_run_records/pr1111_merge_checks.txt`, `pr1112_merge_checks.txt`, `errata_e13_e14_checks.txt`, `branch_facts.txt`, `census_nine_check.txt`, `census_ts_check.txt`, `statics_paths_diff.txt`, `rr_hash_census.txt`, `rr_nofile_hashes.txt`, `rr_cited_paths.txt`, `heading_citations_check.txt`, `owner_quotes_check.txt`, `wg_staleness.txt`, `pr_body_checks.txt` and `sealed_unchanged.txt`.

### 4.1 #1111 → `54f1ba1f6d` (squash): confirmed

- **GitHub:** MERGED at 23:00:19Z, head `18a20d329f`, base `e33f3e2f1b`, merge commit `54f1ba1f6d`.
- **Git:** the squash's single parent is `e33f3e2f1b` (= `PARENTS.txt`). Its tree equals the head's (`91760a2626…`), and its P/execution equals NUM `0b8299e496`'s (`e5ad06e9aa…`).
- **The commit body equals `SQUASH_BODY.txt`** byte for byte, and it carries RV117 N-3's corrections.
- **The gate evidence:**
  - **CI:** `CI_RUNS.txt` lists the four runs on `18a20d329f` (37696600647, …726, …645, …661), all successful on GitHub. So this record cites its own head's runs, unlike `RECORDS_MERGE_2026-10-07B` (E-13).
  - **GEN-8 and the leak check:** `gen8.txt` has the head, the command and the cwd (E-4), and `leaks.txt` the command and its PASS.
- **NUM's absorb `039b17727f`:** its parents are `ac6fae5516` and `54f1ba1f6d`, and its tree equals its first parent's, as the record says.
- **Main after #1111:** first-parent `0b6c5d7362` (#1112) and `f4358eb0be` (#1113) only.

### 4.2 #1112 → `0b6c5d7362` (merge): confirmed

- **GitHub:** MERGED at 23:27:14Z, head `13d02273f4`, base `e33f3e2f1b`. Its commits are `b8bc059e35`, `2881cb1969` and `13d02273f4`, as the record states.
- **Git:** the merge's parents are `54f1ba1f6d` (main) and `13d02273f4`. Main's diff is the 5 slice files plus the 4 package files under `IMPLEMENTATION/SI1C/`: 9 files, +1,788/−161, as RR:15094 and the RECORD say.
- **CI:** the four automatic runs on `13d02273f4` succeeded (37697774199, …147, …158, …138), and so did the full-SHA dispatch 37697773464. The earlier dispatches are 37696852261 (success on `b8bc059e35`) and 37697481281 (cancelled on `2881cb1969`). That is exactly `CI_RUNS_13d02273f4.txt`.
- **DEC-025** (`dec025/`): ALL-DONE at 23:21:20Z on `b8bc059e35`; 40 manifests, 38 identical; EE 58 → 66 and the runner 35 → 44, by added or renamed tests; pytest 3,799 passed, 32 skipped and 130 subtests; vitest 141 files and 3,620 tests. The sweep stopped at the known `t13`.
- **The carry-over reasoning** (only `IMPLEMENTATION/SI1C/` and P/execution changed after the cut) matches Git.
- **RV111's R-2 correction** is in the RECORD.
- **NUM's absorb `46d3f6f937`** has parents `96e52b5e62` and `0b6c5d7362`, with no tree change.

### 4.3 The rulings since `0b8299e496`

RR appends **22 sections** (619 lines, 66,421 B), from "RV109 passes SP in RV-P round 2; …" to "RV115 and RV118 confirm B2-C revision 02: …".

**Every citation resolves** (`rr_hash_census.txt`, `rr_cited_paths.txt`, `heading_citations_check.txt`):
- **88 abbreviated sha256 citations** in the appended text and WG's T3 section:
  - **73 match the named file at H.** They include every return, review and addendum; every sum file cited by hash; I97's statics (v0, r1, r2); I98's and I99's inputs; and the committed `physics_source` fixtures.
  - **The other 15 are canonical or derived values, each stated in the records:** H(DEF-O) `a7ed7ca0…`; H(DEF-C) `9adf5178…`, `0c43cf42…` and `d3fde142…`; the Value hashes `c920a96d…` and `2f5ff465…` (I99); and `0d5bb812…`, the patched SCHEMA's hash, which E-14 corrects.
- **67 of 67 record paths** cited exist at H.
- **73 of 76 quotations resolve to RR headings.** The other three are not heading citations:
  - RR:15435 (a regex artefact around a quoted heading that resolves);
  - RR:15537, quoting REDACTION_E16's own words;
  - RR:15538, quoting ruling 4's words.

**Errata E-13 and E-14** (`errata_e13_e14_checks.txt`):
- **E-13:** the four runs it names are H2 `ea3b1443ea`'s, all successful.
- **E-14:** `b1` at I2 differs from main in 12 files and from I1 in 11. `SCHEMA_ENUM.diff` is `b1597c7b…`. #1109's commits are `4a58bf2a7d` and `b928a20f98`, merged as `cccc41a293`. RV117's N-1 and N-4 are ruled as RR:15045–15055 say.

**The I3 step and the readers' rounds** (`branch_facts.txt`, `census_*.txt`):
- **I3:**
  - `2ba2f81863` has parents `603e238517` and `b5cb7faaeb`. The sides are file-disjoint: SR-RS's 3 RE files against SP's and SA's 11 since I1.
  - `b1` is three commits on, at `03f55e7178`, pushed.
  - **The only production source change is `retained_wire.rs`'s one line** (`constructor_ordinal: t.original`, with its comment). The rest is `retained_facade_tests.rs` and the two W-C2 fixtures.
  - I3_01's suite table (PP 730/6 → 738/1; Stale 731/5 → 738/1) is as RR:15414 quotes it.
- **SR-RS round 2:** `6e3e4fe219`, one commit over `b5cb7faaeb`, touching RS's 2 files (`source_blocks.rs` untouched). Exactly 3 assertion lines are removed. E-15's 8 `out/` files are in `d914194721` and in H, and they are ignore-ruled (`**/out/`).
- **SR-PY:**
  - `70d4a68bd7` is three commits over `11cc14e3e6`, touching PY's 2 files. Its one removed assertion is `dict.fromkeys(got, PREP)`.
  - `2843a59a16` is four commits over R01. **Item 4's diff is byte-identical to the held patch.** It, the held patch and I91's recorded diff all have sha256 `357098ba93df…`, with the same patch-id.
- **SR-TS:** `b82b932923` is one commit over `7e47e51b5d`. `6fa6a64658` follows it with `1d9455c714` (the header at G2) and `6fa6a64658` (the G3 conjunct to G8). The TS tests remove no line over the whole round.
- **All four branch tips are pushed** at those commits.
- **The nine transport changes, recomputed from the committed census files:**
  - **PY**, RV113's `py_head.jsonl` (R01) against I91's item-4 census: bound 0 and unbound 0. Transport changes on exactly entries **277 and 286–293**, each G7 → G2 with the same code, and each equal to RS's at `6e3e4fe219`. PY's transport equals RS's on 339 of 339. Input sha256 is equal on 339 of 339.
  - **TS**, I92's `census_base.jsonl` (`7e47e51b5d`) against `REPAIR_01_ITEM3`'s head census: bound 0 and unbound 0. Transport changes on the same nine: **six admitted → G2**, and **three G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID` → G2** with RS's codes. That is exactly RR:15378.
- **The census ruling** (RR:15376: the no-change rule binds the input, bound and unbound verdicts, and the nine transport verdicts change onto RS's G2 reading) is what the records show.

**B2-C's path to final for J1:**
- **The reviews and verifications:**
  - **RV118's review:** ACCEPT WITH AMENDMENTS, 0/6/15.
  - **I97's revision 01:** verified, `6f6a583f…`.
  - **RV115 ADDENDUM_03:** soundness CONFIRMED, 0/1/5 (SA3-1). ROOT ruled option (ii).
  - **RV118 ADDENDUM_01:** CONFIRMED, 0/1/5 (A-1, routing). ROOT moved (ii)'s formation to B2-K and the 4 h threshold with it.
  - **I97's revision 02:** verified, `79007dcd…`. B2-K's cost is 2.5–3.5 h, under the threshold.
  - **RV115 ADDENDUM_04:** CONFIRMED, 0/1/5 (SA4-1).
  - **RV118 ADDENDUM_02:** CONFIRMED, 0/1/2 (B-1, routing).
  - Each count and verdict is as RR quotes it. RV115's ADDENDUM_02 on DEF-C is ACCEPT, 0/0/5.
- **The statics** (`statics_paths_diff.txt`):
  - DEF-C changes 4 leaf paths from v0 to r1, and 2 from r1 to r2 (`rows/displacement_magnitude`, `stages/observables`).
  - PTABLE changes 2 paths from v0 to r1, and 1 from r1 to r2 (its DEF-C sha256), as RR:15456 and RR:15502 say.
- **J1's inputs at RR:15558–15560** (SCHEMA `abf3225c…`, PTABLE r2 `b2b4a54d…`, DEF-C r2 `3cebce55…`, H `d3fde142…`) match the files and records.
- **The superseded records are unchanged** (§5).

**The owner's decisions, quoted exactly** (`owner_quotes_check.txt`):
- **SI1c:** "D: block at overflow" and "Repair within 1.0.0" are verbatim in RR's owner-decision section (RR:14060ff.) and in WG:603.
- **The memory decision (2026-10-08):** RR:15286 quotes the owner in full. WG:601's shorter quotation is a verbatim substring.
  - RR translates the owner's "64 GB" and "12 GB" as GiB. That is consistent with the owner's earlier "64 GiB" and "12 GiB" decisions.
- **Its clarification:** RR:15318 quotes it. WG:602 paraphrases it without quotation marks, accurately.
- **E-16's choice:** RR:15521 ("The owner chose redaction in place on NUM (option 1 of three)") and REDACTION_E16's "Ruled by the owner (2026-10-08): redact in place on NUM" agree. Neither quotes owner words, and none is claimed.
- **All 7 quoted phrases** in WG's owner-decisions block occur verbatim in RR.

**No owner-held decision was taken by ROOT.** Each item the brief names:
- **B2/B3's decisions 22–24 stay prepared and undecided.**
  - RR:15287 says decision 22 (about 13.25 GiB) "stays owner-held, and is not proposed". WG's T3-B2/B3/B4 row says "22–24 are owner-held".
  - B2-C's D1.4 sets C_eq = c + z ≤ 3 (C-9). That does not admit decision 22's three cases plus a combination (C_eq = 4), so C-9 does not decide decision 22.
- **M above 12 GiB is the owner's.** The 2026-10-08 decision keeps the product's M at 12 GiB. ROOT's host rules (52 GiB start gate, four slots, 22% guard floor) concern development jobs within the owner's 64 GiB allocation. No product M above 12 GiB is selected anywhere in the span.
- **Within ROOT's delegation, and changing no public meaning before B8:**
  - **SA3-1's option (ii)** changes only DEF-C's combination magnitude row. DEF-C is a B2 identity, not public before B8. DEF-O stays frozen, and the 4 h cost condition was honoured (2.5–3.5 h).
  - **C-1 to C-16:** RR:15082 makes them ROOT's, and RV118 agrees with all 16. RV118's REVIEW:248 finds "Nothing in B2-C changes public meaning before B8". C-4 amends C3a rule 4, which is a ROOT-selected B0 reservation.
  - **The header move's nine transport changes and the alignment set** are reader refusals of forged or mislabelled receipts. Successors have no product caller before B8. No corpus entry pins a transport verdict, and the bound and unbound verdicts are unchanged.
  - **The ordinal fix** repairs a latent producer defect in the registered dev/test build, with no product caller and no existing pin changed.
  - **I judge that none of these changes public meaning before B8.**

### 4.4 WG's T3 section (N-1)

- **The positions** agree with Git and RR at N:
  - SI1c on main;
  - #1111 squashed;
  - I3 and I85's I3 step;
  - the three readers' rounds committed and awaiting RV113;
  - the ordinal defect fixed;
  - B3-D and B2-C final for J1;
  - the probes done and the witnesses selected;
  - NUM carrying main `0b6c5d7362`;
  - the four-slot host.

  The exceptions are the T3-B1/B6 row's SP text and the header date (N-1).
- **The owner-held list** carries "M above 12 GiB" and the owner's 2026-10-07 and 2026-10-08 memory directions correctly. It lacks the cleanup of main's tree (N-1).
- **The owner decisions in force** add the 2026-10-08 decision and its clarification correctly, with the quotes verbatim. E-16's choice is not listed (N-1).
- **The next unused IDs at N are I100 and RV119.** I97–I99 and RV118 have folders at N; I100, RV119 and RV120 have none. RV119's brief is not at N. The dispatched ranges (I68–I99, RV97–RV99, RV101–RV118) are right.
- **The running and idle lists** match RR at N:
  - running: RV109 on the I3 step, and RV113 on SR-RS round 2, then SR-TS, then SR-PY;
  - idle: RV111, RV115, RV116, RV117 and RV118, among others.
- **The next safe action** matches RR's order for B1, B2/B3 and records. Item 3 forecasts this PR, and item 4's cleanup list rightly adds `records-pr-c`, `s-i1c` and `si1c-pr` and omits `records-pr-d` (#1114's checkout).

### 4.5 The PR description (N-3)

`_run_records/pr1114_body.md` and `pr_body_checks.txt`:
- **Accurate:**
  - **"Not in this PR":** I96's REVISION_01 and RV116's ADDENDUM_01 are on main. RV113's SR-RS ADDENDUM_02 and SR-TS ADDENDUM_01 are untracked in NUM.
  - **E-15's 8 force-added files** are in H.
  - **"all 156 `.gz` files"** is the right count.
- **Wording:** the two points in N-3.
- **ROOT's one pre-dispatch correction** (RR "Records PR #1114 opened; …", after N) is reflected: the B3-D revision moved to "Not in this PR", and RV113's SR-RS ADDENDUM_01 was added.

## 5. Integrity: PASS

**The sum files**, read from H's committed tree with `git cat-file` (`_run_records/sums_committed_tree.tsv`, `sums_folders.tsv`). "Uncovered" counts files in the folder that none of its sum files lists.

| Folder (T-relative) | Sum file(s) (PR unless marked main) | Result | Uncovered |
|---|---|---|---|
| `IMPLEMENTATION/RECORDS_MERGE_2026-10-07C/` | SHA256SUMS | 6/6 | 0 |
| `IMPLEMENTATION/SI1C_MERGE/` | SHA256SUMS | 28/28 | 0 |
| `IMPLEMENTATION/REDACTION_E16/` | SHA256SUMS | 1/1 | 0 |
| `R/I85/b1_sp_01/` | SHA256SUMS (main); .return (main); **.i3_01** | 44/44; 86/86; **120/120** | 0 |
| `R/I90/b1_sr_rs_01/` | SHA256SUMS (main); .repair_01 (main); **.repair_02** | 64/64; 23/23; **75/75** | 0 |
| `R/I91/b1_sr_py_01/` | SHA256SUMS (main); .repair_01 (main); **.repair_02; .repair_02_item4** | 56/56; 29/29; **56/56; 41/41** | 4, by design: RETURN.md, REPAIR_01.md, REPAIR_02.md and REPAIR_02_ITEM4.md, each anchored by sha in RR (`bc7fa865…`, `f97b46ba…`, `f7e50348…`, `06a72494…`) |
| `R/I92/b1_sr_ts_01/` | SHA256SUMS (main); **.repair_01; .repair_01_item3** | 29/29; **36/36; 13/13** | 0 |
| `R/I97/b2_c_01/` | **SHA256SUMS (v0); .revision_01; .revision_02** | **13/13; 10/10; 9/9** | 0 |
| `R/I98/b2_w_probe_01/` | SHA256SUMS | 62/62 | 0 |
| `R/I99/b3_w_probe_01/` | SHA256SUMS | 38/38 | 0 |
| `R/REVIEW_RV109/rvp_round2_01/` | SHA256SUMS (`1863f506…`) | 125/125 | 0 |
| `R/REVIEW_RV111/si1c_01/` | SHA256SUMS (main); .addendum_01 (main); **.addendum_02–04** | 111/111; 24/24; **6/6, 7/7, 7/7** | 0 |
| `R/REVIEW_RV113/rvr_sr_py_01/` | SHA256SUMS | 245/245 | 0 |
| `R/REVIEW_RV113/rvr_sr_rs_01/` | SHA256SUMS (main); **.addendum_01** | 34/34; **9/9** | 0 |
| `R/REVIEW_RV113/rvr_sr_ts_01/` | SHA256SUMS | 31/31 | 0 |
| `R/REVIEW_RV115/b2_kd_01/` | SHA256SUMS (main); .addendum_01 (main); **.addendum_02–04** | 4/4; 5/5; **4/4, 4/4, 4/4** | 0 |
| `R/REVIEW_RV117/records_01/` | SHA256SUMS (`e3d47596…`) | 45/45 | 0 |
| `R/REVIEW_RV118/b2_c_01/` | **SHA256SUMS; .addendum_01; .addendum_02** | **7/7; 7/7; 5/5** | 0 |

**Totals:** the 28 sum files the PR adds hold 1,014 entries, all OK, 0 bad, 0 missing. With the 12 on main in these folders: 40 files, 1,523 entries, all OK. Every added folder with a sum file is in the table. The briefs are unsealed, as before. The 156 `.gz` files verify as compressed bytes in their folders' sums.

**The superseded sealed files are unchanged** (`sealed_unchanged.txt`). Each was committed once in NUM's history and is byte-identical at H:
- **I97:** CONTRACT.md (`165cd4b1…`), SHA256SUMS (`d8f032d1…`), REVISION_01.md (`6f6a583f…`), SHA256SUMS.revision_01, `statics/` and `statics/r1/`, beside REVISION_02.
- **I91:** REPAIR_02.md (`f7e50348…`) and SHA256SUMS.repair_02, beside REPAIR_02_ITEM4; also RETURN.md and REPAIR_01.md.
- **I92:** REPAIR_01.md and its sums, beside REPAIR_01_ITEM3.
- **RV118:** REVIEW.md and ADDENDUM_01.
- **RV115:** REVIEW.md and ADDENDUM_01–03.
- **RV111:** REVIEW.md and ADDENDUM_01.

**RR is append-only: PASS** (`_run_records/rr_append_only.txt`). Main's RR (1,282,756 B, 14,962 lines) is an **exact byte prefix** of H's (1,349,177 B, 15,581 lines), and H's RR equals N's.

**The originals: PASS** (§3): E-16's 42, E-10's 47 (50 rows) and REDACTIONS.json's 13. None is in H.

## 6. Gate evidence: PASS (the records-only gate set)

The records-only gates are GEN-8, the PR's automatic CI and an independent review. This PR changes no product, test or CI path. It changes one policy path, `P/validation/portability_policy.json`, by E-17's two hash-bound registrations, and nothing under T's `REFERENCES/` or `DESIGN_NUMERICS/`.

| Gate | Evidence | Exact head? | Result |
|---|---|---|---|
| GEN-8 (ROOT) | Relayed at dispatch: 1 passed, 10 deselected, on H. RR's section after N ("Records PR #1114 opened; …") says its first run failed on E-17's two files, which are now registered. I did not see ROOT's file; it goes into the merge record | H | **pass**. The record should carry the head, the command and the cwd (E-4) |
| GEN-8 (RV119) | §3 | H | **pass** |
| `validate_run_record_leaks.py` (ROOT and RV119) | Relayed: 1,056 files, 0, 0, one 8.1 MB warning; mine identical (§2) | M..H | **pass** |
| governance-harness | 37719456554, on the merge ref `717d220e38` (parents M and H; tree = H's), with `CHIRALITY_REQUIRE_LIVE_TESTS: 1`: "1161 passed, 48 subtests passed" | H | **success** |
| Harness Pre-merge Validation | 37719456611: Select App coverage and Harness pre-merge succeeded; the App jobs were skipped by selection | H | **success** |
| pec-tests | 37719456551: Select PEC coverage and pec succeeded; workspace tests skipped | H | **success** |
| Piping Desktop E2E | 37719456552: Select source coverage, **the Numerical cargo suite** (23 min) and Desktop E2E (source mode) succeeded; remainder and accessibility skipped by selection. Unlike #1111's run, this selection included the numerical suite, presumably because the PR touches `P/validation/` | H | **success** |
| Independent review | this report | H | **PASS** |

## What ROOT must rule on

Nothing blocks the squash. In order:
1. **S-1, before the squash:** accept the earlier host-name form in RR:15496, B2C_REVISION_02.md:41 and I90's `write_records_r2.sh:35` as screen text, recording that main gains it; or have it redacted in place on NUM by E-16's method (the owner's call, as E-16's was). Either way:
   - describe that form from now on, as RR:15530 does;
   - add a split-form check to the commit-time screen.
2. **N-3, for the squash body:**
   - name "the owner's own words" among the accepted hits, and reflect S-1's ruling;
   - word RV109's part as "RV109's round 2 on SP (before I3)".
3. **Before the merge:**
   - check that main is still `f4358eb0be`;
   - `gh pr merge 1114 --squash --match-head-commit 57f078b4c8a87756d3d0985f58a67e15bbeda476`, with the explicit subject and body;
   - the merge record carries ROOT's GEN-8 (head, command and cwd), the leak check's output, and CI_RUNS for H (37719456552, 37719456611, 37719456551, 37719456554).
4. **N-2:** one RR erratum at the next append, and correct what the owner was told if needed.
5. **N-1:** the next WG touch.
6. **Keep `WT/records-pr-d`** (#1114's checkout, HEAD = H, clean) out of any cleanup until #1114 merges.

## Host and method

- **My copy:** a detached worktree of H at `WT/rv119`, created with `git worktree add --detach` from NUM's repository, as the brief directs. I wrote nothing in it, and removed it and its registration at the end. Logs and scripts are in `WT/scratch/rv119_records_01/`, with `TMPDIR` there.
- **Reads:**
  - NUM's object store and working tree with `GIT_OPTIONAL_LOCKS=0` (`log`, `diff`, `ls-tree`, `show`, `cat-file`, `merge-base`, `rev-list`, `grep`, `status --ignored`, `check-ignore`, `patch-id`, `ls-remote`);
  - `gh` read-only for #1109, #1111–#1114, #885 and the CI runs, jobs and one job log, plus one `gh api` read of the merge ref;
  - ROOT's PR checkout `WT/records-pr-d` (HEAD = H, clean), read only;
  - `hostname` and `scutil --get` for the machine's names, used in memory only.
- **What I ran:**
  - one GEN-8 pytest, through `WT/tools/t3_slot.sh` (slot 3, 37 s), as one background shell job with one wait, its completion notice, which came when the job's process had gone;
  - one `validate_run_record_leaks.py`, in my copy;
  - read-only VENV Python scans and hashing, with `PYTHONDONTWRITEBYTECODE=1`.

  No cargo, no other test, no install, no DEC-025, and no Git write to any branch, ref or remote beyond creating and removing my worktree. No process or wait of mine remains. Nothing went to the system temp directory.
- **Disclosed slips:**
  1. **A fetch dry run.** My first command ran `git fetch --dry-run` in NUM to test the remote. It updates no ref and no FETCH_HEAD, but it may have written fetched objects into the shared object store.
  2. **The host `python3`.** My first PR-metadata command piped `gh pr view` output through the host `python3` for formatting (a read-only parse; no file written). Everything after used VENV only.

  Neither touched any record, branch or job.
- **The scripts** (`_run_records/scripts/`):
  - **RV117's, unchanged in logic:** `token_shape_scan.py`, `redactions_check.py`, `redactions_e10_check.py`, `sums_committed_tree.py`, `sums_folders.py`, `rr_cited_paths.py` and `heading_citations_check.py`, with their docstrings changed.
  - **RV117's, extended:** `publication_scan.py`, `gz_check.py` and `abs_scan.py`, for the host screen and output sanitizing. The machine's names are read at run time, and the earlier form is read from RR at H.
  - **New:** `host_variants_scan.py`, `extra_host_scan.py`, `redactions_e16_check.py`, `e17_policy_check.py`, `rr_hash_census.py`, `owner_quotes_check.py`, `census_nine_check.py`, `census_ts_check.py` and `statics_paths_diff.py`.
- **Records:** this file, `_run_records/` and `SHA256SUMS`, with placeholder paths only, no symlink and no folder named `build`. `scripts/self_screen.py` screened them before return, with 0 hits for each term: the strict pattern of B1_COMMON; the network name, the local host name and the computer name; the laptop-model form, plain and split; the earlier form and its domain; the dot-local suffix; the junit `hostname` attribute; the owner's e-mail; and absolute temp, home and system roots. There is no `.gz` file and no junit output. `git status --ignored` on the folder shows only untracked files, none ignored. The PR-body copy (`pr1114_body.md`) writes its two host terms as placeholders, and says so in its first line.
