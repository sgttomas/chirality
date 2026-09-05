# Dependency Closure Report

`AUDIT = SCA-APP-010-GATE5-POST-APPLICATION`

## Verdict

`WARNINGS`

The post-application registers close structurally: 52/52 registers are readable and column-schema-valid, 635/635 rows carry evidence, 52/52 deliverables have an `IMPLEMENTS_NODE` anchor, and 129/129 active deliverable endpoints resolve. The thirteen refreshed carriers match their pinned identities exactly. `SCC-001` is reported with membership identical to the baseline and to the SCA-APP-008 audit; no SCC-internal edge was added or retired; no new SCC and no new cycle exists. The warnings are the pre-existing nine-node SCC, four isolated deliverables, two pre-existing enum non-conformances in unchanged registers, and one pre-existing absolute Root path in an unchanged row of DEL-08-01. Nothing here is a blocker, and no blocking result was upgraded.

## Core checks

| Check | Verdict | Result and evidence |
| --- | --- | --- |
| Schema compliance | PASS (analyzer) / WARNING (canonical enums) | 52/52 registers carry all v3.1 columns (`Evidence/coverage.csv`, `Evidence/closure_summary.json`). The canonical validator passes 50/52; the 2 failures are enum values outside `docs/SPEC.md` Section 6.3 in registers untouched by this refresh (`Evidence/schema_validation.json`; issues DC-007, DC-008). |
| Orphan dependency endpoints | PASS | 129/129 active deliverable endpoints resolve to discovered deliverables; 0 unresolved (`Evidence/core_checks.json`). |
| Circular dependencies | WARNING | One directed SCC of nine nodes, 10 elementary cycles, 14 SCC-internal directed edges (`Evidence/scc_summary.csv`, `Evidence/cycles_sample.csv`, `Evidence/edge_list.csv`; issue DC-001). Membership and internal edge set identical to baseline and SCA-APP-008 (`Evidence/delta_vs_baseline.json`, `Evidence/delta_vs_sca_app_008.json`). |
| Anchor coverage | PASS | 52 present, 0 missing (`Evidence/coverage.csv`). |
| Misplaced fields | PASS | 0 ACTIVE EXECUTION rows with a non-DELIVERABLE `TargetType` and a populated `TargetDeliverableID`; 0 invalid directions (`Evidence/core_checks.json`). |
| ID format consistency | PASS | 0 normalizations (`Evidence/id_normalization.csv`). |
| Isolated deliverables | WARNING | `DEL-01-01`, `DEL-09-07`, `DEL-10-04`, `DEL-10-05` (`Evidence/orphans.csv`; issues DC-002 to DC-005). Two baseline isolates (`DEL-01-03`, `DEL-02-04`) were connected by the refresh. |
| Hub analysis | PASS | 0 nodes at degree 20 or above (`Evidence/hubs.csv`). |
| Bidirectional pairs | INFO | `DEL-02-05` / `DEL-04-05` through `DEP-02-05-004` and `DEP-04-05-010` (`Evidence/bidirectional_pairs.csv`; issue DC-006). |

## Graph

- Nodes: 48 connected deliverables of 52 discovered; edges: 109 distinct directed edges from 129 ACTIVE EXECUTION DELIVERABLE rows (341 ACTIVE EXECUTION rows in total; 21 RETIRED EXECUTION rows excluded).
- Direction convention: a live edge `X -> Y` means X depends on Y (an `UPSTREAM` row of X targeting Y, or a `DOWNSTREAM` row of Y targeting X). The full edge list with contributing `DependencyID`s is `Evidence/edge_list.csv`.

## Live directed SCC

`SCC-001` (9 nodes):

```text
DEL-02-05
DEL-03-02
DEL-03-03
DEL-03-04
DEL-04-03
DEL-04-05
DEL-05-02
DEL-05-03
DEL-05-05
```

Shortest representative: `DEL-02-05 -> DEL-04-05 -> DEL-02-05` (`DEP-02-05-004`, `DEP-04-05-010`). Elementary cycles inside `SCC-001` (bounded at 10000; complete):

