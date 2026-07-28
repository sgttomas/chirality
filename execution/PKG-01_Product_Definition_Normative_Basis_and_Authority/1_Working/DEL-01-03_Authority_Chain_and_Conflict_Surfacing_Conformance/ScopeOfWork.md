---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-03
package_id: PKG-01
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-018, SOW-022]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-01-03

## Purpose and Objective Traceability

This Scope of Work defines the production contract for DEL-01-03, *Authority
Chain and Conflict-Surfacing Conformance*, in package PKG-01. Its declared
basis is the accepted root decomposition named in `decomposition_basis`; its
covered project scope is SOW-018 and SOW-022; its package objective is
OBJ-001.

Per the accepted register row, the deliverable exists to *"keep the DIRECTIVE
-> CONTRACT -> SPEC -> TYPES chain plus the live instruction surface
determinable from the repository alone, and keep epistemic discipline
architectural: mandatory provenance, TBD over guessing, conflicts surfaced
with pointers, claims calibrated."* The accepted `ContextEnvelope` note reads
*"bounded to the governance corpus and its conflict surfaces."*

**Write-locus boundary.** The accepted `AnticipatedWriteLocus` for this
deliverable is *"execution-tree; instruction-surface (M2) if a chain statement
must change."* `AnticipatedWriteLocus` is a planning note, not authorization.
Any act touching the instruction surface — `AGENTS.md`, `agents/`, `skills/`,
`tools/`, root `docs/`, `init/`, `.github/workflows/` — **requires an
independently authorized M2 tranche. This Scope of Work grants none.** A chain
statement that must change is surfaced here and routed, never edited from this
contract.

No lifecycle state, acceptance, or reliance is asserted by this document. The
definitions below are candidate content for owner review.

## Deliverable Definition — Ontology

### Expected outputs

