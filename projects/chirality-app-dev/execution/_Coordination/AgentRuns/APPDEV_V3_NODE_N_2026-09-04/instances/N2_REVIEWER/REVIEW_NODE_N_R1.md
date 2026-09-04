# Node N independent software review — round 1

Date: 2026-09-04  
Item: `DEL-09-06-V3-04`  
Basis: `307addfc259b046aeb2ed07d47086cd5686c35b8`  
Reviewed freeze: `dca2ef103f9a22e38d815c5f21638220ad454223`  
Diff: 1 commit; 100 paths; 18,071 insertions; 96 deletions  
Reviewer worktree: `/private/tmp/chirality-app-v3-csp-20260904/nodeN-review-r1` (detached, retained)  
Review mode: fresh, independent, read-only Agent-2 instruction posture. Under the delegated-harness-native calibration, the Agent-2 role is not mechanically enforced; role evidence is instruction-asserted, and K-SUBAGENT/non-delegation is instruction+config asserted rather than mechanism-proven.

## Verdict

**PASS** — zero BLOCKER, zero MAJOR, zero MINOR. Two non-blocking NOTES are recorded below. The frozen implementation is valid for manager fan-in; this is not lifecycle acceptance, release authority, signing/notarization, distribution, or a release-readiness claim.

The nonce implementation is structurally single-source and fail-closed. A cryptographically strong 128-bit nonce is generated for each packaged request. One policy value is placed into the request before Next renders and byte-identically into the response. Packaged `script-src` is exactly `'self'` plus that nonce and contains neither `'unsafe-inline'` nor `'unsafe-eval'`. The app layout consumes the nonce from the same request CSP. Electron installs no packaged fallback that could disagree. Development retains its former exact static policy. All four selected routes build dynamically and rendered successfully in real packaged BrowserWindows.

## Scope and inventory

`307addfc..dca2ef1` is a direct one-commit descendant. Exact change-scope validation passed with the seven implementation/test paths, the Node N deliverable evidence and run-record roots, and the Node N AgentRuns root as the only allowances. No authority-corpus, package/version/lockfile, plan, decision/register, other deliverable state, Root, or `.github` path changed. `_STATUS.md`, `MEMORY.md`, and `loop/LOOP_RECEIPTS.md` remain untouched before review.

All 100 changed paths were read. This is the complete inventory, with `A`/`M` retaining Git's add/modify meaning.

Common prefix `E/` means:
`execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/Evidence/Node_N_CSP_Nonce_2026-09-04/`

