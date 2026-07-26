---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-02
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-038, SOW-093]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-04-02

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-04-02`, "Identity
Attribution and Refusal Controls", a `SECURITY_CONTROL`-type deliverable of
`PKG-04 Developmental Machinery and Change Control`. It serves project scope
items SOW-038 and SOW-093 and package objective OBJ-002.

Per its `_CONTEXT.md` Description, the deliverable exists to keep attribution of
rulings and adoptions matched against the owner-curated identity allowlist, with
identity-dependent checks refusing rather than guessing and the list never
extended programmatically.

The accepted decomposition states no per-deliverable acceptance criteria;
`_CONTEXT.md` records that as unresolved rather than inferring criteria
(K-INVENT-1). The `AC-*` and `VER-*` records below are therefore **candidates**
proposed from the four authorized grounding sources — the deliverable register
row, `_CONTEXT.md`, the scope-ledger statements of SOW-038 and SOW-093, and the
adopted `docs/PRD_ROOT.md`. They assert no acceptance, no approval, and no
lifecycle state; the owner disposes of them at the review gate.

### Grounding sources

- Deliverable register row `DEL-04-02_Identity_Attribution_and_Refusal_Controls`
  in `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`.
- `_CONTEXT.md` of this deliverable.
- Scope-ledger rows SOW-038 and SOW-093 in
  `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`.
- `docs/PRD_ROOT.md` §5.3 commitment D-4, and §9.2 (the RD-2 sub-decision on who
  may amend the allowlist, and the standing clarification of what the allowlist
  identifies).

## Deliverable Definition — Ontology

The anticipated artifacts named in the register row and in `_CONTEXT.md`
Anticipated Artifacts define three outputs.

- **OUT-001** — Identity-match check evidence: recorded evidence that
  attribution of a ruling or adoption was matched against the owner-curated
  identity allowlist rather than accepted on assertion.
- **OUT-002** — Refusal-path tests: tests exercising the branch where an
  identity-dependent check cannot attribute an actor, asserting that the check
  refuses and that no downstream judgment is performed.
- **OUT-003** — Curation-path note: a note fixing that the allowlist is
  owner-curated, that additions and removals are owner edits published through
  change management, and that no code path extends the list.

Descriptive claims that fix what this deliverable is about:

- **CLM-001** — SOW-038 states that attribution of rulings and adoptions matches
  an owner-curated identity allowlist, that identity-dependent checks refuse
  rather than guess, and that the list is not extended programmatically. Source:
  scope-ledger SOW-038, `SourceRef` PRD §5.3 D-4 [TRANSCRIBED].
- **CLM-002** — SOW-093 states that the identity allowlist stays owner-curated —
  additions and removals are owner edits published through change management and
  not extended programmatically. Source: scope-ledger SOW-093, `SourceRef` PRD
  §9.2 sub-decision [OWNER_DECLARED — ruled], `PRDItem` RD-2.
- **CLM-003** — PRD §9.2 carries a standing clarification of what the allowlist
  is: it identifies permitted authors of binding governance records under
  D-GOV-04 identity matching, and is not a registry of every person accountable
  for situated professional work. Work under this deliverable must not widen it
  into the latter.
- **CLM-004** — Refusal is a distinct outcome from failure. An identity-dependent
  check that cannot attribute an actor is not reporting that content is bad; it
  is reporting that it is not in a position to judge, and it stops.
- **CLM-005** — The register row types this deliverable `SECURITY_CONTROL` with
  `ContextEnvelope: S` and the note "One check with a small allowlist surface",
  bounding the work to one identity-dependent check and a small allowlist.

## Completion and Reliance Basis — Epistemology

Requirements restate the covered scope obligations as checkable production
requirements. They are candidates for owner disposition, not accepted criteria.

- **REQ-001** — Identity-match evidence in OUT-001 shall record, per examined
  attribution, the actor claim under test and the allowlist entry it matched,
  naming the allowlist surface relied on rather than asserting a match
  abstractly.
- **REQ-002** — Where an identity-dependent check cannot attribute an actor —
  including where the allowlist is absent — the check shall refuse and shall
  perform no downstream judgment. A refusal shall be distinguishable in the
  recorded result from a substantive finding, per CLM-004.
- **REQ-003** — The tests of OUT-002 shall cover the refusal branch explicitly,
  asserting both the refusal outcome and that no downstream check executed, so
  that a regression which silently guesses an actor fails the tests.
- **REQ-004** — The note of OUT-003 shall state that additions and removals to
  the allowlist are owner edits published through change management, and that no
  code path adds, removes, or infers an entry.
- **REQ-005** — No output of this deliverable shall write an allowlist entry,
  propose a programmatic extension path, or widen the allowlist beyond the
  permitted-authors scope described in CLM-003.
- **REQ-006** — No output shall assert acceptance, approval, lifecycle
  transition, or a ruling; findings are observations routed to the owner.
- **REQ-007** — Production shall write only under the execution tree.
  `_CONTEXT.md` records `AnticipatedWriteLocus: execution-tree; tools/ (M2) if a
  check must change`. That locus is a planning note and not authorization: if a
  check under `tools/` must change, that act requires an independently
  authorized M2 tranche, which this Scope of Work does not grant and cannot
  grant. Within this deliverable, evidence and tests are produced without
  modifying the check.

Candidate acceptance criteria:

- **AC-001** — For every attribution examined, the evidence in OUT-001 records
  the actor claim, the matched allowlist entry, and the allowlist surface; an
  unmatched claim is recorded as a refusal and never as a guessed or inferred
  actor.
- **AC-002** — The OUT-002 tests cover at least the allowlist-absent branch and
  the unattributable-actor branch, and each asserts both the refusal outcome and
  that no downstream judgment ran.
- **AC-003** — The OUT-003 note states the owner-curated change-management
  curation path with no programmatic extension, cites SOW-093 and its PRD §9.2
  RD-2 basis, and this deliverable's production leaves the allowlist file
  byte-unchanged.

## Production and Verification Method — Praxeology

Production reads the four grounding sources and the live identity-matching
surface, then writes evidence, tests, and the note under the execution tree. The
identity allowlist relied on is `docs/governance_harness/human_actors.md`, and
the identity-matching behaviour under observation is implemented in the
practitioner harness at `tools/practitioner_harness/harness_common.py`, which
resolves that allowlist, raises a dedicated identity-refusal error when an
identity-dependent check cannot attribute an actor, and returns an operational
refusal status distinct from its finding-severity statuses.

- **VER-001** — Deterministic identity-match execution: run an identity-dependent
  harness check and capture whether it resolved the actor against
  `docs/governance_harness/human_actors.md` or returned the operational refusal
  outcome, recording the captured output as the evidence of OUT-001. The check
  is executed and observed; it is not modified.
- **VER-002** — Deterministic refusal-path test execution: run the registered
  identity-refusal tests, which exist at this basis —
  `tools/practitioner_harness/test_run_validations.py` (the refusal test
  asserting exit status and that nothing executed) and the three identity-refusal
  tests in `tools/practitioner_harness/test_scope_evidence_closeout.py` (scope
  check judging nothing, evidence check refusal, closeout running no subcheck).
  New tests written for OUT-002 extend this set and are run the same way, for
  example with `python3 -m pytest` over the named test paths.
- **VER-003** — Deterministic allowlist-immutability and write-locus check:
  confirm from the Git record for `docs/governance_harness/human_actors.md`
  (for example `git log --` over that path, and a diff over the produced
  tranche) that this deliverable's production changed no allowlist byte, and
  confirm by path inspection that every produced artifact resolves under the
  execution tree with no write under `tools/` or the wider instruction surface,
  consistent with REQ-005 and REQ-007.

Whether the curation path as written faithfully describes the owner's practice
is a judgment no check settles; the matrix carries an explicit `HUMAN_REVIEW`
method there rather than a fabricated check.

## Governing Values and Decisions — Axiology

- **AX-001** — Refuse rather than guess. Per SOW-038, an identity-dependent check
  that cannot attribute an actor stops. Guessing an actor would manufacture
  attribution, which is the precise harm this control exists to prevent.
- **AX-002** — The allowlist is owner-curated. Per SOW-093 and the PRD §9.2 RD-2
  sub-decision, additions and removals are owner edits published through change
  management; no automation may extend the list, and convenience is not a reason
  to add one.
- **AX-003** — Attribution supports accountability, not access. Per CLM-003 the
  allowlist identifies permitted authors of binding governance records; treating
  it as a general roster of accountable people would misstate both what it
  contains and what a match proves.
- **AX-004** — The instruction surface is governed separately. `_CONTEXT.md`
  states that any locus naming the instruction surface — here `tools/`, if a
  check must change — requires an independently authorized M2 tranche. This
  Scope of Work grants no such authorization, and its acceptance would grant
  none.
- **AX-005** — Nothing is inferred beyond the authorized sources (K-INVENT-1).
  Where the accepted decomposition is silent — on per-deliverable acceptance
  criteria, and on `ResponsibleParty`, which remains `TBD` in the register row —
  the silence is preserved and surfaced.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-038 OBJ-002 | CLM-001 CLM-003 CLM-005 REQ-001 REQ-002 REQ-006 | AC-001 | VER-001 VER-003 | Captured check output per examined attribution, showing the matched allowlist entry or the recorded refusal, with the allowlist surface named |
| OUT-002 | SOW-038 OBJ-002 | CLM-001 CLM-004 REQ-002 REQ-003 REQ-007 | AC-002 | VER-002 | Test sources plus the test-run output covering the allowlist-absent and unattributable-actor branches, each asserting refusal and no downstream judgment |
| OUT-003 | SOW-093 OBJ-002 | CLM-002 CLM-003 REQ-004 REQ-005 REQ-006 REQ-007 | AC-003 | HUMAN_REVIEW: owner reading of the curation-path note against the allowlist's own maintenance rule and the PRD §9.2 RD-2 sub-decision | Note text with its SOW-093 and PRD §9.2 citations, plus the unchanged-allowlist result from the production tranche |
