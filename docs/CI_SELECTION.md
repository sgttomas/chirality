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
| Piping source or tests | Existing Piping lean, affected, changed-spec or full selection. |
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
Root agent/workflow packages and project AGENTS prose are classified as
non-product inputs for that desktop suite.

The governance harness remains on every PR. Its tools tests continue to use
`tools/tools-test-routing.json`; live-tree governance gates remain mandatory.
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
