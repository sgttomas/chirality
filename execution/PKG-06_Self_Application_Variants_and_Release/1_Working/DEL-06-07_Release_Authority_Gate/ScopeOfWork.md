---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-07
package_id: PKG-06
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-086, SOW-087]
package_objective_refs: [OBJ-004]
---

# Scope of Work — DEL-06-07

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-06-07` — Release
Authority Gate — in `PKG-06_Self_Application_Variants_and_Release`. It covers
project scope items SOW-086 and SOW-087 and supports package objective OBJ-004,
exactly as recorded in the deliverable register and in `_CONTEXT.md` §Scope
Traceability.

The deliverable's register description is: keep release a separately
human-gated lifecycle judgment over whether the current product state may be
released, informed by operative and developmental evidence, validation,
coverage, and guard state, and never performed mechanically or collapsed into
iteration.

OBJ-004 is stated in the adopted root PRD (`docs/PRD_ROOT.md` §3) as safe
self-application without self-authorization, with a v1 success condition
requiring falsifiers F1–F3 unobserved, every consumed root capability accepted
through the basis or an explicitly accepted predecessor, and guards G0–G4
registered and passing at every materialization. A release gate that could be
satisfied mechanically would be a self-authorization surface; keeping the
judgment human is how this deliverable serves OBJ-004.

This contract is authored in `MODE=INIT` from the accepted decomposition basis
bound in the frontmatter. Its acceptance criteria and verification methods are
**candidates for owner review**; they assert no acceptance, no reliance, no
release, and no lifecycle transition. Lifecycle state is held solely by
`_STATUS.md`, and `ResponsibleParty` remains `TBD` until a human assigns
ownership.

The register records `AnticipatedWriteLocus: execution-tree` for this
deliverable. That is a planning note, not authorization. Should any output
require touching the shared instruction surface (`AGENTS.md`, `agents/`,
`skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/`), that act
requires an independently authorized M2 instruction-surface tranche; this Scope
of Work grants none.

## Deliverable Definition — Ontology

The three outputs below are transcribed from the register field
`AnticipatedArtifacts` and from `_CONTEXT.md` §Anticipated Artifacts.

- **OUT-001** — Release gate definition: a record in the deliverable folder
  defining the gate as a separately human-gated lifecycle judgment over whether
  the current product state may be released, with its inputs enumerated and its
  performing act identified as an explicit owner act.
- **OUT-002** — Release-act record format: a stated record shape for one
  release act — what state was judged, which inputs were before the judge, the
  outcome, and the accountable human — such that a release act is
  reconstructible from files alone.
- **OUT-003** — Inputs-versus-judgment separation note: a record stating which
  artifacts are inputs to the gate and why none of them constitutes or performs
  the judgment, including the explicit distinction from the iteration decision.

- **CLM-001** — SOW-086 and SOW-087 both carry SourceRef `PRD §8.3
  [PROPOSED]` with `InOutStatus: IN`, and the ledger `Notes` record that the
  label is in effect per the D-GOV-22 adoption ruling, confirmed at the
  D-GOV-25 ruling, with the source label left unchanged under F6 discipline (no
  label change without an instrument). The gate defined here is therefore an
  adopted commitment of the root PRD.
- **CLM-002** — The adopted PRD distinguishes three human judgments that must
  not be collapsed — evaluation, iteration, and release — the third being a
  lifecycle gate drawing on both operative and developmental evidence
  (`docs/PRD_ROOT.md` §4.2, §8.3). OUT-003 exists because the collapse this
  deliverable guards against is a real and named failure mode, not a
  hypothetical one.
- **CLM-003** — `_CONTEXT.md` records `ContextEnvelope: M` with the note "One
  gate with enumerated inputs." The output set is one gate, one record format,
  and one separation note; enumerating the inputs is in scope, building or
  changing them is not.

## Completion and Reliance Basis — Epistemology

The requirements below restate the obligations carried by the covered scope
items, each cited to its ledger row and SourceRef.

- **REQ-001** — The gate definition shall record that release is a
  **separately human-gated lifecycle judgment** over whether the current
  product state may be released (SOW-086; PRD §8.3).
- **REQ-002** — The gate definition shall enumerate the gate's inputs — both
  operative and developmental evidence, plus validation results, decomposition
  coverage, and guard state — as inputs (SOW-086; PRD §8.3).
- **REQ-003** — The separation note shall record that none of the enumerated
  inputs releases the product mechanically and that none of them constitutes
  the judgment; release occurs only when the owner performs the applicable
  explicit release act (SOW-086; PRD §8.3).
- **REQ-004** — The separation note shall record that release is not an
  iteration decision: it asks whether what exists may go out, not whether the
  product should change (SOW-087; PRD §8.3).
- **REQ-005** — The release-act record format shall admit a negative outcome
  with no change proposed and a positive outcome with changes pending, neither
  being a decision to change the product (SOW-087; PRD §8.3).
- **REQ-006** — The release-act record format shall identify the accountable
  human and the exact product state judged, so that a release act is
  attributable and reconstructible from files alone (SOW-086; PRD §5.1 N-3).

- **AC-001** — The gate definition (OUT-001) states the separately human-gated
  lifecycle character of the release judgment and enumerates all five input
  classes named by SOW-086 — operative evidence, developmental evidence,
  validation results, decomposition coverage, and guard state.
- **AC-002** — The separation note (OUT-003) states, for each enumerated input
  class, that it informs and does not decide, and states the release/iteration
  distinction in the terms of SOW-087.
- **AC-003** — The release-act record format (OUT-002) admits all four
  outcome shapes implied by SOW-087 — negative with no change proposed,
  negative with changes proposed, positive with changes pending, positive with
  none — and requires the accountable human and the judged product state in
  every case.
- **AC-004** — No output performs, schedules, or asserts a release, and no
  output makes any tool or guard result sufficient for release.

## Production and Verification Method — Praxeology

Production reads the SOW-086 and SOW-087 ledger rows, the adopted PRD §4.2
(three judgments) and §8.3 (release authority), and the live guard registration
surface `execution/_harness/root_guards.yaml`. The enumerated inputs are named
from what exists at the recorded basis rather than invented.

Verification splits exactly the way the deliverable does. The **inputs** are
deterministically checkable; the **judgment** is not, and must never become so.

- **VER-001** — Confirm the guard-state input class is real and readable by
  running the guards registered in `execution/_harness/root_guards.yaml` —
  `python3 tools/validation/validate_root_harness_adapter.py` (G1),
  `python3 tools/validation/validate_root_surface_ownership.py` (G2),
  `python3 tools/validation/validate_root_work_graph_dispatch.py` (G3), and
  `python3 tools/validation/validate_instruction_tranche_manifest.py` (G4) —
  together with `python3 tools/validation/validate_root_materialization_fence.py`
  (G0), and confirm each input the gate definition enumerates resolves to such
  a surface. Deterministic; a pass evidences input availability only and is
  never release readiness.

No deterministic verification is defined for OUT-002 or OUT-003. Both are prose
records whose defect mode is *omitting an outcome shape or a required field, or
stating an input as deciding*, and no tool in this repository reads a record
format and rules on its adequacy. Validating this contract would not do so
either: `tools/scope_of_work/validate_scope_of_work.py` resolves this
deliverable's production format and reports `SOW_V1`, a result invariant to
whether either record has been written or admits the required outcomes. Those
two rows therefore carry named human review.

No verification method is defined for the release judgment itself. A tool that
could discharge it would contradict SOW-086 (K-AUTH-1; D-GOV-02 — a BLOCK is
bounded to its declared observation boundary and is never a global safety
verdict).

## Governing Values and Decisions — Axiology

- **AX-001** — Inputs inform; humans decide. Every deterministic result
  reaching this gate is a finding, and the gap between findings and the
  judgment is the deliverable's subject matter (SOW-086).
- **AX-002** — Passing is not readiness. Validation results, coverage, and
  guard state may all be green and the answer still be no; recording that
  possibility explicitly is what keeps the gate from decaying into a checklist.
- **AX-003** — Release is not iteration. Folding release into iteration would
  imply nothing can ship without changing something, and that a decision to
  change is a decision to ship; the separation note exists to prevent both
  readings (SOW-087).
- **AX-004** — Attributability outlives the act. A release record whose
  accountable human or judged state cannot be recovered from files leaves no
  release history, only an assertion (PRD §5.1 N-3).
- **AX-005** — Defining the gate performs no release. This deliverable
  produces the gate's description and record shape; it exercises no release
  authority and creates none.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-086 OBJ-004 | REQ-001 REQ-002 CLM-001 CLM-003 | AC-001 AC-004 | VER-001 | Gate definition in the deliverable folder plus the guard-validator output evidencing that each enumerated input class resolves to a real surface |
| OUT-002 | SOW-086 SOW-087 OBJ-004 | REQ-005 REQ-006 CLM-002 | AC-003 AC-004 | HUMAN_REVIEW: owner or delegate reads the release-act record format against the SOW-086 and SOW-087 ledger rows and PRD §8.3, and records that it admits all four outcome shapes named by AC-003, that it requires the accountable human and the exact product state judged in every case, and that no field makes a tool, guard, or coverage result sufficient for release | Release-act record format plus the recorded review note naming the reviewer, the ledger rows read, and the per-outcome-shape disposition |
| OUT-003 | SOW-086 SOW-087 OBJ-004 | REQ-003 REQ-004 CLM-002 | AC-002 AC-004 | HUMAN_REVIEW: owner or delegate reads the separation note against the SOW-086 and SOW-087 ledger rows and records that no input is stated as constituting the judgment | Separation note plus the recorded review note |
