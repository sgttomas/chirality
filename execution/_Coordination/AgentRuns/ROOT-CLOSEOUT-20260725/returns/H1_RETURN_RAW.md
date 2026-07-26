# H1 terminal return — practitioner-harness adoption of the root adapter

Run: ROOT-CLOSEOUT-20260725 / H1. Executor: ephemeral bounded Agent 2
generalist (`opus-5`). Brief: `execution/_Coordination/AgentRuns/ROOT-CLOSEOUT-20260725/briefs/HARNESS-ADOPTION-BRIEF.md`.
Status: **COMPLETE** — objective met, all declared verifications run, no
blockers. Nothing committed; changes left in the working tree.

## 1. Files created / modified (all within write scope)

| Path | Change |
|---|---|
| `tools/practitioner_harness/adapter_loader.py` | MODIFIED — dual registered locations/schemas, strict `root-harness-adapter/v1` validation, normalization into the internal `AdapterManifest`, `kind` / `declares_dag_pointer()` / `declares_validation_commands()` / `manifest_relpath()` |
| `tools/practitioner_harness/harness.py` | MODIFIED — `root` / `chirality-root` aliases, `OBSERVABLE_PROJECTS`, `_project_root` root handling, `_alias_by_root` root exclusion, `_refuse_root` refusals, `drift --all` guard, `brief` others-set filter, docstring |
| `tools/practitioner_harness/adapter_project.py` | MODIFIED — `dag_pointer_facts` reports "not declared by this adapter schema" (`NOT_APPLICABLE`) instead of joining an empty relpath |
| `tools/practitioner_harness/cmd_status.py` | MODIFIED — root-aware PRD-posture heading and working-root note (project output byte-identical) |
| `tools/practitioner_harness/cmd_drift.py` | MODIFIED — baseline finding cites `manifest.manifest_relpath()` instead of a hardcoded `<root>/_harness/adapter.yaml` (project output byte-identical) |
| `tools/practitioner_harness/test_root_adoption.py` | CREATED — 38 tests (34 fixture + 4 live) |
| `tools/practitioner_harness/README.md` | MODIFIED — new `## Root working root (--project root, D-GOV-21)` section, command examples, pilot-scope pointer, test inventory paragraph |

No writes to `tools/validation/`, `execution/` (other than this return),
`docs/`, `agents/`, or CI workflows. The root adapter was not touched.

## 2. Normalization design

### 2.1 Two registered locations, two schemas, no fallback

| Working root | Manifest location | Schema |
|---|---|---|
| project (`projects/<name>`) | `<project-root>/_harness/adapter.yaml` | `practitioner-harness-adapter/v1` |
| root product (`WORKING_ROOT == REPO_ROOT`) | `<repo-root>/execution/_harness/adapter.yaml` | `root-harness-adapter/v1` |

`load_adapter(working_root)` probes both registered locations and requires
**exactly one** to carry a manifest:

- zero → operational error naming both searched locations (exit 2);
- two → refused as *ambiguous adapter registration* — the loader never picks
  one (K-INVENT-1);
- one → the declared `schema` must equal the schema registered **for that
  location**. A known-but-wrong schema (either direction) errors with
  "location and schema must agree — the loader refuses rather than falling
  back to the other shape"; an unknown schema keeps the existing "declares
  unknown schema" wording. There is no field-soup path and no silent fallback
  between shapes; each shape has its own required-key set and validator.

### 2.2 Schema mapping table (root → internal `AdapterManifest`)

| `root-harness-adapter/v1` | internal field | Note |
|---|---|---|
| `product` | `project` | working-root identity (`chirality-root`) |
| `prd` | `plan` | the PRD fills the role `plan` serves for a project |
| `coordination` | `coordination` | same meaning |
| `decision_register` | `decision_register` | same meaning |
| `status_glob`, `states`, `parser_dialect`, `exclude_globs` | same names | same meaning |
| `baselines.status_files` | `drift_baseline_files` | pinned drift denominator |
| `baselines.status_mismatch` | `drift_baseline_mismatch` | pinned drift numerator |
| `baselines.pinned_at` | `baseline_pinned_at` | pin provenance (root only) |
| `working_root`, `execution_root` | same names | declared explicitly by root only |
| *(not declared)* | `dag_pointer = ""` | root registers no DAG pointer surface |
| *(not declared)* | `validation_commands = []` | root declares no validation surfaces |
| — | `kind = "root"` | records which shape was loaded |

