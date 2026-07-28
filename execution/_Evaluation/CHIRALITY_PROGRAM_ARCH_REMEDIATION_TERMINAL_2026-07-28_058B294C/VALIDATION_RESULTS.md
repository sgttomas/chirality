# Terminal validation results

**Basis:** `058b294c49fa2ddc760a520fe6b8a45dc82e7189`
**Verdict:** PASS WITH BOUNDED WARNINGS

| Check | Result |
|---|---|
| Root/App/PEC/Piping PRD and decomposition identities | PASS — eight expected SHA-256 identities reproduced |
| App and PEC hold/preflight tests plus domain profile, path-anchor, and Piping receipt tests | PASS — 45 tests and 72 subtests |
| App hold release | PASS — 0 active rows, 6 released targets, 53 contracts |
| PEC hold release | PASS — 0 active rows, 766 hashes, 32 contracts |
| App SCA-APP-006 Gate-5 live state | PASS — no changed/unexpected paths |
| PEC strict decomposition registers | PASS — 64 registers / 254 rows / 0 findings |
| Path anchors | PASS — 1,101 live surfaces, no literal home paths |
| Piping receipt contract | PASS |
| Practitioner harness self-check | WARNINGS — INFO 15 / N-A 1 / REVIEW 5 / WARN 24 |
| Live routed notices | PASS — 30/30 receiving-surface files exist |

The practitioner-harness findings are preserved as `TERM-007`; they are
bounded governance hygiene, including historical and current record defects,
not evidence that the named architecture boundary, carrier, hold, or
current-effect remediations failed.

The runnable validator requires the repository's configured Python
environment with `pytest` installed. It fails explicitly at that prerequisite
rather than misreporting a product-state failure.
