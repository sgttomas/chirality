# Procedure: DEL-069-03_construction-work-package

## Purpose

Define the procedure for producing and checking the Construction Work Package for `DEL-069-03_construction-work-package`, covering construction-facing installation, tie-in, inspection, and turnover for the `PKG-069` Mole Sieve Drier Unit (Gas) package, including the explicit construction boundary with the cryogenic unit package per the Gate 6 scope-coupling disposition.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Workbook source: `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 73 (declared by `PACKAGE_REGISTER.csv` source field; not re-read in this run).
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM-Deepcut source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, including Construction Responsibility; Site/Environmental Conditions; Plot Plan Status (sec 2.4); SEC-06 Treating, Dehydration, and Cryogenic Recovery Basis — Molecular-Sieve Dehydration and Mercury Removal Basis (Process Description; Design Values; Bed and Regeneration Basis; Equipment, Controls, and Protection; Open Items and Assumptions); pressure-class statement at line 628 (900# molecular sieve system).
- Upstream Package Datasheet (`DEL-069-02`) and Scope of Work (`DEL-069-01`) drafts as technical handoff context. Note: `_DEPENDENCIES.md` does not declare these as upstream constraints; treat them as directional context only and confirm if they should be declared.
- Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state before editing the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against `DELIVERABLE_REGISTER.csv` row `DEL-069-03_construction-work-package`.
3. Read workbook Packages row 73 (via `PACKAGE_REGISTER.csv` row `PKG-069`) and record package ID, WBS, CoA tracking number, package name, discipline, and applicable interface `X` facts.
4. Read `PACKAGE_REGISTER.csv` row `PKG-069` and carry forward the responsibility model, inclusion criteria, exclusions, source references (including the Gate 6 cryogenic-coupling disposition), and objective support.
5. Read `ARTIFACT_REGISTER.csv` rows `ART-8DFE47730E`, `ART-A6B4B8383C`, and `ART-C625A825A6` and confirm the deliverable provides the construction work package, the installation and tie-in workface plan, and the construction interface and turnover checklist.
6. Read `INTERFACE_REGISTER.csv` rows for `PKG-069` and populate the construction-facing interface coverage with all twelve applicable interfaces (Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports).
7. Read DBM-Deepcut source slices for: Construction Responsibility (Tourmaline-assigned scope); Site/Environmental Conditions (geotechnical, climate basis); Plot Plan Status (sec 2.4); SEC-06 Molecular-Sieve Dehydration and Mercury Removal Basis (Process Description; Design Values including BAHX 66 degC temperature protection; Bed and Regeneration Basis including 3A adsorbent / silica gel protective layer; Equipment, Controls, and Protection including Inlet filter/coalescers, Regeneration gas compressor, Regeneration gas heater/cooler/scrubber, Recycle return, Blowdown, Dry-out header, Mercury recovery unit, Dust filters; Open Items and Assumptions); and the line-628 pressure-class statement (900# molecular sieve system).
8. Read the Package Datasheet (`DEL-069-02/Datasheet.md`) if available as technical handoff context. Do not redefine package design values; carry datasheet `TBD` items forward into construction work package gaps.
9. Search accessible package-specific requirements for `PKG-069`. The package-specific binary requirements document (`_Sources/26020-Package_Requirements.docx`) was not opened in this run; record any clause-level reference as `location TBD`.
10. Draft the Datasheet using source-supported values only; preserve unsupported values as `TBD`. Use workbook spelling ("Mole Sieve Drier Unit (Gas)") as the primary identifier and treat "molecular sieve" as the DBM-side equivalent.
11. Draft the Specification requirements and verification hooks from the Datasheet basis, the construction artifact triad, the twelve interface facts, the 900# flange basis, the BAHX 66 degC trip preservation, the operator-initiated blowdown configuration, and the mercury-service handling requirement.
12. Draft Guidance to explain conservative interpretation, source gaps, trade-offs, the cryogenic-coupling boundary, and human-ruling items.
13. Draft this Procedure to make the production and checking sequence repeatable.
14. Perform cross-document consistency checks for package identity, artifact triad coverage, twelve-interface list, responsibility split, cryogenic-coupling boundary, 900# pressure-class basis, BAHX 66 degC trip preservation, blowdown configuration, mercury-service handling, pre-issue alignment, geotechnical dependency, and `TBD` items.
15. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
16. After successful P1/P2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe and authorized.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Source grounding | Non-trivial claims cite workbook row 73 (via `PACKAGE_REGISTER.csv`), Gate 7 registers, DBM-Deepcut source slices, or are marked `TBD` / `ASSUMPTION`. |
| Artifact triad coverage | Construction work package, installation and tie-in workface plan, and construction interface and turnover checklist are all reflected in Specification, Guidance, and Procedure. |
| Interface consistency | All twelve applicable interfaces are consistent across Datasheet, Specification, Guidance, and Procedure. |
| Cryogenic-coupling boundary | The Gate 6 disposition (Gas Mole Sieve scope included with Cryogenic Unit package scope) is recorded and explicitly addressed in Specification, Guidance, and Procedure. |
| Pressure-class basis | The 900# flange basis for molecular sieve system piping is recorded in Datasheet, required in Specification, explained in Guidance, and verified in Procedure. |
| Safety-basis preservation | The BAHX 66 degC bed-bring-online trip and the operator-initiated blowdown configuration (50 psi/min, two valves, compressor bypass) are required in Specification and addressed in Guidance and Procedure. |
| Responsibility consistency | Vendor package design responsibilities and EPC facility/construction integration responsibilities are not conflated. |
| Source-gap handling | Installation plot-plan location, modularization, lift plan, ITPs, hold points, package-specific feeder/conductor/conduit detail, EHT circuit list, building HVAC/F&G/communications tie-in detail, adsorbent-loading procedure, mercury-service handling procedure, and turnover-checklist content remain `TBD` unless source-supported. |
| Geotechnical / pre-issue dependency | Foundation/support content and pre-issue alignment to plot plan, equipment list, and construction work package register are required by Specification and addressed by Guidance and Procedure. |
| Cross-deliverable consistency | The Construction Work Package accepts the Package Datasheet (`DEL-069-02`) as technical handoff basis and supports `DEL-069-05` / `DEL-069-06` consumption. |
| Human ruling items | Open ambiguity about cryogenic-coupling boundary, 900#-vs-600# pressure-class boundary, plot-plan location, pre-issue input availability, mercury-service handling, and building-services tie-in detail appears in the Guidance Conflict Table and run record. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history
- `_run_records/TASK_RUN_*.md`
