---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-07
package_id: PKG-01
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-006, SOW-092, SOW-094]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-01-07

## Purpose and Objective Traceability

This is the candidate production contract for `DEL-01-07` — Jurisdiction,
Accountability, and v1 User Scope Register — in package `PKG-01`. It covers
project scope items SOW-006, SOW-092, and SOW-094 and supports package objective
OBJ-001.

Traceability, transcribed and not inferred:

| Binding | Value | Source |
|---|---|---|
| Covered scope items | SOW-006, SOW-092, SOW-094 | `_CONTEXT.md` Scope Traceability; register `CoversScopeItems` |
| Supported objective | OBJ-001 | `_CONTEXT.md` Scope Traceability; register `SupportsObjectives` |
| Deliverable type | `REGISTER` | register `Type` |
| Context envelope | `S` — "Small register over ruled content; no machinery is introduced." | register `ContextEnvelope`/`ContextEnvelopeNotes` |
| Anticipated write locus | `execution-tree` | register `AnticipatedWriteLocus` |
| Responsible party | `TBD` | register `ResponsibleParty`; preserved unchanged |

Every `AC-*` and `VER-*` below is a **candidate**. The accepted decomposition
states no per-deliverable acceptance criteria (`_CONTEXT.md`); nothing here is
inferred beyond the register row, `_CONTEXT.md`, the three ledger statements,
and the adopted `docs/PRD_ROOT.md`. This document claims no acceptance and no
lifecycle state, and it records ruled content rather than ruling on anything.

The outputs are OUT-001, OUT-002, and OUT-003, defined below.

## Deliverable Definition — Ontology

- **OUT-001** — Jurisdiction/accountability register: an execution-tree register
  recording the ruled v1 jurisdiction and accountability model with its source
  ruling, and carrying the declared scaling path as expressly-not-current-scope.
- **OUT-002** — Capacity separability table: an execution-tree table recording
  the four human capacities and the rule that holding one confers none of the
  others, together with the recorded fact that v1 does not require them to be
  separately held.
- **OUT-003** — v1 user-scope statement: an execution-tree statement recording
  the ruled v1 user scope and its staged A → B → C trajectory, including why the
  trajectory is load-bearing rather than aspirational.

- **CLM-001** — Covered obligation (SOW-092, SourceRef `PRD §9.2 RD-2
  [OWNER_DECLARED — ruled]`): jurisdiction for v1 is a single root owner, and
  accountability is one accountable owner per root inherited by acts within it,
  with a declared scaling path that is expressly not current scope.
- **CLM-002** — Covered obligation (SOW-006, SourceRef `PRD §3 / §9.5 RD-5
  [OWNER_DECLARED — ruled]`): v1 targets the present owner-practitioner on a
  staged trajectory toward individual professional knowledge workers generally
  and then multi-practitioner organizations, and that trajectory is what keeps
  the discoverability condition non-trivial at v1.
- **CLM-003** — Covered obligation, boundary item (SOW-094, `InOutStatus OUT`,
  `DecisionRef DEC-007`, `OpenIssue TRUE`, ledger note `OI-009`): the
  database-backed multi-practitioner attribution interface named in the ruled
  evolution path is expressly not current scope, and its referent is `TBD` in
  the source rather than guessed. The register carries the `TBD` referent; it
  does not resolve it.
- **CLM-004** — Capacity separability (`docs/PRD_ROOT.md` §2.3): four capacities
  — root-governance authority, professional accountability for situated work,
  review, and product maintenance — are separable, holding one confers none of
  the others, and their being held by one person at the accepted basis is a fact
  about the present instantiation rather than a property of the product.
- **CLM-005** — Objective linkage (`docs/PRD_ROOT.md` §3 OBJ-1): OBJ-001 is
  satisfied when a reader can determine what governs from the repository alone.
  This register contributes the jurisdiction, accountability, and user-scope
  answers to that reader; it does not discharge OBJ-001 for the product.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — OUT-001 shall record the ruled jurisdiction and the ruled
  accountability model as two distinct axes, each attributed to the ruling that
  fixed it, and shall not merge them into a single statement.
- **REQ-002** — OUT-001 shall carry the declared scaling path with its
  expressly-not-current-scope standing preserved, so no later work can read the
  path as an obligation.
- **REQ-003** — OUT-002 shall list all four capacities of CLM-004, state that
  holding one confers none of the others, and record separately that v1 does not
  require them to be separately held.
- **REQ-004** — OUT-003 shall record the ruled v1 scope and all three stages of
  the trajectory with their standings — one as v1 scope, the other two as
  declared trajectory — and shall not present a later stage as current scope.
