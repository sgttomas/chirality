# Datasheet: DEL-10-01 DomainEngineProfile Contract Draft

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-10-01 |
| DeliverableName | DomainEngineProfile Contract Draft |
| PackageID | PKG-10 |
| PackageName | Domain Engine Future Boundary |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | API_CONTRACT |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| Current posture | Future-boundary contract, not current implementation |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Contract subject | Future `DomainEngineProfile` profile contract conforming to framework-root canon at `77a327727`. | `_CONTEXT.md`; `_REFERENCES.md` REF-008; `docs/TYPES.md` §11.1 |
| Canonical identity fields | `schema_version`, `id`, `name`, `engine_type`, `profile_version`. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/TYPES.md` §11.1 |
| Profile lifecycle fields | `profile_status` using `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`; `integration_level` using `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE`. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/TYPES.md` §11.1 |
| Path and artifact role fields | `domain_root_patterns`, `authoritative_artifacts`, `chirality_readable_artifacts`, `protected_write_paths`, `agent_writable_paths`. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/CONTRACT.md` §1.10 |
| Tool contract fields | `deterministic_tools[].id`, `mode`, `requires_human_confirmation`, `validate_result_schema`, and `apply_result_schema`. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/TYPES.md` §11.1 |
| Proposal contract field | `operation_proposal_contract` with lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/TYPES.md` §11.1 |
| Professional boundary field | Structured `professional_boundary.agent_must_not_claim` list. | `agents/AGENT_DOMAIN_ENGINE.md` REF-008; `docs/CONTRACT.md` §1.10 K-DOMAIN-4 |
| True future TBDs | Concrete profile instances, concrete schema refs, adapter implementations, tool stores, operation stores, and apply tooling remain TBD until governed amendment. | `docs/PLAN.md` §R7; `docs/SPEC.md` §18 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Release scope | Domain-engine endpoints, source types, MCP tools, path hooks, and runtime domain execution are provisional future platform interfaces and must not be implemented as current-release scope. | `docs/SPEC.md` §18; D-APP-39 F3 |
| Sequencing | Domain Engine Profiles and operation-proposal workflows are introduced only through a future governed amendment. | `docs/PLAN.md` §R7; `docs/PRD.md` §8.17 |
| Engine-specific integration | A generic `DomainEngineProfile` contract precedes any engine-specific integration. | `docs/PRD.md` §8.17 FR-107 |
| Protected path posture | Protected domain paths are write-quarantined; agents write proposals, summaries, and review aids only under profile-approved `agent_writable_paths`. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; REF-008 |
| Human gate posture | Accepted/applied proposal transitions require human approval bound to git SHA per K-AUTH-2 and domain-engine-controlled apply or external terminal acceptance records. | `docs/CONTRACT.md` §1.10 K-DOMAIN-3; REF-008 |
| Professional boundary | Domain-engine outputs must not be represented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/CONTRACT.md` §1.10 K-DOMAIN-4; REF-008 |

## Construction

### Canonical Profile Shape

```yaml
domain_profile:
  schema_version: "1.0"
  id: "<domain_engine_id>"
  name: "<Domain Engine Name>"
  engine_type: "<domain classification>"
  profile_version: "0.1"
  profile_status: "DRAFT"
  integration_level: "MANUAL_BRIDGE"
  domain_root_patterns:
    - "<path or glob>"
  authoritative_artifacts:
    - "<engine-owned path or glob>"
  chirality_readable_artifacts:
    - "<manifest/summary/report path or glob>"
  protected_write_paths:
    - "<agent-prohibited path or glob>"
  agent_writable_paths:
    - "<proposal/review/checklist path or glob>"
  deterministic_tools:
    - id: "<tool.id>"
      mode: "read_only"
      requires_human_confirmation: false
      validate_result_schema: "<schema ref or TBD>"
      apply_result_schema: "<schema ref or TBD>"
  operation_proposal_contract:
    lifecycle: ["draft", "ready_for_review", "accepted", "rejected", "applied"]
    risk_classes: ["engine_checkable", "engine_silent"]
    deterministic_check_result_schema: "<schema ref or TBD>"
    accepted_or_applied_requires:
      - "human approval bound to git SHA per K-AUTH-2"
      - "domain-engine-controlled apply or external terminal acceptance record"
  professional_boundary:
    agent_must_not_claim:
      - "code compliant for reliance"
      - "professionally approved"
      - "externally validated"
```

Source: `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727` and reflected in `docs/TYPES.md` §11.1.

### Validation Notes

| Check | Draft rule | Source |
|---|---|---|
| Required fields present | A future validator should reject profiles missing identity, status, integration-level, path-role, deterministic-tool, operation-proposal-contract, or professional-boundary fields. | REF-008; `docs/PRD.md` §8.17 FR-108, FR-109 |
| Deterministic validation | Profile validation must be deterministic before runtime exposure. | `docs/PRD.md` §8.17 FR-109; D-T0-06 |
| Result schema refs | Missing `validate_result_schema`, `apply_result_schema`, or deterministic-check result schemas remain explicit `TBD`; chat must not infer them. | REF-008 |
| Future-only exposure | Candidate domain endpoints/tools must remain provisional until governed future amendment. | `docs/SPEC.md` §18 |
| Solver separation | Profile contract must preserve that domain engines own authoritative domain truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1 |

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-10, SOW-066, SOW-067, DEC-006
- `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`
- `docs/CONTRACT.md` §1.10
- `docs/SPEC.md` §18
- `docs/TYPES.md` §11
- `docs/PLAN.md` §R7
- `docs/PRD.md` §8.17, §10.10, §R7, KG-016 through KG-020
