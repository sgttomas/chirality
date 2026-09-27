# HGD-1, HGD-3 and the fenced candidates FC-1 to FC-3: recommendations for the owner

Status: **proposal only.** No register has been written. Each ruling below is yours to make.

Basis: `origin/main` `0adfbc7476df33521883ce1573781237cd24d384`, after PR #1009. The simulations reproduce the current
closure snapshot `_Evaluation/DepClosure/CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739` exactly (51 units, 103
edges, 0 SCC; `Evidence/BASIS_CHECK.json`).

## Decisions

| Item | Recommendation | Graph result | Blockers |
|---|---|---|---|
| **HGD-1**: direction of DEP-02-01-006 (DEL-02-01 and DEL-08-02) | **Invert it** to UPSTREAM INTERFACE: DEL-02-01 consumes DEL-08-02's routing contract | Still 0 SCC. DEL-08-02 no longer depends on the shell | No change |
| **HGD-3**: DEL-02-01-V3-01's prerequisite on DEL-02-02-V3-03 | **Close it without adding a row** | Unchanged | No change |
| **FC-1**: redaction helper, owned by DEL-05-03 | **Resolve DEP-02-01-012 to DEL-05-03** | Still 0 SCC, with or without HGD-1 | No change |
| **FC-2**: session binding, DEL-03-02 | **Close it without adding a row** | Unchanged | No change |
| **FC-3**: account row presentation, DEL-02-05 | **Close it without adding a row.** DEP-02-05-014 already records this relation | Unchanged | No change |

Taken together, these rulings leave 104 edges and 0 SCC (scenario `S1+FC1`). No blocker verdict changes. All
53 tracked deliverables stay UNBLOCKED and none is BLOCKED.

### Proposed owner reply (exact)

> HGD-1: invert DEP-02-01-006 to UPSTREAM INTERFACE; HGD-3: close without emitting; FC-1: resolve DEP-02-01-012 to DEL-05-03; FC-2 and FC-3: close without emitting.

Any other combination can be ruled item by item. The consequences of each alternative are set out below.

### Two findings that correct the recorded picture

1. **HGD-3 still creates a cycle, though not the recorded one.** The record says that emitting HGD-3 would
   "no longer close the four-node SCC" (DEL-02-01 `_DEPENDENCIES.md` L99; Receipt-274 to 276). That is true, but
   the row is still not cycle-free. On the current graph it creates an **11-node SCC**, because DEL-02-02 now
   reaches DEL-02-01 by another route:
   - DEP-02-02-020 (DEL-02-02 on DEL-08-02), emitted under D-APP-109 as H-006 after the 2026-09-05 preview ran S2;
   - then DEP-02-01-006 as recorded (DEL-08-02 on DEL-02-01).

   The row becomes acyclic only if HGD-1 is inverted.
2. **The SCC-001 fence no longer holds as stated, but the cycle risk does.** SCC-001 was resolved by D-APP-110's
   decompose of DEP-04-05-010 (workbook SD-001). Undoing that one decompose brings back exactly the original nine
   members (control `C3_UNDO_SD-001`). The risk that remains is different for each candidate:
   - **FC-1** is now cycle-free.
   - **FC-2** still creates a 7-node SCC through DEP-02-01-006 as recorded.
   - **FC-3** always creates at least a two-node SCC with DEP-02-05-014, whatever you rule on HGD-1.

## Simulation results

Method: `Evidence/simulate_hgd.py`, run from the repository root.
- It copies every live unit's `Dependencies.csv`, `_DEPENDENCIES.md` and `_STATUS.md` into a temporary root and
  applies the moves in `Evidence/SCENARIOS.json`.
- It then runs the unchanged `tools/coordination/analyze_dep_closure.py` with the 1739 snapshot's arguments: 51
  units, ACTIVE EXECUTION rows with DELIVERABLE targets, declared entries included.
- It also runs `tools/coordination/build_dev001_blocker_queue.py --execution-root`. This is the App's
  recorded-register semantics, which the App's `recorded-register.ts` mirrors:
  - Each arc is judged by comparing the supplier's `_STATUS.md` state with the arc's `RequiredMaturity`.
  - The default is `INITIALIZED`, because `_COORDINATION.md` names no default.
  - Arcs inside an SCC are held.
