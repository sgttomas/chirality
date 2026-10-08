# B1, the reader follow-up toward I4′, RS's and TS's lanes (I101)

Read `R/BRIEFS/B1_COMMON.md`, `R/BRIEFS/B1_SR_RS.md` and `R/BRIEFS/B1_SR_TS.md` first; their rules still hold, except where this brief changes the host rules or widens TS's fence. Then read:
- RV113's SR-RS addendum 02, `R/REVIEW_RV113/rvr_sr_rs_01/ADDENDUM_02.md` (`c43317f8…`): §5, §6, Findings S-1 and N-1, and "For ROOT";
- RV113's SR-TS addendum 01, `R/REVIEW_RV113/rvr_sr_ts_01/ADDENDUM_01.md` (`5f86b3e7…`): Findings S-1 and N-1;
- RR "I4 made at `30f3d1b24a`; RV113's items for ROOT ruled; …". Rulings 2, 3 and 4 are your specification.

**You are I101, and the owner of B1's Rust and TypeScript reader sides through SC.** After SC writes 07n, you update I-RS's and I-TS's harness pins and counts, by ROOT's message.

## Where

- **RS:** `WT/b1-r`, on `codex/piping-t3-b1-r-20261007`.
- **TS:** `WT/b1-t`, on `codex/piping-t3-b1-t-20261007`.
- ROOT has fast-forwarded both to I4 (`30f3d1b24a`).
- **Your lanes:**
  - RS: `RE/src/retained_precision.rs` and `RE/tests/retained_precision_contract.rs`;
  - TS: `retainedPrecision.ts`, `previewPhysicsEvidence.ts` and their tests. **Ruling 3 widens TS's fence to `previewPhysicsEvidence.ts`** and its test.
- Touch nothing in PY's lane, and no corpus file. Commit RS's work in `WT/b1-r` and TS's in `WT/b1-t`, never across.

## What to change

1. **Ruling 2, RS's and TS's side: the extrema-number demand on transport.** In RS's `preview_physics_transport_metadata` and TS's `validatePreviewPhysicsTransportMetadata`, each case's `global_upper_bound_pa` and `certified_gap_pa` must be finite JSON numbers. Refuse a non-number, null included, at G7 `SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`, as PY does (RV113's `t_extrema_global_upper_string` and `t_extrema_certified_gap_null`). Keep the duplicate-withheld refusal: it is the shared form.
   - TS's check also serves `StressNeutralExportPanel.tsx`. Keep it one function, and say in your RETURN which callers the change reaches.
2. **Ruling 3: TS's raw extrema typing.** In `previewPhysicsEvidence.ts` `validatePreviewPhysicsEvidence`, in the extrema loop, require both members to be finite numbers. Refuse a non-number at G7 with TS's raw base code (`SOURCE_PREVIEW_PHYSICS_EVIDENCE_INVALID`). RS's raw code for it stays `…NUMBER_INVALID`, a declared per-reader raw code (B1_SC item 13).
3. **Ruling 4: RS's twelve unpinned checks (RV113 S-1).** Add one test row per check, each breaking that conjunct alone:
   - `ca_precondition_beside_run`;
   - a `ca_receipt_phase_*` row with `receipt_encoding`;
   - `cb_facade_no_run`;
   - the nine metadata probes RV113 names (N45, N47, N48, N56, N58, N60, N63, N64 and N65).

   Test-only for this item.
4. **RS's doc comment (RV113 N-1):** the metadata check is TS's, check for check, and since ruling 2 it shares PY's extrema demand. Say exactly that.

**No change to any 07m verdict** is allowed. If one would change, stop and return.

## Evidence

- **The census over 07m:** 0 changes against I4 on all three verdicts, in RS and in TS, and 0 misses against the corpus's expectations.
- **RV113's metadata probes** (its 41, from `rvr_sr_rs_01/addendum_02/`), and its `probes_ts1.json` (`rvr_sr_py_01/addendum_01/probes/`):
  - RS equals TS on every transport verdict;
  - both refuse the two extrema shapes at G7 on transport;
  - TS refuses them bound and unbound at G7.

  List any other change from I4.
- **cargo test and vitest, with tsc:** against I4, the only differences are your added or changed tests, listed.
- **Mutants:** one per new check, each killed by an assertion. RV113's twelve mutants are now killed by your rows.

## Host

- **The host rule is the four-slot rule** (RR "Owner decision: development jobs may use up to 64 GiB, …", as amended by "Owner clarification: 64 GiB is T3's own allocation; …"):
  - every cargo goes through `WT/tools/t3_cargo.sh` (`--locked --offline`);
  - every heavy vitest, pytest or test binary goes through `WT/tools/t3_slot.sh <command>`.
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job.
- **vitest needs `node_modules`.** ROOT has none in `WT/b1-t`. Link `P/node_modules` to a checkout whose `package-lock.json` is byte-identical to `WT/b1-t`'s; ROOT names one in your dispatch. Run no install. Remove the link before you commit, and record that you did.
- **Paths:** absolute paths only, with your shell working in `WT/scratch/i101_b1_i4p_rs_ts/`; targets in `WT/targets/i101-b1-i4p-rs-ts/`.
- **Records:**
  - no symlink, and no folder named `build`;
  - remove the `hostname` attribute from junit output;
  - screen with the strict pattern and the machine's host name, decompressing `.gz` files;
  - run `git status --ignored`, and force-add any sealed file an ignore rule hides.

## Output

- **Commits:** RS's on `b1-r`'s branch, and TS's on `b1-t`'s, with truthful messages. ROOT pushes.
- **The record:** `R/I101/b1_i4p_rs_ts_01/RETURN.md`, with `_run_records/` and SHA256SUMS.
- **Budget:** 3–4 h.
- **End your turn with:**
  - the two new heads;
  - RETURN.md's sha256;
  - per item, the change and its evidence;
  - the census and suite deltas, per reader;
  - the mutants;
  - the callers each changed check reaches.
