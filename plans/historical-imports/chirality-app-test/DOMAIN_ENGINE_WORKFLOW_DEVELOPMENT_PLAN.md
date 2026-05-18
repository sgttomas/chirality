# DOMAIN_ENGINE Workflow Development Plan

Status: Draft implementation plan  
Date: 2026-05-03  
Primary owner: DOMAIN_ENGINE  
Related agent: `agents/AGENT_DOMAIN_ENGINE.md`  
Primary governance standard: `agents/AGENT_HELPS_HUMANS.md`  
Primary downstream managers: SKILLMAKER, TOOLMAKER, TASK, CHANGE  
First example domain engine: OpenPipeStress  

---

## 1. Purpose

This plan tells a future implementation instance how to continue from the newly authored `DOMAIN_ENGINE` agent instruction and build the full governed domain-engine workflow.

The goal is not to make Chirality a solver, CAD tool, professional prover, or OpenPipeStress clone. The goal is to give Chirality a reusable, governed integration layer for deterministic domain engines:

```text
DOMAIN_ENGINE
  manages profile adoption, protected paths, tool plans, proposal workflows, handoff state, and human gates.

SKILLMAKER
  creates recurring bounded methods as TASK-loadable skills.

TOOLMAKER
  creates deterministic validators, scanners, matchers, and output-capture tools.

TASK
  executes bounded skill runs within explicit scope and write targets.

Domain engine
  owns canonical domain model truth, computation, native application state, and domain-controlled writes.

Human
  accepts profiles, mutating calls, operation proposals, external validation interpretation, and professional reliance.
```

This plan is intentionally detailed. A future instance should be able to read this file, load the listed source context, and implement the workflow in gated slices without redesigning the architecture.

---

## 2. Read This First

Before implementing any slice, read these files in this order:

1. `INIT.md`
2. `AGENTS.md`
3. `agents/AGENT_HELPS_HUMANS.md`
4. `agents/AGENT_DOMAIN_ENGINE.md`
5. `agents/AGENT_SKILLMAKER.md`
6. `agents/AGENT_TOOLMAKER.md`
7. `agents/AGENT_TASK.md`
8. `agents/AGENT_AUDIT_AGENTS.md`
9. `docs/PRD_CANDIDATE.md`
10. `docs/thesis/bigger-picture/CHIRALITY_PRD_Amendment_Domain_Engine_Integration.md`
11. `docs/thesis/bigger-picture/Chirality_OpenPipeStress_Integration_Plan.md`
12. `docs/thesis/bigger-picture/Chirality_OpenPipeStress_Bigger_Picture_Development_Plan.md`
13. `skills/README.md`
14. `skills/SKILL_TEMPLATE.md`
15. `tools/REGISTRY.md`
16. `docs/REPO_INVENTORY.md`

If these files disagree, use this precedence:

1. `AGENT_HELPS_HUMANS.md`
2. `AGENT_DOMAIN_ENGINE.md`
3. `AGENT_SKILLMAKER.md`, `AGENT_TOOLMAKER.md`, and `AGENT_TASK.md` for their owned layers
4. `AGENTS.md` for indexed suite membership
5. PRD and bigger-picture documents for product direction
6. This plan

Do not silently reconcile conflicts. Record the conflict and ask for human direction.

---

## 3. Current Baseline

Already completed:

| Artifact | Status |
|---|---|
| `agents/AGENT_DOMAIN_ENGINE.md` | Authored and indexed |
| `AGENTS.md` | Updated with `DOMAIN_ENGINE` Type 1 entry |
| `docs/REPO_INVENTORY.md` | Indexed agent count updated |
| `execution/_Reconciliation/AgentAudit/AUDIT_DOMAIN_ENGINE_2026-05-03_2105/` | Audit snapshot showing conformance |

Not yet completed:

| Gap | Status |
|---|---|
| Domain Engine Profile spec | Not written |
| Domain Tool Adapter spec | Not written |
| Domain Write Boundary policy | Not written |
| Operation Proposal spec | Not written |
| Domain Artifact Manifest spec | Not written |
| Boundary Notice spec | Not written |
| DOMAIN_ENGINE skills | Not written |
| DOMAIN_ENGINE deterministic tools | Not written |
| OpenPipeStress example profile | Not written |
| OpenPipeStress adapter implementation | Not in this repo |
| Domain fixture project | Not written |
| Harness API/UI integration for `/api/domain/*` | Not implemented |

---

## 4. Non-Negotiable Boundaries

Preserve these boundaries throughout implementation:

1. DOMAIN_ENGINE is a Type 1 manager. It does not execute bounded content production directly when a TASK skill or deterministic tool is appropriate.
2. SKILLMAKER owns skill contracts under `skills/`.
3. TOOLMAKER owns deterministic tools under `tools/` and their registry entries.
4. TASK is the runtime shell for bounded skill execution.
5. CHANGE owns git staging, committing, tags, and pushes.
6. Domain engines own domain model truth and computation.
7. Agents must not directly write protected domain artifacts.
8. Operation proposals are proposal-only until domain-engine validation and human approval.
9. External prover validation is never claimed unless a human-provided authoritative record exists and is cited.
10. All project-relevant state must be in files, not chat-only memory.

---

## 5. Target Architecture

The full workflow should support these levels:

| Level | Name | Capability | Required assets |
|---:|---|---|---|
| 0 | Manual Bridge | User manually exports manifests/summaries; Chirality agents read and organize them | Agent instruction, review/handoff templates |
| 1 | Read-Only Domain Awareness | Chirality validates profiles, scans artifacts, invokes read-only adapter tools | Profile spec, profile validator, artifact scanner, read-only skills |
| 2 | Domain-Controlled Output Generation | Chirality requests domain-generated runs, comparisons, summaries, handoffs | Tool adapter spec, invocation validator, output capture, protected path matcher |
| 3 | Operation Proposal Workflow | Agents write proposal-only model changes; domain engine validates/previews | Proposal spec, proposal validator, proposal authoring skill |
| 4 | External Result State Support | External results become structured domain-readable artifacts | External result spec, feedback intake skill, comparison workflow |
| 5 | Platform Domain Engine Kit | A second domain engine can integrate without changing core agent instructions | Generic profile registry, fixtures, starter kit |