```text
A E/EVIDENCE.md
A E/MANIFEST.sha256
A E/packaged-security-proof-attempt1-sandbox-abort/MANIFEST.sha256
A E/packaged-security-proof-attempt1-sandbox-abort/cleanup.json
A E/packaged-security-proof-attempt1-sandbox-abort/packaged-daemon.log
A E/packaged-security-proof/MANIFEST.sha256
A E/packaged-security-proof/cleanup.json
A E/packaged-security-proof/packaged-daemon.log
A E/packaged-security-proof/packaged-gui.log
A E/packaged-security-proof/summary.json
A E/packaged-security-proof/tcp-snapshots.json
A E/secret-scan-summary.json
A E/section8-local-attempt1-missing-electron/MANIFEST.sha256
A E/section8-local-attempt1-missing-electron/logs/coalition-supervisor.json
A E/section8-local-attempt1-missing-electron/logs/driver.log
A E/section8-local-attempt1-missing-electron/private/lsof-port-52124.stderr
A E/section8-local/MANIFEST.sha256
A E/section8-local/artifacts/release-quality/logs/full_test.stderr.log
A E/section8-local/artifacts/release-quality/logs/full_test.stdout.log
A E/section8-local/artifacts/release-quality/logs/premerge.stderr.log
A E/section8-local/artifacts/release-quality/logs/premerge.stdout.log
A E/section8-local/artifacts/release-quality/logs/section9.stderr.log
A E/section8-local/artifacts/release-quality/logs/section9.stdout.log
A E/section8-local/artifacts/release-quality/logs/typecheck.stderr.log
A E/section8-local/artifacts/release-quality/logs/typecheck.stdout.log
A E/section8-local/artifacts/release-quality/summary.json
A E/section8-local/artifacts/section8-run/api/regression.session_crud.json
A E/section8-local/artifacts/section8-run/api/section8.boot_error_taxonomy.json
A E/section8-local/artifacts/section8-run/api/section8.interrupt_sigint.json
A E/section8-local/artifacts/section8-run/api/section8.permissions_dontask.json
A E/section8-local/artifacts/section8-run/api/section8.sdk_native_stream.json
A E/section8-local/artifacts/section8-run/api/section8.session_persistence_resume.json
A E/section8-local/artifacts/section8-run/api/section8.smoke_stream.json
A E/section8-local/artifacts/section8-run/api/setup.server_reachable.json
A E/section8-local/artifacts/section8-run/cleanup/sessions.json
A E/section8-local/artifacts/section8-run/logs/regression.session_crud.json
A E/section8-local/artifacts/section8-run/logs/section8.boot_error_taxonomy.json
A E/section8-local/artifacts/section8-run/logs/section8.interrupt_sigint.json
A E/section8-local/artifacts/section8-run/logs/section8.permissions_dontask.json
A E/section8-local/artifacts/section8-run/logs/section8.sdk_native_stream.json
A E/section8-local/artifacts/section8-run/logs/section8.session_persistence_resume.json
A E/section8-local/artifacts/section8-run/logs/section8.smoke_stream.json
A E/section8-local/artifacts/section8-run/logs/setup.server_reachable.json
A E/section8-local/artifacts/section8-run/sse/section8.interrupt_sigint.sse
A E/section8-local/artifacts/section8-run/sse/section8.permissions_dontask.allow.sse
A E/section8-local/artifacts/section8-run/sse/section8.permissions_dontask.deny.sse
A E/section8-local/artifacts/section8-run/sse/section8.sdk_native_stream.sse
A E/section8-local/artifacts/section8-run/sse/section8.smoke_stream.sse
A E/section8-local/artifacts/section8-run/summary.json
A E/section8-local/artifacts/stable/section8-latest-summary.after-release-quality.json
A E/section8-local/artifacts/stable/section8-latest-summary.json
A E/section8-local/artifacts/stable/section9-latest-manifest.json
A E/section8-local/artifacts/stable/section9-latest-summary.json
A E/section8-local/logs/build-electron.log
A E/section8-local/logs/built-bundles.sha256
A E/section8-local/logs/cleanup.txt
A E/section8-local/logs/coalition-capability.json
A E/section8-local/logs/coalition-supervisor.json
A E/section8-local/logs/containment-after.txt
A E/section8-local/logs/containment-before.txt
A E/section8-local/logs/daemon-descendant-audit.json
A E/section8-local/logs/daemon.log
A E/section8-local/logs/driver.log
A E/section8-local/logs/environment.txt
A E/section8-local/logs/git-status-after.txt
A E/section8-local/logs/git-status-before.txt
A E/section8-local/logs/harness-ready.json
A E/section8-local/logs/launchagent-job.stderr.log
A E/section8-local/logs/launchagent-job.stdout.log
A E/section8-local/logs/next-descendant-audit.json
A E/section8-local/logs/next-dev.log
A E/section8-local/logs/premerge.machine-lines.txt
A E/section8-local/logs/premerge.stderr.log
A E/section8-local/logs/premerge.stdout.log
A E/section8-local/logs/registration.redacted.json
A E/section8-local/logs/release-quality.machine-lines.txt
A E/section8-local/logs/release-quality.stderr.log
A E/section8-local/logs/release-quality.stdout.log
A E/section8-local/logs/result.txt
A E/section8-local/logs/teardown.txt
A E/timing-observations.json
```

Common prefix `R/` means `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_N_2026-09-04/`.

```text
A execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/DEL-09-06_Network_Key_Attachment_and_Renderer_Security_Checks/_run_records/TASK_RUN_2026-09-04_NODE_N.md
A R/CHECKS.json
A R/HANDOFF_STATE.md
A R/MANIFEST.sha256
A R/ORCHESTRATION_PLAN.md
A R/RETURN.md
A R/REVIEW_N2_HANDOFF.md
A R/STEP0_DISCOVERY.md
A R/WORK_GRAPH.json
A R/instances/N1_IMPLEMENTER/LAUNCH_BRIEF.md
A R/instances/N1_IMPLEMENTER/RETURN.md
A R/instances/N1_IMPLEMENTER/STATUS.json
M frontend/electron/main.ts
M frontend/electron/renderer-window-policy.ts
M frontend/scripts/run-packaged-security-proof.mjs
M frontend/src/__tests__/contract-pins.manifest.ts
M frontend/src/__tests__/electron/renderer-window-policy.test.ts
M frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts
M frontend/src/app/layout.tsx
```

The inventory comprises 81 evidence paths, one deliverable run record, 11 coordination/run-record paths, and seven product/test paths: 100 total.

