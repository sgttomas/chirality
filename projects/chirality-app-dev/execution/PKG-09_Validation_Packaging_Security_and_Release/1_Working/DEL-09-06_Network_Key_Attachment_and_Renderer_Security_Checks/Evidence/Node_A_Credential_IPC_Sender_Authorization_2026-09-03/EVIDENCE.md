# Evidence — DEL-09-06-V3-01: credential IPC sender authorization and G-CSP renderer-hardening (2026-09-03)

> Derivative evidence package (App AGENTS.md derivative-package rule). Accepted
> upstream: `main` at `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge;
> A12 seating). Run record: `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_A_2026-09-03/`.
> Executed by Claude Fable 5.1 (`claude-fable-5-1`) as ephemeral Agent 2 implementer
> under HELP_HUMAN. This package makes no release-readiness, signing, notarization,
> distribution, certification, or lifecycle claim.

## 1. Claim

All six `ipcMain.handle` credential channels in `frontend/electron/api-key-ipc.ts`
(`chirality:api-key-store`, `chirality:api-key-remove`, `chirality:api-key-status`,
`chirality:provider-api-key-store`, `chirality:provider-api-key-remove`,
`chirality:provider-api-key-status`) reject any sender whose frame origin is not
exactly the renderer origin the main process created the window for, using the one
policy shared with `runtime-control-ipc.ts` (`frontend/electron/ipc-sender-policy.ts`).
A denied request returns a typed, secret-free result (`{ ok: false, error: 'Credential
request was denied' }` on mutation channels; a fail-closed status object carrying the
same `error` on status channels), never reaches the daemon client, never throws into
the renderer, and emits one desktop-log line `desktop.credential_ipc.denied` with the
channel and the sender *origin* only.

## 2. Source identities at freeze (SHA-256 of the file bytes)

| File | SHA-256 |
|---|---|
| `frontend/electron/ipc-sender-policy.ts` (new) | `7bcd48d3bdcc1cbe8e62f187d1dcf53c03160bdcc518283dc16aac051ff1180e` |
| `frontend/electron/api-key-ipc.ts` | `219b7d676ddaa84ca553af7645e0b52c9ce6c9baa36dfe4fef057685fdfba6f8` |
| `frontend/electron/runtime-control-ipc.ts` (imports the shared policy; behaviour identical) | `29eeb34086adefa931d12ad6e7ad542a365127839f994c7883f50081a56f6409` |
| `frontend/electron/main.ts` (plumbing: `rendererOrigin` and desktop-log sink passed to the credential handlers, registered after the renderer URL is resolved) | `9eca0e1a12d1fbf86662837023236612077cf3756a82a31502df897b18f424b3` |
| `frontend/src/__tests__/electron/ipc-sender-policy.test.ts` (new) | `5682b75cd467e2bf6e09a764e1dd2eb7cd7768c4bcc86cbb4bfc05dee057a890` |
| `frontend/src/__tests__/electron/api-key-ipc.test.ts` | `2fa5c5ab4bbd2b1e63a0ed1e7a907ba13388d1c2da9c3a69dec008ab18f0cf59` |
| `frontend/src/__tests__/contract-pins.manifest.ts` | `a7bae2c5b2703754be63f5583db062b05d5513eec102f15c1b2845a9691dac09` |

The frozen commit's tree is the authoritative byte identity; the review PASS and the
receipt name that commit.

## 3. Unit-level evidence (Vitest 4.1.10, node v24.18.0, cwd `frontend`)

- `src/__tests__/electron/ipc-sender-policy.test.ts` — 17 tests: 3 authorized
  forms (root, nested path + query, hash); 12 rejected forms (no frame, null frame,
  no url, empty url, unparseable, different host, different port, different scheme,
  remote origin, `file:` url, origin embedded in path, origin as userinfo); empty
  renderer origin authorizes nothing; `describeIpcSender` yields origin only.
- `src/__tests__/electron/api-key-ipc.test.ts` — 58 tests, of which the
  `sender authorization` block runs, for **each of the six channels**: authorized
  sender reaches the daemon client exactly once with no log line; foreign origin
  (`https://attacker.example/`) is denied with the typed result, the daemon client
  is never called, the result and the log calls contain no key material, and one
  `warn desktop.credential_ipc.denied { channel, sender: 'https://attacker.example' }`
  line is emitted; a request with no sender frame is denied (`sender:
  'no-sender-frame'`); a same-host different-port sender is denied; the sender check
  runs before provider/key argument validation; denial holds without a log sink.
- `src/__tests__/electron/runtime-control-ipc.test.ts` — 11 tests unchanged and
  passing, including its existing foreign-origin rejection, proving the shared policy
  did not change runtime-control behaviour.
- `src/__tests__/contract-pins.test.ts` — 15 targets; new pins (see §5).

Command and result: `npx vitest run <the seven touched files>` → 7 files, 151 passed,
0 failed, exit 0. Full suite `npm test` → 157 files passed, 1 skipped; 1364 tests
passed, 4 skipped; exit 0. `npm run typecheck` exit 0. `npm run build` exit 0.

## 4. Packaged evidence (host surface, ran inside the session sandbox — no escalation needed)

