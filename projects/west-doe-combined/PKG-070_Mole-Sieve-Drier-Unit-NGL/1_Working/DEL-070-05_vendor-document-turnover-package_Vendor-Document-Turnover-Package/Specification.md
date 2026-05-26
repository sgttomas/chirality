# Specification — DEL-070-05 Vendor Document Turnover Package

## Scope

This specification governs the Vendor Document Turnover Package for PKG-070 (Mole Sieve Drier Unit (NGL), tagged 26020-01-PT-22-003). It covers:

- The vendor document register that enumerates every vendor-furnished document required for this package.
- Vendor document submittals (issue, revision, review, and acceptance cycles between Package Vendor and EPC Integrator).
- Source-required vendor documentation listed in 26020-Package_Requirements.docx §Mole Sieve Drier Unit / Vendor Engineering Deliverables.
- Turnover records that close out vendor-furnished documentation at handoff to the EPC Integrator and to operations.

Excluded:
- Vendor-engineered physical equipment design content itself (owned by DEL-070-04). This deliverable carries the documentation register and submittal/turnover wrapper, not the engineering content.
- EPC review and acceptance evidence (owned by DEL-070-06).
- The EPC Scope of Work and Package Datasheet (owned by DEL-070-01 and DEL-070-02).

## Requirements

R-1. The Vendor Document Register SHALL enumerate, at minimum, every vendor document line listed under "Vendor Engineering Deliverables" for 26020-01-PT-22-003 in 26020-Package_Requirements.docx (Mole Sieve heading 24). Source: 26020-Package_Requirements.docx §Mole Sieve / Vendor Engineering Deliverables.

R-2. The Vendor Document Register SHALL include all "Core vendor documents" rows: PRQ-009, DOC-008, QLT-006, QLT-003, QLT-013, QLT-020, QLT-021, PRQ-013, PRQ-015, PRQ-016. Source: same.

R-3. Vendor document control SHALL conform to DOC-008 "Vendor Document Control Procedure" as listed in the source vendor document table. Source: same.

R-4. A Vendor Document Index (PRQ-009) SHALL be issued, maintained, and revised through the project execution lifecycle until handoff. Source: same.

R-5. Final vendor documentation turnover SHALL include the closures PRQ-016 "Vendor Data Book / Final Supplier Documentation" and MEC-023 "Vendor Data Book / Mechanical Final Documentation," and the QLT-021 "Manufacturing Record Book / Vendor Data Book." Source: same.

R-6. Quality-evidence vendor documents SHALL include QLT-006 (Supplier Quality Plan), QLT-003 (Inspection and Test Plan), QLT-013 (Material Test Reports / Certificates), and QLT-020 (Inspection Release Certificate). Source: same.

R-7. Logistics and spares vendor documents SHALL include PRQ-013 (Logistics / Shipping Plan) and PRQ-015 (Spare Parts Interchangeability Record). Source: same.

R-8. Every discipline-specific source-required vendor document listed in the Mole Sieve "Vendor Engineering Deliverables" table SHALL appear in the register with discipline grouping preserved (Core package engineering; Static pressure equipment; Heat transfer equipment; Process package design; Relief/flare/vent design; Process piping interfaces; Drainage/containment interfaces; Electrical/lighting/EHT/grounding; Instrumentation and controls interfaces; Fire and gas / technical safety; Structural/foundations/supports/access). Source: same.

R-9. Each register row SHALL carry a current revision, status (issued/reviewed/accepted/superseded), submittal date, EPC review state, and turnover state. ASSUMPTION: required attributes — minimum needed to support EPC review and turnover closeout; specific attribute names are not enumerated in the accessible source slice. Source: ASSUMPTION (location TBD).

R-10. EPC Integrator interface/integration review SHALL be performed on every register row; review disposition SHALL be recorded with each submittal. Source: DELIVERABLE_REGISTER.csv row 412 ("with EPC Integrator interface/integration review"); _CONTEXT.md ResponsibleParty.

R-11. Source vendor document table rows (rows directly traceable to the docx table) SHALL be retained as artifacts/evidence and SHALL NOT be promoted to standalone deliverables. Source: DELIVERABLE_REGISTER.csv row 412 Notes ("individual source document rows remain artifacts/evidence, not separate deliverables").

R-12. Turnover records SHALL evidence that each in-scope vendor document has reached an accepted/closed state prior to package handoff. Source: ASSUMPTION drawn from "turnover records" scope in DELIVERABLE_REGISTER.csv row 412; location TBD.

R-13. Where regulatory registration applies (REG-022 Pressure Equipment Registration Package), the registration package SHALL be incorporated into turnover before handoff. Source: 26020-Package_Requirements.docx §Mole Sieve / Vendor Engineering Deliverables.

R-14. Interface-bearing vendor documents (CTL-026 Package Vendor Interface Specification; PIP-004 Tie-In List; INS-018 Instrument I/O List; ELE-028 Electrical Interconnection/Connection Diagrams) SHALL be flagged for coordinated EPC review with the relevant facility-level interface owners. Source: same (these rows present in the Mole Sieve vendor table); ASSUMPTION on coordinated-flagging convention.

R-15. Interface coordination notes specific to this package SHALL be incorporated when published; current source-stated value is "TBD." Source: 26020-Package_Requirements.docx §Mole Sieve / Interface Coordination Notes.

## Standards

| Standard / Procedure | Role | Source / Location |
|---|---|---|
| DOC-008 Vendor Document Control Procedure | Document control method governing this register | 26020-Package_Requirements.docx Mole Sieve table |
| QLT-003 Inspection and Test Plan (ITP) | Quality verification baseline | same |
| QLT-006 Supplier Quality Plan | Quality management baseline | same |
| QLT-021 Manufacturing Record Book / Vendor Data Book | Turnover record structure | same |
| REG-022 Pressure Equipment Registration Package | Regulatory registration interface | same |
| Code/jurisdictional pressure-equipment standards | TBD — not stated in accessible source slice | location TBD |

## Verification

| Requirement | Verification approach |
|---|---|
| R-1, R-2, R-8 | Register-to-source cross-check against the Mole Sieve "Vendor Engineering Deliverables" table (all source rows present). |
| R-3, R-4 | Inspect DOC-008 and PRQ-009 issue/revision records. |
| R-5 | Confirm PRQ-016, MEC-023, QLT-021 are issued and accepted at turnover. |
| R-6, R-7 | Confirm QLT-003/006/013/020 and PRQ-013/015 issued and accepted. |
| R-9 | Audit register attributes; verify each row carries revision/status/dates/review/turnover state. |
| R-10 | Sample EPC review records per row; confirm disposition captured. |
| R-11 | Confirm no docx-table row has been registered as a separate deliverable. |
| R-12 | Turnover gate review confirms accepted/closed state per row. |
| R-13 | Confirm REG-022 closure pre-handoff. |
| R-14 | Confirm coordinated-review tags applied to CTL-026, PIP-004, INS-018, ELE-028. |
| R-15 | Confirm interface notes incorporated once source publishes resolution. |

## Documentation

The deliverable produces:
- Vendor Document Register (table form; one row per vendor document ID).
- Vendor document submittals (per-row artifacts as issued).
- Source-required vendor documentation set (per Mole Sieve "Vendor Engineering Deliverables" table).
- Turnover records (Manufacturing Record Book / Vendor Data Book, final acceptance log).

Source for documentation list: DELIVERABLE_REGISTER.csv row 412 "Artifacts" column.
