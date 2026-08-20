# N2 Frozen Candidate Manifest

- **Run:** `APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20`
- **Node:** `N2 / WI-PKG02-API-KEY-PRECEDENCE-01`
- **Basis:** `6710ee6354debc201f6a454e2802897026cd4b38`
- **Frozen at:** 2026-08-20T16:17:00Z
- **Review requirement:** fresh, read-only, 100% product-source review

## Accepted N1 dependency

| Path | SHA-256 |
|---|---|
| `projects/chirality-app-dev/frontend/electron/api-key-storage.ts` | `d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db` |
| `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts` | `c9cadac32f892613a3a0b3e3f9afb8200b14ab375408f5ea89c23e53b817dac4` |

Accepted handoff: `instances/WI-PKG04-API-KEY-PRECEDENCE-01/HANDOFF_STATE_V2.md`.

## N2 product and test candidate

| Path | SHA-256 |
|---|---|
| `projects/chirality-app-dev/frontend/electron/api-key-ipc.ts` | `3293cbf15164105ac61f7cc7e34da66c5c12701823a6e302f90d59c385eed3cb` |
| `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-ipc.test.ts` | `818b7424ef1de3f4418486a4a7ae839cb837d84a23af6fdd73621f847d74b1a6` |

## DEL-02-05 calibration candidate

| Path | SHA-256 |
|---|---|
| `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/Assessment_INSP-03_DEL-02-05.md` | `16a4a05ae44e9841159786cc39563c5cc24e1acf351d0ba21b701a91b50b9871` |
| `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_STATUS.md` | `0a8026a73416f04948d2ed7d6c1671f9197f2caefbbb04985e86b981eb2aaad1` |
| `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/MEMORY.md` | `0b726ce28a27e6145a693ab40859b035bcf685f33b2a0f40595aa3818e89dfbd` |
| `projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback/_run_records/TASK_RUN_2026-08-20_1004.md` | `a733ed10535ca359e9e3a65e47571fbea09560eb45b0d5ecc06fdb51ee7566fc` |

## Verification evidence

| Path | SHA-256 |
|---|---|
| `instances/TASK-PKG02-API-KEY-STATUS-CONSUMER-IMPLEMENT-01/RETURN.md` | `eb3ad48074e4bc851f800616cb58293a8c25d14b2fef7cf3d413d78c0c38fb02` |
| `instances/TASK-PKG02-API-KEY-STATUS-CONSUMER-IMPLEMENT-01/STATUS.json` | `46bff3e7242d72633d2af1e1363cea3f9a4f5b246c0a77a090a4c659ba8df159` |
| `instances/WI-PKG02-API-KEY-PRECEDENCE-01/N2_MANAGER_REGISTERED_CHECKS.json` | `8d4d90e749ac281b90e389ebc5ad51fb4dab14c5705d57f2575718cf6ee146f4` |
| `instances/WI-PKG02-API-KEY-PRECEDENCE-01/N2_MANAGER_HARNESS_PYTEST.json` | `9c8b98d535568983f58b0c10e6df8c38390dfb3d5ff15611e129ec95b81354aa` |
| `instances/WI-PKG02-API-KEY-PRECEDENCE-01/N2_APP_HOLD_RELIANCE_FINAL.json` | `cb1cc5f91ce60928706939263681054a6a94ad7dc347145fa44bf7da2b7bade3` |
| `instances/WI-PKG02-API-KEY-PRECEDENCE-01/secret-scan/secret-scan-summary.json` | `9ef7b72e4bc00e2129b50d8eb08bff0bf46589a2724ce0f94be1a500de8815a3` |

The implementation return records focused Vitest 3 files / 47 tests; full
frontend 150 files / 1,174 tests with one file / four tests skipped;
typecheck, build, 350 harness tests, harness self-check, APP-HOLD integrity, exact scope, and
whitespace PASS. The final secret scan covers 5,846 files with zero blocked
findings.

Review 01 found zero product defects and one evidence-only blocker: several
registered checks were summarized but not persisted in normalized JSON. The
manager-owned `N2_MANAGER_REGISTERED_CHECKS.json` closes that finding with all
six declared checks passing over unchanged product and deliverable bytes.

Any hash mismatch invalidates this review candidate.
