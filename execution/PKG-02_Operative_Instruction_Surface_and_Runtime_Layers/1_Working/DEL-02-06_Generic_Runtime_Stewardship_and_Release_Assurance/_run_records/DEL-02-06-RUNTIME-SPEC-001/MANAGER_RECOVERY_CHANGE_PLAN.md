# WORKING_ITEMS manager preflight — accepted-turn recovery change plan

Status: `PROVISIONAL_HELD_ON_N0_AND_LATER_GATES`
Character: manager inspection and change planning under REQ-027; not an N1,
N2, N3, or N4 accepted return; not implementation or acceptance

## Current-state facts

1. `runtime/packages/core/src/turn-coordinator.ts` persists
   `turn.accepted` before engine preflight/start and writes a terminal event on
   ordinary in-process success, failure, or interruption.
2. `runtime/packages/core/src/session-store.ts` persists session JSON and
   append-only `events.jsonl`, exposes project-scoped session listing and
   replay, and deduplicates `persistEvent` only by `eventId`. It has no
   accepted-without-terminal recovery operation.
3. `runtime/packages/core/src/residency-coordinator.ts` tracks active-turn
   drain count only in memory. `admitTurn()` and `activate()` do not consult
   persisted turn events.
4. `runtime/packages/daemon/src/runtime-daemon.ts` listens on the control
   socket without a persisted-turn reconciliation barrier. Model activation
   calls `service.residency.activate()` directly after the daemon is serving.
5. The terminal vocabulary is `turn.completed`, `turn.failed`,
   `turn.cancelled`, and `turn.interrupted`. The accepted sources do not rule
   which truthful terminal class represents an accepted turn whose completion
   became indeterminate because the owning daemon process ended.

These are read-only observations. They do not accept a repair design.

## Exact recovery requirements proposed for the later implementation gate

| ID | Requirement |
|---|---|
| REC-001 | Before the daemon exposes any admission or model-activation route, scan every registered project and persisted session for each `turn.accepted` event whose `turnId` has no terminal event. |
| REC-002 | Treat `turn.completed`, `turn.failed`, `turn.cancelled`, and `turn.interrupted` as the complete terminal set; never overwrite or supplement a turn that already has exactly one terminal. |
| REC-003 | Reconcile each unterminated accepted turn to one owner-ruled recovery terminal with an explicit daemon-restart/indeterminate-completion reason; do not call an engine, provider, model, tool, or client and do not replay the prompt. |
| REC-004 | Make reconciliation idempotent across unlimited restart/replay attempts: after the first successful reconciliation, every later run makes zero event additions and preserves the same terminal identity and payload. |
| REC-005 | Make a crash between terminal persistence and session-status persistence recoverable: the next run recognizes the terminal, repairs only stale derived session status where required, and creates no second terminal. |
| REC-006 | Fail daemon startup closed when the event log is malformed, a `turn.accepted` lacks a usable `turnId`, a turn has multiple terminal events, or persistence/update fails; do not open the control socket or activate a model under an incomplete census. |
| REC-007 | Reconcile all orphaned accepted turns, not only the latest session event, while deriving current session status from the latest applicable terminal without rewriting historical terminal evidence. |
| REC-008 | Record evidence sufficient to bind project, session, turn, accepted-event identity, recovery-terminal identity, recovery reason, source daemon-start identity, timestamp, and result without persisting prompt content or secrets in new recovery payloads. |
| REC-009 | Preserve append-only audit history. No recovery operation may delete, reorder, mutate, or replace an existing event; malformed or contradictory history is a blocker, not a repair invitation. |
| REC-010 | Complete the barrier before `server.listen`, before `runSessionTurn` can reserve/admit a turn, and before any `ResidencyCoordinator.activate()` reachable through the daemon API. |
| REC-011 | Prove drain-accounting convergence: every pre-restart accepted turn is either already exactly-terminal or becomes exactly-terminal before the new process reports zero live turns and permits a residency transition. |
| REC-012 | Prove exactly one terminal outcome per accepted turn after first recovery, interrupted recovery, and repeated recovery; duplicate accepted records or terminal contradictions have an explicit fail-closed disposition. |
| REC-013 | Keep recovery operational state non-authoritative. Runtime evidence may live in daemon user data, but contract, tests, decision records, and acceptance evidence remain checkout-contained. |
| REC-014 | Preserve project authorization boundaries during enumeration; recovery may inspect only the daemon's registered project/session stores and may not infer or broaden client authority. |
| REC-015 | Emit a bounded startup reconciliation summary (`scanned`, `already_terminal`, `recovered`, `blocked`) suitable for test and support evidence without exposing prompts or credentials. |
| REC-016 | Keep compatibility identity unchanged unless the separately gated semantic review proves the recovery behavior is a consequential compatibility-epoch change; present bytes do not decide that question. |

