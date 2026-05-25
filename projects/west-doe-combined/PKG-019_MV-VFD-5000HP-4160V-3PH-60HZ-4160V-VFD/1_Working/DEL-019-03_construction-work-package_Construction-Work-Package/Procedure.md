# Procedure: Construction Work Package

## Purpose

Define the controlled steps to produce and use the Construction Work Package for `PKG-019` MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD. The procedure supports construction planning, field execution readiness, inspection, interface signoff, turnover, and unresolved-item tracking for the vendor-supplied 4160V VFD that starts the inlet compressor motors (KM-2150 / KM-2250).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Declared upstream dependencies: none declared during PREPARATION.
- Gate 7 rows for `DEL-019-03_construction-work-package` and `PKG-019` are available.
- DBM source slices for the 4160V MCC, the starting-VFD basis (SCA-001 VE #34), capacitor-bank removal (SCA-001 VE #37), UPS services for MV breaker/protective relay, ambient design implications, and geotechnical status are available.
- Accepted EPC Package Datasheet (`DEL-019-02_package-datasheet`), vendor engineered equipment package (`DEL-019-04_vendor-engineered-equipment-package`), IFC electrical drawings, final geotechnical report, harmonic/protection-coordination/arc-flash studies, and project electrical specifications are either accepted or explicitly carried as `TBD`.

## Steps

1. Confirm package identity.
   - Verify `PKG-019` MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD, WBS 02, CoA tracking number `26020-02-30-009`, discipline Electrical, workbook row 21.
   - Record the package basis in the CWP cover/index.

2. Confirm deliverable scope.
   - Include the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
   - Keep exclusions and unknown detailed criteria (VFD ratings, harmonic/reactive mitigation, foundation detailing) visible as `TBD`.

3. Build the interface checklist.
   - Add Electrical Power.
   - Add Grounding / Bonding.
   - Add I&C / Control Cabling.
   - Add Communications / Network.
   - Add Maintenance Access.
   - Add Structural / Foundations / Supports.
   - Add signoff fields for engineering, construction, vendor commissioning, electrical/controls, and turnover review where applicable.

4. Establish Electrical Power and grounding tie-in controls.
   - Confirm source-side feed alignment with the 4160V MCC and the 13.8 kV / 4.16 kV / 12 MVA transformer basis.
   - Confirm load-side connection to the driven motor(s) (KM-2150 / KM-2250) per accepted electrical drawings.
   - Confirm grounding/bonding installation per the project grounding specification (mark `location TBD` where unavailable).
   - Confirm no capacitor-bank reinstatement on the synchronous bus on MCC-8200 where the VFD is present (SCA-001 VE #37).

5. Establish I&C and Communications tie-in controls.
   - Confirm control wiring for MV breaker control and protective relay (UPS-served 120 VAC / 125 VDC) is routed and labeled per drawings.
   - Confirm EtherNet connectivity from the 4160V MCC / VFD to the plant PLC central control panel.
   - Mark loop and signal verification as hold points.

6. Establish readiness gates for incomplete source criteria.
   - Harmonic / reactive-power mitigation: require detailed electrical studies or accepted exception before closing harmonic, reactive, and capacitor-related criteria.
   - Protection / coordination / arc-flash: require studies accepted before energization.
   - Geotechnical: require final geotechnical report and vendor equipment loads before closing foundation, anchorage, frost, settlement, and structural-support criteria.
   - Standards/regulatory: require verification of unavailable standards, permits, and regulatory triggers before final issue for construction.
   - Cold-weather: confirm installation, heat tracing, lubricant, and commissioning provisions match the -40 deg C minimum ambient basis.

7. Prepare workface execution controls.
   - Identify work areas, access, lifting and offloading plans, sequencing, tie-in boundaries, inspection hold points, witness points, and turnover records.
   - Define Maintenance Access provisions (operating clearances, arc-flash boundaries, lifting access, replacement-component access).
   - ASSUMPTION: Include construction logistics only where they affect the MV VFD package or its declared interfaces.

8. Perform pre-issue consistency review.
   - Check the CWP against the EPC Package Datasheet (`DEL-019-02`), the vendor engineered equipment package (`DEL-019-04`), IFC electrical drawings, plot plan, equipment list, and the interface register.
   - Reconcile any package-title vs source-basis differences (see Guidance Conflict Table HRR-019-03-001) before treating ratings as closed.
   - Keep unresolved conflicts in the CWP exception register.

9. Execute field work and inspections.
   - Use approved IFC drawings/specifications, vendor installation instructions, and the CWP workface plan.
   - Record inspection results, exceptions, redlines, and interface signoffs.
   - Coordinate vendor commissioning, factory-fitted accessory verification, and witness points per the EPC/Vendor boundary.

10. Complete turnover.
    - Confirm all checklist items are signed off or carried as accepted exceptions.
    - Compile construction records, inspection records, interface records, electrical-study acceptance evidence, and unresolved/open-item dispositions.
    - Feed acceptance evidence into `DEL-019-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification check | Evidence |
|---|---|
| Package identity is correct | CWP cover/index matches `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Required artifacts are present | CWP includes work package, workface plan, and interface/turnover checklist. |
| Interfaces are covered | Checklist includes all six declared interface types for `PKG-019`. |
| Electrical Power tie-in is controlled | Source-side feed from the 4160V MCC and load-side motor connection witnessed and recorded. |
| Grounding/bonding is controlled | Continuity/impedance test records and inspection signoffs complete. |
| I&C / Communications are controlled | Loop checks, MV breaker/protective relay signal checks, and EtherNet commissioning records complete. |
| Harmonic / reactive mitigation hold is controlled | Detailed electrical studies accepted or unresolved criteria remain `TBD`/exceptioned; no capacitor-bank reinstatement on MCC-8200 synchronous bus where VFD is present. |
| Geotechnical / structural readiness is controlled | Final geotechnical report and vendor equipment loads accepted, or exceptions explicitly carried as `TBD`. |
| Maintenance Access is controlled | Walk-down record confirms clearances, arc-flash boundaries, and replacement-component access. |
| Cold-weather readiness is controlled | Installation, heat tracing, lubricant, and commissioning provisions match -40 deg C basis. |
| Standards/regulatory verification is controlled | Standards and regulatory requirements not available in the workspace remain verification-required. |
| Turnover is complete | Inspection, interface signoff, exception, and turnover records are complete. |

## Records

- Construction Work Package index and issue record.
- Installation and tie-in workface plan.
- Electrical Power interface checklist.
- Grounding / Bonding interface checklist.
- I&C / Control Cabling interface checklist.
- Communications / Network interface checklist.
- Maintenance Access interface checklist.
- Structural / Foundations / Supports interface checklist.
- Inspection and hold-point records (including witness points for vendor commissioning).
- Electrical-study acceptance evidence (harmonic, reactive, protection/coordination, arc-flash).
- Geotechnical, IFC drawing, electrical specification, and regulatory `TBD` and exception register.
- Turnover checklist and signoff record (feeding `DEL-019-06`).
- As-built/redline records where required by project controls.
