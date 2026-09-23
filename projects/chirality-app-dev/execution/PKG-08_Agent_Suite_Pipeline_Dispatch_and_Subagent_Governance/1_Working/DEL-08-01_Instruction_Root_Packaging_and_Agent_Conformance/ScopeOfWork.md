---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-08-01
package_id: PKG-08
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@dbd812a52d5ed0cb3ed173f3aaaa68703a914291
project_scope_refs: [SOW-030, SOW-031, SOW-073, SOW-082, SOW-084]
package_objective_refs: [OBJ-007, OBJ-008]
---

# Scope of Work — DEL-08-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-08-01` in service of project scope [SOW-030, SOW-031, SOW-073, SOW-082, SOW-084] and package objectives [OBJ-007, OBJ-008].

- **OUT-001** — Agent conformance validator, integrity fixtures, and source-completeness checklist that verify required instruction-root assets, agent metadata, write scopes, naming, and section markers.

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

`DEL-08-01 Instruction Root Packaging and Agent Conformance` (TEST_SUITE, applied decomposition row L368):

Verify required instruction-root assets, agent metadata, write scopes, naming,
section markers, the proposal clauses and named triggers in Agent 0 and Agent 1
packages, skill-declared workflow templates, and organisation-layer packaging
and pins.

Applied row notes: Governance assets and checks; no runtime capability
expansion; instruction-file changes under `agents/` or `skills/` ship the routed
agent-index change notice.

Applied row outputs: Agent conformance validator; integrity fixtures;
source-completeness checklist; proposal-clause and template conformance checks;
organisation-layer integrity checks.

### Current acceptance obligations

1. Required instruction-root assets, agent metadata, write scopes, naming, and section markers are verified as before.
2. Agent 0 and Agent 1 packages carry proposal clauses with named triggers and once-per-chat; skill-declared workflow templates are discoverable; the organisation layer's packaging and pins are checked.
3. No runtime capability expands; any instruction-file change under `agents/` or `skills/` ships the routed agent-index change notice and the G4 manifest.

### Seating and rulings

Remaining items seated under D-APP-108 (2026-09-04): DEL-08-01-V3-01. Ruled
questions applied here: Q14. Alignment writes WI-051, WI-052, WI-053, WI-054,
WI-055 performed in run `APP_SCA_APP_010_SEATING_2026-09-04`; dependency writes
DEP-021, DEP-022 were applied by the D-APP-109 extraction on 2026-09-05; the accepted dependency register remains controlling. No lifecycle, Checking Approval SHA,
dependency-acceptance, product, or release act is implied.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-08-01 Instruction Root Packaging and Agent Conformance