## Design and threat analysis

### Nonce generation and header safety

- `createRendererCspNonce` uses `node:crypto.randomBytes(16)` and base64 encoding (`renderer-window-policy.ts:149-155`), giving 128 bits of cryptographic randomness per invocation.
- The accepted alphabet rejects control characters, whitespace, quotes, semicolons, and CR/LF before a nonce can enter a header (`renderer-window-policy.ts:150,157-161`). The test rejects a directive-injection value and decodes generated values back to exactly 16 bytes.
- A new helper invocation occurs inside the Node request callback, not at process or server initialization (`main.ts:482-486`). The live four-route proof observed 12/12 distinct document/response nonces; every route's two consecutive uncached responses differed.

### One coherent policy and nonce source

- `applyPackagedRendererRequestPolicy` constructs the policy once and writes the exact same string into lowercase Node request headers and the response (`renderer-window-policy.ts:239-248`). The unit test uses object identity/value assertions against both sinks.
- The helper runs before `handle(req, res)`, so pinned Next reads the nonce-bearing request CSP while rendering (`main.ts:482-486`). An incoming client CSP is overwritten rather than trusted.
- The async root layout reads only that request CSP and applies its parsed nonce to the app-owned theme script (`layout.tsx:61-95`). There is no separate companion nonce header.
- Packaged `installRendererWindowPolicy` receives no fallback CSP; its response hook therefore cannot fabricate a conflicting policy. Development alone receives the prior static fallback. Real responses confirmed a single conforming policy whose nonce matched every inline script in the corresponding returned HTML.

### Policy preservation and route behavior

- Packaged `script-src` is exactly `'self'` plus one nonce. It contains neither unsafe script allowance. All other directives are unchanged from the basis, including self-only `connect-src`, no frames/objects/embedding, self-only base/form/worker/manifest/media, and the existing style/image/font allowances.
- The development policy is pinned by an exact-string assertion, including its pre-existing inline/eval and same-origin HMR WebSocket allowances. No development execution path changed.
- Reading request headers intentionally changes `/`, `/chat`, `/pipeline`, and `/workbench` from static to dynamic. The build classified all four `ƒ (Dynamic)`, and the packaged proof rendered all four in real BrowserWindows.
- Normal startup still creates one `/` window. Four-window startup is gated by both `app.isPackaged` and the explicit proof environment flag (`main.ts:706-715`).

### Proof fail-closed behavior and non-circularity

- The live proof obtains the loaded-document nonce and separately fetches the same route twice with `cache: no-store`. For each fresh response it parses the actual response CSP and actual returned HTML, requires HTTP 200/HTML/completeness, requires inline scripts to exist, and requires each inline script nonce to equal that response's CSP nonce.
- Its aggregate predicate requires exactly one payload for every named route, exactly three observed nonces per route, global uniqueness, one nonce source and self in every response `script-src`, unsafe script allowances absent, the expected enforced `connect-src` denial, no unexpected recorded violation, window-open denial, navigation denial, and overall credential/network/cleanup success.
- Negative tests fail on a missing route payload, a reused nonce across routes, unsafe inline, widened connect/frame directives, an own-resource violation, missing proof entirely, window/navigation weakening, and malformed/missing/unexpected egress evidence. This prevents empty-log, empty-script, or one-route success.
- Contract pins are additional drift alarms, not the proof source. They pin the actual server call, single-policy assignments, route list, unsafe-inline rejection, and global uniqueness. The behavior tests invoke the implementation and summarizer directly; the real packaged proof independently parses live responses.

### Adjacent controls and cleanup

- No changed code weakens navigation, window-open, egress, credential, renderer preferences, or credential IPC authorization. Existing exact tests remained green.
- The packaged proof found no non-loopback outbound TCP, no credential/metadata leak, and confirmed both root process exits and stream closure. The reviewer exact-freeze run also left no matching process or listener. The separate Node H lifecycle method passed premerge, release quality, all eight Section-8 checks, Section 9 in its report-only premerge position, and coalition teardown with no final member, listener, or socket.
- The packaged bundle had no Developer ID/team identity. macOS reported only the Electron executable's ordinary ad-hoc linker signature (`TeamIdentifier=not set`, no sealed-resource envelope). A direct archive scan found no `sk-ant-` value and only documentation/example URL-credential fixtures. No host identity, Syft, Apple, signing/notarization, distribution, publication, or release state was changed.

## Evidence-vacuity and reproducibility assessment

