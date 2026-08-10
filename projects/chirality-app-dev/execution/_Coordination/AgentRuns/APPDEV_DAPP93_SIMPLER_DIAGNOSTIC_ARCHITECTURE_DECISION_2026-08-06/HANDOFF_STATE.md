# Handoff state — D-APP-93 simpler diagnostic architecture

Handoff: `DECISION_READY — AWAITING_OWNER_RULING`

## Accepted upstream basis

- D-APP-92 remains RULED Option A as a diagnostic objective only.
- Attempt 5 remains accepted only for offline construction method, recorded
  package identity/topology, rollback, and cleanup; no package tree survives
  and raw C216 bytes remain unavailable.
- Attempt 7 remains accepted only as mock timing/order direct-child
  PID/sentinel handshake evidence.
- the LLDB script remains current candidate bytes at SHA-256
  `720ad198b99c45737564ed596147ca438e60586b5b5241cd6852a49838f245f8`,
  reusable only after fresh revalidation and freeze.
- C196/C197 remains valid, exact, unused, and limited to its original
  direct-child/same-PTY/150-second semantics.

## Current decision surface

- D-APP-93 packet SHA-256:
  `6d751a2a595500d63e6700913014aabe7afb6c3e8f8a639fe58ac07b06096f7e`;
- decision register SHA-256:
  `f89ae7cf34b8efe5f7b50d139f71c892d72ac5517ffd93335a43ba9a1e576cd8`;
- fresh verifier return SHA-256:
  `21f2cce48191d07085b52d0912a283b47b32b50eefd8d08e3ff27a949fb38937`;
- validation SHA-256:
  `b23071439b1bb0af349c1a5b8dffac8736ce768ccface210eec21a63526a5857`;
- manager return SHA-256:
  `8a0f344dc8261886956cca8f8143664986ecb2750cffef344d3909a347df79e0`.

The packet is neutral, selects and recommends nothing, and is accepted by the
fresh verifier for owner decision presentation. D-APP-93 is the sole
`AWAITING_RULING` row.

## Closure and next lawful action

Decision-surface preparation is complete. The diagnostic objective is not
closed. The owner must select Option A, Option B, Option C, or issue a custom
ruling. If A or B is selected, the ruling authorizes only preparation of a
later exact execution/runbook or automation packet; execution remains a
separate command gate.

D-APP-88 and DEL-09-04 remain open. TM-APP-036 remains unfired. No package,
runtime, helper/GUI, LLDB/debugger, attach, signal, replay, credential,
product, remedy, acceptance, release, reliance, or Git effect follows from
this handoff.
