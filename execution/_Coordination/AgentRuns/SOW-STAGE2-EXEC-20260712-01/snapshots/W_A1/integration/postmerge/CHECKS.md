# W-A1 Integration Postmerge Checks

Verdict: `PASS`

| Gate | Result |
|---|---|
| PR identity | PASS — #224; base `34b87ec77010035eeaa76f0fa65981ec57e78933`; head `fa66ba00eb95b85cb6c3b8d17f913528b3690fc3` |
| PR source commits | PASS — 17/17 exact; 15 ordered content commits preserved |
| GitHub file inventory | PASS — 1,268 rows; SHA-256 `3be2c08bbbb3fa32877ebeb8a3944e596b228640eb89673d9e3f9d6cac4535ce` |
| Effective GitHub project operations | PASS — 75/75; SHA-256 `eb795a4018d85b28e4b52842f149a92cf4a2c868292b7f50b91104fd39058d42` |
| No-rename project inventory | PASS — 75/75; SHA-256 `dc53fc27676dff65de0702b1ede2ffa2478084bce87affb2722a02563c1c38ee` |
| Required remote checks | PASS — 2/2 SUCCESS |
| Merge authority and method | PASS — blanket approval; merge commit preserving source commits |
| Merge commit | PASS — `3658f40fd492bf8d3db23892c2a9714f5ee915e6`; second parent exact source head |
| Refs before closeout | PASS — local main/origin/main/remote main synchronized; divergence 0/0 |
| Live state | PASS — 15/15 `SOW_V1`; zero legacy/dual/partial/invalid |
| Candidate / status / lifecycle | PASS — 15/15; `IN_PROGRESS` |
| Self-check | PASS — INFO 15, NOT_APPLICABLE 2, REVIEW 27, WARN 6; no BLOCK |
| Governance harness | PASS — 264 passed |
| Frontend | PASS — typecheck; 97 files / 713 tests; 1 file / 4 tests skipped; build |
| Live-stub premerge | PASS — Section 8 8/8; Section 9 report-only 16/16 |
| Dirty tracked paths | none |
| Findings / blockers / unknowns / waivers | none |

GitHub represents the 60 deleted production legacy files as renames into byte-identical evidence copies. Its 15 added SOW paths plus 60 `previous_filename` rows reproduce the exact accepted 75 operations. The local no-rename inventory independently reproduces all 75.
