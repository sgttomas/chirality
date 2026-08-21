# Validation

## Private repository

- Destination: `git@github.com:sgttomas/chirality-domains.git`
- GitHub visibility observed after creation: `Private`
- Pushed HEAD: `5f4c6ffdeefa300521f800f3c50cd27b5fd32a39`
- Migration tag: `migration-2026-08-20`
- Clean-clone verification path: `/private/tmp/chirality-domains-verify.sOpibe/repo`
- Clean-clone tag tree:
  `migration-2026-08-20:domains = b35c91f027ce5a50eeaa99294c0f4be3c06cb9d7`
- The verified clone contained all four `chirality.project/v2` manifests and
  the external-repository cutover notice, and had a clean worktree.

## Local-only domain files

- Every registered Chirality worktree was inspected for untracked, ignored,
  and PDF files under `domains/`.
- Result: zero non-ignored untracked files and zero PDFs in every worktree.
- The original checkout contained only two ignored `.DS_Store` files (12,296
  bytes total). These disposable macOS metadata files were not migrated.
- The private repository ignores future raw `_Sources` binaries, local
  indexes, work areas, runtime state, and build outputs. Such files may remain
  local without being uploaded to GitHub.

## Candidate integrity

- Re-fetched `origin/main` before deletion:
  `1c5945c4cab675f98db24917148b4251d9c52b9e`.
- `origin/main:domains`, the migration tag, and the pre-deletion candidate all
  resolved to `b35c91f027ce5a50eeaa99294c0f4be3c06cb9d7`.
- No registered worktree had a dirty domain path.
- Post-deletion candidate: 36,450 staged deletions, zero tracked paths under
  `domains/`, and `/domains/` protected by the root `.gitignore` rule.

## Tests and validators

- Runtime typecheck: PASS.
- Runtime full Vitest suite: 79 passed.
- Frontend typecheck: PASS.
- Frontend full Vitest suite: 1,199 passed, 4 skipped.
- Python validation/source-catalog set: 320 passed.
- Full `tools/` Pytest estate: 1,143 passed, 3 skipped, 1 pre-existing
  `PytestReturnNotNoneWarning`.
- PR-sized affected-test routing dry-run: PASS with 36,000+ changed paths
  streamed as JSON on standard input; the selector no longer depends on the
  operating system's command-line argument limit.
- Agent-instruction validator: 34 files, 0 errors, 0 warnings.
- Skill metadata validator: 45 valid, 0 invalid.
- G4 instruction-tranche validator: PASS, including commit-pinned external
  notice routes.
- Public release projection: 833 files, zero boundary findings.
- Candidate whitespace: `git diff --check` and `git diff --cached --check`
  PASS.

The first sandboxed runtime/frontend test attempts could not bind local Unix
sockets or loopback listeners (`EPERM`). Both complete suites were rerun with
the required local IPC permission and passed; the sandbox failures were
environmental, not test failures in the candidate.

PR #596's first governance-harness run exposed a routing-infrastructure limit:
the runner supplied every changed path to the selector as a command-line
argument and Linux rejected the 36,000+ argument vector with `E2BIG`. The
runner now streams the exact path list as JSON on standard input. A 40,000-path
regression test, the actual PR-sized dry-run, and the full tools estate pass.

## Publication audit

- Current-tree secret scan: PASS; 46,081 files scanned, zero blocked findings,
  21 allowed fixture findings.
- Reachable-history audit: 93,624 unique blobs scanned; zero unresolved
  findings. All 28 Anthropic-key-shaped matches and all 58 credential-in-URL
  matches were test, fixture, redaction, or documented threat examples.
- Largest reachable blob: 77,692,253 bytes
  (`domains/chirality-piping/_Decomposition/cross_source_toc_matrix.csv`),
  below GitHub's 100 MB hard limit. GitHub emitted its expected advisory for
  exceeding the recommended 50 MB threshold when the private snapshot was
  pushed.
- History policy remains snapshot-only: Chirality history is not rewritten,
  so historical domain material remains reachable in Chirality after the
  current-tree deletion. This is deliberate and was accepted for the public
  cutover; the deletion removes the domain corpus from future checked-out
  trees and worktrees, not from existing Git object history.

## Remaining human gates

- Exact-candidate approval is required before merge because the tranche amends
  ratified doctrine and `agents/AGENT_TASK.md`.
- Chirality repository visibility remains private until after the approved
  candidate is merged and the final GitHub settings review is complete.
