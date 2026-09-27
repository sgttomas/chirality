# Receipt: APP-HGD-1-3-RECOMMENDATION-2026-09-27

This receipt is a derivative account of a proposal-only run. Authority stays with the owner's rulings, the registers
and the sources cited in [RECOMMENDATION.md](RECOMMENDATION.md).

**Status:** `AWAITING_OWNER`. The recommendations for HGD-1, HGD-3 and FC-1 to FC-3 are prepared. No register, index,
lifecycle, scope or pointer was written.

## Owner direction

CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. The owner typed on 2026-09-27, verbatim, as relayed by the coordinating
session:

> You can take care of those remaining items now.  Include the items with the "other owners".  You can make changes as necessary.

For HGD-1 and HGD-3, the coordinating session had told the owner it would rerun the graph simulations on the current
graph and return a recommendation for each. The rulings stay with the owner. This run prepares those
recommendations. It also covers the fenced candidates FC-1 to FC-3, because the SCC-001 fence recorded with them
needed rechecking.

## What was done

- **Basis:** `origin/main` `0adfbc7476df33521883ce1573781237cd24d384`, after PR #1009. The candidate was then
  rebased onto `8bbd022b98140e2128b6132bf661786ee3a8d108` (PR #1011). That merge changes only
  `projects/chirality-app-v4`; `projects/chirality-app-dev` and `tools/` are identical at both commits.
- **Simulation:** `Evidence/simulate_hgd.py`. It copies the live registers into a temporary root, applies the moves
  in `Evidence/SCENARIOS.json`, and runs the unchanged `tools/coordination/analyze_dep_closure.py` (with the
  arguments of the `CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739` snapshot) and
  `tools/coordination/build_dev001_blocker_queue.py --execution-root`.
- **Scenarios:** 35 in all. BASE, 31 subsets of {S1, S2, FC1, FC2, FC3}, and three controls.
- **Basis match:** BASE reproduces the 1739 snapshot exactly, and its 106 input hashes match. Two runs were
  byte-identical, and the live registers were hash-stable.
- **Source reading:** the HGD-1 direction was read against the DEL-02-01 and DEL-08-02 Scopes of Work, the
  decomposition's DEL-02-01, DEL-08-02 and SOW-005 rows, and DEL-08-02 `_DEPENDENCIES.md`. Exact lines are quoted
  in the recommendation.
- **Consulted outside the default read set:**
  - the archived 2026-09-05 N1 preview
    `archive/agent-runs-2026-09-25:projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N1-TASK-DEL-02-01/PREVIEW.md`,
    which holds the original S0 to S5 and FC-1 to FC-3 definitions;
  - the D-APP-110 ruling and the 0518, 0807 and 1034 closure snapshots, which trace how SCC-001 was resolved;
  - the retired-Remaining census and the App Task Management rows, which are the only surviving copy of the HGD-3
    source line.

## Findings

- **HGD-1:** every current source reads DEL-02-01 as the consumer of DEL-08-02's routing contract. Inverting
  DEP-02-01-006 keeps the graph acyclic and changes no blocker verdict.
- **HGD-3:**
  - The four-node SCC recorded in 2026-09-05 no longer forms, but emitting the row still creates an 11-node SCC.
    The path runs through DEP-02-02-020, emitted later under D-APP-109 as H-006, and then DEP-02-01-006 as recorded.
  - The row's only source is a retired Remaining line.
  - The gate it records was met by PR #733.
- **SCC-001:** it was resolved by D-APP-110's SD-001 decompose of DEP-04-05-010. Undoing that one move brings back
  the original nine members.
- **The fenced candidates:**
  - FC-1 is now cycle-free.
  - FC-2 forms a 7-node SCC unless HGD-1 is inverted.
  - FC-3 always forms at least a two-node SCC with DEP-02-05-014.
- **Blocker verdicts:** none changes in any of the 35 scenarios. Where a cycle forms, its arcs become held
  (non-gating) and the closure check `circular_dependencies` fails.

## Recommendation and proposed owner reply

See [RECOMMENDATION.md](RECOMMENDATION.md). The proposed reply is:

> HGD-1: invert DEP-02-01-006 to UPSTREAM INTERFACE; HGD-3: close without emitting; FC-1: resolve DEP-02-01-012 to DEL-05-03; FC-2 and FC-3: close without emitting.

## Written

- `RECOMMENDATION.md` and this receipt.
- `Evidence/`:
  - `SCENARIOS.json`, `simulate_hgd.py`;
  - `SIMULATION_RESULTS.csv` and `.json`;
  - `REACHABILITY.json`, `BASIS_CHECK.json`, `INPUT_HASHES.json`;
  - `runs/<scenario>/`;
  - `MANIFEST.sha256`.
- The loop ledger entry in `loop/LOOP_RECEIPTS.md`: Receipt-278, with parent Receipt-277 (the housekeeping
  pointer-move receipt of PR #1013).

## Checks

These ran on the rebased candidate against `origin/main` `8bbd022b9`:
- this ledger's validator;
- Root G0–G4;
- the conflict-marker and run-record-leak checks;
- `build_workflow_index.py --check` and `git diff --check`;
- export freshness.

The results are in the hand-off.

## Limits

- **Not written:** no `Dependencies.csv` or `_DEPENDENCIES.md`, no MEMORY entry, no pointer and no lifecycle state.
  The recommended register changes are specified field by field for a later `dependency-extract` UPDATE run under
  the owner's ruling.
- **Simulated IDs:** `DEP-02-01-015`, `-016` and `-017` are simulation placeholders. The applying run assigns the
  next free IDs.
- **Blocker semantics:** blocker results use the Root recorded-register reference tool. Its parity with the App's
  `recorded-register.ts` is established by the APP-RECORDED-REGISTER-2026-09-26 fixtures. This run did not execute
  the App module. The coordinating session relayed that the independent review of `bae0d05a9` ran
  `recorded-register.ts` on all 35 scenarios and got 53 UNBLOCKED, 1 NOT_TRACKED and 0 BLOCKED in every one,
  matching the Python queue.

Execution: a Claude Code TASK-type subagent for the coordinating session, in an isolated worktree, with no delegation.
Model identifiers are withheld at the dispatching session's instruction; the commit's session trailer identifies the
run.
