---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-05
package_id: PKG-05
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-056]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-05

## Purpose and Objective Traceability

This deliverable keeps read-only audit and evaluation surfaces existing and
governed, with membership incorporated by reference to the live agent index.
That purpose is transcribed from the deliverable register row for
DEL-05-05 (`Type: DOC_UPDATE`, `ContextEnvelope: S`) and from the deliverable's
`_CONTEXT.md`.

The single covered project scope item is **SOW-056**: "Read-only audit and
evaluation surfaces exist and are governed, with membership incorporated by
reference to the live agent index." Its `SourceRef` is `PRD §5.4 E-5
[TRANSCRIBED]`, whose own label and source line reads: `AGENTS.md` agent
index; `docs/DIRECTIVE.md` §4.1.

The supported package objective is **OBJ-003** — the human evaluation and
iteration loops close, in two conditions, one universal (structural linkage
completeness for every accepted change) and one sampled (retrieval usability
against a threshold and sample fixed before evaluation). This deliverable
serves the universal half by keeping the surfaces that produce evaluation
findings identifiable and read-only, so that a finding's origin is
retrievable from files alone.

Nothing beyond those grounding sources is imported here. The deliverable's
`_CONTEXT.md` records `Acceptance Criteria: TBD — the accepted decomposition
states no per-deliverable acceptance criteria`, so the criteria below are
**candidate** definitions authored from the grounding sources only. They
claim no acceptance and no lifecycle transition.

## Deliverable Definition — Ontology

The register's `AnticipatedArtifacts` field and the `_CONTEXT.md
## Anticipated Artifacts` list name two artifacts, which become the two
expected outputs.

- **OUT-001** — Audit-surface conformance note: a written record stating which
  audit and evaluation surfaces are governed, resolving membership *by
  reference* to the live agent index rather than by restating a list.
- **OUT-002** — Read-only posture check: a per-surface record of the declared
  write scope of each audit and evaluation instruction package named by the
  live index, together with the deterministic check output that observed it.

- **CLM-001** — The register's `ContextEnvelopeNotes` for this deliverable
  state that "Membership is incorporated by reference; the work is conformance
  only." The scope of this deliverable is therefore conformance evidence over
  an existing arrangement, not the design of a new audit surface and not any
  change to index membership.

## Completion and Reliance Basis — Epistemology

The obligations restated below are the covered scope-ledger content, not new
commitments.

- **REQ-001** — Read-only audit and evaluation surfaces shall exist and shall
  be governed (SOW-056; `SourceRef` PRD §5.4 E-5 [TRANSCRIBED]).
- **REQ-002** — Membership of those surfaces shall be incorporated by
  reference to the live agent index; this deliverable shall maintain no
  parallel enumeration of audit or evaluation roles (SOW-056; `SourceRef`
  PRD §5.4 E-5 [TRANSCRIBED], whose source line names the `AGENTS.md` agent
  index and `docs/DIRECTIVE.md` §4.1).
- **REQ-003** — The read-only posture of each such surface shall be observable
  from the surface's own declared write scope in its instruction package,
  rather than asserted in prose alone (SOW-056 read with the register's
  "conformance only" envelope note).

Candidate acceptance criteria:

- **AC-001** — The conformance note names the live agent index as the sole
  membership source for audit and evaluation roles and contains no
  independent role list that could drift from it.
- **AC-002** — For every audit and evaluation role the live index names, the
  note cites the instruction file path recorded in that index, and every cited
  path resolves in the checkout.
- **AC-003** — The posture check records, per named surface, the write scope
  declared in that surface's own instruction package, with the file and
  location cited.
- **AC-004** — The deterministic instruction-contract check over those
  instruction packages completes with zero ERROR findings, and its output is
  captured in the posture check.

Reliance basis: these outputs are structural evidence about surfaces. They are
not an audit result, not an evaluation judgment, and not acceptance of any
deliverable. Completeness of this evidence is never sufficiency for reliance.

## Production and Verification Method — Praxeology

Production reads the live agent index, resolves each named audit and
evaluation instruction package, records its declared write scope, and runs the
deterministic checks below, capturing output verbatim.

- **VER-001** — Run `python3 tools/validation/validate_agent_instructions.py`
  (optionally with the audit and evaluation `agents/AGENT_*.md` paths as
  positional arguments) and require exit 0. The tool validates the
  mechanically observable `AGENT_*.md` instruction contract, including the
  `EVALUATION` dispatch set and the audit-output write-root constraint, and
  reports ERROR and WARN findings with a summary line.
- **VER-002** — Run `python3 tools/validation/validate_instruction_entrypoints.py`
  and require exit 0, confirming that the root instruction entrypoints that
  carry the live index resolve under the import contract.

Both commands are read-only and exist in the checkout at this basis. Where a
question is semantic — whether the note genuinely incorporates membership by
reference instead of restating it — no deterministic check exists, and the
matrix records `HUMAN_REVIEW` with a named method rather than inventing one.

## Governing Values and Decisions — Axiology

- **AX-001** — The live registry governs. PRD §5 registry discipline states
  that this section cites registries rather than their members, and that where
  a live registry and narrative disagree the live registry governs and the
  discrepancy is surfaced. A conformance note that duplicates the index would
  contradict the commitment it is evidence for.
- **AX-002** — The `AnticipatedWriteLocus` recorded for this deliverable is
  "execution-tree; instruction-surface (M2) if the index must change". That is
  a planning note, not authorization. Any act touching the instruction surface
  — `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, or
  `.github/workflows/` — requires an independently authorized M2 tranche.
  **This Scope of Work grants none.** If conformance work finds that the index
  itself must change, that finding is surfaced and routed, never applied here.
- **AX-003** — Evidence is not acceptance. Producing these outputs performs no
  lifecycle transition; the deliverable's state remains `OPEN`, as do all
  root deliverable states at this basis. Acceptance criteria here are
  candidates for owner review, and `ResponsibleParty` remains unassigned in
  the register and is not altered by this contract.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-056 OBJ-003 | REQ-001 REQ-002 CLM-001 | AC-001 AC-002 | HUMAN_REVIEW: incorporation-by-reference read-through of the note against the live agent index | The conformance note itself, with every cited instruction-file path resolvable in the checkout and no independent role list. |
| OUT-002 | SOW-056 OBJ-003 | REQ-003 | AC-003 AC-004 | VER-001 VER-002 | The posture check, carrying per-surface declared write scope with citations, plus verbatim captured output and exit codes of both commands. |
