# Consolidated Exact-Pin Configuration, Method, and Feature Matrix

**State:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

## Configuration and precedence

| Surface | Baseline/user layer | Project fixture | Explicit session layer | Evidence conclusion |
| --- | --- | --- | --- | --- |
| `approval_policy` | `on-request` | absent | not changed | effective `on-request` |
| `sandbox_mode` | `workspace-write` | absent | not changed | effective `workspace-write` |
| workspace-write network | `false` | absent | not changed | effective `false` |
| `check_for_update_on_startup` | `false` | absent | not changed | effective `false`; does not govern observed plugin startup |
| `web_search` | `disabled` | absent | not changed | effective `disabled`; does not govern observed plugin startup |
| analytics / feedback | `false` / `false` | absent | not changed | effective disabled |
| `features.multi_agent` | `true` | `false` | `false` | project disabled as untrusted; session overrides user |
| `features.multi_agent_v2` | `false` | `true` | `true` | project disabled as untrusted; session overrides user |
| `agents.enabled` | `false` | `true` | `true` | project disabled as untrusted; session overrides user |
| `features.plugins` | baseline runtime `true`, default `true`; literal config field absent | absent | `false` | session override reads false and suppresses observed plugin startup |

`configRequirements/read` returned `requirements: null`. The project fixture
was visible but disabled as untrusted; therefore this evidence does not claim
trusted-project precedence. Exact fields and origins are pinned in
`03_EMPIRICAL_EVIDENCE/CONFIG_READBACK_AND_PRECEDENCE.json`.

Nine of ten run-specific executable/profile/preflight gates are committed.
The `version` run has empty preflight records and no per-run gate-hash record;
its output is therefore qualified as `UNAVAILABLE_UNDER_BOUNDS` for gate
provenance. No configuration, precedence, or feature conclusion depends on
that run.

## Methods and entrypoints

| Method or entrypoint | Result | Calibration |
| --- | --- | --- |
| `--version` | captured stdout reports `codex-app-server 0.149.0` | observed with unavailable per-run gate evidence |
| `--help` | transport, session, config, websocket, strict-config options | observed; no generation subcommand |
| `initialize` / `initialized` | successful | observed with stable and experimental client declarations |
| `config/read` | effective config, origins, layers | observed |
| `configRequirements/read` | `null` requirements | observed unmanaged host |
| `experimentalFeature/list` | 118 entries over two pages | observed complete feature inventory |
| `configWarning` | untrusted project layer disabled | observed notification |
| `remoteControl/status/changed` | disabled / unauthenticated | observed notification |
| generated stable/experimental method inventory | unavailable | `UNAVAILABLE_UNDER_BOUNDS` because schema/types could not be generated |
| other documented methods | not invoked | `NOT_PROBED_UNDER_BOUNDED_PURPOSE`; no mutation/account/model calls |

## All 118 features

The exhaustive exact-entry record is
`03_EMPIRICAL_EVIDENCE/FEATURE_INVENTORY.json`, SHA-256
`21a1aa2825fdcadf3f87379a4d456cd338c9af2dc8bee4defeb1e27e5997003d`.
It contains all 118 names, stages, enabled states, defaults, descriptions, and
announcements returned across cursors `null` → `100` → `null`.

| Stage | Count |
| --- | ---: |
| `stable` | 38 |
| `beta` | 2 |
| `underDevelopment` | 41 |
| `deprecated` | 3 |
| `removed` | 34 |
| **Total** | **118** |

The baseline has 42 enabled entries and 42 default-enabled entries. Key
delegation/plugin entries are: `multi_agent` (`stable`, true/true),
`multi_agent_v2` (`stable`, false/false), and `plugins` (`stable`, true/true).
This inventory does not authorize any experimental capability.
