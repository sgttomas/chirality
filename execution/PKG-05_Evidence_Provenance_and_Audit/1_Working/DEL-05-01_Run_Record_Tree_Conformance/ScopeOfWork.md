---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-01
package_id: PKG-05
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-052]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-05-01

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-05-01`
(Run Record Tree Conformance) in service of project scope reference SOW-052
and package objective reference OBJ-006.

DEL-05-01 is a `REQ_SLICE` in `PKG-05` (Evidence, Provenance, and Audit). Its
work is to keep every orchestration run persisting a durable, versioned record
tree, and to make the absence of such a tree — or the presence of a fabricated
one — visible. It does not build orchestration machinery and does not rule on
any run.

Every definition below is grounded only in the deliverable register row for
DEL-05-01, its `_CONTEXT.md`, the scope-ledger statement for SOW-052, and the
adopted `docs/PRD_ROOT.md`. Nothing else is imported (K-INVENT-1). All
acceptance and verification definitions in this contract are **candidate**:
they claim no acceptance, no lifecycle transition, and no owner ruling.

## Deliverable Definition — Ontology

The anticipated artifacts recorded in `_CONTEXT.md ## Anticipated Artifacts`
and in the register `AnticipatedArtifacts` field are three, and they are the
three outputs of this deliverable.

- **OUT-001** — Run-record structure checklist: the enumerated element-by-element
  structure that an orchestration run's durable, versioned record tree must
  carry, each element bound to its scope-ledger and PRD source.
- **OUT-002** — Placeholder-run prohibition check: the check that distinguishes a
  run ID created because a real run began from a run ID, run directory, or
  brief presented as an executed child when no run executed.
- **OUT-003** — Handoff-state conformance notes: notes recording, per run record
  in the observed population, whether a final handoff state is present and what
  it names.

- **CLM-001** — Population and boundary. `docs/PRD_ROOT.md` §3 OBJ-6 fixes the
  observation population for this objective as root-product development runs —
  the run records under this loop's `execution/_Coordination/`. Situated working
  roots' coordination is out of scope, and any aggregated cross-root layer would
  be a new product function. DEL-05-01 inherits that boundary; its outputs
  describe root-product run records only.
