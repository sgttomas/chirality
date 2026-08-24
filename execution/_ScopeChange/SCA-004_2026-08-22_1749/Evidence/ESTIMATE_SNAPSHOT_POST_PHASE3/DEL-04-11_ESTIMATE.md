# Estimate — DEL-04-11 Root Loop Receipt Validator

- **Status:** `DRAFT_AWAITING_OWNER_ACCEPTANCE`
- **Boundary:** derivative, non-authorizing estimate; separate `tools/**` M2 authority remains required
- **Total:** **92 base hours; 53–131 hours**

## Accepted inputs

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`, row `DEL-04-11_Root_Loop_Receipt_Validator`
- `execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-11_Root_Loop_Receipt_Validator/ScopeOfWork.md`, Ontology `OUT-001`..`OUT-004`, Praxeology `VER-001`..`VER-004`, and Output and Evaluation Matrix
- same folder `_CONTEXT.md`, Description, Anticipated Artifacts, and Context Boundary
- same folder `_DEPENDENCIES.md`, upstream doctrine/crosscheck inputs and downstream non-gating validation relationship

## Output-level work breakdown

| Element | Accepted output | Base h | Class | Low h | High h | Grounded rationale |
|---|---|---:|---|---:|---:|---|
| `E-0411-001` | OUT-001 Root-specific deterministic receipt validator and verification | 36 | `HIGH_UNCERTAINTY` | 18 | 54 | Produces the bounded D-7/E-2 validator while preserving DEL-04-05 doctrine and DEL-05-02 crosscheck ownership. |
| `E-0411-002` | OUT-002 deterministic valid/invalid fixtures and verification | 28 | `HIGH_UNCERTAINTY` | 14 | 42 | Builds bounded fixtures for the exact validator; detailed validator behavior is not yet specified. |
| `E-0411-003` | OUT-003 validator contract and CI invocation notes | 16 | `MEDIUM_UNCERTAINTY` | 12 | 20 | Documents the accepted evaluation boundary and invocation notes without selecting CI wiring. |
| `E-0411-004` | OUT-004 validation reports and identity/evaluation binding | 12 | `MEDIUM_UNCERTAINTY` | 9 | 15 | Produces reports bound to exact output identities and their declared evaluation boundary. |
| **Total** |  | **92** |  | **53** | **131** | Sum of line items. |

## Assumptions

- DEL-04-05 and DEL-05-02 provide accepted doctrine/crosscheck inputs; their
  own production work is not duplicated here.
- The non-gating DEL-02-06 validation relationship does not add integration
  hours to this carrier estimate.
- Exact tool behavior and CI wiring remain open and are reflected in
  uncertainty, not invented.

## Exclusions

All ten exact bindings listed in `ESTIMATE_METHOD.md` §Global exclusions are
excluded: `source_identity`, `release_identity`, both client-evidence slots,
Root semantic/regression evidence, census notice, Tier-0 relationship,
implementation act, cutover act, and release act. `TM-ROOT-106`,
`TM-ROOT-122`, C1, and all App-owned obligations are also excluded.

The hours estimate accepted output work if later authorized; they do not grant
the separately required `tools/**` M2 authority. Doctrine changes, DEL-04-05
or DEL-05-02 production, unspecified CI wiring, activation, and foreign-loop
work are not priced.

## Dependency-shaped sequencing risk

Phase 3 records two gating accepted-contract inputs: DEL-04-05 doctrine and
DEL-05-02 evidence discipline. It also records a non-gating validation
relationship to DEL-02-06. Drift in either accepted input would require
reassessment before reliance on this estimate, but no dates, precedence
decision, or schedule are computed.
