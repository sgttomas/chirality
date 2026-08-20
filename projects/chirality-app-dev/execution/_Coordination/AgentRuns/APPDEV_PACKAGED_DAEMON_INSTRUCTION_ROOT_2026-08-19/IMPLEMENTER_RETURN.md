# Implementer return — A2-DAPP100-IMPLEMENT-01

- RunID: `APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19`
- ChildInstanceID: `A2-DAPP100-IMPLEMENT-01`
- PackageID: `PKG-09`
- DeliverableID: `DEL-09-04`
- TaskSkill: `software-bounded-implementation` v1
- Status: `IMPLEMENTED — MANAGER CHECK/PROOF FAN-IN REQUIRED`

## Product result

Packaged daemon startup now asks the app-dev `ProjectRegistry` for
`roots(DESKTOP_PROJECT_ID)` before assigning `CHIRALITY_INSTRUCTION_ROOT`.
That path is the registered-manifest resolution already consumed by app and
bundled-CLI runtime requests. The previous per-process packaged-resources
default no longer wins when a registered root resolves.

If registry/manifest resolution is unavailable, the daemon uses packaged
resources and emits `runtime.daemon.instruction_root.fallback` to the durable
desktop-daemon log with only the selected fallback path and a classified reason
code. Unclassified error text is not logged. Successful resolution emits
`runtime.daemon.instruction_root.resolved` with project ID, root, and source.

An executable isolation proof now performs the existing unsigned
`desktop:pack`, launches the embedded app/daemon and bundled CLI from a temporary
non-repository cwd with a sparse PATH and no `CHIRALITY_INSTRUCTION_ROOT`,
registers the manifest through the bundled CLI, restarts the daemon, verifies
the manifest-resolved log event and CLI registration, launches the packaged GUI,
checks for no distribution signature, and writes exact commands/logs/checks to
`frontend/artifacts/harness/packaged-daemon-instruction-root/latest/summary.json`.

## Changed paths

- `projects/chirality-app-dev/frontend/electron/daemon-instruction-root.ts`
- `projects/chirality-app-dev/frontend/electron/main.ts`
- `projects/chirality-app-dev/frontend/scripts/run-packaged-daemon-instruction-root-proof.mjs`
- `projects/chirality-app-dev/frontend/src/__tests__/electron/daemon-instruction-root.test.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts`
- `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19/IMPLEMENTER_RETURN.md`

## Checks and evidence

- `APP-HOLD-1 accepted-dependency-consumption`, `DEL-09-04`: `ALLOW`; register
  SHA-256 `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`.
- Focused resolver/wiring regression, using the compatible read-only Vitest
  installation in the main checkout: `PASS`, 1 file / 4 tests.
  Command:
  `NODE_PATH=/Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules/.bin/vitest run src/__tests__/electron/daemon-instruction-root.test.ts`
- Proof entry syntax: `node --check frontend/scripts/run-packaged-daemon-instruction-root-proof.mjs` — `PASS`.
- `git diff --check` — `PASS`.
- `python3 tools/software_workflow/validate_change_scope.py ... --path <each changed product/test/proof path>` — `PASS`, zero violations.
- `python3 tools/practitioner_harness/harness.py self-check` — exit `0`; existing repository REVIEW/WARN findings remain outside this node.
- `python3 execution/_Scripts/app_hold.py scan --require-register-match` from the app working root — `PASS`, `held_count: 0`, register match true.
- Registered-check selection for the product/test paths: `frontend-test`,
  `frontend-typecheck`, `harness-self-check`, and `app-hold-integrity`.

## Checks not inferred

- The worktree has no installed frontend dependency tree. Direct
  `npm test -- --run ...` stopped before execution with `vitest: command not found`.
- The agreement integration test could not load
  `@chirality/engine-pi-omlx` when Vitest was borrowed read-only from another
  checkout; the new four-test resolver/wiring file passed in that same run.
- Electron typecheck attempted with the borrowed compiler, but module/type
  resolution failed on absent local dependencies (`electron`, `next`, SDK/MCP/
  Pi packages) before a meaningful project typecheck. No typecheck pass is claimed.
- No packed app exists at `frontend/dist/mac-arm64/Chirality.app`; therefore the
  packaged isolation proof was not run and no packaged pass is claimed.

Manager fan-in should run, after making the already-declared dependency tree
available without changing dependency or lockfile state:

```sh
cd projects/chirality-app-dev/frontend
npm test -- --run src/__tests__/electron/daemon-instruction-root.test.ts src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts
npm run typecheck
npm run build
npm run desktop:pack
node ./scripts/run-packaged-daemon-instruction-root-proof.mjs --skip-pack
```

The last two commands require a macOS arm64 host able to launch Electron. If the
sandbox blocks that surface, request escalation for this exact combined command:

```sh
cd projects/chirality-app-dev/frontend && npm run desktop:pack && node ./scripts/run-packaged-daemon-instruction-root-proof.mjs --skip-pack
```

## Containment

All implementation, test, proof, and return writes are within the sealed
`AllowedWriteTargets`. No root `runtime/**`, manifest, dependency, lockfile,
deliverable truth, decision, register, plan, lifecycle, Approval-SHA, receipt,
or Git state was changed. No commit or push was performed. Parent-owned
activation/work-graph files pre-existed this child and were not modified.

## Residual risks and blockers

- Fresh full test, typecheck, build/pack, packaged integrity, and isolation-proof
  results remain manager-owned evidence gates because dependencies and a packed
  app are absent in this worktree.
- The packaged fallback intentionally permits bootstrapping an unregistered
  runtime. Its durable reason is classified rather than carrying raw exception
  text; deeper failure detail remains available through the runtime's existing
  project-registration diagnostics.
- Independent read-only review over 100% of this diff remains required before
  publication.

## TASK return shape

- `RUN_STATUS:` `SUCCESS` for bounded implementation outputs; acceptance remains with manager fan-in.
- `ControlSurface:` `FILE`
- `TaskProfile:` `NONE`
- `TaskSkill:` `software-bounded-implementation`
- `ScopePath:` `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_PACKAGED_DAEMON_INSTRUCTION_ROOT_2026-08-19`
- `ResolvedSkillPath:` `skills/software-bounded-implementation`
- `ResolvedSkillVersion:` `1`
- `ResolvedTaskProfileRequirement:` `NONE`
- `CompanionFiles:` `BRIEF_SCHEMA.md (found), TOOL_POLICY.md (found), QA_CHECKS.md (found)`
- `WriteAuthorization:` `ALLOWED_WRITE_TARGETS`
- `ToolPolicyCompliance:` `PASS`
- `MISSING:` full registered checks and host proof listed above
- `NEEDS_HUMAN_RULING:` none
- `DEPENDENCY_NOTES:` none
