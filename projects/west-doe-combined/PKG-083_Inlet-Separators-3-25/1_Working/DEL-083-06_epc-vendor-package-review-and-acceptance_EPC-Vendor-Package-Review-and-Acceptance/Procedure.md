# Procedure: EPC Vendor Package Review and Acceptance

## Purpose

Produce the EPC Integrator's vendor package review-and-acceptance artifact set for the Inlet Separators vendor package (PKG-083; equipment V-1600-2, V-1700-2): a vendor document review log, a package acceptance and turnover checklist, test/inspection evidence references, and turnover evidence. The procedure covers both the production of the acceptance package and the operational use of it at handoff.

## Prerequisites

- Issued or working drafts available for:
  - DEL-083-01 EPC Scope of Work
  - DEL-083-02 Package Datasheet
  - DEL-083-03 Construction Work Package
  - DEL-083-04 Vendor Engineered Equipment Package
  - DEL-083-05 Vendor Document Turnover Package
- Access to authoritative source materials:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
  - `26020-Package_Requirements.docx` package heading 36 (currently location TBD as text)
  - PACKAGE_REGISTER, DELIVERABLE_REGISTER, ARTIFACT_REGISTER, INTERFACE_REGISTER, OBJECTIVE_DELIVERABLE_MAP from the Gate 7 published snapshot.
- Declared upstream dependencies from `_DEPENDENCIES.md`: none declared during PREPARATION (TBD — undeclared coupling to DEL-083-01..05 is assumed in practice).
- Authorized EPC reviewer with responsibility per `_CONTEXT.md` (EPC Integrator lead, Package Vendor input).

## Steps

1. **Initialize the review log (ART-AE2840AE44).** Open a vendor document review log structured by vendor document (datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating/design envelopes, sparing philosophy, materials/coating basis, maintenance access, shipped-loose item lists, vendor document registers). For each vendor document expected per 3-25 DBM (Mechanical Packages section), create a row with received/awaiting status.
2. **Compare vendor equipment datasheets to design basis.** For each separator (V-1600-2, V-1700-2), compare vendor-supplied equipment datasheet values to the per-separator basis table (40 MMSCFD gas; 556 m3/d condensate; 1,800 m3/d produced water; 2,743 mm dia; 12,191 mm S/S; ANSI 600#; 4,963 kPag design; 38 m3 slug; Devchem 253 coating). Record matches and deviations in the review log.
3. **Verify internals and control configuration.** Check vendor general-arrangement and P&ID extracts for: Devchem 253 coating; manually adjustable weir; vertical/horizontal high-performance mesh/vane mist eliminators; de-sanding provisions; symmetric inlet piping; at least two parallel inlet pressure-control valves (balanced globe hardened trim, dP <= 5 psid); at least two parallel produced-water level-control valves.
4. **Verify cold-climate and sour-service compliance.** Confirm vendor materials selection, instrumentation suitability, heat tracing, and package building scope are consistent with the -40 deg C ambient basis and sour-service requirements. Flag any catalog selection that defaults to a warmer ambient.
5. **Verify interfaces.** For each interface type listed in PACKAGE_REGISTER PKG-083 (Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports), confirm that vendor tie-in points, loads, and signal lists match the facility-side design. Produce a signed tie-in list.
6. **Review test and inspection evidence (ART-30486BD773).** Collect and review FAT reports, hydrotest records, NDE records, and shop inspection records from the vendor. Where TBD because DEL-083-02/DEL-083-04 detail is not yet issued, record the gap and the planned closure date.
7. **Compile the acceptance and turnover checklist (ART-27FC8B869F).** Roll up the review log, deviation log, interface tie-in list, and test/inspection evidence into a checklist with per-item acceptance disposition (accepted / accepted with carry-forward / rejected). Carry forward all unresolved TBD/TBC items from steps 2-6 into a TBD/TBC disposition log appended to the checklist.
8. **Coordinate with DEL-083-05 turnover index.** Cross-reference the acceptance checklist's document set against the Vendor Document Turnover Package index; reconcile any missing items before signing.
9. **Sign and issue.** EPC Integrator signs acceptance; Package Vendor signs vendor-input attestation. Move artifacts to the package `2_Checking` and then `3_Issued` folders per the project lifecycle convention (TBD — exact movement rule not restated in accessible sources for this deliverable; follow project-level convention).

## Verification

- Review log contains a row for every vendor document expected under 3-25 DBM "Mechanical Packages" required package deliverables.
- Per-separator deviation log is empty or each entry has an explicit accepted/rejected disposition.
- Interface tie-in list is signed and references each PKG-083 interface type.
- Test/inspection evidence log either references actual records or lists a TBD with a closure date.
- Acceptance checklist is signed by EPC Integrator with Package Vendor input.
- TBD/TBC disposition log identifies each open item from the design basis and its handling (resolved, carried to commissioning, blocked).
- Cross-reference with DEL-083-05 shows no orphan documents on either side.

## Records

- Vendor document review and comment log (ART-AE2840AE44).
- Per-separator deviation log (subordinate to review log).
- Interface tie-in list, signed (subordinate to acceptance checklist).
- Test/inspection evidence references (ART-30486BD773).
- Vendor package acceptance and turnover checklist (ART-27FC8B869F), signed.
- TBD/TBC disposition log (subordinate to acceptance checklist).
- Cross-reference index against DEL-083-05 turnover package.