- **CLM-002** — Decomposition identity. The register records DEL-05-01 as
  `Type: REQ_SLICE`, `ContextEnvelope: M` ("One record shape over an existing
  directory convention"), `AnticipatedWriteLocus: execution-tree`, and
  `ResponsibleParty: TBD`. `ResponsibleParty` is preserved as `TBD` here and is
  not assigned by this contract.
- **CLM-003** — Named locus. `docs/PRD_ROOT.md` §5.4 E-1 [TRANSCRIBED] names the
  record tree's locus as `_Coordination/AgentRuns/<RunID>/`. The scope-ledger
  statement for SOW-052 restates E-1 without the locus; this contract carries
  the locus from the PRD, which is the governing product statement the ledger
  item traces to.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The run-record structure shall enumerate the eight record-tree
  elements named by SOW-052 — plan, work graph, briefs, returns, notices,
  dispositions, amendments, and final handoff state — as a durable, versioned
  tree per run. Source: SOW-052 (SourceRef `PRD §5.4 E-1 [TRANSCRIBED]`).
- **REQ-002** — The prohibition check shall hold that a run ID is created only
  when a real run begins, and that placeholder runs and briefs presented as
  executed children are prohibited. Source: SOW-052 (SourceRef
  `PRD §5.4 E-1 [TRANSCRIBED]`).
- **REQ-003** — The handoff-state notes shall treat the final handoff state as a
  required element of the record tree rather than an optional closing remark,
  and shall record its presence or absence per run record. Source: SOW-052
  (SourceRef `PRD §5.4 E-1 [TRANSCRIBED]`), read with OBJ-006's condition that
  no run's effect is discoverable only from chat history.

- **AC-001** — OUT-001 enumerates all eight SOW-052 record-tree elements, states
  the `_Coordination/AgentRuns/<RunID>/` locus from `docs/PRD_ROOT.md` §5.4 E-1,
  and states the durability and versioning properties for each element.
- **AC-002** — Every OUT-001 checklist item is traceable within this contract to
  SOW-052 and OBJ-006 through declared references that resolve under the
  production-contract grammar, with no unresolved or orphaned reference.
- **AC-003** — OUT-002 states both prohibitions of SOW-052 as separately
  checkable conditions — run-ID creation timing, and briefs or directories
  presented as executed children — and names, for each, the recorded evidence a
  reviewer inspects to reach a finding.
- **AC-004** — OUT-003 reports, for each run record in the CLM-001 population, a
  present/absent finding on the final handoff state and, where present, what the
  handoff state names; unexamined records are reported as unexamined rather than
  omitted.

## Production and Verification Method — Praxeology

Production is document work under the deliverable folder. Outputs are drafted
from the four grounding sources, cross-checked against SOW-052 and
`docs/PRD_ROOT.md` §5.4 E-1 and §3 OBJ-6, and left in `OPEN` source state.

- **VER-001** — Production-contract conformance. From the repository root run
  `python3 tools/scope_of_work/validate_scope_of_work.py execution/PKG-05_Evidence_Provenance_and_Audit/1_Working/DEL-05-01_Run_Record_Tree_Conformance`;
  the method passes when it exits 0 and prints a `PASS format=SOW_V1` line. This
  verifies that every output, criterion, and objective reference in this contract
  is declared, resolved, and bound in the matrix. It does not verify the
  substantive content of any output.
- **VER-002** — Work-graph element guard. From the repository root run
  `python3 tools/validation/validate_root_work_graph_dispatch.py`; the method
  passes when it exits 0 against `execution/_harness/work_graph.yaml`. This is
  the D-GOV-21 G3 guard wired into `.github/workflows/governance-harness.yml`;
  it evidences that the work-graph element of the record tree carries declared
  write targets that are disjoint or serialized. It covers the work-graph element
  only and evidences nothing about the other seven elements.

- **CLM-004** — Instruction-surface fence. The register and `_CONTEXT.md` record
  `AnticipatedWriteLocus: execution-tree`. Should any act under this deliverable
  need to touch the instruction surface (`AGENTS.md`, `agents/`, `skills/`,
  `tools/`, root `docs/`, `init/`, `.github/workflows/`), that act requires an
  independently authorized M2 tranche. **This Scope of Work grants no such
  authorization.** The verification commands named in VER-001 and VER-002 are
  read-only invocations of existing tools and are not writes to that surface.

Where no deterministic surface exists at this basis, the matrix records
`HUMAN_REVIEW: <named method>` rather than naming a command that does not exist.

## Governing Values and Decisions — Axiology

- **AX-001** — No invention. Only the deliverable register row, `_CONTEXT.md`,
  the SOW-052 scope-ledger statement, and `docs/PRD_ROOT.md` ground content here
  (K-INVENT-1). `_CONTEXT.md ## Acceptance Criteria` records that the accepted
  decomposition states no per-deliverable acceptance criteria; the criteria above
  are therefore candidate definitions authored under this contract, not
  transcriptions of accepted criteria.
- **AX-002** — Deterministic checks are not judgment. VER-001 and VER-002 are
  hygiene and precondition gates. Neither makes an acceptance judgment, and a
  passing gate is not an owner ruling.
- **AX-003** — Legibility over volume. OBJ-006 asks that concurrency stay
  intelligible; the outputs are sized to let a reviewer reconstruct declared
  write ownership, dependencies, and pending gates from recorded state, not to
  maximize record volume.
- **AX-004** — Lifecycle neutrality. This contract makes no lifecycle transition
  and asserts no approval. Lifecycle state remains `OPEN` and is read from
  `_STATUS.md`, which this contract does not modify.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-052 OBJ-006 | REQ-001 CLM-003 | AC-001 AC-002 | VER-001 VER-002 | Checklist document enumerating the eight elements with the named locus; validator output line; G3 guard exit status |
| OUT-002 | SOW-052 OBJ-006 | REQ-002 CLM-001 | AC-003 | HUMAN_REVIEW: two-condition read-back of the prohibition check against the SOW-052 ledger statement and `docs/PRD_ROOT.md` §5.4 E-1 | Prohibition-check document with per-condition evidence pointers and the reviewer's recorded finding |
| OUT-003 | SOW-052 OBJ-006 | REQ-003 CLM-002 | AC-004 | HUMAN_REVIEW: per-run-record presence audit of the final handoff state across the CLM-001 population | Handoff-state notes listing each examined run record, its present/absent finding, and any unexamined record |
