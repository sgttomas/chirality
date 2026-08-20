# N1 remediation 01 return

## Status

`SUCCESS`

All five R1 proof-glue/evidence findings are closed within the sealed write
fence. Focused, full, build, root, secret, source-host, packaging, packaged-host,
instruction-root, whitespace, APP-HOLD, and write-containment checks pass. The
separate accepted production API-key precedence blocker remains unchanged, so
packaged-security product acceptance remains failed/held outside this node.

## Exact changed paths

- `projects/chirality-app-dev/frontend/scripts/run-network-policy-proof.mjs`
- `projects/chirality-app-dev/frontend/scripts/run-packaged-security-proof.mjs`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-network-policy-proof.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Packaged_Security_Proof_2026-08-20/Remediation_01/**`
- `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_run_records/TASK_RUN_2026-08-20_0047.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20/REMEDIATION_CHECKS_01.json`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20/REMEDIATION_RETURN_01.md`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_SECURITY_PROOF_2026-08-20/STATUS_REMEDIATION_01.json`

No prior frozen/evidence record, production Electron/runtime/provider source,
deliverable status/memory, lifecycle, shared surface, dependency/lockfile,
governance surface, or foreign-loop file was edited.

## Per-finding closure

1. **Source renderer egress — CLOSED.** Source capture now enumerates the full
   Electron descendant tree, records root/descendant PIDs, associates TCP with
   the child PID, records DNS-to-IP allowlist evidence, and rejects empty or
   otherwise unusable lsof capture. Credited attempt 3 has 4/4 usable snapshots,
   four Electron descendants, observed renderer-child loopback and Anthropic
   TCP, and zero non-allowlisted endpoints. The proof explicitly records that
   provider execution is not exercised by this renderer-egress surface.
2. **Packaged credential proof — CLOSED.** oMLX is re-queried after Anthropic
   store and remove. The generated fixture is checked after operations and
   stream closure across the encrypted bytes and every emitted proof artifact;
   no fixture is retained. Negative regressions cover operation-time leakage
   and cross-provider mutation.
3. **Packaged cleanup — CLOSED.** Cleanup errors propagate into normalized
   state; GUI and daemon shutdown plus log-stream closure and temp-root removal
   are recorded and required by the final PASS predicate. Host evidence is
   confirmed PASS.
4. **Source credential fence — CLOSED.** All project provider credential
   variables are scrubbed before build/Next/Electron child launch. A single
   unmistakable non-secret fixture is supplied only when the non-stub proof
   requires a value. Regression coverage passes.
5. **Attempt-history calibration — CLOSED.** The original first source attempt
   remains byte-preserved. `ATTEMPT_HISTORY_CALIBRATION.md` records that it
   launched Electron with the owner's default user-data path, had no pre/post
   filesystem audit, and cannot support the prior global no-owner-write claim.
   All credited remediation reruns isolate user data from process start.

## Final checks and host evidence

- Focused proof regressions: **PASS**, 2 files / 11 tests.
- Full registered checks: **PASS**, 150 frontend files passed / 1 skipped;
  1158 tests passed / 1 expected accepted-precedence failure / 4 skipped;
  typecheck PASS; build PASS; 350 root harness tests PASS; APP-HOLD PASS.
- Mandated mise-Python root self-check: **PASS**.
- Source network proof attempt 3: **PASS** under approved host escalation.
- Fresh `npm run desktop:dist`: **PASS** under approved host escalation.
- Instruction-root integrity: **PASS**, 43/43 checked.
- Packaged host proof: **PASS** under approved host escalation; fresh packaged
  identity `3da8cbbbd5cd543dce0c400975cf42b2bdfadd0b8dc6ccd61aab6489c38acee5`.
- Secret scan: **PASS**, 5772 files / 0 blocked findings.
- Write containment and `git diff --check`: **PASS**.

All failed remediation attempts remain below `Remediation_01/` and are named in
`REMEDIATION_CHECKS_01.json`; none was rewritten as a pass. No host rerun is
required.

## Accepted blocker, residuals, and recommendation

`frontend/electron/api-key-storage.ts` remains untouched. Its reversed
environment fallback precedence is the accepted separate blocker owned by
DEL-02-05 R03 / DEL-04-05 RQ-001 under `RECORD/HOLD scope widening`. The
self-expiring expected failure remains in the full suite. DEL-09-06 and
DEL-09-04 remain open and no Remaining item, lifecycle field, memory, or
Approval SHA changed.

Manager recommendation: freeze the corrected candidate plus this versioned
remediation package and dispatch a new fresh 100% read-only review. Do not infer
packaged-security acceptance or residual removal from this remediation PASS.
No commit, push, PR, merge, release, publication, or delegation was performed.
