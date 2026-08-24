# Estimate — DEL-02-07 Process Supervisor and Purpose-Limited Control

- **Status:** `DRAFT_AWAITING_OWNER_ACCEPTANCE`
- **Boundary:** derivative, non-authorizing estimate; hours are not a commitment or schedule
- **Total:** **180 base hours; 94–266 hours**

## Accepted inputs

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`, row `DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/ScopeOfWork.md`, Ontology `OUT-001`..`OUT-005`, Praxeology `VER-001`..`VER-004`, and Output and Evaluation Matrix
- same folder `_CONTEXT.md`, Description, Anticipated Artifacts, and Context Boundary
- same folder `_DEPENDENCIES.md`, Extraction State and the downstream `EVIDENCE_FAN_IN` edge to DEL-02-06

## Output-level work breakdown

| Element | Accepted output | Base h | Class | Low h | High h | Grounded rationale |
|---|---|---:|---|---:|---:|---|
| `E-0207-001` | OUT-001 supervisor-port contract and contract trace | 16 | `MEDIUM_UNCERTAINTY` | 12 | 20 | One named port contract plus trace to the accepted supervisor boundary; exact interface detail is not specified. |
| `E-0207-002` | OUT-002 purpose-limited private Unix-socket protocol and protocol evidence | 28 | `HIGH_UNCERTAINTY` | 14 | 42 | Covers ownership modes, request-token validation, owner/generation binding, and stale-recovery invalidation across one private protocol. |
| `E-0207-003` | OUT-003 worker-control implementation and evidence | 64 | `HIGH_UNCERTAINTY` | 32 | 96 | Covers acquisition, inventory, reconnect, generation fencing, stale recovery, and their accepted evidence without a prescribed implementation design. |
| `E-0207-004` | OUT-004 daemon-plus-supervisor launch integration and boundary evidence | 32 | `HIGH_UNCERTAINTY` | 16 | 48 | Integrates the two-job topology and verifies sole-broker, no-TCP, and caller-exclusion boundaries. |
| `E-0207-005` | OUT-005 role-parity and hard-containment evidence | 40 | `HIGH_UNCERTAINTY` | 20 | 60 | Exercises parity, labelled fallback, calibrated non-delegation claims, and unchanged hard containment. |
| **Total** |  | **180** |  | **94** | **266** | Sum of line items. |

## Assumptions

- Each line includes its output's bounded production and deliverable-local
  verification only; DEL-02-06 integration/fan-in is not duplicated.
- The accepted lack of a Root upstream edge is preserved; no ordering among
  DEL-02-08..12 is assumed.
- Unspecified interface and implementation choices remain open and are
  reflected through uncertainty rather than invented scope.

## Exclusions

All ten exact bindings listed in `ESTIMATE_METHOD.md` §Global exclusions are
excluded: `source_identity`, `release_identity`, App client evidence, Root CLI
client evidence, Root semantic/regression evidence, census notice, Tier-0
relationship, implementation act, cutover act, and release act. Also excluded
are `TM-ROOT-106`, `TM-ROOT-122`, C1, and all App-owned obligations.

DEL-02-07-specific exclusions are any TCP listener, renderer/CLI-callable
control surface, second runtime broker, activation, and work outside the
accepted five outputs. The accepted anticipated write locus is not authority.

## Dependency-shaped sequencing risk

Phase 3 records no upstream Root edge and one gating evidence-fan-in edge to
DEL-02-06. The estimate can therefore stand independently, but eventual
integration cannot close until DEL-02-07 evidence is accepted into DEL-02-06.
This is a sequencing risk statement only: no date, precedence decision, or
schedule is computed.
