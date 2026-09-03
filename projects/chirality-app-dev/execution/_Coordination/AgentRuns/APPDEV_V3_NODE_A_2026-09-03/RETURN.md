# RETURN — A1_IMPLEMENTER (frozen for independent review; two local commits)

- **Run:** `APPDEV_V3_NODE_A_2026-09-03` · **Executor:** Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN · **Skill method:** `software-bounded-implementation`
- **Basis:** `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge; exactly the required basis) · **Branch:** `codex/app-v3-nodeA-credential-ipc-2026-09-03`
- **Commits:** round 1 `4e4c7e9090891fae98bb63ebf1ee8e3561d4f9ac` (kept as-is); round 2 = the commit containing this file (its SHA is reported in the freeze message; the reviewer takes the full basis→HEAD diff)
- **Items:** DEL-09-06-V3-01, DEL-04-05-V3-01, DEL-02-05-V3-01 (one integration owner for the shared `frontend/electron/api-key-ipc.ts`)
- **Status:** implementation complete for all three items including the coordinator-directed renderer-hardening slice; every registered check passes except the premerge, which failed in the recorded absent-runtime-daemon-bindings class both rounds and is deferred to PR CI; `REVIEW_READY`. Nothing pushed; no `_STATUS.md`, receipt, `HANDOFF_STATE.md`, or `MANIFEST.sha256` written yet (those follow `REVIEW_PASS`).

## 1. Behavioural summary

**Sender authorization (DEL-09-06-V3-01, round 1).** The origin policy formerly private to `runtime-control-ipc.ts` lives in `frontend/electron/ipc-sender-policy.ts` (`isAuthorizedSender`, `describeIpcSender`); `runtime-control-ipc.ts` imports it (behaviour identical). `api-key-ipc.ts` takes `ApiKeyHandlerOptions { rendererOrigin, log? }` and guards all six channels before any argument validation or daemon call; a foreign, missing, or unparseable sender gets `{ ok:false, error:'Credential request was denied' }` on the mutation channels and a fail-closed status object carrying the same `error` on the status channels, plus one `warn desktop.credential_ipc.denied { channel, sender:<origin> }` line. `main.ts` resolves `rendererOrigin` once and registers the credential handlers after the renderer URL is known.

**Renderer window hardening and CSP (DEL-09-06-V3-01, round 2).** New `frontend/electron/renderer-window-policy.ts`: (a) `rendererWebPreferences`/`assertRendererWebPreferences` — every window is created from the policy with `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true` asserted (and `webSecurity: false`, `webviewTag`, `nodeIntegrationInWorker`, `nodeIntegrationInSubFrames`, `allowRunningInsecureContent`, `enableRemoteModule`, `experimentalFeatures` rejected) — creation fails closed; (b) `setWindowOpenHandler` denies every request and logs `renderer.window_open.denied` with protocol+hostname only; (c) `will-navigate` and `will-redirect` allow only `http(s)` at exactly the renderer origin (scheme check first: `blob:` URLs carry the renderer's own origin), `preventDefault` + `renderer.navigation.denied` otherwise; (d) the renderer CSP is set at the source on the packaged renderer HTTP server responses and via `onHeadersReceived` on any renderer-origin response lacking one (the dev server's). Packaged CSP: `default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self' data:; connect-src 'self' https://api.anthropic.com:*; worker-src 'self'; manifest-src 'self'; media-src 'self'; frame-src 'none'; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'`; development adds `'unsafe-eval'` and the dev origin's `ws:`/`wss:` form only. Each allowance is recorded with its verification in the DEL-09-06 `EVIDENCE.md` §1. An opt-in in-page probe (`CHIRALITY_RENDERER_SECURITY_PROBE=1`, used by the packaged proof) reports the page's CSP header, a `window.open` result, CSP violations, and attempts a foreign navigation; it is inert otherwise.

**Typed safeStorage states (DEL-04-05-V3-01, round 1)** and **settings panel (DEL-02-05-V3-01, round 1)** — unchanged from the round-1 return: shared vocabulary `src/lib/credential-storage-state.ts`; `readProviderCredential` / `probeProviderCredentialStorage` / `status().storage` in `api-key-storage.ts` (non-destructive; source precedence untouched; daemon spreads the field verbatim so no `runtime/**` change; confirmed end-to-end in both packaged proofs); validated IPC projection; four-state panel with remediation copy and no key material in the DOM.

## 2. Files (basis → HEAD)

Product: `frontend/electron/{api-key-ipc.ts, api-key-storage.ts, ipc-sender-policy.ts (new), renderer-window-policy.ts (new), main.ts, runtime-control-ipc.ts}`, `frontend/scripts/run-packaged-security-proof.mjs`, `frontend/src/components/settings/api-key-settings.tsx`, `frontend/src/lib/credential-storage-state.ts (new)`. Not changed: `preload.ts`, `next.config.mjs`, `package.json`/lockfiles, `runtime/**`.
Tests: `frontend/src/__tests__/electron/{ipc-sender-policy.test.ts (new), renderer-window-policy.test.ts (new), api-key-ipc.test.ts, api-key-storage.test.ts}`, `frontend/src/__tests__/components/{api-key-settings-storage-states.test.ts (new), api-key-settings.test.ts}`, `frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`, `frontend/src/__tests__/contract-pins.manifest.ts`.
Evidence/state: DEL-09-06 `Evidence/Node_A_Credential_IPC_Sender_Authorization_2026-09-03/{EVIDENCE.md, packaged-security-proof/**, packaged-security-proof-2/**}` and `_run_records/TASK_RUN_2026-09-03_NODE_A.md`; DEL-04-05 and DEL-02-05 evidence + `_run_records`; this run record (`ORCHESTRATION_PLAN.md`, `WORK_GRAPH.json`, `STEP0_DISCOVERY.md` — its §5 is the pre-slice inventory, superseded by `EVIDENCE.md` §5 — `CHECKS.json`, `RETURN.md`, `instances/A1_IMPLEMENTER/LAUNCH_BRIEF.md`).

## 3. Check evidence (full table with commands, cwd, exit codes, both rounds: `CHECKS.json`)

| Check | Round 1 | Round 2 |
|---|---|---|
| `npm run typecheck` | pass | pass |
| `npm test` (full Vitest) | pass — 157 files / 1364 tests (4 skipped) | pass — 158 files / 1408 tests (4 skipped) |
| focused Vitest | pass — 151 | pass — 67 (renderer-window-policy 38, contract-pins 16, proof script 13) |
| `npm run build` | pass | pass |
| premerge (`next dev` + `harness:validate:premerge`) | **FAIL — absent runtime-daemon bindings** (8/8 HTTP 503); PR-CI-owed | same class, same result; PR-CI-owed |
| `npm run desktop:pack` | pass (in-sandbox) | pass (in-sandbox) |
| `npm run proof:packaged-security` | pass; identity `f8b954e1…` | pass; identity `eb23a075…`; renderer-hardening evidence pass (CSP header seen by the page, `connect-src` violation for example.com, zero own-resource violations, `window.open` → `null` + logged, foreign navigation denied + logged); egress layer observed independently via the `:8443` probe |
| `git diff --check` | pass | pass |
| harness `self-check` / pytest | pass / 350 | pass / 350 |
| APP-HOLD preflight / scan | ALLOW / PASS | PASS |
| `validate_change_scope.py` | PASS | PASS (fence extended by `renderer-window-policy.ts` and the proof script) |
| Receipts validator; corpus status | VALID; no drift (Step 0) | — |

## 4. Write-scope validation

Every changed path is inside the seated items' loci as extended by the coordinator's round-2 disposition: the named `electron/` files plus the two new modules, `scripts/run-packaged-security-proof.mjs` (it had to learn the header/denial evidence, and its log writer now truncates so the new checks cannot be satisfied by a stale file), the settings component, `src/lib/credential-storage-state.ts`, `src/__tests__/**`, the three deliverable folders (evidence + `_run_records` only; `_STATUS.md` untouched until `REVIEW_PASS`), and this AgentRuns record. `validate_change_scope.py` → `PASS`, `violations: []`. Not touched: `runtime/**`, `package.json`/lockfiles, `preload.ts`, `next.config.mjs`, any `docs/**`, register, receipts, or Root surface.

## 5. Residual risks and follow-ups (reported, not taken silently)

1. **Nonce-based script CSP** would remove `script-src 'unsafe-inline'`; it needs a Next middleware (`src/middleware.ts`) to mint nonces and set the header per response — outside this locus and a reasonable follow-on for DEL-09-06/DEL-02-xx. External scripts are already `'self'`-only.
2. **`connect-src https://api.anthropic.com:*`** (port wildcard) is a recorded, deliberate deviation from an exactly-equal CSP so the egress layer stays independently observable; the egress layer enforces 443. If the reviewer prefers the exact origin, the trade is losing the packaged proof's egress-layer observation (it would become CSP-only) — a coordinator/owner choice.
3. **What the packaged proof does not drive:** `will-redirect` (unit-tested only), subframe navigation (`frame-src 'none'` at the CSP layer; `will-frame-navigate` not installed), and the development-mode CSP (dev server sets none of its own — verified with `curl -D -`; the per-window hook supplies it; not observable from the proof harness).
4. **Premerge** is PR-CI-owed (recorded class, both rounds).
5. **Packaged proof identity vs. commit:** each bundle was built from the working tree at the time (`sourceRevision` reports the then-HEAD); artifact hashes identify the proved bytes. An `artifact-proof`-labelled CI run would bind a proof to the merged SHA.
6. **Proof-script log writer** was append-mode (`flags: 'a'`) — pre-existing; one round-2 run showed an earlier run's lines inflating the counts. Changed to truncate; the retained run is the post-change one. Worth a glance from the reviewer as a proof-integrity fix.
7. **Compatibility mapping** for a daemon predating the typed storage state (`ui → available`, else `missing`) — documented in code and tests; both processes ship in one bundle.
8. **`instruction-root:integrity` "source completeness status: needs_remediation"** — pre-existing (root commit `3d522842e`); status `pass`.
9. **A1 re-stage rule** applies (declaration in `STEP0_DISCOVERY.md` §3).
10. Concurrent nodes: no shared write path except the append-only receipts ledger at closeout (Receipt 206, parent Receipt-205).

## 6. Coordination notices

None owed beyond this return: no `agents/**`, corpus, register, or Root surface changed.
