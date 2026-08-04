# Sealed Agent 2 brief — D-APP-88 helper bundle resume R3

## Identity and method

- RequestedBy: App `HELP_HUMAN`
- RunID: `APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04`
- ParentInstanceID: `WI-PKG09-DAPP88-R3`
- ChildInstanceID: `A2-DAPP88-R3-IMPLEMENT-01`
- Role: Agent 2 `TASK`; no delegation
- TaskSkill: `software-bounded-implementation`
- ScopePath: `projects/chirality-app-dev/execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-04_macOS_DMG_Packaging_and_Instruction_Root_Integrity`
- WorkingRoot: `projects/chirality-app-dev`
- Profile: `projects/chirality-app-dev/software-workflow.json`
- ApplyEdits: `true`

Read root `AGENTS.md`, `agents/AGENT_TASK.md`, `docs/SOFTWARE_WORKFLOW_PROFILE.md`,
the selected skill plus all companion files, this brief, the R3 activation,
work graph and Root fitness report, D-APP-88 packet/ruling, DEL-09-04 kit, Root
notice and accepted Root bytes/evidence, and the complete R2 manager return,
handoff, verifier return, candidate-source manifest, package manifest and frozen
candidate source. R2 is immutable diagnostic/reconstruction input, not accepted
product state.

## Objective

Rebuild a source-aligned, separately built full Electron runtime-helper `.app`
from the frozen R2 candidate evidence, carefully reconciling onto the current
D-APP-89/D-APP-91 source state. Then build and exercise exact final packaged
bits against the accepted Root repair, capture auditable post-GUI first-signal
process/socket proof, and execute the complete D-APP-88 Option B validation
conjunction. Do not copy/mutate the finished GUI bundle and do not introduce a
signal wrapper.

## Allowed writes

- bounded `projects/chirality-app-dev/frontend/electron/**` helper integration;
- bounded `projects/chirality-app-dev/frontend/scripts/**` build/proof support;
- bounded helper/IPC/CLI tests under `projects/chirality-app-dev/frontend/src/__tests__/**`;
- `projects/chirality-app-dev/frontend/electron-builder.runtime-helper.json`;
- `projects/chirality-app-dev/frontend/package.json` and `package-lock.json` only where genuinely required;
- one new TASK run record under DEL-09-04 `_run_records/**`;
- this R3 run root's `instances/A2-DAPP88-R3-IMPLEMENT-01/**`, implementation return, telemetry-supporting records, and evidence.

Do not write DEL-09-04 `_STATUS.md` or `MEMORY.md`; the manager owns reconciliation.
Do not write decision/TM registers, loop receipt, completion log, other
deliverables/packages, Root runtime/docs, Piping/PEC/domain engines,
PRD/decomposition/SCOPE_CHANGE, or Git. Preserve D-APP-89 rollback state,
D-APP-91 planning-only scope, and all six D-APP-81 UNKNOWN relations.

## Allowed tools and command authority

Use repository reads, `apply_patch`, and ordinary local bash commands necessary
for the explicitly named implementation, package drills, cleanup, and checks.
This brief explicitly authorizes the named npm/Electron/macOS/process/socket
commands needed for D-APP-88 evidence; the TASK skill's registered helper tools
remain preferred where applicable, but do not misreport a five-command-only
tool policy. Never use network/provider calls, reveal token contents, install
software, write outside the worktree, or perform Git mutations.

Named validation commands from `frontend/`, where lawful and feasible:

- focused Vitest for desktop-daemon-posture, runtime-control IPC, CLI launcher,
  helper packaging, and Desktop/CLI shared-daemon integration;
- `npm test`;
- `npm run typecheck`;
- `npm run build`;
- `npm run desktop:pack`;
- `npm run desktop:verify-dependencies`;
- `npm run instruction-root:integrity`;
- `npm run harness:validate:premerge` using the registered isolated managed service;
- `npm run validate:release-quality`; and
- App hold, authority-corpus status, loop receipt, repo self-check, full
  practitioner pytest, scope/whitespace/diff, D-APP-89 zero-consumer, and
  D-APP-81 UNKNOWN preservation checks.

Use `tools/software_workflow/run_registered_checks.py` for registered checks
where its profile applies. If a named command is infeasible, record the exact
reason and acceptance consequence; do not silently substitute weaker evidence.

## Required implementation and evidence

1. Reconstruct the frozen R2 source set by exact file comparison and hunk-wise
   reconciliation; do not overwrite unrelated current changes. Bind before/after
   source hashes in a source manifest.
2. Produce the explicit helper builder config, helper entry/output, and
   deterministic whole-bundle embedding step. Helper identity is
   `com.chirality.app.runtime-helper`, GUI identity remains `com.chirality.app`,
   helper is `LSUIElement`, and child topology must be builder-generated.
3. Prove standalone and embedded helper trees are identical, relocatable, and
   contain exactly one top-level helper with only relative internal symlinks.
4. Prove LaunchAgent `ProgramArguments` and packaged CLI bind the standalone
   helper executable.
5. On exact final packaged bits, prove all of:
   - job-equivalent launch starts helper/daemon posture without a real login;
   - exactly one Root daemon/runtime singleton and shared socket/auth/session/project stores;
   - safeStorage continuity without touching/prompting the owner's login keychain;
   - GUI contact does not replace or retire the healthy daemon;
   - the first post-GUI `SIGTERM`/ordinary stop is auditable: preserve the exact
     signal command identity/time, pre/post process snapshots, control-socket and
     owner-record snapshots, daemon shutdown logs, and bounded termination/cleanup;
   - restart after graceful stop and recover-on-start after SIGKILL are bounded;
   - helper resources, asar, native modules, runtime CLI, and instruction root are intact;
   - no TCP listener, token disclosure, global Node dependency, extra singleton,
     forbidden app listener, or global runtime dependency is introduced.
6. Preserve sanitized logs, plist extracts, hashes, commands, process/socket
   snapshots, package topology, complete acceptance matrix, and exact cleanup.
   Never read or print token values.
7. Clean only the exact processes/jobs/plists/temp trees/sockets/credentials
   created by this run. Leave unrelated owner/concurrent state untouched.

## Expected outputs

- source and package manifests;
- complete D-APP-88 acceptance matrix and drill report;
- normalized validation results;
- cleanup and rollback manifests;
- one final implementation return with exact source/package/evidence hashes,
  limitations, reruns, and provisional `PASS` or truthful `BLOCKED` verdict;
- one immutable DEL-09-04 TASK run record; and
- runtime telemetry with matched start/finish events where the runtime exposes it.

## Stop/escalation conditions

Stop and return an exact blocker if work would require a new generic Root
semantic, unaccepted evidence, scope expansion, owner-machine deployment,
network/provider access, release/signing/notarization/publication/distribution,
DMG work, or a weakening of any mandatory D-APP-88 conjunct. Inability to
produce auditable post-GUI first-signal proof is blocking. Node 22.19 remains
an explicit compatibility limitation, not a reason to claim coverage.
