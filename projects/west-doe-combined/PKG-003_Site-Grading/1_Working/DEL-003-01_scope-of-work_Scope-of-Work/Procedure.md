# Procedure: DEL-003-01_scope-of-work — Scope of Work

## Purpose

Define the procedure for producing and checking the `DEL-003-01_scope-of-work` Site Grading Scope of Work from accepted Gate 7 decomposition truth and locally accessible source material.

## Prerequisites

Before issuing or advancing the Scope of Work, confirm access to:

- deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`;
- Gate 7 final published PROJECT_DECOMP snapshot;
- Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`;
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 4;
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-11 civil/site grading source slices.

Declared upstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm deliverable identity.
   - Verify `DEL-003-01_scope-of-work`, Scope of Work, `PKG-003`, Site Grading, Civil discipline, EPC Integrator, and EPC Scope of Work against `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`.

2. Confirm package source basis.
   - Read Gate 7 `PACKAGE_REGISTER.csv` row `PKG-003` and workbook `Packages` sheet row 4.
   - Record WBS `01`, CoA tracking number `26020-01-42-003`, package name Site Grading, and discipline Civil.

3. Establish deliverable artifacts.
   - Read Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-003-01_scope-of-work`.
   - Include package scope of work, tagged equipment and package identity list, package function and whole-facility integration narrative, and responsibility assignment record.
   - Mark tagged equipment as TBD if no tag list is present in the accessible source slice.

4. Establish package interfaces.
   - Read workbook row 4 and Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-003`.
   - Record Drain / Containment and Grading / Site Drainage / Spill Containment.

5. Establish civil design-basis context.
   - Read DBM SEC-11 civil basis and Site Grading and Surface Water Management slices.
   - Carry source-supported surface-water management intent, retention pond basis, grading principles, and external-input dependencies.
   - Do not finalize survey-dependent, plot-plan-dependent, or detailed-drainage-dependent values.

6. Draft the Scope of Work content.
   - Include package identity, source basis, package function, interfaces, responsibility, scope boundaries, exclusions/TBDs, and downstream handoff notes.
   - Label inferred context as `ASSUMPTION` and unsupported values as `TBD`.

7. Cross-check against the specification.
   - Confirm each requirement in `Specification.md` has a corresponding scope-of-work content hook and verification method.

8. Prepare records for handoff.
   - Preserve open TBDs for downstream or human ruling.
   - Keep decomposition-derived packages and later aggregation/publication outputs derivative unless accepted by the owning workflow.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity check | Deliverable ID, package ID, package name, WBS, CoA tracking number, discipline, type, and responsible party match `_CONTEXT.md`, Gate 7 registers, and workbook row 4. |
| Interface check | Drain / Containment and Grading / Site Drainage / Spill Containment are both present; no unsupported interface type is added. |
| Artifact check | All four anticipated scope-of-work artifacts are represented. |
| Source-grounding check | Workbook and DBM facts cite their source slices; missing detailed design values remain TBD. |
| Status check | `_STATUS.md` is updated only from OPEN to INITIALIZED when the safe-update rule applies. |

## Records

Maintain or produce:

- `Datasheet.md`;
- `Specification.md`;
- `Guidance.md`, including open TBD items and Conflict Table;
- `Procedure.md`;
- `_STATUS.md` safe state history;
- `_run_records/TASK_RUN_*.md` run record.
