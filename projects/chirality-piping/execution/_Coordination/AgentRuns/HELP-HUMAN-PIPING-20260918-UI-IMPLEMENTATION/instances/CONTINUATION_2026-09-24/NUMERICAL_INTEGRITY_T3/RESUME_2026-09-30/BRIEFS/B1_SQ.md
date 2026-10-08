# B1-SQ: the re-qualification (Pass A): G5, G6 and the re-pins, the witnesses, the challenge, peak RSS and time

Read `R/BRIEFS/B1_COMMON.md` first, for records, Git and placeholders. Its host rules are replaced by this brief's. **You are I-A for SQ,** through RV-Q's review rounds and your repairs.

**The specification is PLAN_v2 §3.1 to §3.7** (`R/I84/b1_plan_01/PLAN_v2.md`, `c85786b7…`), with RV107's A1 amendments (B1_COMMON) and the items RR has routed to SQ since, listed below. M is ROOT's: R6a after your G5, and R6b after RV-Q's G6 review.

## Where

- **`WT/b1-q`,** branch `codex/piping-t3-b1-q-20261008`, cut by ROOT from `b1` at `57c92a7b33`. SP, SA, the three readers with their follow-up round (I4′), SC's corpus 07n and the readers' pins are merged there.
- **The production code is frozen there.** RV120's review of SC may still repair the corpus or the reader tests on `b1`, which ROOT merges into `b1-q`. Those touch none of your files. A product-code change after this point comes only by ROOT's ruling.
- **Your writes:**
  - the profile generator's output;
  - the registration diff;
  - the law tests' and the challenge's re-pins (§3.3);
  - the TEXT loop rules;
  - G-B's bound (item 3 below);
  - the guard item (item 6 below).
- **Stop and return** if anything else in PP, RE or the readers needs to change.

## Routed to SQ since PLAN_v2

1. **The inputs** (RR "I86's SW probe accepted; …", rulings 1 to 4). All are committed under `R/I86/b1_w_probe_01/_run_records/inputs/`:
   - `b2_k1e3.json` (`89b05619…`), W2b's replacement, asserting `Fallback("Candidate")`;
   - `c1.json` (`719acbb0…`), the c = 1 publishing cap-maximal input;
   - `i3_c1_case_{a,b,c}.json` and the assembled `i3_c1_three_case.json` (`d05b5996…`), the three-case input with |A| = 3.

   §3.6's stop line does not apply. `RSS_TIME.md` states what the published inputs leave below their caps.
2. **ST's renames** (RR "R3: I85's ST verified …", ruling 4). W2b's test is `witness_w2b_cap_maximal_passed_report_no_triggered_case`, and W6 uses case C's input.
3. **G-B's byte bound** (RR "RV112 passes SA; …", SF-1). Correct it to T11 minus one case's late capture: either emit a per-case late form, or use `F_T11_LATE_CAPTURE / C` with G5 asserting the form is exactly C × one case's. Carry with it:
   - the expression test's change and its re-pin;
   - N-1 and N-2: the runner literal tied both ways, and the parked-slot law test at C = 3, so that mutant G04 dies;
   - N-5: `capture_bytes` includes SP's parked-slot reservation, 2 × 1,560 B at C = 3.
4. **I89's value pins** (RR "I89's SA verified and ruled; …", item 4). Re-pin `TEXT_TEXT_DIAG_ENV`, L_PUB, L_DIAGID, Text(err), PushCap(D_env), D_env and Text(row). `law_tests::cap_maximal` does not solve.
5. **RV107 A1-N-3:** three more law tests to re-pin (`R/REVIEW_RV107/b1_plan_01/ADDENDUM_01.md`).
6. **E-12** (RR "RV109 passes SP in RV-P round 2; …", ruling 3). Either add `retained_product.rs` to `RULE8_FILES` with its site table, or record why its arithmetic lies outside rule 8's scope, so that a reviewer can check either.
7. **c ≥ 2 successors through the registered Direct entry** (same ruling, N-3) are candidate qualification inputs: the three-case input in both modes, and (A, C) in sparse.
8. **RS's new production loops** (RR "I90's SR-RS repair round 2 verified; …", item 2) join your TEXT-rule inventory: G3's loops over `sources` and `material_bases`/`case_indices`, and `g5_ordinary`'s per-case basis lookup.
9. **DEF-O's availability** (RR "RV115 confirms S-4 (a)'s soundness …", NC-1). On your cap-maximal inputs, measure the share of `SharperExact` fallbacks caused by:
   - DEF-O's mm→SI second rounding;
   - the support magnitude's nested hypot.

   Report only. ROOT decides any DEF-O revision.
10. **Optional (RR "RV109 confirms SP's I3 step …", N-2):** a Direct-entry variant with a fault armed, pinning the c ≥ 2 notice path.

## Measurements

- **Every RSS, peak-memory and timing measurement of the product runs through `WT/tools/t3_exclusive.sh <command>`.** This covers §3.4's peaks, §3.5's challenge and §3.6's runs (RR "Owner decision: development jobs may use up to 64 GiB, …", item 3). They run on a quiet host, against the product's 12 GiB cap.
- **One process per measurement, one mode per process,** with the binary run directly, as §3.6 states. Use 3 repetitions, and report the median and the maximum.
- **The target machines are 32 GB, with 16 GB "solving within practical timeframes"** (owner, 2026-10-07). `RSS_TIME.md` sets every peak beside them, as §3.6 states, with its non-claims.

## Host

- **Every cargo** goes through `WT/tools/t3_cargo.sh` (`--locked --offline`), in a fresh target under `WT/targets/sq-*`. **Other heavy commands** go through `WT/tools/t3_slot.sh <command>`. **Measurements** go through `t3_exclusive.sh`.
- **One heavy job of yours at a time;** one wait per job, ending when its process has gone. Never signal another job.
- **Not allowed:** DEC-025 and installs.
- **Python:** `WT/venv/bin/python`.
- **Paths:** absolute paths only. Scratch goes in `WT/scratch/i104_b1_sq/`.
- **Records:** placeholder paths only, no symlink, and no folder named `build`. Remove the `hostname` attribute from junit output.

## Output

- **Commits** on `codex/piping-t3-b1-q-20261008` in `WT/b1-q`, with truthful messages. ROOT pushes, merges into `b1`, and applies the registration after R6b.
- **The record:** `R/I104/b1_sq_01/`:
  - `RETURN.md`;
  - `QUAL_B1.md`, in QUAL's form;
  - `RSS_TIME.md`;
  - `registration.diff`;
  - `_run_records/` and SHA256SUMS.
- **Keep the prose short.** The tables and logs carry the evidence.
- **Budget:** 17–25 h. At R6a, return with G5 and a proposed M before G6, so that ROOT can rule.
- **End each turn with:**
  - the head;
  - G5's E_mov,max + R per mode against the budget;
  - the proposed M;
  - what remains;
  - any stop.