| Cycle | Length | Nodes |
| --- | --- | --- |
| `CYCLE-001` | 2 | `DEL-02-05;DEL-04-05;DEL-02-05` |
| `CYCLE-002` | 6 | `DEL-02-05;DEL-03-03;DEL-03-02;DEL-05-02;DEL-04-03;DEL-04-05;DEL-02-05` |
| `CYCLE-003` | 6 | `DEL-02-05;DEL-03-03;DEL-03-02;DEL-05-02;DEL-05-03;DEL-04-05;DEL-02-05` |
| `CYCLE-004` | 6 | `DEL-02-05;DEL-03-03;DEL-03-04;DEL-05-02;DEL-04-03;DEL-04-05;DEL-02-05` |
| `CYCLE-005` | 6 | `DEL-02-05;DEL-03-03;DEL-03-04;DEL-05-02;DEL-05-03;DEL-04-05;DEL-02-05` |
| `CYCLE-006` | 7 | `DEL-02-05;DEL-03-03;DEL-03-02;DEL-05-02;DEL-05-05;DEL-05-03;DEL-04-05;DEL-02-05` |
| `CYCLE-007` | 7 | `DEL-02-05;DEL-03-03;DEL-03-04;DEL-03-02;DEL-05-02;DEL-04-03;DEL-04-05;DEL-02-05` |
| `CYCLE-008` | 7 | `DEL-02-05;DEL-03-03;DEL-03-04;DEL-03-02;DEL-05-02;DEL-05-03;DEL-04-05;DEL-02-05` |
| `CYCLE-009` | 7 | `DEL-02-05;DEL-03-03;DEL-03-04;DEL-05-02;DEL-05-05;DEL-05-03;DEL-04-05;DEL-02-05` |
| `CYCLE-010` | 8 | `DEL-02-05;DEL-03-03;DEL-03-04;DEL-03-02;DEL-05-02;DEL-05-05;DEL-05-03;DEL-04-05;DEL-02-05` |

The cycle set is identical to the ten cycles recorded by the SCA-APP-008 audit (`Evidence/delta_vs_sca_app_008.json` `cycleSetIdentical=true`). This SCC is surfaced without a proposed cut, merge, inversion, or linearization; its resolution belongs to the cycle-resolution workflow.

## Comparison with the baseline and the SCA-APP-008 audit

| Metric | Baseline (basis `d66395d10114`) | SCA-APP-008 audit (2026-08-24) | This audit |
| --- | --- | --- | --- |
| `total_files` | 52 | 51 | 52 |
| `total_rows` | 580 | 564 | 635 |
| `anchor_rows` | 249 | 247 | 273 |
| `execution_rows` | 331 | 317 | 362 |
| `graph_nodes` | 46 | 46 | 48 |
| `graph_edges` | 99 | 98 | 109 |
| `orphan_count` | 6 | 5 | 4 |
| `scc_count` | 1 | 1 | 1 |
| `scc_sizes` | [9] | [9] | [9] |
| `bidirectional_pair_count` | 1 | 1 | 1 |
| `hub_count` | 0 | 0 | 0 |
| `normalization_count` | 0 | 0 | 0 |

