# Guidance — DEL-019-05 Vendor Document Turnover Package (PKG-019)

## Purpose

This guidance frames how the Vendor Document Turnover Package is to be assembled, interpreted, and reviewed for PKG-019 (MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD). It supports `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` by ensuring the EPC Integrator receives a complete, traceable vendor documentation set sufficient for facility integration, operations, and regulatory readiness.

## Principles

1. **Source-driven document list.** The applicable document classes come from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables". This skill does not invent new document classes for the PKG-019 turnover.
2. **Discipline filtering, not document invention.** The vendor and EPC reviewer apply the source's discipline tables to mark each line APPLICABLE / N/A with a brief rationale, rather than removing or re-inventing IDs.
3. **EPC Integrator as acceptor, not author.** Per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row 100, the Package Vendor authors; the EPC Integrator reviews via `DEL-019-06`. Acceptance is a human decision.
4. **Traceability over volume.** The Vendor Document Index (`PRQ-009`) is the canonical contents list; every document submitted must appear in it with current revision and status. Volume alone is not acceptance.
5. **Codes and standards stay sourced.** Where the accessible source set does not cite a specific standard clause, the turnover set states the applicable standard and leaves clause-level claims to detailed-design documents.

## Considerations

- **MV VFD discipline center.** The package is identified Electrical (`PACKAGE_REGISTER.csv` row 21), WBS 02. Electrical and I&C document classes dominate the applicable list; mechanical applies as packaged-equipment handling (skid, enclosure, lifting, IOM).
- **Pressure / piping / civil minimal.** Unless detailed design surfaces cooling-water piping, oil cooling, or integral civil scope, pressure-equipment, piping, drainage, and civil document classes are presumed N/A. Always record rationale.
- **Interface basis.** Per `PACKAGE_REGISTER.csv` row 21, applicable interface types include Electrical Power; Grounding/Bonding; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports. Vendor documents must cover each of these interfaces somewhere in the turnover set.
- **Turnover gate.** Turnover records (`PRQ-016`, `MEC-023`, `ELE-030`, `QLT-020`, `QLT-021`) are the critical evidence for `DEL-019-06` acceptance. Plan the FAT/SAT/energization milestones backwards from the EPC Integrator's acceptance gate.

## Trade-offs

- **Breadth vs. signal.** A wide vendor document set is more defensible at regulatory and operational reviews, but increases review cost and submittal turnaround. Use the discipline applicability call to keep the set tight while preserving traceability.
- **Early submittal vs. as-built quality.** Releasing documents early gives the EPC Integrator time to coordinate facility-level integration but creates revisioning churn. The Vendor Document Control Procedure (`DOC-008`) should establish a small number of named milestones (e.g., preliminary, certified-for-construction, as-built) rather than continuous trickle.
- **Standalone vendor IOM vs. integrated turnover book.** A combined `PRQ-016` book is easier for operations to use long-term; per-document standalone files are easier for vendor revisioning. Decide upfront and reflect in `DOC-008`.

## Examples

- The source's Acid Gas Compressor section illustrates how the same template is instantiated for a different physical package, with the same core vendor documents and discipline applicability table; the PKG-019 instantiation follows the same shape with VFD-appropriate discipline filtering.
- DBM line 617 explicitly enumerates "vendor document registers" among the required package deliverables, validating that the turnover deliverable is a first-class facility-design expectation, not a vendor optionality.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-019-05-001 | Package title says "5000HP, 4160V" VFD, but DBM compressor basis cites 4,000 V motors at 5,200 hp (DBM line 324) and 600V/4160V/6900V tiers in the package requirements. The accessible source set does not contain a 5000HP/4160V data row that exactly matches the package name. | `PACKAGE_REGISTER.csv` row 21 (package name "5000HP, 4160V") | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 533 (4,000 V / 5,200 hp inlet compressor motors with starting VFD) | Datasheet Identification; Specification standards/applicability | Treat "5000HP / 4160V" as package title/identity nominal; record motor and VFD rating from the as-built electrical detailed design when issued; do not assert specific voltage/horsepower on derived turnover documents until detailed-design source slice is accepted. | TBD |
| HRR-019-05-002 | The accessible sources do not specify VFD-governing standards (IEEE 519, NEMA ICS 7, IEC 61800 series) or define submittal cadence and native-file formats. | `_Sources/26020-Package_Requirements.docx` (no VFD-specific clause cited) | None | Specification R-11, R-12; Standards table | Carry as TBD in the turnover specification; require the EPC Integrator to set these in the package PO or in `DEL-019-06` review criteria before vendor mobilization. | TBD |
| HRR-019-05-003 | The "Vendor Engineering Deliverables" list in the source covers all package types uniformly; per-line applicability for an MV VFD (vs. a compressor) requires human disposition. | `_Sources/26020-Package_Requirements.docx` (uniform template) | Package-specific reality of an MV VFD (no piping, no pressure vessels expected) | Specification R-4, R-5, R-6 | The Vendor Document Index for PKG-019 marks pressure-equipment, piping, civil/foundation, drainage, and process discipline lines as N/A with rationale unless cooling/oil/civil scope surfaces during detailed design. | TBD |
