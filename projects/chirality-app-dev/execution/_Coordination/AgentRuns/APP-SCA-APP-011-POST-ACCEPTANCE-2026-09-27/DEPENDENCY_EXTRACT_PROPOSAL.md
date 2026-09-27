# SCA-APP-011 — dependency-extract proposal (PROPOSAL, not applied)

**Status: PROPOSAL. No `Dependencies.csv` or `_DEPENDENCIES.md` is written.**

**Why this waits for the owner.** The bundled `dependency-extract` workflow
itself runs straight through. In this App loop, though, three things require
an owner act before a register write for this amendment:

1. **The incremental plan comes first.** `dependency-extract` runs here as
   `project-setup` Function 5, Phase 5.6. That phase follows the Phase 5.1
   incremental plan, which says "Do not write before the human confirms the
   plan" (`INCREMENTAL_SETUP_PROPOSAL.md`).
2. **Two rows are open owner decisions.** DEP-02-01-007 and DEP-02-01-008 are
   HGD-2 (DEL-02-01 `_DEPENDENCIES.md`: "retire or keep as
   compatibility-only").
3. **Precedent.** Previous edge retirements and row emissions in this loop were
   applied under owner rulings, with preview and review: D-APP-109 and
   D-APP-110 (`_DEPENDENCIES.md` run notes for DEL-02-01 and DEL-02-02).

**Scope under FULL_GRAPH.** Per the plan, the extraction covers the 9
affected deliverables and their 17 neighbours, one brief each, in
`MODE: UPDATE`. It is followed by `audit-dep-closure` over SCOPE ALL.

**Stale rows found.** The row scan found 11 ACTIVE rows that still describe
surfaces SCA-APP-011 retired. They are the same rows as
`audit-scope-closure` Pass 3, ASC-ISS-011 to ASC-ISS-021.

**Proposed row changes.** The exact field changes, each with its basis and the
decision it needs, are in `DEPENDENCY_EXTRACT_PROPOSAL.csv`:
- **Retire:** DEP-02-02-005 to 009 (Propagation_Plan §8 item 2).
- **HGD-2:** retire DEP-02-01-007. For DEP-02-01-008 the owner chooses between
  retiring it and keeping it as a compatibility-only row, because the
  `/pipeline` URL stays reachable and unlisted.
- **Restate** DEP-07-05-025 to the library and the retained tool contracts.
- **Refresh wording:** DEP-08-03-010, DEP-08-02-003 and DEP-08-02-005.

Retirement sets `Status=RETIRED`. Rows are never deleted.

**Proposed owner answer** (a short reply is enough):

> Confirm the SCA-APP-011 incremental plan with baseline SCA-APP-010 and
> FULL_GRAPH; apply DX-01 to DX-06 and DX-08 to DX-14; HGD-2: retire
> DEP-02-01-007 and [retire | keep compatibility-only] DEP-02-01-008.

**Current graph, with no extraction run.** `analyze_dep_closure` over the
unchanged registers gives:
- 54 nodes, 111 edges, 0 SCC, 0 orphans;
- `subject_status` FAIL, with the same 2 schema-invalid registers and 2
  implements-missing units as the accepted pre-change baseline.

The output is in `dep_closure/`. Retiring rows removes edges only, so no new
cycle can form.
