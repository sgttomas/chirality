# RV120 (RV-R): confirm B1's reader follow-up round toward I4′; then review SC

TASK (Type 2), an independent reviewer dispatched by ROOT (HELP_HUMAN, Agent 0). ROOT is your return path, and you do not delegate. **You are a fresh instance and wrote none of this change.** Build your own oracles where RV113's do not reach.

**You hold RV-R for B1,** succeeding RV113, who is not resumable from this session. Your scope:
- this round: I100's PY follow-up and I101's RS and TS follow-ups;
- then SC (corpus 07n), when ROOT sends it.

Keep your records so a later you can continue from the files alone.

## The candidates

The heads are filled in at dispatch.
- **PY:** `codex/piping-t3-b1-p-20261007` at `{PY head}`, in `WT/b1-p`, over I4 `30f3d1b24a`. The return is `R/I100/b1_i4p_py_01/RETURN.md`.
- **RS:** `codex/piping-t3-b1-r-20261007` at `{RS head}`, in `WT/b1-r`, over I4.
- **TS:** `codex/piping-t3-b1-t-20261007` at `{TS head}`, in `WT/b1-t`, over I4.
- RS's and TS's return is `R/I101/b1_i4p_rs_ts_01/RETURN.md`.
- **Read the returns after forming your own view.**

## The specification

- **RR "I4 made at `30f3d1b24a`; RV113's items for ROOT ruled; …":** rulings 1 to 5.
- **The briefs** `BRIEFS/B1_I4P_PY.md` and `BRIEFS/B1_I4P_RS_TS.md`.
- **RV113's three addenda,** whose findings these rulings dispose of:
  - `R/REVIEW_RV113/rvr_sr_py_01/ADDENDUM_01.md`;
  - `rvr_sr_rs_01/ADDENDUM_02.md`;
  - `rvr_sr_ts_01/ADDENDUM_01.md`.

  Their probe sets and harnesses are committed beside them. Reuse them; do not rebuild the plumbing.

## Confirm, in priority order

1. **The census over 07m, per reader:** 0 changes against I4 on all three verdicts.
2. **Ruling 1:** on RV113's six transport header probes, PY now gives RS's and TS's gate and code.
3. **Ruling 2:** on transport, all three readers refuse a duplicate withheld record, a non-number `global_upper_bound_pa` and a null `certified_gap_pa`, each at G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`. Check the callers of the changed checks, including TS's `StressNeutralExportPanel.tsx`, for any change of behaviour on producer-emittable inputs.
4. **Ruling 3:** TS refuses the two extrema shapes bound and unbound at G7.
5. **Ruling 4:** RS's twelve rows each kill RV113's matching mutant.
6. **Ruling 5:** PY's kernel-no-Run row exists and kills P31.
7. **The three readers agree** on RV113's 392 probes and its metadata probes, except the declared raw G7 codes (B1_SC item 13). List every other difference.
8. **Suites against I4, test by test, per reader:** the only differences are the added or changed tests.
9. **Mutants:** your own, beyond the implementers', on each new or moved check.

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--offline --locked`). **Other heavy commands** (pytest, vitest, test binaries) go through `WT/tools/t3_slot.sh <command>`.
- **vitest** runs as ROOT's I4 check ran it (`T/IMPLEMENTATION/B1_I4/`): a scratch archive with `node_modules` linked and the eight wasm assets copied, never inside a worktree.
- **One heavy job of yours at a time.** One wait per job, ending when the job's process has gone. Never signal another job.
- **Writes:**
  - absolute paths only;
  - your own copies and archives under `WT/scratch/rv120_rvr/`, with targets under `WT/targets/rv120-*`;
  - no record folder named `build`;
  - record paths are placeholders only.
- **Not allowed:** DEC-025, installs and Git writes.

## Output

- **The report:** `R/REVIEW_RV120/rvr_i4p_01/REVIEW.md`, with `evidence/` and SHA256SUMS. It gives:
  - a verdict per lane, CONFIRMED or NOT CONFIRMED;
  - the findings, each as BLOCKING, SHOULD-FIX or NOTE.
- **Keep it short.** Give the result and the evidence; leave out narrative.
- **Budget:** 3–4 h.
- **End your turn with:**
  - the verdicts;
  - one line per finding;
  - the report's sha256;
  - anything ROOT must rule on.
