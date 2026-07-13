# RECON-B1 Caller Closure Audit

Verdict: `PASS`

## Disposition and hash closure

All 64 root rows and nine App rows have a current accepted disposition.

- Root: 60 rows reproduce their recorded post hash directly. Four
  `OUT_OF_LANE_UNCHANGED` App surfaces reproduce the accepted App overlay:
  route test `64523601...ce7`, scanner regression `295fbb03...baf`,
  DocumentView `9dfe17e7...20b1`, and filesystem scanner
  `3f3a45c6...dc3f`.
- App: seven rows reproduce their initial final hash directly. The filesystem
  scanner and scanner regression reproduce the accepted C2A-R1 repair hashes
  `3f3a45c6...dc3f` and `295fbb03...baf`.

The six non-direct lane cells are explicitly superseded, not unknown. Their
current bytes match the accepted C2A/C2A-R1 return and P2 binding evidence.
There is no missing, ambiguous, stale, or unexplained caller hash.

## Commit-bound search refresh

The accepted original query was independently rerun with vocabulary
`Datasheet.md|Specification.md|Procedure.md|Guidance.md|four-documents|four documents|four-document`.
The targeted query used
`ScopeOfWork.md|SOW_V1|LEGACY_FOUR_DOC|PILOT_DUAL|MIGRATION_DUAL`.

| Set | Paths | Sorted-path SHA-256 |
|---|---:|---|
| original | 5,389 | `65170dfe26de49ffe1b0cc3f45ab4377523590bfb725c09da2fbb64b97773efa` |
| targeted | 196 | `902d81220c8a5e64fe16c9b9942c25c0627baaaddea4603a7ca5dada93e56af4` |
| union | 5,496 | `a7f244e9ccf677a662a19763abf536e7e537218e2d189d7943d81a1b7ba99ca9` |

Within active roots, the original set contains 76 paths: 49 exact manifest
rows, 19 P0-classified governance/history/thesis paths, six P0-classified
independent skills, and two P0-classified independent validators. The targeted
set contains 57: 51 exact manifest rows and six P0-classified governance
decision/proposal/history paths. This reproduces the accepted taxonomy and
leaves zero newly active or unclassified caller.

Caller verdict: `PASS`; drift `0`; unknown `0`; waived row `0`.
