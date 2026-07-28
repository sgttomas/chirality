---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-01
package_id: PKG-01
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-084, SOW-088, SOW-089, SOW-090, SOW-091, SOW-095, SOW-098]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-01-01

## Purpose and Objective Traceability

This Scope of Work defines the production contract for DEL-01-01, *Genus
Concordance Closure and Standing Bidirectional Map*, in package PKG-01. Its
declared basis is the accepted root decomposition named in
`decomposition_basis`; its covered project scope is SOW-084, SOW-088, SOW-089,
SOW-090, SOW-091, SOW-095, SOW-098; its package objective is OBJ-001.

Per the accepted register row, the deliverable exists to *"verify and hold
closed the RD-1 genus concordance: obligations (a) DIRECTIVE §1 supersession,
(b) README reword, (c) SPEC/TYPES/AGENTS.md prose propagation; maintain the
bidirectional PRD <-> DIRECTIVE §1 concordance map (RD-3 form y) and keep F5
observable."*

**Standing nature.** The covered ledger entries for obligations (a), (b), (c)
and conflict C-1 carry the note `OI-001`: an accepted act at the current basis
*appears* to have discharged them, so coverage here is **standing
verification, not re-performance**. This contract is written for that posture.

**Write-locus boundary.** The accepted `AnticipatedWriteLocus` for this
deliverable is *"execution-tree; instruction-surface (M2) only if residual
drift requires an exact-prose act."* `AnticipatedWriteLocus` is a planning
note, not authorization. Any act touching the instruction surface —
`AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`,
`.github/workflows/` — **requires an independently authorized M2 tranche.
This Scope of Work grants none.**

No lifecycle state, acceptance, or reliance is asserted by this document. The
definitions below are candidate content for owner review.

## Deliverable Definition — Ontology

### Expected outputs

- **OUT-001** — Concordance-map register: the bidirectional PRD ↔
  `docs/DIRECTIVE.md` §1 coverage map in RD-3 form y, with uncovered items on
  either side marked `TBD`.
- **OUT-002** — Closure verification note recording, for each of RD-1
  obligations (a), (b), and (c), the observed disposition at a named basis
  revision and the evidence relied on.
- **OUT-003** — F5 observation record: the standing record of whether the
  concordance falsifier F5 is observed, checked against OUT-001.
- **OUT-004** — Residual exact-prose supersession packet, produced **only if**
  standing verification finds residual drift requiring an exact-prose act on
  the instruction surface. Producing or landing this packet is an M2 act
  outside this contract's authority.

### Covered scope statements

- **CLM-001** — SOW-084 (`PRD §8.2 F5 [PROPOSED]`) states that F5 —
  concordance failure — occurs when the adopted PRD and the ratified genus
  clause come to say incompatible things about what the root product is,
  without a recorded superseding act on one of them. The ledger records the
  label as in effect per the D-GOV-22 adoption ruling, confirmed at the
  D-GOV-25 ruling with the source label unchanged.
- **CLM-002** — SOW-088 (`PRD §9.1 RD-1 [OWNER_DECLARED - ruled]`) states that
  the ruled genus settles what the product is for this PRD and does not by
  itself amend any governance surface.
- **CLM-003** — SOW-089 (`PRD §9.1 obligation (a) [OWNER_DECLARED - ruled]`)
  states obligation (a): supersede the ratified genus clause through an
  exact-prose, human-gated act, until which the ratified clause remains in
  force as written. Ledger `DecisionRef` is DEC-009; the item is carried as an
  open issue with note OI-001.
- **CLM-004** — SOW-090 (`PRD §9.1 obligation (b) [OWNER_DECLARED - ruled]`)
  states obligation (b): reword the non-binding derivative top-level
  description to the ruled genus, as propagation rather than supersession.
  `DecisionRef` DEC-009; OI-001 applies.
- **CLM-005** — SOW-091 (`PRD §9.1 obligation (c) [OWNER_DECLARED - ruled]`)
  states obligation (c): survey the specification, vocabulary, and live-index
  prose that leans on the contained-level term and propagate where the ruled
  two-level formulation changes the sense; the survey's scope is its own
  output rather than assumed. `DecisionRef` DEC-009; OI-001 applies.
- **CLM-006** — SOW-095 (`PRD §9.3 RD-3 [OWNER_DECLARED - ruled]`) states that
  the adoption instrument is a decision record on the exact-candidate-SHA
  pattern, and that the concordance map it carries is bidirectional with
  uncovered items on either side marked `TBD` — the artifact the concordance
  falsifier is checked against.
- **CLM-007** — SOW-098 (`PRD §10.2 C-1 [CLARIFIED]`) states that conflict
  C-1 — the genus wording divergence between the ratified clause, the
  derivative top-level description, and the ruled genus — is resolved in
  principle with concordance pending, and closes fully only when the
  concordance tranche lands. `DecisionRef` DEC-009; OI-001 records that it
  appears closed by an accepted act at the current basis.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The register in OUT-001 shall be bidirectional in the RD-3
  form-y sense (CLM-006): it shall carry rows in both directions and shall
  mark uncovered items on either side `TBD` rather than omitting them.
