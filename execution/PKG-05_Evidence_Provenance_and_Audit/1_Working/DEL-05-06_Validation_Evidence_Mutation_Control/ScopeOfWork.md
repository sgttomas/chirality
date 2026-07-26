---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-05-06
package_id: PKG-05
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-057]
package_objective_refs: [OBJ-004]
---

# Scope of Work — DEL-05-06

## Purpose and Objective Traceability

This deliverable keeps validation evidence written only under declared
generated paths under the mutation-control contract, keeps the harness from
writing governed authority files, and keeps governed-file mutation by a
validation command an unconditional BLOCK. That purpose is transcribed from
the deliverable register row for DEL-05-06 (`Type: SECURITY_CONTROL`,
`ContextEnvelope: M`) and from the deliverable's `_CONTEXT.md`.

The single covered project scope item is **SOW-057**: "Validation evidence is
written only under declared generated paths under the mutation-control
contract, the harness never writes governed authority files, and governed-file
mutation by a validation command is an unconditional BLOCK." Its `SourceRef`
is `PRD §5.4 E-6 [TRANSCRIBED]`, whose label and source line names D-GOV-01
and the harness phase-4 record in `_REGISTER.md`.

The supported package objective is **OBJ-004** — safe self-application without
self-authorization: falsifiers F1–F3 unobserved, every root capability
consumed by root development accepted through the basis or an explicitly
accepted predecessor, and G0–G4 registered and passing at every
materialization. A validation command that could write governed authority
files would be exactly the self-authorization route OBJ-004 forbids, which is
why this control is scoped as evidence rather than as advice.

The deliverable's `_CONTEXT.md` records `Acceptance Criteria: TBD — the
accepted decomposition states no per-deliverable acceptance criteria`. The
criteria below are therefore **candidate** definitions authored from the
grounding sources only. They claim no acceptance and no lifecycle transition.

## Deliverable Definition — Ontology

The register's `AnticipatedArtifacts` field and the `_CONTEXT.md
## Anticipated Artifacts` list name two artifacts, which become the two
expected outputs.

- **OUT-001** — Mutation-control conformance evidence: a record showing, for
  observed validation runs, where evidence was written, that no governed
  authority file was written by the harness, and how governed-file mutation by
  a validation command is treated.
- **OUT-002** — Generated-path containment tests: the executed test surface
  that exercises the containment and BLOCK behavior, with its captured result
  and exit code.

- **CLM-001** — The register's `ContextEnvelopeNotes` for this deliverable
  state "One control with existing fail-closed machinery." The scope is
  therefore conformance evidence over machinery that already exists, not the
  design of a new control and not a change to the control's implementation.
- **CLM-002** — Structural conformance observed by these outputs is evidence
  about the substrate, never approval of any change and never authentication
  of any claim. A passing run is a fact, not a permission.

## Completion and Reliance Basis — Epistemology

The three obligations below are the three conjuncts of the covered scope
statement, restated without extension.

- **REQ-001** — Validation evidence shall be written only under declared
  generated paths, under the mutation-control contract (SOW-057, first
  conjunct; `SourceRef` PRD §5.4 E-6 [TRANSCRIBED]).
- **REQ-002** — The harness shall never write governed authority files
  (SOW-057, second conjunct; same `SourceRef`).
- **REQ-003** — Governed-file mutation by a validation command shall be an
  unconditional BLOCK (SOW-057, third conjunct; same `SourceRef`). The word
  "unconditional" is load-bearing: no declaration authored by an agent may
  narrow it.

Candidate acceptance criteria:

- **AC-001** — The conformance evidence addresses each of the three conjuncts
  of SOW-057 separately, and cites for each the observed output or file that
  demonstrates it, rather than asserting the conjunct in prose.
- **AC-002** — For every validation run exercised by the containment test
  surface, that run's recorded `changed_paths` accounts for every path the run
  wrote: a path under a declared generated path is recorded as such, and any
  path that is not is recorded with its classification, never omitted or
  summarized away. The evidence cites those executed assertions and their exit
  code, rather than asserting containment in prose. The criterion is scoped to
  the runs that surface exercises because that is the only surface named here
  that executes a validation run at all; extending it to arbitrary observed
  runs would demand an observation no method bound below can make.
