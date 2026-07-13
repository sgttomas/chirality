# Datasheet: DEL-07-03 Deliverable Metadata and Document Kit Contracts

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-07-03 | `_CONTEXT.md` / Identity |
| Deliverable name | Deliverable Metadata and Document Kit Contracts | `_CONTEXT.md` / Identity |
| Package | PKG-07 Filesystem Execution, Lifecycle, and Dependencies | `_CONTEXT.md` / Identity; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` / PKG-07 |
| Decomposition variant | SOFTWARE_DECOMP v3.2 | `_CONTEXT.md` / Identity |
| Responsible party | TBD | `_CONTEXT.md` / Identity |
| Type | BACKEND_FEATURE_SLICE | `_CONTEXT.md` / Identity |
| Context envelope | M | `_CONTEXT.md` / Identity |
| Scope item | SOW-026 | `_CONTEXT.md` / Traceability; decomposition / SOW mapping |
| Objective | OBJ-006 | `_CONTEXT.md` / Traceability |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary subject | Scan and validate deliverable metadata files, canonical memory, semantic placeholders, and document kit buckets. | `_CONTEXT.md` / Deliverable Scope; decomposition / DEL-07-03 row |
| Anticipated artifacts | Metadata scanners; document kit detection; `_MEMORY.md` rejection tests | `_CONTEXT.md` / Anticipated Artifacts; decomposition / DEL-07-03 row |
| Required metadata files | `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md` | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 |
| Minimum PREPARATION fileset | Required metadata files plus `_SEMANTIC.md` placeholder | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 |
| Document kit files | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` | `docs/PRD.md` / Section 10.8; `docs/SPEC.md` / Section 3.1 |
| Canonical memory file | `MEMORY.md` | `docs/SPEC.md` / Section 5.4 |
| Disabled memory file | `_MEMORY.md` MUST NOT be created in this project profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 |
| Optional deliverable files | `Dependencies.csv`, `MEMORY.md`, `_SEMANTIC_LENSING.md`, `HASH_VERIFICATION_BYPASS.jsonl` | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 |
| Lifecycle states | `OPEN`, `INITIALIZED`, `SEMANTIC_READY`, `IN_PROGRESS`, `CHECKING`, `ISSUED` | `docs/SPEC.md` / Section 4.2; `docs/TYPES.md` / lifecycle state table |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Working-root authority | Project truth is written under the working root; instruction-root writes are outside ordinary execution. | `docs/DIRECTIVE.md` / Section 2.7; `docs/CONTRACT.md` / K-ROOT-1 through K-ROOT-3 |
| Evidence posture | Important claims and dependency evidence use source paths; assumptions, proposals, unknowns, and conflicts remain visible. | `docs/DIRECTIVE.md` / Section 2.5; `docs/CONTRACT.md` / K-CONFLICT-1 |
| Lifecycle transition rule | `_STATUS.md` is canonical; transitions are forward-only unless a human explicitly amends the record. | `docs/SPEC.md` / Section 4.3; `docs/PRD.md` / FR-052 and FR-053 |
| Human gate rule | `CHECKING` and `ISSUED` transitions require approval SHA evidence and cannot be authored by agents. | `docs/SPEC.md` / Section 4.3; `docs/CONTRACT.md` / K-AUTH-1, K-GATE-1 |
| Reference hash posture | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` / REF-006 — reconciled under D-APP-38 |

## Construction

| Component | Expected construction | Source |
|---|---|---|
| Metadata scanner | Detect deliverable folders by valid `DEL-XX-YY_Label` or `DEL-XXX-YY_Label` prefix and presence of `_STATUS.md`; validate required metadata files against SPEC/PRD expectations. | `docs/PRD.md` / FR-047, FR-048; `docs/SPEC.md` / Section 3.1 |
| Document kit detector | Treat `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` as first-class knowledge buckets. | `docs/PRD.md` / FR-049; `docs/SPEC.md` / Section 3.1 |
| Memory contract validator | Accept `MEMORY.md` as canonical when present and reject `_MEMORY.md` in this project profile. | `docs/SPEC.md` / Section 3.1 and Section 5.4; `docs/PRD.md` / Section 10.8 |
| Semantic placeholder validator | Recognize `_SEMANTIC.md` as part of the PREPARATION baseline and `_SEMANTIC_LENSING.md` as optional semantic analysis narrative. | `docs/SPEC.md` / Section 3.1; `docs/PRD.md` / Section 10.8 |
| Test coverage | Metadata scanner, document-kit detection, and `_MEMORY.md` rejection coverage lives in `frontend/src/__tests__/lib/workspace-deliverable-contract-scanner.test.ts`; project-deliverables route integration is covered by `frontend/src/__tests__/api/project/deliverables-route.test.ts`. | `_CONTEXT.md` / Anticipated Artifacts; decomposition / DEL-07-03 row |

## References

| RefID | Source | Use | Status |
|---|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Evidence, hidden-memory, root-separation posture | MATCH |
| REF-002 | `docs/CONTRACT.md` | Governance invariants for root, write scope, human gates, conflict surfacing | MATCH |
| REF-003 | `docs/SPEC.md` | Deliverable folder layout, lifecycle, context/dependency/reference/memory contracts | MATCH |
| REF-004 | `docs/TYPES.md` | Deliverable and lifecycle vocabulary | MATCH |
| REF-005 | `docs/PLAN.md` | Local source policy and PKG-07 roadmap context | MATCH |
| REF-006 | `docs/PRD.md` | Filesystem requirements and deliverable folder layout | MATCH status in `_REFERENCES.md` — reconciled under D-APP-38 |
| REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context | MATCH; no deliverable-specific requirements used |
