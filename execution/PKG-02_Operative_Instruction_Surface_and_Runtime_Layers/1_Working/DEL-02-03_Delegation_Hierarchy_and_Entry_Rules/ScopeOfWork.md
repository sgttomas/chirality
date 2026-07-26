---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-03
package_id: PKG-02
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-028]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-02-03

## Purpose and Objective Traceability

This contract defines the production scope of `DEL-02-03` — Delegation Hierarchy
and Entry Rules — in service of project scope item `SOW-028` and package
objective `OBJ-002`, as recorded in the accepted root decomposition and its
companion deliverable register.

The accepted register states the deliverable's purpose as keeping the
Agent 0 → Agent 1 → Agent 2 hierarchy, the entry rules, the
no-delegation-below-Agent-2 rule, and the three Agent 2 construction forms live
and consistent with the incorporated agent index.

**Claim status.** Every `OUT-*`, `CLM-*`, `REQ-*`, `AC-*`, `VER-*`, and `AX-*`
definition below is a *candidate* authored under `MODE=INIT` from the four
authorized grounding sources named in the Axiology section. Nothing here claims
acceptance, review outcome, or lifecycle state.

**Write-locus gate.** The register records this deliverable's
`AnticipatedWriteLocus` as `instruction-surface (M2)`. That is a planning note,
not authorization. Any act that changes `AGENTS.md`, `agents/`, `skills/`,
`tools/`, root `docs/`, or `init/` requires an independently authorized M2
tranche. **This Scope of Work grants no such authorization**, and producing the
outputs below does not create one. This gate binds tightly here, because the
doctrine this deliverable describes lives in the instruction surface itself.

## Deliverable Definition — Ontology

The anticipated artifacts are transcribed from the register's
`AnticipatedArtifacts` field and the deliverable's `_CONTEXT.md`.

- **OUT-001** — Hierarchy conformance notes: notes recording the
  Agent 0 → Agent 1 → Agent 2 delegation hierarchy and the
  no-delegation-below-Agent-2 rule, and whether the live index is consistent
  with them.
- **OUT-002** — Entry-rule checklist: the declared entry rules expressed as a
  checkable list, covering which layers may be entered directly and which may
  delegate to which.
- **OUT-003** — Agent 2 construction-form guidance: guidance covering the three
  Agent 2 construction forms and the conditions distinguishing them.

The register records `ContextEnvelope: M` with the note "Bounded to the
delegation doctrine and its index reference", which bounds these outputs to the
doctrine and its reference to the live index — not to the index membership
itself.

## Completion and Reliance Basis — Epistemology

- **CLM-001** — Covered scope item `SOW-028` (SourceRef: PRD §5.2 O-3
  [TRANSCRIBED]) states that the runtime delegation hierarchy is Agent 0 to
  Agent 1 to Agent 2 with declared entry rules, no delegation below Agent 2, and
  three Agent 2 construction forms, and that role membership is incorporated by
  reference to the live index.
- **CLM-002** — Incorporation by reference is part of the covered statement, not
  a production convenience: the adopted PRD item O-3 enumerates no agents and
  defers role membership to the live index. Restating a membership list inside
  this deliverable's outputs would contradict the statement it implements.
- **REQ-001** — The hierarchy conformance notes shall state the three-layer
  delegation order and the no-delegation-below-Agent-2 rule, each traceable to
  `CLM-001`.
- **REQ-002** — The entry-rule checklist shall express the declared entry rules
  as checkable items and shall attribute each item to the covered statement or
  the live index it incorporates.
- **REQ-003** — The construction-form guidance shall cover exactly three Agent 2
  construction forms per `CLM-001`, and shall neither add a fourth form nor
  collapse the three.
- **REQ-004** — No output shall restate role membership as a parallel list;
  membership is cited to the live index per `CLM-002`.
- **AC-001** — The hierarchy conformance notes state the delegation order and
  the no-delegation-below-Agent-2 rule with source citations, and record any
  observed inconsistency with the live index rather than resolving it silently.
- **AC-002** — The entry-rule checklist is expressed as discrete checkable
  items, each carrying its source, and covers entry at every layer named in
  `CLM-001`.
- **AC-003** — The construction-form guidance describes exactly three forms and
  contains no parallel enumeration of role membership.

## Production and Verification Method — Praxeology

Two deterministic surfaces in this repository bear on these outputs. Both
produce findings about the instruction surface; neither rules on doctrinal
conformance, and neither is treated as a substitute for owner judgment.

- **VER-001** — Run `python3 tools/validation/validate_agent_instructions.py`
  (defaults to `agents/AGENT_*.md`; accepts explicit paths and `--json`). It
  deterministically checks the mechanically observable instruction contract:
  structural fields and section presence, type/class compatibility,
  `R`-identifier references, exact `AGENT_*.md` references, and the D-GOV-11
  dedicated Agent 2 requalification posture. Its own documentation records that
  semantic agent qualification remains a rubric audit; this contract carries
  that limit forward rather than overstating the check.
- **VER-002** — Run `python3 tools/validation/validate_instruction_entrypoints.py`
  (optional repo-root argument). It deterministically checks the root
  instruction entrypoints and the `CLAUDE.md` import contract, including the
  role and routing patterns by which Agent 0, Agent 1, and Agent 2 entry and
  delegation are expressed.

Production method: read the covered scope statement and the adopted PRD item it
cites, transcribe the hierarchy, entry rules, and construction forms, and cite
the live index for membership instead of copying it. The method writes only
within the execution tree and stops at the M2 boundary.

## Governing Values and Decisions — Axiology

- **AX-001** — Grounding boundary (K-INVENT-1): every definition here derives
  only from the deliverable's register row, its `_CONTEXT.md`, the scope-ledger
  statement of `SOW-028`, and the adopted `docs/PRD_ROOT.md`. `_CONTEXT.md`
  records that the accepted decomposition states no per-deliverable acceptance
  criteria; the criteria above are candidates.
- **AX-002** — Registry discipline (K-AGENTS-1): role membership is incorporated
  by reference to the live index. This contract maintains no parallel agent
  list, and `REQ-004` extends that discipline to the deliverable's outputs.
- **AX-003** — Tool limits: `VER-001` and `VER-002` produce findings, not
  conformance rulings. Where their documentation records a limit — such as
  semantic qualification remaining a rubric audit — the limit is carried
  forward, not elided.
- **AX-004** — Human authority (K-AUTH-1): these candidates are reviewed by the
  human owner at the PR gate; no agent act confers acceptance.
- **AX-005** — Path discipline: this contract uses repo-relative paths only and
  embeds no machine-absolute path. `ResponsibleParty` remains `TBD`.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-028 OBJ-002 | CLM-001 CLM-002 REQ-001 REQ-004 | AC-001 | VER-001 | Hierarchy notes with per-statement citations, plus the recorded validator findings for `agents/AGENT_*.md` at the time of check. |
| OUT-002 | SOW-028 OBJ-002 | CLM-001 REQ-002 | AC-002 | VER-002 | Entry-rule checklist as discrete items with sources, plus the recorded entrypoint-validator output at the time of check. |
| OUT-003 | SOW-028 OBJ-002 | CLM-001 CLM-002 REQ-003 REQ-004 | AC-003 | HUMAN_REVIEW: owner reading of the construction-form guidance against the three forms named in the covered scope-ledger statement | Guidance covering exactly three construction forms with their distinguishing conditions and no parallel membership list. |
