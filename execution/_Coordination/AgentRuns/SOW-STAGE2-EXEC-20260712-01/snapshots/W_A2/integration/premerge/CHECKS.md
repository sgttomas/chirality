# W-A2 Integration Premerge Checks

Verdict: `PASS — READY FOR REMOTE VALIDATION`

| Gate | Result |
|---|---|
| Accepted snapshot manifest | PASS — 16/16; SHA-256 `0dbf05dec12668517f3b34097d15afdb5bff3a9bfa9f73569f614883238b000d` |
| Acceptance bindings | PASS — 13/13 |
| Deterministic reconciliation rerun | PASS — zero frozen-byte changes |
| Replacement / rollback | PASS — 80 rows; exact 80-row inverse |
| Evidence binding | PASS — `c6aa2050d23910423bd86c83f09da0247cbfe89e`; 1,188 governed A2 files; zero project paths |
| Serial architecture | PASS — 16 ordered content commits |
| Per-commit containment | PASS — each content commit exactly five manifest paths |
| Candidate identity | PASS — 16/16 |
| Legacy absence | PASS — 64/64 |
| SOW resolver | PASS — 16/16 `SOW_V1`; zero dual/partial/invalid |
| Status identity | PASS — 16/16 |
| Lifecycle | PASS — 16/16 `IN_PROGRESS` |
| Exact project range | PASS — 80 paths; no other project path |
| Project diff hygiene | PASS — zero findings |
| Harness self-check | PASS — INFO 15, NOT_APPLICABLE 2, REVIEW 27, WARN 6; no BLOCK |
| Governance harness | PASS — 264 passed |
| Frontend typecheck | PASS |
| Frontend tests | PASS — 97 files / 713 tests; 1 file / 4 tests skipped |
| Frontend build | PASS |
| Live-stub premerge | PASS — Section 8 8/8; Section 9 report-only 16/16 |
| Excluded / unrelated paths | PASS — `.claude-worktrees/**` absent from branch |
| Findings / blockers / unknowns / waivers | none |

The evidence-binding commit's 122 diff-check diagnostic lines are confined to
immutable accepted upstream evidence (intentional Markdown hard breaks or
terminal blank lines). Mutable CHANGE evidence and all 16 project content
commits have zero findings. No accepted byte was rewritten to suppress a
diagnostic. Check-generated ignored artifacts remain outside Git.
