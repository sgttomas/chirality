# Procedure: DEL-036-04_vendor-engineered-equipment-package

## Purpose

Describe how the Package Vendor produces the engineered equipment package and the vendor design basis/datasheet set for PKG-036, from EPC handoff through factory readiness, in a way that is consistent with the EPC Scope of Work (`DEL-036-01`), the EPC Package Datasheet (`DEL-036-02`), and the DBM electrical design basis.

## Prerequisites

- Accepted EPC Scope of Work (`DEL-036-01`) is available to the vendor.
- Accepted EPC Package Datasheet (`DEL-036-02`) is available to the vendor, including the package interface requirements matrix (`ART-25E7F85421`).
- `_REFERENCES.md` source pointers are accessible.
- DBM source slices used in this procedure (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2811-2816, 2911, 2935, 2955, 2971-2977, 2985, 3008) are available.
- Declared dependencies in `_DEPENDENCIES.md` reviewed; PREPARATION declared none for this deliverable.
- Building-number conflict CT-036-04-001 status reviewed; vendor design freeze should not proceed past Step 5 without a ruling.

## Steps

1. **Receive and confirm EPC handoff inputs.**
   - Confirm receipt and revision of `DEL-036-01` and `DEL-036-02`, including the interface matrix and any tagged-equipment basis.
   - Record any unresolved Conflict Table items (CT-036-04-001, CT-036-04-002, CT-036-04-003) as inputs requiring EPC clarification.

2. **Establish the vendor design basis.**
   - Capture the medium-voltage service basis (6.9 kV, 3-phase, 60 Hz, LRG) per REQ-036-04-003.
   - Capture upstream grounding (100 A, 10 s NGR, tripping) per REQ-036-04-004.
   - Capture MV cable interface (8 kV TECK, 100 percent insulation, shielded) per REQ-036-04-005.
   - Capture building construction baseline (modular, piled, bottom cable entry, n + 1 HVAC) per REQ-036-04-006 and REQ-036-04-007.
   - Capture grounding/bonding rules (two-point ground grid connection; CEC-sized separate copper ground conductors) per REQ-036-04-008.
   - Record TBD items where source/EPC data is silent (e.g., switchgear kA/BIL/bus rating; protection settings) per REQ-036-04-013.

3. **Engineer the switchgear and supporting equipment.**
   - Produce switchgear single-line, protection-and-metering scheme, bus arrangement, breaker schedule, and panel schedules, all aligned with `DEL-036-02`.
   - Confirm Ethernet integration approach to the plant PLC central control panel (ASSUMPTION from MCC convention; see CT-036-04-002).
   - Produce coordinated grounding, lighting, control-cabling, and communications scope aligned with the PKG-036 interface set in `INTERFACE_REGISTER.csv` per REQ-036-04-010.

4. **Engineer the electrical building.**
   - Issue modular building general arrangement, structural piling/elevation drawings, HVAC sizing (n + 1), and cable-entry/under-building tray geometry.
   - Confirm cable tray and conduit routing do not impair maintenance access per REQ-036-04-011.

5. **Hold vendor design freeze.**
   - Do not proceed past freeze until CT-036-04-001 (building number vs. voltage) is ruled by the human authority.
   - Confirm responsibility-split alignment with `PACKAGE_REGISTER.csv` per REQ-036-04-012.

6. **Fabricate, assemble, and ship.**
   - Fabricate the prefabricated electrical building shell (Shop, per DBM equipment-list rows 2811-2816).
   - Assemble switchgear, MV equipment per EPC datasheet allocations, and internal distribution; integrate building services.
   - Apply manufacturer/factory QC at standard inspection hold/witness points.

7. **Produce the vendor design basis and datasheet set.**
   - Compile the vendor design basis, datasheets, schedules, single-lines, layouts, grounding plans, cable schedules, HVAC schedules, and the package-side interface representation.
   - Maintain traceability matrix from vendor outputs to EPC datasheet requirements and to the DBM source slices cited in `Datasheet.md` and `Specification.md`.

8. **Hand off to EPC for review and acceptance.**
   - Provide the physical equipment package and vendor design basis/datasheet set to the EPC Integrator for `DEL-036-06` review, integration into `DEL-036-03`, and turnover via `DEL-036-05`.

## Verification

- Vendor design basis review against REQ-036-04-003 through REQ-036-04-008.
- Interface matrix cross-check between vendor outputs and the EPC Package Datasheet interface matrix (`ART-25E7F85421`) per REQ-036-04-010.
- Factory acceptance test (FAT) records confirming MV switchgear ratings declared in the EPC Package Datasheet (REQ-036-04-013) and protection coordination compatible with the 100 A NGR tripping scheme (REQ-036-04-004).
- Building inspection record confirming modular, piled, bottom-entry construction and n + 1 HVAC (REQ-036-04-006, REQ-036-04-007).
- Grounding drawing and cable-routing review records (REQ-036-04-008, REQ-036-04-011).
- Conflict Table closure records for CT-036-04-001 (before design freeze), CT-036-04-002, and CT-036-04-003.

## Records

- Vendor engineered physical equipment package evidence (`ART-5464B33F42`).
- Vendor package design basis and datasheet set (`ART-4CFD465CF3`).
- Vendor traceability matrix to `DEL-036-01` and `DEL-036-02`.
- Vendor FAT and inspection reports.
- Conflict-table ruling records carried forward into `DEL-036-06` (EPC Vendor Package Review and Acceptance).
- Run record at `{ScopePath}/_run_records/TASK_RUN_*.md` for this initialization run.
