# Procedure — DEL-044-01 Scope of Work

Operational procedure to produce the EPC Integrator Scope of Work for PKG-044.

## Purpose

Produce the four artifacts that constitute the Scope of Work for PKG-044 (`_CONTEXT.md`; `ARTIFACT_REGISTER.csv`):

- Package scope of work (ART-E806968D4A).
- Tagged equipment and package identity list (ART-764F78E24A).
- Package function and whole-facility integration narrative (ART-0F86ED2722).
- Package responsibility assignment record (ART-42A035696B).

## Prerequisites

- Accepted GATE-07 Final Published PROJECT_DECOMP snapshot (2026-05-24) available at the path in `_REFERENCES.md`.
- Read access to the following snapshot files:
  - `DELIVERABLE_REGISTER.csv`
  - `PACKAGE_REGISTER.csv`
  - `ARTIFACT_REGISTER.csv`
  - `INTERFACE_REGISTER.csv`
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
  - `OBJECTIVE_PACKAGE_MAP.csv`
  - `SCOPE_LEDGER.csv`
- Read access to `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Workbook) to extract Workbook Packages row 46.
- Read access to `_Sources/26020-Package_Requirements.docx` for project-wide package requirement language.
- Read access to `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (cited as DBM pointer in `PACKAGE_REGISTER.csv`).
- Deliverable folder Specification.md, Datasheet.md, and Guidance.md drafted (this iteration).
- `_DEPENDENCIES.md` declares no Upstream/Downstream edges; no upstream blockers to satisfy.

## Steps

1. **Open the snapshot rows.** From the GATE-07 snapshot, isolate every row containing `PKG-044` or `DEL-044-01` across the seven registers listed under Prerequisites. Verify the row set is internally consistent (package, deliverable, artifacts, interfaces, objectives, scope ledger).
2. **Extract Workbook Packages row 46.** Open the workbook source and read row 46 in full. Record: package name, workbook ID, CoA tracking number, WBS, discipline, tagged-equipment text, exclusions text, and any inclusion/exclusion qualifiers. Tagged equipment text resolves REQ-044-01-008; if absent in the row, record TBD with rationale.
3. **Draft the Package Scope of Work artifact (ART-E806968D4A).** Compose package identification (REQ-044-01-001..003), package function and integration framing (REQ-044-01-004), scope boundaries (in/out of scope), and provenance header citing GATE-07 snapshot (REQ-044-01-012). Use Specification.md as the requirement checklist.
4. **Draft the Tagged Equipment and Package Identity List (ART-764F78E24A).** Populate from Workbook Packages row 46 equipment text. Where source text is absent, list "TBD — Workbook Packages row 46 (Excel) extraction pending" rather than inventing equipment. Cite the workbook row for each entry.
5. **Draft the Package Function and Whole-Facility Integration Narrative (ART-0F86ED2722).** Describe what PKG-044 does, framed by WBS 02 placement and the plug-n-play package philosophy. Enumerate the five recorded interface types and cite their interface register IDs (REQ-044-01-005). Include the boundary caveat verbatim (REQ-044-01-006) and Gate 6 disposition (REQ-044-01-007).
6. **Draft the Package Responsibility Assignment Record (ART-42A035696B).** Record EPC Integrator as the responsible party for delivering the SoW (REQ-044-01-003). For execution-level responsibility allocation between EPC Integrator and discipline subcontractor, record TBD with citation to `PACKAGE_REGISTER.csv` Notes ("source-dependent; no separate vendor-package ownership model is inferred") and flag for human ruling.
7. **Link objectives.** Add the supported objectives section listing OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010 with citation to `OBJECTIVE_DELIVERABLE_MAP.csv` (REQ-044-01-009). Note PACKAGE_HEURISTIC association mode as ASSUMPTION pending human confirmation.
8. **Cross-check against Specification.md.** Walk each REQ-044-01-xxx row and confirm the SoW artifact addresses it. For any unmet requirement, either resolve or carry as a labeled TBD with rationale and cited gap.
9. **Cross-check against Guidance.md.** Confirm narrative tone and trade-offs align with Guidance; in particular, do not over-claim field supports/power/comms inclusion and do not absorb sibling-deliverable scope.
10. **Provenance audit.** Inspect each non-trivial sentence in the four artifacts. Each MUST cite a register row, a source row, or carry an explicit ASSUMPTION or TBD label (REQ-044-01-011; K-PROV-1).
11. **Issue and log.** Place the four artifacts in the deliverable folder per its publishing convention (TBD: not specified by `_CONTEXT.md`). Update `MEMORY.md` with any durable rulings, conflicts encountered, or open items. Do not modify `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md`, or `_SEMANTIC_LENSING.md`. Run `tools/scaffolding/write_status.sh` to advance `_STATUS.md` only along the authorized lifecycle path (OPEN → INITIALIZED on this skill run; later transitions belong to subsequent runs/agents).

## Verification

- All four artifacts (ART-E806968D4A, ART-764F78E24A, ART-0F86ED2722, ART-42A035696B) are present in the deliverable folder.
- Every requirement REQ-044-01-001..012 in Specification.md is addressed or carries a labeled TBD with cited rationale.
- All five PKG-044 interface IDs are enumerated and cited in the integration narrative.
- Boundary caveat and Gate 6 disposition appear verbatim where required.
- Provenance audit (Step 10) passes; no unsourced assertions remain.
- Objectives section lists exactly OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010 with PACKAGE_HEURISTIC association labeled ASSUMPTION.
- `_STATUS.md` advanced only as authorized; no other metadata files modified.
- Cross-document term and value consistency confirmed against Datasheet.md, Specification.md, and Guidance.md.

## Records

- The four SoW artifacts in the deliverable folder.
- Run record at `_run_records/TASK_RUN_<timestamp>.md` documenting inputs, tools, outputs, missing items, and dependencies.
- `_STATUS.md` history line recording the transition with the run actor (`TASK+four-documents`).
- Any conflicts surfaced go to Guidance.md's Conflict Table; any human rulings required are listed in `Needs Human Ruling` of the run record.
- Reference to GATE-07 PROJECT_DECOMP snapshot path captured in artifact headers.
