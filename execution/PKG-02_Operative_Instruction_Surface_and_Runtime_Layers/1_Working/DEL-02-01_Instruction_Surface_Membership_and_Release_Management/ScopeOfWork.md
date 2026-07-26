---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-01
package_id: PKG-02
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-026]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-02-01

## Purpose and Objective Traceability

This contract defines the production scope of `DEL-02-01` — Instruction Surface
Membership and Release Management — in service of project scope item `SOW-026`
and package objective `OBJ-001`, as recorded in the accepted root decomposition
and its companion deliverable register.

The accepted register states the deliverable's purpose as keeping the shared
instruction surface membership explicit, release-managed, and read-mostly, so
that changing it is a repo-wide governance action rather than ordinary
working-root execution.

**Claim status.** Every `OUT-*`, `CLM-*`, `REQ-*`, `AC-*`, `VER-*`, `CON-*`, and
`AX-*` definition below is a *candidate* authored under `MODE=INIT` from the
four authorized grounding sources named in the Axiology section. Nothing here
claims acceptance, review outcome, or lifecycle state. The deliverable's
lifecycle state remains whatever `_STATUS.md` records; this contract neither
reads authority into nor transitions that state.

**Write-locus gate.** The register records this deliverable's
`AnticipatedWriteLocus` as `instruction-surface (M2)`. That is a planning note,
not authorization. Any act that changes `AGENTS.md`, `agents/`, `skills/`,
`tools/`, root `docs/`, or `init/` requires an independently authorized M2
tranche. **This Scope of Work grants no such authorization**, and producing the
outputs below does not create one.

## Deliverable Definition — Ontology

The anticipated artifacts are transcribed from the register's
`AnticipatedArtifacts` field and the deliverable's `_CONTEXT.md`.

- **OUT-001** — Instruction-surface membership register: an explicit enumeration
  of the paths that constitute the shared instruction surface, each entry bound
  to its stated source, so that membership is answered by a register rather than
  inferred from narrative.
- **OUT-002** — M2 tranche checklist: the ordered change-path steps a proposed
  instruction-surface change must satisfy before it is carried, expressed as a
  checkable list rather than prose guidance.
- **OUT-003** — Read-mostly conformance notes: notes recording how the
  release-managed, read-mostly property is currently held, and where an observed
  practice diverges from the stated property.

The register records `ContextEnvelope: M` with the note "One membership
definition plus the change-path checklist", which bounds these outputs to one
membership definition plus its change path.

## Completion and Reliance Basis — Epistemology

- **CLM-001** — Covered scope item `SOW-026` (SourceRef: PRD §5.2 O-1
  [TRANSCRIBED]) states that the shared instruction surface is release-managed
  and read-mostly, and that changing it is a repo-wide governance action rather
  than ordinary working-root execution.
- **CLM-002** — The adopted PRD item O-1 enumerates the shared instruction
  surface as `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, and
  `init/`.
- **REQ-001** — The membership register shall enumerate instruction-surface
  membership explicitly and cite, per entry, the accepted statement that places
  that path in the surface. Membership shall not be inferred from a narrative
  list.
- **REQ-002** — The change-path checklist shall express instruction-surface
  change as a repo-wide governance action gated by an authorized M2 tranche, and
  shall not describe such a change as ordinary working-root execution.
- **CON-001** — Unresolved membership conflict: the adopted PRD item O-1
  enumerates six instruction-surface members (`CLM-002`), while this
  deliverable's `_CONTEXT.md` write-locus note enumerates the same six plus
  `.github/workflows/`. The two authorized sources disagree on membership. This
  conflict is surfaced, not resolved here; it is exactly the question `OUT-001`
  exists to settle, and settling it is an owner act.
- **AC-001** — The membership register enumerates every path named as an
  instruction-surface member by an authorized source, carries a source citation
  per entry, and records `CON-001` as an open membership question rather than
  silently adopting either enumeration.
- **AC-002** — The M2 tranche checklist states, as a required step, that an
  instruction-surface change is carried only under an authorized M2 tranche, and
  contains no step that authorizes such a change by production activity alone.
- **AC-003** — The read-mostly conformance notes distinguish, for each recorded
  observation, the stated property from the observed practice, and cite the
  authorized source for the stated property.

## Production and Verification Method — Praxeology

Verification below names only surfaces that exist in this repository. Where no
deterministic check exists for a criterion, the matrix records an explicit
`HUMAN_REVIEW` method rather than naming an invented command.

- **VER-001** — Run `python3 tools/validation/validate_root_surface_ownership.py`
  (guard G2, no arguments; reads `execution/_harness/surface_ownership.yaml`).
  It deterministically checks the static root surface-ownership register,
  including each entry's declared write targets and its `instruction_surface`
  flag. It is evidence about register conformance; it does not decide
  membership.
- **VER-002** — Run `python3 tools/validation/validate_instruction_tranche_manifest.py`
  (guard G4; optional `--base` / `--head` refs select diff mode). It
  deterministically checks tranche-manifest presence, schema validity, path
  coverage of an actual diff, and the recorded M2 gate and M6 notice
  disposition. It checks recorded provenance only; a manifest records that a
  gate was taken and grants nothing.

Production method: read the four authorized grounding sources, transcribe
membership statements with their citations, record disagreement as a conflict,
and stop at the M2 boundary. No step of this method writes to the instruction
surface.

## Governing Values and Decisions — Axiology

- **AX-001** — Grounding boundary (K-INVENT-1): every definition here derives
  only from the deliverable's register row, its `_CONTEXT.md`, the scope-ledger
  statements of `SOW-026`, and the adopted `docs/PRD_ROOT.md`. `_CONTEXT.md`
  records that the accepted decomposition states no per-deliverable acceptance
  criteria; the criteria above are therefore candidates, and no obligation was
  invented to fill that gap.
- **AX-002** — Human authority (K-AUTH-1): these candidates are reviewed by the
  human owner at the PR gate. No agent act in this contract confers acceptance,
  and no tool result substitutes for that judgment.
- **AX-003** — Conflict surfacing (K-CONFLICT-1): `CON-001` is recorded with
  pointers to both disagreeing sources instead of being silently resolved in
  favour of either enumeration.
- **AX-004** — Path discipline: this contract uses repo-relative paths only and
  embeds no machine-absolute path.
- **AX-005** — Ownership: `ResponsibleParty` remains `TBD` in the accepted
  register and is not assigned by this contract.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-026 OBJ-001 | CLM-001 CLM-002 REQ-001 CON-001 | AC-001 | VER-001 | Membership register with per-entry source citations, plus the recorded guard G2 output for the surface-ownership register at the time of check. |
| OUT-002 | SOW-026 OBJ-001 | CLM-001 REQ-002 | AC-002 | VER-002 | Change-path checklist, plus the recorded guard G4 output showing manifest presence, schema validity, and recorded gate disposition. |
| OUT-003 | SOW-026 OBJ-001 | CLM-001 REQ-002 | AC-003 | HUMAN_REVIEW: owner reading of the conformance notes against the stated read-mostly property in the covered scope-ledger statement | Conformance notes citing the stated property per observation, with divergences listed and unresolved ones marked. |
