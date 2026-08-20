# N1 implementation review manifest

- FrozenAt: `2026-08-20T15:15:00Z`
- AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38`
- PackageID: `PKG-04`
- DeliverableID: `DEL-04-05`
- Coverage: two product/test paths plus the complete implementation return and
  normalized evidence set.

| SHA-256 | Path |
|---|---|
| `72e9cdb9fabb5beb77ba009933dbb8c1375f012ac0162e088d96a460fe5baaab` | `projects/chirality-app-dev/frontend/electron/api-key-storage.ts` |
| `56b36a5ed44885877d692ad6357b6ee209f96edb8844aec2f5781d6c0a5b4fe7` | `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts` |
| `92b8a4f777ffebda3230f9a3a1fbd0963b3e5d0087661952c2f8f0156626a37f` | `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/TASK_RUN_2026-08-20_0911.md` |
| `f6a34e278140a3e204ee72f2390653b2d676138f1058e44e6cdc1b43997d5961` | `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/TASK_RUN_2026-08-20_0911_REGISTERED_CHECKS.json` |
| `ff7263b7a53c573bb02a560a0dc42c27f91367d01e8714214e1e9e50e05c5cac` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/TASK-PKG04-API-KEY-PRECEDENCE-IMPLEMENT-01/RETURN.md` |

Review must reject any hash mismatch, inspect both product/test files in full,
trace the exact diff from the accepted basis, and backcheck the declared
evidence. Control-plane launch/status records are context, not frozen product
identity.
