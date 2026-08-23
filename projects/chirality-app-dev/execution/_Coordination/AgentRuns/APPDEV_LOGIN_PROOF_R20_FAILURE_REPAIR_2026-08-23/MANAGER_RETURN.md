# WORKING_ITEMS manager return — Phase A

- Run / instance: `APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23` / `WI-PKG09-R20-REPAIR-01`.
- Package / deliverable: `PKG-09 / DEL-09-04` only.
- Basis: branch `codex/app-login-proof-r20-repair`; exact HEAD/origin-main `a702dd6ec5005b361c8c023b12b599a425e5e2b8`; frontend tree `9c1b1d9cec8c45a2a74e78c79ce37d784938a6e4`.
- Result: `PHASE_A_VALIDATED_PASS`; ready for CHANGE to create the final frontend-touching source commit. Phase B is not released until HELP_HUMAN/CHANGE returns that exact commit.
- Root cause: the verbatim R19 launchctl fixture proves a running exact-owned job at PID 34924, runs 1, and exact `(never exited)`. The pre-repair integer-only cleanup parser rejected that sentinel before exact-owned bootout; cleanup also removed diagnostic state without sufficient job/process/refusal and failure-log gates.
- Final source identities: harness script `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`; focused test `6750655e8c7150bce8e6d12bf0e968de9129b80598309c317bea044b40c6ef18`; verbatim fixture `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531` at 3,049 bytes.
- Final diff: two tracked frontend files at 754 insertions / 28 deletions, binary-diff SHA-256 `65ff7075146a0a3c11f16de2431e2d9d829979c11184b9bc7d2cc3b6086d752b`, plus the one verbatim fixture.
- Behavior: exact sentinel parsing with all other noninteger/empty forms fail-closed; exact-owned running bootout; no destructive cleanup on refusal, loaded job, or live proof PID; token-aware two-log preservation for every non-PASS; macOS-compatible canonical-ancestor and O_NOFOLLOW held-descriptor identity snapshots; capture requires both logs; PASS-only copy removal cannot retroactively produce FAIL.
- Failure rule: initial fresh review returned five findings. Repair cycle 1 stopped at its focused gate because macOS rejected `/dev/fd` directory traversal. Owner-authorized final cycle 2 removed that mechanism and passed. Both failed artifacts remain immutable.
- Validation: final syntax PASS; exact focused Vitest 72/72 PASS; typecheck PASS; fixture regular/non-symlink/byte identity PASS; APP-HOLD `ALLOW`; parser and macOS O_NOFOLLOW probes PASS; diff/whitespace, App containment, JSON/JSONL, and empty index PASS.
- Fresh final review: `PASS`, no actionable finding, F-01 through F-05 closed; `REVIEW.md` SHA-256 `51e1e7fa1c3a716eb47e3a2b719acdca61f390f3f250894e9e8410e9c532982b`. The remaining helper/test complexity was independently judged bounded and proportional.
- Execution attribution: delegated-harness-native descendants used sealed briefs. Agent-2 role, freshness, and non-delegation evidence are `instruction-asserted`; role was not mechanically enforced. No descendant delegated.
- Explicitly not run: full `npm test`, build/package, final R20/status/Receipt 191, network, Git integration, proof procedure, GUI, launchd/plist/bootstrap/kickstart/logout/login, default operator query/mutation, prohibited private-root/Desktop reads, signing, notarization, deployment, distribution, or release claim.
- Derivative disposition: this run root is governed execution evidence, not proof acceptance, lifecycle truth, release authority, or a substitute for the eventual DEL run record.
- Requested action: CHANGE creates one scoped commit containing exactly the candidate inventory below and returns its exact 40-character commit. Do not build or begin Phase B in CHANGE.

## Exact 39-path candidate inventory

1. `projects/chirality-app-dev/frontend/scripts/run-packaged-launchagent-login-proof.mjs`
2. `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`
3. `projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt`
4. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/ACTIVATION.md`
5. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/AMENDMENT_01_FAILURE_LOG_FINAL_STATUS_COVERAGE.md`
6. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/CHAT_TRANSCRIPTION.md`
7. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/DISPOSITION_01_IMPLEMENTER_RETURN.md`
8. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/EXECUTION_ATTRIBUTION.md`
9. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/HANDOFF_STATE.md`
10. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/MANAGER_RETURN.md`
11. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/ORCHESTRATION_PLAN.md`
12. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/ORCHESTRATION_PLAN_V2.md`
13. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/ORCHESTRATION_PLAN_V3.md`
14. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/RUNTIME_EVENTS.jsonl`
15. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/RUNTIME_SUMMARY.json`
16. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/WORK_GRAPH.json`
17. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/WORK_GRAPH_V2.json`
18. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/WORK_GRAPH_V3.json`
19. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-IMPLEMENT-01.md`
20. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-REPAIR-01.md`
21. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-REPAIR-02.md`
22. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-REVIEW-01.md`
23. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/briefs/A2-PKG09-R20-REVIEW-R2-01.md`
24. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/ACTIVATION_AND_WORK_GRAPH.md`
25. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/CHECKS.md`
26. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/RETURN.md`
27. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/ROOT_CAUSE.md`
28. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-1/ACTIVATION.md`
29. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-1/CHECKS.md`
30. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-1/REPAIR.md`
31. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-1/RETURN.md`
32. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-2/ACTIVATION.md`
33. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-2/CHECKS.md`
34. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-2/REPAIR.md`
35. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-IMPLEMENT-01/repair-cycle-2/RETURN.md`
36. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-REVIEW-01/ACTIVATION_AND_REVIEW_BOUNDARY.md`
37. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-REVIEW-01/REVIEW.md`
38. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-REVIEW-R2-01/ACTIVATION_AND_REVIEW_BOUNDARY.md`
39. `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R20_FAILURE_REPAIR_2026-08-23/instances/A2-PKG09-R20-REVIEW-R2-01/REVIEW.md`
