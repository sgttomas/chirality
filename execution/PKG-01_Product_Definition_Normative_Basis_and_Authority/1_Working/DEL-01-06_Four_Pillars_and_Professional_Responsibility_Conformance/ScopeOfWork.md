---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-06
package_id: PKG-01
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-023, SOW-024]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-01-06

## Purpose and Objective Traceability

This is the candidate production contract for `DEL-01-06` — Four Pillars and
Professional-Responsibility Conformance — in package `PKG-01`. It covers project
scope items SOW-023 and SOW-024 and supports package objective OBJ-002.

Traceability, transcribed and not inferred:

| Binding | Value | Source |
|---|---|---|
| Covered scope items | SOW-023, SOW-024 | `_CONTEXT.md` Scope Traceability; register `CoversScopeItems` |
| Supported objective | OBJ-002 | `_CONTEXT.md` Scope Traceability; register `SupportsObjectives` |
| Deliverable type | `DOC_UPDATE` | register `Type` |
| Context envelope | `S` — "Documentation-shaped conformance over two stable clauses." | register `ContextEnvelope`/`ContextEnvelopeNotes` |
| Anticipated write locus | `execution-tree` | register `AnticipatedWriteLocus` |
| Responsible party | `TBD` | register `ResponsibleParty`; preserved unchanged |

Every `AC-*` and `VER-*` below is a **candidate**. The accepted decomposition
states no per-deliverable acceptance criteria (`_CONTEXT.md` Acceptance
Criteria); nothing here is inferred beyond the register row, `_CONTEXT.md`, the
SOW-023 and SOW-024 ledger statements, and the adopted `docs/PRD_ROOT.md`. This
document claims no acceptance and no lifecycle state.

The outputs are OUT-001 and OUT-002, defined below.

## Deliverable Definition — Ontology

- **OUT-001** — Pillar mapping note: an execution-tree note recording the
  four-pillar accountability ontology as the ledger states it, and mapping each
  pillar to where it is currently expressed, with any gap recorded as a finding.
- **OUT-002** — Responsibility-model activation note: an execution-tree note
  recording the professional-responsibility model's five carried elements and
  the boundary at which the model activates, with the activation boundary stated
  as such rather than as an applicability boundary for the product.

- **CLM-001** — Covered obligation (SOW-023, SourceRef `PRD §5.1 N-7
  [TRANSCRIBED]`): the four pillars — ontology, epistemology, praxiology,
  axiology — are the accountability ontology, and ontology, praxiology, and
  axiology exist to serve the epistemology. The service relation is part of the
  claim, not decoration: a mapping that lists four pillars without recording
  that relation does not restate SOW-023.
- **CLM-002** — Covered obligation (SOW-024, SourceRef `PRD §5.1 N-8
  [TRANSCRIBED]`): the professional-responsibility model holds where it
  activates — AI outputs are drafts; the licensed professional retains scope,
  code selection, hazard acceptance, adjudication and issuance rights;
  competence includes tool competence; and the hierarchy of authority runs laws
  → codes → project specifications → verified analysis → professional judgment.
- **CLM-003** — Activation boundary (`docs/PRD_ROOT.md` §2.2): the
  `docs/DIRECTIVE.md` §3 clause states the **activation boundary of the
  professional-responsibility model**, not the applicability boundary of the
  product, which is governed professional knowledge work generally. The phrase
  "where it activates" in SOW-024 is read against that distinction.
- **CLM-004** — Objective linkage (`docs/PRD_ROOT.md` §3 OBJ-2): OBJ-002 is
  satisfied by a deliverable stream in which every consequential acceptance,
  reliance, and issuance judgment is performed by an accountable human, while
  deterministic guards remain lawful non-human gates. This deliverable
  contributes the conformance record for the responsibility half of that
  condition; it does not run the stream and does not discharge OBJ-002.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The pillar mapping note (OUT-001) shall name all four pillars
  using the ledger's terms and shall state the service relation of CLM-001
  explicitly.
- **REQ-002** — For each pillar, OUT-001 shall record where that pillar is
  currently expressed, citing the surface, and shall record `TBD` where no
  expression was located rather than supplying one.
- **REQ-003** — The activation note (OUT-002) shall carry all five elements of
  CLM-002 — drafts, retained professional rights, tool competence, the
  hierarchy of authority, and the "where it activates" condition — with none
  paraphrased away.
