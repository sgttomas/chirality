# RV128: the fresh independent review of U3's demo-fixture lane (G10, D-3, RV127 S-1)

TASK (Type 2), an independent reviewer dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You wrote none of this.** `R/BRIEFS/B1_COMMON.md`'s host, records and placeholder rules apply, with WORKING_ITEMS in ROOT's place.

## The candidate

- **Branch:** `codex/piping-t3-demo-fixtures-20261008` (`WT/t3-demo`), head `180bf9b26d`. It is two commits on `4c0d5d7c00` (U3 Stage 1):
  - `ff9d3b7d6e`: RV127 S-1. One re-author text for every legacy primitive.
  - `180bf9b26d`: the valid demo model `invented_demo_model.json` (no joint, no legacy pressure), its regenerated results replacing those computed with the flawed joint and legacy pressure, and every consumer.
- **The direction:** the owner's M07 decision (option A), relayed by ROOT (RR "Owner decision: M07's flawed joint element, option A; U3 Stage 2 released"). G10 and D-3 replace the bundled demo results with results the current product computes from a valid demo model.
- **The implementer's record:** `R/I114/demo_fixtures_01/RETURN.md`.

## Review, in priority order

1. **Provenance.** Every replaced fixture is the current product's output for the stated model and mode, produced by the recorded generator and recipe. Regenerate at least the precision-1 pair and the preview-physics-1 pair yourself and compare the bytes.
2. **The model is valid and honest.**
   - It contains no joint and no legacy pressure.
   - It equals PP's joint-free model except for its identity.
   - The app's view describes it truthfully: a reference, not a solve of the current model.
3. **The consumers.** Every test expectation that changed comes from the product's output, not from hand edits.
   - No test was weakened: no assertion was removed without an equivalent, and no tolerance was widened.
   - Name each "empty state" assertion, such as the comparison workspace's 0 pairs, and judge whether it is still meaningful.
4. **S-1.** One re-author text for every value, naming `2.0.0/exact_straight_pressure_v2`, and the refusal pair regenerated.
5. **I114's notes for WORKING_ITEMS (§6).** Give your view on each:
   - the stale generation records after merging with I110's lane;
   - the app's default session model is still the refused demo;
   - the derived carrier;
   - the comparison workspace throws on preview-physics-1 combination rows.

## Host and output

- Use an archive copy in `WT/rv128/`. Targets go under `WT/targets/rv128*` and scratch in `WT/scratch/rv128_demo/`.
- Cargo goes through `WT/tools/t3_cargo.sh`; vitest, pytest and e2e go through `WT/tools/t3_slot.sh`.
- No Git writes, no DEC-025, no installs. Clone `node_modules` copy-on-write from a T3 tree with the same lockfile if needed.
- **The record:** `R/REVIEW_RV128/u3_demo_01/REVIEW.md` with SHA256SUMS. It gives the verdict, the counts, and the findings with path:line, evidence and remedy. Placeholder paths only. If the host refuses the file, put its content in your final message.
- Time box: 3 h.

End your turn with:
- the verdict and counts, one line per finding;
- REVIEW's sha256;
- anything for ROOT.
