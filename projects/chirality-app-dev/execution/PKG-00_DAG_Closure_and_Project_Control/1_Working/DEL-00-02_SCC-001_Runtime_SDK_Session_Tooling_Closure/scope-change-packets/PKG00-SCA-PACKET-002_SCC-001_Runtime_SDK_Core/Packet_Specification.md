# Packet Specification: PKG00-SCA-PACKET-002 SCC-001 Runtime SDK Core

## Scope

This packet specifies conservative candidate amendments for runtime engine, SDK adapter, provider/settings, mapper/options, and turn lifecycle integration concerns in the SCC-001 runtime SDK core subset.

## Proposed Amendment Requirements

| ID | Requirement | Evidence |
|---|---|---|
| REQ-PKT-002-001 | SCOPE_CHANGE intake must distinguish hard sequencing prerequisites from interface evidence in runtime contract, SDK probe, mapper, options, and lifecycle rows. | E-001; E-002; E-004 |
| REQ-PKT-002-002 | Any amendment must preserve `AgentEnginePort` / `RuntimeEngineContract` as the product-owned boundary while allowing SDK probe evidence to inform adapter fixtures. | E-003; E-005; E-008 |
| REQ-PKT-002-003 | Any amendment must preserve stable `/api/harness/*` and SSE/UIEvent compatibility while SDK message mapping remains adapter-owned. | E-003; E-009; E-010 |
| REQ-PKT-002-004 | Any amendment must clarify the options/persona boundary so `SdkOptionsBuilder` owns settings isolation while `PersonaComposer` owns prompt material. | E-003; E-011 |
| REQ-PKT-002-005 | Provider key, base URL, and provider error handoff must remain redacted and provider-neutral where crossing mapper/runtime surfaces. | E-003; E-012 |

## Action Candidates

The authoritative action table is `Proposed_SCA_Actions.csv`. Candidate actions are intentionally conservative. Rows marked `TBD` require human or SCOPE_CHANGE gate rulings before implementation.

## Acceptance Criteria

- The SCOPE_CHANGE intake names the accepted DepClosure snapshot and decomposition authority.
- Proposed row-level changes cite owning product registers.
- Interface evidence is not converted into prerequisite sequencing without source-grounded ruling.
- Provider/settings and mapper/options concerns remain scoped to PKG-04 boundaries unless SCOPE_CHANGE approves a structural amendment.
- Any accepted amendment is followed by a DepClosure rerun before closure reporting.

## Invariant Checks

- This packet remains derivative and non-authoritative.
- Product deliverables and `Dependencies.csv` files are not modified by this packet.
- `_ScopeChange`, `_Reconciliation`, and decomposition files are not modified by this packet.
- Unknown row disposition remains `TBD`.
