---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-04
package_id: PKG-01
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
project_scope_refs: [SOW-065, SOW-076, SOW-077, SOW-078]
package_objective_refs: [OBJ-009]
---

# Scope of Work — DEL-01-04

## Purpose and Objective Traceability

This migration candidate defines `DEL-01-04` in service of project scope [SOW-065, SOW-076, SOW-077, SOW-078] and package objectives [OBJ-009].

- **OUT-001** — A source-grounded scope-boundary and retired-scope register with amendment-trigger records, traceable to SOW-065, SOW-076, SOW-077, SOW-078, and OBJ-009.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-01-04 Scope Boundary and Retired Scope Register

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":2,"line_start":1,"source_sha256":"c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd","target_id":"CLM-001"} -->
#### Datasheet: DEL-01-04 Scope Boundary and Retired Scope Register

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":17,"line_start":3,"source_sha256":"c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd","target_id":"CLM-002"} -->
##### Identification

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

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":31,"line_start":18,"source_sha256":"c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd","target_id":"CLM-003"} -->
##### Attributes

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

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":42,"line_start":32,"source_sha256":"c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Reference integrity | `docs/PRD.md` is REF-006 and matches the current the current D-APP-38 corpus snapshot in `_REFERENCES.md`. | `_REFERENCES.md` REF-006; D-APP-38 |
| Dependency extraction | Existing derivative `Dependencies.csv` is owned by the separate dependency-extract workflow; this checklist normalization does not create, edit, satisfy, or retire rows. | `_DEPENDENCIES.md`; `Dependencies.csv` |
| Human authority | Agents and tools may draft and organize records, but humans approve, issue, sign, seal, and accept reliance. | `docs/TYPES.md` §3.3; `docs/DIRECTIVE.md` §3 |
| Unknown values | Unknown values remain `TBD`; agents and tools must not invent scope items, dependency targets, parameters, or professional conclusions. | `docs/CONTRACT.md` §1.7 K-INVENT-1 |
| Scope conflicts | Source conflicts must be surfaced rather than silently resolved. | `docs/CONTRACT.md` §1.7 K-CONFLICT-1 |
| Review checklist | Scope-boundary and professional-boundary review uses `docs/BOUNDARY_REVIEW_CHECKLISTS.md`; completion is evidence only, not issuance or release/professional approval. | ADQ-03 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":52,"line_start":43,"source_sha256":"c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd","target_id":"CLM-005"} -->
##### Construction

The register should be constructed as a documentary control surface with at least these record families:

| Record Family | Minimum Fields | Status |
|---|---|---|
| Out-of-scope items | Scope item ID, boundary statement, source reference, amendment trigger, current status, human ruling. | ASSUMPTION: structure inferred from anticipated artifacts and source-control needs. |
| Retired-scope notes | Retired item, prohibited reactivation path, allowed adjacent infrastructure, source reference, human ruling. | ASSUMPTION: structure inferred from SOW-077 and PKG-08 notes. |
| Amendment triggers | Trigger condition, affected boundary, required governed change surface, review evidence, approval status. | ASSUMPTION: structure inferred from `docs/DIRECTIVE.md` §7. |

<!-- sow-source-end -->

### CLM-006 — Boundary Register Rows

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":69,"line_start":53,"source_sha256":"c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd","target_id":"CLM-006"} -->
###### Boundary Register Rows

For this four-document kit, the concrete register-row artifact is this `Datasheet.md` section. Later publication may move these rows into a dedicated register file, but until amended this table is the inspection surface for boundary-row verification.

ADQ-03 also materialized `docs/BOUNDARY_REVIEW_CHECKLISTS.md` as the normalized review checklist for
scope-boundary and professional-boundary checks. The human ruling fields below remain `TBD` until an
accountable human records rulings or explicit deferrals.

