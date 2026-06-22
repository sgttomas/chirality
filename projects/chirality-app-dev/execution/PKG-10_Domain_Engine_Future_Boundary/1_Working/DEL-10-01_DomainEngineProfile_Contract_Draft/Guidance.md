# Guidance: DEL-10-01 DomainEngineProfile Contract Draft

## Purpose

This guidance explains how to read and maintain the `DomainEngineProfile` contract draft as a future-boundary artifact. The draft preserves compatibility with future domain-engine integrations without activating domain execution in the current app-dev slice.

Primary canon: `_REFERENCES.md` REF-008, `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`. Under D-T0-01, the framework-root persona is canonical; app-dev `docs/TYPES.md` Section 11 conforms to it and must not weaken framework invariants.

## Principles

| Principle | Guidance | Source |
|---|---|---|
| Canon first | Maintain the profile shape from REF-008: identity fields, `ProfileStatus`, `IntegrationLevel`, path/artifact roles, deterministic tools, `operation_proposal_contract`, and professional boundary. | REF-008; `docs/TYPES.md` Section 11.1 |
| Generic first | Keep the profile contract generic before any engine-specific integration. OpenPipeStress may be a future concrete profile, but it must not shape Chirality core runtime assumptions. | `docs/PRD.md` Section 8.17 FR-107 |
| Future gated | Treat endpoints, tools, validators, adapters, operation stores, and path hooks as future platform interfaces until a governed amendment accepts them. | `docs/SPEC.md` Section 18; `docs/PLAN.md` R7 |
| Truth separation | Domain engines own authoritative domain truth; Chirality governs interaction, profile records, proposals, review aids, and human gates. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-1 |
| Path quarantine | Protected paths and agent-writable paths must remain distinct. Agents may draft proposals and summaries only under approved writable proposal/review paths. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2; REF-008 |
| Human acceptance | Accepted/applied proposal states require explicit human approval bound to K-AUTH-2 evidence and a domain-engine-controlled apply or external terminal acceptance record. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3; REF-008 |
| Professional boundary | Boundary notices must prevent solver outputs from being presented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4; REF-008 |

## Considerations

- Use `docs/TYPES.md` Section 11.1 as the app-dev vocabulary target, but resolve conflicts against REF-008.
- The older compact draft fields `DomainEngineOperationDescriptor` and `manifestRules` are superseded by canonical `deterministic_tools`, path/artifact role sets, and `operation_proposal_contract`; they are no longer human-ruling blockers for DEL-10-01.
- Keep `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema references explicit. A concrete schema may remain `TBD`, but the schema hook itself is canonical.
- Keep OpenPipeStress references fixture-level only. A concrete OpenPipeStress profile remains future/gated and must not become an app-dev runtime assumption in this tranche.
- Any future validator should be deterministic and reject invalid or incomplete profiles before runtime exposure.
- Preserve `_STATUS.md` as-is. This conformance tranche does not authorize `CHECKING -> ISSUED`, release readiness, or R7 implementation.

## True Future TBDs

| Topic | Conservative position | Risk if loosened |
|---|---|---|
| Concrete profile instances | Leave engine instances, including OpenPipeStress, as future amendment scope. | An illustrative profile could be mistaken for accepted integration. |
| Concrete schema refs | Record `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema as explicit refs or `TBD`. | Prompt-inferred result schemas could become false contract surface. |
| Adapter/tool implementation | Defer deterministic adapters, stores, MCP tools, endpoints, and path hooks. | Crosses F3 and activates domain runtime without tier-0 gate. |
| Boundary notice copy | Require structured boundary fields now; review concrete text per profile instance later. | Generic copy may imply professional reliance in a domain-specific context. |

## Example Generic Skeleton

```yaml
domain_profile:
  schema_version: "1.0"
  id: "TBD"
  name: "TBD"
  engine_type: "TBD"
  profile_version: "0.1"
  profile_status: "DRAFT"
  integration_level: "MANUAL_BRIDGE"
  domain_root_patterns: []
  authoritative_artifacts: []
  chirality_readable_artifacts: []
  protected_write_paths: []
  agent_writable_paths: []
  deterministic_tools:
    - id: "TBD"
      mode: "read_only"
      requires_human_confirmation: false
      validate_result_schema: "TBD"
      apply_result_schema: "TBD"
  operation_proposal_contract:
    lifecycle: ["draft", "ready_for_review", "accepted", "rejected", "applied"]
    deterministic_check_result_schema: "TBD"
  professional_boundary:
    agent_must_not_claim:
      - "code compliant for reliance"
      - "professionally approved"
      - "externally validated"
```

This example is illustrative only. It is not an accepted runtime fixture and must not be treated as implementation-ready.

## References

- `_REFERENCES.md` REF-008
- `agents/AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`
- `docs/CONTRACT.md` Section 1.10
- `docs/SPEC.md` Section 18
- `docs/TYPES.md` Section 11
- `docs/PLAN.md` R7
- `docs/PRD.md` Section 8.17, Section 10.10, KG-016 through KG-020
