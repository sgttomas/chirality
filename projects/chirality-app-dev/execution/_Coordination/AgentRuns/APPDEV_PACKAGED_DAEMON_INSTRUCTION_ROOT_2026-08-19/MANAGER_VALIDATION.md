# Manager validation

- Accepted basis: `219f695d348f1d83ba904ef4dd38781636b423a6`; D-APP-100 B1; APP-HOLD dispatch/scan PASS; corpus v18 no drift.
- Focused regression: `PASS`, 3 files / 12 tests.
- Full Vitest: `PASS`, 147 files plus one skipped file; 1139 tests pass / four skip.
- Typecheck: `PASS`.
- Production build: `PASS`.
- Section 9: `PASS`, governed 16-check inventory.
- Unsigned desktop pack: `PASS`; packaged dependency boundary and instruction-root integrity `PASS`.
- Packaged isolation: `PASS`, invocation `710ca7e3-3fa3-4bf9-9511-50ca94c5b00e`; all nine checks true. App identity SHA-256 `97ab8a2af2e648ba1ac3cb6c54409f3b7fa62694eb56d767ff3c4192893d651d`; executable `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`; `app.asar` `76b64915179e1971b8835a64347ad16c6f08386b6a6a2cdfe72aad6dcff422f0`; bundled CLI `3adc8490634427b814cbebbf93563851f0794f59715b82d4b26415a5aa0cc9a4`.
- Resolver result: initial packaged-resources fallback classified `PROJECT_NOT_FOUND`; after bundled-CLI registration the packaged daemon resolved the manifest instruction root to the repository root; both daemon stops exited code 0.
- Release quality: `pass_with_skips`; full test/typecheck/Section 9 pass. Registered `frontend-premerge` launched its owned Next service successfully but returned FAIL because local runtime-daemon project binding requests returned HTTP 503; PR CI owes this binding-backed row.
- Independent review: attempt 01 FAIL drove four proof remediations; invalidated attempts 02–04 were interrupted on changed diffs; final fresh attempt 05 `PASS`, no actionable findings.
- Repository checks: receipt validator PASS; authority corpus v18 eight MATCH/no drift; APP-HOLD 53 clear/register match; self-check exit 0 at existing 4 REVIEW / 31 WARN baseline; practitioner harness 349 passed; `git diff --check` PASS.
- Boundaries: no runtime/manifest/dependency/lockfile change; no lifecycle or Checking Approval SHA change; no signing/notarization/distribution/release-readiness act; no commit/push/receipt act.
