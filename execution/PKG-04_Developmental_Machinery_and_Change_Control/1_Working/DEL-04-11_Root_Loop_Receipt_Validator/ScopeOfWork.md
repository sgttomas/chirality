---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-11
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@75c4e2ba401a6f5ad0c2f38846c39db6ab157405
project_scope_refs: [SOW-041, SOW-053]
package_objective_refs: [OBJ-003]
status: DRAFT_AWAITING_OWNER_ACCEPTANCE
---

# Scope of Work — DEL-04-11

## Purpose and Objective Traceability

This draft defines the candidate production contract for `DEL-04-11`, Root
Loop Receipt Validator, a `TEST_SUITE` deliverable of
`PKG-04_Developmental_Machinery_and_Change_Control` with Context Envelope
`M`. It serves project scope items `SOW-041` and `SOW-053` and package
objective `OBJ-003`.

The accepted deliverable row describes this carrier as a deterministic
Root-specific loop receipt validator for the D-7 governed-loop and E-2
minimal-receipt disciplines while preserving DEL-04-05 as doctrine and
DEL-05-02 as the evidence-discipline crosscheck. This deliverable is the
bounded validator carrier; it does not replace either preserved carrier.

**Standing boundary:** Root-specific deterministic receipt validator, `tools/**` implementation under separate M2 authority.

## Deliverable Definition — Ontology

The accepted deliverable row and `_CONTEXT.md` define four anticipated
artifacts. This draft expresses them as four candidate outputs without adding
an implementation interface or tool behavior.

- **OUT-001 — Root loop receipt validator.** One Root-specific deterministic
  validator bounded to the D-7 governed-loop and E-2 minimal-receipt
  disciplines allocated to this deliverable.
- **OUT-002 — Deterministic valid and invalid receipt fixtures.** Bounded
  fixture evidence associated with the Root-specific validator.
- **OUT-003 — Validator contract and CI invocation notes.** The contract and
  invocation notes needed to identify the validator's accepted basis and
  declared evaluation boundary.
- **OUT-004 — Validation reports.** Reports carrying the evidence produced by
  separately authorized validation runs.

The accepted anticipated write locus is `tools/** (M2);
execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-11_Root_Loop_Receipt_Validator/**`.
It is a planning note, never authorization.

## Completion and Reliance Basis — Epistemology

### Grounded claims

- **CLM-001** — The applied deliverable-register row identifies this carrier as
  `TEST_SUITE`, Context Envelope `M`, mapped to `SOW-041`, `SOW-053`, and
  `OBJ-003`, with the description and anticipated artifacts represented in
  this draft.
- **CLM-002** — The applied row describes a deterministic Root-specific loop
  receipt validator for the D-7 governed-loop and E-2 minimal-receipt
  disciplines while preserving DEL-04-05 as doctrine and DEL-05-02 as the
  evidence-discipline crosscheck.
- **CLM-003** — The accepted anticipated artifacts are a Root loop receipt
  validator, deterministic valid and invalid receipt fixtures, validator
  contract and CI invocation notes, and validation reports.
- **CLM-004** — The carrier context bounds the deliverable to one Root-specific
  validator plus bounded fixtures and states that implementation under
  `tools/**` requires a separately authorized M2 tranche.

### Completion and reliance limits

- **EVD-001** — A completion claim requires this deliverable's own accepted
  evidence for the exact produced outputs; evidence or acceptance belonging
  to DEL-04-05, DEL-05-02, the SOW draft, or another tranche cannot substitute
  for that evidence.
- **EVD-002** — Evidence supporting determinism must be bound to the exact
  accepted validator, fixture, contract, invocation-note, and report
  identities on which the claim relies.
- **EVD-003** — Any result is limited to its declared evaluation boundary and
  accepted evidence. The existence of a validator, fixture, note, or report
  does not by itself establish completion or reliance.
- **EVD-004** — This SOW lifts no hold, authorizes no implementation, grants no
  `tools/**` M2 authority, and creates no dispatch authority. Acceptance of
  this SOW is a separate owner act against its exact bytes.

