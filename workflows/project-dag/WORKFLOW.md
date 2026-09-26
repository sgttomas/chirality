---
name: project-dag
description: Construct, examine, and obtain human acceptance of a project DAG version from the deliverable-local dependency evidence, audit its currency when that evidence changes, and hold affected deliverables as DAG pending until the human accepts a successor or rejects the change. Use it toward the 30% gate, after a decomposition or scope change, or when local dependency files may have departed from the accepted DAG.
---

# Construct and accept the project DAG

Use this method when a project in `DECLARED` or `FULL_GRAPH` dependency
tracking needs an identified, examined, and accepted project DAG: the
production-order graph for the project as a whole, within which development
loops build their local work graphs. It produces a graph version with its
objective, edge semantics, node inventory, admitted edges, a non-gating
candidate layer, exclusions, evidence provenance, audit results, and the
human's acceptance record. It then hands the accepted version to
`construct-local-work-graph` and keeps it current.

Under `docs/CONTRACT.md` K-DEP-1 and `docs/SPEC.md` §5.4 (D-GOV-49), neither
the DAG nor the local files is self-authorizing. The deliverable-local
`_DEPENDENCIES.md` and `Dependencies.csv` files are the dependency evidence and
may change at any time. An accepted version is a snapshot of that evidence that
the human reviewed and accepted; it carries authority only through its
acceptance record, and only while it is current with the evidence. When a local
file departs from it, neither side silently wins: a currency audit flags the
affected deliverables `DAG pending`, a candidate version is prepared, and the
human accepts it or rejects the change. The
[contract](resources/contract.md#authority) states the rule and its
consequences.

WORKING_ITEMS coordinates the undertaking and integrates contributions.
Extraction, closure analysis, SCC case records, graph assembly, independent
review, and currency audits are bounded TASK assignments. TASK does not
delegate. HELP_HUMAN may coordinate a request for this workflow; execution
routes to an eligible WORKING_ITEMS instance with actual host permissions and a
run-specific brief. Selection grants no permissions and does not launch work.

## Method

1. **Establish the precondition and trigger.** Read the recorded tracking mode.
   `NOT_TRACKED` does not support a project DAG; stop and report. `DECLARED`
   yields a version labelled as a partial view. Resolve the accepted
   decomposition, the accepted version through `_DAG/_LATEST.md`, any open
   candidate, and the latest currency audit. When the accepted version passes
   its currency audit and no departure or decomposition change has occurred,
   report it as current and stop; a new session is not a reason to rebuild.
2. **Freeze the inventory and draft the objective.** Derive the node inventory
   from the accepted decomposition registers independently of the dependency
   files. Draft the graph objective, edge semantics, direction convention,
   completeness posture, and selection rules.
3. **Bring the evidence to a usable state and examine closure.** Reuse
   `dependency-extract` for missing, stale, non-canonical, or incomplete local
   files, one deliverable per brief. Freeze the evidence manifest, then run
   `audit-dep-closure` over the frozen inventory. Route defects to the owners
   of the local files and re-freeze after any change.
4. **Checkpoint 1: basis.** Present the objective, semantics, selection rules,
   inventory and exemptions, coverage and its limitations, and each SCC with
   its proposed treatment. The human confirms or adjusts them and rules on
   any cut or merge that is ready.
5. **Resolve or hold coupled work.** Open or update an `scc-resolution-case`
   for each SCC that needs more than a one-line note, in the project's case
   home: `_DAG/cases/<CASE-ID>/`, or its legacy PKG-00 control deliverable
   where it already holds its cases. A case keeps its own stable ID; an SCC
   from a later closure run is matched to it by member node set. Owner
   workflows apply accepted remedies to decomposition, contracts, and local
   files; rerun closure on the changed evidence. SCCs still unresolved are
   held in the candidate layer, each citing its case.
6. **Assemble and check the graph version.** A TASK assembles the candidate
   by the [graph-version rules](resources/graph-version.md), accounts for every
   in-scope execution row, and runs `audit_dag.py --canonical --strict`, which
   enforces the fields SPEC §5.4 requires. A separate TASK instance
   independently reviews the result.
7. **Checkpoint 2: acceptance.** Present the audited, reviewed graph version,
   its candidate layer, exclusions, limitations, and the proposed handoff. The
   human accepts it, accepts it with stated qualifications, or returns parts
   for repair.
8. **Publish and hand off.** Write the immutable accepted snapshot matching the
   presented hashes, then move `_DAG/_LATEST.md`. Hand the version to
   `construct-local-work-graph` with its reliance boundary.
9. **Audit currency and decide departures.** Audit the accepted version against
   the local files when a consumer relies on it or a change event occurs. A
   departure flags the affected deliverables `DAG pending`; prepare a
   candidate successor for those decisions only, and present it. The human
   accepts it or rejects the change, which clears the flag.

Agents carry authorized preparation forward on their own initiative and present
each checkpoint only after its proposal and checks are ready. Deterministic
findings route repair work; they do not add a human prompt by themselves. For a
small undertaking with no SCC needing a ruling, the human may decide both
checkpoints in one sitting after the independent review.

Acceptance of a version does not pass the 30% gate, change deliverable
lifecycle, satisfy a dependency, or lift a hold. Those remain separate acts.

## Resources

Load the [contract](resources/contract.md) when framing the assignment:
authority under K-DEP-1 and SPEC §5.4, inputs, the `_DAG/` layout, outputs, and
validity. Use the [method](resources/method.md) for stage-by-stage preparation,
checkpoints, recovery, and handoff. Supply the
[graph-version rules](resources/graph-version.md) in the assembly and review
briefs; they define the files, required fields, selection rules, candidate
layer, accounting, and the `audit_dag.py` checks. Use
[currency and departures](resources/currency.md) when auditing an accepted
version against changed local files, holding deliverables as `DAG pending`,
or preparing a successor. Resolve tool commands against the declared tool
root.
