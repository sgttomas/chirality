# Native self-weight verification

ROOT exercised the candidate through the native application UI, using one agent-created, invented local project. The native executable SHA-256 is `65aab38fc4425eb62661e0fa8c52a254f734b4a22adcc149f319162f1763a632`, built from clean `64487068b740977083275baa4ead5ed4171c6084`. All 926 maintained native inputs remain identical on PR892 candidate `3c17e267dd06ee561e8dc9984f6623126095eec1`; intervening changes are the recorded main union and evidence corrections. The build and artifact records are retained under `_run_records`; the independent candidate backcheck is in PR892's `GENERATED_LOADS_MANAGER/ROOT_INTEGRATION`.

The test project is `project:blank-local-20260925t030113z`. A two-metre cantilever was authored with explicit invented geometry and elastic inputs; no material/component library or code rules were populated. Gravity was explicitly -7 m/s². Full native-created models and authoring batches remain private. [CUSTODY.json](CUSTODY.json) identifies the selected raw outputs and hashes of private observations; private hashes do not promise permanent availability.

| Journey | Actual observation |
|---|---|
| Generate, apply, solve, save | One distributed load, -19.792033717615702 N/m, support force 39.584067 N. |
| Add independent -11 N tip load and double density | Solve blocks with `SELF_WEIGHT_INPUTS_STALE`. |
| Explicit self-weight refresh, atomic apply, solve, save | Same generated ID and separate manual load, intensity -39.584067435231404 N/m; support force 90.168135 N. |
| Undo and Redo | Undo clears results and solve again blocks stale inputs; Redo restores the refreshed model and solve succeeds. |
| Save/reopen/recompute | Reopened owned project has no Undo/Redo history and Historical results; native Run recomputes successfully. |
| Length two to three metres | Intensity remains current; support force changes to 129.752202 N and root bending moment to 211.128303 N*m. |
| Deliberately alter generated intensity and change density | Solve and ordinary refresh both reject `SELF_WEIGHT_GENERATED_LOAD_MODIFIED`. |
| Explicitly preserve modified load as manual | Native solve succeeds with `SELF_WEIGHT_MANUAL_OVERRIDE`; -123.456 N/m plus -11 N tip gives 381.368 N reaction and 588.552 N*m root moment. |
| Change density again, 3000 to 4000, solve and save | Preserved load values and IDs remain identical, as do reaction and root moment. |

The reactions and member end moments match independently calculated cantilever force and moment balance using the declared loads. Formula clarification from independent review: with signed distributed load q and signed tip load P_y (here -11 N), supportY = -(qL + P_y) and the reported root bending magnitude = -(qL²/2 + P_y L). The retained raw analytical JSON labels this last signed term incorrectly with a plus; its numeric expected values already use the correct negative signed term. The original raw record is preserved; no product result or numeric comparison changes. The native candidate still uses the existing six-decimal result representation; this witness does not claim the unmerged M34 full-precision behavior. See `_run_records/analytical-native-checks.json` and `final-manual-invariance.json`. Save-state audit used SQLite read-only mode and selected only the owned project.

The initial setup batch was rejected for incomplete agent attribution, then explicitly corrected and validated. Native authoring also exposed a separate `connect_pipe_run` defect: a supplied section density was silently omitted. An explicit density edit completed this fixture; the underlying authoring defect is assigned to the joined engine tranche, not hidden as a successful creation test. The self-weight generator correctly blocked the absent density. These initial observations remain private with hashes because their operation payloads describe the native-created model.

The Mac remained accessible during these checks. Native accessibility output sometimes omitted visible panel subtrees; screenshots supplied the missing controls. No live-controller endpoint was launched, and agent-operated Apply does not satisfy the separately held actual-human live witnesses. Native legacy-v1 upgrade and an intervening-edit-after-queued-refresh scenario were not repeated here; their bounded source/WASM checks remain separate evidence. Final owned state was saved. An initial keyboard Quit request was not reliably established. ROOT then selected the actual native application menu and invoked `Quit SWBPIPE`; the subsequent native app inventory returned no SWBPIPE entry. Cleanup is confirmed for this owned candidate.

This verifies the stated workflows, not completion of all 38 findings, pressure/stress integration, general UI work, or engineering acceptance. Standard claim fence applies (F-PIP-2; claims taxonomy per DEC-081).
