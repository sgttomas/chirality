# Procedure: DEL-01-04 Scope Boundary and Retired Scope Register

## Purpose

Define how to produce and maintain the Scope Boundary and Retired Scope Register for DEL-01-04 without expanding current scope, inventing unsupported facts, assigning human ownership, or reactivating retired work.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Deliverable-local context exists at `_CONTEXT.md`. | Available. |
| Authoritative source pointers exist at `_REFERENCES.md`. | Available; REF-006 `docs/PRD.md` matches under the current D-APP-38 corpus snapshot. |
| Decomposition entry exists for DEL-01-04. | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`. |
| Human-declared upstream dependencies. | TBD; `_DEPENDENCIES.md` declares none extracted yet. |
| ResponsibleParty assignment. | TBD; must remain TBD until human assignment. |

## Steps

1. Confirm the deliverable identity.
   - Verify `DeliverableID=DEL-01-04`, `PackageID=PKG-01`, `Type=DOC_UPDATE`, and `ResponsibleParty=TBD` in `_CONTEXT.md`.

2. Confirm overwrite safety.
   - Read `_STATUS.md`.
   - Proceed with P1/P2 authoring only if the current state is allowed by the task brief and skill contract.

3. Read source authority.
   - Read `_REFERENCES.md`.
   - Read accessible source slices from `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/PRD.md`, `docs/PLAN.md`, `docs/TYPES.md`, and the decomposition entry.
   - Confirm REF-006 `docs/PRD.md` matches the current D-APP-38 corpus version.

4. Build the out-of-scope register content.
   - Materialize the concrete register-row artifact in `Datasheet.md` under `Boundary Register Rows` unless a governed publication step moves the rows to a dedicated register file.
   - Include SOW-065 for remote MCP, plugins, remote execution, marketplace extension, and broad tool search before mature governance.
   - Include SOW-076 for ambient Claude settings and shipped/ordinary `bypassPermissions`.
   - Include SOW-078 for Windows/Linux release packaging.
   - Mark amendment requirements from `docs/DIRECTIVE.md` §7 and `docs/PRD.md` §12.1.

5. Build retired-scope notes.
   - Include SOW-077.
   - Record that retired PKG-08 execution-scope items remain retired unless amended.
   - Record that harness runtime event logging is separate runtime infrastructure and does not reactivate retired unified pipeline run records or broader PKG-08 hardening scope.

6. Build domain-operation boundary notes.
   - Record domain-engine operation execution as future-amendment scope.
   - Record that agents may write proposals and summaries, not protected model truth.
   - Record that applying domain operations requires explicit human acceptance.

7. Preserve unknowns and conflicts.
   - Use `TBD`, `ASSUMPTION`, `PROPOSAL`, or conflict-table entries for unsupported facts.
   - Do not create new scope items or assign ResponsibleParty.

8. Cross-check the four documents.
   - Confirm the same boundary items and terminology appear consistently in `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.
   - Confirm requirements in `Specification.md` have corresponding production and verification hooks here.
   - Use `docs/BOUNDARY_REVIEW_CHECKLISTS.md` as the normalized scope-boundary/professional-boundary review checklist.

9. Preserve current lifecycle state.
   - Current lifecycle state is `CHECKING`.
   - Do not perform a state regression or human-gate transition.
   - Any future `CHECKING -> ISSUED` transition requires the governed status workflow and human approval evidence.

10. Defer dependency extraction.
   - Do not create or edit `Dependencies.csv` during this four-documents run.
   - Treat any existing `Dependencies.csv` as output of the separate `TASK + dependency-extract` workflow described in `_DEPENDENCIES.md`.

## Verification

| Check | Expected Result |
|---|---|
| Document existence | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist and are non-empty. |
| Boundary coverage | SOW-065, SOW-076, SOW-077, and SOW-078 are represented. |
| Source grounding | Non-trivial boundary statements cite source files and sections. |
| ResponsibleParty | Remains `TBD`. |
| Boundary-row artifact | `Datasheet.md` includes concrete `Boundary Register Rows` with source reference, amendment trigger, current status, and human ruling fields. |
| Boundary review checklist | `docs/BOUNDARY_REVIEW_CHECKLISTS.md` exists and preserves checklist completion as evidence only. |
| Dependency extraction | This run does not create or edit `Dependencies.csv`; if present, it remains owned by the separate dependency-extract workflow. |
| Status | `_STATUS.md` remains `CHECKING`; no `CHECKING -> ISSUED` transition occurs in this checklist normalization. |
| Conflicts | Active path mismatch is surfaced for human ruling; historical PRD hash mismatch is closed by the current D-APP-38 corpus snapshot. |

## Records

Records produced or updated by this procedure:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` (read-only lifecycle evidence for this checklist normalization)
- `docs/BOUNDARY_REVIEW_CHECKLISTS.md`
- `_run_records/TASK_RUN_*.md`

Related derivative record owned by a separate workflow:

- `Dependencies.csv`
