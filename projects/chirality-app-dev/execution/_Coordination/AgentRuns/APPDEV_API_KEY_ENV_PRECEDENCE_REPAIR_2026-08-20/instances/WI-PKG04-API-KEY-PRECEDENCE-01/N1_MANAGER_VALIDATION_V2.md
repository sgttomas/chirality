# N1 manager validation — amendment v2

Accepted basis: `6710ee6354debc201f6a454e2802897026cd4b38`
Frozen graph: `ORCHESTRATION_PLAN_V2.md` / `WORK_GRAPH_V2.md`
Scope: PKG-04-owned source fact in `api-key-storage.ts` and its focused test.

## Product identity

- `frontend/electron/api-key-storage.ts` SHA-256
  `d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db`.
- `frontend/src/__tests__/electron/api-key-storage.test.ts` SHA-256
  `c9cadac32f892613a3a0b3e3f9afb8200b14ab375408f5ea89c23e53b817dac4`.
- Exact basis diff: two files, 143 insertions, 19 deletions.

The amended store uses one provider-isolated resolver for `get` and `status`.
`status` returns only `{ configured, source }`, where `source` is
`ui | env | none`; no credential value is returned. Persisted safeStorage/UI
remains first, followed by `ANTHROPIC_API_KEY`, then
`CHIRALITY_ANTHROPIC_API_KEY`. oMLX continues to use only its persisted value
or `CHIRALITY_OMLX_API_KEY`. Unsupported providers return unconfigured/none.

## Verification

- focused API-key storage Vitest: PASS, 1 file / 20 tests;
- full frontend Vitest: PASS, 150 files passed and 1 skipped; 1,167 tests
  passed and 4 skipped;
- frontend plus Electron typecheck: PASS;
- frontend build: PASS;
- practitioner harness: PASS, 350 tests;
- repository self-check: PASS, exit 0; the existing unrelated baseline remains
  4 REVIEW and 31 WARN findings;
- APP-HOLD integrity: PASS, register matches and zero deliverables are held;
- APP-HOLD reliance: ALLOW for DEL-04-05, DEL-02-05, DEL-09-06, and DEL-09-04;
  register SHA-256
  `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`
  and scan fingerprint
  `8df9d9bd5151935d593ea5e6b51393aa31ed29d036dd15d9c1be476115d83c66`;
- secret scan: PASS, 5,833 scanned files, zero blocked findings, 21 allowed
  fixtures;
- explicit two-path scope validation: PASS, zero violations;
- exact two-path `git diff --check`: PASS.

The implementation did not edit IPC, root runtime contracts, dependencies,
lockfiles, other packages, lifecycle, Checking Approval SHA, shared fan-in,
receipt, completion log, or Git state. N2 remains held until a fresh read-only
review passes over this frozen amendment identity.
