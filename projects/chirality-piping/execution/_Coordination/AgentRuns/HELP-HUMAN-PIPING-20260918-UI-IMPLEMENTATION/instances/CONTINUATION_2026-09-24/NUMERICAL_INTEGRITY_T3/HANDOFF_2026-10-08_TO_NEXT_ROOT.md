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

**Updated at handoff (2026-10-08, late):**
- **#1114 is merged,** and so are **E-19's redactions** (#1120, #1123) and **the private-term check** (#1118). NUM has absorbed main at `fb329f31e7`. The rulings section is "E-19 done: …".
- **RV113's three confirmations are verified and committed,** SR-PY's with its pre-commit redaction.

1. **I4 is unblocked.** RV113 CONFIRMED all three readers' rounds. Merge `b1-r` (`6e3e4fe219`), `b1-p` (`2843a59a16`) and `b1-t` (`6fa6a64658`) into `b1` (`03f55e7178`). Then fill `{I4 commit}` in `BRIEFS/B1_SC.md` and dispatch SC.
   - RV113's three items for ROOT (RR "#1114 merged; …") do not block I4.
2. **PR [#1124](https://github.com/sgttomas/chirality/pull/1124) is merged** (`015f9763ea`, by the owner): records-only PRs now run only the governance harness. NUM absorbed it.
3. **The next records PR** carries NUM's records after `dc4ffdc7c8` (the work graph's next safe action 3).

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
- **The merge records:** `IMPLEMENTATION/*_MERGE/`; the redaction records are `IMPLEMENTATION/REDACTION_E16/` (on NUM) and `IMPLEMENTATION/REDACTION_E19/` (on main).
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
- **Git identity:** set `user.email` in the repository's config on both Macs (RR "E-19 done: …"). Until then, the private-term check blocks any PR whose commits carry git's automatic host-derived email.
- **Owner-held, prepared:**
  - B2/B3's decision 23 (R-2, for B8) and 24 (the native witnesses);
  - **decision 22, reframed** as a machine-adaptive memory budget. Prepare a design study after PR-B1 (RR "#1114 merged; …").
- **A-S1:** the earlier host-name form, and E-16's, E-10's and E-19's originals, stay publicly retrievable from Git history, NUM's pushed branch and earlier PR commits. The owner has been told; anything further is the owner's call.
