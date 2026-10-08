# B1, the reader follow-up toward I4′, PY's lane (I100)

Read `R/BRIEFS/B1_COMMON.md` and `R/BRIEFS/B1_SR_PY.md` first; their rules still hold, except where this brief changes the host rules. Then read:
- RV113's SR-PY addendum, `R/REVIEW_RV113/rvr_sr_py_01/ADDENDUM_01.md` (`a61bbe1b…`): §3, Findings S-1, N-1 and N-2, and "For ROOT";
- RV113's SR-RS addendum 02 §6 (`rvr_sr_rs_01/ADDENDUM_02.md`), for the metadata check's three shapes;
- RR "I4 made at `30f3d1b24a`; RV113's items for ROOT ruled; …". Rulings 1, 2 and 5 are your specification.

**You are I100, and the owner of B1's Python side through SC.** After this round, SC (`R/BRIEFS/B1_SC.md`) is yours too, as I-PY, the one corpus writer, by ROOT's message once I4′ is made.

## Where

- **`WT/b1-p`,** on `codex/piping-t3-b1-p-20261007`. ROOT has fast-forwarded it to I4 (`30f3d1b24a`), so it carries SP, SA and all three readers' rounds.
- **Your lane:** PY's reader files (`P/core/analysis_runs/retained_precision.py`, `compatibility.py`, and the `validate_transport_metadata` that the retained reader's transport path calls) and their tests under `P/tests`. Touch nothing in RS's or TS's lane, and no corpus file.

## What to change

1. **Ruling 1: PY's transport header takes Rust's order and codes, as TS did.** On transport:
   - drop the carrier branch: a `carrier_evidence` member alone is a metadata defect, refused at G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`, as in RS and TS;
   - check `source_block_recovery` before `contract_evidence`.

   Pin it with RV113's six transport probes as test rows: `h_carrier_present`, `h_carrier_and_quality_defect`, `h_carrier_and_recovery`, `n6_carrier_evidence_with_case_defect`, `h_recovery_and_evidence_null` and `n6_contract_evidence_null_and_source_block_recovery`. Each takes RS's and TS's gate and code. Correct the docstrings: the order is Rust's.
2. **Ruling 2, PY's side: compare withheld records as multisets.** On transport, a withheld record whose multiplicity differs between cases is refused at G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`, as in RS and TS (RV113's `t_withheld_duplicate_multiset`). Keep PY's extrema-number demand: it becomes the shared form.
   - If that `validate_transport_metadata` also serves a non-retained path, keep the change identical there and say which callers it reaches.
   - If PY's schema typing refuses any further shape that RS and TS admit, **report it to ROOT; do not change it.**
3. **Ruling 5 (RV113 N-2):** add a whole-reader row: a kernel reason on a case with no Run, expected G5 `ATTEMPT` with no cause.
4. **The record's correction:** your RETURN states that I91's REPAIR_02_ITEM4 §2 "declared" holds for raw reads only, and that ruling 1 supersedes it on transport. Sealed records are not edited.

**No change to any 07m verdict** is allowed. If one would change, stop and return.

## Evidence

- **The census over 07m:** 0 changes against I4 on all three verdicts, and 0 misses against the corpus's PY expectations.
- **RV113's probes** (`probes_ts1.json` and its metadata probes, from its addenda's records): PY's verdicts equal RS's and TS's at I4 on every header and metadata probe, except the declared raw G7 codes (B1_SC item 13). List any other difference.
- **pytest:** against I4, the only differences are your added or changed tests, listed.
- **Mutants:** one per new or moved check, each killed by an assertion.

## Host

- **The host rule is the four-slot rule** (RR "Owner decision: development jobs may use up to 64 GiB, …", as amended by "Owner clarification: 64 GiB is T3's own allocation; …"):
  - every cargo goes through `WT/tools/t3_cargo.sh` (`--locked --offline`);
  - every heavy pytest, vitest or test binary goes through `WT/tools/t3_slot.sh <command>`;
  - pytest under `P/tests` sets `OPENPIPESTRESS_CHECKED_JSON_BIN` and `OPENPIPESTRESS_UNITS_BIN` to your own builds, or runs in a slot (RV104 N-6).
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job.
- **Python:** `WT/venv/bin/python`.
- **Paths:** absolute paths only, with your shell working in `WT/scratch/i100_b1_i4p_py/`; targets in `WT/targets/i100-b1-i4p-py/`.
- **Records:**
  - no symlink, and no folder named `build`;
  - remove the `hostname` attribute from junit output;
  - screen with the strict pattern and the machine's host name, decompressing `.gz` files;
  - run `git status --ignored`, and force-add any sealed file an ignore rule hides.

## Output

- **Commit** on `b1-p`'s branch in `WT/b1-p`, with a truthful message. ROOT pushes.
- **The record:** `R/I100/b1_i4p_py_01/RETURN.md`, with `_run_records/` and SHA256SUMS.
- **Budget:** 2–3 h.
- **End your turn with:**
  - the new head;
  - RETURN.md's sha256;
  - per item, the change and its evidence;
  - the census and suite deltas;
  - the mutants;
  - any shape PY refuses that RS and TS admit.

**After you return:** RV120 confirms this round. While it does, you may prepare SC's 07n in your scratch by `R/BRIEFS/B1_SC.md`, but commit nothing for SC until ROOT tells you I4′ is made.