The first implementation target should reach Level 1 safely. Do not jump to Level 2 or Level 3 until profile validation, artifact scanning, and protected path matching are implemented and tested.

---

## 6. Required Documentation Artifacts

Create these docs before or alongside tools/skills. Prefer a new folder:

```text
docs/domain-engine/
  DOMAIN_ENGINE_PROFILE_SPEC.md
  DOMAIN_TOOL_ADAPTER_SPEC.md
  DOMAIN_WRITE_BOUNDARY_POLICY.md
  DOMAIN_OPERATION_PROPOSAL_SPEC.md
  DOMAIN_ARTIFACT_MANIFEST_SPEC.md
  DOMAIN_BOUNDARY_NOTICE_SPEC.md
  OPENPIPESTRESS_PROFILE_DRAFT.yaml
  OPENPIPESTRESS_ARTIFACT_LAYOUT.md
  DOMAIN_ENGINE_IMPLEMENTATION_STATUS.md
```

### 6.1 `DOMAIN_ENGINE_PROFILE_SPEC.md`

Purpose: define the generic profile schema consumed by DOMAIN_ENGINE and deterministic tools.

Minimum sections:

- Purpose
- Status and version
- Profile lifecycle: `DRAFT | VALIDATED | ADOPTED | STALE | INVALID`
- Required YAML shape
- Required fields
- Optional extension fields
- Artifact class definitions
- Tool mode definitions
- Human gate definitions
- Boundary notice requirements
- Validation rules
- Example minimal profile
- OpenPipeStress example excerpt

Required schema fields:

```yaml
domain_profile:
  schema_version: "1.0"
  id: "<stable_ascii_token>"
  name: "<human-readable name>"
  engine_type: "<domain classification>"
  profile_version: "0.1"
  domain_root_patterns: []
  authoritative_artifacts: []
  chirality_readable_artifacts: []
  protected_write_paths: []
  agent_writable_paths: []
  deterministic_tools: []
  human_gates: []
  professional_boundary:
    agent_must_not_claim: []
```

Acceptance criteria:

- The spec is generic, not OpenPipeStress-only.
- It clearly distinguishes domain truth, Chirality-readable artifacts, and agent-writable artifacts.
- It states that profiles are required beyond manual bridge mode.
- It includes controlled enums for tool mode and profile status.

### 6.2 `DOMAIN_TOOL_ADAPTER_SPEC.md`

Purpose: define how deterministic domain engine commands are declared and invoked.

Minimum sections:

- Adapter concept
- Tool ID naming
- Tool modes
- Input schema contract
- Output schema contract
- Side-effect declaration
- Human confirmation rule
- Output capture rule
- Failure behavior
- Logging requirements
- Example read-only command
- Example domain-controlled write command

Required tool modes:

```text
read_only
summary_write
domain_controlled_write
proposal_validate
proposal_apply
boundary_check
```

Acceptance criteria:

- Every mutating tool declares side effects and output paths.
- Every mutating tool declares whether human confirmation is required.
- The adapter spec prohibits raw agent mutation of protected paths.
- The spec distinguishes a tool that validates a proposal from a tool that applies a proposal.

### 6.3 `DOMAIN_WRITE_BOUNDARY_POLICY.md`

Purpose: define path-level governance for domain-engine integrations.

Minimum sections:

- Path classes
- Profile path pattern grammar
- Protected path matching
- Agent-writable path matching
- Conflict resolution when patterns overlap
- Stricter-rule-wins policy
- Symlink and path traversal policy
- Runtime enforcement limits
- Test cases

Path classes:

```text
AUTHORITATIVE_DOMAIN_ARTIFACT
CHIRALITY_READABLE_ARTIFACT
AGENT_WRITABLE_ARTIFACT
PROTECTED_WRITE_PATH
DOMAIN_CONTROLLED_OUTPUT
DERIVED_PUBLICATION_ARTIFACT
UNKNOWN
```

Acceptance criteria:

- The policy states that `PROTECTED_WRITE_PATH` wins over `AGENT_WRITABLE_ARTIFACT` on overlap.
- The policy requires all resolved paths to stay under `WORKING_ROOT`.
- The policy requires unknown paths to be treated as non-writable until classified.

### 6.4 `DOMAIN_OPERATION_PROPOSAL_SPEC.md`

Purpose: define proposal-only model/domain change artifacts.

Minimum sections:

- Proposal lifecycle
- Required fields
- Evidence rules
- Base-state binding
- Assumptions/blockers
- Validation result binding
- Human approval metadata
- Professional boundary text
- Example OpenPipeStress proposal

Required fields:

```yaml
operation_proposal:
  schema_version: "1.0"
  id: "PROP-0001"
  title: "<short title>"
  status: "proposal_only"
  domain_engine_id: "<profile id>"
  base_state_id: "<state id or TBD>"
  created_by: "DOMAIN_ENGINE"
  created_at: "<ISO 8601>"
  operation:
    type: "<controlled or profile-specific type>"
  rationale:
    summary: "<evidence-backed rationale>"
    evidence: []
  unresolved_assumptions: []
  blockers: []
  professional_boundary:
    notice: "<required notice>"
```

Acceptance criteria:

- Proposal status must start as `proposal_only`.
- Missing base state is allowed only as explicit `TBD`.
- Evidence is required for every rationale claim.
- The spec does not permit direct acceptance as model truth.

### 6.5 `DOMAIN_ARTIFACT_MANIFEST_SPEC.md`

Purpose: define scan outputs and domain-readable artifact inventories.

Minimum sections:

- Manifest purpose
- Artifact inventory schema
- Role labels
- Missing/stale markers
- Hash and timestamp guidance
- Profile binding
- Example scan output

Required artifact inventory columns:

```text
ArtifactID
DomainEngineID
Path
ResolvedRole
ProfilePattern
Exists
ReadableByAgents
WritableByAgents
Protected
Hash
ModifiedTime
Status
Notes
```

Acceptance criteria:

- The manifest can be produced deterministically from `WORKING_ROOT` and profile.
- It supports missing artifact reporting.
- It does not require reading unbounded model internals.

