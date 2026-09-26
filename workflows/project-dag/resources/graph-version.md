# project-dag — graph-version rules

These rules govern assembly of a candidate graph version and its independent
review. WORKING_ITEMS supplies them in each assembly or review brief, with the
frozen inventory, evidence manifest, closure snapshot, confirmed objective and
selection rules, recorded rulings, candidate folder, and write boundary. The
assembling TASK writes only inside `{DAG_ROOT}/_Candidates/DAG-NNN/` and its
run record; it never writes a local dependency file, decomposition file, or
case file.

## Files

| File | Content |
|---|---|
| `GRAPH_BASIS.md` | Identity (`DAG-NNN`, trigger, predecessor, and for a successor the currency audit and departures it decides); objective; edge semantics; direction convention; tracking mode and completeness; inventory source, count, exemptions, and evidence states; case home; Git revision, manifest, and closure snapshot(s); selection rules as applied, with the checkpoint-1 decision reference; cut and merge rulings; candidate-layer summary; exclusions by disposition; findings routed to owners; limitations and open questions; how to reproduce the version. |
| `DeliverableNodes.csv` | One row per included inventory unit: `DeliverableID,PackageID,DeliverableName,ExecutionPath,DependenciesPath,RegisterState,TrackingMode,InventorySource`. `RegisterState` is `PRESENT`, `MISSING`, `UNREADABLE`, `SCHEMA_INVALID`, or `DECLARED_ONLY`. Exempt units are listed in `GRAPH_BASIS.md`, not here. Nodes with no edges remain. |
| `DependencyEdges.csv` | Admitted rows: the 29 core v3.1 columns in `docs/SPEC.md` §6.2 order, copied exactly, followed by the provenance columns `SourceRegister` (path relative to `EXECUTION_ROOT`), `SourceRegisterSHA256`, `SourceRecord` (1-based data-record ordinal in the source file), and `SelectionRule`. Source extension columns stay in the register. |
| `CandidateEdges.csv` | Non-gating candidate rows in the same columns, plus `CandidateReason` (`SCC_UNRESOLVED`, `SELF_LOOP`, or `CONFIRMATION_PENDING`), `SCCRef` (the SCC ID in the version's closure snapshot), `CaseRef` (the stable case folder in the project's case home; required for `SCC_UNRESOLVED`), and `OpenQuestion`. |
| `ExcludedRows.csv` | `SourceRegister,SourceRegisterSHA256,SourceRecord,DependencyID,FromDeliverableID,Direction,DependencyType,TargetType,TargetDeliverableID,TargetRefID,Disposition,RuleOrRuling,RepresentedBy,Notes`. |
| `SOURCE_MANIFEST.sha256` | `sha256sum` lines, relative to `EXECUTION_ROOT`, for every in-scope `Dependencies.csv` and `_DEPENDENCIES.md` and the accepted decomposition registers used for the inventory. |
| `SOURCE_BASIS.json` | Git revision and working-state note, manifest hash, closure snapshot path(s) with their input basis, case paths and states, tool paths and hashes. |
| `Evidence/` | `admissible_audit.json`, `dag_audit.json`, optional `candidate_audit.json`, `Tool_Run.json`, `Accounting.md`, any assembly script used (preserved for rerun), and an optional `TopologicalOrder.md`. |

`Status=CANDIDATE` is not a valid register or edge status
(`docs/SPEC.md` §6.7). The candidate layer is therefore a separate file whose
rows keep their source `Status=ACTIVE`; placement in that file is what makes
them non-gating.

## Required fields

Every row in `DependencyEdges.csv` and `CandidateEdges.csv` carries the 29 core
v3.1 columns. `docs/SPEC.md` §5.4 makes three fields that §6.2 marks SHOULD
REQUIRED in an accepted version: `Explicitness`, `SatisfactionStatus`, and
`Confidence`. Each holds a canonical §6.3 value. `audit_dag.py --canonical`
reports a blank or non-canonical value as a canonical finding, and `--strict`
then fails. The value is copied from the local file, so a blank is completed
there by its owner (normally `dependency-extract` with
`MODE=CANONICALIZE_EXISTING`) before the version is presented. It is never
filled in the version, and it is not an acceptable exception.

## Direction convention

Each row keeps its register `Direction`. `audit_dag.py` reads a row as an arc
from consumer to supplier: an `UPSTREAM` row as `From → Target`, a `DOWNSTREAM`
row as `Target → From`. The arc therefore reads "depends on". Drawings and
ordered listings normally show suppliers before consumers; any rendered view
states which reading it uses. Cycle membership is the same in either reading;
precedence is reversed.

