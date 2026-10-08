# I107 B1-SB: Pass B on PR-B1's head (b1_passb_01)

TASK (Type 2), I107, holding I72's Pass B role for B1, for ROOT (HELP_HUMAN, Agent 0). 2026-10-08 UTC. No delegation.

**Read and verified:** NUM `AGENTS.md`, `agents/AGENT_TASK.md`; `R/BRIEFS/B1_COMMON.md` (`2d170307…`) and `R/BRIEFS/B1_SB.md` (`6d2a4c67…`); PLAN_v2 (`c85786b7…`) §1, §2.3, §3; RR "R6b: …", "RV112 passes SA; …" and "I108's package returned; …" (NUM `75cd6be76b`); I72's record; SQ's record (`R/I104/b1_sq_01/`: SHA256SUMS 116/116 and .addendum_01 465/465 OK); RV124's review (`9bb6f811…`, SHA256SUMS OK). ROOT's two mid-task messages: the recut head and item 10; PR #1154's head.

## The candidate

**`d07006c2f001be5565646d6f1cf046e6dc96006c`** (PR-B1, recut from main `3d73db745e`); it supersedes `8248921552`. PR #1154's head `0752ae8b98` is `d07006c2f0` plus one commit of 7 files, all under `P/execution/` (SK's package, `prep/pr_head_records_only.txt`), so **this verdict holds for the PR head.**

Identity from Git (`prep/prep_identity.out.txt`, all PASS): outside P the head is main `3d73db745e`, and P without `execution/` is NUM `75cd6be76b`. SQ's recorded G5 and G6 diffs equal Git byte for byte, and `registration.diff` on `69002bc862` gives `ddc8eaaf54`'s file. The 6 D1-crate files changed since SQ's TEXT basis are b1's blobs, except `retained_memory.rs`, whose difference is ROOT's two comment lines. The 9 other changed files are main's. **Carry-over (P8):** `8248921552 → d07006c2f0` in P is that one comment, with the same line count. The Python-only dry runs on `8248921552` carry over; **every gate below, including every build, ran on `d07006c2f0`.**

## Verdict: `DELTAS TO READ`, exit 6; one gate to read, the challenge's process-floor control, which is environmental (below). No stop.

`VERDICT DELTAS TO READ exit=6 basis=d07006c2f001be5565646d6f1cf046e6dc96006c tag=b1 passA=SQ(57c92a7b3310229406733a7134e271c29bcc6978..69002bc862+registration) gates=tree:0 entry:0 entry_code:0 m:0 law:0 law_sq:0 statics:0 premise57:0 linemap:0 premise:0 text_run:0 delta:0 text:0 text_n5:0 forms:0 forms_g5:0 noncand_run:0 noncand:0 controls_run:0 controls:0 controls_sq:0 pp_outcomes:0 runner_outcomes:0 witnesses:0 challenge:6`

| Brief item | Gates | Result |
|---|---|---|
| 1 tree | tree 0 | 2,970 of 2,970 blobs; none extra |
| 2 entry | entry 0, entry_code 0, m 0 | `REGISTERED_PROFILES` byte-equal to NUM `75cd6be76b`'s. Its code lines equal the applied registration's (`ddc8eaaf54`); only the two comment lines differ. `threshold_bytes` = 11,274,289,152; the identity, reviewed inputs and layouts are as compiled (law) |
| 3 law, statics, line map, premise pins | law 0, law_sq 0, statics 0, premise57 0, linemap 0, premise 0 | law: 54 passed, 0 failed; the 7 registered tests ran; **the 276 `I65_G5_*` record lines equal SQ's registered record, in order.** Statics: none added or removed. Rules carried 57c92a7b33 → head, none unmapped. The three premise pins are as reviewed |
| 4 TEXT and forms | text_run 0, text 0, text_n5 0, forms 0, forms_g5 0 | **D 41,769, D_env 22,911, TAV 6,234,394,666, complete;** text_budget rows equal SQ's G5 point in all four variants (2,847 rows each). The other G5 outputs are byte-equal; edges and loop log equal after the line map. The N-5 point's profile tree, producer caps and call-graph summary are byte-equal. **Both GENERATED PROFILE blocks regenerate exactly:** N-5's tree gives the head's; G5's gives `b075c5c59f`'s |
| 5 delta | delta 0 | below |
| 6 non-candidates | noncand_run 0, noncand 0 | `noncand_compare_nomult.py` (Q-N5): 412 rows, 408 matched, 4 new, 2 gone. The rows are byte-equal to SQ's `noncand.json`. I65's tool reports 288 "new", for information |
| 7 controls | controls_run 0, controls 0, controls_sq 0 | 12 of 12, each control's outcome, TAV and finding equal to SQ's |
| 8 PP and runner outcomes | pp_outcomes 0, runner_outcomes 0 | PP 741 passed, 1 failed (Mac `t13`), 79 ignored: **outcome for outcome SQ's registered suite.** Runner/headless 85 passed, 2 failed (the known `load_reference` pair): identical to SQ's registered tree run beside it. **No test changed** |
| 9 witnesses and challenge | witnesses 0, challenge 6 | **all 40 of SQ's witness entry points pass with SQ's lines** (timing lines excluded). **All 27 product challenge entries equal SQ's to the byte** (peaks, outcomes, bounds), and the default test equals RV124's. The one line that differs is the floor control |

