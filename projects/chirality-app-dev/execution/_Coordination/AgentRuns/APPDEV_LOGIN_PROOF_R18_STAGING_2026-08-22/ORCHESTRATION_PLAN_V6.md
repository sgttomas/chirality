# R18 repair cycle 1 plus full-suite cure — orchestration plan v6

Status: `WHITESPACE REPAIR ACTIVE; FULL-SUITE CURE HELD ON REPAIR RETURN`

This version preserves v5 whitespace lineage and adds the owner-directed
R15/R17 full-suite cure. The two executor write sets are disjoint: whitespace
executor owns exactly five evidence files; cure executor later owns retained
test evidence, R18/status documentation, and the harvest-only TM candidate.

## Graph

1. Complete `A2-PKG09-R18-WS-REPAIR-01` and accept exact lineage.
2. Fresh `A2-PKG09-R18-FULLTEST-CURE-01` freezes source/test/package hashes and
   candidate diff; runs exact `npm test` once with local loopback/Unix-socket
   bind permission; proves no intervening source/test change; updates R18,
   status, and harvest-only TM handoff. No network command or source change.
3. WORKING_ITEMS refreshes candidate freeze and releases fresh
   `A2-PKG09-R18-WS-REVIEW-01` to review both repair/cure evidence without an
   unrestricted rerun.

## Cure acceptance

- Exact command count one: `npm test`, cwd `frontend`, local test-socket
  permission only; no network tool/request.
- Exact five frontend candidate paths and full candidate diff are byte/hash
  identical before and after.
- Retained sandbox diagnostic remains 21 failed / 1,246 passed / 4 skipped and
  classified `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`.
- Unrestricted exact rerun PASS counts are captured in a complete log.
- R18/status record both, do not upgrade the diagnostic, and name future PR
  pre-merge `full_test` + typecheck as independent confirmation not yet seen.
- TM candidate is harvested only; no implementation/register disposition.
- Package/build/network remain untouched and evidence-only/non-adopted.

No additional full-suite run, pack, network, source/test/package change,
R19/proof, receipt, stage, commit, push, PR, or merge.
