# N1 implementer return

## Status

`FAILED`

The bounded proof implementation is valid and all final deterministic/host
proof surfaces pass. Packaged-security acceptance does not close because the
production environment fallback precedence remains reversed. This is a
product acceptance failure, not a host-proof deferral.

## Product changes

- Added `frontend/scripts/run-packaged-security-proof.mjs`: identity-bound
  packaged executable/asar/CLI hashes; isolated packaged daemon and GUI;
  safeStorage store/status/remove; encrypted blob mode/plaintext checks;
  process-tree/TCP capture; blocked renderer signal; metadata leak scan;
  fail-closed normalized summary.
- Added the `proof:packaged-security` non-release package alias and integrated
  it into the unsigned desktop artifact workflow with fail-closed summary and
  real-credential exclusion checks.
- Removed the source renderer-egress proof's obsolete owner-daemon/session-turn
  dependency while retaining isolated Electron/Next startup, renderer probes,
  descendant TCP capture, and fail-closed verdicts. Provider enforcement is
  separately covered by focused/full security tests.
- Added proof-script, CI workflow, contract-pin, unreadable/special attachment,
  and accepted-precedence executable regression coverage. The precedence case
  is deliberately `it.fails` until its semantic-owner production repair lands.

## Exact changed product paths

- `.github/workflows/desktop-release-template.yml`
- `projects/chirality-app-dev/frontend/package.json`
- `projects/chirality-app-dev/frontend/scripts/run-network-policy-proof.mjs`
- `projects/chirality-app-dev/frontend/scripts/run-packaged-security-proof.mjs`
- `projects/chirality-app-dev/frontend/src/__tests__/contract-pins.manifest.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-attachment-resolver.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/desktop-release-workflow.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`

## Evidence and run paths

- Producer package:
  `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Packaged_Security_Proof_2026-08-20/`
- Passing packaged host summary:
  `.../packaged-host-attempt-2/summary.json`
- Retained packaged fail-closed attempt:
  `.../packaged-host-attempt-1/packaged-daemon.log`
- Passing source network summary:
  `.../source-network-policy-attempt-3/summary.json`
- Retained source proof-loop attempts:
  `.../source-network-policy/` and `.../source-network-policy-attempt-2/`
- Final registered checks:
  `.../registered-product-checks-final.json`
- Instruction-root evidence: `.../instruction-root/summary.json` and
  `.../instruction-root/manifest.json`
- Final secret scan: `.../secret-scan-final/secret-scan-summary.json`
- DEL-09-04 derivative pointer:
  `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity/Evidence/Packaged_Security_Proof_2026-08-20/DEPENDENT_EVIDENCE.md`
- TASK record:
  `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_run_records/TASK_RUN_2026-08-19_2354.md`
- Normalized checks: `N1_CHECKS.json` in this RunID root.

The passing packaged subject is the fresh unsigned app at source revision
`357a58b56726feba49507534159c3fbc4656b818`, identity SHA-256
`4eba146b2f4a973c9f2b1e53629878502ecc76eace8508ad403dd959bcef5255`.

## Checks and host commands

`N1_CHECKS.json` contains every surface, command, attempt, result, and evidence
path. Final credited results are:

- Focused regressions: PASS, 9 files / 86 tests plus 1 expected failure.
- Full frontend Vitest: PASS, 149 files passed / 1 skipped; 1152 tests passed,
  1 expected failure, 4 skipped.
- Frontend + Electron typecheck: PASS.
- Registered build: PASS.
- APP-HOLD integrity: PASS, 53 CLEAR contracts, register match, 0 held.
- Mandated root self-check with the mise Python 3.13 interpreter: PASS.
- Final secret scan: PASS, 5731 scanned, 0 blocked findings.
- Source network proof final attempt: PASS.
- `npm run desktop:dist`: PASS; fresh unsigned app + arm64 DMG, dependency
  boundary PASS, instruction-root integrity PASS.
- Packaged host proof final attempt: PASS; real packaged bytes and host
  safeStorage/keychain/process/network surfaces exercised.
- Workflow YAML, change-scope validation, and `git diff --check`: PASS.

No host escalation is pending and no `HOST_RERUN_REQUIRED` classification is
used.

## Acceptance mapping

1. Fresh packaged-byte identity: **PASS**.
2. Fail-closed network/renderer proof and separate focused provider policy:
   **PASS**.
3. Key storage/redaction: **FAIL** only for the accepted environment fallback
   precedence; safeStorage encryption/removal/non-leakage portions pass.
4. Attachment enforcement/partial-total-failure/retry coverage: **PASS**.
5. Named deterministic, build, packaging, and host checks: **PASS**.
6. Residual removal: **NOT ELIGIBLE** because criterion 3 fails.
7. Write containment and exact evidence return: **PASS**.

## Deliverable effects

- DEL-09-06 remains `IN_PROGRESS`; its exact D-APP-97 R4-P49 Remaining item is
  unchanged.
- DEL-09-04 remains `IN_PROGRESS`; its REQ-009 / R4-P49 Remaining item and all
  unrelated Remaining items are unchanged.
- `_STATUS.md`, `MEMORY.md`, lifecycle, Checking Approval SHA, F-APP-2, and
  non-claims were not edited.

## Blocker and rerun

`frontend/electron/api-key-storage.ts` currently resolves
`CHIRALITY_ANTHROPIC_API_KEY` before `ANTHROPIC_API_KEY`, contrary to the
accepted DEL-09-06 order. Agent 0 disposition was
`RECORD/HOLD scope widening`: production repair is jointly owned by DEL-02-05
R03 and DEL-04-05 RQ-001. After that owner-scoped repair lands, rebuild and
rerun focused/full tests, secret scan, `desktop:dist`, instruction-root
integrity, and the packaged host proof against the new identity.

## Derivative status and manager recommendation

The DEL-09-06 evidence package and DEL-09-04 pointer are derivative execution
evidence tied to the accepted source basis; they do not substitute for
deliverable truth or authorize closure. Manager should accept and land the
bounded proof/test/CI product changes as partial engineering progress, retain
both Remaining items, route the precedence repair to its semantic owners, and
rerun packaged acceptance after that repair. No commit, push, PR, merge, or
lifecycle act was performed by this TASK child.
