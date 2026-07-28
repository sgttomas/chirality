# D-A — Degraded and failure semantics candidate

**Status:** `EXACT_CANDIDATE_AWAITING_OWNER_RULING`
**Dependency:** V-A must be accepted before compatibility-mismatch semantics
can become effective
**Candidate effect if accepted:** contract-design basis only

## 1. Common safety floor

Runtime-dependent agent work fails closed when any required client
configuration/access, authorized transport, compatibility, authentication,
project registration, authorization, project adapter, daemon credential,
engine/model/residency, operation-policy, or terminal-evidence condition
fails.

A failed condition never authorizes another runtime loop, daemon, transport,
protocol, model, provider, or silent downgrade. Reconnect/rebind is recovery,
not fallback, and never authorizes silent replay.

After durable acceptance, fail-closed means no further action, retry, replay,
promotion, or reliance until terminal evidence reconciles the outcome. It does
not assert that side effects did not occur.

File-native governance and other separately owned project functions may remain
usable, but they are not an alternate agent-runtime loop. Each client must
name and prove every retained-function claim; there is no blanket App or PEC
availability claim.

## 2. Exact semantic registry

The proposed Root-owned semantic codes are:

```text
INVALID_REQUEST
CLIENT_CONFIGURATION_INVALID
CLIENT_ACCESS_MATERIAL_UNUSABLE
ATTACHMENT_FAILURE

UNAUTHORIZED
FORBIDDEN
PROJECT_NOT_FOUND
PROJECT_MANIFEST_INVALID
PROJECT_MANIFEST_DRIFT
PROJECT_ADAPTER_UNAVAILABLE
PROJECT_ADAPTER_UNAUTHORIZED
PROJECT_ADAPTER_INCOMPATIBLE
NOT_FOUND
SESSION_NOT_FOUND

RUNTIME_UNAVAILABLE
RUNTIME_COMPATIBILITY_MISMATCH
RUNTIME_PROTOCOL_FAILURE

RUNTIME_CREDENTIAL_UNAVAILABLE
ENGINE_UNAVAILABLE
PROVIDER_UNAVAILABLE
PROVIDER_AUTHENTICATION_FAILED
PROVIDER_PROTOCOL_FAILURE
MODEL_UNAVAILABLE
MODEL_NOT_RESIDENT
RESIDENCY_TRANSITION_IN_PROGRESS
RESIDENCY_DRAIN_TIMEOUT
RESIDENCY_UNMANAGED_CONFLICT
CONTEXT_EXHAUSTED

SESSION_TURN_IN_PROGRESS
REQUIRED_DELEGATION_MISSING
DELEGATION_POLICY_VIOLATION
INTERRUPTED
OPERATION_OUTCOME_UNKNOWN
INTERNAL_FAILURE
```

Existing tokens are retained where their meaning is sound. Implementation-
specific legacy aliases may be accepted during an explicitly governed
migration, but must normalize to the accepted generic code and may not be
newly emitted after the accepted cutover.

`UNAUTHORIZED` means authentication absent or invalid. `FORBIDDEN` means an
authenticated identity lacks permission. They must not be collapsed into
provider authentication failure.

`D-A_CODE_MATRIX.csv` is an integral normative part of this candidate. Every
registry code appears exactly once and is bound to its category, originating
boundary, default and permitted outcomes, retry mode, action owner, diagnostic
profile, and whether durable acceptance may already have occurred.

## 3. Required semantic failure fields

Every surfaced failure carries:

- `code`: one registry value;
- `category`: `CLIENT | AUTHORITY | PROJECT | TRANSPORT | COMPATIBILITY |
  RUNTIME_STATE | ENGINE | OPERATION | INTERNAL`;
- `message`: fixed, redacted Root-owned text;
- `outcome`: `NOT_STARTED | REJECTED | COMPLETED | UNKNOWN`;
- `retryMode`: `NEVER_AUTOMATIC | SAFE_AFTER_RECHECK |
  AFTER_INTERVENTION | RECONCILE_BEFORE_RETRY`;
- `actionOwner`: `CLIENT_OPERATOR | PROJECT_OWNER | RUNTIME_OPERATOR |
  CLIENT_MAINTAINER | RUNTIME_MAINTAINER | NONE`;
