# W-A1 Integration Premerge Checks

Verdict: `PASS — READY FOR REMOTE VALIDATION`

| Gate | Result |
|---|---|
| Accepted snapshot manifest | PASS — 23/23; SHA-256 `c8ae005ca8d1007ccf7f7ee12dc81f441ad65ae3fa094d7314249e747831a5eb` |
| Acceptance bindings | PASS — 12/12 |
| Replacement / rollback | PASS — 75 rows; exact 75-row inverse |
| Evidence binding | PASS — `63c26353b2930d03c8301478bae1f935918a9132`; 1,242 governed A1 files; zero project paths |
| Serial architecture | PASS — 15 ordered content commits |
| Per-commit containment | PASS — each content commit exactly five manifest paths |
| Candidate identity | PASS — 15/15 |
| Legacy absence | PASS — 60/60 |
| SOW resolver | PASS — 15/15 `SOW_V1`; zero dual/partial/invalid |
| Status identity | PASS — 15/15 |
| Lifecycle | PASS — 15/15 `IN_PROGRESS` |
| Exact project range | PASS — 75 paths; no other project path |
| Harness self-check | PASS — INFO 15, NOT_APPLICABLE 2, REVIEW 27, WARN 6; no BLOCK |
| Governance harness | PASS — 264 passed |
| Frontend typecheck | PASS |
| Frontend tests | PASS — 97 files / 713 tests; 1 file / 4 tests skipped |
| Frontend build | PASS |
| Live-stub premerge | PASS — Section 8 8/8; Section 9 report-only 16/16 |
| Containment / portability | PASS — generated checks ran in disposable canonical scratch; repository tracked state clean |
| Excluded / unrelated paths | PASS — `.claude-worktrees/**` absent from branch; no unrelated user path |
| Findings / blockers / unknowns / waivers | none |

## Diff-hygiene classification

Fourteen content commits have zero diff-check output. `DEL-03-02` has exactly 20 intentional Markdown two-space hard-break lines (40 diagnostic output lines), all in its immutable accepted `ScopeOfWork.md` candidate at SHA-256 `fa2694dc3b1e7145587c3ba48074122884c234e3461d2134b83f7fb82bccbfab`. The evidence-binding commit's findings are confined to accepted upstream evidence/candidate bytes already bound by the accepted snapshot. Mutable CHANGE evidence is normalized. No unclassified finding exists.

The initial disposable scratch materialization ended before `package.json` was copied and two npm commands failed with ENOENT before test execution. The scratch layout was repaired and all authoritative checks above reran to PASS. No scratch byte entered the repository.