## Proposed implementation surfaces

| Surface | Proposed effect | Gate posture |
|---|---|---|
| `runtime/packages/core/src/session-store.ts` | Add bounded event-census primitives and crash-safe status convergence, or expose sufficient read/persist operations to one recovery coordinator. | Later Root implementation gate only. |
| `runtime/packages/core/src/accepted-turn-reconciler.ts` (new candidate) | Own detection, validation, deterministic/idempotent terminal persistence, summary, and fail-closed result. | Later Root implementation gate only. |
| `runtime/packages/core/src/index.ts` | Export the new Root-owned coordinator/result types if a new module is selected. | Later Root implementation gate only. |
| `runtime/packages/core/src/runtime-service.ts` | Own a one-time readiness/reconciliation barrier and model-activation wrapper so public admission and activation share the same prerequisite. | Later Root implementation gate only. |
| `runtime/packages/daemon/src/runtime-daemon.ts` | Await the barrier before server creation/listen; clean owner/socket artifacts on failure; route model activation through the gated service operation. | Later Root implementation gate only. |
| `runtime/packages/contracts/src/events.ts` and `runtime/packages/contracts/src/harness/event-schema.ts` | Prefer no new event type. A payload/result type may be required only after the recovery-terminal ruling; any wire-contract delta is separately reviewed. | Semantic contract gate before implementation. |
| `runtime/packages/core/src/turn-coordinator.ts` | Expected no semantic rewrite; may consume shared terminal predicates or readiness guard if needed. | Confirm at implementation design review. |
| `runtime/packages/core/src/residency-coordinator.ts` | Prefer no persistence scan here; accept activation only behind the service readiness barrier. A direct readiness guard is required if lawful callers can bypass the service. | Confirm caller inventory before implementation. |
| `runtime/tests/turn-hardening.test.ts` | Unit cases for census, terminality, no replay, and session-state convergence. | Registered checks/profile required. |
| `runtime/tests/daemon.test.ts` | Startup barrier, restart/replay idempotence, fail-closed startup, socket absence, and model/admission ordering. | Registered checks/profile required. |
| `runtime/tests/session-and-residency.test.ts` | Drain/residency ordering and zero-new-admission proof. | Registered checks/profile required. |
| `runtime/packages/cli/test/cli.test.ts` | Candidate process-restart proof only if caller inventory shows CLI launch/restart behavior is materially affected. | Census plus later implementation gate. |
| `projects/chirality-app-dev/frontend/electron/runtime-host.ts` and App integration tests | Current App composition is a read-only consumer observation. No App write is authorized; avoid a signature change where possible, otherwise route a separate App-owned tranche after Root semantics are accepted. | Separate App gate if actually affected. |

No PEC, Piping, Tier-0, or product/release surface is presently an
implementation target. Their status must come from N2 accepted-obligation
evidence, not this source inventory.

## Restart/replay evidence plan

