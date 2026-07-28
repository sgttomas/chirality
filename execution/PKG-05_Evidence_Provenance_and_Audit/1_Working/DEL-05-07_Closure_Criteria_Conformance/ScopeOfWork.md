---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-07
package_id: PKG-05
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-058]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-07

## Purpose and Objective Traceability

This deliverable keeps closure meaning accepted authoritative truth,
regenerated or explicitly deferred derivatives, recorded audit status, and
surfaced unresolved blockers — never merely that files were written. That
purpose is transcribed from the deliverable register row for DEL-05-07
(`Type: REQ_SLICE`, `ContextEnvelope: S`) and from the deliverable's
`_CONTEXT.md`.

The single covered project scope item is **SOW-058**: "A scope unit or phase
is not closed because files were written: closure requires accepted
authoritative truth, regenerated or explicitly deferred derivatives, recorded
audit status, and surfaced unresolved blockers." Its `SourceRef` is
`PRD §5.4 E-7 [TRANSCRIBED]`, whose label and source line names the `AGENTS.md`
closure rule and `docs/DIRECTIVE.md` §2.7.

The supported package objective is **OBJ-003** — the human evaluation and
iteration loops close, universally by structural linkage completeness for
every accepted change and by a sampled retrieval exercise. A scope unit closed
on the strength of written files alone would break the universal half
directly: there would be no accepted ruling to link to, and the record would
show activity where it should show acceptance.

The deliverable's `_CONTEXT.md` records `Acceptance Criteria: TBD — the
accepted decomposition states no per-deliverable acceptance criteria`. The
criteria below are therefore **candidate** definitions authored from the
grounding sources only. They claim no acceptance and no lifecycle transition.

## Deliverable Definition — Ontology

The register's `AnticipatedArtifacts` field and the `_CONTEXT.md
## Anticipated Artifacts` list name three artifacts, which become the three
expected outputs.

- **OUT-001** — Closure checklist: the checkable form of the covered closure
  rule, with one item per condition the rule requires and an explicit
  statement of what does not satisfy it.
- **OUT-002** — Derivative-regeneration status: a per-derivative record of
  whether each derivative package in the unit's scope was regenerated or
  explicitly deferred, with the deferral reason where deferred.
- **OUT-003** — Blocker surfacing evidence: the record of unresolved blockers
  carried out of the unit, or the positive statement that none remained.

- **CLM-001** — The covered statement is stated negatively as well as
  positively: writing files is expressly not closure. The checklist must carry
  that negative, because a checklist of positive conditions alone can be
  satisfied in appearance by the very activity the rule excludes.
- **CLM-002** — The register's `ContextEnvelopeNotes` for this deliverable
  state "One checklist over an existing rule." The scope is conformance
  instrumentation over a rule that already governs, not a new closure policy
  and not an amendment to the existing one.

## Completion and Reliance Basis — Epistemology

The four conditions below are the four conjuncts of the covered scope
statement, restated without extension.

- **REQ-001** — Closure shall require accepted authoritative truth (SOW-058;
  `SourceRef` PRD §5.4 E-7 [TRANSCRIBED]).
- **REQ-002** — Closure shall require derivative packages to be regenerated or
  explicitly deferred (SOW-058; same `SourceRef`). "Explicitly" excludes
  silent omission: a deferral that is not recorded is not a deferral.
- **REQ-003** — Closure shall require recorded audit status (SOW-058; same
  `SourceRef`).
- **REQ-004** — Closure shall require unresolved blockers to be surfaced
  (SOW-058; same `SourceRef`).

Candidate acceptance criteria:

- **AC-001** — The checklist carries exactly one item per condition above,
  each item naming what evidence would satisfy it and where that evidence
  lives.
- **AC-002** — The checklist states explicitly that the existence of written
  files satisfies no item, and no item is phrased so that file production
  alone would discharge it.
- **AC-003** — The derivative-regeneration status names every derivative
  package in the unit's scope and records, for each, either regeneration with
  its upstream accepted snapshot or an explicit deferral with a stated reason.