> #### Datasheet: DEL-08-01 Instruction Root Packaging and Agent Conformance
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-08-01 |
> | DeliverableName | Instruction Root Packaging and Agent Conformance |
> | PackageID | PKG-08 |
> | PackageName | Agent Suite, Pipeline Dispatch, and Subagent Governance |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | TEST_SUITE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | CoversScopeItems | SOW-030, SOW-031, SOW-073, SOW-082, SOW-084 |
> | SupportsObjectives | OBJ-007, OBJ-008 |
>
> Source: `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` applied DEL-08-01 row (SCA-APP-010 Gate 5).
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Deliverable purpose | Verify required instruction-root assets, agent metadata, write scopes, naming, and section markers. | Decomposition DEL-08-01 row, lines 340-344 |
> | Anticipated artifacts | Agent conformance validator; integrity fixtures; source-completeness checklist. | `_CONTEXT.md`; Decomposition DEL-08-01 row, lines 340-344 |
> | Instruction root meaning | Release-managed resource set containing governance documents, agent instructions, and framework materials. | `docs/SPEC.md` section 1.1; `docs/TYPES.md` section 1.5 |
> | Ordinary mutation policy | Instruction root is read-only during ordinary project execution; writes must be blocked by runtime hooks and path policy. | `docs/SPEC.md` section 1.1; `docs/CONTRACT.md` K-ROOT-2 |
> | Required source-tree / packaged-app entries | `AGENTS.md`, `README.md`, `agents/`, `docs/`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, `WHAT-IS-AN-AGENT.md` where required, and `PROFESSIONAL_ENGINEERING.md` where required. | `docs/SPEC.md` section 1.1 |
> | PRD packaging acceptance entries | `agents/`, `docs/`, `AGENTS.md`, `README.md`, `WHAT-IS-AN-AGENT.md`, and `PROFESSIONAL_ENGINEERING.md` where required by integrity policy. | `docs/PRD.md` FR-058; D-APP-38 source basis applies |
> | Agent instruction file naming | Agent instruction files use `AGENT_*.md` names. | `docs/SPEC.md` section 7 |
> | Required instruction header | The applicable instruction basis must identify role identity and type. Current four-role files and registry are the operational evidence; old marker serialization is compatibility history. |1|2}`. | `docs/SPEC.md` section 7.1 |
> | Required agent type table fields | Preserve applicable role type, responsibility, interaction boundary, scope and output semantics in the supplied role/brief basis. Missing live metadata checks remain explicit. | `docs/SPEC.md` section 7.2 |
> | Required section markers | Verify the supplied instructions contain their applicable protocol, specification, structure and rationale. Current role files use headings; old paired-marker parsing is compatibility evidence. | `docs/SPEC.md` section 7.3 |
> | Type 2 candidate definition | Agent instruction with `AGENT_TYPE: 2`; preferred `AGENT_CLASS: TASK`. | `docs/TYPES.md` Type 2 vocabulary |
> | Type 2 execution constraint | Type 2 task-agent execution requires sealed context and gate approval metadata. | `docs/CONTRACT.md` K-SEAL-1 |
> | Write-scope invariant | Every agent instruction file declares explicit write scope; agents must not write outside declared scope. | `docs/CONTRACT.md` K-WRITE-1 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> - This deliverable is a test-suite work item for PKG-08 and must not expand runtime capability. Source: `_CONTEXT.md`; decomposition DEL-08-01 row.
> - The test suite must respect instruction-root / working-root separation. Ordinary project execution may write project truth only under the working root. Source: `docs/DIRECTIVE.md` section 2.7; `docs/CONTRACT.md` K-ROOT-3.
> - `docs/PRD.md` is locally accessible and historical D-APP-38 source state; verify current candidate bytes. Treat PRD-derived items as current source-basis inputs, separate from implementation proof.
> - Declared upstream/downstream lists remain `TBD`; the current extracted register records PKG-08/SOW/OBJ anchors and upstream prerequisites for REF-001 through REF-007, DEC-004, and a `TBD current instruction-root source tree`, with no downstream handoff edges populated because the extraction ran with `CONSUMER_CONTEXT=NONE`. Source: `_DEPENDENCIES.md`.
> - The selected Vitest evidence is `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts`; its synthetic legacy fixtures do not establish conformance of shipped role files.
>

### CLM-005 — Construction

> ##### Construction
>
> The required outputs are evidence of conformance, packaging integrity and bounded execution. Their acceptance does not depend on a particular parser, fixture directory or function name. Apply the current App `AGENTS.md` role/context instructions; preserve the unresolved App SPEC §7 / CONTRACT K-WRITE-1 format-and-carrier question separately. This record repair does not accept D-GOV-42's exact bytes or amend the App corpus.
>
> | Output | Requirement | Named verification hook and limit |
> |---|---|---|
> | Agent conformance evidence | Identify the supplied role, instruction origin and content, declared scope and applicable conformance contract; report missing or contradictory metadata. | `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts` is retained legacy-format evidence. Current-basis conformance still requires an applicable packaging/role test; a legacy parser pass does not prove it. |
> | Integrity fixtures | Detect missing, changed and unexpected required instruction assets against the selected packaging basis. | `frontend/src/__tests__/scripts/verify-instruction-root-integrity.test.ts`; D-APP-127's `instruction-root:integrity` check. |
> | Source-completeness checklist | Identify incomplete required assets and carry remediation status, including SOW-073/OI-004. | `frontend/scripts/verify-instruction-root-integrity.mjs` checklist output and its named test above. |
> | Governance fixtures | Verify child eligibility, explicit context and write scope, applicable approval gates, fail-closed admission and absence of authority expansion; distinguish instruction-asserted limits from mechanical enforcement. | `frontend/src/__tests__/lib/harness-subagent-governance.test.ts`, `agent-instruction-conformance.test.ts` and `chirality-hooks.test.ts` are legacy fixtures. Their coverage does not close missing invalid-write-scope or live-path enforcement evidence. |
>
> D-GOV-43/D-APP-127 leave native sandbox and approval policy to the user's Codex configuration; declaring scope never proves host containment. The remaining evidence gaps above retain their owning implementation/governance route.

### CLM-006 — References

> ##### References
>
> - `docs/DIRECTIVE.md` sections 2.7, 5.
> - `docs/CONTRACT.md` sections 1.3 and 1.8.
> - `docs/SPEC.md` sections 1.1, 1.2, 7.1, 7.2, 7.3, 15.2.
> - `docs/TYPES.md` sections 1.5, 3.2, 4.4, Type 2 vocabulary.
> - `docs/PLAN.md` R3 subagent implementation targets and section 6.1.
> - `docs/PRD.md` sections 8.10 and 15, historically reconciled under D-APP-38; verify current bytes.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-08-01, OBJ-007, OBJ-008, SOW-030, SOW-031, SOW-073, and PKG-08 knowledge groups.
> - `../../workflows/software-decomp/WORKFLOW.md` method source; actual conformance examples use the supplied four-role files/registry.

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-08-01 Instruction Root Packaging and Agent Conformance

> #### Specification: DEL-08-01 Instruction Root Packaging and Agent Conformance
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable specifies the test-suite expectations for verifying instruction-root packaging and agent instruction conformance in PKG-08.
>
> In scope:
>
> - Required instruction-root asset presence and packaging integrity checks.
> - Agent instruction filename, header, metadata, write-scope, and section-marker conformance.
> - Source-completeness checklist coverage for instruction-root assets.
> - Fixture coverage for valid and invalid instruction-root and agent-instruction cases.
>
> Out of scope:
>
> - General SDK adapter mechanics. Source: `_CONTEXT.md`.
> - Runtime capability expansion. Source: decomposition DEL-08-01 row.
> - Implementation of the subagent governance bridge itself, which belongs to DEL-08-04. Source: decomposition DEL-08-04 row.
> - Parent-child subagent run records, which belong to DEL-08-05. Source: decomposition DEL-08-05 row.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | DEL0801-REQ001 | The test suite MUST verify that the instruction root is treated as release-managed and read-only during ordinary project execution. | `docs/SPEC.md` section 1.1; `docs/CONTRACT.md` K-ROOT-2 | Negative fixture or runtime-policy test denies instruction-root writes. |
> | DEL0801-REQ002 | The test suite MUST verify that the working root is separate from the instruction root and is the ordinary project-truth write location. | `docs/DIRECTIVE.md` section 2.7; `docs/CONTRACT.md` K-ROOT-1/K-ROOT-3 | Path-policy fixture validates separate roots and rejects working-root-inside-instruction-root cases. |
> | DEL0801-REQ003 | The test suite MUST check the required instruction-root entries listed by SPEC section 1.1. | `docs/SPEC.md` section 1.1 | Integrity fixture enumerates required entries and reports missing assets as blockers. |
> | DEL0801-REQ004 | The test suite SHOULD include PRD FR-058 packaging acceptance entries under the current D-APP-38 authority corpus. | `_REFERENCES.md`; `docs/PRD.md` FR-058; D-APP-38 | Checklist output cites the current historical D-APP-38 source state; verify current candidate bytes source state. |
> | DEL0801-REQ005 | The source-completeness checklist MUST surface SOW-073 / OI-004 required instruction-root asset incompleteness as a packaging-readiness issue. | Decomposition SOW-073 and OI-004; `docs/PRD.md` KG-001 under D-APP-38 | Checklist contains SOW-073/OI-004 row and remediation status. |
> | DEL0801-REQ006 | Agent instruction files MUST be named with the `AGENT_*.md` convention. | `docs/SPEC.md` section 7 | Validator rejects nonconforming agent instruction filenames when they are in the instruction agent set. |
> | DEL0801-REQ007 | The shipped instruction basis MUST identify each role and type; verify current role files and registry together and reject missing identity. | `docs/SPEC.md` section 7.1 | Validator positive/negative fixtures cover missing `[[DOC:AGENT_INSTRUCTIONS]]`, title, and `AGENT_TYPE`. |
> | DEL0801-REQ008 | Conformance MUST verify the applicable role type, responsibility, interaction boundary, scope and output semantics in the supplied basis; missing required fields must fail explicitly. | `docs/SPEC.md` section 7.2 | Validator fixture rejects missing table or missing required rows. |
> | DEL0801-REQ009 | Conformance MUST verify the required protocol, specification, structure and rationale in the applicable supplied instruction format; legacy marker tests alone do not qualify shipped role files. | `docs/SPEC.md` section 7.3 | Validator fixture rejects missing begin/end marker pairs. |
> | DEL0801-REQ010 | Agent conformance MUST verify explicit write-scope declaration and preserve the invariant that agents do not write outside declared scope. | `docs/CONTRACT.md` K-WRITE-1; `docs/TYPES.md` AGENT classification properties | Validator checks `WRITE_SCOPE` value; downstream runtime tests cover enforcement. |
> | DEL0801-REQ011 | TASK is the current Type 2 role. Conformance MUST reject ineligible delegation and must not create a direct-entry TASK role. | `docs/TYPES.md` Type 2 vocabulary | Fixture set includes valid Type 2 task, Type 2 non-task warning/TBD behavior, and non-Type-2 rejection. |
> | DEL0801-REQ012 | Subagent-related conformance MUST fail closed when required governance metadata is absent and MUST NOT grant child agents expanded capabilities. | `docs/CONTRACT.md` K-SEAL-1, K-GHOST-1, K-SUBAGENT-1, K-SUBAGENT-2; `docs/PRD.md` FR-060 under D-APP-38 | Governance fixture asserts absent metadata is denied and child cwd/tools remain restricted. |
> | DEL0801-REQ013 | The validator MUST treat registry surfaces as source registries rather than relying on mutable count prose. | `docs/PRD.md` KG-013 under D-APP-38 | Checklist records registry source paths and generated discovery output. |
> | DEL0801-REQ014 | Unrecognized metadata MUST NOT silently alter execution authority. Verify the current strict registry contract separately from retained legacy unknown-key warning behavior. | `docs/SPEC.md` section 7.4 | Fixture includes unknown key and expects warning-only behavior. |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / authority | Applicability | Location |
> |---|---|---|
> | Chirality instruction root model | Defines required assets, read-only policy, and root separation. | `docs/SPEC.md` section 1; `docs/DIRECTIVE.md` section 2.7 |
> | Chirality agent instruction contract | Defines required filenames, headers, metadata table, and section markers. | `docs/SPEC.md` section 7 |
> | Chirality invariant contract | Defines K-ROOT, K-PACKAGE, K-WRITE, K-SEAL, K-GHOST, and K-SUBAGENT checks. | `docs/CONTRACT.md` sections 1.3 and 1.8 |
> | Chirality vocabulary | Defines Type 2 candidates, task agents, write-scope vocabulary, and pipeline/task scope terms. | `docs/TYPES.md` sections 3.2, 4.4, Type 2 vocabulary |
> | PRD acceptance requirements | Provides FR-058 through FR-063 and known source-completeness gaps, historically reconciled under D-APP-38; verify current bytes. | `docs/PRD.md` sections 8.10 and 15 |
>

### CLM-011 — Verification

> ##### Verification
>
> Verification approach:
>
> - Static source-tree checks for required instruction-root entries.
> - Static agent-instruction parsing checks for filename, header, required metadata, and marker pairs.
> - Fixture-driven positive and negative cases for missing assets and malformed agent files.
> - Path-policy / hook-level tests for instruction-root write denial where runtime enforcement is available.
> - Checklist output that separates SPEC-backed requirements from PRD-backed source-corpus items.
>
> Minimum verification matrix:
>
> | Requirement IDs | Verification artifact |
> |---|---|
> | DEL0801-REQ001, DEL0801-REQ002 | Root policy fixtures and hook/path-policy test |
> | DEL0801-REQ003, DEL0801-REQ004, DEL0801-REQ005 | Instruction-root integrity fixture and source-completeness checklist |
> | DEL0801-REQ006 through DEL0801-REQ010, DEL0801-REQ014 | Agent conformance validator fixture suite |
> | DEL0801-REQ011, DEL0801-REQ012 | Type 2/subagent governance fixture suite |
> | DEL0801-REQ013 | Registry discovery / source registry fixture |
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required records:
>
> - Validator output showing checked files, failures, warnings, and skipped checks.
> - Integrity fixture inventory for required instruction-root assets.
> - Source-completeness checklist, including SOW-073/OI-004 status.
> - D-APP-38 source-corpus state in any checklist item that relies on `docs/PRD.md`.
> - Named verification hook: `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts` (Vitest), instruction-root integrity, and the repository harness-premerge workflow. Actual output location and checked shipped files belong in the candidate verification record.
> - When the implementation owner selects those paths, this deliverable must record the command, fixture directory, pass/fail artifact directory, and whether CI runs the same command or a named wrapper.
> - Human ruling record if the authority-corpus basis changes.

- **AC-001** — The test suite verifies required instruction-root assets, agent instruction metadata, declared write scopes, naming, and required section markers using integrity and conformance fixtures, and produces a source-completeness checklist.

## Production and Verification Method — Praxeology

### CLM-013 — Procedure: DEL-08-01 Instruction Root Packaging and Agent Conformance

> #### Procedure: DEL-08-01 Instruction Root Packaging and Agent Conformance
>

### CLM-014 — Purpose

> ##### Purpose
>
> Define the operational procedure to produce and verify the DEL-08-01 test-suite artifacts: agent conformance validator, integrity fixtures, and source-completeness checklist.
>

### CLM-015 — Prerequisites

> ##### Prerequisites
>
> - Accepted deliverable context in `_CONTEXT.md`.
> - Accessible authoritative references from `_REFERENCES.md`.
> - Decomposition reference: `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`.
> - Current instruction-root source tree containing the candidate root assets and `agents/AGENT_*.md` files.
> - Test framework: Vitest; named fixture/validator hook: `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts`; check the candidate through the registered harness-premerge chain.
> - Declared upstream/downstream lists: TBD. The extracted dependency register currently records upstream source prerequisites and no populated downstream handoff edges; do not invent deliverable edges from boundary references alone. Source: `_DEPENDENCIES.md`.
>

### CLM-016 — Steps

> ##### Steps
>
> 1. Establish the accepted source basis.
>    - Read `_REFERENCES.md`.
>    - Record matching sources and source warnings.
>    - Record `docs/PRD.md` historical D-APP-38 source state; verify current candidate bytes.
>
> 2. Build the instruction-root asset manifest.
>    - Start from `docs/SPEC.md` section 1.1 required entries.
>    - Add PRD FR-058 and KG-001 entries under the current D-APP-38 source basis.
>    - Record each asset as present, missing, not required by active policy, or TBD.
>
> 3. Define agent-instruction conformance checks.
>    - Check filename convention `AGENT_*.md`.
>    - Check required header: `[[DOC:AGENT_INSTRUCTIONS]]`, title, and `AGENT_TYPE`.
>    - Check Agent Type table rows: `AGENT_TYPE`, `AGENT_CLASS`, `INTERACTION_SURFACE`, `WRITE_SCOPE`, `BLOCKING`, and `PRIMARY_OUTPUTS`.
>    - Check required section-marker pairs for `PROTOCOL`, `SPEC`, `STRUCTURE`, and `RATIONALE` when applicable.
>    - Warn on unknown runtime metadata option keys rather than mutating behavior.
>
> 4. Define Type 2 and subagent governance fixture checks.
>    - Identify Type 2 candidates by `AGENT_TYPE: 2`.
>    - Prefer `AGENT_CLASS: TASK` for Type 2 candidates.
>    - Deny non-Type-2 or non-allowlisted delegation fixtures.
>    - Deny subagent requests without sealed context, approved pipeline state, approval reference, and restricted child tool/cwd configuration.
>
> 5. Implement or update validator and fixtures.
>    - Validator path: TBD.
>    - Fixture path: TBD.
>    - Test framework: TBD.
>    - CI or local command: TBD.
>    - Pass/fail artifact directory: TBD.
>    - Record the selected path, framework, command, fixture directory, and artifact directory before treating verification as executable.
>    - Keep outputs under the working root; do not write to the instruction root during ordinary test execution.
>
> 6. Run verification.
>    - Execute the local validator/test command when available.
>    - Confirm positive fixtures pass.
>    - Confirm negative fixtures fail with actionable messages.
>    - Confirm PRD-backed checks cite the D-APP-38 source basis and remain separate from implementation proof.
>    - Capture pass/fail evidence with the command, working tree or commit identifier when available, fixture summary, warning/failure counts, and output artifact location.
>
> 7. Record results.
>    - Store validator output, source-completeness checklist, and fixture summary in the appropriate test artifact location: TBD.
>    - Record unresolved source warnings and human-ruling needs, if any remain.
>

### CLM-017 — Verification

> Use the accepted requirement and verification contract in CLM-009/022 and frontend/src/__tests__/lib/agent-instruction-conformance.test.ts. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit gaps against governing scope and any selected graph. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

### CLM-018 — Records

> Use the accepted requirement and verification contract in CLM-009/022 and frontend/src/__tests__/lib/agent-instruction-conformance.test.ts. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit gaps against governing scope and any selected graph. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

- **VER-001** — Review the agent conformance validator output, integrity fixture results, conformance fixture results, and source-completeness checklist against the preserved legacy requirements.

## Governing Values and Decisions — Axiology

### CLM-019 — Guidance: DEL-08-01 Instruction Root Packaging and Agent Conformance

> #### Guidance: DEL-08-01 Instruction Root Packaging and Agent Conformance
>

### CLM-020 — Purpose

> ##### Purpose
>
> DEL-08-01 exists to make instruction-root packaging and agent conformance explicit and repeatable. It supports OBJ-007 by maintaining agent-suite integrity and governed subagent delegation without expanding authority, and OBJ-008 by keeping validation and instruction-root checks repeatable. Source: decomposition DEL-08-01, OBJ-007, OBJ-008.
>

### CLM-021 — Principles

> ##### Principles
>
> - Treat the instruction root as release-managed. The working root is mutable project truth; the instruction root is not ordinary task output. Source: `docs/DIRECTIVE.md` section 2.7; `docs/SPEC.md` section 1.1.
> - Validate conformance from source files and registries, not from narrative counts. Source: `docs/PRD.md` KG-013 under D-APP-38.
> - Keep the validator conservative. Missing source evidence becomes `TBD`, warning, or failure depending on the governing source; it must not be silently accepted. Source: `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1.
> - Separate conformance validation from runtime capability implementation. DEL-08-01 verifies packaging and instruction conformance; DEL-08-04 and DEL-08-05 cover subagent bridge execution and child records. Source: decomposition PKG-08 rows.
> - Preserve source authority labels. SPEC-backed requirements remain governing structure; PRD-backed requirements are historically reconciled under D-APP-38; verify current bytes and `_REFERENCES.md` historical D-APP-38 source state; verify current candidate bytes state.
>