Root-shape strictness added by the loader (validated before normalization):
`product` / `execution_root` / `prd` / `coordination` / `decision_register` /
`status_glob` / `parser_dialect` non-empty strings; `working_root == "."`;
`states` a non-empty list of non-empty strings; `exclude_globs` a list of
strings; `baselines` a mapping carrying `status_files` / `status_mismatch` /
`pinned_at`; both baselines plain integers (bools rejected), `>= 0`, and
`status_mismatch <= status_files`; `pinned_at` a non-empty string.

**G1 relationship.** `tools/validation/validate_root_harness_adapter.py`
remains the root adapter's authority. The loader's required-key set mirrors
G1's; it adds only requirements the harness itself needs to read the manifest
at all (the two baseline integers, non-empty pointer strings). It does not
re-implement G1's pointer-existence checks, its `pinned_at` hex-SHA regex, its
observed-vs-declared `status_files` recount, or its `mismatch_disposition`
rule — nothing is weakened, nothing is duplicated. G1 still PASSes unchanged.

### 2.3 Absent-field policy, per command

`dag_pointer == ""` is the normalized "not declared" marker. Consumers branch
on `declares_dag_pointer()`; an empty relpath is never joined onto a working
root and never rendered as "artifact absent" (which would be a wrong answer,
not a missing one).

| Command | `--project root` | Behavior / reason |
|---|---|---|
| `status` | supported | `## DAG pointer` reports `dag.pointer: not declared by this adapter schema (root-harness-adapter/v1)` at `NOT_APPLICABLE`, citing `execution/_harness/adapter.yaml`. Plan section heading reads "PRD posture (the root adapter's `prd` fills the `plan` role)". Validation surfaces: "none declared". |
| `drift` | supported, alone | Baselines come from `baselines.*`; the INFO baseline finding cites the actual manifest path. |
| `drift --all` | refuses when combined with `--project root` | `--all` audits the pilot projects; refusing beats silently dropping the requested root. The default `--all` scope is unchanged (app-dev + piping; root is never folded in). |
| `brief` | **refuses (exit 2)** | `brief` projects from the working root's DAG pointer and a fence under that root; root declares no `dag_pointer` and its working root IS the repository, so no containing fence can be derived. A guessed pointer plus a repo-wide fence is worse than a refusal (K-INVENT-1). |
| `next` | **refuses (exit 2)** | Its rows carry ready-made `brief` command lines that would not run; the message redirects to `status --project root` for per-state counts. (Emitting the existing `NO_ALIAS_NOTE` would have been *false* now that an alias is registered.) |
| `run-validations`, `scope-check`, `evidence-check`, `closeout-digest` | unchanged | They resolve the project from the brief's write fence via `_alias_by_root`, from which the root is deliberately excluded: the repository root prefix-matches every `write_scope` entry and would convert their "no registered pilot project root" refusal into a wrong answer. Root has observation citizenship, not fence citizenship. |
| `self-check` | unchanged | Its scope is the pilot roots + control areas and it prints that scope; it makes **no** claim about the root `execution/` tree, so no untruthful coverage was added. Output byte-identical to pre-change. |

`PROJECT_ALIASES["root"] = PROJECT_ALIASES["chirality-root"] = "."`.
`_project_root` special-cases `ROOT_RELPATH` and returns `repo_root` itself, so
no `…/.`-shaped path can ever be produced (pathlib also drops a lone `.`
segment on join; the identity is made explicit rather than relied upon).
`brief`'s "other project roots" set filters out the root rel-path, so brief
generation for app-dev/piping is unchanged.

## 3. Refusal behaviors added

1. `brief --project root|chirality-root` → exit 2, `ERROR: brief does not
   support --project root: …declares no dag_pointer…` (full reason above).
