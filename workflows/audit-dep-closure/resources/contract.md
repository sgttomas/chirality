# audit-dep-closure — contract

## Mission

Build and analyze the cross‑deliverable dependency graph from each deliverable's recorded register (`docs/SPEC.md` §5.3): the union of the entries in the declared sections of its `_DEPENDENCIES.md` and the rows of its `Dependencies.csv`. A declared entry and a row for the same `Direction` and target are one edge; where they disagree, the declaration governs and the disagreement is reported. With `INCLUDE_DECLARED=false` the graph is read from `Dependencies.csv` alone, the prior reading. Produce:

- a closure report with PASS/WARNING/BLOCKER outcomes for core checks,
- machine-readable metrics (JSON),
- the registered tool fingerprint, effective arguments, input manifest, and output evidence (reproducibility).

---

## Non-negotiable invariants

- **Read-only on deliverables.** Never modify any `Dependencies.csv`, `_DEPENDENCIES.md` or other deliverable file.
- **Evidence-first.** Every finding must trace to specific files/rows (report paths + row identifiers).
- **No invention.** If uncertain or data is missing, mark as `UNKNOWN` / `INCOMPLETE` and continue.
- **Deterministic.** Same inputs → same outputs (no non-deterministic sampling).
- **Immutable snapshots.** Each run writes a new snapshot folder; never overwrite prior snapshots.
- **Pointer moves are brief-controlled.** `_LATEST.md` is overwritten only when the brief sets `UPDATE_LATEST_POINTER=true` (default `false`); snapshots remain immutable. That pointer is an **observation pointer** (the most recent completed observation). It is not an **accepted pointer**: reliance on a closure result as a project's accepted basis is recorded by the manager after human acceptance in the project's accepted-basis record, never by this TASK.

---

## Inputs (brief schema)

Required:
- `EXECUTION_ROOT`: default `execution/` (repo-relative)
- `SCOPE`: `ALL` (default) | list of deliverable IDs | list of package IDs | list of explicit paths
  - `ALL` means the independent scope inventory derived from the accepted decomposition registers (see `SCOPE_INVENTORY_SOURCE`), less declared exemptions; it is not merely whatever folders exist.
- `RUN_LABEL`: short label for this run (default `TASK`)

Optional:
- `REQUESTED_BY`: invoking agent name (default `WORKING_ITEMS`)
- `SCOPE_INVENTORY_SOURCE`: accepted decomposition register that defines the unit inventory (default: `Deliverables.csv` of the accepted decomposition resolved through `{EXECUTION_ROOT}/_Decomposition/checkpoint_snapshots/_LATEST_ACCEPTED.md` when present, otherwise the accepted decomposition named by the brief). If no accepted register can be resolved, fall back to the workspace folder inventory and record the degraded basis in `QA_Report.md`.
- `EXEMPT_UNITS`: declared exemptions, each with unit ID, class (`CONTROL` such as a PKG-00 control deliverable, `RETIRED`, or another declared class), and the accepted authority or register row that declares it. Exempt units are reported in `QA_Report.md` and the report's inventory section but are not counted as FAIL/BLOCKER for missing or invalid registers; they remain in the workspace inventory, so edges that target them are outside-scope, not orphans.
- `UPDATE_LATEST_POINTER`: `false` (default) | `true` — move the `_LATEST.md` observation pointer after a completed run.
- `FILTER_ACTIVE_ONLY`: `true` (default) | `false`
- `NORMALIZE_IDS`: `true` (default) | `false`
  - When `true`, normalize long-form IDs by stripping descriptive suffixes for analysis only. Examples: `DEL-XXX-YY_Label` → `DEL-XXX-YY` (WORKING_ITEMS (workflow: project-decomp)), `DEL-XX-YY` (WORKING_ITEMS (workflow: software-decomp), already short-form). If DOMAIN folders are encountered in a mixed workspace, their `KTY-CC-TT_Label` IDs are normalized to `KTY-CC-TT`.
- `EDGE_FILTER` (default):
  - `DependencyClass = EXECUTION`
  - `TargetType = DELIVERABLE`
- `HUB_THRESHOLD`: integer (default `20`)
- `MAX_CYCLES`: integer (default `10000`)
- `INCLUDE_DECLARED`: `true` (default) | `false` — passed to the analyzer as `--include-declared`. `true` reads the §5.3 recorded register (declared entries without a matching CSV row join the graph); `false` reads `Dependencies.csv` alone, reproducing the prior reading, for both the graph and the accepted-DAG comparison.
- `PRIOR_SUMMARY`: optional explicit path to a prior `closure_summary.json` for comparison mode, passed to the analyzer as `--prior-summary <path>`. A legacy `PRIOR_RUN_LABEL` is accepted only after the owner resolves it to that explicit path; the analyzer takes no label.

If `EXECUTION_ROOT` is missing/invalid or no deliverables can be discovered in scope: write `RUN_SUMMARY.md` with `RUN_STATUS = FAILED_INPUTS` and return.

---

## Outputs (write zone)

Bootstrap tool root: `tools/scaffolding/scaffold_tool_root.sh {EXECUTION_ROOT}/_Evaluation DepClosure`

