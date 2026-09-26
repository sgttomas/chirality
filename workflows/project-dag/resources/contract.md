# project-dag — contract

## Authority

`docs/CONTRACT.md` K-DEP-1 and `docs/SPEC.md` §5.4, as amended by D-GOV-49,
govern this workflow:

- **Neither side is self-authorizing.** Authority comes from the human's
  acceptance, as with an accepted decomposition snapshot.
- **The local files are the evidence.** `_DEPENDENCIES.md` and
  `Dependencies.csv` hold human declarations and agent extractions. They may
  change at any time.
- **An accepted version is accepted evidence.** It is a snapshot of that
  evidence, selected for a stated objective and edge semantics, which the human
  reviewed and accepted. It carries authority only through its
  `ACCEPTANCE_RECORD.md`, and only while it is current with the evidence.
  Acceptance establishes reliance for sequencing and route selection; it does
  not satisfy a dependency or change lifecycle.
- **Provenance.** Every node traces to the accepted decomposition register;
  every edge, candidate, and exclusion traces to one local row by file path,
  file hash, and `DependencyID`. The version states the Git revision and
  evidence manifest it was assembled from.
- **Departures are decided, not absorbed.** When a local file departs from the
  accepted version (a new edge, a removed edge, or a cycle), neither side
  silently wins. A currency audit flags the DAG stale for the affected
  deliverables, which become `DAG pending`; a candidate new version is
  prepared; and the human accepts it or rejects the change. The flag clears on
  that decision. Unaffected work keeps using the accepted version. See
  [currency and departures](currency.md).
- **No silent rewriting.** This workflow writes no local file. Rows are copied
  from the local files into a version, and copied values are never edited to
  pass a check. A defect in a local file is repaired there by its owner. When a
  change is rejected, bringing the local file back in line is routed to its
  owner.
- **Blockers.** In a project with an accepted DAG, blockers come from the
  accepted current version, with satisfaction read from the local files; its
  held candidate edges are non-gating, and `DAG pending` deliverables get no
  ready or blocked verdict from dependencies. A project without an accepted
  DAG uses its recorded registers (SPEC §5.3).
- **Scope.** The Chirality repository has no cross-project dependency graph.
  This workflow builds one project's DAG. Development loops build work graphs
  (`construct-local-work-graph`) for a tranche of work within it.
- **Other arrangements.** Some project loops have adopted records that call
  their aggregate DAG the "dependency graph authority" and their local
  registers "synchronized mirrors". That wording is stronger than D-GOV-49,
  under which a DAG carries authority only through acceptance while it is
  current, and a departure is decided by the human rather than resolved in
  the DAG's favour. `audit_dag.py`'s generated markdown report carries
  similar fixed "synchronized mirrors" wording. This workflow neither adopts nor extends it. Such a loop keeps its
  own accepted records until its owning loop decides otherwise.

Human-owned sections of `_DEPENDENCIES.md` (tracking mode and declarations)
stay human-owned. Agent-owned content is changed only through
`dependency-extract` or the project's recorded evidence-maintenance method.

## Tracking-mode precondition

The project's tracking mode is recorded in `_COORDINATION.md` and in each
deliverable's Dependency Tracking Mode section (`docs/SPEC.md` §5.3, §13).

| Mode | Treatment |
|---|---|
| `NOT_TRACKED` | Not applicable. Report that the files do not hold the graph. Changing the mode is the human's coordination decision, normally recorded through `project-setup`. |
| `DECLARED` | A graph may be constructed from the recorded register as a **partial view** (`Completeness: PARTIAL_DECLARED`). An absent edge is not evidence of independence. Every output, the acceptance record, and the handoff carry that label. |
| `FULL_GRAPH` | The graph is intended to cover the selected semantics (`Completeness: FULL`). Missing, unreadable, or invalid registers are coverage defects to repair, or limitations the human accepts explicitly at a checkpoint. |

A legacy `TRACKED` value is read as `FULL_GRAPH`. Where deliverable-level mode
records disagree with the coordination record, report the disagreement as an
inventory finding for the human; do not choose a mode for them.

The graph is assembled from `Dependencies.csv`. Where the recorded evidence for
an in-scope deliverable exists only as declarations in `_DEPENDENCIES.md`, route
it to its owner so that the declarations are carried in `Dependencies.csv` as
`DECLARED`-origin rows (SPEC §5.3) before assembly. Do not synthesize rows from
Markdown inside the graph.

## Inputs (brief)

Required:

