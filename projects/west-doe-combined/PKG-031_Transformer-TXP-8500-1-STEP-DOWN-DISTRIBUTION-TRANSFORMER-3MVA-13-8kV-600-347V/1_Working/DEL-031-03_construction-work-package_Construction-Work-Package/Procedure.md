# Procedure: DEL-031-03_construction-work-package — Construction Work Package

## Purpose

Produce the EPC Integrator Construction Work Package (CWP) for `PKG-031` (Transformer TXP-8500-1 — 3 MVA 13.8 kV / 600 V step-down distribution transformer), including the installation and tie-in workface plan and the construction interface and turnover checklist, ready for issue for construction.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot (this deliverable's authoritative basis).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for `DEL-031-03` initialized.
- Companion `DEL-031-01` (Scope of Work) and `DEL-031-02` (Package Datasheet) for `PKG-031` — declared upstream dependencies (none declared in `_DEPENDENCIES.md`; ASSUMPTION based on EPC anchor-deliverable convention; HRR-031-03-001).
- Vendor engineered equipment package outline from `DEL-031-04` (for installation handles, lifting points, dimensions); status TBD.
- Accepted final geotechnical report (foundation/pile/frost) — currently TBD per `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 141.
- Plot plan, equipment list, and construction work package register, all current to the same revision as the CWP.
- Project electrical specifications and CEC for grounding conductor sizing.

## Steps

1. **Confirm package identity.** Verify tagged equipment TXP-8500-1, 3 MVA, 13.8 kV / 600/347 V from workbook row 33 and DBM line 745. Record in CWP cover page.
2. **Lock interface scope.** Populate the CWP interface section from `INTERFACE_REGISTER.csv` for `PKG-031` (seven interfaces: Electrical Power, Grounding/Bonding, Area/Exterior Lighting, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports).
3. **Capture vendor handover inputs.** Pull dimensions, weights, lifting/rigging points, primary/secondary termination boxes, cooling/oil arrangement, and shipped-loose lists from the vendor package (`DEL-031-04`). Mark unavailable items TBD.
4. **Assign field-construction scope.** Allocate off-loading, setting, mechanical hookup, shipped-loose installation, structural supports, home-run cabling, electrical terminations, area lighting, and demolition where required to Tourmaline field construction per DBM lines 101-125.
5. **Define tie-in workface plan.** Sequence: foundation acceptance → setting on pad → grounding (two-point ground-grid connection per CEC) → 13.8 kV primary cable pull + termination → 600 V secondary cable pull + termination to MCC → control/instrument cabling separated per DBM line 768 → area-lighting tie-in → comms/network tie-in.
6. **Cross-discipline coordination.** Coordinate package buildings, MCC interface, RIO interface, heat tracing, HVAC, fire/gas detection, and drain/vent tie-ins per `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 619. Capture sign-offs.
7. **Tie-in timing.** Schedule tie-ins to existing/related facilities jointly per DBM line 127; record cut-over windows and energization sequence (primary energization gating MCC commissioning is ASSUMPTION; TBD until project schedule confirms).
8. **Build construction interface and turnover checklist.** One row per interface type with status (planned / installed / inspected / accepted) and signature columns.
9. **Pre-IFC alignment audit.** Confirm CWP, plot plan, equipment list, and CWP register are at consistent revisions per `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 661.
10. **Issue for construction.** Issue the CWP, workface plan, and turnover checklist. Hand to construction execution.
11. **Execute installation.** Construction contractor performs Step 5 sequence; QC inspects per Verification.
12. **Construction turnover.** Walk-down per checklist; resolve punch list; EPC Integrator signs construction turnover; package handed to `DEL-031-06` for vendor-package review/acceptance and final integration.

## Verification

- CWP cover page matches workbook row 33 identity (REQ-031-03-01).
- Responsibility matrix matches DBM Construction Responsibility table (REQ-031-03-02).
- Grounding continuity test confirms two ground-grid connections with CEC-sized conductors (REQ-031-03-03).
- Field walkdown confirms power/control circuit separation per DBM line 768 (REQ-031-03-04).
- Maintenance-access clearances confirmed at transformer and MCC face (REQ-031-03-05).
- Tie-in coordination minutes and schedule entries present (REQ-031-03-06).
- Geotechnical and foundation inspection records present (REQ-031-03-07).
- Pre-IFC alignment audit signed (REQ-031-03-08).
- Discipline-interface checklist signed by civil, electrical, controls, instrumentation leads (REQ-031-03-09).
- Workface plan and turnover checklist artifacts exist and are signed (REQ-031-03-10).
- Interface matrix is complete against `INTERFACE_REGISTER.csv` row set for `PKG-031` (REQ-031-03-11).
- Installation location assignment is confirmed in detailed design (REQ-031-03-12; removes ASSUMPTION).

## Records

- Issued CWP (`ART-7627442199`).
- Issued installation and tie-in workface plan (`ART-F476EFD32E`).
- Issued construction interface and turnover checklist (`ART-273816BADA`).
- Off-loading and setting records.
- Mechanical hookup punch list.
- Electrical termination records (13.8 kV primary; 600 V secondary).
- Grounding continuity test results.
- Foundation/structural support inspection records.
- Tie-in close-out records per interface type.
- Pre-IFC alignment audit record.
- Construction turnover package signed by EPC Integrator.
