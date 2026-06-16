# Source Pack: SRC-DEL-DEL-08-04-TYPE-2-SUBAGENT-GOVERNANCE-BRIDGE

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/Datasheet.md

### Datasheet: DEL-08-04 Type 2 Subagent Governance Bridge

#### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-08-04 |
| DeliverableName | Type 2 Subagent Governance Bridge |
| PackageID | PKG-08 |
| PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| Type | BACKEND_FEATURE_SLICE |
| ResponsibleParty | TBD |
| ContextEnvelope | M |
| CoversScopeItems | SOW-063 |
| SupportsObjectives | OBJ-005, OBJ-007 |

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary function | Bridge fail-closed subagent governance to SDK agents with allowlists, sealed context, approval refs, and restricted child tools/cwd. | `_CONTEXT.md`; decomposition DEL-08-04 |
| Governance gate | `evaluateSubagentGovernance` is the authoritative fail-closed gate for delegation. | `docs/TYPES.md` Section 10; `docs/PLAN.md` R5 |
| SDK integration point | SDK `agents` definitions generated from allowed Type 2 task-agent instructions. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| Hook integration point | `Agent` tool hook calls `evaluateSubagentGovernance` and fails closed. | `docs/PLAN.md` R5; `docs/SPEC.md` Section 15.2 |
| Child execution constraints | Child tool lists and working directory are restricted; child runs must not inherit or expand parent capabilities. | `docs/CONTRACT.md` K-SUBAGENT-2 |
| Required governance inputs | Environment enablement, persona allowlist, context sealing, pipeline approval, approval reference, and Type 2 eligibility. | `docs/CONTRACT.md` K-SUBAGENT-1; `docs/PRD.md` Section 8.15 |
| Acceptance denials | Delegation without governance metadata is denied; delegation to a non-allowlisted or non-Type-2 candidate is denied. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| Related child-record behavior | Parent session records child lifecycle and output reference when execution support exists. | `docs/PLAN.md` R5; decomposition DEL-08-05 |

#### Conditions

| Condition | Value |
|---|---|
| PRD source status | Source warning: REF-006 has expected SHA `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34` and observed SHA `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`; dispatch instructed this is not a blocker. |
| Sequencing | PLAN R5 places governed subagent runtime after earlier runtime, permission, hook, and tool-governance work. |
| Scope boundary | This deliverable covers the governance bridge, SDK agent definitions, and `Agent` hook tests. Persistent parent-child run records are primarily DEL-08-05. |
| Authority boundary | SDK subagent mechanics are an implementation substrate; Chirality-owned governance, permission, audit, and runtime contracts control product semantics. |
| Dependency boundary | Declared upstream/downstream dependency lists remain `TBD`; the current extracted register records ACTIVE execution prerequisites for the source corpus, `evaluateSubagentGovernance` contract, permission/hook infrastructure, DEL-04-01 SDK probe, and DEL-08-05 handoff. Source: `_DEPENDENCIES.md`. |

#### Construction

| Component | Expected artifact/status |
|---|---|
| Governance bridge | `evaluateSubagentGovernance` bridge that consumes explicit governance metadata and returns fail-closed allow/deny outcomes. |
| SDK agent definitions | Definitions generated only for allowed Type 2 task-agent candidates, with deterministic restricted tool lists and cwd. |
| Agent hook | PreToolUse or equivalent `Agent` hook that invokes the bridge before SDK subagent execution. |
| Tests | `Agent` hook tests for missing metadata, non-allowlisted candidates, non-Type-2 candidates, unsealed context, missing approval reference, and restricted child tools/cwd. |
| Events/records handoff | Interface with DEL-08-05 for child lifecycle and artifact-path persistence. |
| Implementation paths | TBD until the coding task identifies the bridge module, SDK agent-definition builder, `Agent` hook module, fixture files, and runnable test command. |

#### References

| RefID | Source | Status |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | MATCH |
| REF-002 | `docs/CONTRACT.md` | MATCH |
| REF-003 | `docs/SPEC.md` | MATCH |
| REF-004 | `docs/TYPES.md` | MATCH |
| REF-005 | `docs/PLAN.md` | MATCH |
| REF-006 | `docs/PRD.md` | HASH_MISMATCH warning per dispatch |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | MATCH |

## Component: execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/Guidance.md

### Guidance: DEL-08-04 Type 2 Subagent Governance Bridge

#### Purpose

