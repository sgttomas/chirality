# Performed checks and replay

Run date: 2026-09-30. Commands ran in `<repo>` using the installed standard-library
Python recorded in `CONTEXT.json`. No product build/test/model or heavy experiment
was invoked. Every script below completed with exit status 0.

From the repository root, let `review` be the repository-relative directory
`projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260930-T3-AUDIT-RESPONSE/instances/AUDIT-REVIEW`.

```sh
python3 -B "$review/independent_math.py"
python3 -B "$review/check_records.py"
python3 -B "$review/check_admissions_figures.py"
```

Captured stdout: `math_results.json`, `records_results.json`, and
`admission_figure_results.json`, respectively. Send later replay output to
owned scratch; do not overwrite these preserved results. Run the records
check before relying on admission/figure replay: it verifies the packet and
its principal source inputs against the sealed revisions. For later history,
use a source/evidence snapshot at the exact audit candidate; the records check
intentionally fails source drift. Its historical manifest scan assumes the
preserved T3 set, not arbitrary new future manifests.

The math probe was re-run after adding explicit checks that the verification
target does not alter the maxima. Its results are unchanged. It uses an
independently written exact integer rounding function and no audit/solver
imports. Admission replay uses independently written policy arithmetic with
assertions for the exercised branch, not the audit's runner import. The
script deliberately does not cover unexercised refusal branches.

Other performed checks:

- `git status --short`, `git diff --stat <base> <audit-head>`,
  `git diff --name-status <base> <audit-head>`: initial checkout clean;
  exactly 15 additive audit files. Later uncommitted changes belong to this
  and other authorized response owners, including ROOT's graph maintenance.
- `git show <revision>:<path>`, `git show -s --format=%P <merge>`,
  `git merge-base --is-ancestor <dispatch-base> <candidate>`, and bounded
  `git diff <candidate> <merge> -- projects/chirality-piping tools .github`:
  all six local identities/tree checks pass, with KF3's disclosed first-parent
  exception. `check_records.py` preserves the exact full SHA inputs through
  the frozen `merges.json` and checked Git objects.
- `git diff cef218a10 <audit-base> -- <FK>/src/structural/retained/factor.rs`:
  inspected the complete factor delta; no arithmetic-loop change found.
- `rg`, `sed`, `cat` and `nl -ba` source/document reads: consulted ranges and
  hashes are in `CONTEXT.json`; audit/reference role files were not activated
  as other roles. Initial exploratory misses for nonexistent `ROOT_RULINGS.md`,
  `recovery.rs`, and `core/product` were corrected to the actual paths. An
  exploratory record-schema read requested nonexistent key `kind`; the
  independent replay uses the actual `order/mode/model` schema and passes.
- Read-only `gh` queries are captured in `github_samples.json`. The first
  sandbox query failed to connect to api.github.com (exit 1); its subsequent
  shell subcommands did not run. The supported `require_escalated` read-only
  PR queries and the sampled dispatch query succeeded. No auto-review
  rejection, Git mutation or workflow dispatch occurred.
- Final JSON syntax/manifest/hash checks and a portable-path scan cover this
  owned review folder. This is records QA, not GEN-8 or product validation.

No fresh verification is claimed for DEC-025, GEN-8, Rust, mutation tests,
source solves, performance, M5 logs or M3 admission. The prior audit's own
commands were inspected; its arithmetic script was not used as this review's
oracle. Its historical figures/results were checked independently rather than
relaunching model binaries or downloading large gate artifacts.

Verify the review packet's `SHA256SUMS` from this directory. The manifest
includes `REVIEW.md`, context, commands, scripts and captured results, and
excludes itself. ROOT receives the report hash separately.
