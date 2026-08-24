# Estimate — DEL-02-10 Adapter Event Schema and Approval API v2

- **Status:** `DRAFT_AWAITING_OWNER_ACCEPTANCE`
- **Boundary:** derivative, non-authorizing estimate; hours are not a commitment or schedule
- **Total:** **144 base hours; 88–200 hours**

## Accepted inputs

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`, row `DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/ScopeOfWork.md`, Ontology and Output and Evaluation Matrix `OUT-001`..`OUT-006`
- same folder `_CONTEXT.md`, Description, Anticipated Artifacts, and Context Boundary
- same folder `_DEPENDENCIES.md`, Extraction State and downstream `EVIDENCE_FAN_IN` edge to DEL-02-06

## Output-level work breakdown

| Element | Accepted output | Base h | Class | Low h | High h | Grounded rationale |
|---|---|---:|---|---:|---:|---|
| `E-0210-001` | OUT-001 Root runtime API v2 contract | 24 | `MEDIUM_UNCERTAINTY` | 18 | 30 | One versioned contract spanning event, approval, role-posture, and managed-network projection boundaries. |
| `E-0210-002` | OUT-002 attributed approval request/decision schemas | 20 | `MEDIUM_UNCERTAINTY` | 15 | 25 | Defines and verifies attributed request and decision records while excluding unattributed decisions. |
| `E-0210-003` | OUT-003 closed HarnessEvent v2 union | 20 | `MEDIUM_UNCERTAINTY` | 15 | 25 | Defines the closed union and verifies exactly four terminal identifiers with no fifth terminal. |
| `E-0210-004` | OUT-004 role-posture evidence projection | 20 | `HIGH_UNCERTAINTY` | 10 | 30 | Preserves parity, labelled fallback, and instruction-asserted calibration across the adapter projection. |
| `E-0210-005` | OUT-005 managed-network approval routing | 32 | `HIGH_UNCERTAINTY` | 16 | 48 | Covers routed context, host/protocol, grouping caveat, explicit-user session consent, three postures, and service-endpoint separation. |
| `E-0210-006` | OUT-006 adapter projection/redaction fixtures | 28 | `HIGH_UNCERTAINTY` | 14 | 42 | Produces deterministic reject/redact/project fixtures and verifies no provider-shaped persistence. |
| **Total** |  | **144** |  | **88** | **200** | Sum of line items. |

## Assumptions

- Each schema/fixture line includes only its accepted Root API/adapter output
  and deliverable-local verification.
- No ordering is inferred from semantic overlap with supply, consent,
  retirement, or conformance carriers.
- Provider-specific details absent from the accepted contract are not assumed.

## Exclusions

All ten exact bindings listed in `ESTIMATE_METHOD.md` §Global exclusions are
excluded: `source_identity`, `release_identity`, both client-evidence slots,
Root semantic/regression evidence, census notice, Tier-0 relationship,
implementation act, cutover act, and release act. `TM-ROOT-106`,
`TM-ROOT-122`, C1, and all App-owned adapter/client obligations are also
excluded.

Provider-shaped persistence, unattributed decisions, consent grants,
activation, hold satisfaction, and foreign-loop work are not priced.

## Dependency-shaped sequencing risk

Phase 3 records no Root upstream edge and one gating evidence-fan-in edge to
DEL-02-06. Contract and fixture work is estimable without inventing carrier
precedence, while accepted evidence must later fan in before integration can
close. No dates, precedence decision, or schedule are computed.