### CLM-022 — Considerations

> Check the actual shipped four-role instruction basis and its registry, including identity, required content, declared scope and delegation eligibility. Paired-marker/header fixtures remain legacy evidence and cannot qualify current role files. Required packaged assets and ordinary two-layer instruction-root protection remain obligations; a boot hash or a sandbox label does not prove write prevention.
>
> Verification hooks: `frontend/src/__tests__/lib/agent-instruction-conformance.test.ts`, the instruction-root integrity command and actual packaged role-file inspection. Missing packaged-file conformance, negative write-scope cases and organisation-layer fixtures remain delivery work. D-APP-131 applies current roles without asserting D-GOV-42 exact-byte acceptance or silently amending the App authority corpus.

### CLM-023 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Preferred approach | Rationale |
> |---|---|---|
> | Strict failure vs warning for PRD-only items | Treat current PRD-backed items as source-current but still separate source truth from implementation proof. | D-APP-38 resolves the former source warning without advancing lifecycle state. |
> | Parser complexity vs text checks | Use structured parsing where feasible; allow simple text fixtures only for early validator scaffolding. | Section-marker and metadata checks have stable schemas in SPEC. |
> | Broad packaging validation vs DEL-08-01 scope | Check instruction-root assets and conformance only; leave DMG packaging to DEL-09-04. | Decomposition separates DEL-08-01 from release packaging deliverables. |
> | Runtime subagent behavior vs conformance fixtures | Include fail-closed fixture expectations, but do not implement the runtime bridge here. | DEL-08-04 owns `evaluateSubagentGovernance` bridge implementation. |
>