2. `next --project root|chirality-root` → exit 2, with the redirect to
   `status --project root`.
3. `drift --project root --all` → exit 2, "…must be requested on its own.
   Refusing rather than silently dropping the requested root."
4. Loader: ambiguous double registration; location/schema disagreement (both
   directions); each missing root required key / baseline key; non-integer,
   negative, or over-count baselines; `working_root != "."`; absent manifest
   naming both registered locations.

All are `HarnessOperationalError` → `ERROR: …` on stderr, exit 2. No stack
traces (asserted in tests).

## 4. Test inventory (`tools/practitioner_harness/test_root_adoption.py`, 38 tests)

Alias resolution:
- `test_root_aliases_resolve_to_the_repository_root` — both aliases resolve to
  the repo root; no `.` component in the resolved path.
- `test_root_aliases_are_registered_and_observable_but_not_full_citizens` —
  pins that root is in `PROJECT_ALIASES`/`OBSERVABLE_PROJECTS` but not in
  `FULL_CITIZENSHIP_PROJECTS`.
- `test_root_is_excluded_from_the_brief_fence_alias_table` — reverse table has
  exactly `{app-dev, piping, pec}` and never the repo root.
- `test_fence_resolution_still_refuses_paths_outside_a_project` — regression
  pin: `_resolve_project_root` still raises "registered pilot project root"
  for a `docs/…` fence (i.e. root did not become a catch-all).

Adapter load / normalization:
- `test_root_adapter_loads_and_normalizes_into_the_internal_shape` — every row
  of the mapping table, plus `declares_dag_pointer()/declares_validation_commands()`
  False and `manifest_relpath()`.
- `test_project_manifest_still_reports_kind_project` — project shape unchanged,
  `kind == "project"`, `declares_dag_pointer()` True.
- `test_root_adapter_missing_required_key_is_operational_error` ×10
  (parametrized over `product`, `working_root`, `execution_root`, `prd`,
  `coordination`, `decision_register`, `status_glob`, `states`,
  `parser_dialect`, `baselines`).
- `test_root_adapter_missing_baseline_key_is_operational_error` ×3
  (`status_files`, `status_mismatch`, `pinned_at`).
- `test_root_adapter_non_integer_baseline_is_operational_error`.
- `test_root_adapter_mismatch_exceeding_files_is_operational_error`.
- `test_root_adapter_working_root_must_be_dot`.
- `test_project_schema_at_the_root_location_is_refused`,
  `test_root_schema_at_the_project_location_is_refused` — no silent fallback,
  both directions.
- `test_both_registered_locations_present_is_ambiguous`.
- `test_absent_manifest_names_both_registered_locations`.
- `test_absent_dag_pointer_is_reported_not_applicable` — `NOT_APPLICABLE`,
  manifest cited, never an empty/joined-empty path.

status / drift / refusals on a tmp fixture root tree:
- `test_status_root_fixture_reports_the_states_and_the_prd`.
- `test_drift_root_fixture_measures_and_cites_the_root_adapter` — a seeded
  mismatch is measured and the finding cites `execution/_harness/adapter.yaml`.
- `test_cli_status_and_drift_accept_both_root_aliases` — exit 0 for both
  aliases, both commands.
- `test_cli_brief_refuses_root_with_a_named_reason` — exit 2, reason present,
  `"Traceback" not in stderr`.
- `test_cli_next_refuses_root_with_a_named_reason`.
- `test_cli_drift_all_with_root_refuses_rather_than_dropping_it`.
- `test_cli_drift_all_default_scope_excludes_the_root` — default `drift --all`
  on the mini-repo fixture never mentions `chirality-root`.

LIVE-repo pins (skipped when `CHIRALITY_SKIP_LIVE_TESTS=1` or the live root
adapter is absent; same conscious-pin discipline as the app-dev 0/53 and
piping 0/101 pins):
- `test_live_root_adapter_pins_45_files_0_mismatch` — adapter pin 45 / 0,
  `kind == root`, product `chirality-root`.
- `test_live_root_drift_baseline_0_of_45` — measured `files=45`,
  `mismatches=0`, `unparseable_docs=0`, `no_state_assertion=0`; summary
  45 / 0; baseline finding text and cited path pinned.
