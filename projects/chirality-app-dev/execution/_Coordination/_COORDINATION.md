# Coordination Record - Chirality App Dev

**Recorded:** 2026-06-13
**Active persona:** `WORKING_ITEMS`
**Default work mode:** bounded app-integration tranches
**Current strategic focus:** Chirality-owned agent harness runtime, with Claude Agent SDK as the current privileged adapter path and Pi as a reference / possible later backend-adapter spike.

## Active Surface

Use this coordination surface as the active entrypoint for app-integration work. Keep it lean: project truth remains in governed docs, decomposition and deliverable artifacts, source, tests, evidence records, and git history.

Primary authority and guidance:

- `/Users/ryan/ai-env/projects/chirality/AGENTS.md`
- `/Users/ryan/ai-env/projects/chirality/agents/AGENT_WORKING_ITEMS.md`
- `docs/PRD.md` - product requirements and current runtime scope
- `docs/PLAN.md` - strategic roadmap, not the active queue
- `docs/DIRECTIVE.md`
- `docs/CONTRACT.md`
- `docs/SPEC.md`
- `docs/TYPES.md`
- `docs/VALIDATION_STRATEGY.md`
- `docs/RELEASE_QUALITY_GATES.md`
- `docs/BUILD_AND_RELEASE.md`
- `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`
- `docs/README.md`
- `docs/MANIFEST.json`
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
- `frontend/docs/harness/runtime_engine_contract.md`
- `plans/PLAN_2026-06-13_runtime_completion.md` - active non-governing tranche-selection plan
- `plans/PLAN_COMPLETION_LOG.md` - landed-tranche narrative history
- `plans/chirality-app-future-development-plan.md` - seed runtime roadmap/reference
- `plans/claude-agent-sdk-implementation-followups.md` - SDK implementation reference
- `plans/pi-agent-harness-assessment.md`
- `plans/pi-assessment/*.md`
- `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
- `execution/_Coordination/NEXT_INSTANCE_STATE.md`
- `execution/_Coordination/_DECISIONS/_REGISTER.md`

## Authority And State Rules

Use two layers of state. Do not let handoff prose, completion plans, or runtime logs become substitute authority.

Authoritative state:

1. `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/TYPES.md` define requirements, invariants, mechanics, and vocabulary.
2. `docs/PLAN.md` records strategic runtime direction and roadmap rationale. It is not the ordinary active work queue.
3. `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` route evidence, release-quality checks, and local build/package evidence. They do not create release readiness, lifecycle issuance, publication authorization, or professional acceptance.
4. `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md`, `docs/README.md`, and `docs/MANIFEST.json` are workflow/index surfaces. They help discovery and orientation, but they do not replace canonical agent instructions, coordination policy, project truth, or human rulings.
5. `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` records the package/deliverable decomposition and source-governed scope basis.
6. Deliverable-local `_STATUS.md`, `MEMORY.md`, `_run_records/**`, four-document kits, dependency files, and review/evidence files carry lifecycle, working memory, and execution evidence inside their ownership boundary.
7. Current implementation truth lives in source, tests, build scripts, validation artifacts, and git history.

Guidance and history surfaces:

1. `plans/PLAN_2026-06-13_runtime_completion.md` is the active non-governing completion plan. It orders tranche selection toward the PRD and strategic roadmap.
2. `plans/PLAN_COMPLETION_LOG.md` preserves landed-tranche narrative after plan rows are compressed.
3. `execution/_Coordination/_DECISIONS/_REGISTER.md` tracks human-gated decision-packet status. Agents prepare `PROPOSAL` packets; humans rule.
4. `execution/_Coordination/NEXT_INSTANCE_STATE.md` is compact state only: pointers, current active queue, pending rulings, and update protocol. It is not authority and must not accumulate landed-tranche history.

When guidance surfaces disagree with authoritative surfaces, surface the discrepancy and correct the guidance surface. Do not silently rewrite authority.

## Baseline Intake

At the start of a new loop:

1. Read `AGENT_WORKING_ITEMS.md` and act in the `WORKING_ITEMS` persona.
2. Read this file and `NEXT_INSTANCE_PROMPT.md`.
3. Read `NEXT_INSTANCE_STATE.md` for compact pointers and queue state.
4. Read `plans/PLAN_2026-06-13_runtime_completion.md` for active tranche ordering.
5. Read `_DECISIONS/_REGISTER.md` for pending human rulings.
6. Read `docs/PRD.md`, `docs/PLAN.md`, and `frontend/docs/harness/runtime_engine_contract.md` enough to confirm the selected tranche's runtime target.
7. Read `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md` when selecting validation for governance, runtime, SDK/tool, network, packaging, build, or release-significant work.
8. Read `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md` and `docs/README.md` when changing the coordination loop or docs index.
9. Read the implementation reference surfaces needed for the selected tranche.
10. Run `git status --short` before coordination-sensitive planning or edits.

## Active Development Loop

Use bounded app-integration tranches. If a human has already approved or requested a tranche, continue it within its write bounds. Otherwise select exactly one earliest unblocked item from `plans/PLAN_2026-06-13_runtime_completion.md`.

A tranche is acceptable when it has:

- one clear objective tied to the active completion plan;
- a narrow write scope;
- a validation command or concrete manual verification target;
- all required human rulings recorded in `_DECISIONS/_REGISTER.md`;
- work contained within accepted professional-boundary, network, dependency, runtime, and release policy.

Default ordering:

1. Repair failing validation or incomplete evidence for already-landed runtime work.
2. Select the earliest unblocked item on the active completion plan's dependency spine.
3. Prepare a decision packet only when the next plan item is blocked by a human ruling and no packet exists.
4. If a packet already awaits ruling, continue to the next unblocked implementation item.
5. Stop when no current plan item remains unblocked; do not substitute unrelated hardening or out-of-stage scope.

## Subagent Use

Spawn `TASK` agents only for separable subscopes with explicit briefs and disjoint write scopes. Use fan-out/fan-in when the work naturally separates by subsystem, for example:

- runtime contract and event schema;
- SDK options and message mapping;
- session storage and replay;
- permission overlay and tool descriptor design;
- documentation / evidence update.

Every subagent brief must state:

- source files to read;
- files it may write;
- validation expected;
- whether it may modify production code or only produce assessment/docs.

Keep parallel write scopes disjoint.

## Git And Validation Closeout

At the end of a validated tranche:

1. Run the tranche-specific verification.
2. Run broader checks when the tranche touches shared runtime behavior:
   - from `frontend/`: `npm run test`;
   - from `frontend/`: `npm run typecheck`;
   - from `frontend/`: `npm run harness:validate:premerge`;
   - from `frontend/`: `npm run instruction-root:integrity`.
3. For governance/control-plane-only tranches, run static governance checks and explicitly record that frontend tests were skipped because no runtime/source files changed.
4. Route build, packaging, and release-significant changes through `docs/VALIDATION_STRATEGY.md`, `docs/RELEASE_QUALITY_GATES.md`, and `docs/BUILD_AND_RELEASE.md`.
5. Update affected rows in `plans/PLAN_2026-06-13_runtime_completion.md`.
6. Move landed narrative detail to `plans/PLAN_COMPLETION_LOG.md`; keep the plan row compressed.
7. Update `_DECISIONS/_REGISTER.md` only when a decision packet or ruling state changes.
8. Update `NEXT_INSTANCE_STATE.md` only for pointer, queue, blocker, or pending-ruling changes.
9. Record any skipped checks and why.
10. Commit and push completed validated work when validation and git state allow closeout.

Git closeout is source-control hygiene. Lifecycle issuance, release readiness, professional approval, certification, sealing, authentication, and code-compliance acceptance remain human-governed states.

## Human-Ruling Stops

Stop and surface a human-ruling request when further progress requires a change to:

- product runtime policy in `docs/PRD.md` or strategic roadmap policy in `docs/PLAN.md`;
- outbound network policy or shipped provider scope;
- package/runtime requirements for Pi-backed execution;
- write/edit/bash/tool-execution exposure beyond the current approved plan item;
- the project-truth model for sessions, transcripts, chats, runtime logs, or completion logs;
- professional-boundary claims or release-readiness posture.

Record human-gated questions in `_DECISIONS/_REGISTER.md`.
