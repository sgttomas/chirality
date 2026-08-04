# HELPS_HUMANS manager return — TM-ROOT-112 semantic gate

RunID: `ROOT_TM112_STOP_CONTRACT_2026-08-03`
Verdict: `PASS FOR ACCOUNTABLE-HUMAN DECISION / IMPLEMENTATION HELD`
Artifact class: `DERIVATIVE DECISION SUPPORT — NON-AUTHORITATIVE`

## Outcome first

The exact shutdown-semantic decision packet is ready. It recommends
`G2 + C1 + F1`:

1. **G2:** 2,000 ms production grace from first `STOPPING` transition;
2. **C1:** close admission, immediately request generation-owned/idempotent
   canonical interruption for active SSE, allow the shared grace, and expire an
   unresolved pre-identity Agent 1 latch at force without a late interrupt; and
3. **F1:** after grace call `server.closeAllConnections()` after
   `server.close()`, then destroy every tracked residual socket.

The recommended shared policy adds a human-selected 500 ms force-settle cap,
making the G2 connection-governed bound 2,500 ms before filesystem cleanup.
This cap and the 2,000 ms grace are product choices, not empirical Node/provider
guarantees.

## Why this recommendation

E1 ran the installed Node v24.18.0 matrix twice, 27 cases per run with identical
semantic results. `close()` stopped admission but remained pending for
accepted/no-bytes, incomplete header/body, live SSE, and upgrade connections.
`closeAllConnections()` forced the ordinary HTTP classes but neither stopped
admission nor closed upgrade; tracked socket destruction closed the residual.
Repeated close can report `ERR_SERVER_NOT_RUNNING`, and Node permits overlapping
server generations. These facts support close-first ordering, daemon-level
idempotence/state, bulk force plus explicit tracking, and generation ownership.

E2 mapped accepted Root ownership/security constraints, current source/SSE
flow, exact N1 distinctions, and all eight owner-approved tests. It preserved
completed keep-alive vs incomplete request vs SSE; socket disappearance vs
owner completion; Root mechanism vs App causality; and daemon method vs
process/SIGTERM behavior.

## Exact decision artifacts

- `OWNER_SEMANTIC_DECISION_PACKET.md` — bounded options, evidence, and
  recommendation.
- `SEMANTIC_OPTIONS.json` — machine-checkable exactly-one selection form.
- `CANDIDATE_NORMATIVE_CLAUSES.md` — exact recommended N-STOP-1..7 wording,
  visibly non-authoritative.
- `OWNER_RETURN_TEMPLATES.md` — exact recommended, alternate, and return-for-
  revision templates.
- `IMPLEMENTATION_TEST_SCOPE_MAP.md` and `RISKS_AND_CAVEATS.md` — later scope,
  observations, evidence gaps, and platform/version boundaries.
- `BASIS_MANIFEST.sha256` — final content bindings.

## Refutation result

The first exact-bound E3 refutation found two blockers and three review gaps.
All were repaired. Fresh E4 backcheck closed all five and returned `PASS WITH
NON-BLOCKING WARN`; its sole structured-parity warning was then applied exactly
and revalidated. `REFUTATION_DISPOSITION.md` preserves the full session and
finding history.

## Holds and next decision

No contract, runtime source, daemon test, register, App content, lifecycle, or
Git surface changed. Implementation remains held until the accountable human
returns one complete selection and the selected clauses are hash-bound as
authority. The Root-to-App notice remains held until semantic acceptance **and**
an accepted repair lands. Even then, App owns the parity rerun and Root has not
proved App R2 causality or signal/process behavior.

Recommended owner action: use the exact G2/C1/F1 template in
`OWNER_RETURN_TEMPLATES.md`, or choose one option per dimension through the
alternate path (which requires regenerated/hash-bound clauses before work).
