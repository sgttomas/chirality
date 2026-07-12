# Guidance: DEL-01-04 Scope Boundary and Retired Scope Register

## Purpose

This deliverable is a scope guard. It keeps known out-of-scope and retired items visible so they are not accidentally reintroduced through implementation enthusiasm, runtime event logging, release packaging, plugin/tool expansion, SDK settings behavior, or future domain-engine work.

The controlling objective is OBJ-009: preserve professional boundary, product identity, and reliance-boundary ownership in docs, UI, runtime, and release behavior. Source: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §Objectives and §PKG-01 / DEL-01-04.

## Principles

1. Treat boundary rows as negative scope controls, not implementation backlog.
   Source: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` marks SOW-065, SOW-076, SOW-077, and SOW-078 as `OUT`.

2. A future-facing statement is not current shipping scope.
   Domain-engine profiles, plugin-like extension points, and remote MCP may be described as future-compatible concepts, but implementation requires amendment and mature local governance first. Sources: `docs/PRD.md` §6.4, §8.14 FR-105, R7; `docs/PLAN.md` R7.

3. Runtime event logging is allowed runtime infrastructure, but it does not revive retired pipeline hardening work.
   Source: `docs/PLAN.md` §9; `docs/PRD.md` §3.2.

4. Shipped safety posture cannot depend on SDK defaults, ambient user settings, ordinary bypass behavior, or prompt text alone.
   Sources: `docs/CONTRACT.md` §1.4 K-SDK-1, §1.6 K-PERM-2/K-PERM-3/K-PERM-6; `docs/PRD.md` §3.2.

5. Human authority remains non-delegable.
   This register can guide amendment and review, but it cannot approve professional work or create reliance by itself. Sources: `docs/DIRECTIVE.md` §3; `docs/TYPES.md` §3.3; `docs/CONTRACT.md` §1.2.

## Considerations

| Topic | Guidance | Source |
|---|---|---|
| Boundary-row placement | Inspect the concrete boundary rows in `Datasheet.md` under `Boundary Register Rows`; that section is the current register-row artifact unless a governed publication step moves the rows elsewhere. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-01 / DEL-01-04; `docs/DIRECTIVE.md` §7 |
| Remote MCP and plugins | Keep as out of current scope until local/in-process SDK integration, permission policy, hooks, event logging, and result storage are stable and a governed amendment permits expansion. | `docs/PRD.md` §3.2, §6.4; `docs/PLAN.md` §11 |
| Broad tool search | Treat as deferred; if later introduced, it must reveal only currently allowed tools and never denied tools. | `docs/PRD.md` §8.14 FR-103 |
| Shipped settings | Do not allow shipped builds to load ambient Claude settings. A change attempt should trigger governance review before implementation. | `docs/PRD.md` §3.2; `docs/CONTRACT.md` §1.4 K-SDK-1 |
| Bypass permissions | Separate developer-local guarded bypass from shipped or ordinary operator workflows. Do not blur this distinction in copy, config, or tests. | `docs/PRD.md` §3.2; `docs/CONTRACT.md` §1.6 K-PERM-6 |
| Retired PKG-08 items | Keep retired execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record, and staleness propagation tooling out of current commitments. | `docs/PLAN.md` §9; `docs/PRD.md` KG-012 |
| Release targets | Treat macOS 15+ Apple Silicon DMG as the current release target; Windows/Linux packaging needs amendment. | `docs/CONTRACT.md` §1.9 K-RELEASE-1; `docs/PRD.md` §6.4 |
| Domain operations | Keep domain operation execution behind future profile, proposal, deterministic checks, and human acceptance. | `docs/CONTRACT.md` §1.10; `docs/PRD.md` R7 |
| Boundary review checklist | Use `docs/BOUNDARY_REVIEW_CHECKLISTS.md` for repeatable scope-boundary and professional-boundary review evidence. Checklist completion is not a human ruling, dependency closure, lifecycle issuance, or release/professional approval. | ADQ-03 |

## Trade-offs

| Trade-off | Preferred Position | Rationale |
|---|---|---|
| Future compatibility vs current scope discipline | Preserve future vocabulary, but mark implementation as future-amendment scope. | Prevents premature implementation while keeping architectural runway. |
| Developer convenience vs shipped safety | Allow only guarded developer-local bypass; forbid shipped/ordinary bypass behavior. | Maintains product-owned permission boundaries and release posture. |
| Event logging vs retired pipeline scope | Permit runtime audit event logging; keep retired pipeline run records and hardening tools retired. | Preserves auditability without reactivating retired work. |
| Cross-platform ambition vs release certainty | Keep Windows/Linux packaging out of current scope. | Current release invariant names macOS 15+ Apple Silicon DMG unless amended. |

## Examples

| Scenario | Register Disposition |
|---|---|
| A developer proposes adding a plugin marketplace before local permission hooks are stable. | Mark as blocked by SOW-065; requires governed amendment after local governance maturity. |
| A packaged build reads `.claude/settings.local.json` from the working root. | Mark as forbidden by SOW-076 / K-SDK-1; requires correction, not amendment-by-default. |
| Runtime events are added under `.chirality/sessions/<id>/events.jsonl`. | Allowed as runtime audit infrastructure if aligned with runtime contract; do not relabel as unified pipeline run records. |
| A release issue asks for Windows packaging in the current slice. | Mark as out of scope under SOW-078; requires release-scope amendment. |
| A domain adapter attempts to write directly to protected domain-engine model paths. | Mark as out of current scope and prohibited by domain boundary policy; future work must use proposal records and human acceptance. |

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CF-001 | Dispatch path names `PKG-01_Governance_and_Product_Boundaries`, but the only matching deliverable folder on disk is under `PKG-01_Product_Governance_and_Reliance_Boundaries`. | TASK dispatch | Filesystem path and `_CONTEXT.md` PackageName | Run record, final report | Use the located deliverable folder for this run and surface the stale path as a warning. | TBD |

Closed historical conflict: `CF-002` is superseded by the current D-APP-38 corpus snapshot; current `_REFERENCES.md`
records REF-006 `docs/PRD.md` as `MATCH`.

## Normalized Checklist Artifact

ADQ-03 materialized `docs/BOUNDARY_REVIEW_CHECKLISTS.md` as the shared review checklist package. For
DEL-01-04, it supplies the scope-boundary checklist, amendment-trigger prompts, and finding template.
The boundary-row human ruling fields remain `TBD` until an accountable human records rulings or
explicit deferrals.
