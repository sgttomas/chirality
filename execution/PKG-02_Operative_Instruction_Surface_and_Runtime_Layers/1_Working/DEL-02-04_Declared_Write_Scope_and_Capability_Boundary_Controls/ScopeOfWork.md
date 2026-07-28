---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-04
package_id: PKG-02
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-019, SOW-029]
package_objective_refs: [OBJ-004]
---

# Scope of Work — DEL-02-04

## Purpose and Objective Traceability

This contract defines the production scope of `DEL-02-04` — Declared Write Scope
and Capability-Boundary Controls — in service of project scope items `SOW-019`
and `SOW-029` and package objective `OBJ-004`, as recorded in the accepted root
decomposition and its companion deliverable register.

The accepted register states the deliverable's purpose as keeping every agent's
declared write scope explicit and keeping capability from conferring authority:
sealed context, gate approval, path containment, enforced read/write scope, and
durable evidence on every child. Its register `Type` is `SECURITY_CONTROL`, and
its `ContextEnvelopeNotes` record that the work is control-shaped over the agent
surface and that the enforcement points already exist.

**Claim status.** Every `OUT-*`, `CLM-*`, `REQ-*`, `AC-*`, `VER-*`, and `AX-*`
definition below is a *candidate* authored under `MODE=INIT` from the four
authorized grounding sources named in the Axiology section. Nothing here claims
acceptance, review outcome, lifecycle state, or that any control is currently
effective.