- `EXECUTION_ROOT` — the execution instance root (`docs/SPEC.md` §0.3).
- `TRIGGER` — `INITIAL` (first graph, normally toward 30%), `SUCCESSOR` (a
  departure found by a currency audit, a decomposition revision, or an
  accepted scope change), or `CURRENCY_AUDIT` (audit an accepted version only).
- Authorized write targets: `{DAG_ROOT}/` except `{DAG_ROOT}/cases/`, and, for
  currency audits, `{EXECUTION_ROOT}/_Evaluation/DAGCurrency/`. Dispatched
  child workflows use their own write boundaries; `scc-resolution-case` writes
  its case folder.

Optional (defaults shown):

- `DAG_ROOT` — `{EXECUTION_ROOT}/_DAG/`, the tool root registered in
  `docs/SPEC.md` §0.3 and §1.2. A project with an earlier adopted DAG location
  or pointer name keeps it; record which it uses.
- `CASE_HOME` — `{DAG_ROOT}/cases/`. A project that already holds its SCC
  cases in a PKG-00 control deliverable may keep that legacy home. Use one home
  per project; existing cases are not migrated.
- `SCOPE_INVENTORY_SOURCE` — the accepted `Deliverables.csv` resolved through
  `{DECOMP_ROOT}/checkpoint_snapshots/_LATEST_ACCEPTED.md`, or the accepted
  decomposition the brief names. Without an accepted register, stop and report;
  a folder listing is not an accepted inventory for this workflow.
- `EXEMPT_UNITS` — declared exemptions (for example `CONTROL` or `RETIRED`
  units), each with its class and the accepted authority declaring it, as in
  `audit-dep-closure`.
- `GRAPH_OBJECTIVE` — what the graph governs, for example production order for
  the next development phase. Drafted by the agent when absent and confirmed at
  checkpoint 1.
- `EDGE_SEMANTICS` — default: *the consumer requires the supplier's stated
  contribution, at the stated maturity, before the stated part of its work*.
