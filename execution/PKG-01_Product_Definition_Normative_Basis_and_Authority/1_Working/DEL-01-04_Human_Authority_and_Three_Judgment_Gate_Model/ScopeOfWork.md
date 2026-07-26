---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-04
package_id: PKG-01
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-010, SOW-011, SOW-017]
package_objective_refs: [OBJ-002, OBJ-003]
---

# Scope of Work — DEL-01-04

## Purpose and Objective Traceability

This Scope of Work defines the production contract for DEL-01-04, *Human
Authority and Three-Judgment Gate Model*, in package PKG-01. Its declared
basis is the accepted root decomposition named in `decomposition_basis`; its
covered project scope is SOW-010, SOW-011, SOW-017; its package objective is
OBJ-002.

Per the accepted register row, the deliverable exists to *"hold the
human-authority commitments at every consequential gate and keep the
evaluation, iteration, and release judgments distinct and undelegated, with
deterministic tools supplying findings and gating objective preconditions
only."* The accepted `ContextEnvelope` note reads *"one coherent authority
model over a bounded set of gate points."*

**Write-locus boundary.** The accepted `AnticipatedWriteLocus` for this
deliverable is `execution-tree`. `AnticipatedWriteLocus` is a planning note,
not authorization. Should this work find that a gate statement on the
instruction surface — `AGENTS.md`, `agents/`, `skills/`, `tools/`, root
`docs/`, `init/`, `.github/workflows/` — must change, that act **requires an
independently authorized M2 tranche. This Scope of Work grants none.**

**Ownership boundary.** The scope ledger records against SOW-010 that release
*"is separately gated at §8.3 and owned by DEL-06-07."* This deliverable
models the release judgment's distinctness from evaluation and iteration; it
does not own the release gate.

No lifecycle state, acceptance, or reliance is asserted by this document. The
definitions below are candidate content for owner review.

## Deliverable Definition — Ontology

### Expected outputs

- **OUT-001** — Gate model register: the enumerated set of consequential gate
  points, each classified and bound to the source that establishes it.
- **OUT-002** — Judgment-separation checklist: the standing check that the
  evaluation, iteration, and release judgments remain distinct and
  undelegated.
- **OUT-003** — Non-human-gate boundary notes: the recorded boundary between
  deterministic gates on objective preconditions and the judgments they may
  never perform.

### Covered scope statements

- **CLM-001** — SOW-010 (`PRD §4.2 [OWNER_DECLARED]`) states that the single
  human-judgment step resolves into three judgments that must not be
  collapsed: evaluation of the work, iteration on the product, and the release
  lifecycle judgment. The adopted PRD §4.2 distinguishes them by input,
  decision, and question: evaluation acts on operative evidence and decides
  the work; iteration acts on developmental candidates plus iteration evidence
  and decides the change to the product; release acts on both plus validation
  results, decomposition coverage, and guard state, and decides whether the
  current state may be released. The ledger records that release is separately
  gated at PRD §8.3 and owned by DEL-06-07.
- **CLM-002** — SOW-011 (`PRD §4.2 [OWNER_DECLARED / TRANSCRIBED support]`)
  states that deterministic tools, guards, and validators supply findings to
  the three judgments and gate objective preconditions; they never perform any
  of the judgments.
- **CLM-003** — SOW-017 (`PRD §5.1 N-3 [TRANSCRIBED]`) states that human
  authority holds at every consequential gate: only humans author binding
  approvals; approvals bind to a specific git SHA and are voided by content
  change; approvals are always and only binding; gates are dynamic per project
  with a stated minimum; and no machine BLOCK on the issuance judgment is
  non-overridable. The adopted PRD sources this to K-AUTH-1, K-AUTH-2,
  K-BIND-1, K-GATE-1 and `docs/DIRECTIVE.md` §2.3.
- **CLM-004** — The adopted PRD states OBJ-002's v1 success condition in the
  terms this deliverable serves: a complete deliverable stream runs end to end
  where every consequential acceptance, reliance, and issuance judgment is
  performed by an accountable human, while deterministic guards, fan-in gates,
  and structural validation gates remain lawful non-human gates on objective
  preconditions and hygiene.
- **CON-001** — Objective-reference divergence, surfaced not resolved. The
  deliverable register and `_CONTEXT.md` both record `SupportsObjectives:
  OBJ-002` for DEL-01-04, and this contract's frontmatter follows them. The
  scope ledger row for SOW-010 records `ObjectiveIDs = OBJ-003` for that scope
  item, while SOW-011 and SOW-017 record OBJ-002. The conservative reading
  taken here is that the deliverable-level objective governs the frontmatter
  and the ledger's item-level objective is additional traceability, not a
  contradiction to reconcile in this document. `HumanRuling = TBD`. **Ruled
  (D-GOV-27, 2026-07-25): additive propagation** — the ledger mapping stands,
  the register and this frontmatter gained OBJ-003, and this divergence is
  closed.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — OUT-001 shall enumerate the gate points it covers and, for
  each, record the source that establishes it and its classification as a
  human-judgment gate or a deterministic gate on objective preconditions
  (CLM-002, CLM-003). The enumeration is an output, never assumed.
