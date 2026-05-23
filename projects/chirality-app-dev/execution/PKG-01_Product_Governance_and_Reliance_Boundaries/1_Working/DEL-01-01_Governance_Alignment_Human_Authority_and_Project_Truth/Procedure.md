# Procedure: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

## Purpose

This procedure describes how to produce and use the DEL-01-01 governance-alignment artifacts while preserving human authority, project truth, accepted git evidence, and runtime-audit boundaries.

## Prerequisites

| Prerequisite | Status |
|---|---|
| Deliverable-local context files exist: `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md`, `_SEMANTIC_LENSING.md` | Present at P3 enrichment. |
| Current lifecycle state permits four-document enrichment | `INITIALIZED`; P3 may enrich the four-document kit but does not transition `_STATUS.md` under the local status policy. |
| Authoritative references are locally accessible | Accessible; PRD has known hash mismatch warning. |
| Upstream dependencies | TBD; no accepted dependency edges extracted yet. |
| Downstream dependencies | TBD; no accepted dependency edges extracted yet. |
| Human owner | `ResponsibleParty: TBD`. |

## Steps

1. Confirm scope identity.
   - Verify `PackageID=PKG-01`, `DeliverableID=DEL-01-01`, `Type=DOC_UPDATE`, and `ResponsibleParty=TBD` against `_CONTEXT.md` and SOFTWARE_DECOMP v3.2.
   - If path labels disagree but stable IDs match, record the mismatch as a source warning or human-ruling-needed item.

2. Check source status.
   - Read `_REFERENCES.md`.
   - Confirm hash status for each source.
   - Treat the REF-006 PRD hash mismatch as a warning for this run, not a blocker.
   - Do not treat the source warning as clean reliance until the exact reference row, accepted hash update, or explicit human bypass decision is recorded.
   - Mark any inaccessible or unsupported source-dependent content as `TBD`.

3. Build governance consistency notes.
   - Compare changes against the authority order in `docs/DIRECTIVE.md`.
   - Check CONTRACT invariant families owned or co-owned by PKG-01: project truth, human authority, binding/non-binding records, gates, professional boundary, reliance boundaries, SDK identity, lifecycle, invention/conflict discipline, validation/release boundaries, and retired scope.
   - Record conflicts rather than resolving them silently.

4. Build the human-authority checklist.
   - Check that no document, UI copy, runtime event, SDK behavior, tool, validator, agent, or domain adapter claims to approve, certify, sign, seal, issue, transmit, externally validate, or make professional work reliable by itself.
   - Check that CHECKING, ISSUED, domain-operation acceptance, residual-risk acceptance, and source-conflict rulings remain human-gated where applicable.

5. Build the project-truth checklist.
   - Check that reliance-relevant facts land in versioned project files or accepted artifacts.
   - Check that hidden app state, chat, SDK transcripts, runtime logs, model context, caches, UI state, API keys, provider transcripts, and convenience state are not treated as project truth unless imported by governance.
   - Check that accepted decisions bind to git SHA or equivalent immutable evidence where approval is claimed.

6. Build the runtime-audit boundary checklist.
   - Check that `.chirality/sessions/<sessionId>/events.jsonl` remains the Chirality-owned runtime audit mirror.
   - Check that SDK transcripts remain secondary runtime state unless imported into `HarnessEvent` form or a governed artifact.
   - Check that runtime events explain execution and do not approve deliverables.

7. Build the document diff checklist.
   - Review `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, and active SOFTWARE_DECOMP changes for mutual consistency.
   - Confirm SOW-074, SOW-075, and OBJ-009 remain satisfied.
   - Flag lower-authority conflicts with higher-authority sources for human ruling.

8. Build the acceptance checklist.
   - Confirm every P0 reliance boundary referenced by this deliverable has a documented enforcement surface or open gap.
   - Confirm unknowns are marked `TBD`, `ASSUMPTION`, `PROPOSAL`, source warning, or human-ruling-needed.
   - Confirm dependency extraction remains deferred unless a later task explicitly authorizes it.

9. Record results.
   - Write outputs to authorized deliverable-local artifacts only.
   - Do not create `Dependencies.csv` in this P1/P2 run.
   - For P3 enrichment, preserve `_STATUS.md` unless an explicit governed status policy authorizes a transition.

## Verification

| Check | Pass condition |
|---|---|
| Four-doc kit | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist and are non-empty. |
| Lifecycle | `_STATUS.md` reads `Current State: INITIALIZED` only after the four-doc kit exists. |
| Source warnings | PRD hash mismatch and dispatch path mismatch are visible for human ruling. |
| Responsible party | `ResponsibleParty` remains `TBD`. |
| Dependency deferral | `Dependencies.csv` is not created. |
| No invention | Unsupported facts are `TBD`, `ASSUMPTION`, `PROPOSAL`, conflict, source warning, or human-ruling-needed. |
| Boundary posture | Human authority, project truth, and runtime-audit boundaries are not weakened by the drafted artifacts. |
| Immutable acceptance evidence | Governance notes or checklist outputs used as acceptance evidence are bound to a git SHA or equivalent immutable evidence, and a separate accountable human approval record exists. |

## Records

| Record | Status |
|---|---|
| `Datasheet.md` | Produced by this P1/P2 run. |
| `Specification.md` | Produced by this P1/P2 run. |
| `Guidance.md` | Produced by this P1/P2 run. |
| `Procedure.md` | Produced by this P1/P2 run. |
| `_STATUS.md` | Updated to `INITIALIZED` only after non-empty four-doc kit verification. |
| `_run_records/TASK_RUN_2026-05-20_1610.md` | Durable run record for this task. |
| P3 run record | Records semantic-lensing dispositions, source rereads, validation results, and status policy outcome. |
| Dependency records | Not created or updated by this P3 run. |
