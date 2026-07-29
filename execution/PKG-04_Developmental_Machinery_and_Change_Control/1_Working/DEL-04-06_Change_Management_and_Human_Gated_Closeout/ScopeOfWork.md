---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-06
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-042]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-04-06

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-04-06`, Change
Management and Human-Gated Closeout, a `CI_CD_CHANGE` deliverable of
`PKG-04_Developmental_Machinery_and_Change_Control`. It serves project scope
item SOW-042 and package objective OBJ-002.

The register describes the deliverable as keeping git closeout running through
the change-management role with human-gated pull requests as the standing
default, preserving the four closeout identities. The scope ledger states
SOW-042 as: git closeout runs through the shared change-management role with
human-gated pull requests as the standing default; merge execution beyond that
default is lawful only under a bounded owner grant recorded per PRD annex
§5.3.1, preserving K-MERGE-1 and the four closeout identities. Its SourceRef
is PRD §5.3 D-8, the successor merge-gate policy adopted by D-GOV-31
(PROPOSED at Rev 7, in force through that ruling's effective merge).

OBJ-002 is the governed production of professional knowledge work — the product
carries work to an issuance decision that an accountable human makes. A
closeout path that a non-human actor can complete unilaterally would defeat
that objective at its final step, which is why this narrow procedural control
is traced to it.

The register records ContextEnvelope `S` with the note that this is one narrow
procedural control. This Scope of Work is bounded accordingly: it contracts the
evidence that the control holds, not a redesign of the control.

## Deliverable Definition — Ontology

The anticipated artifacts recorded in the register and `_CONTEXT.md` are a
closeout checklist, closeout-identity evidence, and PR gate notes. They are
expressed here as three outputs.

- **OUT-001** — A closeout checklist that enumerates, for a closeout act in
  the covered window, the steps performed through the change-management role
  and the human-gated pull-request step that terminates them under the
  standing default, or the recorded bounded owner grant that authorized merge
  execution beyond that default.
- **OUT-002** — A closeout-identity evidence set that records, per closeout
  act in the covered window, the four closeout identities — the semantic
  approval, the approved source SHA, the merge authorization, and the
  effective merge SHA — plus the grant reference when a bounded owner grant
  was exercised.
- **OUT-003** — PR gate notes that record, per pull request in the covered
  window, the gate decision and the accountable human who made it.

- **CLM-001** — SOW-042 is an `IN`-scope item of this package mapped to
  OBJ-002. Its source row, PRD §5.3 D-8, is the successor merge-gate policy:
  PROPOSED at Rev 7 and adopted by the D-GOV-31 owner ruling, in force from
  that ruling's effective merge. This deliverable therefore contracts
  evidence for an obligation in force through an adopted ruling rather than
  for a proposed one.
- **CLM-002** — The obligation has three separable elements: routing through
  the shared change-management role, the human-gated pull-request standing
  default with merge execution beyond it lawful only under a bounded owner
  grant recorded per PRD annex §5.3.1, and preservation of the four closeout
  identities (semantic approval, approved source SHA, merge authorization,
  effective merge SHA). PRD §5.3 D-8 records the supporting basis as
  `execution/_Coordination/LOOP_INIT.md` §7, annex §5.3.1, and invariant
  K-MERGE-1.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The outputs shall demonstrate, for every closeout act in the
  declared covered window, that closeout ran through the change-management role
  and terminated in a human-gated pull request under the standing default — or
  under a bounded owner grant recorded per PRD annex §5.3.1 before exercise —
  and that in either case the four closeout identities are observable
  (SOW-042; PRD §5.3 D-8, adopted by D-GOV-31).
- **REQ-002** — The outputs shall declare their covered window explicitly, so
  that a reader can determine which closeout acts the evidence does and does
  not speak to. An undeclared window makes the evidence uninterpretable for
  reliance.
- **REQ-003** — Where a closeout act in the covered window cannot be shown to
  satisfy REQ-001, the exception shall be recorded and surfaced rather than
  omitted, in keeping with the conflict-surfacing discipline PRD §5.1 N-4
  transcribes.

- **AC-001** — The closeout checklist names each of the three elements of
  SOW-042 — change-management routing, the human-gated pull-request standing
  default with its bounded-grant exception, and the four-identity closeout
  discipline — and each checklist step resolves to an observable act rather
  than an intention.
- **AC-002** — For every closeout act inside the declared covered window, the
  evidence set records the four closeout identities — semantic approval,
  approved source SHA, merge authorization, and effective merge SHA — and,
  where merge execution relied on a bounded owner grant, names the grant
  record and shows it was recorded before exercise; any act for which an
  identity or a required grant reference cannot be shown is listed as an
  exception.
- **AC-003** — The PR gate notes and the evidence set agree on the covered
  window and on the set of pull requests within it, with no pull request
  present in one and silently absent from the other.

## Production and Verification Method — Praxeology

Production reads the closeout record for the declared window from Git and from
the pull-request record, compiles the checklist against the transcribed
obligation, and records exceptions rather than resolving them.

- **VER-001** — Enumerate merges on the target branch with
  `git log --merges --first-parent` over the declared covered window and
  reconcile the resulting set against the pull-request record, confirming for
  each merge that a pull request exists and that the four closeout identities
  resolve to recorded acts — including, where the merge executor was the
  authoring actor of the merged content, a bounded owner grant recorded per
  PRD annex §5.3.1 before exercise.
- **VER-002** — Cross-check the covered-window declaration and the pull-request
  identifiers appearing in the PR gate notes against those appearing in the
  closeout-identity evidence set, confirming set equality in both directions.

Verification of whether the checklist faithfully expresses the adopted
obligation is a semantic judgment against `agents/AGENT_CHANGE.md`,
`execution/_Coordination/LOOP_INIT.md` §7, and PRD annex §5.3.1, not a
mechanical comparison; it is routed to human review in the matrix below.

Deterministic checks in this deliverable gate on objective preconditions only.
Consistent with PRD §3 OBJ-2, they never make the acceptance or issuance
judgment.

## Governing Values and Decisions — Axiology

- **AX-001** — Human authority at the consequential gate governs. PRD §5.1 N-3
  transcribes that only humans author binding approvals and that approvals bind
  to a specific git SHA. No artifact produced under this Scope of Work
  substitutes for the human gate it evidences.
- **AX-002** — Every `AC-*` and `VER-*` defined here is a candidate. This
  document claims no acceptance, no approval, and no lifecycle state; the owner
  reviews these criteria at the pull-request gate.
- **AX-003** — The register records `AnticipatedWriteLocus: execution-tree` for
  this deliverable. That is a planning note, not authorization. This Scope of
  Work grants no act on the instruction surface — `AGENTS.md`, `agents/`,
  `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/` — and any
  such act requires an independently authorized M2 tranche.
- **AX-004** — `_CONTEXT.md` records `ResponsibleParty: Ryan Tufts` under D-GOV-27, and the accepted decomposition states no per-deliverable acceptance criteria. Nothing is inferred here to fill the acceptance-criteria gap (K-INVENT-1); the criteria above are derived
  from the cited scope statement and PRD text alone.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-042 OBJ-002 | REQ-001 CLM-002 | AC-001 | HUMAN_REVIEW: owner walkthrough of the checklist against `agents/AGENT_CHANGE.md` and `execution/_Coordination/LOOP_INIT.md` §7 | Checklist with each step bound to the element of SOW-042 it evidences, and a recorded walkthrough disposition |
| OUT-002 | SOW-042 OBJ-002 | REQ-001 REQ-003 | AC-002 | VER-001 | Per-act closeout record naming the semantic approval, the approved source SHA, the merge authorization (with the grant reference when a bounded owner grant was exercised), and the effective merge SHA, plus an explicit exception list |
| OUT-003 | SOW-042 OBJ-002 | REQ-002 CLM-001 | AC-003 | VER-002 | Gate notes with a declared covered window and pull-request identifiers reconcilable against the evidence set |
