# Specification — Vendor Document Turnover Package (DEL-057-05)

> Normative view. Requirements are derived from accessible source slices in `_Sources/26020-Package_Requirements.docx` (Inlet Stabilizers section). Inferences are labeled **ASSUMPTION**. Where the source slice is silent, items are marked **TBD**.

## Scope

### In Scope
- Compilation, control, submittal, and final turnover to EPC Integrator of the vendor documentation enumerated in the Vendor Engineering Deliverables table for the Inlet Stabilizers package (`26020-01-PT-17-005`).
- The vendor document register (PRQ-009 — Vendor Document Index) used to schedule, track, and report status of every required vendor document for the three (3) Inlet Stabilizer Packages.
- Vendor document submittals at the lifecycle milestones agreed with EPC Integrator (lifecycle milestone names: **TBD** — not stated in accessible source slice).
- Final turnover records consolidated in PRQ-016 (Vendor Data Book / Final Supplier Documentation) and MEC-023 (Vendor Data Book / Mechanical Final Documentation).
- Quality records bound to the package: QLT-003 (ITP), QLT-013 (MTRs/Certificates), QLT-020 (Inspection Release Certificate), QLT-021 (Manufacturing Record Book).

### Out of Scope
- Authoring of the underlying engineering content (covered by sibling deliverables DEL-057-02 Package Datasheet, DEL-057-03 Construction Work Package, DEL-057-04 Vendor Engineered Equipment Package).
- EPC Integrator acceptance decisions (covered by sibling deliverable DEL-057-06 EPC Vendor Package Review and Acceptance).
- Site-installation as-built generation by the EPC (`PIP-028` produced by vendor for vendor-supplied piping only).

## Requirements

| ID | Requirement | Source / Basis |
|---|---|---|
| REQ-VDT-01 | The Package Vendor shall maintain a Vendor Document Index (PRQ-009) listing every required document by ID and title for the three (3) Inlet Stabilizer Packages. | 26020-Package_Requirements.docx, Inlet Stabilizers > Vendor Engineering Deliverables > Core vendor documents (PRQ-009). |
| REQ-VDT-02 | The Package Vendor shall execute document control in accordance with DOC-008 (Vendor Document Control Procedure). | 26020-Package_Requirements.docx, Inlet Stabilizers > Core vendor documents (DOC-008). |
| REQ-VDT-03 | The Package Vendor shall submit, for EPC Integrator review, every document category enumerated in the Inlet Stabilizers Vendor Engineering Deliverables table (categories listed in `Datasheet.md` § Construction). | 26020-Package_Requirements.docx, Inlet Stabilizers > Vendor Engineering Deliverables. |
| REQ-VDT-04 | The Package Vendor shall compile and deliver, at turnover, PRQ-016 (Vendor Data Book / Final Supplier Documentation) and MEC-023 (Vendor Data Book / Mechanical Final Documentation), containing the as-shipped/as-built vendor record set. | 26020-Package_Requirements.docx, Inlet Stabilizers > PRQ-016, MEC-023. |
| REQ-VDT-05 | The Package Vendor shall deliver quality records bound to the package: QLT-003, QLT-013, QLT-020, QLT-021. | 26020-Package_Requirements.docx, Inlet Stabilizers > Core vendor documents. |
| REQ-VDT-06 | The Package Vendor shall deliver SPIR (PRQ-015) and Logistics/Shipping Plan (PRQ-013). | 26020-Package_Requirements.docx, Inlet Stabilizers > Core vendor documents. |
| REQ-VDT-07 | Submittal lifecycle (IFR / IFA / IFC / As-Built or equivalent) shall follow the project document control procedure. **ASSUMPTION** — exact lifecycle names not in accessible source slice (`location TBD`). | ASSUMPTION (industry-typical mechanical package practice). |
| REQ-VDT-08 | Document numbering shall conform to the project's vendor document numbering convention. **TBD** — convention not in accessible source slice. | TBD (`location TBD`). |
| REQ-VDT-09 | Native (editable) file formats shall be provided where the project requires them. **TBD** — list not in accessible source slice. | TBD. |
| REQ-VDT-10 | EPC Integrator shall review the submitted vendor documentation; acceptance is performed under DEL-057-06 (EPC Vendor Package Review and Acceptance). | `_CONTEXT.md` (ResponsibleParty); package decomposition. |

## Standards

| Standard / Procedure | Applicability | Location |
|---|---|---|
| DOC-008 — Vendor Document Control Procedure (project) | Governs the document control activity for this deliverable. | location TBD (referenced by ID in 26020-Package_Requirements.docx; full procedure text not co-located in accessible sources). |
| PRQ-009 — Vendor Document Index (project template) | Format/template for the vendor document register. | location TBD. |
| Pressure Equipment Registration (REG-022) jurisdictional code | Applicable because Inlet Stabilizers contain trayed reboiled distillation columns and the Vendor Engineering Deliverables table lists REG-022 (Pressure Equipment Registration Package). Jurisdictional code = TBD. | 26020-Package_Requirements.docx, Inlet Stabilizers > Static pressure equipment; jurisdictional clause `location TBD`. |
| Industry codes (ASME, API, IEC, NFPA, etc.) | ASSUMPTION — typical for stabilizer packages, not enumerated in accessible source slice. | ASSUMPTION. |

## Verification

| Requirement | Verification Approach |
|---|---|
| REQ-VDT-01 | Receipt and review of PRQ-009 by EPC Integrator at submittal milestones; cross-check against the category table reproduced in `Datasheet.md` § Construction. |
| REQ-VDT-02 | Audit of vendor's document control activity against DOC-008 (procedure walkdown). |
| REQ-VDT-03 | Per-category submittal log; transmittal review by EPC Integrator. |
| REQ-VDT-04 | Vendor Data Book completeness review at turnover; documented under DEL-057-06. |
| REQ-VDT-05 | Quality records reviewed by EPC Integrator QA/QC against QLT IDs listed. |
| REQ-VDT-06 | Receipt of PRQ-013, PRQ-015 prior to shipment / commissioning gates (gates **TBD**). |
| REQ-VDT-07–09 | TBD — pending project document-control procedure access. |
| REQ-VDT-10 | Acceptance evidenced by DEL-057-06 records. |

## Documentation

Required artifacts (anticipated, per `_CONTEXT.md`):

- Vendor document register (instance of PRQ-009 scoped to PKG-057).
- Vendor document submittal transmittals (per category, per revision).
- Source vendor document table rows captured as artifacts where available (i.e., the entries from the Inlet Stabilizers Vendor Engineering Deliverables table).
- Turnover records: PRQ-016, MEC-023, and all bound quality records (QLT-003, QLT-013, QLT-020, QLT-021).
