# Dependency Closure Report - SCC-DECOMPOSE-SCA-APP-010

`AUDIT = SCC-DECOMPOSE-SCA-APP-010` (1034, after the D-APP-110 decompose move applied by N14 and reviewed by N15)

## Verdict

PASS: the strict active deliverable execution graph is acyclic after
`SCC-DECOMPOSE-SCA-APP-010`.

The deterministic closure analyzer reports `scc_count = 0` in
`Evidence/closure_summary.json`. The SCC membership file
`Evidence/scc_summary.csv` contains only the header row. An independent
re-derivation of the strict edge set from the 52 registers agrees with the
analyzer on every shared metric, finds no non-trivial strongly connected
component, and produces a complete Kahn topological order of all 48 connected
nodes (`Evidence/core_checks.json`, `Evidence/topological_order.csv`), which
is the acyclicity witness.

Carried warnings, listed for completeness and unchanged by the move: four
isolated deliverables (`DEL-01-01`, `DEL-09-07`, `DEL-10-04`, `DEL-10-05`),
two canonical-enum non-conformances in the untouched registers `DEL-05-01`
and `DEL-05-05`, and one absolute Root path in the untouched row
`DEP-08-01-013`. None is a blocker, none was introduced or altered by the
move, and no blocking result was upgraded or downgraded.

This snapshot is derivative dependency-closure evidence. It does not replace
decomposition truth, product requirements, source/test evidence, decision
records, or human lifecycle approvals.

## Move Basis

Owner ruling D-APP-110 ("Decompose the SCC, record it as part of PR #714.")
authorized the `decompose` move of `docs/CYCLE_DRIVEN_RESOLUTION.md` section
2.3 against both SCCs recorded by the 0807 snapshot under D-APP-109, in the
form this loop established in `SCC-SAFE-MOVES-001`: a coarse
deliverable-to-deliverable edge that records consumption of a documented
contract is re-targeted to that contract as a `DOCUMENT` node, the row stays
`ACTIVE` with its evidence and its deliverable relation preserved in `Notes`,
and `cut` and `merge` remain human-gated and unused.

This tranche applied only `decompose` moves. No dependency row was retired,
no row was marked out-of-objective, no row was inverted, no deliverable was
merged, no `PREREQUISITE` row was re-targeted or otherwise changed in any
field but `Notes`, and no decomposition package topology was changed
(`Evidence/delta_vs_0807.json`: 0 rows added, 0 removed, 0 `Status` changes,
0 `Direction` changes, 0 `PREREQUISITE` rows with a target or graph change;
`Evidence/move_basis.json` `allRowsPass=true`).

Eligibility was limited to `INTERFACE`, `HANDOVER`, `CONSTRAINT`, and
`ENABLES` rows; the seven rows are four `INTERFACE` and three `HANDOVER` rows.
The workbook `SCC_DECOMPOSE_RULINGS.csv` equals
`Evidence/scc_decompose/decompose_choice.json` (same seven `DependencyID`s,
same five edges). Restoring any one of the five decomposed edges to the live
strict graph re-creates a cycle (`Evidence/move_basis.json`
`eachDecomposedEdgeNecessary`), so no proper subset of the five would have
sufficed; `search_log.txt` records that full enumeration finds exactly two
minimum five-edge sets, the alternative opening the two-node SCC from the
`DEP-08-01-018` side, and that the `DEP-06-03-014` side was chosen for its
documented Scope of Work anchor (recorded here, not adjudicated; issue DC-015).

Rows decomposed from strict deliverable edges into document-scoped contract
targets:

| Dependency ID | Prior strict graph edge | New target |
|---|---|---|
| `DEP-04-05-010` | `DEL-04-05 -> DEL-02-05` | `DOCUMENT` target `DEL-02-05-KEY_STATUS_CONTRACT` |
| `DEP-02-01-010` | `DEL-02-01 -> DEL-02-04` | `DOCUMENT` target `DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1` |
| `DEP-02-04-017` | `DEL-02-01 -> DEL-02-04` | `DOCUMENT` target `DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1` |
| `DEP-02-04-019` | `DEL-02-03 -> DEL-02-04` | `DOCUMENT` target `DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1` |
| `DEP-02-02-022` | `DEL-02-02 -> DEL-02-04` | `DOCUMENT` target `DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1` |
| `DEP-02-04-018` | `DEL-02-02 -> DEL-02-04` | `DOCUMENT` target `DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1` |
| `DEP-06-03-014` | `DEL-06-03 -> DEL-08-01` | `DOCUMENT` target `DEL-08-01-PROPOSAL_TRIGGER_CLAUSES` |