- **REQ-004** — OUT-002 shall state the activation boundary of CLM-003 and shall
  not present it as the product's applicability boundary.
- **REQ-005** — Neither output shall assert that an agent, tool, validator, or
  runtime performs an acceptance, adjudication, or issuance act; those are
  reserved to the accountable human (`docs/PRD_ROOT.md` §5.1 N-3, §3 OBJ-2).
- **REQ-006** — Both outputs are `DOC_UPDATE`-shaped conformance records in the
  execution tree. Neither may change a governing clause; a needed change to a
  governing clause is recorded as a finding and routed, not applied.

- **AC-001** — OUT-001 names the four pillars in the ledger's terms, states the
  service relation to the epistemology, and records for each pillar either a
  cited current expression or an explicit `TBD`.
- **AC-002** — OUT-002 carries all five elements of CLM-002 intact, in the
  ledger's order of sense, and states the hierarchy of authority as an ordered
  chain rather than an unordered list.
- **AC-003** — OUT-002 states the activation boundary as the activation boundary
  of the responsibility model, distinct from the product's applicability, and
  neither output claims a non-human acceptance, adjudication, or issuance act.

## Production and Verification Method — Praxeology

Production sequence: transcribe the two ledger statements; locate each pillar's
current expression by reading the cited governing surfaces read-only; write the
mapping note; write the activation note against the §2.2 distinction; then check
both notes for authority-claim language before recording completion.

- **VER-001** — Deterministic anchor check: confirm the source anchors the two
  covered items cite still resolve, by locating the `N-7` and `N-8` rows in
  `docs/PRD_ROOT.md` §5.1 and the pillar and responsibility sections of
  `docs/DIRECTIVE.md` (`grep -n` over those files from the repository root).
  A non-resolving anchor is recorded as a finding, not repaired here.
- **VER-002** — `HUMAN_REVIEW: reviewer compares OUT-001 against the SOW-023
  ledger statement clause by clause and confirms the four pillars and the
  service relation are present and unweakened.`
- **VER-003** — `HUMAN_REVIEW: reviewer compares OUT-002 against the SOW-024
  ledger statement element by element — drafts, retained rights, tool
  competence, hierarchy of authority, activation condition — and confirms the
  activation boundary is stated per docs/PRD_ROOT.md §2.2.`
- **VER-004** — `HUMAN_REVIEW: reviewer scans both notes for language
  attributing acceptance, adjudication, issuance, approval, or certification to
  an agent, tool, validator, or runtime, and returns any occurrence as a
  finding.`

## Governing Values and Decisions — Axiology

- **AX-001** — Candidate status. Nothing here is accepted; `AC-*` and `VER-*` are
  candidates for owner review (`docs/PRD_ROOT.md` §5.1 N-3; K-AUTH-1).
- **AX-002** — Write-locus boundary. The register's `AnticipatedWriteLocus` is
  `execution-tree`, a planning note rather than authorization (`_CONTEXT.md`).
  Any act touching the instruction surface — `AGENTS.md`, `agents/`, `skills/`,
  `tools/`, root `docs/`, `init/`, or `.github/workflows/` — requires an
  independently authorized M2 tranche, and **this Scope of Work grants none**.
  `docs/DIRECTIVE.md` and `docs/PRD_ROOT.md` are read-only inputs here; a
  conformance finding against either is surfaced, never edited.
- **AX-003** — Conformance is preservation, not restatement authority. This
  deliverable keeps two stable clauses intact where they activate; it does not
  reinterpret them, extend them, or narrow the activation boundary.
- **AX-004** — Unknowns stay `TBD`. Where a pillar's current expression cannot
  be located, the note records that rather than inventing one
  (`docs/PRD_ROOT.md` §5.1 N-4).
- **AX-005** — `ResponsibleParty` remains `TBD` until a human assigns ownership
  (`_CONTEXT.md` Source Authority).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-023 OBJ-002 | CLM-001 CLM-004 REQ-001 REQ-002 REQ-006 | AC-001 | VER-001 VER-002 | Pillar-by-pillar mapping with cited expression or explicit TBD, and the service relation stated |
| OUT-002 | SOW-024 OBJ-002 | CLM-002 CLM-003 CLM-004 REQ-003 REQ-004 REQ-005 REQ-006 | AC-002 AC-003 | VER-001 VER-003 VER-004 | Element-by-element responsibility-model record with the activation boundary stated and no non-human authority claim |
