# Procedure — DEL-082-01 Scope of Work (LP Flare KO Drum Package)

This Procedure describes the steps to **produce** the PKG-082 Scope of Work artifact (this deliverable) so that it is source-anchored, internally consistent, and ready to be consumed by the Package Datasheet (DEL-082-02) and the downstream PKG-082 deliverables. Operational use of the LP flare KO drum equipment itself is out of scope for this artifact.

## Prerequisites

- Accepted upstream decomposition snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24` [SourcePath: `_REFERENCES.md`]
- Deliverable-local truth set present: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`
- Read access to:
  - `DELIVERABLE_REGISTER.csv` row 300 (this deliverable)
  - `PACKAGE_REGISTER.csv` row 56 (PKG-082)
  - `OBJECTIVE_DELIVERABLE_MAP.csv` (OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 → DEL-082-01)
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (LP flare/KO slices)
- Awareness that `_Sources/26020-Package_Requirements.docx` heading 35 and `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 56 are referenced sources but are **not locally machine-readable** in their current binary form; their content is treated as `location TBD` until extracted.
- No declared upstream blocker dependencies in `_DEPENDENCIES.md`.

## Steps

1. **Read deliverable-local truth set.** Open `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`. Confirm the deliverable identity (DEL-082-01_scope-of-work, PKG-082, Mechanical, EPC Integrator). [SourcePath: `_CONTEXT.md`]
2. **Read decomposition row.** Open `DELIVERABLE_REGISTER.csv` row 300 and `PACKAGE_REGISTER.csv` row 56. Capture: description, responsible party, anticipated artifacts, applicable interface types, supported objectives, source references. [SourcePath: DELIVERABLE_REGISTER.csv row 300; PACKAGE_REGISTER.csv row 56]
3. **Locate accessible source slices.** Open `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. Extract slices for: §"Flare and Blowdown" (LP flare KO drum V-3900-2, transfer pump P-3900-2, services, header size, blowdown reference); §"Sparing Philosophy" (LP flare KO drum transfer pump sparing); §"Equipment Design Margins" (vessel and pump margins). [SourcePath: DBM-Comp_and_Liquids L495–501, L584, L588–599]
4. **Record source inaccessibility.** Record in this SoW set that `26020-Package_Requirements.docx` heading 35 and `26020-Packages_Interfaces_4_export.xlsx` row 56 are **not locally machine-readable** in this run. Mark dependent content `TBD: location TBD` rather than substituting decomposition prose for source text.
5. **Draft Datasheet.md.** Populate Identification, Attributes, Conditions, Construction, References using the slices extracted in Steps 2–3. Use `TBD` for any field with no accessible source.
6. **Draft Specification.md.** Express the package boundary, function, and responsibility split as numbered requirements (R-082-01-NN). Each requirement cites either the DBM source slice or the PACKAGE_REGISTER.csv row 56 ScopeNotes/ApplicableInterfaceTypes field. Label any inferred margin or convention as **ASSUMPTION**.
7. **Draft Guidance.md.** Express the rationale for the responsibility split, the facility-shared nature of the flare/KO infrastructure, the external dependency on W242510-PRC-REP-000003-001 for blowdown, and the consequence of the binary source files not yet being machine-readable. Include the Conflict Table heading even when no conflicts are present.
8. **Draft Procedure.md.** Document the production sequence (these steps) and the verification checks that confirm the resulting SoW is source-anchored and consistent.
9. **Pass 2 cross-document consistency check.** Confirm: equipment tags (V-3900-2, P-3900-2) appear identically across all four documents; the sparing basis (1 x 100 percent) and header size (508 mm / 20 in) are consistent; the responsibility split language is consistent across Specification and Guidance; anticipated artifacts match `_CONTEXT.md`; interface types match PACKAGE_REGISTER.csv row 56. Record any unresolved differences in the Guidance Conflict Table.
10. **Status update.** If `_STATUS.md` Current State is `OPEN`, advance to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents` (or equivalent in-band edit honoring the same contract). Do not regress state. [SourcePath: skill four-documents Step 7]
11. **Write run record.** Persist `_run_records/TASK_RUN_<timestamp>.md` documenting inputs, sources read, outputs produced, status update, and any TBD / NEEDS_HUMAN_RULING items.

## Verification

| Check | Pass criterion |
|---|---|
| Four files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` are present in `{DELIVERABLE_PATH}` |
| Default sections present | Each of the four documents contains the default schema sections defined by the four-documents skill |
| Tag consistency | V-3900-2 (drum) and P-3900-2 (transfer pump) appear consistently in Datasheet, Specification, Guidance, Procedure |
| Value consistency | Sparing (1 x 100 percent) and LP relief header size (508 mm / 20 in) consistent across documents |
| Source citation | Every non-trivial value cites either a DBM section/line or PACKAGE_REGISTER.csv row 56 / DELIVERABLE_REGISTER.csv row 300, or is explicitly marked `TBD` / `location TBD` |
| Responsibility split | Vendor scope and EPC scope language is identical in substance across Specification R-082-01-06 / R-082-01-07 and Guidance Principles |
| `_STATUS.md` safe update | State changed `OPEN → INITIALIZED` only when prior state was `OPEN`; otherwise unchanged |
| Run record present | `_run_records/TASK_RUN_<timestamp>.md` exists with required headings |

## Records

The artifacts produced/updated by this Procedure are:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` (safe state advance to `INITIALIZED` when prior state was `OPEN`)
- `_run_records/TASK_RUN_<timestamp>.md`

Downstream consumers (DEL-082-02 Package Datasheet, DEL-082-03 Construction Work Package, DEL-082-04 Vendor Engineered Equipment Package, DEL-082-05 Vendor Document Turnover Package, DEL-082-06 EPC Vendor Package Review and Acceptance) inherit the source basis and responsibility split established here.