### 6.6 `DOMAIN_BOUNDARY_NOTICE_SPEC.md`

Purpose: define standard language checks for professional, external-prover, IP, and private-data boundaries.

Minimum sections:

- Required prohibitions
- Required notice patterns
- Allowed wording
- Disallowed wording
- Project-specific extensions
- Boundary check output schema

Disallowed claim examples:

```text
code compliant for reliance
professionally approved
certified
sealed
ready for construction
external prover validated
accepted engineering change
```

Acceptance criteria:

- The spec supports deterministic string/pattern checks.
- It distinguishes "internal analysis summary" from "professional validation".
- It allows a human-supplied external record to be cited without letting agents invent status.

---

## 7. Deterministic Tools To Build

TOOLMAKER should implement these tools. A future instance should not hand-write tool code casually inside another workflow. Use TOOLMAKER or follow `AGENT_TOOLMAKER.md` exactly.

Recommended directory:

```text
tools/domain_engine/
```

Also update `tools/REGISTRY.md`. If TOOLMAKER prefers existing categories, place validators under `tools/validation/` and scanners under `tools/query/`, but keep names and registry entries stable.

### Tool 1: `validate_domain_engine_profile.py`

Purpose: validate one Domain Engine Profile YAML.

Inputs:

```text
--profile <path>
--repo-root <path optional>
--working-root <path optional>
--output-report <path optional>
--output-json <path optional>
```

Outputs:

- PASS/FAIL summary to stdout
- optional Markdown report
- optional JSON findings
- exit codes:
  - `0` pass
  - `1` validation findings
  - `2` input/tool failure

Checks:

- YAML parses.
- Root key is `domain_profile`.
- Required fields exist.
- `id` is stable ASCII token.
- lists are lists, not strings.
- tool modes are controlled values.
- human confirmation flags are booleans.
- protected paths are non-empty for Level 1+ profiles.
- profile does not silently downgrade protected paths.
- profile paths do not escape `WORKING_ROOT` when a working root is supplied.

Acceptance criteria:

- Invalid profiles fail with clear finding IDs.
- Valid minimal profile passes.
- Output is deterministic for same input.
- Tool is registered.

### Tool 2: `scan_domain_artifacts.py`

Purpose: scan a working root using a valid profile and produce artifact inventory.

Inputs:

```text
--working-root <path>
--profile <path>
--output-inventory <csv>
--output-report <md>
--include-hashes
```

Outputs:

- `Artifact_Inventory.csv`
- `Artifact_Scan_Report.md`

Checks:

- profile validates or stops with `FAILED_INPUTS`
- profile patterns are resolved relative to working root
- missing expected artifacts are reported
- discovered artifacts are role-labeled
- protected and writable overlaps are flagged
- symlinks are rejected or labeled blocked

Acceptance criteria:

- Works on fixture root with OpenPipeStress-like layout.
- Does not read file contents except metadata/hash where requested.
- Does not follow symlinks.
- Produces stable sorted output.

### Tool 3: `check_domain_write_paths.py`

Purpose: decide whether candidate write paths are allowed under a profile.

Inputs:

```text
--working-root <path>
--profile <path>
--candidate <path>    # repeatable
--output-findings <csv optional>
```

Outputs:

- stdout path verdicts
- optional findings CSV

Verdicts:

```text
ALLOW_AGENT_WRITE
ALLOW_DOMAIN_TOOL_WRITE
DENY_PROTECTED
DENY_OUTSIDE_WORKING_ROOT
DENY_UNKNOWN
DENY_PATTERN_CONFLICT
```

Acceptance criteria:

- Protected paths override agent-writable paths.
- Paths outside working root are denied.
- Unknown paths are denied unless profile explicitly permits them.
- Tool can be used in tests and future runtime guards.

### Tool 4: `validate_domain_tool_invocation.py`

Purpose: validate a planned adapter call against profile tool declarations.

Inputs:

```text
--profile <path>
--tool-id <id>
--args-json <path>
--working-root <path>
--output-plan <md optional>
--output-findings <csv optional>
```

Outputs:

- invocation validity result
- optional `Invocation_Plan.md`
- optional findings CSV

Checks:

- tool ID exists in profile
- mode is declared
- required arguments exist if schema is supplied
- output paths are declared
- required human confirmation is reported
- mutating tools cannot run as read-only

Acceptance criteria:

- Fails closed on unknown tool ID.
- Flags missing human confirmation for mutating calls.
- Can validate read-only OpenPipeStress-style commands.

### Tool 5: `capture_domain_tool_output.py`

Purpose: copy or index declared domain tool outputs into a Chirality-readable result capture record.

Inputs:

```text
--working-root <path>
--profile <path>
--tool-id <id>
--tool-output-root <path>
--capture-root <path>
--invocation-plan <path optional>
```

Outputs:

- `RESULT_CAPTURE.md`
- `Captured_Outputs.csv`
- optional checksums

Acceptance criteria:

- Does not mutate domain tool outputs.
- Does not copy protected internals unless profile marks them as readable/capturable.
- Produces a manifest with path, role, hash, and notes.

### Tool 6: `validate_domain_operation_proposal.py`

Purpose: validate proposal-only operation files against the proposal spec and active profile.

Inputs:

```text
--proposal <path>
--profile <path>
--working-root <path>
--output-report <md optional>
--output-findings <csv optional>
```

Checks:

- YAML parses.
- status is `proposal_only`.
- proposal ID format is valid.
- domain engine ID matches profile.
- proposal path is agent-writable.
- base state exists or is explicit `TBD`.
- rationale has evidence entries.
- professional boundary notice exists.
- proposal does not claim acceptance.

Acceptance criteria:

- Bad proposals fail with actionable findings.
- Valid proposal fixture passes.
- Tool never applies a proposal.

### Tool 7: `check_domain_boundary_language.py`

Purpose: deterministic string/pattern check for prohibited professional/external validation claims.

Inputs:

```text
--input <path>        # repeatable
--profile <path optional>
--policy <path optional>
--output-findings <csv optional>
```

Outputs:

- PASS/FAIL summary
- optional findings CSV

Acceptance criteria:

- Finds prohibited phrases.
- Supports profile-specific prohibited claims.
- Does not rewrite files.

