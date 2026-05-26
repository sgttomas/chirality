# Procedure: DEL-046-01 — Scope of Work (PKG-046 Acid Gas Compressors)

## Purpose

Procedure to **produce** the EPC Scope of Work artifact for the Acid Gas Compressor package (`26020-01-PT-12-001`). This procedure is for the EPC Integrator (author) and reviewers; it does not cover operation of the compressor itself (operating procedures are vendor-supplied per DEL-046-04 and DEL-046-05).

Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-046-01.

## Prerequisites

### Required references and inputs

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- PROJECT_DECOMP GATE-07 snapshot:
  - `DELIVERABLE_REGISTER.csv` (row DEL-046-01)
  - `PACKAGE_REGISTER.csv` (row PKG-046)
  - `OBJECTIVE_DELIVERABLE_MAP.csv`
  - `INTERFACE_REGISTER.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, §Compression Configuration, §Acid Gas Injection Compression Basis, §Acid Gas Compressor Design Conditions, §Acid Gas Disposal Well Interface (lines 867-1061)
- `_Sources/26020-Package_Requirements.docx` package heading 1 — TBD (binary; extract slice if available)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 48 — TBD (binary; extract slice if available)

Source: `_REFERENCES.md`; `_CONTEXT.md` Source Reference.

### Declared upstream dependencies

- None declared during PREPARATION. Source: `_DEPENDENCIES.md`.

### Declared downstream dependencies

- None declared during PREPARATION; logical downstream consumers are DEL-046-02 through DEL-046-06. Source: `_DEPENDENCIES.md`; `DELIVERABLE_REGISTER.csv` PKG-046 rows.

## Steps

1. **Confirm scope identity.** Read `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row PKG-046. Record DeliverableID, package tag, vendor/EPC responsibility split, applicable interfaces, supported objectives, and source references. Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv`.
2. **Extract source slices.** Read the DBM Deepcut sections cited in §Prerequisites. Where binary sources are cited but not locally readable, record `location TBD` rather than fabricate values. Source: SKILL §Authority hierarchy; `4-25_Deepcut_DBM.md` lines 867-1061.
3. **Draft the package identity and tagged equipment list** for the Scope of Work narrative. Use values from Step 1 and Step 2 (configuration, package count, driver, model basis, capacity envelope). Source: Datasheet §Tagged Equipment and Package Identity.
4. **Draft the package function and integration narrative.** State the process function (compress amine acid gas for injection/disposal), upstream/downstream battery limits, and the shared 02-25 disposal well interface. Source: `4-25_Deepcut_DBM.md` §Acid Gas Injection Compression Basis; §Acid Gas Disposal Well Interface.
5. **Draft the Responsibility Assignment Record (RAR).** Map Package Vendor scope vs EPC Integrator scope per `PACKAGE_REGISTER.csv` Responsibility, plus the disposal well/pipeline exclusion and the Tourmaline-provided well pressure data dependency. Source: `PACKAGE_REGISTER.csv` Responsibility; `4-25_Deepcut_DBM.md` lines 84, 1049-1055.
6. **Enumerate covered scope items.** List `SOW-0047`, `SOW-0048`, `SOW-0049`, `SOW-0050` with `location TBD` notes where workbook row content is not locally readable. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.
7. **Enumerate supported objectives.** List `OBJ-001`, `OBJ-003..010` as ASSUMPTION (package-grouped heuristic) until human-confirmed. Source: `_CONTEXT.md`; SKILL §Step 1.3.
8. **Identify exclusions and TBDs.** Capture pipeline/well exclusion, 02-25 modification scope TBD, configuration alternative TBD, compressor model TBD, dry-out case TBC, disposal well pressure characteristics TBC, 5th-stage design discharge pressure reference TBD. Source: Guidance §Conflict Table.
9. **Cross-reference to companion deliverables.** Add explicit handoff pointers to DEL-046-02 (Package Datasheet), DEL-046-03 (Construction Work Package), DEL-046-04 (Vendor Engineered Equipment Package), DEL-046-05 (Vendor Document Turnover), DEL-046-06 (EPC Vendor Package Review and Acceptance). Source: `DELIVERABLE_REGISTER.csv` PKG-046 rows.
10. **Cross-document consistency check.** Verify that Datasheet identity/configuration values, Specification requirements, and Guidance Conflict Table entries align (terminology, package count, configuration basis, model basis, capacity values, exclusions). Source: SKILL §Step 5.
11. **Conflict logging.** For any source disagreement or unresolved item, add or update a row in `Guidance.md` §Conflict Table with provenance and a PROPOSAL; do not silently resolve. Source: SKILL §Step 5; this deliverable's `Guidance.md`.
12. **Provenance review.** Confirm each substantive claim cites a source slice (`SourcePath` + `SectionRef` or `location TBD`). Source: SKILL §Non-negotiable constraints.
13. **Status update.** If `_STATUS.md` Current State is `OPEN`, advance to `INITIALIZED` via `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Otherwise, leave `_STATUS.md` unchanged. Source: SKILL §Step 7.

## Verification

| Check | Pass criterion | Source |
|---|---|---|
| All four documents exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` are present in `DELIVERABLE_PATH` | SKILL §Non-negotiable constraints |
| Default schema sections present | Datasheet (Identification, Attributes, Conditions, Construction, References); Specification (Scope, Requirements, Standards, Verification, Documentation); Guidance (Purpose, Principles, Considerations, Trade-offs, Examples); Procedure (Purpose, Prerequisites, Steps, Verification, Records) | SKILL §Step 2 schema table |
| Source-grounded claims | Each non-trivial claim cites a source slice; unknowns marked `TBD`; inferences marked `ASSUMPTION` | SKILL §Non-negotiable constraints |
| Cross-document consistency | Terminology, configuration, capacity, and exclusions consistent across all four documents | SKILL §Step 5 |
| Conflicts captured | Unresolved items appear in `Guidance.md` §Conflict Table with provenance | SKILL §Step 5 |
| Status update safe | `_STATUS.md` only modified when current state is `OPEN`; no state regression | SKILL §Step 7 |
| No metadata file modified except `_STATUS.md` | `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md` unchanged | SKILL §Non-negotiable constraints |
| No writes outside `DELIVERABLE_PATH` | Run record confirms in-scope writes only | AGENT_TASK §Hard scope boundary |

## Records

The following evidence/records result from this procedure:

- The four documents in `DELIVERABLE_PATH`: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`.
- Updated `_STATUS.md` (when safe; `OPEN → INITIALIZED`).
- Run record at `{DELIVERABLE_PATH}/_run_records/TASK_RUN_<YYYY-MM-DD>_<HHmm>.md` with input echo, resolved state, tools used, outputs, missing items, dependency notes, and applied changes.
- `Guidance.md` §Conflict Table entries capturing items needing human ruling.
