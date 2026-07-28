# R-A — Root runtime release and rollback candidate

**Status:** `EXACT_SCHEMA_CANDIDATE_AWAITING_OWNER_RULING`
**Candidate effect if accepted:** future release-assurance design basis only;
no release instance, build, distribution, activation, or rollback

## 1. Aggregate release identity

The proposed case-sensitive aggregate release identity grammar is:

```text
chirality.runtime.release.v1.sha256.<64-lowercase-hex>
```

Formally:

```abnf
release-id = "chirality.runtime.release.v1.sha256." 64lowerhex
lowerhex = DIGIT / %x61-66
```

The digest is SHA-256 of the exact UTF-8 bytes of a canonical Root runtime
release-binding manifest serialized using RFC 8785 JSON Canonicalization
Scheme. The manifest does not contain its own `releaseId` or
`manifestSha256`; the later release-act record derives and records them after
hashing. This avoids a self-hash cycle.

An optional tag or display label may alias a release ID but is never release,
compatibility, or authority identity.

## 2. Manifest schema

`R-A_RELEASE_MANIFEST_SCHEMA_CANDIDATE.json` is the normative nested schema.
Its lexical patterns, required fields, nullability, closed objects,
conditional requirements, enum values, sorting keys, and uniqueness keys are
part of this exact candidate.

The schema literal is:

```text
chirality.runtime.release-manifest/v1
```

V1 rejects unknown members at every object level. Required members are:

- `schema`: the exact literal above;
- `subject`: exact literal `chirality-root-runtime`;
- `source`: `{repositoryId, commitSha, treeSha, dirty:false}`;
- `compatibility`: `{rootRuntimeCompatibilityIdentity,
  apiRouteNamespace, flowAConcordance}`;
- `components`: a sorted array of `{packageName, packageVersion,
  sourcePath}`;
- `build`: `{buildRecord, toolchain[], lockfiles[],
  commands[], environmentClass, reproducibilityDisposition}`;
- `artifacts`: a non-empty array sorted by `artifactId`;
- `affectedClients`: a sorted array by `clientId`;
- `migrations`: a sorted array by `migrationId`;
- `validation`: regression, conformance, security, packaging, and known-
  limitation references;
- `rollback`: exact assessment and target/evidence/plan fields; and
- `preparation`: immutable provenance
  `{preparedAt, preparedByRunId, acceptedSourceBasis}`.

All Git object IDs and SHA-256 values are full lowercase strings. Paths are
repository-relative. Every referenced record or file carries its own path,
hash, and accepted basis. Secrets are excluded.

Every evidence-reference array is set-like and serialized in ascending order
by `(basis.commitSha, basis.treeSha, path, sha256)`, with that tuple unique.
This rule applies recursively to validation, client, migration, rollback,
limitation, build, and Flow-A concordance references.

### Artifacts

Each artifact is:

```text
{artifactId, role, relativePath, sha256, sizeBytes, mediaType,
 platform:{os,arch}, packagingContext}
```

Allowed roles are `contracts | core | daemon | client | cli |
engine-adapter | other`; `other` requires a reason. Hashes cover
the distributed bytes.

An App bundle is not a Root-owned release artifact. If App packages Root
runtime bytes, the Root manifest records the Root artifacts and the
`affectedClients` row cites a separately accepted App-owned packaging act and
its evidence. Enumeration never grants Root App write or release authority.

### Affected clients

Each affected-client row is:

```text
{clientId, implementationState, applicability, acceptedBasis,
 compatibilityIdentityExpected, disposition, evidenceRefs[],
 migrationRefs[], degradedModeEvidenceRef, rollbackEvidenceRef}
```

Allowed values:

- `implementationState`: `ACTIVE_IMPLEMENTED | PROSPECTIVE | RETIRED`;
- `applicability`: `AFFECTED | NOT_AFFECTED | UNRESOLVED`;
- `disposition`: `CONFORMANT | MIGRATION_ACCEPTED | BLOCKED |
  NOT_APPLICABLE | DEFERRED`.

