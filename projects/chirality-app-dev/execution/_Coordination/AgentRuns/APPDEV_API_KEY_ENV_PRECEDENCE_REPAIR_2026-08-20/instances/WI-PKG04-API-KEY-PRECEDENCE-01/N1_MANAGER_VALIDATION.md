# N1 manager validation — pre-rereview

Product identity remains the two bytes frozen in `FROZEN_DIFF_MANIFEST.md`:

- `frontend/electron/api-key-storage.ts` SHA-256
  `72e9cdb9fabb5beb77ba009933dbb8c1375f012ac0162e088d96a460fe5baaab`.
- `frontend/src/__tests__/electron/api-key-storage.test.ts` SHA-256
  `56b36a5ed44885877d692ad6357b6ee209f96edb8844aec2f5781d6c0a5b4fe7`.

Validated results:

- focused API-key storage Vitest: PASS, 1 file / 18 tests;
- full frontend Vitest: PASS, 150 files passed, 1 skipped; 1,165 tests
  passed, 4 skipped;
- frontend plus Electron typecheck: PASS;
- frontend build: PASS;
- practitioner harness: PASS, 350 tests;
- repository self-check: exit 0; existing baseline remains 4 REVIEW and 31
  WARN findings, all outside N1 scope;
- APP-HOLD integrity scan: PASS, register match, zero held deliverables;
- APP-HOLD reliance check for DEL-04-05: ALLOW, active/scanned held sets empty,
  register SHA-256
  `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`,
  scan fingerprint
  `8df9d9bd5151935d593ea5e6b51393aa31ed29d036dd15d9c1be476115d83c66`;
- secret scan: PASS, 5,810 scanned files, zero blocked findings, 21 allowed
  fixtures; summary SHA-256
  `bfd22271383a95c8e6a68ca279bd8e5ee1529233520333e58d956a5d232fd0b0`;
- tracked diff whitespace: PASS;
- explicit-path implementation scope validation: PASS, zero violations.

The machine-readable frontend results are in the implementation TASK record;
the manager-only harness/self-check/APP-HOLD integrity results are in
`N1_MANAGER_REGISTERED_CHECKS.json` (PASS). No lifecycle transition,
Checking Approval SHA change, dependency/lock change, provider expansion,
release claim, or product edit was introduced by the evidence remediation.