- **REQ-002** — The closure note in OUT-002 shall record a disposition for
  each of obligations (a), (b), and (c) (CLM-003, CLM-004, CLM-005) that is
  bound to a named basis revision and cites the act relied on, and shall
  distinguish standing verification from re-performance per OI-001.
- **REQ-003** — The outputs shall not assert that any governance surface has
  been amended. Per CLM-002 the ruling settles the genus for the PRD only;
  per CLM-003 the ratified clause remains in force as written until the
  exact-prose act lands.
- **REQ-004** — The outputs shall not close C-1 (CLM-007) on their own
  authority. C-1 closes fully only when the concordance tranche lands, which
  is an owner-gated act.
- **REQ-005** — OUT-004, if produced, shall be scoped as an M2 instruction
  surface packet requiring independent owner authorization, a single
  serialized integration owner, a tranche manifest, and routed notices. This
  contract authorizes no instruction-surface write.

- **AC-001** — OUT-001 contains rows in both directions (PRD → `DIRECTIVE`
  §1 and `DIRECTIVE` §1 → PRD), every row resolves to a cited section or
  clause on both sides or is explicitly marked `TBD`, and no row is silently
  omitted.
- **AC-002** — OUT-002 records exactly one disposition for each of obligations
  (a), (b), (c), each disposition names the basis revision and the evidence
  relied on, and each is labelled either *discharged at the named basis* or
  *residual*; a residual disposition names OUT-004 as its routed follow-on.
- **AC-003** — OUT-003 states, at a named basis revision, whether F5 is
  observed or not observed, and cites the OUT-001 rows that support the
  statement; it makes no claim that a governance surface was amended.

## Production and Verification Method — Praxeology

Production sequence for this deliverable:

1. Read the adopted PRD sections cited in CLM-001 through CLM-007 and the
   corresponding sections of `docs/DIRECTIVE.md` §1, at a recorded revision.
2. Build OUT-001 as a two-directional coverage table, marking uncovered items
   on either side `TBD` (REQ-001).
3. Record the observed disposition of obligations (a), (b), (c) into OUT-002
   against that same recorded revision (REQ-002), preserving the standing
   verification posture of OI-001.
4. Derive OUT-003 from OUT-001 only; F5 is checked against the map, not
   asserted independently (CLM-001, CLM-006).
5. If and only if step 3 finds residual drift, prepare OUT-004 as an M2
   packet proposal and route it for independent authorization (REQ-005).

- **VER-001** — For OUT-004 only: run
  `python3 tools/validation/validate_instruction_tranche_manifest.py` (the
  registered G4 guard for `instruction-tranche-manifest/v1`) against the
  packet's tranche manifest and record its exit status and output. A passing
  manifest is a structural precondition, never an authorization to land the
  packet.

No registered deterministic tool verifies the semantic content of OUT-001,
OUT-002, or OUT-003 at this basis. Those rows therefore carry a named
human-review method in the matrix rather than a fabricated tool reference.

## Governing Values and Decisions — Axiology

- **AX-001** — Ratified governance controls. The ruled genus settles the
  product definition for the PRD and amends nothing by itself (CLM-002); the
  ratified clause remains in force as written until obligation (a) lands
  (CLM-003).
- **AX-002** — Conflicts are surfaced, not silently resolved. C-1 stays listed
  with pointers until the concordance tranche lands (CLM-007), and uncovered
  map items are marked `TBD` rather than dropped (CLM-006).
- **AX-003** — The instruction surface is gated. Any exact-prose act on
  ratified root `docs/`, `AGENTS.md`, `agents/`, `skills/`, `tools/`, `init/`,
  or `.github/workflows/` is an M2 governance tranche requiring independent
  owner authorization; this Scope of Work grants none.
- **AX-004** — Standing verification is not re-performance. Where OI-001
  records that an accepted act appears to have discharged an obligation, this
  deliverable verifies and holds that state; it does not redo the act.
- **AX-005** — Nothing in this contract asserts acceptance, lifecycle state,
  or professional reliance. `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-095 SOW-098 OBJ-001 | CLM-006 CLM-007 REQ-001 | AC-001 | HUMAN_REVIEW: Owner or delegated reviewer reads the register row-by-row against docs/PRD_ROOT.md §9.3 and docs/DIRECTIVE.md §1 at the recorded revision and confirms bidirectional coverage with TBD marking | The register artifact, the recorded basis revision, and the reviewer's recorded confirmation |
| OUT-002 | SOW-088 SOW-089 SOW-090 SOW-091 OBJ-001 | CLM-002 CLM-003 CLM-004 CLM-005 REQ-002 REQ-003 REQ-004 | AC-002 | HUMAN_REVIEW: Owner or delegated reviewer checks each recorded obligation disposition against the cited accepted act at the named basis revision and confirms the standing-verification posture of OI-001 | The closure note, the cited acts, and the named basis revision |
| OUT-003 | SOW-084 OBJ-001 | CLM-001 REQ-003 | AC-003 | HUMAN_REVIEW: Owner or delegated reviewer confirms the F5 observation statement is derived from the OUT-001 rows cited and from no other basis | The F5 observation record and the OUT-001 rows it cites |
| OUT-004 | SOW-089 OBJ-001 | CLM-003 REQ-005 | AC-002 | VER-001 | Tranche manifest, recorded validator exit status and output, and the independent M2 authorization reference |