- `test_live_root_status_reports_45_open_and_no_dag_pointer` — `| OPEN | 45 |`,
  `status_files == 45`, absent-DAG line present.
- `test_live_root_cli_status_and_drift_exit_zero`.

No existing test was modified; none had a premise conflicting with adoption.

## 5. Verification transcript (verbatim, every exit code)

```
$ python3 -m pytest tools/practitioner_harness -q
349 passed in 45.22s
EXIT=0        # was 311 passed pre-change; +38 new, 0 modified
```

```
$ python3 -m pytest tools/validation -q
233 passed in 2.72s
EXIT=0        # unchanged from pre-change run
```

```
$ python3 tools/practitioner_harness/harness.py status --project root
EXIT=0
# key report lines:
# Status — chirality-root
## PRD posture (the root adapter's `prd` fills the `plan` role)
- `docs/PRD_ROOT.md`: artifact present
- `docs/PRD_ROOT.md` (line 19): > **Status: `ADOPTION-READY — adopted only by the instrument named below`.
- `execution/_Coordination/CURRENT_WORKPLAN.md`: artifact present
| State | Count |
| OPEN | 45 |
Source: 45 file(s) matching `execution/PKG-*/1_Working/DEL-*/_STATUS.md` under `.` (the repository root — WORKING_ROOT == REPO_ROOT) (parser: prose-bullet-v1).
- dag.pointer: not declared by this adapter schema (root-harness-adapter/v1) — `execution/_harness/adapter.yaml`
- project: chirality-root
- status_files: 45
```

```
$ python3 tools/practitioner_harness/harness.py drift --project root
EXIT=0
| Project | Files | Matches | Mismatches | via strict rule | via assumption rules | Unparseable docs | Recorded baseline |
| chirality-root | 45 | 45 | 0 | 0 | 0 | 0 | 0/45 |
Denominator: 45 status file(s) audited; 0 mismatch(es) measured.
| INFO | DRIFT_BASELINE_COMPARISON | staleness/drift | `execution/_harness/adapter.yaml` | K-STATUS-1 (RATIFIED) | chirality-root: measured 0 mismatch(es) over 45 file(s) vs recorded baseline 0/45 (trend statement only). |
```

```
$ python3 tools/practitioner_harness/harness.py self-check
EXIT=0        # output byte-identical to the pre-change run (diff clean)
```

```
$ python3 tools/practitioner_harness/harness.py status --project app-dev
EXIT=0        # diff vs pre-change capture: IDENTICAL
$ python3 tools/practitioner_harness/harness.py drift --project piping
EXIT=0        # diff vs pre-change capture: IDENTICAL
$ python3 tools/practitioner_harness/harness.py drift --all
EXIT=0
$ python3 tools/practitioner_harness/harness.py next
EXIT=0
$ python3 tools/practitioner_harness/harness.py bridge-status
EXIT=0
```

Refusals:

```
$ python3 tools/practitioner_harness/harness.py brief --project root --deliverable DEL-01-01
ERROR: brief does not support --project root: `brief` projects a tranche brief from the working root's DAG pointer and a write fence under that root. The root adapter (root-harness-adapter/v1, execution/_harness/adapter.yaml) declares no dag_pointer, and the root working root IS the repository root, so no containing fence can be derived from it. Refusing rather than emitting a brief with a guessed pointer and a repo-wide fence (K-INVENT-1).
EXIT=2

$ python3 tools/practitioner_harness/harness.py next --project root
ERROR: next does not support --project root: `next` emits a ready-made `brief` command line per active deliverable, and `brief` does not support the root working root (run `brief --project root` for the reason). Refusing rather than emitting a pick-list whose commands would not run (K-INVENT-1). Use `status --project root` for the root's per-state counts.
EXIT=2

$ python3 tools/practitioner_harness/harness.py drift --project root --all
ERROR: drift --all audits the pilot projects only; --project root must be requested on its own. Refusing rather than silently dropping the requested root.
EXIT=2
```

Guards:

