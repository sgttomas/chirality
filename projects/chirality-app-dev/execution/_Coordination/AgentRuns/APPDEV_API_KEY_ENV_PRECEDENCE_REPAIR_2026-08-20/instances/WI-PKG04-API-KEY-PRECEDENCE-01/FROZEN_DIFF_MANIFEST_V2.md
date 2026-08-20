# N1 implementation review manifest v2

- FrozenAt: `2026-08-20T15:23:30Z`
- Supersedes: `FROZEN_DIFF_MANIFEST.md`
- Reason: Review 01 found the product/test implementation correct but the
  frozen evidence set omitted two registered always-checks.
- AcceptedBasis: `6710ee6354debc201f6a454e2802897026cd4b38`
- PackageID: `PKG-04`
- DeliverableID: `DEL-04-05`
- Coverage: unchanged product/test identity, implementation return/evidence,
  and evidence-only Review-01 remediation.

| SHA-256 | Path |
|---|---|
| `72e9cdb9fabb5beb77ba009933dbb8c1375f012ac0162e088d96a460fe5baaab` | `projects/chirality-app-dev/frontend/electron/api-key-storage.ts` |
| `56b36a5ed44885877d692ad6357b6ee209f96edb8844aec2f5781d6c0a5b4fe7` | `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts` |
| `92b8a4f777ffebda3230f9a3a1fbd0963b3e5d0087661952c2f8f0156626a37f` | `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/TASK_RUN_2026-08-20_0911.md` |
| `f6a34e278140a3e204ee72f2390653b2d676138f1058e44e6cdc1b43997d5961` | `projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge/_run_records/TASK_RUN_2026-08-20_0911_REGISTERED_CHECKS.json` |
| `ff7263b7a53c573bb02a560a0dc42c27f91367d01e8714214e1e9e50e05c5cac` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/TASK-PKG04-API-KEY-PRECEDENCE-IMPLEMENT-01/RETURN.md` |
| `973c0d29d5171c381a4bea5df881b7b1c119c27efe2aa03af206bdd0939ed02e` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/N1_MANAGER_REGISTERED_CHECKS.json` |
| `f162cc12946a62b47833d8459395d6b2c54cffa726fa94cdc90695585132378c` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/REVIEW_01_DISPOSITION.md` |
| `08397e3c952e44f0773ac1245b78c97aa249d7620fe69ff22b9b896b97f8f7b1` | `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_API_KEY_ENV_PRECEDENCE_REPAIR_2026-08-20/instances/WI-PKG04-API-KEY-PRECEDENCE-01/N1_MANAGER_VALIDATION.md` |

Review must reject any of the eight hash mismatches, inspect the complete
two-file basis diff and both product/test files, confirm Review-01 closure,
and validate the combined check set. Product/test bytes are unchanged from
Review 01; no product rerun is owed by the evidence-only remediation.
