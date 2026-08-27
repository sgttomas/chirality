# DEL-02-08 OUT-002 Endpoint-Policy Candidate — R16 Attempt

- **Overall state:** `UNAVAILABLE_UNDER_BOUNDS`
- **Reason:** exact exhaustive account, model, and turn service-destination
  enumeration is not established by the accepted empirical packet, current
  static exact-pin scan, or any permitted no-auth/no-connection operation.
- **Command-network separation:** all service rows are distinct from command
  network authority. This candidate grants no connection or approval.

## Row-by-row policy

| Row | Exact destination | Epistemic state | Policy disposition | Primary evidence |
| --- | --- | --- | --- | --- |
| Account service destinations | not enumerated | `UNAVAILABLE_UNDER_BOUNDS` | no endpoint inferred; live authentication, service observation, or stronger generated/runtime evidence would be required for exhaustive enumeration | `STATIC_ENDPOINT_SCAN.md` |
| Model service destinations | not enumerated | `UNAVAILABLE_UNDER_BOUNDS` | no endpoint inferred; no live account/model request or external connection is authorized | `STATIC_ENDPOINT_SCAN.md` |
| Turn service destinations | not enumerated | `UNAVAILABLE_UNDER_BOUNDS` | no endpoint inferred; no production `turn/start` or service connection is authorized | `STATIC_ENDPOINT_SCAN.md` |
| Plugin featured-cache destination | `https://chatgpt.com/backend-api/plugins/featured?platform=codex` | `EMPIRICALLY_OBSERVED_SANDBOX_DENIED` | `NOT_REQUIRED_FOR_RC_MANAGED_PROFILE__NO_NETWORK_AUTHORITY` | accepted `DENIED_EGRESS_INVENTORY.json` @ `abf745deb28f57c74eccac0d9f0f68c6bd5b07e7646cde66e5b6ea3d83d4b513` |
| Plugin GitHub fallback destination | `https://api.github.com/repos/openai/plugins` | `EMPIRICALLY_OBSERVED_SANDBOX_DENIED` | `NOT_REQUIRED_FOR_RC_MANAGED_PROFILE__NO_NETWORK_AUTHORITY` | accepted `DENIED_EGRESS_INVENTORY.json` @ `abf745deb28f57c74eccac0d9f0f68c6bd5b07e7646cde66e5b6ea3d83d4b513` |
| Plugin export fallback destination | `https://chatgpt.com/backend-api/plugins/export/curated` | `EMPIRICALLY_OBSERVED_SANDBOX_DENIED` | `NOT_REQUIRED_FOR_RC_MANAGED_PROFILE__NO_NETWORK_AUTHORITY` | accepted `DENIED_EGRESS_INVENTORY.json` @ `abf745deb28f57c74eccac0d9f0f68c6bd5b07e7646cde66e5b6ea3d83d4b513` |
| Configured remote-control base | `https://chatgpt.com/backend-api/` | `CONFIGURED_BUT_NOT_ATTEMPTED` | not an observed connection and not command-network authority | accepted `DENIED_EGRESS_INVENTORY.json` @ `abf745deb28f57c74eccac0d9f0f68c6bd5b07e7646cde66e5b6ea3d83d4b513` |

## Proposed RC managed-profile posture

Set `features.plugins = false` in the proposed RC managed profile. This is a
policy candidate only; production configuration is unchanged. Exact accepted
0.149.0 evidence establishes that:

- the baseline feature readback was enabled/current and enabled/default;
- `-c features.plugins=false` read back as false;
- two independent runs suppressed every observed plugin-startup attempt; and
- the switch disables the whole plugins feature, not a documented dedicated
  curated-sync subfeature.

Primary evidence is the accepted
`CONFIG_READBACK_AND_PRECEDENCE.json` @
`3eea0e0f075a8cbd0f143f5a0bc6b441ddb9691aca4c9a7d1d6d921d42581a93`
and `PLUGIN_SYNC_SWITCH.md` @
`c3024e555589995acc685d2feb15d1ca38db2d4e9fa2855eb1a3f7d4e025928c`.
The predecessor destination handoff remains
`OUT-002_ENDPOINT_INVENTORY.md` @
`fd6bd4e4dd7c2a0dc477e567becd5d2d092514db36dfedaf2fa2a529798d9f47`.

## Completion decision

The three missing required service classes prevent DEL-02-08 OUT-002
completion. The four exact completed rows and the proposed plugin-off posture
are preserved; overall OUT-002 remains `UNAVAILABLE_UNDER_BOUNDS`. No endpoint
is inferred from a base URL, string adjacency, method name, or service class.