**The challenge's one difference: `process_floor` printed 4,161 live bytes; SQ's run printed 4,162.** This control runs no product code: it prints the counting allocator's live bytes at the test's start. That count is **4,060 + len(argv[0])** (`prep/floor_argv0.txt`: four runs at paths of 101, 57, 58 and 59 bytes printed 4,161, 4,117, 4,118 and 4,119). SQ's binary path is 102 bytes, so 4,162; RV124's is 100, so 4,160 (its record). It depends on the environment, not on B1's code.

## The delta rows (`runs/b1/delta_inventory.json.gz`; from 57c92a7b33, SQ's TEXT basis, to the head)

**15 files and 83 rows,** every one classified: 17 generated, 4 test, 1 no-code, **1 item, 1 live**, 48 qualification-test and 11 not-d1.
- **Production class (2), both SQ's reviewed changes:**
  - `retained_memory.rs:983–985` (item): the registration's `threshold_bytes`. Its code line is `registration.diff`'s; its comment lines are ROOT's citation correction (P5b: comments only).
  - `:2706` (live): G6's SF-1 bound in the const fn `phase_caps` (integer arithmetic, no allocation or text).
- **Qualification tests (48):** SQ G6's re-pins. They are in the law tests (17), the witness tests (20) and the challenge (11).
- **No-code (1):** `:2688–2693`, the SF-1 doc. **Generated (17):** the G5 and N-5 blocks, which pass FORMS. **Test (4):** `#[cfg(test)]` items inside the block.
- **Not-d1 (11):** `tests/common/b1_sq_inputs.rs`, `tests/s11f_site_test.rs`, and main's 9 (the rules crates' SI1c files, CI docs and scripts, `portability_policy.json`).
- **`delta_reviewed_b1.json`** (sha256 `d1e186bb…46e58dc`) has 50 entries, all matched and none refused. `mk_delta_reviewed.py` writes an entry only for a hunk whose lines are removed or added by RV124-reviewed diffs: SQ's G5 diff, SQ's G6 commit, `registration.diff`, or (comment lines only) ROOT's correction. Each entry cites RV124 and is for RV-Q's confirmation.
- **No production-class row that SQ did not review.** Against SQ's head `69002bc862`, the delta is the registration, the comment and main's 9 files.

## Item 10: the retained route's error-text owners (`runs/b1/item10_error_owners.json`; RR "I108's package returned; …" item 4)

**The only String-bearing error variant** in the types the producer stores is `CaptureError::Association(String)` (`retained_product.rs:69`). PP's G5aFailure, OperationalError, PreparedCandidateError and AdapterFault, and the kernel's 14 error types, have none.

**The owners, Direct route:** every setter is reached from the Direct root on this pass's graph.

