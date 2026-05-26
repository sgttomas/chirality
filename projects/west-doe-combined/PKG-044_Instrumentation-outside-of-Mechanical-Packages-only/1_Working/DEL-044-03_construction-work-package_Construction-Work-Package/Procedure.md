# Procedure — DEL-044-03 Construction Work Package

**Interpretation:** This procedure describes the steps to **produce** the Construction Work Package deliverable artifact. Steps for using/operating the resulting package in the field belong to the construction execution phase and are out of scope for this deliverable's procedure.

## Prerequisites

1. Accepted upstream decomposition snapshot available: GATE-07 Final Published (2026-05-24). Source: `_REFERENCES.md`.
2. Deliverable-local context files present and read: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
3. Sibling deliverables underway or completed in PKG-044:
   - DEL-044-01 Scope of Work (provides package scope and tagged equipment).
   - DEL-044-02 Package Datasheet (provides technical handoff data, interface requirements matrix, interface facts).
   Note: `_DEPENDENCIES.md` declares no upstream dependencies at PREPARATION; this prerequisite is therefore an `ASSUMPTION` based on the sibling-deliverable structure in SCOPE_LEDGER.csv row 46. Upgrade to a declared dependency if `TASK + dependency-extract` confirms.
4. Access to underlying sources for source-grounded extension:
   - Workbook Packages row 46 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`).
   - `_Sources/DBM-Comp_and_Liquids/` and `_Sources/DBM-Deepcut/` DBM markdown.
   - `_Sources/26020-Package_Requirements.docx` for vendor document/turnover requirements (referenced by OBJ-010).
5. Tool authorization: writes are limited to the deliverable folder. Status updates use `tools/scaffolding/write_status.sh`.

## Steps

1. **Confirm scope and identity.** Re-read `_CONTEXT.md` and PACKAGE_REGISTER.csv row 46. Confirm DeliverableID, ParentPackageID, discipline (Instrumentation), WBS (02), and the package-name boundary ("outside of Mechanical Packages only").
2. **Compile the anticipated artifact list.** Open `Datasheet.md` and `Specification.md` and confirm the three required artifacts (construction work package narrative, installation and tie-in workface plan, construction interface and turnover checklist) are listed and traceable to ARTIFACT_REGISTER rows 979-981.
3. **Enumerate declared interfaces.** From INTERFACE_REGISTER.csv rows 302-306, list the five declared interface types and capture the Gate 6 disposition note verbatim for inclusion in the construction interface and turnover checklist.
4. **Draft the construction work package narrative (ART-98EDB38A63).** Describe physical installation, construction, and tie-in to larger systems. Cite Workbook Packages row 46 for package identity and PACKAGE_REGISTER.csv row 46 for applicable interface types. Mark equipment counts, weights, and lift methodology as `TBD (location TBD)` unless a workbook slice is in-folder.
5. **Draft the installation and tie-in workface plan (ART-48F9265F2F).** Cover workface planning evidence for installing/building the package and connecting it to adjacent process, utility, electrical, controls, civil, structural, and safety systems as applicable (ARTIFACT_REGISTER.csv row 980). Include one section per declared interface type from Step 3. Treat instrumentation field supports, power, and communications as in-scope per the Gate 6 disposition.
6. **Draft the construction interface and turnover checklist (ART-C05FF15A97).** Cover construction-facing interface, tie-in, inspection, and turnover evidence (ARTIFACT_REGISTER.csv row 981). Map each interface row to a checklist item. Map each verification approach from `Specification.md` to a checklist item. Include turnover items aligned to OBJ-010 (commissioning, vendor document closure, open-item closure).
7. **Build the traceability matrix.** Map each requirement (REQ-044-03-01 through REQ-044-03-10) to its narrative/workface-plan/checklist section. Map SOW-0045 and each supported objective (OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-010) to deliverable sections.
8. **Cross-document consistency check.** Verify Datasheet entities (interface IDs, artifact IDs, objective IDs) match Specification and Procedure references. Verify all values cited are either source-grounded or explicitly TBD. Update the Conflict Table in `Guidance.md` if any conflict is found.
9. **Status update.** When this is the initial pass (`OPEN → INITIALIZED`) and the brief authorizes it, invoke `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Otherwise do not modify `_STATUS.md`.
10. **Write run record.** Persist `_run_records/TASK_RUN_<timestamp>.md` summarizing inputs, outputs, missing items, and rulings needed.

## Verification

| Check | Pass criterion |
|---|---|
| All four documents exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` present in `{DELIVERABLE_PATH}` |
| Default schema sections present | Each document contains its default sections (per SKILL.md Step 2 table) |
| Source-grounding | Every non-trivial claim cites a source or is labeled `TBD` / `ASSUMPTION` |
| Interface coverage | All five interface rows from INTERFACE_REGISTER appear in the workface plan and checklist sections |
| Objective coverage | All seven supported objectives appear in the traceability matrix |
| Cross-document consistency | Identifiers and values used identically across all four documents |
| Status discipline | `_STATUS.md` updated only via safe-update rule (`OPEN → INITIALIZED`) |
| Run record present | `_run_records/TASK_RUN_<timestamp>.md` exists with required headings |

## Records

- `Datasheet.md` — produced/updated
- `Specification.md` — produced/updated
- `Guidance.md` — produced/updated (including Conflict Table when needed)
- `Procedure.md` — produced/updated (this file)
- `_STATUS.md` — updated only when safe (`OPEN → INITIALIZED`)
- `_run_records/TASK_RUN_<timestamp>.md` — durable run record
