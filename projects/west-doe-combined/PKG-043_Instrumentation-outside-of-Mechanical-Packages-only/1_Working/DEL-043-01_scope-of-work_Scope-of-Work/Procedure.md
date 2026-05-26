# Procedure — DEL-043-01 Scope of Work

This procedure describes how to **produce** the EPC Integrator Scope of Work for PKG-043. It does not describe how to operate the resulting instrumentation; operating procedures are downstream of the Construction Work Package (DEL-043-03) and discipline production package (DEL-043-04).

## Purpose

Produce a source-grounded, boundary-clear Scope of Work for PKG-043 covering tagged equipment, package function, source basis, boundaries, and whole-facility integration narrative — satisfying the requirements in `Specification.md`.

## Prerequisites

| Prerequisite | Location | Status |
|---|---|---|
| Accepted decomposition snapshot | `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` | Accepted (Gate 7 final published) |
| Deliverable identity and context | `_CONTEXT.md` | Present |
| Reference index | `_REFERENCES.md` | Present |
| Declared dependencies | `_DEPENDENCIES.md` | Present (none declared) |
| Workbook 26020 Package Requirements | `_Sources/26020-Package_Requirements.docx` | Present (binary; clause-level extraction TBD) |
| DBM Deepcut basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` | Present (locally accessible) |
| Mechanical package equipment lists (for boundary check) | Other PKG-* deliverables in `projects/west-doe-combined/PKG-*` | TBD — verify availability before boundary cross-check |
| Project E&I specification set incl. ELC-QAS-000014-001 | TBD | Not locally accessible |

## Steps

1. **Confirm package identity.** Re-read `_CONTEXT.md` and PACKAGE_REGISTER.csv row PKG-043. Confirm DeliverableID, CoA tracking (26020-01-32-002), WBS (01), and PackageName.
2. **Extract tagged equipment from workbook row 45.** Open `_Sources/26020-Package_Requirements.docx` (or its extracted markdown form when produced) and isolate row 45 contents. Record the tagged-equipment list verbatim. If extraction is not yet performed, mark `TBD` in `Datasheet.md` §Construction with the workbook reference.
3. **Establish boundary against Mechanical packages.** Enumerate the Mechanical packages in the project and the instrumentation each owns. For each candidate instrument tag, decide INCLUDE (PKG-043) / EXCLUDE (Mechanical package). Document the exclusion list in `Specification.md` §Scope.
4. **Resolve overlap with consolidated 04-25 Instrument Air package.** Cross-check against DBM SEC-08 (L1822, L1906-1925). Apply the Conflict Table CONF-043-01-001 disposition once the human ruling is recorded; until then, carry as `TBD` / `ASSUMPTION`.
5. **Resolve overlap with analyzers and special instrumentation.** Cross-check against DBM SEC-08 (L2093 ff.). Record disposition.
6. **Confirm interface set.** For each interface type in PACKAGE_REGISTER (Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network), confirm active vs. not-confirmed per the InterfaceReviewNotes caveat. Update `Datasheet.md` §Conditions and `Specification.md` REQ-043-01-06.
7. **Draft whole-facility integration narrative.** Describe how PKG-043 integrates with each adjacent package (Mechanical packages, Instrument Air package, control system / DCS, ESD/SIS, fire-and-gas, electrical distribution). Cite DBM sections where applicable.
8. **Draft responsibility assignment record.** Identify EPC Integrator scope, discipline subcontractor scope (if assigned), and field-construction scope (per DBM L115 allocation). Mark unconfirmed assignments as `ASSUMPTION`.
9. **Cite governing specifications.** Reference ELC-QAS-000014-001 and the project E&I specification set (per DBM L2870, L2887). Mark `location TBD` for specifications not locally accessible.
10. **Mark unresolved items.** Use `TBD`, `ASSUMPTION`, or Conflict Table entries (in `Guidance.md`) for any item not source-supported. Do not invent values.
11. **Cross-document consistency sweep.** Verify terminology, tag identifiers, numeric values, and references are consistent across `Datasheet.md`, `Specification.md`, `Guidance.md`, and this `Procedure.md`.
12. **Record run.** Ensure a `_run_records/TASK_RUN_*.md` file documents the produced state, missing items, and any human rulings required.

## Verification

| Step | Verification check |
|---|---|
| 1 | Identity fields match PACKAGE_REGISTER row PKG-043 exactly. |
| 2 | Tagged-equipment list present or `TBD` with explicit workbook reference. |
| 3 | Boundary statement names Mechanical-package exclusion construct; cross-check log exists. |
| 4-5 | Conflict Table updated; no silent overlap. |
| 6 | Each interface type marked active / not-confirmed with rationale. |
| 7 | Integration narrative cites adjacent packages and DBM sections. |
| 8 | Responsibility record present; unconfirmed assignments labeled. |
| 9 | Governing specifications cited; missing locations marked `location TBD`. |
| 10 | No unsupported claims; all gaps are `TBD` / `ASSUMPTION` / Conflict. |
| 11 | Cross-document terminology/value consistency confirmed. |
| 12 | Run record present in `_run_records/`. |

## Records

Records produced by executing this procedure:

- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` in the deliverable folder.
- Tagged-equipment cross-check log (TBD — may live in `MEMORY.md` or a supplementary artifact).
- Conflict Table entries in `Guidance.md` requiring human ruling.
- `_STATUS.md` reflecting current lifecycle state.
- `_run_records/TASK_RUN_*.md` capturing the production run.
