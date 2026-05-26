# Procedure: DEL-060-05_vendor-document-turnover-package

## Purpose

Produce, submit, and turn over the Package Vendor's Vendor Document Turnover Package for `PKG-060` (Tank Farm Pump Building 4-25) so that the EPC Integrator's interface/integration review (`DEL-060-06`) can be completed against accepted source-required vendor documentation, the vendor document register, vendor document submittals, and turnover records.

## Prerequisites

- Gate 7 PROJECT_DECOMP snapshot accepted and referenced (see `_REFERENCES.md`).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` initialized for this deliverable.
- `PACKAGE_REGISTER.csv` row `PKG-060`, `DELIVERABLE_REGISTER.csv` row `DEL-060-05`, `ARTIFACT_REGISTER.csv` rows for `DEL-060-05`, and `INTERFACE_REGISTER.csv` rows for `PKG-060` accessible.
- Source materials accessible:
  - `_Sources/26020-Package_Requirements.docx` (package heading 15 — Vendor Engineering Deliverables table); extraction to markdown is pending and is recorded as a `TBD` for content-level detail.
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Packages sheet row 85).
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Tank Farm Pump Building 2 entries, lines 2555, 2618-2622, and surrounding pump-building scope).
- Project vendor document control specification identified (location `TBD`).
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`. Declared downstream: none; the de-facto downstream consumer is `DEL-060-06_epc-vendor-package-review-and-acceptance`.

## Steps

1. **Confirm package identity and responsibility model.** Restate `PKG-060` identity (workbook row 85, WBS 01, CoA 26020-01-18-001, discipline Mechanical) and the Package Vendor / EPC Integrator responsibility split from `PACKAGE_REGISTER.csv` row `PKG-060`. Record in the turnover package cover sheet.
2. **Issue the Vendor Document Register.** Build the register (`ART-0D208A7734`) by enumerating each artifact-register row tied to `DEL-060-05`, grouped by the category headers in `ARTIFACT_REGISTER.csv` (Core vendor documents; Core package engineering; Rotating equipment / pumps; Relief / flare / vent design; Process piping interfaces; Utility piping interfaces; Drainage / containment interfaces; Electrical and grounding; Instrumentation and controls interfaces; Building / HVAC / code interfaces; Fire and gas / technical safety interfaces; Structural / access). Each register row shall include: document title, vendor identifier, project identifier (`TBD` until project vendor document control specification is accessible), source reference (`ARTIFACT_REGISTER.csv` row ID), category, planned submittal date, status.
3. **Cover the fourteen PKG-060 interface facts.** Cross-walk the register against `INTERFACE_REGISTER.csv` rows for `PKG-060` (Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports). For each interface, identify the register rows that carry corresponding vendor documentation. Record any interface not covered as a gap (Cathodic Protection is a known gap; see Guidance Conflict Table).
4. **Produce and submit vendor documents.** Issue each register row as a vendor document submittal, in the agreed-upon submittal cadence (per-package or per-discipline; record the chosen approach). Each submittal shall reference its register row, the applicable source artifact row, and the applicable interface fact(s).
5. **Capture FAT and quality records.** Produce Equipment FAT / Performance Test Procedure (`ART-632A37166D`) and Report (`ART-660C5F8E55`), Pump Hydraulic / NPSH Calculations (`ART-BC76FBFF8B`), Motor Starting Study (`ART-E7FADAEFB7`), ITP (`ART-75C9A5E28A`), MTRs (`ART-D923215BF0`), and Inspection Release Certificate (`ART-946006CE7C`). Quality records shall flow into the Manufacturing Record Book / Vendor Data Book (`ART-326C9FD2D6`).
6. **Assemble turnover records.** Compile the Vendor Data Book / Final Supplier Documentation (`ART-C3FA5659EF`) and Vendor Data Book / Mechanical Final Documentation (`ART-450778DCDF`). Include the IOM Manual (`ART-28257581F3`), Mechanical Spares / Special Tools Requirements (`ART-B3D7653AB8`), Spare Parts Interchangeability Record (`ART-65B229930D`), and Logistics / Shipping Plan (`ART-85EF313552`).
7. **Record source gaps.** Document items remaining `TBD`: vendor document numbering scheme, submittal acceptance criteria, turnover record templates, and any unaddressed Cathodic Protection artifact. Link each `TBD` to its `ARTIFACT_REGISTER.csv` or `INTERFACE_REGISTER.csv` row.
8. **Hand off to EPC Integrator review.** Transmit the assembled package to `DEL-060-06_epc-vendor-package-review-and-acceptance`. Include the register, submittals, turnover records, gap list, and traceability matrix (register row → submittal → interface → register source row).
9. **Track close-out.** Maintain register status until all submittals are accepted or dispositioned by EPC review; record acceptance outcomes; preserve dispositioned-comment incorporation evidence for each revision.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| Identity completeness | Compare cover sheet to workbook row 85 and Gate 7 registers. | All identity fields match. |
| Register completeness | Compare register rows to `ARTIFACT_REGISTER.csv` rows for `DEL-060-05`. | All artifact-register rows are represented or explicitly excluded with rationale. |
| Interface coverage | Cross-walk register to `INTERFACE_REGISTER.csv` rows for `PKG-060`. | All fourteen interface facts are addressed; gaps explicitly recorded. |
| Rotating-equipment artifacts | Confirm pump data sheets, NPSH calculations, seal/lube oil specification, motor starting study, FAT procedure, and FAT report are produced. | All present or explicitly dispositioned. |
| Source-gap discipline | Confirm `TBD` items are recorded against source-availability gaps, not invented values. | Gap list complete; no fabricated specifics. |
| Cross-document consistency | Verify Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved inconsistencies. |
| EPC review handoff | Verify transmission to `DEL-060-06`. | Handoff record present in turnover folder. |

## Records

- Vendor document register (issued and revised).
- Vendor document submittals (one transmittal package per register row, with revision history).
- Source vendor document artifacts (Vendor Engineering Deliverables table rows captured as evidence under this production unit).
- Turnover records: Manufacturing Record Book / Vendor Data Book, Final Supplier Documentation, Mechanical Final Documentation, IOM Manual, Spares/Special Tools Requirements, SPIR, Logistics/Shipping Plan.
- Source-gap / `TBD` list with links to applicable register or interface rows.
- Traceability matrix (register row → submittal → interface → source row).
- Handoff transmittal to `DEL-060-06_epc-vendor-package-review-and-acceptance`.
