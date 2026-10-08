# T3 handoff to the next ROOT session (ephemeral, 2026-10-08)

This note is for the owner's next T3 session only. It is not a standing record and is not maintained after use. Durable facts live in the records it points to.

T3's current account is the piping work graph's **T3 current route** section, `execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md`. It holds:
- the route;
- the owner-held choices;
- the decisions and rulings in force;
- the next IDs;
- the next safe action.

## Starting the session

- **The owner starts it** in the T3 integration worktree, `<repo>/.claude/worktrees/swbpipe-control-layer-8a41be/.claude/t3/numerics`, on branch `codex/piping-numerical-integrity-20260926` (NUM).
- **The first message** is piping's init prompt with the steer filled in: [HANDOFF_2026-10-08_PROMPT.md](HANDOFF_2026-10-08_PROMPT.md).
- **The loop instructions** are piping's `loop/LOOP_INIT.md`.

## In flight at handoff

**The previous session stays open, idle, only so its two running reviewers can finish writing their records. It takes no further action.** Verify their records from disk. If a record is missing or unsealed once that session has closed, dispatch a fresh reviewer (the next ID) with the same brief.

1. **Records PR [#1114](https://github.com/sgttomas/chirality/pull/1114),** branch `codex/piping-t3-records-20261008`, head `8568fb2053`, in `WT/records-pr-d`.
   - **Its content:** NUM's `execution/` at `dc4ffdc7c8`, plus E-17's two entries in `P/validation/portability_policy.json`.
   - **RV119 passed it** (0/1/3; `R/REVIEW_RV119/records_01/REVIEW.md`, `ef2c9538…`). **Its ADDENDUM_01** confirms the S-1 delta, and was being written at handoff. It is complete when `SHA256SUMS.addendum_01` exists and verifies.
   - **Hosted CI** on `8568fb2053` was still running its numerical cargo suite.
   - **Then:**
     1. check that main touched nothing under piping's `execution/` or the policy file (main moved to `0e62b8e36b`, app-v4 only);
     2. `gh pr merge 1114 --squash --match-head-commit <full 8568fb2053 sha>`, with an explicit subject and a body that answers RV119's N-3. The screen sentence names "the owner's own words", and RV109's round 2 reviewed SP before I3. Its I3 confirmation is in the PR's second commit;
     3. the merge record `IMPLEMENTATION/RECORDS_MERGE_2026-10-08/`, in `RECORDS_MERGE_2026-10-07C/`'s form;
     4. NUM absorbs main.
2. **RV113's confirmations of the three readers' rounds,** all in `R/REVIEW_RV113/`:
   - **SR-RS round 2:** CONFIRMED and sealed (`rvr_sr_rs_01/ADDENDUM_02.md`, `c43317f8…`, 252 sums).
   - **SR-TS repair 01:** CONFIRMED and sealed (`rvr_sr_ts_01/ADDENDUM_01.md`, `5f86b3e7…`, 84 sums).
   - **SR-PY repair 02 with item 4:** its mutant runs were in progress (`rvr_sr_py_01/ADDENDUM_01.md`).
   - ROOT has verified and committed none of the three.
   - **When all three are verified, make I4:** merge `b1-r` (`6e3e4fe219`), `b1-p` (`2843a59a16`) and `b1-t` (`6fa6a64658`) into `b1` (`03f55e7178`).
   - Then fill `{I4 commit}` in `BRIEFS/B1_SC.md` and dispatch SC.
3. **Uncommitted on NUM at handoff:** RV119's records and RV113's addenda. Commit them after verifying, with the run-time host screen (below).

## Where things are, in this folder

- **The rulings:** `ROOT_RULINGS_V1.md`, append-only. The graph lists the sections in force. The newest are 2026-10-08's: the alignment rounds, B2-C final for J1, E-16 to E-18 and S-1.
- **B1:**
  - the plan: `RESUME_2026-09-30/I84/b1_plan_01/PLAN_v2.md`;
  - the common rules: `BRIEFS/B1_COMMON.md`;
  - SC's brief, prepared: `BRIEFS/B1_SC.md`.
- **B2/B3:**
  - the plan: `R/I93/b2b3_plan_01/`;
  - B2-C, final for J1: `R/I97/b2_c_01/` (CONTRACT, REVISION_01, REVISION_02);
  - B3-D: `R/I96/b3_d_01/`.
  - B2-K's brief must carry SA4-1's midpoint conditions and the boundary vectors, and SC2's must carry B-1 (RR "RV115 and RV118 confirm B2-C revision 02: …").
- **The merge records:** `IMPLEMENTATION/*_MERGE/`; the redaction record is `IMPLEMENTATION/REDACTION_E16/`.
- **Terms:** `RESUME_2026-09-30/GLOSSARY.md`.

## The host (machine-local; check it)

| | |
|---|---|
| **Machine** | The M5 Max, 128 GiB. All heavy work runs here |
| **WT** | `<repo>/.claude/worktrees/swbpipe-control-layer-8a41be/.claude/t3` |
| **NUM** | `WT/numerics` |
| **B1's worktrees** | `WT/b1` (SP, SA and SR-RS, at I3), `WT/b1-r`, `WT/b1-p`, `WT/b1-t`. `WT/b1-a` holds SA, already merged at I2 |
| **DEC-025** | The candidate tree is `WT/sweep-skewpin`; the baseline tree is `WT/main-baseline`, still at an old main (`e33f3e2f1b`), so refresh it before any run. Run `WT/scratch/u9_dec025/run_dec025.sh` through `WT/tools/t3_exclusive.sh`. A run counts only when its `meta.txt` ends with `ALL-DONE` |
| **The memory guard** | `WT/guard/memguard.sh`, PID 29411 at handoff, with a floor of 22% free. Check it with `pgrep -f memguard.sh`. It must run during any heavy job |
| **Lock slots** | Four: `WT/guard/cargo_job.lock` and `cargo_job.slot{2,3,4}.lock`. Cargo goes through `WT/tools/t3_cargo.sh`, and other heavy commands through `WT/tools/t3_slot.sh`. A job starts only while T3 is under 52 GiB and at least 30% of memory is free. Exclusive mode (`t3_exclusive.sh`) takes all four slots |
| **The host screen** | `WT/tools/t3_host_screen.py <repo> --staged` or `<repo> <base> <head>`. It reads this machine's names at run time, plus earlier names from `WT/tools/t3_host_names.private.txt`, and prints only `<host>`. **Never commit, copy or quote that list** |
| **VENV** | `<repo>/.claude/worktrees/swbpipe-control-layer-8a41be/projects/chirality-piping/.venv` |
| **Cleanup** | `WT/tools/t3_cleanup.py`: `gather`, then `plan`, then `apply` (`IMPLEMENTATION/HANDOFF_2026-10-05/CLEANUP.md`). The merged worktrees waiting for it are listed in the graph's next safe action |
| **Disk** | About 979 GiB free at handoff |

## Open items for the owner

- **G10,** the native witness, needs the owner's Mac.
- **Owner-held, prepared:**
  - B2/B3's decisions 22–24;
  - M above 12 GiB;
  - whether main's earlier host-name exposure is cleaned from main's tree (RR "Erratum E-16: …" with its addendum, and the RV119 section's N-2).