### Tool 8: `scan_private_data_boundary.py`

Purpose: initial conservative private/protected data scan for domain artifacts and generated summaries.

Inputs:

```text
--input <path>        # repeatable file/folder
--policy <path optional>
--output-findings <csv>
```

Initial checks:

- obvious API keys/secrets
- private rule-pack markers
- proprietary standards references when configured
- external vendor data markers when configured

Acceptance criteria:

- Conservative findings only; no automatic deletion.
- Report contains path, line/field when possible, rule ID, severity, and recommendation.

### Tool 9: `build_domain_task_brief.py`

Purpose: render valid INIT-TASK briefs for DOMAIN_ENGINE-dispatched skills.

Inputs:

```text
--skill <skill-name>
--scope-path <path>
--profile <path>
--readable-artifacts-json <path optional>
--allowed-write-target <path repeatable>
--runtime-overrides-json <path optional>
```

Outputs:

- INIT-TASK brief to stdout or `--output <path>`

Acceptance criteria:

- Uses canonical TASK fields.
- Emits `TaskSkill` matching the requested skill.
- Includes profile path, protected paths, readable artifacts, and allowed write targets.
- Fails if required fields for the selected skill are missing.

Implementation note:

This can be deferred until repeated hand-composed briefs become a problem. It is useful for Level 2+ reliability.

---

## 8. Repo-Native Skills To Build

SKILLMAKER should create these skills. Each skill folder must include:

```text
skills/<skill-name>/
  SKILL.md
  BRIEF_SCHEMA.md
  TOOL_POLICY.md
  QA_CHECKS.md
```

Run this after each skill is added:

```sh
python3 tools/validation/validate_skill_metadata.py skills
```

### Skill 1: `domain-profile-review`

Purpose: review or draft one Domain Engine Profile against the profile spec.

Suitable shell:

- TASK generic shell mode
- `metadata.chirality-task-profile: NONE`

Required inputs:

- `RuntimeOverrides.ProfilePath`
- `RuntimeOverrides.WorkingRoot`
- `RuntimeOverrides.DomainEngineID`
- optional source docs or known engine layout

Preferred tools:

- `python3 tools/domain_engine/validate_domain_engine_profile.py:*`
- optional `python3 tools/domain_engine/check_domain_boundary_language.py:*`

Outputs:

- `Profile_Review.md`
- `Profile_Open_Issues.md`
- optional proposed profile patch as `PROPOSAL`, not applied unless `ApplyEdits: true` and allowed

QA checks:

- required profile fields checked
- protected paths present
- agent-writable paths present
- tool modes checked
- OpenPipeStress-specific content does not leak into generic fields unless profile ID is OpenPipeStress

Acceptance criteria:

- Skill passes metadata validation.
- It can review `OPENPIPESTRESS_PROFILE_DRAFT.yaml`.
- It does not silently adopt a profile.

### Skill 2: `domain-artifact-review`

Purpose: review a domain artifact inventory and produce evidence-backed review notes and TBDs.

Required inputs:

- `RuntimeOverrides.ProfilePath`
- `RuntimeOverrides.ArtifactInventoryPath`
- `RuntimeOverrides.ReadableArtifacts`
- `RuntimeOverrides.ProtectedWritePaths`

Preferred tools:

- `python3 tools/domain_engine/scan_domain_artifacts.py:*`
- `python3 tools/domain_engine/check_domain_write_paths.py:*`

Outputs:

- `Domain_Artifact_Review.md`
- `TBD_Register.md` or configured TBD output
- `Artifact_Gaps.md`

QA checks:

- every cited artifact appears in inventory
- missing artifacts are listed as gaps
- no protected artifact is recommended for direct agent edit
- review notes cite file paths, manifest IDs, run IDs, or `TBD`

Acceptance criteria:

- Can run against fixture project after scan.
- Produces no direct domain model edits.

### Skill 3: `domain-operation-proposal`

Purpose: draft a proposal-only domain operation from deterministic evidence.

Required inputs:

- `RuntimeOverrides.ProfilePath`
- `RuntimeOverrides.DomainEngineID`
- `RuntimeOverrides.BaseStateID`
- `RuntimeOverrides.Evidence`
- `RuntimeOverrides.ProposalID`
- `AllowedWriteTargets` containing the proposal path

Preferred tools:

- `python3 tools/domain_engine/validate_domain_operation_proposal.py:*`
- optional `python3 tools/domain_engine/check_domain_boundary_language.py:*`

Outputs:

- `PROP-<NNNN>_<short_name>.yaml`
- `Proposal_Rationale.md`
- `Proposal_Blockers.md`

QA checks:

- status is `proposal_only`
- base state present or `TBD`
- rationale evidence is cited
- professional boundary notice exists
- validation tool passes or findings are reported

Acceptance criteria:

- Drafts a valid proposal fixture.
- Does not call `proposal_apply`.
- Does not claim proposal acceptance.

### Skill 4: `domain-handoff-checklist`

Purpose: produce Chirality-side handoff checklist and external-review TBDs from domain-generated handoff artifacts.

Required inputs:

- `RuntimeOverrides.ProfilePath`
- `RuntimeOverrides.HandoffManifestPath`
- `RuntimeOverrides.ExportWarningsPath`
- optional `RuntimeOverrides.ExternalReviewContext`

Preferred tools:

- `python3 tools/domain_engine/check_domain_boundary_language.py:*`
- `python3 tools/domain_engine/scan_private_data_boundary.py:*`

Outputs:

- `HANDOFF_CHECKLIST.md`
- `External_Review_TBDs.md`
- `Handoff_Readiness_QA.md`

QA checks:

- handoff manifest exists
- warnings exported by domain engine are carried forward
- unresolved assumptions are surfaced
- no external validation status is claimed
- boundary notices included

Acceptance criteria:

- Can run on an OpenPipeStress-style handoff fixture.
- Produces human-actionable checklist.

### Skill 5: `external-review-feedback-intake`

Purpose: convert human-supplied external review comments into TBDs, proposal candidates, and change-record scaffolds.

Required inputs:

- `RuntimeOverrides.ExternalReviewRecordPath`
- `RuntimeOverrides.ProfilePath`
- `RuntimeOverrides.BaseStateID`
- optional comparison/run evidence

