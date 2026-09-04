# RETURN — G1_IMPLEMENTER (reviewed freeze plus closeout)

- **Run:** `APPDEV_V3_NODE_G_2026-09-03` · **Executor:** Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN · **Skill method:** `software-bounded-implementation`
- **Basis:** `e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge; exactly the required basis) · **Branch:** `codex/app-v3-nodeG-egress-probe-restriction-2026-09-03`
- **Commits:** reviewed freeze `39adfa6a6c5972d489dbe3b4cc6d60f0ade172d8` (one commit; independent review round 1 **PASS**, 0 blocking / 0 major / 1 minor / 7 notes — `instances/G2_REVIEWER/REVIEW_01_2026-09-03_over_39adfa6a6.md`, byte copy), rebased without conflict onto `origin/main` `40ab9b34beff3079402d01e336e8b72f8bd780f2` (PR #687 merge, node I) as `6947f4b9c` with an identical diff (20 files, +2,149 / −39), plus the closeout commit that carries this text (record-only: review copy, `_STATUS.md`/`MEMORY.md`, `HANDOFF_STATE.md`, `MANIFEST.sha256`, Receipt 214, the G1-F2 text widening).
- **Item:** DEL-09-06-V3-05 (`SELECTABLE`) — egress-layer probe URL restriction (residual R-B of node A).
- **Status:** `REVIEW_PASS` received from HELP_HUMAN 2026-09-03 over `39adfa6a6`; closeout executed. Every registered check passes except the premerge, which failed in the recorded absent-runtime-daemon-bindings class (`FAIL_DEFERRED_TO_PR_CI`, Receipts 172/177) and is deferred to PR CI with no pass inferred. Post-rebase typecheck and full Vitest re-run on `6947f4b9c` (results in `CHECKS.json` closeout round). No product or test byte changed after the reviewed freeze.

## 1. Behavioural summary

Design decision **D1** (`COORDINATOR_DECISIONS.md`; the implementer's own decision under the brief's delegated latitude, not an owner ruling): hard-code the probe destination and retire the environment variable, because nothing needs the variable and a constant cannot be redirected, whereas a refuse-if-allowed filter would have to mirror the unexported `main.ts` policy.

- `frontend/electron/renderer-window-policy.ts` — new exported constant `EGRESS_LAYER_PROBE_URL = 'https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked'`. `runEgressLayerProbe(window, { env })` now runs only under `CHIRALITY_RENDERER_SECURITY_PROBE=1` (delay from the existing `_DELAY_MS`), requests **only** the constant through `session.fetch`, and logs `[egress-layer-probe]` with `destination: { protocol, hostname, port }` (port added; no path). The string `CHIRALITY_EGRESS_LAYER_PROBE_URL` no longer occurs in `frontend/electron/**`; the module never reads `process.env` (env is injected by `main.ts`, unchanged).
- `frontend/scripts/run-packaged-security-proof.mjs` — `EGRESS_PROBE_URL` exported (same literal; the summarizer's expectation), plus `EGRESS_PROBE_DECOY_URL = 'http://127.0.0.1:9/chirality-packaged-security-egress-probe-decoy'`. `summarizeNetworkEvidence` matches the probe payload on protocol + hostname + **port** (derived from `EGRESS_PROBE_URL`) and reports `egressProbeUnexpectedDestinations`, which must be empty to pass. `proofEnv` no longer supplies a probe URL; it sets the retired variable to the loopback decoy as a negative control (policy would allow it; port 9 refuses; nothing leaves the host). The whole-directive CSP check is untouched.
- `frontend/electron/main.ts` — **not changed**: the wiring `runEgressLayerProbe(window, { env: process.env })` still fits the signature (now contract-pinned).
- Tests: `renderer-window-policy.test.ts` egress-probe block rewritten (destination shape vs. the pinned port rule; gate-only inertness; the environment — including allowlisted Anthropic-443 and loopback URLs — cannot change the destination; arity; rejected/response outcomes with port). `run-packaged-security-proof.test.ts`: `EGRESS_PROBE_URL === EGRESS_LAYER_PROBE_URL`; decoy shape; fixture with port; negatives for port 443, missing port, the decoy destination, and an extra destination beside the expected one.
- Contract pins changed **deliberately** (`frontend/src/__tests__/contract-pins.manifest.ts`; the brief's `frontend/src/lib/contract-pins/**` path does not exist in the live tree — the manifest lives under `src/__tests__/`, inside the tests locus; delta recorded in `STEP0_DISCOVERY.md` §5):
  - `electron/renderer-window-policy.ts`: **replaced** `contains "CHIRALITY_EGRESS_LAYER_PROBE_URL"` with `notContains`; added `contains "export const EGRESS_LAYER_PROBE_URL ="`, the exact literal, `".fetch(EGRESS_LAYER_PROBE_URL, {"`, `notContains "process.env"`; description extended.
  - `electron/main.ts` (network-policy target): added the port rule `if (parsed.port !== '' && parsed.port !== '443') {`, its reason template, the wiring line, and `notContains "CHIRALITY_EGRESS_LAYER_PROBE_URL"`.
  - `scripts/run-packaged-security-proof.mjs`: **replaced** `CHIRALITY_EGRESS_LAYER_PROBE_URL: EGRESS_PROBE_URL` with `CHIRALITY_EGRESS_LAYER_PROBE_URL: EGRESS_PROBE_DECOY_URL`; added the two exported constant lines and `egressProbeUnexpectedDestinations.length === 0`.

## 2. Files (basis → HEAD)

`git diff --stat e59efa483 HEAD` (paths under `projects/chirality-app-dev/`): 20 files changed, 2,149 insertions(+), 39 deletions(-) —

| File | Stat |
|---|---|
| `frontend/electron/renderer-window-policy.ts` | 41 ± |
| `frontend/scripts/run-packaged-security-proof.mjs` | 38 ± |
| `frontend/src/__tests__/contract-pins.manifest.ts` | 22 ± |
| `frontend/src/__tests__/electron/renderer-window-policy.test.ts` | 104 ± |
| `frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts` | 53 ± |
| DEL-09-06 `Evidence/Node_G_Egress_Probe_Restriction_2026-09-03/EVIDENCE.md` + `packaged-security-proof/{MANIFEST.sha256, cleanup.json, packaged-daemon.log, packaged-gui.log, summary.json, tcp-snapshots.json}` | new (1,279 lines) |
| DEL-09-06 `_run_records/TASK_RUN_2026-09-03_NODE_G.md` | new |
| this run record: `ORCHESTRATION_PLAN.md`, `WORK_GRAPH.json`, `STEP0_DISCOVERY.md`, `COORDINATOR_DECISIONS.md`, `CHECKS.json`, `RETURN.md`, `instances/G1_IMPLEMENTER/LAUNCH_BRIEF.md` | new |

Untouched: `frontend/electron/main.ts`, `preload.ts`, `next.config.mjs`, `package.json`/lockfiles, `runtime/**`, `docs/**`, `.github/**`, `_STATUS.md`, `MEMORY.md`, decision register, prior receipts, Root surfaces.

## 3. Check evidence (full table with commands, cwd, exit codes: `CHECKS.json`)

| Check | Result |
|---|---|
| receipts validator (Step 0) | VALID |
| authority corpus (Step 0 and after edits) | v20, no drift |
| pinned completion reference | matches `b0a57a91…` |
| APP-HOLD dispatch preflight (DEL-09-06) | ALLOW |
| `npm run typecheck` | pass |
| `npm test` | 162 files passed / 1 skipped; 1493 tests passed / 4 skipped (+4 over basis) |
| focused Vitest (3 files) | 91 passed (65 / 16 / 10; basis 62 / 16 / 9) |
| `npm run build` | pass |
| `npm run desktop:pack` | pass (in-sandbox; pre-existing completeness note) |
| `npm run proof:packaged-security` | **pass** — identity `e716439f…`; `egressLayerDiagnostics: 1`; `[egress-layer-probe]` `{https:, api.anthropic.com, 8443}` rejected `ERR_BLOCKED_BY_CLIENT`; `egressProbeUnexpectedDestinations: []` with the decoy in the env; zero non-allowlisted TCP; cleanup pass; retained under DEL-09-06 evidence with `MANIFEST.sha256` |
| premerge | FAIL — `FAIL_DEFERRED_TO_PR_CI` (8/8 HTTP 503, absent runtime-daemon bindings; Receipts 172/177); no pass inferred |
| `git diff --check` | pass (working tree; basis..HEAD range re-run after the commit — freeze message) |
| `validate_change_scope.py` (exact command in `CHECKS.json`) | PASS, 0 violations, 16 paths before the commit; `--head <commit>` form run after the commit (freeze message) |
| harness self-check / pytest | exit 0 / 350 passed |
| APP-HOLD scan `--require-register-match` | PASS, held 0 |
| `select_affected_checks.py` | app-hold-integrity, frontend-test, frontend-typecheck, harness-pytest, harness-self-check — all executed |

## 4. Write-scope validation

All changed paths lie inside the sealed fence (`CHECKS.json` `scope_validation_command`): `renderer-window-policy.ts`, the proof script, `src/__tests__/**`, DEL-09-06 evidence and `_run_records`, and this run record. `main.ts` is deliberately outside the fence and untouched.

## 5. Residual risks and follow-ups (reported, not taken silently)

1. **R-B is closed by construction.** The probe has no destination input; the proof's negative control would expose a regression on the wire.
2. **Review G1-F1 (MINOR, test coverage — recorded as a residual, deliberately not taken after PASS):** `run-packaged-security-proof.test.ts` has no case for an entirely absent or a malformed `[egress-layer-probe]` line. The summarizer already fails closed in both cases (`.some()` over no payloads → `egressProbeObserved false`; a parse error → `null` in `egressProbeUnexpectedDestinations` → `pass false`), shown empirically by the reviewer's direct call (review cmd 19). Adding the two test lines after `REVIEW_PASS` would have been unreviewed, so it is seeded into DEL-09-06 `Remaining` as a tests-only follow-on (coordinator disposition at closeout).
3. **R-A (DEL-09-06-V3-04, nonce-based script CSP)** is untouched and remains owner-gated.
4. **Payload shape change** (`destination.port` added to the `[egress-layer-probe]` line): consumed only by the proof summarizer, which now requires it; retained node A bundles are history and are not re-evaluated.
5. **Premerge** is PR-CI-owed (recorded class).
6. **Packaged proof identity vs. commit:** the bundle was built from the pre-commit working tree (`sourceRevision e59efa483`); the artifact hashes identify the proved bytes; unsigned bundles are not byte-deterministic across builds. An `artifact-proof`-labelled CI run binds a proof to the merged SHA (review G1-F7).
7. **Absolute paths in the retained bundle** (review G1-F2): the scratch-worktree path appears in `summary.json` (`artifactIdentity.appPath`), `packaged-daemon.log`, `packaged-gui.log`, and `tcp-snapshots.json` (Electron helper command lines with the disposable `--user-data-dir` temp root), and the launcher opt-out path `/Users/ryan/.local/bin/chirality` in `packaged-gui.log` — verbatim proof output, same pattern as the bundles on `main`, no secret (node A review NOTE-7 class). `MANIFEST.sha256` entries are bare filenames, so `shasum -c` verifies from the bundle directory (review G1-F3; the convention question is the owner's).
8. **A1 re-stage rule** applies (declaration in `STEP0_DISCOVERY.md` §3).
9. Concurrent nodes: node I landed first (Receipt 213, PR #687); this node's receipt is 214 with Parent-Receipt `Receipt-212` (ledger rule 7). Nodes F/H had not landed at rebase time.

## 6. Fences

F-APP-1: no new destination, provider, dependency, or `runtime/**` change — the only destination the probe can request is the one already denied by REQ-NET-001; the decoy is loopback and set only in the proof's own environment. F-APP-2: no signing, notarization, distribution, publication, or readiness claim (evidence and this file carry explicit disclaimers only). F-APP-3: no domain-engine surface. F-APP-4: no lifecycle line touched (no `_STATUS.md` in the diff). F-APP-5: no new standing surface; the run record follows the existing AgentRuns convention.

## 7. Coordination notices

- Independent review dispatched by HELP_HUMAN over 100% of `e59efa483..39adfa6a6`: PASS (filed verbatim under `instances/G2_REVIEWER/`). Coordinator disposition at closeout (transcribed in `COORDINATOR_DECISIONS.md` D2): G1-F1 recorded as a residual, not fixed after PASS; G1-F2 text widened in the evidence docs; G1-F3..F8 no action. No write-locus extension was needed.
- For the owner at byte review: decision D1 (hard-code + retire the variable; loopback decoy as negative control) is the implementer's, recorded in `COORDINATOR_DECISIONS.md`; the PR carries the `artifact-proof` label so CI binds a packaged proof to the merged SHA.
