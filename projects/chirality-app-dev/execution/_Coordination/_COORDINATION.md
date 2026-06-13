# Coordination Record - Chirality App Dev

**Recorded:** 2026-06-13
**Active persona:** `WORKING_ITEMS`
**Default work mode:** bounded app-integration tranches
**Current strategic focus:** Chirality-owned agent harness runtime, with Claude Agent SDK as the current privileged adapter path and Pi as a reference / possible later backend-adapter spike.

## Current Authority

Use this coordination surface as the active entrypoint for app-integration work.

Primary authority and guidance:

- `/Users/ryan/ai-env/projects/chirality/AGENTS.md`
- `/Users/ryan/ai-env/projects/chirality/agents/AGENT_WORKING_ITEMS.md`
- `docs/PRD.md`
- `docs/PLAN.md`
- `docs/DIRECTIVE.md`
- `docs/CONTRACT.md`
- `docs/SPEC.md`
- `docs/TYPES.md`
- `frontend/docs/harness/runtime_engine_contract.md`
- `plans/chirality-app-future-development-plan.md`
- `plans/claude-agent-sdk-implementation-followups.md`
- `plans/agent-harness-patterns-from-claw-code-assessment.md`
- `plans/pi-agent-harness-assessment.md`
- `plans/pi-assessment/*.md`
- `execution/_Coordination/NEXT_INSTANCE_PROMPT.md`
- `execution/_Coordination/NEXT_INSTANCE_STATE.md`
- `execution/_Coordination/_DECISIONS/_REGISTER.md`

## Baseline Intake

At the start of a new loop:

1. Read `AGENT_WORKING_ITEMS.md` and act in the `WORKING_ITEMS` persona.
2. Read this file and `NEXT_INSTANCE_PROMPT.md`.
3. Read `NEXT_INSTANCE_STATE.md` for the current active tranche queue.
4. Read `docs/PRD.md` and `docs/PLAN.md` enough to confirm the current runtime target.
5. Read `frontend/docs/harness/runtime_engine_contract.md` before changing adapter, event, or session behavior.
6. Read the relevant plan surfaces for the selected tranche:
   - current runtime roadmap: `plans/chirality-app-future-development-plan.md`;
   - Claude SDK implementation details: `plans/claude-agent-sdk-implementation-followups.md`;
   - Pi reference and adapter implications: `plans/pi-agent-harness-assessment.md`.
7. Run `git status --short` before planning edits and again before closeout.

## Active Development Loop

Use bounded app-integration tranches. A tranche is acceptable when it has:

- one clear objective tied to the runtime roadmap or accepted plan surfaces;
- a narrow write scope;
- a validation command or concrete manual verification target;
- all required human rulings recorded in `_DECISIONS/_REGISTER.md`;
- work contained within accepted professional-boundary, network, dependency, and release policy.

Default tranche ordering:

1. Repair or complete validation for already-landed runtime surfaces.
2. Generalize Chirality-owned contracts that are still Claude/SDK-shaped.
3. Extract route-owned lifecycle into runtime services where already planned.
4. Expand `HarnessEvent` and session evidence toward message/tool/queue/compaction coverage.
5. Define `HarnessToolDescriptor` and deny-first permission semantics before exposing new tools.
6. Continue Claude Agent SDK R0/R1 hardening before R2+ tool expansion.
7. Use Pi as reference/design input, with any runtime-adapter spike handled as a separate approved tranche.

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
3. Record any skipped checks and why.
4. Update `NEXT_INSTANCE_STATE.md` if the active queue, blockers, or next recommended tranche changed.
5. Commit and push completed validated work when validation and git state allow closeout.

Git closeout is source-control hygiene. Lifecycle issuance, release readiness, professional approval, certification, sealing, authentication, and code-compliance acceptance remain human-governed states.

## Human-Ruling Stops

Stop and surface a human-ruling request when further progress requires a change to:

- product runtime policy in `docs/PRD.md` or `docs/PLAN.md`;
- outbound network policy or shipped provider scope;
- package/runtime requirements for Pi-backed execution;
- write/edit/bash/tool-execution exposure;
- the project-truth model for sessions, transcripts, chats, or runtime logs;
- professional-boundary claims or release-readiness posture.

Record human-gated questions in `_DECISIONS/_REGISTER.md`.
