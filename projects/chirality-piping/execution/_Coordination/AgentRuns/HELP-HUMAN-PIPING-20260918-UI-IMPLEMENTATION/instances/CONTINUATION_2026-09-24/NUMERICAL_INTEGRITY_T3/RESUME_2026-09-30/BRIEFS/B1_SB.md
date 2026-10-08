# I107: SB, Pass B on PR-B1's head

Read `R/BRIEFS/B1_COMMON.md`. It binds you, except where this brief changes the host rules. You hold I72's Pass B role for B1. **The owner directs production first: keep the record short.**

## The candidate

- **PR-B1's code commit:** `8248921552` on `codex/piping-t3-pr-b1-20261008` (`WT/pr-b1`). It is cut from main `6c821d9ccf` and carries the 33 maintained files that NUM `a41eea7b5f` changes. `source_equality.py` passes checks 1–3 and 5. Check 4 waits for SK's package.
- **Pass A is SQ:** `R/I104/b1_sq_01/`, on `b1-q` `69002bc862`, with `registration.diff` applied. That diff is applied on `b1` as `ddc8eaaf54`, and the PR carries it.
- **The method:** PLAN_v2 §3.8 (`R/I84/b1_plan_01/PLAN_v2.md`). The tools:
  - I65's fail-closed `g7_pass.sh`, retargeted as I72 did (`R/I72/u8_passb_01/_run_records/`);
  - SQ's tools (`R/I104/b1_sq_01/_run_records/tools/` and `g6/tools/`).
- **The rulings:** RR "R6b: RV124 passes SQ and confirms M; …", notes Q-N1 and Q-N5.

## Pass B must show

On an archive of `8248921552`:
1. the tree;
2. the entry equal to the applied registration (`threshold_bytes` 11,274,289,152, with the reviewed inputs);
3. law, statics, the line map and the premise pins;
4. **TEXT and forms equal to SQ's** (D = 41,769 and D_env = 22,911, both GENERATED PROFILE blocks);
5. every delta row classified against SQ's head, with a reviewed `delta_reviewed.json` entry for each of B1's production hunks;
6. the non-candidates equal to SQ's swept set, using **`noncand_compare_nomult.py`** (Q-N5);
7. the controls;
8. PP and runner outcomes changed only by the listed tests;
9. the witnesses and the challenge equal to SQ's.

**Q-N1:** state B1's unpriced heap owners with their bound: `Vec<CaseAttempt>` is 28,200 B at |A| = 3, plus small O(c) locals, about 30 KB in all, against the 287 MB dense margin. Say whether Pass B finds any other unpriced owner.

**Stops:**
- any production-class row SQ did not review;
- any difference in TEXT, forms, the entry or M;
- a witness or challenge regression.

Expected: the PR head's maintained source is NUM's, which is `b1`'s plus main's non-piping changes. So the delta against SQ's head is the G6 re-pins and the registration, and nothing else of production class.

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`), with targets under `WT/targets/i107-sb*`. **Other heavy commands** go through `WT/tools/t3_slot.sh`.
- One heavy job of yours at a time, with one wait per job. Never signal another job.
- **Not allowed:** DEC-025, RSS or timing measurements, and installs.
- Scratch goes in `WT/scratch/i107_b1_sb/`. Absolute paths only.

## Output

- **The record:** `R/I107/b1_passb_01/`, containing RETURN.md (the verdict line, the gate codes, the delta rows and Q-N1), `_run_records/` and SHA256SUMS. Use placeholder paths only. No Git writes.
- **Budget:** 2–3 h, plus build time.
- **End your turn with:**
  - the verdict;
  - the gate codes;
  - the delta rows;
  - Q-N1;
  - the RETURN's sha256;
  - any stop.
