# W-A3 Independent Reconciliation Checks

Overall verdict: `PASS`.

| Gate | Result |
|---|---|
| Frozen population / package ownership | PASS — 16, split 5/6/5 |
| Live source/status/control identity | PASS — 144/144 |
| Package manifests | PASS — 220/220 |
| Accepted child statuses/manifests | PASS — 32/32 terminal surfaces, 1,470/1,470 bindings |
| Candidate identity | PASS — 16/16 |
| Standalone / authorized dual format | PASS — 16/16 `SOW_V1`; 16/16 `MIGRATION_DUAL` with exact D-GOV-16 authority |
| Claim map / full source-line parity | PASS — 481 PRESERVED mappings, 4,985/4,985 lines |
| Checklist and render determinism | PASS — 16/16; zero active external resource/script findings |
| Partial and unauthorized-dual negatives | PASS_FAIL_CLOSED — 16/16 each |
| Replacement / inverse rollback | PASS — 80/80, exact inverse, disjoint, status/control excluded |
| Isolated apply | PASS — 16/16 `SOW_V1`, status/control preserved |
| Isolated rollback | PASS — 16/16 exact legacy tree restored |
| Registered App checks | PASS — each package preserves five base PASS checks and expected no-server premerge FAIL |
| Server-backed frontend-premerge | PASS — 3/3; Section 8 8/8 and Section 9 16/16 report-only |
| Portability | PASS — 151 classified checkout-root occurrences; zero machine-temp or unclassified occurrences |
| Recovery/failure history | PASS — preserved and classified; no predecessor evidence repaired |
| Lifecycle and authority | PASS — 16 IN_PROGRESS, non-pilot, non-ISSUED; derivative only |
| Project read-only containment | PASS — zero project dirty paths |
| Main identity | PASS — local HEAD and origin/main equal frozen main |
| Diff hygiene | PASS |

The deterministic reproduction record is
`detailed/REPRODUCTION_SUMMARY.json`; exact normalized binding ledgers and
recovery classifications are under `detailed/`. Blockers, waivers, unknowns,
stale bindings, missing outputs, decision needs, and rerun requirements at
these identities: none.
