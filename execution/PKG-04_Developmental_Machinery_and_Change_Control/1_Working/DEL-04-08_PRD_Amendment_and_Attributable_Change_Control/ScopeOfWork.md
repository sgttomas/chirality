---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-08
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-047, SOW-051, SOW-085, SOW-096, SOW-102]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-04-08

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-04-08`, PRD
Amendment and Attributable Change Control, a `REQ_SLICE` deliverable of
`PKG-04_Developmental_Machinery_and_Change_Control`. It serves project scope
items SOW-047, SOW-051, SOW-085, SOW-096 and SOW-102, and package objective
OBJ-003.

The register describes the deliverable as keeping the adopted PRD amendable
only by a superseding instrument bound to a git SHA, keeping every change to
approved content a new attributable act with prior bytes recoverable, keeping
declared-immutable classes never overwritten while living surfaces amend in
place, and keeping provenance labels from decaying.

OBJ-003 requires that the human evaluation and iteration loops close, with
structural completeness holding universally: every accepted change has a
retrievable linkage, from files alone, between the evidence that informed it,
the ruling that accepted it, and the state it changed. Change control is the
mechanism that makes that linkage exist at all, which is why these five items
converge on one deliverable.

The register records ContextEnvelope `M` with the note that this is one
change-control regime with an enumerated immutable-class list.

## Deliverable Definition — Ontology

The anticipated artifacts recorded in the register and `_CONTEXT.md` are an
amendment procedure note, an immutable-class register, a label-integrity check,
and placement pointer maintenance. They are expressed here as four outputs.

- **OUT-001** — An amendment procedure note stating how the adopted PRD is
  amended: by a superseding instrument bound to a git SHA, as a new attributable
  act, with the adopted bytes never overwritten at their path.
- **OUT-002** — An immutable-class register enumerating the artifact classes
  declared immutable, distinguishing them from living authoritative surfaces
  that amend in place, and recording where prior approved bytes are recoverable.
- **OUT-003** — A label-integrity check over provenance labels, reporting any
  label that changed without a superseding instrument and any item relied upon
  as adopted while still labelled PROPOSED.
- **OUT-004** — A placement pointer maintenance record showing that the pointer
  identifies the exact adopted bytes and that the split between the doctrinal
  and coordination surfaces holds.

- **CLM-001** — SOW-047 states that once adopted the PRD is amended only by a
  superseding instrument bound to a git SHA, that the adopted bytes are never
  overwritten at their path, and that each revision is a new attributable act.
  Its SourceRef is PRD §5.3 D-13, whose source label is PROPOSED; the ledger
  note records that the adoption instrument puts the PROPOSED items in effect
  while the source bytes retain the label.
- **CLM-002** — SOW-051 states the general rule: any change to previously
  approved content requires a new attributable act bound to the resulting SHA
  with prior approved bytes recoverable in Git; only artifact classes explicitly
  declared immutable are never overwritten at their path, while living
  authoritative surfaces amend in place through accepted commits. Its SourceRef
  is PRD §5.3 D-16, which names the immutable classes as decision records,
  accepted candidate packets, and snapshots, and names living surfaces
  including `AGENTS.md`, `docs/DIRECTIVE.md`, `docs/SPEC.md`, `docs/TYPES.md`,
  and status files.
- **CLM-003** — The two rules are not the same rule at different scopes. PRD
  §5.3 D-2 is expressly confined to two record classes and states that the
  broader change-control rule is carried separately at D-16. The register must
  therefore not silently widen D-2 into the general rule.
- **CLM-004** — SOW-096 states that placement is a split with a pointer: the
  adopted bytes are placed on the doctrinal surface through the existing export
  allowlist with no boundary change, candidates and revision evidence remain
  immutable on the coordination surface, and future amendments are
  instruction-surface tranches. Its SourceRef is PRD §9.4 RD-4, an owner-ruled
  decision.
- **CLM-005** — SOW-102 states that adoption requires the exact bytes bound at
  a named SHA, the bidirectional concordance map, and the owner ruling recorded
  verbatim and attributed to a matching registered actor; that no agent act
  substitutes for any of these; and that until adoption every PROPOSED item is
  inert while transcribed commitments remain in force on their own authority.
- **CON-001** — SOW-085 and SOW-102 both carry `OpenIssue: TRUE` against
  OI-002: the adoption instrument records that the PROPOSED items take effect,
  while the source bytes still carry the PROPOSED label. This is a live
  label-status question for owner ruling. It is surfaced here and not resolved;
  resolving it by choosing a reading would itself be the label decay SOW-085
  names.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The amendment procedure note shall state the superseding-
  instrument requirement, the git-SHA binding, and the never-overwrite-at-path
  property of the adopted bytes, and shall state that no agent act substitutes
  for the owner ruling, the exact-byte binding, or the bidirectional
  concordance map (SOW-047, SOW-102).
- **REQ-002** — The immutable-class register shall enumerate the declared
  immutable classes and, separately, the living authoritative surfaces that
  amend in place, and shall not classify a living surface as immutable
  (SOW-051).
- **REQ-003** — The label-integrity check shall report, without resolving, any
  provenance label that changed without a superseding instrument and any
  PROPOSED item relied upon as though adopted (SOW-085; PRD §8.2 F6).
- **REQ-004** — The placement pointer maintenance record shall show that the
  pointer resolves to the exact adopted bytes and shall record that no export
  boundary change accompanied placement (SOW-096).

- **AC-001** — The amendment procedure note names all three adoption
  requirements of SOW-102 and both properties of SOW-047, and asserts no
  amendment authority of its own.
- **AC-002** — Every entry in the immutable-class register is either a declared
  immutable class or a living surface, with no entry in both and no living
  surface listed as never-overwritable; the register cites D-16 for the
  membership rather than deriving it.
- **AC-003** — The label-integrity check reports its findings as findings,
  leaves OI-002 open, and changes no provenance label.
- **AC-004** — The pointer record demonstrates byte identity between the
  pointer target and the adopted bytes, and records the placement as
  boundary-neutral.

## Production and Verification Method — Praxeology

Production reads the change-control rules from their cited PRD locations,
compiles the registers, and runs the mechanical checks. It performs no
amendment.

- **VER-001** — For each path in the declared immutable classes, enumerate
  modifying commits with
  `git log --diff-filter=M --follow -- <path>`, expecting an empty result;
  a nonempty result is reported as a finding rather than corrected.
- **VER-002** — Compare the pointer target bytes to the adopted bytes with
  `git hash-object <path>` on both, or `shasum -a 256` on the resolved files,
  expecting identical digests.
- **VER-003** — Demonstrate recoverability of prior approved bytes by resolving
  each recorded prior revision with `git show <sha>:<path>` for the SHAs the
  register records, expecting each to resolve.

Whether the amendment procedure note faithfully restates the adoption mechanics
and whether the label-integrity findings are correctly characterized are
semantic judgments over provenance labels, not mechanical comparisons; PRD §5.3
D-14 records that four of the nine currency classes require semantic judgment.
They are routed to human review in the matrix below.

## Governing Values and Decisions — Axiology

- **AX-001** — Only humans author binding approvals, and approvals bind to a
  specific git SHA (PRD §5.1 N-3; K-AUTH-1, K-AUTH-2). No output of this
  deliverable amends, adopts, or relabels anything.
- **AX-002** — Conflicts are surfaced with pointers and never silently
  resolved (PRD §5.1 N-4). OI-002 is carried open by CON-001.
- **AX-003** — The register records `AnticipatedWriteLocus: execution-tree;
  instruction-surface (M2) for any PRD amendment`. That is a planning note, not
  authorization. PRD §9.4 RD-4 states that every amendment to the adopted PRD
  is an M2 instruction-surface tranche requiring independent owner
  authorization, a tranche manifest, routed notices, and export-manifest
  regeneration. This Scope of Work grants no such act on `AGENTS.md`, `agents/`,
  `skills/`, `tools/`, root `docs/`, `init/`, or `.github/workflows/`; any such
  act requires an independently authorized M2 tranche.
- **AX-004** — Every `AC-*` and `VER-*` defined here is a candidate. This
  document claims no acceptance, no approval, and no lifecycle state. The
  accepted decomposition states no per-deliverable acceptance criteria and
  `ResponsibleParty` remains `TBD`; nothing is inferred to fill either gap
  (K-INVENT-1).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-047 SOW-102 OBJ-003 | REQ-001 CLM-001 CLM-005 | AC-001 | HUMAN_REVIEW: owner reading of the procedure note against PRD §5.3 D-13 and §10.3 adoption mechanics | Procedure note citing each adoption requirement to its PRD location, with no authority claim of its own |
| OUT-002 | SOW-051 OBJ-003 | REQ-002 CLM-002 CLM-003 | AC-002 | VER-001 VER-003 | Two-column register with per-class citation to D-16, an empty modifying-commit result per immutable path, and resolvable prior-revision SHAs |
| OUT-003 | SOW-085 OBJ-003 | REQ-003 CON-001 | AC-003 | HUMAN_REVIEW: owner adjudication of the label-integrity findings and the open OI-002 label-status question | Findings list with each item traced to the label and instrument at issue, OI-002 recorded as open |
| OUT-004 | SOW-096 OBJ-003 | REQ-004 CLM-004 | AC-004 | VER-002 | Matching digests for pointer target and adopted bytes, plus a recorded boundary-neutrality statement |
