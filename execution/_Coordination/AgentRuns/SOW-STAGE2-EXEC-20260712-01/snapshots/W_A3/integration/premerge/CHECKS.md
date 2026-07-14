# W-A3 Integration Premerge Checks

Verdict: `PASS — READY FOR REMOTE VALIDATION`

| Gate | Result |
|---|---|
| Accepted snapshot manifest | PASS — 19/19; SHA-256 `53fbec09f4d174f4de1744fdaf38b88f3d28ba2936b10cdc83087d1bbb76f10f` |
| Acceptance bindings | PASS — 15/15; SHA-256 `37bfceeb53e8eedbdbb481e9b777889d2f7abaaa370b4ffcc156db1e32e23ffc` |
| Replacement / rollback | PASS — 80 rows; exact 80-row inverse |
| Evidence binding | PASS — `0f8b1ddd8ddce76a7e8d2cac3fbd5bde65455ce0`; 1,634 governed A3 files; zero project paths |
| Serial architecture | PASS — 16 ordered content commits |
| Per-commit containment | PASS — each content commit exactly five manifest paths |
| Candidate identity | PASS — 16/16 |
| Legacy absence | PASS — 64/64 |
| SOW validator / resolver | PASS — 16/16 `SOW_V1`; zero dual/partial/invalid |
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
| Excluded / unrelated paths | PASS — Piping audit changes and `.claude-worktrees/**` absent from branch |
| Findings / blockers / unknowns / waivers | none |

The evidence-binding commit's 131 diff-check diagnostic lines are confined to
immutable accepted predecessor evidence: intentional Markdown hard breaks or
terminal blank lines. Mutable CHANGE evidence, all candidate files, and all
16 project content commits have zero findings. No accepted byte was rewritten
to suppress a diagnostic. Five accepted PKG-08 ADD rows carry
`source_path=-`; their exact carriers resolve one-to-one through the accepted
candidate manifest and reproduce the operation hashes.
