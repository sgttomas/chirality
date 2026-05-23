# Datasheet: DEL-01-04 Scope Boundary and Retired Scope Register

## Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-01-04 |
| DeliverableName | Scope Boundary and Retired Scope Register |
| PackageID | PKG-01 |
| PackageName | Product Governance and Reliance Boundaries |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | DOC_UPDATE |
| ResponsibleParty | TBD |
| ContextEnvelope | S |
| Primary Objective | OBJ-009: preserve professional boundary, product identity, and reliance-boundary ownership in docs, UI, runtime, and release behavior. |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable purpose | Keep remote MCP, plugins, shipped bypass, non-macOS packaging, domain operations, and retired PKG-08 items outside active scope unless amended. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-01 / DEL-01-04 |
| Anticipated artifacts | Out-of-scope register; retired-scope notes; amendment triggers. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-01 / DEL-01-04 |
| Covered scope items | SOW-065, SOW-076, SOW-077, SOW-078. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §Scope Item Ledger |
| Remote MCP/plugins status | Out of current scope; remote MCP, plugins, remote execution, marketplace extension, and shell-network expansion require governed future scope. | `docs/PRD.md` §3.2, §6.4; `docs/CONTRACT.md` §1.9 K-NET-1 |
| Shipped bypass/settings status | Shipped builds must not load ambient Claude settings or use ordinary `bypassPermissions`; developer-only bypass remains guarded. | `docs/PRD.md` §3.2; `docs/CONTRACT.md` §1.4 K-SDK-1 and §1.6 K-PERM-6 |
| Retired PKG-08 status | Retired execution-scope items remain out of scope unless reactivated by governed amendment; runtime event logging does not reactivate retired hardening scope. | `docs/PRD.md` §3.2 and §12.1; `docs/PLAN.md` §9 / PKG-08 status; `docs/CONTRACT.md` §1.9 K-RETIRED-1 |
| Non-macOS packaging status | Windows/Linux packaging is out of scope until amended; current release target is macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG. | `docs/PRD.md` §6.4; `docs/CONTRACT.md` §1.9 K-RELEASE-1 |
| Domain operation status | Domain-engine integration and operation execution are future-amendment scope; agents must not write protected domain-engine model truth and applying domain operations requires explicit human acceptance. | `docs/PRD.md` §6.4 and R7; `docs/CONTRACT.md` §1.10 |
| Amendment authority | Changes that alter scope, release target, data contracts, professional-boundary posture, runtime engine semantics, permission behavior, transcript canonicality, or retired/active execution scope require governed product change. | `docs/DIRECTIVE.md` §7 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Source hash warning | `docs/PRD.md` has a PRD hash mismatch in `_REFERENCES.md`; this run treats it as a source warning, not a blocker, per dispatch. | `_REFERENCES.md` REF-006; TASK dispatch override |
| Dependency extraction | Deferred. `Dependencies.csv` is not created by this deliverable run. | `_DEPENDENCIES.md`; TASK dispatch |
| Human authority | Agents and tools may draft and organize records, but humans approve, issue, sign, seal, and accept reliance. | `docs/TYPES.md` §3.3; `docs/DIRECTIVE.md` §3 |
| Unknown values | Unknown values remain `TBD`; agents and tools must not invent scope items, dependency targets, parameters, or professional conclusions. | `docs/CONTRACT.md` §1.7 K-INVENT-1 |
| Scope conflicts | Source conflicts must be surfaced rather than silently resolved. | `docs/CONTRACT.md` §1.7 K-CONFLICT-1 |

## Construction

The register should be constructed as a documentary control surface with at least these record families:

| Record Family | Minimum Fields | Status |
|---|---|---|
| Out-of-scope items | Scope item ID, boundary statement, source reference, amendment trigger, current status, human ruling. | ASSUMPTION: structure inferred from anticipated artifacts and source-control needs. |
| Retired-scope notes | Retired item, prohibited reactivation path, allowed adjacent infrastructure, source reference, human ruling. | ASSUMPTION: structure inferred from SOW-077 and PKG-08 notes. |
| Amendment triggers | Trigger condition, affected boundary, required governed change surface, review evidence, approval status. | ASSUMPTION: structure inferred from `docs/DIRECTIVE.md` §7. |

### Boundary Register Rows

For this four-document kit, the concrete register-row artifact is this `Datasheet.md` section. Later publication may move these rows into a dedicated register file, but until amended this table is the inspection surface for boundary-row verification.

| RowID | Boundary Item | Boundary Statement | Source Reference | Amendment Trigger | Current Status | Human Ruling |
|---|---|---|---|---|---|---|
| DEL-01-04-BR-001 | SOW-065 remote MCP/plugins/tool expansion | Remote MCP servers, plugins, remote execution, plugin marketplace, and broad tool search remain outside current scope until local SDK governance, permissions, hooks, event logging, and result storage are reliable. | `docs/PRD.md` §3.2 and §6.4; `docs/CONTRACT.md` §1.9 K-NET-1; `docs/PLAN.md` §11 | Governed amendment that admits remote or expanded tool scope and updates governance, tests, release checks, and implementation artifacts. | OUT | TBD |
| DEL-01-04-BR-002 | SOW-076 ambient settings and shipped bypass | Shipped builds must not load ambient Claude settings and must not use `bypassPermissions` in shipped or ordinary operator workflows; developer-local bypass remains guarded. | `docs/PRD.md` §3.2 and FR-117; `docs/CONTRACT.md` §1.4 K-SDK-1 and §1.6 K-PERM-6 | Governed amendment plus SDK option, hook, environment guard, and release-check updates. | OUT | TBD |
| DEL-01-04-BR-003 | SOW-077 retired PKG-08 scope | Retired PKG-08 execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record, and staleness propagation tooling remain retired; harness runtime event logging does not reactivate them. | `docs/PRD.md` §3.2 and KG-012; `docs/PLAN.md` §9; `docs/CONTRACT.md` §1.9 K-RETIRED-1 | Governed amendment that explicitly reactivates retired execution scope and updates active decomposition/package commitments. | OUT | TBD |
| DEL-01-04-BR-004 | SOW-078 Windows/Linux packaging | Windows/Linux release packaging remains outside current release scope; current release target is macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG. | `docs/PRD.md` §6.4 and KG-014; `docs/CONTRACT.md` §1.9 K-RELEASE-1 | Governed release-scope amendment with packaging, validation, and instruction-root integrity updates. | OUT | TBD |
| DEL-01-04-BR-005 | Domain operation execution and protected domain paths | Domain-engine integration as a shipping feature, direct protected-domain-path writes, and domain operation execution remain future-amendment scope; agents may write proposals and summaries, while application requires explicit human acceptance. | `docs/PRD.md` §6.4 and FR-106 through FR-115; `docs/CONTRACT.md` §1.10; `docs/PLAN.md` R7 | Governed domain-profile amendment with protected-path, proposal, deterministic-adapter, and human-gate controls. | OUT | TBD |

## References

| RefID | Source | Use |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Product intent, professional authority, out-of-scope and change discipline. |
| REF-002 | `docs/CONTRACT.md` | Binding invariants for settings, permissions, retired scope, domain boundaries, and unknown/conflict handling. |
| REF-003 | `docs/SPEC.md` | Runtime mechanics and boundary surfaces; used only where source slices were relevant. |
| REF-004 | `docs/TYPES.md` | Authority model and vocabulary. |
| REF-005 | `docs/PLAN.md` | Roadmap sequencing, PKG-08 retirement notes, and future-amendment exclusions. |
| REF-006 | `docs/PRD.md` | Current vNext product requirements and explicit non-goals; hash mismatch warning applies. |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method reference; no deliverable-specific requirements extracted. |