Preferred tools:

- `python3 tools/domain_engine/check_domain_boundary_language.py:*`
- optional `python3 tools/domain_engine/validate_domain_operation_proposal.py:*`

Outputs:

- `External_Review_Findings.md`
- `External_Review_TBDs.md`
- optional proposal candidate stubs marked `PROPOSAL`
- `Change_Record_Scaffold.md`

QA checks:

- every finding cites the human-supplied external review record
- unclear findings become `TBD`
- proposed domain changes remain proposal-only
- no external validation status is invented

Acceptance criteria:

- Handles a small fixture review comment file.
- Produces no accepted model changes.

### Skill 6: `domain-report-fragment-review`

Purpose: review domain-generated report fragments before they are used in broader deliverables.

Required inputs:

- `RuntimeOverrides.ProfilePath`
- `RuntimeOverrides.ReportFragmentPaths`
- optional `RuntimeOverrides.SourceManifestPaths`

Preferred tools:

- `python3 tools/domain_engine/check_domain_boundary_language.py:*`
- `python3 tools/domain_engine/scan_private_data_boundary.py:*`

Outputs:

- `Report_Fragment_Review.md`
- `Boundary_Findings.md`
- `Missing_Provenance.md`

QA checks:

- fragments cite domain tool outputs or manifests
- no prohibited professional claims
- private/protected content findings surfaced
- unresolved assumptions listed

Acceptance criteria:

- Can review fixture report fragments.
- Produces findings, not rewritten accepted reports, unless explicitly authorized within allowed write scope.

---

## 9. OpenPipeStress First Profile

OpenPipeStress should be the first concrete profile, but implementation must not bake piping-specific behavior into generic tools.

Create:

```text
docs/domain-engine/OPENPIPESTRESS_PROFILE_DRAFT.yaml
docs/domain-engine/OPENPIPESTRESS_ARTIFACT_LAYOUT.md
fixtures/domain-engine/open_pipe_stress_minimal/
```

If `fixtures/` does not exist, create it only when implementation begins and the human accepts the test fixture location.

### 9.1 Draft Profile Shape

The draft profile should include:

```yaml
domain_profile:
  schema_version: "1.0"
  id: "open_pipe_stress"
  name: "OpenPipeStress"
  engine_type: "piping_design_and_stress_model_authoring"
  profile_version: "0.1"

  domain_root_patterns:
    - "OpenPipeStress/"
    - "**/OpenPipeStress/"

  authoritative_artifacts:
    - "OpenPipeStress/project.ops.yaml"
    - "OpenPipeStress/states/**"
    - "OpenPipeStress/runs/**"
    - "OpenPipeStress/comparisons/**"
    - "OpenPipeStress/handoff/**"

  chirality_readable_artifacts:
    - "Model_Manifest.md"
    - "Model_Manifest.yaml"
    - "Model_Warnings.md"
    - "Model_Assumptions.md"
    - "RUN-*_summary.md"
    - "CMP-*_summary.md"
    - "CMP-*_delta_table.csv"
    - "Handoff_Manifest.md"
    - "Export_Warnings.md"
    - "TBD_Register.md"

  protected_write_paths:
    - "OpenPipeStress/project.ops.yaml"
    - "OpenPipeStress/states/**"
    - "OpenPipeStress/runs/**"
    - "OpenPipeStress/comparisons/**"
    - "OpenPipeStress/handoff/**"

  agent_writable_paths:
    - "OpenPipeStress/proposals/**"
    - "Review_Notes.md"
    - "TBD_Register.md"
    - "Draft_Report_Sections/**"

  deterministic_tools:
    - id: "ops.validate_model"
      mode: "read_only"
      requires_human_confirmation: false
    - id: "ops.summarize_model"
      mode: "read_only"
      requires_human_confirmation: false
    - id: "ops.list_states"
      mode: "read_only"
      requires_human_confirmation: false
    - id: "ops.list_runs"
      mode: "read_only"
      requires_human_confirmation: false
    - id: "ops.run_analysis"
      mode: "domain_controlled_write"
      requires_human_confirmation: true
    - id: "ops.compare_states"
      mode: "domain_controlled_write"
      requires_human_confirmation: false
    - id: "ops.compare_runs"
      mode: "domain_controlled_write"
      requires_human_confirmation: false
    - id: "ops.generate_handoff"
      mode: "domain_controlled_write"
      requires_human_confirmation: true
    - id: "ops.generate_report_fragment"
      mode: "summary_write"
      requires_human_confirmation: false
    - id: "ops.validate_operation_proposal"
      mode: "proposal_validate"
      requires_human_confirmation: false
    - id: "ops.apply_operation_proposal"
      mode: "proposal_apply"
      requires_human_confirmation: true

  professional_boundary:
    agent_must_not_claim:
      - "code compliant for reliance"
      - "professionally approved"
      - "certified"
      - "sealed"
      - "ready for construction"
      - "external prover validated unless supplied as external human record"
```

### 9.2 Fixture Layout

The first fixture should be small and static:

```text
fixtures/domain-engine/open_pipe_stress_minimal/
  INIT.md
  PKG-01_PipingDesign/
    DEL-01-02_OpenPipeStressModel/
      _STATUS.md
      Model_Manifest.md
      Model_Manifest.yaml
      Model_Warnings.md
      Model_Assumptions.md
      Review_Notes.md
      TBD_Register.md
      OpenPipeStress/
        project.ops.yaml
        states/
          STATE-0001.yaml
        runs/
          RUN-0001/
            analysis_run.yaml
            results_summary.md
            warnings.md
        comparisons/
        handoff/
        proposals/
```

Fixture rules:

- Keep data synthetic.
- Do not include licensed standard text.
- Include at least one warning and one assumption.
- Include one protected path and one allowed proposal path.
- Include one intentionally missing readable artifact for scan testing.

---

## 10. Harness API And UI Work

This plan is primarily instruction/skills/tools, but the PRD amendment identifies later harness work.

Do not implement API/UI until docs, tools, skills, and fixtures are stable enough to test.

Proposed endpoints:

