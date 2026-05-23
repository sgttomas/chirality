# Datasheet: DEL-08-04 Type 2 Subagent Governance Bridge

## Identification

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

## Attributes

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

## Conditions

| Condition | Value |
|---|---|
| PRD source status | Source warning: REF-006 has expected SHA `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34` and observed SHA `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`; dispatch instructed this is not a blocker. |
| Sequencing | PLAN R5 places governed subagent runtime after earlier runtime, permission, hook, and tool-governance work. |
| Scope boundary | This deliverable covers the governance bridge, SDK agent definitions, and `Agent` hook tests. Persistent parent-child run records are primarily DEL-08-05. |
| Authority boundary | SDK subagent mechanics are an implementation substrate; Chirality-owned governance, permission, audit, and runtime contracts control product semantics. |
| Dependency boundary | Declared upstream/downstream dependency lists remain `TBD`; the current extracted register records ACTIVE execution prerequisites for the source corpus, `evaluateSubagentGovernance` contract, permission/hook infrastructure, DEL-04-01 SDK probe, and DEL-08-05 handoff. Source: `_DEPENDENCIES.md`. |

## Construction

| Component | Expected artifact/status |
|---|---|
| Governance bridge | `evaluateSubagentGovernance` bridge that consumes explicit governance metadata and returns fail-closed allow/deny outcomes. |
| SDK agent definitions | Definitions generated only for allowed Type 2 task-agent candidates, with deterministic restricted tool lists and cwd. |
| Agent hook | PreToolUse or equivalent `Agent` hook that invokes the bridge before SDK subagent execution. |
| Tests | `Agent` hook tests for missing metadata, non-allowlisted candidates, non-Type-2 candidates, unsealed context, missing approval reference, and restricted child tools/cwd. |
| Events/records handoff | Interface with DEL-08-05 for child lifecycle and artifact-path persistence. |
| Implementation paths | TBD until the coding task identifies the bridge module, SDK agent-definition builder, `Agent` hook module, fixture files, and runnable test command. |

## References

| RefID | Source | Status |
|---|---|---|
| REF-001 | `docs/DIRECTIVE.md` | MATCH |
| REF-002 | `docs/CONTRACT.md` | MATCH |
| REF-003 | `docs/SPEC.md` | MATCH |
| REF-004 | `docs/TYPES.md` | MATCH |
| REF-005 | `docs/PLAN.md` | MATCH |
| REF-006 | `docs/PRD.md` | HASH_MISMATCH warning per dispatch |
| REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | MATCH |
