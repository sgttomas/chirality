# V-A — Root runtime compatibility identity candidate

**Status:** `EXACT_CANDIDATE_AWAITING_OWNER_RULING`
**Candidate effect if accepted:** contract-design basis only; not effective,
implemented, released, or relied upon

## 1. Identity

The proposed Root runtime compatibility identity is:

```text
chirality.runtime.compatibility/v1
```

Its grammar is:

```regex
^chirality\.runtime\.compatibility/v([1-9][0-9]*)$
```

The terminal positive decimal integer is the **compatibility epoch**. The
identity is case-sensitive UTF-8 text. Comparison is exact code-point equality
after JSON decoding. Trimming, case folding, Unicode normalization, SemVer
interpretation, range negotiation, prefix matching, downgrade selection, and
multi-version negotiation are prohibited.

The candidate supports only the exact identity above. A future epoch requires
its own governed successor.

## 2. Declaration and same-request check

The authenticated `GET /v1/health` response must include:

```json
{
  "compatibilityIdentity": "chirality.runtime.compatibility/v1"
}
```

The JSON field is required. Missing, null, non-string, duplicate, or
grammar-invalid values are `RUNTIME_PROTOCOL_FAILURE`, not compatibility
mismatches.

Every consequential runtime request must include:

```text
Chirality-Runtime-Compatibility: chirality.runtime.compatibility/v1
```

The HTTP field name is case-insensitive as required by HTTP. Exactly one field
occurrence is allowed. The field value must be the exact ASCII octets of the
identity: no leading or trailing optional whitespace, comma joining, duplicate
occurrence, non-ASCII octet, or normalization is allowed. Missing, duplicated,
comma-joined, malformed, or grammar-invalid header values are
`RUNTIME_PROTOCOL_FAILURE` at P4. One well-formed but unequal value is
`RUNTIME_COMPATIBILITY_MISMATCH` at P5.

The transaction uses this canonical preflight order:

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

The client enforces P0–P2. P3 is limited to establishing requester identity and whether the requester may
receive compatibility diagnostics. It is not P7 authorization to perform the
requested operation. At P4 the daemon emits and the client validates the
health declaration; the daemon also validates the request header. At P5 the
client compares the health declaration and the daemon compares the header.
The daemon completes P5
before request-body interpretation, durable acceptance, or side effects.
Health/status reads are exempt from carrying the header: the client applies
P0–P2, the daemon applies P3 and emits the declaration at P4, and the client
validates at P4 and compares at P5. The same-request check prevents a daemon
restart or rebinding between
health inspection and consequential work from bypassing compatibility
enforcement.

## 3. Exact mismatch behavior

A reachable daemon with a well-formed identity unequal to the expected exact
identity rejects the consequential request with semantic code:

```text
RUNTIME_COMPATIBILITY_MISMATCH
```

The semantic failure data includes:

```json
{
  "code": "RUNTIME_COMPATIBILITY_MISMATCH",
  "category": "COMPATIBILITY",
  "message": "Runtime compatibility identity does not match.",
  "outcome": "REJECTED",
  "retryMode": "AFTER_INTERVENTION",
  "actionOwner": "CLIENT_OPERATOR",
  "correlationId": "<redacted correlation identifier>",
  "expectedCompatibilityIdentity": "chirality.runtime.compatibility/v1",
  "observedCompatibilityIdentity": "<well-formed unequal identity>",
  "redacted": true
}
```

The response may additionally carry only the D-A `COMPATIBILITY` profile's
`operationId` and `componentName`. It must not expose credentials, tokens,
request bodies, environment state, daemon process identity, method, or route
template.

This is the D-A semantic envelope, not a second envelope. V-A adds no
`retryable`, `rebindRequired`, or other redundant semantic field.

Missing or malformed declarations and invalid envelopes are
`RUNTIME_PROTOCOL_FAILURE`. No valid daemon response before known acceptance
is `RUNTIME_UNAVAILABLE`. A possible accepted operation without conclusive
terminal evidence is `OPERATION_OUTCOME_UNKNOWN`. D-A defines those
distinctions and overrides.

## 4. Client obligations

Before consequential work, a client:

1. authenticates and obtains health;
2. validates the required identity and exact equality;
3. sends the exact header on the consequential request; and
4. treats mismatch as intervention-required and fail-closed.

The client must not automatically retry, negotiate a range, select another
daemon, executable, transport, model, or runtime loop, downgrade the protocol,
or replay a consequential operation. Reconnect or rebind is recovery only
after all preconditions are re-evaluated.

## 5. Binding record

Any later effective contract must be accompanied by a record with schema:

```text
chirality.runtime-compatibility-binding/v1
```

It records:

- `bindingStatus`: `CANDIDATE | ACCEPTED | EFFECTIVE | SUPERSEDED`;
- the exact identity, grammar, and epoch;
- Root authority and accepted carrier;
- an ordered contract set and its manifest SHA-256;
- declaration and same-request comparison points;
- source identity;
- release identity, or explicit `UNSET`;
- effective and supersession boundaries;
- affected clients and dispositions;
- verification evidence;
- accountable-human disposition;
- open items; and
- an evidence-manifest digest.

Only `EFFECTIVE` supports reliance. Candidate or accepted prose alone does not.
Each lifecycle transition creates a new immutable record that cites its
predecessor. An accepted, effective, or superseded record is never edited to
change state.

## 6. Identity separation

This identity is not:

- `/v1`, which is a route namespace;
- an npm package version;
- a Git commit or tree;
- a build record or artifact hash;
- the R-A aggregate release identity;
- a runtime fingerprint;
- a tag or display label; or
- `flow-a.contract.v0.1.0`, which remains a separate historical Tier-0
  identity pending a separately ruled disposition.

## 7. Minimum deterministic tests

Acceptance of a later implementation requires positive exact-equality tests
and negative tests for absent, null, non-string, case-changed,
whitespace-changed, malformed, older-epoch, newer-epoch, restart-between-health
and-request, and missing-header cases. Tests must prove:

- no consequential side effect occurs on rejection;
- authentication/authorization diagnostic precedence remains bounded;
- mismatch never causes downgrade, alternate runtime selection, or replay; and
- the candidate identity is distinct from release, source, package, route, and
  Flow-A identities.

## 8. Non-effects

This candidate does not change runtime code, select a compatibility range,
adopt an error vocabulary beyond the proposed cross-reference to D-A, migrate
a client, map or retire Flow-A, or establish an effective identity.