`npm run desktop:pack` (exit 0) then `npm run proof:packaged-security` (exit 0,
status `pass`). Compact non-secret bytes are retained under
`packaged-security-proof/` with `MANIFEST.sha256` (sorted; verify with
`shasum -a 256 -c MANIFEST.sha256` in that directory):

- artifact identity `f8b954e1d926867f28aa961c9ba186303be5fc039f1dd47229988ad5e0988de6`
  (`Contents/MacOS/Chirality` 33,968 B `79019361…`; `app.asar` 448,803,467 B
  `f7913db4…`; `runtime-cli/chirality-cli.mjs` 75,460 B `0503c40a…`); built from the
  pre-commit working tree, `sourceRevision` reports HEAD `0c683fb16`;
- all 10 packaged policy markers present; credential proof pass — and the
  daemon-owned status observed through the real packaged daemon and `RuntimeClient`
  carries the typed storage state (`missing` → `available`/`ui` → `missing`), which
  is the DEL-04-05-V3-01 field arriving without any `runtime/**` change;
  `retainedSecretFindings: []`;
- network proof pass: 5 snapshots, 7 loopback endpoints, `nonAllowlistedOutboundTcp: []`,
  1 blocked renderer diagnostic (`host_not_allowlisted:example.com`), probe payload
  observed; `retainedMetadataLeakFindings: []`;
- cleanup pass: GUI pid 58785 and daemon pid 58729 both exited 0 on SIGTERM,
  temp root removed (`cleanup.json`).

Retained-copy normalization (recorded, not hidden): the proof script writes its
`START …` line with one trailing space after the command arguments, which the
repository's `git diff --check` gate rejects. The retained `packaged-gui.log` has that
single trailing space on line 1 removed (raw bytes 2,513 → 2,512; raw SHA-256
`a08669d17e92833c0858d2940f1fae914af012c1acf2d1e6853047c14dde24c9`, retained SHA-256 in
`MANIFEST.sha256`). No other byte differs; `packaged-daemon.log`, `summary.json`,
`cleanup.json`, and `tcp-snapshots.json` are byte-identical to the proof output.

The packaged proof exercises the credential channels through the daemon client, not
through a renderer frame, so the sender check itself is proved at unit level (§3);
the packaged run proves the changed bytes still build, launch, store/status/remove
through safeStorage, and keep the egress policy intact.

## 5. G-CSP renderer-hardening inventory (unit-level)

| Surface | Policy in source | Test evidence |
|---|---|---|
| Explicit `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true`, preload wiring | `frontend/electron/main.ts:512-517` | **New** contract pins (`contract-pins.manifest.ts`, target `electron/main.ts` "G-CSP renderer hardening"): contains the three flags and the preload path; notContains `contextIsolation: false`, `nodeIntegration: true`, `sandbox: false`, `webSecurity: false`, `allowRunningInsecureContent`, `nodeIntegrationInWorker`, `nodeIntegrationInSubFrames`, `enableRemoteModule` |
| Per-window bounded egress | `main.ts:68-70, 225-292, 524` | Existing pins (`contract-pins.manifest.ts` "Renderer network-policy hardening"); **new** pin `registerRendererEgressPolicy(window);`; packaged proof §4 (blocked diagnostic, zero non-allowlisted outbound) |
| Privileged IPC sender authorization | `ipc-sender-policy.ts`; adopted in `api-key-ipc.ts` and `runtime-control-ipc.ts` | §3 tests; **new** pins on both IPC modules (shared import, six `denied(event, …)` guards, no private `isAuthorizedSender` copy, no `senderFrame.url` logging) |
| Window-open denial (`setWindowOpenHandler`) | **absent** | none — outside this tranche's write locus (`main.ts` plumbing only); reported as a scope need in the run record `RETURN.md` |
| Navigation constraint (`will-navigate`/`will-redirect`) | **absent** | none — same scope need |
| CSP effectiveness (renderer document CSP) | **absent** (no header/meta in `electron/`, `src/`, `scripts/`, `next.config.mjs`) | none — same scope need |

No existing policy was weakened. The three absent surfaces are reported truthfully
rather than inferred; closing them needs a write-locus extension (a renderer-window
hardening module under `frontend/electron/` plus a CSP at the Next response layer)
and is a HELP_HUMAN decision.

## 6. Environment, containment, and rerun method

- cwd for frontend commands: `projects/chirality-app-dev/frontend`; effective env for
  the packaged proof: defaults of `scripts/run-packaged-security-proof.mjs` (isolated
  `CHIRALITY_USER_DATA` temp root, `CHIRALITY_SKIP_CLI_LAUNCHER=1`, fixture credential
  only; `realCredentialsUsed: false`, `ownerUserDataTouched: false`).
- Containment: write-scope validation `validate_change_scope.py` PASS against the
  brief's fence (run record `CHECKS.json`); no `runtime/**`, `package.json`, or
  dependency change.
- Rerun: from `frontend`, `npm ci`; from `runtime`, `npm ci && npm run build`; then
  `npm run typecheck && npm test && npm run build && npm run desktop:pack && npm run
  proof:packaged-security`. Packaged results are reproduced only as to their
  pass/fail observations and marker set; unsigned bundle bytes are not asserted to
  be byte-deterministic across rebuilds.