### CLM-024 — Human Ruling Path

> ##### Human Ruling Path
>
> PRD-backed checks are current under D-APP-38 and `_REFERENCES.md` historical D-APP-38 source state; verify current candidate bytes. This resolves the former source-state warning only; it does not convert source requirements into implementation proof or lifecycle transition evidence. SPEC, CONTRACT, and TYPES remain the governing authority for instruction-root packaging and agent conformance where they define the narrower runtime contract.
>

### CLM-025 — Examples

> ##### Examples
>
> Example positive agent-instruction expectations:
>
> - Filename matches `AGENT_*.md`.
> - Header includes `[[DOC:AGENT_INSTRUCTIONS]]`.
> - Header declares `AGENT_TYPE`.
> - Agent Type table includes all required rows from SPEC section 7.2.
> - Required marker pairs are present for `PROTOCOL`, `SPEC`, `STRUCTURE`, and `RATIONALE` when the contract requires those sections.
>
> Example negative fixture expectations:
>
> - Missing `AGENTS.md` in an instruction-root fixture is a packaging-readiness failure under SPEC section 1.1.
> - Missing `WRITE_SCOPE` in an agent instruction is a conformance failure under SPEC section 7.2 and CONTRACT K-WRITE-1.
> - A Type 2 subagent request without sealed context or approval metadata is denied under CONTRACT K-SEAL-1 and K-SUBAGENT-1.
> - A PRD KG-001-only asset such as `tools/REGISTRY.md` is surfaced as a source-completeness item under the current authority corpus; implementation evidence still determines whether the item is satisfied.
>

