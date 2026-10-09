# I116, U5: the piping governance documents follow the pressure retirement

TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), your return path. You do not delegate. **You are a fresh instance.** `R/BRIEFS/B1_COMMON.md`'s host, Git and records rules apply, with WORKING_ITEMS in ROOT's place.

## Why

The owner retired `1.0.0/legacy_pressure_v1` product-wide (RR "Owner decisions: the legacy pressure contract is retired product-wide; …"; U3 is PR #1168). The piping project's `docs/TYPES.md`, `SPEC.md`, `VALIDATION_STRATEGY.md`, `INTENT.md` and `PRD.md` still list pressure membrane stress and pressure thrust as current capabilities (RV127 A1-N-2). The owner authorized one small PR to correct them (RR "Owner decisions: T4 starts now; the governance-documents PR is authorized").

**The authorized scope, exactly:**
- correct only those capability statements, so that they match the retirement;
- cite the owner decisions;
- include a tranche manifest;
- route notices to any project loop that mirrors those texts (Root `AGENTS.md`, "Execution and governance"; `docs/PRD_ROOT.md` on amendments);
- have it reviewed independently;
- cut it after #1168 merges, so the texts never describe something not yet true.

Nothing else in these documents changes.

## What is true after U3

Read U3's change record (`T/IMPLEMENTATION/U3/CHANGE_RECORD.md`) and the product's own text. The corrected `preview_formulation_basis` limitation [1] reads: "Pressure is not solved on this profile: legacy pressure inputs are refused, and pressure is solved only on the exact straight-pressure profile, under that profile's own qualifications." Each corrected statement must be true of the product at #1168's head, and no stronger than its evidence.
- The exact straight-pressure profile's standing is its own. State only what its accepted records support, and cite them.
- T4 (pressure stress, ACTIVE in planning) may later add capability. Do not anticipate it.
- **A statement you cannot ground** in the product or an accepted record is a question for WORKING_ITEMS, not a guess.

## The task

1. **Find every capability statement** on pressure membrane stress, pressure thrust or the legacy pressure contract in the five documents, and anywhere else in piping's `docs/` that states current capability on the same footing. Give file, line and the current text. Report other places you find; do not edit them.
2. **Draft the corrections:** the smallest truthful edit to each, each citing the owner decision by its RR heading.
3. **The tranche manifest:** follow the repository's convention in `docs/governance_harness/tranche_manifests/` (read two or three recent manifests and the harness that validates them). Run that validation locally if it can run offline.
4. **The notices:** find every project loop whose authority corpus, contract mirror or pinned instruction set mirrors any changed text (search for the paths and their content hashes in other loops' accepted bases). Draft one notice per affected loop, in the repository's notice convention. A notice communicates the change; each loop decides its own adoption. Say plainly if you find none, and how you searched.
5. **Gates you can run:** GEN-8 (`pytest tools/practitioner_harness/test_live_baseline.py -k gen8`), the governance harness, and both screens before every commit.

## Where

- **Worktree `WT/u5-docs`,** branch `codex/piping-t3-u5-governance-docs-20261009`, cut by WORKING_ITEMS from main `7b2715cb0e`. U3 does not touch these documents, so main's copies equal what #1168 leaves.
- **Commit your draft there.** Do not push and do not open a PR. After #1168 merges, WORKING_ITEMS merges main into the branch, opens the PR and dispatches the independent review.

## Host and records

- No cargo is needed. Heavy pytest goes through `WT/tools/t3_slot.sh`. No DEC-025, no installs, and never signal another job.
- Scratch in `WT/scratch/i116_u5/`.
- Records go directly in `R/I116/u5_docs_01/` in NUM (RETURN.md, `_run_records/`, SHA256SUMS), placeholder paths only. If the host refuses a record file, give its full content in your final message with its intended path; do not work around the refusal.
- **Budget:** 3–5 h.

End your turn with:
- the branch head;
- every statement found, with its correction;
- the manifest and its validation;
- the notices, or none with the search;
- GEN-8;
- any question.
