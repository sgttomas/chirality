# Plan amendment v1.4 — actual ordering and first-pass findings

The prior graph incorrectly encoded N0 discover_other_lanes as a prerequisite of N1 CHANGE branch setup. Actual branch creation completed while the independent other-lane scan remained running. Parent had already verified the clean origin/main basis; N0 completion was neither required nor observed before creation. Current N1 depends_on is therefore empty. Historical plan and amendments v1–v1.3 are preserved; this correction does not assert an earlier discovery completion.

Selection effect remains limited to the initially lawful scopes and remains subject to current implementation boundaries, reviews and checks.

First-pass evidence is now available at validation/FIRST_PASS_FINDINGS.md; WORK_GRAPH.json records its observed hash. It reports build and basic checks passed, typecheck failed on a new test-fixture cast routed for bounded repair, full Vitest had one provider-fixture timeout, and premerge requests failed with HTTP 503 in a profile missing daemon-client bindings. The diagnosis is provisional, not a premerge waiver. No rerun PASS is anticipated. Follow the cited finding's owned-server diagnostic and rerun requirements; frontend login-proof re-stage consequence remains in force.

This is a derivative evidence/order correction only. No receipt, register, product, accepted pointer, historical amendment or manager-owned instance file is changed.
