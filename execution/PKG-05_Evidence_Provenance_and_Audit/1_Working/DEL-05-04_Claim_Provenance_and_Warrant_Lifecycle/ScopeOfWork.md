---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-04
package_id: PKG-05
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-055, SOW-059]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-04

## Purpose and Objective Traceability

This Scope of Work defines the production contract for `DEL-05-04`
(Claim Provenance and Warrant Lifecycle) in service of project scope references
SOW-055 and SOW-059 and package objective reference OBJ-003.

DEL-05-04 is a `REQ_SLICE` in `PKG-05` (Evidence, Provenance, and Audit). Its
work is one lifecycle over a stable vocabulary: claims carry epistemic labels
and progress through the warrant lifecycle; authentication is a bounded act by
an accountable actor; and evidence completeness is never read as evidence
sufficiency.

Every definition below is grounded only in the deliverable register row for
DEL-05-04, its `_CONTEXT.md`, the scope-ledger statements for SOW-055 and
SOW-059, and the adopted `docs/PRD_ROOT.md`. Nothing else is imported
(K-INVENT-1). All acceptance and verification definitions are **candidate**:
they claim no acceptance, no lifecycle transition, and no owner ruling.

## Deliverable Definition — Ontology

The anticipated artifacts recorded in `_CONTEXT.md ## Anticipated Artifacts`
and in the register `AnticipatedArtifacts` field are three, and they are the
three outputs of this deliverable.

- **OUT-001** — Warrant lifecycle conformance notes: notes recording, for the
  claims examined, where each sits on the warrant lifecycle and whether its
  recorded position is supported by the recorded evidence.
- **OUT-002** — Label taxonomy check: the check that every epistemic label in use
  is drawn from the closed vocabulary and that no out-of-vocabulary label is
  circulating.
- **OUT-003** — Completeness-versus-sufficiency guidance: the guidance that keeps a
  provenance-ladder reading from being restated as a reliance judgment.

- **CLM-001** — The lifecycle and the vocabulary. `docs/PRD_ROOT.md` §5.4 E-4
  [TRANSCRIBED] states that claims carry epistemic labels and progress through the
  warrant lifecycle `UNWARRANTED → CITED → REVIEWED → AUTHENTICATED`, and that
  authentication is an accountable actor's scoped, purpose-specific, SHA-bound act
  that neither creates knowledge nor establishes truth. The scope-ledger statement
  for SOW-055 restates the same. Those four values are the closed vocabulary
  OUT-002 checks against; this contract introduces no fifth value.
- **CLM-002** — The completeness boundary. `docs/PRD_ROOT.md` §5.4 E-8 is labelled
  **CLARIFIED**, not TRANSCRIBED, and states that evidence completeness is not
  evidence sufficiency: the provenance ladder measures whether warrant is present,
  never whether it is adequate for a given reliance purpose, and adequacy is a
  human judgment against scope and purpose. SOW-059 carries the same statement
  with SourceRef `PRD §5.4 E-8 [CLARIFIED]`. OUT-003 must preserve that label
  rather than presenting E-8 as transcribed.
