# Procedure: Construction Work Package

## Purpose

Define the controlled steps to produce and use the Construction Work Package for `PKG-020` 13.8kV SWITCHGEAR EQUIPMENT. The procedure supports construction planning, field execution readiness, inspection, interface signoff, turnover, and unresolved-item tracking for the vendor-supplied 13.8 kV switchgear that functions as the plant main power distribution center for the 04-25 West Doe Deepcut expansion.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Declared upstream dependencies: none declared during PREPARATION.
- Gate 7 rows for `DEL-020-03_construction-work-package` and `PKG-020` are available.
- DBM source slices for the Power System (utility-side and radial load-side distribution), Grounding and Bonding, Electrical Buildings, Cable Specifications (13.8 kV TECK basis), UPS services for MV breaker/protective relay, removal of the centralized 13.8 kV emergency generator, and Construction Responsibility are available.
- Accepted EPC Scope of Work (`DEL-020-01_scope-of-work`), EPC Package Datasheet (`DEL-020-02_package-datasheet`), vendor engineered equipment package (`DEL-020-04_vendor-engineered-equipment-package`), IFC electrical drawings, final geotechnical report, protection-coordination/arc-flash studies, utility coordination agreement, and project electrical/grounding/controls specifications are either accepted or explicitly carried as `TBD`.

## Steps

1. Confirm package identity.
   - Verify `PKG-020` 13.8kV SWITCHGEAR EQUIPMENT, WBS 01, CoA tracking number `26020-01-30-011`, discipline Electrical, workbook row 22.
   - Record the package basis in the CWP cover/index.

2. Confirm deliverable scope.
   - Include the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
   - Keep exclusions (Package Vendor design scope; no centralized 13.8 kV emergency-generator tie-in) and unknown detailed criteria (switchgear ratings, lineup count, foundation detailing, utility scope split) visible as `TBD`.

3. Build the interface checklist.
   - Add Electrical Power (utility-side feed and load-side radial distribution).
   - Add Grounding / Bonding (utility-transformer 200 A neutral grounding resistor and plant ground grid two-point connections).
   - Add I&C / Control Cabling (UPS-served 120 VAC / 125 VDC MV breaker control and protective relay).
   - Add Communications / Network (switchgear-to-plant-control connectivity).
   - Add Maintenance Access (operating clearances, arc-flash boundaries, breaker/lineup withdrawal, replacement-component access).
   - Add Structural / Foundations / Supports (switchgear lineup and Electrical Building 810-1 foundations and supports).
   - Add signoff fields for engineering, construction (Tourmaline field construction), vendor commissioning, electrical/controls, utility coordination, and turnover review where applicable.

4. Establish Electrical Power tie-in controls.
   - Confirm source-side feed alignment with the 25/13.8 kV, 50 MVA utility-supplied transformer and the BC Hydro 25 kV (TBC) supply.
   - Confirm load-side radial feeders to the 6.9 kV, 4.16 kV, and 600 V step-down transformers and electrical buildings per accepted single-line and electrical drawings.
   - Confirm 13.8 kV cable installation matches the 15 kV / 133% insulation / shielded TECK basis; record cable insulation tests (megger, hi-pot or VLF as applicable) and termination inspection.
   - Mark utility-side metering, protection, isolation, and telemetry as readiness-gated by utility coordination (HRR-020-03-001).

5. Establish Grounding / Bonding controls.
   - Confirm the utility transformer is grounded by a 200 A, 10 s neutral grounding resistor configured as a tripping system.
   - Confirm the plant ground grid uses driven piles interconnected by a #2/0 green insulated main grounding conductor in the highest-voltage carrying tray.
   - Confirm the 13.8 kV switchgear lineup is connected to the ground grid at two points and that all bonding connections are compression type.
   - Record ground-resistance/continuity test results.

6. Establish I&C and Communications tie-in controls.
   - Confirm MV breaker control and MV protective relay wiring is UPS-served (120 VAC / 125 VDC) and that source feeders trace to the accepted UPS packages.
   - Confirm switchgear-to-plant-control communications (PLC/SCADA) per the project controls/communications design.
   - Mark loop and signal verification, and network commissioning, as hold points.

7. Establish readiness gates for incomplete source criteria.
   - Protection / coordination / arc-flash: require studies accepted before energization.
   - Standby-power scope split and protection coordination: require detailed-engineering decisions accepted (no 13.8 kV emergency-generator scope is included).
   - Geotechnical: require final geotechnical report and vendor equipment loads before closing foundation, anchorage, frost, settlement, and structural-support criteria for the switchgear lineup and Electrical Building 810-1.
   - Utility coordination: require BC Hydro coordination, metering point, and protection split accepted before utility-side energization.
   - Standards/regulatory: require verification of unavailable standards, permits, and regulatory triggers before final issue for construction.
   - Cold-weather: confirm installation, heating, anti-condensation, and commissioning provisions match the -40 deg C minimum ambient basis.

