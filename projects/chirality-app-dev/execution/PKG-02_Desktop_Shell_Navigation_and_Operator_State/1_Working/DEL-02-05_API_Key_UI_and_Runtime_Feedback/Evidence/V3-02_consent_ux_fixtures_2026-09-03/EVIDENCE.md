# Evidence — DEL-02-05-V3-02: static WP-07 account/consent UX fixtures behind a fake consent port (2026-09-03)

> Derivative evidence package (App AGENTS.md derivative-package rule). Accepted
> upstream: `main` at `e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge;
> node A). Run record: `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_F_2026-09-03/`.
> Executed by Claude Fable 5.1 (`claude-fable-5-1`) as ephemeral Agent 2 implementer
> under HELP_HUMAN (Claude Fable 5.1). This package makes **no live-account, login,
> network, release, signing, lifecycle, or reliance claim**: every state below is a
> static fixture rendered behind an in-memory fake; G3/G-WIRE/G-CSP/G4 are not
> claimed; the accepted Root/App account/consent contract (Root DEL-02-09) is not
> yet routed and its live consumption is DEL-02-05-V3-03.

## 1. Claim (OUT-002, REQ-001/003/004/005, AC-002, VER-002; CLM-028; fixture evidence toward the UI portions of AT-008/009/010/012/016/020/023/034)

The App now carries, under `frontend/src/**`, a renderer-side vocabulary and a
fake adapter shaped by App `docs/CONTRACT.md` K-CONSENT-1 (`HostedEngineConsentPort`),
K-NET-1 (posture vocabulary), K-KEY-1, and K-ROLE-2 (`docs/CONTRACT.md` SHA-256 in
`FIXTURE_INVENTORY.sha256`), thirteen static fixture snapshots, and an account/consent
settings panel that renders each of them distinctly with controls enabled or disabled as
the state requires. Every Return-contract item of the seated `_STATUS.md` entry is a
rendered, tested fixture:

| Return item | Fixture(s) | Rendered evidence (marker / verbatim copy) |
|---|---|---|
| Per-root login explanation | every fixture and the not-connected state | `p[data-explainer="per-root-login"]`: "Sign-in and consent are per working root. Signing in here applies only to the active root (`<canonicalRoot>`); every other root asks separately, and consent is never carried across roots, accounts, policies, or root generations." |
| Root-private app-owned `CODEX_HOME` copy | every fixture (`data-private-home` = `absent` / `present` / `invalidated`) | `p[data-explainer="private-home"]`: "Chirality keeps a root-private, app-owned Codex home for this root (`CODEX_HOME` = `<app user-data path>`). It never reads, copies, or links your ambient `~/.codex` directory." + per-status line. The snapshot type admits only `ambientCodexRead: false`. |
| Login/logout/account states | `loggedOutDefault`, `loggedInNotGranted`, `nullEmailEpoch`, `accountTransitionStale` | `p[data-account]` = `loggedOut` / `loggedIn`; `data-account-identity` = `none` / `digest` / `nullEmailEpoch`; label shows a digest **suffix** ("account …2d63f80e") or the volatile epoch — the full digest, and any email, never reaches the DOM; "Sign in for this root" / "Sign out of this root" |
| Consent/revocation states | `loggedInNotGranted` (`notGranted`), `grantedNetworkOff` (`granted`, generation shown), `accountTransitionStale` / `policyRotatedStale` (`stale` with `data-consent-mismatch` naming the changed field; "It is not reused. Grant consent again for this root"), `revoked` ("Root generation 1 was retired and its private home invalidated … Nothing from it is reused … start root generation 2") | `p[data-consent]` ∈ {`notGranted`,`granted`,`stale`,`revoked`}; "Grant consent for this root" disabled while signed out (hint "Sign in for this root before granting consent."); "Revoke consent for this root" offered for `granted` and `stale` only |
| Three command-network postures | `grantedNetworkOff` (**off, default**), `askPerDestinationPending`, `askPerDestinationSessionAccepted`, `networkOn` | `fieldset[data-section="network"][data-network-posture]`; radios "No command network (default)", "Ask per destination", "Command network on (`network_access = true`)"; the fieldset is **disabled until consent is `granted`** (hint "Grant consent for this root before choosing a command-network posture. Until then commands have no network."); `on` renders `p[data-network-on-label]` "Command network is on for this root: commands run with `network_access = true`. This label is shown wherever a session from this root runs." |
| Ask-per-destination prompt: host/protocol + queued-request caveat; `acceptForSession` only as an explicit user act | `askPerDestinationPending` | `div[data-prompt-id][data-prompt-host="api.example.test"][data-prompt-protocol="https"]`: "npm install wants to reach **api.example.test** over **https** (port 443)."; `p[data-queued-caveat="2"]`: "2 requests to this destination are already queued; allowing it may let those requests proceed too."; buttons `data-prompt-decision` = `allowOnce` / `acceptForSession` / `deny`. The fake's act log proves `resolveNetworkPrompt:acceptForSession` occurs only when that button is pressed; mounting, port-driven updates, selecting the posture, and the prompt's existence add nothing to `sessionAcceptedDestinations`. |
| Rate-limit / approval status | `rateLimitedApprovalsPending` (and `ok`/none on the others) | `p[data-rate-limit]` "Rate limited until 2026-09-03T10:45:00.000Z — Provider rate limit reached for this account" / "Rate limit: OK"; `p[data-approvals-pending="2"]` "Approvals: 2 pending requests — last denied (shell) at …" / "Approvals: none pending" |
| `Opt-in Preview` label (G0 A8) | every fixture and the not-connected state | `section[data-product-posture="Opt-in Preview"]` and `span.consent-badge[data-posture-label]` with the verbatim text |
| Role entry with `role not mechanically enforced` (K-ROLE-2) | `roleAgent2NotMechanicallyEnforced` (label + note), `roleAgent2MechanicallyProven` (no label), every other fixture (label present on the Agent 2 choice while `enforcement` ≠ `mechanicallyProven`) | `fieldset[data-section="role"][data-role][data-role-enforcement]`; four radios (Untyped session / Agent 0 / Agent 1 / Agent 2 / TASK); `label[data-role-choice="agent2"][data-role-label="role not mechanically enforced"]` with the badge; `p[data-role-hint="not-mechanically-enforced"]` naming G-ROLE and marking evidence `instruction-asserted`; "Native descendants acquire no role by descent." |

Not-connected state (no port): the two explanations, the `Opt-in Preview` badge, and
"Account and consent controls are not connected in this build." — no button, no input,
no account claim. The panel is **not mounted** in the product shell in this tranche
(design decision, run record `RETURN.md` §1); the fake is never wired into product code.

## 2. Exact input/source identities and cited-byte inventory

`FIXTURE_INVENTORY.sha256` (sorted, `LC_ALL=C`, paths relative to `projects/chirality-app-dev/`) lists
the SHA-256 of every fixture, evaluator, and adapted-source byte this claim depends on: the vocabulary
module, the fixture module, the fake adapter, the panel, the appended styles, the three test files,
and `docs/CONTRACT.md` (the K-CONSENT-1 / K-NET-1 / K-KEY-1 / K-ROLE-2 text the shapes were taken from;
authority corpus v20, D-APP-38 status `no drift` at Step 0). Recompute with
`cd projects/chirality-app-dev && LC_ALL=C shasum -a 256 -c Evidence/…/FIXTURE_INVENTORY.sha256`
(from the deliverable folder: `shasum -a 256 -c` against the repository paths).

Fixture module: `frontend/src/lib/consent/consent-ux-fixtures.ts` — thirteen named snapshots
(`loggedOutDefault`, `loggedInNotGranted`, `grantedNetworkOff`, `askPerDestinationPending`,
`askPerDestinationSessionAccepted`, `networkOn`, `accountTransitionStale`, `policyRotatedStale`,
`revoked`, `nullEmailEpoch`, `rateLimitedApprovalsPending`, `roleAgent2NotMechanicallyEnforced`,
`roleAgent2MechanicallyProven`). Hosts use the reserved `.test` TLD (RFC 2606); identities are
digests (`sha256:acct-…`) or a volatile epoch; the private home is an app user-data path; no email,
token, cookie, device code, or `~/.codex` path appears (asserted by tests over `JSON.stringify` of
every fixture and of every rendered tree).

## 3. Commands, cwd, effective environment, versions, exit status

`ENVIRONMENT.json` records the platform and toolchain (node v24.18.0, npm 11.16.0, Vitest 4.1.10,
Next 15.5.21, TypeScript 5.9.3, react-test-renderer 18.3.1, Electron 43.2.0). The complete
check table with commands, cwd, exit codes, and summaries is the run record `CHECKS.json`.

Focused evidence command (cwd `projects/chirality-app-dev/frontend`, exit 0):

```
npx vitest run src/__tests__/lib/consent/fake-hosted-engine-consent-port.test.ts \
  src/__tests__/components/account-consent-settings-states.test.ts \
  src/__tests__/components/account-consent-settings.test.ts \
  --reporter=verbose --reporter=json --outputFile.json=<this folder>/focused_vitest_results.json
```

## 4. Results (machine-readable and canonical stdout)

- `focused_vitest_results.json` — Vitest JSON reporter: 3 files, 14 suites, **65 passed, 0 failed**,
  `success: true` (fake port 35; panel states/interactions 24, react-test-renderer per D-APP-36;
  static markup 6).
- `focused_vitest_stdout.txt` — the verbose reporter's stdout/stderr for the same run.
- Both files had the session's scratch-worktree absolute path replaced by `{REPO_ROOT}` (the App
  AGENTS.md path-anchor convention; same normalization as DEL-05-01's node D packet). Raw bytes
  before normalization: stdout SHA-256 `792362b58bb9dcb3425a32f72375b20b3d6ab13d3bf544c64451143176e35f14`,
  JSON `9a2e515d6feec0269dbae59c01e53490970281af6958f91f3ee05bf667a6a866`; retained (normalized)
  bytes are the ones listed in `MANIFEST.sha256`. No other byte was changed.

Registered gates at the same freeze (run record `CHECKS.json`): typecheck pass; full Vitest
165 files passed / 1 skipped, 1554 tests passed / 4 skipped; `npm run build` pass; premerge
(`npm run harness:validate:premerge` behind a stub Next dev server, and `npm run validate:release-quality`)
**fail in the absent-runtime-daemon-bindings class** — 8/8 results HTTP 503 from the session routes
with no runtime daemon bound in the sandbox, the class recorded at Receipts 172/177 and by node A —
deferred to PR CI with no pass inferred; `git diff --check`, change-scope validation, harness
self-check, harness pytest (350), APP-HOLD dispatch preflight and register-match scan, corpus status,
receipts validator all pass.

## 5. Process, filesystem, containment, and denied-egress observations

The fixtures, the fake adapter, and the tests perform no I/O: no process is spawned, no file is read
or written, no socket is opened, no keychain or `safeStorage` call is made, and no ambient `~/.codex`
path is consulted (the vocabulary type admits only `ambientCodexRead: false`; tests assert no `.codex`
path and no `.com/.net/.org/.io/.ai` host in any fixture). No new network destination is introduced
(F-APP-1); the only host names are `api.example.test` (fixtures) and `mutated.test` (a test mutation
probe), both under RFC 2606's reserved `.test` TLD. The premerge stub server observed only loopback
`127.0.0.1:51447` traffic from the validator, answered HTTP 503 by the session routes (no daemon), and
was stopped with SIGTERM.

## 6. Sorted manifest and independent hash recomputation

`MANIFEST.sha256` lists every file in this folder except itself (sorted, `LC_ALL=C`). Verify with
`cd <this folder> && shasum -a 256 -c MANIFEST.sha256`. Verify the cited sources with
`cd projects/chirality-app-dev && shasum -a 256 -c <this folder>/FIXTURE_INVENTORY.sha256`.

## 7. Cleanup proof for disposable state

The fixtures and tests create no disposable state. The only disposable state of the check run was the
premerge stub Next dev server (started `node node_modules/next/dist/bin/next dev --port 51447` with
`CHIRALITY_HARNESS_PROVIDER=stub NEXT_TELEMETRY_DISABLED=1`, pid 52705): stopped with SIGTERM and
`wait` returned ("server stopped" in the run log); its `.next` build output and the validator's
`/var/folders/…/chirality-harness-validation/` workroot are gitignored/outside the repository, as at
node A. `git status --porcelain` after the checks lists only the tranche's own paths (change-scope
validator: PASS, 0 violations).

## 8. Bounded rerun method

From a checkout containing this tranche's commit (any platform with Node 24 / npm 11):

1. `cd runtime && npm ci && npm run build` (the `file:`-linked runtime packages), then
   `cd projects/chirality-app-dev/frontend && npm ci`.
2. `npm run typecheck`.
3. The focused command in §3 (writing the JSON to a scratch path); compare its `numPassedTests` (65),
   `numFailedTests` (0), and `success` (true) with `focused_vitest_results.json`.
4. `npm test` for the full suite; `npm run build`.
5. Recompute `FIXTURE_INVENTORY.sha256` and `MANIFEST.sha256` as in §6.

Deterministic: the fake's clock is a fixed counter, the fixtures are constants, and the tests use no
timers, randomness, network, or filesystem.
