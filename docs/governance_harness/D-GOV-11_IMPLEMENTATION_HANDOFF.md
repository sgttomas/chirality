# Handoff State — D-GOV-11 Agent Hierarchy Refactor

Status: OWNER RULINGS TRANSCRIBED / PROTO-RUNS INTEGRATED / FINAL VALIDATION IN PROGRESS
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

The owner-ruled, SHA-bound candidate currently has the following verified
evidence:

- App-dev integration checkpoint: the complete merged Vitest suite passes 97
  files (one skipped), 699 tests (four skipped); TypeScript typechecking and
  generated tool-catalog identity pass. The D-APP-55 R6 handoff is
  `CLOSED / PASS` with no concordance blocker.
- Root governance/tool checks: instruction entrypoints pass; all 43 live skills
  validate; all 33 agent packages validate with zero errors and warnings; 433
  live path-anchor surfaces pass; 42 targeted review-remediation Python tests
  pass; the complete practitioner governance harness passes 264 tests; and
  `git diff --check origin/main` reports no whitespace errors.
- After app-dev integration, 434 live path-anchor surfaces pass. The public
  derivative regenerates with 584 files and zero boundary findings.
  Its independent staging tree passes all 33 agent packages, all 43 skills,
  canonical instruction entrypoints, and the exported path-anchor validator.
- D-GOV-13 and D-GOV-14 are bound to ruling publication commit
  `d22f80bf5d6c1190ce151df75d936bfcf4d38bc3`; the post-ruling validator no
  longer emits `TYPE2_APPROVAL_NOT_RULED`.

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

The owner ratified the three standards and approved D-GOV-13 through D-GOV-14,
published at `d22f80bf5d6c1190ce151df75d936bfcf4d38bc3`.
The app-dev proto-run is `CLOSED / PASS`; its accepted changes and R6 terminal
handoff are integrated from `main`. The piping D-41 proto-run is also closed;
its distributed terminal package and accepted R4/R5 changes are integrated
from `main`. The owner confirmed on 2026-07-12 that a
non-rewriting merge of `main` satisfies D-GOV-14 item 8 in place of a literal
history-rewriting rebase, preserving the SHA-bound D-GOV-13/D-GOV-14 ruling
commits. PR #188 must not merge until full packaging, live-premerge,
piping-sensitive, independent public-staging, and completion-audit validation
passes.

## Required Resume Sequence

1. Regenerate and validate every affected root and project surface.
2. Re-audit every PR #188 review finding against the final integrated tree.
3. Merge
   PR #188 only when hosted and local acceptance evidence is green.

## Closure Verdict

Instruction tranche: OWNER-RULED; FINAL VALIDATION IN PROGRESS.
RECONCILIATION activation: COMPLETE.
Runtime bridge: REMEDIATED; CORE TESTS PASS, FULL ACCEPTANCE PENDING.
Overall D-GOV-11 implementation: owner-approved; both proto-runs integrated;
pending completion audit, full acceptance validation, and merge.
