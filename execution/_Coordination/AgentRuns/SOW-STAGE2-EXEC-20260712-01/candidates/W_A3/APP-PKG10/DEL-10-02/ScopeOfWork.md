---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-02
package_id: PKG-10
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
project_scope_refs: [SOW-068]
package_objective_refs: [OBJ-010]
---

# Scope of Work — DEL-10-02

## Purpose and Objective Traceability

This migration candidate defines `DEL-10-02` in service of project scope [SOW-068] and package objectives [OBJ-010].

- **OUT-001** — Protected/proposal path policy, hook implications, and examples for DEL-10-02 under SOW-068 and OBJ-010.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-10-02 Protected Path and Proposal Path Policy

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":4,"line_start":1,"source_sha256":"f86b287997fabb185245da52f2b1cf43a852fcf28c7b8526f8bcf2d9d12a610d","target_id":"CLM-001"} -->
#### Datasheet: DEL-10-02 Protected Path and Proposal Path Policy

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":20,"line_start":5,"source_sha256":"f86b287997fabb185245da52f2b1cf43a852fcf28c7b8526f8bcf2d9d12a610d","target_id":"CLM-002"} -->
##### Identification

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

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":34,"line_start":21,"source_sha256":"f86b287997fabb185245da52f2b1cf43a852fcf28c7b8526f8bcf2d9d12a610d","target_id":"CLM-003"} -->
##### Attributes

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

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":46,"line_start":35,"source_sha256":"f86b287997fabb185245da52f2b1cf43a852fcf28c7b8526f8bcf2d9d12a610d","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Activation condition | Governed future amendment after core harness stability. | `docs/PRD.md` §8.17; `docs/PLAN.md` R7 |
| Profile prerequisite | A generic `DomainEngineProfile` contract precedes engine-specific integration. | `docs/PRD.md` §8.17 FR-107 |
| Enforcement prerequisite | Profile validation determines what the harness may read, propose, validate, or request without guessing from prompt text. | `docs/PRD.md` §8.17 FR-108 |
| Direct protected writes | Prohibited for agents and ordinary Chirality tools. | `docs/PRD.md` §8.17 FR-110; `docs/PRD.md` §10.10 |
| Human acceptance | Required before application of a domain operation. | `docs/PRD.md` §8.17 FR-113; `docs/SPEC.md` §18 |
| PRD source status | Source warning: expected SHA256 `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`; observed SHA256 `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`. Treated as source status by dispatch instruction. | `_REFERENCES.md` REF-006 |
| Responsible ownership | TBD - downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership. P3 disposition: B-001 converted to closure-relevant TBD. | `_CONTEXT.md` §Source Authority |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":56,"line_start":47,"source_sha256":"f86b287997fabb185245da52f2b1cf43a852fcf28c7b8526f8bcf2d9d12a610d","target_id":"CLM-005"} -->
##### Construction

| Element | Construction Rule | Source |
|---|---|---|
| Policy record | Define the separation between protected paths and proposal paths, plus enforcement implications. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-10-02 |
| Hook implication | Protected path writes must be denied or routed away from direct agent mutation; hook implementation detail remains TBD until future amendment. | `docs/PRD.md` §8.17 FR-110; `docs/SPEC.md` §18 |
| Proposal outputs | Agents may create proposals, summaries, and review aids under declared proposal paths. | `docs/PRD.md` §8.17 FR-111; `docs/TYPES.md` §11.3 |
| Adapter route | Accepted protected-state changes require approved adapter or operation workflow plus explicit human gate. | `docs/PRD.md` §10.10 |
| Examples | Only example category supported by accessible sources is OpenPipeStress as a possible fixture profile, not core runtime behavior. Concrete file examples are TBD. | `docs/PRD.md` §8.17 FR-114; `docs/TYPES.md` §11.3 |

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":65,"line_start":57,"source_sha256":"f86b287997fabb185245da52f2b1cf43a852fcf28c7b8526f8bcf2d9d12a610d","target_id":"CLM-006"} -->
##### References

- `docs/PRD.md` §8.17, §10.10, source warning per `_REFERENCES.md` REF-006.
- `docs/CONTRACT.md` §1.10.
- `docs/SPEC.md` §18.
- `docs/TYPES.md` §11.
- `docs/PLAN.md` R7.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-10 and SOW-068 rows.

