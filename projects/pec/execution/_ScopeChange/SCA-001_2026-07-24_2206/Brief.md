---
amendment_id: SCA-001
doc_kind: scope_change.brief
decomp_variant: SOFTWARE
gate: 1
created: 2026-07-24
status: awaiting_gate_1_confirmation
authority: D-PEC-61
---

# SCA-001 — Directed Full-DAG Self-Bootstrap

## Human initiation

Owner direction of record is `D-PEC-61`, which records the in-session
instruction:

> "PLEASE IMPLEMENT THIS PLAN:"

The accompanying owner-authored plan, titled `PEC SCA-001 — Directed
Full-DAG Self-Bootstrap`, is incorporated by reference as the exact request.
It adopts PRD v2.1, selects `FULL_GRAPH` for PEC Project Setup, opens this
five-gate amendment, and preserves separate owner approval at every
SCOPE_CHANGE gate.

## Normalized session parameters

| Parameter | Value |
|---|---|
| `DECOMP_VARIANT` | `SOFTWARE` |
| `CONTEXT_ROOT` | `projects/pec/execution` |
| `DECOMPOSITION_PATH` | `projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md` |
| `SCOPE_CHANGE_ROOT` | `projects/pec/execution/_ScopeChange` |
| `AMENDMENT_ID` | `SCA-001` |
| `ALLOW_RENUMBERING` | `false` |
| Owner packet | `D-PEC-61` |
| Selected Project Setup representation | `FULL_GRAPH` |
| Current gate | Gate 1 — intake and validation |

## Accepted basis resolved