- Baseline agreement: the basis graph reconstructed from `HEAD` reproduces the baseline snapshot exactly (graph_nodes, graph_edges, orphan_count, isolates, scc all equal; `Evidence/delta_vs_baseline.json`).
- Registers changed in the working tree relative to basis: exactly the thirteen refreshed carriers (`DEL-02-01`, `DEL-02-02`, `DEL-02-04`, `DEL-02-05`, `DEL-03-02`, `DEL-04-04`, `DEL-05-02`, `DEL-06-03`, `DEL-07-01`, `DEL-07-03`, `DEL-08-01`, `DEL-08-03`, `DEL-08-04`); no register was added or removed by the refresh. `DEL-09-07` was added between the SCA-APP-008 audit and the basis (PR #712) and is isolated in both the baseline and this audit.
- Nodes connected by the refresh: `DEL-01-03`, `DEL-02-04`; nodes disconnected: none.
- Directed edges added by the refresh (10); edges retired: 0.

| Added edge (dependent -> dependency) | Carrying rows | SCC-internal |
| --- | --- | --- |
| `DEL-02-01` -> `DEL-01-03` | `DEP-02-01-014` | no (neither endpoint is an SCC-001 member) |
| `DEL-02-01` -> `DEL-07-01` | `DEP-02-01-009` | no (neither endpoint is an SCC-001 member) |
| `DEL-02-02` -> `DEL-06-03` | `DEP-02-02-014`; `DEP-06-03-016` | no (neither endpoint is an SCC-001 member) |
| `DEL-02-02` -> `DEL-07-03` | `DEP-02-02-013`; `DEP-07-03-012` | no (neither endpoint is an SCC-001 member) |
| `DEL-02-04` -> `DEL-07-03` | `DEP-02-04-020` | no (neither endpoint is an SCC-001 member) |
| `DEL-04-04` -> `DEL-07-01` | `DEP-04-04-014`; `DEP-07-01-010` | no (neither endpoint is an SCC-001 member) |
| `DEL-04-04` -> `DEL-07-03` | `DEP-04-04-013`; `DEP-07-03-013` | no (neither endpoint is an SCC-001 member) |
| `DEL-05-02` -> `DEL-06-03` | `DEP-06-03-017` | no (at most one endpoint is an SCC-001 member) |
| `DEL-08-01` -> `DEL-07-01` | `DEP-08-01-019` | no (neither endpoint is an SCC-001 member) |
| `DEL-09-04` -> `DEL-02-01` | `DEP-02-01-013` | no (neither endpoint is an SCC-001 member) |

- SCC-internal edges added or retired by the refresh: **none** (`sccInternalEdgesAdded=[]`, `sccInternalEdgesRemoved=[]`); the fourteen SCC-internal edges carry the same `DependencyID`s before and after (`Evidence/delta_vs_baseline.json` `sccInternalEdgeIds`). Amendment v1.1 section B permitted evidence-field refreshes on SCC-internal rows only; the graph-bearing fields are unchanged.
- SCC membership versus baseline: identical (`DEL-02-05;DEL-03-02;DEL-03-03;DEL-03-04;DEL-04-03;DEL-04-05;DEL-05-02;DEL-05-03;DEL-05-05`). New SCCs: none. New cycles: none. Bidirectional pairs: unchanged (one). Hubs: none before or after.
- Isolates: baseline 6 -> 4; resolved `DEL-01-03`, `DEL-02-04`; new: none.

## Accepted A2-B ordering comparison

Orientation note: in `DAG.md` a solid edge `A --> B` means A precedes B, so it corresponds to a live register edge `B -> A`; a dashed edge is objective feedback inside an accepted SCC and is non-gating.

| Accepted SCC and feedback edge | Live evidence | Conclusion |
| --- | --- | --- |
| `SCC-DELEGATION-EVIDENCE`; `E-020` `DEL-08-05 - -> DEL-08-04` [NON-GATING] | Live edge `DEL-08-05 -> DEL-08-04` only, carried by `DEP-08-04-006`, `DEP-08-05-004`, `DEP-08-05-011` (the accepted gating orientation E-019); no live `DEL-08-04 -> DEL-08-05` row. DEL-08-04 carries exactly one managed-class row (`DEP-08-04-009`) and one native-class row (`DEP-08-04-010`, "without assigning an Agent 0 1 or 2 role"); DEL-08-05 carries exactly one managed-class row (`DEP-08-05-004`) and one native-class row (`DEP-08-05-011`, "without assigning an Agent 0/1/2 role"). | E-020 remains objective-relative and non-gating; no feedback row invented; accepted move `DECOMPOSE` preserved; WP-03/WP-05 fixtures (`DEP-08-04-011`) remain an EXTERNAL constraint with `TargetLocation=TBD`. |
| `SCC-ACCOUNT-MIGRATION-UX`; `E-018` `DEL-05-04 - -> DEL-02-05` [NON-GATING] | No live row in either orientation between `DEL-05-04` and `DEL-02-05`. DEL-02-05 retains `DEP-02-05-004` (DEL-04-05) and `DEP-02-05-006` (DEL-03-03) as SCC-internal rows with graph fields unchanged, and its Root account/consent rows (`DEP-02-05-008`, `-009`, `-013`) as EXTERNAL with `TargetLocation=TBD`. | E-018 remains objective-relative and non-gating; no row invented; accepted move `DECOMPOSE` preserved. |
| `SCC-RUNBOOK-VALIDATION`; `E-032` `DEL-09-05 - -> DEL-09-06` [NON-GATING] | Live edge `DEL-09-05 -> DEL-09-06` only (`DEP-09-05-009`, the accepted gating orientation E-031, a live security interface); no live `DEL-09-06 -> DEL-09-05` row. Neither register was touched by this refresh. | E-032 remains objective-relative and non-gating; accepted move `INVERT` preserved; G6a exact-candidate gate retained. |

Accepted source identities: `DAG.md` SHA-256 `0b721c2e4c461b134cf62baf9a6df87d3ee45257ddbb0bf58e3a4358a9266996` (verified live), `WORK_GRAPH.json` `273c14cc9abe8b2f61696757507b1879479f2ac5d0b94138b6a8fcc07d5e6428` (as recorded by the SCA-APP-008 audit).

## Root-owned targets in the thirteen refreshed registers

- 18 `EXTERNAL` rows; 16 carry `TargetLocation=TBD`: `DEP-02-01-011`, `DEP-02-02-016`, `DEP-02-04-021`, `DEP-02-05-008`, `DEP-02-05-009`, `DEP-02-05-013`, `DEP-03-02-014`, `DEP-03-02-015`, `DEP-05-02-013`, `DEP-05-02-015`, `DEP-06-03-018`, `DEP-07-03-014`, `DEP-08-01-020`, `DEP-08-01-021`, `DEP-08-04-011`, `DEP-08-04-014`.
- The remaining 2 (`DEP-08-04-009`, `DEP-08-04-010`) are the descendant-class rows whose `TargetLocation` is the repo-relative App decomposition, not a Root path; both pre-date this refresh (issue DC-011).
- No refreshed row proposes a Root path. The single absolute Root path in the thirteen carriers is the pre-existing `DEP-08-01-013` (`TargetType=DOCUMENT`), byte-identical at basis and already on the owner slate (HANDOFF_STATE.md R-004; issue DC-009). Three further pre-existing absolute paths exist outside the refreshed set (issue DC-010).

## Held edge proposals (non-emitted)

`HELD_EDGE_PROPOSALS.csv` records 19 register rows (15 distinct directed edges) that HELP_HUMAN's amendment v1.1 removed from the N1 post-images before any register was written, because the fan-in simulation showed that together they would merge `SCC-001` into a twenty-node SCC and create a new two-node SCC (`DEL-06-03` / `DEL-08-01`), while none of them alone changes the SCC set. Choosing among them would be a cut, which `docs/CYCLE_DRIVEN_RESOLUTION.md` makes human-gated, and SCA-APP-010 `DOWNSTREAM_HANDOFFS.csv` row 3 requires the SCC unchanged unless separately ruled. They are therefore **not emitted** and this audit does not treat them as edges: none of the 19 reserved `DependencyID`s exists in any live register and none of the held edges exists in the live graph (`Evidence/posture_checks.json` `heldProposals`). All carry `Disposition=HELD_NON_EMITTED_PENDING_OWNER_RULING`.

| Held | Carrier | Reserved ID | Edge (dependent -> dependency) | Would form or join |
| --- | --- | --- | --- | --- |
| `H-001` | `DEL-02-01` | `DEP-02-01-010` | `DEL-02-01` -> `DEL-02-04` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-002` | `DEL-02-02` | `DEP-02-02-015` | `DEL-02-02` -> `DEL-05-02` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-003` | `DEL-02-02` | `DEP-02-02-017` | `DEL-02-02` -> `DEL-08-05` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-004` | `DEL-02-02` | `DEP-02-02-018` | `DEL-02-02` -> `DEL-05-04` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-005` | `DEL-02-02` | `DEP-02-02-019` | `DEL-02-02` -> `DEL-08-04` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-006` | `DEL-02-02` | `DEP-02-02-020` | `DEL-02-02` -> `DEL-08-02` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-007` | `DEL-02-02` | `DEP-02-02-022` | `DEL-02-02` -> `DEL-02-04` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-008` | `DEL-02-04` | `DEP-02-04-015` | `DEL-02-04` -> `DEL-02-02` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-009` | `DEL-02-04` | `DEP-02-04-016` | `DEL-02-04` -> `DEL-02-03` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-010` | `DEL-02-04` | `DEP-02-04-017` | `DEL-02-01` -> `DEL-02-04` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-011` | `DEL-02-04` | `DEP-02-04-018` | `DEL-02-02` -> `DEL-02-04` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-012` | `DEL-02-04` | `DEP-02-04-019` | `DEL-02-03` -> `DEL-02-04` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-013` | `DEL-02-05` | `DEP-02-05-014` | `DEL-02-05` -> `DEL-02-01` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-014` | `DEL-02-05` | `DEP-02-05-015` | `DEL-02-05` -> `DEL-02-03` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-015` | `DEL-03-02` | `DEP-03-02-013` | `DEL-08-04` -> `DEL-03-02` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-016` | `DEL-05-02` | `DEP-05-02-016` | `DEL-02-02` -> `DEL-05-02` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |
| `H-017` | `DEL-06-03` | `DEP-06-03-014` | `DEL-06-03` -> `DEL-08-01` | new two-node SCC DEL-06-03/DEL-08-01 |
| `H-018` | `DEL-08-01` | `DEP-08-01-018` | `DEL-08-01` -> `DEL-06-03` | new two-node SCC DEL-06-03/DEL-08-01 |
| `H-019` | `DEL-08-04` | `DEP-08-04-013` | `DEL-08-04` -> `DEL-03-02` | joins SCC-001 into the simulated 20-node SCC (with the other held edges) |

Any owner ruling that emits some or all of these rows changes the graph and requires a fresh closure audit.

## Canonical validator findings outside the refresh

| Register | Findings |
| --- | --- |
| `DEL-05-01` | `Row 7 invalid TargetType: 'CODE' (DependencyID=DEP-05-01-006; allowed=DELIVERABLE, DOCUMENT, EQUIPMENT, EXTERNAL, PACKAGE, REQUIREMENT, UNKNOWN, WBS_NODE)`; `Row 10 invalid TargetType: 'DECISION' (DependencyID=DEP-05-01-009; allowed=DELIVERABLE, DOCUMENT, EQUIPMENT, EXTERNAL, PACKAGE, REQUIREMENT, UNKNOWN, WBS_NODE)` |
| `DEL-05-05` | `Row 10 invalid TargetType: 'CODE' (DependencyID=DEP-05-05-009; allowed=DELIVERABLE, DOCUMENT, EQUIPMENT, EXTERNAL, PACKAGE, REQUIREMENT, UNKNOWN, WBS_NODE)`; `Row 11 invalid TargetType: 'DECISION' (DependencyID=DEP-05-05-010; allowed=DELIVERABLE, DOCUMENT, EQUIPMENT, EXTERNAL, PACKAGE, REQUIREMENT, UNKNOWN, WBS_NODE)` |

Both registers are byte-identical to the basis, were not part of the SCA-APP-010 write set, and their affected rows are not DELIVERABLE-typed, so the live graph is unaffected. The registered analyzer's column-level schema check passes them; the finding is surfaced for the owner because the audit contract asks for v3.1 verification of every discovered register.

## Closure statement

This derivative audit package is current to the applied decomposition (`c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`), the basis commit `d66395d101143df68d956984f7ab93f5027418ec`, and the thirteen refreshed register identities pinned in `Brief.md` and `Evidence/refreshed_registers.json`. It is warning-bearing but not blocking. It grants no source repair, pointer movement, activation, implementation, or release authority; acceptance of this snapshot as the loop's DepClosure snapshot (`_Reconciliation/DepClosure/_LATEST.md`) is an owner act.
