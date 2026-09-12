# APP_V3_CODEX_HOST_REPLATFORM_20260912 — implementing session run log

Entry basis: main at e83cb1f47 (merge of PR #772), which contains a5fa05544 (PR #769),
230be0ca9 (PR #768) and d2878462b (PR #767, the publication SHA of the D-GOV-43 ruling
and its A2 supplement). Working branch: claude/chirality-codex-replatform-3999f1 in
worktree .claude/worktrees/project-first-impressions-06aed9. Lead model: Fable 5.1.
Type 2 dispatches: Fable 5.1 (medium) for implementation, tests and packaging; Opus 5
permitted for read-only exploration; independent source reviewer is a fresh Fable 5.1
session with no authorship. Times UTC.

Git integration follows the owner's standing authorization of 2026-09-12 (Root AGENTS.md,
Execution and governance): commit, push, open/update PRs and merge within the authorized
scope; merge only with required CI green and independent review without unresolved
blocking findings covering the actual candidate revision.

## 2026-09-12T07:13:18Z — orientation
- Repository root and branch confirmed; `git merge-base --is-ancestor a5fa05544 HEAD` passed;
  HANDOFF.md section 0 precondition (3ef2ef524 ancestor, A2 supplement present) passed.
- Read in order: Root AGENTS.md; PERSPECTIVE.md; HANDOFF.md; D-GOV-43 ruling; A2 supplement;
  IMPACT.md purpose test by family; TOPOLOGY_COMPARISON.md sections 1, 3, 8, 9;
  R17_FUNCTIONAL_FINDINGS.md; PR #767 comment thread (interrupt-versus-retirement defect).
- Live state: R17 GUI (pid 31613) and LaunchAgent daemon com.chirality.runtime (pid 27838)
  running; left intact. Preserved originating worktree not entered.
