# Run Identity

| Field | Value |
|---|---|
| Run | `CHIRALITY_PROGRAM_POST_REMEDIATION_HORIZON_2026-07-28_85EA0628` |
| Parent | HELP_HUMAN (Agent 0) |
| Manager | EVALUATION (Agent 1) |
| Dispatch mechanism | native managed subagent facility |
| Frozen Git basis | `85ea0628fa4e57dd6aae53b06139b2b8734a9612` |
| Manager engine / provider / model | Codex / OpenAI / `UNKNOWN` |

## Child runs

| Dispatch | Canonical run identity | Brief SHA-256 | Return SHA-256 | Engine / provider / model |
|---|---|---|---|---|
| `HZN-GOV-01` | `/root/horizon_scan_evaluation_run/hzn_gov_01` | `b040918c453e1d07d6eb199c3d26223d63293d44937e346760603e17305b7247` | `40779e092b1add0cf0a4d820d6e0f4f2a659e3acc169cce9eb15822b7513cf59` | `UNKNOWN / UNKNOWN / UNKNOWN` |
| `HZN-BND-01` | `/root/horizon_scan_evaluation_run/hzn_bnd_01` | `a03cdf63895d2516d5b504c5fc5708e088f2ae5514486f68588b7030dd1ebd38` | `36bc31c99f638a7c6de81be7e7e284478d0fa79eb633ad235b09f9b2179aa74b` | `UNKNOWN / UNKNOWN / UNKNOWN` |

The platform did not expose trustworthy per-child engine/provider/model
identities to the manager, so the record preserves `UNKNOWN` rather than
inferring them. Both children attested to no writes, delegation, network use,
or sibling communication.
