# Datasheet: DEL-10-02 Protected Path and Proposal Path Policy

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-10-02 |
| DeliverableName | Protected Path and Proposal Path Policy |
| PackageID | PKG-10 |
| PackageName | Domain Engine Future Boundary |
| ResponsibleParty | TBD |
| Type | SECURITY_CONTROL |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ContextEnvelope | M |
| Scope Item | SOW-068 |
| Objective | OBJ-010 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Policy posture | Future-boundary / gated scope, not current-release domain operation execution. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-10; `docs/PRD.md` §8.17 |
| Protected path | Authoritative domain-engine artifact path not directly writable by agents. | `docs/TYPES.md` §11.3 |
| Proposal path | Agent-writable folder for proposed changes, summaries, or review aids. | `docs/TYPES.md` §11.3; `docs/PRD.md` §8.17 FR-111 |
| Domain truth owner | Domain engines own authoritative domain truth when adopted by amendment; Chirality governs interaction, proposals, records, and human gates. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1; `docs/PRD.md` §8.17 FR-106 |
| Agent write rule | Agents may write proposals and summaries, not protected domain-engine model truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PLAN.md` R7 |
| Accepted mutation route | Any accepted mutation of domain state must flow through an approved adapter or operation workflow and an explicit human gate. | `docs/PRD.md` §10.10; `docs/SPEC.md` §18 |
| Boundary notice requirement | Domain-engine outputs must not be represented as professional approval, code compliance, external validation, or solver truth owned by Chirality. | `docs/PRD.md` §8.17 FR-115; `docs/CONTRACT.md` §1.10 K-DOMAIN-4 |
| Current concrete path patterns | TBD - profile-specific protected/proposal path patterns are not defined in the accessible sources for DEL-10-02. | `docs/PRD.md` §8.17 FR-108 |
| Profile-specific examples | TBD - example categories are source-supported, but concrete protected/proposal path patterns remain blocked until `DomainEngineProfile` path syntax is accepted. P3 disposition: X-002 incorporated as future slot. | `docs/TYPES.md` §11.1; `docs/PRD.md` §8.17 FR-108 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Activation condition | Governed future amendment after core harness stability. | `docs/PRD.md` §8.17; `docs/PLAN.md` R7 |
| Profile prerequisite | A generic `DomainEngineProfile` contract precedes engine-specific integration. | `docs/PRD.md` §8.17 FR-107 |
| Enforcement prerequisite | Profile validation determines what the harness may read, propose, validate, or request without guessing from prompt text. | `docs/PRD.md` §8.17 FR-108 |
| Direct protected writes | Prohibited for agents and ordinary Chirality tools. | `docs/PRD.md` §8.17 FR-110; `docs/PRD.md` §10.10 |
| Human acceptance | Required before application of a domain operation. | `docs/PRD.md` §8.17 FR-113; `docs/SPEC.md` §18 |
| PRD source status | Source warning: expected SHA256 `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`; observed SHA256 `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. Treated as source warning only by dispatch instruction. | `_REFERENCES.md` REF-006 |
| Responsible ownership | TBD - downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership. P3 disposition: B-001 converted to closure-relevant TBD. | `_CONTEXT.md` §Source Authority |

## Construction

| Element | Construction Rule | Source |
|---|---|---|
| Policy record | Define the separation between protected paths and proposal paths, plus enforcement implications. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-10-02 |
| Hook implication | Protected path writes must be denied or routed away from direct agent mutation; hook implementation detail remains TBD until future amendment. | `docs/PRD.md` §8.17 FR-110; `docs/SPEC.md` §18 |
| Proposal outputs | Agents may create proposals, summaries, and review aids under declared proposal paths. | `docs/PRD.md` §8.17 FR-111; `docs/TYPES.md` §11.3 |
| Adapter route | Accepted protected-state changes require approved adapter or operation workflow plus explicit human gate. | `docs/PRD.md` §10.10 |
| Examples | Only example category supported by accessible sources is OpenPipeStress as a possible fixture profile, not core runtime behavior. Concrete file examples are TBD. | `docs/PRD.md` §8.17 FR-114; `docs/TYPES.md` §11.3 |

## References

- `docs/PRD.md` §8.17, §10.10, source warning per `_REFERENCES.md` REF-006.
- `docs/CONTRACT.md` §1.10.
- `docs/SPEC.md` §18.
- `docs/TYPES.md` §11.
- `docs/PLAN.md` R7.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-10 and SOW-068 rows.
