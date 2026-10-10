# Development verification

`harness` is the single required GitHub result. It combines repository checks
with the selected App v4 and Piping workflows.
Branch protection does not require an up-to-date branch merely because main
advanced; checks still apply to the candidate head.

Selection uses the complete PR diff, including both sides of renamed paths.
The executable mapping is [hosted-ci-routing.json](../tools/hosted-ci-routing.json),
interpreted by [hosted_ci.py](../tools/software_workflow/hosted_ci.py).
Missing or unknown inputs select conservative coverage. Each job reports its
selection and reasons; unrelated product jobs are explicitly skipped. Failed,
cancelled or missing selected work fails the aggregate result.

Routine PRs use focused checks of consequential behaviour. Full App v4 suites,
broad browser matrices and other expanded checks are available through manual
workflow dispatch or release preparation. There is no blanket local sweep,
nightly duplicate or post-merge duplicate requirement. Do not repeat a passing
hosted suite locally without a new change or unresolved concern.

Repository checks retain conflict/secret detection and relevant tool tests.
Dependency YAML edits select the structural deliverable check; unresolved needs
and cycles are reported without failing. Role and workflow package changes
select the checks for those consumed formats. The tool-test mapping is
[tools-test-routing.json](../tools/tools-test-routing.json).

Piping's [CI strategy](../projects/chirality-piping/docs/CI_STRATEGY.md) describes
its numerical, persistence, browser and Python selection. Numerical and browser
results can be reused only for identical tracked inputs, selected commands and
runner/language environment. A reused pass names its original run and says no
tests executed. Manual runs bypass result reuse. Dependency/build caches are
separate and do not themselves establish a passing result.

Verification is proportional to consequence under Root `AGENTS.md`. CI success
is not product acceptance, engineering approval or release authorization.

App v3, Runtime and PEC are retired and have no verification jobs or dependency
builds. Historical App packaging and instruction-root reproduction use a checkout
of `archive/pre-docs-cleanup-1`. Their source remains available without an ongoing
CI maintenance obligation.
