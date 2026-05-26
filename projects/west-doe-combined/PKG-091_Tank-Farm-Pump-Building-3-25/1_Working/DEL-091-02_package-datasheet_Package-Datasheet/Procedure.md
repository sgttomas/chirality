# Procedure — DEL-091-02 Package Datasheet (Tank Farm Pump Building 3-25)

This procedure describes how to **produce** the Package Datasheet artifact for PKG-091. Operating procedures for the physical equipment package are out of scope (Package Vendor / Operations).

## Prerequisites

- Read access to the GATE-07 Final Published 2026-05-24 PROJECT_DECOMP snapshot.
- Locally accessible source materials under `_Sources/`:
  - `26020-Package_Requirements.docx` (package heading 44 — Tank Farm Pump Building 3-25)
  - `26020-Packages_Interfaces_4_export.xlsx` (Packages row 84)
  - `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`
  - (TBD) `26020-03-PT-RFQ-18-002-Tank Farm Pumps.docx` — location TBD; if accessible, treat as authoritative for RFQ-stage clarifications.
- Deliverable-local truth-set files (`_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`) present and read.
- Declared upstream dependencies: none at PREPARATION (`_DEPENDENCIES.md`). Effective upstream artifact is `DEL-091-01_scope-of-work` of the same package — ASSUMPTION based on DELIVERABLE_REGISTER anchoring narrative.

## Steps

1. **Initialize.** Confirm `_STATUS.md` Current State is `OPEN` (overwrite-safe). Record the upstream snapshot ID (GATE-07 Final Published 2026-05-24).
2. **Identity block.** Populate Datasheet > Identification from `_CONTEXT.md` and PACKAGE_REGISTER row PKG-091. Verify Workbook row 84, WBS 03, tag prefix 26020-03-18-001.
3. **Equipment inventory.** From SOW-0187 (`SCOPE_LEDGER.csv`), transcribe each tagged pump (tag, count, type, seal plan, power, drive). Preserve source units and parenthetical HP values. Mark voltage as TBD only where the source line is itself truncated.
4. **Capacity / conditions.** From SOW-0188, transcribe throughput per service and site/driver basis (575 V / 3 Ph / 60 Hz, 600 V MCC, DOL or VFD, H-O-A or On-Off, −40 °C motor sizing). Reproduce TBC verbatim; do not infer.
5. **By-others boundaries.** Carry DCS integration, foundations, and electrical supply to MCC as explicit "by others" boundary statements (SOW-0188).
6. **Interface matrix.** From INTERFACE_REGISTER.csv filtered to PKG-091, transcribe all fifteen InterfaceIDs with their interface types. Confirm count = 15 and `Applies = YES` for all.
7. **Responsibility narrative.** From PACKAGE_REGISTER responsibility-mode cell, summarize Package Vendor vs EPC Integrator split.
8. **Specification mapping.** Map each datasheet element to a Specification requirement (R-1 .. R-12) and a verification approach.
9. **Guidance & conflict capture.** Record principles, considerations, trade-offs, and any source ambiguity (truncations, TBC values, alternative starting methods) in `Guidance.md`, populating the Conflict Table.
10. **Cross-document consistency sweep (Pass 2).** Reconcile entity names, tags, values, and units across Datasheet ↔ Specification ↔ Guidance ↔ Procedure.
11. **Status update.** If state is `OPEN`, advance `_STATUS.md` to `INITIALIZED` via `tools/scaffolding/write_status.sh`.
12. **Run record.** Write `_run_records/TASK_RUN_<timestamp>.md` per AGENT_TASK Run-record format.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| V-1 Equipment inventory complete | Compare count of tagged pumps in Datasheet against SOW-0187 enumeration. | All listed tags present: P-9295-2; P-9290-2; P-9293-2; P-9215-2; P-9216-2; P-9210-2; P-9220-2; P-9200-2; P-9230-2; P-9211-2; P-9221-2; P-9240-2. |
| V-2 Interface matrix count | Count rows of interface matrix in Datasheet. | Exactly 15 rows, each with `Applies = YES` and matching InterfaceID from INTERFACE_REGISTER. |
| V-3 No fabricated values | Grep Datasheet for numeric values; cross-check each against SOW-0187 / SOW-0188. | Every non-TBD numeric value has a source citation. |
| V-4 TBC preservation | Inspect capacity table. | TBC entries preserved verbatim; not silently filled. |
| V-5 Responsibility split | Compare narrative against PACKAGE_REGISTER responsibility-mode cell. | Vendor vs EPC Integrator split matches source. |
| V-6 Cross-doc terminology | Spot-check pump tags and seal plan strings across all four documents. | Identical strings; same units. |
| V-7 Status discipline | Inspect `_STATUS.md` after run. | State = `INITIALIZED` only if prior state was `OPEN`; no state regression. |
| V-8 Run record | Inspect `_run_records/`. | One new `TASK_RUN_<timestamp>.md` exists, with required YAML frontmatter and headings. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — the four documents (this deliverable's primary outputs).
- `_STATUS.md` — updated to `INITIALIZED` on successful Pass 1+2 run from `OPEN`.
- `_run_records/TASK_RUN_<timestamp>.md` — durable run record for this invocation.
- Source citations carried inline reference: `PACKAGE_REGISTER.csv` PKG-091, `DELIVERABLE_REGISTER.csv` DEL-091-02, `SCOPE_LEDGER.csv` SOW-0185..SOW-0188, `INTERFACE_REGISTER.csv` fifteen PKG-091 rows, `OBJECTIVE_DELIVERABLE_MAP.csv`.
