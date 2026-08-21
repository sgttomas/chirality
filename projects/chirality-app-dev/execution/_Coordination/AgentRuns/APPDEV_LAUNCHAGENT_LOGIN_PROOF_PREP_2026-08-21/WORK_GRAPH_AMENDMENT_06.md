# Work graph amendment 06

- REVIEW-03 verdict: `FAIL`, one blocking P1 despite prior fixes.
- Finding: prepare marks installation only after the packaged CLI promise
  resolves. A timeout/rejection after the CLI has already written proof state
  can skip cleanup; post-install validation failures also discard cleanup
  outcome. This can leave persistent proof-only login-autostart state without
  truthful residual evidence.
- Dispatch exact two-file remediation
  `A2-PKG09-LOGIN-PROOF-PREP-REMEDIATE-03`, then fresh full-diff review.
- Required posture: once the install attempt begins, any failure must inspect
  and boundedly clean only provably proof-owned state; cleanup result/residuals
  must be surfaced fail-closed. No concurrent writes or authority expansion.
