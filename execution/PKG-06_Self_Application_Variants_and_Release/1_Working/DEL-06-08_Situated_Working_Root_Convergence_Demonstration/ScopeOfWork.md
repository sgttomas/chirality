---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-08
package_id: PKG-06
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-003]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-06-08

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-06-08` — Situated
Working Root Convergence Demonstration — in
`PKG-06_Self_Application_Variants_and_Release`. It covers project scope item
SOW-003 and supports package objective OBJ-005, exactly as recorded in the
deliverable register and in `_CONTEXT.md` §Scope Traceability.

The deliverable's register description is: demonstrate at least one situated
working root operating on the same instruction basis with a recorded
convergence path.

SOW-003 carries SourceRef `PRD §3 v1 boundary (c) [PROPOSED]` and
`DecisionRef: DEC-006`. In the adopted root PRD (`docs/PRD_ROOT.md` §3), v1
boundary clause (c) is one of the three conditions constituting Chirality Root
v1: at least one situated working root operates on the same instruction basis
with a recorded convergence path. This deliverable is the demonstration that
clause (c) holds.

The demonstration is a **demonstration**, not a survey: SOW-003 requires at
least one situated working root, and `_CONTEXT.md` bounds the envelope to "One
demonstration over one working root." Generalizing the result to every working
root is outside this scope.

This contract is authored in `MODE=INIT` from the accepted decomposition basis
bound in the frontmatter. Its acceptance criteria and verification methods are
**candidates for owner review**; they assert no acceptance, no reliance, and no
lifecycle transition. Lifecycle state is held solely by `_STATUS.md`, and
`ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register.

The register records `AnticipatedWriteLocus: execution-tree` for this
deliverable. That is a planning note, not authorization. The demonstration
observes the shared instruction surface (`AGENTS.md`, `agents/`, `skills/`,
`tools/`, root `docs/`, `init/`, `.github/workflows/`) and must not change it;
any such change requires an independently authorized M2 instruction-surface
tranche, which this Scope of Work does not grant.

## Deliverable Definition — Ontology

The two outputs below are transcribed from the register field
`AnticipatedArtifacts` and from `_CONTEXT.md` §Anticipated Artifacts.

- **OUT-001** — Convergence path record: a record in the deliverable folder
  naming the one demonstrated situated working root and tracing its convergence
  path — how it came to operate on the shared instruction basis, what it
  overlays or specializes locally, and how it takes up changes to the shared
  basis.
- **OUT-002** — Instruction-basis conformance evidence: the evidence that the
  named working root operates on the **same** instruction basis — the identity
  of the shared basis it resolves against, and the deterministic checks run
  against that basis with their results.

- **CLM-001** — The adopted PRD states that one instruction root serves many
  working roots — `projects/*`, `domains/*`, and desktop-harness user-selected
  folders — without per-workspace instruction drift; a working root may extend
  the invariant catalog and may overlay or specialize the agent suite, but
  **must not weaken** framework governance, and no variant inherits the
  D-GOV-21 root exception (`docs/PRD_ROOT.md` §7.1). "Same instruction basis"
  in SOW-003 is read against that clause: shared basis plus lawful overlay, not
  a copy.
- **CLM-002** — The ledger `Notes` for SOW-003 record that the `[PROPOSED]`
  label is in effect per the D-GOV-22 adoption ruling and confirmed at the
  D-GOV-25 ruling, the source label being left unchanged under F6 discipline
  (no label change without an instrument). The obligation demonstrated here is
  therefore an adopted commitment.
- **CLM-003** — The demonstration is evidence about the product's structure,
  not an acceptance of the demonstrated working root's own work. Whatever that
  working root produces remains governed by its own loop and instruments.

## Completion and Reliance Basis — Epistemology

The requirements below restate the obligation carried by the covered scope
item. SOW-003 (SourceRef: PRD §3 v1 boundary (c), `[PROPOSED]`, in effect per
D-GOV-22 and confirmed at D-GOV-25) requires at least one situated working root
operating on the same instruction basis with a recorded convergence path.

- **REQ-001** — The demonstration shall name exactly one situated working root
  that exists at the recorded basis, identified by its repo-relative path
  (SOW-003; `_CONTEXT.md` envelope note).
- **REQ-002** — The conformance evidence shall establish that the named
  working root resolves its instruction surface to the shared instruction root
  rather than to a divergent local copy (SOW-003; PRD §7.1).
- **REQ-003** — The convergence path record shall state what the named working
  root overlays or specializes locally and shall record that no overlay weakens
  framework governance and that the working root does not inherit the D-GOV-21
  root exception (PRD §7.1).
