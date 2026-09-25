# Pull-request CI selection

PRs automatically run the checks justified by their complete changed-file set.
Use a workflow's **Run workflow** action on the candidate branch when full
coverage is wanted. These choices select evidence; they do not change scope,
review, acceptance, native verification or release requirements.

| PR contents | Hosted checks |
|---|---|
| Deliverable records, coordination notices, project loop prose | Governance harness; product selectors report not applicable. Documents used as executable validation inputs retain their consumer checks. |
| Root instructions, bundled workflows/skills and packaged instruction assets | Governance harness and App instruction-bundle construction/integrity. No App server or browser setup. |
| App frontend, application configuration or public App export | Full App/Runtime pre-merge integration. |
| Runtime source, tests, dependencies or configuration | Full App/Runtime integration and PEC workspace tests. |
| PEC source, tests, fixtures or configuration | PEC workspace tests with its Runtime dependency. |
| Piping desktop, core, fixtures, schemas, examples or Piping CI | Existing Piping lean, affected, changed-spec or full selection. |
| Piping validation, Python tests or non-CI project tools | Piping numerical suite only; browser selector reports not applicable. |
| Routing policy or unknown input | Full checks for the affected product consumers; unknown shared inputs select full product coverage. |

Mixed PRs take the union of their required checks. Selectors inspect the complete
merge-base-to-head diff, including both old and new paths of a rename. A missing
diff selects full coverage. Failed selection or a failed, cancelled or skipped
required job fails the corresponding result check. A not-applicable product
result explicitly states that no product tests ran.

## Existing selection machinery

App/PEC hosted jobs use `tools/hosted-ci-routing.json` through the same
`select_affected_checks.py` function used by project software profiles.
`tools/software_workflow/hosted_ci.py` binds that selection to the PR's base and
head, retains matched paths and fallback reasons, and checks the selected job
results. Unknown paths remain visible in the selection artifact.

The App's project-local `software-workflow.json` still selects local checks.
The hosted profile describes GitHub job groups and cross-project consumers,
including packaged instruction checks, rather than changing local commands.
Full App coverage still includes its instruction-bundle check.

Piping retains `projects/chirality-piping/tools/ci/e2e_plan.py` and its
[source-coverage policy](../projects/chirality-piping/docs/CI_STRATEGY.md).
Piping is self-contained below its project directory: root directories other
than its own workflow and setup action (execution records, root tools,
instruction packages, exports) are non-inputs for both its desktop and
numerical suites; root-level build files remain conservative inputs.
Pull-request runs execute every desktop-profile identity and the compact
profile only for layout/viewport specs; a manual full dispatch keeps both
profiles in full. Piping jobs skip checking out
`execution/` run evidence, which none of them read.

The governance harness remains on every PR. Its tools tests continue to use
`tools/tools-test-routing.json`; live-tree governance gates remain mandatory.
The always-run practitioner-harness suite is also the self-check gate: its live
baseline module runs the self-check once and requires no BLOCK finding or
identity refusal, and CI sets `CHIRALITY_REQUIRE_LIVE_TESTS=1` so those tests
fail rather than skip. Its checkout omits binary run evidence (archives, images,
databases) under `_Coordination/AgentRuns`, which no gate or test reads; governed
binaries elsewhere are still checked out. Under D-GOV-45, run records are
history and are not tested: governance-harness scans only the run records a
change adds or modifies, for credentials (BLOCK) and files over 5 MB (WARN).
Closed run records are archived out of the working tree by
`tools/archive_agent_runs.py`; references into them resolve to the archive tag.
Main pushes and manually requested governance runs retain the full tools estate.
Existing stable check names and branch-protection configuration are unchanged.

Selection artifacts (`app-ci-selection`, `pec-ci-selection`, and
`piping-e2e-selection`) preserve the candidate, examined diff, selection and
reasons. App/PEC job summaries also state the selected mode.

## Request full coverage

In GitHub Actions, choose the workflow and **Run workflow**, selecting the
candidate branch. Equivalent CLI commands are:

```sh
gh workflow run harness-premerge.yml --ref <candidate-branch>
gh workflow run pec-tests.yml --ref <candidate-branch>
gh workflow run piping-desktop-e2e.yml --ref <candidate-branch> -f target_base=<integrated-base-sha>
gh workflow run governance-harness.yml --ref <candidate-branch>
```

Each request runs that workflow's full coverage. Piping validates its optional
explicit target base against the candidate; supply it for a retarget/integration
proof. A manual result belongs to the selected revision, so recheck the candidate
after later changes. Labels and PR-body edits do not select reduced coverage or
start competing runs. Unsigned artifact verification retains its existing
separate trigger and qualification boundary.
