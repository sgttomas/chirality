# Guidance: DEL-089-03 — Construction Work Package

> **Document role:** Directional — explains why this deliverable exists, the principles and considerations that should shape it, the trade-offs the author must navigate, and the open conflicts that require human ruling before the CWP is issued for construction.

## Purpose

The Construction Work Package (CWP) for PKG-089 *Pig Receivers (Inlet) 3-25* is the EPC Integrator's authoritative description of how the vendor-supplied pig receiver package will be physically installed, built, inspected, turned over, and tied into the larger facility. It sits between the Package Vendor's engineered equipment (`DEL-089-04`) and operations, and is the Gate 5 EPC anchor for constructability and interface acceptance. [Source: DELIVERABLE_REGISTER.csv row DEL-089-03; PACKAGE_REGISTER.csv row PKG-089]

## Principles

1. **Source-grounded means and methods.** Construction methods, inspection requirements, and acceptance criteria shall trace to accessible standards and source materials (`26020-Package_Requirements.docx` heading 42, the pig receiver RFQ, and the project welding/NDE/pressure-test standards). Where the source is not locally readable, mark **location TBD** rather than invent values. [Authority hierarchy: SKILL.md]
2. **Interface-led structure.** The CWP shall be organized around the package's interface-type list so that nothing in the PACKAGE_REGISTER.csv interface set is silently dropped during execution.
3. **Vendor-EPC boundary respected.** The CWP shall not duplicate or override Package Vendor scope (engineering, design, fabrication, vendor documentation); it shall consume the vendor package and integrate it. [Source: PACKAGE_REGISTER.csv row PKG-089 (Scope/Boundary)]
4. **Sour-service awareness.** All construction provisions (materials, weld procedures, testing, drainage/containment) shall be consistent with sour natural gas service. [Source: DBM line 244]
5. **Turnover as a first-class outcome.** Mechanical completion, punchlist closeout, and operations turnover are core deliverables of this package, not afterthoughts. [Source: DELIVERABLE_REGISTER.csv row DEL-089-03 (Description)]

## Considerations

- **Pig receiver count and size:** The PACKAGE_REGISTER.csv row records two identical 610 mm (24") OD pig receivers, while the locally accessible DBM records a single combined three-phase pig receiver with receiver size TBD. The CWP team must obtain a ruling before mobilization (see Conflict Table). [Sources: PACKAGE_REGISTER.csv row PKG-089; DBM lines 230, 236]
- **Plant inlet boundary handover:** The lease-boundary first-aboveground-flange handover from the Doe field pipeline contractor to the facility fabricator/construction contractor is a contractual and physical interface; the workface plan must clearly identify where the CWP scope starts. [Source: DBM line 228]
- **Inlet ESDV functional integrity:** The full-port, piggable, position-transmitter ESDV is critical to safe operation and pigging; construction shall preserve piggable bore alignment and verify position-transmitter calibration before turnover. [Source: DBM lines 230, 239]
- **Purge/vent/flare tie-ins:** Sweet-gas purge and HP flare vent provisions require careful sequencing with the relief/flare system to enable safe commissioning. [Source: DBM line 238]
- **Operator-managed pigging downstream:** Construction handover must align operator-facing documentation with the DBM expectation that the operator manages pigging and flowback to avoid overrunning downstream stabilization capacity. [Source: DBM line 270]
- **Binary-source dependence:** Several normative inputs (`26020-Package_Requirements.docx` heading 42, the pig receiver RFQ, and the interfaces workbook row 77) are referenced by registers but were not locally readable in this drafting pass; the CWP authors must read those slices and replace TBDs before IFC.

## Trade-offs

- **Single combined receiver vs. two identical receivers.** A single combined receiver simplifies foundations, instrumentation, and tie-ins but couples both inlet trains to one device; two receivers add redundancy, doubled tie-ins, and increased footprint, instrumentation, and turnover complexity. The CWP cannot finalize foundations, tie-in routing, or workface sequencing until this is resolved.
- **Modular vs. stick-built tie-ins.** Skid-mounted package favors modular tie-ins (spool-piece prefabrication) but the inlet pipeline and flare/vent tie-ins may require field-welded stick-built sections; the CWP should weigh schedule against weld/NDE/PWHT logistics for sour service.
- **Hold-point density.** Higher hold-point/witness density improves quality assurance but extends schedule; the CWP should calibrate to risk in sour-service, high-pressure pigging service.

## Examples

- Workface plan ordering example (illustrative; subject to detailed design): foundations → skid set → structural/anchor verification → pipeline tie-in at lease-boundary flange → process piping tie-in to inlet separators → relief/flare/vent and drain tie-ins → electrical/EHT/I&C tie-ins → pressure test → purge/inert → ESDV functional test → mechanical completion → operations turnover.
- Interface checklist example (illustrative): one row per interface type from PACKAGE_REGISTER.csv with columns for tie-in IFC drawing, contractor, completion criteria, witness/hold points, and turnover acceptor.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-089-03-01 | Pig receiver count and size: two identical 610 mm (24") OD pig receivers vs. single combined three-phase pig receiver (size TBD). | PACKAGE_REGISTER.csv row PKG-089 (Process function): "2 identical 610mm (24") OD Pig receivers with ESDV" | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 230, 236: "A single combined three-phase pig receiver … size is TBD" | Datasheet (Attributes), Specification (R-089-03-01, R-089-03-03, R-089-03-07), Guidance (Considerations, Trade-offs), Procedure (Steps) | PROPOSAL: align CWP to the upstream Package Datasheet (DEL-089-02) at IFC; until ruled, treat as HRR and do not finalize foundations or tie-in count. | TBD — requires human ruling |
| CFT-089-03-02 | Inlet separator ESDV shutdown pressure is recorded as 635 psig; delivery-point ESDV shutdown pressure is TBC. CWP test/turnover criteria depend on the resolved pressure basis. | DBM line 230 (635 psig) | DBM line 230 ("delivery-point ESDV shutdown pressure still TBC") | Specification (R-089-03-05, R-089-03-08), Procedure (Verification) | PROPOSAL: defer delivery-point pressure-dependent provisions until DBM update or detailed-design ruling. | TBD — requires human ruling |
| CFT-089-03-03 | Pig receiver design pressure / pressure class is not stated in accessible sources (only inlet separator class 600# and design 4,963 kPag are accessible). | DBM line 253 (separator 600#) | None accessible (binary source `26020-Package_Requirements.docx` heading 42 — location TBD) | Datasheet (Conditions), Specification (R-089-03-08), Procedure (Pressure test) | PROPOSAL: read `26020-Package_Requirements.docx` heading 42 and the pig receiver RFQ to extract the design pressure / class before issuing CWP for construction. | TBD — requires source read + human ruling |