```text
GET  /api/domain/profiles/list
POST /api/domain/profile/validate
GET  /api/domain/artifacts/scan
POST /api/domain/tool/invoke
GET  /api/domain/proposals/list
POST /api/domain/proposal/validate
```

Minimum API constraints:

- Resolve all paths under selected working root.
- Reject symlinks/special files for profile and proposal inputs unless explicitly supported by security policy.
- Do not expose arbitrary command execution through `/api/domain/tool/invoke`.
- Invoke only profile-declared tools.
- Capture tool outputs as project files when they affect reasoning.
- Return typed errors, not string-only failures.

Minimum UI surfaces:

- Domain profile status panel
- Artifact inventory panel
- Protected path summary
- Available domain tools list
- Proposal list and validation status
- Boundary findings display
- Handoff state display

Out of scope for first UI pass:

- Embedding OpenPipeStress GUI
- Direct model editing
- External commercial prover parsing
- Professional approval workflow

---

## 11. Implementation Phases

### Phase 0 - Baseline Confirmation

Owner: future implementation instance as DOMAIN_ENGINE

Tasks:

1. Read the files listed in Section 2.
2. Confirm `AGENT_DOMAIN_ENGINE.md` still passes audit.
3. Confirm whether the human wants to implement Level 1 only or proceed toward Level 2/3.
4. Confirm target file locations for docs, tools, skills, and fixtures.
5. Record any deviations from this plan.

Exit criteria:

- Human accepts implementation scope.
- No unresolved governance conflict exists.

### Phase 1 - Author Domain Engine Specs

Owner: DOMAIN_ENGINE, with human review

Create:

- `docs/domain-engine/DOMAIN_ENGINE_PROFILE_SPEC.md`
- `docs/domain-engine/DOMAIN_TOOL_ADAPTER_SPEC.md`
- `docs/domain-engine/DOMAIN_WRITE_BOUNDARY_POLICY.md`
- `docs/domain-engine/DOMAIN_OPERATION_PROPOSAL_SPEC.md`
- `docs/domain-engine/DOMAIN_ARTIFACT_MANIFEST_SPEC.md`
- `docs/domain-engine/DOMAIN_BOUNDARY_NOTICE_SPEC.md`
- `docs/domain-engine/DOMAIN_ENGINE_IMPLEMENTATION_STATUS.md`

Acceptance checks:

- Specs are generic and OpenPipeStress is example-only.
- Specs preserve human decision rights.
- Specs define controlled enums and fail-closed behavior.
- Specs identify which rules are enforced by tools vs instructions.

Recommended validation:

- Run `git diff --check`.
- Run `AUDIT_AGENTS` only if agent instructions change.

### Phase 2 - Build Deterministic Tool Foundation

Owner: TOOLMAKER

Implement first:

1. `validate_domain_engine_profile.py`
2. `scan_domain_artifacts.py`
3. `check_domain_write_paths.py`

Then implement:

4. `validate_domain_tool_invocation.py`
5. `capture_domain_tool_output.py`
6. `validate_domain_operation_proposal.py`
7. `check_domain_boundary_language.py`
8. `scan_private_data_boundary.py`

Defer until needed:

9. `build_domain_task_brief.py`

Acceptance checks:

- All tools have usage comments, input/output contracts, exit codes, and scope boundaries.
- All tools are registered in `tools/REGISTRY.md`.
- Tools have minimal fixture tests or smoke commands.
- Tools do not call LLMs.
- Tools are deterministic.

Suggested test command pattern:

```sh
python3 tools/domain_engine/validate_domain_engine_profile.py --profile docs/domain-engine/OPENPIPESTRESS_PROFILE_DRAFT.yaml
python3 tools/domain_engine/scan_domain_artifacts.py --working-root fixtures/domain-engine/open_pipe_stress_minimal --profile docs/domain-engine/OPENPIPESTRESS_PROFILE_DRAFT.yaml --output-inventory /tmp/domain_artifacts.csv --output-report /tmp/domain_artifacts.md
python3 tools/domain_engine/check_domain_write_paths.py --working-root fixtures/domain-engine/open_pipe_stress_minimal --profile docs/domain-engine/OPENPIPESTRESS_PROFILE_DRAFT.yaml --candidate fixtures/domain-engine/open_pipe_stress_minimal/PKG-01_PipingDesign/DEL-01-02_OpenPipeStressModel/OpenPipeStress/project.ops.yaml
```

### Phase 3 - Create OpenPipeStress Draft Profile And Fixture

Owner: DOMAIN_ENGINE with TOOLMAKER validation support

Create:

- `docs/domain-engine/OPENPIPESTRESS_PROFILE_DRAFT.yaml`
- `docs/domain-engine/OPENPIPESTRESS_ARTIFACT_LAYOUT.md`
- `fixtures/domain-engine/open_pipe_stress_minimal/`

Acceptance checks:

- Profile validates.
- Scanner finds expected artifacts and missing items.
- Protected path checker denies `OpenPipeStress/project.ops.yaml`.
- Protected path checker allows declared proposal path.
- Boundary checker finds no prohibited claims in fixture summaries.

### Phase 4 - Build Level 1 Skills

Owner: SKILLMAKER

Build first:

1. `skills/domain-profile-review/`
2. `skills/domain-artifact-review/`

Acceptance checks:

- Both skills pass `validate_skill_metadata.py`.
- Both skills include explicit `TOOL_POLICY.md`.
- TASK can load both skills.
- Both skills run in generic TASK shell mode (`chirality-task-profile: NONE`).
- Both skills write only to allowed targets.

Pilot runs:

- Review OpenPipeStress draft profile.
- Scan fixture artifacts.
- Produce review notes and TBDs from fixture summaries.

### Phase 5 - Build Proposal And Handoff Skills

Owner: SKILLMAKER

Build:

1. `skills/domain-operation-proposal/`
2. `skills/domain-handoff-checklist/`
3. `skills/external-review-feedback-intake/`
4. `skills/domain-report-fragment-review/`

Acceptance checks:

- All skills pass metadata validation.
- Proposal skill produces `proposal_only` YAML.
- Proposal validator passes on a good proposal and fails on an accepted-status proposal.
- Handoff checklist skill does not claim external validation.
- Report fragment review catches prohibited boundary language.

