# I110: retiring the legacy pressure contract product-wide — inventory and removal plan

TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), which is your return path. You do not delegate. **You are a fresh instance.** Read `R/BRIEFS/B1_COMMON.md` for the host, Git and records rules, reading "ROOT" there as "WORKING_ITEMS" for pushes, merges and record commits. This round is read-and-probe only: no product change is committed.

## Why

The owner retired the legacy pressure contract on 2026-10-08 (RR "Owner decisions: the legacy pressure contract is retired product-wide; T3 gains a WORKING_ITEMS manager"): "If you have replaced old code with new because the old was flawed, don't maintain the flawed code or compatibility with it"; then "1a, retire it product-wide". The decision:
- `1.0.0/legacy_pressure_v1` stops being accepted anywhere, including zero-pressure documents, which must be re-authored to the exact contract (`2.0.0/exact_straight_pressure_v2`);
- the legacy nonzero-pressure computation path goes, with the pressure part of the test-only historical scope (`PP/src/historical_pressure_reference.rs`) and the oracles that depend on it;
- every exact-pressure behaviour stays byte-identical, shown with evidence;
- the historical scope's other premise (M07's refused user-stiffness joint, "T0R") is inventoried and brought to ROOT with a recommendation, and is not removed.

Today the ordinary route already refuses a legacy-contract model with a nonzero pressure load (`PRESSURE_MODEL_REAUTHOR_REQUIRED`, `PP/src/pressure_runtime.rs`); only the historical scope suspends that refusal.

## The basis

Read the product code on NUM (main plus PR-B1's code; PR-B1 merges before this work is cut). Use `git -C NUM grep` / `git show` with `GIT_OPTIONAL_LOCKS=0`. For probes, make your own detached worktree `WT/t3-pret` at NUM's HEAD. B3a on `b2` (the retained route's and the three readers' admission of the legacy label) is dropped separately by WORKING_ITEMS; list its sites on `b2` (`72b3e5d9ea` and the reader branches `b2-p`, `b2-r`, `b2-t`) for completeness only.

## The task

1. **The inventory.** Every acceptance, use, fixture, schema enum, reader branch, UI path, doc and test of `1.0.0/legacy_pressure_v1`, and every piece of the legacy nonzero-pressure computation reachable only through the historical scope. Cover `PP`, the solver and loads crates, the headless runner, `RE`, the Python packages and `P/tests`, `P/tools`, the desktop app (`P/apps/desktop/src` and `src-tauri`), schemas, fixtures (`P/fixtures`, `P/validation/qualification/fixtures`, goldens and corpora) and docs. For each site: path:line, kind, and a proposed disposition (remove; becomes a refusal; re-author to the exact contract; delete the test; keep, with the reason). Give counts by kind and area. Put the table in `inventory.json` and summarize it in the record.
2. **Answer these, with evidence:**
   - **Q1, implicit legacy documents.** Model documents 0.1.0 and 0.2.0 carry no pressure contract and take the same non-exact pressure semantics. Are they the legacy contract in substance? What reads or writes them (fixtures, the app's migration, tests, qualification)? Recommend; ROOT rules.
   - **Q2, capability left after retirement.** List what the exact contract refuses today (components and fittings, nonlinear and constant-effort supports, combinations, `equivalent_static`, the id-suffix rules, anything else). For zero-pressure documents accepted today only under the legacy label (or Q1's implicit form), which of them would have no route at all after retirement? Count them in the committed fixtures, the app's authoring defaults and the qualification corpus.
   - **Q3, the app.** What the desktop app authors for a new document, a migration and the pressure panel (`model_document_migration.rs`, `projectService.ts`, `blankLoadStateModel`, `PressureAuthoringPanel`), and what the user sees after retirement.
   - **Q4, the refusal.** Where and how a legacy-labelled document is refused after retirement (one code or the existing ones; the message must tell the user to re-author to the exact contract), on the ordinary, retained and runner routes, and in the three result readers for result documents that carry the legacy label.
   - **Q5, M07.** Every use of the user-stiffness joint premise in the historical scope, which oracles need it, and a recommendation (keep the scope for M07 alone, convert, or remove) for ROOT.
   - **Q6, the old branches.** Whether `codex/piping-pressure-stress-20260924` (one commit `af4120ba52` not patch-equivalent to main) and `codex/piping-result-compatibility-pressure-20260914` (PR #788, merged) hold live work main lacks.
3. **The removal plan:** the change list by file, the order, the tests removed and the tests added (one refusal test per route and reader, and the app's path), the fixtures re-authored or deleted, and the evidence that exact-pressure behaviour is byte-identical (which suites, corpora, goldens and per-test outcome comparisons, against which base). Estimate the size in hours.

**Stop and return** (do not plan around it) if Q2 finds an accepted model class with no route after retirement, or if any disposition needs a change to an accepted design (B0, B2-C, B3-D), a weakened check, or public meaning beyond the owner's decision. Give the options and your recommendation.

## Rules

- **Host:** as `B1_COMMON.md`; cargo targets under `WT/targets/i110-pret`, scratch in `WT/scratch/i110_pret/`. Probes are targeted tests only (a crate's tests, never the 40 manifests). No DEC-025, no measurements, no installs. ROOT's DEC-025 may hold the exclusive lock; wait for it.
- **Git:** no commits. Leave NUM, `b2` and every other lane's worktree untouched.
- **Records:** `R/I110/pressure_retire_01/` (RETURN.md with the inventory summary, the answers and the plan; `inventory.json`; `_run_records/`; SHA256SUMS), placeholder paths only. WORKING_ITEMS commits them.
- **Budget:** 4–6 h. If your context runs low, write what you have and return.

## Return

End your turn with: the inventory's counts by kind and area; Q1–Q6 in a line each; the plan's size; any stop; the record's path and its RETURN.md sha256.