Per-row conformance (`Evidence/move_basis.json`, all seven pass every
check): each row is present exactly once in its workbook carrier with
`Status=ACTIVE`, `DependencyClass=EXECUTION`, `TargetType=DOCUMENT`, empty
`TargetPackageID` and `TargetDeliverableID`, `TargetRefID`, `TargetName`, and
`TargetLocation` byte-equal to the workbook, `Direction` and `DependencyType`
equal to the workbook and to the basis row, a `Notes` clause
`DECOMPOSE 2026-09-05 under D-APP-110 (SD-nnn)` that names the replaced edge,
the contract, and the preserved deliverable relation; the basis row's
`TargetType`/`TargetDeliverableID` equal the workbook's `Previous*` fields and
its derived edge equals the workbook `GraphEdge`; that edge is present in the
0807 edge list with this `DependencyID` and absent from the live strict
graph; the `TargetLocation` file exists and its heading fragment is found in
the file. Six of the seven rows were emitted under D-APP-109 (H-001, H-007,
H-010, H-011, H-012, H-017); `DEP-04-05-010` is pre-existing. Only
`TargetType`, `TargetPackageID`, `TargetDeliverableID`, `TargetRefID`,
`TargetName`, `TargetLocation`, `Notes`, and (for `DEP-04-05-010` alone)
`LastSeen` changed versus the basis.

Preserved strict rows: the thirteen other rows emitted under D-APP-109 stay
strict deliverable edges of the acyclic graph and gate per their
`SatisfactionStatus` exactly like every other strict edge; their `Notes`
changed only by the appended clause
`RESOLVED 2026-09-05: the SCC this row participated in was decomposed under D-APP-110; this row is a strict edge of the acyclic approved graph and gates per its SatisfactionStatus`
(`Evidence/resolved_rows.json`, all thirteen pass every check):

| Dependency ID | Carrier | Strict edge (dependent -> dependency) | Direction / type | `SatisfactionStatus` |
|---|---|---|---|---|
| `DEP-02-02-015` | `DEL-02-02` | `DEL-02-02 -> DEL-05-02` | UPSTREAM INTERFACE | PENDING |
| `DEP-02-02-017` | `DEL-02-02` | `DEL-02-02 -> DEL-08-05` | UPSTREAM INTERFACE | PENDING |
| `DEP-02-02-018` | `DEL-02-02` | `DEL-02-02 -> DEL-05-04` | UPSTREAM INTERFACE | TBD |
| `DEP-02-02-019` | `DEL-02-02` | `DEL-02-02 -> DEL-08-04` | UPSTREAM CONSTRAINT | PENDING |
| `DEP-02-02-020` | `DEL-02-02` | `DEL-02-02 -> DEL-08-02` | UPSTREAM CONSTRAINT | TBD |
| `DEP-02-04-015` | `DEL-02-04` | `DEL-02-04 -> DEL-02-02` | UPSTREAM PREREQUISITE | PENDING |
| `DEP-02-04-016` | `DEL-02-04` | `DEL-02-04 -> DEL-02-03` | UPSTREAM PREREQUISITE | PENDING |
| `DEP-02-05-014` | `DEL-02-05` | `DEL-02-05 -> DEL-02-01` | UPSTREAM PREREQUISITE | PENDING |
| `DEP-02-05-015` | `DEL-02-05` | `DEL-02-05 -> DEL-02-03` | UPSTREAM PREREQUISITE | PENDING |
| `DEP-03-02-013` | `DEL-03-02` | `DEL-08-04 -> DEL-03-02` | DOWNSTREAM INTERFACE | PENDING |
| `DEP-05-02-016` | `DEL-05-02` | `DEL-02-02 -> DEL-05-02` | DOWNSTREAM INTERFACE | TBD |
| `DEP-08-01-018` | `DEL-08-01` | `DEL-08-01 -> DEL-06-03` | UPSTREAM INTERFACE | PENDING |
| `DEP-08-04-013` | `DEL-08-04` | `DEL-08-04 -> DEL-03-02` | UPSTREAM INTERFACE | PENDING |

