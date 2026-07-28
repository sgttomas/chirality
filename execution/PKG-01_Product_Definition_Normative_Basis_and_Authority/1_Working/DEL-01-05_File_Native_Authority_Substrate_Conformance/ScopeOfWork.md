---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-05
package_id: PKG-01
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-014]
package_objective_refs: [OBJ-007]
---

# Scope of Work — DEL-01-05

## Purpose and Objective Traceability

This is the candidate production contract for `DEL-01-05` — File-Native
Authority Substrate Conformance — in package `PKG-01`. It covers project scope
item SOW-014 and supports package objective OBJ-007.

Traceability, transcribed and not inferred:

| Binding | Value | Source |
|---|---|---|
| Covered scope item | SOW-014 | `_CONTEXT.md` Scope Traceability; register `CoversScopeItems` |
| Supported objective | OBJ-007 | `_CONTEXT.md` Scope Traceability; register `SupportsObjectives` |
| Deliverable type | `REQ_SLICE` | register `Type` |
| Context envelope | `S` — "Narrow rule with a small inventory surface." | register `ContextEnvelope`/`ContextEnvelopeNotes` |
| Anticipated write locus | `execution-tree` | register `AnticipatedWriteLocus` |
| Responsible party | `Ryan Tufts` | D-GOV-27; current deliverable register `ResponsibleParty` |

Every `AC-*` and `VER-*` below is a **candidate**. The accepted decomposition
states no per-deliverable acceptance criteria (`_CONTEXT.md` Acceptance
Criteria), so nothing here is inferred beyond the four authorized grounding
sources: the register row, `_CONTEXT.md`, the SOW-014 scope-ledger statement,
and the adopted `docs/PRD_ROOT.md`. This document claims no acceptance and no
lifecycle state; the owner rules on it at a later human-gated review.

The outputs are OUT-001, OUT-002, and OUT-003, defined below.

## Deliverable Definition — Ontology

- **OUT-001** — Substrate conformance checklist: an execution-tree artifact that
  enumerates the authoritative governance and project-coordination surfaces in
  scope and records, per surface, whether it is a git-tracked plain file.
- **OUT-002** — Projection inventory: an execution-tree artifact listing the
  rebuildable projections that exist at the checked basis, each with its rebuild
  source and an explicit statement that it is never citable as authority.
- **OUT-003** — Recoverability evidence: a recorded check that the governed
  state named in OUT-001 is reconstructible from the checkout alone, with the
  method, the basis commit, and the result.

- **CLM-001** — Covered obligation (SOW-014, SourceRef `PRD §5.1 N-1
  [TRANSCRIBED]`, `DecisionRef DEC-004`): for authoritative governance and
  project-coordination state the substrate is git-tracked plain files; no
  external database, server state, or configuration holds that truth;
  rebuildable projections are permitted and never citable as authority; and a
  decision not in a versioned file does not exist for reliance.
- **CLM-002** — Scope boundary carried from the ledger `Notes` for SOW-014: the
  stated domain-engine exception is split out as SOW-015 and is **not** covered
  by this deliverable. This deliverable neither restates nor narrows that
  exception; encountering engine-owned domain truth is a routing question for
  the SOW-015 owner, not a finding here.
- **CLM-003** — Objective linkage (`docs/PRD_ROOT.md` §3 OBJ-7): the v1 success
  condition for OBJ-007 is that the full governed state — decisions, approvals,
  scope, evidence, and each loop's current position — survives loss of every
  non-file substrate and is recoverable from the checkout alone. OUT-003 is the
  evidence surface for that condition at this deliverable's scale; it does not
  by itself discharge OBJ-007 for the product.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The checklist (OUT-001) shall record, for each enumerated
  authoritative governance or project-coordination surface, that the surface is
  a git-tracked plain file, with the evidence used to determine it.
- **REQ-002** — The checklist shall record any case in which authoritative
  governance or project-coordination truth is held by an external database,
  server state, or configuration, as a finding rather than a correction.
- **REQ-003** — The projection inventory (OUT-002) shall mark every listed
  projection as rebuildable and as not citable as authority, and shall name the
  source from which it is rebuilt.
- **REQ-004** — The recoverability evidence (OUT-003) shall state the basis
  commit, the reconstruction method, and whether the enumerated state was
  recovered from the checkout alone.