| RowID | Boundary Item | Boundary Statement | Source Reference | Amendment Trigger | Current Status | Human Ruling |
|---|---|---|---|---|---|---|
| DEL-01-04-BR-001 | SOW-065 remote MCP/plugins/tool expansion | Remote MCP servers, plugins, remote execution, plugin marketplace, and broad tool search remain outside current scope until local SDK governance, permissions, hooks, event logging, and result storage are reliable. | `docs/PRD.md` §3.2 and §6.4; `docs/CONTRACT.md` §1.9 K-NET-1; `docs/PLAN.md` §11 | Governed amendment that admits remote or expanded tool scope and updates governance, tests, release checks, and implementation artifacts. | OUT | DEFERRED 2026-07-12 — D-APP-56 R4-P22; no scope amendment authorized. |
| DEL-01-04-BR-002 | SOW-076 ambient settings and shipped bypass | Shipped builds must not load ambient Claude settings and must not use `bypassPermissions` in shipped or ordinary operator workflows; developer-local bypass remains guarded. | `docs/PRD.md` §3.2 and FR-117; `docs/CONTRACT.md` §1.4 K-SDK-1 and §1.6 K-PERM-6 | Governed amendment plus SDK option, hook, environment guard, and release-check updates. | OUT | DEFERRED 2026-07-12 — D-APP-56 R4-P22; no scope amendment authorized. |
| DEL-01-04-BR-003 | SOW-077 retired PKG-08 scope | Retired PKG-08 execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record, and staleness propagation tooling remain retired; harness runtime event logging does not reactivate them. | `docs/PRD.md` §3.2 and KG-012; `docs/PLAN.md` §9; `docs/CONTRACT.md` §1.9 K-RETIRED-1 | Governed amendment that explicitly reactivates retired execution scope and updates active decomposition/package commitments. | OUT | DEFERRED 2026-07-12 — D-APP-56 R4-P22; no scope amendment authorized. |
| DEL-01-04-BR-004 | SOW-078 Windows/Linux packaging | Windows/Linux release packaging remains outside current release scope; current release target is macOS 15+ Apple Silicon unsigned/unnotarized local-builder DMG. | `docs/PRD.md` §6.4 and KG-014; `docs/CONTRACT.md` §1.9 K-RELEASE-1 | Governed release-scope amendment with packaging, validation, and instruction-root integrity updates. | OUT | DEFERRED 2026-07-12 — D-APP-56 R4-P22; no release-scope amendment authorized. |
| DEL-01-04-BR-005 | Domain operation execution and protected domain paths | Domain-engine integration as a shipping feature, direct protected-domain-path writes, and domain operation execution remain future-amendment scope; ruled staged read tools and loopback propose/refresh/validate tools are in scope, while apply and direct protected-path writes remain out. | `docs/PRD.md` §6.4 and FR-106 through FR-115; `docs/CONTRACT.md` §1.10; `docs/PLAN.md` R7; D-APP-49 through D-APP-52 | Governed domain-profile amendment with protected-path, proposal, deterministic-adapter, and human-gate controls. | OUT, except ruled staged read/proposal surface | RULED 2026-07-12 — D-APP-56 R4-P22/P25 ratifies the staged carve-in; apply and protected-path writes remain OUT. |
| DEL-01-04-BR-006 | Provider/residency expansion and Pi runtime use | Concrete provider/residency expansion is default-closed and requires explicit owner configuration/ruling under D-APP-44 F1. Pi remains pattern-corpus-only: no adapter, import, fork, Node 22 sidecar, runtime-floor migration, or spike is authorized. | SCA-APP-001; D-APP-01; D-APP-02; D-APP-44 F1; `docs/PRD.md` §3.2 | Explicit owner provider/residency authorization plus bounded implementation and verification; a separate scope reversal is required for any Pi runtime use. | OUT except explicitly owner-permitted provider/residency configurations | RULED 2026-07-12 — D-APP-56 R4-P06(f); retain default-closed posture and Pi prohibition. |

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":80,"line_start":70,"source_sha256":"c28d8755a9437bf814e3747219b88011d95ef3a6ff7892bbfcd5344fe66c0bbd","target_id":"CLM-007"} -->
##### References

| RefID | Source | Use |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | Product intent, professional authority, out-of-scope and change discipline. |
| REF-002 | `docs/CONTRACT.md` | Binding invariants for settings, permissions, retired scope, domain boundaries, and unknown/conflict handling. |
| REF-003 | `docs/SPEC.md` | Runtime mechanics and boundary surfaces; used only where source slices were relevant. |
| REF-004 | `docs/TYPES.md` | Authority model and vocabulary. |
| REF-005 | `docs/PLAN.md` | Roadmap sequencing, PKG-08 retirement notes, and future-amendment exclusions. |
| REF-006 | `docs/PRD.md` | Current vNext product requirements and explicit non-goals; the current D-APP-38 corpus snapshot records a matching authority-doc hash. |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method reference; no deliverable-specific requirements extracted. |
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-01-04 Scope Boundary and Retired Scope Register

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"2c62f5727c02f036097d1d1ce1361cbbe0b10fe6594fa21d0ffbfacc87cedc66","target_id":"CLM-008"} -->
#### Specification: DEL-01-04 Scope Boundary and Retired Scope Register

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":24,"line_start":3,"source_sha256":"2c62f5727c02f036097d1d1ce1361cbbe0b10fe6594fa21d0ffbfacc87cedc66","target_id":"CLM-009"} -->
##### Scope

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

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":40,"line_start":25,"source_sha256":"2c62f5727c02f036097d1d1ce1361cbbe0b10fe6594fa21d0ffbfacc87cedc66","target_id":"CLM-010"} -->
##### Requirements

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

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":51,"line_start":41,"source_sha256":"2c62f5727c02f036097d1d1ce1361cbbe0b10fe6594fa21d0ffbfacc87cedc66","target_id":"CLM-011"} -->
##### Standards

