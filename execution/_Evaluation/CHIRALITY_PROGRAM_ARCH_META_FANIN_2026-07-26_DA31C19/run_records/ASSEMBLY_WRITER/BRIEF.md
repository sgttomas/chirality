---
run-id: ASSEMBLY_WRITER_2026-07-26
timestamp: 2026-07-26T00:00:00-06:00
status: PENDING
agent-type: 2
agent-form: ephemeral-generalist
agent-role: serialized-integration-writer
engine: Codex
provider: OpenAI
model: gpt-5.6-sol
parent: EVALUATION Agent 1 (/root/evaluation_freeze)
supervising-agent: HELP_HUMAN Agent 0 (/root)
accepted-basis: da31c19b5656dd74615e308c4215688971d33dc9
---

# Sealed Brief — Evidence Assembly Writer

## Objective

As the sole Bash-bearing serialized integration writer, immediately preserve
the six named source packages byte-for-byte inside the one allowed package
root and create deterministic source/destination identity records. Do not
perform census or synthesis.

## Requested By

EVALUATION Agent 1 (`/root/evaluation_freeze`), under HELP_HUMAN Agent 0
(`/root`).

## Accepted Basis

Clean worktree:

`/Users/ryan/dev/chirality-meta-fanin-worktree`

Commit:

`da31c19b5656dd74615e308c4215688971d33dc9`

The basis and clean state must be verified before writes. Stop on mismatch.

## Read Scope

- The six exact source directories listed below.
- `/Users/ryan/dev/chirality-meta-fanin-worktree/AGENTS.md`
- `/Users/ryan/dev/chirality-meta-fanin-worktree/agents/AGENT_TASK.md`
- Git metadata required to verify the accepted basis.

## Sole Write Target

`/Users/ryan/dev/chirality-meta-fanin-worktree/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19/`

## Permitted Tools

- Read-only filesystem tools.
- Bash for deterministic `mkdir`, copy, `find`, `shasum`, and `diff` within
  declared scopes.
- `apply_patch` only inside the sole write target.
- No Git mutation.

## Source-to-Destination Map

1. `/Users/ryan/.codex/worktrees/d9d0/chirality/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19`
   → `source_reviews/independent_managed`
2. `/private/tmp/claude-501/-Users-ryan-dev-chirality--claude-worktrees-chirality-root-prd-inquiry-799a78/2f009cef-c385-4df3-8ea0-196308681f90/scratchpad/TANDEM_REVIEW_2026-07-26`
   → `source_reviews/root_managed`
3. `/Users/ryan/dev/chirality-tandem-review-2026-07-26`
   → `source_reviews/pec_managed`
4. `/private/tmp/chirality-comparative-meta-review-2026-07-26-codex-root`
   → `meta_reviews/independent_meta_1`
5. `/private/tmp/claude-501/-Users-ryan-dev-chirality--claude-worktrees-help-human-chirality-app-99df76/673bb00e-6fb9-4780-b9ad-7306bca3325f/scratchpad/META_REVIEW_TANDEM_2026-07-26`
   → `meta_reviews/independent_meta_2`
6. `/Users/ryan/dev/chirality/.claude/worktrees/help-human-chirality-app-99df76/plans/reviews/tandem_2026-07-26`
   → `excluded_supplemental/excluded_fourth_pass1`

## Byte-Preservation Requirements

- Copy every regular file byte-for-byte.
- Preserve directory layout and source filenames.
- Do not normalize, edit, rename, omit, or overwrite source artifacts.
- Do not follow symlinks as files.
- Inventory symlinks explicitly and stop if safe byte identity cannot be
  established.
- Stop if the package root preexists with content.

## Required Artifacts

- `SOURCE_IDENTITY_MANIFEST.csv`, one row per source regular file, with:
  `SourceLabel`, `SourceRoot`, `RelativePath`, `SourceSHA256`, `SourceBytes`,
  `DestinationPath`, `DestinationSHA256`, `DestinationBytes`,
  `IdentityVerdict`.
- `SOURCE_PACKAGE_SUMMARY.csv`.
- `INITIAL_ARTIFACT_HASHES.sha256`, covering all copied artifacts and identity
  records without recursively hashing itself.
- `COPY_VALIDATION.md`.
- `DERIVATIVE_STATUS.md`.
- `run_records/ASSEMBLY_WRITER/RETURN.md`.
- Generic TASK run record under the package `_run_records/` directory.

## Acceptance

- All sources are present.
- Every regular source file is copied exactly once.
- Relative paths are preserved.
- Source/destination SHA-256 and byte count match for every row.
- No writes occur outside the package root.
- Git basis remains unchanged.
- Report `PASS` only if all checks pass.

Escalate missing sources, preexisting destination content, symlinks or special
files, hash mismatch, or basis drift. Return exact artifact paths and hashes
to the parent. Do not begin census or author supervisory conclusions.

