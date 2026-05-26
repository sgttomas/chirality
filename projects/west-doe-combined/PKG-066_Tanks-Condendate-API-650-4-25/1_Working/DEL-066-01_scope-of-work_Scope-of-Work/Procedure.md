# Procedure — DEL-066-01 Scope of Work (PKG-066 Tanks, Condendate (API 650) 4-25)

## Purpose

Produce the EPC Integrator's `PKG-066` Scope of Work artifact set such that the Specification requirements (SPEC-066-01-R01 through R12) are satisfied with source-grounded content and explicit `TBD` markers where source is not locally accessible.

## Prerequisites

- Read deliverable-local truth files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Access to the GATE-07 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `PACKAGE_REGISTER.csv` (PKG-066 row, row 89)
  - `DELIVERABLE_REGISTER.csv` (DEL-066-01 row and sibling DEL-066-02 … DEL-066-06)
  - `SCOPE_LEDGER.csv` (SOW-0205 through SOW-0208)
  - `ARTIFACT_REGISTER.csv` (DEL-066-01 rows)
  - `INTERFACE_REGISTER.csv` (PKG-066 rows — nine interface types)
  - `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-066-01 rows)
- ASSUMPTION: where deeper source extraction is needed, retrieve source slices from `26020-Package_Requirements.docx` package heading 21 and `DBM-Deepcut/4-25_Deepcut_DBM.md` (residing in `_Sources/`). If not locally extracted, treat as `location TBD`.
- ASSUMPTION: analog basis `26020-03-PT-RFQ-19-006 - Conde Tanks.docx` (3-25 condensate tank package) is informational only; do not promote analog values into 4-25 requirements without explicit human ruling.
- No declared upstream deliverable dependencies (`_DEPENDENCIES.md`). Downstream deliverables `DEL-066-02` … `DEL-066-06` consume this SOW.

## Steps

1. **Identity load.** Populate Datasheet identification block from `PACKAGE_REGISTER.csv` PKG-066 row and `DELIVERABLE_REGISTER.csv` DEL-066-01 row. Verify workbook row 89, WBS 01, CoA tracking 26020-01-19-004, discipline Mechanical.
2. **Function and equipment.** Reproduce SOW-0206 (basic scope: condensate product storage tanks, 3-25 analog basis) and SOW-0207 (major included equipment: API 650 modified atmospheric tanks, blanket gas, PVRV/EPRV, VRU connection, CP/grounding provisions, instrumentation, appurtenances). Carry final tank count, tags, capacity as TBD; cite Deepcut roster (5) and 3-25 analog (4 × 3,800 bbl) as candidate bases.
3. **Integration narrative.** Reproduce SOW-0208 (open items: count/tags/capacity, inlet/outlet sources, mercaptan treating bypass/recycle applicability, VRU/blanket-gas requirements, design-condition alignment with 3-25 basis). Cross-reference the nine applicable interface types from `INTERFACE_REGISTER.csv` PKG-066 rows. Add commercial disposition context from the 04-25 DBM (C5+ → NEBC Connector via LACT; 03-25/04-25 cross-facility transfer).
4. **Responsibility assignment record.** Reproduce the responsibility model verbatim from `PACKAGE_REGISTER.csv` PKG-066 (Package Vendor scope; EPC Integrator integration scope).
5. **Source basis.** List Workbook Packages row 89, `26020-Package_Requirements.docx` heading 21, `DBM-Deepcut/4-25_Deepcut_DBM.md`; label `26020-03-PT-RFQ-19-006 - Conde Tanks.docx` and `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` as analog/informational. Note that no direct package-folder brief.md/DOCX/PDF scope source exists for 4-25.
6. **Objectives + scope items.** Echo `{OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}` and `{SOW-0205, SOW-0206, SOW-0207, SOW-0208}` from `OBJECTIVE_DELIVERABLE_MAP.csv` and `SCOPE_LEDGER.csv`.
7. **TBD audit.** Any design value (tank count/tags/capacity, P, T, materials, code citations) lacking a locally accessible source slice MUST be marked `TBD` with `location TBD`. Do not infer.
8. **Conflict capture.** Record open ownership/extraction conflicts in the Guidance Conflict Table with proposed authority and `TBD` human ruling (VRU/blanket-gas ownership; CP/grounding split; final design values; mercaptan path).
9. **Cross-document consistency sweep.** Verify Datasheet, Specification, Guidance, and Procedure use the same terms (PKG-066, "Tanks, Condendate (API 650) 4-25", C5+, NEBC Connector, LACT, VRU, PVRV/EPRV), the same scope items, the same objectives, and the same nine interface types.
10. **Status update.** When current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.

## Verification

| Step | Check |
|---|---|
| 1 | Identity table matches PKG-066 row in `PACKAGE_REGISTER.csv` (every field). |
| 2 | SOW-0206 and SOW-0207 text is present; final 4-25 count/tags/capacity carried as TBD with candidate bases cited. |
| 3 | Integration narrative reproduces SOW-0208; the nine interface types match `INTERFACE_REGISTER.csv` for PKG-066; commercial disposition context included. |
| 4 | Responsibility text preserves vendor/EPC split. |
| 5 | Source basis list cites Workbook row 89, package requirements doc heading 21, and DBM section(s); analog/informational sources labeled. |
| 6 | Objective set equals `{OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`; scope set equals `{SOW-0205, SOW-0206, SOW-0207, SOW-0208}`. |
| 7 | No unsourced numeric value exists outside a `TBD` cell. |
| 8 | Conflict Table present in Guidance with at least the VRU/blanket-gas, CP/grounding, design-value-extraction, and mercaptan-path items. |
| 9 | Same terms, lists, and counts appear in all four documents (no aliases). |
| 10 | `_STATUS.md` State transitions `OPEN → INITIALIZED` (only if currently `OPEN`); History appended. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated (safe update only).
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill, tools used, applied changes, MISSING, and any NEEDS_HUMAN_RULING items.
- Conflict Table entries in `Guidance.md` carry forward as `NEEDS_HUMAN_RULING` items into the run record.
