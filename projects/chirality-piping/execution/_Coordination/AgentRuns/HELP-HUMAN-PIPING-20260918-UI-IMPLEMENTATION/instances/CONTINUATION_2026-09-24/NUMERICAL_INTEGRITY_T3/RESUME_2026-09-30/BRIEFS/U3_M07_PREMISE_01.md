# I111: the historical scope's M07 premise (the refused user-stiffness joint) — a one-page decision report

TASK (Type 2), dispatched by WORKING_ITEMS for T3 (Agent 1), which is your return path. You do not delegate. **You are a fresh instance.** Read `R/BRIEFS/B1_COMMON.md` for the host and records rules, reading "ROOT" there as "WORKING_ITEMS". Read-and-probe only: no product change, no commits.

## Why

The owner retired the legacy pressure contract (RR "Owner decisions: the legacy pressure contract is retired product-wide; …"). The test-only historical scope `PP/src/historical_pressure_reference.rs` also admits a second premise, T0R's refused user-stiffness joint (M07), for the named historical oracles frozen with it. The owner has asked ROOT for a recommendation on it, ahead of the pressure removal. I110 is inventorying the pressure part in parallel; leave that to it.

The work graph's T4 row (section "Route" table, T4) records the flaw: the expansion-joint user-stiffness element's lateral springs lack the rigid-body moment coupling (frame_kernel `user_stiffness_local_matrix`), so it is not in moment equilibrium; on the invented demo the reactions are out of balance by 658.44 N·m. The ordinary route refuses such models. T4 repairs it from the joint reference (`../CORRECTNESS_DESIGN/JOINT_REFERENCE/RETURN.md`, beside T's folder).

## Answer, with path:line evidence (read NUM's HEAD with `GIT_OPTIONAL_LOCKS=0`)

1. **The flaw.** The premise exactly: the element, its matrix and the code that builds and assembles it, and what is wrong with it. Confirm the moment-equilibrium defect from the matrix itself (a rigid-body rotation test on the local matrix is enough), and reproduce or cite the 658.44 N·m figure.
2. **Reachability.** Where the flawed element code is reachable today. Is the ordinary route's refusal the only gate? Does any other product path (the retained route, the runner, the WASM engine, `self_weight_wasm`, the solver crates' own entry points), a reader, the desktop app or its authoring UI build or use it?
3. **The oracles.** Which tests enter the historical scope for this premise, what each asserts, and what it protects now that the element is refused: byte oracles of flawed results, or checks of something still valid (for example, parts of a model unaffected by the joint)?
4. **What T4 needs.** What T4's repair needs from the joint reference, and whether removing the oracles or the element code would lose anything the corrected element needs (test models, inputs, independent references).
5. **The options and their cost,** each with its blast radius in files and tests:
   - (a) remove the oracles and the historical scope now, keeping the refused element code until T4 repairs it;
   - (b) also remove the flawed element code, so joint models are refused until T4 builds a correct element from the joint reference;
   - (c) leave it until T4.

   Note how each interacts with the pressure retirement (the same scope file and some of the same tests).

Keep the report to one page, plus `evidence.json` for the path:line table. No recommendation is required; if you have one, give it in one line with its reason.

## Rules

- **Host:** as `B1_COMMON.md`; scratch in `WT/scratch/i111_m07/`, cargo targets under `WT/targets/i111-m07`. A targeted test or a small probe binary is allowed; no suites, no DEC-025, no measurements. ROOT's DEC-025 holds the exclusive lock now; wait for it.
- **Records:** `R/I111/m07_premise_01/` (REPORT.md, `evidence.json`, `_run_records/`, SHA256SUMS), placeholder paths only. WORKING_ITEMS commits them.
- **Budget:** 1.5–2.5 h.

## Return

End your turn with the five answers in a line or two each, the record's path and REPORT.md's sha256.