Prospective clients do not acquire work, authority, or a closure veto.

`flowAConcordance.disposition=SEPARATE_UNRESOLVED` is permitted with citations
to existing Tier-0 authority. A mapping, retirement, or supersession requires
its own later Tier-0 authority reference; D-T0-24 adoption is not a prerequisite
for preparing or releasing a separately identified Root runtime.

### Migrations

Each migration is:

```text
{migrationId, stateSurface, fromSchema, toSchema, direction,
 evidenceRefs[], inverseOrRestoreRef}
```

`direction` is `NO_STATE_CHANGE | REVERSIBLE | FORWARD_ONLY`.

### Rollback

The rollback object is:

```text
{assessment, targetReleaseId, targetReleaseActRef,
 artifactAvailabilityEvidenceRef, stateCompatibilityEvidenceRefs[],
 affectedClientEvidenceRefs[], executionPlanRef, verificationPlanRef,
 blockedReasons[]}
```

`assessment` is `ELIGIBLE | INELIGIBLE | UNASSESSED | NOT_APPLICABLE`.
Initial release may be `NOT_APPLICABLE`. A target is named when eligibility
is assessed against a specific prior release.

## 3. Validator contract

A deterministic validator:

1. validates schema, enums, required fields, and exact literals;
2. rejects unknown top-level members, duplicates, unsorted arrays, absolute
   paths, dirty source, malformed IDs, and noncanonical values;
3. resolves and verifies every referenced path and hash at its accepted basis;
4. verifies each declared artifact size and SHA-256 against the exact resolved
   artifact bytes and verifies each artifact identity is unique;
5. RFC-8785 canonicalizes the manifest;
6. derives the SHA-256 and exact release ID; and
7. emits a reproducible validation report.

Validation or hash existence does not release anything. Release state is never
a mutable field inside the content-addressed manifest. A release ID becomes
`RELEASED` only through a separate accountable-human act naming the exact
manifest SHA-256, release ID, and candidate source basis.

## 4. Release-admission predicate

A release candidate is **deterministically admissible for human judgment**
only when all of the following are true:

1. the complete manifest validates against the normative JSON Schema,
   canonical ordering/uniqueness extensions, reference resolver, RFC-8785
   canonicalizer, and artifact-byte verifier;
2. source is clean; every referenced basis and hash resolves; every build,
   artifact, migration, validation, and limitation record is present;
3. `reproducibilityDisposition` is `REPRODUCIBLE`, or is
   `CONDITIONALLY_REPRODUCIBLE` with a non-BLOCK limitation explicitly marked
   `ACCEPTED_FOR_RELEASE`; `NOT_REPRODUCIBLE` and `UNASSESSED` block admission;
4. every `ACTIVE_IMPLEMENTED` client has applicability resolved:
   - `AFFECTED` requires `CONFORMANT` or `MIGRATION_ACCEPTED`, non-null expected
     compatibility identity, degraded-mode evidence, rollback evidence, and
     at least one exact evidence reference;
   - `NOT_AFFECTED` requires `NOT_APPLICABLE` plus evidence;
   - `UNRESOLVED`, `BLOCKED`, or `DEFERRED` blocks admission;
5. `PROSPECTIVE` and `RETIRED` clients are recorded as `NOT_APPLICABLE` or
   `DEFERRED` and never veto admission or create work;
6. every migration has evidence; `REVERSIBLE` has an inverse/restore reference;
   every `FORWARD_ONLY` migration is disclosed in rollback assessment;
7. all four validation arrays are non-empty and verified; any limitation with
   severity `BLOCK` or disposition `BLOCKS_RELEASE` blocks admission;
