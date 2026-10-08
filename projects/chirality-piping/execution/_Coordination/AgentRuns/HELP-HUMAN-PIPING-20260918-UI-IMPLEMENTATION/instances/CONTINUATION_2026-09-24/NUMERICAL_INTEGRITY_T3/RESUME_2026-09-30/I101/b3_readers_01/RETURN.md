# I101: B3's readers (RS, TS) and lane T's carriers

TASK (Type 2), I101 (I-RS, I-TS and lane T), for ROOT (HELP_HUMAN, Agent 0), the return path. I made no delegation. 2026-10-08 UTC.

**Basis:**
- `R/BRIEFS/B3_READERS.md` (sha256 `185ba738…`, verified);
- I93 PLAN §1.3, §1.4 and decision 21;
- B3-D `R/I96/b3_d_01/` with REVISION_01 (sums verified);
- RR's RV116 rulings and "I99's B3-W verified; …";
- lane P's Part 1 (`b2` at `56e44fa081`).

ROOT's mid-turn item, the G8 sourced-case alignment, is in `ADDENDUM_01.md`.

**Placeholders:** WT, P, R; RE = `P/core/reporting/result_export`; PP = `P/core/product_physics`; DT = `P/apps/desktop`.

## Heads (not pushed)

| Lane | Head | Commits over `e67c364680` (first parent) |
|---|---|---|
| RS, `WT/b2-r` | **`c845e899da`** | `977b317d05` B3a; `bc78c508a0` B3b; `d53ef81f72`, `54a72e3a68` shapes, readings, derivative; `2c6629b918` merge of `b2` at `56e44fa081`; `b2b58699bb` m3x pins; `3c2030b094` shapes 23b, 25b; `c845e899da` addendum 01 |
| TS and lane T, `WT/b2-t` | **`77aaaa61d1`** | `faa6ac2058` B3a; `a89e289aa3` B3b; `cc203b7d61` route `retained_physics` and the `outputPolicy.ts` entry; `40572427e0` carrier branches; `9b6342295d` merge of `b2` at `56e44fa081`; `8376677e07` m3x pins; `0ab8a63288` merge of `b2-r`; `36823f5b2d` the golden; `9a580c6704` shapes 23b, 25b; `5ddb2a3eac` addendum 01; `77aaaa61d1` merge of `b2-r` at `c845e899da` |

- **Merging:** `b2-t` contains `b2-r` (the golden's RE test needs RS's reader), so merging `b2-t` alone brings both lanes. No merge conflicted.
- **Lane T:**
  - the three schemas' exact branches, with `CARRIER_PROFILE_ENUMS.diff`'s two profile enums;
  - the `retained_physics` entry in `outputPolicy.ts`, with its own reason and its test;
  - the `SourceContract` union member;
  - **the golden** `retained_precision_exact_successor_derivative_{sparse_interactive,dense_scrutiny}.json` (`79d99305…1ff8`, `32b4182c…a891`), with three RE tests. **TS's `deriveResultDocument` reproduces both goldens byte for byte.** The T6S-2 goldens regenerate byte for byte.
- **Host screen** (`WT/tools/t3_host_screen.py`): 0 hits on both ranges (RS 15 files, TS 44 files).

## Census

The corpus at `e67c364680` is **07m, not 07n** (sha256 `c21112fd…6807`, the same at every head). I compared RV113's unchanged harnesses with I100's I4′ 07m census over 339 entries, reading each in full.
- **07m: 0 changes** in RS and TS at `b2`, after B3a, after B3b and at both final heads.
- **07n:** 0 changes at the final heads; see `ADDENDUM_01.md`.

## Suites against `e67c364680`, test by test (final heads)

| Suite | `e67c364680` | Head | Differences |
|---|---|---|---|
| RE at RS's head | 196 ok | 202 ok | +6 added |
| RE at TS's head | 196 ok | 205 ok | +9 added (RS's 6, the golden's 3) |
| Desktop vitest | 3,637 passed | 3,677 passed | +41 added; 1 renamed (D31) |
| `tsc --noEmit` | rc 0 | rc 0 | — |
| PY carrier-schema set (12 files) | 1,202 passed, 29 skipped | 1,205 passed, 29 skipped | +3 added |

**Declared changes:**
- **d31/D31** (B3D-10): 0.3.0 without a contract moves from admitted to G8 `INVOCATION_MISMATCH`.
- **PY carrier-order pins** now end with the exact successor.
- **T6S-2's test bodies** became helpers over a golden set. Names, checks and golden bytes are unchanged.

