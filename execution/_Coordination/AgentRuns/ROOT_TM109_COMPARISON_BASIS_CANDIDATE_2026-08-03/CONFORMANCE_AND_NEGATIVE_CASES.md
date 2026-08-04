# TM109-A structural conformance and negative-claim cases

Status: `NON-AUTHORITATIVE CANDIDATE TEST BASIS`

## Test oracle boundary

The companion JSON Schema can return only `STRUCTURALLY_VALID` or
`STRUCTURALLY_INVALID`. It cannot return `EQUAL`, `MATCHES`, `CONFORMS`,
`COMPATIBLE`, `ENGINEERING_ACCEPTABLE`, `AUTHORIZED`, or `HUMAN_ACCEPTED`.

All positive cases below are positive only for carrier structure. All claim
cases are evaluated against the semantic fence even if their JSON is
structurally valid.

## Positive structural cases

| ID | Input variation | Expected structural result | Non-effect |
|---|---|---|---|
| P-01 | One subject; operation identity; required basis/hash identities/outcome/evidence/provenance/claimant/caller/timestamp | `STRUCTURALLY_VALID` | Does not prove any comparison occurred |
| P-02 | Two subjects; tool identity only; no unit or tolerance refs | `STRUCTURALLY_VALID` | Does not imply subjects are comparable |
| P-03 | Both operation and tool identities | `STRUCTURALLY_VALID` | Does not define their relationship or authorize the tool |
| P-04 | Optional subject version and multiple described hashes | `STRUCTURALLY_VALID` | Does not select a preferred hash or establish equality |
| P-05 | Opaque unit and tolerance refs with only IDs | `STRUCTURALLY_VALID` | Does not dereference or apply either record |
| P-06 | `outcome.status = MISSING` with a diagnostic | `STRUCTURALLY_VALID` | Missing truth conditions remain consumer-local |
| P-07 | `outcome.status = INCOMPATIBLE` with two subjects | `STRUCTURALLY_VALID` | The label is claimant-asserted; no generic incompatibility is computed |
| P-08 | `outcome.status = BUDGET_EXHAUSTED` with evidence | `STRUCTURALLY_VALID` | Does not define budget dimensions limits continuation or finality |
| P-09 | Empty diagnostics array with `SUCCEEDED` | `STRUCTURALLY_VALID` | Does not prove success or lack of concerns |
| P-10 | Separate claimant and caller identities | `STRUCTURALLY_VALID` | Does not transfer accountability or prove authorization |

## Negative structural cases

| ID | Input defect | Expected result | Reason |
|---|---|---|---|
| S-01 | Missing `basis.id`, `basis.version`, or `basis.canonicalHash` | `STRUCTURALLY_INVALID` | Basis identity is incomplete |
| S-02 | Hash has digest only | `STRUCTURALLY_INVALID` | Algorithm canonicalization method and payload scope are mandatory descriptors |
| S-03 | Empty subjects array | `STRUCTURALLY_INVALID` | At least one subject is required |
| S-04 | Subject missing `subjectId` | `STRUCTURALLY_INVALID` | Subject identity is absent |
| S-05 | Neither operation nor tool identity | `STRUCTURALLY_INVALID` | At least one activity identity is required |
| S-06 | Missing consumer sandbox or policy identity | `STRUCTURALLY_INVALID` | Required identity context is absent |
| S-07 | Unknown top-level or nested property | `STRUCTURALLY_INVALID` | Objects are closed to prevent silent semantic smuggling |
| S-08 | Unit/tolerance reference is a free-form rule object | `STRUCTURALLY_INVALID` | Only opaque ID/version/hash carriage is allowed |
| S-09 | Outcome status not in candidate enum | `STRUCTURALLY_INVALID` | Candidate status vocabulary is closed pending human selection |
| S-10 | Evidence or provenance array empty | `STRUCTURALLY_INVALID` | At least one evidence ref and provenance record are required |
| S-11 | Provenance record lacks source or evidence refs | `STRUCTURALLY_INVALID` | Source-linked provenance is incomplete |
| S-12 | Claimant or caller missing | `STRUCTURALLY_INVALID` | Both identities are required |
| S-13 | Timestamp is not RFC 3339 date-time under the selected validator | `STRUCTURALLY_INVALID` | Candidate format check fails |

