# G1-B schema-validation and canonical-digest plan

Status: **ROOT-LOCAL VALIDATION PLAN — NOT EXECUTED — NO REGISTRATION OR APPROVAL EFFECT**

## Objective and fixed target

The human Root owner selected `G1-B` for validation only in
`execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/OWNER_RULING_2026-08-03_S2_APPLY_PI_G1B.md`
(SHA-256 `12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129`).
The selected family is `chirality.app.pi-agent-engine-adapter`, with ownership
boundary `APP_AFFECTED_CLIENT`. The materialized target envelope is
`G1B_VALIDATION_TARGET.json` at SHA-256
`c5b2087e070cc92cc3daecd35460497be47b6f9dff3155bde5b1cbd0aef2db01`.

The schema is the accepted PIA-U10
`identity_proposal/CANDIDATE_IDENTITY.schema.json` at SHA-256
`ecb9f93908d7948c7d0b4ec284745a471ff4c4a096d9cb76e4fc46c396154a5c`.
H4 does not amend that schema.

## Why H4 does not publish a candidate digest

The schema requires exact stable build, capability-profile, registration,
policy-bundle, canonical client-composition, packaging-asset, platform, and
rollback-identity records. Those records are not present in accepted PIA-U10
evidence and PIA-U20 through PIA-U25 have not been accepted or executed.
`G1B_VALIDATION_TARGET.json` records each missing schema path as `TBD` with its
closure owner. Under K-INVENT-1 and K-CLAIM-1, H4 does not substitute source
hashes for semantically different artifact hashes and does not claim that the
envelope validates against the PIA-U10 instance schema.

`identity_digest_sha256` and `registry_key` therefore remain deliberately
unmaterialized. Any all-zero, placeholder, branch-derived, or partially
populated digest must be rejected.

## Deterministic completion procedure

The future PIA-U30 run, after its predecessor evidence is accepted, must use a
tested deterministic canonicalization implementation and preserve the command,
tool version, and input/output hashes in its immutable evidence bundle.

1. Verify the PIA-U10 schema SHA-256 exactly equals
   `ecb9f93908d7948c7d0b4ec284745a471ff4c4a096d9cb76e4fc46c396154a5c`.
2. Verify the selected target envelope SHA-256 exactly equals
   `c5b2087e070cc92cc3daecd35460497be47b6f9dff3155bde5b1cbd0aef2db01`.
3. Reproduce every frozen/current App file hash in the target envelope. If any
   byte differs, stop with `TARGET_DRIFT`; do not repair or silently update the
   target.
4. Ingest only accepted, immutable predecessor returns. PIA-U20 may supply the
   accepted proof-launcher repair/build recipe; PIA-U21 supplies the extracted
   upstream manifest and exact-install evidence; PIA-U22 supplies build,
   packaging, platform, and asset manifests; PIA-U23 supplies exact source and
   conformance evidence. App acceptance and Root contract instruments must
   separately supply exact profile, registration, policy, composition, and
   rollback records.
5. Construct one complete `stable_identity` object with the exact field names,
   types, and `additionalProperties: false` discipline in the PIA-U10 schema.
   Preserve the App family ID and `APP_AFFECTED_CLIENT` ownership boundary.
6. Construct `mutable_evidence` separately. Evidence bundle paths, observed
   time, runtime fingerprint, residency epoch, live model, and verdict must
   never enter `stable_identity` or its digest.
7. Validate the complete instance against Draft 2020-12 before digesting.
   Treat format validation as asserted: `observed_at` must be an RFC 3339
   date-time and every hash/ID/path must pass its schema pattern.
8. Canonicalize only the parsed `stable_identity` value using RFC 8785 JSON
   Canonicalization Scheme (JCS), encoded as UTF-8 without a byte-order mark.
   Do not canonicalize the outer instance, pretty-printed source, or
   `mutable_evidence`.
9. Compute lowercase hexadecimal SHA-256 over those canonical UTF-8 bytes.
10. Set `identity_digest_sha256` to that value and set `registry_key` to
    `chirality.pi-implementation-identity/v1/sha256:<digest>`.
11. Revalidate the complete outer instance, recompute the digest independently
    from the serialized artifact, and require declared digest/key equality.
12. Preserve the canonical byte stream, its byte count and SHA-256, the full
    identity instance, schema validation result, and independent recomputation
    result in the PIA-U30 immutable artifact manifest.

## Required positive and negative checks

| Check | Mutation or input | Required result |
|---|---|---|
| Positive round trip | Complete accepted G1-B stable identity | Schema PASS; independent JCS digests equal; declared key equals recomputed key |
| Same-descriptor alternative | Substitute Root `createPiOmlxEngineAdapter` family/source/composition while retaining `pi`/`omlx`/`0.82.0` | Different digest and registry key; App key cannot resolve the Root wrapper |
| Source drift | Change any implementation source hash | Different digest; dependent proof becomes stale |
| Build drift | Change build recipe, toolchain profile, or artifact manifest | Different digest; package proof rerun required |
| Capability or policy drift | Change any capability boolean or profile/policy hash | Different digest; no silent widening |
| Client drift | Change owner, host family, dependency owner, composition inventory, or composition hash | Different digest; affected client remains explicit |
| Package drift | Change manifest, lock, packaging policy, asset manifest, or target platform | Different digest; supply/package proof rerun required |
| Rollback drift | Change rollback identity, compatibility epoch, or authority bytes | Different digest; restoration basis remains explicit |
| Evidence-only rerun | Change only evidence bundle, observed time, fingerprint, residency epoch, live model, or verdict | Same digest and registry key; new evidence remains attributable |
| Declared digest mismatch | Alter `identity_digest_sha256` or registry suffix only | Validation FAIL |
| Partial identity | Omit or use `TBD` for any required stable field | Validation FAIL; no digest/key published |
| Unknown field | Add any undeclared field at any closed schema object | Validation FAIL |

## Failure and rerun posture

- Any input-hash mismatch, missing accepted predecessor, schema error,
  canonicalizer disagreement, digest/key mismatch, or collision-test failure
  terminates PIA-U30 as `FAIL` or `BLOCKED`; it never causes source repair.
- A changed stable input creates a new identity proposal and requires all
  dependent evidence to be requalified. Prior identity/evidence artifacts are
  immutable.
- A mutable-evidence-only rerun creates a new evidence bundle under the same
  stable key; it does not rewrite the earlier bundle.
- Schema PASS and digest PASS are structural/factual evidence only. They are
  not Pi approval, App adoption, authority supersession, release, reliance, or
  Task Management closure.

## Current verdict

`PLAN_READY / DIGEST_BLOCKED_PENDING_EXACT_STABLE_IDENTITY`.

The next lawful owners are the App loop for any independently accepted
PIA-U20–U25 work, the Root owning instrument for generic identity-contract
records, and a separately authorized Root PIA-U30 validation run after
accepted PIA-U22 and PIA-U23 evidence exists.
