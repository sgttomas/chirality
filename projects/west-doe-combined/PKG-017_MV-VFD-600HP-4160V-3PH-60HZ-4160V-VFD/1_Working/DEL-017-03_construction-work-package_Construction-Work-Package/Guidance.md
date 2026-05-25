# Guidance: DEL-017-03_construction-work-package

## Purpose

The Construction Work Package (CWP) for `PKG-017` exists to translate the accepted EPC Scope of Work and Package Datasheet for the medium-voltage VFD package into a field-executable construction, tie-in, inspection, and turnover plan. It is the mandatory Gate 5 EPC anchor deliverable that bridges vendor-engineered equipment delivery and facility-level integration.

## Principles

- **Authority hierarchy.** Local source material (DBM electrical section, project electrical specifications when available) is authoritative; Gate 7 register entries identify scope; decomposition narrative does not create construction requirements where source text is silent.
- **Conservative inference.** Where the accessible source set does not establish a value (driven-machine identity, foundation layout, cooling system, exact location), the CWP shall carry `TBD`, not an invented value.
- **Interface discipline.** Each of the six PKG-017 interface facts in `INTERFACE_REGISTER.csv` shall appear as a construction tie-in scope; the CWP shall not silently drop or add interface facts.
- **Responsibility discipline.** The CWP describes EPC Integrator-owned installation, construction tie-in, and turnover; it does not absorb Package Vendor scope (engineering, design, vendor documentation, equipment package) or reverse the responsibility split recorded in `PACKAGE_REGISTER.csv`.

## Considerations

- The 03-25 facility's accessible 4160 V electrical basis is dominated by the inlet compressor motors KM-2150 and KM-2250 (5,200 hp / 3,878 kW at 4,000 V with starting VFDs under SCA-001 VE #34). A 4160 V, 600 HP MV VFD does not appear in the accessible DBM source slice. Construction execution should not assume the inlet-compressor VFD basis applies to PKG-017 without explicit confirmation.
- The 4160V MCC is the typical source-supported MV tie-in point and the EtherNet path to the plant PLC central control panel. The CWP should anchor electrical and communication tie-ins on this basis unless detailed design designates an alternative.
- MV cable segregation, grounding/bonding, cable tray/conduit support, and electrical-building HVAC interactions are recurring construction risks called out by the DBM and should be reflected in walkdown checklists rather than treated as design questions.
- Foundation and anchorage execution must follow the accepted civil/structural design package, which depends on the final geotechnical report (DBM treats geotechnical values as design placeholders until that report is accepted).
- Cold-climate exposure (-40 °C design basis) affects rigging, grouting, sealants, and pre-energization testing seasons; the workface plan should sequence weather-sensitive activities accordingly.

## Trade-offs

- **Sequencing tie-ins:** Energizing MV before grounding, segregation, and communication checks complete creates safety and protection-coordination risk; the CWP should bias toward complete hold-point sign-off before energization rather than parallel commissioning of incomplete scope.
- **Outdoor vs. indoor location:** TBD pending detailed design. Outdoor placement reduces electrical-building footprint and HVAC load but increases enclosure rating, heat tracing, and weather-sealing scope.
- **Workface plan granularity:** Higher granularity (per-cable, per-anchor) increases CWP authoring effort but reduces field RFI volume; recommended granularity is set by detailed design completeness.

## Examples

The accessible source set contains no PKG-017-specific construction example. Source-grounded analogs:

- 4160V MCC contactor and protection-relay tie-ins for KM-2150/KM-2250 illustrate the MV tie-in pattern (source: 4160V MCC paragraph).
- Compressor package modules disassembled into three pieces for transportation and field installation in self-framing buildings (source: line 294) illustrate a module-delivery and field-reassembly pattern that may or may not apply to PKG-017; allocation TBD.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-017-03-001 | Package title asserts "MV VFD - 600HP, 4160V" but accessible DBM source describes 4160 V starting VFDs only for the 5,200 hp / 4,000 V inlet compressor motors KM-2150 and KM-2250; no 600 HP MV motor or VFD load is identified in PKG-017-accessible source slices. | Workbook Packages row 19 / `PACKAGE_REGISTER.csv` row `PKG-017` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 326, 752-756 | Datasheet "600 HP motor service basis"; Specification REQ-017-03-005; Procedure prerequisites | PROPOSAL: treat "600HP" as title/identity only and carry driven-machine identity, MCC bus assignment, and feeder/protection basis as `TBD` until vendor data or detailed electrical study allocates PKG-017 to a specific 600 HP load. | TBD |
| HRR-017-03-002 | Source contains no PKG-017-specific installation location, foundation, cooling, or area classification data. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings paragraph | `26020-Package_Requirements.docx` (no PKG-017 match in accessible slice) | Datasheet "Installation location", "Foundations/anchorage", "Cooling/HVAC"; Specification REQ-017-03-009/010; Procedure steps | PROPOSAL: keep these as `TBD` and require detailed-design issuance before the CWP is taken to issue-for-construction. | TBD |
| HRR-017-03-003 | No `Dependencies.csv` has been generated; declared upstream/downstream lists for DEL-017-03 are empty although DEL-017-01 (Scope of Work) and DEL-017-02 (Package Datasheet) are logical upstream sources of construction requirements. | `_DEPENDENCIES.md` | `DELIVERABLE_REGISTER.csv` rows DEL-017-01, DEL-017-02 | Procedure prerequisites; coordination notes | PROPOSAL: when dependencies are declared, list DEL-017-01 and DEL-017-02 as upstream and the vendor package (DEL-017-04) and EPC review (DEL-017-06) as adjacent for review. | TBD |
