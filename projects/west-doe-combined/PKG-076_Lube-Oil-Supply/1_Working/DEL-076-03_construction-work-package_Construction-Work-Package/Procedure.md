# Procedure — DEL-076-03 Construction Work Package (Lube Oil Supply, PKG-076)

This Procedure describes how the Construction Work Package is **produced** (as an EPC Integrator deliverable) and how the installation it specifies is **executed** in the field. The two threads are kept separate below.

## Prerequisites

### To produce the CWP

- DEL-076-01 Scope of Work — accepted (defines the package scope in EPC terms).
- DEL-076-02 Package Datasheet — accepted (defines technical handoff data, including vendor interface points).
- DEL-076-04 Vendor Engineered Equipment Package — vendor GA / nozzle list / weights available (needed for foundation, lift, and tie-in design).
- Accessible source slices from 26020-Package_Requirements.docx heading 30 (SCOPE_LEDGER SOW-0135..SOW-0138 already extracted into decomposition; deliverable-local source slice — location TBD).
- Facility design basis references from DBM-Deepcut/4-25_Deepcut_DBM.md (SEC-11 Civil/Buildings; SEC-12 Electrical; SEC-13 Controls; SEC-15 Regulatory/Codes/Standards). Locally accessible at `_Sources/DBM-Deepcut/` per `_REFERENCES.md` Shared Source Root.

### To execute the installation

- Vendor lube oil package delivered to site (P-9240-1, P-9250-1, split horizontal storage tank; vendor scope per PACKAGE_REGISTER row 70).
- Pile foundations completed at the Storage Tank Area location.
- Facility utility piping, drain headers, electrical feeders, grounding grid, lighting circuits, and I&C cable trays available to the lube oil package boundary (interfaces IFC-B592C2D9F7, IFC-09EA6BEDB8, IFC-4D53A7E70E, IFC-7117284B73, IFC-986D504634, IFC-8C17CDE23B).
- Lift plan approved; vendor weights confirmed.
- Receipt inspection complete — motor nameplate verified as **non-Toshiba** (SCOPE_LEDGER SOW-0138).

## Steps

### A. Produce the Construction Work Package

1. Confirm scope split: extract EPC-side scope items from SCOPE_LEDGER SOW-0135..SOW-0138 and PACKAGE_REGISTER row 70. Verify against `_CONTEXT.md` Scope.
2. Enumerate the eight interface facts (INTERFACE_REGISTER IFC-* for PKG-076). For each, capture the field-work scope, tie-in location, materials class, and acceptance check.
3. Draft the installation and tie-in workface plan covering:
   - Pile installation and foundation acceptance
   - Package set / rigging plan
   - Mounting platform and stairs erection
   - Tie-in piping (suction, discharge to compressor frame day tanks, drain, vent if any)
   - Electrical feeder pulls and motor terminations
   - Grounding and bonding
   - Lighting tie-in
   - I&C / control cabling pulls and terminations
4. Draft the construction interface and turnover checklist covering each requirement (REQ-CWP-01 through REQ-CWP-12 in `Specification.md`).
5. Cross-check terminology and values against the Datasheet, Specification, and Guidance documents.
6. Mark all unresolved items `TBD` with source-slice pointers rather than guessing. Surface conflicts in the Guidance Conflict Table.
7. Submit the CWP into the package gate review (DEL-076-06 EPC Vendor Package Review and Acceptance is the consuming review surface).

### B. Execute the installation (field thread, summarized for the CWP itself)

1. Receipt inspection of vendor package; verify motor nameplate (no Toshiba — REQ-CWP-05).
2. Set package on pile foundations; verify foundation acceptance (REQ-CWP-01).
3. Erect mounting platform and stairs (REQ-CWP-09).
4. Install tie-in piping (suction from heated tank sections; discharge routing to compressor frame day tanks; vents/drains to facility headers) — REQ-CWP-02, REQ-CWP-03. Verify sour-service materials traceability (REQ-CWP-10).
5. Pull and terminate electrical feeders to P-9240-1 and P-9250-1 motors (REQ-CWP-04).
6. Install grounding and bonding for pump skids, tank, and piping (REQ-CWP-06).
7. Verify exterior lighting coverage of the package area (REQ-CWP-07).
8. Pull and terminate I&C / control cabling for pump controls and any tank instrumentation (REQ-CWP-08).
9. Hydrotest tie-in piping at piping-class pressure (value TBD — location TBD).
10. Loop check controls and verify motor rotation.
11. Walk down maintenance access (REQ-CWP-09).
12. Complete and sign construction interface and turnover checklist (REQ-CWP-11); hand off to commissioning.

## Verification

| Step / Requirement | Verification | Evidence |
|---|---|---|
| REQ-CWP-01 (foundations) | Foundation acceptance inspection | Foundation acceptance record |
| REQ-CWP-02 (tie-in piping) | Visual + hydrotest at piping class pressure | Piping inspection report; hydrotest record |
| REQ-CWP-03 (containment/drains) | Drain routing walk-down | Containment inspection record |
| REQ-CWP-04 (electrical connections) | Loop check; megger; continuity | Electrical test records |
| REQ-CWP-05 (No Toshiba motors) | Nameplate inspection at receipt | Receipt inspection log |
| REQ-CWP-06 (grounding/bonding) | Ground resistance test; bonding continuity | Grounding test record |
| REQ-CWP-07 (lighting) | Lighting walk-down vs facility lighting standard (TBD) | Walk-down report |
| REQ-CWP-08 (I&C cabling) | Loop check; point-to-point | I&C test records |
| REQ-CWP-09 (maintenance access) | Access walk-down vs vendor maintenance requirements | Walk-down report |
| REQ-CWP-10 (sour-service integrity) | Materials traceability review; weld NDE per applicable code (TBD) | MTR file; NDE reports |
| REQ-CWP-11 (turnover checklist) | Signed checklist | Signed construction interface and turnover checklist |
| REQ-CWP-12 (design conditions) | Operating/design condition cross-check at turnover | Turnover review record |

## Records

The CWP execution shall produce and retain:

- Construction work package master document (this deliverable)
- Installation and tie-in workface plan
- Construction interface and turnover checklist (signed)
- Foundation acceptance record
- Piping inspection report and hydrotest record
- Electrical and grounding test records
- I&C loop check and point-to-point records
- Materials traceability file (MTRs) for sour-service segments
- Weld NDE reports per applicable code (code TBD)
- Receipt inspection log (including motor nameplate confirmation)
- Maintenance access walk-down report

These records feed DEL-076-05 Vendor Document Turnover Package (where applicable) and DEL-076-06 EPC Vendor Package Review and Acceptance.
