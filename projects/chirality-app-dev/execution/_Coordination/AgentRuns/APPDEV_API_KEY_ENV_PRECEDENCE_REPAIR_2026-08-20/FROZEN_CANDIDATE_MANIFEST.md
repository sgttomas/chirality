# Frozen integrated candidate manifest

- RunID: `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- Frozen at: after N1, amended N1, N2, and N3 terminal implementation returns;
  before integrated review dispatch
- Branch: `codex/app-api-key-precedence-20260820`
- Basis / stacked PR base: `6710ee6354debc201f6a454e2802897026cd4b38`
- Candidate paths: `86`
- Product/test paths: `4`
- Evidence/state/control paths: `82`
- Aggregate SHA-256: `ee2623a620af684ed6b67a678466d46db186b4e590c9dd606f61542ff322acec`
- Raw N3 host proof retained through review:
  `/tmp/chirality-precedence-closure.pXvs6Z`

## Exact reconstruction

From repository root, excluding this manifest and the integrated-review launch,
status, and return controls created after the freeze:

```text
{ git diff --name-only --diff-filter=ACMRTUXB; git ls-files --others --exclude-standard; } | sort -u
```

The frozen aggregate is the SHA-256 of the newline-delimited per-file
`shasum -a 256` output in that exact sorted path order. The reviewer must
independently reconstruct exactly 86 paths and the aggregate above. Any other
path or hash is a failed identity check.

## Product/test identities

```text
d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db  projects/chirality-app-dev/frontend/electron/api-key-storage.ts
c9cadac32f892613a3a0b3e3f9afb8200b14ab375408f5ea89c23e53b817dac4  projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts
3293cbf15164105ac61f7cc7e34da66c5c12701823a6e302f90d59c385eed3cb  projects/chirality-app-dev/frontend/electron/api-key-ipc.ts
818b7424ef1de3f4418486a4a7ae839cb837d84a23af6fdd73621f847d74b1a6  projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-ipc.test.ts
```

## N3 compact evidence identities

```text
0ec3c501c1406210b30fb32509d972e7dd8b9f0e0686aa97e1e009eb40f82df3  projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Packaged_Security_Proof_2026-08-20_Precedence_Closure/summary.json
4fe82d2b2297b8665e4e2331762a78e2108e6184533cc0f365a4e8e22787ffc6  projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Packaged_Security_Proof_2026-08-20_Precedence_Closure/SUMMARY.md
```

## Review boundary

Review covers all 86 frozen paths semantically, all four product/test files in
full, and the raw host proof for backcheck. This manifest and the review's own
launch/status/return controls are inspected for consistency but excluded from
the 86-path aggregate. No candidate edit is permitted during review.
