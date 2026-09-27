# Receipt: APP-HGD-1-3-RECOMMENDATION-2026-09-27

This receipt is a derivative account of the run. Authority stays with the owner's rulings, the registers and the
sources cited in [RECOMMENDATION.md](RECOMMENDATION.md).

**Status:** `EXECUTED`.
- **Proposal (Receipt-278):** the run prepared recommendations for HGD-1, HGD-3 and FC-1 to FC-3.
- **Application (Receipt-279):** the owner ruled on 2026-09-27, adopting the proposed reply word for word. The ruling
  is applied to the DEL-02-01 register.
- **Remaining:** no owner graph ruling is open for DEL-02-01. The DepClosure pointer move is proposed to the manager,
  not made.

## Owner directions

CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING. The owner typed on 2026-09-27, verbatim, as relayed by the coordinating
session:

> You can take care of those remaining items now.  Include the items with the "other owners".  You can make changes as necessary.

The coordinating session had told the owner it would rerun the graph simulations on the current graph and return a
recommendation for HGD-1 and for HGD-3. The rulings stayed with the owner. The recommendation also covered the
fenced candidates FC-1 to FC-3, because the SCC-001 fence recorded with them needed rechecking.

The owner's ruling, typed in chat on 2026-09-27 (verbatim; [CHAT_TRANSCRIPTION_HGD_2026-09-27.md](CHAT_TRANSCRIPTION_HGD_2026-09-27.md)):

> HGD-1: invert DEP-02-01-006 to UPSTREAM INTERFACE; HGD-3: close without emitting; FC-1: resolve DEP-02-01-012 to DEL-05-03; FC-2 and FC-3: close without emitting.

## Proposal phase