- **OUT-001** — Authority-chain reading map: the recorded route by which a
  reader determines, from the repository alone, which document is
  authoritative for a given question across `docs/DIRECTIVE.md`,
  `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, and the live
  instruction surface.
- **OUT-002** — Conflict register: the standing record of conflicts between
  governance surfaces, each entry carrying pointers to both sides and a
  disposition.
- **OUT-003** — Provenance-label conformance notes: the record of whether the
  epistemic-discipline commitments hold across the surveyed surfaces, with
  unknowns carried as `TBD`.

### Covered scope statements

- **CLM-001** — SOW-018 (`PRD §5.1 N-4 [TRANSCRIBED]`) states that epistemic
  discipline is architectural rather than advisory: mandatory provenance,
  unknowns become `TBD` rather than guesses, conflicts are surfaced with
  pointers rather than silently resolved, and claims are calibrated to their
  warrant. The adopted PRD sources this to K-PROV-1, K-INVENT-1, K-CONFLICT-1,
  K-CLAIM-1 and `docs/DIRECTIVE.md` §2.4. Ledger categories are
  `NormativeBasis;Evidence`.
- **CLM-002** — SOW-022 (`PRD §5.1 N-6 [TRANSCRIBED]`) states that the
  authority chain runs DIRECTIVE to CONTRACT to SPEC to TYPES with the live
  instruction surface alongside; where a lower or candidate document conflicts
  with ratified governance, ratified governance controls and the conflict is
  surfaced. The adopted PRD sources this to `docs/DIRECTIVE.md` §Authority
  chain.
- **CLM-003** — The adopted PRD states OBJ-001's v1 success condition in the
  terms this deliverable must satisfy: for every governance surface in the
  instruction root, a reader can determine without asking a person which
  document is authoritative for a given question, whether it is ratified, and
  what superseded it; and no ratified clause has an unrecorded conflicting
  live variant. PRD Revision 6 records C-1 closed by D-GOV-23 and C-2
  closed by PR #345/Receipt 44. DEL-01-01 and DEL-01-02 retain their standing
  verification roles; this deliverable holds the standing register and
  surfaces new conflicts without reruling those closures.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — OUT-001 shall enumerate the governance surfaces it covers and,
  for each, record which document is authoritative for which class of
  question, whether it is ratified, and what superseded it (CLM-002, CLM-003).
  Coverage is stated as an output, never assumed.
- **REQ-002** — OUT-001 shall record the ordering rule explicitly: where a
  lower or candidate document conflicts with ratified governance, ratified
  governance controls and the conflict is surfaced (CLM-002).
- **REQ-003** — Every entry in OUT-002 shall carry pointers to both
  conflicting sources and a disposition. No conflict shall be recorded as
  resolved without naming the instrument that resolved it; an outstanding
  ruling is carried as `TBD` (CLM-001).
- **REQ-004** — Every claim in OUT-001, OUT-002, and OUT-003 shall carry a
  provenance label and a source pointer; unknowns shall be recorded as `TBD`
  rather than guessed (CLM-001).
- **REQ-005** — Where conformance work finds that a chain statement on the
  instruction surface must change, this deliverable shall surface it with
  pointers and route it as an M2 tranche candidate. It shall not edit the
  instruction surface.

- **AC-001** — For every governance surface enumerated in OUT-001, the map
  records the authoritative document for its question class, its ratification
  status, and its superseding instrument or an explicit `TBD` — and a reader
  can follow the map from the repository alone, without a person.
- **AC-002** — Every OUT-002 entry cites both conflicting sources by file and
  section and carries a disposition; entries with no ruling carry `TBD`, and
  no ratified clause listed in OUT-001 has a live conflicting variant that is
  absent from OUT-002.
- **AC-003** — Every claim in OUT-003 carries a provenance label and a source
  pointer, and no unknown is stated as a fact; each surveyed surface is
  recorded as conforming, non-conforming with pointers, or `TBD`.

## Production and Verification Method — Praxeology

Production sequence for this deliverable:

1. Enumerate the governance corpus and the live instruction surface at a
   recorded basis revision (REQ-001).
2. Build OUT-001 as a reading map, recording the ordering rule of CLM-002
   explicitly (REQ-002).
3. Build OUT-002 from conflicts observed against that map, each with pointers
   on both sides and a disposition (REQ-003).
4. Record OUT-003 by checking each surveyed surface against the four
   epistemic-discipline commitments of CLM-001 (REQ-004).
5. Route any required chain-statement change as an M2 candidate; make no
   instruction-surface edit under this contract (REQ-005).

- **VER-001** — Run
  `python3 tools/validation/validate_instruction_entrypoints.py` and record its
  exit status and output. It validates the root instruction entrypoints and
  the import contract by which a reader reaches the live instruction surface,
  which is the mechanically checkable part of OUT-001. It does not judge the
  authority ordering itself.

No registered deterministic tool judges whether the authority ordering is
correctly stated, whether a conflict register is complete, or whether a claim
is calibrated to its warrant. Those rows carry named human-review methods in
the matrix rather than a fabricated tool reference.

## Governing Values and Decisions — Axiology

- **AX-001** — Ratified governance controls. Where a lower or candidate
  document conflicts with it, the ratified text governs and the conflict is
  recorded rather than reconciled in place (CLM-002).
- **AX-002** — Determinable from the repository alone. The map must let a
  reader settle an authority question without asking a person; that is the
  stated OBJ-001 condition (CLM-003).
- **AX-003** — Conflicts are surfaced with pointers, never silently resolved,
  and unknowns become `TBD` rather than guesses (CLM-001).
- **AX-004** — Claims are calibrated to their warrant. This deliverable
  records what it verified and at which revision, and does not upgrade an
  observation into an acceptance (CLM-001).
- **AX-005** — The instruction surface is gated. A chain statement that must
  change is routed as an M2 tranche candidate requiring independent owner
  authorization; this Scope of Work grants none.
- **AX-006** — Nothing in this contract asserts acceptance, lifecycle state,
  or professional reliance. `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-022 OBJ-001 | CLM-002 CLM-003 REQ-001 REQ-002 REQ-005 | AC-001 | VER-001 | The reading map, the recorded basis revision, and the recorded validator exit status and output |
| OUT-002 | SOW-018 SOW-022 OBJ-001 | CLM-001 CLM-002 REQ-003 | AC-002 | HUMAN_REVIEW: Owner or delegated reviewer walks each register entry back to both cited sources and confirms the disposition, and confirms that no ratified clause in the reading map has an unrecorded live variant | The conflict register, both cited sources per entry, and the reviewer's recorded confirmation |
| OUT-003 | SOW-018 OBJ-001 | CLM-001 REQ-004 | AC-003 | HUMAN_REVIEW: Owner or delegated reviewer samples the recorded claims and confirms each carries a provenance label and source pointer and that unknowns are carried as TBD rather than asserted | The conformance notes, the sampled claims with their labels and pointers, and the recorded sample basis |