- It runs 35 scenarios: BASE, all 31 subsets of {S1, S2, FC1, FC2, FC3}, and three controls.
- Two runs produced byte-identical outputs, and the live registers were hash-stable before and after
  (`Evidence/INPUT_HASHES.json`).

Edges use the analyzer's direction: consumer → supplier. An UPSTREAM row keeps its direction; a DOWNSTREAM row is
reversed.

| Scenario | Edges | SCCs (members) | New edges | Blocked / held arcs | Blocker verdict change |
|---|---:|---|---|---|---|
| BASE (current) | 103 | none | none | 0 / 0 | none |
| S1: HGD-1 inverted | 103 | none | DEL-02-01→DEL-08-02 replaces DEL-08-02→DEL-02-01 (DEP-02-01-006) | 0 / 0 | none. DEL-02-01 gains 1 gating arc (satisfied) and DEL-08-02 loses its only one |
| S2: HGD-3 row | 104 | **1 SCC, 11 nodes**: DEL-02-01, 02-02, 03-02, 04-02, 04-03, 04-04, 05-02, 05-04, 08-02, 08-04, 08-05 | DEL-02-01→DEL-02-02 | 0 / **15 held** | none BLOCKED. The closure check `circular_dependencies` becomes BLOCKER |
| FC1 | 104 | none | DEL-02-01→DEL-05-03 (DEP-02-01-012) | 0 / 0 | none |
| FC2 | 104 | **1 SCC, 7 nodes**: DEL-02-01, 03-02, 04-02, 04-03, 04-04, 05-02, 08-02 | DEL-02-01→DEL-03-02 | 0 / 7 held | none BLOCKED; closure BLOCKER |
| FC3 | 104 | **1 SCC, 10 nodes**: DEL-02-01, 02-05, 03-02, 03-03, 03-04, 04-02, 04-03, 04-04, 05-02, 08-02 | DEL-02-01→DEL-02-05 | 0 / 13 held | none BLOCKED; closure BLOCKER |
| S1+S2 | 104 | none | the S1 edge and DEL-02-01→DEL-02-02 | 0 / 0 | none |
| **S1+FC1 (recommended)** | 104 | none | the S1 edge and DEL-02-01→DEL-05-03 | 0 / 0 | none |
| S1+FC2 | 104 | none | the S1 edge and DEL-02-01→DEL-03-02 | 0 / 0 | none |
| S1+FC3 | 104 | **1 SCC, 2 nodes**: DEL-02-01, DEL-02-05 | the S1 edge and DEL-02-01→DEL-02-05 | 0 / 2 held | none BLOCKED; closure BLOCKER |
| S1+S2+FC1+FC2 | 106 | none | S1, S2, FC1 and FC2 edges | 0 / 0 | none |
| All five | 107 | 1 SCC, 2 nodes: DEL-02-01, DEL-02-05 | all five | 0 / 2 held | as S1+FC3 |
| All five except S1 | 107 | 1 SCC, 14 nodes | S2, FC1, FC2 and FC3 edges | 0 / 23 held | closure BLOCKER |
| C1: S2 with the retired pair DEP-02-02-005 and DEP-02-01-007 restored | 105 | 1 SCC, 11 nodes | S2 and DEL-02-02→DEL-02-01 | 0 / 16 held | control |
| C2: that pair only | 104 | none | DEL-02-02→DEL-02-01 | 0 / 0 | control |
| C3: undo D-APP-110 SD-001 (DEP-04-05-010 back to DEL-02-05) | 104 | **1 SCC, 9 nodes: the original SCC-001** (DEL-02-05, 03-02, 03-03, 03-04, 04-03, 04-05, 05-02, 05-03, 05-05) | DEL-04-05→DEL-02-05 | 0 / 13 held | control |

