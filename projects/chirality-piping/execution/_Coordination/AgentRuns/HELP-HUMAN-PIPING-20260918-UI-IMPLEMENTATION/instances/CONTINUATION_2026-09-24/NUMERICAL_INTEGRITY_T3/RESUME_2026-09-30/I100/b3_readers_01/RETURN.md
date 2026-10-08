# I100 B3 readers (PY): B3a and B3b

TASK (Type 2), I100 (I-PY), for ROOT (HELP_HUMAN, Agent 0), the return path. I made no delegation. 2026-10-08 UTC.

**Basis** (each verified before use):
- `R/BRIEFS/B3_READERS.md`, sha256 `185ba738adb64c7bf416eb7675128f4488d5ab76647f5d3b23cd4739c38eee4b`;
- I93's PLAN §1.3–§1.4 and REVISION_01 (`R/I93/b2b3_plan_01/`);
- I96's B3-D, DESIGN.md with REVISION_01 (`R/I96/b3_d_01/`: SHA256SUMS 11 of 11, SHA256SUMS.revision_01 20 of 20). The `statics/r1` files equal `b2`'s: DEF-E `71f63d39…`, H `5a3bac43…`; XTABLE `c4987e87…`;
- RR "RV116 (RV-D) accepts B3-D …", "RV116 confirms B3-D's revision 01 …", "I99's B3-W verified …", and the dispatch "Lane A returned; `b2` built …".

**Placeholders:** `WT`, `NUM`, `P`, `R`, `VENV`; `S` = `WT/scratch/i100_b3r`.

## Result

**HEAD = `9ec1a736eb`** on `codex/piping-t3-b2-p-20261008` in `WT/b2-p`, over `e67c364680`. Not pushed.

