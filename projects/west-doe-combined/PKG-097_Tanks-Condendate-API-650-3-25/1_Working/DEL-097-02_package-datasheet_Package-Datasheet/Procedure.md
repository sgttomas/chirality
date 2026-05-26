# Procedure — Package Datasheet (DEL-097-02)

Deliverable: `DEL-097-02_package-datasheet`
Package: `PKG-097` — Tanks, Condensate (API 650) 3-25 (`26020-03-PT-19-006`)

Interpretation: This Procedure describes the steps to **produce and maintain** the EPC Package Datasheet artifact for PKG-097. Steps to *operate* the storage tanks are out of scope (covered by vendor IOM MEC-025 once issued).

## Purpose

Produce a source-grounded, RFQ-ready Package Datasheet for the four (4) 3,800 bbl C5+ condensate storage tanks defined by 26020-Package_Requirements.docx §49 and the 3-25 DBM, consistent with the requirements in `Specification.md` and the rationale in `Guidance.md`.

## Prerequisites

- Access to authoritative source materials:
  - `_Sources/26020-Package_Requirements.docx` (Heading 1 #49 — Tanks, Condensate).
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Workbook Packages row 88).
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
  - Bid Docs/Budgetary/26020-03-PT-RFQ-19-006 — Conde Tanks.docx (cited Source Basis; **TBD — not locally accessible at run time**).
- Accepted upstream decomposition snapshot: GATE-07 Final Published (2026-05-24).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` present and reviewed.
- Declared Upstream dependencies: none declared (per `_DEPENDENCIES.md`). Treat DEL-097-01 (Scope of Work) and the PROJECT_DECOMP snapshot as informational upstream context only.

## Steps

1. **Read source slices.** Open §49 of `26020-Package_Requirements.docx` (Tanks, Condensate); read Basic Scope, Major Included Equipment, Physical Interface Summary, Vendor Engineering Deliverables, and Interface Coordination Notes sub-sections, including all embedded tables.
2. **Cross-read interface row.** Open `26020-Packages_Interfaces_4_export.xlsx` row 88 and confirm each Yes/No applicability matches the §49 interface table.
3. **Read DBM context.** Open `3-25_Comp_and_Liquids_DBM.md`, sections covering site/winterization, Liquids Hub, Condensate and Produced-Water Receipts, and Condensate Mercaptan Treating, to frame hub-level service.
4. **Populate Identification.** Transfer DeliverableID, ParentPackageID, package tag, location, discipline, type, responsible party, and source basis into `Datasheet.md` Identification table.
5. **Populate Attributes (Equipment).** From §49 Basic Scope and Major Included Equipment, transcribe quantity, capacity, code, insulation status, blanket-gas standard, coating, relief devices, VRU connection, blanket-gas connection, fill limit, and fill-rate basis. Do not paraphrase normative wording.
6. **Populate Conditions.** From §49 Scope Notes table, transcribe operating P/T and design P/T verbatim, including units as written. Add hub-level throughput context from the DBM and mark each row with source.
7. **Populate Construction.** Record code (API 650 modified), venting basis (API 2000), Devchem 253 coating system, and By-Others exclusions verbatim. For items not in source (MOC, roof type, external coating), record `TBD` with `source location TBD`.
8. **Populate Package Boundary.** State By-Others exclusions explicitly per §49 Scope Notes.
9. **Populate Physical Interface Summary.** Render the §49 interface table verbatim; cite the workbook row 88 source.
10. **Populate References.** List all source documents read (Word §49, Workbook row 88, DBM, GATE-07 snapshot). Flag the RFQ docx as cited-but-not-locally-read.
11. **Build Requirements table in `Specification.md`.** One requirement per normative statement extracted from §49; map each to a Verification row.
12. **Build Verification table.** Each VID maps verification approach to one or more requirements.
13. **Build Documentation list.** Include anticipated artifacts from `_CONTEXT.md` and the §49 vendor deliverables enumeration.
14. **Draft `Guidance.md`.** Capture purpose, principles, considerations, trade-offs, and examples; build the Conflict Table for unresolved or potentially conflicting items.
15. **Cross-check consistency.** Run the Step-5 (skill) cross-document consistency checks: entity names, units, code refs, fitting names appear identically across Datasheet, Specification, Guidance, and Procedure. Resolve discrepancies or escalate via Conflict Table.
16. **Mark TBD and ASSUMPTION.** Ensure no invented values; every inference is labeled.
17. **Update `_STATUS.md` (safe-update).** If current state is `OPEN`, run `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Otherwise, do not modify.
18. **Write run record.** Create `_run_records/TASK_RUN_<DATE>_<HHMM>.md` capturing pass directive, sources read, files written, RUN_STATUS.

## Verification

| Check | Pass criterion |
|---|---|
| Four documents present | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` all exist in deliverable folder. |
| Default sections | Each document contains the SKILL default schema sections. |
| Source grounding | Every non-trivial value cites a source (`SourcePath` + `SectionRef`) or is labeled `TBD` / `ASSUMPTION`. |
| Spec ↔ Datasheet | R-01..R-14 in Spec map back to Datasheet Attributes/Conditions/Construction rows with identical values. |
| Spec ↔ Procedure | Every requirement has a verification hook (V-…). |
| Spec ↔ Guidance | Each unresolved item is reflected in the Guidance Conflict Table or in TBD/ASSUMPTION labels. |
| Interface matrix fidelity | All 18 interface-type rows from §49 are present with identical Yes/No applicability. |
| Status safe-update | `_STATUS.md` updated only when prior state is `OPEN`; no regression. |

## Records

The following records are produced or updated by this run:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` (this set).
- `_STATUS.md` — updated to `INITIALIZED` if prior state was `OPEN`.
- `_run_records/TASK_RUN_2026-05-25_<HHMM>.md` — run report with sources consulted, files written, RUN_STATUS.
- Open items / conflicts surfaced in `Guidance.md` Conflict Table for human ruling.

Records NOT modified by this run (per skill constraints): `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_MEMORY.md`, `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`.
