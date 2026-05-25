# Procedure: DEL-035-04 — Vendor Engineered Equipment Package

This Procedure describes how the Package Vendor produces the engineered equipment package for PKG-035 (13.8kV Switchgear Electrical Building 810-1) and how the EPC Integrator interacts with it. Steps that require values not yet available are marked `TBD` and routed to the Conflict Table in `Guidance.md`.

## Prerequisites

- EPC Scope of Work (`DEL-035-01`) issued by EPC Integrator and available to the Package Vendor.
- EPC Package Datasheet (`DEL-035-02`) issued by EPC Integrator; this is the binding handoff for switchgear ratings and interface requirements.
- Declared upstream dependencies: none recorded in `_DEPENDENCIES.md` (coordination mode DECLARED). Vendor should treat `DEL-035-01` and `DEL-035-02` as functional upstream inputs even though not yet listed as declared edges.
- Access to:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical Design Basis; Electrical Buildings)
  - `PACKAGE_REGISTER.csv` row `PKG-035`
  - `DELIVERABLE_REGISTER.csv` row `DEL-035-04`
  - `_Sources/26020-Package_Requirements.docx` (parsing required in a follow-up pass)

## Steps

1. **Confirm package identity and scope.** Verify package tag `26020-01-30-026`, workbook row 37, and the SOW item `SOW-0036` from `_CONTEXT.md` and the Gate 7 registers. Validate that scope (engineering, design, fabrication/supply, physical equipment) matches the PKG-035 ownership statement.
2. **Lock the DBM-derived role.** Adopt 13.8 kV / 3-phase / 3-wire / 60 Hz / low-resistance grounded for the main bus; size for full facility scope; configure radial outgoing feeders to 820-1, 830-1, 840-1, 850-1, 860-1 electrical buildings (per DBM).
3. **Reconcile the EPC Package Datasheet (`DEL-035-02`).** Extract short-circuit duty, BIL, continuous current, arc-flash class, enclosure rating, lineup count, breaker counts, control voltage, and protection scheme. Where the datasheet is silent, record `TBD` and add to the Conflict Table; do not invent values.
4. **Develop the modular electrical building design.** Apply DBM electrical-building basis: prefabricated and shop-built; elevated on piles; bottom cable entry; HVAC n+1; TECK / ACIC wiring; EMT only between adjacent panels; outdoor GFI receptacle; doors sized (or transomed) for largest equipment removal.
5. **Develop the 13.8 kV switchgear lineup.** Produce single-line, three-line, schematic, and protection coordination drawings consistent with Steps 2 and 3. Coordinate with the upstream 25 kV/13.8 kV utility transformer interface.
6. **Develop interface package.** For each PKG-035 interface type (Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Utility Piping; Drain/Containment; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports), define the vendor-side battery limit, signal list, connection method, and acceptance criteria.
7. **Develop grounding and bonding design.** Two-point ground-grid connection for all major equipment; bolted ground-well test points; above-grade green-insulated ground wires in PVC conduit where mechanical protection is required.
8. **Fabricate / procure the physical package.** Shop-fabricate the building; procure switchgear and ancillary equipment; conduct factory inspections.
9. **Run factory acceptance testing (FAT).** Execute FAT on the 13.8 kV switchgear lineup (mechanical, dielectric, control wiring, protection logic, HMI, ground continuity). Record test results.
10. **Issue the vendor engineering / design record set and physical package.** Submit drawings, calculations, datasheets, FAT reports, and operations/maintenance documentation through `DEL-035-05` (Vendor Document Turnover Package). The physical building and switchgear are released to site per EPC procurement/construction coordination.
11. **Support EPC integration review.** Provide responses, clarifications, and revisions through `DEL-035-06` (EPC Vendor Package Review and Acceptance).

## Verification

- Drawing review by EPC Integrator confirms one-line / radial feeder schedule matches DBM electrical building list.
- FAT results show: dielectric tests passed at design BIL; primary injection of protection schemes verified; control wiring 100% point-to-point checked; ground continuity within tolerance.
- Building inspection confirms: shop-build, elevated on piles, bottom cable entry, n+1 HVAC operation under single-unit shutdown, TECK/ACIC wiring, EMT only between adjacent panels, outdoor GFI receptacle, door/transom sizing.
- Interface matrix review confirms vendor-side battery limits are defined for every PKG-035 interface type.
- Plot plan check confirms ≥ 25 m separation from any fired heater per OGAOM Sec. 9.6.15 (as cited in DBM).
- Reconciliation of vendor datasheet values vs. EPC Package Datasheet (`DEL-035-02`) closed with no open `TBD` against ratings before EPC acceptance.

## Records

- Vendor design basis and datasheet set (anticipated artifact).
- Single-line / three-line / schematic / protection coordination drawings.
- Building general arrangement, layout, grounding, HVAC drawings.
- Interface matrix and battery-limit schedule for PKG-035 interface types.
- FAT plan and test reports; inspection reports; punch list closures.
- Vendor Document Turnover Package inputs (`DEL-035-05`).
- EPC Vendor Package Review log entries (`DEL-035-06`).
