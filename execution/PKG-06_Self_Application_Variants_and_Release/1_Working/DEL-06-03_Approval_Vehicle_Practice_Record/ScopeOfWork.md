---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-03
package_id: PKG-06
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-064]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-06-03

## Purpose and Objective Traceability

DEL-06-03 (`DOC_UPDATE`) serves project scope SOW-064 and package objective
OBJ-003. Its purpose, transcribed from the accepted deliverable register, is to
keep the exact-candidate-SHA procedure recorded as **observed practice rather
than a rule**, to keep the actual invariant (approval binds to a SHA)
governing, and to keep vehicle selection a matter of professional judgment
unless evidence later warrants promotion.

OBJ-003 in `docs/PRD_ROOT.md` §3 is "the human evaluation and iteration loops
close", whose universal condition is that every accepted change has a
retrievable linkage, from files alone, between the evidence that informed it,
the ruling that accepted it, and the state it changed. A record of how
approvals have actually been bound to commits is part of that linkage surface.

`_CONTEXT.md` sets this deliverable's context envelope to `S` with the note
"a short record with no machinery". The scope of this contract is accordingly
a record and two short accompanying notes. It introduces no procedure, no
gate, no validator, and no obligation on any future approval.

Every definition below is grounded in the deliverable-register row for
DEL-06-03, this deliverable's `_CONTEXT.md`, the scope-ledger statement for
SOW-064, and the adopted `docs/PRD_ROOT.md`. Acceptance criteria and
verification methods are **candidates for owner review**; this contract claims
no acceptance and no lifecycle state.

## Deliverable Definition — Ontology

The three anticipated artifacts transcribed from the register
(`AnticipatedArtifacts`) and from `_CONTEXT.md ## Anticipated Artifacts` are:

- **OUT-001** — Practice record: the exact-candidate-SHA procedure written down
  as observed practice, with its instances of record and their evidence
  pointers, carrying an explicit `[OBSERVED]` label.
- **OUT-002** — Vehicle-selection guidance: a short statement that approval
  vehicle selection is professional judgment under the governing invariant,
  written as guidance and not as a requirement.
- **OUT-003** — Promotion-trigger note: a statement of what evidence would make
  promoting the practice into a PROPOSED requirement worth considering, and by
  whose act such promotion could occur.

- **CLM-001** — SOW-064 (SourceRef `PRD §6.2 [OBSERVED / CLARIFIED]`) records
  that the exact-candidate-SHA procedure is an observed practice exercised on
  substantial governance proposals rather than a governing rule; that the actual
  invariant is that every approval binds to a specific git SHA; and that vehicle
  selection is professional judgment.
- **CLM-002** — `docs/PRD_ROOT.md` §6.2 records the practice as a five-step
  procedure — commit the exact candidate; record its SHA; have the owner rule on
  that exact commit, recorded verbatim in a fence; publish the ruling as a
  separate durable record; record the merged implementation commit, returning
  for exact-prose re-acceptance if implementation would change approved prose —
  exercised three times, with instances of record D-GOV-18, D-GOV-19, and
  D-GOV-21.
- **CLM-003** — `docs/PRD_ROOT.md` §6.2 records that the governing invariant is
  K-AUTH-2 — every approval binds to a specific git SHA and is voided by content
  change — and that K-AUTH-2 admits other vehicles, a PR approval against branch
  HEAD satisfying it differently. It states that no governing clause requires
  the multi-SHA packet procedure of every substantial proposal.
- **CLM-004** — `docs/PRD_ROOT.md` §6.2 records that promotion of the pattern
  into a PROPOSED requirement remains available if evidence later shows that
  selecting among approval vehicles causes ambiguity or failure — either as a
  governed default with stated criteria, or as a mandatory rule with
  "substantial" defined.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — Per SOW-064 and CLM-001, the practice record shall carry the
  `[OBSERVED]` provenance label and shall contain no normative verb — no
  "shall", "must", or "is required to" — applied to any future approval. It
  states what the record shows and claims nothing more.
- **REQ-002** — Per CLM-002, each of the three instances of record shall be
  cited with its durable record location and the commit identity it bound, so
  that a reader can retrieve the instance from files alone (OBJ-003).
