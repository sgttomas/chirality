# Node O independent-review handoff

Review 100% of `git diff e2f8317dadb8ac95b7aff5ac5637d967fb7e6d40..<FROZEN_HEAD>` from a fresh detached worktree at the frozen head. The reviewer is read-only with respect to the candidate branch and must return an immutable report plus PASS only when there are zero BLOCKER and zero MAJOR findings.

## Required determinations

1. Verify ancestry, exact basis, clean frozen head, and that every changed path is inside only these pre-review write loci:
   - the existing DEL-09-01 Node H evidence bundle, limited to revision-3 evidence/index additions;
   - `_run_records/TASK_RUN_2026-09-04_NODE_O.md`;
   - `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_O_2026-09-04/**`.
2. Prove no tracked `frontend/**`, `runtime/**`, `.github/**`, product, test, CSS, hardened-runner, or comparator byte changed in the candidate.
3. Verify the trigger from live tree: accepted revision 2 basis `ede175910c67b384332324622b17695f69e6a715`; PR #695 changes the named `frontend/electron/**` surfaces; intervening PR #696 is plan-only/non-triggering.
4. Recompute source/evaluator identities and every sorted SHA-256 manifest. Validate every retained JSON with duplicate-key and non-finite rejection and every SSE `data:` payload as JSON.
5. Inspect the retained failed attempt and ensure it is not conflated with a pass. Verify the successful run's exact environment, command, exit results, machine summaries, checkout cleanliness, daemon/project binding, containment, and cleanup evidence.
6. Rerun the unchanged comparator between revision 3 and accepted revision 2 and require `BEHAVIOUR_PROJECTIONS_EQUAL=true`, exact required-ID order, overall and per-row pass, and retired-ID absence.
7. On a host capable of the accepted method, rerun `rerun-section8-local.sh` unchanged from a clean detached frozen-head checkout using fresh disposable state and `WITH_RELEASE_QUALITY=1`; require real premerge and release-quality passes and complete teardown. Do not repair the runner in review.
8. Rerun runtime install/build as needed; frontend typecheck, focused and full Vitest, and build; registered `harness-self-check`, `app-hold-integrity`, and `harness-pytest` using `/Users/ryan/.local/share/mise/installs/python/3.13/bin/python3`; receipt validation; corpus status; SOW; exact change-scope; APP-HOLD; secret/host-identifier and F-APP-2 scans; and `git diff --check`.
9. Confirm the A1 declaration is present and calibrated: ignored/generated frontend writes occurred; historical R20 remains historical; this agent-run proof is not fresh owner proof and creates no reliance entitlement.
10. Confirm the package makes no lifecycle, G5/G6a, live-provider, host-act, signing, notarization, publication, distribution, certification, professional, or release-readiness claim. D-APP-36 visual comparison is not applicable only if no tracked UI/product byte changed.

## Evidence identities expected

- Basis: `e2f8317dadb8ac95b7aff5ac5637d967fb7e6d40`.
- Accepted revision 2: `ede175910c67b384332324622b17695f69e6a715`.
- Clean runner commit cited: `9dfbb7962cd22b56b1899d10c05c3e97f2a10d2f`.
- Revision-3 Section 8 summary SHA-256: `ee89c9ce35acbdfb09c7ba44b354e35a86aa9db7d557f92d85080081270bbc82`.
- Revision-3 release-quality summary SHA-256: `c8599f2f5580b109718a854cf8ad19aef363d4eecaec703428e34b39a13b07ac`.
- Revision-3 successful-run manifest SHA-256: `14291495dfb8f270631143a02cc869969af599e72b56b6848a4f196b9f0edb82`.

The reviewer must write its own launch/status/return/report records only in its separate scratchpad or supervisor-authorized review record location. No reviewer is claimed to exist by this handoff itself.
