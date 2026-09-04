# Node N — per-response packaged renderer CSP nonce evidence

Status: implementation complete and awaiting independent review. This evidence is not acceptance, lifecycle issuance, release authority, signing/notarization, distribution, or a future-proof reliance claim.

## Identity and boundary

- Basis: `307addfc259b046aeb2ed07d47086cd5686c35b8` (PR #694 merge).
- Selected item: `DEL-09-06-V3-04` only.
- Host/toolchain: macOS 26.6.2 build 25G83, Darwin 25.6.0 arm64; Node v24.18.0; npm 11.16.0; Next 15.5.21; Electron 43.2.0; TypeScript 5.9.3; Vitest 4.1.10.
- No credentials, tokens, private account material, signing identity, distributable artifact, or owner user-data is retained here.

## Design and implementation locus

The packaged custom server generates 16 random bytes per request with Node `randomBytes` and base64-encodes them. It builds the CSP once, writes the byte-identical value to the incoming `content-security-policy` request header before Next handles the request, and attaches that same value to the outgoing response. Next 15.5 reads the request policy and nonces its framework scripts; the async root layout reads the same request policy and applies its nonce to the app-owned theme bootstrap. There is deliberately no companion nonce header, so only one nonce-bearing policy can govern Next, the layout, and the response.

Packaged `script-src` is exactly `'self'` plus the per-request nonce and contains neither `'unsafe-inline'` nor `'unsafe-eval'`. Every other directive is preserved. Development still uses the pre-change static policy including `'unsafe-inline'`, `'unsafe-eval'`, and the same-origin HMR WebSocket sources; an exact-string unit assertion pins that posture.

The normal desktop launch still opens one root window. Only `CHIRALITY_RENDERER_SECURITY_PROBE=1` opens four hardened BrowserWindows so the proof observes `/`, `/chat`, `/pipeline`, and `/workbench` independently. The proof gathers the loaded document nonce and two fresh same-route responses, verifies every inline script against the applicable policy nonce, rejects any packaged `script-src` unsafe allowance, requires all observed nonces to be globally unique, and treats every CSP violation other than its exact deliberate `connect-src` denial as unexpected.

Changed implementation/test loci:

- `frontend/electron/renderer-window-policy.ts`
- `frontend/electron/main.ts`
- `frontend/src/app/layout.tsx`
- `frontend/scripts/run-packaged-security-proof.mjs`
- directly relevant renderer-policy, packaged-proof, and contract-pin tests/manifests

Rejected alternatives:

- A second nonce-bearing request header was prototyped, then removed before the final proof because it creates an avoidable disagreement surface beside the enforced CSP.
- A static packaged fallback in Electron's `onHeadersReceived` hook was rejected because it cannot know the nonce already embedded in a rendered response. That hook remains development-only.
- Hash/SRI was not attempted; A15 selected the nonce pathway, and a hash approach would require a separate spike.

## Timing method and observations

The timing comparison is observational only: no acceptance threshold exists or is invented. Both measurements use the same host, checkout, Node/Next versions, build command, route order, and commands. The server-reported production-start readiness time and `curl` response TTFB/total are recorded. “Cold start to first response” is reported as the server readiness observation plus the first `/` request TTFB; it is a descriptive sum, not an end-user visual metric or a gate.

Exact method for each side:

1. `npm run build` in `projects/chirality-app-dev/frontend`.
2. `NEXT_TELEMETRY_DISABLED=1 node node_modules/next/dist/bin/next start --hostname 127.0.0.1 --port 52123`.
3. After the server prints its `Ready in …` value, sequentially run `curl -fsS -o /dev/null -w 'route=… status=%{http_code} ttfb=%{time_starttransfer} total=%{time_total}\n'` for `/`, `/chat`, `/pipeline`, and `/workbench`.
4. Send SIGINT to the server and confirm exit 0.

### Pre-change basis observation

- Build: PASS; all four routes reported `○ (Static) prerendered as static content`.
- Server readiness: 120 ms.
- `/`: HTTP 200; TTFB 0.009756 s; total 0.009792 s.
- `/chat`: HTTP 200; TTFB 0.002051 s; total 0.002080 s.
- `/pipeline`: HTTP 200; TTFB 0.001867 s; total 0.001897 s.
- `/workbench`: HTTP 200; TTFB 0.001567 s; total 0.001587 s.
- Descriptive cold-start-to-first-response sum: 129.756 ms.
- Cleanup: server received SIGINT and exited 0.

### Post-change observation

- Build: PASS; `/`, `/chat`, `/pipeline`, and `/workbench` each reported `ƒ (Dynamic) server-rendered on demand`.
- Server readiness: 139 ms.
- `/`: HTTP 200; TTFB 0.025740 s; total 0.026817 s.
- `/chat`: HTTP 200; TTFB 0.007210 s; total 0.007657 s.
- `/pipeline`: HTTP 200; TTFB 0.006604 s; total 0.007021 s.
- `/workbench`: HTTP 200; TTFB 0.005114 s; total 0.005574 s.
- Descriptive cold-start-to-first-response sum: 164.740 ms.
- Cleanup: server received SIGINT, exited 0, and the retained process session closed.

These single-run observations show the intended static-to-dynamic classification change. They do not establish a performance distribution, end-user visual latency, or an acceptance threshold. In this observation the descriptive cold-start sum and each per-route response time were higher after the change; G5 can weigh that observation in its later fan-in.

## Assurance results

### Finalized product/test checks

- Focused Vitest: PASS — renderer policy, packaged proof, and contract pins; three files, 97 tests.
- Full Vitest: PASS under the required host permissions — 165 files passed, one skipped; 1,567 tests passed, four skipped. The first sandboxed full-suite attempt failed only on denied loopback/Unix-socket binds and is not counted as a pass.
- Typecheck: PASS.
- Production build and Electron build: PASS; all four operator routes are dynamic.
- `desktop:pack`: PASS with signing auto-discovery disabled; dependency boundary PASS; instruction-root integrity PASS with its pre-existing `source completeness: needs_remediation` informational result.
- Project evidence secret scan: PASS; 7,381 files scanned, zero blocked findings, 26 allowlisted fixture findings; retained result `secret-scan-summary.json` SHA-256 `556808bb24125eb94dd062fcc3662e3feaaedb8716c02363b2676d36f4bea62c`.

### Real packaged/browser proof

`packaged-security-proof/` is the compact retained final run. `summary.json` is `7d05f5a49b4f87099bed08243a21e1d3f1897240419752c877aef1f55cb9ef1b`; its unsigned artifact identity is `21caf9abd8b0d90a31c6d784e48575e5a276a1ae9131106fd418790aa4be0686`. The source-revision field names basis HEAD because the artifact was built from the pre-freeze working tree; the artifact hashes identify the exact proved bytes. This is not a signed, notarized, distributable, or release-ready artifact.

The real Electron run reports:

- exactly four route payloads, one each for `/`, `/chat`, `/pipeline`, and `/workbench`;
- 12 observed document/response nonces, all globally unique; every route's two consecutive response nonces differ;
- all response CSPs conform; `scriptUnsafeInlineAbsent: true` and `scriptUnsafeEvalAbsent: true` for every route;
- 7, 7, 9, and 7 inline scripts respectively, all carrying the nonce that matches their document or fetched response CSP;
- the deliberate enforced `connect-src` violation on every route and `unexpectedViolations: []`, so no own-resource CSP violation was observed;
- all four `window.open` and cross-origin navigation probes denied;
- zero non-allowlisted outbound TCP observations;
- GUI and daemon exit 0, stream closure confirmed, disposable root removed, and cleanup PASS.

The first in-sandbox packaged attempt is retained separately as `packaged-security-proof-attempt1-sandbox-abort/`: the daemon aborted before any GUI launch, its cleanup record is FAIL, and no passing inference is made. The same command rerun with the required host permission produced the final PASS bundle.

### Registered premerge/release-quality method

`section8-local/` is the final run of the Node H lifecycle method with `WITH_RELEASE_QUALITY=1`: premerge exit 0, release-quality exit 0, eight Section-8 checks PASS, Section 9 PASS in its report-only premerge position, coalition cleanup PASS, no final coalition members, no final port listener, and no final socket. The earlier attempt made before the cached Electron binary was materialized is retained as `section8-local-attempt1-missing-electron/` and is not counted as a pass.

Retained-copy normalization: `git diff --check` identifies a final empty line in five captured stdout/stderr logs and five SSE transcripts as a blank-at-EOF error. Only those empty terminal lines were removed from the retained copies; Section-8 event/log content is unchanged, and the updated folder manifest identifies the normalized bytes.

The D-APP-36 render/browser bar is met by the real packaged four-BrowserWindow proof. No CSS, geometry, user-facing copy, control state, or interaction behavior changed, so a screenshot comparison would not add layout evidence beyond the packaged render and zero-violation route matrix.

## Rerun boundary

Run-control `CHECKS.json` records the exact commands, cwd, runtime selection, exit results, initial operational failures, and final dispositions. Each generated proof folder has its own recomputable manifest; the run-level manifest covers every retained Node N byte.

Historical R20 is not relied upon: A1 requires a newly staged revision and a fresh owner-executed proof before any future proof claim. Node N does not perform or claim the later Section-8 revision 3; that separate tranche is owed only after this product change lands.