This deliverable exists to let Chirality use SDK subagent mechanics while keeping Type 2 delegation under Chirality governance. The bridge should make delegation possible only when the product-owned gate says the request is allowed, the child context is sealed, the candidate is eligible, approvals are traceable, and child capabilities are narrower than or equal to the permitted boundary.

#### Principles

| Principle | Guidance |
|---|---|
| Deny first | Treat any missing governance metadata, unknown candidate status, hook error, unsealed context, missing approval reference, or unsupported state as denial or human-ruling-needed. Do not infer permission from SDK defaults. |
| Chirality owns semantics | SDK `agents`, `Agent` tool behavior, permission modes, and transcripts are implementation details. Public runtime contracts, audit events, and governance decisions remain Chirality-owned. |
| No capability inheritance by accident | A child subagent should receive an explicit restricted tool list and cwd. It should not inherit parent capabilities implicitly, and it should not broaden parent authority. |
| Sealed context only | Type 2 task-agent context is limited to folder contents and declared references. Avoid "ghost inputs" that are not in the sealed brief or declared sources. |
| Approval is evidence, not vibes | The approval reference must be non-empty and traceable to human/gate evidence. Until the accepted format is selected, the bridge should treat absent, ambiguous, mutable, or SDK-only approval data as denial or human-ruling-needed. |
| Separate gate from record persistence | This slice owns bridge and hook behavior. Full parent-child record persistence and output artifact-path storage should be handed to DEL-08-05 through a clear interface. |

#### Considerations

- The PLAN places governed subagent runtime after earlier engine, permission, tool, hook, and result-storage work. If those prerequisites are absent or unstable, the bridge should remain disabled or deny execution.
- `allowedTools` alone is not a restriction boundary. Restrictions require disallowed tools, permission mode, hooks, and overlay policy.
- Hook failures fail closed for subagent actions. This should include bridge exceptions, missing policy inputs, malformed approval references, and failed candidate resolution.
- The candidate resolver should prefer explicit `AGENT_TYPE: 2` and task-agent metadata. If an instruction file is ambiguous, classify it as ineligible until a human or conformance validator resolves it.
- Child cwd should be the approved bounded working root for the task, not the instruction root and not a broad ambient workspace.
- The bridge should produce denial reasons suitable for audit and tests without leaking sensitive prompt or environment data.
- REF-006 remains warning-qualified because `_REFERENCES.md` records a PRD hash mismatch. PRD-derived delegation behavior should remain traceable to the mismatch warning until a human refreshes or waives the accepted PRD snapshot.

#### Trade-offs

| Trade-off | Preferred direction |
|---|---|
| Convenience vs. safety | Prefer denial over opportunistic delegation when governance metadata is incomplete. |
| SDK-native shape vs. product contract | Wrap SDK-native fields behind Chirality types so later SDK changes do not redefine product behavior. |
| Broad child capability vs. bounded execution | Prefer narrow child tool/cwd definitions generated from the approved Type 2 task scope. |
| Bridge-only scope vs. record persistence | Keep this deliverable focused on gate/hook/definition behavior and expose a minimal handoff to DEL-08-05 for lifecycle records. |

#### Examples

| Scenario | Expected outcome |
|---|---|
| Delegation request lacks approval reference | Denied before SDK `Agent` execution. |
| Delegation request includes only an SDK transcript path or mutable UI label as approval evidence | Denied or human-ruling-needed until the accepted approval-reference format is selected. |
| Candidate agent is not on the persona allowlist | Denied before SDK `Agent` execution. |
| Candidate instruction is Type 1 or lacks `AGENT_TYPE: 2` | Denied as non-Type-2 candidate. |
| Context is not sealed or includes undeclared references | Denied or human-ruling-needed; do not execute with ghost inputs. |
| Child tool list requests write/bash beyond approved scope | Denied or reduced to explicit approved tools; do not inherit parent capability. |
| Hook throws during governance evaluation | Denied with fail-closed hook outcome. |

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Impact | Human ruling needed |
|---|---|---|---|
| C-001 | REF-006 PRD hash mismatch is present but dispatch says it is a warning, not a blocker. | Source acceptance state should be refreshed or waived in a later governance pass. | Confirm whether to update the expected PRD hash or preserve the warning for downstream review. |

#### Open Items

