# Procedure: Construction Work Package

## Purpose

Define the controlled steps to produce and use the Construction Work Package for `PKG-081` Flare KO Drum (High Pressure) 3-25. The procedure supports construction planning, field execution readiness, inspection, interface signoff, turnover, and unresolved-item tracking for the vendor-supplied two HP flare KO drums (V-4100-2 in the compressor area; V-4150-2 in the tank farm) and their dedicated transfer pumps (P-4100-2 and P-4150-2).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Declared upstream dependencies: none declared during PREPARATION.
- Gate 7 rows for `DEL-081-03_construction-work-package`, `PKG-081`, and the `PKG-081` `INTERFACE_REGISTER.csv` rows are available.
- DBM source slices for the Flare and Blowdown system (V-4100-2, V-4150-2, P-4100-2, P-4150-2, HP/Cryo flare stack, 508 mm headers), the Construction Scope Summary, ambient design implications, geotechnical status, and standards constraints are available.
- Accepted EPC Package Datasheet (`DEL-081-02_package-datasheet`), vendor engineered equipment package (`DEL-081-04_vendor-engineered-equipment-package`), IFC piping/mechanical drawings, final geotechnical report, flare-system relief and blowdown studies, the external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001, and project mechanical/piping specifications are either accepted or explicitly carried as `TBD`.

## Steps

1. Confirm package identity.
   - Verify `PKG-081` Flare KO Drum (High Pressure) 3-25, WBS 02, CoA tracking number `26020-02-17-001`, discipline Mechanical, workbook row 54.
   - Record the package basis in the CWP cover/index, including the named in-scope tags V-4100-2, V-4150-2, P-4100-2, P-4150-2.

2. Confirm deliverable scope.
   - Include the construction work package, installation and tie-in workface plan, and construction interface and turnover checklist.
   - Keep exclusions and unknown detailed criteria (drum and pump mechanical data, flare relief/blowdown loads, shared-system split, foundation detailing) visible as `TBD`.

3. Build the interface checklist.
   - Add Process Piping.
   - Add Relief / Flare / Vent.
   - Add Drain / Containment.
   - Add Electrical Power.
   - Add EHT.
   - Add Grounding / Bonding.
   - Add Area / Exterior Lighting.
   - Add I&C / Control Cabling.
   - Add Maintenance Access.
   - Add Structural / Foundations / Supports.
   - Add signoff fields for engineering, construction, vendor commissioning, mechanical/piping, electrical/controls, and turnover review where applicable.

4. Establish Process Piping and Relief / Flare / Vent tie-in controls.
   - Confirm HP relief inlet connections to V-4100-2 (compressor area) and V-4150-2 (tank farm) align with the 508 mm (20 inch) HP header basis.
   - Confirm manifolding from both KO drums to the shared HP/Cryo flare stack (660 mm OD x 60,957 mm tall) per accepted flare-system drawings.
   - Confirm header slope, drainage back to KO drums, and isolation provisions per accepted piping drawings.
   - Mark pressure-test and NDE checkpoints per accepted project mechanical/piping specifications (`location TBD` where unavailable).

5. Establish Drain / Containment and pump-out controls.
   - Confirm drum drains and pump-out / liquid-transfer routing for P-4100-2 and P-4150-2 to slop or truck-out per accepted drawings.
   - Confirm containment provisions for the drum and pump areas.

6. Establish Electrical Power, EHT, Grounding / Bonding, and Area / Exterior Lighting tie-in controls.
   - Confirm pump motor and instrumentation power supply per accepted electrical drawings; verify phasing, cable, termination, and grounding.
   - Confirm EHT layout, control, and energization per cold-weather provisions for the -40 deg C minimum ambient basis.
   - Confirm grounding/bonding installation per the project grounding specification (mark `location TBD` where unavailable).
   - Confirm area lighting for the drum and pump locations per accepted lighting drawings.

7. Establish I&C / Control Cabling tie-in controls.
   - Confirm level, pressure, and pump control wiring from the package to the plant control system per accepted drawings.
   - Mark loop and signal verification as hold points.

8. Establish readiness gates for incomplete source criteria.
   - Flare relief loads and staggered blowdown sequence: require acceptance of the external Plant Shutdown and Blowdown Philosophy W242510-PRC-REP-000003-001 (or accepted exception) before closing relief and pressure-test criteria.
   - Shared HP/Cryo flare-stack and incinerator service split: require source ruling on the 03-25 / 04-25 allocation before closing the Relief / Flare / Vent scope boundary.
   - Geotechnical: require final geotechnical report and vendor equipment loads before closing foundation, anchorage, frost, settlement, and structural-support criteria for the two drums and two pumps.
   - Standards/regulatory: require verification of unavailable mechanical/piping specifications, standards, permits, and regulatory triggers before final issue for construction.
   - Cold-weather: confirm EHT, insulation, drainage, and commissioning provisions match the -40 deg C minimum ambient basis.