## Selection rules

The default rule set follows. Checkpoint 1 confirms it or records the human's
adjustments. Apply the rules in the order listed.

| Rule | Selection | Other rows go to |
|---|---|---|
| SR-1 Register scope | Registers of included inventory units, at the frozen manifest. | Not in scope; registers of exempt units are not read for edges. |
| SR-2 Topological rows | `Status=ACTIVE`, `DependencyClass=EXECUTION`, valid canonical `Direction`, `TargetType=DELIVERABLE`, target in the included inventory. | `NOT_TOPOLOGICAL` (non-deliverable target, still relevant to readiness); `OUTSIDE_INVENTORY` (existing exempt or out-of-scope target); `UNRESOLVED_TARGET` (target absent from the workspace); `INVALID_ROW` (invalid values, ragged record, or long-form ID). |
| SR-3 Objective types | `DependencyType` in the admitted set; default all canonical types. Each excluded type is stated with its reason. | `TYPE_NOT_SELECTED`. |
| SR-4 Rulings | Arcs not cut by a recorded human ruling and not internal to a ruled merge group. | `RULED_OUT_OF_OBJECTIVE` or `MERGE_GROUP_INTERNAL`, citing the ruling. |
| SR-5 Confirmation hold (optional) | Only when confirmed at checkpoint 1: arcs whose every row meets the stated hold condition, for example `Confidence=LOW` with `Explicitness=IMPLICIT`, are held pending confirmation by the register owner. | Candidate layer, `CONFIRMATION_PENDING`. |
| SR-6 One row per arc | One representative row per ordered arc: the consumer register's `UPSTREAM` row, then a `DECLARED` row before an `EXTRACTED` row, then the lowest `DependencyID`. | `MIRROR` (the counterpart row in the other endpoint's register) or `SAME_ARC`, each with `RepresentedBy`. |
| SR-7 Cycle hold | Compute SCCs on the admissible set. Rows whose endpoints lie in the same non-trivial SCC, and self-loops, are held. | Candidate layer, `SCC_UNRESOLVED` or `SELF_LOOP`, with the SCC and its case in the project's case home. |

Rules on rows and arcs:

- A cut or merge ruling names the arc or node group and the rows it covers,
  and cites the case `Ruling_Register.csv` row or decision record. A merge
  group is recorded in `GRAPH_BASIS.md` with its combined inputs,
  responsibility, and examination. A merge that changes the accepted
  decomposition goes through `scope-change` first.
- A material disagreement between a representative and its mirror (type,
  required maturity, or statement) is a conflict in the evidence. List it in
  `GRAPH_BASIS.md` and route it to both owners. The representative is still
  chosen by rule; the human may direct at a checkpoint that the arc is held.
- Copy endpoint IDs as they appear in the local file. A long-form ID is an
  `INVALID_ROW` routed to `dependency-extract`, unless checkpoint 1 accepted a
  declared normalization. In that case normalize only the endpoint ID columns
  and preserve the original values in `SourceFromDeliverableID` and
  `SourceTargetDeliverableID` extension columns.
- Removing all intra-SCC rows leaves the condensation, which is acyclic. Do not
  choose a subset of cycle edges to remove; automated edge removal would choose
  a graph shape without establishing its basis.

## Assembly procedure

1. Confirm the basis has not moved: from `EXECUTION_ROOT`, run
   `sha256sum -c {candidate}/SOURCE_MANIFEST.sha256`. Any failure stops
   assembly and returns to the manager for a re-freeze.
2. Write `DeliverableNodes.csv` from the frozen inventory.
3. Read each in-scope local file and apply SR-1 to SR-6. Write
   the admissible rows to `Evidence/admissible_edges.csv` in the edge-file
   columns.
4. Compute SCCs on the admissible set:

   ```text
   python3 tools/coordination/audit_dag.py \
     --edges {candidate}/Evidence/admissible_edges.csv \
     --nodes {candidate}/DeliverableNodes.csv \
     --canonical --json-out {candidate}/Evidence/admissible_audit.json
   ```

   Its `active_graph.sccs` lists the non-trivial SCCs. Detect self-loops by
   inspection (from ID equal to target ID). Apply SR-7 and write
   `DependencyEdges.csv`, `CandidateEdges.csv`, and `ExcludedRows.csv`.
