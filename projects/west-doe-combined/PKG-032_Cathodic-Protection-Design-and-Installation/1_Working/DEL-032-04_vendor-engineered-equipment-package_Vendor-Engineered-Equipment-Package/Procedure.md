# Procedure: DEL-032-04_vendor-engineered-equipment-package

## Purpose

Procedure to produce the Vendor Engineered Equipment Package for `PKG-032` (Cathodic Protection Design and Installation), and to support EPC Integrator integration review.

## Prerequisites

- Accepted EPC Scope of Work (`DEL-032-01`) available as vendor engineering input.
- Accepted EPC Package Datasheet (`DEL-032-02`) available as vendor engineering input.
- Gate 7 PROJECT_DECOMP snapshot accessible: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24`.
- DBM source slices for cathodic protection accessible: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cathodic Protection section; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical design scope paragraph.
- Interface rows for PKG-032 accessible: `INTERFACE_REGISTER.csv` `IFC-C2719906C1`, `IFC-F1FE9DF9DD`, `IFC-4D092EC70F`, `IFC-8594557BD3`.
- Declared upstream dependencies: none declared during PREPARATION (`_DEPENDENCIES.md`).

## Steps

1. Confirm vendor engineering inputs (`DEL-032-01`, `DEL-032-02`) are at INITIALIZED or later, and capture their accepted versions.
2. Develop the vendor package design basis grounded in the EPC inputs and the accessible DBM cathodic-protection source slices. Do not pull facility-design scope into the vendor package contrary to the 4-25 DBM exclusion.
3. Select cathodic protection method (impressed-current vs. sacrificial anode) based on protected-asset list and site conditions provided through `DEL-032-02`. Record the selection and rationale; cite source(s) or mark `ASSUMPTION`.
4. Engineer each declared interface explicitly:
   - Electrical Power (`IFC-C2719906C1`): supply, feeder, and disconnection for rectifier(s) where applicable.
   - Grounding / Bonding (`IFC-F1FE9DF9DD`): coordinate with facility grounding scheme; document interaction with cathodic protection currents.
   - I&C / Control Cabling (`IFC-4D092EC70F`): control, monitoring, and alarm signal interfaces.
   - Communications / Network (`IFC-8594557BD3`): remote monitoring path where applicable.
5. Produce the vendor package datasheet set with values traceable to source. Values not supported by source remain `TBD` for vendor closure.
6. Fabricate/supply the physical equipment package consistent with the design basis and datasheet set.
7. Package deliverables for EPC Integrator integration review (interfaces to sibling deliverables for turnover and acceptance, where present in PKG-032).

## Verification

| Verification | Method | Pass criterion |
|---|---|---|
| Inputs traceability | Compare vendor design basis to `DEL-032-01` and `DEL-032-02`. | All vendor scope traces back to accepted EPC inputs. |
| Interface completeness | Compare vendor design to `INTERFACE_REGISTER.csv` PKG-032 rows. | All four interfaces are explicitly addressed. |
| Facility-design boundary | Compare to 4-25 DBM Cathodic Protection section. | Vendor package does not pull cathodic protection engineering/supply into facility electrical design scope. |
| Source fidelity | Spot-check non-trivial values for cited source slices. | Unsupported values marked `TBD` or labeled `ASSUMPTION`. |
| Responsibility split | Compare to `PACKAGE_REGISTER.csv` row `PKG-032`. | Vendor and EPC scopes not conflated. |
| Cross-document consistency | Spot-check Datasheet/Specification/Guidance/Procedure for consistent IDs, names, values. | No unresolved internal inconsistency. |

## Records

- Vendor package design basis document.
- Vendor package datasheet set.
- Vendor cathodic protection method selection record (with rationale).
- Interface design records for the four declared interfaces.
- Source-gap / `TBD` list for vendor data closure.
- EPC Integrator integration review record (handled via sibling acceptance deliverable when present).
