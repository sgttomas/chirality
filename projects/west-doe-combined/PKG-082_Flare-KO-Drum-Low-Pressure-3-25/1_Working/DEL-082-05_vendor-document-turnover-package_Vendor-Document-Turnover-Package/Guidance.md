# Guidance — DEL-082-05 Vendor Document Turnover Package

## Purpose

This deliverable assembles the controlled vendor document set that travels with the LP Flare KO Drum package from kickoff through engineering, fabrication, FAT, shipment, site installation, and turnover. It exists so the EPC Integrator and Owner receive a single, traceable, version-controlled body of evidence sufficient to:

- accept the physical equipment package (`DEL-082-04`) at the package boundary,
- demonstrate regulatory and code compliance for the pressure vessel `V-3900-2` (`REG-022`),
- support EPC Integrator review and acceptance (`DEL-082-06`), and
- enable safe operation, maintenance, and future modification.

The deliverable also covers the four scope items declared in `_CONTEXT.md`: `SOW-0079`, `SOW-0080`, `SOW-0081`, `SOW-0082`.

## Principles

1. **One register, many artifacts.** Per `_CONTEXT.md` Notes and the DELIVERABLE_REGISTER row, individual source document rows remain artifacts/evidence inside this single deliverable; they are not promoted to separate deliverables. The Vendor Document Index (`PRQ-009`) is the canonical register; everything else is a row beneath it.
2. **Source-anchored completeness.** The source-enumerated list in `26020-Package_Requirements.docx §26020-02-PT-17-002` is the floor for required submittals. Vendor may add documents; vendor may not silently omit listed documents.
3. **Boundary discipline.** Source explicitly excludes the LP flare stack and places the package boundary at the KO drum outlet flange. Submittals must consistently reflect this boundary; ambiguity here propagates downstream into tie-in errors.
4. **TBD over invention.** Where source defers detail (blowdown valve details; full interface spreadsheet contents), surface the gap as `TBD` in the relevant submittals rather than filling with assumption.
5. **Review-feeds-acceptance.** Every EPC review action on a submittal here produces evidence consumed by `DEL-082-06`. Treat review records as deliverable output, not byproduct.

## Considerations

- **Two-party authoring with split review.** Package Vendor authors content; EPC Integrator reviews for interface/integration consistency. The vendor's internal QA review does not substitute for EPC interface review.
- **Pressure equipment registration timing.** `REG-022` is jurisdictionally gated; its lead time often drives the critical path for vessel acceptance. Start early.
- **Rotating equipment scope addition.** The package includes a transfer pump (`P-3900-2`) in addition to the vessel. This drags rotating-equipment, motor-starting, NPSH, and seal documents (MEC-004/007/019, PRO-013, ELE-011) into the otherwise vessel-centric submittal set. Do not omit on the basis of "it's just a KO drum."
- **Slop tank transfer and truck-out provision.** Major Included Equipment lists slop tank liquid transfer and truck-out provision. Drainage/containment interfaces (PRO-023, CIV-014) and procedure for truck-out should be reflected in P&ID and operating narrative, not only in the equipment list.
- **Interface spreadsheet not yet parsed.** Detailed interface row content from `26020-Packages_Interfaces_4_export.xlsx` is not in the locally accessible textual source slice. Interface coverage statements below the document-type level are `TBD` pending that source.

## Trade-offs

| Trade-off | Discussion |
|---|---|
| Early partial submittals vs. consolidated turnover book | Early partial submittals (e.g., MEC-001 Mechanical Design Basis, PRO-008 P&IDs) enable EPC interface review during design; deferring to a consolidated Vendor Data Book (`QLT-021`/`MEC-023`) compresses schedule risk into the back end and is discouraged. |
| Vendor's standard document set vs. project-enumerated set | When the vendor's standard documentation set differs from the source-enumerated list, the source list governs; the vendor may submit equivalents but must map equivalents in the Vendor Document Index. |
| Treating individual source rows as artifacts vs. deliverables | Per `_CONTEXT.md` Notes, rows are artifacts. Promoting them to deliverables would fragment ownership and break the single-vendor accountability for the turnover package. |

## Examples

The source enumeration provides a worked example of the required structure: see `26020-Package_Requirements.docx §26020-02-PT-17-002 Vendor Engineering Deliverables`, which groups artifacts under "Core vendor documents", "Core package engineering", "Rotating equipment / pumps", "Static pressure equipment", "Relief / flare / vent design", "Process piping interfaces", "Drainage / containment interfaces", "Electrical, lighting, EHT, grounding", "Instrumentation and controls interfaces", and "Structural, foundations, supports, access". The Vendor Document Index should preserve this grouping.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none open) | No conflicts identified in this pass. Sources used (deliverable-local metadata and the package source slice) are consistent. | — | — | — | — | TBD |