```
$ python3 tools/validation/validate_root_harness_adapter.py
G1 PASS: root harness adapter execution/_harness/adapter.yaml is schema-valid (root-harness-adapter/v1); declared pointers exist and pinned baselines match the observed tree (status_files=45, pinned_at=653fabc9b3e8abf369f5e776a7d3ee24bf235e7a).
G1: materialized root packages/deliverables observed: PKG-01_…, PKG-02_…, PKG-03_…, PKG-04_…, PKG-05_…, PKG-06_…
EXIT=0

$ python3 tools/validation/validate_path_anchors.py
PASS: no literal home-dir absolute paths found in 996 live path-anchor surfaces
EXIT=0
```

```
$ git status --porcelain     # (45 `?? …/_SEMANTIC.md` lines from Agent 0's
                             #  concurrent work elided for readability)
 M agents/AGENT_CHANGE.md                                             # Agent 0
 M execution/_Coordination/LOOP_RECEIPTS.md                            # Agent 0
 M execution/_Coordination/WORKPLAN_2026-07-25_root_product_development.md  # Agent 0
 M tools/practitioner_harness/README.md                                # H1
 M tools/practitioner_harness/adapter_loader.py                        # H1
 M tools/practitioner_harness/adapter_project.py                       # H1
 M tools/practitioner_harness/cmd_drift.py                             # H1
 M tools/practitioner_harness/cmd_status.py                            # H1
 M tools/practitioner_harness/harness.py                               # H1
?? execution/_Coordination/AgentRuns/ROOT-CLOSEOUT-20260725/           # brief + this return
?? tools/practitioner_harness/test_root_adoption.py                    # H1
```

Every H1-attributed path is under `tools/practitioner_harness/**` plus this
return. The remaining entries are Agent 0's concurrent tranche work.

## 6. Constraint confirmations

- Write scope honored: `tools/practitioner_harness/**` + this return only. No
  writes to `tools/validation/`, `docs/`, `agents/`, CI workflows, or the root
  adapter.
- No commits, no branches, no pushes. Working tree only.
- Python 3 stdlib + pyyaml only; no new dependencies.
- No machine-absolute paths in any changed file (grep for `/Users/`, `/home/`,
  `C:\` over all seven files: none) — and `validate_path_anchors.py` PASSes.
- `app-dev`, `piping`, `pec` behavior unchanged: `status --project app-dev`,
  `drift --project piping`, and `self-check` outputs are byte-identical to
  pre-change captures (diff clean); all 311 pre-existing tests pass unmodified.
- The G1 validator was neither weakened nor duplicated; it still PASSes.
- A transient `_harness_generated/` created during a `--json-report` spot-check
  was removed; the tree carries no stray generated output.

## 7. Open items (for Agent 0 / the tranche manifest)

1. **Tranche manifest** — `docs/governance_harness/tranche_manifests/ROOT-CLOSEOUT-20260725.yaml`
   is Agent 0's to author; it must list the seven `tools/practitioner_harness/`
   paths above.
2. **G1 docstring reason 3 is now stale** — `tools/validation/validate_root_harness_adapter.py`
   lines 31–34 still read "the root is not in it… Adopting the root into the
   practitioner-harness project table… is a recorded open item". That open item
   is now closed. Correcting the docstring is outside this brief's write scope;
   it is a one-paragraph follow-up for a `tools/validation/`-scoped act.
3. **Root decision-register parsing** — `status --project root` reports
   "No rows parsed" for `docs/governance_harness/_DECISIONS/_REGISTER.md`
   (the register's table shape does not carry the `| ID | … | State | … |`
   header the project-shaped parser matches). This is truthful and sourced, not
   an error, but if a root register count is wanted the register shape or the
   parser is a separate, deliberate decision — not something to guess.
4. **Live pin discipline** — the 45/0 live pins in `test_root_adoption.py` and
   `baselines.*` in the root adapter must move together; any root
   materialization change updates both in the same PR, consciously.
5. **Root fence citizenship remains unopened** — if root-scoped tranche briefs
   are ever wanted (`run-validations` / `scope-check` on a root fence), that
   needs a deliberate decision about what a root write fence means; it is not
   implied by this adoption.
