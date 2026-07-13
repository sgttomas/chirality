# Procedure: DEL-07-06 Reference Hash and Snapshot Conventions

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Purpose

Use this procedure to produce or review the DEL-07-06 convention notes: snapshot/runbook notes, hash bypass convention, and CHANGE/SHA checklist.

## Prerequisites

| Prerequisite | Status / Source |
|---|---|
| Deliverable-local context, references, dependencies, and status files are present. | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` |
| Current lifecycle state permits drafting. | `_STATUS.md` was `OPEN` at P1/P2 start |
| Authoritative sources are locally accessible. | `_REFERENCES.md` REF-001 through REF-007; REF-006 has MATCH status — reconciled under D-APP-38 |
| Accepted dependency edges are available. | TBD: `_DEPENDENCIES.md` declares no accepted upstream/downstream edges yet |
| Human owner is assigned. | TBD: `_CONTEXT.md` preserves `ResponsibleParty: TBD` |

## Steps

1. Confirm source state.
   - Read `_REFERENCES.md`.
   - Record the status of each authoritative reference.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

2. Confirm scope boundary.
   - Use `_CONTEXT.md` and the decomposition row for DEL-07-06.
   - Confirm the deliverable covers SOW-032, SOW-033, and SOW-034.
   - Confirm the work remains a `DOC_UPDATE`, not an implementation task.

3. Draft snapshot/runbook notes.
   - State that snapshot-producing workflows should create timestamped immutable folders.
   - State that `_LATEST.md` pointers may move when the owning workflow permits.
   - State that accepted snapshots must not be overwritten.
   - Cite `docs/SPEC.md` Section 2 and `docs/CONTRACT.md` K-SNAP-1.

4. Draft the hash bypass convention.
   - State that `_REFERENCES.md` carries source references and hash notes.
   - State that out-of-folder references should include content hashes when tooling is available.
   - State that hash bypasses require human approval and durable bypass records.
   - When a concrete bypass is used, confirm the review package includes both human approval evidence and the durable bypass record before treating the bypass as accepted.
   - Identify `HASH_VERIFICATION_BYPASS.jsonl` as the deliverable-local bypass record surface where applicable.
   - Cite `docs/SPEC.md` Sections 3.1 and 5.3.

5. Draft the CHANGE/SHA checklist.
   - Confirm candidate content evidence and action list are recorded before approval.
   - Confirm human approval evidence is present and SHA-like where required.
   - Before any `CHECKING` or `ISSUED` transition, confirm approval SHA evidence exists for the exact candidate content under review.
   - Recheck HEAD/current candidate content before executing approved CHANGE/publication actions.
   - State that content changed after approval requires renewed review.
   - Cite `docs/DIRECTIVE.md` Section 2.4, `docs/CONTRACT.md` K-AUTH-2, and `docs/PRD.md` FR-063 with REF-006 hash warning.

6. Guard retired scope.
   - Confirm the convention notes do not reactivate execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record persistence, or automated staleness propagation.
   - Cite `docs/PLAN.md` Section 9 and `docs/PRD.md` KG-012 with REF-006 hash warning.

7. Confirm human-authority language.
   - Remove any wording implying that an agent, SDK, tool, runtime event, validator, or adapter approves, issues, certifies, signs, seals, or externally validates work.
   - Cite `docs/DIRECTIVE.md` Sections 2.3-2.4 and `docs/CONTRACT.md` K-AUTH-1/K-BIND-1.

8. Run cross-document consistency check.
   - Confirm Datasheet attributes map to Specification requirements.
   - Confirm Specification verification rows have corresponding procedure steps.
   - Confirm Guidance source warnings match Datasheet and Specification warning language.
   - Leave unresolved values as `TBD` and list human rulings in Guidance.

## Verification

| Check | Acceptance |
|---|---|
| Source-state warning | REF-006 `docs/PRD.md` hash status: MATCH is visible anywhere PRD-derived requirements or examples are used. — reconciled under D-APP-38 |
| Snapshot convention | Notes include timestamped immutable folders, optional `_LATEST.md`, and non-overwrite of accepted snapshots. |
| Hash bypass convention | Notes include human approval, durable bypass record, and `HASH_VERIFICATION_BYPASS.jsonl` where applicable. |
| Hash bypass evidence | If a bypass is used, review confirms explicit human approval evidence and a durable bypass record exist before accepting the bypass. |
| CHANGE/SHA checklist | Notes include candidate evidence, approval token/SHA, approval SHA evidence before `CHECKING` or `ISSUED`, HEAD/current-content recheck, and renewed review after content changes. |
| Retired scope | No current commitment is made for retired execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record persistence, or automated staleness propagation. |
| Human authority | No automated approval, signing, sealing, issue, certification, external validation, or professional reliance claim is introduced. |

## Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` for DEL-07-06.
- `_run_records/TASK_RUN_*.md` capturing the TASK run and source-state warnings.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
- Future exact deterministic tool/script registry evidence: TBD unless produced by the owning implementation slice.
- Future accepted dependency edge record source: TBD until `_DEPENDENCIES.md` or `Dependencies.csv` records accepted upstream/downstream edge availability.

## Pass 3 Disposition Notes

| Item ID | Disposition | Evidence |
|---|---|---|
| F-001 | Converted to explicit `TBD`; dependency edge availability remains unresolved until an accepted dependency record source is present. | Prerequisites; Records |
| D-001 | Incorporated; the CHANGE/SHA checklist now requires approval SHA evidence before any `CHECKING` or `ISSUED` transition. | Steps; Verification |
| X-001 | Incorporated; bypass review now requires human approval evidence and a durable bypass record when a bypass is used. | Steps; Verification |
