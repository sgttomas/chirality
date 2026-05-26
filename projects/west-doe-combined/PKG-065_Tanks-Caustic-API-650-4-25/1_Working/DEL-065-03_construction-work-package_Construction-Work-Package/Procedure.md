# Procedure: DEL-065-03 — Construction Work Package (PKG-065)

This procedure describes how the EPC Integrator shall **produce** the Construction Work Package artifact for PKG-065 Tanks, Caustic (API 650) 4-25, and how the field team shall **use** it to execute installation and turnover.

## Prerequisites

- Accepted upstream snapshot: PROJECT_DECOMP GATE-07_Final_Published_2026-05-24 (per `_REFERENCES.md`).
- Locally accessible source materials read: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (analog only).
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` during PREPARATION. (Practically, this CWP depends on DEL-065-01 Scope of Work and DEL-065-02 Package Datasheet — ASSUMPTION from EPC anchor structure; declare formally before issue.)
- API-650 (Modified) full standard text — required for clause-level construction and inspection citations; not in local source set, location TBD.
- PKG-065 tank register (TBD) confirming tank inventory and capacities.

## Steps

### A. Produce the CWP artifact

1. Confirm tank inventory and capacities from the PKG-065 Tank Register (resolve CFL-01). Update Datasheet "Attributes" rows accordingly.
2. Resolve internal-coating selection for caustic service (resolve CFL-02). Update Datasheet "Construction" and Specification R-10.
3. Compile API-650 Modified clause references for testing, NDE, and erection tolerances. Replace "location TBD" markers in Specification R-11.
4. Develop the tank-by-tank installation sequence (foundation, shell erection, roof, internals, coating, insulation/heat trace, instrumentation, vent system, drains, truck-out connection).
5. Develop tie-in workface plan referencing P&IDs (P&ID identifiers TBD) and the package boundary defined in DEL-065-01 / DEL-065-02.
6. Develop turnover checklist organized by tank, including mechanical completion, hydrotest, NDE, coating QA, heat-trace commissioning, PVRV install/cert, drain proof-of-flow, and truck-out connection test.
7. Issue the CWP for review through ORCHESTRATOR Gate-5 EPC anchor flow.

### B. Use the CWP in the field

1. Verify site readiness (foundations complete, lay-down area defined, spacing per R-09 confirmed against plot plan).
2. Receive tank materials; perform receiving inspection (verify aluminum-exclusion R-05; verify coating system per R-10).
3. Erect tanks per API-650 Modified (R-01); record courses, weld map, and NDE per fabricator inspection plan.
4. Apply internal coating; record DFT, holiday-test results, and ambient/dewpoint conditions during application.
5. Install external insulation and heat-trace circuits (R-04); test continuity and control wiring.
6. Install PVRVs, vent piping, and drain piping (R-03, R-06); confirm 300# rating at spent-caustic tank flange.
7. Perform hydrotest at 16 oz test pressure (R-01, R-02, R-11); record results.
8. Coordinate tie-in to DEL-065-04 vendor caustic treating package; sign interface checklist (R-12).
9. Walk down against P&ID and plot plan; clear punch list.
10. Issue mechanical completion certificate per tank and submit to DEL-065-06 (EPC Vendor Package Review and Acceptance, ASSUMPTION analog).

## Verification

| Step | Verification |
|---|---|
| A.1-A.6 | EPC Integrator internal review against this Specification and Conflict Table closure |
| A.7 | Gate-5 review record |
| B.3 | Fabricator NDE record package; witness points cleared |
| B.4 | Coating QA record; vendor sign-off |
| B.5 | Heat-trace commissioning record |
| B.7 | Hydrotest record signed by QC |
| B.8 | Interface checklist signed by both DEL-065-03 and DEL-065-04 owners |
| B.10 | Mechanical completion certificate filed in turnover package |

## Records

- Construction work package document (this artifact set, issued)
- Installation and tie-in workface plan
- Construction interface and turnover checklist
- Hydrotest and NDE record set
- Coating QA record set
- Heat-trace commissioning record
- PVRV certification and install record
- Mechanical completion certificate per tank
- Punch list and clearance record
- Red-line as-built markups
- Closed Conflict Table entries (CFL-01, CFL-02, CFL-03) with human rulings
