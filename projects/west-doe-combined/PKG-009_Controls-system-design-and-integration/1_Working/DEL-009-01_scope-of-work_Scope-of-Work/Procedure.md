# Procedure: DEL-009-01_scope-of-work - Scope of Work

## Purpose

Define the working procedure for producing, checking, and handing off the EPC Scope of Work for DEL-009-01_scope-of-work, PKG-009 Controls system design and integration.

## Prerequisites

- Accepted Gate 7 final published PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Current deliverable state allows overwrite under the active four-documents workflow.
- Declared upstream dependencies are reviewed. For this run, none are declared.
- Source limitations are understood: no deliverable-specific source slices were copied during PREPARATION.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`.
2. Confirm package identity from `PACKAGE_REGISTER.csv`, including PKG-009, WBS 02, workbook row 10, discipline Controls, and CoA tracking number 26020-01-32-001.
3. Confirm SOW-0009 in `SCOPE_LEDGER.csv`.
4. Build the scope-of-work content around the four anticipated artifacts:
   - Package scope of work.
   - Tagged equipment and package identity list.
   - Package function and whole-facility integration narrative.
   - Responsibility assignment record.
5. Add source-basis and boundary language naming the Gate 7 snapshot and Workbook Packages row 10.
6. Carry applicable interface types from `PACKAGE_REGISTER.csv` and `INTERFACE_REGISTER.csv` as high-level scope and boundary context.
7. Carry mapped objectives from `OBJECTIVE_DELIVERABLE_MAP.csv` as traceability context.
8. Mark unavailable package-specific exclusions, design values, equipment counts, standards clauses, and unresolved source slices as TBD.
9. Check the draft against `Specification.md` requirements REQ-001 through REQ-008.
10. Record unresolved source gaps or conflicts for human ruling when they affect deliverable closure.

## Verification

| Check | Acceptance basis |
|---|---|
| Identity complete | DEL-009-01_scope-of-work, PKG-009, WBS 02, workbook row 10, discipline Controls, and EPC Integrator responsibility are present. |
| Scope item correct | SOW-0009 is present and no sibling package scope is substituted. |
| Artifacts complete | Four anticipated artifacts from the accepted snapshot are present. |
| Interfaces consistent | Interface types match `PACKAGE_REGISTER.csv` and `INTERFACE_REGISTER.csv`. |
| Source-limited details controlled | Unsupported details are marked TBD or ASSUMPTION rather than asserted. |
| Dependency blockers checked | Declared dependency lists are checked; no blockers are asserted without declared edges. |
| Cross-document consistency | Datasheet, Specification, Guidance, and Procedure use the same package identity, objective list, interface list, and source-basis wording. |

## Records

- Completed Scope of Work production document or draft package.
- Requirements verification checklist.
- TBD/open-item list for source gaps.
- Responsibility assignment record.
- Source-basis record citing the accepted Gate 7 snapshot.
- This four-document kit as Phase 2.2 initialization evidence.