- **REQ-002** — OUT-002 shall keep the three judgments of CLM-001 separately
  recorded, each with its own input, decision, and accountable-human slot. No
  entry shall record a judgment as performed by machinery (CLM-002).
- **REQ-003** — Every approval entry the model recognizes shall bind a
  specific git SHA and shall be recorded as voided by content change; approval
  entries are always and only binding (CLM-003).
- **REQ-004** — OUT-003 shall record that no machine BLOCK on the issuance
  judgment is non-overridable, and shall state for each deterministic gate the
  objective precondition it gates (CLM-002, CLM-003, CLM-004).
- **REQ-005** — This deliverable shall model the release judgment's
  distinctness only. The release gate itself is separately gated at PRD §8.3
  and owned by DEL-06-07 (CLM-001); this contract asserts no authority over
  it.

- **AC-001** — Every gate point in OUT-001 carries a classification —
  human-judgment or deterministic precondition — and a cited establishing
  source; no gate point is left unclassified, and unknowns are recorded as
  `TBD` rather than inferred.
- **AC-002** — OUT-002 records the evaluation, iteration, and release
  judgments as three separate entries, each with a distinct input, a distinct
  decision, and a named accountable-human slot; no entry attributes any of the
  three to a tool, guard, or validator.
- **AC-003** — OUT-003 names, for every deterministic gate it lists, the
  objective precondition gated and the judgment that gate does not perform,
  and records that no machine BLOCK on the issuance judgment is
  non-overridable.

## Production and Verification Method — Praxeology

Production sequence for this deliverable:

1. Enumerate the consequential gate points at a recorded basis revision and
   record each with its establishing source (REQ-001).
2. Classify each as a human-judgment gate or a deterministic gate on objective
   preconditions (REQ-001, CLM-002).
3. Build OUT-002 as three separate judgment entries and check that none is
   recorded as machine-performed (REQ-002).
4. Record approval-binding behavior — SHA binding, voiding on content change,
   always-and-only-binding — into the model (REQ-003).
5. Record OUT-003 from the registered guard surface, stating for each
   deterministic gate what it gates and what it does not decide (REQ-004).

- **VER-001** — Read the registered guard surface
  `execution/_harness/root_guards.yaml` and run each registered guard
  validator it names — `python3 tools/validation/validate_root_harness_adapter.py`,
  `python3 tools/validation/validate_root_surface_ownership.py`,
  `python3 tools/validation/validate_root_work_graph_dispatch.py`, and
  `python3 tools/validation/validate_instruction_tranche_manifest.py` —
  recording each exit status and output. This produces the deterministic
  evidence for OUT-003: each guard is observably a gate on objective
  preconditions. A passing guard is evidence, never a judgment, and guard
  registration holds no authority and confers none.

No registered deterministic tool can verify that a human judgment was in fact
made by an accountable human, or that three judgments were not collapsed in
practice. OUT-001 and OUT-002 therefore carry named human-review methods in
the matrix rather than a fabricated tool reference — which is itself the
commitment of CLM-002.

## Governing Values and Decisions — Axiology

- **AX-001** — The three judgments are not collapsed. Evaluation, iteration,
  and release have different inputs, failure modes, and evidence needs
  (CLM-001).
- **AX-002** — No judgment is delegated to machinery. Tools, guards, and
  validators supply findings and gate objective preconditions; they never
  decide (CLM-002).
- **AX-003** — Approvals are human-authored, SHA-bound, and voided by content
  change; they are always and only binding (CLM-003).
- **AX-004** — No non-overridable machine BLOCK on the issuance judgment. A
  gate may hold on an objective precondition; it may not become the decision
  (CLM-003, CLM-004).
- **AX-005** — Boundaries are respected rather than absorbed. Release is owned
  by DEL-06-07 and gated at PRD §8.3; the objective-reference divergence
  CON-001 is surfaced with pointers and left for owner ruling.
- **AX-006** — Nothing in this contract asserts acceptance, lifecycle state,
  or professional reliance. `ResponsibleParty` remains `TBD` until a human
  assigns ownership.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-017 OBJ-002 | CLM-003 CLM-004 REQ-001 REQ-003 CON-001 | AC-001 | HUMAN_REVIEW: Owner or delegated reviewer walks each enumerated gate point back to its cited establishing source and confirms the classification and the SHA-binding treatment of approvals | The gate model register, the cited sources per gate point, and the reviewer's recorded confirmation |
| OUT-002 | SOW-010 OBJ-002 | CLM-001 REQ-002 REQ-005 | AC-002 | HUMAN_REVIEW: Owner or delegated reviewer confirms the three judgments are separately recorded with distinct inputs, decisions, and accountable-human slots, and that none is attributed to machinery | The judgment-separation checklist and the reviewer's recorded confirmation at a named basis revision |
| OUT-003 | SOW-011 OBJ-002 | CLM-002 CLM-004 REQ-004 | AC-003 | VER-001 | The boundary notes, the registered guard surface read, and the recorded exit status and output of each guard validator |
