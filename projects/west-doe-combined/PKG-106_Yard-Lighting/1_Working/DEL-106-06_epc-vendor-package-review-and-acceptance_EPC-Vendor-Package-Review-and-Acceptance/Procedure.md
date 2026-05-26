# Procedure — EPC Vendor Package Review and Acceptance (DEL-106-06)

> Operational document. How the EPC Integrator produces the review and acceptance evidence package for the Yard Lighting vendor scope.

## Purpose

Define the sequence of actions the EPC Integrator follows to review the vendor-engineered Yard Lighting package (DEL-106-04) and the Vendor Document Turnover (DEL-106-05), and to produce the acceptance evidence (DEL-106-06) against the EPC SOW (DEL-106-01), Package Datasheet (DEL-106-02), and Construction Work Package (DEL-106-03).

## Prerequisites

- Sibling deliverables available or in progress:
  - DEL-106-01 EPC Scope of Work
  - DEL-106-02 EPC Package Datasheet
  - DEL-106-03 EPC Construction Work Package
  - DEL-106-04 Vendor Engineered Equipment Package
  - DEL-106-05 Vendor Document Turnover Package
- Local references identified in `_REFERENCES.md`, including:
  - DBM `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` "Lighting and Receptacles" section (lines 3027, 3031, 3035) and area-lighting scope note (line 120)
  - DBM `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-04 site basis (line 145) and construction-scope summary (lines 38, 75)
  - Workbook `_Sources/26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` row 12
- Declared upstream/downstream dependencies (none formally declared as of `_DEPENDENCIES.md` 2026-05-24; ASSUMPTION: DEL-106-01..05 are *de facto* upstream).
- Identified EPC Integrator review lead and assigned discipline reviewers (Electrical, Instrumentation/Controls for lighting-control circuits, Civil for pole foundations, HSE for area-classification and light-pollution) — TBD assignment.
- Current revision of facility area-classification drawings available to reviewers (per CFT-5).
- Jurisdictional light-pollution regulatory citation confirmed (per CFT-3) or recorded as outstanding.

## Steps

1. **Initiate acceptance package.**
   - Create or maintain the records listed under Records (review log, checklist, test/inspection index, turnover index, punchlist register) in this deliverable folder.
   - Record reviewers and roles.

2. **Vendor document review.**
   - For each document delivered under DEL-106-05, open a row in the review log: document ID, revision, reviewer, comments, disposition (Approved / Approved with comments / Revise and resubmit / Rejected), and date.
   - Verify completeness of the vendor document register against the EPC SOW (DEL-106-01) and Package Datasheet (DEL-106-02).

3. **Technology and electrical-basis conformance check (REQ-1, REQ-2, REQ-4).**
   - Confirm all luminaires are LED (DBM line 3027/3031).
   - Confirm general-purpose lighting circuits at 120/208 V fed from the nearest power distribution centre, or document deviation.
   - Confirm emergency-lighting provisions where buildings fall within the package scope (DBM line 3031); verify at least two emergency fixtures per building and battery-backup specification.

4. **Area-classification and code conformance check (REQ-3, REQ-7, REQ-8).**
   - For each luminaire/location combination, confirm area-classification suitability against the current area-classification drawing revision; attach the certification document(s) to the review log row.
   - Confirm wiring methods, conduit selection, and area-class sealing comply with the CEC (DBM cable/conduit prose).
   - Confirm grounding and bonding continuity tests for poles, fixture chassis, panels, and conduit systems.

5. **Cold-climate and environmental conformance check (REQ-6).**
   - Confirm luminaires, drivers, controls, and field wiring rated for -40 deg C to +35 deg C (DBM `3-25_Comp_and_Liquids_DBM.md` SEC-04).
   - Document any heater, gasket, or low-temperature lens provisions and their vendor evidence.

6. **Light-pollution and layout conformance check (REQ-5, REQ-15).**
   - Confirm downward illumination, no horizontally aimed floodlights, photocell or switch control, selective minimization of exterior lighting to working areas, and mast-pole placement away from pad edges where mast poles are used (DBM line 3035).
   - Confirm compliance against the governing jurisdictional light-pollution regulation (citation per CFT-3 ruling, TBD).
   - Cross-check as-built lighting layout against design layout.

7. **Test and inspection evidence collection (REQ-11).**
   - Index factory photometric reports, hazardous-area certification documents, grounding/bonding continuity test records, field illumination/uniformity measurements, energization check records, and photocell/lighting-control verification records.
   - Record any witnessed-test attendance and outcomes.
   - For deferred or not-applicable items, record rationale.

8. **Acceptance checklist consolidation (REQ-10).**
   - Populate the package acceptance checklist with one row per requirement (REQ-1 ... REQ-15), referencing the supporting evidence row(s) from the review log and the test/inspection index.
   - Record scope conformance to DEL-106-01, technical conformance to DEL-106-02, constructability/turnover conformance to DEL-106-03, and integration interface conformance (Electrical Power, Grounding/Bonding, Area/Exterior Lighting per workbook row 12).

9. **Punchlist management (REQ-14).**
   - Capture any open items as punchlist entries with owner, target date, and severity.
   - Cross-link each punchlist entry to the originating review-log row, checklist item, or test record.
   - Flag any open items dependent on Conflict Table rulings (CFT-1 ... CFT-6).

10. **Turnover record assembly (REQ-12).**
    - Compile Mechanical Completion, Pre-Commissioning, and Commissioning/Operational Acceptance records for the yard lighting system.

11. **Human acceptance signature (REQ-13).**
    - Route the consolidated acceptance package to the EPC Integrator (and Owner where required) for signature.
    - Record signatory name, role, and date in the acceptance signature record. Agent involvement is limited to drafting and checking; no agent certifies.

## Verification

- Each requirement (REQ-1 ... REQ-15) is satisfied by a verification ID (V-1 ... V-7) in `Specification.md §Verification` and supported by at least one row in the review log, test/inspection index, or turnover register.
- The acceptance checklist explicitly states pass/fail status per requirement; any "conditional" disposition references the corresponding punchlist entry.
- The Conflict Table in `Guidance.md` is reviewed and either rulings have been applied or unresolved items are carried forward as punchlist items.

## Records

- Vendor document review log
- Package acceptance checklist
- Test/inspection evidence index (factory photometric, hazardous-area certification, grounding continuity, field illumination/uniformity, energization, lighting-controls verification)
- Punchlist register
- Turnover record set (MC, PC, Commissioning/OA)
- Acceptance signature record (human signatories)