Create snapshot folder: `tools/scaffolding/create_snapshot_folder.sh {EXECUTION_ROOT}/_Evaluation/DepClosure CLOSURE {RUN_LABEL}`

Run graph analysis: `python3 tools/coordination/analyze_dep_closure.py {EXECUTION_ROOT} --output-dir {snapshot_folder}/Evidence --scope {SCOPE_UNITS} --filter-active-only {FILTER_ACTIVE_ONLY} --normalize-ids {NORMALIZE_IDS} --dependency-class EXECUTION --target-type DELIVERABLE --hub-threshold {HUB_THRESHOLD} --max-cycles {MAX_CYCLES} --include-declared {INCLUDE_DECLARED} [--prior-summary {PRIOR_SUMMARY}]`
`{SCOPE_UNITS}` is `ALL` only when the accepted inventory, the workspace inventory, and the exemption list agree; otherwise pass the explicit non-exempt accepted unit IDs that have a workspace folder, and report accepted units without one as inventory findings (the analyzer stops if a selected ID matches no production unit).
The analyzer writes flat into its `--output-dir` (here `Evidence/`): `closure_summary.json`, `coverage.csv`, `orphans.csv` (missing workspace targets), `outside_scope.csv` (existing targets outside selected scope), `isolated.csv` (zero-edge nodes), `cycles_sample.csv`, `scc_summary.csv`, `hubs.csv`, `bidirectional_pairs.csv`, `id_normalization.csv`, `declared_only.csv` (declared entries with no matching CSV row, added to the graph), `declared_disagreements.csv` (a declaration and a CSV row that disagree, including a declaration whose only matching row is `RETIRED`), `declared_unread.csv` (lines in the declared sections that name a deliverable but are not in the §5.2 entry form; never inferred), and, when `{EXECUTION_ROOT}/_DAG/_LATEST.md` names an accepted project DAG, `dag_pending.csv` (deliverables whose local evidence departs from that version, `docs/SPEC.md` §5.4; the `project-dag` currency audit governs where it differs). With `INCLUDE_DECLARED=false` the three `declared_*` files are empty. It also prints the summary JSON to stdout and exits 0 for a completed observation (even when the subject FAILs) and 2 for `FAILED_INPUTS`.

The analyzer does not write `Tool_Run.json`. The executing TASK writes it at the snapshot root, recording the tool path and SHA-256, exact arguments, accepted input basis, exit code, `run_status`, and `subject_status`. The accepted input basis lists every file the analyzer read: each in-scope `Dependencies.csv` and, with `INCLUDE_DECLARED=true`, each in-scope `_DEPENDENCIES.md`, and `{EXECUTION_ROOT}/_DAG/_LATEST.md` with the version files it names when present. The accepted-DAG comparison reads the registers of every unit under the execution root, not only those in scope, so with an accepted DAG those files are listed too. Record each file with its SHA-256. Process success is distinct from subject PASS.

Additional snapshot contents (minimum, produced by LLM):
- `Brief.md` (verbatim + normalized)
- `RUN_SUMMARY.md` (`RUN_STATUS = OK|WARNINGS|FAILED_INPUTS`)
- `QA_Report.md` (coverage + schema issues + limits)
- `Decision_Log.md` (defaults, overrides, tie-breaks)
- `Dependency_Closure_Report.md`
- `Dependency_Closure_IssueLog.csv`

Update pointer (only when `UPDATE_LATEST_POINTER=true`): `tools/scaffolding/update_latest_pointer.sh {EXECUTION_ROOT}/_Evaluation/DepClosure {snapshot_folder_name}`. This moves the observation pointer only; it records no acceptance.

---

## Validity

A run is valid when:
- Outputs are written to a new immutable snapshot folder under `{EXECUTION_ROOT}/_Evaluation/DepClosure/`.
- `Dependency_Closure_Report.md`, `Dependency_Closure_IssueLog.csv`, `Evidence/closure_summary.json`, and `Tool_Run.json` exist.
- The report states the scope inventory source, the counted units, and each declared exemption with its class and authority.
- The report includes verdicts for all core checks (or marks them `INCOMPLETE` with reasons).
- Every WARNING/BLOCKER finding includes evidence pointers (file + row identifiers).
- No deliverable file is modified.

---

## Artifacts and schemas

### Tool-root layout

```
{EXECUTION_ROOT}/_Evaluation/DepClosure/
  _Archive/
  _LATEST.md
  CLOSURE_{RUN_LABEL}_{YYYY-MM-DD}_{HHMM}/
    Brief.md
    RUN_SUMMARY.md
    QA_Report.md
    Decision_Log.md
    Dependency_Closure_Report.md
    Dependency_Closure_IssueLog.csv
    Tool_Run.json              # written by the executing TASK, not the analyzer
    Evidence/                  # analyzer --output-dir (flat)
      closure_summary.json
      coverage.csv
      orphans.csv
      outside_scope.csv
      isolated.csv
      cycles_sample.csv
      scc_summary.csv
      hubs.csv
      bidirectional_pairs.csv
      id_normalization.csv
      declared_only.csv
      declared_disagreements.csv
      declared_unread.csv
      dag_pending.csv          # only when _DAG/_LATEST.md names an accepted project DAG
```

---