<!-- sow-source-end -->

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":68,"line_start":66,"source_sha256":"f86b287997fabb185245da52f2b1cf43a852fcf28c7b8526f8bcf2d9d12a610d","target_id":"CLM-007"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-149 acknowledges concrete path blocks in ADOPTED profiles while retaining accepted-glob syntax and hook API as TBD/gated.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-10-02 Protected Path and Proposal Path Policy

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":4,"line_start":1,"source_sha256":"9dfb63e33ed32658a9ce0fba9615547fb04a2515ce9f49ced1416b6757048ef7","target_id":"CLM-008"} -->
#### Specification: DEL-10-02 Protected Path and Proposal Path Policy

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":24,"line_start":5,"source_sha256":"9dfb63e33ed32658a9ce0fba9615547fb04a2515ce9f49ced1416b6757048ef7","target_id":"CLM-009"} -->
##### Scope

This deliverable specifies the future policy boundary separating domain-engine protected paths from agent-writable proposal paths for PKG-10. It covers SOW-068 and supports OBJ-010 by preserving future domain-engine compatibility without turning domain solvers into Chirality core.

In scope:

- Define protected path and proposal path semantics for future `DomainEngineProfile` integration.
- State the write-quarantine rule for protected domain-engine model truth.
- State that proposals, summaries, review aids, operation records, and human gates are separate from authoritative protected artifacts.
- Capture hook and workflow implications at policy level.

Out of scope:

- Current-release domain operation execution.
- Concrete OpenPipeStress implementation.
- Concrete filesystem path patterns for any specific engine profile.
- Direct implementation of `/api/domain/*` endpoints.

Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-10-02; `docs/PRD.md` §8.17; `docs/SPEC.md` §18.

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":41,"line_start":25,"source_sha256":"9dfb63e33ed32658a9ce0fba9615547fb04a2515ce9f49ced1416b6757048ef7","target_id":"CLM-010"} -->
##### Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-10-02-REQ-001 | The policy shall preserve PKG-10 as future-boundary scope and shall not activate current-release domain operation execution. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-10; `docs/PRD.md` §8.17 |
| DEL-10-02-REQ-002 | The policy shall define protected paths as authoritative domain-engine artifact paths not directly writable by agents. | `docs/TYPES.md` §11.3 |
| DEL-10-02-REQ-003 | The policy shall define proposal paths as agent-writable folders for proposed changes, summaries, or review aids. | `docs/TYPES.md` §11.3 |
| DEL-10-02-REQ-004 | Protected domain paths shall be write-quarantined from direct agent and ordinary tool mutation. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110 |
| DEL-10-02-REQ-005 | Agents shall write proposals, summaries, and review aids rather than protected domain-engine model truth. | `docs/PRD.md` §8.17 FR-111; `docs/PLAN.md` R7 |
| DEL-10-02-REQ-006 | Any accepted mutation of domain state shall flow through an approved adapter or operation workflow and explicit human gate. | `docs/PRD.md` §10.10; `docs/SPEC.md` §18 |
| DEL-10-02-REQ-007 | The policy shall preserve separation between authoritative domain truth owned by the domain engine and Chirality records/proposals/human gates. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1; `docs/PRD.md` §8.17 FR-106 |
| DEL-10-02-REQ-008 | The policy shall require boundary notices or equivalent copy so domain-engine outputs are not presented as professional approval, code compliance, external validation, or Chirality-owned solver truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115 |
| DEL-10-02-REQ-009 | ASSUMPTION: Path policy enforcement should be expressed through future profile policy, path hooks, and operation workflow checks because those enforcement surfaces are named by CONTRACT. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2 |
| DEL-10-02-REQ-010 | Concrete path glob syntax, adapter manifest schema, and per-engine examples remain TBD until DEL-10-01 / future amendment defines the profile contract. | `docs/PRD.md` §8.17 FR-108; `docs/TYPES.md` §11.1 |
| DEL-10-02-REQ-011 | Future acceptance evidence shall include a proof slot showing that direct protected-path writes fail closed and cannot be performed by ordinary agent tools. P3 disposition: F-001 and X-001 incorporated as future evidence criteria. | `docs/CONTRACT.md` §1.6 K-PERM-2, §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110 |
| DEL-10-02-REQ-012 | Future acceptance evidence shall include proof slots for proposal-path write allowance and accepted mutation through an approved adapter or operation workflow plus explicit human gate. P3 disposition: F-002 and D-002 incorporated as future workflow evidence criteria. | `docs/PRD.md` §8.17 FR-111, FR-113; `docs/SPEC.md` §18 |

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":52,"line_start":42,"source_sha256":"9dfb63e33ed32658a9ce0fba9615547fb04a2515ce9f49ced1416b6757048ef7","target_id":"CLM-011"} -->
##### Standards

