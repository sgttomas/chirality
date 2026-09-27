# SCA-APP-011 — dependency-extract: expected outcomes and the HGD-2 decision

**Status: not run.** No `Dependencies.csv` or `_DEPENDENCIES.md` is written.

## What this file is

This file lists **what the extraction is expected to produce**. It is not a set
of values for the owner to approve.
- The bundled `dependency-extract` workflow "Runs straight-through; never
  blocks on human decisions" (`workflows/dependency-extract/WORKFLOW.md` line 28).
- In `MODE: UPDATE` it derives rows from the source text: it matches existing
  IDs, sets `LastSeen`, and marks unseen extracted rows `RETIRED`.
- So the owner does not approve field values. The post-extraction
  `audit-scope-closure` checks each outcome below against the register.

## Why it has not run

This loop runs `dependency-extract` as `project-setup` Function 5, Phase 5.6.
That phase comes after the Phase 5.0 baseline and the Phase 5.1 plan, and both
need the owner's confirmation (`INCREMENTAL_SETUP_PROPOSAL.md`). Nothing about
the extraction itself needs an owner act, except the HGD-2 ruling on
DEP-02-01-008.

**Scope.** Under FULL_GRAPH the run covers:
- the 9 modified deliverables;
- their 16 neighbours with ACTIVE edges (see the setup proposal);
- one brief per deliverable in `MODE: UPDATE`;
- then `audit-dep-closure` over SCOPE ALL.

## Already accepted: not asked again

The following were settled when SCA-APP-011 was accepted, so they are outcomes,
not questions:
- **Retire DEP-02-01-007.**
  - Accepted at group 1: `Impact_Assessment.md` line 389, DQ-R column: "Retire
    DEP-02-01-007".
  - Accepted at group 2: `Propagation_Plan.md` §8 item 2, lines 476–477.
  - The DEP-02-01-007 half of HGD-2 is resolved by that acceptance.
- **Retire DEP-02-02-005 to 009.**
- **Refresh the wording of DEP-08-03-010 and DEP-08-02-003/005.**

## Expected outcomes

The exact checks are in `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.csv`, one row
each.

| ID | Row | Expected outcome |
|---|---|---|
| DX-01 to DX-05 | DEP-02-02-005 to 009 | `RETIRED` (kept, not deleted) |
| DX-06 | DEP-02-01-007 | `RETIRED`; Notes cite SCA-APP-011 |
| DX-07 | DEP-02-01-008 | Follows the owner's HGD-2 ruling (below) |
| DX-08 to DX-10 | DEP-07-05-025 | Restated in place (see below) |
| DX-11 to DX-12 | DEP-08-03-010 | TargetName and Statement say task-scope selection, not pipeline selectors |
| DX-13 | DEP-08-02-003 | TargetName and Statement describe the current SOW-006, with no "Workbench"; the location moves off `#L382` |
| DX-14 | DEP-08-02-005 | Statement describes OBJ-001 without the retired forms; the location moves off `#L238` |
| DX-15 | DEP-02-03-009 | Kept `ACTIVE`, with the tension recorded in Notes (see below) |
| DX-16 | All registers | No ACTIVE row describes a retired surface, except DEP-02-01-008 under HGD-2 option (b) |

**DEP-07-05-025 in full.** The row keeps its ID and is `ACTIVE`, with these
fields:
- TargetName names the dependency library and the Chirality dependency tool
  contracts.
- TargetLocation includes `frontend/src/lib/workspace/deliverable-contracts.ts`
  and drops `/api/working-root/deliverable/dependencies`.
- The Statement uses the library and the tool contracts, not the API.
- The evidence moves to the live text:
  - `EvidenceFile` `ScopeOfWork.md`;
  - `SourceRef` `ScopeOfWork.md §CLM-011 — Scope`;
  - `EvidenceQuote` is a verbatim span of DEL-07-05 `ScopeOfWork.md` line 188.
- Today the row still quotes the route text. That text survives only inside the
  `[RETIRED — SCA-APP-011]` bullet at line 345 (CLM-021).

## DEP-02-03-009: kept, with a reason

The row cites DEL-02-03-REQ-009, "routing to PIPELINE `TASK*` with a
deliverable preselected".
- **The tension.** Accepted E80 (DEL-02-03 `ScopeOfWork.md` line 322, CLM-029)
  withdrew the old Pipeline scope-scan and deliverable-routing examples.
- **Why it is still kept:**
  - SCA-APP-011 did not amend REQ-009, which is still stated at lines 143
    and 181.
  - `Propagation_Plan.md` §7 records "No own-register change" for DEL-02-03.
  - The row targets DEL-08-03's retained task-scope dispatch contract
    (`frontend/src/lib/pipeline/pipeline-dispatch-contract.ts`), not the retired
    form.
- **So** the extraction is expected to keep the row and record the tension in
  its Notes. Aligning the REQ-009 wording is a DEL-02-03 scope question for a
  later change. It is recorded as a residual, and no decision is asked here.

## HGD-2: the one dependency decision for the owner

**What remains open.** Only DEP-02-01-008 (DEL-02-01 → DEL-08-03, "retained
PIPELINE deep-link/query compatibility").

**What the choice turns on: who owns the target, not whether the URL still
works.**
- Both `/workbench` and `/pipeline` still resolve:
  - both page directories exist (`frontend/src/app/workbench/`,
    `frontend/src/app/pipeline/`);
  - `components/shell/chat-panel.tsx` lines 194–201 map both paths to a mode.
- So the URL surviving cannot be what separates DEP-02-01-007 from
  DEP-02-01-008.
- What does separate them is target ownership:
  - **DEL-02-02** was rescoped by SCA-APP-011 (DQ-R), so DEP-02-01-007 has no
    target duty left.
  - **DEL-08-03** keeps the task-scope dispatch semantics.
  - The surviving route/query compatibility is keyed with **DEL-08-02**,
    through DEP-08-02-013 and the DEL-02-01 CLM-003 quote "The exact surviving
    TYPES §4 route/query compatibility question remains keyed with DEL-08-02".

**Options**
- **(a) Retire DEP-02-01-008. Recommended by the independent reviewer.**
  - The handler that folds `/pipeline` query intent into the shell URL,
    `mergeMatrixTargetIntoCurrentUrl` in `frontend/src/lib/portal/agent-matrix-launch.ts`,
    is dead legacy shell code: only tests import it.
  - Route/query compatibility stays covered through DEL-08-02.
- **(b) Keep it ACTIVE as compatibility-only.**
  - Choose this only if you want the `/pipeline` deep link tracked as a
    DEL-02-01 obligation.
  - The Statement would then say that, with no selector or presentation
    ownership.

**Consequence for HGD-3.** HGD-3 held a DEL-02-01 → DEL-02-02 prerequisite out
of the register. The reason was that emitting it while DEP-02-02-005 and
DEP-02-01-007 were present would create a four-node SCC {DEL-02-01, DEL-02-02,
DEL-08-02, DEL-08-03}. Once both rows retire (DX-01 and DX-06), that premise
no longer holds. HGD-3 is not asked here. After extraction, its owner can
revisit it on the new graph.

## Graph today (no extraction run)

`analyze_dep_closure` over the unchanged registers gives:
- 54 nodes, 111 edges, 0 SCC, 0 orphans;
- `subject_status` FAIL, from the same 2 schema-invalid registers and 2
  implements-missing units as the accepted baseline.

The output is in `dep_closure/`. The expected outcomes only retire rows or
restate rows in place, so no new edge can create a cycle.
