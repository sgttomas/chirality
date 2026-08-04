# Accepted-turn recovery specification candidate

- RunID: `DEL-02-06-RUNTIME-SPEC-001`
- Node: `N4`
- Status: `CANDIDATE_NOT_ADOPTED`
- Scope: exact no-implementation semantic candidate assembled from accepted N0-N3 evidence
- Accepted Scope of Work: `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`

## Authority and interpretation

This file is derivative planning evidence. It does not adopt a contract, choose
an unresolved value, authorize implementation or checks, change lifecycle or
dependency truth, classify PEC as affected, or confer release or reliance.
Normative words below describe candidate behavior only. Every bracket-free
symbol prefixed `OWNER_SELECTED_` denotes an exact value that must be supplied
by a later accountable-human decision; it is not an implementation default.

## Accepted facts

1. Durable `turn.accepted` can exist without any of the four terminal event
   forms after process loss; startup and later admission do not scan for that
   residue (`N1-F01`, `N1-F02`).
2. Current persistence deduplicates exact event IDs, not accepted/terminal
   state by turn, and replay is descriptive only (`N1-F03`, `N1-F06`).
3. Local drain accounting and ordinary/governed active reservations are
   process-memory state and are not reconstructed after restart (`N1-F04`).
4. Client and CLI transport failure cannot distinguish pre-acceptance failure
   from accepted work with unknown completion (`N1-F05`).
5. Runtime and harness terminal vocabularies disagree about
   `turn.cancelled`, while session summary maps cancellation to failure
   (`N1-F07`). Existing tests do not prove restart reconciliation or repeated
   idempotence (`N1-F08`).
6. Root CLI and App are `AFFECTED`; Piping and Tier-0 are `NOT_AFFECTED`; PEC
   remains `UNRESOLVED` and creates no obligation or closure veto
   (`N2-F-001`).
7. N3 designed but did not execute recovery, replay, rollback, or regression
   evidence. Its results remain `DESIGNED_NOT_EXECUTED`.

## Candidate semantic clauses

