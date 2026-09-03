# Evidence — DEL-09-06-V3-01: credential IPC sender authorization and G-CSP renderer hardening (2026-09-03)

> Derivative evidence package (App AGENTS.md derivative-package rule). Accepted
> upstream: `main` at `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge;
> A12 seating). Run record: `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_A_2026-09-03/`.
> Executed by Claude Fable 5.1 (`claude-fable-5-1`) as ephemeral Agent 2 implementer
> under HELP_HUMAN, in two local commits on one branch: round 1 (sender authorization,
> typed states, settings panel; commit `4e4c7e9090891fae98bb63ebf1ee8e3561d4f9ac`) and
> round 2 (renderer window hardening and CSP, added on the coordinator's disposition
> that the seated item's locus and Return govern; the commit that contains this file).
> This package makes no release-readiness, signing, notarization, distribution,
> certification, or lifecycle claim.

## 1. Claims

**Sender authorization.** All six `ipcMain.handle` credential channels in
`frontend/electron/api-key-ipc.ts` reject any sender whose frame origin is not exactly
the renderer origin, using the one policy shared with `runtime-control-ipc.ts`
(`frontend/electron/ipc-sender-policy.ts`). A denied request returns a typed,
secret-free result, never reaches the daemon client, never throws into the renderer,
and emits one `desktop.credential_ipc.denied` line carrying the channel and sender
*origin* only.

**Renderer window hardening (G-CSP).** `frontend/electron/renderer-window-policy.ts`
supplies, and `main.ts` applies to every BrowserWindow it creates:

- web preferences asserted at creation (`contextIsolation: true`, `nodeIntegration:
  false`, `sandbox: true`; `webSecurity: false`, `webviewTag`, `nodeIntegrationInWorker`,
  `nodeIntegrationInSubFrames`, `allowRunningInsecureContent`, `enableRemoteModule`,
  `experimentalFeatures` rejected) — window creation fails closed otherwise;
- `setWindowOpenHandler` → `{ action: 'deny' }` for every request, logged as
  `renderer.window_open.denied` with protocol and hostname only;
- `will-navigate` and `will-redirect` allow only `http(s)` URLs at exactly the renderer
  origin; `javascript:`, `file:`, `data:`, `about:`, `blob:` (which carries the
  renderer's own origin — caught by the scheme check), foreign hosts, other ports and
  other schemes are `preventDefault`ed and logged as `renderer.navigation.denied`;
- a Content-Security-Policy set at the source on the packaged renderer HTTP server
  responses and, through `webRequest.onHeadersReceived`, on any renderer-origin
  response that carries none (the dev server's), so both modes render under one policy.

The CSP (packaged): `default-src 'self'; script-src 'self' 'unsafe-inline'; style-src
'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self' data:; connect-src 'self'
https://api.anthropic.com:*; worker-src 'self'; manifest-src 'self'; media-src 'self';
frame-src 'none'; object-src 'none'; base-uri 'self'; form-action 'self';
frame-ancestors 'none'`. Development adds `'unsafe-eval'` to `script-src` and the
`ws:`/`wss:` form of the dev origin to `connect-src`; nothing else differs.

Why each allowance exists (verified, not assumed):

| Allowance | Verification |
|---|---|
| `script-src 'unsafe-inline'` | `npm run build` output `.next/server/app/{index,chat}.html` each contain 8 inline `<script>self.__next_f.push(…)</script>` flight-payload tags and no nonce; a nonce pipeline needs a Next middleware (outside this locus). External scripts stay `'self'`. |
| no `'unsafe-eval'` in packaged mode | packaged proof run 2: zero `securitypolicyviolation` events against the app's own resources under the eval-free policy (`unexpectedViolations: []`) |
| `'unsafe-eval'` in development only | Next dev runtime / React Refresh evaluate source; never delivered to the packaged renderer (`cspHeaderPresent` requires its absence) |
| `style-src 'unsafe-inline'` | two components use React `style` props (`grep -rl "style={{" src --include=*.tsx` → 2); Next injects style elements in development |
| `img-src`/`font-src` `data:` | no `data:`/`blob:` use found in `src/`; kept for Next's dev overlay assets; no network reach |
| `connect-src https://api.anthropic.com:*` (port wildcard) | deliberate, recorded: with a CSP exactly equal to the REQ-NET-001 egress allowlist no page-originated request could ever reach the egress layer, and the packaged proof would silently lose its independent observation of that layer. The egress policy still enforces `https:443` exactly (`anthropic_port_not_allowlisted`), and the proof drives `https://api.anthropic.com:8443/…` to watch it deny (§4). The renderer never legitimately calls Anthropic; the daemon does. |

## 2. Source identities (SHA-256 at the round-2 freeze; the frozen commit tree is authoritative)

Round-1 identities are in the committed history of this file at `4e4c7e909`. Round-2 files:

