# W-A2 Integration Postmerge Checks

Verdict: `PASS`

| Gate | Result |
|---|---|
| PR identity | PASS — #225; base `0af23f4709e1c95f6b2e0f19db80779bd4c968fa`; head `f496282e458fc27af48fb650ad4db7f182746f13` |
| PR source commits | PASS — 18/18 exact; 16 ordered content commits preserved |
| GitHub file inventory | PASS — 1,212 rows |
| Effective GitHub project operations | PASS — 80/80; SHA-256 `f8837dbb50c199d6864b74467b1f88e6c55387dbd8f70f71b0ce139aea8041e0` |
| No-rename project inventory | PASS — 80/80 exact |
| Required remote checks | PASS — 2/2 SUCCESS |
| Merge authority and method | PASS — blanket approval; merge commit preserving source commits |
| Merge commit | PASS — `e0f1d8be30879a943697fa9d85e63299f5b0a320`; second parent exact source head |
| Refs before closeout | PASS — local main/origin main/remote main synchronized; divergence 0/0 |
| Live state | PASS — 16/16 `SOW_V1`; zero legacy/dual/partial/invalid |
| Candidate / status / lifecycle | PASS — 16/16; `IN_PROGRESS` |
| Self-check | PASS — INFO 15, NOT_APPLICABLE 2, REVIEW 27, WARN 6; no BLOCK |
| Governance harness | PASS — 264 passed |
| Frontend | PASS — typecheck; 97 files / 713 tests; 1 file / 4 tests skipped; build |
| Live-stub premerge | PASS — Section 8 8/8; Section 9 report-only 16/16 |
| Dirty tracked paths | none |
| Findings / blockers / unknowns / waivers | none |

GitHub represents the 64 deleted production legacy files as renames into
byte-identical evidence copies. Its 16 added SOW paths plus 64
`previous_filename` rows reproduce the exact accepted 80 operations. The
local no-rename inventory independently reproduces all 80.
