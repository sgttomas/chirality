# WORKING_ITEMS manager return

- Manager: `WI-PKG09-LOGIN-PROOF-PREP-02`
- Coverage: exactly PKG-09 / DEL-09-04.
- Result: `PREPARATION_COMPLETE`; publishable pending Git integration and
  PR-CI.
- Restored reviewed candidate: frozen diff 04, script SHA
  `980e2e710ab66006baeefc14d400584bc8837f3ea3b35390db94b879413e2c20`,
  test SHA `f168e7d18326a536ff07b4e3a82019904bc43753fa3999acd439b8353171f01a`.
  Exact bytes are restored to the two live frontend candidate paths.
- Review: REVIEW-04 PASS, zero actionable findings, verified hashes/scope and
  100% of 902 product + 484 test lines. Earlier FAIL reviews and remediations
  are preserved as provenance.
- Integrated review chain: direct reviewer
  `A2-APPDEV-INTEGRATED-REVIEW-DIRECT-01` returned FAIL with three record-only
  findings and zero product findings; amendment 10 applied all three fixes;
  backcheck `A2-APPDEV-INTEGRATED-REVIEW-DIRECT-02` returned PASS with zero
  actionable findings, closed all three findings, and confirmed unchanged
  product hashes.
- Passing evidence: syntax; focused Vitest 15/15; exact scope; practitioner
  pytest 350; root harness self-check; APP-HOLD integrity; APP-HOLD dispatch
  preflight ALLOW.
- Final deterministic gates: registered typecheck/build/harness self-check/
  APP-HOLD integrity PASS; host full Vitest PASS (152 files + 1 skipped, 1,214
  tests + 4 skipped); focused affected trio PASS 35/35.
- Setup evidence: sandbox `npm ci` failed `ENOTFOUND`; exact escalated `npm ci`
  passed (753 packages, 762 audited, 15 existing advisories, no audit fix).
  Agent 0 rebuilt/relinked current root runtime only under ignored frontend
  dependencies; no tracked root/App setup file changed.
- Premerge calibration: `REGISTERED_CHECKS_PREMERGE_AGENT0.json` records managed
  Next service READY and check FAIL only because shared runtime daemon/project
  registration were absent (`HTTP 503`). No local product failure; premerge is
  PR-CI-owned and must rerun after PR through the full runtime lifecycle.
- Integration decision: the owner superseded the stop with **“Push through
  failures.”** Agent 0's ignored dependency rebuild cleared local deterministic
  gates without tracked root/App setup writes.
- Deliverable effect: DEL-09-04 remains IN_PROGRESS. Implementation preparation,
  local deterministic gates, and integrated review/backcheck are complete. Git/
  PR, PR-CI premerge, packaged identity, and the later owner act remain. No
  login-session proof or publication is claimed.
- Derivative status: run records and check JSON cite frozen product hashes and
  accepted R10/R11; they do not substitute for product truth.
- Runtime summary: `RUNTIME_SUMMARY.json`, `PARTIAL_MEASUREMENT`; predecessor
  telemetry initialization was absent, so timing/token/context data are not
  inferred. `EXECUTION_ATTRIBUTION.md` records actual engine/provider/model
  family for every governed dispatched role, substitutions included, with the
  exact model/build identifier limitation explicit.
- Reruns: PR-CI premerge after PR using the full runtime build/start/register
  lifecycle. Only after Git, CI, packaged identity, and owner scheduling may
  logout/login/capture run.
- Notices/decisions/waivers: no waiver; owner PREPARE-THEN-OWNER boundary held.
- Requested Agent 0 action: route CHANGE for Git/PR and require the PR-CI
  premerge lifecycle before any packaged owner procedure is released.
