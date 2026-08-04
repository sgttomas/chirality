# Owner semantic decision packet — TM-ROOT-112

DecisionID: `ROOT-TM112-SEMANTICS-01`  
RequestedBy: `HELPS_HUMANS`, managed by `HELP_HUMAN`  
Status: `DECISION READY / UNSIGNED / IMPLEMENTATION HELD`  
Authority required: accountable human

## Decision requested

Select exactly one grace option, one SSE cancellation-order option, and one
residual-force option; then accept or return the shared cleanup,
error/idempotence, restart, and claim-boundary consequences. The recommendation
is **G2 + C1 + F1**.

The exact recommended wording is in `CANDIDATE_NORMATIVE_CLAUSES.md`. It remains
non-authoritative until the signed owner return.

## Outcome and recommendation

Use a fixed **2,000 ms** production grace. Stop admission first; immediately
request the existing canonical runtime interruption for every active SSE,
including a latched request for an Agent 1 run whose manager identity is not yet
known; the latch expires at force with a recorded identity-unavailable failure
and no late interrupt. Allow interruption/terminal persistence and natural
response completion to use the same grace. At deadline, call Node's force-close after
`server.close()` and destroy every tracked residual server socket. Do not let
transport or interruption acknowledgement extend stop beyond the force step.
Allow at most 500 ms after force for Node close/socket settlement, then treat a
remaining close as a timeout and continue cleanup. The 500 ms is a proposed
product-policy cap, not an evidence-derived Node guarantee. Attempt all cleanup,
aggregate actual failures, coalesce stop calls, block
concurrent start and start during stop, and allow same-instance restart only
after a fully successful stop (not `STOPPED_DEGRADED`).

This is the smallest coherent choice that gives canonical interruption a real
window while preventing the reproduced active-request/SSE mechanism from
holding Root shutdown open indefinitely. The 2 s value leaves empirical margin
relative to App's one observed approximately 5.06 s launchd escalation, but that
external timing is not promoted to a Root guarantee. No executed evidence
proves that a real provider always reaches terminal persistence within 2 s;
G2 is a product-policy recommendation under that explicit uncertainty, not a
measured natural cutoff.

## Bound authority and currentness

