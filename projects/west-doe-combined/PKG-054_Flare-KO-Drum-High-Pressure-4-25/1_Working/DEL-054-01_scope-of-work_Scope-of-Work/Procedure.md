# Procedure — DEL-054-01 Scope of Work (PKG-054 Flare KO Drum (High Pressure) 4-25)

## Purpose

Produce the EPC Integrator's `PKG-054` Scope of Work artifact set such that the Specification requirements (SPEC-054-01-R01 through R11) are satisfied with source-grounded content and explicit `TBD` markers where source is not locally accessible.

## Prerequisites

- Read deliverable-local truth files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Access to the GATE-07 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `PACKAGE_REGISTER.csv` (PKG-054 row)
  - `DELIVERABLE_REGISTER.csv` (DEL-054-01 row and sibling DEL-054-02 … DEL-054-06)
  - `SCOPE_LEDGER.csv` (SOW-0075 through SOW-0078)
  - `ARTIFACT_REGISTER.csv` (DEL-054-01 rows)
  - `INTERFACE_REGISTER.csv` (PKG-054 rows)
  - `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-054-01 rows)
- ASSUMPTION: where deeper source extraction is needed, retrieve source slices from `26020-Package_Requirements.docx` package heading 9 and `DBM-Deepcut/4-25_Deepcut_DBM.md` (residing in `_Sources/`). If not locally extracted, treat as `location TBD`.
- No declared upstream deliverable dependencies (`_DEPENDENCIES.md`). Downstream deliverables `DEL-054-02` … `DEL-054-06` consume this SOW.

## Steps

1. **Identity load.** Populate Datasheet identification block from `PACKAGE_REGISTER.csv` PKG-054 row and `DELIVERABLE_REGISTER.csv` DEL-054-01 row. Verify workbook row 55, WBS 01, CoA tracking 26020-01-17-002, discipline Mechanical.
2. **Function and equipment.** Reproduce SOW-0076 (basic scope) and SOW-0077 (major included equipment, including tags `V-4100-1` and `P-4100-1`) as the package function and tagged-equipment artifacts. Verify tags appear verbatim.
3. **Integration narrative.** Reproduce SOW-0078 (HP flare header tie-in to cryogenic flare header; EHT + insulation). Cross-reference the ten applicable interface types from `INTERFACE_REGISTER.csv` PKG-054 rows.
4. **Responsibility assignment record.** Reproduce the responsibility model verbatim from `PACKAGE_REGISTER.csv` PKG-054 (Package Vendor scope; EPC Integrator integration scope).
5. **Source basis.** List Workbook Packages row 55, `26020-Package_Requirements.docx` heading 9, `DBM-Deepcut/4-25_Deepcut_DBM.md`; label `Bid Docs/Budgetary/24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` as budgetary-only.
6. **Objectives + scope items.** Echo `{OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}` and `{SOW-0075, SOW-0076, SOW-0077, SOW-0078}` from `OBJECTIVE_DELIVERABLE_MAP.csv` and `SCOPE_LEDGER.csv`.
7. **TBD audit.** Any design value (P, T, capacity, materials, code citations) lacking a locally accessible source slice MUST be marked `TBD` with `location TBD`. Do not infer.
8. **Conflict capture.** Record open ownership/extraction conflicts in the Guidance Conflict Table with proposed authority and `TBD` human ruling.
9. **Cross-document consistency sweep.** Verify Datasheet, Specification, Guidance, and Procedure use the same terms (PKG-054, V-4100-1, P-4100-1, condensate slop tank), the same scope items, the same objectives, and the same ten interface types.
10. **Status update.** When current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.

## Verification

| Step | Check |
|---|---|
| 1 | Identity table matches PKG-054 row in `PACKAGE_REGISTER.csv` (every field). |
| 2 | SOW-0076 and SOW-0077 text is present and tag names are exact. |
| 3 | Integration narrative reproduces SOW-0078; the ten interface types match `INTERFACE_REGISTER.csv` for PKG-054. |
| 4 | Responsibility text preserves vendor/EPC split. |
| 5 | Source basis list cites all required sources; budgetary go-by labeled informational. |
| 6 | Objective set equals `{OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`; scope set equals `{SOW-0075, SOW-0076, SOW-0077, SOW-0078}`. |
| 7 | No unsourced numeric value exists outside a `TBD` cell. |
| 8 | Conflict Table present in Guidance with at least the EHT-ownership and source-slice-extraction items, or explicit "none" if resolved. |
| 9 | Same terms, tags, and lists appear in all four documents (no aliases). |
| 10 | `_STATUS.md` State transitions `OPEN → INITIALIZED` (only if currently `OPEN`); History appended. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated (safe update only).
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill, tools used, applied changes, MISSING, and any NEEDS_HUMAN_RULING items.
- Conflict Table entries in `Guidance.md` carry forward as `NEEDS_HUMAN_RULING` items into the run record.