- **REQ-003** — Per CLM-003, the record and the guidance shall state K-AUTH-2 as
  the governing invariant and shall state that it admits vehicles other than the
  packet procedure, naming PR approval against branch HEAD as the recorded
  alternative.
- **REQ-004** — Per CLM-004, the promotion-trigger note shall state the
  evidence condition and the two available promotion forms, and shall state that
  promotion occurs only by an owner act; the note itself proposes nothing and
  triggers nothing.
- **REQ-005** — The record shall not upgrade, downgrade, or restate any
  provenance label of a cited source. Relying on a `[PROPOSED]` item as though
  adopted, or changing a label without a superseding instrument, is the F6
  failure mode named in `docs/PRD_ROOT.md` §8.2 and is out of bounds here.

- **AC-001** — The practice record carries the `[OBSERVED]` label, states the
  five procedure steps and the three instances of record with retrievable
  locations and bound commit identities, and contains no normative verb directed
  at any future approval.
- **AC-002** — The vehicle-selection guidance states K-AUTH-2 as the governing
  invariant, states that it admits other vehicles including PR approval against
  branch HEAD, and frames selection as professional judgment without ranking,
  defaulting, or recommending a vehicle.
- **AC-003** — The promotion-trigger note states the evidence condition, both
  promotion forms, and that promotion is an owner act, and asserts no promotion.

## Production and Verification Method — Praxeology

Production reads the SOW-064 ledger row, `_CONTEXT.md`, and `docs/PRD_ROOT.md`
§6.2 and §8.2, transcribes the practice and its instances, and writes the three
short artifacts inside this deliverable folder. It builds no tool, adds no gate,
and touches no governance record. The `S` envelope is a scope constraint on the
work, not only on the artifact length.

- **VER-001** — For each instance of record cited in the practice record,
  confirm deterministically that the cited durable record exists at its stated
  repo-relative path and that each cited commit identity resolves in the
  checkout (`git cat-file -e <sha>`). Unresolvable citations are reported, not
  repaired or silently dropped.

## Governing Values and Decisions — Axiology

- **AX-001** — Recording is not legislating. SOW-064 and `docs/PRD_ROOT.md` §6.2
  keep the practice `[OBSERVED]`; the whole value of this deliverable is that
  writing a practice down does not make it a rule. Any wording that would make
  the packet procedure obligatory defeats the deliverable's purpose.
- **AX-002** — The invariant governs, the practice illustrates. K-AUTH-2 is what
  binds; the five-step procedure is one vehicle that satisfies it. Guidance
  therefore names the invariant first and the vehicle second.
- **AX-003** — Judgment is left where it is. `docs/PRD_ROOT.md` §6.2 records
  that leaving the pattern OBSERVED is "the product's own movement applied to
  itself: practice supplies evidence, evidence informs judgment, and judgment
  alone makes the rule". This contract preserves that ordering.
- **AX-004** — This deliverable's `AnticipatedWriteLocus` is `execution-tree`
  and this contract grants no instruction-surface authority. Any act that would
  change `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, or
  `.github/workflows/` requires an independently authorized M2 tranche, which
  this contract does not grant.
- **AX-005** — Nothing is inferred where the accepted decomposition is silent
  (K-INVENT-1). `_CONTEXT.md ## Acceptance Criteria` records `TBD`; AC-001
  through AC-003 are candidate criteria derived only from the authorized
  grounding sources and remain subject to owner review.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-064 OBJ-003 | CLM-001 CLM-002 REQ-001 REQ-002 REQ-005 | AC-001 | VER-001 | Practice record plus the per-citation record-existence and commit-resolution check output |
| OUT-002 | SOW-064 OBJ-003 | CLM-001 CLM-003 REQ-003 | AC-002 | HUMAN_REVIEW: owner reads the guidance against PRD §6.2 and confirms it names K-AUTH-2 as governing, admits other vehicles, and neither ranks nor defaults a vehicle | Guidance text and the reviewer's recorded disposition |
| OUT-003 | SOW-064 OBJ-003 | CLM-004 REQ-004 REQ-005 | AC-003 | HUMAN_REVIEW: owner reads the note against PRD §6.2 and confirms it states the evidence condition and both promotion forms while proposing no promotion | Promotion-trigger note and the reviewer's recorded disposition |
