# TM109-A next human semantic-acceptance form

Status: `UNSIGNED / NO EFFECT / POST-REFUTATION BYTES HASH-BOUND`

Prepared candidate: `chirality.identity-provenance-envelope/candidate-2026-08-03`

Authority basis: signed TM109-A ruling transcript SHA-256
`66b967008f67934b08383291e68ef0af9923463d749cac9dbe7a74090e9cbb06`.

## Preconditions before presentation

HELPS_HUMANS has frozen the exact post-refutation semantic candidate in
`POST_REFUTATION_MANIFEST.csv`. Each listed artifact hash was reverified after
the RF-109-01 inventory repair. The package SHA-256 below is the SHA-256 of the
exact manifest bytes; the manifest in turn binds these six semantic files:

- `ENVELOPE_CANDIDATE.md`;
- `ENVELOPE_SCHEMA_CANDIDATE.json`;
- `FIELD_INVENTORY.csv`;
- `COMPATIBILITY_ADJACENCY.md`;
- `CONFORMANCE_AND_NEGATIVE_CASES.md`; and
- `OPEN_DECISIONS.md`.

Package SHA-256: `2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489`

## Option H109-ACCEPT-DESIGN

Accept the exact hash-bound package as semantic contract-design bytes only.
Acceptance selects each `Candidate choice in prepared bytes` entry in
`OPEN_DECISIONS.md` exactly. Where that entry deliberately selects no value,
algorithm, rule, validator, trust profile, or evolution policy, the
non-selection remains an explicit blocker to implementation or reliance.
This does not authorize implementation. Before any implementation, a separate
human-gated activation must name exact source/test surfaces, mapping to the
accepted schema, validator/version, migration/rollback, affected consumers,
checks, writes, and return evidence.

```text
ACCEPT TM109-A IDENTITY-PROVENANCE ENVELOPE DESIGN 2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489 — EXACT CANDIDATE BYTES AND EACH RECORDED CANDIDATE CHOICE ACCEPTED AS CONTRACT-DESIGN SEMANTICS ONLY; RECORDED NON-SELECTIONS REMAIN BLOCKERS; THE ENVELOPE RECORDS IDENTITY AND PROVENANCE AND DOES NOT PERFORM OR AUTHORIZE EQUALITY, MAPPING, NORMALIZATION, TOLERANCE EVALUATION, SEMANTIC COMPARISON, CONFORMANCE, OR COMPATIBILITY; UNIT-SYSTEM AND TOLERANCE-PROFILE REFERENCES REMAIN OPAQUE; ALL CONSUMER-LOCAL SOLVER/RULE, ENGINEERING, PRIVACY, PROFESSIONAL, AND HUMAN-REVIEW MEANINGS REMAIN LOCAL; NO IMPLEMENTATION, AFFECTED-CLIENT ACCEPTANCE, LIFECYCLE, RELEASE, PUBLICATION, OR RELIANCE AUTHORIZED — <ACCOUNTABLE_HUMAN_NAME> <YYYY-MM-DD>
```

## Option H109-RETURN

Return named exact decisions or files for revision. No bytes are accepted.

```text
RETURN TM109-A IDENTITY-PROVENANCE ENVELOPE 2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489 — REQUIRED REVISIONS: <OPEN_DECISION_IDS_AND_EXACT_REASONS> — NO SEMANTIC ACCEPTANCE OR IMPLEMENTATION AUTHORIZED — <ACCOUNTABLE_HUMAN_NAME> <YYYY-MM-DD>
```

## Option H109-DEFER

Defer with an exact re-entry trigger. No bytes are accepted.

```text
DEFER TM109-A IDENTITY-PROVENANCE ENVELOPE 2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489 — REENTRY TRIGGER: <EXACT_TRIGGER> — NO SEMANTIC ACCEPTANCE OR IMPLEMENTATION AUTHORIZED — <ACCOUNTABLE_HUMAN_NAME> <YYYY-MM-DD>
```

## Option H109-DECLINE

Decline the generic-envelope direction. Consumer-local comparison remains
possible under consumer-local contracts, but no generic carrier or
cross-consumer claim is established.

```text
DECLINE TM109-A GENERIC IDENTITY-PROVENANCE ENVELOPE 2cec641d89ef45a1e920c77c5ea99a8e5d26c7102b43d89cc65ab2eca949e489 — CONSUMER-LOCAL CONTRACTS REMAIN LOCAL; NO GENERIC ENVELOPE, CROSS-CONSUMER COMPATIBILITY CLAIM, OR IMPLEMENTATION AUTHORIZED — <ACCOUNTABLE_HUMAN_NAME> <YYYY-MM-DD>
```

## Recorder validation

The recorder must reject a response when the package hash is absent or stale,
the option is ambiguous, required revision IDs/reasons or a deferral trigger
are missing, or signer/date is absent. No normalization, inferred option,
partial acceptance, implementation grant, or compatibility claim is allowed.

These prepared templates do not mean the bytes are already accepted. Only a
later exact signed return over the frozen post-refutation hash can select one
option.
