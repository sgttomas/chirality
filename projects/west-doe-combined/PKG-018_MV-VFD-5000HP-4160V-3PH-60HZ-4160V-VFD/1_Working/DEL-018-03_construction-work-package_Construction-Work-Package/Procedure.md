# Procedure: DEL-018-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-018-03_construction-work-package`, covering the `PKG-018` "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" package. The procedure covers both producing the Construction Work Package artifact set (work package, installation and tie-in workface plan, construction interface and turnover checklist) and using it to coordinate field installation, inspection, and turnover.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 20.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM source slices from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (construction scope, inlet compressor motor, 4160V MCC, BPCS/RIO, cable tray and conduit, miscellaneous facilities alignment) and `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (grounding and bonding).
- Declared upstream dependencies: none declared during PREPARATION (use of `DEL-018-01_scope-of-work` and `DEL-018-02_package-datasheet` is recommended context but not a declared edge).

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row 92.
3. Read workbook Packages row 20 and `PACKAGE_REGISTER.csv` row `PKG-018`; carry forward package ID, WBS, CoA tracking number, package name, discipline, responsibility model, and supported objectives.
4. Read `INTERFACE_REGISTER.csv` rows for `PKG-018` and populate the construction interface and turnover checklist with Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-018-03_construction-work-package` and confirm the deliverable produces the construction work package, the installation and tie-in workface plan, and the construction interface and turnover checklist.
6. Read DBM source slices for facility construction scope, 4160V MCC tie-in, BPCS/PRP communications, cable tray and conduit routing, and grounding and bonding.
7. Search accessible package-specific construction materials for PKG-018. If no source-supported package-specific match is found, mark detailed VFD construction parameters (lift plan, modular split, foundation loads, cable schedules, commissioning hold points) as `TBD`.
8. Draft the Datasheet using source-supported identification, attributes, conditions, and construction content; preserve unsupported values as `TBD` or `ASSUMPTION`.
9. Draft the Specification requirements and verification hooks aligned with the Datasheet basis, the construction interface set, and the DBM construction/electrical source slices.
10. Draft Guidance to explain conservative interpretation, source gaps, trade-offs (including the motor allocation assumption), and human-ruling items.
11. Draft this Procedure so that the production and field-use sequence is repeatable.
12. Perform cross-document consistency checks for package identity, interface list, responsibility split, motor-allocation assumption, TBD items, and SCA references.
13. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry items into the run record as `NEEDS_HUMAN_RULING`.
14. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

### Field-use sequence (use of the Construction Work Package)

A. Confirm the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist are aligned to the current plot plan, equipment list, and construction work package register before issue for construction.
B. Mobilize and execute civil/structural foundation and support work per detailed design.
C. Offload and set the VFD package per the vendor general arrangement and lift plan (TBD until issued).
D. Execute electrical tie-ins to the 4160V MCC (field-fused contactor, motor protection relay) and home-run cabling/terminations per detailed design.
E. Execute I&C and communications terminations (EtherNet/PRP) to the plant PLC central control panel.
F. Install grounding/bonding per facility basis (two-point ground-grid connection; CEC-sized separate copper ground conductors as applicable) and inspect.
G. Walk down cable tray, conduit, and physical placement for maintenance access compliance.
H. Complete the construction interface and turnover checklist with sign-offs; carry residual open items into commissioning hold-point tracking.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 20, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Interface consistency | All six applicable PKG-018 interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility construction/integration responsibilities are not conflated. |
| Source-gap handling | VFD ratings, modular split, lift plan, foundation loads, cable schedules, installation location, pre-energization checks, and commissioning hold points remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about package title vs. DBM motor ratings and missing vendor construction documentation appears in the Guidance Conflict Table and the run record. |
| Issue-for-construction readiness | The Construction Work Package is aligned to the plot plan, equipment list, and construction work package register before issue. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
- Completed construction interface and turnover checklist (field-produced)
- Installation and tie-in workface plan execution record (field-produced)