- Signed authorizing transcript:
  `../ROOT_TM112_DECISION_PREP_2026-08-03/OWNER_RULING_TRANSCRIPT_2026-08-03.md`,
  SHA-256
  `66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.
- It authorizes semantic return first, then a separate implementation/test
  tranche only after the human selects exact grace, cancellation obligations,
  and residual-force behavior.
- Current HEAD and `origin/main` at run binding:
  `88e7590d3664d4f1daf91bed2a8899bda0748b92`.
- Current daemon source:
  `runtime/packages/daemon/src/runtime-daemon.ts`, SHA-256
  `a6bb6b2388bbca084640611d15f4186b3c98379776001e2335b96831cebe2d46`.
- Current tests SHA-256:
  `bbcfcabb48dd7c4b5c5e0645b14601efd89404e34a5cdde322a0bef5b22a693e`.
- N1 results SHA-256:
  `cc2d703a32899e905ee44455f32a75f0ac7c79ca912d7dd4e2e181201f903ea2`.
- Runtime declares Node `>=22.19.0`; this run's installed runtime is Node
  v24.18.0 on macOS arm64.

## Evidence that constrains the choice

1. Current `stop()` clears its server reference, awaits `server.close()`, and
   only then unlinks the socket and owned record
   (`runtime-daemon.ts:90-102`). It has no finite timer or force step.
2. N1 executed twice: idle and completed keep-alive stopped immediately;
   incomplete request and live SSE remained pending at 750 ms. Client release
   resolved stop; the live SSE invoked one interrupt. The child SIGTERM/SSE case
   likewise remained alive at 750 ms and exited zero after client release.
3. N1 observed the Unix socket pathname absent while stop was pending and the
   owner record still existed. Path disappearance is therefore not completion.
4. Current SSE code binds response close to its route interruption callback and
   waits for the async iterator; session-turn identity is known from the route,
   while high-level Agent 1 identity is learned from the first harness event
   (`runtime-daemon.ts:210-231,306-313,388-443`).
5. Root's accepted contract makes the daemon the sole owner of interruption and
   uses authenticated HTTP/1.1/SSE over its Unix socket (`CONTRACT.md`
   K-RUNTIME-1/K-CONTROL-1; `SPEC.md` section 14.1). A shutdown choice that
   silently abandons runtime stream interruption would conflict with that
   ownership posture.
6. E1 ran the installed Node v24.18.0 behavior matrix twice (27 cases per run,
   semantically identical after timestamp/PID removal). `close()` stopped
   admission but remained pending for no-bytes, incomplete header/body, SSE,
   and upgrade connections. `closeAllConnections()` destroyed the ordinary
   classes but not upgrade and did not stop admission; tracked socket destruction
   covered upgrade. This directly supports close-first plus F1 and lifecycle
   serialization (`instances/E1-NODE-BEHAVIOR/EVIDENCE.md`).

## Options

### Grace — choose exactly one

| ID | Exact value | Tradeoff |
|---|---:|---|
| G1 | 1,000 ms | Fastest; least opportunity for engine interruption and terminal persistence. |
| **G2** | **2,000 ms** | **Recommended balance: bounded local-control shutdown with a meaningful cancellation window.** |
| G3 | 4,000 ms | Most drain time; least empirical margin beneath the one observed external ~5.06 s escalation. |

The values are mutually exclusive exact constants. None is derived as an
external launchd guarantee; the human selects the product policy.

### Cancellation/order — choose exactly one

| ID | Order | Tradeoff |
|---|---|---|
| **C1** | **close admission → immediately request idempotent canonical SSE interruption → share grace → force** | **Recommended: preserves Root interruption ownership and maximizes time for terminal persistence.** |
| C2 | close admission → natural drain for full grace → interrupt at expiry → force | Gives streams more natural time but almost no time for canonical interruption before force. |
| C3 | close admission → immediately destroy SSE transport → disconnect-triggered interrupt; grace only for other work | Fastest SSE release, but makes transport loss—not an explicit shutdown request—the primary cancellation mechanism. |

These options differ in the first point at which active SSE is terminated or
interrupted; selecting one excludes the other two. All leave completed
responses untouched and treat incomplete pre-route HTTP as transport only.

### Forced residual connections — choose exactly one

| ID | Mechanism at grace | Tradeoff |
|---|---|---|
| **F1** | **`server.closeAllConnections()` then destroy tracked residual sockets** | **Recommended defense in depth, including pre-header/future upgraded residuals.** |
| F2 | `server.closeAllConnections()` only | Smallest code, but bound Node v24 left upgrade open and installed declarations give no upgrade guarantee. |
| F3 | destroy tracked server sockets only | Explicit coverage without bulk API, but correctness depends entirely on complete tracking. |

All three occur only after `server.close()` has stopped admission. They are
mutually exclusive by force mechanism. F1's second step operates on the
post-bulk-close residual snapshot, not as an alternate timing policy.

## Shared consequences accepted with a selection

- concurrent stop calls coalesce on one promise; stopped stop is a fulfilled
  no-op; a concurrent second start and start while stop is in flight reject;
- reaching force is an expected bounded path, not itself an error;
- post-force close/socket settlement has a human-selected 500 ms policy cap;
  the connection-governed bound is selected grace + 500 ms (1,500 ms for G1,
  2,500 ms for G2, or 4,500 ms for G3), before filesystem cleanup;
- pending interruption at grace becomes a reported timeout and cannot extend
  stop; eventual settlement is observed to prevent unhandled rejection;
- all cleanup steps are attempted and collected failures reject only after
  cleanup attempts; clean-metadata interruption failure enters
  `STOPPED_DEGRADED` and blocks instance reuse; incomplete cleanup enters
  `STOP_FAILED_CLEANUP`, and repeated stop retries only incomplete cleanup;
- successful stop requires settled transport plus owned socket/owner absence;
- same-instance restart after successful stop is required and tested; a second
  concurrent start rejects; late prior-generation close/error/iterator/identity
  events cannot mutate or interrupt the new listener/owner generation;
- no App-specific cause or SIGTERM/process guarantee is inferred.

## Implementability and test boundary

`IMPLEMENTATION_TEST_SCOPE_MAP.md` maps every already-approved case to the
candidate obligations and the exact later seams. It includes no additional
source surface. If implementation cannot meet pre-identity interruption within
`runtime-daemon.ts`, it must return a scope-change request.

## Risks

`RISKS_AND_CAVEATS.md` records the supported-Node-floor gap, timer precision,
upgraded connection exclusion, provider interruption risk, pre-identity run
gap, external-process distinction, and App causality boundary.

## Downstream and holds

- Implementation remains held until a signed semantic return is captured and
  hash-bound.
- Canonical contracts, source, tests, registers, App content, lifecycle, and Git
  are unchanged by this run.
- Owner Addition 4 remains conditional: route a Root-to-App notice only after
  semantic acceptance **and** an accepted repair lands. The later App parity
  rerun remains App-owned.

## Exact returns

Use `OWNER_RETURN_TEMPLATES.md`. The recommended template selects G2/C1/F1 and
accepts candidate N-STOP-1 through N-STOP-7. The alternate template requires
exactly one choice per dimension and regeneration/hash-binding before any
implementation.
