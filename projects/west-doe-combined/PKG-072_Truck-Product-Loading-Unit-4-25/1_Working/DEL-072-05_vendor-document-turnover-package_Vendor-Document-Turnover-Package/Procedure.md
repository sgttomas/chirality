# Procedure — Vendor Document Turnover Package (DEL-072-05)

## Purpose

Produce, review, and close out the Vendor Document Turnover Package for PKG-072 (Truck Product Loading Unit 4-25) such that the Owner / EPC Integrator can take custody of a complete, register-indexed, vendor-authored documentation set with documented EPC Integrator integration review.

This procedure covers both:
- producing the deliverable (Package Vendor authoring; EPC Integrator review), and
- using it at turnover (acceptance handover).

## Prerequisites

**Declared upstream dependencies:** None declared during PREPARATION (`_DEPENDENCIES.md`). Undeclared edges are advisory only.

**Required references and access:**

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable.
- `DELIVERABLE_REGISTER.csv` row 562 (DEL-072-05) — GATE-07 snapshot.
- `PACKAGE_REGISTER.csv` row 99 (PKG-072) — GATE-07 snapshot.
- `26020-Package_Requirements.docx` package heading 26 — clause-level vendor document requirements (binary; access TBD).
- `26020-Packages_Interfaces_4_export.xlsx` Packages row 99 — package interface list (binary; access TBD).
- Project document control standard (numbering, revisioning, transmittal conventions) — location TBD.

**Authoring roles ready:** Package Vendor document control identified; EPC Integrator reviewer assigned. (ASSUMPTION — confirmed during execution, not by this skill.)

## Steps

### A. Authoring (Package Vendor)

1. Extract clause-level vendor-document requirements from `26020-Package_Requirements.docx` heading 26 (TBD — requires docx extraction task).
2. Build the initial **vendor document register** with one row per required document, populating: document number, title, type, required revision stages, linked SOW row(s), linked interface type(s), source-required flag.
3. For each register row, draft / collect the underlying vendor document at the first required stage (preliminary).
4. Issue preliminary submittals via transmittal; record transmittal reference on the register row.
5. Iterate stages (for-approval, final, as-built) per `26020-Package_Requirements.docx` heading 26 (specific stage list TBD).
6. For "source-required" rows, capture the upstream workbook row content as an artifact (e.g., a snapshot or extract) and attach it to the register row.

### B. Review (EPC Integrator)

7. For each submitted document, perform interface/integration review against the PKG-072 interface list (`PACKAGE_REGISTER.csv` row 99 InterfaceTypes).
8. Record disposition (e.g., accepted / accepted-with-comments / rejected) on the register row, with reviewer and date.
9. Flag any interface gap or inter-document inconsistency back to the Package Vendor for revision.

### C. Turnover (Joint)

10. When all required register rows reach final / as-built stage and have EPC Integrator dispositions of accepted (or accepted-with-comments closed out), assemble the closed turnover package: register + all final-stage submittals + transmittals + acceptance evidence.
11. Capture final sign-off transmittal as the turnover record.
12. Archive the closed package per project document control retention policy (retention period TBD).

### D. Status update (this deliverable)

13. Update `_STATUS.md` from INITIALIZED → SEMANTIC_READY (after Pass 3 lensing enrichment is applied; out of scope for this P1_P2 run).
14. On completion of all turnover sign-offs, update `_STATUS.md` to its closed state per project lifecycle convention (TBD — specific state name not authoritatively located).

## Verification

- The vendor document register contains a row for every required document per `26020-Package_Requirements.docx` heading 26 (TBD authoritative count).
- Every register row has a documented EPC Integrator disposition.
- Every PKG-072 applicable interface type (per `PACKAGE_REGISTER.csv` row 99) has at least one supporting register row.
- Every SOW item in {SOW-0245, SOW-0246, SOW-0247, SOW-0248} traces to at least one register row.
- Source-required rows have attached source-row evidence.
- A final transmittal / sign-off exists.
- No register row remains in "preliminary" or "for-approval" stage at turnover.

## Records

The following records constitute closed evidence:

- Final `VendorDocumentRegister.xlsx` (or equivalent) with all rows at final/as-built stage and dispositions.
- All transmittals (vendor → EPC Integrator; EPC Integrator → Owner).
- All final-revision vendor documents (the submittals themselves).
- Source-row artifact evidence for source-required documents.
- Final acceptance / sign-off record (the turnover record).
- EPC Integrator review log per document.

## Notes

- This procedure is bounded by available source visibility. Steps marked with TBD references require resolution of binary source slices (docx / xlsx) before the deliverable can be advanced past INITIALIZED in a source-grounded manner.
- The Conflict Table in `Guidance.md` lists identity, tagging, and source-access conflicts that should be ruled on by a human before binding decisions are made under this procedure.