Six re-targeted emitted rows plus these thirteen are exactly the nineteen
rows emitted under D-APP-109 (H-001 to H-019). The four `PREREQUISITE` rows
in this table changed only in `Notes`; no `PREREQUISITE` row was re-targeted.
The pre-existing rows of the former nine-node SCC that are not re-targeted
(for example `DEP-05-03-010`, `DEP-03-02-006`, `DEP-05-02-012`) are likewise
strict edges of the acyclic graph and are byte-identical to the basis.

## Metrics

| Metric | Baseline (pre-extraction) | 0807 (post D-APP-109) | Current |
|---|---:|---:|---:|
| Total registers | 52 | 52 | 52 |
| Total rows | 580 | 654 | 654 |
| ACTIVE EXECUTION rows | - | 360 | 360 |
| ACTIVE deliverable-endpoint rows | - | 148 | 141 |
| Connected nodes | 46 | 48 | 48 |
| Active strict deliverable execution edges | 99 | 124 | 119 |
| Strict SCC count | 1 | 2 | 0 |
| Largest SCC size | 9 | 20 | 0 |
| Bidirectional pair count | 1 | 4 | 0 |
| Schema-invalid registers (analyzer, columns) | 0 | 0 | 0 |
| Canonical-validator failures (enums) | 2 | 2 | 2 |
| ID normalizations | 0 | 0 | 0 |
| Isolated deliverables | 6 | 4 | 4 |
| Hubs (degree >= 20) | 0 | 0 | 0 |

Evidence:

- `Evidence/closure_summary.json`
- `Evidence/scc_summary.csv`
- `Evidence/coverage.csv`
- `Evidence/orphans.csv`
- `Evidence/bidirectional_pairs.csv`
- `Evidence/hubs.csv`
- `Evidence/id_normalization.csv`
- `Evidence/edge_list.csv`, `Evidence/topological_order.csv`, `Evidence/core_checks.json`
- `Evidence/delta_vs_0807.json`, `Evidence/delta_vs_baseline.json`, `Evidence/fanin_agreement.json`
- `Evidence/move_basis.json`, `Evidence/resolved_rows.json`, `Evidence/refreshed_registers.json`
- `Evidence/posture_checks.json`, `Evidence/schema_validation.json`

## Core checks

| Check | Verdict | Result and evidence |
| --- | --- | --- |
| Schema compliance | PASS (analyzer) / WARNING (canonical enums) | 52/52 registers carry all v3.1 columns (`Evidence/coverage.csv`). The canonical validator passes 50/52; the 2 failures are enum values outside `docs/SPEC.md` Section 6.3 in registers untouched by SCA-APP-010 and by N14 (`Evidence/schema_validation.json`; issues DC-006, DC-007). All ten N14 carriers pass, including the new `DOCUMENT` targets. |
| Orphan dependency endpoints | PASS | 141/141 active deliverable endpoints resolve to discovered deliverables; 0 unresolved (`Evidence/core_checks.json`). |
| Circular dependencies | PASS | 0 non-trivial SCCs (Tarjan, analyzer and supplement); Kahn order covers all 48 nodes; `Evidence/scc_summary.csv` header only; `Evidence/cycles_sample.csv` header only; `MAX_CYCLES=10000` not exercised (issue DC-001 records the resolution). |
| Anchor coverage | PASS | 52 present, 0 missing (`Evidence/coverage.csv`). |
| Misplaced fields | PASS | 0 ACTIVE EXECUTION rows with a non-DELIVERABLE `TargetType` and a populated `TargetDeliverableID` (the seven re-targeted rows have empty `TargetDeliverableID`); 0 DELIVERABLE-typed rows without a target; 0 invalid directions. |
| ID format consistency | PASS | 0 normalizations (`Evidence/id_normalization.csv`). |
| Isolated deliverables | WARNING | `DEL-01-01`, `DEL-09-07`, `DEL-10-04`, `DEL-10-05` (`Evidence/orphans.csv`; issues DC-002 to DC-005); unchanged from the 0807 run. |
| Hub analysis | PASS | 0 nodes at degree 20 or above (`Evidence/hubs.csv`); highest total degree is `DEL-09-02` at 15 (2 in, 13 out). |
| Bidirectional pairs | PASS (none) | The analyzer reports zero (`Evidence/bidirectional_pairs.csv` header only). The 0807 run's four pairs `DEL-02-02`/`DEL-02-04`, `DEL-02-03`/`DEL-02-04`, `DEL-02-05`/`DEL-04-05`, and `DEL-06-03`/`DEL-08-01` are all dissolved by the move, one side of each having been re-targeted. |

