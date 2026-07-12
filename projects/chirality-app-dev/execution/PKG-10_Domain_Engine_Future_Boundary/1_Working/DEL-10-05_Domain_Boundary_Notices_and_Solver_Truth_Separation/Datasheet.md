# Datasheet: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-10-05 |
| DeliverableName | Domain Boundary Notices and Solver Truth Separation |
| PackageID | PKG-10 |
| PackageName | Domain Engine Future Boundary |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ResponsibleParty | TBD |
| Type | DOC_UPDATE |
| ContextEnvelope | S |
| Current Scope Posture | Future-boundary/gated scope; not current-release domain operation execution |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Covered scope item | SOW-071: domain outputs must not imply professional approval, code compliance, external validation, or solver truth | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW table; `docs/PRD.md` Section 8.17 |
| Supported objectives | OBJ-009 and OBJ-010 | `_CONTEXT.md`; decomposition objective table |
| Primary artifact class | Boundary notice copy, domain review checklist, UI/doc examples | `_CONTEXT.md`; decomposition DEL-10-05 row |
| Domain truth ownership rule | Domain engines own authoritative domain truth when adopted by amendment; Chirality governs interaction, proposals, records, and human gates | `docs/PRD.md` FR-106; `docs/CONTRACT.md` K-DOMAIN-1 |
| Solver-truth separation rule | Domain-engine output must not be represented as professional approval, code compliance, external validation, or solver truth owned by Chirality | `docs/PRD.md` FR-115; `docs/CONTRACT.md` K-DOMAIN-4 |
| Human authority rule | Professional approval, issue, reliance, standard selection, residual-risk acceptance, and conflict adjudication remain human-only | `docs/DIRECTIVE.md` Sections 2.4 and 3.2; `docs/CONTRACT.md` K-AUTH-1 and K-GATE-1 |
| Protected-path implication | Agents may write proposals and summaries, not protected domain-engine model truth | `docs/PRD.md` FR-110 and FR-111; `docs/CONTRACT.md` K-DOMAIN-2 |
| Operation acceptance implication | Domain operations require OperationProposal records and explicit human acceptance before application | `docs/PRD.md` FR-112 and FR-113; `docs/CONTRACT.md` K-DOMAIN-3 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Current implementation partition | D-APP-49 through D-APP-52 rule source types/guards, a closed registry, read tools, and pec-scoped loopback propose/refresh/validate tools live; endpoints, apply, protected-path hooks/writes, and general runtime remain future/gated | `docs/SPEC.md` Section 18; `docs/PRD.md` KG-016; D-APP-49 through D-APP-52 |
| Adoption gate | Future domain-engine work requires governed amendment and stable core harness/runtime boundaries | Decomposition OI-005 and DEC-006; `docs/PRD.md` Section 8.17 |
| Fixture posture | OpenPipeStress may be a first fixture profile if adopted, but it is not Chirality core behavior | `docs/PRD.md` FR-114; `docs/TYPES.md` Section 11.3 |
| PRD reference integrity | WARNING: `_REFERENCES.md` records PRD ExpectedSHA256 `86cb6f...eb34` and ActualSHA256 `fb1c73...6fc8`; per dispatch, this is treated as a source status | `_REFERENCES.md`; user dispatch |

## Construction

The deliverable is constructed as a copy and review package, not an implementation package. It should provide:

- Boundary notice language for UI, documentation, event records, domain profile descriptions, and operation proposal surfaces.
- A domain review checklist that catches claims of Chirality-owned solver truth, professional approval, code compliance, external validation, or direct protected-model mutation.
- Examples that preserve the split between domain-engine truth, deterministic adapter outputs, Chirality records/proposals, and human acceptance.
- Future amendment notes where current source material does not define accepted domain profile details.

## References

| RefID | Source | Use |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Human authority, professional boundaries, project truth hierarchy |
| REF-002 | `docs/CONTRACT.md` | K-AUTH, K-PROF, K-DOMAIN invariants |
| REF-003 | `docs/SPEC.md` | Future domain endpoint and profile interface posture |
| REF-004 | `docs/TYPES.md` | Domain terms: protected path, proposal path, deterministic adapter, boundary notice |
| REF-005 | `docs/PLAN.md` | Future domain-engine direction and OpenPipeStress fixture posture |
| REF-006 | `docs/PRD.md` | Product requirements FR-106 through FR-115 and current-release non-goals |
| REF-007 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | DEL-10-05 scope, SOW-071, OBJ-009, OBJ-010, OI-005, DEC-006 |
