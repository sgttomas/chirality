# Procedure: DEL-052-01 — Scope of Work, PKG-052 Inlet / TEG Dehy Cross Exchanger

This Procedure describes the steps to produce the EPC Integrator Scope of Work artifact for PKG-052. It is the operational counterpart to the normative Specification and the directional Guidance.

## Purpose

To produce a source-grounded EPC Integrator Scope of Work for PKG-052 that satisfies the four anticipated artifacts in _CONTEXT.md: package scope of work, tagged equipment and package identity list, package function and integration narrative, and responsibility assignment record.

## Prerequisites

- Accepted upstream PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. Source: _REFERENCES.md; _CONTEXT.md.
- Locally accessible reference materials:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — section "Inlet / TEG Dehy Cross Exchanger" and section "Interfaces". Required.
  - `_Sources/26020-Package_Requirements.docx` package heading 7. Available as binary; markdown slice TBD.
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 62. Available as binary; markdown slice TBD.
- Deliverable-local truth set present: `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md`.
- No declared upstream dependency blockers. Source: _DEPENDENCIES.md.

## Steps

1. **Confirm deliverable identity.** Open `_CONTEXT.md`. Confirm DeliverableID, ParentPackageID, Workbook row, Discipline, Responsible Party, Covers Scope Items, and Supports Objectives match PACKAGE_REGISTER.csv row 62 and DELIVERABLE_REGISTER.csv row 336. Verification: identity table in Datasheet.md.

2. **Extract package scope from authoritative sources.** Read PACKAGE_REGISTER.csv row 62 (columns: Package Name, Scope, Responsibility, Applicable interface types, Exclusions, Source). Read DBM-Deepcut section "Inlet / TEG Dehy Cross Exchanger" (design table and process function narrative) and section "Interfaces" (warm-side framing). Source: PACKAGE_REGISTER.csv row 62; DBM-Deepcut.

3. **Populate Datasheet (Identification, Attributes, Conditions, Construction, References).** Use only values explicitly present in the sources read in Step 2. Mark missing values TBD. Verification: each value carries a Source column entry that names file + section.

4. **Draft Specification scope, requirements, standards, verification, documentation.** Bind requirement R2.2 (warm-side identity) to the open conflict and reference Guidance Conflict Table CT-01. Bind Standards rows that are not source-stated to "location TBD" and ASSUMPTION. Verification: every R-numbered requirement carries a Source line.

5. **Draft Guidance principles, considerations, trade-offs, and Conflict Table.** Capture CT-01 (warm-side identity), CT-02 (sour-service materials), CT-03 (pressure vessel code). Verification: each conflict cites both Source A and Source B (or marks one as "not stated in accessible sources").

6. **Cross-check terminology and values across documents (Pass 2).** Confirm Datasheet, Specification, Guidance, and Procedure use the same package identity, equipment tag, design pressure, design temperature, and duty. Confirm warm-side identity is consistently flagged unresolved. Resolve any inconsistencies in-document; otherwise add a Conflict Table row.

7. **Update `_STATUS.md` (safe update).** If current state is `OPEN`, run: `tools/scaffolding/write_status.sh {DELIVERABLE_PATH} INITIALIZED TASK+four-documents`. Otherwise skip and record in run report. Source: SKILL.md Step 7.

## Verification

| Check | Method |
|---|---|
| All four documents exist in `{DELIVERABLE_PATH}` | Directory listing |
| Default schema sections present in each document | Heading scan |
| At least one locally accessible reference was consulted from `_REFERENCES.md` | Citation scan (DBM-Deepcut cited) |
| Every non-trivial value carries SourcePath + SectionRef or "location TBD" | Source-column scan |
| Cross-document terminology and values consistent (Pass 2) | Manual cross-check; conflicts captured in Guidance CT-01..CT-03 |
| `_STATUS.md` updated only when current state was `OPEN` | Status history line |
| Run record persisted at `_run_records/TASK_RUN_<timestamp>.md` | File present |

## Records

The following records result from this Procedure and constitute the evidence trail for DEL-052-01:

1. `Datasheet.md` — tagged equipment and package identity list, process conditions, boundaries.
2. `Specification.md` — normative scope, requirements R1–R6, standards (with TBDs), verification matrix, documentation list.
3. `Guidance.md` — purpose, principles, considerations, trade-offs, and Conflict Table CT-01..CT-03.
4. `Procedure.md` — this document.
5. `_STATUS.md` — state transition `OPEN -> INITIALIZED` (when applicable).
6. `_run_records/TASK_RUN_<timestamp>.md` — TASK + four-documents run record with input echo, resolved state, tools used, and outputs.