| Standard / Authority | Applicability |
|---|---|
| `docs/DIRECTIVE.md` | Governs founding intent, professional responsibility, out-of-scope posture, and change discipline. |
| `docs/CONTRACT.md` | Governs binding invariants for scope boundaries, settings, permissions, retired scope, and human authority. |
| `docs/PRD.md` | Governs current vNext product requirements and explicit non-goals; source hash warning applies. |
| `docs/PLAN.md` | Governs roadmap sequencing and retired PKG-08 interpretation. |
| `docs/TYPES.md` | Governs agent authority vocabulary and domain proposal vocabulary. |
| `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Governs DEL-01-04 identity, scope item mapping, and objective mapping. |

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":66,"line_start":52,"source_sha256":"2c62f5727c02f036097d1d1ce1361cbbe0b10fe6594fa21d0ffbfacc87cedc66","target_id":"CLM-012"} -->
##### Verification

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

<!-- sow-source-end -->

### CLM-013 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":82,"line_start":67,"source_sha256":"2c62f5727c02f036097d1d1ce1361cbbe0b10fe6594fa21d0ffbfacc87cedc66","target_id":"CLM-013"} -->
##### Documentation

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
<!-- sow-source-end -->

- **AC-001** — Preservation and traceability to SOW-065, SOW-076, SOW-077, SOW-078, and OBJ-009 are demonstrated without adding scope, reliance claims, lifecycle meaning, or obligations.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-01-04 Scope Boundary and Retired Scope Register

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"d738950bca0956f5f655ea701f268d6234a87ee30d2ecc5fb078edd3d813aeca","target_id":"CLM-014"} -->
#### Procedure: DEL-01-04 Scope Boundary and Retired Scope Register

<!-- sow-source-end -->

### CLM-015 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"d738950bca0956f5f655ea701f268d6234a87ee30d2ecc5fb078edd3d813aeca","target_id":"CLM-015"} -->
##### Purpose

Define how to produce and maintain the Scope Boundary and Retired Scope Register for DEL-01-04 without expanding current scope, inventing unsupported facts, assigning human ownership, or reactivating retired work.

<!-- sow-source-end -->

### CLM-016 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":16,"line_start":7,"source_sha256":"d738950bca0956f5f655ea701f268d6234a87ee30d2ecc5fb078edd3d813aeca","target_id":"CLM-016"} -->
##### Prerequisites

| Prerequisite | Status |
|---|---|
| Deliverable-local context exists at `_CONTEXT.md`. | Available. |
| Authoritative source pointers exist at `_REFERENCES.md`. | Available; REF-006 `docs/PRD.md` matches under the current D-APP-38 corpus snapshot. |
| Decomposition entry exists for DEL-01-04. | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`. |
| Human-declared upstream dependencies. | TBD; `_DEPENDENCIES.md` declares none extracted yet. |
| ResponsibleParty assignment. | TBD; must remain TBD until human assignment. |

<!-- sow-source-end -->

### CLM-017 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":65,"line_start":17,"source_sha256":"d738950bca0956f5f655ea701f268d6234a87ee30d2ecc5fb078edd3d813aeca","target_id":"CLM-017"} -->
##### Steps

1. Confirm the deliverable identity.
   - Verify `DeliverableID=DEL-01-04`, `PackageID=PKG-01`, `Type=DOC_UPDATE`, and `ResponsibleParty=TBD` in `_CONTEXT.md`.

2. Confirm overwrite safety.
   - Read `_STATUS.md`.
   - Proceed with P1/P2 authoring only if the current state is allowed by the task brief and skill contract.

3. Read source authority.
   - Read `_REFERENCES.md`.
   - Read accessible source slices from `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/PRD.md`, `docs/PLAN.md`, `docs/TYPES.md`, and the decomposition entry.
   - Confirm REF-006 `docs/PRD.md` matches the current D-APP-38 corpus version.