- Validator note: tools/validation/validate_instruction_tranche_manifest.py now accepts
  `merge_gate: owner-authorized-pr` with `self_merge: true` (standing grant, PR #770);
  the tranche manifest will use that mode and still record the owner_direction block.
- Plan: (1) application tranche (governance) first, dispatched as bounded Type 2 work with
  disjoint write scopes; (2) spike on the production path; (3) S-1..S-8 plus the
  disconnect-during-tool-work check from source; (4) independent source review; (5) one
  consolidated signed build and the post-build minimum checks.

## 2026-09-12T08:05:00Z — application tranche (governance) applied and validated
- Four bounded Type 2 dispatches (Fable 5.1, disjoint write scopes) returned: Root
  (`tranche/ROOT_RETURN.md`), Runtime loop (`tranche/RUNTIME_RETURN.md`), App execution
  records (`tranche/APP_EXECUTION_RETURN.md`), App docs corpus (`tranche/APP_DOCS_RETURN.md`).
- Lead corrections before commit: (a) three Runtime records that Root pins by exact hash
  (`docs/PRD.md`, `DEL-02-06/ScopeOfWork.md`, `_Coordination/MIGRATION_APPLICATION.md`) and
  the Root-adopted `_ScopeChange/_LATEST.md` were restored to their pinned bytes (ruling
  item 11: historical records are read with D-GOV-43, not rewritten); the D-GOV-43
  readings moved into the hold-closure packet, relocated to
  `projects/chirality-runtime/execution/_Coordination/AgentRuns/RUNTIME_DGOV43_HOLD_CLOSURE_20260912/`
  (`PRD_REVISION.md`, `Impact_Assessment.md` carrier notes); (b) `RETIRED` is not a
  lifecycle state in the App or Runtime loop vocabulary, so DEL-02-07..12 and DEL-09-07 are
  retired in place with their prior state and a history entry; (c) Root `docs/CONTRACT.md`
  K-STORE-2 left as is (session records remain JSON/JSONL); (d) App project `AGENTS.md`
  Shared Runtime Boundary re-expressed to A2; (e) one heading em-dash removed.
- Validators (local, CI-equivalent): agent instructions 0/0; workflow metadata OK;
  entrypoints PASS; G0-G3 PASS; G4 PASS (71 manifests, plain and CI form); self-check exit
  0; harness `next` exit 0; path anchors PASS; conflict markers PASS; `git diff --check`
  clean; `pytest tools/` 1464 passed. Pre-existing register-validator errors in the
  Runtime loop (204) are unchanged and out of scope.
- Manifest `ROOT-DGOV43-APPLICATION-20260912.yaml`: `merge_gate: owner-authorized-pr`,
  `self_merge: true`, owner_direction recorded; `approved_source_sha` to be set to the
  candidate HEAD before merge.
- Concurrently dispatched W1-W4 (spike implementation) against `SPIKE_DESIGN.md`; their
  product-source edits are not part of this commit.

## 2026-09-12T08:20:00Z — tranche committed; spike dispatched; draft PR opened
- Commit 23b3879b3 (application tranche, 181 files) and 555ae90b9 (SPIKE_DESIGN.md) pushed to
  origin; draft PR #774 opened against main. Governance harness signal expected green;
  Harness pre-merge expected red until the spike retires the two Runtime tests that import
  the deleted supplier tooling (W1 scope).
- Contract seam authored in `packages/contracts` (progress events, request port,
  PolicySelection, codex.* event types, turn-state and request routes); W2 is extending it
  and it will be committed with the transport step.
- Protocol facts for the pinned 0.154.0 app-server established by a scratch-home probe:
  Plan Mode is `thread/settings/update` with `collaborationMode`; `collaborationMode/list`
  exists; `turn/start` carries no collaborationMode; `model/list` answers signed-out.
- Dispatched W1 (Runtime core), W2 (daemon transport), W3 (Electron lifecycle and
  packaging), W4 (App renderer) as bounded Type 2 assignments, Fable 5.1 medium, disjoint
  write scopes, no git operations; returns expected under `spike/`.

## 2026-09-12T08:37:00Z — W1-W4 returned; integration dispatched
- W1-W4 returned (`spike/W1_RETURN.md` .. `spike/W4_RETURN.md`) with their scoped tests
  passing. Cross-scope blockers identified by the lead: the CLI's import of the retired
  conformance module and its LaunchAgent, hosted-login, delegated and approvals command
  groups; the frontend controlled CI runtime fixture and the `harness-premerge.yml` daemon
  start and registration steps; three frontend integration tests that import retired
  modules; `desktop-release-template.yml` RunAtLoad proof steps; contract dead surface
  (`DelegatedTurnRequest.compatibility`/`preflight`, `consent-required`); unused daemon
  login option; `runtime.service.restart()` not surfaced.
- Dispatched I1 (Runtime workspace cleanup: CLI, contracts, client, daemon routes and
  exports, runtime tests) and I2 (frontend CI fixture, workflows, integration tests,
  packaging boundary scripts, Restart Runtime action) as bounded Type 2 assignments, Fable
  5.1, disjoint write scopes, no git operations.
- Manifest `instruction_surface_paths` extended with `.github/workflows/harness-premerge.yml`
  and `.github/workflows/desktop-release-template.yml` ahead of I2's edits (the validator's
  instruction surface includes `.github/workflows/`).

## 2026-09-12T09:15:00Z — integration committed: Runtime and App workspaces green
- I1 returned (`spike/I1_RETURN.md`): CLI reduced to the v1 surface, contracts and client
  dead v2 surface removed, daemon v2 routes and login option removed. Lead follow-up:
  the historical admission fields (`compatibility`, `preflight`, and their identity types)
  dropped from `DelegatedTurnRequest`; `consent-required` dropped from
  `HostedBootstrapStatus` and the four test fixtures that emitted it now emit the daemon's
  real signed-out state (`ready-to-start`, `canStartLogin: true`).
