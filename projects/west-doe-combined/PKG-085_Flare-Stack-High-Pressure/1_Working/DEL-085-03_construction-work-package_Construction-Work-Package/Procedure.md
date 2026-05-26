# Procedure — DEL-085-03 Construction Work Package (Flare Stack, High Pressure)

## Purpose

This Procedure describes the operational steps the EPC Integrator follows to
produce the Construction Work Package artifacts (work pack, workface plan,
turnover checklist) and to physically install, inspect, and turn over
`PKG-085` (Flare Stack, High Pressure)
(Source: `DELIVERABLE_REGISTER.csv` DEL-085-03).

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` reviewed for this
  deliverable.
- EPC Scope of Work (DEL-085-01) and Package Datasheet (DEL-085-02) issued.
- Vendor engineered equipment package (DEL-085-04) at a maturity allowing
  installation drawings and erection method statements (TBD — declared
  upstream dependencies not yet registered in `_DEPENDENCIES.md`).
- Final geotechnical report and structural design basis for the flare stack
  foundation issued (Source: `3-25_Comp_and_Liquids_DBM.md` line 700;
  status: `location TBD`).
- Issued-for-construction P&IDs identifying HP and LP relief header tie-in
  points at DN 500 / 20 in to V-4100-2, V-4150-2, V-3900-2
  (Source: `3-25_Comp_and_Liquids_DBM.md` lines 497, 499).
- 03-25 / 04-25 interface allocation memo for the shared dual stack
  (Source: `3-25_Comp_and_Liquids_DBM.md` lines 56, 548; status: TBD —
  see Guidance Conflict Table CWP-085-03-CF-001).
- Project NDE plan, F&G IFC layout, grounding/bonding standard (status: TBD).

## Steps

### Phase A — Construction Work Package Authoring (EPC office work)

1. Compile the Construction Work Package document set covering Scope items
   `SOW-0087`-`SOW-0090` and binding to Specification requirements
   CWP-085-03-R-001 through R-009.
2. Develop the installation and tie-in workface plan listing each interface
   from the PKG-085 interface set (utility piping; relief/flare/vent;
   drain/containment; electrical power; grounding/bonding; I&C/control
   cabling; fire & gas/safety; structural/foundations/supports)
   (Source: `PACKAGE_REGISTER.csv` PKG-085 "Applicable interface types").
3. Develop the construction interface and turnover checklist with one row per
   interface and per Specification requirement, sequenced for sign-off at
   turnover.
4. Validate the work pack against the vendor erection method statement
   (status: TBD pending vendor doc).

### Phase B — Site Preparation and Foundations

5. Survey and lay out the flare stack location per IFC civil drawings.
6. Construct foundations, anchorage, and grade-level structural supports per
   the final geotechnical/structural basis
   (Source: `3-25_Comp_and_Liquids_DBM.md` line 700). Record concrete
   strength, rebar inspection, anchor bolt grout, and survey-as-built.

### Phase C — Stack Erection

7. Receive and inspect the vendor-supplied stack sections (660 mm OD, 60,957 mm
   total HP/Cryo riser; LP riser OD TBD)
   (Source: `3-25_Comp_and_Liquids_DBM.md` line 499).
8. Execute the controlled lift per the vendor-approved erection method
   statement; record dimensional and verticality checks.

### Phase D — Tie-in and Interface Installation

9. Install HP relief headers from V-4100-2 and V-4150-2 to the HP riser tie-in
   flange at DN 500 / 20 in
   (Source: `3-25_Comp_and_Liquids_DBM.md` lines 497, 499).
10. Install LP relief header from V-3900-2 to the LP riser tie-in flange at
    DN 500 / 20 in (Source: same).
11. Install KO drum pump piping interfaces for P-4100-2, P-4150-2, P-3900-2
    where they fall within facility integration scope.
12. Install electrical power, grounding/bonding, I&C/control cabling, F&G
    detection mounts, and drain/containment interfaces per the PKG-085
    interface set.

### Phase E — Inspection, Pre-commissioning, and Turnover

13. NDE the new welds per the project NDE plan (plan: TBD).
14. Perform grounding continuity tests and F&G loop checks against the IFC
    F&G layout (Source: `3-25_Comp_and_Liquids_DBM.md` line 838; layout
    issuance: TBD).
15. Walk down the interface checklist with operations (03-25 and 04-25 as
    applicable) per the interface allocation memo.
16. Compile the turnover package and transmit to DEL-085-06 (EPC Vendor
    Package Review and Acceptance) for acceptance evidence.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| Foundation conformance | Survey and concrete records | Within tolerances of IFC structural drawings (tolerances: TBD). |
| Stack verticality and elevation | Survey | Within vendor tolerance (TBD). |
| HP/LP header dimensional and weld | NDE records per project plan (TBD) | 100% per plan; no open NCRs. |
| Grounding/bonding | Continuity test | Resistance per project standard (value: TBD). |
| F&G | Loop check and functional test | All loops pass IFC functional test (criteria: TBD). |
| Interface checklist | Joint walkdown | All rows signed by EPC Integrator and operations. |

## Records

- Construction work package (final issued version)
- Installation and tie-in workface plan (final issued version)
- Construction interface and turnover checklist (signed)
- Foundation inspection records (concrete, rebar, anchorage)
- Stack erection method statement and lift records
- NDE records
- Grounding/bonding continuity test records
- F&G loop check and functional test records
- Punch list and turnover acceptance record (input to DEL-085-06)