## Mutants (one per new check; each kill is a failing assertion)

| Set | Head | Killed |
|---|---|---|
| RS, B3a and B3b | `b2b58699bb` (survivors rerun at `c845e899da`) | 39 of 43 |
| TS, B3a, B3b and the route | `36823f5b2d` (survivors rerun at `77aaaa61d1`) | 43 of 47 |
| PY carrier schemas (lane T) | `36823f5b2d` | 12 of 12 |

- **B25 is killed by shape 23b.** In 23b a case names a point equal to the base, with the receipt's selector named alike. Only G8 step 3 refuses it.
- **Four survivors are equivalent in both readers:**
  - **B06b** drops step 6's call. The packaged XTABLE is hash-pinned at G0, and B06a kills the function on drifted tables.
  - **B28** drops step 4's E bits. The receipt's E is bound at G8, with the same code, to its copies in the id-map members, the prepared old sources and the operational inputs. The sources' native hashes, which the 07e rule does not reseal, bind those copies in turn. I traced it in RS: shape 25b, and a probe carrying E into every copy, are refused by those bindings with B28 applied.
  - **B29** drops step 4's Ĝ bits. The check is implied by N-6, G7's G binding and S-C.
  - **B30** drops step 4's Poisson unit. S-C refuses the same unit with the same code (32b).
- **Run note:** the first TS run's parser missed vitest's coloured failure lines. I re-read the logs with the colour codes stripped (`ts_reparsed.jsonl`).

## The three readers on one shape set

There are **165 shapes on 5 bases**: the 3 synthetic exact successors and **lane P's two m3x successors**.
- **The synthetic base `ordinary_prepared_synthetic` and each m3x successor:** 54 shapes each. These are the base, 52 rows and S-1's entry 11. The 52 rows are REVISION_01 §4.3's 30 row entries and 22 added shapes.
- **The two other synthetic bases:** the base only.
- **Entry 9:** on the relabelled preview base.

RS's and TS's materialized inputs are equal. PY (I100's `b7721d27e9`) read RS's inputs.

**RS = TS = PY at every gate and code, except G7, in all three readings.** At G7 each reader gives its own base code (12 triples). There are no disagreements.

Bound readings:

| Result | Shapes |
|---|---|
| eligible | 5 |
| G0 | 40 |
| G1 | 3 |
| G5b | 36 |
| G7 | 9 |
| G8 | 72 |

No shape is eligible unbound or on transport.

**Through the producer:** PP's 20 B3 tests pass at TS's head.
- m3x validates at precommit in both modes, on the private driver and on the Direct entry.
- m3l validates through RS's B3a (`precommit=None`).

## Stops and open points

1. **Fresh-identity sets.** physics-retained-1 is in none of RS's, TS's or PY's static sets; I changed none, and I100 pins PY's as unchanged. The policy entry admits result-export and stress-neutral at eligible standing, but the Current builders refuse non-fresh identities. Both panels therefore stay closed to the exact successor until ROOT rules. The golden and its TS parity do not depend on this.
2. **m3l has no committed fixture.** B3a's reader tests stay on synthetic receipts. The producer's m3l witness is PP's own test.

## Host

- **Jobs:**
  - Every cargo run went through `WT/tools/t3_cargo.sh --locked --offline`, with targets `WT/targets/i101-b3r-{b2h,b2s,r,t,mut,pp,pyh}`.
  - All other heavy work went through `t3_slot.sh`, in archive copies.
  - One heavy job ran at a time, with one wait at a time; I stopped and restarted my own timed-out waiters, never another job.
  - No DEC-025 and no installs.
- **Disclosed:**
  - (a) `chain_base` was launched detached with one waiter.
  - (b) The first two PY schema sessions let `conftest` build its two helper binaries (`cargo build --locked --release`) inside my slot job. Later sessions used binaries built once through `t3_cargo.sh` (`py_helpers.sh`).
  - (c) My first mutant launch failed at once (`cargo` not on the minimal PATH). I stopped it and relaunched it with the caller's PATH.
- **Junit:** hostname attributes were removed.

## Records

`_run_records/` holds `harness/`, `mutants/`, `census/`, `suites/`, `logs/`, `shapes/{final,final2}` and `addendum_01/`.
- `final` is the heads before the addendum (`b2b58699bb`, `36823f5b2d`); `final2` is the final heads.
- `mutants/logs` keeps the last log per label. The controls' and the five survivors' logs there come from the reruns at the final heads.
- `SHA256SUMS` covers every file.
