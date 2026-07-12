# Handoff State — D-GOV-11 Agent Hierarchy Refactor

Status: OWNER RULINGS TRANSCRIBED / PROTO-RUN INTEGRATION AND FINAL VALIDATION PENDING
DecisionBasis: `docs/governance_harness/_DECISIONS/D-GOV-11_runtime_agent_hierarchy.md`; `docs/governance_harness/_DECISIONS/D-GOV-12_multi_agent_orchestration.md`
Branch: `codex/agent-governance-redesign`

## Accepted Direction

- HELP_HUMAN is sole Agent 0 Supervising Architect.
- Agent 1 managers are direct human entry points and may run under Agent 0.
- Agent 2 may be TASK, ephemeral generalist, or approved dedicated specialist.
- Standards are external constraints, not agents.
- Runtime delegation is hierarchical; filesystem and Git state provide many-to-many coordination.
- EVALUATION owns generic audit/reconciliation semantics.
- RECONCILIATION is reserved for deliverable-corpus concordance.
- PDF2MD and DRAWING_EXTRACT remain Agent 1.
- Terminal fan-out/fan-in and supervised many-to-many agency are complementary
  canonical patterns; mixed work graphs are allowed.
- WORKING_ITEMS is a package-level Agent 1 and SOFTWARE_DEV is deferred.

## Implemented in This Instruction Tranche

- Canonical doctrine in `AGENTS.md`; exact `CLAUDE.md` import and validator/export enforcement.
- HELPS_HUMANS consolidated component design, skill/tool design, context transposition, and decomposition-component design.
- HELP_HUMAN rewritten as sole read-only Agent 0 with managed delegation; durable launch briefs are runtime evidence, not an execution fallback.
- `docs/DECOMPOSITION_STANDARD.md` extracted; DECOMP_BASE persona removed and live managers rebound.
- EVALUATION expanded; old generic RECONCILIATION semantics transferred.
- RECONCILIATION activated from the ratified method and integrated app-dev and
  piping calibration/pause evidence.
- SCHEDULING merged into ORCHESTRATOR; SKILLMAKER, TOOLMAKER, CONTEXT_TRANSPOSE, and SCHEDULING persona files removed after live caller redirection.
- PDF2MD and DRAWING_EXTRACT source/target calibration and novel-generalist semantics added.
- D-GOV-12 doctrine, package-level WORKING_ITEMS, cross-package HELP_HUMAN,
  orchestration vocabulary, and managed-runtime record schema added.
- DBM, disposition matrix, TYPES, DIRECTIVE, README, professional-engineering mapping, roadmap, validators, skill/tool ownership, and export contract updated.
- App-dev and piping loops now use package-level WORKING_ITEMS work graphs.
- Project software profiles, five software TASK skills, and deterministic
  discovery/check/scope/comparison/drift tools are live.
- Managed child sessions, terminal/background execution, coordination notices,
  updates, amendments, acknowledgments, runtime records, actual named
  instruction loading, and fail-closed retirement of the record-less SDK
  compatibility path are implemented.
- Completion-audit hardening enforces child read scopes and write targets at
  permission/hook boundaries, fails closed on unbounded managed Bash, validates
  return markers, versions replans, injects updates at safe turn boundaries,
  requires acknowledgments, reconstructs handoff state, and isolates failures.
- Current generic audit and REVIEW snapshots write under `_Evaluation/`;
  historical generic `_Reconciliation/` snapshots remain immutable evidence.
  RECONCILIATION alone owns new deliverable-corpus concordance runs.
- D-GOV-13 records the approved fourteen-role requalification baseline with
  persistent output/recovery and live-reference compatibility evidence. Named
  execution remains subject to every declared runtime gate.

## Validation Evidence

The review-remediation candidate currently has the following verified evidence:

- App-dev runtime: the complete Vitest suite passes 94 files (one skipped),
  686 tests (four skipped); TypeScript typechecking passes; the focused managed
  delegation and coordination suite passes 16 tests.
- Root governance/tool checks: instruction entrypoints pass; all 43 live skills
  validate; 433 live path-anchor surfaces pass; 42 targeted review-remediation
  Python tests pass; `git diff --check origin/main` reports no whitespace
  errors.
- The public derivative regenerates with 583 files and zero boundary findings.
- Before the ruling, the agent validator reported only the fourteen
  `TYPE2_APPROVAL_NOT_RULED` authority-gate errors and no warnings. Post-ruling
  validation is part of the publication checks below.

The following was the accepted pre-review evidence at PR #188 head before the
review-remediation tranche. It is retained as historical evidence, not as a
claim about the current unvalidated remediation tree:

- Root governance/tool suite: 762 tests passed. Agent hierarchy/output-root,
  project-loop/entrypoint, skill, and path validators pass with 33 agent
  packages at zero errors and zero warnings and all 43 live skills valid.
- App-dev runtime: TypeScript typecheck passed; the complete Vitest suite passed
  94 files (one skipped), 682 tests (four skipped). The unsigned desktop package
  built; packaged instruction-root integrity passed; the live premerge probe
  passed 8 Section 8 scenarios and 16 Section 9 gates.
- Piping: the complete evidence sweep passed 36 Rust crate tests, 459 Python
  tests, 471 desktop unit/component tests, 18 development browser-flow tests,
  the production-distribution WASM test, and the desktop production build.
- Path-anchor and instruction-entrypoint validators passed. `git diff --check`
  reported no whitespace errors.
- Public derivative regenerated from the audit-repair commit with 585 manifest
  entries and zero boundary findings. Its staging tree independently passed the
  agent, instruction-entrypoint, skill-metadata, and path-anchor validators.

## Deferred Evolution

- Continue slimming retained Agent 1 roles around human decisions and handoffs
  when use evidence identifies a safe replacement-first migration.
- Reconsider `SOFTWARE_DEV` only if WORKING_ITEMS plus the software activation
  profile, TASK skills, and deterministic tools prove insufficient in practice.

## Integration Hold

The owner ratified the three standards and approved D-GOV-13 through D-GOV-14.
The app-dev and piping reconciliation proto-runs have resumed under their
pinned methods. PR #188 must not merge until both produce stable terminal
handoffs, their accepted changes integrate, this branch rebases onto that
state, and full packaging, live-premerge, piping-sensitive, and independent
public-staging validation passes.

## Required Resume Sequence

1. Publish the owner ruling and backfill its immutable ruling SHA.
2. Allow both reconciliation proto-runs to finish under their pinned methods
   and produce the D-GOV-14 item 8 terminal evidence.
3. Integrate their accepted changes, rebase PR #188, and resolve any instruction,
   loop, index, runtime, or export conflicts.
4. Regenerate and validate every affected root and project surface, then merge
   PR #188 only when hosted and local acceptance evidence is green.

## Closure Verdict

Instruction tranche: OWNER-RULED; INTEGRATION HOLD ACTIVE.
RECONCILIATION activation: COMPLETE.
Runtime bridge: REMEDIATED; CORE TESTS PASS, FULL ACCEPTANCE PENDING.
Overall D-GOV-11 implementation: owner-approved, pending proto-run integration,
final rebase, full acceptance validation, and merge.