**Write-locus gate.** The register records this deliverable's
`AnticipatedWriteLocus` as `instruction-surface (M2); execution-tree for audit
evidence`. That is a planning note, not authorization. Any act that changes
`AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, or `init/` requires an
independently authorized M2 tranche. **This Scope of Work grants no such
authorization.** Audit evidence is written within the execution tree.

## Deliverable Definition — Ontology

The anticipated artifacts are transcribed from the register's
`AnticipatedArtifacts` field and the deliverable's `_CONTEXT.md`.

- **OUT-001** — Write-scope declaration audit: a read-only audit recording, per
  agent surface examined, whether an explicit declared write scope is present
  and what it declares.
- **OUT-002** — Sealed-brief conformance checks: checks recording whether
  dispatched children carry sealed context and the declared read/write scope the
  covered statements require.
- **OUT-003** — Capability-boundary control notes: notes recording the five
  controls named in `CLM-002` — sealed context, gate approval, path containment,
  enforced read/write scope, and durable evidence — and how each is held on a
  child.

## Completion and Reliance Basis — Epistemology

- **CLM-001** — Covered scope item `SOW-019` (SourceRef: PRD §5.1 N-5
  [TRANSCRIBED], DecisionRef `DEC-005`) states that every agent has an explicit
  declared write scope.
- **CLM-002** — Covered scope item `SOW-029` (SourceRef: PRD §5.2 O-4
  [TRANSCRIBED]) states that capability never confers authority: delegation
  implies no capability inheritance, a child's capability never becomes its
  parent's, and every child remains subject to sealed context, gate approval,
  path containment, enforced read/write scope, and durable evidence.
- **CLM-003** — The scope-ledger note on `SOW-019` records that PRD item N-5 is
  split across three enforcement loci, of which `SOW-019` is one. This
  deliverable therefore covers the declared-write-scope locus only; the other
  two loci belong to their own scope items and are out of scope here.
- **CLM-004** — The register's `ContextEnvelopeNotes` record that the
  enforcement points already exist. The audit and checks below are therefore
  observational over an existing surface; they are not a mandate to build new
  enforcement.
- **REQ-001** — The write-scope declaration audit shall record, per examined
  agent surface, the presence or absence of an explicit declared write scope and
  the declaration's content, per `CLM-001`.
- **REQ-002** — The conformance checks shall record, per examined dispatch,
  whether sealed context and an enforced read/write scope were declared, per
  `CLM-002`.
- **REQ-003** — The control notes shall cover each of the five controls named in
  `CLM-002` without merging or omitting any, and shall state that capability
  does not confer authority.
- **REQ-004** — All three outputs shall be read-only over the surfaces they
  examine: the audit observes and records, and does not alter a declaration to
  make a check pass.
- **AC-001** — The audit covers every agent surface within its declared
  examination set, records presence or absence of a declared write scope per
  surface, and marks gaps as findings rather than repairing them.
- **AC-002** — The conformance checks record, per examined dispatch, both the
  sealed-context and enforced-scope observations, and identify any dispatch for
  which the observation could not be made.
- **AC-003** — The control notes address all five named controls and state the
  capability-does-not-confer-authority rule with its source citation.

## Production and Verification Method — Praxeology

The deterministic surfaces named below exist in this repository and are
read-only. Each is evidence about a declared surface; none of them rules that a
control is effective, and none substitutes for the owner's judgment.

- **VER-001** — Run `python3 tools/validation/validate_root_surface_ownership.py`
  (guard G2, no arguments; reads `execution/_harness/surface_ownership.yaml`).
  It deterministically checks the static register that maps root packages and
  deliverables to declared write targets finer than the checkout, including each
  entry's `instruction_surface` flag. It is the direct mechanical surface for
  the declared-write-scope obligation in `CLM-001`, at package and deliverable
  granularity.
- **VER-002** — Run `python3 tools/validation/validate_path_anchors.py` (optional
  repo-root argument; `--json` or `--text` output). It deterministically checks
  that live instruction and executable handoff surfaces do not bake
  machine-local home paths. Its own documentation records that it is
  intentionally narrow and ignores historical evidence, generated outputs,
  archives, and plans. It is supporting evidence for path discipline, not a
  proof of path containment.

Production method: read the covered scope statements and the adopted PRD items
they cite; observe the existing declaration surfaces read-only; record findings
and gaps as findings. No step repairs a surface to make a check pass, and no
step writes to the instruction surface.

## Governing Values and Decisions — Axiology

- **AX-001** — Grounding boundary (K-INVENT-1): every definition here derives
  only from the deliverable's register row, its `_CONTEXT.md`, the scope-ledger
  statements of `SOW-019` and `SOW-029`, and the adopted `docs/PRD_ROOT.md`.
  `_CONTEXT.md` records that the accepted decomposition states no
  per-deliverable acceptance criteria; the criteria above are candidates.
- **AX-002** — Capability is not authority (`CLM-002`): this contract is itself
  bound by the rule it describes. Authoring it conferred no write authority
  beyond its own declared targets, and no output of it grants authority to any
  agent.
- **AX-003** — Read-only posture (`REQ-004`): a control audit that edits the
  surface it audits destroys its own evidence. Findings stay findings.
- **AX-004** — Scope honesty (`CLM-003`): only one of the three N-5 enforcement
  loci is covered here. The other two are not silently absorbed.
- **AX-005** — Human authority (K-AUTH-1): these candidates are reviewed by the
  human owner at the PR gate; no agent act and no passing check confers
  acceptance.
- **AX-006** — Path discipline: this contract uses repo-relative paths only and
  embeds no machine-absolute path. `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-019 OBJ-004 | CLM-001 CLM-003 CLM-004 REQ-001 REQ-004 | AC-001 | VER-001 VER-002 | Audit table of examined surfaces with per-surface declaration findings, plus the recorded guard G2 and path-anchor outputs at the time of check. |
| OUT-002 | SOW-029 OBJ-004 | CLM-002 CLM-004 REQ-002 REQ-004 | AC-002 | HUMAN_REVIEW: owner reading of the conformance checks against the sealed-context and enforced-scope clauses of the covered scope-ledger statement | Per-dispatch check records naming sealed context and enforced read/write scope, with unobservable cases listed. |
| OUT-003 | SOW-019 SOW-029 OBJ-004 | CLM-002 REQ-003 | AC-003 | HUMAN_REVIEW: owner reading of the control notes against the five controls named in the covered scope-ledger statement | Control notes covering all five controls with the capability-does-not-confer-authority rule and its citation. |