8. rollback is not `UNASSESSED`: `NOT_APPLICABLE` is allowed only for a true
   initial release, while `ELIGIBLE` and `INELIGIBLE` satisfy their schema
   evidence/blocked-reason conditions; and
9. V-A, D-A, the Root carrier, exact implementation/build authority, and all
   affected-client dispositions are effective at the candidate basis.

Passing this predicate makes the candidate eligible to be presented. It never
waives a failed prerequisite and never releases, distributes, or activates
anything. A separate accountable-human release judgment remains mandatory.

## 5. Identity distinctions

- compatibility identity: semantic daemon/client epoch compared before
  consequential operations;
- release identity: exact aggregate artifact/evidence manifest;
- source commit/tree: source bytes only;
- build record/hash: one construction event and environment;
- package versions: component labels;
- `/v1`: route namespace;
- runtime fingerprint: observed execution/configuration provenance;
- Flow-A: separate Tier-0 historical contract identity;
- tag/display label: optional alias only;
- publication/effective SHA: identity of later human acts, recorded outside
  the content-addressed manifest.

No identity substitutes for another.

## 6. Rollback eligibility

A target is `ELIGIBLE` only when:

1. it has a prior human release act and exact manifest/artifacts remain
   hash-verifiable;
2. current-to-target operational state and schema transition is proven
   reversible or restore-tested;
3. every active implemented affected client is compatible with the target or
   has an accepted coordinated rollback/migration;
4. credential, session, registration, and adapter state is explicitly
   dispositioned without exposing secrets;
5. in-flight and indeterminate operations have accepted drain, cancel, and
   reconciliation rules;
6. project-authoritative checkout truth remains untouched;
7. exact rollback and verification plans and evidence exist; and
8. an accountable human separately approves the exact current-to-target act.

`UNASSESSED` blocks rollback reliance. A `FORWARD_ONLY`
migration makes the target ineligible unless an independently accepted restore
path proves otherwise.

Rollback is not reconnect/rebind, automatic daemon fallback, model/provider
fallback, source checkout, or Git history rewrite. A patched successor is a
new forward release.

## 7. Rollback execution

1. The human approves exact current release, target release, plan hash,
   write/data fence, and abort conditions.
2. New consequential operations stop; typed degraded state is exposed; active
   and indeterminate work is inventoried.
3. Work drains or cancels under accepted rules; redacted state census and
   tested backup/snapshot are captured where allowed.
4. Target release act, manifest, artifact hashes, state/client compatibility,
   and authority are reverified immediately before switching.
5. Exact target artifacts and only accepted inverse/restore migrations are
   applied; no alternate runtime loop is introduced.
6. Exact-identity preflight, health, security, regression smoke, and affected-
   client checks run after restart.
7. Failure does not cause oscillation or silent return to either version. The
   runtime remains fail-closed unless the approved plan expressly authorizes a
   restoration step; unresolved state returns to the human.
8. The outcome, effective artifacts, client results, and every indeterminate
   operation disposition are recorded.

## 8. Later gates

- `R0`: accepted `DEL-02-06` ScopeOfWork and sealed activation.
- `R1`: exact release schema and validator acceptance.
- `R2`: accepted compatibility identity, D-A semantics, and preflight
  contract.
- `R3`: exact implementation/build/write-fence authorization.
- `R4`: candidate freeze with clean source, canonical manifest, derived ID,
  exact artifacts, and hashes.
- `R5`: affected-client applicability, conformance, and migration dispositions
  through their own instruments.
- `R6`: accountable-human Root release judgment.
- `R7`: separate distribution/activation act.
- `R8`: separate exact rollback target/plan act when needed.

## 9. Values intentionally unresolved

No actual compatibility or release ID, repository ID, source/tree/release/
publication/effective SHA, package-version change, artifact/platform matrix,
build command/environment, manifest path, affected-client disposition,
migration, predecessor, rollback target, retention, signing/notarization,
publication, tag, implementation byte, or release/activation/rollback act is
selected here.