- **REQ-004** — The convergence path shall be **recorded**: the path by which
  the working root reached and maintains the shared basis shall be
  reconstructible from files in the checkout alone, without reliance on chat
  history or operator memory (SOW-003; PRD §5.1 N-1 and §3 OBJ-7).
- **REQ-005** — The conformance evidence shall be dated and bound to the
  instruction-basis state it was produced against, so a later reader can tell
  what was checked and when (SOW-003).
- **REQ-006** — No output shall claim that the demonstrated result generalizes
  to other working roots, and none shall assert acceptance of the demonstrated
  working root's own deliverables (SOW-003 scope; `_CONTEXT.md` envelope note).

- **AC-001** — The convergence path record (OUT-001) names one existing
  situated working root by repo-relative path and traces its convergence path
  end to end, including its local overlays and its non-weakening and
  non-inheritance statements.
- **AC-002** — The conformance evidence (OUT-002) shows the named working root
  resolving against the shared instruction root, with the deterministic checks
  run and their results recorded and dated against the checked basis state.
- **AC-003** — The convergence path is reconstructible from the checkout
  alone, and no claim of generalization beyond the one demonstrated working
  root appears in either output.

## Production and Verification Method — Praxeology

Production reads the SOW-003 ledger row and the adopted PRD §3 (v1 boundary
clause (c)) and §7.1 (downward service), then selects one existing situated
working root under `projects/` or `domains/` and records its convergence path
and conformance evidence. The selection is recorded with its reason; no working
root is created for this demonstration.

- **VER-001** — Run
  `python3 tools/validation/validate_instruction_entrypoints.py` and
  `python3 tools/validation/validate_agent_instructions.py` against the shared
  instruction root the named working root resolves to, requiring exit 0, and
  record the output as the conformance evidence's deterministic component. The
  first checks the root instruction entrypoints and the `CLAUDE.md` import
  contract; the second checks the mechanically observable `AGENT_*.md`
  contract. Deterministic.
- **VER-002** — Run
  `python3 tools/validation/validate_path_anchors.py` and require exit 0,
  evidencing that the live instruction and handoff surfaces the working root
  reads carry no machine-local home paths — the drift symptom a shared basis
  must not exhibit. Deterministic.
- **VER-003** — Where the named working root maintains its convergence through
  a recorded harness-contract pull, run
  `python3 tools/coordination/validate_harness_contract_pull.py` against that
  record and require it to pass, evidencing that the working root's take-up of
  the shared basis is bound to a commit rather than asserted. Deterministic,
  and applicable only to a working root that uses this mechanism; at the
  recorded basis the tool's consumption-record schema is
  `chirality.piping.harnessContractConsumption.v1`, so a working root using a
  different take-up mechanism is verified by the human-review row instead.

Validating this contract is not itself a verification of either output:
`tools/scope_of_work/validate_scope_of_work.py` resolves this deliverable's
production format and reports `SOW_V1`, a result invariant to whether the
demonstration record and its conformance evidence have been written at all.

Whether a recorded path is genuinely a *convergence* path — that the working
root converged onto the shared basis rather than drifting alongside it — is a
reading of the record and is verified by named human review in the matrix.

## Governing Values and Decisions — Axiology

- **AX-001** — One demonstration, honestly bounded. SOW-003 asks for at least
  one working root; the value of the deliverable lies in the demonstration
  being real and inspectable, not in its breadth.
- **AX-002** — Shared basis, lawful overlay. Specialization is expected and
  permitted; what the demonstration must show is that specialization did not
  become divergence and did not weaken framework governance (PRD §7.1).
- **AX-003** — The record is the demonstration. A convergence that happened but
  is not reconstructible from files did not, for purposes of reliance, happen
  (PRD §5.1 N-1).
- **AX-004** — Observation, not change. The demonstration reads the shared
  instruction surface and the working root; producing it must not modify
  either, and any instruction-surface effect belongs to a separately authorized
  tranche.
- **AX-005** — Evidence about structure, not acceptance of work. Demonstrating
  that a working root shares the basis says nothing about the quality or
  acceptance of what that working root produces.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-003 OBJ-005 | REQ-001 REQ-003 REQ-004 REQ-006 CLM-001 CLM-003 | AC-001 AC-003 | HUMAN_REVIEW: owner or delegate reads the convergence path record against the SOW-003 ledger row and confirms it traces convergence onto the shared basis rather than parallel drift | Convergence path record naming one working root, plus the recorded review note |
| OUT-002 | SOW-003 OBJ-005 | REQ-002 REQ-005 CLM-001 CLM-002 | AC-002 | VER-001 VER-002 VER-003 | Conformance evidence with verbatim validator output for each check, dated and bound to the instruction-basis state checked |