- `correlationId`;
- optional `operationId`, `sessionId`, `turnId`,
  `expectedCompatibilityIdentity`, `observedCompatibilityIdentity`, and
  `retryAfterMs` only when semantically applicable; and
- `redacted: true`.

This candidate fixes the semantic contract. Exact wire serialization, HTTP
status, CLI exit mapping, and migration aliases remain later-gated.

## 4. Classification precedence

The system classifies the first failed boundary and does not probe later
boundaries:

```text
P0 CLIENT — request syntax and local configuration
P1 CLIENT — access-material safety
P2 CLIENT — authorized local transport reachability
P3 DAEMON — requester authentication and minimum diagnostic-disclosure authorization
P4 BOTH — compatibility declaration/header validity
P5 BOTH — compatibility exact comparison
P6 DAEMON — project registration and manifest currency
P7 DAEMON — requested-operation authorization
P8 DAEMON+PROJECT — required project adapter
P9 DAEMON — credential, engine, model, and residency readiness
P10 DAEMON — operation conflict and delegation rules
P11 DAEMON+CLIENT — execution and terminal evidence
```

The client enforces P0–P2. P3 establishes requester identity and permission to receive compatibility
diagnostics. It does not grant P7 permission to perform the requested
operation. At P4 the daemon emits and the client validates the health
declaration; the daemon also validates the request header. At P5 the client
compares the health declaration and the daemon compares the header. V-A and
D-A use this same canonical ordering.

Two overrides apply:

1. `OPERATION_OUTCOME_UNKNOWN` overrides the causal code whenever acceptance
   or completion cannot be disproved or reconciled.
2. `INTERNAL_FAILURE` is last-resort only and must not hide a recognized
   condition.

`INTERRUPTED` requires conclusive matching durable interruption evidence.

## 5. Load-bearing distinctions

- `RUNTIME_UNAVAILABLE`: no valid response from the authorized local daemon
  can be obtained before the operation is known accepted.
- `RUNTIME_COMPATIBILITY_MISMATCH`: a reachable daemon reports a well-formed
  V-A identity unequal to the client's accepted identity, before
  consequential acceptance.
- `RUNTIME_PROTOCOL_FAILURE`: the daemon is reachable but its compatibility
  declaration, error envelope, JSON/SSE, or required terminal evidence is
  malformed or contract-invalid.
- `OPERATION_OUTCOME_UNKNOWN`: a consequential request may have been accepted,
  but transport/protocol evidence ends without one reconcilable terminal
  outcome.
- `CLIENT_ACCESS_MATERIAL_UNUSABLE`: client access material is missing,
  malformed, unsafe, or inaccessible.
- `RUNTIME_CREDENTIAL_UNAVAILABLE`: the daemon cannot use a runtime-owned
  credential.
- `PROVIDER_AUTHENTICATION_FAILED`: the provider rejects a daemon-owned
  credential.

The P4/P5 header and declaration rules are exactly those in V-A: one JSON
string declaration; one case-insensitive HTTP field occurrence with the exact
ASCII value; malformed or missing values at P4; exact unequal values at P5.

## 6. Diagnostic profiles

The matrix's diagnostic profiles allow only the following fields in addition
to the required common envelope:

- `CLIENT`: `operationId`, `componentName`.
- `AUTHORITY`: `operationId`, `projectStableId`.
- `PROJECT`: `operationId`, `sessionId`, `projectStableId`,
  `componentName`.
- `TRANSPORT`: `operationId`, `componentName`, `retryAfterMs`.
- `COMPATIBILITY`: `operationId`, `componentName`,
  `expectedCompatibilityIdentity`, `observedCompatibilityIdentity`.
- `PROTOCOL`: at P4, `operationId`, `componentName`, and
  `expectedCompatibilityIdentity`; at P11, `operationId`, `sessionId`,
  `turnId`, `componentName`, and `expectedCompatibilityIdentity` when the
  protocol failure concerns compatibility. Malformed or contract-invalid
  observed values are attacker-controlled and are never echoed.
- `RUNTIME_STATE`: `operationId`, `sessionId`, `turnId`, `componentName`,
  `retryAfterMs`, `residencyEpoch`, `transitionId`.
