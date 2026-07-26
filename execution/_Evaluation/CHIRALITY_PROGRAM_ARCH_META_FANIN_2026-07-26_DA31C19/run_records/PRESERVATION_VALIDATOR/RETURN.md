# Preservation Validator Return

RUN_STATUS: `PASS_WITH_WARNING`

Observed at `2026-07-26T19:49:11Z`.

## Independently reproduced results

- Basis: `da31c19b5656dd74615e308c4215688971d33dc9`
- Branch: `codex/chirality-program-architecture-meta-fanin`
- Tracked changes: none
- Changes outside authorized package: none
- Sources available: 6/6
- Source/destination files: 83/83
- Source/destination bytes: 1,882,678/1,882,678
- SHA-256 identities: 83/83
- Relative file and directory layouts: identical
- Symlinks or special files: none

| Package | Files | Bytes |
|---|---:|---:|
| Independent managed | 36 | 754,498 |
| Root managed | 13 | 305,229 |
| PEC managed | 13 | 377,322 |
| Independent meta 1 | 4 | 72,000 |
| Independent meta 2 | 5 | 70,476 |
| Excluded fourth pass | 12 | 303,153 |

The complete package contained 93 regular files totaling 1,946,665 bytes at
validation time, including ten administrative records.

## Registers and hashes

- `SOURCE_IDENTITY_MANIFEST.csv`: exact expected schema, 83 unique rows,
  83 `PASS`.
- `SOURCE_PACKAGE_SUMMARY.csv`: exact expected schema, six unique rows, six
  `PASS`; five relied and one excluded.
- `INITIAL_ARTIFACT_HASHES.sha256`: 88 unique entries, all verified.
- Coverage: all 83 replicas plus the five declared initial administrative
  records.
- Relied/excluded and derivative/non-authoritative labels are consistent.
- No census or supervisory synthesis was added during initial preservation.
- Parent, assembler, write scope, engine identity, and interrupted-terminal
  delivery disposition are internally consistent.

## Downstream warning

Two byte-preserved relied artifacts are ignored by `.gitignore`:

- `source_reviews/independent_managed/__pycache__/build_frozen_manifest.cpython-313.pyc`
- `source_reviews/independent_managed/__pycache__/validate_review_artifacts.cpython-313.pyc`

They are present and hash-correct, but ordinary `git add` will omit them.
`CHANGE` must force-add them or govern an explicit preservation exception.

## Limitations

Current state proves present byte identity, not historical package-root
nonexistence or initial cleanliness before assembly. The collaboration
interruption itself is evidenced only by the manager's durable disposition;
its claimed lack of file impact is corroborated by the independently
reproduced package state.

## Runtime

- Engine: Codex
- Provider: OpenAI
- Model: `gpt-5.6-sol`