## Graph

- Nodes: 48 connected deliverables of 52 discovered; edges: 119 distinct directed edges from 141 ACTIVE EXECUTION DELIVERABLE rows (360 ACTIVE EXECUTION rows in total; 21 RETIRED EXECUTION rows excluded).
- Direction convention: a live edge `X -> Y` means X depends on Y (an `UPSTREAM` row of X targeting Y, or a `DOWNSTREAM` row of Y targeting X). The full edge list with contributing `DependencyID`s is `Evidence/edge_list.csv` (the `SCCInternal` column is empty for every edge).
- Acyclic by construction: the strict active edge set is now acyclic, as `docs/CYCLE_DRIVEN_RESOLUTION.md` section 4 requires of an approved graph, and it became so through a recorded move on named rows rather than through any silent linearization. Every strict edge, including the thirteen resolved rows, gates per its `SatisfactionStatus`; no edge is held non-gating by cycle participation, because no cycle exists.

## Delta versus the 0807 snapshot

| Metric | 0807 run (basis `f38f1448` + N8/N9 tree) | This run (1034; basis `7eb4b0c7` + N13/N14/N15 tree) |
| --- | --- | --- |
| `total_files` | 52 | 52 |
| `total_rows` | 654 | 654 |
| `anchor_rows` | 273 | 273 |
| `execution_rows` | 381 | 381 |
| ACTIVE deliverable-endpoint rows | 148 | 141 |
| `graph_nodes` | 48 | 48 |
| `graph_edges` | 124 | 119 |
| `orphan_count` (isolates) | 4 | 4 |
| `scc_count` | 2 | 0 |
| `scc_sizes` | [2, 20] | [] |
| `bidirectional_pair_count` | 4 | 0 |
| `hub_count` | 0 | 0 |
| `normalization_count` | 0 | 0 |

- The committed basis `7eb4b0c7` carries the 0807 registers: deriving the strict edge set from `git show 7eb4b0c7:<path>` for all 52 registers reproduces the 0807 `Evidence/edge_list.csv` exactly, edge for edge and `DependencyID` for `DependencyID` (`Evidence/delta_vs_0807.json` `basisRegistersReproduce0807EdgeList=true`).
- Directed edges removed: exactly five, the workbook's five (`DEL-02-01 -> DEL-02-04` carried by `DEP-02-01-010`+`DEP-02-04-017`; `DEL-02-02 -> DEL-02-04` by `DEP-02-02-022`+`DEP-02-04-018`; `DEL-02-03 -> DEL-02-04` by `DEP-02-04-019`; `DEL-04-05 -> DEL-02-05` by `DEP-04-05-010`; `DEL-06-03 -> DEL-08-01` by `DEP-06-03-014`); the first four were internal to the 0807 `SCC-002` and the fifth to `SCC-001`. Directed edges added: none. Common edges whose carrying rows changed: none.
- Registers changed versus the basis: exactly the ten N14 carriers `DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-02-05`, `DEL-03-02`, `DEL-04-05`, `DEL-05-02`, `DEL-06-03`, `DEL-08-01`, `DEL-08-04`. Row-level diff over all 52 registers: 0 rows added, 0 removed, 7 rows re-targeted, 13 rows changed in `Notes` only, 0 rows otherwise changed, 0 `Status` changes, 0 `Direction` changes.
- Nodes connected or disconnected: none (48 before and after; `DEL-02-04` and `DEL-08-01` keep other strict edges). Isolates: identical. Hubs: none before or after. Bidirectional pairs: 4 -> 0.
- Against the pre-extraction baseline (`Evidence/delta_vs_baseline.json`): 46 -> 48 nodes, 99 -> 119 edges, 6 -> 4 isolates, SCC [9] -> []; the 0518 run added ten edges, the 0807 run the fifteen emitted edges, and this run removes five by re-targeting.
- Against the parent's live check (`Evidence/fanin_agreement.json`): `closure_summary.json` identical field for field to `Evidence/fanin_live_v1.3/closure_summary.json`; SCC summary, bidirectional pairs, isolates, and hubs identical; the brief's expected `scc_count = 0`, 48 nodes, 119 edges met.

