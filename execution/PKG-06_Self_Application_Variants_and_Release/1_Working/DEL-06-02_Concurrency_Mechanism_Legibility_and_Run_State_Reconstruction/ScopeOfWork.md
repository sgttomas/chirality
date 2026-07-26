---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-02
package_id: PKG-06
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-065, SOW-066]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-06-02

## Purpose and Objective Traceability

DEL-06-02 (`OBSERVABILITY`) serves project scope SOW-065 and SOW-066 and
package objective OBJ-006. Its purpose, transcribed from the accepted
deliverable register, is to demonstrate that concurrent root-product activity
stays legible: write ownership disjoint or serialized, a frozen instruction
basis per run, worktree isolation, and pre-dispatch work-graph validation, with
every run's ownership, dependencies, and pending gates reconstructible and
stale or orphaned runs detectable.

OBJ-006 in `docs/PRD_ROOT.md` §3 is "coordination remains intelligible as
concurrent activity grows", and it fixes the observation population explicitly:
root-product development runs — the run records under this loop's
`execution/_Coordination/`. Situated working roots' coordination remains their
own surface and is out of scope; the PRD states that any future aggregated
cross-root coordination layer would be a new product function, not implied by
this objective. This deliverable observes that population; it does not build,
own, or modify the mechanisms it observes.

Every definition below is grounded in the deliverable-register row for
DEL-06-02, this deliverable's `_CONTEXT.md`, the scope-ledger statements for
SOW-065 and SOW-066, and the adopted `docs/PRD_ROOT.md`. Acceptance criteria
and verification methods are **candidates for owner review**; this contract
claims no acceptance and no lifecycle state.

## Deliverable Definition — Ontology

The three anticipated artifacts transcribed from the register
(`AnticipatedArtifacts`) and from `_CONTEXT.md ## Anticipated Artifacts` are:

- **OUT-001** — Run-state reconstruction report: for each run record in the
  declared population, whether its declared write ownership, its dependencies,
  and its pending gates are reconstructible from recorded state alone.
- **OUT-002** — Stale/orphan detection method: a stated, repeatable method that
  distinguishes interrupted, abandoned, or crashed runs from live ones, applied
  across the same population with its results recorded.
- **OUT-003** — Work-graph-before-dispatch evidence: evidence that work graphs
  are recorded before dispatch rather than after, and that concurrently active
  nodes' declared write targets are disjoint or serialized.

- **CLM-001** — SOW-065 (SourceRef `PRD §6.3 [TRANSCRIBED]`, DecisionRef
  DEC-008) records four accepted mechanisms that make concurrent root
  development safe: fine-grained write ownership with disjoint or serialized
  targets; a frozen instruction basis per run, so an in-flight run never
  consumes a sibling's candidate instruction change; worktree isolation for
  concurrent children; and a pre-dispatch work-graph check validating declared
  and disjoint write targets before dispatch.
- **CLM-002** — The scope-ledger note on SOW-065 records that the mechanisms'
  state surfaces are instantiated in PKG-03; this unit owns the concurrency-
  safety *relation*, not those surfaces. `_CONTEXT.md` restates this as
  "observation over the run-record population; the mechanisms' state surfaces
  are owned elsewhere". Nothing in this contract authorizes creating or
  modifying a mechanism state surface.
- **CLM-003** — SOW-066 (SourceRef `PRD §6.3 [CLARIFIED]`) records that
  legibility of concurrent work is a property of declared, file-recorded write
  ownership — not of coordination held in conversation. The PRD states the
  corresponding OBJ-6 condition that no run's effect is discoverable only from
  chat history.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — Per SOW-066, the reconstruction report shall be produced from
  file-recorded coordination state alone. Any finding that depends on chat
  history, agent recollection, or a live session is recorded as a
  reconstruction **failure** for that run, not as a satisfied condition.
- **REQ-002** — Per SOW-066, the observed population shall be stated explicitly
  as the run records under this loop's `execution/_Coordination/`, and each
  record in that population shall appear in the report exactly once, including
  records that fail reconstruction.
- **REQ-003** — Per SOW-065, the report shall record, per run, whether declared
  write targets exist and whether concurrently active siblings' targets are
  disjoint or serialized; an undeclared write target is a finding, not an
  omission to be filled in.
- **REQ-004** — Per SOW-066, the stale/orphan detection method shall be stated
  before it is applied, shall be repeatable by another party from the statement
  alone, and shall classify every run in the population as live, complete,
  stale, or orphaned with the evidence for that classification named.
- **REQ-005** — Per SOW-065, work-graph evidence shall show recording **before**
  dispatch; an ordering that cannot be established from recorded state is
  reported as indeterminate rather than assumed compliant.
- **CON-001** — The four mechanisms of CLM-001 include a frozen instruction
  basis per run and worktree isolation. Where the population contains runs
  predating the state surfaces that would evidence those two mechanisms
  (CLM-002), the report records the gap as a population-coverage limit rather
  than as a mechanism failure or a pass.