| Evidence ID | Fixture / action | Required proof |
|---|---|---|
| EV-RR-01 | Persist one session with one `turn.accepted` and no terminal; construct a new daemon and start it. | Recovery terminal is persisted before socket availability; no engine/model call occurs. |
| EV-RR-02 | Stop and restart the recovered daemon at least twice. | Event count and terminal identity/payload remain byte-stable; every later reconciliation reports zero recovered rows. |
| EV-RR-03 | Inject failure immediately after terminal append but before session-status update, then restart. | One terminal total; derived session status converges; no prompt replay. |
| EV-RR-04 | Seed mixed sessions/projects: completed, failed, cancelled, interrupted, orphaned, and multiple historical turns. | Existing terminals remain unchanged; every orphan receives exactly one ruled recovery terminal; latest session status is truthful. |
| EV-RR-05 | Seed duplicate terminals, missing `turnId`, malformed JSONL, inaccessible evidence file, and append/update failure. | Startup fails closed, socket remains unavailable, model control is untouched, and blocker evidence names the exact source. |
| EV-RR-06 | Hold reconciliation on a test barrier while attempting health/admission/model activation. | No request route exists before reconciliation completes; after release, admission/activation proceeds only on PASS. |
| EV-RR-07 | Seed orphaned local-model turns, then request a different model after recovery. | All accepted turns are terminal before residency drain reports zero and before unload/load begins. |
| EV-RR-08 | Recover an event containing sensitive prompt data in its accepted payload. | New recovery payload/summary contains identifiers and reason only; no prompt/credential duplication. |
| EV-RR-09 | Recreate the daemon with the same user-data store after each scenario and replay the canonical event log. | Checkout test evidence proves exactly one terminal event per accepted `turnId`, stable ordering, and no deletion/mutation. |
| EV-RR-10 | Run positive and adversarial tests under the later accepted Root software-workflow profile twice from a clean checkout. | Identical test selection and passing results, with changed-path containment and no client-byte drift. |

## Later implementation sequence

1. Resolve N0 source/basis blockers and complete N1–N5 planning fan-in.
2. Obtain the human semantic ruling for the recovery terminal class, payload,
   deterministic identity strategy, duplicate-history posture, and whether
   the change advances the compatibility epoch.
3. Obtain S1 disposition for any decomposition/scope impact and adopt a lawful
   Root-local `software-workflow.json` with exact registered checks.
4. Seal one Root implementation activation naming the exact paths above,
   integration owner, before/after identities, checks, rollback, and evidence
   return. Route any actually affected App change separately.
5. Implement the recovery coordinator/barrier and tests; run unit,
   restart/replay, negative, typecheck/build, scope-containment, and repeated
   idempotence evidence.
6. Fresh review attempts to refute terminal uniqueness, crash consistency,
   fail-closed startup, no replay, drain ordering, redaction, and client
   boundaries.
7. Return exact SHAs and executable evidence for human acceptance. Only then
   may Task Management later evaluate TM-ROOT-108 closure.

## Current semantic decisions requiring a human gate

1. Recovery terminal: recommend `turn.failed` with a distinct
   `DAEMON_RESTART_RECOVERY`/indeterminate-completion reason rather than
   claiming operator interruption or successful completion; this is a
   proposal, not a ruling.
2. Terminal `eventId`: deterministic derivation from schema version + project
   + session + turn is recommended for crash/retry deduplication, subject to
   the event-identity contract review.
3. Existing duplicate terminal evidence: recommend fail daemon startup closed
   and preserve bytes for diagnosis; do not silently choose a survivor.
4. Compatibility epoch: unresolved. Internal startup behavior may be a
   no-wire-change repair, but consequential recovery semantics require the
   exact contract gate to decide.

## Current verdict

`HELD_BEFORE_N1`: this plan is decision support only. N0 must pass before the
formal inventory/evidence/integration nodes can run; runtime implementation
also remains held on S1 and later semantic/profile/implementation gates.
