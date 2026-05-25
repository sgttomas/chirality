# Guidance — DEL-033-05 Vendor Document Turnover Package (PKG-033)

## Purpose

This guidance frames how the Vendor Document Turnover Package is to be assembled, interpreted, and reviewed for PKG-033 (4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)). It supports `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` by ensuring the EPC Integrator receives a complete, traceable vendor documentation set sufficient for facility integration, operations, energization, and regulatory readiness.

## Principles

1. **Source-driven document list.** The applicable document classes come from `_Sources/26020-Package_Requirements.docx` "Vendor Engineering Deliverables". This skill does not invent new document classes for the PKG-033 turnover.
2. **Discipline filtering, not document invention.** The vendor and EPC reviewer apply the source's discipline tables to mark each line APPLICABLE / N/A with a brief rationale, rather than removing or re-inventing IDs.
3. **EPC Integrator as acceptor, not author.** Per `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`, the Package Vendor authors; the EPC Integrator reviews via `DEL-033-06`. Acceptance is a human decision.
4. **Traceability over volume.** The Vendor Document Index (`PRQ-009`) is the canonical contents list; every document submitted must appear in it with current revision and status. Volume alone is not acceptance.
5. **Codes and standards stay sourced.** Where the accessible source set does not cite a specific standard clause, the turnover set states the applicable standard and leaves clause-level claims to detailed-design documents.

## Considerations

- **Switchgear + building discipline center.** The package is identified Electrical (`PACKAGE_REGISTER.csv` PKG-033 row), WBS 02. Electrical and I&C document classes dominate the applicable list; mechanical applies as packaged-equipment handling for the building enclosure, integral HVAC, fire/gas, and lifting/transport.
- **Building services scope split.** DBM SEC-11 (line 766) requires electrical buildings to house "MCCs, switchgear, distribution equipment, and associated HVAC/ventilation systems" with area classification, ventilation, and remote distribution coordination. The vendor scope-of-supply for HVAC, fire/gas detection, building heaters, and lighting must be confirmed; whichever lines are vendor-supplied generate turnover documentation here, the remainder remain EPC Integrator scope.
- **Pressure / piping minimal.** Pressure-equipment and piping document classes are presumed N/A. Always record rationale on the Index.
- **Interface basis.** Per `PACKAGE_REGISTER.csv` PKG-033 row, applicable interface types include Utility Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports. Vendor documents must cover each interface where it is vendor-supplied; remaining interfaces are EPC Integrator-managed.
- **Turnover gate.** Turnover records (`PRQ-016`, `MEC-023`, `ELE-030`, `QLT-020`, `QLT-021`) are the critical evidence for `DEL-033-06` acceptance. Plan the FAT/SAT/energization milestones backwards from the EPC Integrator's acceptance gate; the 4160V switchgear must be energization-ready before downstream 4160V loads (per DBM SEC-12) can be commissioned.

## Trade-offs

- **Breadth vs. signal.** A wide vendor document set is more defensible at regulatory and operational reviews, but increases review cost and submittal turnaround. Use the discipline applicability call to keep the set tight while preserving traceability.
- **Early submittal vs. as-built quality.** Releasing documents early gives the EPC Integrator time to coordinate facility-level integration (especially feeder routing, grounding, and PCN interfaces) but creates revisioning churn. The Vendor Document Control Procedure (`DOC-008`) should establish a small number of named milestones (e.g., preliminary, certified-for-construction, as-built) rather than continuous trickle.
- **Standalone vendor IOM vs. integrated turnover book.** A combined `PRQ-016` book is easier for operations to use long-term; per-document standalone files are easier for vendor revisioning. Decide upfront and reflect in `DOC-008`.
- **Building integral vs. EPC-supplied services.** Routing HVAC, fire/gas, and lighting through the switchgear vendor simplifies turnover and warranty for the building, but reduces the EPC Integrator's flexibility to standardize across multiple electrical buildings on site. Confirm the split-of-supply in the package PO before fixing the Vendor Document Index baseline.

## Examples

- The source's Acid Gas Compressor section illustrates how the same template is instantiated for a different physical package, with the same core vendor documents and discipline applicability table; the PKG-033 instantiation follows the same shape with switchgear/electrical-building discipline filtering.
- DBM line 617 explicitly enumerates "vendor document registers" among the required package deliverables, validating that the turnover deliverable is a first-class facility-design expectation, not a vendor optionality.
- DBM SEC-12 (lines 752-756) describes the 4160V MCC PCN/EtherNet interface to the plant PLC; the 4160V switchgear analogously requires protection-relay communications (e.g., to historian, alarm/event) documented in the I&C turnover set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-033-05-001 | Package name says "4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)" but accessible DBM SEC-12 detail is concentrated on the 4160V MCC serving inlet compressors KM-2150 / KM-2250 (lines 752-756). Whether the (830-2) 4160V switchgear is a distinct upstream switchgear feeding the 4160V MCC, or another 4160V distribution element, is not unambiguously stated in the accessible source. | `PACKAGE_REGISTER.csv` PKG-033 row (package name and workbook tag `26020-02-30-024`) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 730-756 (system voltages, incoming power, 4160V MCC description) | Datasheet Identification/Construction; Specification R-4, R-5 | Treat the "4160V Switchgear Electrical Building (830-2)" as the upstream MV distribution lineup at the 4,160 V system level per DBM line 733 (`Medium-voltage service 4,160 V`); do not assert load-list or feeder-count facts until detailed-design source slice is accepted. | TBD |
| HRR-033-05-002 | The accessible sources do not specify switchgear-governing standards (IEEE C37, IEEE C57, CSA Z462 / IEEE 1584 arc-flash) or define submittal cadence and native-file formats. | `_Sources/26020-Package_Requirements.docx` (no switchgear-specific clause cited) | None | Specification R-11, R-12; Standards table | Carry as TBD in the turnover specification; require the EPC Integrator to set these in the package PO or in `DEL-033-06` review criteria before vendor mobilization. | TBD |
| HRR-033-05-003 | The "Vendor Engineering Deliverables" list in the source covers all package types uniformly; per-line applicability for a 4160V switchgear in an electrical building (vs. a process compressor) requires human disposition, particularly for building-HVAC, fire/gas, lighting, and civil/foundation lines whose vendor-vs-EPC split is not stated in the accessible source. | `_Sources/26020-Package_Requirements.docx` (uniform template) | Package-specific reality of an MV switchgear electrical building (pressure/piping/process expected N/A; building services depend on split-of-supply) | Specification R-4, R-5, R-6 | The Vendor Document Index for PKG-033 marks pressure-equipment, piping, and process discipline lines as N/A with rationale; building/HVAC/fire-gas/civil lines are marked APPLICABLE or N/A based on the package PO split-of-supply, with rationale recorded. | TBD |