- `execution/_Decomposition/_LATEST.md` identifies
  `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 1.0 as the accepted
  current basis under `D-PEC-60`.
- The accepted topology is 94 scope items, 64 deliverables, 11 packages, and
  6 objectives.
- Revision 1.0 declares PRD v2.0 (`D-PEC-58`) as its source corpus. PRD v2.1
  is now adopted by `D-PEC-61`; reconciling that temporary source-basis drift
  is part of this amendment.
- `PROJECT_SETUP` is held by `D-PEC-61` until an accepted SCA-001 successor
  exists. This Gate 1 record does not release that hold.

## Parsed atomic actions

| Ref | ActionType | EntityType | EntityID | Requested change | Affected semantic sections |
|---|---|---|---|---|---|
| A001 | `MODIFY` | `OTHER` | Hard Constraints (§1.3) | Add C16, Directed Self-Bootstrap: `FULL_GRAPH` is the seed representation; capability production precedes consumption; no node depends on the capability it creates; discoveries route to evidence-linked candidates and human gates; file-native fallback remains operable. | Intake constraints; constraint references; decision log; revision/source basis |
| A002 | `MODIFY` | `OTHER` | `SOW-064` | Expand one-time self-ingestion into progressive full-DAG self-ingestion and boundary-discovery evidence; cite PRD v2.1 §12 and `D-PEC-61`; map to `OBJ-006`. | SSOW; `ScopeLedger.csv`; objective mapping; coverage/source basis |
| A003 | `MODIFY` | `DELIVERABLE` | `DEL-10-10` | Rename to “Directed bootstrap self-ingest validation”; keep P1 introduction and standing use thereafter; require a bootstrap progression record covering DAG ingestion, capability cutovers, observed friction, proposed/rejected/unnecessary functions, fallback evidence, and amendment routes; add `OBJ-006`; change Context Envelope `S` → `M`. | Deliverables; `Deliverables.csv`; `ContextBudgetQA.csv`; objective mapping; coverage |
| A004 | `MODIFY` | `OTHER` | Decomposition summaries and traceability | Reconcile OBJ-006 mapped items/deliverables, source-corpus references, coverage summary, decision log, and revision history for revision 1.1 while preserving all stable IDs and topology counts. | Objectives; intake/source corpus; coverage and telemetry; decision log; revision history; decomposition handoff pointer |

`A001` is classified as `MODIFY OTHER`, rather than `ADD`, because it amends
the existing Hard Constraints semantic section. C16 is a new row within that
section, does not collide with C1–C15, and creates no product entity or
topology member.

## Gate 1 validation

| Action | Validation result | Evidence |
|---|---|---|
| A001 | `PASS` | Hard Constraints §1.3 exists and currently ends at C15; adding C16 is a valid section-level attribute/narrative modification. |
| A002 | `PASS` | `SOW-064` exists, is `IN`, maps to `PKG-10` and `DEL-10-10`, and currently has no objective mapping. The requested fields are valid Scope Ledger fields. |
| A003 | `PASS` | `DEL-10-10` exists in `PKG-10`, covers `SOW-064`, is `TEST_SUITE`, has envelope `S`, and has `PhaseHint=P1`. Matching QA row exists with envelope `S`. |
| A004 | `PASS` | OBJ-006, source-corpus references, coverage summary, decision log, revision history, and `_LATEST.md` all exist as amendment-capable surfaces. |

No action removes, reclassifies, merges, splits, or renumbers a package,
deliverable, objective, or scope item. The parent-closure rule is therefore
not triggered. The request is a narrowly bounded contract/acceptance
clarification, not a decomposition-ontology change.

## Pre-change evidence

### `AUDIT_DECOMP`

The governed read-only audit is preserved at:

`execution/_Evaluation/DecompCoverage/COV_SCA001_PRECHANGE_2026-07-24_2209/`

Its `RUN_STATUS` is `FAILED_INPUTS`, as expected before Project Setup:

- the execution root and decomposition are readable;
- 11 packages and 64 deliverables are declared;
- zero folders match
  `execution/PKG-XX_*/1_Working/DEL-XX-YY_*/`.

This is not a negative filesystem-coverage verdict. Under the
`AUDIT_DECOMP` contract it means filesystem coverage cannot yet be measured.

### Deterministic register-integrity baseline

`Pre_Change_Coverage.json` records the usable Gate 1 baseline:

- 94 scope items: 71 `IN`, 14 `OUT`, 9 `TBD`;
- 11 packages, 64 deliverables, 6 objectives;
- all `IN` rows have exactly one package and one deliverable;
- all forward and reverse scope/deliverable references resolve;
- package lineage and `DEL-XX-YY` parent coupling pass;
- all 64 deliverables have one Context Budget QA row and matching envelope;
- all companion-inventory paths exist;
- target pre-change values for `SOW-064`, `DEL-10-10`, and its QA row are
  captured with SHA-256 hashes for the accepted package.

## Warnings and unknowns

1. **Expected audit limitation:** filesystem coverage is unavailable until
   Project Setup scaffolds package and deliverable folders.
2. **Telemetry label:** decomposition front matter and `_LATEST.md` say
   revision 1.0, while the Coverage & Telemetry table retains the Phase 6
   validation label “Revision 0.9.” Gate 3 must state the exact replacement.
3. **Temporary source-basis drift:** PRD v2.1 is adopted, while accepted
   decomposition revision 1.0 still cites PRD v2.0. `D-PEC-61` explicitly
   holds Project Setup until SCA-001 closes.
4. **Validator limitation:** OI-013 records that the original register
   generator was session-local; Gate 5 must rerun equivalent deterministic
   integrity checks and preserve this limitation.
5. **Exact amendment prose:** the owner has specified its required semantic
   content, but the complete before/after text is deliberately deferred to
   Gate 3.
6. **Dependency edges:** no `Dependencies.csv` exists or is authorized here.
   The complete DAG is downstream `PROJECT_SETUP` work after SCA-001 closure.

## Gate boundary

No PRD, decomposition working surface, authoritative companion register,
decomposition pointer, dependency register, project pointer, estimate,
schedule, scaffolding, implementation, or frozen-reference-corpus file was
modified by Gate 1.

## Gate 1 confirmation question

**Is this what you intend?**
