# Procedure: DEL-032-03_construction-work-package

## Purpose

Operational steps to produce the Construction Work Package deliverable for `PKG-032 Cathodic Protection Design and Installation` and to use it as the construction-execution basis for installing the CP system into the 03-25 Comp and Liquids facility.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in the deliverable folder.
- Gate 7 PROJECT_DECOMP snapshot accessible at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Authoritative source slices available: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Electrical Design Scope; Construction Scope Summary; Cable, Tray, Bonding; Package and Third-Party Interfaces; Miscellaneous Facilities; Design Implications).
- No declared upstream dependencies (DECLARED mode, none recorded in `_DEPENDENCIES.md`). Vendor engineered equipment package (`DEL-032-04`) is not declared but is the natural upstream input for detailed construction content; absence at the time of authoring is recorded as a source gap, not a blocker.

## Steps

### A. Produce the Construction Work Package artifact

1. **Establish package identity.** Confirm package responsibility model and interface set from `PACKAGE_REGISTER.csv` row `PKG-032` and `INTERFACE_REGISTER.csv` rows for `PKG-032` (`IFC-C2719906C1`, `IFC-F1FE9DF9DD`, `IFC-4D092EC70F`, `IFC-8594557BD3`).
2. **Extract CP-relevant DBM source slices.** Read Electrical Design Scope (line 718, 770), Construction Scope Summary (line 75), Cable/Tray/Bonding paragraph (line 768), and Package/Third-Party Interfaces (line 812) from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
3. **Draft construction work package narrative.** Capture: package identity; protected-asset list (`TBD` until vendor design); CP system type (`TBD`); rectifier/anode-bed configuration (`TBD`); power feed source (`TBD`); grounding/bonding coordination strategy (ASSUMPTION pending vendor); cable schedule references (`TBD`); communications protocol selection (`TBD`); construction execution party (Tourmaline facility construction scope per DBM line 75); tie-in coordination plan; commissioning plan reference; turnover plan reference.
4. **Draft installation and tie-in workface plan (`ART-7FA44ED0D3`).** Cover workface planning evidence for installing CP equipment and connecting it to adjacent electrical, controls, civil, and structural systems. Identify sequencing dependencies for test stations, isolation joints, and anode connections relative to buried-asset installation.
5. **Draft construction interface and turnover checklist (`ART-9C1116778C`).** Define inspection points, hold points, and turnover acceptance items for CP system handover to operations.
6. **Mark unresolved items.** Any value not supported by accessible source or vendor input is recorded as `TBD`; any best-effort inference is labeled `ASSUMPTION`.

### B. Use the Construction Work Package for execution

7. **Pre-IFC alignment check.** Confirm the construction work package, plot plan, equipment list, and construction work package register are aligned prior to issue for construction (per DBM line 661).
8. **Material readiness.** Confirm vendor CP equipment delivery, anode/coke breeze delivery (if applicable), isolation flange kits/dielectric joints, test-station enclosures, and cable bills of material are available.
9. **Civil readiness.** Confirm rectifier shelter foundation, anode bed civil work, and trench routes are complete or scheduled against geotechnical caveats.
10. **Electrical installation.** Install power feed to rectifier(s), maintain power/control segregation per project electrical specifications (DBM line 768), and terminate per vendor wiring.
11. **Grounding coordination.** Install isolation devices per vendor design between CP-protected assets and the facility ground grid; document continuity/isolation test results.
12. **I&C and communications installation.** Install monitoring cables and communications drops per vendor wiring and the facility communications basis (DBM line 812).
13. **Pre-commissioning.** Perform native potential survey, energize rectifier(s), record polarized potentials, perform interference survey with adjacent buried metallic systems; acceptance criteria `TBD` pending vendor commissioning procedure.
14. **Turnover.** Complete the construction interface and turnover checklist with operations; transfer records.

## Verification

- Construction work package artifact (`ART-655045CC72`) exists, is signed/issued, and references the vendor CP design (when accepted).
- Workface plan artifact (`ART-7FA44ED0D3`) exists and covers all four declared interface types.
- Turnover checklist (`ART-9C1116778C`) exists, includes CP-specific hold points, and is signed off at handover.
- All `TBD` items in `Datasheet.md` and `Specification.md` are resolved or carried forward to the vendor engineered equipment package (`DEL-032-04`) as input gaps.
- Native potential survey, energized polarized potentials, and interference test results recorded against acceptance criteria.

## Records

- Construction work package document (`ART-655045CC72`).
- Installation and tie-in workface plan (`ART-7FA44ED0D3`).
- Construction interface and turnover checklist (`ART-9C1116778C`).
- Inspection and test records (electrical termination, grounding continuity/isolation, loop check).
- CP commissioning records (native potentials, polarized potentials, interference survey).
- Turnover package signed by Construction, EPC Integrator, and Operations.
