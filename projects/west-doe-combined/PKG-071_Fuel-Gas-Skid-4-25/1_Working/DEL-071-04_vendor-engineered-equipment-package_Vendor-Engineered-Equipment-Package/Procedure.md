# Procedure: DEL-071-04 Vendor Engineered Equipment Package

This procedure describes the operational sequence to produce the vendor-engineered equipment package for PKG-071 (Fuel Gas Skid 4-25). It is written for the Package Vendor as the producer, with EPC Integrator review interfaces.

## Purpose

To produce the skid-mounted Low-Pressure Fuel Gas equipment package (heater + scrubber on a skid) developed from the EPC Scope of Work (DEL-071-01) and the EPC Package Datasheet (DEL-071-02), satisfying the source-supported requirements in Specification.md and meeting the twelve declared facility interfaces in the Gate 7 INTERFACE_REGISTER for PKG-071.

## Prerequisites

- Approved EPC Scope of Work (DEL-071-01) for PKG-071 is available to the vendor.
- Approved EPC Package Datasheet (DEL-071-02) for PKG-071 is available to the vendor (this governs design flow, fuel-gas composition and heating value, interface terminations, and any project-specific overrides).
- Access to the package requirements text in 26020-Package_Requirements.docx package heading 25 (currently TBD as a locally accessible text slice).
- Access to the vendor RFQ basis 26020-01-PT-RFQ-23-001_FG_Skid_2.docx (currently TBD as a locally accessible text slice).
- Acceptance of the Gate 7 INTERFACE_REGISTER PKG-071 row set as the binding interface-type list.
- Declared upstream dependencies in `_DEPENDENCIES.md`: none currently declared; functional upstream from DEL-071-01 and DEL-071-02 should be promoted to declared upstream when those deliverables reach the agreed maturity threshold.

## Steps

1. Confirm receipt of DEL-071-01 (Scope of Work) and DEL-071-02 (Package Datasheet) from the EPC Integrator and capture any deviations or open items.
2. Develop the vendor design basis covering process (flow, pressure, temperature, fuel-gas composition and heating value), mechanical (heater duty and construction, scrubber sizing per k=0.35 imperial max with pressure de-ration), structural (skid), electrical (cabling for SCR remote panels at 600 V, grounding/bonding), and I&C (skin-temperature thermocouple override, package controls and signals).
3. Size the heater for the EPC Package Datasheet design flow and temperature rise (gas heated to 95 F / 35 C) at operating pressure 150 psig; establish required heater capacity. (Capacity TBD until DEL-071-02 inputs are confirmed.)
4. Size the fuel gas scrubber using k factor 0.35 (imperial) maximum with operating-pressure de-ration; select internals consistent with the EPC Package Datasheet gas-quality basis.
5. Establish MAWP for pressure parts and stamp accordingly; record on the vendor datasheet. (MAWP value TBD per source until vendor sets it.)
6. Lay out the skid and package piping to terminate the twelve facility interfaces declared in the Gate 7 INTERFACE_REGISTER for PKG-071 at the package boundary. Coordinate termination locations, sizes, and ratings with the EPC Integrator per the EPC Package Datasheet.
7. Produce vendor equipment datasheets (heater, scrubber, skid, instrumentation), GA drawings, P&ID extracts at the package boundary, electrical schematics for skid-side equipment, and I&C wiring diagrams.
8. Coordinate with the EPC Integrator on by-others items excluded from the vendor scope: shipping to site, installation, tie-in piping, and electrical tie-in.
9. Fabricate / supply the physical equipment package; perform shop fabrication checks, pressure tests on pressure-containing equipment, FAT on the skid, and produce as-built records.
10. Hand over vendor documentation under DEL-071-05 (Vendor Document Turnover Package), supplying the vendor document register, submittals, and source-required vendor documentation.
11. Support EPC Integrator review and acceptance under DEL-071-06 (EPC Vendor Package Review and Acceptance), including responses to review comments and turnover evidence.

## Verification

- Step 1: Document receipt log showing DEL-071-01 and DEL-071-02 ingest and any open-item list.
- Steps 2-5: Design basis review by the EPC Integrator against the EPC Package Datasheet; vendor datasheet check; pressure-test certificates and nameplate verification (MAWP, design P/T).
- Step 6: Interface termination check against `INTERFACE_REGISTER.csv` PKG-071 rows and the EPC Package Datasheet interface matrix.
- Step 7: Vendor document register completeness check at submittal milestones.
- Step 8: Confirmation that the vendor scope excludes the listed by-others items.
- Step 9: FAT records and shop QA/QC records; shipping documentation when applicable (note: shipping is by others).
- Step 10: Acceptance log under DEL-071-05.
- Step 11: Acceptance log under DEL-071-06.

## Records

- Vendor design basis document set.
- Vendor equipment datasheets (heater, scrubber, skid, instrumentation).
- Vendor general arrangement (GA) and P&ID extracts at the package boundary.
- Electrical and I&C schematics for skid-side scope.
- Pressure-test certificates, weld and NDE records, FAT records.
- Vendor document register and submittal evidence (delivered under DEL-071-05).
- EPC Integrator review log and acceptance evidence (collected under DEL-071-06).