### Phase 6 - Wire DOMAIN_ENGINE Runtime Patterns

Owner: DOMAIN_ENGINE

Update `agents/AGENT_DOMAIN_ENGINE.md` only if necessary after skills/tools exist.

Potential updates:

- Replace placeholder skill names in examples with actual skill folder names.
- Add exact preferred tool names.
- Add reference to `docs/domain-engine/` specs.
- Add Level 1 runbook examples using actual fixture paths.

Do not broaden DOMAIN_ENGINE into tool or skill ownership.

Acceptance checks:

- `AGENT_DOMAIN_ENGINE.md` still passes `AUDIT_AGENTS`.
- `AGENTS.md` index still accurate.
- `docs/REPO_INVENTORY.md` updated only if indexed agent count changes.

### Phase 7 - Pilot End-To-End Level 1

Owner: DOMAIN_ENGINE

Pilot flow:

1. Validate OpenPipeStress profile.
2. Scan fixture artifacts.
3. Run `domain-profile-review`.
4. Run `domain-artifact-review`.
5. Produce `Handoff_State.md`.
6. Confirm protected path was not edited.
7. Confirm all outputs cite artifact inventory or fixture files.

Expected pilot output:

```text
fixtures/domain-engine/open_pipe_stress_minimal/_DomainEngines/
  scans/
    SCAN_<timestamp>/
      ARTIFACT_INVENTORY.md
      PROFILE_STATUS.md
      MISSING_ITEMS.md
  handoffs/
    HANDOFF_<timestamp>/
      Handoff_State.md
```

Acceptance checks:

- Level 1 can run without OpenPipeStress executable.
- Output is useful for human review.
- No protected model artifact is modified.
- All unknowns are `TBD`.

### Phase 8 - Prepare Level 2 Adapter Invocation

Owner: DOMAIN_ENGINE + TOOLMAKER + external OpenPipeStress owner

Do not implement actual OpenPipeStress adapter in this repo unless OpenPipeStress source or a stable CLI is available and explicitly in scope.

Prepare:

- Adapter spec alignment.
- Mock adapter fixture or stub outputs.
- Invocation validation.
- Output capture.
- Human confirmation records.

Acceptance checks:

- Unknown tool IDs fail closed.
- Mutating tools require confirmation when profile says so.
- Output capture does not mutate domain outputs.
- `DOMAIN_CONTROLLED_WRITE` outputs are labeled as domain-controlled, not agent-written.

### Phase 9 - Prepare Level 3 Operation Proposal Workflow

Owner: DOMAIN_ENGINE + SKILLMAKER + TOOLMAKER

Implement only after Level 1 is reliable.

Tasks:

1. Finalize proposal spec.
2. Implement proposal validator.
3. Build proposal skill.
4. Create one OpenPipeStress proposal fixture.
5. Validate proposal without applying it.
6. Produce human review packet.

Acceptance checks:

- Proposal remains `proposal_only`.
- Validator catches missing evidence.
- Validator catches accepted-status claim.
- No domain model files are edited.

### Phase 10 - Harness API/UI Planning

Owner: product/frontend/backend implementation instance

Do this only after CLI tools and file contracts stabilize.

Tasks:

1. Add PRD amendment text to `docs/PRD_CANDIDATE.md` or successor PRD.
2. Design backend endpoint contracts.
3. Implement read-only profile list/validate/scan first.
4. Implement proposal list/validate.
5. Defer mutating tool invocation until confirmation and output capture are safe.

Acceptance checks:

- API cannot invoke undeclared tools.
- API cannot write protected paths directly.
- UI labels authoritative domain artifacts vs readable summaries vs proposals.

---

## 12. Work Package Breakdown

Use these work packages for tracking.

| WP | Name | Owner | Depends on | Done when |
|---|---|---|---|---|
| WP-00 | Scope confirmation | DOMAIN_ENGINE | none | Human approves Level 1 first target |
| WP-01 | Specs | DOMAIN_ENGINE | WP-00 | `docs/domain-engine/*.md` specs written |
| WP-02 | Profile validator | TOOLMAKER | WP-01 | `validate_domain_engine_profile.py` registered and tested |
| WP-03 | Artifact scanner | TOOLMAKER | WP-01 | `scan_domain_artifacts.py` registered and tested |
| WP-04 | Write path checker | TOOLMAKER | WP-01 | `check_domain_write_paths.py` registered and tested |
| WP-05 | OpenPipeStress profile | DOMAIN_ENGINE | WP-02 | draft profile validates |
| WP-06 | OpenPipeStress fixture | DOMAIN_ENGINE | WP-03 | scanner produces inventory |
| WP-07 | Profile review skill | SKILLMAKER | WP-02 | skill validates and reviews profile |
| WP-08 | Artifact review skill | SKILLMAKER | WP-03, WP-04 | skill validates and reviews fixture inventory |
| WP-09 | Invocation validator | TOOLMAKER | WP-01 | read-only and mutating examples validated |
| WP-10 | Output capture tool | TOOLMAKER | WP-09 | captures fixture tool outputs |
| WP-11 | Proposal spec/tool | DOMAIN_ENGINE/TOOLMAKER | WP-01 | proposal validator registered and tested |
| WP-12 | Proposal skill | SKILLMAKER | WP-11 | proposal-only fixture generated |
| WP-13 | Handoff skill | SKILLMAKER | WP-06 | handoff checklist fixture generated |
| WP-14 | Boundary tools | TOOLMAKER | WP-01 | boundary/private scans registered and tested |
| WP-15 | End-to-end Level 1 pilot | DOMAIN_ENGINE | WP-02..WP-08 | handoff state proves safe read-only workflow |
| WP-16 | Level 2 mock adapter pilot | DOMAIN_ENGINE/TOOLMAKER | WP-09, WP-10 | mock domain tool invocation captured safely |
| WP-17 | PRD/API/UI update | product/backend/frontend | WP-15 | `/api/domain/*` read-only endpoints scoped |

---

## 13. Acceptance Gates

### Gate A - Architecture Acceptance

Accept when:

- Human agrees DOMAIN_ENGINE is the manager.
- Specs are written or explicitly deferred.
- Level 1 is confirmed as the first implementation target.