| Standard / Source | Applicability |
|---|---|
| `docs/CONTRACT.md` §1.10 | Binding invariants K-DOMAIN-1 through K-DOMAIN-4. |
| `docs/PRD.md` §8.17 | Future domain compatibility requirements FR-106 through FR-115; REF-006 has a hash status: MATCH status in `_REFERENCES.md`. — reconciled under D-APP-38 |
| `docs/PRD.md` §10.10 | Future domain artifact categories and protected mutation route. |
| `docs/SPEC.md` §18 | Provisional endpoint boundary and future profile requirements. |
| `docs/TYPES.md` §11 | Vocabulary for `DomainEngineProfile`, `OperationProposal`, protected path, proposal path, deterministic adapter, boundary notice, and OpenPipeStress fixture. |
| `docs/PLAN.md` R7 | Roadmap placement and acceptance posture for future domain profiles and operation proposals. |

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":66,"line_start":53,"source_sha256":"9dfb63e33ed32658a9ce0fba9615547fb04a2515ce9f49ced1416b6757048ef7","target_id":"CLM-012"} -->
##### Verification

| Requirement | Verification Approach |
|---|---|
| DEL-10-02-REQ-001 | Review text for future-boundary language and absence of implementation activation. |
| DEL-10-02-REQ-002, DEL-10-02-REQ-003 | Confirm definitions match `docs/TYPES.md` §11.3. |
| DEL-10-02-REQ-004, DEL-10-02-REQ-005 | Confirm policy distinguishes protected model truth from proposal/summarization outputs. |
| DEL-10-02-REQ-006 | Confirm accepted mutation route includes approved adapter or operation workflow and explicit human gate. |
| DEL-10-02-REQ-007, DEL-10-02-REQ-008 | Confirm professional-boundary and solver-truth separation language is present. |
| DEL-10-02-REQ-009 | Human review required because hook implementation detail is not fully specified in accessible source slices. |
| DEL-10-02-REQ-010 | Human review required when profile contract or engine-specific path patterns are drafted. |
| DEL-10-02-REQ-011 | Future validation fixture or equivalent review evidence confirms direct protected writes are denied or routed away from mutation and fail closed. |
| DEL-10-02-REQ-012 | Future validation fixture or equivalent review evidence confirms proposal-path writes remain allowed as non-binding artifacts and accepted mutation requires the approved route plus human gate. |

<!-- sow-source-end -->

### CLM-013 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":80,"line_start":67,"source_sha256":"9dfb63e33ed32658a9ce0fba9615547fb04a2515ce9f49ced1416b6757048ef7","target_id":"CLM-013"} -->
##### Documentation

Required artifacts for this deliverable:

- Protected/proposal path policy.
- Hook implications.
- Examples.

Current documentation gaps:

- Concrete protected/proposal path pattern examples are TBD.
- Profile-specific adapter and manifest details are TBD.
- ResponsibleParty remains TBD by dispatch instruction and `_CONTEXT.md`.
- Future test fixture categories remain TBD until the governed `DomainEngineProfile` syntax and operation workflow are accepted: direct protected-write denial, proposal-path write allowance, and accepted mutation through human gate. P3 disposition: F-002 and X-002 incorporated as future slots.
<!-- sow-source-end -->

- **AC-001** — The DEL-10-02 protected/proposal path policy, hook implications, and examples preserve the exact legacy source content and remain bounded to SOW-068 and OBJ-010.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-10-02 Protected Path and Proposal Path Policy

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":4,"line_start":1,"source_sha256":"a0c963df1ea2827000501fef17b2e14f40e80e87829c83e41fa389e9e94db72c","target_id":"CLM-014"} -->
#### Procedure: DEL-10-02 Protected Path and Proposal Path Policy

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-015 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":8,"line_start":5,"source_sha256":"a0c963df1ea2827000501fef17b2e14f40e80e87829c83e41fa389e9e94db72c","target_id":"CLM-015"} -->
##### Purpose

Define a repeatable procedure for producing and reviewing the protected path and proposal path policy without activating domain-engine implementation. The procedure preserves the future-boundary posture of PKG-10 and keeps protected domain-engine model truth separate from agent-writable proposal outputs.

