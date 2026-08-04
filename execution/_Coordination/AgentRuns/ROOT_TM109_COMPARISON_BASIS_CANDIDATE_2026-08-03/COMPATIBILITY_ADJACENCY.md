# Compatibility adjacency and difference analysis

Status: `NON-AUTHORITATIVE CANDIDATE ANALYSIS`

## Controlling distinction

The TM109-A carrier records identity and provenance. It does not define or
apply compatibility. The same word appearing in adjacent Root, App, or Piping
surfaces does not merge those surfaces' contracts.

| Surface | What it owns | What this carrier may record | What this carrier must not do |
|---|---|---|---|
| Root runtime compatibility identity | Runtime protocol declaration, exact preflight comparison, epoch/binding, affected-client gating, and mismatch handling if later accepted | Basis, runtime/consumer/tool/policy identities, described hashes, outcome label, diagnostics, and evidence references | Mint a runtime epoch, select equality, perform preflight, declare a client compatible, or replace a binding record |
| App parity and strict resume | App-local parity evidence and exact replay binding over accepted Root identity, Pi version, sandbox profile, model, residency epoch, and transcript/event prefix | Record the App consumer, session/tool/sandbox/policy identities, subjects, opaque evidence, and App-asserted outcome | Establish parity, decide replay admissibility, hydrate a session, authorize resume, or claim App compatibility |
| Piping comparison | Participant identity, mapping admissibility, unit/dimension taxonomy, normalization, tolerance rules, result-family/solver meaning, diagnostics, privacy, professional boundaries, and human review | Carry Piping-owned identities, opaque unit/tolerance refs, Piping-asserted status/diagnostics, and provenance | Map participants, normalize units, apply tolerances, compare results, make engineering claims, or upgrade review state |

## Root runtime adjacency

Current implemented Root source is evidence of vocabulary and gaps, not
semantic authority for this candidate:

- `runtime/packages/contracts/src/protocol.ts` at
  `1d8d329fb2f296de30aa13c04f5d528efa717a762b49936000a9b162f50bfa9e`
  defines route/API identity and a health response with `apiVersion`,
  `daemonId`, and process state, but no accepted generic comparison envelope
  or runtime compatibility declaration.
- `runtime/packages/contracts/src/session.ts` at
  `22e49ccf47a83e93d065a1d731a0e726cba6559f8436f78c3451d4db2fd8bf51`
  carries session schema, project/session/role, engine selection, residency
  epoch, lifecycle state, and parent identity. Those are adjacent identity
  sources; the TM109-A carrier does not change session semantics.
- `runtime/packages/contracts/src/errors.ts` at
  `75d30b4139c8ba11264cb1165c4e51401cbc9c930770e8cb966513509b6b1501`
  defines implemented runtime errors but lacks the candidate's explicit
  `MISSING`, `INCOMPATIBLE`, and `BUDGET_EXHAUSTED` carrier vocabulary. The
  candidate does not amend the error taxonomy.
- `runtime/packages/core/src/compatibility-session-policy.ts` at
  `965ded92cbfb8430c6950a55fb267eb7e3307a4b669c5cc0c6e1b11060c32785`
  resolves a default engine adapter/provider/model. It is selection policy,
  not a comparison-basis or compatibility decision.
- `runtime/packages/contracts/src/harness/types.ts` at
  `7e035b3a7b1d50176b7f0605b62da9695502305a38d61e27b7c3799531de70e3`
  carries session, engine, instruction/brief, runtime fingerprint, and
  orchestration identities. These may become envelope identity inputs only
  after later accepted mapping rules; the candidate performs no mapping.
- `runtime/packages/contracts/src/harness/tool-descriptor.ts` at
  `bcb87844dce118a3f7743b3e2e0ecc0c376627d2dbaf1dee483a281c6f2b767b`
  carries tool registry version, descriptor name, permissions, result budget,
  provenance policy, gate, adapter, and runtime support. The envelope may
  record a tool/policy identity and a `BUDGET_EXHAUSTED` assertion, but does
  not authorize a tool, evaluate a budget, or prove descriptor conformance.

The earlier `chirality.runtime.compatibility/v1` document at SHA-256
`79ea5982db946fda9e1c5356a471da4f3bb8509507a6648595abaf65e928eb5f`
is explicitly a candidate awaiting owner ruling. It proposes exact code-point
equality, preflight ordering, a mismatch envelope, and a lifecycle binding
record. None of those semantics flow into TM109-A. The current DEL-02-06
compatibility disposition at SHA-256
`689b41e3fc9416a5fcc637c4ebe543f4b6272b96fe32f65f47766855c222dda1`
also remains candidate/not adopted and holds exact compatibility values open.