| File | Note |
|---|---|
| `frontend/electron/renderer-window-policy.ts` (new) | pure policy + installer + optional in-page security probe |
| `frontend/electron/main.ts` | window creation from the policy; packaged renderer server sets the CSP header; probe hook |
| `frontend/scripts/run-packaged-security-proof.mjs` | learns the renderer-hardening evidence (§4); log writer truncates instead of appending |
| `frontend/src/__tests__/electron/renderer-window-policy.test.ts` (new) | 38 tests |
| `frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts` | new evidence summarizer tests and fixtures |
| `frontend/src/__tests__/contract-pins.manifest.ts` | pins for the policy module, `main.ts` wiring, and the proof script |

Hashes: `git show <frozen commit> --stat` and `git rev-parse <commit>:<path>` reproduce
them exactly; the run record `MANIFEST.sha256` (written at closeout) lists the final bytes.

## 3. Unit-level evidence (Vitest 4.1.10, node v24.18.0, cwd `frontend`)

- `ipc-sender-policy.test.ts` — 17; `api-key-ipc.test.ts` — 58 incl. the six-channel
  authorized/unauthorized matrix; `runtime-control-ipc.test.ts` — 11 unchanged (round 1).
- `renderer-window-policy.test.ts` — 38: hardened preferences produced and 8 weakening
  variants rejected; window-open always denied; navigation allow (3 same-origin forms) /
  deny matrix (`javascript:`, `file:`, `data:`, `about:blank`, `blob:` of the renderer
  origin, `ws:` on the renderer host, foreign https/http, same host other port, other
  scheme, `localhost` alias of the same server, origin-in-path, origin-as-userinfo,
  unparseable, empty, empty renderer origin); CSP builder (packaged: no eval, closed
  frames/objects/embedding; development: eval + HMR websocket only; `connect-src` never
  wider than `'self'`, the Anthropic host, and the dev websocket); header application
  (added when absent, preserved when present, foreign origins untouched); installer on a
  fake window (deny-all handler with redacted log; both navigation events registered;
  `preventDefault` on every denied form; CSP through `onHeadersReceived` for
  renderer-origin responses only; works without a log sink); probe inert without the
  env flag, runs after load, reports under `[renderer-security-probe]`.
- `run-packaged-security-proof.test.ts` — the network summarizer now requires the egress
  layer to be observed on its own (a CSP-only block is rejected); the renderer-security
  summarizer requires CSP header presence without eval, the expected `connect-src`
  violation, zero own-resource violations, `window.open` → `null` plus its log line, and
  the navigation-denied line; the marker set gains `Content-Security-Policy`,
  `renderer.window_open.denied`, `renderer.navigation.denied`.
- `contract-pins.test.ts` — 16 targets: `electron/renderer-window-policy.ts` (the three
  preferences, `{ action: 'deny' }`, both navigation events, `preventDefault`, the
  scheme and origin checks, every closed CSP directive, the eval-only-in-development
  template, the exact `connect-src` list, no `unsafe-hashes`, no `'*'`); `electron/main.ts`
  (`webPreferences: rendererWebPreferences(…)`, `installRendererWindowPolicy(window, {`,
  packaged/development mode selection, `res.setHeader(CONTENT_SECURITY_POLICY_HEADER, …)`,
  per-window egress registration, no weakening preference anywhere); the proof script
  (probe env flag, `rendererSecurityProofPass === true`, the `:8443` egress probe URL).

Results: focused `npx vitest run` over the round-2 files → 3 files, 67 passed;
`npm test` → 158 files passed / 1 skipped, 1408 tests passed / 4 skipped, exit 0;
`npm run typecheck` exit 0; `npm run build` exit 0 (both rounds).

## 4. Packaged evidence (host surface; ran inside the session sandbox — no escalation needed)

Two retained runs, each `npm run desktop:pack` (exit 0) then `npm run
proof:packaged-security` (exit 0, `status: pass`), compact non-secret bytes with a sorted
`MANIFEST.sha256` (verify with `shasum -a 256 -c MANIFEST.sha256` in the directory):

- `packaged-security-proof/` — round 1, bundle identity
  `f8b954e1d926867f28aa961c9ba186303be5fc039f1dd47229988ad5e0988de6` (before the
  renderer-hardening slice; `sourceRevision` HEAD `0c683fb16`, built from the pre-commit
  working tree). Credential proof shows the typed storage state through the real daemon
  (`missing → available/ui → missing`).
