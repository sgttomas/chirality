# project-dag — currency and departures

An accepted version is a snapshot of identified local evidence that the human
accepted. The local files keep changing as work proceeds: satisfaction
advances, extraction reruns, declarations are added, and scope changes add or
retire relationships. Under `docs/SPEC.md` §5.4 the version carries authority
only while it is current with that evidence. A currency audit determines
whether it still is. When a local file has departed from it, neither side
silently wins: the affected deliverables are held `DAG pending` until the human
accepts a successor or rejects the change. Under
`docs/CYCLE_DRIVEN_RESOLUTION.md` §4, a new version is event-driven, not
periodic.

## When to audit

- Before a consumer relies on the version for route selection or a blocker
  verdict, when the local files may have changed since its basis or since the
  latest audit. `construct-local-work-graph` calls for this audit when it
  establishes a route.
- After `dependency-extract` runs on in-scope deliverables, or a human changes
  declarations.
- After an accepted scope change or decomposition revision. `scope-change`
  treats the accepted DAG as a derivative package.
- When a consumer finds the version and a local file disagree.
- After the human decides a departure, to record that the flag has cleared.

## Currency audit

A TASK assignment, or the manager directly, performs the audit and writes a new
snapshot under
`{EXECUTION_ROOT}/_Evaluation/DAGCurrency/CURRENCY_{LABEL}_{YYYY-MM-DD}_{HHMM}/`
(`tools/scaffolding/create_snapshot_folder.sh`), then moves
`_Evaluation/DAGCurrency/_LATEST.md` to it. It never modifies an accepted
version or a local file.

1. Resolve the accepted version through `{DAG_ROOT}/_LATEST.md`. Verify the
   snapshot itself: from its folder, `sha256sum -c MANIFEST.sha256`.
2. From `EXECUTION_ROOT`, run `sha256sum -c {DAG_ROOT}/DAG-NNN/SOURCE_MANIFEST.sha256`
   and keep the output. Compare the accepted decomposition pointer with the
   inventory source recorded in `GRAPH_BASIS.md`.
3. If nothing changed, the result is `CURRENT`.
4. Otherwise re-apply the accepted selection rules to the current local files
   in the audit snapshot's `Evidence/` folder, as a scratch assembly rather
   than a graph version. Compare the admitted arc set, candidate arc set, SCCs
   and node inventory with the accepted version. The files at the basis can be
   recovered from Git at the recorded revision. Where they cannot, compare
   against the accepted edge, candidate, and exclusion files, and treat any
   field that cannot be compared as changed.
5. Read the rejection records of candidates opened since the accepted version
   (`{DAG_ROOT}/_Candidates/DAG-NNN/REJECTION_RECORD.md`). A departure the
   human rejected is reported as `REJECTED_DEPARTURE`, not as pending, while
   its rows are unchanged since the rejection.
6. Classify the result and write `CURRENCY_REPORT.md` with the evidence and
   `Tool_Run.json`. The report lists every deliverable that is `DAG pending`,
   the departure affecting it, and the decision awaited.

| Result | Meaning | Consequence |
|---|---|---|
| `CURRENT` | No source bytes changed. | Rely on the accepted version. |
| `CURRENT_WITH_EVIDENCE_DRIFT` | Bytes changed, but the admitted and candidate arc sets, SCCs, and inventory are unchanged. Examples: satisfaction, dates, quotes, notes, `ANCHOR` rows, or a further row on an arc already represented. | Rely on the accepted version for blockers. Read the changed fields from the live local files. Record the drift; no successor is needed. |
| `DEPARTURE` | A local file departs from the accepted version: an arc added or removed (including one redirected or reclassified out of or into the selection), or an SCC formed, changed, or dissolved; or the accepted inventory changed. | Flag the DAG stale for the affected deliverables, which become `DAG pending`. Prepare a candidate successor. The human accepts it or rejects the change. |
| `INCOMPLETE` | A source is missing or unreadable, or the comparison could not be completed. | Report the limitation. The deliverables whose evidence could not be compared are `DAG pending` until the audit completes. |

Affected deliverables are the endpoints of each added or removed arc, the
members of each new or changed SCC, and each deliverable the inventory change
adds, removes, or splits. The audit may name further deliverables whose route
runs through a changed arc, as advice for renewed examination; they are not
`DAG pending` on that account.

## DAG pending

While a departure is undecided:

- unaffected deliverables keep using the accepted version;
- a `DAG pending` deliverable gets no ready or blocked verdict from
  dependencies. Reports show the departure and the decision awaited instead;
- the accepted version is not edited, and the local file is not rewritten to
  match it. Neither side has won.

A departure that forms a cycle is also routed to `scc-resolution-case` in the
project's case home (`{DAG_ROOT}/cases/<CASE-ID>/` by default). A cycle whose
member node set matches an existing case updates that case rather than
opening a new one.

## Preparing a successor

Run the [method](method.md) with `TRIGGER=SUCCESSOR` and `CURRENCY_REPORT`
naming the audit.

- Carry forward the objective, semantics, rules, exemptions, and rulings that the
  departure does not affect. Reopen only decisions whose rows, arcs, or
  warrants changed. A cut or merge ruling carries forward only while its arcs
  and evidence are unchanged.
- Rerun closure on the re-frozen manifest. Open or update cases for new or
  changed SCCs. Close cases whose SCC dissolved only on a cited closure result.
- Checkpoint 1 may be limited to the reopened decisions. Present what carries
  forward as carried forward, not as newly decided. Checkpoint 2 is still
  required: the successor is a new version with a new acceptance record.
- Several departures may be decided in one successor. A departure the human
  wants decided separately gets its own candidate.

## Deciding a departure

At checkpoint 2 for a successor, the human decides each departure it
presents:

- **Accept.** Publish `DAG-(NNN+1)`, move `_DAG/_LATEST.md`, and name the
  predecessor as superseded. The predecessor and its decisions remain unchanged
  as history.
- **Reject the change.** The accepted version stands. Write
  `REJECTION_RECORD.md` in the candidate folder with the human's decision as
  given, date, actor, relay provenance, and the rows and hashes rejected. The
  candidate keeps its number. Route the departing evidence to its owner for
  correction or retirement: `dependency-extract` for extracted rows, the human
  for declarations.

Either decision clears the `DAG pending` flag for the deliverables it covers.
Run a follow-up currency audit to record that. A later change to rejected rows
is a new departure.

A change in a relationship can call for renewed examination of dependent work
even where that work's own files have not changed. List such work in the
successor's handoff.

## What currency work never does

- It does not edit an accepted version in place or move the pointer to a
  version the human has not accepted.
- It does not write local files to match the version, or the version to match
  the local files.
- It does not rebuild a version because a session began or local tasks were
  rearranged.