9. Prepare workface execution controls.
   - Identify work areas (compressor area for V-4100-2; tank farm for V-4150-2), access, lifting and offloading plans for drums and pumps, sequencing, tie-in boundaries, inspection hold points, witness points, and turnover records.
   - Define Maintenance Access provisions (drum manway access, internals lifting/handling, pump replacement, and truck-out access for collected liquids).
   - ASSUMPTION: Include construction logistics only where they affect the HP KO drum package, its transfer pumps, or its declared interfaces.

10. Perform pre-issue consistency review.
    - Check the CWP against the EPC Package Datasheet (`DEL-081-02`), the vendor engineered equipment package (`DEL-081-04`), IFC piping/mechanical drawings, plot plan, equipment list, the interface register, and the open shared-system interface item.
    - Reconcile any package-identity vs vendor-data differences (see Guidance Conflict Table HRR-081-03-001) before treating drum and pump ratings as closed.
    - Keep unresolved conflicts (HRR-081-03-002, HRR-081-03-003, HRR-081-03-004) in the CWP exception register.

11. Execute field work and inspections.
    - Use approved IFC drawings/specifications, vendor installation instructions, and the CWP workface plan.
    - Record inspection results, exceptions, redlines, pressure-test/NDE records, and interface signoffs.
    - Coordinate vendor commissioning, factory-fitted internals verification, and witness points per the EPC/Vendor boundary.

12. Complete turnover.
    - Confirm all checklist items are signed off or carried as accepted exceptions.
    - Compile construction records, inspection records, interface records, pressure-test/NDE acceptance evidence, flare-system acceptance evidence, and unresolved/open-item dispositions.
    - Feed acceptance evidence into `DEL-081-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Verification check | Evidence |
|---|---|
| Package identity is correct | CWP cover/index matches `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`; named tags V-4100-2, V-4150-2, P-4100-2, P-4150-2 carried forward. |
| Required artifacts are present | CWP includes work package, workface plan, and interface/turnover checklist. |
| Interfaces are covered | Checklist includes all ten declared interface types for `PKG-081`. |
| Process Piping tie-in is controlled | Inlet HP relief and pump-out/transfer piping connections witnessed and recorded; pressure-test and NDE records complete. |
| Relief / Flare / Vent tie-in is controlled | Manifolding to HP/Cryo flare stack witnessed; 508 mm header alignment, slope, drainage, and isolation verified. |
| Drain / Containment is controlled | Drum drain and pump-out/slop routing inspection signoffs complete. |
| Electrical Power tie-in is controlled | Pump motor and instrumentation power supply per accepted drawings; phasing, cable, termination, grounding witnessed. |
| EHT is controlled | Energization, insulation, and cold-weather provisions match -40 deg C basis. |
| Grounding/bonding is controlled | Continuity/impedance test records and inspection signoffs complete. |
| Area / Exterior Lighting is controlled | Field inspection confirms drum/pump area lighting per accepted drawings. |
| I&C / Communications are controlled | Loop checks and signal verification records complete. |
| Maintenance Access is controlled | Walk-down record confirms drum manway, internals lifting, pump replacement, and truck-out access. |
| Structural / Foundations / Supports is controlled | Foundation, anchorage, and structural support installation matches accepted drawings; final geotechnical inputs accepted or exceptioned. |
| Blowdown / relief readiness is controlled | External philosophy W242510-PRC-REP-000003-001 accepted or unresolved criteria remain `TBD`/exceptioned. |
| Shared-system readiness is controlled | HP/Cryo flare stack and incinerator service split with 04-25 resolved or carried as open interface. |
| Standards/regulatory verification is controlled | Standards, external philosophy documents, and regulatory requirements not available in the workspace remain verification-required. |
| Turnover is complete | Inspection, interface signoff, exception, and turnover records are complete. |

## Records

- Construction Work Package index and issue record.
- Installation and tie-in workface plan.
- Process Piping interface checklist.
- Relief / Flare / Vent interface checklist.
- Drain / Containment interface checklist.
- Electrical Power interface checklist.
- EHT interface checklist.
- Grounding / Bonding interface checklist.
- Area / Exterior Lighting interface checklist.
- I&C / Control Cabling interface checklist.
- Maintenance Access interface checklist.
- Structural / Foundations / Supports interface checklist.
- Inspection and hold-point records (including pressure-test, NDE, and witness points for vendor commissioning).
- Flare-system acceptance evidence (relief loads, blowdown sequence, shared-system allocation rulings).
- Geotechnical, IFC drawing, mechanical/piping specification, and regulatory `TBD` and exception register.
- Turnover checklist and signoff record (feeding `DEL-081-06`).
- As-built/redline records where required by project controls.
