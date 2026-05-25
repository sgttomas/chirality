# Procedure: DEL-032-05_vendor-document-turnover-package

## Purpose

Produce, review, and turn over the Vendor Document Turnover Package for `PKG-032` Cathodic Protection Design and Installation, culminating in EPC Integrator acceptance of the Final Vendor Data Book (PRQ-016).

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` initialized for this deliverable (PREPARATION complete).
- Vendor Engineered Equipment Package (`DEL-032-04`) under active vendor engineering so vendor documents can be produced against the actual CP design.
- EPC anchor deliverables `DEL-032-01` (Scope of Work), `DEL-032-02` (Package Datasheet), `DEL-032-03` (Construction Work Package) available as integration references.
- Accessible upstream source set: `_Sources/26020-Package_Requirements.docx` (Vendor Engineering Deliverables table); `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 34 (interface declarations).
- EPC document control procedure and review/disposition convention. **TBD — not in accessible source set.**

## Steps

1. **Initialize vendor document index.** The vendor establishes PRQ-009 Vendor Document Index covering all submittals planned for PKG-032 (core list per `26020-Package_Requirements.docx`; CP-specific additions per CONF-032-05-001 ruling).
2. **Establish vendor document control procedure.** Vendor authors DOC-008 Vendor Document Control Procedure compatible with the EPC document control convention. **TBD — EPC convention required.**
3. **Issue submittals on lifecycle cadence.** Vendor issues each document (QLT-003, QLT-006, QLT-013, QLT-020, QLT-021, PRQ-013, PRQ-015) at its scheduled lifecycle state. Submittal lifecycle codes are **TBD** pending CONF-032-05-002 ruling.
4. **EPC interface and integration review.** EPC Integrator reviews each submittal against (a) `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 34 interface declarations (electrical power, grounding/bonding, I&C/control cabling, communications/network) and (b) EPC anchor deliverables (`DEL-032-01`/`-02`/`-03`). Dispositions are logged in PRQ-009.
5. **CP-specific submittals (tailoring).** If accepted under CONF-032-05-001, vendor adds CP-specific submittals (anode design records, soil resistivity surveys, rectifier data, reference-cell installation, commissioning potential surveys). **Content TBD pending ruling.**
6. **Mechanical completion and commissioning records.** Vendor produces installation, pre-commissioning, and commissioning records per the EPC's record templates. **Templates TBD.**
7. **Carry source vendor document table rows as artifacts.** Any vendor document rows referenced by upstream sources are filed inside this deliverable as artifacts/evidence, not promoted to new deliverables (`_CONTEXT.md`, Notes).
8. **Compile Final Vendor Data Book (PRQ-016).** Vendor consolidates all accepted submittals, certificates, test records, turnover records, and as-built data into PRQ-016.
9. **EPC acceptance and turnover.** EPC Integrator records final acceptance of PRQ-016. The deliverable's `_STATUS.md` is advanced by authorized human action; this procedure does not modify status.

## Verification

| Check | Method |
|---|---|
| Index completeness | Confirm every transmitted document appears in PRQ-009 with current revision and disposition. |
| Document control compliance | Confirm DOC-008 procedure matches the EPC's document control convention (once provided). |
| Interface coverage | Cross-walk vendor documents against PKG-032 interface row (`26020-Packages_Interfaces_4_export.xlsx` row 34). |
| Quality records present | Confirm QLT-003/006/013/020/021 are present with the required signoffs for the CP equipment supplied. |
| Spares and logistics | Confirm PRQ-013 and PRQ-015 cover delivered scope. |
| Turnover record completeness | Confirm installation, pre-commissioning, and commissioning records cover the CP system. (Template TBD.) |
| Final Vendor Data Book closure | Audit PRQ-016 against PRQ-009 index; confirm no open dispositions remain. |
| Artifact-vs-deliverable rule | Confirm no source vendor document row has been treated as a standalone deliverable (`_CONTEXT.md`, Notes). |

## Records

- PRQ-009 Vendor Document Index (live during execution, final at turnover).
- DOC-008 Vendor Document Control Procedure (vendor-authored, EPC-accepted).
- QLT-006 Supplier Quality Plan; QLT-003 ITP; QLT-013 MTRs/Certificates; QLT-020 Inspection Release Certificates; QLT-021 Manufacturing Record Books.
- PRQ-013 Logistics / Shipping Plan; PRQ-015 SPIR.
- Installation, pre-commissioning, commissioning, mechanical completion, and final acceptance records (formats TBD).
- PRQ-016 Final Vendor Data Book (turnover closure artifact).
- EPC review/disposition log for each submittal.
