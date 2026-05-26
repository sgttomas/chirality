# Guidance — Vendor Document Turnover Package (DEL-057-05)

> Directional view. Rationale, considerations, and trade-offs for executing the vendor document turnover for the Stabilizers package (`PKG-057`, source heading `26020-01-PT-17-005 - Inlet Stabilizers`).

## Purpose

The Vendor Document Turnover Package exists so the EPC Integrator receives a complete, controlled, and verifiable set of vendor documentation for the three (3) Inlet Stabilizer Packages. It is the contractual evidence trail that the package was engineered, manufactured, inspected, tested, and shipped consistent with the project's Vendor Engineering Deliverables list, and it is the substrate over which DEL-057-06 (EPC Vendor Package Review and Acceptance) makes the acceptance decision.

## Principles

- **Single index, many submittals.** The Vendor Document Index (PRQ-009) is the canonical register; everything submitted should be traceable to a row in it. (Source: 26020-Package_Requirements.docx, Inlet Stabilizers > Core vendor documents.)
- **Control procedure precedes content.** DOC-008 (Vendor Document Control Procedure) defines how revisions, statuses, and transmittals are handled; following it is what makes the turnover auditable rather than a file dump.
- **The data book is the durable artifact.** PRQ-016 and MEC-023 (Vendor Data Books) are what the owner-operator retains long-term; they should be assembled progressively, not at the end.
- **Quality records are vendor-owned, EPC-reviewed.** QLT-003, QLT-013, QLT-020, QLT-021 are produced and signed by the vendor (and their NDE/inspection chain); EPC Integrator reviews completeness and conformance, but does not author them.
- **Source vendor document rows are evidence, not deliverables.** Per `_CONTEXT.md` Notes, individual rows in the Vendor Engineering Deliverables table are artifacts; the deliverable is the controlled set, not each row.

## Considerations

- **Three identical packages, one document set?** The source identifies three (3) Inlet Stabilizer Packages. ASSUMPTION: the vendor will issue per-package serialized records (FAT reports, MTRs, IRC, MRB) and shared engineering documents (design basis, P&IDs, general arrangements). The submittal cadence should make the per-package vs. shared split explicit; treat as **TBD** until confirmed with the vendor.
- **Lifecycle naming.** IFR/IFA/IFC/As-Built (or equivalent) is industry-typical but is not in the accessible source slice for Inlet Stabilizers. Confirm with project document control before issuing the first submittal.
- **Native files.** Whether DWG/DGN/native CAD, native P&ID exports, native instrument index spreadsheets, etc. must be delivered is **TBD** — confirm with project document control.
- **Pressure equipment registration scope.** REG-022 is listed in Inlet Stabilizers > Static pressure equipment, but the jurisdictional code (ASME, CRN, PED, etc.) is not in the accessible slice — confirm before manufacturing release of the trayed columns.
- **Interface with DEL-057-06.** The acceptance evidence DEL-057-06 produces should reference the PRQ-009 row IDs from this deliverable; align the column scheme early.
- **Interface with DEL-057-04 (Vendor Engineered Equipment Package).** DEL-057-04 owns the engineered content; this deliverable owns the *control* over its movement and final compilation. Do not duplicate authoring scope.

## Trade-offs

- **Progressive Data Book vs. final-only compilation.** Progressive assembly is more administrative work for the vendor but reduces end-of-project schedule risk. Final-only compilation is simpler day-to-day but creates a single large risk at turnover. ASSUMPTION: progressive assembly is preferred for a three-package supply; confirm with project.
- **Strict native-format policy vs. PDF-only.** Strict native policy improves long-term maintainability for the owner-operator but raises vendor IP and licensing concerns. Project-level policy applies; do not over- or under-promise unilaterally.
- **Per-category transmittals vs. consolidated transmittals.** Per-category is easier to review and easier to register-update; consolidated reduces transmittal count. Default to per-category aligned with the section banners in the Vendor Engineering Deliverables table.

## Examples

- *Register snapshot row (illustrative):* `PRQ-009 | DOC-008 | rev B | IFA | submitted 2026-MM-DD | EPC review by 2026-MM-DD | status Open` — exact lifecycle codes **TBD** pending project document-control procedure.
- *Turnover Data Book table of contents (illustrative):* Tab 1 — Index (PRQ-009); Tab 2 — Quality records (QLT-003, QLT-013, QLT-020, QLT-021); Tab 3 — Engineering (MEC-001..025); Tab 4 — Static pressure (MEC-005, MEC-009, REG-022); Tab 5 — Relief/Flare/Vent; Tab 6 — Piping; Tab 7 — Electrical/EHT/Grounding; Tab 8 — I&C; Tab 9 — Fire & Gas; Tab 10 — Structural; Tab 11 — Spares/Tools (MEC-024) and SPIR (PRQ-015); Tab 12 — Logistics (PRQ-013).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| C-01 | Submittal lifecycle code names (IFR/IFA/IFC/As-Built) are industry-typical but not present in the accessible Inlet Stabilizers source slice. | 26020-Package_Requirements.docx (silent in Inlet Stabilizers section) | Industry convention | Specification REQ-VDT-07, Guidance § Considerations | Adopt project document-control procedure when accessible. | TBD |
| C-02 | Whether per-package vs. shared documents are issued separately for the three (3) Inlet Stabilizer Packages. | 26020-Package_Requirements.docx (basic scope: 3 packages) | No source guidance on shared vs. per-package issue | Datasheet, Specification, Procedure | Per-package serialized records for QA records; shared for engineering. | TBD |
| C-03 | REG-022 jurisdictional code not stated. | 26020-Package_Requirements.docx (lists REG-022 only by ID) | No jurisdictional code source in accessible slice | Specification § Standards | Confirm with project regulatory lead. | TBD |
