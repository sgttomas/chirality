# Procedure — DEL-097-05 Vendor Document Turnover Package

> Pass 1/2 generation by `TASK + four-documents`. Steps marked `TBD` where source-grounded judgement was unavailable.

## Purpose

Produce, control, and hand off the Vendor Document Turnover Package for `PKG-097` Tanks, Condendate (API 650) 3-25, so EPC review/acceptance (`DEL-097-06`) can proceed against a complete, source-traceable vendor documentation set.

## Prerequisites

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` present in the deliverable folder (PREPARATION outputs).
- Upstream EPC inputs available, in particular:
  - `DEL-097-01` Scope of Work
  - `DEL-097-02` Package Datasheet
  - (No upstream dependencies declared in `_DEPENDENCIES.md` as of this pass; treat the above as `ASSUMPTION` informational prerequisites.)
- Accessible source materials extracted from `_REFERENCES.md`, including:
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (text-accessible)
  - `26020-Package_Requirements.docx` package heading 49 — `TBD`, currently binary
  - `26020-Packages_Interfaces_4_export.xlsx` row 88 — `TBD`, currently spreadsheet
- A vendor document register template (controlled). Source for template: `TBD`.

## Steps

1. **Confirm deliverable identity and scope** by reading `_CONTEXT.md` and the deliverable register row `DEL-097-05`. Record any deviations.
2. **Enumerate source-required vendor documents** from Workbook Packages row 88 and `26020-Package_Requirements.docx` heading 49. (Currently `TBD` until those binary sources are extracted to text; carry as register placeholders with `TBD` markers.)
3. **Initialize the vendor document register** with one row per required document, populating at minimum: document number, title, document type, applicable tank service (condensate / produced water / shared), source row reference, planned revision schedule, and hold/issue code.
4. **Capture code-of-construction tagging** on each register row touching tank design: API 650 for condensate tanks (per package name; specific clause `TBD`) and API-650 Modified for produced-water tanks (DBM SEC-06 line 421). Mark coating (Devchem 253) and external insulation/heating where applicable.
5. **Issue vendor submittals against the register** using a controlled revision scheme (scheme `TBD`). Each submittal carries a transmittal entry referencing its register row.
6. **EPC Integrator interface review**: route each submittal (or batch) to the EPC Integrator for interface/integration review. Capture EPC review comments against the register row. (`_CONTEXT.md` ResponsibleParty.)
7. **Resolve open items / TBCs** carried in vendor documentation (e.g., produced-water tank SG 1.25 vs pump basis 1.18, DBM SEC-06 line 421) by routing to detailed design closure; record closure evidence on the register row.
8. **Compile turnover records**: final-revision document set, complete transmittal log, EPC acceptance evidence, certification originals (mill certs, NDE reports, hydrotest records — specific list `TBD`).
9. **Hand off to `DEL-097-06`** EPC Vendor Package Review and Acceptance with the final register, final-rev submittals, and turnover records bundle.

## Verification

| Step | Verification |
|---|---|
| 2, 3 | Every source-required vendor document row in the source list maps to a register row (or is explicitly marked `TBD` pending source extraction). |
| 4 | Register rows for tanks cite the correct code basis (API 650 / API-650 Modified) and reflect DBM SEC-06 attributes. |
| 5 | Each submitted document appears in the transmittal log with revision and date; revision code matches the controlled scheme. |
| 6 | EPC review comments are dispositioned (incorporated / rejected with reason / open) on the register. |
| 7 | Each TBC/`TBD` item carried on a register row has a closure entry or remains explicitly open with owner identified. |
| 8 | Turnover bundle index lists all required artifact classes and points to the final-rev document set. |
| 9 | `DEL-097-06` receives the bundle; receipt acknowledged. |

## Records

- Vendor document register (controlled, final revision)
- Vendor document submittals (final revisions)
- Transmittal log
- EPC review/comment disposition log
- Open-item / TBC closure log
- Turnover bundle index and final acceptance evidence