The full 35-row table is in `Evidence/SIMULATION_RESULTS.csv`. Per-row detail, including every changed queue field,
is in `Evidence/SIMULATION_RESULTS.json`. Each scenario's analyzer and queue outputs are under `Evidence/runs/`.
Path witnesses are in `Evidence/REACHABILITY.json`:
- BASE:
  - DEL-02-02→DEL-08-02→DEL-02-01;
  - DEL-03-02→DEL-05-02→DEL-04-03→DEL-04-02→DEL-04-04→DEL-08-02→DEL-02-01;
  - DEL-02-05→DEL-02-01;
  - DEL-05-03 has no path to DEL-02-01.
- S1: only DEL-02-05→DEL-02-01 remains.

No scenario changes a BLOCKED/UNBLOCKED verdict. Every supplier involved is IN_PROGRESS, which reaches each arc's
SEMANTIC_READY. The effect of a cycle is different: its arcs become **held** and stop gating, and the closure
audit's `circular_dependencies` check fails. Such a state would then need a recorded move under
`docs/CYCLE_DRIVEN_RESOLUTION.md` (the `scc-resolution-case` workflow).

## HGD-1: which way the contract runs

**Finding: DEL-02-01 consumes DEL-08-02's contract.** Every current source puts ownership of routing, selection
guards and route/query compatibility with DEL-08-02 and presentation with DEL-02-01. No source names anything that
DEL-02-01 hands over to DEL-08-02.

Quotations are exact. Paths are under `projects/chirality-app-dev/execution/`, with SHA-256 prefixes.

- **The row itself** (`PKG-02_…/DEL-02-01_…/Dependencies.csv` L7, `3baf2660…`). Its 2026-09-22 Statement reads:
  "DEL-02-01 consumes DEL-08-02 routing/guarded-selection contracts; current folder/direct-entry behavior preserves
  exact retained query compatibility without restoring the old matrix." The Statement describes consumption, but
  the Direction still says DOWNSTREAM HANDOVER. The historical statement preserved in `Notes` is an ownership
  boundary, not a handover: "DEL-02-01 leaves persona alias and deeper routing-contract ownership to DEL-08-02
  unless a human ruling expands this slice."
- **DEL-02-01 Scope of Work** (`ScopeOfWork.md`, `e6b9bdd6…`):
  - L257 (CLM-015): "DEL-08-02 owns routing/guarded selection; old persona-picker and isMatrixLaunchBlockedByStreaming identifiers are earlier evidence, not a current required component name."
  - L337 (CLM-027): "The exact surviving TYPES §4 route/query compatibility question remains keyed with DEL-08-02; … DEL-08-02 owns routing/guarded selection; DEL-02-02/03 own adjacent right-panel/workspace presentation."
  - L210 (DEL-02-01-REQ-007): "Resolve the exact surviving TYPES §4 row/column query contract with DEL-08-02 before assigning a current compatibility handler."
  - L205 (DEL-02-01-REQ-002): "their exact TYPES §4 query-intent semantics remain keyed with DEL-08-02."
  - L194 (CLM-009): "Own navigation and presentation handoff, preserving the primary dialogue and session identity. Adjacent DEL-02-02/03 and DEL-08-02/03 retain selector, workspace and routing semantics." This is the only text that says "handoff". It names no recipient and no artifact that DEL-08-02 receives.
  - L375 (APP-R017): "DEL-08-02 carries routing and DEL-09-04 carries packaging evidence".
- **Decomposition** (`_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`, `cf6e56eb…`):
  - L413, the SOW-005 reverse view (the L408 of the original note): "DEL-02-01 presents; DEL-08-02 owns aliases, routing, selection guards, and legacy compatibility."
  - L312, the DEL-02-01 row: "Shell integration owns presentation only".
  - L374, the DEL-08-02 row: "Does not own shell presentation, work-plan authority, dispatch semantics, replay evidence, or parent-child records."
- **The counterpart, DEL-08-02:**
  - `ScopeOfWork.md` (`2a9dc258…`):
    - L139, out of scope: "Shell or Work/Agents Coordination Panel presentation, owned by DEL-02-01/02."
    - L72: "DEL-08-02 does not own shell presentation, Work-plan authority, dispatch semantics, replay evidence, child-run parentage, lifecycle, or approval."
  - `_DEPENDENCIES.md` (`65454552…`) L63: "Non-emitted edge note: shared SOW ownership with DEL-02-01 and DEL-02-02 was not converted into execution edges because the allowed source documents do not state a concrete handoff or interface contract to those deliverables." DEL-08-02 records no input from DEL-02-01.
