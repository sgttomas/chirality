# Human Ruling and CHANGE Closeout Amendment

Date: 2026-07-14

Authority: human direction in the controlling Codex task

Applies to: `SOW-PKG02-BATCH-EXPERIMENT-20260714-01`

## Ruling

The human accepts the PKG-02 experimental ordinary-package result as
sufficient for adoption together with the already completed PKG-01
experimental result. Plan, instruction, integration, pull-request, and merge
changes remain later work and are not authorized by this evidence commit.

The human also accepts the 55 `git diff --cached --check` findings in 33 files
as an immutable-evidence variance: 28 trailing-whitespace findings and 27
blank-line-at-EOF findings. The affected files are copied experimental
evidence bound by accepted manifests. Their bytes must remain unchanged so
that the six manifests and their accepted snapshots continue to reproduce.

Accordingly, CHANGE is authorized to create the scoped evidence commit while
retaining and reporting these warnings as approved warnings, not as a passing
whitespace check.

## CHANGE validation basis

- Branch: `codex/adopt-pkg-batch-workflow`
- Parent basis: `3efa950aa981f9d3491bab2ab3b3319a5a2c6d5c`
- Pre-amendment staged evidence: 1,933 paths, all under this run root
- Manifest validation: six manifests and 1,960 rows rehashed successfully;
  hashes and byte counts passed, and all binding text line counts passed
- Structured validation: 402 JSON files and three JSONL files parsed
- Containment: no staged path outside this run root; no symlink in the run
- Exclusions: unrelated dirty paths remain untouched and unstaged
- Push and pull request: explicitly deferred

This amendment is additive root-level closeout evidence and is not part of an
already-sealed child, package, or reconciliation manifest.