### CLM-026 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | CT-001 | Former PRD source-state conflict resolved. | `_REFERENCES.md` historical D-APP-38 source state; verify current candidate bytes | D-APP-38 authority corpus v2 | Datasheet Attributes; Specification DEL0801-REQ004, DEL0801-REQ005, DEL0801-REQ012, DEL0801-REQ013; Guidance Considerations | Use PRD content under the current authority corpus; keep implementation proof separate from source-state proof. | D-APP-38 accepted current authority corpus |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-030 SOW-031 SOW-073 OBJ-007 OBJ-008 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

## Retired status detail (2026-09-23)

These clauses preserve operative meaning from the retired App status source. The immutable [source census](../../../_Reconciliation/DeliverableConcordance/RUN_D128_CONCORDANCE_2026-09-21_1614Z/BACKCHECK/APP_RECORD_CLOSEOUT_2026-09-22/REMAINING_WORK_CENSUS.csv) and [finite Task Management account](../../../_Coordination/_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/ROWS.csv) preserve the full original wording, evidence and disposition. These clauses do not assert implementation, acceptance, lifecycle promotion, foreign-loop assignment or a selected execution slot. Current decisions and formal change gates control where they differ from historical wording.

- **APP-R065:** Package the current four-role instruction and proposal/template surfaces and verify their shipped paths. Retired skills-path and legacy marker assumptions are historical compatibility evidence only.

- **APP-R066:** Use shipped four-role source-bound conformance evidence; synthetic legacy-only fixtures do not establish the packaged current role path.