The principal nonce proof is non-vacuous: four actual windows produced four route payloads; each loaded document contained inline scripts; two independently returned HTML responses per route also contained inline scripts; all applicable policies and script attributes matched; 12 distinct values were observed; and deliberate block actions proved CSP, navigation, and window-open enforcement remained active. A response-only nonce, a request-only nonce, a static/process nonce, an unsafe fallback, an empty page, or a missing route would fail the recorded predicate.

All 39 changed JSON files parsed under strict duplicate-key/non-finite rejection. The run-level manifest verified 10 entries, and five nested evidence manifests verified every listed byte. The Node N evidence root's manifest accounts for all 80 children other than the manifest itself. The evidence and run records consistently identify the basis, selected item, A15, A1 consequence, and separate post-merge Section-8 revision-3 obligation. The timing comparison is explicitly a single-run observation with `acceptance_threshold: null`; it does not invent a performance gate.

The retained packaged proof is exact about the artifact it ran: summary SHA-256 `7d05f5a49b4f87099bed08243a21e1d3f1897240419752c877aef1f55cb9ef1b`, artifact identity `21caf9abd8b0d90a31c6d784e48575e5a276a1ae9131106fd418790aa4be0686`, and file hashes are manifest-covered. It candidly records basis `307addfc...` as `sourceRevision` because the artifact was produced from the pre-freeze dirty working tree. The independent reviewer rebuilt and ran the same proof at exact freeze `dca2ef1...`; it passed with exact-freeze artifact identity `1c235d502ffd698e3db10d7bfe54911ace0e9692f406256dcd159a57f9bd8228` and summary SHA-256 `2e79a0fb0c764c04a3add956a24f23a1f6de27cd5a7b110c9b5d2db2a2f26937`. The compiled Electron `dist-electron/main.js` inside both artifacts was byte-identical (`a3c3309f93c99d96b9d3be6b573e9e9d52a592086c590c47cdef749ac9718180`). The whole `app.asar` differs because the broad `.next/**/*` packaging rule admits cache state, and Next server chunks embed worktree paths and derived module identifiers. See NOTE N1-R1-N1.

## Independent checks

| Check | Result | Reviewer evidence |
|---|---|---|
| Basis ancestry / commits | PASS | Basis is direct ancestor; exactly one reviewed commit. |
| Exact change-scope, run first | PASS | 100 paths; `violations: []`; independent manual classifier also accounts for all paths. |
| Affected-check selector | PASS | Selected `app-hold-integrity` and `harness-self-check`; broader sealed-brief gates were also run. |
| Runtime `npm ci` + build | PASS | 61 packages; TypeScript build passed. |
| Frontend `npm ci` | PASS after host permission | Initial sandbox attempt failed `ENOTFOUND` and was not counted; exact rerun installed 753 packages. |
| Typecheck | PASS | `npm run typecheck`. |
| Focused Vitest | PASS | Three files; 97 tests. |
| Full Vitest | PASS | 165 files passed, one suite intentionally skipped; 1,567 tests passed, four intentionally skipped. |
| Production build | PASS | Next 15.5.21; all four routes dynamic; Electron build passed. |
| `desktop:pack` | PASS | Unsigned/local arm64 package; dependency boundary and instruction-root integrity passed; known source-completeness informational status remains `needs_remediation`. |
| Real exact-freeze packaged proof | PASS | Four routes; 12 unique nonces; inline matches; no unsafe script allowances; no unexpected recorded violations; egress/credential/cleanup predicates passed. |
| Node H lifecycle premerge/release-quality/Section 8 | PASS after prerequisite repair | First attempt failed honestly because cached Electron had not been unpacked and cleanup passed; the pinned cached Electron zip was verified and unpacked, then the exact rerun passed with coalition cleanup. |
| D-APP-36 risk-calibrated render bar | PASS | Four real packaged BrowserWindows; no CSS, geometry, copy, control-state, or interaction change warrants screenshot comparison. |
| Independent project secret scan | PASS | 7,386 files; zero blocked; 26 allowlisted fixtures; relevant environment secret inputs absent. |
| Packaged archive secret/prohibited-identity inspection | PASS | No Anthropic-key pattern; URL-credential matches were documentation fixtures; no Developer ID/team identity. |
| Receipts validator, read-only | PASS | `VALID`; ledger unchanged. |
| Authority corpus | PASS | v20, no drift. |
| APP-HOLD dispatch | PASS | `ALLOW`; no active hold. |
| APP-HOLD integrity | PASS | 53 contracts; register match. |
| Scope-of-work validator | PASS | `SOW_V1`. |
| Harness self-check | PASS | Only known repo-wide informational/not-applicable/review/warning findings, outside Node N. |
| Harness pytest | PASS | 350 tests. |
| Strict JSON | PASS | 39 changed JSON files; duplicate keys and non-finite values rejected. |
| Manifests / membership | PASS | Run manifest 10/10; five nested evidence manifests; complete path accounting. |
| `git diff --check` | PASS | Basis-to-freeze diff clean. |
| F-APP-2 / forbidden paths | PASS | Matches are negations, proof exclusions, or future mechanics; no prohibited claim or path mutation. |
| Reviewer cleanup | PASS | No residual reviewer process/listener; detached worktree remains as instructed. |