- **Sibling consumers record the same relation as UPSTREAM:**
  - DEP-02-02-020, DEL-02-02 UPSTREAM CONSTRAINT on DEL-08-02: "DEL-08-02 retains routing".
  - DEP-04-04-006, DEL-04-04 UPSTREAM INTERFACE on DEL-08-02.

### HGD-1: recommended ruling, invert

Consequences:
- The graph stays acyclic (S1).
- DEL-08-02, the routing contract, no longer appears to wait on the shell. As recorded today, DEL-02-01 is
  DEL-08-02's only strict supplier.
- DEL-02-01 gains a satisfied gating arc on DEL-08-02 and no blocker verdict changes.
- The inversion also removes the path that makes HGD-3 and FC-2 cycle-forming. Both would then be acyclic if you
  ever chose to emit them.
- DEL-08-02's register needs no write; its L63 note stays true.

Register change, on DEP-02-01-006 only. All other fields and rows stay byte-identical:

| Field | From | To |
|---|---|---|
| `Direction` | `DOWNSTREAM` | `UPSTREAM` |
| `DependencyType` | `HANDOVER` | `INTERFACE` |
| `LastSeen` | `2026-09-27` | the apply date |
| `Notes` | (existing) | existing text, then: `<apply date> UPDATE: INVERTED by owner ruling HGD-1 (verbatim: "<ruling>"). Prior Direction=DOWNSTREAM, DependencyType=HANDOVER. Basis: row Statement; ScopeOfWork.md CLM-015, CLM-027, DEL-02-01-REQ-007; decomposition L413 (SOW-005 reverse view); DEL-08-02 ScopeOfWork.md L139. Graph: APP-HGD-1-3-RECOMMENDATION-2026-09-27 scenario S1 (0 SCC).` |

`Statement`, `EvidenceFile`, `SourceRef`, `EvidenceQuote`, `RequiredMaturity` (SEMANTIC_READY),
`SatisfactionStatus` (TBD), `Confidence`, `Status` (ACTIVE) and `DependencyID` do not change.

`_DEPENDENCIES.md` index changes:
- the Compact Register row for 006 becomes UPSTREAM / INTERFACE;
- the Lifecycle Summary moves from HANDOVER 2 to 1 and from INTERFACE 6 to 7;
- HGD-1 is marked CLOSED at the dated HGD line (L98–99) and in Downstream Handoff Notes (L181).

### HGD-1: alternative, keep DOWNSTREAM HANDOVER

Consequences:
- The graph stays acyclic today.
- DEL-08-02 remains recorded as depending on the shell.
- The row's Statement ("consumes") contradicts its Direction. No current source supplies handover wording to
  repair that.
- Every future DEL-02-01 upstream row to a deliverable that reaches DEL-08-02 closes a cycle. This covers HGD-3,
  FC-2, and anything reaching DEL-04-04 or DEL-02-02.

Register change: none to the row fields. The index records HGD-1 CLOSED with the ruling quoted.

## HGD-3: DEL-02-01-V3-01's prerequisite on DEL-02-02-V3-03

**Row derived from the cited source.** This is the row the 2026-09-05 N1 preview held (`PREVIEW.md` §3). It is
simulated as S2 and its exact fields are in `Evidence/SCENARIOS.json` → `moves.S2`:
- `DEP-02-01-015`: EXECUTION / NOT_APPLICABLE / UPSTREAM / PREREQUISITE / DELIVERABLE, PKG-02, `DEL-02-02` "Right-Panel Coordination, Workflows, and Proposal UX";
- `EvidenceQuote`: "DEL-02-02-V3-03 (the woven route this item re-frames)";
- `RequiredMaturity` SEMANTIC_READY, EXPLICIT / MEDIUM.

Its only source was the `_STATUS.md` `## Remaining` Depends line of DEL-02-01-V3-01. That section was retired on
2026-09-23 (APP-R013, `OWNER_FINAL_RETIREMENT_2026-09-23`). The line survives only in the historical census
`_Reconciliation/…/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv`, which is the `EvidenceFile` the
simulation used.