| ID | Exact candidate requirement | Evidence design |
|---|---|---|
| `REC-001` | Before daemon readiness, request admission, governed Agent 1 admission, session boot, model activation, or local-model admission, Root shall enumerate the entire registered central-session corpus and classify every durable accepted turn against the complete terminal set. | N3-R01, N3-R03 |
| `REC-002` | A turn is `ORPHAN_ACCEPTED` only when exactly one valid acceptance exists and zero valid terminal events exist for the same project, session, and turn identities. No status field, in-memory map, transport result, or event-ID deduplication may substitute for this comparison. | N3-R01, N3-R04 |
| `REC-003` | The terminal set shall preserve the distinct observed forms `turn.completed`, `turn.failed`, `turn.cancelled`, and `turn.interrupted`; the recovery terminal vocabulary, payload, and session-status mapping remain `OWNER_SELECTED_RECOVERY_TERMINAL_POLICY` under D1. | N3-R04; D1 |
| `REC-004` | Recovery shall never restart, resume, resend, infer completion of, or invoke engine/provider/model/tool work for an orphan. Any operator-initiated retry remains `OWNER_SELECTED_RETRY_POLICY`; automatic replay is prohibited. | N3-R05; D2; REQ-012/026 |
| `REC-005` | One authenticated reconciliation writer shall own one exact corpus/batch basis. Concurrent or ambiguous ownership shall fail closed without mutation. | N3-R12; D4 |
| `REC-006` | Reconciliation shall be idempotent: after a first successful ruled disposition, every later pass over identical or reordered input shall append no additional terminal and shall preserve the canonical outcome digest. | N3-R02, RR-07/RR-08 |
| `REC-007` | For an already-terminal turn, recovery shall append no terminal. Duplicate acceptance, duplicate terminal, conflicting terminals, terminal without acceptance, malformed possible terminal, or foreign attribution shall block the affected recovery unit without choosing a winner or synthesizing missing truth. | N3-R04, N3-R08; D7 |
| `REC-008` | Malformed, truncated, invalid-UTF-8, unsupported-schema, non-canonical, misattributed, symlink-substituted, or path-substituted evidence shall remain byte-preserved and shall block admission/activation at the `OWNER_SELECTED_MALFORMED_EVIDENCE_GRANULARITY`. Skip-and-count replay is insufficient for recovery classification. | N3-R08; D7 |
| `REC-009` | The durability unit spanning recovery terminal or marker, session summary, recovery audit, and writer ownership shall be `OWNER_SELECTED_TRANSACTION_BOUNDARY`. No state may claim reconciliation unless that exact boundary is satisfied. | N3-R07, N3-R10; D4 |
| `REC-010` | Every recovery attempt shall produce checkout-reconstructible, evidence-bearing output with `OWNER_SELECTED_AUDIT_SCHEMA`: stable run identity, exact input/output hashes, classification, disposition authority, before/after state, result, redaction, and retained provenance. Operational daemon state remains non-authoritative. | N3-R09; D3; REQ-033/039 |
| `REC-011` | Governed Agent 1 turns shall receive the same discovery, no-replay, terminal-cardinality, status, audit, and concurrency guarantees as ordinary turns. Child or manager returns shall never be promoted to completion by inference. | N3-R11 |
| `REC-012` | Every unresolved accepted local turn shall contribute to activation/drain posture according to `OWNER_SELECTED_DRAIN_ACCOUNTING`, based only on `OWNER_SELECTED_ATTRIBUTION_SCHEMA`. Missing or stale provider/model/epoch attribution shall be reported, never invented. | N3-R06; D5/D8; REQ-044/045 |
| `REC-013` | Until the full corpus has reconciled successfully, all consequential paths shall remain closed behind `OWNER_SELECTED_READINESS_LATCH`. Only the exact `OWNER_SELECTED_RETAINED_FUNCTION_SET` may respond, and its evidence must prove no consequential mutation or alternate-runtime characterization. | N3-R03, N3-R13; D6 |
| `REC-014` | Root CLI and the generic Root-client path shall surface a distinct machine-readable indeterminate/recovery class without automatic resend. Presentation may simplify wording but shall preserve the class. | N1-F05; N2 Root CLI row; REQ-014/048 |
| `REC-015` | App shall conform its separately owned session, proxy, compatibility, error/presentation, interruption, and runtime-evidence surfaces only through an App-owned accepted tranche; Root shall write no App byte here. | N2 App row; REQ-015/032/049 |
| `REC-016` | PEC shall remain `UNRESOLVED`: no PEC work, dependency, or closure veto exists until a PEC-owned owner-ruling binds an exact v2 operation to accepted Root contract bytes or rules no effect. | N2-F-001; REQ-016/050 |
| `REC-017` | Cutover and rollback shall use `OWNER_SELECTED_CUTOVER_ROLLBACK_POLICY`, exact before/after identities, evidence preservation, fail-closed abort thresholds, and no silent replay. Git, deployment, lifecycle, and release remain separate acts. | N3-R14; D9; REQ-034/035 |
| `REC-018` | Recovery shall add no TCP or in-process fallback, alternate daemon/model, automatic model scheduling, credential transfer, client write, foreign authority, lifecycle, release, publication, issuance, or reliance effect. | N3-R16; REQ-035/040/047 |

## Required corpus classifications

The later adopted contract must define exact envelopes for these distinct
classes without collapsing them: `ORPHAN_ACCEPTED`, `ALREADY_TERMINAL`,
`INVALID_DUPLICATE_ACCEPTANCE`, `INVALID_DUPLICATE_TERMINAL`,
`INVALID_CONFLICTING_TERMINAL`, `INVALID_UNBOUND_TERMINAL`,
`MALFORMED_INDETERMINATE`, and `INVALID_ATTRIBUTION`. These names are candidate
identifiers, not accepted runtime constants.

## Human decisions held open

| Decision | Exact unresolved field | Required next instrument |
|---|---|---|
| D1 | recovery terminal vocabulary, payload, terminal/status mapping | accountable-human Root semantic decision |
| D2 | operator retry identity, timing, preconditions, and proof | human-accepted recovery/retry decision |
| D3 | audit schema, mandatory fields, redaction, retention, ordering, hashing | human-accepted evidence-schema record |
| D4 | transaction/durability unit, writer ownership, crash repair semantics | human-accepted storage/reconciliation decision |
| D5 | unresolved-turn drain contribution and release point | human-accepted drain-accounting decision |
| D6 | readiness latch and exact retained route/direct-entry set | Root decision plus affected-client decisions where applicable |
| D7 | malformed/contradictory evidence preservation, blocking and repair | human-accepted malformed-evidence decision |
| D8 | durable local/remote/model/epoch attribution basis | human-accepted evidence/attribution schema |
| D9 | exact cutover, abort, restore, compatibility, and deployment authority | exact cutover/rollback acceptance plus separately authorized act |

No D1-D9 value is resolved by this candidate.

## Acceptance boundary

Adoption is held until D1-D9 exact bytes are accepted and inserted into a new
versioned contract candidate, N5 independently attempts refutation, and the
accountable human expressly accepts the resulting semantic package. This file
contains no present-byte, executable-test, implementation, closure, lifecycle,
release, or reliance claim.
