# Estimate — DEL-02-09 Hosted Account and Consent Boundary

- **Status:** `DRAFT_AWAITING_OWNER_ACCEPTANCE`
- **Boundary:** derivative, non-authorizing estimate; hours are not a commitment or schedule
- **Total:** **148 base hours; 82–214 hours**

## Accepted inputs

- `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`, row `DEL-02-09_Hosted_Account_and_Consent_Boundary`
- `execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/ScopeOfWork.md`, Ontology and Output and Evaluation Matrix `OUT-001`..`OUT-006`
- same folder `_CONTEXT.md`, Description, Anticipated Artifacts, and Context Boundary
- same folder `_DEPENDENCIES.md`, Extraction State and downstream `EVIDENCE_FAN_IN` edge to DEL-02-06

## Output-level work breakdown

| Element | Accepted output | Base h | Class | Low h | High h | Grounded rationale |
|---|---|---:|---|---:|---:|---|
| `E-0209-001` | OUT-001 `HostedEngineConsentPort` contract | 16 | `MEDIUM_UNCERTAINTY` | 12 | 20 | One named port contract bounded to the accepted hosted account/consent responsibility. |
| `E-0209-002` | OUT-002 root-private `CODEX_HOME` and account-continuity controls | 28 | `HIGH_UNCERTAINTY` | 14 | 42 | Covers root-private home, ambient-home exclusion, account/epoch and policy continuity, and cross-boundary refusal evidence. |
| `E-0209-003` | OUT-003 `K-ROLE-2` digest schema | 16 | `MEDIUM_UNCERTAINTY` | 12 | 20 | One role-posture digest schema with accepted continuity and evidence-calibration content. |
| `E-0209-004` | OUT-004 role-parity and labelled-fallback controls | 24 | `HIGH_UNCERTAINTY` | 12 | 36 | Covers always-offered Agent 0/1/2 entry and the instruction-asserted labelled fallback without overclaim. |
| `E-0209-005` | OUT-005 per-root three-posture consent-state model | 28 | `HIGH_UNCERTAINTY` | 14 | 42 | Covers default-off, ask-per-destination, labelled-on, visible host/protocol, grouping caveat, and explicit-user session consent. |
| `E-0209-006` | OUT-006 Root-owned isolation, consent, and continuity tests | 36 | `HIGH_UNCERTAINTY` | 18 | 54 | Verifies the accepted Root boundary; App-owned consent-mirror or client evidence is excluded. |
| **Total** |  | **148** |  | **82** | **214** | Sum of line items. |

## Assumptions

- The lines price only Root-owned production and deliverable-local verification.
- No ordering is inferred from shared account, prompt, policy, or continuity
  concepts, consistent with the Phase-3 omission record.
- Acceptance criteria not specified by the SOW remain unspecified; the hours
  do not invent them.

## Exclusions

All ten exact bindings listed in `ESTIMATE_METHOD.md` §Global exclusions are
excluded: `source_identity`, `release_identity`, App and Root CLI client
evidence, Root semantic/regression evidence, census notice, Tier-0
relationship, implementation act, cutover act, and release act. Also excluded
are `TM-ROOT-106`, `TM-ROOT-122`, C1, and all App-owned consent-mirror,
implementation, conformance, and release obligations.

No ambient `~/.codex` use, consent crossing root/account/policy-digest drift,
containment weakening, activation, or foreign-loop work is priced.

## Dependency-shaped sequencing risk

Phase 3 records no Root upstream edge and one gating evidence-fan-in edge to
DEL-02-06. Root-owned evidence can be estimated independently, but the wider
release fan-in must keep absent App-owned evidence unresolved. No dates,
precedence decision, or schedule are computed.