4. Build the out-of-scope register content.
   - Materialize the concrete register-row artifact in `Datasheet.md` under `Boundary Register Rows` unless a governed publication step moves the rows to a dedicated register file.
   - Include SOW-065 for remote MCP, plugins, remote execution, marketplace extension, and broad tool search before mature governance.
   - Include SOW-076 for ambient Claude settings and shipped/ordinary `bypassPermissions`.
   - Include SOW-078 for Windows/Linux release packaging.
   - Mark amendment requirements from `docs/DIRECTIVE.md` §7 and `docs/PRD.md` §12.1.

5. Build retired-scope notes.
   - Include SOW-077.
   - Record that retired PKG-08 execution-scope items remain retired unless amended.
   - Record that harness runtime event logging is separate runtime infrastructure and does not reactivate retired unified pipeline run records or broader PKG-08 hardening scope.

6. Build domain-operation boundary notes.
   - Record domain-engine operation execution as future-amendment scope.
   - Record that agents may write proposals and summaries, not protected model truth.
   - Record that applying domain operations requires explicit human acceptance.

7. Preserve unknowns and conflicts.
   - Use `TBD`, `ASSUMPTION`, `PROPOSAL`, or conflict-table entries for unsupported facts.
   - Do not create new scope items or assign ResponsibleParty.

8. Cross-check the four documents.
   - Confirm the same boundary items and terminology appear consistently in `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.
   - Confirm requirements in `Specification.md` have corresponding production and verification hooks here.
   - Use `docs/BOUNDARY_REVIEW_CHECKLISTS.md` as the normalized scope-boundary/professional-boundary review checklist.

9. Preserve current lifecycle state.
   - Current lifecycle state is `CHECKING`.
   - Do not perform a state regression or human-gate transition.
   - Any future human-gate transition requires the governed status workflow and its required human approval evidence.

10. Defer dependency extraction.
   - Do not create or edit `Dependencies.csv` during this four-documents run.
   - Treat any existing `Dependencies.csv` as output of the separate `TASK + dependency-extract` workflow described in `_DEPENDENCIES.md`.

<!-- sow-source-end -->

### CLM-018 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":79,"line_start":66,"source_sha256":"d738950bca0956f5f655ea701f268d6234a87ee30d2ecc5fb078edd3d813aeca","target_id":"CLM-018"} -->
##### Verification

| Check | Expected Result |
|---|---|
| Document existence | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist and are non-empty. |
| Boundary coverage | SOW-065, SOW-076, SOW-077, and SOW-078 are represented. |
| Source grounding | Non-trivial boundary statements cite source files and sections. |
| ResponsibleParty | Remains `TBD`. |
| Boundary-row artifact | `Datasheet.md` includes concrete `Boundary Register Rows` with source reference, amendment trigger, current status, and human ruling fields. |
| Boundary review checklist | `docs/BOUNDARY_REVIEW_CHECKLISTS.md` exists and preserves checklist completion as evidence only. |
| Dependency extraction | This run does not create or edit `Dependencies.csv`; if present, it remains owned by the separate dependency-extract workflow. |
| Status | Current state is read from `_STATUS.md`; no lifecycle transition occurs in this checklist normalization. |
| Conflicts | Active path mismatch is surfaced for human ruling; historical PRD hash mismatch is closed by the current D-APP-38 corpus snapshot. |

<!-- sow-source-end -->

### CLM-019 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":95,"line_start":80,"source_sha256":"d738950bca0956f5f655ea701f268d6234a87ee30d2ecc5fb078edd3d813aeca","target_id":"CLM-019"} -->
##### Records

Records produced or updated by this procedure:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` (read-only lifecycle evidence for this checklist normalization)
- `docs/BOUNDARY_REVIEW_CHECKLISTS.md`
- `_run_records/TASK_RUN_*.md`

Related derivative record owned by a separate workflow:

- `Dependencies.csv`

<!-- sow-source-end -->

### CLM-020 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":98,"line_start":96,"source_sha256":"d738950bca0956f5f655ea701f268d6234a87ee30d2ecc5fb078edd3d813aeca","target_id":"CLM-020"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-104 supersedes the setup-era statement that no dependency rows had been extracted: the 13-row derivative register exists and remains owned by the separate dependency workflow.
<!-- sow-source-end -->

- **VER-001** — Run deterministic validation, claim mapping, parity, checklist derivation, and rendering checks, followed by human review.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-01-04 Scope Boundary and Retired Scope Register

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"631d22964fc7c0d91ffddd577daa6c85244e1713d1bfb3ef445354361ff7383c","target_id":"CLM-021"} -->
#### Guidance: DEL-01-04 Scope Boundary and Retired Scope Register

<!-- sow-source-end -->

### CLM-022 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":8,"line_start":3,"source_sha256":"631d22964fc7c0d91ffddd577daa6c85244e1713d1bfb3ef445354361ff7383c","target_id":"CLM-022"} -->
##### Purpose

