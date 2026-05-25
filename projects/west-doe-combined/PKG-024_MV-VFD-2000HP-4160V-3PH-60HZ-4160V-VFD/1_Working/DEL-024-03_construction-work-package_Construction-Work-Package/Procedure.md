# Procedure: DEL-024-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-024-03_construction-work-package`, covering the `PKG-024` MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD package. The procedure covers both the production of the EPC construction work package documents and the operational sequence for executing and verifying installation, tie-in, inspection, and turnover scope.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 26.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM Construction Responsibility section and electrical/MCC/VFD/grounding source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

### Document production

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv`.
3. Read workbook Packages row 26 and record package ID, WBS, CoA tracking number, package name, discipline, and interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-024` and carry forward the responsibility model, inclusion criteria, applicable interface types, and objective support set.
5. Read `INTERFACE_REGISTER.csv` rows for `PKG-024` and record all six interface IDs: `IFC-68C5E24846` (Electrical Power), `IFC-F8A6E25E1C` (Grounding / Bonding), `IFC-8062D6F881` (I&C / Control Cabling), `IFC-22E88310C9` (Communications / Network), `IFC-DD889EF8E3` (Maintenance Access), `IFC-850A8082BB` (Structural / Foundations / Supports).
6. Read DBM Construction Responsibility section to extract the Tourmaline field-scope list and the ISBL/OSBL tie-in external-interface marker.
7. Read DBM electrical/MCC/VFD/electrical-buildings/grounding/cable-tray paragraphs for technical context (4.16 kV motor starting `TBD`; MV VFD housing context; grounding two-point and CEC sizing; cable tray/conduit not to interfere with maintenance access; VFD-fed motor Zone 2 marking).
8. Search accessible package-specific requirements for PKG-024 in `26020-Package_Requirements.docx`. If no source-supported match is found, mark detailed turnover checklist content as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and source slices.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
12. Draft this Procedure to make the production and field-execution sequence repeatable.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, construction scope, and `TBD` set.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

### Field execution (workface plan outline)

16. Receive vendor package documentation and confirm the construction-relevant subset (general arrangement, weights, lift points, foundation loads, terminal locations).
17. Confirm foundation design and complete grading/piling/foundation work (Tourmaline field scope).
18. Off-load the VFD module/skid and stage to the assigned installation location (location `TBD` pending plot plan).
19. Set the VFD module/skid on its foundation; install miscellaneous structural supports as required.
20. Perform mechanical hookup of any package-internal interconnecting piping (e.g., cooling, if applicable per vendor design).
21. Install shipped-loose instruments, valves, and components per vendor instructions.
22. Pull, terminate, and meg-test MV power cables to/from the VFD per project electrical specifications and CEC.
23. Pull and terminate I&C / control cabling to/from the plant PLC and any local control station.
24. Pull and terminate communications / network cabling for data acquisition.
25. Complete grounding/bonding tie-in to the facility ground grid per the DBM two-point grounding basis and CEC sizing.
26. Walk down cable tray and conduit routing to confirm no interference with maintenance access.
27. If the driven motor is in a Zone 2 area, verify motor marking and temperature code against the area-classification drawing or fugitive-emissions study.
28. Complete the construction interface and turnover checklist (structural skeleton; detailed line items `TBD` per vendor input).
29. Coordinate tie-in execution with the tie-in plan, confirming per-tie-in responsibility for each ISBL/OSBL tie-in.
30. Hand over to commissioning with completed construction records.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 26, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design, EPC facility integration, and Tourmaline field construction responsibilities are not conflated. |
| Construction-scope fidelity | Field-scope items map to the DBM Construction Responsibility list. |
| Tie-in handling | Each tie-in carries a responsibility assignment or `TBD` marker. |
| Source-gap handling | Installation location, driven-motor identity, tie-in coordinates, foundation details, cable schedules, and turnover checklist content remain `TBD` unless source-supported. |
| Human ruling items | Driven-motor identity, missing package-specific requirements source slice, and installation location appear in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
- (Field execution) construction workface plan, tie-in plan, construction interface and turnover checklist, grounding/bonding inspection records, cable termination/meg-test records, and pre-energization sign-offs.
