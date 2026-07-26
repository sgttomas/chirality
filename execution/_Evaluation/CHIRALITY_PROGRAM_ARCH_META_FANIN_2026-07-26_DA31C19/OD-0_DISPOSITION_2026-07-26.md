# OD-0 Disposition — Incidental Bytecode Preservation Exception

Date: 2026-07-26
Status: OWNER-APPROVED
Applies to: evidence-only Git closeout of
`CHIRALITY_PROGRAM_ARCH_META_FANIN_2026-07-26_DA31C19`

## Ruling

The two Python bytecode-cache files listed below are excluded from Git. They
are incidental, non-relied artifacts ignored by the repository's
`**/__pycache__/` rule. No review finding, meta-review conclusion, owner
decision, or package-admission verdict depends on either file.

Their observed paths, byte counts, and SHA-256 identities remain in this
record and in `SOURCE_IDENTITY_MANIFEST.csv`. The two manifest rows are
annotated `PASS_OBSERVED_OD0_GIT_EXCEPTION`; this preserves the successful
source-to-copy identity observation without representing the cache bytes as
part of the durable Git corpus.

| Observed package path | Bytes | SHA-256 | Git disposition |
|---|---:|---|---|
| `source_reviews/independent_managed/__pycache__/build_frozen_manifest.cpython-313.pyc` | 17,485 | `af89e297e465acbd6733d246caf796b08c16a6ba9005c0f2d98a09785e1b41ea` | EXCEPTED / NOT STAGED |
| `source_reviews/independent_managed/__pycache__/validate_review_artifacts.cpython-313.pyc` | 25,302 | `d09061cbaabf3a4a15aa5767ecc6a2f86e518d3778e81fffc049c6b92d427e9d` | EXCEPTED / NOT STAGED |

## Recoverability

The exact bytes remain recoverable from the non-governed loss-insurance
archive:

`/Users/ryan/dev/chirality-review-safety-2026-07-26-DA31C19.tar`

Archive SHA-256:
`2d41947d7fb68625d01d46034e73b1676808e4c9a0f6a6e8438d948c4ffe7417`

On 2026-07-26, the archive checksum was reverified and its table of contents
was rechecked for both bytecode paths:

- `Users/ryan/.codex/worktrees/d9d0/chirality/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19/__pycache__/build_frozen_manifest.cpython-313.pyc`
- `Users/ryan/.codex/worktrees/d9d0/chirality/execution/_Evaluation/CHIRALITY_PROGRAM_ARCH_TANDEM_2026-07-26_DA31C19/__pycache__/validate_review_artifacts.cpython-313.pyc`

The safety archive is loss insurance and is not part of the governed
evaluation package.

## Additive correction and final publication counts

This disposition is additive. It does not rewrite the already-backchecked
`FINAL_VALIDATION.md`, `EVALUATION_REPORT.md`, or
`SUPERVISORY_META_FANIN.md`.

The pre-disposition local package contained 113 files: 112 files covered by
`ARTIFACT_HASHES.sha256` plus the hash list itself. The durable Git candidate
adds this disposition and excludes the two bytecode caches. Its terminal
shape is therefore:

- 112 files in the Git candidate;
- 111 entries in the regenerated `ARTIFACT_HASHES.sha256`;
- the hash list itself excluded from its own contents.

## Git diff-check disposition

The full staged `git diff --check` reports only pre-existing whitespace
warnings in package records that were already source-preserved, hash-frozen,
or adversarially backchecked before OD-0. Those bytes are retained unchanged
under the owner's additive-only instruction. The OD-0 disposition,
`SOURCE_IDENTITY_MANIFEST.csv`, and `ARTIFACT_HASHES.sha256` are checked
separately and introduce no whitespace error.

`ARTIFACT_HASHES.sha256` is regenerated last and must verify end-to-end before
staging.
