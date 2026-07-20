# R5 D-APP-70 CQ-F1 Mapping Application — DEL-09-04

- Date: 2026-07-20
- Authority: D-APP-70 `RULED (Option A)`; ruling SHA-256 `1428294b9af34a97b19b7284860a5fdefc7fdb6157cce8c9516f4b54b064638a`
- Applied derivative: `execution/_Reconciliation/DeliverableConcordance/SCOPED_CQF1_POST_DAPP68_CONCORDANCE_2026-07-19/APPLIED_DAPP70_36A422AC/`
- Status before SHA-256: `f733bf5c4cb14e760bc5e0dadc39cdedc1ffabeb536893078df5f6c3a2415382`
- Status after SHA-256: `e571ae16bc62800f6d14ce33630a6d7b1414fdebcccc35b6bb11c0be93c476f3`
- Disposition: the `chirality-window.d.ts`, scripted SDK proof, and contract-dependency-lint CQ-F1 residuals were removed. The preload shared boundary is applied but its unnamed physical lead remains the sole CQ-F1 residual, gated by D-APP-71. The unrelated packaging/release Remaining item is byte-preserved.

| Mapping row | Group | Application | Source SHA-256 |
|---|---:|---|---|
| `projects/chirality-app-dev/frontend/src/types/chirality-window.d.ts` | 2 | DEL-02-03 primary; DEL-09-04 verification consumer retained | `974c070a0a0d02e43c7a0b477a6d0934bc8755b34d0a4c2dbc699ea4453bb1cd` |
| `projects/chirality-app-dev/frontend/electron/preload.ts` | 6 | shared boundary applied; physical lead unresolved among DEL-02-03, DEL-02-05, DEL-09-06, or deferral | `189b0d30bd8f6daf84862e14cfc3ec68c2c211b5c123283c7108c50c3b750ba0` |
| `projects/chirality-app-dev/frontend/src/lib/harness/scripted-agent-sdk-proof.ts` | 7 | DEL-09-06 primary; DEL-04-01 evidence edge retained; dev/test only, not packaged proof | `ebbe4240fd373cb916bec5611e716c1c2500bb674347b6b50f588dff384d7c87` |
| `projects/chirality-app-dev/frontend/scripts/assert-harness-contract-deps.mjs` | 8 | DEL-03-01 semantic lint; DEL-09-05 release-quality consumer retained | `ee310bee0f74f519c43c18d98c556b9f1b2fbdd72b4db539acf8edc05865f8e8` |

No-change assertions: every listed source SHA reproduced before and after this documentary application. `ScopeOfWork.md` remains `6692a81799558f3999f52db8cdf9c5382eec33c0e389ed3ae327790accccccd3`; `_DEPENDENCIES.md` remains `20f8f5e35713d0f0bb1ffd629e75156c71321615f125a3e2ad5c04881fd0c7df`; `Dependencies.csv` remains `27b30fb0fb729b9194912094731d22d301fe7f3dcf5408e3211b7c35011c0cbe`. Lifecycle state, authorization basis, Checking Approval SHA, MEMORY, and frontend/runtime source are unchanged. No preload physical lead, path owner, or source repair was selected.