- `SELECTION_RULES` — default rule set SR-1 to SR-7 in
  [graph-version rules](graph-version.md#selection-rules); adjustments are
  confirmed at checkpoint 1.
- `PRIOR_ACCEPTED` — the accepted version a successor replaces; default
  resolved through `{DAG_ROOT}/_LATEST.md`.
- `CURRENCY_REPORT` — the currency audit snapshot that found the departure,
  for a `SUCCESSOR` trigger.
- `CLOSURE_SNAPSHOT` — an existing `audit-dep-closure` snapshot to reuse when its
  input basis equals the frozen evidence manifest.

## Outputs and layout

```
{DAG_ROOT}/
  _LATEST.md                       accepted pointer (mutable; SPEC §11.2 form);
                                   names only an accepted version
  _Candidates/
    DAG-NNN/                       candidate being prepared; working record until
                                   accepted or rejected (a change after presentation
                                   requires re-presentation); immutable once accepted
                                   as a version; frozen once REJECTION_RECORD.md is
                                   written when the human rejects the change
  cases/
    <CASE-ID>/                     SCC resolution case (scc-resolution-case); working
                                   record keyed by its stable SCC-CASE-NNN identity
  DAG-NNN/                         accepted graph version; immutable once complete
    GRAPH_BASIS.md                 objective, semantics, direction, completeness,
                                   selection rules, rulings, limitations
    DeliverableNodes.csv           frozen node inventory
    DependencyEdges.csv            admitted sequencing edges
    CandidateEdges.csv             non-gating candidate layer
    ExcludedRows.csv               every other in-scope EXECUTION row, with reason
    SOURCE_MANIFEST.sha256         local-file and decomposition bytes at the basis
    SOURCE_BASIS.json              revision, closure snapshots, cases, tool fingerprints
    Evidence/                      audit JSON, Tool_Run.json, accounting
    REVIEW_PACKET.md               what checkpoint 2 decided, with presented hashes
    INDEPENDENT_REVIEW.md
    ACCEPTANCE_RECORD.md           the human decision and reliance boundary
    HANDOFF_STATE.md               handoff to construct-local-work-graph
    MANIFEST.sha256                hashes of every file in the snapshot
```

`DAG-NNN` is a stable, sequential graph identity (three digits). A number is
assigned when its candidate is opened and is never reused; a withdrawn or
rejected candidate keeps its number and records why. File contents are
defined in the [graph-version rules](graph-version.md#files).

`_DAG/_LATEST.md` is the accepted pointer; it never names a candidate, a
closure snapshot, or an audit. Closure observations stay under
`_Evaluation/DepClosure/` with their own `_LATEST.md`, and currency audits under
`_Evaluation/DAGCurrency/` with theirs.

The accepted pointer follows `docs/SPEC.md` §11.2:

```markdown
Latest: DAG-NNN
Updated: YYYY-MM-DD
Acceptance: DAG-NNN/ACCEPTANCE_RECORD.md
Completeness: FULL | PARTIAL_DECLARED
Basis revision: <40-hex commit>
Supersedes: DAG-MMM | (none)
```

Currency audits write
`{EXECUTION_ROOT}/_Evaluation/DAGCurrency/CURRENCY_{LABEL}_{YYYY-MM-DD}_{HHMM}/`
snapshots (created with `tools/scaffolding/create_snapshot_folder.sh`) and move
`_Evaluation/DAGCurrency/_LATEST.md`; they never modify an accepted version.
The latest currency audit lists the deliverables that are `DAG pending`.

## Non-negotiable invariants

- Authority as stated above; no local-file write by this workflow.
- The node inventory is frozen from accepted registers before edges are read;
  a deliverable without usable evidence remains a node with its evidence state
  recorded.
- The admitted edge set is acyclic, has one row per ordered arc, and passes
  `audit_dag.py --canonical --strict`.
- Every admitted and candidate row carries the 29 core v3.1 columns, matching
  its source row byte for byte, with provenance only in extension columns.
  `Explicitness`, `SatisfactionStatus`, and `Confidence` are non-blank
  canonical values (SPEC §5.4); a blank is completed at the local file, never
  in the version.
- Every `ACTIVE` `EXECUTION` row of every in-scope local file at the frozen
  basis appears in exactly one of `DependencyEdges.csv`, `CandidateEdges.csv`,
  or `ExcludedRows.csv`.
- Candidate edges are non-gating. They cannot drive blocker queues, wave
  placement, schedules, dispatch readiness, or readiness claims
  (`docs/CYCLE_DRIVEN_RESOLUTION.md` §2 rule 4). Holding a candidate does not
  make the affected work ready. Every candidate held for an unresolved SCC
  cites its case in the project's case home.
- A departure makes the affected deliverables `DAG pending` until the human
  decides; neither the accepted version nor the local file is treated as
  having won.
- Cut and merge rulings are human decisions, recorded with evidence; decompose
  and invert remedies are applied by their owner workflows, never in the graph.
- A snapshot is immutable once complete. The accepted pointer moves only after
  the accepted snapshot and its manifest are complete, and only to a version
  the human accepted. Reopened decisions create successors.
- Unknowns remain `TBD` and visible; limitations are stated, not smoothed over.

## Validity

A graph version is valid for acceptance when:

- the tracking-mode precondition is met and the completeness label is correct;
- the inventory source, exemptions, evidence manifest, and Git revision are
  recorded, and the closure snapshot used was computed on that same manifest;
- `audit_dag.py --canonical --strict` exits 0 on the admitted edges with
  `Tool_Run.json` recording the tool hash, arguments, and exit code, so the
  fields SPEC §5.4 requires are present and canonical;
- row accounting balances and byte fidelity holds;
- every candidate edge cites its SCC and its case in the project's case home,
  or its selection rule and open question; every exclusion cites its rule or ruling;
- an independent review by an instance that did not assemble the graph has no
  unresolved blocking finding, or its remaining findings are presented;
- limitations, held work, and open questions are stated in `GRAPH_BASIS.md`.

An accepted version additionally has `ACCEPTANCE_RECORD.md` with the human's
decision as given, `HANDOFF_STATE.md`, a complete `MANIFEST.sha256` whose
graph files match the hashes presented at checkpoint 2, and an accepted
pointer naming it.

## Relationship to other methods

| Method | Relationship |
|---|---|
| `project-setup` | Phase 2.2b extracts dependency evidence and runs closure; it hands off here when the project needs an accepted DAG. |
| `dependency-extract` | Owns the agent-extracted evidence rows. Reused, not duplicated, for coverage, canonicalization, declared-row mirroring, and remedies. |
| `audit-dep-closure` | Owns closure analysis and its observation pointer. Its snapshot is evidence for checkpoint 1, not the accepted graph. |
| `scc-resolution-case` | Holds evidence and rulings for coupled work in the project's case home: `_DAG/cases/<CASE-ID>/`, or a legacy PKG-00 control deliverable. |
| `scope-change` | Owns decomposition and accepted-scope amendments, including decompose remedies and merges that change the decomposition. An accepted DAG is one of its derivative packages. |
| `construct-local-work-graph` | Builds a development loop's work graph for a tranche of work within the accepted current version, respecting `DAG pending`. |
| Scheduling in `project-setup` | May use the accepted version as a sequencing input; a DAG is not a schedule. |