No required command was skipped. The full suite's four test skips are suite-declared skips, not skipped review commands.

## Findings

### BLOCKER

None.

### MAJOR

None.

### MINOR

None.

### NOTE N1-R1-N1 — retained artifact is byte-bound but not commit-bound

Locations: `E/EVIDENCE.md:82`; `E/packaged-security-proof/summary.json:10`; `R/CHECKS.json:63`.

The retained final proof identifies exact artifact bytes but labels its `sourceRevision` with basis `307addfc...`, because the package was built before the implementation/evidence freeze commit. The disclosure is truthful, and the independent exact-freeze rebuild/proof passed. The compiled Electron main bundle was byte-identical between the retained and reviewer artifacts. The enclosing `app.asar` was not byte-identical: the package includes `.next/cache` when present, and Next chunks contain worktree-specific paths/derived module identifiers. This does not undermine the reviewed nonce behavior, but the retained artifact should not be described as cryptographically source-commit-bound to `dca2ef1...`.

Disposition: non-blocking evidence calibration. Carry the exact-freeze reviewer proof identity and summary hash into the durable review record, and rerun the packaged proof after any rebase/closeout before reliance. A future packaging-hardening tranche may exclude `.next/cache` if reproducible/minimal packages become an acceptance goal; that is outside this item and no release/distribution claim exists here.

### NOTE N1-R1-N2 — violation telemetry begins after initial document load

Location: `frontend/electron/renderer-window-policy.ts:403-535`, especially `:465` and the after-load scheduling at `:523-525`.

The injected `securitypolicyviolation` listener observes the deliberate post-load connect denial and later probe activity. It cannot retrospectively observe an initial-load own-resource violation. Therefore `unexpectedViolations: []` is not, by itself, complete initial-load telemetry. The target nonce invariant is still non-vacuously proved by the loaded document's nonced inline scripts, two actual fresh response CSP/HTML comparisons per route, exact request/response helper tests, all-route rendering, and the real packaged pass.

Disposition: no remediation required for DEL-09-06-V3-04. Interpret the empty violation array with its actual post-load boundary and rely on the combined evidence, not that array alone. If a future item requires comprehensive initial-load violation telemetry, install instrumentation at document start or use an equivalent browser/devtools capture before navigation.

## Residual risk and handoff

- Random uniqueness is probabilistic by design; 128-bit entropy makes accidental collision negligible, while the aggregate proof rejects any observed reuse.
- The timing record is one same-host observation, not a distribution or threshold. G5 may weigh it later.
- The broader packaged-source completeness result remains the pre-existing `needs_remediation` informational state; Node N neither changes nor closes it.
- A1 is correctly declared: this `frontend/` mutation invalidates staged R20 for future reliance. A separate `DEL-09-01-V3-01` revision 3 is owed only after this product change lands; Node N does not perform or claim it.
- Product/test bytes must remain frozen after this PASS. Narrative-only closeout evidence may record this report and the two notes. Any product/test mutation requires a fresh review.

Exact product/test blob identities at the reviewed freeze:

```text
frontend/electron/main.ts                                               ee6aec3137a130096b85a9a4e8fb556aec996a07
frontend/electron/renderer-window-policy.ts                             2d225dbfb7eb1f297acc4f76c54c70e9379ba0c0
frontend/scripts/run-packaged-security-proof.mjs                        b8e5dad3f388bb76f1e4bc5c80a9e186078376b2
frontend/src/__tests__/contract-pins.manifest.ts                        d948c6d6eff4c39413a49da285ec49864098fd47
frontend/src/__tests__/electron/renderer-window-policy.test.ts          cd9d7ddaec0d3599a09f322e7767e9456eb8ff03
frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts      e30d0ecb63d734dbed7acfa71e09802a8b68124d
frontend/src/app/layout.tsx                                             0d89358787b2f55340267d78738b0bd943ae862e
```

