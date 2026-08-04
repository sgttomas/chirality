# Provenance contract — fresh DEL-02-06 accepted-input candidate

Status: `BLUEPRINT — NOT ACCEPTED`

## Candidate character

The future packet is a fresh current-basis synthesis. It is not a recovery,
reproduction, reconstruction, transcription, or replacement claim for the
missing historical authoring-envelope bytes named by the accepted Scope of
Work. Historical filename continuity is required by the live first-activation
contract; it does not imply byte, authorship, or acceptance continuity.

## Governing and source classes

| Class | Permitted use | Required binding |
|---|---|---|
| Accepted deliverable contract | Defines packet purpose, filenames, requirements, open items, and first-activation boundary | `ScopeOfWork.md` SHA-256 `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146` |
| Owner preparation authority | Authorizes a fresh candidate and preserves its later exact acceptance gate | Continuation ruling SHA-256 `9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6` |
| Applied current basis | Supplies only the post-S2 current-facing PRD/decomposition identities and acceptance-state proof | `{{S2_APPLIED_REPOSITORY_BASIS}}`, `{{S2_PRD_SHA256}}`, `{{S2_DECOMPOSITION_SHA256}}`, `{{S2_DECISION_LOG_SHA256}}`, `{{S2_GATE5_VALIDATION_SHA256}}`, `{{S2_HANDOFF_SHA256}}` |
| Routed concern | Establishes the recovery concern and eventual evidence request, not packet acceptance or repair semantics | TM-ROOT-108 handoff SHA-256 `da191f8c12207398c676531daf8941148797dc4f206c33ad58797a1e74a77fbc`; D-APP-85 route SHA-256 `0b34cefdc9abd5927db1b6bdda07225c37c42806ff5b3f946bb182227f08dc41` |
| Manager planning evidence | Supplies provisional recovery requirements and test design without authority effect | `MANAGER_RECOVERY_CHANGE_PLAN.md`; its hash is recomputed at candidate instantiation |
| Candidate synthesis | May organize and restate accepted requirements for planning | Must label every file fresh/current-basis/candidate/not accepted |

## S2 placeholder rule

The six templates may contain placeholders only for values that do not exist
until the S2 basis reconciliation is accepted, applied, and validated:

- `{{S2_APPLIED_REPOSITORY_BASIS}}`
- `{{S2_PRD_SHA256}}`
- `{{S2_DECOMPOSITION_SHA256}}`
- `{{S2_DECISION_LOG_SHA256}}`
- `{{S2_GATE5_VALIDATION_SHA256}}`
- `{{S2_HANDOFF_SHA256}}`
- `{{S2_APPLIED_FILE_HASHES_SHA256}}`
- `{{POST_S2_SHA256_DEGRADED_MODE_CONTRACT_CANDIDATE_MD}}`
- `{{POST_S2_SHA256_OPEN_ITEMS_CSV}}`
- `{{POST_S2_SHA256_OWNER_GATE_MD}}`
- `{{POST_S2_SHA256_OWNER_SELECTION_MD}}`
- `{{POST_S2_SHA256_ROOT_COMPATIBILITY_POLICY_CANDIDATE_MD}}`

No placeholder may stand for a semantic choice, compatibility value, terminal
class, retry rule, affected-client result, owner identity, acceptance token, or
evidence result. Those remain explicit unresolved fields or later gate acts.

## Claim rules

1. Accepted requirements may be restated only with their exact `REQ-*`,
   `AC-*`, `VER-*`, or `TBD-*` source identity and accepted Scope-of-Work hash.
2. D-APP-85 and TM-ROOT-108 may support the observed recovery concern and
   requested proof only; they cannot select a terminal state or implementation.
3. S2 may cure current-facing acceptance/status metadata only. It cannot be
   cited as creating runtime semantics, scope, topology, client obligation, or
   packet acceptance.
4. `AFFECTED` client status requires a separately accepted obligation source.
   The packet leaves actual-client results unresolved.
5. Candidate validation proves internal consistency and provenance bindings,
   not semantic acceptance, implementation fitness, release readiness, or
   reliance.
6. Owner acceptance of this packet accepts it only as the exact first-
   activation planning input. It does not accept either semantic candidate as
   the runtime contract.

## Candidate identity

The five content files are hashed into
`CANDIDATE_SET_MANIFEST.sha256`. The SHA-256 of the exact manifest bytes is the
candidate-set identity presented to the owner. The external acceptance record
quotes that manifest identity. Neither the acceptance record nor the manifest
hash is written into a content file, avoiding a self-referential hash cycle.
