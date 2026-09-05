# Sealed TASK implementation brief
RequestedBy: HELP_HUMAN through WORKING_ITEMS pkg07
RunID: APP_LOOP_SHELL_2026-09-05
ParentInstanceID: pkg07
ChildInstanceID: workflow-author
PackageID: PKG-07
DeliverableIDs: [DEL-07-03]
TaskSkill: software-bounded-implementation
ApplyEdits: true
PROFILE_PATH: {WORKING_ROOT}/software-workflow.json
ScopePath: {WORKING_ROOT}/execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/instances/pkg07/workflow-author

Resolve REPO_ROOT with git rev-parse --show-toplevel; WORKING_ROOT={REPO_ROOT}/projects/chirality-app-dev. Act TASK Agent 2; no descendants. Read actual agents/AGENT_TASK.md, skills/software-bounded-implementation/SKILL.md and companions, root/project AGENTS and source files below. Native class delegated-harness-native, role instruction-asserted; actual model GPT-6 per parent, exact serving ID unavailable; no model override.

Objective: implement DEL-07-03-V3-01 governed workflow file contract OUT-001/AC-001/VER-001.
AcceptedBasis: live carrier ScopeOfWork SCA-APP-010 controlling section/decomposition dbd812a52d5ed0cb3ed173f3aaaa68703a914291; D-APP-108 Q16; target plans/shell-redesign_2026-09-04/03_TARGET_SPEC.md SHA256 d1643e3cf8156b7084b370aa8624bd5e87a75bfb4c0cd7b3a2552a4cbef82b45 section5.10; plan SHA e25fbe82f675e9f282803599a497ab24c6aab3f763b1e7f6db97042fed1117bb meaning only; accepted DepClosure CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034 PASS with carried warnings. Parent selection review COMMIT-SAFE; branch ready. Dependencies none. APP-HOLD dispatch preflight must pass before work and be preserved locally.

DeclaredReads: governing files above, DEL-07-03 records, docs/CONTRACT.md/SPEC.md/TYPES.md/PRD.md, frontend/src/lib/workspace and adjacent parsers/types/tests/package config, software-workflow tools.
AllowedTools: read, write, local exec; registered checks only as allowed below; no network/install/global check execution/Git mutation.
AllowedWriteTargets (relative WORKING_ROOT):
- frontend/src/lib/workspace/governed-workflow.ts
- frontend/src/__tests__/lib/governed-workflow.test.ts
- execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/instances/pkg07/workflow-author/** (includes _run_records)

EXCLUSIONS: UI/API wiring, filesystem writes to user workflows, lifecycle/truth/approval/evidence storage, Root or other-manager files, shared package files, global tests/build/check runs, dependency installation, commits. No ScopeOfWork/status edits by author. A1 frontend re-stage consequence recorded by parent; new staged revision/fresh owner proof is required for future login-proof claim.

AcceptanceCriteria:
- Pure parser/validator/serializer contract: front matter agent (Agent1 role), folder canonical absolute path, permission, policy, briefsRunOn, roadmapSource identity and SHA256, acceptedAt; roadmap ordered list with [gate] human markers; reject unknown/status/approval/evidence fields rather than persisting them.
- App-maintained current step plus who-advanced attribution; advancing position only at human gates per Q16. Explicitly document concurrent editing unsupported. Workflow is steering derivative context, never authority.
- Bind copy content resets current and attribution, rewrites canonical destination folder, retains roadmapSource identity/hash. Pure content helper; callers own actual write authorization and prerequisites; never silently auto-approve.
- Fixtures for valid examples, malformed/frontmatter duplicates, forbidden fields, malformed roadmap, gate-only attribution, retained source hashes, safe path/slug contract if exposed. Preserve acceptedAt when a source field, distinguish from stored approval record.
- Define practical API for downstream Workflows view and composer, with source currency check possible without mutation. Avoid dependencies; strict documented grammar is acceptable. Surface any source ambiguity, do not widen acceptance.

Checks: parent will run registered frontend-test/frontend-typecheck/frontend-build/frontend-premerge and harness gates serially after fresh review. No full check run here. Prepare focused test command/evidence; execute focused tests only after parent authorizes installed dependencies and exact test command. Use validate_change_scope.py where applicable. Record unrun checks honestly.
ExpectedReturn: source+tests, run record and RETURN.md under ScopePath with source identities, exact changed paths, tests/commands/status, acceptance mapping, limitations, downstream API contract, blockers. Return to pkg07 only; no direct sibling messages.
