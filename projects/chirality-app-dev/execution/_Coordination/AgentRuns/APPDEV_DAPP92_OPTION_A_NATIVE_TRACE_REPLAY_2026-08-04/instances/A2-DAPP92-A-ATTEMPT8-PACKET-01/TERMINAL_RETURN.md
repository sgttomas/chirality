# A2-DAPP92-A-ATTEMPT8-PACKET-01 — terminal return

Status: `COMPLETE — PACKET PREPARATION ONLY — OWNER APPROVAL REQUIRED`

Prepared the separately governed D-APP-92 Attempt 8 real-runtime packet. No
proposed command was run, and no proposed script or command was syntax-checked.

## Immutable outputs

- `COMMAND_REGISTER_AMENDMENT_V1_16_PROPOSED.md` — commands C245-C335 plus
  the separately previously approved exact C196/C197; SHA-256
  `6ddf4b0fca2556b27f05fffd0a20cfe29aeb713520909da93c631b3148ebc073`.
- `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST.md` — SHA-256
  `1c0b6cafa028460f47928f555606d05ae7167c02aa4b073a54bbb23b09dc9515`.
- `proposed/attempt8/real-runtime-controller.mjs` — SHA-256
  `11a97d620e7f742e04d91418a1bbbeec2d1ef20b43e48596b75900c8cba4bd2f`.
- `proposed/attempt8/real-second-session-sentinel.mjs` — SHA-256
  `a75b91299cb20f7daa2154a2ba9b36e4f71235ed634bfe81f80d16d7874d4242`.
- `proposed/attempt8/real-runtime-fallback-cleanup.mjs` — SHA-256
  `ed577526d8d1122c24b96db1f62e4e796341bce27878145498288f94a1c19fec`.

The public authenticated contact path is source-derived from the packaged GUI
executable plus `Contents/Resources/runtime-cli/chirality-cli.mjs`, with
`ELECTRON_RUN_AS_NODE=1` and exact `project register` arguments. It is newly
sealed for this packet, not represented as recovered historical bytes. Token
material and raw registration stdout are excluded from retained evidence.

The packet carries one candidate reconstruction, one package invocation, the
28.0-second/102.0-second timing bounds, at most 80 0.1-second polls, same-PID
two-session sentinels, mandatory C197 detach and terminal proof, exact-PID
cleanup, evidence freeze, and exact D-APP-89 product rollback. C335 closes the
cleanup race if C196 starts but fails before trace-ready.

## Remaining gate

The exact owner decision token is recorded in the approval request. Until it
is issued, there is no runtime, product, acceptance, release, reliance, Git,
Task Management, or foreign-loop effect. D-APP-88 and DEL-09-04 remain open;
TM-APP-036 remains unfired.