### HGD-3: recommended ruling, close without emitting

Reasons:
- **No current source.** The register's current-source note (L3) says "The historical Depends text adds no
  prerequisite". The receiving clause APP-R013 (`ScopeOfWork.md` L369) carries no DEL-02-02 dependency. A
  CONSERVATIVE `dependency-extract` run emits only from current sources.
- **The gate is already met.** DEL-02-02-V3-03 landed on 2026-09-06 (PR #733, merge `8e649eaa5`; DEL-02-02
  `_STATUS.md` L14). The row would record a sequencing gate that has already passed.
- **Your ESR-1 ruling set the precedent.** It retired DEP-02-04-015, whose only basis was a gate on the same item:
  "not selectable until DEL-02-02-V3-03 landed", stated nowhere current.
- **Emitting it risks a cycle.** On the current graph the row creates an 11-node SCC (see the findings above).

Consequences: the graph and blockers are unchanged.

Register change: none. `_DEPENDENCIES.md` records HGD-3 CLOSED, with the ruling quoted, at L99 and L181–183.

### HGD-3: alternative, emit the row

This is safe only together with the HGD-1 inversion. S1+S2 gives 104 edges and 0 SCC. Without the inversion, S2
creates the 11-node SCC, holds 15 arcs and fails the closure check. That would need an `scc-resolution-case`.

Register change: add the S2 row, with these differences from the simulated fields:
- `SatisfactionStatus=SATISFIED`, citing PR #733 and DEL-02-02 `_STATUS.md` L14;
- `FirstSeen` and `LastSeen` set to the apply date;
- `Notes` quoting the ruling and stating that its evidence is a retired, historical source.

Expect an evidence-source warning, because the source is retired.

## FC-1 to FC-3

The fence, F1 ("do not make DEL-02-01 an SCC-001 member"), no longer applies as written: the closure has no SCC.
SCC-001 was the nine-node component in `_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0518/Evidence/scc_summary.csv`.
Its history:
1. D-APP-109 merged it into a 20-node SCC (`…_0807/Evidence/scc_summary.csv`).
2. D-APP-110 decomposed five edges: `_Coordination/_DECISIONS/D-APP-110_RULING_SCA_APP_010_SCC_DECOMPOSE_2026-09-05.md`, and `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`, which reports 0 SCC.
3. Every later snapshot, through 1739, reports 0 SCC.

For the original nine, the decisive move is SD-001, which re-targeted DEP-04-05-010 to a DOCUMENT contract. C3 shows
that reversing that move alone restores them. Because each candidate carries a different remaining risk, each needs
its own ruling. The register notes (L181) keep them out "unless separately ruled".

### FC-1: recommended ruling, resolve DEP-02-01-012 to DEL-05-03

The current sources name the owner:
- decomposition L343: DEL-05-03 artifacts "App redaction helper";
- SOW-041 L449;
- DEL-05-03 `ScopeOfWork.md` L67: "Historical helper contract: `frontend/src/lib/harness/run-logger.ts` exports … `redactJsonLike`".

The row's own `Notes` already name DEL-05-03 as a PROPOSAL.

Consequences:
- 0 SCC, with or without HGD-1 (FC1, S1+FC1).
- A satisfied gating arc; no blocker change.
- The `TARGET_UNRESOLVED` warning is cleared.

Register change on DEP-02-01-012:

| Field | From | To |
|---|---|---|
| `TargetType` | `UNKNOWN` | `DELIVERABLE` |
| `TargetPackageID` | (empty) | `PKG-05` |
| `TargetDeliverableID` | (empty) | `DEL-05-03` |
| `TargetRefID` | `TBD` | `DEL-05-03` |
| `TargetName` | `Existing redaction helper under frontend/src/lib/harness/** (derived chat titles, Q6)` | `Redacted RunLogger and Secret Hygiene` (prior value kept in `Notes`) |
| `TargetLocation` | `TBD` | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
| `LastSeen` / `Notes` | | apply date / the ruling verbatim, prior values, and the basis above |

Alternative, keep `UNKNOWN`: nothing changes, and the warning stays.

### FC-2: recommended ruling, close without emitting

