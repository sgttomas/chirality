# I100 — B3 readers, addendum 01: G8's sourced-case check on the preview route

TASK (Type 2), I-PY; return path ROOT. Lane head **`b7721d27e9`** on `codex/piping-t3-b2-p-20261008` (parent
`9ec1a736eb`, the accepted B3 return). One commit: the PY reader and its test. RS and TS are not edited; their change is
given to I101 as diffs (§3). Run records: `_run_records/addendum_01/` (sums in `SHA256SUMS.addendum_01`).

## 1. Reachability

Each shape sets one key on the milestone successor's sourced case (`request.model.load_cases[0]`) and reseals by the
07e format rule with DEF-O's H: 22 values × 2 modes = 44 probes (`probes.json`, sha256 `f113aab6…`). The three readers
read them through RV113's harnesses in probe mode, at b2-p `9ec1a736eb` (RS and TS there equal main's at this check).
**All 44 pass G0–G7 in all three readers**, so every key below reaches G8's sourced-case check in every reader (G0–G7
read the invocation only at G3, which compares case ids). Bound verdicts, the same in both modes:

| Key = value | PY | RS | TS | aligned |
|---|---|---|---|---|
| `analysis_state` = `{"kind":…}`, `null`, `{}` | pass | **G8** | pass | G8 |
| `pressure` = quantity, `0` | pass | pass | **G8** | pass |
| `pressure` = `null` | pass | pass | pass | pass |
| `pressure_regions` = `"x"` | G8 | **pass** | G8 | G8 |
| `pressure_regions` = `{"id":…}`, `1`, `true` | **G8** | pass | pass | G8 |
| `pressure_regions` = `{}`, `0`, `false`, `""` | pass | pass | pass | G8 |
| `pressure_regions` = `[]`, `null` | pass | pass | pass | pass |
| `pressure_regions` = one region | G8 | G8 | G8 | G8 |
| `equivalent_static` = `{}`, `false`, `0` | G8 | G8 | G8 | G8 |
| `equivalent_static` = `null`; `notes` (unknown key) | pass | pass | pass | pass |

G8 is `RETAINED_PRECISION_PREPARATION_MISMATCH`; pass is eligible. Today **18 bound readings differ**; unbound and
transport readings agree (G8 does not run). No reader refuses another case key at this check.

What a producer-emitted successor can carry (PP at the lane head): `PreviewLoadCase` (product_physics lib.rs:560) has
no `pressure` field and no `deny_unknown_fields`, and the invocation digest covers the raw request, so a successor
**can** carry a case-level `pressure`: TS refuses a receipt PP can emit. W1's admission (retained_memory.rs:876–895,
D1.5) refuses `analysis_state` other than `Absent`, so no successor carries one, `null` included: RS's clause is right.
A non-array `pressure_regions` fails PP's parse; `null` parses as `None` and is admitted.

