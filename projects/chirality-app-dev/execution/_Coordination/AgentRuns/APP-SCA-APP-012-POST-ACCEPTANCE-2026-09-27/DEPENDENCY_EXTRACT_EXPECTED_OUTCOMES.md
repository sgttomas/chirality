# SCA-APP-012 — dependency-extract: expected outcomes

> **2026-09-27 — run.** The owner confirmed the plan and DX-07 ("DEP-02-03-008: retire"; `CHAT_TRANSCRIPTION.md`). The extraction ran (`DEPENDENCY_EXTRACT_RESULTS.md`), and the post-setup scope-closure audit verified DX-01 to DX-07. The text below is the reviewed expectation and is kept unchanged.

**Status: not run.** No `Dependencies.csv` or `_DEPENDENCIES.md` is written.

## What this file is

This file lists **what the extraction is expected to produce**. It is not a set
of values for the owner to approve, as for SCA-APP-011.
- The bundled `dependency-extract` workflow "Runs straight-through; never
  blocks on human decisions" (`workflows/dependency-extract/WORKFLOW.md` line 28).
- In `MODE: UPDATE` it derives rows from the source text: it matches existing
  IDs, sets `LastSeen`, and marks unseen extracted rows `RETIRED`.
- The post-setup `audit-scope-closure` checks each outcome below against the
  registers.

`Propagation_Plan.md` §8 item 2 asks the extraction run to record its expected
outcomes in this kind of file. It is written before the setup gate because
it needs no owner act and it lets the owner confirm the plan knowing what the
extraction will change.

## Why it has not run

This loop runs `dependency-extract` as `project-setup` Function 5, Phase 5.6.
That phase comes after the Phase 5.1 plan, which needs the owner's
confirmation (`INCREMENTAL_SETUP_PROPOSAL.md`). No row below needs an owner
ruling.

**Scope.** Under FULL_GRAPH the run covers:
- the 8 modified deliverables;
- their 16 neighbours with ACTIVE edges (see the setup proposal);
- one brief per deliverable in `MODE: UPDATE`;
- then `audit-dep-closure` over SCOPE ALL.

## Expected outcomes

The exact checks are in `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.csv`, one row
each. DX-01 to DX-05 are the accepted `Propagation_Plan.md` §8 table. DX-06 and
DX-07 are found by this run's pre-extraction screen (below).

| ID | Row | Expected outcome | Settled by |
|---|---|---|---|
| DX-01 | DEP-02-03-009 (DEL-02-03 → DEL-08-03) | `RETIRED`, `SatisfactionStatus=NOT_APPLICABLE`; ID kept; Notes cite SCA-APP-012 (R-b) | Group 1 (R-b) and group 2 |
| DX-02 | DEP-02-03-004 (→ REF-003) | `ACTIVE`; `EvidenceQuote` from the restated CLM-003 (line 63), without `/api/working-root/scope`; prior quote in Notes | Group 2 |
| DX-03 | DEP-08-03-007 (→ REF-003) | `ACTIVE`; `TargetName` names the `/api/project/deliverables` scan surface; `SOURCE_ENDPOINT_LABEL_CONFLICT` no longer reported | Group 2 |
| DX-04 | DEP-08-02-013 | Does not apply (P-keep): unchanged | Group 1 (P-keep) |
| DX-05 | All registers | No `ACTIVE` row names a retired surface | Group 2 |
| DX-06 | DEP-02-03-007 (DEL-02-03 → DEL-07-04) | `ACTIVE`; re-evidenced to the restated DEL-02-03-REQ-010 (line 153) | The extraction, disclosed here |
| DX-07 | DEP-02-03-008 (DEL-02-03 → DEL-07-05) | `RETIRED`; Notes cite SCA-APP-012 | The extraction, disclosed here |

## Found before extraction: two rows the plan did not list

A read-only quote screen over the 315 ACTIVE rows of the 24 in-scope
registers found every quote in its cited source except four, all in DEL-02-03:

- **DEP-02-03-009** is DX-01 and **DEP-02-03-004** is DX-02, as planned
  (DEP-02-03-009's quoted row now carries the `[RETIRED — SCA-APP-012]` marker).
- **DEP-02-03-007 and DEP-02-03-008** lost their quotes to accepted SCA-APP-012
  text: register row 3 (DEL-02-03-REQ-010 restated) and the CLM-005 widget row
  (line 90). `Propagation_Plan.md` §7 lists only DX-01 and DX-02 for DEL-02-03,
  so these two are outcomes beyond the accepted plan.
  - **DEP-02-03-007 → re-evidenced (DX-06).** The restated REQ-010 still has
    deliverable summaries "present lifecycle status read-only from
    `/api/project/deliverables`". DEL-07-04 owns the lifecycle status
    semantics and the canonical `_STATUS.md` parser (OUT-001;
    `frontend/src/lib/lifecycle/`, DEL-07-04 `ScopeOfWork.md` line 22), so the
    read-only status relationship still holds and only the evidence moves. The
    transition-control clause is not the basis: the accepted `execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/Impact_Assessment.md`
    lines 463-464 says it leaves DEL-02-03, so the row's Statement drops its
    transition-control wording.
  - **DEP-02-03-008 → retired (DX-07).** CLM-005 now says SCA-APP-012 "moved
    dependency snapshots out of this UI". REQ-010 names the dependency library
    only as the place where snapshots are read instead of a browser API. No
    current DEL-02-03 text says its widgets consume DEL-07-05 output, so under
    `STRICTNESS=CONSERVATIVE` the row is unseen and retires. The accepted
    `execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement/Impact_Assessment.md` lines 457-464 (Row 3,
    `ScopeChanging` YES) records that "the dependency-snapshot presentation
    and the transition-control clause leave DEL-02-03".

These follow from the accepted text and need no owner ruling. They are listed
so that the plan confirmation covers them knowingly. If the owner would rather
keep DEP-02-03-008 as a read-only dependency-snapshot consumer, that is a
DEL-02-03 scope question for a later change, not an extraction choice.

The same screen flagged no row of the other 23 registers, and no ACTIVE row
anywhere names a retired SCA-APP-012 surface apart from DX-02 and DX-03.

## Graph today and expected

`analyze_dep_closure` over the unchanged registers (`dep_closure/`):
- 54 nodes, 104 edges, 0 SCC, 0 orphans, 7 isolates;
- `subject_status` FAIL, from the same 2 schema-invalid registers (the CONTROL
  units DEL-00-01 and DEL-00-02 have none) and 2 implements-missing units as
  the accepted census `_Evaluation/DepClosure/CLOSURE_HGD_FC_RULING_2026-09-27_1923/Evidence/ALL/`.
  The graph counts equal that census.

Expected after extraction: 102 edges (DX-01 and DX-07 each remove one distinct
edge; DX-02, DX-03 and DX-06 change no edge), 0 SCC, no new isolate
(DEL-08-03, DEL-07-05 and DEL-02-03 keep other edges). Rows are only retired
or restated in place, so no cycle can form.
