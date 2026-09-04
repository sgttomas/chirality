# Evidence — DEL-09-06-V3-05: egress-layer probe destination fixed to a policy-denied form (2026-09-03)

> Derivative evidence package (App AGENTS.md derivative-package rule). Accepted
> upstream: `main` at `e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge; node A
> closeout, Receipt 212). Run record:
> `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_G_2026-09-03/`. Executed by Claude
> Fable 5.1 (`claude-fable-5-1`) as ephemeral Agent 2 implementer under HELP_HUMAN, in one
> local commit on branch `codex/app-v3-nodeG-egress-probe-restriction-2026-09-03` (the
> commit that contains this file). The design decision is recorded as D1 in the run
> record's `COORDINATOR_DECISIONS.md` (an implementer decision under the brief's
> delegated latitude; not an owner ruling). This package makes no release-readiness,
> signing, notarization, distribution, certification, or lifecycle claim.

## 1. Claim

The main-process egress-layer probe that the packaged security proof observes
(`runEgressLayerProbe` in `frontend/electron/renderer-window-policy.ts`) can no longer be
pointed at any destination the REQ-NET-001 egress policy would allow. Its destination is
the module-level constant

```
EGRESS_LAYER_PROBE_URL = 'https://api.anthropic.com:8443/chirality-packaged-security-egress-blocked'
```

and nothing else: the environment variable `CHIRALITY_EGRESS_LAYER_PROBE_URL` is retired
(no longer read anywhere in `frontend/electron/**`), the function takes no URL from its
caller, and the module never reads `process.env`. The environment still controls only
whether the probe runs (`CHIRALITY_RENDERER_SECURITY_PROBE=1`) and its delay.

Why that destination is always denied: `main.ts`'s `evaluateRendererEgressPolicy` allows
the Anthropic API host only over `https:` with an empty or `443` port; any other port is
`anthropic_port_not_allowlisted:<port>` (the rule is now contract-pinned). Port 8443 is
therefore denied by the real policy — which is exactly the `egressLayerDiagnostics` line
the packaged proof counts. The residual R-B of DEL-09-06-V3-01 (one unauthenticated
main-process GET to an already-allowlisted URL under a deliberately set launch
environment) is closed by removing the input, not by adding a check that could drift.

The packaged proof (`frontend/scripts/run-packaged-security-proof.mjs`) now:

- exports its expectation `EGRESS_PROBE_URL` (same literal) and matches the observed
  `[egress-layer-probe]` payload on protocol, hostname **and port** — a payload for the
  allowlisted port, a payload without the port, or a payload for any other destination
  does not count, and any unexpected destination fails the proof
  (`egressProbeUnexpectedDestinations` must be empty);
- no longer supplies a probe URL; instead it sets the retired variable to a **loopback
  decoy** the egress policy would allow (`EGRESS_PROBE_DECOY_URL =
  'http://127.0.0.1:9/chirality-packaged-security-egress-probe-decoy'`; port 9 refuses the
  connection, so nothing leaves the host). A regression that re-read the variable would
  surface on the wire as a payload naming `127.0.0.1:9` and fail the proof without any
  external request;
- keeps the whole-directive CSP check untouched.

## 2. Source identities (the frozen commit tree is authoritative; `git rev-parse <commit>:<path>` reproduces them)

| File | Change |
|---|---|
| `frontend/electron/renderer-window-policy.ts` | `EGRESS_LAYER_PROBE_URL` exported; `runEgressLayerProbe` gated on `CHIRALITY_RENDERER_SECURITY_PROBE` only, requests the constant only, logs `{protocol, hostname, port}` (no path) |
| `frontend/scripts/run-packaged-security-proof.mjs` | `EGRESS_PROBE_URL` and `EGRESS_PROBE_DECOY_URL` exported; summarizer matches the exact destination incl. port and reports `egressProbeUnexpectedDestinations` (must be empty to pass); `proofEnv` sets the decoy instead of the probe URL |
| `frontend/src/__tests__/electron/renderer-window-policy.test.ts` | egress-probe block rewritten (65 expanded cases in the file, was 62) |
| `frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts` | new cross-check case; fixture carries the port; negative cases (10 cases in the file, was 9) |
| `frontend/src/__tests__/contract-pins.manifest.ts` | pins changed deliberately — see §3 |
| `frontend/electron/main.ts` | **unchanged** (wiring `runEgressLayerProbe(window, { env: process.env })` still fits; now pinned) |

## 3. Unit-level evidence (Vitest 4.1.10, node v24.18.0, cwd `frontend`)

`renderer-window-policy.test.ts` — `runEgressLayerProbe`:

- *fixes the destination to the allowlisted Anthropic host on a port the egress policy
  denies*: `EGRESS_LAYER_PROBE_URL` parses to `https:` / `api.anthropic.com` / port `8443`
  (non-empty, not `443`; not a loopback host; no userinfo; no query) and equals the
  literal above;
- *does nothing without the gate, whatever else the environment says* (incl. the retired
  variable set to the probe URL);
- *cannot be pointed at any other destination by the environment*: with the gate on and
  the retired variable set in turn to `https://api.anthropic.com/v1/messages`,
  `https://api.anthropic.com:443/v1/messages`, `http://127.0.0.1:3000/api/session`,
  `http://localhost:3000/`, `http://[::1]:8080/`, and `https://example.com/…`, the probe
  issues exactly one `session.fetch` to `EGRESS_LAYER_PROBE_URL`, never to the supplied
  URL, and logs the fixed destination `{https:, api.anthropic.com, 8443}` without any
  supplied path;
- *takes no destination from its caller* (arity 2: `(window, { env })`);
- rejected / response outcomes reported under `[egress-layer-probe]` with the port in the
  destination and no path in the log.

`run-packaged-security-proof.test.ts`:

- `EGRESS_PROBE_URL` (proof) `===` `EGRESS_LAYER_PROBE_URL` (app); the decoy is
  `127.0.0.1:9` and differs from the probe URL;
- the network summarizer passes only with a rejected payload naming
  `api.anthropic.com` **port 8443** and the `anthropic_port_not_allowlisted:8443`
  diagnostic; it fails for a `response` outcome, for port `443`, for a payload without
  the port, for the decoy destination (reported in `egressProbeUnexpectedDestinations`),
  and when an extra payload for another destination appears beside the expected one.

`contract-pins.test.ts` (16 targets) — pins changed deliberately:

- `electron/renderer-window-policy.ts`: the pin requiring the string
  `CHIRALITY_EGRESS_LAYER_PROBE_URL` is **replaced** by `notContains` of that string;
  added `contains` `export const EGRESS_LAYER_PROBE_URL =`, the exact literal,
  `.fetch(EGRESS_LAYER_PROBE_URL, {`, and `notContains 'process.env'`;
- `electron/main.ts` (network-policy target): added `contains` of the port rule
  `if (parsed.port !== '' && parsed.port !== '443') {` and its reason
  `anthropic_port_not_allowlisted:${parsed.port}`, the wiring line
  `runEgressLayerProbe(window, { env: process.env });`, and `notContains
  'CHIRALITY_EGRESS_LAYER_PROBE_URL'`;
- `scripts/run-packaged-security-proof.mjs`: the pin `CHIRALITY_EGRESS_LAYER_PROBE_URL:
  EGRESS_PROBE_URL` is **replaced** by `CHIRALITY_EGRESS_LAYER_PROBE_URL:
  EGRESS_PROBE_DECOY_URL`; added the exported `EGRESS_PROBE_URL` and
  `EGRESS_PROBE_DECOY_URL` lines and `egressProbeUnexpectedDestinations.length === 0`.

Results: focused `npx vitest run` over the three files → 91 passed (renderer-window-policy
65; contract-pins 16; run-packaged-security-proof 10; basis bytes: 87 = 62/16/9); `npm
test` → 162 files passed / 1 skipped (163), 1493 tests passed / 4 skipped (1497), exit 0;
`npm run typecheck` exit 0; `npm run build` exit 0.

## 4. Packaged evidence (host surface; ran inside the session sandbox — no escalation needed)

`packaged-security-proof/` — `npm run desktop:pack` (exit 0; dependency boundary PASS;
instruction-root integrity `pass` with the pre-existing `source completeness status:
needs_remediation` note) then `rm -rf artifacts/release-verification/packaged-security &&
npm run proof:packaged-security` (exit 0, `status: pass`), 2026-09-04T01:23Z (local
2026-09-03 19:23). Bundle identity
`e716439fc797d2d7d5bb4021d5f940a9bc2de84ba7161444999030aeaeeb7452`
(`Contents/MacOS/Chirality` 33,968 B `79019361…`; `Contents/Resources/app.asar`
407,600,367 B `010839f1…`; `runtime-cli/chirality-cli.mjs` 75,460 B `0503c40a…`;
`sourceRevision` HEAD `e59efa483`, built from the pre-commit working tree — the artifact
hashes identify the proved bytes; an `artifact-proof`-labelled CI run binds a proof to
the merged SHA). Unsigned bundles are not byte-deterministic across builds (electron-builder
timestamps and the Next build id vary), so the identity is a record of this run, not a
reproducible target.

Observations (retained `summary.json`, `packaged-gui.log`):

- all 13 packaged policy markers present; credential proof pass; `retainedSecretFindings:
  []`; `retainedMetadataLeakFindings: []`; renderer-hardening proof pass (exact CSP,
  `connect-src` violation for example.com, `unexpectedViolations: []`, `window.open` →
  `null` + denial logged, navigation denied + logged);
- **network proof pass with the decoy present in the environment**: 7 snapshots,
  `nonAllowlistedOutboundTcp: []`; `blockedRendererDiagnostics: 1` = `egressLayerDiagnostics: 1`
  (`Blocked renderer outbound request by network policy … reason:
  'anthropic_port_not_allowlisted:8443'`); `egressProbePayloadCount: 1`;
  `[egress-layer-probe] {"policy":"REQ-NET-001","destination":{"protocol":"https:","hostname":"api.anthropic.com","port":"8443"},"outcome":"rejected","error":"net::ERR_BLOCKED_BY_CLIENT"}`;
  `egressProbeObserved: true`; `egressProbeUnexpectedDestinations: []` — the app ignored
  `CHIRALITY_EGRESS_LAYER_PROBE_URL=http://127.0.0.1:9/…` and requested only the fixed
  `:8443` destination, which the real policy cancelled; both in-page probes observed;
- cleanup pass (GUI and daemon exit 0, temp root removed).

Retained-copy normalization (recorded): the proof script's `START …` line carries one
trailing space that the repository's `git diff --check` gate rejects; the retained
`packaged-gui.log` has that single trailing space removed — raw 3,710 B
`f5a71eeefc123a4d8c859210a008b85f62b5d70b5213caae6610ece2eaecaf13`, retained 3,709 B
`ba9d2379998dc61b0ee32337824f7faca26a2fe751b263922658beb9e9750288`. The other four files are
byte-identical to the run output. `MANIFEST.sha256` (sorted by filename) lists the retained
bytes; verify with `shasum -a 256 -c MANIFEST.sha256` in the directory. The retained
`packaged-gui.log` carries the scratch-worktree `appPath` and the launcher opt-out path
`/Users/ryan/.local/bin/chirality` — verbatim proof output, same pattern as the bundles
already on `main`, no secret.

## 5. Environment, containment, and rerun method

- cwd for frontend commands: `projects/chirality-app-dev/frontend`; node v24.18.0, npm
  11.16.0, Vitest 4.1.10, Next 15.5.21, Electron 43.2.0, electron-builder 26.15.3; darwin
  25.6.0 arm64. Packaged-proof effective env: the script's own (`CHIRALITY_USER_DATA` temp
  root, `CHIRALITY_SKIP_CLI_LAUNCHER=1`, two in-page network probe URLs,
  `CHIRALITY_RENDERER_SECURITY_PROBE=1`, `CHIRALITY_RENDERER_SECURITY_PROBE_DELAY_MS=1500`,
  `CHIRALITY_EGRESS_LAYER_PROBE_URL` = the loopback decoy; fixture credential only;
  `realCredentialsUsed: false`, `ownerUserDataTouched: false`, `providerScopeExpanded: false`).
- Containment: `validate_change_scope.py` PASS with 0 violations against the sealed fence
  (exact command in the run record `CHECKS.json`); no `main.ts`, `runtime/**`,
  `package.json`, dependency, `preload.ts`, `next.config.mjs`, `docs/**`, or CI workflow
  change; no destination added to REQ-NET-001 (F-APP-1); no release act (F-APP-2).
- Rerun: from `frontend`, `npm ci` (after `npm ci && npm run build` in `runtime/`), `npx
  vitest run src/__tests__/electron/renderer-window-policy.test.ts
  src/__tests__/scripts/run-packaged-security-proof.test.ts src/__tests__/contract-pins.test.ts`,
  then `npm run desktop:pack && rm -rf artifacts/release-verification/packaged-security &&
  npm run proof:packaged-security` and compare `summary.json` `networkProof` fields
  (`egressLayerDiagnostics > 0`, `egressProbeObserved: true`, `egressProbeUnexpectedDestinations: []`)
  and the `[egress-layer-probe]` line's `"port":"8443"` in `packaged-gui.log`.
- A1 re-stage rule: this tranche mutates `frontend/`; the staged R20 procedure is
  invalidated for any future proof claim and a newly staged revision plus a fresh
  owner-executed proof are required (run record `STEP0_DISCOVERY.md` §3).