5. Run the acceptance check on the admitted edges:

   ```text
   python3 tools/coordination/audit_dag.py --dag-dir {candidate} \
     --canonical --strict --json-out {candidate}/Evidence/dag_audit.json
   ```

   Exit 0 is required. `--dag-dir` reads `DependencyEdges.csv` and
   `DeliverableNodes.csv`; `--edges` and `--nodes` override either path. The
   strict check requires a valid schema, no ragged rows, no canonical findings
   (so the [required fields](#required-fields) are present), every endpoint in
   the node file, and no SCC, duplicate arc, or bidirectional pair in the
   `ACTIVE` graph. Optionally run the same command without
   `--strict` on `CandidateEdges.csv` (via `--edges`) and keep
   `candidate_audit.json` as evidence.
6. Write `Evidence/Tool_Run.json` for each tool run: tool path and SHA-256,
   exact arguments, exit code, `run_status`, and `subject_status`. Process
   success is distinct from subject pass. Record and preserve any assembly
   script with its hash.
7. Complete the accounting and fidelity checks below, then `GRAPH_BASIS.md`,
   `SOURCE_BASIS.json`, and, if useful, `Evidence/TopologicalOrder.md`
   (supplier-before-consumer layers of the admitted edges, labelled as a
   derived reading aid and not a schedule).

Do not publish `--markdown-out` output in a graph version. The tool's markdown
report names the audited edge file and states that the audit establishes no
authority, as the [contract](contract.md#authority) holds: neither side is
self-authorizing; a version carries authority only through its acceptance
while it is current, and a departure is decided by the human. Its title and
front matter, however, are a project-specific DEV-001 audit record, and the
JSON's `dev001_projection` section is a project-specific projection outside
this workflow's checks. Report both points rather than relying on them.

## Accounting and fidelity

`Evidence/Accounting.md` records, per register and in total:

- `ACTIVE` `EXECUTION` rows = admitted + candidate + excluded, with no row in two
  files and none missing, keyed by `SourceRegister` and `DependencyID`
  (`SourceRecord` disambiguates a duplicate ID, which is also a register
  finding);
- counts of `ANCHOR` rows and `RETIRED` rows, which are outside the execution
  graph and remain in the registers;
- exclusions by disposition, and candidates by reason;
- byte fidelity: each admitted and candidate row equals its source record in the
  29 core columns;
- closure consistency: the SCCs on the admissible set compared with the closure
  snapshot's `scc_summary.csv`. Differences must be explained by SR-3, SR-4,
  SR-5, or a declared normalization. A closure snapshot computed on a different
  manifest is not comparable.

## Failure treatment

Never edit copied values or drop rows silently to pass a check.

| Finding | Treatment |
|---|---|
| Manifest mismatch | Basis moved; return for re-freeze and, when edges changed, a new closure run. |
| Schema invalid or ragged edge rows | Assembly column defect, or an `INVALID_ROW` defect in the local file routed to `dependency-extract`. |
| Canonical findings, including a blank required field | Route to the owner of the local file, normally `dependency-extract` with `MODE=CANONICALIZE_EXISTING`. The [required fields](#required-fields) admit no exception; the version is not presented until the local file is complete and the basis is re-frozen. |
| Endpoint issues | SR-2 not applied, or the inventory is wrong; repair assembly or return the inventory question. |
| SCC, duplicate, or bidirectional pair in admitted edges | SR-6 or SR-7 not applied; repair assembly. |
| Accounting imbalance or fidelity mismatch | Assembly defect; repair and rerun every check. |
| Unexplained closure difference | Investigate before presenting; report it if unresolved. |

## Independent review

A TASK instance that did not assemble the candidate reviews it against the
confirmed basis. It reruns the manifest check, `audit_dag.py --canonical
--strict`, accounting, and fidelity. It then examines:

- whether the edge semantics fit the objective;
- the rule applications, especially `NOT_TOPOLOGICAL`, `OUTSIDE_INVENTORY`, and
  `TYPE_NOT_SELECTED` patterns that could hide a scope-boundary question;
- mirror conflicts;
- isolated nodes and hubs;
- candidate reasons and the held work they imply;
- ruling citations and stated limitations.

`INDEPENDENT_REVIEW.md` lists findings as blocking or non-blocking with evidence
pointers. Mechanical defects return for repair. Substantive findings the
manager cannot resolve within the confirmed basis are presented at checkpoint 2.