### Gate B - Tool Foundation Acceptance

Accept when:

- Profile validator passes valid fixture and fails invalid fixture.
- Artifact scanner produces deterministic inventory.
- Write path checker denies protected paths and allows proposal paths.

### Gate C - Skill Foundation Acceptance

Accept when:

- `domain-profile-review` and `domain-artifact-review` pass skill metadata validation.
- TASK can load both skills.
- Pilot outputs have citations and no protected writes.

### Gate D - OpenPipeStress Fixture Acceptance

Accept when:

- OpenPipeStress profile validates.
- Fixture scan reports expected artifacts, missing artifacts, protected paths, and agent-writable paths.
- No proprietary/licensed content appears in fixture.

### Gate E - Level 1 Pilot Acceptance

Accept when:

- A full read-only workflow completes from profile validation through handoff state.
- All project-relevant outputs are files.
- Unknowns are `TBD`.
- Human gate points are visible.

### Gate F - Level 2 Readiness

Accept when:

- Invocation validator and output capture are ready.
- Mutating tool confirmation behavior is explicit.
- Mock adapter output can be captured without touching protected paths.

---

## 14. Validation Commands

Expected commands once implementation exists:

```sh
git diff --check
python3 tools/validation/validate_skill_metadata.py skills
python3 tools/domain_engine/validate_domain_engine_profile.py --profile docs/domain-engine/OPENPIPESTRESS_PROFILE_DRAFT.yaml
python3 tools/domain_engine/scan_domain_artifacts.py --working-root fixtures/domain-engine/open_pipe_stress_minimal --profile docs/domain-engine/OPENPIPESTRESS_PROFILE_DRAFT.yaml --output-inventory /tmp/domain_artifacts.csv --output-report /tmp/domain_artifacts.md
python3 tools/domain_engine/check_domain_write_paths.py --working-root fixtures/domain-engine/open_pipe_stress_minimal --profile docs/domain-engine/OPENPIPESTRESS_PROFILE_DRAFT.yaml --candidate fixtures/domain-engine/open_pipe_stress_minimal/PKG-01_PipingDesign/DEL-01-02_OpenPipeStressModel/OpenPipeStress/project.ops.yaml
```

Expected audit after agent-instruction changes:

```text
Run AUDIT_AGENTS on agents/AGENT_DOMAIN_ENGINE.md.
```

If tests are added, create a small test runner or documented pytest command for the new domain-engine tools. Do not rely only on manual inspection.

---

## 15. Risks And Controls

| Risk | Impact | Control |
|---|---:|---|
| Chirality becomes domain-specific | High | Keep generic profile spec; OpenPipeStress only as first profile |
| Agents mutate domain model truth | High | Protected path checker, profile policy, TASK `AllowedWriteTargets` |
| Tool invocation becomes arbitrary command execution | High | Invoke only profile-declared tools; validate tool ID and args |
| Proposal mistaken for accepted change | High | `proposal_only` schema, proposal validator, human gate |
| External validation status invented | High | boundary-language checker and external review evidence rules |
| Private/protected data leaks into generated summaries | High | private-data scan and boundary notices |
| Skills duplicate tool logic | Medium | SKILLMAKER/TOOLMAKER boundary, explicit tool policies |
| Tools embed method guidance | Medium | TOOLMAKER R12 compliance; method remains in skills |
| Fixture overfits OpenPipeStress | Medium | Add later mock second domain profile |
| API/UI built before contracts stabilize | Medium | Do API/UI after Level 1 pilot |

---

## 16. Out Of Scope For This Plan

- Implementing the OpenPipeStress solver.
- Embedding the OpenPipeStress GUI in Chirality.
- Parsing CAESAR II, AutoPIPE, or other commercial tool outputs.
- Declaring professional approval or code compliance.
- Building a runtime monitor that intercepts every file write.
- Implementing cloud/vendor integrations.
- Building multi-user concurrency controls.
- Creating a second domain engine before OpenPipeStress fixture proves the pattern.

---

## 17. Future Instance Execution Prompt

Use this prompt when resuming implementation:

```text
You are continuing the DOMAIN_ENGINE workflow buildout in chirality-app-test.

First read:
- plans/DOMAIN_ENGINE_WORKFLOW_DEVELOPMENT_PLAN.md
- agents/AGENT_DOMAIN_ENGINE.md
- agents/AGENT_HELPS_HUMANS.md
- agents/AGENT_SKILLMAKER.md
- agents/AGENT_TOOLMAKER.md
- agents/AGENT_TASK.md
- tools/REGISTRY.md
- skills/SKILL_TEMPLATE.md
- docs/thesis/bigger-picture/CHIRALITY_PRD_Amendment_Domain_Engine_Integration.md

Then determine the current phase from the work packages in Section 12.

Do not jump to adapter execution or operation proposals until:
1. Domain Engine Profile spec exists.
2. OpenPipeStress draft profile validates.
3. Artifact scanner works on a fixture.
4. Protected path checker denies canonical domain files.
5. domain-profile-review and domain-artifact-review skills exist and validate.

Preserve boundaries:
- DOMAIN_ENGINE manages.
- SKILLMAKER owns skills.
- TOOLMAKER owns deterministic tools.
- TASK executes bounded skills.
- Domain engines own domain truth.
- Humans accept.

At the end of each implementation slice:
- run relevant validation commands,
- update this plan or DOMAIN_ENGINE_IMPLEMENTATION_STATUS.md,
- report changed files and remaining blockers.
```

---

## 18. Minimum Viable Next Slice

If the future instance has limited time, do this first:

1. Create `docs/domain-engine/DOMAIN_ENGINE_PROFILE_SPEC.md`.
2. Create `docs/domain-engine/DOMAIN_WRITE_BOUNDARY_POLICY.md`.
3. Create `docs/domain-engine/OPENPIPESTRESS_PROFILE_DRAFT.yaml`.
4. Implement `tools/domain_engine/validate_domain_engine_profile.py`.
5. Register the tool in `tools/REGISTRY.md`.
6. Add a minimal valid/invalid profile fixture or documented smoke command.
7. Run `git diff --check`.
8. Report what remains.

This gives the workflow its first enforceable contract. Everything else depends on it.

