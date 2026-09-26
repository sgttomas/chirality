# project-dag — method

WORKING_ITEMS carries each stage forward and integrates the returns. Bounded
contributions go to TASK through the named workflows or through briefs that
carry the [graph-version rules](graph-version.md). Record actual briefs,
returns, input revisions, and tool fingerprints so the graph can be reproduced
and its preparation inspected.

## Stage 0 — Precondition and trigger

1. Read `{COORDINATION_ROOT}/_COORDINATION.md` for the coordination
   representation and tracking mode, and apply the
   [tracking-mode precondition](contract.md#tracking-mode-precondition).
2. Resolve the accepted decomposition through
   `{DECOMP_ROOT}/checkpoint_snapshots/_LATEST_ACCEPTED.md` or the brief. Without
   one, stop: an accepted DAG needs an accepted node basis.
3. Resolve any accepted version through `{DAG_ROOT}/_LATEST.md` or the
   project's adopted pointer, any open candidate under `_Candidates/`, and the
   latest currency audit through `_Evaluation/DAGCurrency/_LATEST.md`.
4. Establish the trigger. For `CURRENCY_AUDIT`, go to
   [currency and departures](currency.md). For `SUCCESSOR`, identify the
   change event (a departure found by a currency audit, a decomposition
   revision, or an accepted scope change), the `DAG pending` deliverables, and
   the decisions it can affect. A current accepted version with no such event
   is reported as current; do not rebuild it.
5. Resolve the project's SCC case home. The default is `{DAG_ROOT}/cases/`,
   registered in SPEC §1.2, with one `<CASE-ID>/` folder per case. A project whose cases are already held in a PKG-00
   control deliverable may keep that legacy home. Use one home per project,
   and record which one. Existing cases are not migrated.

## Stage 1 — Frozen inventory and objective

1. Build the node inventory from `SCOPE_INVENTORY_SOURCE`, less declared
   exemptions. Compare it with the workspace folders. Report accepted units
   without a folder and folders without an accepted row as inventory findings.
2. Record each unit's register state and deliverable-level tracking mode.
3. Draft the graph objective, edge semantics, direction convention, completeness
   label, and selection rules. Start from the contract defaults and the
   project's recorded dependency rules (`project-setup` Phase 1.3). State any
   departure and its reason: for example, excluding a `DependencyType` from a
   production-order graph, or proposing a confirmation hold.
4. Open the candidate folder `{DAG_ROOT}/_Candidates/DAG-NNN/` with the next
   unused number. For a successor, record the predecessor and the change event.

## Stage 2 — Register coverage and closure

1. Identify local files needing their owner's work: missing `Dependencies.csv`
   where extraction is called for; files stale against changed sources;
   non-canonical values; declarations not yet carried as `DECLARED`-origin rows;
   long-form IDs; blank `Explicitness`, `SatisfactionStatus`, or `Confidence`
   values, which an accepted version requires (SPEC §5.4). Dispatch
   TASK + `dependency-extract`, one deliverable per brief,
   with the mode the defect needs (`UPDATE`, `CANONICALIZE_EXISTING`, or, only
   when a brief records that the prior extraction is unreliable,
   `RESET_EXTRACTED`). Human-owned declarations are the human's to change.
2. When the local files are settled, freeze the basis: record the Git revision
   and write `SOURCE_MANIFEST.sha256` into the candidate folder.
3. Dispatch TASK + `audit-dep-closure` over the frozen inventory, with
   `SCOPE_INVENTORY_SOURCE`, `EXEMPT_UNITS`, and `UPDATE_LATEST_POINTER` as the
   brief sets. Reuse `CLOSURE_SNAPSHOT` instead when its recorded input basis
   equals the frozen manifest.
4. Read the closure report. Separate coverage defects (missing or invalid
   files, unresolved targets) from topology findings (SCCs, bidirectional
   pairs, hubs, isolated nodes). Route coverage defects back to step 1. Any
   change to a local file re-freezes the manifest and requires a new closure
   run.

## Checkpoint 1 — Basis

Prepare a decision package containing:

- the objective, edge semantics, direction convention, completeness label, and
  selection rules, with each departure from the defaults explained;
- the frozen inventory, exemptions with their authority, and inventory findings;
- evidence coverage, remaining defects, and the limitation each would impose
  if accepted as is;
- the closure snapshot and each SCC or bidirectional pair, with proposed
  treatment. Obvious decompose or invert refinements carry a one-line note and
  their owner workflow. Cut or merge proposals, and contested or
  objective-dependent treatments, carry a decision packet: the relationship,
  evidence, proposed treatment, and consequences;
- which SCCs the manager proposes to resolve before acceptance and which to
  hold as candidates, with the work each hold would leave without an input.

The human confirms or adjusts the basis, rules on any ready cut or merge,
accepts or rejects coverage limitations, and directs the SCC plan. Record the
decision as given. A rejected element returns to the stage that prepared it.

## Stage 3 — Resolve or hold coupled work

1. For each SCC needing more than a one-line note, dispatch
   `scc-resolution-case` to open or update its case in the project's case home
   (`{DAG_ROOT}/cases/<CASE-ID>/` by default). Supply the closure snapshot,
   its SCC ID and member node set, affected deliverables, and any seed packets.
   The case workflow matches the SCC to an existing case by member node set
   before opening a new `SCC-CASE-NNN`. Its brief states that case
   work does not change local files or claim closure.
2. Commission bounded TASK inquiries the case needs: interface inspection,
   tracing a disputed dependency, or testing a proposed refinement. Consequential
   product questions return to the human through the design relationship.
3. Route accepted remedies to their owners. `scope-change` handles
   decomposition changes and merges that alter the decomposition. `scope-of-work`
   or the project's contract method handles production contracts.
   `dependency-extract` refreshes the affected local files. Record cut and merge
   rulings in the case's `Ruling_Register.csv` or the project's decision
   register; they enter the graph through SR-4.
4. After remedies are applied, re-freeze the manifest and rerun closure. A case
   closes only on a cited closure result. Iterate while resolution is directed
   before acceptance; remaining unresolved SCCs are held as candidates, each
   citing its case.

## Stage 4 — Assemble and review

1. Dispatch one TASK to assemble the candidate by the
   [graph-version rules](graph-version.md) against the frozen manifest, the
   confirmed rules, and recorded rulings.
2. Resolve mechanical findings by repairing assembly or by routing defects in
   local files to their owners. A repair moves the basis, so return to Stage
   2's freeze and closure steps.
3. Dispatch a separate TASK instance for the independent review. Repair
   mechanical findings; carry substantive ones to checkpoint 2.
4. Write `REVIEW_PACKET.md` with the SHA-256 of every graph file being
   presented.

## Checkpoint 2 — Acceptance

Present:

- the graph identity and basis;
- node and edge counts;
- the `audit_dag.py` result and the accounting summary;
- the candidate layer, by SCC or confirmation hold, with the case, what would
  resolve it, and the work lacking its input;
- exclusions by disposition, especially those still relevant to readiness;
- mirror conflicts and findings in local files routed to their owners;
- the independent review and its open findings;
- any tool-strictness exceptions;
- limitations and the completeness label;
- the proposed handoff and reliance boundary.

The human accepts the version, accepts it with stated qualifications for a
stated scope, or returns identified parts for repair. For a successor prepared
because of a departure, the human may instead reject the change; record it as
[currency and departures](currency.md#deciding-a-departure) describes. A change to the presented
graph after the decision reopens the affected checks and requires a new
presentation of the changed parts.

For a small undertaking where no SCC needs a ruling, the human may decide
checkpoints 1 and 2 together. Prepare checkpoint 2's package on the proposed
basis, complete the independent review first, and record that the decision
covers both.

## Stage 5 — Publish and hand off

1. Create `{DAG_ROOT}/DAG-NNN/` containing the presented files byte for byte;
   verify them against the `REVIEW_PACKET.md` hashes.
2. Add `ACCEPTANCE_RECORD.md`: the question and the human's decision as given,
   with date, actor, and relay provenance. Include qualifications and the
   reliance boundary: what the version may be relied on for while it is
   current, and what remains separate (dependency satisfaction, lifecycle,
   holds, the 30% gate, schedule).
3. Add `HANDOFF_STATE.md` for `construct-local-work-graph` and other consumers:
   - accepted identity and pointer;
   - objective, semantics, direction, and completeness label;
   - the reading rule: blockers from the accepted current version's edges;
     required contributions and satisfaction from the live local files,
     including rows listed as `MIRROR` or `SAME_ARC`; deliverables listed
     `DAG pending` by the latest currency audit get no ready or blocked
     verdict from dependencies until the human decides;
   - candidate edges held and non-gating, with the work lacking their inputs;
   - exclusions still relevant to readiness;
   - the currency audit command, where its latest result is found, and the
     events that call for one;
   - open matters.
4. Write `MANIFEST.sha256` over every file in the snapshot; the snapshot is then
   immutable.
5. Update `{DAG_ROOT}/_LATEST.md` (or the project's adopted pointer). Name the
   superseded version, which remains as history with its decisions. Run a
   currency audit against the new version, so that the deliverables its
   acceptance decided are no longer listed `DAG pending`.
6. Report the accepted pointer to the loop that routes through it. A project
   whose `_COORDINATION.md` notes locate the accepted graph keeps those
   human-owned notes current through the human.

## Recovery and interruption

- Resume from what exists: the candidate folder, closure snapshots, case states,
  review packet, and pointer. Do not treat a candidate, a closure snapshot, a
  currency audit, or the `_LATEST.md` pointer of `_Evaluation/DepClosure/` or
  `_Evaluation/DAGCurrency/` as the accepted version.
- If the manifest no longer verifies, the basis moved. Re-freeze, rerun closure,
  and reopen only the decisions whose rows changed.
- If an accepted snapshot is incomplete (no `MANIFEST.sha256`, or the pointer not
  yet moved), complete it from the presented hashes. If the bytes cannot be
  reproduced, withdraw it and present again.
- A withdrawn or superseded candidate keeps its number and records why.
- Unresolved questions stay `TBD` in `GRAPH_BASIS.md` with their owner. They do
  not stop independent authorized work.
