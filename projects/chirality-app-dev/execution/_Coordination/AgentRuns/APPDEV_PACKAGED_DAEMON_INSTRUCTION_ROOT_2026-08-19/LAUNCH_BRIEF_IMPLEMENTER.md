# Sealed Agent 2 brief — D-APP-100 implementation

- RequestedBy: `HELP_HUMAN -> WORKING_ITEMS`
- RunID: `APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19`
- ParentInstanceID: `AGENT1-PKG09-WORKING-ITEMS`
- ChildInstanceID: `A2-DAPP100-IMPLEMENT-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- TaskSkill: `software-bounded-implementation`
- ApplyEdits: `true`
- Objective: implement D-APP-100 with the smallest coherent app-owned source/test/proof diff: packaged daemon must obtain the manifest-resolved instruction root used by app/CLI, packaged-resources fallback is legal only if manifest resolution is unavailable and must be logged, app/CLI/daemon agreement is regression-tested, and the unsigned package has an executable isolation proof.
- AcceptedBasis: branch base `219f695d348f1d83ba904ef4dd38781636b423a6`; exact ruling `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-100_RULING_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-17.md`; frozen activation/work graph in this run root; existing manifest `projects/chirality-app-dev/chirality.project.json` resolves `instructionRoot: ../..` through the registered project contract.
- Dependencies: current app/runtime client contracts and already-registered project state; do not alter them.
- DeclaredReads: root and project `AGENTS.md`; `agents/AGENT_TASK.md`; `skills/software-bounded-implementation/SKILL.md`; `docs/SOFTWARE_WORKFLOW_PROFILE.md`; project `software-workflow.json`; D-APP-100; DEL-09-04 SOW/status/memory/context/dependencies/references; `chirality.project.json`; relevant `frontend/electron/**`, `frontend/scripts/**`, `frontend/src/__tests__/**`, frontend package/build config, and read-only `runtime/packages/{contracts,client,core,cli}/**` needed to understand manifest root resolution.
- AllowedTools: repository read/search; `apply_patch`; package-local npm test/typecheck/build/pack commands already defined in `frontend/package.json`; registered software-workflow checks; existing project-local verification scripts. Exact Electron/package host proof may be requested with sandbox escalation. No installs or network.
- AllowedWriteTargets: `projects/chirality-app-dev/frontend/electron/**`; `projects/chirality-app-dev/frontend/src/__tests__/**`; `projects/chirality-app-dev/frontend/scripts/**`; `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19/IMPLEMENTER_RETURN.md`.
- ExpectedOutputs: minimal production implementation; focused agreement regression; deterministic packaged-under-isolation proof entry using existing packaging conventions; concise implementer return with exact changed paths, commands/results, scope proof, residual risks, and any host-proof command still owed.
- AcceptanceCriteria:
  1. Packaged daemon derives instruction root from the same registered manifest root that governs app/CLI behavior, without using repository cwd or a per-process packaged-resource default when that root resolves.
  2. Packaged resources fallback occurs only after manifest root resolution is unavailable and emits an explicit structured desktop-daemon log event containing the chosen fallback path and reason without secrets.
  3. Regression proves app, bundled CLI context, and packaged daemon agree on the resolved root and fails against the prior packaged-daemon resources-path branch.
  4. Isolation proof exercises a freshly unsigned packed app/daemon without ambient `CHIRALITY_INSTRUCTION_ROOT`, global Node, or repository cwd, and captures exact evidence; if sandbox prevents execution, return the exact command requiring manager escalation rather than inferring success.
  5. Focused tests pass; run other authorized checks proportional to the changed paths and report any check left for manager fan-in.
  6. No path outside AllowedWriteTargets changes.
- EXCLUSIONS: no root `runtime/**` writes; no manifest semantics or registration mutation; no dependencies/lockfiles; no DEL status/memory/run-record/receipt/plan/decision/register writes; no lifecycle or Approval-SHA act; no signing, notarization, distribution, release-readiness claim, provider/network expansion, owner-machine deployment, Git commit, or push.
- Escalation: stop and return a precise blocker if the ruling cannot be satisfied without excluded root runtime/manifest/public-contract changes or a new dependency.
- ExpectedReturn: code-first summary, exact path list, evidence, containment, risks, and host rerun needs.