Accepted grounding citations:

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`,
  row `DEL-04-11_Root_Loop_Receipt_Validator`.
- `execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-11_Root_Loop_Receipt_Validator/_CONTEXT.md`.
- `execution/_ScopeChange/SCA-004_2026-08-22_1749/Propagation_Plan.md` §2,
  `INIT-07`.

## Production and Verification Method — Praxeology

This draft plans the work locus and evidence shape only. Production may begin
only under a later, separately authorized tranche that supplies the exact
accepted basis, write scope, and authority for its work. In particular, the
anticipated `tools/**` implementation requires separate M2 authority.

Within that later authority, production is limited to the four outputs in the
Ontology. Verification must evaluate the produced outputs against the
accepted bounded purpose and retain the deliverable's own evidence for the
resulting claims. The exact validator behavior, interfaces, dependencies,
dispatch plan, schedule, implementation method, CI wiring, and acceptance act
remain for their owning later gates; this draft does not invent or authorize
them.

The later evidence review must establish, from accepted evidence, whether:

- **VER-001** — `OUT-001` is the Root-specific deterministic receipt validator
  allocated to this carrier and remains within its accepted boundary;
- **VER-002** — `OUT-002` contains the bounded valid and invalid receipt
  fixtures claimed for the exact accepted validator;
- **VER-003** — `OUT-003` identifies the accepted validator contract and CI
  invocation notes without treating either as implementation authority; and
- **VER-004** — `OUT-004` binds validation reports to the exact accepted
  output identities and declared evaluation boundary.

These are candidate evaluation statements, not evidence that the work has
occurred and not owner acceptance of any output.

## Governing Values and Decisions — Axiology

- **AX-001 — Authority separation.** A coordination surface, draft SOW,
  anticipated write locus, fixture, contract, invocation note, or report does
  not create authority. Owner acceptance of this SOW is separate from every
  later implementation, dispatch, lifecycle, and reliance act.
- **AX-002 — Doctrine and evidence ownership.** DEL-04-05 remains the D-7
  doctrine carrier and DEL-05-02 remains the E-2 evidence-discipline
  crosscheck. DEL-04-11 validates within its accepted allocation and does not
  supplant either carrier.
- **AX-003 — Grounding before detail.** No dependency, interface, tool
  behavior, estimate, schedule, CI wiring, or acceptance criterion absent from
  the accepted sources is asserted here. A grounding gap is a blocker, not a
  license to infer content.
- **AX-004 — Draft status.** These bytes remain
  `DRAFT_AWAITING_OWNER_ACCEPTANCE`. `_STATUS.md` remains `OPEN`, no hold is
  lifted, and nothing is implemented or activated by drafting this contract.

## Output and Evaluation Matrix

| Output | Scope and objective refs | Grounded claim refs | Evidence refs | Verification ref | Evaluation boundary |
|---|---|---|---|---|---|
| OUT-001 | SOW-041; SOW-053; OBJ-003 | CLM-001; CLM-002; CLM-003; CLM-004 | EVD-001; EVD-002; EVD-003; EVD-004 | VER-001 | Root-specific deterministic receipt validator; completion requires its own accepted evidence |
| OUT-002 | SOW-041; SOW-053; OBJ-003 | CLM-001; CLM-004 | EVD-001; EVD-002; EVD-003 | VER-002 | Bounded valid and invalid receipt fixtures associated with the exact accepted validator |
| OUT-003 | SOW-041; SOW-053; OBJ-003 | CLM-001; CLM-004 | EVD-001; EVD-002; EVD-004 | VER-003 | Validator contract and CI invocation notes; neither grants implementation or dispatch authority |
| OUT-004 | SOW-041; SOW-053; OBJ-003 | CLM-001; CLM-002; CLM-003 | EVD-001; EVD-002; EVD-003 | VER-004 | Validation reports bound to exact output identities and their declared evaluation boundary |