Since 2026-09-22 (D-GOV-43/D-APP-127), DEL-02-01's session-record relation is recorded as DEP-02-01-011, an EXTERNAL
row: "Runtime-owned current session record and project identity". No current DEL-02-01 clause names a DEL-03-02
contract. Decomposition L418 maps SOW-010 to DEL-03-02 alone.

Consequences: none.

Alternative, add the FC2 row (`SCENARIOS.json` → `moves.FC2`: UPSTREAM INTERFACE on DEL-03-02, IMPLICIT/MEDIUM,
quoting obligation 8 at L111). This is safe only with the HGD-1 inversion. Without it, the row creates a 7-node SCC.

### FC-3: recommended ruling, close without emitting

The relation is already in the register from the other side. DEP-02-05-014 records DEL-02-05 UPSTREAM PREREQUISITE
on DEL-02-01, SATISFIED: "DEL-02-05 current account row and Settings feedback integrate with the DEL-02-01 shell
host". A deliverable row in the opposite direction pairs with it into a two-node SCC under every HGD-1 choice. The
DEL-02-05-V3-05 gate was sequencing in a retired Remaining line (F3).

Consequences: none.

Alternative: record DEL-02-01's side in the D-APP-110 decompose form, which adds no deliverable edge. The row would
be UPSTREAM INTERFACE, `TargetType=DOCUMENT`, with:
- `TargetRefID=DEL-02-05-ACCOUNT_ROW_PRESENTATION`;
- `TargetName` "DEL-02-05 account row and popover presentation contract";
- `TargetLocation` at DEL-02-05 `ScopeOfWork.md`;
- `EvidenceQuote` "the account row is hosted here and its presentation is DEL-02-05's" (obligation 6, L109).

The deliverable form (`moves.FC3`) is not recommended.

## How a ruling is applied

Each ruling is applied by one `TASK + bundled:chirality-root/dependency-extract` run, as follows:
- **Settings:** `SCOPE=DEL-02-01`, `MODE=UPDATE`, `STRICTNESS=CONSERVATIVE`, apply mode.
- **The rows:** it writes the ruled rows in the form used for the ESR-1 and HGD-2 rulings
  (`AgentRuns/APP-SCA-APP-011-POST-ACCEPTANCE-2026-09-27/dep_extract/apply_esr1_ruling.py`):
  - it sets the ruled fields and quotes the ruling verbatim in `Notes` with the prior values;
  - it keeps every ID and deletes nothing;
  - it assigns any new row the next free `DEP-02-01-NNN`.
- **The index and checks:** it then refreshes the `_DEPENDENCIES.md` index (Function 4) and runs the Function 5
  checks (schema, enum, ID format, parent anchor).
- **Closure snapshot:** a fresh `audit-dep-closure` snapshot follows, with `UPDATE_LATEST_POINTER=false`.
  Rerunning `Evidence/simulate_hgd.py` beforehand confirms the expected result.

Other registers:
- With the recommended rulings, no other register is written.
- Only the FC-3 DOCUMENT alternative, or a ruling that leaves an SCC, would involve other workflows. An SCC would
  need an `scc-resolution-case`.

## Evidence

- `Evidence/SCENARIOS.json`: the exact moves and rows.
- `Evidence/simulate_hgd.py`: the simulation script.
- `Evidence/SIMULATION_RESULTS.csv` and `.json`: the results.
- `Evidence/REACHABILITY.json`: the path witnesses.
- `Evidence/BASIS_CHECK.json`: BASE equals the 1739 snapshot; all 106 basis input hashes match.
- `Evidence/INPUT_HASHES.json`: the tool, spec and register hashes.
- `Evidence/runs/<scenario>/`: `closure_summary.json`, `scc_summary.csv`, `bidirectional_pairs.csv`,
  `cycles_sample.csv`, `blocker_queue.csv`, `blocker_queue_stdout.txt`.
- `Evidence/MANIFEST.sha256`: hashes of all of the above.

Rerun from the repository root:
`python3 projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP-HGD-1-3-RECOMMENDATION-2026-09-27/Evidence/simulate_hgd.py`.
Afterwards, `sha256sum -c` against `Evidence/MANIFEST.sha256` from inside `Evidence/` should pass.
