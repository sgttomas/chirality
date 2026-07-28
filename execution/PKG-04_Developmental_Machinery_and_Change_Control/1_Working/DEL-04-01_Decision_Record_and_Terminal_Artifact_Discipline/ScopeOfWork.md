---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-01
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-036, SOW-037]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-04-01

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-04-01`, "Decision Record
and Terminal-Artifact Discipline", a `REGISTER`-type deliverable of
`PKG-04 Developmental Machinery and Change Control`. It serves project scope
items SOW-036 and SOW-037 and package objective OBJ-003.

Per its `_CONTEXT.md` Description, the deliverable exists to keep design change
carried by one of two terminal artifacts — a superseding decision record or PR
review — never a new plan document, and to keep corrections to ruled content
superseding acts within the two record classes where that convention governs.

The accepted decomposition states no per-deliverable acceptance criteria; the
`_CONTEXT.md` Acceptance Criteria section records this as unresolved rather than
inferring criteria (K-INVENT-1). The `AC-*` and `VER-*` records below are
therefore **candidates** proposed from the four authorized grounding sources —
the deliverable register row, `_CONTEXT.md`, the scope-ledger statements of
SOW-036 and SOW-037, and the adopted `docs/PRD_ROOT.md`. They assert no
acceptance, no approval, and no lifecycle state; the owner disposes of them at
the review gate.

### Grounding sources

- Deliverable register row `DEL-04-01_Decision_Record_and_Terminal_Artifact_Discipline`
  in `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`.
- `_CONTEXT.md` of this deliverable.
- Scope-ledger rows SOW-036 and SOW-037 in
  `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`.
- `docs/PRD_ROOT.md` §5.3, commitments D-1 and D-2.

## Deliverable Definition — Ontology

The anticipated artifacts named in the register row and in `_CONTEXT.md`
Anticipated Artifacts define three outputs.

- **OUT-001** — Decision-record structure checklist: an enumerated checklist of
  the fields a decision record must carry when a decision record is the vehicle
  of a design change, applied to the published records under
  `docs/governance_harness/_DECISIONS/`.
- **OUT-002** — Register navigational-vs-governing note: a written note fixing
  that the decision register is navigational and that the per-decision records
  govern, so that a reader who consults only the register knows the register is
  not the authority.
- **OUT-003** — Supersede-never-edit conformance report: a report examining,
  within the two record classes where the convention governs, whether
  corrections to ruled content were carried as superseding acts rather than
  edits.

Descriptive claims that fix what this deliverable is about:

- **CLM-001** — SOW-036 states that a design change is carried by one of two
  terminal artifacts — it supersedes a decision record or arrives as PR review,
  never a new plan document — and that where the vehicle is a decision record it
  carries status, verbatim owner ruling, SHAs, date, framing, accepted basis,
  and record convention, with the register navigational and the per-decision
  records governing. Source: scope-ledger SOW-036, `SourceRef` PRD §5.3 D-1
  [TRANSCRIBED at that scope].
- **CLM-002** — SOW-037 states that within the two record classes where the
  convention governs — published decision records carrying the
  supersede-never-edit convention, and ruled candidate packets bound to an
  accepted candidate SHA — corrections to ruled content are superseding acts
  rather than edits. Source: scope-ledger SOW-037, `SourceRef` PRD §5.3 D-2
  [CLARIFIED].
- **CLM-003** — SOW-037's obligation is bounded to those two record classes and
  asserts nothing beyond them; the adopted PRD carries the broader
  change-control rule separately at D-16, and the scope-ledger `Notes` field for
  SOW-037 records the same separation. This deliverable therefore does not
  extend the convention to any third class of artifact.
- **CLM-004** — The register row types this deliverable `REGISTER` with
  `ContextEnvelope: M` and the note "Convention conformance over one record
  family", so the work is conformance observation over one existing record
  family, not the creation of a new governance instrument.

## Completion and Reliance Basis — Epistemology

Requirements restate the covered scope obligations as checkable production
requirements. They are candidates for owner disposition, not accepted criteria.

- **REQ-001** — The checklist of OUT-001 shall enumerate every field SOW-036
  names for a decision-record vehicle — status, verbatim owner ruling, SHAs,
  date, framing, accepted basis, and record convention — and shall not silently
  add or drop a field relative to that statement.
- **REQ-002** — The checklist of OUT-001 shall be applied to the published
  decision records under `docs/governance_harness/_DECISIONS/`, recording per
  record and per field whether the field is present, and shall report a missing
  field as a finding rather than resolving it.
- **REQ-003** — The note of OUT-002 shall state the navigational-versus-governing
  split exactly as SOW-036 states it, and shall cite SOW-036 and its
  `SourceRef` PRD §5.3 D-1 rather than restating the rule on its own authority.
- **REQ-004** — The report of OUT-003 shall declare its examined population as
  the two record classes named in SOW-037 and shall state explicitly that no
  finding extends to any artifact outside those two classes.
- **REQ-005** — No output of this deliverable shall assert acceptance, approval,
  lifecycle transition, or a ruling. Findings are observations routed to the
  owner; a conformance gap is reported, never repaired by an agent editing a
  ruled record.
- **REQ-006** — Production shall write only under the execution tree.
  `_CONTEXT.md` records `AnticipatedWriteLocus: execution-tree;
  instruction-surface (M2) for the register itself`. That locus is a planning
  note and not authorization: any act touching the instruction surface —
  including the decision register itself — requires an independently authorized
  M2 tranche, which this Scope of Work does not grant and cannot grant.

Candidate acceptance criteria:

- **AC-001** — Every field named in SOW-036 appears exactly once in the OUT-001
  checklist, and the applied tabulation covers every published decision record
  under `docs/governance_harness/_DECISIONS/` with a present/absent result per
  field.
- **AC-002** — The OUT-002 note states that the register is navigational and the
  per-decision records govern, and cites SOW-036 and PRD §5.3 D-1 as its basis.
- **AC-003** — The OUT-003 report names its population as exactly the two record
  classes of SOW-037, classifies each examined correction as a superseding act
  or a finding, and contains no claim about artifacts outside those classes.

## Production and Verification Method — Praxeology

Production reads the four grounding sources and the live record family, then
writes the three outputs under the execution tree. Verification distinguishes
what a deterministic pass can settle from what requires a human reader.

- **VER-001** — Deterministic field tabulation: enumerate the record files under
  `docs/governance_harness/_DECISIONS/` and, for each checklist field, record
  presence or absence per record by literal text search over those files
  (for example `grep -n` per field token). The result is a table of present and
  absent fields. No purpose-built validator for decision-record structure exists
  at this basis; the verification is therefore the named surface plus the
  recorded tabulation, and building a dedicated check is out of this
  deliverable's scope.
- **VER-002** — Deterministic supersession trace: for each correction examined by
  OUT-003, resolve whether a later record supersedes the earlier one, or whether
  the earlier record's bytes at its own path were changed, using Git history for
  the record path (for example `git log --follow` over the record file) together
  with the record's own convention field. A byte change at the path of a ruled
  record without a superseding record is reported as a finding.
- **VER-003** — Boundary check on write locus: confirm by path inspection that
  every artifact produced by this deliverable resolves under the execution tree
  and that no file under the instruction surface — `AGENTS.md`, `agents/`,
  `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/` — was written
  by this deliverable's production, consistent with REQ-006.

Where no deterministic method settles a criterion, the matrix carries an
explicit `HUMAN_REVIEW` method instead of a fabricated check.

## Governing Values and Decisions — Axiology

- **AX-001** — Human judgment is the closing step. SOW-036's terminal artifacts
  are a superseding decision record or PR review, both of which terminate in an
  attributable human act. Nothing in this deliverable may substitute an
  agent-produced conformance finding for that act.
- **AX-002** — The instruction surface is governed separately. `_CONTEXT.md`
  states that any locus naming the instruction surface requires an
  independently authorized M2 tranche. This Scope of Work grants no such
  authorization, and its acceptance would grant none.
- **AX-003** — Nothing is inferred beyond the authorized sources (K-INVENT-1).
  Where the accepted decomposition is silent — for example on per-deliverable
  acceptance criteria and on `ResponsibleParty`, which is `Ryan Tufts` under D-GOV-27 and the current deliverable register — the accepted assignment is preserved, while the acceptance-criteria silence is surfaced rather than filled.
- **AX-004** — Bounded claims. SOW-037's convention is asserted only within its
  two record classes, matching the CLARIFIED label its scope-ledger `SourceRef`
  carries; a stronger general rule is the adopted PRD's separately labelled D-16
  and is not borrowed here.
- **AX-005** — Conformance observation, never repair. A finding against a ruled
  record is routed to the owner; correcting ruled content is itself a
  superseding act reserved to the governed record convention.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-036 OBJ-003 | CLM-001 REQ-001 REQ-002 REQ-005 REQ-006 | AC-001 | VER-001 VER-003 | Checklist document plus the per-record, per-field tabulation over `docs/governance_harness/_DECISIONS/`, with findings listed and unresolved |
| OUT-002 | SOW-036 OBJ-003 | CLM-001 CLM-004 REQ-003 REQ-005 | AC-002 | HUMAN_REVIEW: owner reading of the note against the terminal-artifact rule as it stands in the decision register and against SOW-036 | Note text with its SOW-036 and PRD §5.3 D-1 citations, and the owner's recorded reading |
| OUT-003 | SOW-037 OBJ-003 | CLM-002 CLM-003 REQ-004 REQ-005 REQ-006 | AC-003 | VER-002 VER-003 | Conformance report naming its two-class population, the supersession trace per examined correction, and any finding routed to the owner |