Therefore:

- a TM109-A `basis.id` is not the Root runtime compatibility epoch;
- an envelope hash is not the same-request compatibility header check;
- `outcome.status = INCOMPATIBLE` is not
  `RUNTIME_COMPATIBILITY_MISMATCH`; and
- envelope structural validity is not an `EFFECTIVE` runtime binding record.

## App parity and resume adjacency

D-APP-84 is an App-local ruling. It targets strict resume only after exact
equality over an accepted Root compatibility identity, Pi version, sandbox
profile, model, residency epoch, and transcript/event-prefix SHA-256. It also
requires a fresh sandboxed worker and disallows silent resume/replay after a
mismatch.

The TM109-A carrier could later record those identities and the evidence of an
App-local decision, but cannot:

1. choose which fields form App parity or resume equality;
2. validate an event prefix or replay state;
3. declare a sandbox profile conforming;
4. reconcile Pi versions;
5. turn App's prospective R1 target into operational permission; or
6. satisfy App affected-client, SCOPE_CHANGE, conformance, implementation, or
   acceptance gates.

Two byte-identical TM109-A envelopes do not prove two App sessions are safe to
resume. They could be duplicate unsupported assertions, use an unaccepted
canonicalization method, omit locally mandatory state, or refer to stale or
forged evidence.

## Piping comparison adjacency

Piping response section 6 separates locally owned comparison semantics from a
candidate cross-consumer identity carrier. Direct local evidence shows why:

- E-11 (`operation_outcome.schema.json`) carries validation, model-basis,
  audit, acceptance, and professional-boundary meanings. Its model-basis
  record expressly distinguishes claimed hash echo from evaluated equality.
- E-13 (`headless_runner.schema.yaml`) carries request/run/job identities,
  local analysis status, unit-system refs, checksums, diagnostics, provenance,
  privacy, cancellation, and professional-boundary fields.
- E-18 (`comparison_tolerance.schema.json`) defines Piping dimension,
  normalization, unit-metadata, tolerance-profile, review, and provenance
  vocabulary. It explicitly does not define default numeric tolerances or a
  result-delta engine.
- E-19 (`comparison_mapping.schema.json`) defines participants, stable record
  refs, mappings, mapping status/evidence/confidence, unmatched records,
  tolerance refs, exports, review, provenance, and professional boundaries.

TM109-A intentionally does not copy Piping's `MappingStatus`, `DimensionId`,
`ToleranceRule`, `AnalysisStatus`, privacy classes, professional-boundary
record, or review semantics. A Piping adapter may reference a Piping record as
opaque evidence, but only Piping decides whether that evidence is admissible
and what it means.

## Difference matrix

| Question | TM109-A carrier answer | Owning answer |
|---|---|---|
| Are two basis records equal? | Not defined | Consumer-local or separately accepted Root runtime contract |
| Do two subject IDs name the same object? | Not defined | Consumer namespace and mapping rules |
| Are hashes comparable? | Not defined; four descriptors are carried | Consumer-selected algorithm/canonicalization/scope and validation |
| Are units convertible? | Not defined | Piping/consumer unit taxonomy and conversion rules |
| Is a tolerance suitable or satisfied? | Not defined | Piping/consumer tolerance and engineering review |
| Is a runtime/client compatible? | Not defined | Root compatibility binding plus affected-client evidence |
| Is an App session resumable? | Not defined | App replay-and-bind policy after Root prerequisites |
| Is a tool authorized? | Not defined | Accepted tool/sandbox/policy contracts and request-time decision |
| Is an outcome true? | Not established; claimant assertion is carried | Consumer evidence and acceptance process |
| Is professional or human acceptance present? | Never inferred | Consumer-local human/professional instrument |

## No-conflation rule

No adapter may convert any of the following into a generic compatibility
claim merely because an envelope is present or structurally valid:

- equal strings, versions, hashes, or opaque reference IDs;
- identical envelope bytes;
- a `SUCCEEDED` or `INCOMPATIBLE` label;
- absence of diagnostics;
- presence of provenance/evidence references;
- App parity or resume metadata;
- Root API/runtime/session identity; or
- Piping mapping/tolerance/review records.

