# Estimate — DEL-02-11 Worker Retirement, Restart, and Terminal Reconciliation

- **Status:** `DRAFT_AWAITING_OWNER_ACCEPTANCE`
- **Boundary:** derivative, non-authorizing estimate; hours are not a commitment or schedule
- **Total:** **136 base hours; 72–200 hours**

## Accepted inputs

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`, row `DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/ScopeOfWork.md`, Ontology and Output and Evaluation Matrix `OUT-001`..`OUT-005`
- same folder `_CONTEXT.md`, Description, Anticipated Artifacts, and Context Boundary
- same folder `_DEPENDENCIES.md`, Extraction State and downstream `EVIDENCE_FAN_IN` edge to DEL-02-06

## Output-level work breakdown

| Element | Accepted output | Base h | Class | Low h | High h | Grounded rationale |
|---|---|---:|---|---:|---:|---|
| `E-0211-001` | OUT-001 `WorkerRetirementCoordinatorPort` contract | 16 | `MEDIUM_UNCERTAINTY` | 12 | 20 | One named coordinator contract bounded to retirement, restart, and reconciliation. |
| `E-0211-002` | OUT-002 retirement journal and reconciliation state | 28 | `HIGH_UNCERTAINTY` | 14 | 42 | Covers prepared, committed, and reconciliation-required states without an accepted storage design. |
| `E-0211-003` | OUT-003 exactly-once terminalization implementation/evidence | 32 | `HIGH_UNCERTAINTY` | 16 | 48 | Implements and verifies exactly-once terminalization for active turns on retirement or crash. |
| `E-0211-004` | OUT-004 conditional `thread/resume` and fresh-thread fallback | 28 | `HIGH_UNCERTAINTY` | 14 | 42 | Covers canonical-root, account-identity, policy-digest, and canonical-cwd continuity conditions and the fresh-thread alternative. |
| `E-0211-005` | OUT-005 crash-retirement and replay tests | 32 | `HIGH_UNCERTAINTY` | 16 | 48 | Exercises crash and restart behavior while proving no automatic replay or in-flight re-attach claim. |
| **Total** |  | **136** |  | **72** | **200** | Sum of line items. |

## Assumptions

- The estimate preserves the SOW's explicit lack of a declared upstream
  dependency and does not manufacture one from continuity semantics.
- Journal storage, process implementation, and test tooling remain unspecified;
  uncertainty captures those gaps without selecting them.

## Exclusions

All ten exact bindings listed in `ESTIMATE_METHOD.md` §Global exclusions are
excluded: `source_identity`, `release_identity`, both client-evidence slots,
Root semantic/regression evidence, census notice, Tier-0 relationship,
implementation act, cutover act, and release act. `TM-ROOT-106`,
`TM-ROOT-122`, C1, and all App-owned obligations are also excluded.

No in-flight re-attach, automatic replay, activation, release, hold satisfaction,
or work outside OUT-001..OUT-005 is priced.

## Dependency-shaped sequencing risk

Phase 3 records no Root upstream edge and one gating evidence-fan-in edge to
DEL-02-06. The carrier's internal continuity conditions do not establish an
inter-deliverable order. Its accepted evidence must later reach DEL-02-06;
no dates, precedence decision, or schedule are computed.
