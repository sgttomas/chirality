# D-PEC-74 O-A — DEL-08-02 production activation

**State:** PRODUCER COMPLETE / CANDIDATE OUTPUT / REVIEW AND OWNER GATES OPEN

**Run date:** 2026-08-01

**Manager:** WORKING_ITEMS, managed by HELP_HUMAN

**Package:** PKG-08 API & Access

**Selected deliverable:** DEL-08-02 only

**Authority:**
`projects/pec/execution/_Coordination/D-PEC-74_FIRST_P1_SOURCE_SLICE_2026-08-01/O-A_ACTIVATION_AUTHORITY_2026-08-01.md`
at authority commit `49676473884e07a78fa197a23451e13a12850427`

## Activation resolution

- Contract form: `SOW_V1`.
- Contract SHA-256:
  `eb171e9dac40b313be8ea8ff75ad395171b599a41d2a1dbf290a9c5b44290c20`.
- Accepted ADR SHA-256:
  `f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5`.
- Accepted SPEC SHA-256:
  `8b25a0d1f7ec7451ed3d19839904ee0c5f9a69b94df50f2122d9065c59a02315`.
- Reliance-hold preflight target:
  `execution/PKG-08_API_Access/1_Working/DEL-08-02_Versioned_additive_API_schema/ScopeOfWork.md`.
- Operation: `dispatch-for-production`; result: `ALLOW`.
- Lifecycle before and after production: `INITIALIZED`; `_STATUS.md` was not
  written.

## Frozen work graph v1

Selection authority is the owner's `D-PEC-74: O-A.` ruling. The posture was a
serialized, single-integration-node activation because all six production
files form one compatibility contract.

| Node | Objective | Ownership | Dependencies | Return gate | Outcome |
|---|---|---|---|---|---|
| N1 | Implement the schema, compatibility mechanism, fixtures, and exact profile | One bounded ephemeral Agent 2 integration owner | reliance preflight | six exact files; unit evidence; no out-of-fence write | Two attempted child sessions were interrupted before producing a file or return and were not accepted at fan-in. |
| N2 | Bounded integration remediation under the same frozen objective and paths | WORKING_ITEMS serialized integration owner | N1 returned no output; no partial state existed | exact profile; targeted tests; affected checks; registered evidence | Complete. |
| N3 | Validate package fan-in and publish candidate evidence | WORKING_ITEMS | N2 | SOW, registered checks, fixtures, registers, closure, containment, manifest, harness, coordination, whitespace | Complete subject to committed-range coordination rerun by CHANGE. |

No child brief, failure, or remediation changed objective, scope, write paths,
acceptance criteria, lifecycle, or authority. No concurrent write occurred.

## Producer outputs

| Output | SHA-256 |
|---|---|
| `projects/pec/software-workflow.json` | `46f8495444de922d5f85bd71ee473d8ff980fac0b8c30392d7ddf76fee4fff82` |
| `projects/pec/v2/contracts/api/v1/schema.json` | `0a4e42737e628be604bd163e8c6f835cda488f7978ae9e973cff03d1f8695c67` |
| `projects/pec/v2/tests/contracts/api/test_api_schema_compatibility.py` | `efdd32f24c0045160d7a736b1ffbdc2b8685246a66c8c362aba8899747decc92` |
| `projects/pec/v2/tests/contracts/api/fixtures/v1_additive_candidate.json` | `b3ed8554e93e1380617ceb9d1de6030e684ddd91c89763d0d7565af56e079718` |
| `projects/pec/v2/tests/contracts/api/fixtures/v1_removed_element_candidate.json` | `eb25e52b14e4fcf98e48fec7a66d4988e5bfac590c6c30806cde3ed78338bacb` |
| `projects/pec/v2/tests/contracts/api/fixtures/v1_meaning_changed_candidate.json` | `bd2617a7cc47049af503c45fe6f86ec2c5f8270ae47950c9970288780c318cb8` |

The schema declares JSON Schema draft 2020-12, API schema version integer `1`
at the artifact and request/response shape levels, and PEC-owned capability /
use-case names. Its compatibility mechanism preserves every published
element's value and `x-pec-meaning`, admits only new definitions and optional
properties with declared meaning, and fails closed on an unclassifiable
change.

## Verification evidence

- Exact profile comparison to the authority's JSON block: byte-equal apart
  from the allowed terminating newline.
- Scope validation: `PASS format=SOW_V1`.
- Affected-check selection: `v2-api-contract` selected for all five v2
  source/test paths and `software-workflow.json`; `harness-self-check`
  selected by `always_checks`.
- Registered evidence:
  `D-PEC-74_REGISTERED_CHECKS.json`, SHA-256
  `1505fc3973509f81feb62449d8d917076ce6891e37cc426081e6aa233736fa89`.
- `v2-api-contract`: PASS, six tests.
- `harness-self-check`: PASS; unchanged baseline
  `INFO=15 / NOT_APPLICABLE=1 / REVIEW=5 / WARN=28`.
- Additive fixture: PASS with `[]` findings.
- Removal fixture: FAIL as intended at
  `/$defs/CapabilityRequest/properties/use_case` and
  `/$defs/CapabilityRequest/required`.
- Meaning-change fixture: FAIL as intended at
  `/$defs/CapabilityRequest/properties/capability/x-pec-meaning`.
- Strict decomposition registers: 64 registers / 254 rows / zero errors /
  zero warnings.
- Dependency closure: 64 valid registers / 254 rows / 119 execution edges /
  zero SCCs / zero bidirectional pairs.
- Exact changed-path containment: PASS.
- `git diff --check`: PASS.
- No frozen-corpus, root-runtime, store, service, socket, network,
  dependency-manifest, other-loop, ScopeOfWork, decomposition, accepted
  ADR/SPEC, `_STATUS.md`, or lifecycle write occurred.

## Fan-in disposition and open gates

Producer fan-in is accepted as a complete candidate return. This is not
artifact fitness, lifecycle acceptance, release, or professional reliance.
The following remain separate human-gated acts:

1. REVIEW type selection and any review-from-`INITIALIZED` override;
2. finding disposition and REVIEW Gate 5;
3. AC-005 confirmation of the MEDIUM-confidence `DEL-08-02 → OBJ-001`
   attribution given the unadopted `OBJ-001;OBJ-004` and full-consumer-set
   alternatives;
4. exact-hash artifact-fitness acceptance; and
5. Git publication and merge through CHANGE.

No later P1 node opens automatically. OI-009, transport/access/authentication,
compact citation-bearing response format, latency, subscriptions,
service/store/runtime integration, actor-specific cross-loop types, release,
and professional reliance remain outside this activation.