## Accepted A2-B ordering comparison

Orientation note: in `DAG.md` a solid edge `A --> B` means A precedes B, so it corresponds to a live register edge `B -> A`; a dashed edge is objective feedback inside an accepted SCC and is non-gating.

| Accepted SCC and feedback edge | Live evidence | Conclusion |
| --- | --- | --- |
| `SCC-DELEGATION-EVIDENCE`; `E-020` `DEL-08-05 - -> DEL-08-04` [NON-GATING] | Live edge `DEL-08-05 -> DEL-08-04` only, carried by `DEP-08-04-006`, `DEP-08-05-004`, `DEP-08-05-011` (the accepted gating orientation E-019); no live `DEL-08-04 -> DEL-08-05` row. DEL-08-04 carries exactly one managed-class row (`DEP-08-04-009`) and one native-class row (`DEP-08-04-010`); DEL-08-05 exactly one of each (`DEP-08-05-004`, `DEP-08-05-011`); the native rows deny Agent-role inference. The pair no longer lies inside any live SCC (it lay inside the 0807 `SCC-002`). | E-020 remains objective-relative and non-gating; no feedback row invented; accepted move `DECOMPOSE` preserved; the 0807 enclosure is dissolved. |
| `SCC-ACCOUNT-MIGRATION-UX`; `E-018` `DEL-05-04 - -> DEL-02-05` [NON-GATING] | No live row in either orientation between `DEL-05-04` and `DEL-02-05`. The pair no longer lies inside any live SCC (it lay inside the 0807 `SCC-002`). | E-018 remains objective-relative and non-gating; no row invented; accepted move `DECOMPOSE` preserved; enclosure dissolved. |
| `SCC-RUNBOOK-VALIDATION`; `E-032` `DEL-09-05 - -> DEL-09-06` [NON-GATING] | Live edge `DEL-09-05 -> DEL-09-06` only (`DEP-09-05-009`, the accepted gating orientation E-031); no live `DEL-09-06 -> DEL-09-05` row; neither node is in a live SCC. | E-032 remains objective-relative and non-gating; accepted move `INVERT` preserved. |

Accepted source identity: `DAG.md` SHA-256 `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996` (verified live, `Evidence/posture_checks.json`).

## Root-owned targets in the swept carriers

The sweep covers the fourteen carriers touched across SCA-APP-010 (the thirteen of the 0807 run plus `DEL-04-05`, which carries no `EXTERNAL` row).

- 18 `EXTERNAL` rows; 16 carry `TargetLocation=TBD`; every Root-named EXTERNAL row is `TBD`. The remaining 2 (`DEP-08-04-009`, `DEP-08-04-010`) are the descendant-class rows whose `TargetLocation` is the repo-relative App decomposition (issue DC-010). Unchanged from the 0807 run.
- No re-targeted row is `EXTERNAL` and none proposes a Root path: all seven new `TargetLocation` values are repo-relative `ScopeOfWork.md` anchors inside `projects/chirality-app-dev/execution/`. The single absolute Root path in the swept carriers is the pre-existing `DEP-08-01-013` (`TargetType=DOCUMENT`), byte-identical to the basis in every field (issue DC-008); the N14 Notes-only edit to `DEP-08-01-018` left it unchanged as required. Three further pre-existing absolute filesystem paths exist outside the swept carriers (`DEP-01-01-011`, `DEP-01-02-013`, `DEP-07-02-004`; issue DC-009); the sweep in `Evidence/posture_checks.json` also lists `DEP-07-05-025`, whose `TargetLocation` is an API route string (`/api/working-root/...`), not a filesystem path.