- `packaged-security-proof-2/` — round 2, bundle identity
  `eb23a0756253e6a01ab8d05da23fe5331c605dfd7b7e6108df45340c9e07673b`
  (`Contents/MacOS/Chirality` 33,968 B `79019361…`; `app.asar` 448,840,503 B
  `133e7092…`; `chirality-cli.mjs` 75,460 B `0503c40a…`; `sourceRevision` HEAD
  `4e4c7e909`, built from the round-2 working tree; run into a freshly removed output
  root so no earlier run's bytes are present). Observations:
  - all 13 packaged policy markers present (10 prior + the three renderer-hardening ones);
  - credential proof pass; `retainedSecretFindings: []`; `retainedMetadataLeakFindings: []`;
  - **renderer hardening (`rendererSecurityProof`)**: `cspHeaderPresent: true` — the
    packaged page's own same-origin fetch of its document returned the full policy above;
    `cspViolationObserved: true` — the probe's `https://example.com/…-csp-blocked` fetch
    raised `securitypolicyviolation` with `effectiveDirective: connect-src`,
    `disposition: enforce`; `unexpectedViolations: []` — the app's own scripts, styles,
    fonts, images, and API calls raised none under the eval-free policy;
    `windowOpenReturnedNull: true` and `renderer.window_open.denied
    {"destination":{"protocol":"https:","hostname":"example.com"}}` logged;
    `navigationAttempted: true` and `renderer.navigation.denied
    {"event":"will-navigate","reason":"ORIGIN_NOT_RENDERER","destination":{"protocol":"https:","hostname":"example.com"}}`
    logged — the page stayed alive after the attempt (the probe payload was emitted and
    the GUI exited 0 on SIGTERM);
  - **network (`networkProof`)**: 7 snapshots, `nonAllowlistedOutboundTcp: []`;
    `blockedRendererDiagnostics: 1` = `egressLayerDiagnostics: 1`, the egress layer's
    `anthropic_port_not_allowlisted:8443` denial of the `:8443` probe (`egressProbeObserved`);
    the `example.com` network probe failed with **no** egress diagnostic — it was stopped
    earlier, by the CSP (`blockedProbeObserved`); loopback probe observed;
  - cleanup pass (GUI and daemon exit 0, temp root removed).

Retained-copy normalization (both runs, recorded): the proof script's `START …` line
carries one trailing space that the repository's `git diff --check` gate rejects; the
retained `packaged-gui.log` copies have that single trailing space removed (raw and
retained SHA-256 are printed in the run record `CHECKS.json`; `MANIFEST.sha256` lists the
retained bytes). No other byte differs.

What the packaged proof does **not** drive: a `will-redirect` (server-side redirect)
attempt — covered at unit level only; a subframe navigation (`will-frame-navigate` is
not installed; `frame-src 'none'` forbids frames at the CSP layer); the development-mode
CSP (the dev server sets no header of its own — verified with `curl -D -` against `next
dev` — and the per-window hook supplies it; not observable from the proof harness, which
runs the packaged bundle only).

## 5. G-CSP renderer-hardening inventory (final)

| Surface | Policy in source | Evidence |
|---|---|---|
| Explicit `contextIsolation` / `sandbox` / `nodeIntegration: false` | `renderer-window-policy.ts` (`REQUIRED_RENDERER_WEB_PREFERENCES`, `assertRendererWebPreferences`, `rendererWebPreferences`); applied at `main.ts` `createMainWindow` | unit (9 tests); contract pins on both files |
| Window-open denial | `evaluateWindowOpen` / `setWindowOpenHandler` in the installer | unit; **packaged run 2**: `window.open` → `null`, denial logged |
| Navigation constraint | `evaluateRendererNavigation` on `will-navigate` and `will-redirect` | unit (18-case matrix incl. `javascript:`, `file:`, redirect event); **packaged run 2**: foreign `location.assign` denied and logged |
| CSP effectiveness | `buildRendererContentSecurityPolicy`; packaged server header at the source; `onHeadersReceived` fallback | unit; **packaged run 2**: header observed by the page, enforced (`connect-src` violation), no own-resource violation |
| Per-window bounded egress | `main.ts` egress policy, registered per window (unchanged) | existing pins; **packaged run 2**: `:8443` denial observed at the egress layer independently of the CSP; zero non-allowlisted TCP |
| Privileged IPC sender authorization | `ipc-sender-policy.ts` adopted by both IPC modules | round-1 unit matrix; pins |

No existing policy was weakened; every allowance in the CSP is recorded with its reason.

## 6. Environment, containment, and rerun method

- cwd for frontend commands: `projects/chirality-app-dev/frontend`; node v24.18.0,
  Vitest 4.1.10, Next 15.5.21, Electron 43.2.0, electron-builder 26.15.3. Packaged-proof
  effective env: the script's own (`CHIRALITY_USER_DATA` temp root,
  `CHIRALITY_SKIP_CLI_LAUNCHER=1`, three network probe URLs,
  `CHIRALITY_RENDERER_SECURITY_PROBE=1`, fixture credential only;
  `realCredentialsUsed: false`, `ownerUserDataTouched: false`).
- Containment: `validate_change_scope.py` PASS against the extended fence (run record
  `CHECKS.json`); no `runtime/**`, `package.json`, dependency, `preload.ts`, or
  `next.config.mjs` change.
- Rerun: from `frontend`, `npm ci`; from `runtime`, `npm ci && npm run build`; then `npm
  run typecheck && npm test && npm run build && npm run desktop:pack && rm -rf
  artifacts/release-verification/packaged-security && npm run proof:packaged-security`.
  Packaged results reproduce as observations and marker sets; unsigned bundle bytes are
  not asserted to be byte-deterministic across rebuilds.