- **Basis:**
  - First run on `origin/main` `0adfbc7476df33521883ce1573781237cd24d384`, after PR #1009.
  - Rebased onto `8bbd022b9` (PR #1011), then onto `adc8bdae18b2e1e48dcf01a304cc055d2cbf84e0` (PR #1013).
  - `projects/chirality-app-dev/execution/PKG-*` and `tools/coordination` did not change across these bases.
  - `simulate_hgd.py` reran on the final base and matches its manifest byte for byte.
- **Simulation:** `Evidence/simulate_hgd.py`.
  - It copies the live registers into a temporary root and applies the moves in `Evidence/SCENARIOS.json`.
  - It then runs the unchanged `tools/coordination/analyze_dep_closure.py`, with the arguments of the
    `CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739` snapshot.
  - It also runs `tools/coordination/build_dev001_blocker_queue.py --execution-root`.
  - It covers 35 scenarios: BASE, the 31 subsets of {S1, S2, FC1, FC2, FC3}, and three controls.
  - BASE reproduces the 1739 snapshot exactly.
- **Consulted outside the default read set:**
  - the archived 2026-09-05 N1 preview (`archive/agent-runs-2026-09-25:…/instances/N1-TASK-DEL-02-01/PREVIEW.md`);
  - the D-APP-110 ruling;
  - the 0518, 0807 and 1034 closure snapshots;
  - the retired-Remaining census and the App Task Management rows.
- **Findings:**
  - Every current source reads DEL-02-01 as the consumer of DEL-08-02's routing contract.
  - HGD-3 would still form an 11-node SCC, through DEP-02-02-020 and then DEP-02-01-006 as recorded, unless HGD-1
    were inverted.
  - SCC-001 was resolved by D-APP-110 SD-001.
  - FC-1 was cycle-free. FC-2 needed the inversion. FC-3 always pairs with DEP-02-05-014.
  - No blocker verdict changes in any scenario.
- **Independent review:** the review of `bae0d05a9` reproduced every simulation. The coordinating session relayed
  that it also ran the App's `recorded-register.ts` on all 35 scenarios. Every scenario gave 53 UNBLOCKED,
  1 NOT_TRACKED and 0 BLOCKED, matching the Python queue. Review fixes N1–N7 are in the recommendation.

## Application phase

The application is one `bundled:chirality-root/dependency-extract` UPDATE run.
- **Settings:** `SCOPE=DEL-02-01`, `STRICTNESS=CONSERVATIVE`, apply mode.
- **Script:** `dep_extract/apply_hgd_ruling.py`, in the form of the ESR-1 application.
- **Log:** `dep_extract/EXTRACTION_LOG.json`.

`Dependencies.csv`: pre-image `3baf2660…`, post-image `de142db3d40b6101bf0b1423f06fe4ad0fa35146cf7edd517bcf049dae92be30`.

| Row | Field | From | To |
|---|---|---|---|
| DEP-02-01-006 | `Direction` | `DOWNSTREAM` | `UPSTREAM` |
| DEP-02-01-006 | `DependencyType` | `HANDOVER` | `INTERFACE` |
| DEP-02-01-006 | `Notes` | prior text | prior text + the dated INVERTED clause quoting the ruling |
| DEP-02-01-012 | `TargetType` | `UNKNOWN` | `DELIVERABLE` |
| DEP-02-01-012 | `TargetPackageID` | (empty) | `PKG-05` |
| DEP-02-01-012 | `TargetDeliverableID` | (empty) | `DEL-05-03` |
| DEP-02-01-012 | `TargetRefID` | `TBD` | `DEL-05-03` |
| DEP-02-01-012 | `TargetName` | `Existing redaction helper under frontend/src/lib/harness/** (derived chat titles, Q6)` | `Redacted RunLogger and Secret Hygiene` |
| DEP-02-01-012 | `TargetLocation` | `TBD` | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| DEP-02-01-012 | `Explicitness` | `EXPLICIT` | `IMPLICIT` |
| DEP-02-01-012 | `Notes` | prior text | prior text + the dated TARGET RESOLVED clause quoting the ruling |

Unchanged:
- `LastSeen` was already `2026-09-27`; `Confidence` stays `MEDIUM`; `SatisfactionStatus` stays `TBD`.
- Every other field and row is byte-identical.
- No row is added, retired or deleted. HGD-3, FC-2 and FC-3 are closed without a row.

`_DEPENDENCIES.md`: pre-image `d2ffed68…`, post-image `14257f5036c791de3a6a16e50c61de4f4e12a110d511eb1f70b6e041f7caea7c`.
The human-owned sections are unchanged. The Function 4 refresh made these changes:
- the summary counts and Compact Register (006 is UPSTREAM / INTERFACE; 012 targets DEL-05-03);
- the Lifecycle Summary (HANDOVER 1, INTERFACE 7);
- dated closure bullets at the HGD line, the F1 fence line, the TARGET_UNRESOLVED warning and the SCC_EXPOSURE note;
- the L181 open-rulings sentence, replaced by the dated ruling line;
- a new Run Notes subsection and a Run History row.

Function 5 (`dep_extract/FUNCTION5_CHECKS.json`):
- schema VALID (29 columns, 14 rows);
- `DependencyID` unique; one ACTIVE `IMPLEMENTS_NODE`;
- ID format 0 failures; all 11 enum values of the changed rows VALID;
- the index counts and Compact Register match the CSV.

No other register was touched.

Closure snapshot: `execution/_Evaluation/DepClosure/CLOSURE_HGD_FC_RULING_2026-09-27_1923/` (`UPDATE_LATEST_POINTER=false`).
- The 51 current units PASS: 104 edges, 0 SCC, 0 orphans, 0 bidirectional pairs, 4 isolates (unchanged).
- Its `closure_summary.json` equals the prediction of scenario `S1+FC1`.
- Edge delta against `adc8bdae1`, in production direction:
  - DEL-02-01→DEL-08-02 removed and DEL-08-02→DEL-02-01 added (DEP-02-01-006 reversed);
  - DEL-05-03→DEL-02-01 added (DEP-02-01-012).
- Recorded-register blocker queue (`dep_extract/POST_APPLY_BLOCKER_QUEUE.csv`): 53 UNBLOCKED, 0 BLOCKED,
  1 NOT_TRACKED, 0 held arcs. This is identical to the `S1+FC1` prediction.
  - DEL-02-01's two new gating arcs are met by supplier state: IN_PROGRESS is at or above SEMANTIC_READY.
  - Their `SatisfactionStatus` stays TBD.

**Proposed to the manager (not done):** move `_Evaluation/DepClosure/_LATEST.md` from
`CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739` to `CLOSURE_HGD_FC_RULING_2026-09-27_1923`.

MEMORY `## Runs` rows were added for:
- DEL-02-01, the changed register;
- DEL-08-02 and DEL-05-03, the new suppliers of DEL-02-01's inverted and resolved arcs. No file of theirs changed
  otherwise. DEL-05-03 had no `## Runs` section, so one was added.

## Written

- `RECOMMENDATION.md`, `CHAT_TRANSCRIPTION_HGD_2026-09-27.md` and this receipt.
- `Evidence/`, the simulation package with its `MANIFEST.sha256`.
- `dep_extract/`:
  - `apply_hgd_ruling.py`, `function5_checks.py`;
  - `EXTRACTION_LOG.json`, `FUNCTION5_CHECKS.json`, `POST_APPLY_BLOCKER_QUEUE.csv`.
- DEL-02-01 `Dependencies.csv` and `_DEPENDENCIES.md`.
- `MEMORY.md` rows in DEL-02-01, DEL-08-02 and DEL-05-03.
- The closure snapshot named above.
- Loop ledger entries in `loop/LOOP_RECEIPTS.md`:
  - Receipt-278, the proposal, with parent Receipt-277 (the housekeeping pointer-move receipt of PR #1013);
  - Receipt-279, the application, with parent Receipt-278.

## Checks

These ran on the candidate against `origin/main` `adc8bdae1`:
- this ledger's validator;
- `validate_dependencies_schema.py` on DEL-02-01;
- `validate_decomposition_registers.py`: EVQ-006 is 84 before and after, with no new finding;
- Root G0–G4;
- the conflict-marker and run-record-leak checks;
- `build_workflow_index.py --check` and `git diff --check`;
- `run_affected_tests.py --base origin/main`;
- export freshness.

The results are in the hand-off.

## Limits

- **No other register:** only DEL-02-01's register changed. DEL-08-02's `_DEPENDENCIES.md` L63 note (no concrete
  handoff to DEL-02-01) stays true. DEL-05-03's register records no reverse row, which the recorded-register
  semantics do not require.
- **Not changed:** no scope, lifecycle, `_STATUS.md` or pointer; no release.
- **Simulated IDs:** `DEP-02-01-015`, `-016` and `-017` in `Evidence/SCENARIOS.json` are simulation placeholders.
  None was emitted.

Execution: a Claude Code TASK-type subagent for the coordinating session, in an isolated worktree, with no delegation.
Model identifiers are withheld at the dispatching session's instruction; the commit's session trailer identifies the
run.
