# MEMORY - DEL-09-06

## Decisions And Evidence

- 2026-08-20 - The selected D-APP-97 packaged-security residual passed against
  a fresh unsigned arm64 app built from the accepted N1/N2 API-key precedence
  bytes. Compact D-APP-99 evidence identity-binds the DMG, executable,
  `app.asar`, CLI, and extracted packaged main; focused/full gates,
  instruction-root and dependency boundaries, a 5,868-file secret scan, and
  the host safeStorage/network/renderer proof all passed. DEL-09-06 remains
  IN_PROGRESS for unrelated dependency and lifecycle closure; Checking
  Approval SHA, dependencies, F-APP-2, signing, notarization, distribution,
  publication, and release readiness are unchanged.
- 2026-08-01 - SCA-APP-007 corrected the physical ownership of 38 historical network-policy proof files by moving their two byte-identical bundles from the retired DEL-03-06 container into `Evidence/Historical_DEL-03-06/`. `PROVENANCE.md` and `MIGRATION_SHA256_MANIFEST.csv` retain old/new paths, source commits, historical tree identity, byte counts, and 38/38 SHA-256 parity. This provenance-only correction does not alter Remaining work, authorization, lifecycle, approval, release readiness, or the Checking Approval SHA.
- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-06-21 - ADQ-16 added `npm run proof:secret-scan`, ran the secret scan over git-tracked app-dev files plus generated harness evidence, ran `npm run proof:network-policy -- --runs 1 --idle-seconds 5 --idle-sample-seconds 5 --provider agentSdk --scripted-agent-sdk --output-dir artifacts/harness/network-policy/adq16-2026-06-21`, and reran the secret scan after network artifacts were generated. Evidence is recorded in `Evidence_ADQ-16_Secret_Network_Proof.md`. The final secret scan reported `status=pass`, 1734 scanned files, 0 blocked findings, and 10 allowed test fixtures. The network proof reported aggregate `PASS`, 1 scripted `agentSdk` run, 0 failed runs, 0 non-allowlisted endpoints, 1 blocked renderer diagnostic, and 1 network probe payload. No provider/network expansion, release-readiness claim, lifecycle issuance, professional approval, certification, sealing, authentication, or code-compliance acceptance changed.
- 2026-07-12 - D-APP-56 R5 P40 executed UPD-075, UPD-078: REF-006 current-state kit/register wording now agrees with D-APP-38 MATCH; dated source-warning and assessment history is preserved. No lifecycle transition.
- 2026-07-12 - D-APP-56 consolidated decision-application tranche recorded the applicable ruled ownership, mapping, gate-reaffirmation, or dated-deferral result for DEL-09-06; proposal-only source rows were not treated as human rulings, no unruled work was executed, and no lifecycle transition occurred.
