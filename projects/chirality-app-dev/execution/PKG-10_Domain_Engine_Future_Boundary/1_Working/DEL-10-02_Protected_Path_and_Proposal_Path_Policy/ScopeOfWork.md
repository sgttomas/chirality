---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-02
package_id: PKG-10
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-068]
package_objective_refs: [OBJ-010]
---

# Scope of Work — DEL-10-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-10-02` in service of project scope [SOW-068] and package objectives [OBJ-010].

- **OUT-001** — Protected/proposal path policy, hook implications, and examples for DEL-10-02 under SOW-068 and OBJ-010.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-10-02 Protected Path and Proposal Path Policy

> #### Datasheet: DEL-10-02 Protected Path and Proposal Path Policy
>
> REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-10-02 |
> | DeliverableName | Protected Path and Proposal Path Policy |
> | PackageID | PKG-10 |
> | PackageName | Domain Engine Future Boundary |
> | ResponsibleParty | TBD |
> | Type | SECURITY_CONTROL |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ContextEnvelope | M |
> | Scope Item | SOW-068 |
> | Objective | OBJ-010 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Policy posture | Future-boundary / gated scope, not current-release domain operation execution. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-10; `docs/PRD.md` §8.17 |
> | Protected path | Authoritative domain-engine artifact path not directly writable by agents. | `docs/TYPES.md` §11.3 |
> | Agent-writable path | Profile-approved folder for proposed changes, summaries, review aids, checklists, TBD registers, or reconciliation notes; proposal paths are a subset. | `docs/TYPES.md` §11.3; `docs/PRD.md` §8.17 FR-111 |
> | Domain truth owner | Domain engines own authoritative domain truth when adopted by amendment; Chirality governs interaction, proposals, records, and human gates. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1; `docs/PRD.md` §8.17 FR-106 |
> | Agent write rule | Agents may write proposals and summaries, not protected domain-engine model truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PLAN.md` R7 |
> | Accepted mutation route | Any accepted mutation of domain state must flow through an approved adapter or operation workflow and an explicit human gate. | `docs/PRD.md` §10.10; `docs/SPEC.md` §18 |
> | Boundary notice requirement | Domain-engine outputs must not be represented as professional approval, code compliance, external validation, or solver truth owned by Chirality. | `docs/PRD.md` §8.17 FR-115; `docs/CONTRACT.md` §1.10 K-DOMAIN-4 |
> | Current concrete path patterns | Read `protected_write_paths` and `agent_writable_paths` in the ADOPTED OpenPipeStress and PEC profiles; accepted glob syntax and enforcement remain outstanding. | `docs/PRD.md` §8.17 FR-108 |
> | Profile-specific examples | The ADOPTED OpenPipeStress and PEC profile path blocks provide concrete examples; no glob matching or enforcement proof is inferred from declarations. | `docs/TYPES.md` §11.1; `docs/PRD.md` §8.17 FR-108 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Activation condition | Governed future amendment after core harness stability. | `docs/PRD.md` §8.17; `docs/PLAN.md` R7 |
> | Profile prerequisite | A generic `DomainEngineProfile` contract precedes engine-specific integration. | `docs/PRD.md` §8.17 FR-107 |
> | Enforcement prerequisite | Profile validation determines what the harness may read, propose, validate, or request without guessing from prompt text. | `docs/PRD.md` §8.17 FR-108 |
> | Direct protected writes | Prohibited for agents and ordinary Chirality tools. | `docs/PRD.md` §8.17 FR-110; `docs/PRD.md` §10.10 |
> | Human acceptance | Required before application of a domain operation. | `docs/PRD.md` §8.17 FR-113; `docs/SPEC.md` §18 |
> | PRD source status | REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical. | `_REFERENCES.md` REF-006 |
> | Responsible ownership | TBD - downstream TASK work must preserve `ResponsibleParty: TBD` until a human assigns ownership. P3 disposition: B-001 converted to closure-relevant TBD. | `_CONTEXT.md` §Source Authority |
>

### CLM-005 — Construction

> ##### Construction
>
> | Element | Construction Rule | Source |
> |---|---|---|
> | Policy record | Define the separation between protected paths and proposal paths, plus enforcement implications. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-10-02 |
> | Hook implication | Protected path writes must be denied or routed away from direct agent mutation; hook implementation detail remains TBD until future amendment. | `docs/PRD.md` §8.17 FR-110; `docs/SPEC.md` §18 |
> | Proposal outputs | Agents may create proposals, summaries, and review aids under declared proposal paths. | `docs/PRD.md` §8.17 FR-111; `docs/TYPES.md` §11.3 |
> | Adapter route | Accepted protected-state changes require approved adapter or operation workflow plus explicit human gate. | `docs/PRD.md` §10.10 |
> | Examples | Use ADOPTED OpenPipeStress and PEC path blocks as concrete profile examples; keep solver assumptions outside core behavior. | `docs/PRD.md` §8.17 FR-114; `docs/TYPES.md` §11.3 |
>

### CLM-006 — References

> ##### References
>
> - `docs/PRD.md` §8.17, §10.10, reference basis and observed status in `_REFERENCES.md` REF-006.
> - `docs/CONTRACT.md` §1.10.
> - `docs/SPEC.md` §18.
> - `docs/TYPES.md` §11.
> - `docs/PLAN.md` R7.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-10 and SOW-068 rows.
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-149 acknowledges concrete path blocks in ADOPTED profiles while retaining accepted-glob syntax and hook API as TBD/gated.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-10-02 Protected Path and Proposal Path Policy

> #### Specification: DEL-10-02 Protected Path and Proposal Path Policy
>
> REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable specifies the future policy boundary separating domain-engine protected paths from agent-writable proposal paths for PKG-10. It covers SOW-068 and supports OBJ-010 by preserving future domain-engine compatibility without turning domain solvers into Chirality core.
>
> In scope:
>
> - Define protected path and proposal path semantics for future `DomainEngineProfile` integration.
> - State the write-quarantine rule for protected domain-engine model truth.
> - State that proposals, summaries, review aids, operation records, and human gates are separate from authoritative protected artifacts.
> - Capture hook and workflow implications at policy level.
>
> Out of scope:
>
> - Current-release domain operation execution.
> - Concrete OpenPipeStress implementation.
> - Concrete filesystem path patterns for any specific engine profile.
> - Direct implementation of `/api/domain/*` endpoints.
>
> Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-10-02; `docs/PRD.md` §8.17; `docs/SPEC.md` §18.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-10-02-REQ-001 | The policy shall preserve PKG-10 as future-boundary scope and shall not activate current-release domain operation execution. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-10; `docs/PRD.md` §8.17 |
> | DEL-10-02-REQ-002 | The policy shall define protected paths as authoritative domain-engine artifact paths not directly writable by agents. | `docs/TYPES.md` §11.3 |
> | DEL-10-02-REQ-003 | The policy shall define agent-writable paths as profile-approved folders for proposed changes, summaries, review aids, checklists, TBD registers, or reconciliation notes; proposal paths are a subset. | `docs/TYPES.md` §11.3 |
> | DEL-10-02-REQ-004 | Protected domain paths shall be write-quarantined from direct agent and ordinary tool mutation. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110 |
> | DEL-10-02-REQ-005 | Agents shall write proposals, summaries, and review aids rather than protected domain-engine model truth. | `docs/PRD.md` §8.17 FR-111; `docs/PLAN.md` R7 |
> | DEL-10-02-REQ-006 | Any accepted mutation of domain state shall flow through an approved adapter or operation workflow and explicit human gate. | `docs/PRD.md` §10.10; `docs/SPEC.md` §18 |
> | DEL-10-02-REQ-007 | The policy shall preserve separation between authoritative domain truth owned by the domain engine and Chirality records/proposals/human gates. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1; `docs/PRD.md` §8.17 FR-106 |
> | DEL-10-02-REQ-008 | The policy shall require boundary notices or equivalent copy so domain-engine outputs are not presented as professional approval, code compliance, external validation, or Chirality-owned solver truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115 |
> | DEL-10-02-REQ-009 | Protected-path enforcement must uphold K-DOMAIN-2 on the applicable execution path. Codex uses the user-selected policy; no policy label proves profile-path quarantine. Verify forbidden writes fail and approved proposal writes remain allowed with named fixtures; this live-path evidence is outstanding, not a renewed owner choice on fixed supplier policy. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2 |
> | DEL-10-02-REQ-010 | Accepted glob syntax and enforcement semantics remain TBD. Profile path blocks exist; D-APP-58 assigns `_DomainEngines/profiles/<profileId>.adapter.yaml` and `domain-engine-adapter-manifest/v1`. Manifest instances and validation remain engine-side future work. | `docs/PRD.md` §8.17 FR-108; `docs/TYPES.md` §11.1 |
> | DEL-10-02-REQ-011 | Future acceptance evidence shall include a proof slot showing that direct protected-path writes fail closed and cannot be performed by ordinary agent tools. P3 disposition: F-001 and X-001 incorporated as future evidence criteria. | `docs/CONTRACT.md` §1.6 K-PERM-2, §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110 |
> | DEL-10-02-REQ-012 | Future acceptance evidence shall include proof slots for proposal-path write allowance and accepted mutation through an approved adapter or operation workflow plus explicit human gate. P3 disposition: F-002 and D-002 incorporated as future workflow evidence criteria. | `docs/PRD.md` §8.17 FR-111, FR-113; `docs/SPEC.md` §18 |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Source | Applicability |
> |---|---|
> | `docs/CONTRACT.md` §1.10 | Binding invariants K-DOMAIN-1 through K-DOMAIN-4. |
> | `docs/PRD.md` §8.17 | Future domain compatibility requirements FR-106 through FR-115; retain the accepted reference basis and current observed drift under D-APP-38 |
> | `docs/PRD.md` §10.10 | Future domain artifact categories and protected mutation route. |
> | `docs/SPEC.md` §18 | Provisional endpoint boundary and future profile requirements. |
> | `docs/TYPES.md` §11 | Vocabulary for `DomainEngineProfile`, `OperationProposal`, protected path, agent-writable path (including proposal paths), deterministic adapter, boundary notice, and OpenPipeStress fixture. |
> | `docs/PLAN.md` R7 | Roadmap placement and acceptance posture for future domain profiles and operation proposals. |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement | Verification Approach |
> |---|---|
> | DEL-10-02-REQ-001 | Review text for future-boundary language and absence of implementation activation. |
> | DEL-10-02-REQ-002, DEL-10-02-REQ-003 | Confirm definitions match `docs/TYPES.md` §11.3. |
> | DEL-10-02-REQ-004, DEL-10-02-REQ-005 | Confirm policy distinguishes protected model truth from proposal/summarization outputs. |
> | DEL-10-02-REQ-006 | Confirm accepted mutation route includes approved adapter or operation workflow and explicit human gate. |
> | DEL-10-02-REQ-007, DEL-10-02-REQ-008 | Confirm professional-boundary and solver-truth separation language is present. |
> | DEL-10-02-REQ-009 | Named live-path denial/allowance fixtures must demonstrate the preserved obligation; design unspecified hook details within the owning implementation brief and F-APP-3 gate. |
> | DEL-10-02-REQ-010 | Compare adopted profile path blocks and D-APP-58 manifest convention; keep glob syntax and manifest-instance verification outstanding. |
> | DEL-10-02-REQ-011 | Future validation fixture or equivalent review evidence confirms direct protected writes are denied or routed away from mutation and fail closed. |
> | DEL-10-02-REQ-012 | Future validation fixture or equivalent review evidence confirms proposal-path writes remain allowed as non-binding artifacts and accepted mutation requires the approved route plus human gate. |
>

### CLM-013 — Documentation

> ##### Documentation
>
> Required artifacts for this deliverable:
>
> - Protected/proposal path policy.
> - Hook implications.
> - Examples.
>
> Current documentation gaps:
>
> - Accepted glob syntax and its enforcement fixtures remain TBD; ADOPTED profile path examples exist.
> - Adapter manifest instances and their loader/validation remain engine-side future work under D-APP-58; location and schema identity are assigned.
> - ResponsibleParty remains TBD by dispatch instruction and `_CONTEXT.md`.
> - Future test fixture categories remain TBD until the governed `DomainEngineProfile` syntax and operation workflow are accepted: direct protected-write denial, proposal-path write allowance, and accepted mutation through human gate. P3 disposition: F-002 and X-002 incorporated as future slots.

- **AC-001** — The DEL-10-02 protected/proposal path policy, hook implications, and examples preserve the substantive source obligations and remain bounded to SOW-068 and OBJ-010.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-10-02 Protected Path and Proposal Path Policy

> #### Procedure: DEL-10-02 Protected Path and Proposal Path Policy
>
> REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-015 — Purpose

> ##### Purpose
>
> Define a repeatable procedure for producing and reviewing the protected path and proposal path policy without activating domain-engine implementation. The procedure preserves the future-boundary posture of PKG-10 and keeps protected domain-engine model truth separate from agent-writable proposal outputs.
>

### CLM-016 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Source |
> |---|---|
> | Deliverable context for DEL-10-02 | Available in `_CONTEXT.md`. |
> | Decomposition entry for DEL-10-02 and SOW-068 | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`. |
> | Domain invariants | Available in `docs/CONTRACT.md` §1.10. |
> | Future domain requirements | Available in `docs/PRD.md` §8.17 and §10.10, with accepted reference basis and current observed hash status preserved separately under D-APP-38 |
> | Future profile vocabulary | Available in `docs/TYPES.md` §11. |
> | Declared upstream dependencies | Read `Dependencies.csv`: profile prerequisite SATISFIED; operation-workflow interface NOT_APPLICABLE; DEP-10-02-005 glob/hook constraint remains TBD. The descriptive index changes no formal edge. |
> | ResponsibleParty | TBD. |
>

### CLM-017 — Steps

> ##### Steps
>
> 1. Confirm the work remains future-boundary scope.
>    - Check that the policy does not implement current-release domain operation execution or activate `/api/domain/*` endpoints.
>    - Source: `docs/PRD.md` §8.17; `docs/SPEC.md` §18.
>
> 2. Define policy terms from authoritative vocabulary.
>    - Use `Protected path` as an authoritative domain-engine artifact path not directly writable by agents.
>    - Use `Agent-writable path` for profile-approved proposal, summary, review-aid, checklist, TBD-register and reconciliation-note folders; proposal paths are a subset.
>    - Source: `docs/TYPES.md` §11.3.
>
> 3. State the protected write quarantine.
>    - Require direct agent writes to protected domain paths to be denied or routed through the future approved adapter / operation workflow.
>    - Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110.
>
> 4. State the proposal write allowance.
>    - Permit agents to write proposals, summaries, and review aids to declared proposal paths.
>    - Do not treat those outputs as accepted protected state.
>    - Source: `docs/PRD.md` §8.17 FR-111; `docs/TYPES.md` §11.3.
>
> 5. State the accepted mutation path.
>    - Require an approved adapter or operation workflow and explicit human gate before protected domain state changes.
>    - Source: `docs/PRD.md` §10.10; `docs/SPEC.md` §18.
>
> 6. Capture hook implications without over-specifying implementation.
>    - Record that future enforcement must distinguish protected paths from proposal paths and fail closed for direct protected writes.
>    - Mark exact hook API, path glob syntax, and adapter manifest behavior as TBD unless supplied by a future accepted profile contract.
>    - Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-108.
>
> 7. Add boundary-notice requirements.
>    - Confirm the policy prevents domain-engine outputs from being represented as professional approval, code compliance, external validation, or solver truth owned by Chirality.
>    - Source: `docs/PRD.md` §8.17 FR-115; `docs/CONTRACT.md` §1.10 K-DOMAIN-4.
>
> 8. Review examples.
>    - Include only category examples supported by sources unless profile-specific path patterns are later accepted.
>    - Cite the ADOPTED OpenPipeStress and PEC path blocks; keep only unsupported matching/enforcement semantics TBD.
>    - Source: `docs/PRD.md` §8.17 FR-114; `docs/TYPES.md` §11.3.
>

### CLM-018 — Verification

> ##### Verification
>
> | Check | Pass Criteria |
> |---|---|
> | Future-boundary check | No current-release domain engine execution is activated or implied. |
> | Terminology check | Protected and agent-writable path definitions (with proposal paths as a subset) match `docs/TYPES.md` §11.3. |
> | Write-quarantine check | Protected domain paths are not agent-writable in policy text. |
> | Proposal-path check | Agent-writable outputs use profile-approved paths for proposals, summaries, review aids, checklists, TBD registers and reconciliation notes; none is accepted domain truth. |
> | Human-gate check | Accepted protected-state mutation requires explicit human acceptance. |
> | Boundary-copy check | No text says Chirality approves, validates, certifies, or owns solver truth. |
> | TBD check | Concrete path patterns, hook implementation details, and engine-specific examples remain TBD where unsupported. |
> | Future fixture check | Future verification records include categories for direct protected-write denial, proposal-path write allowance, and accepted mutation through human gate once profile syntax and workflow are accepted. P3 disposition: F-002 incorporated. |
>

### CLM-019 — Records

> Policy and requirements: ScopeOfWork CLM-003/010; enforcement implications: CLM-012/017/024; examples/conflicts: CLM-025/026. Dependency selection remains governed by `Dependencies.csv` and the accepted DepClosure; this descriptive index supplies no new acceptance. Current reference drift is in `_REFERENCES.md`; current enforcement evidence is outstanding in Remaining.

- **VER-001** — Review the current ScopeOfWork claims and output matrix against their cited requirements and retained gates. Historical conversion/parity evidence is recovered in `R5/CONVERSION_EVIDENCE_REVIEW.csv` of RUN_D128_CONCORDANCE_2026-09-21_1614Z; it proves the dated conversion only. Current reconciliation uses W10_CHANGES.csv and independent changed-block review; product and human-acceptance checks remain separately required.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-10-02 Protected Path and Proposal Path Policy

> #### Guidance: DEL-10-02 Protected Path and Proposal Path Policy
>
> REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-021 — Purpose

> ##### Purpose
>
> DEL-10-02 exists to define a future security boundary for domain-engine filesystem interaction: agents may write proposals, summaries, and review aids, but they must not write protected domain-engine model truth. This supports OBJ-010 while keeping PKG-10 in future-boundary scope. Sources: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-10-02; `docs/PRD.md` §8.17.
>

### CLM-022 — Principles

> ##### Principles
>
> 1. **Future-boundary first.** Treat this policy as compatibility design for a governed future amendment, not as permission to activate domain-engine execution now. Source: `docs/PRD.md` §8.17; `docs/SPEC.md` §18.
> 2. **Protected truth stays protected.** Protected paths hold authoritative domain-engine artifacts and are not directly writable by agents. Source: `docs/TYPES.md` §11.3; `docs/CONTRACT.md` §1.10 K-DOMAIN-2.
> 3. **Proposals are non-binding work products.** Proposal paths may hold proposed changes, summaries, or review aids, but they do not become accepted protected domain state without the future workflow. Source: `docs/TYPES.md` §11.3; `docs/PRD.md` §8.17 FR-111.
> 4. **Accepted mutation needs a gate.** Any accepted mutation of protected domain state must flow through an approved adapter or operation workflow and explicit human gate. Source: `docs/PRD.md` §10.10; `docs/SPEC.md` §18.
> 5. **Chirality does not become the solver.** Domain engines own authoritative domain truth; Chirality governs interaction, proposals, records, and human gates. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-1; `docs/PRD.md` §8.17 FR-106.
> 6. **Boundary copy matters.** Domain-engine outputs must not be presented as professional approval, code compliance, external validation, or solver truth owned by Chirality. Source: `docs/CONTRACT.md` §1.10 K-DOMAIN-4; `docs/PRD.md` §8.17 FR-115.
>

### CLM-023 — Considerations

> Use the existing `DomainEngineProfile` contract and the ADOPTED OpenPipeStress/PEC `protected_write_paths` and `agent_writable_paths` declarations. Accepted glob syntax and the actual live enforcement integration remain unfinished. D-APP-58 supplies the manifest convention, not an instance or loader. Preserve generic policy and non-binding proposal output; solver assumptions belong in profile/adapter layers. Verify current reference drift under D-APP-38 without replacing accepted expected hashes.

### CLM-024 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance | Source |
> |---|---|---|
> | Proposal usability vs protected-state safety | Permit agent-authored proposals and summaries, but deny direct protected model writes. | `docs/PRD.md` §8.17 FR-110, FR-111 |
> | Generic profile policy vs engine-specific convenience | Keep policy generic until profile contract and fixture adoption are accepted. | `docs/PRD.md` §8.17 FR-107, FR-114 |
> | Prompt guidance vs runtime enforcement | Do not rely on prompt text alone for protected path denies; live execution needs demonstrated protected-write denial and permitted proposal writes. D-GOV-43 user-selected Codex policy is not proof of universal domain-path enforcement; retain the delivery gap and F-APP-3 gate. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; `docs/PRD.md` §8.17 FR-110 |
> | Review velocity vs human authority | Require explicit human acceptance before applying domain operations. | `docs/PRD.md` §8.17 FR-113; `docs/SPEC.md` §18 |
>

### CLM-025 — Examples

> ##### Examples
>
> Supported example categories:
>
> - Agent writes a proposed domain change package, summary, or review aid to a proposal path. Source: `docs/TYPES.md` §11.3; `docs/PRD.md` §8.17 FR-111.
> - Agent direct write to a protected model path is denied or routed to a proposal workflow. Source: `docs/PRD.md` §8.17 FR-110; `docs/PRD.md` §10.10.
> - ADOPTED OpenPipeStress and PEC profiles provide concrete path examples; declarations alone are not enforcement evidence. Source: `docs/PRD.md` §8.17 FR-114.
>

### CLM-026 — Conflict Table (for human ruling)

> CT-001/CT-003/CT-004: old PRD warning and owner-selection wording concerned historical source snapshots. Current reference drift is recorded under D-APP-38 while accepted expected hashes stay fixed; no repeat owner choice is created by metadata lag. CT-002: concrete profile path blocks exist. Accepted glob syntax and named denial/allowance fixture evidence remain outstanding under DEP-10-02-005 and F-APP-3; do not confuse this record repair with enforcement completion.

### CLM-027 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-149 acknowledges concrete path blocks in ADOPTED profiles while retaining accepted-glob syntax and hook API as TBD/gated.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-068 OBJ-010 | CLM-008 | AC-001 | VER-001 | Historical conversion mapping; current claim-block review and applicable named verification evidence |

## Retired status detail (2026-09-23)

These clauses retain the operative meaning of the named App `Remaining` entries after their one-time retirement. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R090:** The glob/protected-path semantics and negative fixtures need an accepted DEL-10-02/Runtime stage contract before live exposure. The specific unresolved policy choice is deferred in App Task Management.

- **APP-R091:** Manifest instances, loader and validation belong to the tier-0 bridge under D-APP-58. App integration must consume the accepted instance and does not create or accept tier-0 work.
