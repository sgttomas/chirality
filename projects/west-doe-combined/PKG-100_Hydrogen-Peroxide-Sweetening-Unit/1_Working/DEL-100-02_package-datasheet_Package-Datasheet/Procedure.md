# Procedure — DEL-100-02 Package Datasheet (PKG-100 Hydrogen Peroxide Sweetening Unit)

> Operational steps to **produce** the Package Datasheet artifact (rather than to operate the package equipment).
> Source key: see `Datasheet.md` References.

## Purpose

Produce a source-grounded Package Datasheet artifact for `PKG-100 Hydrogen Peroxide Sweetening Unit` that satisfies Specification requirements R-01 through R-15 and resolves (or surfaces) the Guidance Conflict Table entries.

## Prerequisites

### Inputs

- Accepted upstream decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (FACT — `_CONTEXT.md`).
- `PACKAGE_REGISTER.csv` row `PKG-100` (FACT).
- `DELIVERABLE_REGISTER.csv` row `DEL-100-02_package-datasheet` (FACT).
- `INTERFACE_REGISTER.csv` rows for `PKG-100` (13 rows) (FACT).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (FACT).
- `_Sources/26020-Package_Requirements.docx` package heading 52 (text extraction required — currently binary).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` (text/tabular extraction required — currently binary).
- RFQ `26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` (acquisition required — not present under `_Sources`).

### Declared upstream dependencies

None declared during PREPARATION (`_DEPENDENCIES.md`). The accepted Gate 7 snapshot is treated as the upstream decomposition basis (`_DEPENDENCIES.md` Run Notes).

### Roles

- EPC Integrator Mechanical lead (responsible party — `_CONTEXT.md`, `DEL-REG`).
- EPC Integrator interface owner (for the 13 interface rows).
- EPC Integrator process engineer (chemistry/throughput).
- Human approver for Conflict Table rulings (per K-AUTH-1).

## Steps

1. **Initialize working copy.** Open `Datasheet.md` for editing. Confirm `_STATUS.md` is in an overwriteable state (`OPEN` or `INITIALIZED`).
2. **Populate Identification.** Copy all identification fields from `_CONTEXT.md` and `PKG-REG`. Verify tag `26020-03-PT-27-001`. (Specification R-01, R-09, R-10.)
3. **Populate Package Function.** Quote process function from `PKG-REG` package scope and corroborate against `DBM` lines 214 and 216. (R-02.)
4. **Populate Equipment Constituents.** List Hydrogen Peroxide Pumps, Hydrogen Peroxide Reactors, Static Mixer from `PKG-REG`. Mark quantities `TBD` where not stated. (R-03, R-04.)
5. **Populate Throughput.** Record 3,840 m3/d (`TBC`) from `DBM` line 427. Open CT-02. (R-05.)
6. **Populate Site/Environmental Conditions.** Record elevation 673 m AMSL and -40 °C to +35 °C ambient from `DBM` SEC-11. (R-06, R-14.)
7. **Populate Interfaces.** For each of the 13 interface rows in `IFC-REG` for `PKG-100`, create a datasheet interface row. For each row, record (or mark `TBD`):
   - Battery limit / boundary point,
   - Responsible party on each side (Package Vendor vs. EPC Integrator),
   - Handoff condition (flange / terminal / connection / signal).
   Align EHT, Fire & Gas, Grounding, Area Lighting, HVAC, and Hazardous Area Classification to the facility-level basis (`DBM` SEC-11). (R-07, R-08, R-13.)
8. **Resolve storage-tank scope.** Apply Conflict Table CT-01 ruling; if no ruling yet, carry the 400 bbl H2O2 tank as facility-side (PROPOSAL) and add to Utility Piping interface description. (R-12.)
9. **Populate per-equipment design data (R-04).** Where the binary sources (`PKG-REQ`, RFQ, Interfaces XLSX) are inaccessible, mark P, T, MOC, drivers, and electrical class `TBD` with `location TBD` to the source heading. Do not invent values. Open CT-04.
10. **Populate Construction section.** Record fabrication, inspection, shipping, and site assembly fields, marking `TBD` where the source is not accessible.
11. **Cross-document consistency sweep (Pass 2).** Verify:
    - Datasheet ↔ Specification: entities/attributes in Datasheet match Specification requirements,
    - Specification ↔ Guidance: requirements have rationale,
    - Specification ↔ Procedure: requirements have verification hooks,
    - Terminology consistency (especially CT-05 — "Hydrogen Peroxide Sweetening Unit" preferred),
    - Numeric values and units consistent (3,840 m3/d; 400 bbl; -40/+35 °C; 673 m AMSL).
12. **Verify References completeness.** Confirm `_REFERENCES.md` and the Datasheet References block list every source actually used; flag inaccessible sources for follow-up extraction.
13. **Run pre-issue checks.** Confirm Specification verification approaches map to actual document content; confirm no FACT claim lacks a source citation.
14. **Status update.** Apply `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` (Step 7) when `_STATUS.md` is `OPEN`.
15. **Write run record.** Append a `_run_records/TASK_RUN_<date>_<HHMM>.md` entry summarizing inputs, passes run, outputs, conflicts, and `RUN_STATUS`.

## Verification

| Verification ID | Check | Pass Criterion |
|---|---|---|
| V-01 | All Identification fields populated from `_CONTEXT.md` and `PKG-REG`. | Field-by-field match. |
| V-02 | Process function paragraph corroborated by both `PKG-REG` and `DBM`. | Both citations present. |
| V-03 | All 13 PKG-100 interfaces in `IFC-REG` present in Datasheet, each with battery limit / parties / handoff (or `TBD`). | Count == 13 and per-row completeness. |
| V-04 | Every non-trivial numeric value carries a source citation or `TBD`. | Lint sweep finds no unsourced numerics. |
| V-05 | Conflict Table entries CT-01 through CT-05 present in `Guidance.md` and referenced from the affected Specification requirements. | Cross-reference check. |
| V-06 | Units consistent with DBM (m3/d, bbl, °C, m AMSL). | Unit lint pass. |
| V-07 | `_STATUS.md` advanced via `write_status.sh` only when previous state was `OPEN`. | History entry exists with TASK+four-documents actor. |
| V-08 | Run record written under `_run_records/`. | File exists with expected fields. |

## Records

The following evidence/documents should result from executing this procedure:

- Updated `Datasheet.md` (this deliverable's core artifact).
- Updated `Specification.md`, `Guidance.md`, `Procedure.md`.
- Updated `_STATUS.md` (safe transition `OPEN → INITIALIZED`).
- Run record `_run_records/TASK_RUN_<date>_<HHMM>.md` capturing inputs, sources read, passes run, conflicts surfaced, and `RUN_STATUS`.
- (Downstream, when source slices become text-accessible) An interface requirements matrix expansion and a per-equipment design data table — pending CT-04 resolution.