- **AC-003** — The containment test surface is executed, its exit code is 0,
  and its captured output is included in the evidence.
- **AC-004** — The evidence states explicitly whether the governed-file
  mutation BLOCK was observed as unconditional, and records any observed
  detection boundary as a stated limit rather than leaving it implicit.

Reliance basis: these outputs establish that the control behaved as specified
on the runs observed. The runs observed under AC-002 are the runs the
containment test surface constructs and executes; production runs against a
live brief are not observed by any method named here, and that gap is a stated
limit of this contract rather than a silent assumption. They do not establish
that the substrate is globally safe. Evidence completeness is never evidence sufficiency, and a BLOCK never
means globally proven safe or unsafe.

## Production and Verification Method — Praxeology

Production executes the deterministic surfaces below against the checkout and
captures their output verbatim, including exit codes.

- **VER-001** — Run `python3 -m pytest tools/practitioner_harness/test_run_validations.py`
  and require exit 0. This is the executable test surface for the
  `run-validations` mutation-control behavior; at this basis it reports
  20 passing tests. Its cases construct validation runs, execute them, and
  assert the per-path `changed_paths` classification each run records —
  including the governed-file mutation BLOCK and the classification of paths
  outside the declared generated root. It is therefore the only method named
  here under which a written path can be observed at all.
- **VER-002** — Run `python3 tools/practitioner_harness/harness.py run-validations --brief <BRIEF> --list`
  for the brief under observation. `--list` resolves and prints the declared
  command list and stops: nothing is executed and nothing is written, so the
  declared command set can be recorded without side effects.
- **VER-003** — Run `python3 tools/validation/validate_root_harness_adapter.py`
  and require exit 0. This is the G1 guard over the root harness adapter
  manifest; at this basis it reports the manifest schema-valid and its pinned
  baselines matching the observed tree.

All three commands exist in the checkout at this basis and were observed to
run. No verification method here is invented, and none is a substitute for the
human judgment that decides reliance.

## Governing Values and Decisions — Axiology

- **AX-001** — Fail closed. PRD §5.3 D-5 records that validation is
  deterministic and severity-typed, that "BLOCK" never means globally proven
  safe or unsafe, and that a validator finding may never mechanically reject
  owner-ruled content. Evidence produced under this contract reports; it does
  not adjudicate.
- **AX-002** — Write containment is architectural, not advisory. PRD §5.1 N-5
  records that every agent has an explicit declared write scope, that every
  scope path and write target resolves under the active checkout or the task
  stops, and that task outputs to tool roots are immutable snapshots. A
  validation command that wrote governed files would break that architecture
  rather than bend it.
- **AX-003** — The `AnticipatedWriteLocus` recorded for this deliverable is
  "tools/ (M2); execution-tree for evidence". That is a planning note, not
  authorization. Any act touching the instruction surface — `AGENTS.md`,
  `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, or
  `.github/workflows/` — requires an independently authorized M2 tranche.
  **This Scope of Work grants none.** Work under this contract produces
  evidence in the execution tree only; if the evidence shows the control
  itself must change, that is surfaced and routed, never applied here.
- **AX-004** — Evidence is not acceptance. Producing these outputs performs no
  lifecycle transition; the deliverable's state remains `OPEN`, as do all root
  deliverable states at this basis. The criteria above are candidates for
  owner review, and `ResponsibleParty` remains unassigned in the register and
  is not altered by this contract.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-057 OBJ-004 | REQ-001 REQ-002 REQ-003 CLM-001 | AC-001 AC-002 AC-004 | VER-001 VER-002 VER-003 | The conformance record, carrying the resolved declared command list, the per-path write classification recorded by each executed run, an explicit statement on the unconditional BLOCK, and verbatim command output with exit codes. |
| OUT-002 | SOW-057 OBJ-004 | REQ-003 CLM-002 | AC-003 | VER-001 | The captured test-surface result: command line, exit code, pass count, and full output, retained alongside the conformance record. |