- **CLM-003** — Decomposition identity. The register records DEL-05-04 as
  `Type: REQ_SLICE`, `ContextEnvelope: M` ("One lifecycle over a stable
  vocabulary"), `AnticipatedWriteLocus: execution-tree`, and
  `ResponsibleParty: TBD`. `ResponsibleParty` is preserved as `TBD` here and is
  not assigned by this contract.
- **CLM-004** — Objective linkage. `docs/PRD_ROOT.md` §3 OBJ-3 makes structural
  completeness universal — every accepted change carries a retrievable linkage
  from files alone between evidence, ruling, and changed state — while retrieval
  usability is sampled. A claim's recorded label is part of that linkage; an
  unlabelled or mislabelled claim is a completeness defect regardless of sampling.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The conformance notes shall record each examined claim's position
  on the lifecycle `UNWARRANTED → CITED → REVIEWED → AUTHENTICATED` and the
  recorded evidence supporting that position. Source: SOW-055 (SourceRef
  `PRD §5.4 E-4 [TRANSCRIBED]`).
- **REQ-002** — The conformance notes shall treat authentication as a scoped,
  purpose-specific, SHA-bound act by an accountable actor, and shall not represent
  it as creating knowledge or establishing truth. Source: SOW-055 (SourceRef
  `PRD §5.4 E-4 [TRANSCRIBED]`).
- **REQ-003** — The label taxonomy check shall treat the four lifecycle values as a
  closed vocabulary and shall report any label outside it as a finding. Source:
  SOW-055 (SourceRef `PRD §5.4 E-4 [TRANSCRIBED]`).
- **REQ-004** — The guidance shall hold that a provenance-ladder reading reports
  whether warrant is present and never whether it is adequate for a reliance
  purpose, and shall attribute the adequacy judgment to a human against scope and
  purpose. Source: SOW-059 (SourceRef `PRD §5.4 E-8 [CLARIFIED]`).

- **AC-001** — OUT-001 gives, per examined claim, its lifecycle position, the
  recorded evidence for that position, and — where the position is
  `AUTHENTICATED` — the actor, the scope, the purpose, and the SHA the act was
  bound to; any element not recorded is reported as not recorded.
- **AC-002** — OUT-002 states the four-value vocabulary exactly as SOW-055 states
  it, with no added, renamed, or dropped value.
- **AC-003** — OUT-002 reports every label occurrence it examined and lists each
  out-of-vocabulary occurrence with its location, rather than reporting only a
  pass or fail summary.
- **AC-004** — OUT-003 states the completeness-versus-sufficiency boundary, carries
  the `CLARIFIED` label of `docs/PRD_ROOT.md` §5.4 E-8 explicitly, and contains no
  statement that a complete provenance record is by itself sufficient for any
  reliance purpose.

## Production and Verification Method — Praxeology

Production is document work under the deliverable folder. Outputs are drafted
from the four grounding sources, cross-checked against SOW-055, SOW-059, and
`docs/PRD_ROOT.md` §5.4 E-4, §5.4 E-8, and §3 OBJ-3, and left in `OPEN` source
state.

- **VER-001** — Production-contract conformance. From the repository root run
  `python3 tools/scope_of_work/validate_scope_of_work.py execution/PKG-05_Evidence_Provenance_and_Audit/1_Working/DEL-05-04_Claim_Provenance_and_Warrant_Lifecycle`;
  the method passes when it exits 0 and prints a `PASS format=SOW_V1` line. This
  verifies that every output, criterion, and objective reference in this contract
  is declared, resolved, and bound in the matrix. It does not verify the
  substantive content of any output.
- **VER-002** — Closed-vocabulary probe. Over the labelled surface the check
  examines, run
  `grep -nE '\b(UNWARRANTED|CITED|REVIEWED|AUTHENTICATED)\b' <labelled-surface>`
  to enumerate conforming label occurrences, and the corresponding inverse
  selection over the same label positions to enumerate the rest. The method passes
  when the inverse selection is empty. It uses `grep` only and requires no
  repository tool. It evidences vocabulary membership; it makes no judgment about
  whether a given claim's label is the correct one.

- **CLM-005** — Instruction-surface fence. The register and `_CONTEXT.md` record
  `AnticipatedWriteLocus: execution-tree`. Should any act under this deliverable
  need to touch the instruction surface (`AGENTS.md`, `agents/`, `skills/`,
  `tools/`, root `docs/`, `init/`, `.github/workflows/`), that act requires an
  independently authorized M2 tranche. **This Scope of Work grants no such
  authorization.** The methods in VER-001 and VER-002 are read-only invocations
  and are not writes to that surface.

Where no deterministic surface exists at this basis, the matrix records
`HUMAN_REVIEW: <named method>` rather than naming a command that does not exist.
Whether a claim's recorded label is the *right* label is not machine-decidable
here and is left to named human review.

## Governing Values and Decisions — Axiology

- **AX-001** — No invention. Only the deliverable register row, `_CONTEXT.md`, the
  SOW-055 and SOW-059 scope-ledger statements, and `docs/PRD_ROOT.md` ground
  content here (K-INVENT-1). `_CONTEXT.md ## Acceptance Criteria` records that the
  accepted decomposition states no per-deliverable acceptance criteria; the
  criteria above are therefore candidate definitions authored under this contract.
- **AX-002** — Authentication is bounded. Under SOW-055 it is scoped,
  purpose-specific, SHA-bound, and attributable to an accountable actor. It
  neither creates knowledge nor establishes truth, and no output here may present
  it as doing either.
- **AX-003** — Completeness is not sufficiency. Under SOW-059 the ladder measures
  presence of warrant only. Reporting a complete record as adequate for a reliance
  purpose is the specific error this deliverable exists to prevent.
- **AX-004** — Labels are load-bearing, so they stay closed. A vocabulary that
  grows informally destroys the comparability that makes the lifecycle readable;
  new values require an authorized act, not local usage.
- **AX-005** — Deterministic checks are not judgment. VER-001 and VER-002 are
  hygiene and precondition gates. Neither makes an acceptance judgment, and a
  passing gate is not an owner ruling.
- **AX-006** — Lifecycle neutrality. This contract makes no lifecycle transition
  and asserts no approval. Deliverable lifecycle state remains `OPEN` and is read
  from `_STATUS.md`, which this contract does not modify; the warrant lifecycle
  discussed above is a property of claims, not of this deliverable.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-055 OBJ-003 | REQ-001 REQ-002 CLM-001 | AC-001 | HUMAN_REVIEW: per-claim read-back of lifecycle position and supporting evidence against the SOW-055 ledger statement and `docs/PRD_ROOT.md` §5.4 E-4 | Conformance notes listing each examined claim, its lifecycle position, its supporting evidence, and the authentication elements recorded or missing |
| OUT-002 | SOW-055 OBJ-003 | REQ-003 CLM-004 | AC-002 AC-003 | VER-001 VER-002 | Taxonomy check stating the four-value vocabulary, the enumerated label occurrences, and any out-of-vocabulary occurrence with its location; validator output line; grep output |
| OUT-003 | SOW-059 OBJ-003 | REQ-004 CLM-002 CLM-003 | AC-004 | HUMAN_REVIEW: adequacy-language read-back of the guidance against the SOW-059 ledger statement and `docs/PRD_ROOT.md` §5.4 E-8, confirming the CLARIFIED label is carried | Guidance text with the boundary stated, the source label preserved, and the reviewer's recorded finding on adequacy language |