| Item | Status |
|---|---|
| Exact TypeScript module/file names for the bridge and SDK agent-definition builder | TBD |
| Exact serialized shape of the governance decision object | TBD; must include allow/deny or human-ruling-needed behavior, stable denial reason vocabulary, decision source, safe metadata, approval reference, candidate/scope facts, and DEL-08-05 handoff fields. |
| Exact approval reference format | TBD; must be non-empty, traceable to human/gate evidence, and stable enough for audit and tests. |
| SDK R0/R1 probe readiness evidence | TBD; treat missing accepted probe evidence as a blocking prerequisite, not as runtime sufficiency. |
| Exact interface boundary with DEL-08-05 | TBD; should carry child lifecycle metadata and output artifact-path hooks without duplicating persistence ownership. |

## Component: execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/Procedure.md

### Procedure: DEL-08-04 Type 2 Subagent Governance Bridge

#### Purpose

Define the operational steps to produce and verify the Type 2 subagent governance bridge for SDK-backed subagent execution.

#### Prerequisites

| Prerequisite | Status |
|---|---|
| Accepted source corpus for DEL-08-04 | Available; REF-006 has hash mismatch warning per dispatch. |
| Current deliverable status permits authoring | INITIALIZED; P3 enrichment is allowed by the four-documents skill, and `_STATUS.md` remains read-only under `NO_STATUS_TOUCH`. |
| Existing `evaluateSubagentGovernance` behavior or target contract | TBD at implementation time; source docs identify it as authoritative but do not provide the code shape. |
| Permission overlay and hook infrastructure | Required by source sequencing; implementation readiness TBD. |
| SDK `agents` capability verified by R0/R1 probes | Required by PLAN/PRD sequencing; current accepted probe reference is TBD and blocks executable runtime-sufficiency claims. |
| Declared upstream dependencies | TBD; no declared upstream edges have been accepted outside the extracted register. Current extracted ACTIVE prerequisites are source corpus, `evaluateSubagentGovernance` contract, permission/hook infrastructure, DEL-04-01 SDK probe, and DEL-08-05 handoff. |

#### Steps

1. Locate the existing `evaluateSubagentGovernance` implementation or define the narrow adapter contract that will call it.
2. Define the governance input required by the bridge: parent session identity, requested candidate agent, requested task scope, context-sealed indicator, pipeline approval indicator, approval reference, persona allowlist result, environment enablement, and requested child tool/cwd constraints.
3. Ensure every required input has a fail-closed default. Missing, malformed, or unknown values must deny or require human ruling.
4. Record the selected implementation paths for the bridge module, SDK agent-definition builder, `Agent` hook module, fixture directory, runnable test command, and output evidence location; if any path is not selected, keep it as a blocking `TBD`.
5. Build or configure SDK `agents` definitions only from allowed Type 2 task-agent instructions.
6. Apply explicit child restrictions to each SDK agent definition, including restricted tools and working directory.
7. Add the SDK `Agent` tool hook or equivalent pre-execution guard.
8. In the hook, call the bridge before SDK subagent execution.
9. Deny execution when the bridge returns denial, when hook execution fails, or when the candidate/tool/cwd configuration cannot be verified.
10. Return structured denial reasons suitable for tests and audit records, with stable reason vocabulary and without sensitive prompt or environment leakage.
11. Provide handoff fields or callback points for DEL-08-05 to persist parent-child lifecycle records and output artifact paths when execution is enabled.
12. Add table-driven tests for all denial paths and for the allowed path with restricted child tools/cwd.
13. Add regression tests proving SDK defaults, inherited permissions, and `allowedTools` alone cannot authorize delegation.

#### Verification

| Check | Expected result |
|---|---|
| Missing governance metadata | Denied; no SDK subagent execution. |
| Missing approval reference | Denied; no SDK subagent execution. |
| Unsealed context | Denied or human-ruling-needed; no ghost-input execution. |
| Non-allowlisted candidate | Denied. |
| Non-Type-2 candidate | Denied. |
| Hook error | Denied fail-closed. |
| Child requests broad tools/cwd | Denied or narrowed to explicit approved restrictions before execution. |
| Allowed governed request | SDK `Agent` execution may proceed only with restricted child tools/cwd and handoff data for child record persistence. |
| Denial reason audit safety | Denial reason uses stable reason vocabulary and safe metadata; it preserves enough detail for review without prompt or environment leakage. |
| Event/persistence handoff | DEL-08-05 can consume bridge/hook result metadata without DEL-08-04 owning full persistence. |

#### Records

The implementation should produce or update these records/artifacts:

- bridge module or adapter for `evaluateSubagentGovernance`;
- SDK agent-definition builder or definitions;
- `Agent` hook tests;
- denial fixtures for missing metadata, non-allowlisted candidate, non-Type-2 candidate, unsealed context, missing approval reference, hook error, and broad child capability request;
- allowed-path fixture showing restricted tools/cwd;
- handoff/interface note for DEL-08-05 child run record persistence.
- implementation path record naming the bridge module, SDK agent-definition builder, `Agent` hook module, fixture directory, runnable test command, and output evidence location, with any unresolved path retained as a blocking `TBD`.
- SDK probe evidence reference for the accepted `agents` capability probe, or an explicit blocking `TBD`.

Do not create or modify `Dependencies.csv` during this procedure. Use `_DEPENDENCIES.md` only as current dependency context until declared edges are accepted.

## Component: execution/PKG-08_Agent_Suite_Pipeline_Dispatch_and_Subagent_Governance/1_Working/DEL-08-04_Type_2_Subagent_Governance_Bridge/Specification.md

### Specification: DEL-08-04 Type 2 Subagent Governance Bridge

#### Scope

This deliverable specifies a backend feature slice that connects Chirality's fail-closed Type 2 subagent governance to SDK-backed subagent execution. It covers:

- generation or assembly of SDK `agents` definitions from allowed Type 2 task-agent instructions;
- the `evaluateSubagentGovernance` bridge used as the authoritative delegation gate;
- `Agent` tool hook behavior that fails closed before SDK subagent execution;
- restrictions on child tool lists and child working directory;
- tests proving denial and restriction behavior.

This deliverable excludes:

- general SDK adapter mechanics outside the subagent bridge;
- persistence of full parent-child runtime records and output artifact paths, except for interface handoff points to DEL-08-05;
- dependency extraction and `Dependencies.csv` creation.

#### Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-08-04-R01 | The bridge MUST call `evaluateSubagentGovernance` as the authoritative fail-closed gate before SDK `Agent` subagent execution. | `docs/TYPES.md` Section 10; `docs/SPEC.md` Section 15.2; `docs/PLAN.md` R5 |
| DEL-08-04-R02 | Delegation MUST be denied unless environment enablement, persona allowlist, context sealing, pipeline approval, approval reference, and Type 2 eligibility all pass. | `docs/CONTRACT.md` K-SUBAGENT-1; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R03 | Delegation without governance metadata MUST be denied. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R04 | Delegation to a non-allowlisted candidate MUST be denied. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R05 | Delegation to a non-Type-2 candidate MUST be denied. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R06 | SDK `agents` definitions MUST be generated or selected only from allowed Type 2 task-agent instructions. | `docs/PLAN.md` R5; `docs/PRD.md` Section 8.15 |
| DEL-08-04-R07 | Child subagents MUST use restricted tool lists and restricted cwd; they MUST NOT inherit or expand capabilities beyond parent governance. | `docs/CONTRACT.md` K-SUBAGENT-2; `docs/PLAN.md` R5 |
| DEL-08-04-R08 | Hook failures for subagent actions MUST fail closed. | `docs/CONTRACT.md` K-HOOK-1; `docs/SPEC.md` Section 15.2 |
| DEL-08-04-R09 | The bridge MUST preserve Chirality-owned runtime semantics rather than treating SDK defaults, SDK transcript shape, SDK tool names, or SDK permission modes as product authority. | `docs/DIRECTIVE.md` Sections 7-8; `docs/PRD.md` Principles 9-10 |
| DEL-08-04-R10 | Unknown values or unsupported facts in governance metadata MUST produce `TBD`, denial, or human-ruling-needed behavior rather than guessed allow decisions. | `docs/CONTRACT.md` K-INVENT-1; `docs/CONTRACT.md` K-CONFLICT-1 |
| DEL-08-04-R11 | The bridge SHOULD expose a clear interface for DEL-08-05 to persist parent-child lifecycle records and output artifact references when execution is enabled. | `docs/CONTRACT.md` K-SUBAGENT-3; decomposition DEL-08-05 |

#### Governance Decision Contract

The exact serialized decision-object type is `TBD` until implementation locates or defines the `evaluateSubagentGovernance` contract. The accepted contract must, at minimum, preserve these product-owned semantics without becoming SDK-shaped:

