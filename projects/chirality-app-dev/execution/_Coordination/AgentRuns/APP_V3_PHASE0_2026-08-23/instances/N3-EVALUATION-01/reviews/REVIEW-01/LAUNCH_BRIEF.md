# Sealed N3 fresh review brief

- RequestedBy: `N3-EVALUATION-01` (`EVALUATION`, Agent 1).
- RunID: `APP_V3_PHASE0_2026-08-23`.
- ReviewID: `N3-EVALUATION-REVIEW-01`.
- RoleForm: fresh ephemeral Agent 2 evidence reviewer; delegation prohibited.
- AcceptedBasis: `origin/main` and HEAD both
  `3af765222bbd4f43a52dcbe17bd151c13942e5ac`; frontend tree
  `74e3dbe858b5a4e31d7bf4d3d5e9a7e7f13e76eb`.
- ReviewSubject:
  `projects/chirality-app-dev/execution/_Evaluation/V3_PREP_BASELINE_2026-08-23/REPORT.md`.
- ReviewQuestions:
  1. Does the report cover every N3 fact in the re-issued Phase-0 steer?
  2. Is every factual claim bound to an exact repo-relative path and live line,
     complete basis-blob SHA-256, and verbatim quoted line(s)?
  3. Do all citations reproduce from `origin/main` and do the hashes match the
     exact Git bytes?
  4. Are the Electron 43.1.1/43.2.0 authority, scanner `.jsonl`, tool-path,
     PEC-glob, sibling-overlap, RQG, release, and R20-seed interpretations
     calibrated without upgrading evidence or recommendations to authority?
  5. Are AT mappings grounded in quoted plan rows and expressly non-closing?
  6. Is the subject write scope assessment-only and frontend-free?
- PermittedTools: read-only filesystem/Git, `rg`, `sed`, `shasum`, and local
  deterministic parsing. No network.
- FixedWriteTarget:
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_PHASE0_2026-08-23/instances/N3-EVALUATION-01/reviews/REVIEW-01/`
  only.
- RequiredOutputs: `REVIEW.md`, `RETURN.md`, and final `STATUS.json`.
- Acceptance: `PASS` only with every required fact covered, all quotes/hashes
  reproducible, no material overstatement, zero actionable findings, and no
  scope violation. Otherwise `BLOCK` with exact location, evidence, impact,
  and bounded remediation direction.
- Prohibitions: do not edit the subject, code, frontend, contracts, registers,
  lifecycle/pointers, Git index/state, or any path outside the fixed target; do
  not commit, push, open/merge a PR, use network, or delegate.