<!-- sow-source-end -->

### CLM-016 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":20,"line_start":9,"source_sha256":"a0c963df1ea2827000501fef17b2e14f40e80e87829c83e41fa389e9e94db72c","target_id":"CLM-016"} -->
##### Prerequisites

| Prerequisite | Status / Source |
|---|---|
| Deliverable context for DEL-10-02 | Available in `_CONTEXT.md`. |
| Decomposition entry for DEL-10-02 and SOW-068 | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`. |
| Domain invariants | Available in `docs/CONTRACT.md` §1.10. |
| Future domain requirements | Available in `docs/PRD.md` §8.17 and §10.10, with REF-006 hash status: MATCH treated as source status. — reconciled under D-APP-38 |
| Future profile vocabulary | Available in `docs/TYPES.md` §11. |
| Declared upstream dependencies | Extracted dependency register exists in `_DEPENDENCIES.md`; declared upstream/downstream sections remain TBD. P3 disposition: B-002 already covered as deferred closure input. |
| ResponsibleParty | TBD. |

<!-- sow-source-end -->

### CLM-017 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":58,"line_start":21,"source_sha256":"a0c963df1ea2827000501fef17b2e14f40e80e87829c83e41fa389e9e94db72c","target_id":"CLM-017"} -->
##### Steps

1. Confirm the work remains future-boundary scope.
   - Check that the policy does not implement current-release domain operation execution or activate `/api/domain/*` endpoints.
   - Source: `docs/PRD.md` §8.17; `docs/SPEC.md` §18.

2. Define policy terms from authoritative vocabulary.
   - Use `Protected path` as an authoritative domain-engine artifact path not directly writable by agents.
   - Use `Proposal path` as an agent-writable folder for proposed changes, summaries, or review aids.
   - Source: `docs/TYPES.md` §11.3.

3. State the protected write quarantine.
   - Require direct agent writes to protected domain paths to be denied or routed through the future approved adapter / operation workflow.
   - Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110.

4. State the proposal write allowance.
   - Permit agents to write proposals, summaries, and review aids to declared proposal paths.
   - Do not treat those outputs as accepted protected state.
   - Source: `docs/PRD.md` §8.17 FR-111; `docs/TYPES.md` §11.3.

5. State the accepted mutation path.
   - Require an approved adapter or operation workflow and explicit human gate before protected domain state changes.
   - Source: `docs/PRD.md` §10.10; `docs/SPEC.md` §18.

6. Capture hook implications without over-specifying implementation.
   - Record that future enforcement must distinguish protected paths from proposal paths and fail closed for direct protected writes.
   - Mark exact hook API, path glob syntax, and adapter manifest behavior as TBD unless supplied by a future accepted profile contract.
   - Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-108.

7. Add boundary-notice requirements.
   - Confirm the policy prevents domain-engine outputs from being represented as professional approval, code compliance, external validation, or solver truth owned by Chirality.
   - Source: `docs/PRD.md` §8.17 FR-115; `docs/CONTRACT.md` §1.10 K-DOMAIN-4.

8. Review examples.
   - Include only category examples supported by sources unless profile-specific path patterns are later accepted.
   - Mark concrete OpenPipeStress or engine-specific paths as TBD.
   - Source: `docs/PRD.md` §8.17 FR-114; `docs/TYPES.md` §11.3.

<!-- sow-source-end -->

### CLM-018 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":71,"line_start":59,"source_sha256":"a0c963df1ea2827000501fef17b2e14f40e80e87829c83e41fa389e9e94db72c","target_id":"CLM-018"} -->
##### Verification

| Check | Pass Criteria |
|---|---|
| Future-boundary check | No current-release domain engine execution is activated or implied. |
| Terminology check | Protected/proposal path definitions match `docs/TYPES.md` §11.3. |
| Write-quarantine check | Protected domain paths are not agent-writable in policy text. |
| Proposal-path check | Agent-writable outputs are limited to proposals, summaries, and review aids. |
| Human-gate check | Accepted protected-state mutation requires explicit human acceptance. |
| Boundary-copy check | No text says Chirality approves, validates, certifies, or owns solver truth. |
| TBD check | Concrete path patterns, hook implementation details, and engine-specific examples remain TBD where unsupported. |
| Future fixture check | Future verification records include categories for direct protected-write denial, proposal-path write allowance, and accepted mutation through human gate once profile syntax and workflow are accepted. P3 disposition: F-002 incorporated. |

<!-- sow-source-end -->

### CLM-019 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":79,"line_start":72,"source_sha256":"a0c963df1ea2827000501fef17b2e14f40e80e87829c83e41fa389e9e94db72c","target_id":"CLM-019"} -->
##### Records

- Protected/proposal path policy: `Specification.md`.
- Hook implications and TBDs: `Specification.md`, `Guidance.md`.
- Examples and conflicts: `Guidance.md`.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
- Dependency register: `_DEPENDENCIES.md` includes extracted active rows, while human-declared upstream/downstream sections remain TBD; closure must not treat those extracted rows as human-declared acceptance.
- Future workflow owner: TBD - the owner who defines the approved adapter or operation workflow that can convert proposals into protected-state changes is not named in accessible sources. P3 disposition: D-002 converted to closure-relevant TBD.
<!-- sow-source-end -->

- **VER-001** — Verify DEL-10-02 source-marker coverage and byte parity against the exact legacy four-document source, and confirm SOW-068 and OBJ-010 traceability.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-10-02 Protected Path and Proposal Path Policy

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":4,"line_start":1,"source_sha256":"95d362c022b44d3aee1e1dbbf1aabe64ddf82cfc22f4f72992e3aa6b792ca8e8","target_id":"CLM-020"} -->
#### Guidance: DEL-10-02 Protected Path and Proposal Path Policy

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-021 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":8,"line_start":5,"source_sha256":"95d362c022b44d3aee1e1dbbf1aabe64ddf82cfc22f4f72992e3aa6b792ca8e8","target_id":"CLM-021"} -->
##### Purpose

DEL-10-02 exists to define a future security boundary for domain-engine filesystem interaction: agents may write proposals, summaries, and review aids, but they must not write protected domain-engine model truth. This supports OBJ-010 while keeping PKG-10 in future-boundary scope. Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-10-02; `docs/PRD.md` §8.17.

<!-- sow-source-end -->

### CLM-022 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":17,"line_start":9,"source_sha256":"95d362c022b44d3aee1e1dbbf1aabe64ddf82cfc22f4f72992e3aa6b792ca8e8","target_id":"CLM-022"} -->
##### Principles

1. **Future-boundary first.** Treat this policy as compatibility design for a governed future amendment, not as permission to activate domain-engine execution now. Source: `docs/PRD.md` §8.17; `docs/SPEC.md` §18.
2. **Protected truth stays protected.** Protected paths hold authoritative domain-engine artifacts and are not directly writable by agents. Source: `docs/TYPES.md` §11.3; `docs/CONTRACT.md` §1.10 K-DOMAIN-2.
3. **Proposals are non-binding work products.** Proposal paths may hold proposed changes, summaries, or review aids, but they do not become accepted protected domain state without the future workflow. Source: `docs/TYPES.md` §11.3; `docs/PRD.md` §8.17 FR-111.
4. **Accepted mutation needs a gate.** Any accepted mutation of protected domain state must flow through an approved adapter or operation workflow and explicit human gate. Source: `docs/PRD.md` §10.10; `docs/SPEC.md` §18.
5. **Chirality does not become the solver.** Domain engines own authoritative domain truth; Chirality governs interaction, proposals, records, and human gates. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-1; `docs/PRD.md` §8.17 FR-106.
6. **Boundary copy matters.** Domain-engine outputs must not be presented as professional approval, code compliance, external validation, or solver truth owned by Chirality. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115.

<!-- sow-source-end -->

### CLM-023 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":26,"line_start":18,"source_sha256":"95d362c022b44d3aee1e1dbbf1aabe64ddf82cfc22f4f72992e3aa6b792ca8e8","target_id":"CLM-023"} -->
##### Considerations

- Policy should be profile-driven once `DomainEngineProfile` exists; the accessible sources name `protectedPaths` and `proposalPaths` fields but do not define concrete path glob syntax. Source: `docs/TYPES.md` §11.1.
- Hook implications are policy-level in the current source set. CONTRACT names path hooks and operation workflow as enforcement surfaces, but the exact hook API for domain paths is TBD. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-2.
- OpenPipeStress is only a potential first fixture profile. Avoid hardcoding OpenPipeStress assumptions into Chirality core policy. Source: `docs/PRD.md` §8.17 FR-114; `docs/TYPES.md` §11.3.
- REF-006 `docs/PRD.md` has a hash status: MATCH in `_REFERENCES.md`; dispatch instruction says to treat that MATCH as a source status. (reconciled under D-APP-38).
- Concrete protected/proposal path examples stay category-level because `DomainEngineProfile` exposes `protectedPaths` and `proposalPaths` fields but the accessible sources do not define accepted glob syntax or per-engine path patterns. P3 disposition: C-001 already covered and made explicit; X-002 remains a future documentation slot.
- Final publication wording should continue to say proposal artifacts are review aids only: they do not become accepted protected domain state without the future approved workflow and explicit human gate. P3 disposition: E-002 incorporated as closure wording guidance.

<!-- sow-source-end -->

### CLM-024 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":35,"line_start":27,"source_sha256":"95d362c022b44d3aee1e1dbbf1aabe64ddf82cfc22f4f72992e3aa6b792ca8e8","target_id":"CLM-024"} -->
##### Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Proposal usability vs protected-state safety | Permit agent-authored proposals and summaries, but deny direct protected model writes. | `docs/PRD.md` §8.17 FR-110, FR-111 |
| Generic profile policy vs engine-specific convenience | Keep policy generic until profile contract and fixture adoption are accepted. | `docs/PRD.md` §8.17 FR-107, FR-114 |
| Prompt guidance vs runtime enforcement | Do not rely on prompt text alone for protected path denies; future implementation needs profile/path/hook enforcement. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110 |
| Review velocity vs human authority | Require explicit human acceptance before applying domain operations. | `docs/PRD.md` §8.17 FR-113; `docs/SPEC.md` §18 |

<!-- sow-source-end -->

### CLM-025 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":43,"line_start":36,"source_sha256":"95d362c022b44d3aee1e1dbbf1aabe64ddf82cfc22f4f72992e3aa6b792ca8e8","target_id":"CLM-025"} -->
##### Examples

Supported example categories:

- Agent writes a proposed domain change package, summary, or review aid to a proposal path. Source: `docs/TYPES.md` §11.3; `docs/PRD.md` §8.17 FR-111.
- Agent direct write to a protected model path is denied or routed to a proposal workflow. Source: `docs/PRD.md` §8.17 FR-110; `docs/PRD.md` §10.10.
- OpenPipeStress may be represented as a future fixture profile if adopted, but concrete OpenPipeStress path examples are TBD. Source: `docs/PRD.md` §8.17 FR-114.

<!-- sow-source-end -->

### CLM-026 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":52,"line_start":44,"source_sha256":"95d362c022b44d3aee1e1dbbf1aabe64ddf82cfc22f4f72992e3aa6b792ca8e8","target_id":"CLM-026"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | PRD source hash status: MATCHes expected reference hash, but dispatch instruction says to treat it as source status. | `_REFERENCES.md` REF-006 | Dispatch brief | All PRD-grounded sections | Use local `docs/PRD.md` as accessible source with warning recorded. | TBD — reconciled under D-APP-38 |
| CT-002 | Concrete protected/proposal path examples are requested as anticipated artifacts, but accessible sources define only categories and fields, not specific path patterns. | `_CONTEXT.md` Anticipated Artifacts | `docs/TYPES.md` §11.1/§11.3; `docs/PRD.md` §8.17 | Examples, requirements, procedure | Mark concrete patterns TBD until `DomainEngineProfile` contract/future amendment supplies them. | TBD |
| CT-003 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006 | `docs/PRD.md` §8.17 and §10.10 | PRD-grounded requirements, closure language | Keep A-001 and E-001 visible as a source-warning conflict until a human accepts or replaces the PRD snapshot. | TBD |
| CT-004 | No accountable owner is named for accepting or replacing the REF-006 PRD snapshot before final policy closure. | `_REFERENCES.md` REF-006 | `_CONTEXT.md` Source Authority | Source warning closure | Treat D-001 as a human-ruling TBD; do not close the PRD source warning by agent judgment. | TBD |

<!-- sow-source-end -->

### CLM-027 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":55,"line_start":53,"source_sha256":"95d362c022b44d3aee1e1dbbf1aabe64ddf82cfc22f4f72992e3aa6b792ca8e8","target_id":"CLM-027"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-149 acknowledges concrete path blocks in ADOPTED profiles while retaining accepted-glob syntax and hook API as TBD/gated.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-068 OBJ-010 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
