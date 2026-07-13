# Specification: DEL-01-04 Scope Boundary and Retired Scope Register

## Scope

This deliverable defines a documentary scope boundary and retired-scope register for DEL-01-04. It covers SOW-065, SOW-076, SOW-077, and SOW-078, and supports OBJ-009.

In scope:

- Record that remote MCP, plugins, remote execution, broad tool search before mature local governance, and marketplace extension are outside current scope unless amended.
- Record that shipped ambient Claude settings and ordinary shipped `bypassPermissions` operation are outside current scope and forbidden by product invariants.
- Record that retired PKG-08 execution-scope items remain retired unless a governed amendment explicitly reactivates them.
- Record that Windows/Linux release packaging is outside current release scope unless amended.
- Record that domain operation execution and protected-domain-path writes are future-amendment concerns, not current shipping scope.
- Define amendment triggers for attempts to cross these boundaries.

Out of scope:

- Implementing runtime guardrails, release packaging, domain-engine adapters, plugin systems, remote MCP servers, or dependency extraction.
- Creating `Dependencies.csv`.
- Assigning `ResponsibleParty`; it remains `TBD` until a human assigns ownership.
- Treating this document as an approval record or release authorization.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-01 / DEL-01-04; `docs/PRD.md` §3.2 and §6.4.

## Requirements

| ReqID | Requirement | Verification | Source |
|---|---|---|---|
| DEL-01-04-REQ-001 | The register must include SOW-065, SOW-076, SOW-077, and SOW-078 as boundary items. | Inspect register rows against decomposition scope item ledger. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §Scope Item Ledger |
| DEL-01-04-REQ-002 | Remote MCP, plugins, remote execution, marketplace extension, and shell-network expansion must remain outside current scope unless a governed future amendment explicitly permits them. | Confirm each item appears as out of scope with amendment trigger. | `docs/PRD.md` §3.2, §6.4; `docs/CONTRACT.md` §1.9 K-NET-1 |
| DEL-01-04-REQ-003 | Shipped builds must not load ambient `~/.claude/settings.json` or `.claude/settings.local.json`. | Confirm boundary row cites shipped settings prohibition and routes change attempts to governed amendment. | `docs/PRD.md` §3.2; `docs/CONTRACT.md` §1.4 K-SDK-1 |
| DEL-01-04-REQ-004 | Shipped builds and ordinary operator workflows must not use `bypassPermissions`; developer-only bypass remains guarded by explicit local configuration and Chirality deny hooks. | Confirm boundary row distinguishes shipped/ordinary operation from developer-local guarded use. | `docs/PRD.md` §3.2; `docs/CONTRACT.md` §1.6 K-PERM-6 |
| DEL-01-04-REQ-005 | Retired execution-scope items, including retired PKG-08 deliverables, must remain out of scope unless reactivated by governed amendment. | Confirm retired-scope notes identify prohibited reactivation and allowed adjacent runtime event logging. | `docs/PRD.md` §3.2, §12.1; `docs/PLAN.md` §9; `docs/CONTRACT.md` §1.9 K-RETIRED-1 |
| DEL-01-04-REQ-006 | Harness runtime event logging must not be treated as reactivating retired unified pipeline run records or broader PKG-08 hardening scope. | Confirm retired PKG-08 note separates runtime event logging from retired pipeline hardening scope. | `docs/PLAN.md` §9; `docs/PRD.md` §3.2 |
| DEL-01-04-REQ-007 | Windows/Linux release packaging must remain out of current release scope until amended; current release target is macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG. | Confirm packaging boundary row names current release target and amendment condition. | `docs/PRD.md` §6.4; `docs/CONTRACT.md` §1.9 K-RELEASE-1 |
| DEL-01-04-REQ-008 | Domain-engine operation execution must remain future-amendment scope; domain operations require proposal records and explicit human acceptance before application. | Confirm domain boundary row cites future-amendment status and human gate. | `docs/PRD.md` §6.4 and R7; `docs/CONTRACT.md` §1.10 K-DOMAIN-3 |
| DEL-01-04-REQ-009 | The register must not imply automated professional approval, code compliance, external validation, or solver truth owned by Chirality. | Review copy for professional-boundary language. | `docs/DIRECTIVE.md` §3; `docs/CONTRACT.md` §1.2 K-AUTH-1 and K-PROF-1 |
| DEL-01-04-REQ-010 | Unknown or unsupported scope facts must remain `TBD`, `ASSUMPTION`, `PROPOSAL`, conflict, or human-ruling-needed entries rather than invented content. | Inspect rows and notes for unsupported facts. | `docs/CONTRACT.md` §1.7 K-INVENT-1 and K-CONFLICT-1 |
| DEL-01-04-REQ-011 | The concrete boundary rows for this four-document kit must be inspectable in `Datasheet.md` under `Boundary Register Rows` until a governed amendment or publication step moves them into a dedicated register artifact. | Inspect `Datasheet.md` `Boundary Register Rows` for RowID, boundary item, source reference, amendment trigger, current status, and human ruling fields. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-01 / DEL-01-04; `docs/DIRECTIVE.md` §7; `docs/CONTRACT.md` §1.7 K-INVENT-1 |

## Standards

| Standard / Authority | Applicability |
|---|---|
| `docs/DIRECTIVE.md` | Governs founding intent, professional responsibility, out-of-scope posture, and change discipline. |
| `docs/CONTRACT.md` | Governs binding invariants for scope boundaries, settings, permissions, retired scope, and human authority. |
| `docs/PRD.md` | Governs current vNext product requirements and explicit non-goals; source hash warning applies. |
| `docs/PLAN.md` | Governs roadmap sequencing and retired PKG-08 interpretation. |
| `docs/TYPES.md` | Governs agent authority vocabulary and domain proposal vocabulary. |
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Governs DEL-01-04 identity, scope item mapping, and objective mapping. |

## Verification

Verification is documentary and review-based for this phase:

| Verification Item | Method |
|---|---|
| Four-doc kit completeness | Confirm `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist and are non-empty. |
| Boundary coverage | Trace SOW-065, SOW-076, SOW-077, and SOW-078 from decomposition to register requirements. |
| Source fidelity | Confirm non-trivial requirements cite source files and sections. |
| Conservative drafting | Confirm unsupported facts are marked `TBD`, `ASSUMPTION`, `PROPOSAL`, conflict, or human-ruling-needed. |
| Boundary-row inspection | Confirm the concrete register rows are present in `Datasheet.md` under `Boundary Register Rows` and include source reference, amendment trigger, current status, and human ruling fields. |
| Boundary review checklist | Confirm `docs/BOUNDARY_REVIEW_CHECKLISTS.md` covers scope-boundary and professional-boundary review without treating checklist completion as approval. |
| Scope containment | Confirm this run does not satisfy or mutate dependency rows and does not modify files outside the authorized tranche scope. |
| Status transition | Read current state from `_STATUS.md`; this work makes no transition, and any future human-gate transition requires governed approval evidence. |

## Documentation

Required artifacts for this deliverable:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_*.md`
- `Datasheet.md` `Boundary Register Rows` section as the concrete inspection surface for this kit
- `docs/BOUNDARY_REVIEW_CHECKLISTS.md` as the normalized review checklist and evidence template

Existing derivative artifact:

- `Dependencies.csv` is maintained by the separate dependency-extract workflow. This Pass 3 enrichment must not create or edit it.
