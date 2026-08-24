# Estimate — DEL-02-08 Exact Supply and Protocol Pinning

- **Status:** `DRAFT_AWAITING_OWNER_ACCEPTANCE`
- **Boundary:** derivative, non-authorizing estimate; hours are not a commitment or schedule
- **Total:** **100 base hours; 57–143 hours**

## Accepted inputs

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`, row `DEL-02-08_Exact_Supply_and_Protocol_Pinning`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/ScopeOfWork.md`, Ontology and Output and Evaluation Matrix `OUT-001`..`OUT-005`
- same folder `_CONTEXT.md`, Description, Anticipated Artifacts, and Context Boundary
- same folder `_DEPENDENCIES.md`, Extraction State, G1-blocker statement, and downstream `EVIDENCE_FAN_IN` edge to DEL-02-06

## Output-level work breakdown

| Element | Accepted output | Base h | Class | Low h | High h | Grounded rationale |
|---|---|---:|---|---:|---:|---|
| `E-0208-001` | OUT-001 exact supply manifest and protocol pin contract | 16 | `MEDIUM_UNCERTAINTY` | 12 | 20 | Defines one exact-supply/protocol contract without changing a deferred pin. |
| `E-0208-002` | OUT-002 enumerated OpenAI service-endpoint policy | 12 | `MEDIUM_UNCERTAINTY` | 9 | 15 | Separates the bounded account/model/turn endpoint enumeration from command-network authority. |
| `E-0208-003` | OUT-003 three-posture G-APPR fixture construction | 32 | `HIGH_UNCERTAINTY` | 16 | 48 | Builds fixtures for prompt delivery, destination grouping, and the three consent postures; exact-pin execution requiring C1 is excluded. |
| `E-0208-004` | OUT-004 G-WIRE and G-SUPPLY conformance fixture construction | 24 | `HIGH_UNCERTAINTY` | 12 | 36 | Produces bounded exact-basis fixtures; the not-yet-authorized artifact run is excluded. |
| `E-0208-005` | OUT-005 pin-drift and refusal-case evidence design | 16 | `HIGH_UNCERTAINTY` | 8 | 24 | Defines refusal coverage that preserves both G1 blockers and prohibits silent substitution; no pin act is priced. |
| **Total** |  | **100** |  | **57** | **143** | Sum of line items. |

## Assumptions

- Fixture construction and bounded verification design are estimable from the
  accepted outputs; empirical execution against the unavailable exact artifact
  is not included.
- No Root upstream deliverable edge or inferred ordering with DEL-02-09,
  DEL-02-10, or DEL-02-12 is assumed.

## Exclusions

All ten exact bindings listed in `ESTIMATE_METHOD.md` §Global exclusions are
excluded: `source_identity`, `release_identity`, both client-evidence slots,
Root semantic/regression evidence, census notice, Tier-0 relationship,
implementation act, cutover act, and release act. Also excluded are all
App-owned obligations.

DEL-02-08 specifically excludes any `TM-ROOT-106` or `TM-ROOT-122` disposition,
pin amendment, silent substitution, and C1/App Server 0.149.0 artifact download
or exact-artifact empirical run. The hours do not imply that those blockers
have cleared.

## Dependency-shaped sequencing risk

Phase 3 records no upstream Root edge and one gating fan-in edge to DEL-02-06.
The exact-pin empirical portion remains unavailable until its separately ruled
inputs exist, so the priced fixture work may precede an unpriced later evidence
run. No dates, precedence decision, or schedule are computed.
