# Procedure — DEL-095-01 Scope of Work (PKG-095 Tanks, Slop (API 650))

## Purpose

Produce the EPC Integrator's `PKG-095` Scope of Work artifact set such that the Specification requirements (SPEC-095-01-R01 through R12) are satisfied with source-grounded content and explicit `TBD` markers where source is not locally accessible.

## Prerequisites

- Read deliverable-local truth files: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- Access to the GATE-07 PROJECT_DECOMP snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`:
  - `PACKAGE_REGISTER.csv` (PKG-095 row)
  - `DELIVERABLE_REGISTER.csv` (DEL-095-01 row and sibling DEL-095-02 … DEL-095-06)
  - `SCOPE_LEDGER.csv` (SOW-0213 through SOW-0216)
  - `ARTIFACT_REGISTER.csv` (DEL-095-01 rows)
  - `INTERFACE_REGISTER.csv` (PKG-095 rows — nine interfaces)
  - `OBJECTIVE_REGISTER.csv` and `OBJECTIVE_DELIVERABLE_MAP.csv` (DEL-095-01 rows)
- ASSUMPTION: where deeper source extraction is needed, retrieve source slices from `26020-Package_Requirements.docx` package heading 47 and `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (residing in `_Sources/`). If not locally extracted, treat as `location TBD`.
- No declared upstream deliverable dependencies (`_DEPENDENCIES.md`). Downstream deliverables `DEL-095-02` … `DEL-095-06` consume this SOW.

## Steps

1. **Identity load.** Populate Datasheet identification block from `PACKAGE_REGISTER.csv` PKG-095 row and `DELIVERABLE_REGISTER.csv` DEL-095-01 row. Verify workbook row 91, WBS 03, CoA tracking 26020-03-19-004, discipline Mechanical, package name "Tanks, Slop (API 650)".
2. **Function and equipment.** Reproduce SOW-0214 (basic scope) and SOW-0215 (major included equipment: API 650 modified atmospheric slop storage tank, preliminary tag `TK-9130-2` as ASSUMPTION, appurtenances, drain/recycle/truck-out connections, standard instrumentation) as the package function and tagged-equipment artifacts.
3. **Integration narrative.** Reproduce SOW-0216 slop definition, expected sources (off-spec condensate, tank drains, KO drum pump-out, VRU/scrubber liquids, treating-unit drains, other contaminated hydrocarbon liquids), and the open-item flag for process confirmation. Cross-reference the nine applicable interface types from `INTERFACE_REGISTER.csv` PKG-095 rows.
4. **Responsibility assignment record.** Reproduce the responsibility model verbatim from `PACKAGE_REGISTER.csv` PKG-095 (Package Vendor owns package engineering/design/documentation/equipment; EPC Integrator owns facility integration).
5. **Source basis.** List Workbook Packages row 91, `26020-Package_Requirements.docx` heading 47, `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; explicitly note that no package-folder brief.md, DOCX, or PDF scope source was found per `PACKAGE_REGISTER.csv` SourceRefRaw.
6. **Objectives + scope items.** Echo `{OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}` and `{SOW-0213, SOW-0214, SOW-0215, SOW-0216}` from `OBJECTIVE_DELIVERABLE_MAP.csv` and `SCOPE_LEDGER.csv`.
7. **TBD audit.** Any design value (tank capacity, dimensions, P, T, materials, API 650 modification scope, instrument list, code citations) lacking a locally accessible source slice MUST be marked `TBD` with `location TBD`. Do not infer.
8. **Conflict capture.** Record open ownership/extraction conflicts in the Guidance Conflict Table with proposed authority and `TBD` human ruling (CONF-095-01-01 through CONF-095-01-04).
9. **Cross-document consistency sweep.** Verify Datasheet, Specification, Guidance, and Procedure use the same terms (PKG-095, slop storage tank, `TK-9130-2` always ASSUMPTION-labeled, API 650 modified, the nine interface types), the same scope items, and the same objectives.
10. **Status update.** When current state is `OPEN`, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`.

## Verification

| Step | Check |
|---|---|
| 1 | Identity table matches PKG-095 row in `PACKAGE_REGISTER.csv` (every field). |
| 2 | SOW-0214 and SOW-0215 text is present; tank tag `TK-9130-2` carries ASSUMPTION label. |
| 3 | Integration narrative reproduces SOW-0216; the nine interface types match `INTERFACE_REGISTER.csv` for PKG-095. |
| 4 | Responsibility text preserves vendor/EPC split. |
| 5 | Source basis list cites Workbook row 91, package requirements doc heading 47, and the 3-25 Comp_and_Liquids DBM; missing brief.md/DOCX/PDF noted. |
| 6 | Objective set equals `{OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010}`; scope set equals `{SOW-0213, SOW-0214, SOW-0215, SOW-0216}`. |
| 7 | No unsourced numeric value exists outside a `TBD` cell. |
| 8 | Conflict Table present in Guidance with at least the four enumerated conflicts (process-basis confirmation, design-conditions extraction, CP/grounding ownership, API 650 modification scope). |
| 9 | Same terms, tags, and lists appear in all four documents (no aliases). |
| 10 | `_STATUS.md` State transitions `OPEN → INITIALIZED` (only if currently `OPEN`); History appended. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in `{DELIVERABLE_PATH}`.
- `_STATUS.md` updated (safe update only).
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<timestamp>.md` capturing inputs, resolved skill, tools used, applied changes, MISSING, and any NEEDS_HUMAN_RULING items.
- Conflict Table entries in `Guidance.md` carry forward as `NEEDS_HUMAN_RULING` items into the run record.
