---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-01
package_id: PKG-06
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-060, SOW-062, SOW-080, SOW-081, SOW-082]
package_objective_refs: [OBJ-004]
---

# Scope of Work — DEL-06-01

## Purpose and Objective Traceability

DEL-06-01 (`REQ_SLICE`) serves project scope SOW-060, SOW-062, SOW-080,
SOW-081, and SOW-082, and package objective OBJ-004. Its purpose, transcribed
from the accepted deliverable register, is to keep root self-application
disciplined — no root node consuming a capability produced by root development
before that capability was accepted — and to keep the containment falsifiers
observable, so that a containment failure, loop bypass, or self-authorization
would be **detected rather than inferred**.

OBJ-004 in `docs/PRD_ROOT.md` §3 is "safe self-application without
self-authorization", whose stated v1 success condition is that falsifiers F1–F3
remain unobserved through v1, that every root capability consumed by root
development was accepted through the basis or an explicitly accepted
predecessor, and that guards G0–G4 are registered and passing at every
materialization. This deliverable produces the observation surface against
which that condition can be checked; it does not itself assert the condition
holds.

Every definition below is grounded in the deliverable-register row for
DEL-06-01, this deliverable's `_CONTEXT.md`, the scope-ledger statements for
the five covered scope items, and the adopted `docs/PRD_ROOT.md`. Acceptance
criteria and verification methods here are **candidates for owner review**;
this contract claims no acceptance and no lifecycle state.

## Deliverable Definition — Ontology

The three anticipated artifacts transcribed from the register
(`AnticipatedArtifacts`) and from `_CONTEXT.md ## Anticipated Artifacts` are:

- **OUT-001** — Self-application discipline checklist: a checkable statement of
  the SOW-062 discipline rule together with the current gating status of the
  D-GOV-21 §6 sequence steps that SOW-060 records as individually gated.
- **OUT-002** — Falsifier observation record: one entry per containment
  falsifier F1 (SOW-080), F2 (SOW-081), and F3 (SOW-082), each naming its
  observation method, its observed / not-observed disposition at a stated
  basis, and the evidence surface consulted.
- **OUT-003** — Consumed-capability provenance list: for each root capability
  consumed by root development, the accepted basis or explicitly accepted
  predecessor through which it was accepted.

- **CLM-001** — SOW-060 (SourceRef `PRD §6.1 [TRANSCRIBED]`) records that
  self-application is operationalized by the ruled D-GOV-21 §6 sequence, whose
  later steps — PRD adoption, first root decomposition with Project Setup, and
  materialization behind the §5.3 gate — are individually gated. The checklist
  of OUT-001 records that gating; it does not close, waive, or advance any gate.
- **CLM-002** — `docs/PRD_ROOT.md` §8.2 adopts F1–F3 as product-level
  falsifiers of the *containment* of self-application. They are falsifiers, not
  gates: recording one as observed is an evidence event that returns to the
  owner, not an automatic verdict.
- **CON-001** — The scope ledger marks SOW-060 `OpenIssue TRUE` with note
  `OI-001`: the PRD's step-status statements pre-date later accepted acts at
  the current basis. The step-status column of OUT-001 therefore records the
  PRD statement and the observed current state as two distinct fields rather
  than reconciling them. Reconciliation is an owner act, not an act of this
  deliverable.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — Per SOW-062 (SourceRef `PRD §6.2 [TRANSCRIBED]`), the discipline
  checklist shall state that a root node may not consume a capability produced
  by root development before that capability was accepted through the basis or
  an explicitly accepted predecessor, and shall express that rule as a condition
  checkable per consumption event rather than as narrative guidance.
- **REQ-002** — Per SOW-080 (SourceRef `PRD §8.2 F1 [TRANSCRIBED]`), the
  observation record shall carry an F1 entry — root self-development corrupting
  a shared instruction surface out from under a situated loop in a way the
  superseded separation would have prevented, undetected and ungated by the
  containment mechanisms and guards — with a stated observation method.
- **REQ-003** — Per SOW-081 (SourceRef `PRD §8.2 F2 [TRANSCRIBED]`), the
  observation record shall carry an F2 entry — root development proceeding
  outside the root governed loop, materialized without a current workplan
  pointer, receipts, and the governance machinery engaged — with a stated
  observation method.
- **REQ-004** — Per SOW-082 (SourceRef `PRD §8.2 F3 [TRANSCRIBED]`), the
  observation record shall carry an F3 entry — a root node consuming a
  capability produced by root development before that capability was accepted —
  cross-referenced to the provenance list of OUT-003.
