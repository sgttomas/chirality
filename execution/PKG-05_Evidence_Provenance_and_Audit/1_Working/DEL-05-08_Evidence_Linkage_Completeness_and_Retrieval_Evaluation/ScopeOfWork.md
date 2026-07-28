---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-08
package_id: PKG-05
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-009]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-05-08

## Purpose and Objective Traceability

This deliverable makes the evidence to ruling to changed-state linkage
retrievable from files alone for every accepted change, and runs the sampled
retrieval-usability evaluation with the time threshold and tranche sample
fixed and recorded before the evaluation runs. That purpose is transcribed
from the deliverable register row for DEL-05-08 (`Type: OBSERVABILITY`,
`ContextEnvelope: M`) and from the deliverable's `_CONTEXT.md`.

The single covered project scope item is **SOW-009**: "The categories are
related by a generative loop whose closing step - human judgment - no agent
can perform." Its `SourceRef` is `PRD §4.2 [OWNER_DECLARED]` and its
`DecisionRef` is DEC-010. The ledger row maps SOW-009 to two deliverables and
records the reason: "Cross-package deliverable mapping: the loop's
evidence-to-evaluation arc is instrumented by the evidence package." This
deliverable is that instrumentation.

The supported package objective is **OBJ-003**, whose v1 success condition is
stated in two parts: **(i) structural completeness, universal** — every
accepted change has a retrievable linkage from files alone between the
evidence that informed it, the ruling that accepted it, and the state it
changed, and a missing link is a defect regardless of sampling; and
**(ii) retrieval usability, sampled** — the linkage can be followed within a
bounded time, verified as a retrieval exercise where the time threshold and
the tranche sample are fixed and recorded before the evaluation runs.
Completeness is a property of the record; usability is measured, not asserted.

The deliverable's `_CONTEXT.md` records `Acceptance Criteria: TBD — the
accepted decomposition states no per-deliverable acceptance criteria`. The
criteria below are therefore **candidate** definitions authored from the
grounding sources only. They claim no acceptance and no lifecycle transition.

## Deliverable Definition — Ontology

The register's `AnticipatedArtifacts` field and the `_CONTEXT.md
## Anticipated Artifacts` list name three artifacts, which become the three
expected outputs.

- **OUT-001** — Linkage completeness check: the universal check over the
  declared population of accepted changes, recording per change whether the
  evidence, ruling, and changed-state endpoints each resolve from files alone.
- **OUT-002** — Pre-registered sample and threshold record: the record fixing
  the time threshold and the tranche sample, created and committed before any
  evaluation observation is made.
- **OUT-003** — Retrieval evaluation report: the result of the timed retrieval
  exercise measured against that pre-registered threshold and sample.

- **CLM-001** — The covered scope statement holds that the loop's closing step
  is human judgment, which no agent can perform. This deliverable instruments
  the evidence-to-evaluation arc that feeds that step; it never performs it.
  The retrieval exercise is conducted by the accountable human, and its result
  informs a judgment rather than constituting one.
- **CLM-002** — The register's `ContextEnvelopeNotes` for this deliverable
  state "One universal check plus one pre-registered sampled exercise." The
  two are different in kind, and the contract keeps them separable: a
  favourable usability result never substitutes for a completeness finding.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — For every accepted change in the declared population, the
  linkage between the evidence that informed it, the ruling that accepted it,
  and the state it changed shall be retrievable from files alone (OBJ-003
  condition (i); deliverable Description in the register row for DEL-05-08).
- **REQ-002** — The sampled retrieval-usability evaluation shall run only with
  the time threshold and the tranche sample fixed and recorded beforehand;
  neither may be chosen or adjusted after results are seen (OBJ-003 condition
  (ii); deliverable Description in the same register row).
- **REQ-003** — A missing link shall be recorded as a defect regardless of
  sampling (OBJ-003 condition (i)). Sampling governs the usability half only
  and never narrows the universal half.

Candidate acceptance criteria:

- **AC-001** — The completeness check declares its population boundary
  explicitly — which accepted changes are in scope and which are not — before
  reporting any result over it.
- **AC-002** — For each change in that population, the check records the three
  linkage endpoints as resolvable file locations, or records the missing
  endpoint as a defect with its identity; no change is silently omitted.
- **AC-003** — The pre-registration record fixes both the time threshold and
  the tranche sample, and its commit precedes the first evaluation
  observation, with the ordering demonstrable from repository history.
- **AC-004** — The evaluation report measures against the pre-registered
  threshold and sample only; any departure is recorded as a deviation with its
  reason and never applied by re-fixing the threshold or the sample.
- **AC-005** — The report keeps completeness findings and usability findings
  distinct, and states no usability result as evidence of completeness.

Reliance basis: the completeness check establishes a property of the record;
the evaluation measures how the record performs for a human reader on a fixed
sample. Neither establishes that the underlying changes were sound. Evidence
completeness is never evidence sufficiency.

## Production and Verification Method — Praxeology

Production declares the population, runs the deterministic surfaces below over
it, records the pre-registration before observing anything, and only then runs
the timed exercise.

- **VER-001** — Run `python3 tools/practitioner_harness/harness.py coord-check --diff <RANGE>`
  over the range covering the population and require exit 0. The command is
  report-only over a git diff range and checks citation resolution,
  decision-register coverage, named precedent presence where packet-shaped
  records call for it, and machine-absolute paths on diff-added lines — the
  mechanical part of "evidence and ruling references actually resolve".
- **VER-002** — Run `git log --format='%H %cI' -- <PRE_REGISTRATION_PATH>` and
  the same command for the evaluation report path, and require the
  pre-registration record's earliest commit to precede the report's earliest
  commit. This makes REQ-002's ordering claim checkable from history rather
  than asserted.

Both commands exist in the checkout at this basis and were observed to run
read-only. The timed retrieval exercise itself has no deterministic
implementation and must not acquire one: the covered scope statement holds
that the loop's closing step is a human judgment no agent can perform, so the
matrix records `HUMAN_REVIEW` with a named method.

## Governing Values and Decisions — Axiology

- **AX-001** — Pre-registration exists to make the usability result
  falsifiable. A threshold chosen after seeing results measures nothing, which
  is why REQ-002 fixes the ordering rather than the value.
- **AX-002** — Universal and sampled conditions are not interchangeable. A
  sampled pass cannot discharge a universal obligation, and a completeness
  defect is not mitigated by a favourable retrieval time.
- **AX-003** — The closing step stays human. Instrumentation may make evidence
  retrievable and time it; it may never render the evaluation judgment
  (SOW-009; PRD §4.2 [OWNER_DECLARED]).
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
| OUT-001 | SOW-009 OBJ-003 | REQ-001 REQ-003 CLM-002 | AC-001 AC-002 | VER-001 | The completeness check with its declared population boundary, per-change endpoint resolutions or recorded defects, and verbatim command output with its exit code. |
| OUT-002 | SOW-009 OBJ-003 | REQ-002 | AC-003 | VER-002 | The pre-registration record carrying the fixed threshold and sample, plus the captured history output showing its commit precedes the report's. |
| OUT-003 | SOW-009 OBJ-003 | REQ-002 CLM-001 | AC-004 AC-005 | HUMAN_REVIEW: timed retrieval exercise performed by the accountable human against the pre-registered threshold and tranche sample | The evaluation report measured against the pre-registered values only, with completeness and usability findings kept distinct and any deviation recorded as such. |
