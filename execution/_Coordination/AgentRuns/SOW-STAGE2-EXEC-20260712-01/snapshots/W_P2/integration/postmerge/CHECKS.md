# W-P2 Postmerge Checks

Verdict: `PASS`.

- Exact live replacement target hashes: 145/145 rows.
- Clean `SOW_V1`: 29/29 members; four legacy files absent for each.
- Preserved status/control/context/reference/dependency hashes: PASS.
- Project containment against the accepted basis: exact 145 paths.
- Exact replacement/inverse manifests and 29 rollback simulations: PASS;
  rollback not executed.
- Dependency schema: 29/29 PASS.
- Practitioner self-check: accepted baseline, no W-P2 finding.
- Practitioner harness: 264 tests PASS.
- Agent, skill, path-anchor, and instruction-entrypoint validators: PASS.
- Public-export/Scope-of-Work tests: 20 PASS.
- Strict project-range `git diff --check`: PASS.
- PR required check on exact source head: SUCCESS.