- **CON-002** — The population **predicate** is unresolved and its resolution is
  an owner act. REQ-002 and PRD OBJ-6 both scope the population to root-product
  development runs "under this loop's `execution/_Coordination/`", but neither
  they, the SOW-065/SOW-066 ledger rows, nor the PRD state a rule for deciding
  which files satisfy that description. Observed at the recorded basis:
  `git ls-files 'execution/_Coordination/**/_run_records/*.md'` returns **6084**
  files; all 6084 lie inside exactly two run trees —
  `AgentRuns/SOW-STAGE2-EXEC-20260712-01/` (5700) and
  `AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/` (384) — and every one is
  nested under `.../instances/...` as a per-member or per-workspace task record
  of batch and simulation corpora, at least 1600 of which record a `scope-path`
  belonging to a different project (`chirality-piping`). This loop's own
  root-product run trees under `execution/_Coordination/AgentRuns/ROOT-*-20260725/`
  contain no `_run_records/` directory at all. The literal enumeration is
  therefore over-broad against OBJ-6, and no narrowed enumeration is derivable
  from the authorized grounding sources without inventing a predicate they do
  not state (K-INVENT-1, K-CONFLICT-1). The predicate is recorded here for owner
  ruling and is not settled by this contract.

- **AC-001** — The reconstruction report covers every run record in the stated
  population exactly once and records, per run, a determinate verdict on each
  of the three reconstruction subjects — declared write ownership,
  dependencies, and pending gates — using file-recorded state only.
- **AC-002** — The stale/orphan detection method is stated before application,
  is repeatable from its own statement, and yields a classification for every
  run in the population with named evidence, with no run left
  indistinguishable between live and abandoned.
- **AC-003** — The work-graph evidence establishes, per dispatched node, that
  the work graph was recorded before dispatch and that concurrently active
  nodes' declared write targets were disjoint or serialized, or reports the
  case as indeterminate with the missing record named.

## Production and Verification Method — Praxeology

Production enumerates the run-record population under
`execution/_Coordination/`, reads each record's declared write targets,
dependencies, and gate state, and compares them against the work-graph and
surface-ownership surfaces under `execution/_harness/`. It writes only within
this deliverable folder. It does not modify any run record, coordination
record, or harness state surface; all three are read-only inputs.

No deterministic verification is defined for OUT-001, because the population it
would enumerate is not yet determined. Reconciling the report against a file set
is only as sound as the predicate that produces that file set, and CON-002
records that the predicate is an owner call: the literal enumeration returns 6084
records that OBJ-6 does not describe, and no narrower one is derivable from the
authorized grounding sources. Naming a command here would fix a population this
contract has no authority to fix, so OUT-001 carries named human review until the
predicate is ruled. Once it is, the reconciliation it names is deterministic.

- **VER-002** — Execute `python3
  tools/validation/validate_root_work_graph_dispatch.py` (G3, the pre-dispatch
  work-graph check over `execution/_harness/work_graph.yaml`) and `python3
  tools/validation/validate_root_surface_ownership.py` (G2, the static
  surface-ownership register over
  `execution/_harness/surface_ownership.yaml`), and record each exit status and
  message as evidence for the declared-and-disjoint write-target findings. A
  guard result is evidence; it is not the report's verdict.

## Governing Values and Decisions — Axiology

- **AX-001** — Legibility is a file property. Per SOW-066, coordination held in
  conversation does not count as recorded state; the observation therefore runs
  from the checkout alone and treats any conversational dependency as a defect
  to report.
- **AX-002** — Observe, do not own. Per CLM-002 and the `_CONTEXT.md`
  envelope note, the mechanisms' state surfaces are owned elsewhere (PKG-03).
  This deliverable reports on them and never repairs, backfills, or
  instantiates them.
- **AX-003** — Population honesty. Per the PRD's OBJ-6 boundary, the population
  is this loop's own run records; situated working roots are out of scope and
  are not silently included to improve a result.
- **AX-004** — This deliverable's `AnticipatedWriteLocus` is `execution-tree`
  and this contract grants no instruction-surface authority. Any act that would
  change `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, or
  `.github/workflows/` requires an independently authorized M2 tranche, which
  this contract does not grant.
- **AX-005** — Nothing is inferred where the accepted decomposition is silent
  (K-INVENT-1). `_CONTEXT.md ## Acceptance Criteria` records `TBD`; AC-001
  through AC-003 are candidate criteria derived only from the authorized
  grounding sources and remain subject to owner review.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-065 SOW-066 OBJ-006 | CLM-001 CLM-003 REQ-001 REQ-002 REQ-003 CON-001 CON-002 | AC-001 | HUMAN_REVIEW: owner rules on the CON-002 population predicate — which files under `execution/_Coordination/` are root-product development runs for OBJ-6 — then reads the reconstruction report against the enumeration that ruled predicate produces and records that the report's row set equals it with no addition, omission, or duplicate, and that each row carries a determinate verdict on all three reconstruction subjects | Recorded population predicate as ruled, the enumeration it produces, the reconstruction report, and the reviewer's recorded reconciliation and disposition |
| OUT-002 | SOW-066 OBJ-006 | REQ-002 REQ-004 | AC-002 | HUMAN_REVIEW: owner reads the stated detection method before its results and confirms it is repeatable from its own statement and classifies every run in the declared population | Method statement dated before application, the resulting classification table, and the reviewer's recorded disposition |
| OUT-003 | SOW-065 OBJ-006 | CLM-001 CLM-002 REQ-003 REQ-005 | AC-003 | VER-002 | Work-graph-before-dispatch evidence plus captured G2 and G3 guard exit status and messages at the stated basis |
