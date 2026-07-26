---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-02
package_id: PKG-02
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-027, SOW-035]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-02-02

## Purpose and Objective Traceability

This contract defines the production scope of `DEL-02-02` — Three-Layer
Authority Boundary Conformance — in service of project scope items `SOW-027` and
`SOW-035` and package objective `OBJ-002`, as recorded in the accepted root
decomposition and its companion deliverable register.

The accepted register states the deliverable's purpose as keeping the operative
product bounded to instruction artifacts, deterministic tools, and the runtime
substrate, with no fourth execution substrate claimed and no layer holding or
granting project authority. Its register `Type` is `REQ_SLICE`: the work slices
an existing stated requirement into checkable form and implies no implementation
change.

**Claim status.** Every `OUT-*`, `CLM-*`, `REQ-*`, `AC-*`, `VER-*`, and `AX-*`
definition below is a *candidate* authored under `MODE=INIT` from the four
authorized grounding sources named in the Axiology section. Nothing here claims
acceptance, review outcome, or lifecycle state.

**Write-locus gate.** The register records this deliverable's
`AnticipatedWriteLocus` as `execution-tree; instruction-surface (M2) if a layer
statement must change`. That is a planning note, not authorization. If the work
concludes that a layer statement must change, that change touches `AGENTS.md`,
`agents/`, `skills/`, `tools/`, root `docs/`, or `init/` and therefore requires
an independently authorized M2 tranche. **This Scope of Work grants no such
authorization.** Under `SOW-035` this is not an incidental restriction: an
instruction-surface change is a governance act rather than a code change.

## Deliverable Definition — Ontology

The anticipated artifacts are transcribed from the register's
`AnticipatedArtifacts` field and the deliverable's `_CONTEXT.md`.

- **OUT-001** — Layer boundary register: an enumeration of the three operative
  layers with, per layer, its stated authority boundary and the accepted
  statement that establishes it.
- **OUT-002** — Runtime transport/authority separation notes: notes recording
  how the runtime substrate's execution and transport role is held separate from
  project authority, and how its user-data state is treated as operational
  rather than project truth.
- **OUT-003** — Fourth-substrate guard note: a note stating the closed boundary
  — that the operative product is exactly the three layers — and the check by
  which a claimed fourth machine execution substrate would be recognized.

The register records `ContextEnvelope: M` with the note "Three bounded layers
with one authority rule; no implementation change implied", which bounds these
outputs to the three layers and the single authority rule.

## Completion and Reliance Basis — Epistemology

- **CLM-001** — Covered scope item `SOW-027` (SourceRef: PRD §5.2 O-2
  [TRANSCRIBED]) states that the product operates through three layers with
  distinct authority boundaries: instruction artifacts carrying semantic
  authority contracts; deterministic tools producing facts and findings and
  never substituting for semantic judgment; and the runtime executable substrate
  whose transport never grants project authority and whose user-data state is
  operational rather than project truth.
- **CLM-002** — Covered scope item `SOW-035` (SourceRef: PRD §5.2 O-10
  [CLARIFIED]) states that the operative product's boundary is exactly those
  three layers, that no fourth machine execution substrate is claimed, and that
  none of the layers holds or grants project authority — which is why an
  instruction-surface change is a governance act rather than a code change.
- **CLM-003** — `SOW-035` carries the label `CLARIFIED` rather than
  `TRANSCRIBED`: it is recorded as an interpretation of the transcribed items,
  not as an independently transcribed statement. Work under this contract
  preserves that distinction and does not upgrade it.
- **REQ-001** — The layer boundary register shall enumerate exactly the three
  layers of `CLM-001` and shall state, per layer, the authority boundary that
  the covered scope statements assign to it.
- **REQ-002** — The separation notes shall record the runtime substrate's
  transport role as conferring no project authority and its user-data state as
  operational rather than project truth, per `CLM-001`.
- **REQ-003** — The guard note shall state the closed three-layer boundary of
  `CLM-002` and shall not introduce, name, or imply a fourth machine execution
  substrate.
- **AC-001** — The layer boundary register enumerates exactly three layers,
  assigns each an authority boundary traceable to `SOW-027` or `SOW-035`, and
  introduces no layer beyond those three.
- **AC-002** — The separation notes state, for the runtime substrate, both that
  transport grants no project authority and that its user-data state is
  operational rather than project truth, each with its source citation.
- **AC-003** — The guard note states the closed boundary and records that no
  layer holds or grants project authority, and the deliverable's outputs contain
  no claim of a fourth execution substrate.

## Production and Verification Method — Praxeology

This deliverable's own subject matter constrains its verification design:
`CLM-001` states that deterministic tools produce facts and findings and never
substitute for semantic judgment. Layer-boundary conformance is therefore
verified by human reading, and deterministic checks are used only where a
genuine mechanical surface exists. No invented command appears below.

- **VER-001** — Run `python3 tools/validation/validate_root_surface_ownership.py`
  (guard G2, no arguments; reads `execution/_harness/surface_ownership.yaml`).
  It deterministically checks the static root surface-ownership register,
  including declared write targets and each entry's `instruction_surface` flag.
  It bears on this deliverable only through the conditional write locus: it is
  evidence about whether a write target is declared as intersecting the
  instruction surface, and therefore whether M2 applies. It does not decide any
  layer boundary.

Production method: read the covered scope-ledger statements and the adopted PRD
items they cite, transcribe each layer with its authority boundary, and record
the closed boundary. The method writes only within the execution tree; it stops
at the M2 boundary if a layer statement is found to need change.

## Governing Values and Decisions — Axiology

- **AX-001** — Grounding boundary (K-INVENT-1): every definition here derives
  only from the deliverable's register row, its `_CONTEXT.md`, the scope-ledger
  statements of `SOW-027` and `SOW-035`, and the adopted `docs/PRD_ROOT.md`.
  `_CONTEXT.md` records that the accepted decomposition states no
  per-deliverable acceptance criteria; the criteria above are candidates.
- **AX-002** — Tools do not judge (`CLM-001`): a passing deterministic check is
  evidence, never a conformance ruling. This is why most acceptance here routes
  to human review rather than to a command.
- **AX-003** — Human authority (K-AUTH-1): these candidates are reviewed by the
  human owner at the PR gate; no agent act confers acceptance.
- **AX-004** — Label discipline (K-CLAIM-1): the `CLARIFIED` provenance of
  `SOW-035` is carried forward as recorded and is not restated as transcription.
- **AX-005** — Path discipline: this contract uses repo-relative paths only and
  embeds no machine-absolute path. `ResponsibleParty` remains `TBD`.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-027 SOW-035 OBJ-002 | CLM-001 CLM-002 REQ-001 | AC-001 | HUMAN_REVIEW: owner reading of the layer boundary register against the covered scope-ledger statements | Layer register listing three layers with per-layer authority boundary and source citation. |
| OUT-002 | SOW-027 OBJ-002 | CLM-001 REQ-002 | AC-002 | VER-001 | Separation notes citing the transport and user-data clauses, plus the recorded guard G2 output for declared write targets at the time of check. |
| OUT-003 | SOW-035 OBJ-002 | CLM-002 CLM-003 REQ-003 | AC-003 | HUMAN_REVIEW: owner reading of the guard note against the closed-boundary statement, confirming its CLARIFIED provenance is preserved | Guard note stating the closed three-layer boundary and the no-authority rule, with the recognition check for a claimed fourth substrate. |
