---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-05
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-009, SOW-041]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-04-05

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-04-05`, "Root Governed
Loop and Receipt Discipline", a `DOC_UPDATE`-type deliverable of
`PKG-04 Developmental Machinery and Change Control`. It serves project scope
items SOW-009 and SOW-041 and package objective OBJ-003.

Per its `_CONTEXT.md` Description, the deliverable exists to keep root-product
development running through the governed loop — session-init contract,
deterministic standing-plan pointer, append-only receipts — with coordination
surfaces carrying no authority merely by existing.

The accepted decomposition states no per-deliverable acceptance criteria;
`_CONTEXT.md` records that as unresolved rather than inferring criteria
(K-INVENT-1). The `AC-*` and `VER-*` records below are therefore **candidates**
proposed from the four authorized grounding sources — the deliverable register
row, `_CONTEXT.md`, the scope-ledger statements of SOW-009 and SOW-041, and the
adopted `docs/PRD_ROOT.md`. They assert no acceptance, no approval, and no
lifecycle state; the owner disposes of them at the review gate.

### Grounding sources

- Deliverable register row `DEL-04-05_Root_Governed_Loop_and_Receipt_Discipline`
  in `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`.
- `_CONTEXT.md` of this deliverable.
- Scope-ledger rows SOW-009 and SOW-041 in
  `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`.
- `docs/PRD_ROOT.md` §4.2 (the generative loop and its three human judgments)
  and §5.3 commitment D-7.

## Deliverable Definition — Ontology

The anticipated artifacts named in the register row and in `_CONTEXT.md`
Anticipated Artifacts define three outputs.

- **OUT-001** — Loop-init conformance notes: notes recording, for root-product
  development work, whether the session ran through the three loop elements
  SOW-041 names — a session-init contract, a deterministic standing-plan
  pointer, and an append-only receipts log.
- **OUT-002** — Receipts-log discipline check: a check that the root receipts
  log grows by append and that previously written receipt content was not
  rewritten in place.
- **OUT-003** — Coordination-authority disclaimer audit: an audit over the root
  coordination surfaces recording whether each carries the statement that it
  holds no authority merely by existing, and that on disagreement with a live
  source the live source governs and the delta is recorded.

Descriptive claims that fix what this deliverable is about:

- **CLM-001** — SOW-041 states that root-product development runs through a
  governed loop with a session-init contract, a deterministic standing-plan
  pointer, and an append-only receipts log; that coordination surfaces carry no
  authority merely because they exist; and that on disagreement with a live
  source, the live source governs and the delta is recorded. Source:
  scope-ledger SOW-041, `SourceRef` PRD §5.3 D-7 [TRANSCRIBED].
- **CLM-002** — SOW-009 states that the categories are related by a generative
  loop whose closing step — human judgment — no agent can perform. Source:
  scope-ledger SOW-009, `SourceRef` PRD §4.2 [OWNER_DECLARED], `DecisionRef`
  DEC-010.
- **CLM-003** — PRD §4.2 resolves that single human-judgment step into three
  judgments that must not be collapsed — the evaluation judgment over the work,
  the iteration judgment over changes to the product, and the release judgment
  over whether the present state may go out — and states that none is delegated
  to machinery: deterministic tools, guards, and validators supply findings and
  gate objective preconditions but never perform any of the three.
- **CLM-004** — Taken together, CLM-001 and CLM-002 fix the deliverable's
  posture: the loop surfaces are the observable machinery, and the closing act
  is not one of them. A conformance record about the loop is evidence for a
  human judgment, never a substitute for one.
- **CLM-005** — The register row types this deliverable `DOC_UPDATE` with
  `ContextEnvelope: M` and the note "Loop surfaces are few and stable", bounding
  the work to a small, stable set of coordination surfaces.

## Completion and Reliance Basis — Epistemology

Requirements restate the covered scope obligations as checkable production
requirements. They are candidates for owner disposition, not accepted criteria.

- **REQ-001** — The conformance notes of OUT-001 shall address all three loop
  elements SOW-041 names — session-init contract, deterministic standing-plan
  pointer, append-only receipts log — and shall identify, for each, the actual
  surface relied on rather than asserting the element abstractly.
- **REQ-002** — The standing-plan pointer shall be treated as deterministic:
  the notes shall record how the current plan was resolved from the pointer, so
  that resolution is reproducible rather than recalled.
- **REQ-003** — The discipline check of OUT-002 shall establish append-only
  behaviour by comparing the previously written prefix of the receipts log
  byte-for-byte against its prior state, and shall report an in-place rewrite as
  a finding rather than normalizing it away.
- **REQ-004** — The audit of OUT-003 shall cover each root coordination surface
  in the examined set and shall record, per surface, whether the no-authority
  statement and the live-source-governs rule are present, treating absence as a
  finding.
- **REQ-005** — Every output shall report rather than decide. Per CLM-002 and
  CLM-003, no output may perform, simulate, or stand in for the evaluation,
  iteration, or release judgment, and no output may describe a machine check as
  having closed the loop.
- **REQ-006** — No output shall assert acceptance, approval, lifecycle
  transition, or a ruling; findings are observations routed to the owner.
- **REQ-007** — Production shall write only under the execution tree, matching
  the `AnticipatedWriteLocus: execution-tree` recorded in `_CONTEXT.md`. That
  locus is a planning note and not authorization.

Candidate acceptance criteria:

- **AC-001** — The OUT-001 notes address all three loop elements named in
  SOW-041, name the actual surface relied on for each, and record how the
  current plan was resolved from the standing-plan pointer.
- **AC-002** — The OUT-002 check demonstrates that the receipts log's prior
  content is byte-identical to its earlier state and that new content was added
  only after it, or else reports the divergence as an explicit finding.
- **AC-003** — The OUT-003 audit lists every coordination surface it examined
  with a present/absent result for both the no-authority statement and the
  live-source-governs rule, and asserts nothing about surfaces it did not
  examine.

## Production and Verification Method — Praxeology

Production reads the four grounding sources and the live root loop surfaces —
`execution/_Coordination/LOOP_INIT.md`, the standing workplan pointed to by the
current-workplan pointer, and `execution/_Coordination/LOOP_RECEIPTS.md` — then
writes the three outputs under the execution tree.

- **VER-001** — Deterministic append-only check over the receipts log: compare
  the frozen prefix of `execution/_Coordination/LOOP_RECEIPTS.md` — its byte
  length and its SHA-256 — against the prior accepted state, and corroborate
  with the file's Git history (for example `git log -p` over that path) that
  earlier receipt bytes were not modified. The registered shared engine
  `tools/validation/loop_receipt_contract.py` implements exactly this
  frozen-prefix contract for versioned development-loop receipts; its wrappers
  are project-specific, and no root wrapper is registered at this basis, so the
  check runs against the engine's contract semantics and the Git record. Adding
  a root wrapper would be an instruction-surface act outside this deliverable.
- **VER-002** — Deterministic disclaimer presence check: for each coordination
  surface in the examined set, confirm by literal text search over the file
  (for example `grep -n`) that the no-authority statement and the
  live-source-governs rule are present, recording the matched line per surface
  and an explicit absence where there is no match.
- **VER-003** — Deterministic surface-resolution and write-locus check: confirm
  by path inspection that each loop surface named in the outputs resolves in the
  active checkout, and that every artifact this deliverable produced resolves
  under the execution tree, consistent with REQ-007.

Whether a given session genuinely ran through the loop, as distinct from
whether the loop surfaces exist and are well formed, is a judgment no check
settles; the matrix carries an explicit `HUMAN_REVIEW` method there rather than
a fabricated check.

## Governing Values and Decisions — Axiology

- **AX-001** — The closing step is human. SOW-009 states the loop's closing step
  is a human judgment no agent can perform, and PRD §4.2 holds that none of the
  three judgments is delegated to machinery. Every output here is an input to
  that judgment.
- **AX-002** — Coordination surfaces carry no authority merely by existing. Per
  SOW-041, a receipts log, workplan, or handoff note is not made authoritative
  by being written; on disagreement with a live source, the live source governs
  and the delta is recorded.
- **AX-003** — Append, never rewrite. The receipts log's value is that its past
  entries are stable; a silent in-place correction destroys the linkage OBJ-003
  depends on, so a rewrite is surfaced as a finding rather than tidied.
- **AX-004** — No simulated execution. A record must reflect work that actually
  ran; a plan, brief, or placeholder is never recorded as an executed step.
- **AX-005** — Nothing is inferred beyond the authorized sources (K-INVENT-1).
  Where the accepted decomposition is silent — on per-deliverable acceptance
  criteria, and on `ResponsibleParty`, which is `Ryan Tufts` under D-GOV-27 and the current deliverable register — the accepted assignment is preserved, while the acceptance-criteria silence is surfaced.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-041 OBJ-003 | CLM-001 CLM-005 REQ-001 REQ-002 REQ-005 REQ-007 | AC-001 | HUMAN_REVIEW: owner reading of the conformance notes against the session-init contract and the plan resolved from the standing-plan pointer | Conformance notes naming the surface relied on per loop element, with the recorded pointer resolution |
| OUT-002 | SOW-041 OBJ-003 | CLM-001 REQ-003 REQ-006 REQ-007 | AC-002 | VER-001 VER-003 | Recorded frozen-prefix byte length and SHA-256 comparison for the receipts log, the corroborating Git history result, and any rewrite finding |
| OUT-003 | SOW-009 SOW-041 OBJ-003 | CLM-002 CLM-003 CLM-004 REQ-004 REQ-005 REQ-006 | AC-003 | VER-002 VER-003 | Audit table of examined coordination surfaces with matched lines or explicit absences for the no-authority statement and the live-source-governs rule |
