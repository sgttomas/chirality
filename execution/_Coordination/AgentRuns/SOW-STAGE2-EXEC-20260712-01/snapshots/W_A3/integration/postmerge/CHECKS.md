# W-A3 Integration Postmerge Checks

Verdict: `PASS`

| Gate | Result |
|---|---|
| PR identity | PASS — #226; base `193663b1d93299c18d64f59b543b36a0dd5f0ee1`; head `06dc10e90c60b933fdf0273d63fe164911bb68c3` |
| PR source commits | PASS — 18/18 exact; 16 ordered content commits preserved |
| GitHub file inventory | PASS — 1,658 rows |
| Effective GitHub project operations | PASS — 80/80; SHA-256 `744a5956c09b3a01c6717a3a6283893486cc92684b6e75c031fe60534ded15ff` |
| No-rename project inventory | PASS — 80/80 exact |
| Required remote checks | PASS — 2/2 SUCCESS |
| Merge authority and method | PASS — blanket approval; merge commit preserving source commits |
| Merge commit | PASS — `c7e3c1317d2cb96b8cda4505b8a434d343a12fdf`; second parent exact source head |
| Refs before evidence closeout | PASS — local main/origin main/remote main synchronized at merge commit; divergence 0/0 |
| Live state | PASS — 16/16 `SOW_V1`; zero legacy/dual/partial/invalid |
| Candidate / status / lifecycle | PASS — 16/16; `IN_PROGRESS` |
| Self-check | PASS — INFO 15, NOT_APPLICABLE 2, REVIEW 27, WARN 6; no BLOCK |
| Governance harness | PASS — 264 passed |
| Frontend | PASS — typecheck; 97 files / 713 tests; 1 file / 4 tests skipped; build |
| Live-stub premerge | PASS — Section 8 8/8; Section 9 report-only 16/16 |
| Governed/project dirty paths | none |
| Fenced unrelated state | PASS — four Piping audit paths preserved, uninspected, unstaged, and excluded |
| Findings / blockers / unknowns / waivers | none |

GitHub represents the 64 deleted production legacy files as renames into
byte-identical evidence copies. Its 16 added SOW paths plus 64
`previous_filename` rows reproduce the exact accepted 80 operations. The
local no-rename inventory independently reproduces all 80. Five accepted
PKG-08 ADD rows whose carrier marker is `source_path=-` remain bound through
the accepted candidate manifest and exact candidate hashes.
