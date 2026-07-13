# W-A1 Independent Reconciliation Checks

Overall verdict: `PASS`.

| Gate | Result |
|---|---|
| Frozen 15-member population and package ownership | PASS — 2/4/5/4 |
| Source/status/control/candidate identity | PASS — 15/15 |
| Current package manifests | PASS — 189/189 |
| Author/verifier terminal pairs | PASS — 15/15, 30 children |
| Schema and target resolution | PASS — 15/15 |
| Claim map and source-line parity | PASS — 456 mappings, 4,817/4,817 lines |
| Checklist identity/linkage | PASS — 15/15 |
| Render identity and script/external-resource safety | PASS — 15/15 |
| Partial input negative | PASS_FAIL_CLOSED — 15/15 |
| Unauthorized dual negative | PASS_FAIL_CLOSED — 15/15 |
| Replacement / inverse rollback | PASS — 75 / 75; status/control excluded |
| Isolated apply | PASS — 15/15 exact SOW_V1; status/control preserved |
| Isolated rollback | PASS — 15/15 exact legacy tree restored; candidate absent |
| PKG01 R1-to-R2 chain | PASS — two exact substitutions and reverse proofs |
| Generated-evidence portability | PASS — zero unclassified prefixes |
| harness-self-check | PASS |
| harness-pytest | PASS — 264 tests |
| frontend-typecheck | PASS |
| frontend-test | PASS — 713 passed, 4 skipped |
| frontend-build | PASS |
| frontend-premerge | PASS — Section 8: 8; Section 9 report-only: 16 |
| Project read-only containment | PASS — zero project dirty paths |
| Diff hygiene | PASS |

The first package fan-in held on a real PKG01 portability contradiction. That
hold and the 186-binding audit remain historical evidence. The versioned R2
owning-manager repair was independently rerun against 189 current bindings
before this verdict. App-check scratch attempts are recorded in
`detailed/APP_CHECKS.md`; only the final canonical-layout PASS attempts are
accepted.

Blockers, conflicts, stale bindings, missing outputs, waivers, human rulings,
and rerun requirements at these recorded identities: none.