- **REQ-005** — The enumeration in OUT-001 shall declare its own observation
  boundary — which surfaces were examined and which were not — so a reader can
  tell coverage from silence. Unknowns remain `TBD` rather than being filled in
  (`docs/PRD_ROOT.md` §5.1 N-4).
- **REQ-006** — No output shall assert that the SOW-015 domain-engine exception
  is satisfied, unsatisfied, or narrowed (CLM-002).

- **AC-001** — Every surface enumerated in OUT-001 carries a recorded
  git-tracked determination with its evidence, and any surface whose
  authoritative truth is held outside git-tracked plain files is recorded as a
  finding.
- **AC-002** — Every entry in OUT-002 names its rebuild source and carries the
  explicit "not citable as authority" statement.
- **AC-003** — OUT-003 records a reconstruction attempt from the checkout alone
  with its basis commit, method, and result, and its observation boundary is
  stated rather than implied.

## Production and Verification Method — Praxeology

Production sequence: enumerate the in-scope surfaces from the accepted
decomposition and coordination tree; determine tracked/ignored status per
surface with deterministic git commands; record projections and their rebuild
sources; then perform and record one reconstruction check. Deterministic
commands produce facts; they make no acceptance judgment.

- **VER-001** — Deterministic tracked-state check: for each surface listed in
  OUT-001, run `git ls-files --error-unmatch <path>` from the repository root
  and record the exit status. A non-zero status is an untracked surface and is
  reported as a finding, not silently dropped.
- **VER-002** — Deterministic projection check: for each entry in OUT-002, run
  `git check-ignore -v <path>` from the repository root and record the matching
  ignore rule, confirming the entry is an ignored rebuildable projection rather
  than tracked authority.
- **VER-003** — Deterministic recoverability check: produce a clean tree at the
  recorded basis with `git archive <commit>` (or an equivalent fresh checkout)
  into a scratch location outside the working tree, and confirm every surface
  enumerated in OUT-001 is present in it. The scratch location is not a write
  target of this deliverable.
- **VER-004** — `HUMAN_REVIEW: reviewer reads OUT-001..OUT-003 against the
  SOW-014 ledger statement and confirms the observation boundary is stated, no
  SOW-015 claim is made, and no finding was resolved by editing a governed
  surface.`

## Governing Values and Decisions — Axiology

- **AX-001** — Candidate status. Nothing in this document is accepted. `AC-*`
  and `VER-*` are candidates authored under the four authorized grounding
  sources; the owner's review is the accepting act (`docs/PRD_ROOT.md` §5.1 N-3;
  K-AUTH-1).
- **AX-002** — Write-locus boundary. The register's `AnticipatedWriteLocus` for
  this deliverable is `execution-tree`, and that is a planning note rather than
  authorization (`_CONTEXT.md`). Any act touching the instruction surface —
  `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, or
  `.github/workflows/` — requires an independently authorized M2 tranche, and
  **this Scope of Work grants none**. Instruction-surface files are read-only
  inputs to the checks above.
- **AX-003** — Findings are surfaced, not fixed. Where a check fails, the
  outputs record the discrepancy with pointers; conflicts are never silently
  resolved (`docs/PRD_ROOT.md` §5.1 N-4).
- **AX-004** — `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register
  (`_CONTEXT.md` Source Authority). No output claims an owner.
- **AX-005** — Deterministic checks are evidence, not authority. `VER-001`
  through `VER-003` compute facts about the checkout; they confer no acceptance,
  release, or reliance judgment (`docs/PRD_ROOT.md` §5.2 O-2).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-014 OBJ-007 | CLM-001 CLM-002 REQ-001 REQ-002 REQ-005 REQ-006 | AC-001 | VER-001 VER-004 | Per-surface tracked-state determination with recorded command exit status and stated observation boundary |
| OUT-002 | SOW-014 OBJ-007 | CLM-001 REQ-003 | AC-002 | VER-002 | Projection list with rebuild source, matching ignore rule, and explicit non-authority statement |
| OUT-003 | SOW-014 OBJ-007 | CLM-003 REQ-004 REQ-005 | AC-003 | VER-003 VER-004 | Recorded reconstruction from the checkout alone with basis commit, method, and result |
