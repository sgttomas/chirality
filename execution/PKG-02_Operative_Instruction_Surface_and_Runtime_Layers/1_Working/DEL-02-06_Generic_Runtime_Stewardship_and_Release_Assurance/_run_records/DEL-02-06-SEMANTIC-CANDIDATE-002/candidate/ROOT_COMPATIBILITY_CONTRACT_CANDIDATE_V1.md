# Root compatibility contract candidate V1

- Status: `DERIVATIVE_SEMANTIC_CANDIDATE_NOT_ACCEPTED`
- Signed selection package: `623833310e2fa871bd895532f4831f87de97f2750ae92e03e0daeb9acf93329d`
- Upstream disposition candidate: `689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1`

## Identity grammar

The Root-owned compatibility identity grammar is
`root-runtime-<positive-decimal-epoch>`. The exact initial epoch remains the
explicit unresolved placeholder
`<OWNER_SUPPLIED_FUTURE_POSITIVE_DECIMAL_EPOCH__UNRESOLVED>`.

This candidate mints no epoch and no compatibility identity. The placeholder
is not a permitted runtime value and must be replaced only by a later
accountable-human act that supplies a positive decimal epoch and binds the
resulting exact bytes.

The identity is not a route namespace, package version, runtime fingerprint,
source or release commit, distributable identity, or Tier-0 Flow-A identity.

## Declaration and comparison

Before every consequential runtime-dependent operation:

1. the daemon declares its exact Root compatibility identity in a preflight
   response bound to the authenticated daemon and project context;
2. the affected client declares the exact identity accepted by its contract
   basis in the operation request; and
3. the daemon and client each require byte-for-byte equality of both values
   before consequential work begins.

An absent, malformed, stale, inferred, unequal, range-compatible, or
version-label-only value rejects before acceptance, engine, provider, model,
tool, or mutation. Daemon- or session-start equality never substitutes for the
per-operation request-bound check. Range negotiation, downgrade, and
multi-version inference remain unsupported.

## Mismatch envelope

The exact machine class is `RUNTIME_COMPATIBILITY_MISMATCH`. Its candidate
envelope contains:

- `code`: `RUNTIME_COMPATIBILITY_MISMATCH`;
- `operation_id`, `project_id`, and safe daemon identity;
- `client_compatibility_identity` and `daemon_compatibility_identity`;
- `client_contract_basis_sha256` and `daemon_contract_basis_sha256`;
- `retryable`: `false`;
- `consequential_work_started`: `false`; and
- `diagnostic` describing the exact absent, malformed, or unequal condition.

Root client and CLI must preserve the code and machine fields. App may map
presentation only through an App-owned accepted tranche and must preserve the
machine class. This candidate writes no Root CLI or App byte.

## Compatibility binding record

Before implementation, one immutable checkout-contained manifest must bind:

1. the exact compatibility identity and this accepted contract's SHA-256;
2. exact source and release identities;
3. every accepted affected-client basis and its exact operation;
4. separately accepted conformance or migration artifacts and hashes;
5. the complete Root semantic/regression evidence bundle and hashes;
6. census, Tier-0 relationship, PEC-routing, notice, and open-finding state;
7. cutover, rollback, replay, and indeterminate-operation disposition; and
8. accountable-human semantic, implementation, cutover, and release acts.

Every required field is present in one sorted manifest; a missing or
placeholder field blocks implementation and release. The manifest is evidence,
not a substitute for authoritative decomposition or accepted contract bytes.

## Epoch-change criteria

A new epoch is required whenever accepted Root bytes add, remove, rename, or
change consequential client-visible semantics, including operation admission,
machine-readable results, terminal/status meaning, retry/replay rules,
preconditions, or retained-function behavior. Evidence-only changes and
strictly internal changes proven non-observable to every client do not change
the epoch. Uncertain observability is treated as requiring impact analysis and
does not silently produce a no-change ruling.

## Recovery compatibility disposition

If and only if the recovery semantic package is later accepted, it is a
compatibility `DELTA`: recovery-before-readiness, a distinct recovery terminal,
new machine-readable states/results, and new admission conditions are
consequential client-visible semantics. A later owner must then supply the
exact epoch, accept the complete binding manifest, and separately authorize
implementation. If the recovery package is not accepted, this conditional
candidate makes neither a delta nor a no-change ruling.

## No-effect boundary

No compatibility identity, epoch, contract, source/release binding, repin,
client obligation, implementation, lifecycle, release, reliance, or Git act
is created by these candidate bytes.
