---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-02
package_id: PKG-05
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-021, SOW-053]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-02

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-05-02`
(Snapshot, Handoff, and Receipt Discipline) in service of project scope
references SOW-021 and SOW-053 and package objective reference OBJ-003.

DEL-05-02 is a `REQ_SLICE` in `PKG-05` (Evidence, Provenance, and Audit). It
covers three related conventions that together make an accepted change
retrievable from files alone: phase-boundary decisions terminating in immutable
snapshots, stopping work emitting an explicit handoff state, and each lawful
tranche appending a minimal receipt — plus the write-containment corollary that
task outputs to tool roots are immutable snapshots.

Every definition below is grounded only in the deliverable register row for
DEL-05-02, its `_CONTEXT.md`, the scope-ledger statements for SOW-021 and
SOW-053, and the adopted `docs/PRD_ROOT.md`. Nothing else is imported
(K-INVENT-1). All acceptance and verification definitions are **candidate**:
they claim no acceptance, no lifecycle transition, and no owner ruling.

## Deliverable Definition — Ontology

The anticipated artifacts recorded in `_CONTEXT.md ## Anticipated Artifacts`
and in the register `AnticipatedArtifacts` field are three, and they are the
three outputs of this deliverable.

- **OUT-001** — Snapshot immutability check: the check that a phase-boundary
  snapshot, once written, is not later edited in place, and that a task output
  written to a tool root is a snapshot rather than mutable working state.
- **OUT-002** — Handoff-state template conformance: the conformance statement for
  the explicit handoff state that stopping work must emit, expressed as a fixed
  set of fields a reader can look for.
- **OUT-003** — Receipts append-only evidence: the evidence that each lawful
  tranche appended a minimal receipt and that prior receipts were not rewritten.

- **CLM-001** — Objective condition. `docs/PRD_ROOT.md` §3 OBJ-3 states two
  conditions: structural completeness, which is universal — every accepted change
  has a retrievable linkage from files alone between the evidence that informed
  it, the ruling that accepted it, and the state it changed — and retrieval
  usability, which is sampled against a time threshold and a tranche sample fixed
  and recorded before the evaluation runs. The three conventions in this
  deliverable serve the universal condition; measuring the sampled condition is
  not this deliverable's work.