- **REQ-005** — Each falsifier entry shall record a disposition of `OBSERVED`,
  `NOT_OBSERVED`, or `NOT_YET_OBSERVABLE` against a named basis, and shall never
  record an inferred disposition; an entry whose observation method cannot be
  run at the stated basis is `NOT_YET_OBSERVABLE` with the blocker named.

- **AC-001** — The discipline checklist states the SOW-062 rule as a per-event
  checkable condition and records, for each D-GOV-21 §6 step that SOW-060
  identifies as individually gated, both the PRD-stated status and the observed
  current status as separate fields (CON-001).
- **AC-002** — The falsifier observation record contains exactly three entries,
  F1, F2, and F3, mapped one-to-one to SOW-080, SOW-081, and SOW-082; each
  names an observation method, a disposition drawn from the REQ-005 vocabulary,
  a stated basis, and the evidence surface consulted.
- **AC-003** — Every entry in the consumed-capability provenance list names the
  consuming root node, the consumed capability, and the accepted basis commit or
  the explicitly accepted predecessor record through which that capability was
  accepted; no entry cites an unaccepted or pending candidate.

## Production and Verification Method — Praxeology

Production reads the accepted decomposition basis, this deliverable's
`_CONTEXT.md`, the covered scope-ledger rows, `docs/PRD_ROOT.md` §3, §6, and
§8.2, and the root coordination and guard surfaces under
`execution/_Coordination/` and `execution/_harness/`. It writes only within this
deliverable folder. Where an observation depends on a surface that root Project
Setup instantiates later, the entry is recorded as `NOT_YET_OBSERVABLE` rather
than estimated.

- **VER-001** — Execute the guards registered in
  `execution/_harness/root_guards.yaml` — `python3
  tools/validation/validate_root_harness_adapter.py` (G1), `python3
  tools/validation/validate_root_surface_ownership.py` (G2), `python3
  tools/validation/validate_root_work_graph_dispatch.py` (G3), and `python3
  tools/validation/validate_instruction_tranche_manifest.py` (G4) — together
  with `python3 tools/validation/validate_root_materialization_fence.py` (G0),
  which that registration file records as requiring no entry for itself, and
  record each exit status and message against the falsifier entries they bear
  on. A guard result is evidence for a falsifier disposition; it is never itself
  the disposition.
- **VER-002** — For each provenance-list entry, confirm deterministically that
  the cited accepted basis commit resolves in the checkout (`git cat-file -e
  <sha>`) and that the cited accepted-predecessor record exists at its stated
  repo-relative path; entries failing either check are reported, not repaired.

## Governing Values and Decisions — Axiology

- **AX-001** — Detection over inference. The register description for DEL-06-01
  requires that a containment failure, loop bypass, or self-authorization "would
  be detected rather than inferred". An unrunnable observation is recorded as
  such; it is never replaced by a plausible reading of the record.
- **AX-002** — Containment is not authorization. `docs/PRD_ROOT.md` §6.2 states
  that deterministic guards and human gates supply containment and that neither
  supplies authorization (K-AUTH-1). A passing guard in VER-001 therefore
  supports a disposition and authorizes nothing.
- **AX-003** — This deliverable's `AnticipatedWriteLocus` is `execution-tree`
  and this contract grants no instruction-surface authority. Any act that would
  change `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, or
  `.github/workflows/` requires an independently authorized M2 tranche, which
  this contract does not grant and cannot supply.
- **AX-004** — Nothing is inferred where the accepted decomposition is silent
  (K-INVENT-1). `_CONTEXT.md ## Acceptance Criteria` records `TBD` because the
  accepted decomposition states no per-deliverable acceptance criteria; AC-001
  through AC-003 above are candidate criteria derived only from the authorized
  grounding sources and remain subject to owner review.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-060 SOW-062 OBJ-004 | CLM-001 REQ-001 CON-001 | AC-001 | HUMAN_REVIEW: owner reads the checklist against PRD §6.1–§6.2 and the SOW-060/SOW-062 ledger statements and confirms each rule and gated step is a checkable field | Checklist artifact with per-step PRD-stated and observed-current fields, and the reviewer's recorded disposition |
| OUT-002 | SOW-080 SOW-081 SOW-082 OBJ-004 | CLM-002 REQ-002 REQ-003 REQ-004 REQ-005 | AC-002 | VER-001 | Falsifier observation record plus the captured exit status and message of each of the five root guards at the stated basis |
| OUT-003 | SOW-062 OBJ-004 | REQ-001 REQ-004 | AC-003 | VER-002 | Provenance list plus the per-entry commit-resolution and record-existence check output |