Exact route: the same two clauses split the readers there. In RV113's census mode (bases read raw, so the
exact route's preparation hash stands), on the synthetic and lane P's m3x successors, both modes: `x08` (an
`analysis_state` member) PY G8, RS G8, **TS pass**; `p02` (a case-level `pressure`) PY pass, RS pass, **TS G8**; the
bases pass in all three (PY's exact arm is unchanged by `b7721d27e9`). Today 8 of 12 bound readings differ; with
the TS diff, 0.

## 2. The governing text

- DOMAIN D1.5 (`R/I65/u4_g2_01/DOMAIN.md`:18, sha256 `08a72dde…`): "for the one case: `pressure_regions` is `None`;
  `equivalent_static` is `None`; … `analysis_state` is `Absent`".
- C1's G8 row (`R/I32/f2a_wire_c1/WIRE_CONTRACT.md`:154, sha256 `c8ab2318…`): "… ordinary eligibility; no 0.4
  extension". `analysis_state` is the 0.4.0 load-reference state.
- C3_DELTA's G8 row (`R/I52/prepared_public_contract_02/C3_DELTA.md`:308, sha256 `fd00d2c1…`): "Existing raw
  invocation/mode/project/material/order/family/pressure checks" — named, not listed.
- D2 §4.9.3's G8 row (`T/DESIGN_STANDING/DESIGN.md`:546, sha256 `993f5f3a…`) does not state the case condition.
- B3D-11 (`R/I96/b3_d_01/DESIGN.md`:477, sha256 `ad7942f6…`): keep the `pressure_regions: []` leniency.

**No D-number added RS's `analysis_state` clause.** All three readers' clauses come from the reader drafts frozen in WIP
`ae97b7d5c2` (2026-10-03 handoff: I58 PY, I59 RS, I60 TS), carried into main by `5a0461661f`. The aligned rule is
D1.5 read through C1's "no 0.4 extension", with B3D-11's leniency: `pressure_regions` absent, `null` or `[]`
(type-strict); `equivalent_static` absent or `null`; no `analysis_state` member; a key PP's typed case lacks is not
read. ROOT may wish to rule it.

## 3. The change

PY (`b7721d27e9`), `_g8`'s preview arm (the exact arm already refused `analysis_state`):

```python
regions = case.get("pressure_regions")
need((regions is None or (type(regions) is list and regions == [])) and case.get("equivalent_static") is None
     and "analysis_state" not in case)
```

Test: `test_addendum01_sourced_case_on_the_preview_route` (the 22 values × 2 modes, bound, unbound and transport) and
B3b's `p02` (a case-level `pressure` on the exact route, synthetic and producer, both modes, must pass).

For I101 (`_run_records/addendum_01/diffs/`; not applied by me; rustfmt may reflow):

RS, against b2-r `b2b58699bb` (sha256 `cfd94449…`); the `analysis_state` clause is unchanged:

```diff
             } else {
-                list(&case["pressure_regions"]).is_empty()
+                // Preview route: absent, null or [] (B3D-11's leniency), type-strict (I100 B3 addendum 01).
+                case.get("pressure_regions")
+                    .is_none_or(|r| r.is_null() || r.as_array().is_some_and(Vec::is_empty))
             } && case["equivalent_static"].is_null()
```

TS, against b2-t `36823f5b2d` (sha256 `d4926986…`), both routes:

```diff
-    fail(c.id === s.owner.case_id && (route.exact ? Array.isArray(c.pressure_regions) && c.pressure_regions.length === 0 : !c.pressure_regions?.length) && c.equivalent_static == null && c.pressure == null);
+    const regions = c.pressure_regions;
+    fail(c.id === s.owner.case_id && (route.exact ? Array.isArray(regions) && regions.length === 0 : regions == null || (Array.isArray(regions) && regions.length === 0)) && c.equivalent_static == null && !Object.hasOwn(c, 'analysis_state'));
```

(plus a four-line comment). With both applied and PY at `b7721d27e9`, the 44 probes give **0 differing readings**.

## 4. Shapes, census, suites, mutants

**Shapes** (`_run_records/addendum_01/shapes/`, B3's format: 07n grammar plus `definition_sha256` and
`expected_python`): `add1_shapes.json` (sha256 `08d9ceba…`; gz `1afd891b…`): 6 bases (`milestone`, `m3x`, `m3xp` ×
2 modes) and 52 shapes: the 44 probes (DEF-O's H) and `x08`/`p02` on `m3x` and `m3xp` (DEF-E's H). Each re-materializes
from the file to the test module's construction. PY's verdicts in RV113's line format (`py_add1_shapes.jsonl`, 0 differ
from `expected_python`), I101's input lines (`add1_inputs.jsonl`), and `SHAPES.tsv`. The three readers' tables:
`readers/{today,aligned,exact_today,exact_aligned}_TABLE.tsv`.

**Census** (PY, b7721d27e9 against B3's base runs): 07m 339 entries, **0 changes**; 07n 638 entries, **0 changes**.

**Suites** (29 modules, the B3 module included): 2395 passed, 30 skipped. Against the pre-B3 base (2020 passed,
30 skipped): 0 removed, 0 changed, 375 added (all in the B3 module, all pass; 48 are this addendum's: 44 sourced-case
and 4 `p02`).

**Mutants** (guarded, in a copy of b7721d27e9; the B3 module, 375 tests): control 0 failed; C1 (`analysis_state`
admitted on the preview route) killed, 6 failures; C2 (`pressure_regions` read as falsy, the reading before the change)
killed, 8; C3 (any list admitted) killed, 2. Every failure is an assertion; no errors.

Host: one heavy job at a time through `t3_slot.sh` / `t3_cargo.sh` (`--locked --offline`; fresh targets
`WT/targets/i100-b3r-rs*`); readers in scratch archives; vitest with `node_modules` linked from `WT/sweep-skewpin`
(package-lock compared) and its wasm assets copied, the link removed after. No installs, no DEC-025.

## 5. Stop

None. The census changed nothing; the readers agree on every shape with the two diffs applied. Until I101 lands
them, RS and TS disagree with PY at b7721d27e9 on the preview shapes above, and TS with both on `x08`/`p02`.