| Commit | What |
|---|---|
| `8263a38a64` | **B3a.** G8's namespace is type-strict. Branch L is 0.1.0/0.2.0 with `pressure_contract` absent or null; branch L3 is 0.3.0 with exactly `{1.0.0, legacy_pressure_v1}`. 0.3.0 without that contract is refused (B3D-10). |
| `ac0598f64f` | **B3b.** The `<physics-retained>` branch, plus S-1 (detailed below). |
| `e33c783721` | `FRESH_CONTRACT_IDS` left unchanged (note 1). Adds the G8 step-order controls and the G-hat forgery shape. |
| `7175329c41`, `dc0cc5ee8c` | Tests only: shapes aligned with RS's, and the record checks made assertions. |
| `1149d79bb2` | **Merge of `b2` at `56e44fa081`** (lane P's B3b-P), as I101 merged it into `b2-r`. Product physics and the two m3x fixtures; no Python. |
| `9ec1a736eb` | Tests only: the pins on lane P's m3x successors. |

Against `b2` `56e44fa081`, the head differs in exactly four files: `retained_precision.py`, `compatibility.py`, `test_retained_precision_contract.py` (D31) and the new `test_retained_precision_b3.py`.

**The B3b branch** (B3-D §6 with REVISION_01; no new failure code):
- **Dispatch:** one route descriptor, chosen once at G0 from the identity.
- **G0:** §2.4 steps 3–9:
  - XTABLE's identity and profile;
  - H(DEF-E) and the one bound definition, refused with `FORMATION_MISMATCH`;
  - the bytes and the inherited physics-1 hash;
  - the table/constant cross-check;
  - the body's policies, canonicalization and limits read from the table;
  - each attempt's definition id.
- **S-1:** the route's definition hash at G1 and G8 (PY `:364`, now `_preparation_payload(a, route H)`).
- **G5b:** the owner entry's `pipe_sections` match bit for bit: As, Z, I, J, ro, OD and the effective wall.
- **G7:** the projection onto physics-1, then its unchanged validator. On transport, physics-1's metadata check runs, with its code at G7.
- **G8:**
  - the exact namespace;
  - the base E/ν only;
  - E, G-hat = RN64(E/(2·RN64(1+ν))) and `derived_e_nu`;
  - S-C (`physics_source._actual_materials` and `_canonical_inputs`, used as they are, with their code as detail only);
  - N-6;
  - regions present and `[]`, with no `equivalent_static` or `analysis_state`;
  - route `exact`;
  - the old tuple bound to E and G-hat.
- **`compatibility.py`:**
  - the exact identity, hash and path;
  - `_is_retained` covers both successors. Dispatch, standing, the classification summary, binding refusal, F-5 and the AnalysisRun record (receipt carried, no `contract_evidence`) all follow from that.
- **`physics_source.py`** is unchanged.

**Bases:**
- **Synthetic:**
  - m3l: the milestone successor on I99's m3l request.
  - m3x: the milestone successor re-expressed on I99's m3x request, with physics-1 evidence stating the prepared section. With ν = 0.25, G-hat equals the milestone's G bit for bit.
- **Lane P's producer-solved m3x successors.** B3b-P landed on `b2`, and I merged `b2` at `56e44fa081` into this lane (`1149d79bb2`), as I101 did for RS.
  - Pinned: document `02465c6c…`/`31f10f04…`, receipt `b1b4a668…`/`eabd2fc5…`.
  - Both modes are eligible with their invocation, in the milestone's classes (25/69/3/1 and 25/69/3/2), and these equal the synthetic base's class for class.
  - Every B3b shape is also read on them.
- **Not available yet:** B3a's m3l has no producer fixture (PP: "B3a's m3l needs no producer change"), and there is no `m3x_mix_anchor` fixture.

## Census (R5)

- **The corpus at `e67c364680` is 07m** (`c21112fd…`, 339 entries); `b2` is from I4′.
  - PY at `e67c364680` equals I4′'s 07m census on all 339 entries.
  - At B3a and at the head: **0 changes** against `e67c364680`, and against I4′.
- **07n** (`ea113e7b…`, from `b1` `09fe4cc69b`, 638 entries) was run in a scratch tree:
  - `e67c364680`'s reader equals SC's acceptance verdicts with 0 differences;
  - at B3a and at the head, **0 changes**.
  - So B3D-10's condition holds, and its tightenings are adopted.
- The reader files are unchanged after `e33c783721`, where the head census ran.

## Suites

I83's 27 files plus `test_physics_source_contract.py`. At the head, also the new `tests/test_retained_precision_b3.py`. Compared test by test:

| | Passed | Skipped | Failed |
|---|---|---|---|
| `e67c364680` | 2,020 | 30 | 0 |
| `7175329c41` | 2,209 | 30 | 0 |

- **Added:** 189, all passing.
- **Removed:** 0.
- **Outcome changed:** 0.
- **One existing test body changed, as ruled:** `test_model_schema_versions_d31`. Under B3D-10, 0.3.0 now needs the legacy contract.
- **After `7175329c41`, the only Python file that changed is B3's test file.** At `9ec1a736eb` it runs 327 tests, all passing; with the two existing tests it touches, 329 passed. That is 2,347 by composition.

## Mutants

- **47 mutants,** one per new check: 7 for B3a and 40 for B3b (`mutants/TABLE.json`).
- **All 47 are killed by an assertion** in B3's test file or the D31 test. The control passes all 328 tests at the head's test file.
- **Two kills needed added shapes:**
  - x26 kills B31 (the G-hat binding). It is a receipt G-hat one ulp high, with every copy made consistent.
  - The step-order test kills B32 (ν's unit and range at step 4, before S-C).
- A1 to B39 ran on the test file at `e33c783721`. B31, B40 and the control ran at the head's test file; tests added since can only add kills.

## Shapes for the three-reader comparison

**`_run_records/shapes/b3_shapes.json.gz`:**
- **8 bases:** milestone, m3l, the synthetic m3x and lane P's m3x (`m3xp`), each in both modes.
- **318 shapes** in 07n's grammar, plus `definition_sha256`. That is the hash the format rule's preparation step uses: DEF-E's on m3x and m3xp, otherwise DEF-O's. Entry 11 deliberately uses DEF-O's on the exact bases.
- Every shape re-materializes from the file, byte-equal to the test module's construction.

**The sets:**
- **B3a:**
  - m3l: the base plus 12 mutations;
  - branch L on 0.1.0 and 0.2.0: `{}`, `false`, `[]`, `""`, `0`, legacy, and null (must-pass);
  - 0.3.0 bare.
- **B3b:**
  - REVISION_01 §4.3's entries 1–32;
  - x01–x32, which include each of I101's RS-only shapes;
  - p01, an authored redundant G (must-pass);
  - each set on both m3x and m3xp.
- `SHAPES.tsv` has one line per shape. `RS_LABEL_MAP.tsv` maps each RS label to its PY shape.

**`py_b3_shapes.jsonl.gz`:** PY's bound, unbound and transport verdicts in RV113's line format. Every bound verdict equals the stated expectation. The bound tally:

| Verdict | Shapes |
|---|---|
| G0 `SOURCE_PRODUCER_CONTRACT_UNSUPPORTED` | 54 |
| G1 `RECEIPT_MISMATCH` | 4 |
| G5b `SECTION_MISMATCH` | 52 |
| G7 (base code) | 16 |
| G8 `INVOCATION_MISMATCH` | 88 |
| G8 `PREPARATION_MISMATCH` | 90 |
| Pass, eligible | 14 |

There are no escapes.

**Three readers on identical bytes:**
- I ran PY at `9ec1a736eb` on I101's 159 RS-materialized inputs (`WT/scratch/i101_b3r/out/final/rs_inputs.jsonl`; the sha256 values are in `shapes/i101_inputs.sha256`). I compared the three readings with RS's and TS's readings of the same lines: **0 differences** outside G7's per-language base codes (`shapes/PY_ON_I101_INPUTS.json`).
  - I101's own `CMP_THREE.json`, on my `e33c783721`, says the same.
  - PY's G7 base code is `SOURCE_PHYSICS_EVIDENCE_INVALID`, with physics-1's detail. RS uses `SOURCE_PHYSICS_*` and TS `PHYSICS_EVIDENCE_*`.
- Every RS label also has a counterpart in my set, with the same gate and code.
- **No disagreement to send.**
- For RS and TS to read my 318 shapes, the same inputs in I101's line format are at `S/tmp/b3_inputs_i101_format.jsonl` (scratch only, not a record).

## Notes for ROOT (no stop)

1. **`FRESH_CONTRACT_IDS`:** the exact successor is not added. RS's `FRESH_IDENTITIES` leaves it out, and the rule is one static set in every language. Adding it would also change `test_preview_physics_consumer_contract`'s pin. Standing is the reader's either way.
2. **Entry 22** (a combination): PY refuses it at G8 `INVOCATION_MISMATCH`, as RS does. REVISION_01 §4.3 notes this depends on B2-C's G3 placement.
3. **A preview-branch difference that predates B3:** RS's G8 refuses `analysis_state` in a sourced case and PY's does not; TS checks `pressure`. The exact branch refuses `analysis_state` in PY, as in RS.
4. **Host:** fresh authorities under `WT/targets/i100-b3r-auth`. Every heavy job went through `t3_slot.sh`, one at a time, with one wait each. Nothing else was signalled.