## Claims that must be rejected despite structural validity

| ID | Prohibited claim | Rejection basis |
|---|---|---|
| N-01 | “The two subjects are equal because their IDs match.” | IDs are namespace-local carrier text; no equality rule exists |
| N-02 | “The subjects match because all four hash fields match.” | Digest validation and accepted comparability remain outside the envelope |
| N-03 | “Two byte-identical envelopes prove the underlying runs are equivalent.” | Duplicate assertions can be false stale forged incomplete or locally inadmissible |
| N-04 | “Identical basis fields establish cross-consumer compatibility.” | A basis descriptor is not an accepted compatibility binding |
| N-05 | “Identical unit refs prove normalized quantities are equal.” | Unit taxonomy conversion and normalization remain consumer-local |
| N-06 | “Identical tolerance refs prove the same tolerance was applied or satisfied.” | Dereference suitability application and evaluation remain consumer-local |
| N-07 | “`INCOMPATIBLE` is a Root-wide compatibility decision.” | It is a claimant-asserted label with consumer-local truth conditions |
| N-08 | “`SUCCEEDED` authorizes reliance or means engineering acceptance.” | Outcome labels confer no authority professional standing or human acceptance |
| N-09 | “No diagnostics means conformance.” | Empty diagnostics carry no completeness or conformance guarantee |
| N-10 | “A sandbox ID proves OS containment.” | Identity carriage is not backend/profile/conformance evidence |
| N-11 | “A policy ID proves the operation was authorized.” | Identity is not request-time authorization or policy satisfaction |
| N-12 | “A tool ID proves the selected implementation family ran.” | Tool identity is not implementation evidence unless consumer-local evidence proves it |
| N-13 | “Evidence references prove the evidence is authentic and sufficient.” | References are opaque and are not fetched or validated by the schema |
| N-14 | “Claimant identity proves the claim is correct or professionally approved.” | Identity conveys neither truth nor professional authority |
| N-15 | “Matching timestamps prove causality or freshness.” | The carrier supplies no trusted clock or ordering semantics |
| N-16 | “A structurally valid envelope conforms to Piping comparison contracts.” | Piping mappings units tolerances review and professional boundaries remain local |
| N-17 | “A structurally valid envelope satisfies App parity or resume.” | App exact replay bindings and affected-client gates are separate |
| N-18 | “A structurally valid envelope satisfies Root runtime preflight.” | Runtime compatibility identity/header/binding remain separate and unresolved |

## Identical-envelope adversarial case

Given envelopes `A` and `B` with identical bytes, a generic processor may
state only that their serialized candidate instances are byte-identical under
the processor's explicitly named byte-comparison operation. It must still
reject every claim about subject equality, run equivalence, result
conformance, engineering acceptability, runtime compatibility, App resume, or
Piping comparison. It must not turn byte identity into semantic identity.

## Canonical-hash adversarial cases

1. Same digest, different algorithm IDs: reject equality inference.
2. Same digest/algorithm, different canonicalization-method IDs: reject.
3. Same digest/algorithm/method, different payload-scope IDs: reject.
4. All four fields match but method/scope is unaccepted by the consumer:
   reject.
5. All four fields match but evidence does not prove recomputation: reject.
6. All four fields match across different subject namespaces: reject.

## Consumer-local adapter obligation

Any later adapter that reads the envelope must fail closed when its own
accepted semantics, namespace mapping, reference resolution, evidence checks,
or authorization are missing. It may not infer a default equality rule,
canonicalization, tolerance, conversion, compatibility state, or acceptance
from this candidate.