| Scope | Owner (path:line) | At once |
|---|---|---|
| per case (own fields, or a parked `CaseSlot`) | `error` (`retained_product.rs:126` / `:198`); assignments replace, `fail` sets once | 1 |
| per case | `observable_error` (`:130` / `:202`), replaced at `:1992`, `:4369`, `:4395` | 1 |
| per attempt (|A| ≤ c) | `trace.native_error` (`retained_receipt.rs:41`), set at `retained_product.rs:3705` from **`native`'s clone of the batch call's one error, `:3692`** (QUAL_B1 §11's row) | 1, either this… |
| per attempt | `AttemptEnd::Candidate(RefusedCase { error })` (`:3642`; Capture or Abandoned hold one `CaptureError`, `:4176–4177`) | …or this: an attempt ends Native or reaches T-9, never both |
| per invocation | the call's own `Err` local during the clones (`:3688–3692`); or `CustodyFailure.error` (`:3669`), only when custody fails, with no attempts, dropped at `lib.rs:3290` | 1 |
| off route | `PreparedCandidateRefusal.error` (`:4179`) and the one-case `solve_native` (`:4099–4112`): the private driver only, not reached from the Direct root | — |

**Counts:**
- **3 owners per case** (2 in the slot, 1 per attempt). 3m + 1 = 97 bounds them;
- **3c + 1 = 10 per invocation.**

**Each owner's text is within Text(err) = 16,384 B (capacity).** Its sources are:
- 234 literals of at most 58 B;
- the `format!` sites `:2210`, `:2510`, `:2713` and `lib.rs:14015`, at most 2,098 B capacity by TEXT;
- `From<&str>` at `:3431`, at most 654 B;
- `native`'s clone, which TEXT prices at 16,384 per prepared case (3 × 16,384 in TAV_W).

**No breach.**
- **The bound's scope:** G-C's fact reads the slots' 2c owners; the attempt owners arise after G-C (T-8, T-9), and TEXT prices their text.
- **Other error-text owners, outside this fact:** the ordinary seeds' error clones (`:374`, `:379`, `:380`, `:418`) are G-C's `OrdinarySeedBytes`, and the serializer's `"detail"` copies (`retained_wire.rs:587`) are wire text in TEXT.

## Q-N1

- **The owners and their bound.** B1's unpriced heap owners are `Vec<CaseAttempt>` (9,400 B each, so 28,200 B at |A| = 3, live from T-7 through the serializer) and small O(c) locals in the serializer and the RS reader (a few KB). That is **about 30 KB in all, against the 287,052,726 B dense margin** (0.01 %). M is unaffected.
- **Pass B finds no other unpriced owner.** The delta from SQ's TEXT basis adds no allocating production code: its two production rows are a static's field and const arithmetic. Item 10's attempt owners are inline in `CaseAttempt` (Q-N1's 9,400 B), and their text is TEXT-priced.
- **The sizes are RV124's probe,** not re-measured. The head's D1 sources equal the tree RV124 probed, apart from one comment.

## For ROOT and RV-Q

1. **Pass A's revision is SQ's TEXT basis `57c92a7b33`, not its head `69002bc862`.** SQ's chains are keyed to and priced 57c92a7b33's code, so the line map and the delta run from there. That puts SQ's G6 re-pins and the registration in the delta, as the brief expects. The delta against `69002bc862` alone is in P2 (10 files).
2. **The tools:** I65's checks unchanged; SQ's chain, linemap, n5, controls and nomult tools unchanged. Mine are `tools/` (`b1_pass.sh`, `run_cargo_b1.sh`, `run_point_b1.sh`, `b1_checks.py`, `mk_delta_reviewed.py`, `prep_identity.sh`, `item10_error_owners.py`, `post_run_b1.py`), with diffs against I72's and SQ's in `tools/tools_diff_vs_i72_and_sq.txt`.
   - **Added gates:** `entry_code`, `m`, `law_sq`, `premise57`, `text_n5`, `forms_g5` and `controls_sq`.
   - **Not run:** `price_delta.py` (U6's F5).
   - **The edges comparison:** a span's byte offsets may move only within a changed file, and its length may change only for a fn that encloses a reviewed hunk. Only `phase_caps` grew, by 4 B.
   - **One edit after the run:** `post_run_b1.py`'s path pattern was spelt in pieces, with the same pattern.
3. **The floor control** could compare `live_bytes − len(argv[0])` in a later Pass B. I left the gate as it ran.

## Execution

- **Host.**
  - Cargo: 4 jobs through `t3_cargo.sh` (`--locked --offline`), in fresh targets `WT/targets/i107-sb-b1`, `-b1-runner` and `-b1-runner-sq`.
  - Python: the TEXT points, the sweep and the controls ran through `t3_slot.sh`, as did every test binary, one process each (40 witnesses, 28 challenge entries, plus the 4 floor runs).
  - No `time -l`, no `t3_exclusive.sh`, no DEC-025, no install, no Git write (reads with `GIT_OPTIONAL_LOCKS=0`). `WT/pr-b1` was not touched; I used `git archive` copies.
- **The superseded head's run:** stopped by me, on ROOT's recut, about 1 minute in. It was my own process group, during its Python points. `cargo_jobs.log` keeps one unmatched START, slot 1 at 14:01:44Z. Its log is `logs/pass_b1_8248921552_stopped.log`.
- **Twice a job had two of my waiters** (a background one and a foreground one); no other job was waited on or signalled.
- **Records:** placeholder paths only, with no symlink and no `build` folder. Large outputs are gzipped (`gzip`, mtime 0). Scratch is kept in `WT/scratch/i107_b1_sb/` for RV-Q.
- **SHA256SUMS** covers every other file in this folder.