8. Prepare workface execution controls.
   - Identify work areas, access, lifting and offloading plans for the switchgear lineup and Electrical Building 810-1 module setting, sequencing, tie-in boundaries, inspection hold points, witness points, and turnover records.
   - Define Maintenance Access provisions (operating clearances, arc-flash boundaries, breaker withdrawal envelope, replacement-component access).
   - ASSUMPTION: Include construction logistics only where they affect the 13.8 kV switchgear package or its declared interfaces; broader Tourmaline construction scope is referenced, not redefined.

9. Perform pre-issue consistency review.
   - Check the CWP against the EPC Scope of Work (`DEL-020-01`), Package Datasheet (`DEL-020-02`), the vendor engineered equipment package (`DEL-020-04`), IFC electrical drawings, plot plan, equipment list, and the interface register.
   - Reconcile any equipment-allocation or building-assignment differences (see Guidance Conflict Table HRR-020-03-004) before treating ratings or quantities as closed.
   - Reaffirm that no centralized 13.8 kV emergency-generator scope is included (HRR-020-03-005).
   - Keep unresolved conflicts in the CWP exception register.

10. Execute field work and inspections.
    - Use approved IFC drawings/specifications, vendor installation instructions, and the CWP workface plan.
    - Record inspection results, exceptions, redlines, and interface signoffs.
    - Coordinate vendor commissioning, factory-fitted accessory verification, energization witness, and protection-relay testing per the EPC/Vendor/Tourmaline boundary.

11. Complete turnover.
    - Confirm all checklist items are signed off or carried as accepted exceptions.
    - Compile construction records, inspection records, interface records, cable test records, protection-relay test records, electrical-study acceptance evidence, utility coordination evidence, and unresolved/open-item dispositions.
    - Feed acceptance evidence into `DEL-020-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification check | Evidence |
|---|---|
| Package identity is correct | CWP cover/index matches `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Required artifacts are present | CWP includes work package, workface plan, and interface/turnover checklist. |
| Interfaces are covered | Checklist includes all six declared interface types for `PKG-020`. |
| Utility-side Electrical Power tie-in is controlled | Feed from the 25/13.8 kV, 50 MVA utility-supplied transformer witnessed and recorded; utility coordination accepted or exceptioned. |
| Load-side Electrical Power tie-in is controlled | Radial feeders to downstream step-down transformers/electrical buildings witnessed and recorded against accepted single-line drawings. |
| 13.8 kV cable installation is controlled | TECK 15 kV / 133% insulation / shielded basis verified; insulation/hi-pot/VLF and termination tests complete. |
| Grounding/bonding is controlled | Utility-transformer 200 A neutral grounding resistor installed and verified; plant ground grid #2/0 main installed; two-point ground connections at switchgear lineup verified; ground-resistance/continuity records complete. |
| I&C / Communications are controlled | UPS-served MV breaker control and protective relay loops verified; switchgear-to-plant-control network commissioning records complete. |
| Protection / coordination / arc-flash hold is controlled | Detailed electrical studies accepted or unresolved criteria remain `TBD`/exceptioned. |
| Standby-power scope split hold is controlled | DBM-current standby-power basis preserved (no 13.8 kV emergency-generator scope); decisions accepted or exceptioned. |
| Geotechnical / structural readiness is controlled | Final geotechnical report and vendor equipment loads accepted, or exceptions explicitly carried as `TBD`. |
| Maintenance Access is controlled | Walk-down record confirms clearances, arc-flash boundaries, breaker withdrawal envelope, and replacement-component access. |
| Cold-weather readiness is controlled | Installation, heating, anti-condensation, and commissioning provisions match -40 deg C basis. |
| Standards/regulatory verification is controlled | Standards and regulatory requirements not available in the workspace remain verification-required. |
| Turnover is complete | Inspection, interface signoff, exception, and turnover records are complete. |

## Records

- Construction Work Package index and issue record.
- Installation and tie-in workface plan.
- Electrical Power interface checklist (utility-side and load-side).
- Grounding / Bonding interface checklist.
- I&C / Control Cabling interface checklist.
- Communications / Network interface checklist.
- Maintenance Access interface checklist.
- Structural / Foundations / Supports interface checklist.
- 13.8 kV MV cable test records (insulation/hi-pot/VLF) and termination inspection records.
- Protection-relay test and energization records.
- Inspection and hold-point records (including witness points for vendor commissioning and energization).
- Electrical-study acceptance evidence (protection/coordination, arc-flash).
- Utility coordination evidence (BC Hydro agreement, metering point acceptance, protection split acceptance).
- Geotechnical, IFC drawing, electrical specification, and regulatory `TBD` and exception register.
- Turnover checklist and signoff record (feeding `DEL-020-06`).
- As-built/redline records where required by project controls.