| Field family | Required content | Source |
|---|---|---|
| Decision behavior | `allow`, `deny`, or application-level `ask`/human-ruling-needed outcome; deny overrides allow. | `docs/PRD.md` FR-087, FR-089; `docs/CONTRACT.md` K-PERM-1 |
| Denial reason | Audit-suitable reason code and summary that are stable enough for tests and do not leak sensitive prompt or environment data. | `docs/PRD.md` FR-092; `Guidance.md` Considerations |
| Decision source | Whether the outcome came from Chirality policy, hook, governance gate, SDK callback, or human gate. | `docs/PRD.md` FR-087, FR-092; `docs/TYPES.md` Section 8.2 |
| Approval reference | Non-empty human/gate evidence string when delegation is allowed; missing or ambiguous approval references deny. | `docs/TYPES.md` Section 10; `docs/CONTRACT.md` K-AUTH-1, K-AUTH-2 |
| Candidate and scope facts | Candidate agent identity, Type 2 eligibility result, allowlist result, context-sealed result, requested tools, restricted tools, requested cwd, and approved cwd. | `docs/TYPES.md` Section 10; `docs/PLAN.md` R5 |
| DEL-08-05 handoff | Parent session/turn identifiers and child lifecycle/output-reference hooks sufficient for DEL-08-05 to persist child records without this deliverable owning persistence. | `docs/TYPES.md` Section 10; `docs/PRD.md` FR-101 |

#### Standards

| Standard or contract | Applicability |
|---|---|
| `docs/CONTRACT.md` K-SEAL-1, K-GHOST-1, K-SUBAGENT-1, K-SUBAGENT-2, K-SUBAGENT-3 | Core subagent governance invariants. |
| `docs/SPEC.md` Sections 14-15 | Tool surface, permission modes, and hook requirements. |
| `docs/TYPES.md` Section 10 | Canonical subagent vocabulary and `evaluateSubagentGovernance` meaning. |
| `docs/PLAN.md` R5 | Implementation sequencing, targets, and acceptance criteria. |
| `docs/PRD.md` Section 8.15 | User/runtime behavior for governed delegation. |
| `AGENT_SOFTWARE_DECOMP.md` deliverable sizing rules | Confirms Type 2 deliverables are bounded executable units; no sub-task level should be invented. |

#### Verification

| Requirement | Verification approach |
|---|---|
| DEL-08-04-R01 | Unit or integration test proves `Agent` hook invokes `evaluateSubagentGovernance` before execution and denies on gate failure. |
| DEL-08-04-R02 | Table-driven tests cover each missing governance condition: environment enablement, persona allowlist, context sealing, pipeline approval, approval reference, and Type 2 eligibility. |
| DEL-08-04-R03 | Test missing/empty governance metadata produces denial and no child execution. |
| DEL-08-04-R04 | Test non-allowlisted candidate produces denial. |
| DEL-08-04-R05 | Test candidate without `AGENT_TYPE: 2` or acceptable Type 2 task metadata produces denial. |
| DEL-08-04-R06 | Fixture test proves SDK `agents` definitions are limited to allowed Type 2 task-agent instructions. |
| DEL-08-04-R07 | Fixture or integration test proves child tool list and cwd are restricted and cannot broaden parent governance. |
| DEL-08-04-R08 | Hook failure test proves fail-closed denial. |
| DEL-08-04-R09 | Contract test verifies bridge inputs/outputs use Chirality-owned types and do not expose SDK-specific state as product authority. |
| DEL-08-04-R10 | Negative tests prove missing or unknown governance values deny or require human ruling. |
| DEL-08-04-R11 | Interface test or type test verifies handoff fields needed by DEL-08-05 are available without this deliverable owning persistence. |

The concrete fixture paths, passing test names, and local/CI commands are `TBD` until the implementation task selects module paths. Before implementation closure, verification evidence must name fixtures for missing metadata, missing approval reference, unsealed context, non-allowlisted candidate, non-Type-2 candidate, hook error, broad child capability request, allowed restricted execution, audit-safe denial reasons, and DEL-08-05 handoff fields.

#### Documentation

Required artifacts for this deliverable:

- `evaluateSubagentGovernance` bridge;
- SDK agent definitions or deterministic definition builder;
- `Agent` hook tests;
- denial/restriction fixtures;
- handoff notes or typed interface for DEL-08-05 child-run persistence.
- implementation path record naming the bridge module, SDK agent-definition builder, `Agent` hook module, fixture directory, runnable test command, and output evidence location, or an explicit blocking `TBD` if any path is not yet selected.

#### Conflict Table (for human ruling)

| Conflict ID | Source A | Source B | Issue | Proposed handling |
|---|---|---|---|---|
| C-001 | `_REFERENCES.md` expected PRD SHA | `_REFERENCES.md` actual PRD SHA | PRD hash mismatch exists. Dispatch explicitly says to treat it as a source warning, not a blocker. | Proceeded with REF-006 as warning; human may later decide whether to refresh the accepted snapshot/hash. |
