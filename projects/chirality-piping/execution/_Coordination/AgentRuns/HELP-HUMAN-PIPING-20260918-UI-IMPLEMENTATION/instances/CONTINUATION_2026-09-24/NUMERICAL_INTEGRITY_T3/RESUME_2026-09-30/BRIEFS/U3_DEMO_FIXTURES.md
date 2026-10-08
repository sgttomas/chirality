# I114: the app's demo results — replace those computed with the flawed joint and the legacy pressure (G10, D-3, RV127 S-1)

TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You are a fresh instance.** `R/BRIEFS/B1_COMMON.md`'s host, Git and records rules apply, with WORKING_ITEMS in ROOT's place. Production code: working, tested code on a branch, with a short record.

## Why

The owner retired the legacy pressure contract and, under M07 option A, the oracles of the flawed expansion-joint element. See RR "Owner decisions: the legacy pressure contract is retired product-wide; …" and RR "Owner decision: M07's flawed joint element, option A; U3 Stage 2 released".

The app's reference-only view and many tests still use bundled demo results computed with the flawed joint (C-150) and legacy nonzero pressure. The owner's direction, through ROOT:
- **Replace them** with results the current product computes from a valid demo model, one with no joint and no legacy pressure.
- **If that is impractical,** remove them and the view's dependence on them, and say which you did.

## The scope (`P/fixtures/product_preview/`)

| Fixture | Role |
|---|---|
| `invented_mechanics_result.json` | D-3: the demo's frozen result |
| `invented_mechanics_result_precision_1_{sparse,dense}.json` | G10: `apps/desktop/src/services/previewService.ts:639-646` loads them |
| `invented_mechanics_result_preview_physics_1_{sparse,dense}.json` | the demo's refusal envelopes |

Their consumers, from I110's inventory (`R/I110/pressure_retire_01/inventory.json`, D-3 rows) and I111's G10: 14 app unit-test files, 2 e2e specs, 6 Python tests, 2 RE sites and `core/product_preview/service.py`. Find every consumer yourself as well.

**RV127 S-1** (`R/REVIEW_RV127/u3_stage1_01/REVIEW.md`) is yours too. A nonzero legacy primitive keeps the pre-retirement text at `PP/src/pressure_runtime.rs:226-228`, which does not name `2.0.0/exact_straight_pressure_v2`. It was kept only so the preview-physics-1 pair stays byte-identical. Use the one re-author text for every value, and regenerate or replace that pair.

## The branch and the boundary

- **Branch:** `codex/piping-t3-demo-fixtures-20261008`, from `4c0d5d7c00` (U3 Stage 1). Make it in a new worktree, `WT/t3-demo`.
- **I110 works in parallel** on `codex/piping-t3-pressure-retire-20261008`. Its work covers Stage 1's repairs and Stage 2: the historical scope, O1–O4, the legacy computation, G11, and other refusal texts in `pressure_runtime.rs`. Edit only the lines above in that file.
- **Do not change `invented_preview_model.json` or the PP test fixtures.** They stay as the refused demo for PP's tests. Put the valid demo model in a new fixture; the joint-free `PP/tests/fixtures/preview_physics_invented_model.json` is a candidate starting point. Then point the app's demo and the consumers at it.
- WORKING_ITEMS merges your branch with I110's.

## The task

1. Choose and justify the valid demo model: no joint and no legacy pressure. It needs exact pressure only if the view needs pressure.
2. Generate its results with the current product, through the same generators that made the old fixtures (`preview_physics_fixture_generation.json` and its kin), and record the generation.
3. Point every consumer at the new fixtures, and update the tests' expectations from the product's output, never by hand.
4. Make S-1's text change and regenerate the refusal pair.
5. Run vitest, the 2 e2e specs if the host can (otherwise say so; Linux CI will), the Python tests, RE's tests and PP's tests touched by S-1.

**Stop** if the view cannot work with a valid model without a design change. In that case give the removal option and its consequences.

## Host and records

- Targets go under `WT/targets/i114-*`, scratch in `WT/scratch/i114_demo/`. Cargo goes through `WT/tools/t3_cargo.sh`; vitest and pytest go through `WT/tools/t3_slot.sh`. No DEC-025 and no installs. If `node_modules` is missing, clone it copy-on-write from a T3 tree with the same lockfile, as I110 did.
- Commit on your branch, product files only, with truthful messages. Records go in `R/I114/demo_fixtures_01/` (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a file, put its content in your final message.
- Budget: 4–6 h.

End your turn with:
- the head and commits;
- the model chosen;
- the fixtures replaced or removed;
- the consumers changed;
- the suites;
- any stop.
