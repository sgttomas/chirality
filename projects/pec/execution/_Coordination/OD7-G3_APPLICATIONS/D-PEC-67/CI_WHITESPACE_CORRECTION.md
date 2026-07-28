# D-PEC-67 Archive CSV Line-Ending Correction

**Date:** 2026-07-27
**Status:** BOUNDED CORRECTION CANDIDATE — NOT APPLIED
**Trigger:** PR #382 governance-harness run `30322867333`

## Finding

The accepted source package generated two CSV artifacts with CRLF line
endings. Their live archive copies are semantically correct and byte-identical
to the accepted source bytes, but the repository committed-range whitespace
gate reports each carriage return as trailing whitespace.

Affected archive copies:

| Path | Accepted CRLF SHA-256 | Corrected LF SHA-256 |
|---|---|---|
| `ACCEPTED_APPLICATION_MANIFEST.csv` | `188fa6db06b31ecd93af3b89acc43967234346b2cee45552ee47436f1bf1ea14` | `ce5d5aad3eaae369b3cf1832f842ec1c426f2611f27425aea81e654a5ea1a58c` |
| `SECTION_INDEX.csv` | `147dc6e712019f4926af6fdf8d5b7a5e5be8ce8741036ff6b75f2c30f304560d` | `baae879816b60ff46414e44c5d164fc92c9f2369c7dae204e25f6299e413a1cd` |

## Exact correction

Remove only the terminal carriage-return byte from every line of the two
archive copies. Preserve every field, comma, character, row, row order, and
terminal newline. `diff --strip-trailing-cr` must report no semantic
difference.

The frozen accepted source package remains unchanged. Its original identities
remain preserved in `ACCEPTED_TRANCHE_HASHES.sha256`; this record preserves
both original and normalized identities.

After normalization, update only `APPLIED_PATHS_AND_HASHES.csv` and
`ARTIFACT_HASHES.sha256` for the corrected hashes and this additive record,
then rerun all application and Git checks.

This correction changes no decision, authority, product requirement,
decomposition, ScopeOfWork, hold state, implementation, runtime, lifecycle,
release, dependency, estimate, or schedule semantics.
