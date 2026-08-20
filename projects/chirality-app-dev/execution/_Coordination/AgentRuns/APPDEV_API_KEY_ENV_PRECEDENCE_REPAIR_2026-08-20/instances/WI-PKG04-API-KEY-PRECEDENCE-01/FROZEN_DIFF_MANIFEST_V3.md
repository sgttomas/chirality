# N1 amended implementation review manifest v3

- FrozenAt: `2026-08-20T15:47:09Z`
- Supersedes: `FROZEN_DIFF_MANIFEST_V2.md`
- Reason: frozen graph v2 amended N1 to expose the store-owned non-secret
  credential source fact required by dependent N2.
- AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38`
- PackageID: `PKG-04`
- DeliverableID: `DEL-04-05`
- Coverage: complete two-file product/test identity plus implementation,
  manager verification, v2 graph, and N2 amendment evidence.

| SHA-256 | Path |
|---|---|
| `d810b1ef79d528ee86d09b879d76f2c1e46dec1517d77c4d8749c8d0741444db` | `projects/chirality-app-dev/frontend/electron/api-key-storage.ts` |
| `c9cadac32f892613a3a0b3e3f9afb8200b14ab375408f5ea89c23e53b817dac4` | `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts` |
| `01346527d1d1154d82031299a129b4af9a5ae684e32d81c430f14940452f1297` | `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/TASK_RUN_2026-08-20_0939.md` |
| `b32ae9c9d059891986d04993dde7745b29ad56bea9f9b1360d8037a07fa0685d` | `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/TASK_RUN_2026-08-20_0939_REGISTERED_CHECKS.json` |
| `36c47648763081c34b2450debec0865f919af848382a7102a5bc69751e80c9db` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/TASK-PKG04-API-KEY-STATUS-SOURCE-IMPLEMENT-02/RETURN.md` |
| `72148cef6648e14f31fc68ebf2816094a84f4ecfe6c48dba006e3b3821435021` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/N1_MANAGER_REGISTERED_CHECKS_V2.json` |
| `f1c49fc0f8f0147b92b7629f5d80bd9a4b33324945b2e2f2b88dc365e2c9aefe` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/N1_APP_HOLD_RELIANCE_V2.json` |
| `9b289a11e651c16f8501c15070be3cf9b44eeeea8a61b6982749739db774593b` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/secret-scan-v2/secret-scan-summary.json` |
| `0898571cffde86e2a0fdc002663cf14bfc36fc623c9ec9db92574764b39f4925` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/N1_MANAGER_VALIDATION_V2.md` |
| `0c4391db238c354a632769901d87b21d522d5ee5f132ce288890c107b0e2931d` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/ORCHESTRATION_PLAN_V2.md` |
| `2aa4effb89d49f65ca76b879880bf58eb37407ab65ae701dbf0423baf7d6e0d6` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/WORK_GRAPH_V2.md` |
| `57345444a1e1d8c3dcbcd74ba3f1bc97ccbd8ee346a1f899b75210bedb40fadb` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/amendments/WI-PKG02-API-KEY-PRECEDENCE-01/v2.md` |

Review must reject any of the twelve hash mismatches; inspect 100% of both
product/test files and the exact two-file basis diff; trace the daemon status
serialization and dependent N2 consumer contract; validate the combined
focused/full/typecheck/build/harness/self-check/APP-HOLD/secret/scope/
whitespace evidence; and confirm the result is non-secret, provider-isolated,
and preserves accepted environment precedence and get/set/remove behavior.