## Canonical validator findings outside SCA-APP-010

| Register | Findings |
| --- | --- |
| `DEL-05-01` | `Row 7 invalid TargetType: 'CODE' (DependencyID=DEP-05-01-006)`; `Row 10 invalid TargetType: 'DECISION' (DependencyID=DEP-05-01-009)` |
| `DEL-05-05` | `Row 10 invalid TargetType: 'CODE' (DependencyID=DEP-05-05-009)`; `Row 11 invalid TargetType: 'DECISION' (DependencyID=DEP-05-05-010)` |

Both registers are byte-identical to the basis, outside every SCA-APP-010 and N14 write set, and the affected rows are not DELIVERABLE-typed, so the live graph is unaffected. Same finding and calibration as the 0518 and 0807 runs (`Decision_Log.md` DEC-008).

## Validation Command

```sh
PYTHONDONTWRITEBYTECODE=1 python3 tools/coordination/analyze_dep_closure.py \
  projects/chirality-app-dev/execution \
  --output-dir projects/chirality-app-dev/execution/_Reconciliation/DepClosure/CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034/Evidence
```

## Not claimed

- This audit does not accept this snapshot as the loop's DepClosure pointer. `_Reconciliation/DepClosure/_LATEST.md` was not moved (it still names `CLOSURE_D53A_DEP_RECONCILIATION_2026-07-11_0224Z`); acceptance is an owner act.
- It grants no implementation, activation, selection, lifecycle-transition, dependency-acceptance, signing, release, pointer-movement, or Root authority, and it authorizes no source repair. The carried warnings are reported, not fixed.
- It does not adjudicate the semantic fit of the seven decompose moves (that a row records contract consumption rather than build sequencing); it verifies their structural conformance to the workbook and the ruling, the existence of the cited contract anchors, and the graph result. Semantic fit was reviewed row by row in `REVIEW_v1.3.md` Check 1, which this audit consumes but does not re-perform.
- It does not claim the chosen five-edge set is the unique minimum; the recorded search finds two, and the choice between them is the parent's recorded rationale under the owner's directed move (issue DC-015).
- It does not claim that the acyclic graph is the correct ordering. SCC analysis catches circular subjectivity only (`docs/CYCLE_DRIVEN_RESOLUTION.md` section 3); an acyclic-but-wrong ordering is not detected here.
- It does not claim that any `DOCUMENT` contract target or any strict edge is satisfied: the seven re-targeted rows carry `SatisfactionStatus` PENDING (six) or TBD (one), and the thirteen resolved rows PENDING (ten) or TBD (three). Gating per `SatisfactionStatus` is the consumer's act under its own instruments.
- It makes no cut, merge, inversion, or linearization, proposes none, and re-runs no search.

## Closure statement

This derivative audit package is current to the committed basis
`7eb4b0c79e9fda39a1599ef5ef0dcf4d9d846985` (equal to `HEAD` at run time), the
uncommitted N13/N14/N15 working tree, and the ten carriers' post-write
identities pinned in `Evidence/n14_postwrite_identities.json` and verified in
`Evidence/refreshed_registers.json`. It records that the strict active
deliverable execution graph is acyclic after the D-APP-110 decompose move and
that the move was applied exactly as ruled. `SCC-DECOMPOSE-SCA-APP-010`
therefore produces fresh closure evidence with `scc_count = 0`; the next step
is the parent's fan-in (amendment v1.3 node N17), and acceptance of this
snapshot as the loop's DepClosure snapshot (`_Reconciliation/DepClosure/_LATEST.md`)
is an owner act. Any later recorded move, decomposition revision, or scope
change requires a fresh closure audit.
