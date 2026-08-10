# A2-DAPP92-A-ATTEMPT8-PACKET-02 — terminal return

Status: `COMPLETE — V1.17 REPAIR PREPARATION ONLY — FRESH VERIFIER REQUIRED`

Prepared the bounded Attempt-8 R2 repair without executing or syntax-checking
any proposed script or command. Preserved v1.16, its request, and its scripts
unchanged as rejected history.

## Frozen outputs

- `COMMAND_REGISTER_AMENDMENT_V1_17_PROPOSED.md` — C336-C374 plus separately
  prior-approved exact C196/C197; SHA-256
  `94309f250bc5a8489c34e5328c920ff66c19a89a9c08e5e348fce76335be39df`.
- `ATTEMPT_8_REAL_RUNTIME_COMMAND_APPROVAL_REQUEST_R2.md` — SHA-256
  `9bdb19de6944205435485350d7533b1a2d03646cb436005e4248a02803f0f5a4`.
- `proposed/attempt8-r2/real-runtime-controller-r2.mjs` — SHA-256
  `6da4821fb04550af01e4deaf0c05c398f93267f1c75e7c764f660e50c8c02059`.
- `proposed/attempt8-r2/real-second-session-sentinel-r2.mjs` — SHA-256
  `30f8bd60858a4c86fb7cb8ca0a4350b41b8c69ac78116c1d9fbcb2768c726213`.
- `proposed/attempt8-r2/real-runtime-cleanup-verifier-r2.mjs` — SHA-256
  `690b1b10d0afa48fc9963d4e4722121032880b15b8eb97c5f53a5be2a298ba26`.

All seven verifier blockers are addressed: live attach/signal identity;
controller-owned-handle signaling only; exhaustive outer-scoped child reap
and pre-controller cleanup-safe receipt; strict 139.5/148.0-second deadlines;
pre-runtime network-attempt scan; post-cleanup-receipt durable evidence copy;
and mutation-marker-separated rollback branches. Internal executable commands
and ChildProcess signal calls are enumerated in v1.17.

The exact prospective owner token is in the R2 request. Fresh adversarial
verification must accept these frozen bytes before it is presented for owner
reliance. There is no runtime, package, helper, GUI, LLDB, signal, credential,
release, reliance, Git, Task Management, or foreign-loop effect.