- **CLM-002** — Decomposition identity. The register records DEL-05-02 as
  `Type: REQ_SLICE`, `ContextEnvelope: M` ("Three related conventions with
  existing surfaces"), `AnticipatedWriteLocus: execution-tree`, and
  `ResponsibleParty: TBD`. `ResponsibleParty` is preserved as `TBD` here and is
  not assigned by this contract.
- **CLM-003** — Two ledger items, one deliverable. SOW-053 supplies the three
  phase-boundary conventions and traces to `docs/PRD_ROOT.md` §5.4 E-2
  [TRANSCRIBED]. SOW-021 supplies the tool-root corollary and traces to
  `docs/PRD_ROOT.md` §5.1 N-5 [TRANSCRIBED], where write containment is
  architectural: every agent has an explicit declared write scope, every scope
  path and write target resolves under the active checkout or the task stops, and
  task outputs to tool roots are immutable snapshots.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The snapshot check shall hold that a phase-boundary decision
  terminates in an immutable snapshot: the snapshot is written once and is not
  edited in place thereafter. Source: SOW-053 (SourceRef
  `PRD §5.4 E-2 [TRANSCRIBED]`).
- **REQ-002** — The snapshot check shall extend the same immutability property to
  task outputs written to tool roots. Source: SOW-021 (SourceRef
  `PRD §5.1 N-5 [TRANSCRIBED]`).
- **REQ-003** — The handoff-state conformance statement shall hold that work which
  stops emits an explicit handoff state, and shall express that state as a named,
  enumerable field set rather than as free narrative. Source: SOW-053 (SourceRef
  `PRD §5.4 E-2 [TRANSCRIBED]`).
- **REQ-004** — The receipts evidence shall hold that each lawful tranche appends a
  minimal receipt, and that appending is the only lawful mutation of the receipt
  surface. Source: SOW-053 (SourceRef `PRD §5.4 E-2 [TRANSCRIBED]`).

- **AC-001** — OUT-001 states the immutability property for both loci covered here
  — phase-boundary snapshots per SOW-053 and tool-root task outputs per SOW-021 —
  and names, for each, the recorded evidence a reviewer inspects.
- **AC-002** — OUT-001 defines the probe it relies on in terms a second party can
  rerun unchanged, naming the snapshot path and the accepted upstream commit the
  probe compares against.
- **AC-003** — OUT-002 enumerates the handoff-state fields as a closed list, and
  each field is traceable to SOW-053 or to `docs/PRD_ROOT.md` §5.4 E-2; no field
  is introduced without such a trace.
- **AC-004** — OUT-003 reports, for the receipt surface it examines, that every
  change since the named accepted upstream commit is an addition, and reports any
  deletion or in-place edit as a finding rather than omitting it.

## Production and Verification Method — Praxeology

Production is document work under the deliverable folder. Outputs are drafted
from the four grounding sources, cross-checked against SOW-021, SOW-053, and
`docs/PRD_ROOT.md` §5.4 E-2, §5.1 N-5, and §3 OBJ-3, and left in `OPEN` source
state.

- **VER-001** — Production-contract conformance. From the repository root run
  `python3 tools/scope_of_work/validate_scope_of_work.py execution/PKG-05_Evidence_Provenance_and_Audit/1_Working/DEL-05-02_Snapshot_Handoff_and_Receipt_Discipline`;
  the method passes when it exits 0 and prints a `PASS format=SOW_V1` line. This
  verifies that every output, criterion, and objective reference in this contract
  is declared, resolved, and bound in the matrix. It does not verify the
  substantive content of any output.
- **VER-002** — Snapshot immutability probe. For each snapshot path the check
  names, run `git log --oneline -- <snapshot-path>` and
  `git diff --name-only <accepted-upstream-commit>..HEAD -- <snapshot-path>`. The
  method passes when the log shows the introducing commit and the diff is empty,
  evidencing that the snapshot was not edited after it was written. It uses git
  only and requires no repository tool. It evidences in-place mutation or its
  absence; it makes no judgment about whether the snapshot's content is correct.
- **VER-003** — Receipt append-only probe. Run
  `git diff --unified=0 <accepted-upstream-commit>..HEAD -- <receipt-surface-path>`.
  The method passes when the diff contains only added lines and no removed or
  modified line. It evidences append-only mutation of the receipt surface; it
  makes no judgment about whether a receipt's prose is reconstructible or true.

- **CLM-004** — Instruction-surface fence. The register and `_CONTEXT.md` record
  `AnticipatedWriteLocus: execution-tree`. Should any act under this deliverable
  need to touch the instruction surface (`AGENTS.md`, `agents/`, `skills/`,
  `tools/`, root `docs/`, `init/`, `.github/workflows/`), that act requires an
  independently authorized M2 tranche. **This Scope of Work grants no such
  authorization.** The methods in VER-001 through VER-003 are read-only
  invocations and are not writes to that surface.

Where no deterministic surface exists at this basis, the matrix records
`HUMAN_REVIEW: <named method>` rather than naming a command that does not exist.

## Governing Values and Decisions — Axiology

- **AX-001** — No invention. Only the deliverable register row, `_CONTEXT.md`, the
  SOW-021 and SOW-053 scope-ledger statements, and `docs/PRD_ROOT.md` ground
  content here (K-INVENT-1). `_CONTEXT.md ## Acceptance Criteria` records that the
  accepted decomposition states no per-deliverable acceptance criteria; the
  criteria above are therefore candidate definitions authored under this contract.
- **AX-002** — Immutability is recorded, not asserted. A snapshot is immutable
  because the record shows it was not changed, not because a document says it is.
  VER-002 and VER-003 are the recorded form of that distinction.
- **AX-003** — Completeness is structural. Under CLM-001, a missing linkage is a
  defect regardless of sampling; these conventions exist so the universal
  condition can be met from files alone, without recourse to chat history.
- **AX-004** — Deterministic checks are not judgment. VER-001 through VER-003 are
  hygiene and precondition gates. None makes an acceptance judgment, and a passing
  gate is not an owner ruling.
- **AX-005** — Lifecycle neutrality. This contract makes no lifecycle transition
  and asserts no approval. Lifecycle state remains `OPEN` and is read from
  `_STATUS.md`, which this contract does not modify.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-021 SOW-053 OBJ-003 | REQ-001 REQ-002 CLM-003 | AC-001 AC-002 | VER-001 VER-002 | Immutability-check document naming each snapshot path and accepted upstream commit; validator output line; git log and diff output per path |
| OUT-002 | SOW-053 OBJ-003 | REQ-003 CLM-001 | AC-003 | HUMAN_REVIEW: field-by-field read-back of the handoff-state field list against the SOW-053 ledger statement and `docs/PRD_ROOT.md` §5.4 E-2 | Handoff-state conformance statement with a closed field list and a per-field source trace |
| OUT-003 | SOW-053 OBJ-003 | REQ-004 CLM-002 | AC-004 | VER-003 | Append-only evidence naming the receipt surface and accepted upstream commit, with the diff output and any deletion reported as a finding |
