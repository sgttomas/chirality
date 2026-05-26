# Guidance — DEL-079-01 Scope of Work: Instrument Air Building (PKG-079)

## Purpose

This Scope of Work is the EPC Integrator's anchor deliverable for the PKG-079 Instrument Air Building. It establishes what the EPC is responsible for, what the Package Vendor is responsible for, and which scope items, interfaces, and design conditions must propagate to all downstream PKG-079 deliverables (Datasheet, Construction Work Package, Vendor Engineered Equipment Package, Vendor Document Turnover, EPC Vendor Package Review and Acceptance). (Source: _CONTEXT.md; DELIVERABLE_REGISTER.csv PKG-079; PACKAGE_REGISTER.csv responsibility model.)

It exists to satisfy Gate 5 EPC-anchor requirements identified in the decomposition: every Mechanical vendor package needs a vendor/EPC responsibility split, a tagged equipment basis, and an integration interface set carried forward as authoritative EPC content. (Source: OBJ-004; DELIVERABLE_REGISTER.csv notes "Mandatory Gate 5 EPC anchor deliverable".)

## Principles

1. **Vendor owns the package; EPC owns the facility integration.** This split is non-negotiable per OBJ-004 and the PACKAGE_REGISTER.csv responsibility-model cell. The EPC Scope of Work must never absorb vendor package design or vendor documentation authorship, and it must never delegate facility-side integration back to the vendor.
2. **The Word package heading 32 (Basic scope / Major included equipment / Scope notes) is the source of truth for equipment count, ratings, and design conditions.** Workbook row 69 is the structural source of truth for package identity, tag, discipline, WBS, and the ten declared interface types. Where these disagree, the document slice and workbook row are co-equal — only the human may rule on conflicts. (Source: SOW-0131..0134; PACKAGE_REGISTER.csv; INTERFACE_REGISTER.csv.)
3. **Vendor sizing is allowed; vendor invention is not.** Where the source explicitly defers a parameter to the vendor (e.g., wet air receiver, pre-filter, dryer, dry air receiver sizing; speed), this Scope of Work carries the TBD forward rather than fabricating a value. (Source: SOW-0132; SOW-0133; SOW-0134.)
4. **Interfaces are obligations, not labels.** Each of the ten declared interface types (Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports) must be carried into Package Datasheet evidence and into the Construction Work Package as a tie-in scope assignment. (Source: INTERFACE_REGISTER.csv PKG-079 rows.)

## Considerations

- **"By Others" assignments are EPC scope assignments, not vendor escapes.** Shipping, piles, tie-in piping, electrical connections, and mounting platform/stairs are stated "By Others" in SOW-0134; the EPC integration scope must explicitly absorb each of these as an integration responsibility, with discipline assignment confirmed in the Construction Work Package (DEL-079-03).
- **Air quality and pressure relationships are coupled.** The -73.3 °C dewpoint is stated at 1000 kPag (compressor max discharge / shutdown), the 1113 SCFM rating is at 861 kPag (compressor rated discharge), and PSVs sit at 948 kPag — between rated discharge and max design (1034 kPag). When carrying these forward to the Package Datasheet, preserve the pressure datum each value is tied to. (Source: SOW-0133; SOW-0134.)
- **The dryer "sized for 2 compressors and leave" phrasing is a sizing margin statement, not a redundancy claim.** Do not promote this to an N+1 redundancy requirement in downstream deliverables; record as ASSUMPTION pending vendor confirmation if the operational philosophy needs it. (Source: SOW-0133.)
- **Non-classified motor designation.** The motor "non-classified" wording in SOW-0134 implies the package will sit in an unclassified electrical area; if the facility area classification document later assigns a classified area to the Instrument Air Building location, this becomes a CONFLICT for human ruling. The area classification source slice was not re-read in this pass.
- **Objective coverage is broad and best-effort.** This deliverable is mapped to OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 by the package-grouping heuristic (per skill Step 1.3). Treat these as directional context, not as additional binding requirements. The strongest objective ties are OBJ-004 (vendor/EPC split) and OBJ-007 (instrument air as a shared utility/support system). (Source: OBJECTIVE_REGISTER.csv.)

## Trade-offs

- **One 100% dryer vs. multiple smaller dryers.** Source specifies one regenerative desiccant air dryer at 100% capacity with two towers. This trades capital and footprint efficiency for the operational sensitivity of a single dryer asset; mitigated by the two-tower regenerative design and the dryer sizing margin. (Source: SOW-0132; SOW-0133. Rationale beyond source is ASSUMPTION.)
- **One dry air receiver vs. two at 50%.** Source explicitly permits either configuration. The choice trades single-vessel inventory and footprint for sectionalized maintenance ability; vendor proposal will dictate. (Source: SOW-0132.)
- **Soft starter vs. VFD on compressor motors.** Source states "soft starter or VFD ready"; either is acceptable. Selection will depend on electrical infrastructure (OBJ-005) and operational turndown philosophy; final choice belongs to the Package Vendor's package design (DEL-079-04) with EPC integration review. (Source: SOW-0133.)

## Examples

- A subordinate Package Datasheet (DEL-079-02) entry for "PSV set pressure" should cite this Scope of Work R4.1 and SOW-0133, value 948 kPag (137.5 psig), with no alteration.
- A Construction Work Package tie-in line item for "electrical connections to compressor 1 and compressor 2" should cite Scope of Work R9 and SOW-0134 ("By Others — electrical connections") and assign to the Electrical discipline scope.
- An EPC Vendor Package Review and Acceptance checklist item should verify each of the ten interface obligations (R8) has an interface evidence artifact, citing INTERFACE_REGISTER.csv IFC-* IDs.

## Conflict Table (for human ruling)

No unresolved cross-document conflicts identified within the drafted four-document kit at the end of Pass 2. Numeric values, equipment counts, and the responsibility split are consistent across Datasheet, Specification, Guidance, and Procedure. Items requiring human ruling (e.g., the area-classification check noted above, the dryer redundancy framing, and the standards/codes slice not yet re-read) are tracked as TBD/ASSUMPTION in the respective documents and are candidates for Pass 3 lensing.