- **REQ-005** — The register shall carry SOW-094's `TBD` referent as `TBD`, with
  its open-issue standing recorded, and shall not substitute a guessed referent
  (`docs/PRD_ROOT.md` §5.1 N-4).
- **REQ-006** — The register introduces no machinery: no interface, database,
  delegation mechanism, or quorum rule is specified, implied, or scheduled by
  these outputs (register `ContextEnvelopeNotes`).
- **REQ-007** — Each entry shall cite its ruling source so a reader can reach the
  ruled text from the register alone.

- **AC-001** — OUT-001 records jurisdiction and accountability as separately
  attributed ruled positions, each citing its source, with the scaling path
  present and marked not current scope.
- **AC-002** — OUT-002 lists the four capacities with the confers-none rule and
  records the v1 non-requirement as a distinct statement rather than a
  qualification that weakens separability.
- **AC-003** — OUT-003 records the ruled v1 scope and all three stages with
  distinct standings, and carries the SOW-094 `TBD` referent unresolved with its
  open-issue standing visible.

## Production and Verification Method — Praxeology

Production sequence: transcribe the three ledger statements with their
SourceRefs; read the cited ruled sections of `docs/PRD_ROOT.md` read-only;
assemble the register, the capacity table, and the user-scope statement; then
re-check the live actor registry against the ruled jurisdiction claim and record
the result.

- **VER-001** — Deterministic live-registry check: read
  `docs/governance_harness/human_actors.md` and record the registered-actor
  entries it contains, comparing that count against the ruled single-root-owner
  jurisdiction recorded in OUT-001. Divergence is recorded as a finding and
  routed to the owner; the live registry governs and the register is not edited
  to agree with a stale narrative (`docs/PRD_ROOT.md` §5, registry discipline).
- **VER-002** — Deterministic anchor check: confirm the cited ruling anchors
  still resolve by locating the RD-2 and RD-5 sections and the §2.3 capacity
  table in `docs/PRD_ROOT.md` (`grep -n` from the repository root). A
  non-resolving anchor is a finding, not a repair.
- **VER-003** — `HUMAN_REVIEW: reviewer compares OUT-001 and OUT-003 against the
  SOW-092, SOW-006, and SOW-094 ledger statements and confirms every
  not-current-scope standing and every stage standing is preserved exactly.`
- **VER-004** — `HUMAN_REVIEW: reviewer confirms OUT-002 states the four
  capacities and the confers-none rule, and that the v1 non-requirement is
  recorded without being read back as a denial of separability.`

## Governing Values and Decisions — Axiology

- **AX-001** — Candidate status. Nothing here is accepted; `AC-*` and `VER-*` are
  candidates for owner review (K-AUTH-1).
- **AX-002** — Write-locus boundary. The register's `AnticipatedWriteLocus` is
  `execution-tree`, a planning note rather than authorization (`_CONTEXT.md`).
  Any act touching the instruction surface — `AGENTS.md`, `agents/`, `skills/`,
  `tools/`, root `docs/`, `init/`, or `.github/workflows/` — requires an
  independently authorized M2 tranche, and **this Scope of Work grants none**.
  `docs/governance_harness/human_actors.md` and `docs/PRD_ROOT.md` are read-only
  inputs to `VER-001` and `VER-002`.
- **AX-003** — Recording is not ruling. These outputs carry ruled content with
  attribution; they neither re-open a ruling nor extend one, and a disagreement
  with a ruling is surfaced to the owner rather than resolved here.
- **AX-004** — Not-current-scope standings are load-bearing. The scaling path and
  the B and C stages are carried precisely so later work cannot silently import
  them as obligations.
- **AX-005** — `ResponsibleParty` remains `TBD` until a human assigns ownership
  (`_CONTEXT.md` Source Authority).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-092 OBJ-001 | CLM-001 CLM-005 REQ-001 REQ-002 REQ-006 REQ-007 | AC-001 | VER-001 VER-002 VER-003 | Two attributed ruled positions with the scaling path recorded not-current-scope, plus the recorded live-registry comparison |
| OUT-002 | SOW-092 OBJ-001 | CLM-004 REQ-003 REQ-006 REQ-007 | AC-002 | VER-002 VER-004 | Four-capacity table with the confers-none rule and the v1 non-requirement recorded separately |
| OUT-003 | SOW-006 SOW-094 OBJ-001 | CLM-002 CLM-003 CLM-005 REQ-004 REQ-005 REQ-007 | AC-003 | VER-002 VER-003 | Ruled v1 scope with three stage standings and the unresolved SOW-094 TBD referent carried with its open-issue standing |
