# Method, Configuration, Feature, and Experimental Matrix

**Candidate state:** `CANDIDATE_AWAITING_G2_OWNER_ACCEPTANCE`

| Surface | Exact 0.149.0 observation | Evidence state |
| --- | --- | --- |
| `--version` | captured stdout reports `codex-app-server 0.149.0` | `OBSERVED_WITH_UNAVAILABLE_PER_RUN_GATE_EVIDENCE` |
| `--help` | transport, session-source, config-override, websocket-auth, and strict-config options; no schema/type subcommand | `OBSERVED` |
| `initialize` | versioned user agent, disposable `codexHome`, Unix/macOS platform | `OBSERVED_STABLE_AND_EXPERIMENTAL_CLIENTS` |
| `initialized` | accepted notification | `OBSERVED` |
| `config/read` | full effective config, origins, and layers | `OBSERVED` |
| `configRequirements/read` | `requirements: null` | `OBSERVED_UNMANAGED` |
| `experimentalFeature/list` | 118 entries over cursors `null` → `100` → `null` | `OBSERVED_COMPLETE_FEATURE_INVENTORY` |
| `configWarning` | project-local config disabled because project is untrusted | `OBSERVED_NOTIFICATION` |
| `remoteControl/status/changed` | disabled, unauthenticated disposable state | `OBSERVED_NOTIFICATION` |
| generated stable/experimental method list | no generated schema/types entrypoint exists in the authorized package | `UNAVAILABLE_UNDER_BOUNDS` |
| all other documented methods | not invoked; they were unnecessary or could mutate state/model/account surfaces | `NOT_PROBED_UNDER_BOUNDED_PURPOSE` |

## Appendix-B.1 configuration result

| Setting | User-layer value | Project fixture | Effective result |
| --- | --- | --- | --- |
| `approval_policy` | `on-request` | absent | `on-request` |
| `sandbox_mode` | `workspace-write` | absent | `workspace-write` |
| `sandbox_workspace_write.network_access` | `false` | absent | `false` |
| `check_for_update_on_startup` | `false` | absent | `false` |
| `web_search` | `disabled` | absent | `disabled` |
| `analytics.enabled` | `false` | absent | `false` |
| `feedback.enabled` | `false` | absent | `false` |
| `features.multi_agent` | `true` | `false` | `true`; project layer disabled as untrusted |
| `features.multi_agent_v2` | `false` | `true` | `false`; project layer disabled as untrusted |
| `agents.enabled` | `false` | `true` | `false`; project layer disabled as untrusted |

A second run set session flags to `multi_agent=false`,
`multi_agent_v2=true`, and `agents.enabled=true`; each read back at that value
with origin type `sessionFlags`. Thus the observed precedence is session flags
over user config, while the untrusted project layer is present for inspection
but supplies no effective override. `CONFIG_READBACK_AND_PRECEDENCE.json`
preserves the exact fields and origins.

## Feature stages

The complete pin-specific inventory has 118 features: 38 `stable`, 2 `beta`,
41 `underDevelopment`, 3 `deprecated`, and 34 `removed`. Forty-two were
currently enabled and 42 reported `defaultEnabled: true` under the probe
posture. `FEATURE_INVENTORY.json` preserves every exact entry; experimental
surfaces are not inferred from names alone and are not enabled by this packet.
