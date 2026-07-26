---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-02-05
package_id: PKG-02
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-013, SOW-030]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-02-05

## Purpose and Objective Traceability

This contract defines the production scope of `DEL-02-05` — Live Registry
Discipline for Skills and Tools — in service of project scope items `SOW-013`
and `SOW-030` and package objective `OBJ-001`, as recorded in the accepted root
decomposition and its companion deliverable register.

The accepted register states the deliverable's purpose as keeping method packs
and deterministic operations maintained as live registries that govern their own
membership, with the live registry authoritative over any narrative list and
discrepancies surfaced. Its register `Type` is `REGISTER`.

**Claim status.** Every `OUT-*`, `CLM-*`, `REQ-*`, `AC-*`, `VER-*`, `TBD-*`, and
`AX-*` definition below is a *candidate* authored under `MODE=INIT` from the four
authorized grounding sources named in the Axiology section. Nothing here claims
acceptance, review outcome, or lifecycle state.

**Write-locus gate.** The register records this deliverable's
`AnticipatedWriteLocus` as `instruction-surface (M2); execution-tree for drift
reports`. That is a planning note, not authorization. Any act that changes
`AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, or `init/` requires an
independently authorized M2 tranche. **This Scope of Work grants no such
authorization.** Drift reports are written within the execution tree. Note the
asymmetry this creates and preserves: a drift report may *record* that a
narrative list disagrees with a live registry, but correcting the narrative is
itself an instruction-surface act requiring M2.

## Deliverable Definition — Ontology

The anticipated artifacts are transcribed from the register's
`AnticipatedArtifacts` field and the deliverable's `_CONTEXT.md`. The register
records `ContextEnvelope: S` with the note "Two registries and a comparison
rule", which bounds this deliverable to two registries and one comparison rule.

- **OUT-001** — Registry drift check: a repeatable read-only check comparing the
  live registry membership of the two registries against what the narrative
  surfaces assert, producing findings.
- **OUT-002** — Narrative-vs-registry discrepancy report: the recorded output of
  that check, listing each discrepancy with both sides cited and with the live
  registry identified as governing.

## Completion and Reliance Basis — Epistemology

- **CLM-001** — Covered scope item `SOW-013` (SourceRef: PRD §5 registry
  discipline [TRANSCRIBED]) states that dynamic registries are incorporated by
  reference rather than restated, and that where a live registry and a narrative
  list disagree, the live registry governs and the discrepancy is surfaced.
- **CLM-002** — Covered scope item `SOW-030` (SourceRef: PRD §5.2 O-5
  [TRANSCRIBED]) states that method packs and deterministic operations are
  maintained as live registries, and that the live registry is authoritative
  over any narrative list.
- **CLM-003** — The adopted PRD item O-5 incorporates membership by reference to
  `skills/README.md` and `tools/REGISTRY.md`. Those two are the registries this
  deliverable compares against narrative assertions.
- **REQ-001** — The drift check shall determine live membership from the
  registries themselves, not from any narrative restatement of them, per
  `CLM-001` and `CLM-002`.
- **REQ-002** — The discrepancy report shall, for each finding, cite the live
  registry entry and the disagreeing narrative statement, and shall record the
  live registry as governing.
- **REQ-003** — The discrepancy report shall surface discrepancies rather than
  resolve them: correcting a narrative surface is an instruction-surface act
  outside this contract's authorization.
- **REQ-004** — Neither output shall introduce a parallel membership list that
  would itself become a narrative surface subject to drift.
- **TBD-001** — Unresolved: `SOW-030` covers both method packs and deterministic
  operations, but a deterministic membership check exists for the skills
  registry only (see `VER-001`). Whether an equivalent check for the tool
  registry is in scope for this deliverable or belongs elsewhere is unresolved
  and is recorded rather than assumed.
- **AC-001** — The drift check derives live membership from the registries
  themselves, is repeatable, and alters neither registry nor narrative surface.
- **AC-002** — The discrepancy report lists each discrepancy with both sides
  cited, identifies the live registry as governing, and leaves every discrepancy
  open rather than correcting it.

## Production and Verification Method — Praxeology

- **VER-001** — Run `python3 tools/validation/validate_skill_metadata.py skills`
  (skills-root argument optional, default `skills`; `--json` available). It
  deterministically checks the repo-native skill folders under `skills/`:
  `SKILL.md` presence, frontmatter delimitation, required `name` and
  `description`, name-to-folder-name agreement, name character rules, and the
  presence and validity of the `chirality-skill-version` and
  `chirality-task-profile` metadata. It establishes conformant live membership
  of the skills registry; it does not compare that membership against any
  narrative list.

No deterministic tool in this repository compares live registry membership to a
narrative assertion, and none checks `tools/REGISTRY.md` membership. That gap is
recorded in `TBD-001` and is the reason `OUT-002` routes to human review rather
than to a command. Naming a check that does not exist would defeat the drift
discipline this deliverable implements.

Production method: read membership from the two registries directly, compare it
to the narrative statements that assert membership, record every disagreement
with both citations, and stop. The method writes only drift reports within the
execution tree.

## Governing Values and Decisions — Axiology

- **AX-001** — Grounding boundary (K-INVENT-1): every definition here derives
  only from the deliverable's register row, its `_CONTEXT.md`, the scope-ledger
  statements of `SOW-013` and `SOW-030`, and the adopted `docs/PRD_ROOT.md`.
  `_CONTEXT.md` records that the accepted decomposition states no
  per-deliverable acceptance criteria; the criteria above are candidates.
- **AX-002** — The live registry governs (K-AGENTS-1): where narrative and
  registry disagree, the registry is authoritative and the disagreement is
  surfaced. `REQ-004` applies that rule reflexively, so this deliverable's own
  outputs do not become a new drifting narrative.
- **AX-003** — Surface, do not resolve (K-CONFLICT-1, `REQ-003`): recording a
  discrepancy is in scope; correcting the instruction surface is an M2 act that
  this contract does not authorize.
- **AX-004** — Unknowns become `TBD` rather than guesses (K-INVENT-1): the
  asymmetric tool coverage is recorded as `TBD-001`, not filled in with an
  assumed check.
- **AX-005** — Human authority (K-AUTH-1): these candidates are reviewed by the
  human owner at the PR gate; no agent act confers acceptance.
- **AX-006** — Path discipline: this contract uses repo-relative paths only and
  embeds no machine-absolute path. `ResponsibleParty` remains `TBD`.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-013 SOW-030 OBJ-001 | CLM-002 CLM-003 REQ-001 REQ-004 TBD-001 | AC-001 | VER-001 | Repeatable check definition plus the recorded skill-metadata validator output establishing conformant live skills-registry membership at the time of check. |
| OUT-002 | SOW-013 OBJ-001 | CLM-001 CLM-003 REQ-002 REQ-003 REQ-004 | AC-002 | HUMAN_REVIEW: owner reading of the discrepancy report against the two live registries cited by the covered scope-ledger statements | Discrepancy report citing both sides per finding, naming the live registry as governing, with all findings left open. |