- I2 returned (`spike/I2_RETURN.md`): controlled CI runtime fixture registers the App
  project itself and prints one ready line; `harness-premerge.yml` reads it (operator-token
  registration step removed); `desktop-release-template.yml` RunAtLoad proof removed;
  shared-daemon integration test retired; boundary script cleaned; Restart Runtime action.
- Verification by the lead on the candidate tree: Runtime `tsc -b` clean, `npm test
  --maxWorkers=1` 34 files / 309 tests passed; App `tsc --noEmit` 0 errors,
  `build:electron` exit 0, `npm test` 202 files passed (1 opt-in skip), 2066 tests passed
  (4 skipped).
- Commits 95364569a (Runtime) and 39c0bb6ab (App) pushed to PR #774; contract cleanup and
  this log follow as their own commit. Governance validators rerun locally after the
  manifest and workflow edits (results in the next entry).

## 2026-09-12T09:05:00Z — validators, live-path fix, spike launched from source
- Local validators on the candidate: agent instructions OK, workflow metadata OK, conflict
  markers PASS, harness self-check exit 0, tranche manifest validator exit 0 (13 surface
  paths against one manifest), root fence/adapter/ownership/dispatch validators exit 0,
  candidate whitespace PASS (one trailing blank line trimmed, 087a7c8dc).
- Live-path defect found while preparing the source run: the Next server's hosted bootstrap
  port factory still required the retired `CHIRALITY_RUNTIME_BOOTSTRAP_TOKEN_FILE`, which
  the Electron main removes, so folder binding, status and sign-in would have failed with
  503 on the App path. Fixed in 5fe619fdd (factory reads `CHIRALITY_RUNTIME_TOKEN_FILE`,
  unit test added). The full frontend suite had passed without covering this seam; noted
  for the independent reviewer.
- App launched from source at 08:56Z with isolated userData (details and filtered log
  excerpts in `spike/EVIDENCE.md` notes). Service child ready 0.5 s after spawn; pinned
  Codex 0.154.0 child running; effective home carries no `auth.json`; status route answers
  over the client token. Waiting on the owner to bind a folder and complete OAuth.

## 2026-09-12T15:40:00Z — acceptance run from source: findings fixed on the live path
- Owner bound `projects/chirality-app-dev` and signed in (OAuth in the browser, 15 s;
  `auth.json` lands only in the App's effective home; `~/.codex/auth.json` untouched).
- Live-path defects found by the checks and fixed as bounded commits: (1) sign-in used the
  project-scoped token, which lacks the credential scope (df748c5cd: account actions travel
  over the App-host client); (2) session creation refused the sole engine for folders whose
  manifest predates D-GOV-43 (fca60696d: Codex is not gated by `enabledAdapterIds`);
  (3) the App proxy emitted no keepalive during silent tool runs (36f269d62); (4) changing a
  selected workflow or editing its body mid-session hit the retired context-successor
  machinery (`RUNTIME_COMPATIBILITY_MISMATCH`, "cannot prepare a reversible context
  successor"): method transitions are now additive for engines without successor
  preparation and changed instruction bytes re-freeze with the accepting turn; (5) the
  renderer's legacy boot turn ("bootstrap" as a real model turn) never completed on the
  Codex path and timed out after 150 s ("Chat took too long to start"): the Codex adapter
  declares `boot: "none"` and boot records readiness without a turn (258 ms measured).
  Also: `requireServerRequestAnswer` moved out of a Next route module (a non-handler export
  fails `next build`), and the SIGKILL escalation test no longer depends on wall-clock.
- Development-only: from source the instruction root resolved to the repository root, so
  no folder inside the repo could be a project; the source run now uses the staged copy
  produced by `instruction-root:prepare`, as the packaged App does.
- Checks S-1..S-7 and the transport-level disconnect check PASS (`spike/EVIDENCE.md`);
  S-8 sign-out and the window-level disconnect check pending with the owner.
- Observation for review: after `turn/interrupt` the sandboxed `sleep 120` child of the
  interrupted command kept running to its natural end (stock Codex behaviour; the turn
  itself was interrupted within 1.1 s and the session continued).