- **AC-004** — The blocker evidence records each unresolved blocker with a
  resolvable location, or states positively that none remained; silence is
  never treated as absence.
- **AC-005** — The recorded audit status cites the deterministic output it was
  read from, including the command and its exit code.

Reliance basis: these outputs make a closure judgment checkable; they do not
make it. Closure remains a human act. Structural conformance here is evidence
about the record, and evidence completeness is never evidence sufficiency for
the reliance the closure decision carries.

## Production and Verification Method — Praxeology

Production instantiates the checklist against the unit under consideration and
runs the deterministic surfaces below, capturing output and exit codes.

- **VER-001** — Run `python3 tools/practitioner_harness/harness.py status --project root`
  and require exit 0. The command reports the root product's posture and the
  deliverable-state distribution read from `Current State` fields, giving the
  recorded-state observation that audit status is cited against. Root
  citizenship of this command is observation only; it decides nothing.
- **VER-002** — Run `python3 tools/validation/scan_deliverable_consistency.py <DELIVERABLE_PATH>`
  for each deliverable in the unit. The scanner is read-only and reports the
  resolved production format, production-format issues, missing core files,
  identity mismatches, and marker findings as JSON.
- **VER-003** — Run `python3 tools/validation/validate_root_surface_ownership.py`
  and require exit 0. This is the G2 guard; it reports whether every
  materialized package and deliverable child is registered against the
  declared decomposition.

All three commands exist in the checkout at this basis and were observed to
run read-only. Whether a checklist faithfully expresses the closure rule is a
semantic question with no deterministic check, so the matrix records
`HUMAN_REVIEW` with a named method rather than inventing one.

## Governing Values and Decisions — Axiology

- **AX-001** — Activity is not acceptance. The covered statement exists
  because file production is the most available proxy for progress and the
  least reliable evidence of it. The checklist's value is precisely that it
  refuses that proxy.
- **AX-002** — An explicit deferral is a lawful closure state; a silent gap is
  not. Recording a deferral with its reason keeps the record honest without
  forcing work that is not ready, which is why REQ-002 is written
  disjunctively.
- **AX-003** — Deterministic guards gate objective preconditions and never
  make the judgment. PRD §3 OBJ-2 records that deterministic guards, fan-in
  gates, and structural validation gates remain lawful non-human gates that
  never make the acceptance or issuance judgment. Nothing in this contract
  converts a passing command into a closure decision.
- **AX-004** — The `AnticipatedWriteLocus` recorded for this deliverable is
  "execution-tree". Work under this contract writes evidence in the execution
  tree only. Any act touching the instruction surface — `AGENTS.md`,
  `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, or
  `.github/workflows/` — would require an independently authorized M2 tranche,
  and **this Scope of Work grants none.**
- **AX-005** — Evidence is not acceptance. Producing these outputs performs no
  lifecycle transition; the deliverable's state is `INITIALIZED`, as are all 46 Root deliverable states at this basis. The criteria above are candidates for
  owner review, and `ResponsibleParty` is `Ryan Tufts` in the current register under D-GOV-27 and is not altered by this contract.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-058 OBJ-003 | REQ-001 REQ-002 REQ-003 REQ-004 CLM-001 CLM-002 | AC-001 AC-002 | HUMAN_REVIEW: conjunct-by-conjunct read-through of the checklist against the covered closure statement, including its negative clause | The checklist itself, one item per conjunct, each naming its satisfying evidence and its location, with the files-written exclusion stated. |
| OUT-002 | SOW-058 OBJ-003 | REQ-002 | AC-003 | VER-002 VER-003 | The per-derivative status record, plus verbatim scanner JSON per deliverable and the G2 guard output with exit codes. |
| OUT-003 | SOW-058 OBJ-003 | REQ-003 REQ-004 | AC-004 AC-005 | VER-001 | The blocker record with resolvable locations or an explicit none-remained statement, alongside the captured state-distribution output and its exit code. |