- `ENGINE`: `operationId`, `sessionId`, `turnId`, `componentName`,
  `providerId`, `modelId`, `retryAfterMs`, where provider/model disclosure is
  already authorized.
- `OPERATION`: `operationId`, `sessionId`, `turnId`, `componentName`.
- `INTERNAL`: `operationId`, `sessionId`, `turnId`, `componentName`.

No profile permits raw causes or secrets. `PermittedOutcomeOverrides=UNKNOWN`
means the normal code is replaced by `OPERATION_OUTCOME_UNKNOWN`; it does not
permit the original code to carry `outcome=UNKNOWN`.

A row whose only origin is P9 has `MayAlreadyBeAccepted=NO`; a P9 readiness
failure must be classified before durable acceptance. Rows that also originate
at P11 may be post-acceptance. At P11, protocol evidence always carries the
operation/session/turn identifiers needed for reconciliation when applicable.
`INTERRUPTED` assigns `RUNTIME_OPERATOR` as the reconciliation owner; the
operator must reconcile durable terminal evidence before any retry.

## 7. Retry and recovery

Automatic retry is forbidden by default.

- `SAFE_AFTER_RECHECK` applies only to an idempotent read/preflight or when
  durable evidence proves a consequential operation was not accepted.
- `AFTER_INTERVENTION` requires the named owner to repair the condition, then
  full P0–P10 preflight restarts.
- `RECONCILE_BEFORE_RETRY` applies to interrupted or unknown outcomes.
- mismatch, protocol, authentication, authorization, invalid request,
  manifest drift, adapter inconsistency, unmanaged residency conflict, and
  internal failure are never automatically retried.
- transient availability/readiness/conflict conditions are retryable only
  when the outcome is `NOT_STARTED` or `REJECTED`, and the boundary is
  rechecked.

No retry rule authorizes alternate runtime, daemon, transport, model, provider,
protocol downgrade, or automatic resend.

## 8. Acceptance, terminal evidence, and replay

Every consequential operation needs a stable client-generated `operationId`
before transmission. Its operation contract must guarantee:

1. durable acceptance evidence before side effects; and
2. exactly one durable terminal receipt.

A transport break before any request bytes are written may be
`RUNTIME_UNAVAILABLE / NOT_STARTED`. Once transmission begins, absence of a
conclusive rejecting or terminal receipt yields
`OPERATION_OUTCOME_UNKNOWN / UNKNOWN` unless an accepted idempotency contract
proves otherwise.

Replay means querying durable evidence/status; it never means resubmitting the
operation. Missing, duplicate, malformed, or contradictory terminal evidence
remains unknown. Partial UI/SSE output is explicitly partial and unconfirmed;
it is not completion evidence or accepted work.

## 9. Redaction

The machine-readable class, code, outcome, retry mode, and action owner survive
every adapter and presentation layer.

Failures must not emit or persist raw tokens, credentials, authorization
headers, prompts/request bodies, attachment/tool contents, provider raw
bodies, environment variables, stack traces, absolute user-data paths, or raw
causal exceptions.

Allowlisted diagnostics are limited to redacted correlation/operation/session/
turn IDs; component name; project stable ID; non-secret compatibility
identities; retry timing; residency epoch/transition ID; and adapter/provider/
model identifiers only where already authorized for the recipient.

## 10. Affected-client evidence

### Root client and CLI

Later conformance must prove every registry class and outcome/retry tuple,
configuration/access/socket separation, exact V-A rejection, malformed
envelope handling, no automatic resend, machine-readable output preservation,
redaction, and deterministic unknown-outcome reconciliation.

### Chirality App

Any later App-owned gate must prove an injective mapping of applicable generic
codes through its adapter and UI, preserve outcome/retry/action-owner data,
prevent resend on reconnect, prove every retained-function claim separately,
and preserve existing Root/App ownership partitions.

### PEC

PEC evidence is conditional on a separately accepted v2 carrier and affected
operation. Frozen v0.4 is reference evidence only. PEC must remain optional,
must not start a retired agent loop, and must not mutate or promote accepted
PEC truth from an unknown outcome.

## 11. Non-effects and later gates

This candidate does not select wire encoding, HTTP status, CLI exit values,
retry timing, alias-retirement window, client migration, implementation bytes,
or PEC v2 work. It does not itself prove retained functions or effective
behavior.
