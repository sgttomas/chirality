# Procedure: DEL-042-01_scope-of-work — Scope of Work (PKG-042)

Operational procedure to **produce** the EPC Scope of Work artifact for PKG-042 "Control Room Building". This procedure operationalizes the Specification requirements.

## Purpose

Produce a source-grounded, decomposition-consistent EPC Scope of Work for PKG-042 that satisfies the requirements in `Specification.md` and is suitable for Gate 5 issuance.

## Prerequisites

- Decomposition snapshot accepted and accessible: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`. [`_REFERENCES.md`]
- Workbook source file present: `_Sources/26020-Packages_Interfaces_4_export.xlsx`. [`_Sources/` listing]
- Package requirements document present: `_Sources/26020-Package_Requirements.docx`. [`_Sources/` listing]
- DBM folders present: `_Sources/DBM-Comp_and_Liquids/`, `_Sources/DBM-Deepcut/`. [`_Sources/` listing]
- Declared upstream dependencies: none declared during PREPARATION. [`_DEPENDENCIES.md`]
- This deliverable's `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` read. [skill Step 1]
- `_STATUS.md` `Current State` is in `ALLOW_OVERWRITE_STATES` (`OPEN`, `INITIALIZED`). [skill Step 0]

## Steps

1. **Open the package row.** Read Workbook row 44 from `26020-Packages_Interfaces_4_export.xlsx`. Capture: package name, workbook ID (42), CoA tracking number (26020-03-39-010), WBS (03), discipline (Electrical), function statement, responsibility model, applicable interface types, exclusions, detailed major-equipment text (if any). Record direct quotations where the text will be carried verbatim into the Scope of Work. [`PACKAGE_REGISTER.csv` confirms expected values]
2. **Identify supporting source slices.** From the `_Sources/` tree, open the DBM section(s) most plausibly relevant to a Control Room Building (e.g., electrical basis, controls/communications basis, instrumented protection basis, civil/buildings basis). Capture section references that will be cited. If no DBM section addresses the Control Room Building directly, record this as an open item rather than fabricating a citation. [skill source-grounding rule]
3. **Populate Identification.** Fill the Identification block of the Scope of Work artifact using the exact values from PACKAGE_REGISTER.csv for PKG-042. Verify match against `Datasheet.md` Identification table.
4. **Draft the package function and whole-facility integration narrative.** Write a short narrative (1–3 paragraphs) describing what the Control Room Building does and how it integrates into the process facility, grounded in Workbook row 44 function text and accessible DBM sections. Mark any inferred claim as `ASSUMPTION`. Satisfies REQ-042-01-02 and produces ART-B33959740B.
5. **Draft the tagged-equipment and package-identity list.** Render package name, workbook ID, CoA tracking number, WBS, and detailed major-equipment text from the Workbook row 44 source slice. Mark unsupported entries `TBD`. Satisfies REQ-042-01-06 and produces ART-09426CDD36.
6. **Draft the responsibility assignment record.** Reproduce the responsibility model verbatim-faithfully (Package Vendor scope vs. EPC Integrator scope) from PACKAGE_REGISTER.csv ResponsibilityModel. Satisfies REQ-042-01-03/04 and produces ART-93D323D241.
7. **Enumerate the integration interface boundary.** List all interface types flagged for PKG-042 per the `applicable interface types` column on PACKAGE_REGISTER.csv and the corresponding `IFC-*` rows in `INTERFACE_REGISTER.csv`. Point the reader to DEL-042-02 (Package Datasheet) for per-interface battery limits and tie-in details. Satisfies REQ-042-01-05.
8. **State exclusions.** If Workbook row 44 carries package-specific exclusions, list them. Otherwise record "no package-specific exclusions stated in source". Satisfies REQ-042-01-09.
9. **Record supported objectives as ASSUMPTION.** List OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 with the explicit `ASSUMPTION (best-effort PACKAGE_HEURISTIC mapping)` label. Satisfies REQ-042-01-10.
10. **Cite sources.** Each non-trivial claim references `PACKAGE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `SCOPE_LEDGER.csv`, `ARTIFACT_REGISTER.csv`, Workbook row 44, or the relevant DBM section. Where the exact section is unknown, write `location TBD`. Satisfies REQ-042-01-07.
11. **Cross-check against scope ledger.** Confirm the Scope of Work is consistent with `SCOPE_LEDGER.csv` row `SOW-0043` and does not modify decomposition-defined scope. Satisfies REQ-042-01-08.
12. **Self-review for conflicts.** Run the Conflict Table checks in `Guidance.md`; surface any new conflicts; do not silently reconcile.

## Verification

| Check | Pass Criterion |
|---|---|
| Identification block matches PACKAGE_REGISTER.csv | All seven identification fields equal source values |
| Function & integration narrative present | ART-B33959740B drafted with citations |
| Tagged equipment list present | ART-09426CDD36 drafted; unsupported items marked `TBD` |
| Responsibility record present | ART-93D323D241 drafted; exact split preserved |
| Interface types enumerated | All flagged types from PACKAGE_REGISTER and IFC-* rows listed |
| Exclusions stated | Explicit list or explicit "no exclusions stated in source" |
| Supported objectives recorded | List present with `ASSUMPTION` label |
| Sources cited | Every non-trivial claim has SourcePath + SectionRef or `location TBD` |
| Scope ledger consistency | No conflict with SOW-0043 |
| Conflict Table reviewed | All conflicts captured or resolved with citation |
| `_STATUS.md` safe update | If `Current State = OPEN`, set to `INITIALIZED` after Pass 1/2 |

## Records

The following records SHOULD result from execution of this procedure (some are produced by this skill run; others by downstream runs):

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` populated in this deliverable folder.
- `_STATUS.md` updated `OPEN → INITIALIZED` (this run, if applicable).
- `_run_records/TASK_RUN_<timestamp>.md` recording inputs, sources read, outputs produced, conflicts, and TBDs (this run).
- Future: `_SEMANTIC_LENSING.md` produced by the `lens-register` skill, and a Pass 3 enrichment run record.
- Future: Conflict Table dispositions ruled by a human reviewer.