This deliverable is a scope guard. It keeps known out-of-scope and retired items visible so they are not accidentally reintroduced through implementation enthusiasm, runtime event logging, release packaging, plugin/tool expansion, SDK settings behavior, or future domain-engine work.

The controlling objective is OBJ-009: preserve professional boundary, product identity, and reliance-boundary ownership in docs, UI, runtime, and release behavior. Source: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §Objectives and §PKG-01 / DEL-01-04.

<!-- sow-source-end -->

### CLM-023 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":25,"line_start":9,"source_sha256":"631d22964fc7c0d91ffddd577daa6c85244e1713d1bfb3ef445354361ff7383c","target_id":"CLM-023"} -->
##### Principles

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

<!-- sow-source-end -->

### CLM-024 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":39,"line_start":26,"source_sha256":"631d22964fc7c0d91ffddd577daa6c85244e1713d1bfb3ef445354361ff7383c","target_id":"CLM-024"} -->
##### Considerations

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

<!-- sow-source-end -->

### CLM-025 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":48,"line_start":40,"source_sha256":"631d22964fc7c0d91ffddd577daa6c85244e1713d1bfb3ef445354361ff7383c","target_id":"CLM-025"} -->
##### Trade-offs

| Trade-off | Preferred Position | Rationale |
|---|---|---|
| Future compatibility vs current scope discipline | Preserve future vocabulary, but mark implementation as future-amendment scope. | Prevents premature implementation while keeping architectural runway. |
| Developer convenience vs shipped safety | Allow only guarded developer-local bypass; forbid shipped/ordinary bypass behavior. | Maintains product-owned permission boundaries and release posture. |
| Event logging vs retired pipeline scope | Permit runtime audit event logging; keep retired pipeline run records and hardening tools retired. | Preserves auditability without reactivating retired work. |
| Cross-platform ambition vs release certainty | Keep Windows/Linux packaging out of current scope. | Current release invariant names macOS 15+ Apple Silicon DMG unless amended. |

<!-- sow-source-end -->

### CLM-026 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":58,"line_start":49,"source_sha256":"631d22964fc7c0d91ffddd577daa6c85244e1713d1bfb3ef445354361ff7383c","target_id":"CLM-026"} -->
##### Examples

| Scenario | Register Disposition |
|---|---|
| A developer proposes adding a plugin marketplace before local permission hooks are stable. | Mark as blocked by SOW-065; requires governed amendment after local governance maturity. |
| A packaged build reads `.claude/settings.local.json` from the working root. | Mark as forbidden by SOW-076 / K-SDK-1; requires correction, not amendment-by-default. |
| Runtime events are added under `.chirality/sessions/<id>/events.jsonl`. | Allowed as runtime audit infrastructure if aligned with runtime contract; do not relabel as unified pipeline run records. |
| A release issue asks for Windows packaging in the current slice. | Mark as out of scope under SOW-078; requires release-scope amendment. |
| A domain adapter attempts to write directly to protected domain-engine model paths. | Mark as out of current scope and prohibited by domain boundary policy; future work must use proposal records and human acceptance. |

<!-- sow-source-end -->

### CLM-027 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":67,"line_start":59,"source_sha256":"631d22964fc7c0d91ffddd577daa6c85244e1713d1bfb3ef445354361ff7383c","target_id":"CLM-027"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CF-001 | Dispatch path names `PKG-01_Governance_and_Product_Boundaries`, but the only matching deliverable folder on disk is under `PKG-01_Product_Governance_and_Reliance_Boundaries`. | TASK dispatch | Filesystem path and `_CONTEXT.md` PackageName | Run record, final report | Use the located deliverable folder for this run and surface the stale path as a warning. | TBD |

Closed historical conflict: `CF-002` is superseded by the current D-APP-38 corpus snapshot; current `_REFERENCES.md`
records REF-006 `docs/PRD.md` as `MATCH`.

<!-- sow-source-end -->

### CLM-028 — Normalized Checklist Artifact

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":73,"line_start":68,"source_sha256":"631d22964fc7c0d91ffddd577daa6c85244e1713d1bfb3ef445354361ff7383c","target_id":"CLM-028"} -->
##### Normalized Checklist Artifact

ADQ-03 materialized `docs/BOUNDARY_REVIEW_CHECKLISTS.md` as the shared review checklist package. For
DEL-01-04, it supplies the scope-boundary checklist, amendment-trigger prompts, and finding template.
The boundary-row human ruling fields remain `TBD` until an accountable human records rulings or
explicit deferrals.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-065 SOW-076 SOW-077 SOW-078 OBJ-009 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
