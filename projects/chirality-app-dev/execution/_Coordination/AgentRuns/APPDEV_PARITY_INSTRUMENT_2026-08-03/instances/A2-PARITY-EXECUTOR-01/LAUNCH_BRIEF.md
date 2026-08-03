# Sealed Launch Brief — A2-PARITY-EXECUTOR-01

RequestedBy: `WI-PKG09-DAPP86-A`

RunID: `APPDEV_PARITY_INSTRUMENT_2026-08-03`

ParentInstanceID: `WI-PKG09-DAPP86-A`

ChildInstanceID: `A2-PARITY-EXECUTOR-01`

PackageID: `PKG-09`

DeliverableID: `DEL-09-04`

## One objective

Execute the D-APP-86 Option A integrated parity instrument exactly as frozen
in `ACTIVATION.md`, using one source snapshot, one unsigned packaged App, one
isolated packaged daemon/App posture, and one evidence manifest for all four
required observations.

## Declared reads

- `AGENTS.md`, App loop instructions and committed selected workplan;
- `agents/AGENT_TASK.md` as the Agent-2 base contract;
- D-APP-86 packet/ruling and the activation/work graph;
- DEL-09-04, DEL-02-02, DEL-08-02, and DEL-05-04 current
  ScopeOfWork/context/status/references;
- `docs/SOFTWARE_WORKFLOW_PROFILE.md` and App `software-workflow.json`;
- D-APP-89 accepted return/handoff and D-APP-88 R2 blocked return/handoff;
- the smallest relevant frontend Electron/runtime/UI/API/test/script surface;
- prior App packaged-drill and Woven evidence only as method history, never as
  current proof.

## Allowed tools

- Read/search/diff/hash/process/filesystem commands necessary for the sealed
  local proof.
- Exact App `npm` commands in the D-APP-86 validation contract and focused
  Vitest targets.
- The already-built local package/runtime executables and local loopback/Unix
  socket clients needed for the isolated proof.
- Computer Use through `node_repl + @oai/sky` for native App UI inspection and
  interaction; read that skill in full first. Launch the package through the
  explicitly isolated terminal environment, not by asking Computer Use to
  launch a default-identity App. Use current accessibility state before each
  action, prefer element indices, and capture window-scoped evidence only.

This brief authorizes bounded Bash/tool use for this proof instance; it does
not change Agent-2 product capability policy or D-APP-84 H1.

## Allowed write targets

- `execution/_Coordination/AgentRuns/APPDEV_PARITY_INSTRUMENT_2026-08-03/`
  except parent-frozen `ACTIVATION.md`, `WORK_GRAPH.md`, and this brief;
- ignored/generated `frontend/.next/`, `frontend/dist/`,
  `frontend/dist-electron/`, and `frontend/artifacts/` only through the exact
  build/package/validation commands;
- one fresh, explicitly named isolated temporary root under `/private/tmp/` or
  another manager-approved private temporary location.

No tracked product/config/test/document edit is allowed. Do not stage,
commit, branch, push, reset, checkout, clean, or delete shared ignored output.
Do not alter or remove `frontend/node_modules`.

## Required execution contract

1. Freeze before-build evidence: exact HEAD/branch, dirty status, runtime
   versions, all current frontend source/config file hashes needed to reproduce
   the package, D-APP-89 zero-consumer guard, and an exact current diff digest.
2. Snapshot potentially live owner Chirality processes/state read-only. Use a
   fresh absolute `CHIRALITY_USER_DATA`, isolated runtime root, and direct
   packaged executable launch. Never touch the owner's real userData,
   LaunchAgent, installed launcher, registered projects, or credentials.
3. Stop unrelated local App dev servers before build/pack/premerge. Build
   exactly one unsigned local package with `npm run desktop:pack`; freeze its
   identity/content manifest and reuse those exact bytes for all observations.
4. Start a packaged daemon and packaged GUI in the isolated posture. Register
   only this worktree's App manifest. Ensure the stub adapter is selected and
   no provider credential/network path is used. Produce one real daemon-owned
   recorded session and a completed turn whose persisted events can yield at
   least one transcript item.
5. Through the packaged UI, capture equivalent persistent state for each
   observation (accessibility tree plus window-scoped PNG where available):
   Workbench opens/returns with its governed Documents/evidence boundary;
   Pipeline opens/returns with its governed dispatch boundary; navigator
   selection changes to the exact created recorded session while the primary
   dialogue remains mounted and no in-flight turn is mutated; replay is
   labelled read-only and renders at least one transcript item with exact
   session/event provenance. Report manager/child attribution only when exact
   admitted identifiers exist; otherwise state the limitation without
   inference.
6. Re-read the real session/events from the isolated daemon store and bind UI
   observations to exact session/event IDs and hashes.
7. Run the exact D-APP-86 validation contract: applicable focused Vitest
   component/runtime tests; `npm run typecheck`; `npm run build`; the already
   completed single `npm run desktop:pack` (do not build a second package);
   `npm run harness:validate:premerge` against an isolated reachable App; and
   `npm run validate:release-quality` with no provider-backed check silently
   skipped. Then run the receipt validator, App corpus status, practitioner
   status/self-check/full pytest required by the standing plan. Record exact
   commands, exits, summaries, hashes, skips, and reasons.
8. Prove tracked frontend bytes and the frozen source manifest are unchanged,
   D-APP-89's zero-consumer/13-rollback-probe boundary still holds, the six
   D-APP-81 UNKNOWN relations are unchanged, and no disallowed path changed.
9. Scan durable evidence for secrets/private session content. Sanitize by
   replacing sensitive values with bounded non-reversible placeholders while
   retaining IDs required by the ruling; never retain tokens or credentials.
10. Terminate only exact run-owned daemon/GUI processes, remove only the exact
    isolated root, and prove no run process/socket/token/temp residue and no
    owner-state change. Shared generated package/check outputs may remain but
    must be identified as derivative/non-authoritative.

## Expected outputs

At the run root, complete:

- `RUN_MANIFEST.md`
- `EVIDENCE_INDEX.csv`
- `PACKAGED_UI_SMOKE.md`
- `REAL_DAEMON_REPLAY.md`
- `VALIDATION.md`
- `HANDOFF.md`

Under this instance, write `RETURN.md`, raw/sanitized evidence, exact command
records, source/package manifests, and cleanup/containment records. Every
indexed artifact receives a SHA-256.

## Acceptance and escalation

PASS requires all four observations on the same frozen package/source basis,
all validation gates as written, zero secret/containment/cleanup defects, and
no tracked product change. A partial observation is not parity closure.

If the lawful UI seam cannot capture a required observation, a gate fails, or
isolation is uncertain, stop and return `BLOCKED/PARTIAL` with exact evidence;
do not change product code or weaken D-APP-86. A later accepted D-APP-88 helper
implementation is always recorded as a parity rerun trigger.
