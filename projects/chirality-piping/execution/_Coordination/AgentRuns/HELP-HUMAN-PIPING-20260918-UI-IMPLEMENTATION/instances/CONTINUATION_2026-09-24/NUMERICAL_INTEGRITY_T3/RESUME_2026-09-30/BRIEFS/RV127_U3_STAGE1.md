# RV127: the fresh independent review of U3 Stage 1 (the legacy pressure contract retired)

TASK (Type 2), an independent reviewer dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You wrote none of this code.** `R/BRIEFS/B1_COMMON.md`'s host, records and placeholder rules apply, with WORKING_ITEMS in ROOT's place.

## The candidate

- **Branch** `codex/piping-t3-pressure-retire-20261008` (`WT/t3-pret`), head `4c0d5d7c00`: four commits on main `7eae707bb7`, 22 files.
- **The owner's decision:** RR "Owner decisions: the legacy pressure contract is retired product-wide; …". **ROOT's rulings:** RR "U3 rulings on I110's pressure inventory: D-1 A, D-2 A1, D-3 held with M07".
  - D-1 A: 0.1.0 and 0.2.0 stay as the pressure-free namespace.
  - D-2 A1: a pressure primitive of any value in a non-exact document is refused with `PRESSURE_MODEL_REAUTHOR_REQUIRED`.
  - D-3: held.
  - D-4: reuse that code.
- **The M07 hold:** the historical scope file, its bypasses, O1–O4, G10 and G11 stay untouched until the owner answers.
- **The implementer's records:** `R/I110/pressure_retire_01/` (inventory and plan) and `R/I110/pressure_retire_02/` (Stage 1, with the outcome diffs and byte-equality evidence).

## Review, in priority order

1. **Exact-pressure behaviour is byte-identical.** Read every hunk in `validate_profile` and every route that reaches it. Confirm the exact contract's acceptance and checks are unchanged. Reproduce a sample of I110's byte-equality rows yourself: at least 10 exact documents and 10 implicit pressure-free documents in both modes, plus 4 of B1's corpus through W1.
2. **The refusals are complete and correct:** the label and any pressure primitive in 0.1.0 and 0.2.0, on the ordinary, retained and runner routes; the three readers at G8; the app (panel, load-case manager, src-tauri open and solve); and the applier.
   - Look for a route that still accepts the label or computes legacy pressure outside the held test scope.
   - Look for a refusal text that does not tell the user to re-author to `2.0.0/exact_straight_pressure_v2`.
3. **Deleted and edited tests:** each deletion is a pressure-only oracle the plan lists, and each edit preserves what the test protected. In particular, strip-instead-of-zero must leave every non-held user's assertions intact.
4. **Public meaning.** The new applier code `OP-PRESSURE-PRIMITIVE-RETIRED`, the panel's "retired" and "none (pressure-free)" texts, and any other user-visible change are within the owner's decision. Flag anything beyond it for ROOT.
5. **The held items are untouched.**

## Host and output

- Use an archive copy in `WT/rv127/`, with targets under `WT/targets/rv127*` and scratch in `WT/scratch/rv127_u3/`. Delete the copies afterwards.
- Every cargo goes through `WT/tools/t3_cargo.sh`; heavy pytest and vitest go through `WT/tools/t3_slot.sh`.
- No Git writes, DEC-025 or installs.
- **The record:** `R/REVIEW_RV127/u3_stage1_01/REVIEW.md` with SHA256SUMS. Give the verdict, the counts, and a findings table with path:line, evidence and remedy. Use placeholder paths only. If the host refuses the file, put its full content in your final message with the intended path; do not work around the refusal.
- After repairs, you confirm them. Time box: 4 h.

**End your turn with:**
- the verdict and counts, with one line per finding;
- REVIEW's sha256;
- anything for ROOT.
