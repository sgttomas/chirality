---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-04
package_id: PKG-08
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-063, SOW-083]
package_objective_refs: [OBJ-005, OBJ-007]
---

# Scope of Work — DEL-08-04

## Purpose and Objective Traceability

This Scope of Work defines `DEL-08-04` in service of project scope [SOW-063, SOW-083] and package objectives [OBJ-005, OBJ-007].

- **OUT-001** — The managed-delegation admission bridge for DEL-08-04, including `delegate_agent`, fail-closed governance evaluation, parent-relative hierarchy checks, restricted child tools/cwd, and the DEL-08-05 handoff interface.
- **OUT-002** — The dated 2026-09-03 v3.0.0-rc.1 carrier outputs assigned to `DEL-08-04` by the applied decomposition row (`execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` line 357 at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`): App project-authority and managed-delegation bridge; daemon-client dispatch; class-aware `subagent-governance` behavior; managed sibling-overlap checks; role/native-origin fixtures; sealed-brief, containment, approval, cancellation, and cleanup conformance tests. Traceable to SOW-063 and OBJ-005, OBJ-007.

## SCA-APP-010 Gate-5 Current Contract (Controlling)

The owner-approved SCA-APP-010 amendment (Gate 3 approved, Gate 5 applied
2026-09-04 at content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, merged
as `7795b0972cac147869607d994173753e4a2fc232`; active pointer moved as
`311a2f0b811d55315d6eb623130cad0be1417565`) makes the centre dialogue the
invariant primary surface and seats the prompted specification ladder. Where any
earlier current-contract section or older clause in this document disagrees with
the applied row below, this section controls. Earlier sections, clauses, and
evidence remain dated compatibility history and are not deleted.

### Current responsibility

`DEL-08-04 Type 2 Subagent Governance Bridge` (BACKEND_FEATURE_SLICE, applied decomposition row L371):

Apply the current Root/App four-role graph: HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS may enter directly; TASK is delegated and cannot delegate. The App-owned Runtime carries managed delegation, while delegated-harness-native descendants remain a distinct class. Enforce managed hierarchy, named allowlist or declared generalist policy, sealed brief, approvals, context/cwd/tool/write boundaries, active-sibling write-overlap fail-close, cancellation/cleanup and class-aware routing. Native descent does not infer a managed role; record its actual parentage, supplied basis, host enforcement limits and return. Honour the per-chat delegation policy (`none` by default) as a narrowing input. The older Agent 0/1/2 and daemon-client wording in the applied row is dated carrier history; CLM-033 retains its exact provenance.

Applied row notes (dated decomposition history): Project authority/client-dispatch slice; daemon owns
operational managed delegation and Root owns delegated-harness-native semantics.
The D-APP-74 exclusion remains historical and tranche-scoped to SCA-APP-004;
this v3 carrier prospectively supersedes it without retroactive edit. D-GOV-35
is necessary but App carrier acceptance and WP-03/05 fixtures remain required.

Applied row outputs (dated decomposition history): App project-authority and managed-delegation bridge;
daemon-client dispatch; class-aware `subagent-governance` behavior; managed
sibling-overlap checks; role/native-origin fixtures; sealed-brief, containment,
approval, cancellation, and cleanup conformance tests.

### Current acceptance obligations

1. The Chirality-managed delegation bridge enforces managed hierarchy, named allowlist or declared generalist policy, sealed brief, approvals, context/cwd/tool/write boundaries, active-sibling write-overlap fail-close, cancellation and cleanup, and class-aware routing; native descent does not infer a managed role.
2. The per-chat delegation policy carried with the session (`none` by default) is honoured as a narrowing input to managed delegation and adds no delegation class.
3. Current role entry follows the Root/App four-role instructions; record actual host enforcement limits and evidence provenance for managed and native descendants. WP-03/05 fixtures and D-GOV-35 remain required for class-aware paths; older posture labels are historical carrier evidence.

### Seating and rulings

Remaining items seated under D-APP-108 (2026-09-04): DEL-08-04-V3-02. Ruled
questions applied here: none beyond SR-24. Alignment writes WI-061, WI-062,
WI-063, WI-064, WI-065 performed in run `APP_SCA_APP_010_SEATING_2026-09-04`;
dependency writes DEP-025, DEP-026 await the registered dependency-extract pass
after owner acceptance of this alignment. No lifecycle, Checking Approval SHA,
dependency-acceptance, product, or release act is implied.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-08-04 Type 2 Subagent Governance Bridge

> #### Datasheet: DEL-08-04 Type 2 Subagent Governance Bridge
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-08-04 |
> | DeliverableName | Type 2 Subagent Governance Bridge |
> | PackageID | PKG-08 |
> | PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | CoversScopeItems | SOW-063, SOW-083 |
> | SupportsObjectives | OBJ-005, OBJ-007 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Requirement | Authority / verification hook |
> |---|---|---|
> | Managed admission | A managed child requires an eligible direct parent/child relation, a sealed bounded brief, declared context/cwd/tools/write targets, applicable approval references and fail-closed admission. | D-APP-68 disposition 4; SCA-APP-010 current contract; `frontend/src/__tests__/lib/managed-delegation.test.ts` (legacy evidence). |
> | Current role relation | HELP_HUMAN may coordinate managers or dispatch bounded Type 2 work directly; HELPS_HUMANS and WORKING_ITEMS may dispatch TASK or an allowed ephemeral Type 2 instance; Type 2 does not delegate. | Current Root `AGENTS.md` Roles and App `AGENTS.md` Active Roles; role-basis evidence must identify origin and hash. |
> | Delegation class | Chirality-managed execution and delegated-harness-native descent retain their distinct admission/evidence semantics; native descent alone assigns no Chirality role or approval. | D-GOV-35; SCA-APP-010; `projects/chirality-runtime/tests/native-event-adapter.test.ts` (repository-relative). |
> | Authority ceiling | Role instructions, the bounded brief and actual host enforcement jointly limit execution. A child cannot acquire authority from a UI label, model choice, parent narrative or a compatibility module. | Root/App `AGENTS.md`; D-GOV-43/D-APP-127; named managed/native verification must state enforcement limits. |
> | Record handoff | Preserve actual parentage, supplied basis, scope, admission/approval evidence and return/artifact linkage for DEL-08-05. | DEL-08-05 CLM-037; `frontend/src/__tests__/lib/managed-delegation.test.ts` and Runtime native-event evidence. |
>
> The former `evaluateSubagentGovernance` function and App-harness `delegate_agent` implementation are retained compatibility evidence. Neither is asserted to be the live Codex admission path. Missing live managed admission, scope enforcement and record integration remain work; this repair does not close them or accept D-GOV-42's exact bytes.

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value |
> |---|---|
> | PRD source status | `docs/PRD.md` is historically reconciled under D-APP-38; verify current bytes; PRD-derived subagent governance details are accepted for this tranche. |
> | Sequencing | PLAN R5 places governed subagent runtime after earlier runtime, permission, hook, and tool-governance work. |
> | Scope boundary | This deliverable covers `delegate_agent` admission, fail-closed governance, parent-relative hierarchy eligibility, and the disabled legacy-bridge boundary. Persistent parent-child run records are DEL-08-05. |
> | Authority boundary | D-GOV-14 item 7 retires the record-less SDK `Agent` bridge. Chirality-owned managed sessions, governance, permission, audit, and runtime contracts control executable delegation. |
> | Dependency boundary | Existing Dependencies.csv rows and the accepted closure pointer control selectability. Legacy SDK-probe and hook targets are historical evidence; refresh their formal applicability only through the owning dependency process. |
>

### CLM-005 — Construction

> ##### Construction
>
> Required construction is a verifiable admission boundary and a class-aware handoff, not a named function call. It must preserve eligible parent/child relations, sealed context, required approval references, declared scope, restricted execution, managed sibling-overlap denial, cancellation/cleanup and the DEL-08-05 record interface. The record-less SDK `Agent` bridge remains retired; native Codex descendants are a distinct permitted class, not a revival of that bridge.
>
> | Evidence surface | Use and limit |
> |---|---|
> | `frontend/src/__tests__/lib/managed-delegation.test.ts` | Managed-admission, hierarchy, context, scope and coordination compatibility evidence. |
> | `frontend/src/__tests__/lib/sdk-options-builder.test.ts`; `frontend/src/__tests__/lib/permission-overlay.test.ts` | Evidence that the retired SDK Agent bridge is not exposed or used as a fallback. |
> | `projects/chirality-runtime/tests/native-event-adapter.test.ts` (repository-relative) | Native child identity and activity evidence; it does not prove managed sealed-brief admission. |
> | DEL-08-05 class-aware record verification | Required return/artifact linkage; completeness must be checked against the actual delegation class. |
>
> The legacy implementation lives under `frontend/src/lib/harness/`; its tests do not qualify the live Codex path.

### CLM-006 — References

> ##### References
>
> | RefID | Source | Status |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | historical D-APP-38 source state; verify current candidate bytes |
> | REF-002 | `docs/CONTRACT.md` | historical D-APP-38 source state; verify current candidate bytes |
> | REF-003 | `docs/SPEC.md` | historical D-APP-38 source state; verify current candidate bytes |
> | REF-004 | `docs/TYPES.md` | historical D-APP-38 source state; verify current candidate bytes |
> | REF-005 | `docs/PLAN.md` | historical D-APP-38 source state; verify current candidate bytes |
> | REF-006 | `docs/PRD.md` | historical D-APP-38 source state; verify current candidate bytes|
> | REF-007 | `../../workflows/software-decomp/WORKFLOW.md` | historical D-APP-38 source state; verify current candidate bytes |
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-135/136 record the landed `SubagentGovernanceDecision`, preflight `safeMetadata`, and `ChildRunRecord` shapes plus implementation/test paths; only the separately gated approval-reference question remains open. UPD-137 aligns DEP-08-04-003 to that contract.

### CLM-033 — Applied decomposition v3 carrier assignment (SCA-APP-008 Gate 5, 2026-09-03)

> ##### Applied decomposition row for DEL-08-04 at commit `d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f`
>
> The accepted SCA-APP-008 Gate-5 application (PR #662) amended this deliverable's row. The row text below is transcribed verbatim as dated 2026-09-03 provenance. Current four-role applicability and App-owned Runtime topology follow later Root/App instructions, D-GOV-43/D-APP-127 and D-APP-131; the verbatim row does not revive its older role or daemon mechanism.
>
> | Column | Applied row text |
> |---|---|
> | Description | Remain the Chirality-managed delegation bridge and prospectively carry multi-child managed execution plus the root `AGENTS.md` Agent 0/1/2 graph for v3 work, while consuming delegated-harness-native descent as a distinct Root-originated class. Enforce managed hierarchy, named allowlist or declared generalist policy, sealed brief, approvals, context/cwd/tool/write boundaries, active-sibling write-overlap fail-close, cancellation/cleanup, and class-aware routing; native descent assigns no Agent 0/1/2 role. Agent 0/1/2 role entry is offered for Codex sessions, with Agent 2/TASK labelled `role not mechanically enforced` and governed evidence marked `instruction-asserted` when G-ROLE cannot mechanically prove non-delegation. |
> | Principal outputs | App project-authority and managed-delegation bridge; daemon-client dispatch; class-aware `subagent-governance` behavior; managed sibling-overlap checks; role/native-origin fixtures; sealed-brief, containment, approval, cancellation, and cleanup conformance tests |
> | Notes | Project authority/client-dispatch slice; daemon owns operational managed delegation and Root owns delegated-harness-native semantics. The D-APP-74 exclusion remains historical and tranche-scoped to SCA-APP-004; this v3 carrier prospectively supersedes it without retroactive edit. D-GOV-35 is necessary but App carrier acceptance and WP-03/05 fixtures remain required. |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-08-04 Type 2 Subagent Governance Bridge

> #### Specification: DEL-08-04 Type 2 Subagent Governance Bridge
>

### CLM-009 — Scope

> ##### Scope
>
> DEL-08-04 owns the App's managed-delegation admission and project-authority interface: bounded parent-relative eligibility, sealed context, applicable approvals, context/cwd/tool/write limits, sibling-overlap denial, cancellation/cleanup and fail-closed outcomes. It consumes delegated-harness-native descent as a distinct Root-owned class under the controlling SCA-APP-010 contract. Native descent alone is neither managed admission evidence nor a Chirality role assignment.
>
> The live App uses the Codex-hosted boundary under D-GOV-43/D-APP-127. The earlier App-harness function names and SDK bridge are compatibility/history evidence; the retired record-less SDK Agent bridge is not a permitted fallback. Preserve truthful `instruction-asserted` and `role not mechanically enforced` calibration where host evidence cannot prove a role constraint.
>
> Verification hooks are the managed-delegation and retired-bridge tests in CLM-005, paired with class-specific live-path evidence. Any missing managed admission, approval, restriction or record guarantee stays open; a native-child event is insufficient to close it.
>
> Excluded: general adapter implementation, DEL-08-05's full parent-child record/artifact persistence, dependency-register authoring and any change to Root native-delegation semantics. This carrier application does not grant lifecycle, release or D-GOV-42 exact-byte acceptance.

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-08-04-R01 | `delegate_agent` MUST call the Chirality governance/admission logic before any managed child session is created and MUST fail closed on rejection or error. | D-GOV-14 item 7; D-APP-68 disposition 4 |
> | DEL-08-04-R02 | Delegation MUST be denied unless the direct parent and proposed direct child satisfy the root hierarchy, the context is sealed, the pipeline run is approved, the approval reference is present, and all declared execution fields pass admission. | root `AGENTS.md`; D-APP-68 disposition 4 |
> | DEL-08-04-R03 | Delegation without governance metadata MUST be denied. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
> | DEL-08-04-R04 | Delegation to a non-allowlisted candidate MUST be denied. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
> | DEL-08-04-R05 | A proposed managed child MUST be denied when ineligible under the supplied current role basis. HELP_HUMAN may coordinate managers or dispatch bounded Type 2 work directly; HELPS_HUMANS and WORKING_ITEMS may dispatch TASK or an allowed ephemeral Type 2 instance; Type 2 cannot delegate. Preserve the actual scope and enforcement limits in verification evidence. | Current Root `AGENTS.md` Roles; App `AGENTS.md` Active Roles; bounded R5 Agent 0 application |
> | DEL-08-04-R06 | Chirality-managed child execution MUST satisfy managed admission; delegated-harness-native descent is a distinct class under D-GOV-35 and the controlling SCA-APP-010 contract. The record-less SDK `Agent` bridge MUST remain disabled and not model-visible. Neither native descent nor a compatibility implementation grants managed admission or a Chirality role. | D-GOV-35; D-GOV-43/D-APP-127; SCA-APP-010; D-GOV-14 item 7 retirement boundary |
> | DEL-08-04-R07 | Managed children MUST use explicit restricted tools, cwd, declared context, and write targets; they MUST NOT inherit or expand capabilities or authority beyond the direct parent and sealed brief. | `docs/CONTRACT.md` K-SUBAGENT-2; root `AGENTS.md` |
> | DEL-08-04-R08 | Admission, policy, path, or managed-child launch failures MUST fail closed. | D-GOV-14 item 7; root `AGENTS.md` |
> | DEL-08-04-R09 | The bridge MUST preserve Chirality-owned runtime semantics rather than treating SDK defaults, SDK transcript shape, SDK tool names, or SDK permission modes as product authority. | `docs/DIRECTIVE.md` Sections 7-8; `docs/PRD.md` Principles 9-10 |
> | DEL-08-04-R10 | Unknown values or unsupported facts in governance metadata MUST produce `TBD`, denial, or human-ruling-needed behavior rather than guessed allow decisions. | `docs/CONTRACT.md` K-INVENT-1; `docs/CONTRACT.md` K-CONFLICT-1 |
> | DEL-08-04-R11 | The bridge SHOULD expose a clear interface for DEL-08-05 to persist parent-child lifecycle records and output artifact references when execution is enabled. | `docs/CONTRACT.md` K-SUBAGENT-3; decomposition DEL-08-05 |
>

### CLM-011 — Governance Decision Contract

> Managed admission must preserve the decision and reason actually observed, decision source, applicable approval reference, eligible parent/child identity, sealed supplied basis, cwd/tools/write targets, and DEL-08-05 return linkage. These semantics are checkable through `frontend/src/__tests__/lib/managed-delegation.test.ts`; its selected serialized shape is retained compatibility evidence, not a current live-Codex admission guarantee.
>
> Native Codex descendants are a distinct D-GOV-35 class and do not imply managed admission. Record actual parentage, basis, scope, enforcement limits, decisions and return. D-APP-132 leaves the additional D-APP-117 per-attempt replay product unadopted; existing class-aware evidence duties continue. Missing live managed admission, sibling-overlap and per-chat policy evidence remains implementation/verification work.

### CLM-012 — Standards

> ##### Standards
>
> | Standard or contract | Applicability |
> |---|---|
> | `docs/CONTRACT.md` K-SEAL-1, K-GHOST-1, K-SUBAGENT-1, K-SUBAGENT-2, K-SUBAGENT-3 | Core subagent governance invariants. |
> | `docs/SPEC.md` Sections 14-15 | Tool surface, permission modes, and hook requirements. |
> | `docs/TYPES.md` Section 10 | Canonical subagent vocabulary and `evaluateSubagentGovernance` meaning. |
> | `docs/PLAN.md` R5 | Implementation sequencing, targets, and acceptance criteria. |
> | `docs/PRD.md` Section 8.15 | User/runtime behavior for governed delegation. |
> | `../../workflows/software-decomp/WORKFLOW.md` deliverable sizing rules | Confirms Type 2 deliverables are bounded executable units; no sub-task level should be invented. |
>

### CLM-013 — Verification

> ##### Verification
>
> Verification must identify the actual delegation class, selected role/instruction basis, source revision, exercised path and result. Preserve the managed R01–R11 obligations; legacy tests are evidence of the compatibility implementation, not proof of live Codex enforcement.
>
> | Obligation | Named evidence and required limit |
> |---|---|
> | R01–R05: pre-execution admission, sealed context, required approvals, allowlist/generalist policy and direct-parent eligibility | `frontend/src/__tests__/lib/managed-delegation.test.ts`. Record the current Root/App role basis; current HELP_HUMAN authority includes bounded direct Type 2 dispatch. Older Agent 0-to-Type 2 denial cases describe their historical policy, not the current role ceiling. |
> | R06: retired SDK bridge cannot execute as a fallback | `frontend/src/__tests__/lib/sdk-options-builder.test.ts`; `frontend/src/__tests__/lib/permission-overlay.test.ts`. Native Codex descent is evaluated separately under D-GOV-35. |
> | R07–R08: explicit scope, restricted execution, overlap denial, launch/policy failure, cancellation and cleanup | Managed-delegation fixtures plus actual live-path negative and allowed-path records are required. R3's missing launch-error/hook-failure and live-path coverage findings remain open. |
> | R09–R10: truthful authority boundary and unknown values | Managed-admission negative fixtures must show no guessed allow decision; native evidence must retain stock Codex events and distinguish observed capability from granted authority. |
> | R11: DEL-08-05 handoff | Class-aware record/replay evidence must preserve actual lineage, supplied basis and accepted artifact linkage. `projects/chirality-runtime/tests/native-event-adapter.test.ts` (repository-relative) checks native identity/activity only, not full managed-record closure. |
>
> Keep missing metadata, missing approval, unsealed context, ineligible child, non-allowlisted candidate, broad capability request, launch failure, audit-safe denial and allowed bounded execution as distinct checks. Do not infer mechanical sandbox/role enforcement from instructions or passing legacy fixtures.

### CLM-014 — Documentation

> ##### Documentation
>
> Required artifacts for this deliverable:
>
> - `evaluateSubagentGovernance` bridge;
> - managed-child resolution and admission logic;
> - `delegate_agent` tool-surface and legacy-bridge retirement tests;
> - denial/restriction fixtures;
> - handoff notes or typed interface for DEL-08-05 child-run persistence.
> - implementation path record naming managed delegation, legacy bridge, coordination registration, fixtures, runnable tests, and output evidence.
>

### CLM-015 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Source A | Source B | Issue | Proposed handling |
> |---|---|---|---|---|
> | C-001 | `_REFERENCES.md` REF-006 | D-APP-38 authority corpus | Former PRD source-state warning is resolved for this tranche. | Use PRD-derived subagent governance text under D-APP-38; keep implementation proof separate from source-state proof. |
>

### CLM-016 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-135/136 record the landed `SubagentGovernanceDecision`, preflight `safeMetadata`, and `ChildRunRecord` shapes plus implementation/test paths; only the separately gated approval-reference question remains open. UPD-137 aligns DEP-08-04-003 to that contract.

- **REQ-001** — The deliverable shall preserve managed multi-child delegation under the current Root/App four-role graph and App-owned Runtime, with TASK unable to delegate and actual host limits recorded.
- **REQ-002** — The deliverable shall consume delegated-harness-native descent as a distinct Root-originated class; native descent does not infer a managed Chirality role, and Root owns its native semantics.
- **REQ-003** — The bridge shall enforce managed hierarchy, named allowlist or declared generalist policy, sealed brief, approvals, context/cwd/tool/write boundaries, active-sibling write-overlap fail-close, cancellation/cleanup, and class-aware routing.
- **REQ-004** — Direct entry shall offer HELP_HUMAN, HELPS_HUMANS and WORKING_ITEMS; TASK is delegated. Record selected role, scope and mechanical enforcement limits truthfully for each managed/native class.
- **REQ-005** — The D-APP-74 exclusion remains historical and tranche-scoped to SCA-APP-004 and is prospectively superseded without retroactive edit; D-GOV-35 is necessary, but App carrier acceptance and WP-03/05 fixtures remain required before v3 delegation work.
- **AC-001** — The DEL-08-04 bridge requires current App-owned Runtime managed/native class checks for denial, restriction, allowed path, audit safety and DEL-08-05 handoff, bound to the candidate and actual host limits. Preserved legacy fixtures establish only their compatibility subjects for SOW-063 and OBJ-005, OBJ-007.
- **AC-002** — The v3 outputs assigned by the applied decomposition row (App project-authority and managed-delegation bridge through App-owned Runtime, class-aware descendant handling, managed sibling-overlap checks, role/native-origin fixtures, and sealed-brief, containment, approval, cancellation, and cleanup conformance tests) exist and satisfy REQ-001 through REQ-005 without inferring an Agent role from native descent.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-08-04 Type 2 Subagent Governance Bridge

> #### Procedure: DEL-08-04 Type 2 Subagent Governance Bridge
>

### CLM-018 — Purpose

> ##### Purpose
>
> Define the operational steps to produce and verify managed child-session admission through `delegate_agent`.
>

### CLM-019 — Prerequisites

> Use current `_STATUS.md`, Dependencies.csv and the accepted closure pointer rather than the P3 INITIALIZED/NO_STATUS_TOUCH snapshot. Named retained managed-admission evidence is in CLM-005/011. Live implementation requires the current Runtime interface and class-aware App handoff; native descendants are allowed under D-GOV-35 without reviving the disabled SDK Agent bridge. Required sealed context, scope, actor/approval and return evidence remains class-specific. D-APP-132 defers only the optional additional replay product.

### CLM-020 — Steps

> ##### Steps
>
> 1. Locate the existing `evaluateSubagentGovernance` implementation or define the narrow adapter contract that will call it.
> 2. Define the governance input required by the bridge: parent session identity, requested candidate agent, requested task scope, context-sealed indicator, pipeline approval indicator, approval reference, persona allowlist result, environment enablement, and requested child tool/cwd constraints.
> 3. Ensure every required input has a fail-closed default. Missing, malformed, or unknown values must deny or require human ruling.
> 4. Record the managed-delegation, legacy-bridge, coordination-registration, fixture, runnable-test, and evidence paths.
> 5. Resolve child eligibility relative to the current direct parent: HELP_HUMAN may coordinate managers or dispatch bounded TASK work; HELPS_HUMANS and WORKING_ITEMS may dispatch TASK or an allowed ephemeral Type 2 instance; TASK cannot delegate. Record actual selected role and host enforcement limits.
> 6. Apply explicit child restrictions, including declared context, tools, write targets, dependencies, output contract, and working directory.
> 7. Keep the record-less SDK `Agent` bridge disabled and absent from the model-visible tool surface.
> 8. Invoke the governance/admission bridge before managed child-session creation.
> 9. Deny execution when the bridge returns denial, when hook execution fails, or when the candidate/tool/cwd configuration cannot be verified.
> 10. Return structured denial reasons suitable for tests and audit records, with stable reason vocabulary and without sensitive prompt or environment leakage.
> 11. Provide handoff fields or callback points for DEL-08-05 to persist parent-child lifecycle records and output artifact paths when execution is enabled.
> 12. Add table-driven tests for all denial paths and for the allowed path with restricted child tools/cwd.
> 13. Add regression tests proving SDK defaults, inherited permissions, and `allowedTools` alone cannot authorize delegation.
>

### CLM-021 — Verification

> ##### Verification
>
> | Check | Expected result |
> |---|---|
> | Missing governance metadata | Denied; no managed child session. |
> | Missing approval reference | Denied; no managed child session. |
> | Unsealed context | Denied or human-ruling-needed; no ghost-input execution. |
> | Non-allowlisted candidate | Denied. |
> | Child type ineligible relative to direct parent | Denied. |
> | Hook error | Denied fail-closed. |
> | Child requests broad tools/cwd | Denied or narrowed to explicit approved restrictions before execution. |
> | Allowed governed request | `delegate_agent` may create a managed child only with a hierarchy-eligible child, sealed context, restricted tools/cwd, declared write targets, and handoff data for child-record persistence. |
> | Legacy SDK `Agent` bridge | Disabled and not model-visible; cannot execute or bypass managed-session records. |
> | Denial reason audit safety | Denial reason uses stable reason vocabulary and safe metadata; it preserves enough detail for review without prompt or environment leakage. |
> | Event/persistence handoff | DEL-08-05 can consume bridge/hook result metadata without DEL-08-04 owning full persistence. |
>

### CLM-022 — Records

> ##### Records
>
> The implementation should produce or update these records/artifacts:
>
> - bridge module or adapter for `evaluateSubagentGovernance`;
> - managed child resolver and admission bridge;
> - `delegate_agent` and legacy-bridge retirement tests;
> - denial fixtures for missing metadata, non-allowlisted candidate, direct-parent/child hierarchy mismatch, unsealed context, missing approval reference, launch error, and broad child capability request;
> - allowed-path fixture showing restricted tools/cwd;
> - handoff/interface note for DEL-08-05 child run record persistence.
> - implementation path record naming managed delegation, legacy bridge, coordination registration, fixtures, runnable tests, and evidence.
>
> Do not create or modify `Dependencies.csv` during this procedure. Use `_DEPENDENCIES.md` only as current dependency context until declared edges are accepted.

- **VER-001** — Review the complete preserved legacy source and execute its specified missing-metadata, approval-reference, unsealed-context, non-allowlisted, parent/child-hierarchy, launch-error, broad-capability, allowed-restricted-execution, audit-safety, and DEL-08-05 handoff checks; record concrete evidence.
- **VER-002** — Run the class-aware routing, managed sibling-overlap, role/native-origin, sealed-brief, containment, approval, cancellation, and cleanup conformance tests; confirm native descent does not infer a managed role and record actual selected role, scope and host enforcement limits. Older posture-label fixtures remain dated compatibility evidence.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-08-04 Type 2 Subagent Governance Bridge

> #### Guidance: DEL-08-04 Type 2 Subagent Governance Bridge
>

### CLM-024 — Purpose

> ##### Purpose
>
> This deliverable exists to admit managed child sessions while keeping delegation under Chirality governance. `delegate_agent` may create a child only when the product-owned gate allows the request, the child is eligible relative to its direct parent, context is sealed, approvals are traceable, and capabilities are bounded by the declared scope. The SDK `Agent` bridge is not an executable fallback.
>

### CLM-025 — Principles

> ##### Principles
>
> | Principle | Guidance |
> |---|---|
> | Deny first | Treat any missing governance metadata, unknown candidate status, hook error, unsealed context, missing approval reference, or unsupported state as denial or human-ruling-needed. Do not infer permission from SDK defaults. |
> | Chirality owns semantics | `delegate_agent`, managed-session records, public runtime contracts, audit events, and governance decisions remain Chirality-owned; the SDK `Agent` tool is not model-visible. |
> | Parent-relative hierarchy | Current HELP_HUMAN may coordinate managers or dispatch bounded TASK work directly; HELPS_HUMANS and WORKING_ITEMS may dispatch TASK or allowed ephemeral Type 2 work; TASK does not delegate. Eligibility remains relative to the direct parent, with actual host limits recorded. |
> | No capability inheritance by accident | A managed child receives explicit declared context, tools, write targets, and cwd. It does not inherit parent capabilities implicitly or broaden parent authority. |
> | Sealed context only | Managed child context is limited to the sealed brief and declared references. Avoid "ghost inputs" that are not in the sealed brief or declared sources. |
> | Approval is evidence, not vibes | The approval reference must be non-empty and traceable to human/gate evidence. Until the accepted format is selected, the bridge should treat absent, ambiguous, mutable, or SDK-only approval data as denial or human-ruling-needed. |
> | Separate gate from record persistence | This slice owns bridge and hook behavior. Full parent-child record persistence and output artifact-path storage should be handed to DEL-08-05 through a clear interface. |
>

### CLM-026 — Considerations

> ##### Considerations
>
> - The PLAN places governed subagent runtime after earlier engine, permission, tool, hook, and result-storage work. If those prerequisites are absent or unstable, the bridge should remain disabled or deny execution.
> - `allowedTools` alone is not a restriction boundary. Restrictions require disallowed tools, permission mode, hooks, and overlay policy.
> - Hook failures fail closed for subagent actions. This should include bridge exceptions, missing policy inputs, malformed approval references, and failed candidate resolution.
> - The candidate resolver should prefer explicit `AGENT_TYPE: 2` and task-agent metadata. If an instruction file is ambiguous, classify it as ineligible until a human or conformance validator resolves it.
> - Child cwd should be the approved bounded working root for the task, not the instruction root and not a broad ambient workspace.
> - The bridge should produce denial reasons suitable for audit and tests without leaking sensitive prompt or environment data.
> - REF-006 is historically reconciled under D-APP-38; verify current bytes. PRD-derived delegation behavior remains traceable to PRD text, while implementation proof remains separate.
>

### CLM-027 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Preferred direction |
> |---|---|
> | Convenience vs. safety | Prefer denial over opportunistic delegation when governance metadata is incomplete. |
> | Provider-native shape vs. product contract | Keep provider fields behind Chirality types so adapter changes do not redefine managed-delegation behavior. |
> | Broad child capability vs. bounded execution | Prefer narrow child tool/cwd definitions generated from the approved Type 2 task scope. |
> | Bridge-only scope vs. record persistence | Keep this deliverable focused on gate/hook/definition behavior and expose a minimal handoff to DEL-08-05 for lifecycle records. |
>

### CLM-028 — Examples

> ##### Examples
>
> | Scenario | Expected outcome |
> |---|---|
> | Delegation request lacks approval reference | Denied before managed child creation. |
> | Delegation request includes only an SDK transcript path or mutable UI label as approval evidence | Denied or human-ruling-needed until the accepted approval-reference format is selected. |
> | HELP_HUMAN requests bounded TASK work directly | Eligible for further sealed-brief and policy checks under current Root role instructions. |
> | HELPS_HUMANS or WORKING_ITEMS requests an allowed TASK or ephemeral Type 2 child | Eligible for further sealed-brief and policy checks. |
> | TASK requests any child | Denied; TASK cannot delegate. |
> | Context is not sealed or includes undeclared references | Denied or human-ruling-needed; do not execute with ghost inputs. |
> | Child tool list requests write/bash beyond approved scope | Denied or reduced to explicit approved tools; do not inherit parent capability. |
> | Hook throws during governance evaluation | Denied with fail-closed hook outcome. |
>

### CLM-029 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Impact | Human ruling needed |
> |---|---|---|---|
> | C-001 | Former REF-006 PRD source-state warning resolved by D-APP-38. | PRD-derived delegation behavior is accepted for this tranche. | No additional ruling required for source-state status. |
>

### CLM-030 — Open Items

> The retained managed implementation and tests are named in CLM-005; their serialized shape is evidence, not an unresolved naming decision. Current work is live managed admission and class-aware DEL-08-05 handoff, scope/sibling-overlap protection, cancellation/cleanup, policy application and actual return evidence on the App-owned Runtime/Codex path. Optional D-APP-117 per-attempt replay is not adopted for this undertaking under D-APP-132 and is deferred to its future adoption/implementation gate. Required existing evidence is not deferred with it.

### CLM-031 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-135/136 record the landed `SubagentGovernanceDecision`, preflight `safeMetadata`, and `ChildRunRecord` shapes plus implementation/test paths; only the separately gated approval-reference question remains open. UPD-137 aligns DEP-08-04-003 to that contract.

### CLM-032 — D-APP-68 managed-delegation refresh (2026-07-19)

> ##### D-APP-68 managed-delegation refresh (2026-07-19)
>
> D-GOV-14 item 7 retires the record-less SDK `Agent` bridge after managed-delegation acceptance. `delegate_agent` managed child sessions are the sole executable app-harness delegation path, and the SDK `Agent` tool is disabled and not model-visible. Child eligibility is parent-relative under root `AGENTS.md`: Agent 0 → named Agent 1; Agent 1 → allowed Agent 2; Agent 2 → no delegation. DEL-08-04 owns admission and delegation; DEL-08-05 owns the resulting managed-child lifecycle, parent/scope linkage, records, and artifacts. The separately gated per-attempt decision-replay artifact remains gated and is not authorized by D-APP-68.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-063 OBJ-005 OBJ-007 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
| OUT-002 | SOW-063 OBJ-005 OBJ-007 | CLM-033 REQ-001 REQ-002 REQ-003 REQ-004 REQ-005 | AC-002 | VER-002 | Class-aware routing and overlap fixtures; role/native-origin fixtures; conformance test evidence bound to the WP-03/05 fixtures they consume |
