# W-A2 Independent Reconciliation Checks

Overall verdict: `PASS`.

| Gate | Result |
|---|---|
| Frozen population / package ownership | PASS — 16, split 5/5/6 |
| Live source/status/control identity | PASS — 144/144 |
| Package manifests | PASS — 208/208 |
| Child statuses/manifests | PASS — 32/32 statuses, 1,052/1,052 bindings |
| Candidate identity | PASS — 16/16 |
| Schema / target resolution | PASS — 16/16 SOW_V1 |
| Claim map / full source-line parity | PASS — 491 mappings, 5,584/5,584 lines |
| Checklist determinism | PASS — 16/16 |
| Render determinism / active-resource safety | PASS — 16/16 |
| Partial state negative | PASS_FAIL_CLOSED — 16/16 |
| Unauthorized dual state negative | PASS_FAIL_CLOSED — 16/16 |
| Replacement / inverse rollback | PASS — 80/80, disjoint, status/control excluded |
| Isolated apply | PASS — 16/16 SOW_V1, status/control preserved |
| Isolated rollback | PASS — 16/16 exact legacy tree restored |
| Registered App checks | PASS — each package retains five base PASS checks |
| Initial frontend-premerge substrate record | PASS — preserved no-server FAIL, zero tests where recorded |
| Server-backed frontend-premerge | PASS — 3/3; Section 8 8/8 and Section 9 16/16 report-only |
| Generated-evidence portability | PASS — zero unclassified machine/temp literals |
| Project read-only containment | PASS — zero project dirty paths |
| Diff hygiene | PASS |

DEL-04-05 contains the required literal `https://api.anthropic.com` as escaped
code content. Pairwise render hashes are identical and no active external
`href`/`src` or script exists; this is preserved policy content, not a render
safety finding.

The deterministic reproduction record is
`detailed/REPRODUCTION_SUMMARY.json`. Blockers, waivers, stale bindings,
missing outputs, human rulings, and rerun requirements at these identities:
none.

