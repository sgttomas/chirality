# Procedure: DEL-030-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-030-03_construction-work-package`, covering the `PKG-030` Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V package. Procedure steps cover both producing the construction-work-package artifacts (work package narrative, workface plan, turnover checklist) and the field-execution sequence those artifacts will guide under the DBM Construction Responsibility basis.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 32.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM Construction Responsibility and electrical source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`.
- Declared upstream dependencies: none declared during PREPARATION.
- For field execution (downstream of this deliverable's authoring): accepted Package Datasheet (`DEL-030-02`), accepted vendor engineered package (`DEL-030-04`), and accepted vendor document turnover package (`DEL-030-05`) — these are not prerequisites for drafting this construction work package, but are prerequisites for executing the construction steps it plans.

## Steps

### Authoring the construction work package

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify it against `DELIVERABLE_REGISTER.csv` row `DEL-030-03_construction-work-package`.
3. Read workbook Packages row 32 and record package ID, WBS, CoA tracking number, package name, discipline, and the seven interface `X` facts for PKG-030.
4. Read `PACKAGE_REGISTER.csv` row `PKG-030` and carry forward the responsibility model, source references, and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows for `DEL-030-03_construction-work-package` (`ART-8A966A4CD7`, `ART-370E7F8537`, `ART-E6DA4BF5C2`) and confirm the construction-work-package narrative, the installation and tie-in workface plan, and the construction interface and turnover checklist are scoped.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-030` and confirm the seven interfaces (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are addressed as construction-execution scope.
7. Read DBM source slices for Construction Responsibility, foundation basis, the Transformers paragraph, electrical power distribution (utility 25 kV/13.8 kV transformer and 13.8 kV switchgear basis), low-voltage 600 V services, cable schedule (13.8 kV row and 600 V transformer-secondary row), grounding and bonding, neutral grounding resistor paragraph, cable tray and conduit, and maintenance access.
8. Search accessible package-specific requirements for PKG-030 in `_Sources/26020-Package_Requirements.docx`. If no source-supported package-specific match is found, mark vendor-driven content as `TBD`.
9. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`.
10. Draft the Specification requirements and verification hooks from the Datasheet basis and DBM source slices, including the seven interface obligations, the foundation/Transformers basis, the grounding basis, and the 600 V secondary resistor-grounding obligation.
11. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, and human-ruling items.
12. Draft this Procedure to make the production and checking sequence repeatable, and to outline the field-execution sequence that the construction artifacts will guide.
13. Perform cross-document consistency checks for package identity, interface list, responsibility split, construction-execution basis, and `TBD` items.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

### Field-execution sequence planned by the construction artifacts

16. Confirm prerequisites for field execution: accepted `DEL-030-02` datasheet, accepted `DEL-030-04` vendor engineered package (including transformer nameplate data, dimensions, weights, rigging information, and oil-filling/processing procedure), and accepted `DEL-030-05` vendor document turnover package. If any prerequisite is incomplete, hold field execution.
17. Confirm installation location assignment (electrical building, outdoor pad, or other) is `TBD`-resolved before foundation execution.
18. Execute grading, piling, and foundation work for the transformer base in accordance with the DBM foundation basis (precast concrete bearing foundation and/or structural steel transformer base; CEC spacing for oil-filled transformers; secondary-containment review).
19. Receive and off-load the transformer at site; verify shipment per the vendor packing list and damage-inspect on arrival.
20. Set the transformer on its foundation using the vendor-supplied rigging/lift plan (lift plan: `TBD` pending vendor data).
21. Install structural supports and any shipped-loose components per vendor instructions and Tourmaline field construction scope.
22. Install grounding: two-point ground-grid connection, separate CEC-sized copper ground conductor for the distribution transformer, ground well at the transformer/electrical building with bolted/compression connections, above-grade green-insulated conductors in PVC conduit where mechanical protection is required, and the 5 A continuous high-resistance grounding resistor on the 600 V secondary per the DBM neutral grounding basis. Configure 600 V ground-fault detection as alarm-only.
23. Install medium-voltage primary feeder cable (13.8 kV three-conductor copper TECK rated 15 kV with 133 percent insulation, shielded) from the 13.8 kV switchgear bus to the transformer primary in accordance with the DBM cable schedule basis and project routing.
24. Install 600 V secondary cabling from the transformer secondary to the plant 600 V MCC using ACWU cable per the DBM cable schedule (single-conductor cables avoided); specific sizing and routing: `TBD` pending detailed design.
25. Install I&C / control cabling and any communications/network cabling required for transformer monitoring and protective-relay integration (specific cable schedules and termination details: `TBD` pending vendor data).
26. Install area lighting around the transformer location in accordance with Tourmaline field construction scope and area-classification requirements.
27. Verify maintenance-access clearances against vendor footprint and access drawings; remediate any tray/conduit routing that obstructs oil sampling, tap-changer, bushings, or cooling-system access.
28. Coordinate tie-ins to adjacent process, utility, electrical, controls, civil, structural, and safety systems under the DBM joint-tie-in basis; record the tie-in plan and timing in the construction interface and turnover checklist.
29. Perform pre-commissioning checks (insulation testing, oil testing, protective-relay testing, ground continuity testing, energization sequence): specific values and sequence `TBD` pending vendor data; carry as `TBD` until established.
30. Complete the construction interface and turnover checklist (`ART-E6DA4BF5C2`) and hand the package over to `DEL-030-06` (EPC Vendor Package Review and Acceptance) with all turnover evidence.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 32, Gate 7 registers, DBM source slices, or are marked `TBD` / `ASSUMPTION`. |
| Artifact completeness | Construction work package narrative, installation and tie-in workface plan, and construction interface and turnover checklist are scoped. |
| Interface completeness | All seven applicable interfaces (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are addressed consistently across all four documents. |
| Responsibility consistency | Vendor package design responsibilities (`DEL-030-04`, `DEL-030-05`), EPC integration responsibilities, and Tourmaline field construction responsibilities are not conflated. |
| Foundation/grounding basis | Foundation and grounding execution language matches the DBM foundation, Transformers, grounding/bonding, and neutral grounding resistor source slices; 600 V secondary 5 A high-resistance grounding resistor is reflected; package-specific sizes/values remain `TBD`. |
| Cable schedule reference | 13.8 kV primary cable reference matches DBM cable schedule (three-conductor copper TECK, 15 kV rated, 133 percent insulation, shielded); 600 V secondary cable reference matches DBM cable schedule (ACWU; single-conductor cables avoided). |
| Source-gap handling | Vendor nameplate, rigging/lift plan, oil-filling procedure, energization sequence, protective-relay settings, and installation location remain `TBD` unless source-supported. |
| Human ruling items | Open ambiguity about nameplate values, installation location, and PKG-029/PKG-030 twin coordination appears in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
- (Field-execution records produced downstream, not by this drafting run): construction work package narrative, installation and tie-in workface plan, construction interface and turnover checklist, inspection/test records, and turnover evidence to `DEL-030-06`.
