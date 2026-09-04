# RETURN — F1_IMPLEMENTER (frozen for independent review)

- **Run:** `APPDEV_V3_NODE_F_2026-09-03` · **Executor:** Claude Fable 5.1 (`claude-fable-5-1`), ephemeral Agent 2 under HELP_HUMAN · **Skill method:** `software-bounded-implementation`
- **Basis:** `e59efa4830fb54143c86e511ec35a6d1a476f72e` (PR #686 merge; exactly the required basis) · **Branch:** `codex/app-v3-nodeF-consent-ux-fixtures-2026-09-03`
- **Commits:** round 1 content `1bda97f990f8c2c7a2b89122ec6e230690702a03`; this file lands in a record-only commit on top of it (SHA in the freeze message). Nothing pushed.
- **Diff stat (basis → `1bda97f99`):** 21 files changed, 3464 insertions(+), 0 deletions — product `frontend/src/lib/consent/{hosted-engine-consent-port.ts (355), consent-ux-fixtures.ts (237), fake-hosted-engine-consent-port.ts (353)}`, `frontend/src/components/settings/account-consent-settings.tsx (459)`, `frontend/src/app/globals.css (+110, appended block)`; tests `frontend/src/__tests__/lib/consent/fake-hosted-engine-consent-port.test.ts (500)`, `frontend/src/__tests__/components/account-consent-settings-states.test.ts (550)`, `frontend/src/__tests__/components/account-consent-settings.test.ts (117)`; DEL-02-05 `Evidence/V3-02_consent_ux_fixtures_2026-09-03/` (6 files) and `_run_records/TASK_RUN_2026-09-03_NODE_F.md`; this run record (7 files incl. the verbatim launch brief).
- **Item:** DEL-02-05-V3-02 (static WP-07 account/consent UX fixtures behind a fake consent port). DEL-02-05-V3-03 untouched.
- **Status:** `REVIEW_READY`. Every registered check passes except the premerge, which fails in the recorded absent-runtime-daemon-bindings class and is deferred to PR CI. No `_STATUS.md`, `MEMORY.md`, receipt, `HANDOFF_STATE.md`, or run-record `MANIFEST.sha256` written yet (those follow `REVIEW_PASS`).

## 1. Behavioural summary

**Vocabulary (`hosted-engine-consent-port.ts`).** The renderer-side shape of `HostedEngineConsentPort` taken from K-CONSENT-1 / K-NET-1 / K-KEY-1 / K-ROLE-2: `COMMAND_NETWORK_POSTURES = ['off','askPerDestination','on']` with `DEFAULT … = 'off'` and the verbatim `network_access = true` label; `NetworkDestinationPrompt` (host, protocol, port, `queuedRequestCount`, non-secret `requestedBy`) and the three decisions with `acceptForSession` documented as explicit-user-act-only; `AccountIdentity` = non-secret digest **or** volatile null-email epoch (never email/token); `PrivateHomeState` whose `ambientCodexRead` type admits only `false`; `ROLE_POSTURES` (untyped/agent0/agent1/agent2), `RoleEnforcement`, and the verbatim labels `role not mechanically enforced` / `instruction-asserted`; `ConsentScope` (canonical root, project, adapter, account, policy digest, role posture, config digest, worker generation) with `compareConsentScopes` and the four consent states (`notGranted`, `granted`, `stale` + mismatches, `revoked` + retired generation + `privateHomeInvalidated: true`); rate-limit/approval status; the snapshot; the port interface (snapshot/subscribe + seven explicit user acts). `PRODUCT_POSTURE_LABEL = 'Opt-in Preview'`.

**Fixtures (`consent-ux-fixtures.ts`).** Thirteen static, secret-free snapshots covering all four consent states, all three postures (pending prompt and session-accepted variants), account A / B transition, policy rotation, revocation (generation 1 → 2, home invalidated), null-email epoch, rate-limited + approvals pending, Agent 2 with and without G-ROLE proof. Hosts use the reserved `.test` TLD; `consentUxFixture()` deep-copies.

**Fake adapter (`fake-hosted-engine-consent-port.ts`).** In-memory, deterministic, no I/O. Login creates the root-private home (`present`) and never touches ambient state; grant binds to the current scope; **staleness is sticky** (any validated field change → `stale`; only a fresh explicit grant returns to `granted`, even when account A signs back in); revocation retires the generation, starts the next, invalidates the private home, drops the posture to `off`, and clears session acceptances; posture selection requires `granted` consent; leaving ask-per-destination drops a pending prompt unanswered; `acceptForSession` happens only through `resolveNetworkPrompt(id, 'acceptForSession')`; role change after a grant stales the consent; `control.admit()` denies `notGranted`/`stale`/`revoked` and any field mismatch while ignoring a caller-supplied `cwd`; a failed act changes nothing and notifies nobody; `actLog` records every act for explicit-act-only assertions.

**Panel (`account-consent-settings.tsx`).** Container (`AccountConsentSettings`, injected `port`, subscribes, runs acts with a busy flag and an error line) + pure `AccountConsentSettingsView` following the `api-key-settings.tsx` pattern with `data-*` markers: `Opt-in Preview` badge; per-root login and `CODEX_HOME` explanations (always present, including the not-connected state); account section (digest **suffix** or epoch, sign-in/sign-out); consent section (four states, stale mismatch reasons, revoked generation copy, grant disabled while signed out, revoke for granted/stale); network fieldset **disabled until consent is granted**, three radios, the `network_access = true` label under `on`, the ask-per-destination prompt with host/protocol/port, the queued-request caveat, and the three decision buttons, plus the session-accepted list; rate-limit/approval lines; role fieldset with the `role not mechanically enforced` badge on Agent 2 / TASK whenever enforcement is not mechanically proven, the `instruction-asserted` note, and the no-role-by-descent line. **Not mounted in the product shell** — the panel is rendered only by tests with the fake; nothing for the live DEL-02-05-V3-03 wiring to undo (design decision with rejected alternatives in `TASK_RUN_2026-09-03_NODE_F.md`).

## 2. Files (basis → HEAD)

Product: `frontend/src/lib/consent/{hosted-engine-consent-port.ts, consent-ux-fixtures.ts, fake-hosted-engine-consent-port.ts}` (new), `frontend/src/components/settings/account-consent-settings.tsx` (new), `frontend/src/app/globals.css` (appended `.consent-*` block). Not changed: `frontend/electron/**`, `frontend/src/components/shell/**`, `package.json`/lockfiles, `runtime/**`, `docs/**`.
Tests: `frontend/src/__tests__/lib/consent/fake-hosted-engine-consent-port.test.ts`, `frontend/src/__tests__/components/{account-consent-settings-states.test.ts, account-consent-settings.test.ts}` (all new).
Evidence/state: DEL-02-05 `Evidence/V3-02_consent_ux_fixtures_2026-09-03/{EVIDENCE.md, FIXTURE_INVENTORY.sha256, ENVIRONMENT.json, focused_vitest_stdout.txt, focused_vitest_results.json, MANIFEST.sha256}` and `_run_records/TASK_RUN_2026-09-03_NODE_F.md`; this run record (`ORCHESTRATION_PLAN.md`, `WORK_GRAPH.json`, `STEP0_DISCOVERY.md`, `CHECKS.json`, `COORDINATOR_DECISIONS.md`, `RETURN.md`, `instances/F1_IMPLEMENTER/LAUNCH_BRIEF.md`).

## 3. Check evidence (full table with commands, cwd, exit codes: `CHECKS.json`)

| Check | Round 1 |
|---|---|
| `npm run typecheck` | pass |
| `npm test` (full Vitest) | pass — 165 files / 1554 tests (1 file, 4 tests skipped, pre-existing) |
| focused Vitest (3 files) | pass — 65 (fake port 35; states/interactions 24, react-test-renderer D-APP-36; static markup 6); stdout + JSON retained in the evidence bundle |
| `npm run build` | pass |
| premerge (`harness:validate:premerge` behind a stub dev server; `validate:release-quality`) | **FAIL — absent runtime-daemon bindings** (8/8 HTTP 503 from the session routes; Receipts 172/177 and node A precedent); `FAIL_DEFERRED_TO_PR_CI`; no pass inferred |
| `git diff --check` | pass (working tree and full basis→HEAD range) |
| harness `self-check` / pytest | pass / 350 |
| APP-HOLD dispatch preflight / register-match scan | ALLOW / PASS (held_count 0, register match true) |
| corpus status / receipts validator / pinned reference SHA | no drift (v20) / VALID / matches |
| `validate_change_scope.py` (exact command in `CHECKS.json`) | PASS, 0 violations — over the working tree at the freeze and with `--head 1bda97f99` (21 paths) |

## 4. Write-scope validation

Every changed path is inside the seated item's locus: `frontend/src/**` (the new `lib/consent/` root, the new settings component, the appended `globals.css` block, tests under `__tests__/**`), DEL-02-05 `Evidence/**` and `_run_records/**` (no `_STATUS.md` / `MEMORY.md` yet), and this AgentRuns record. `validate_change_scope.py` → `PASS`, `violations: []` at `--head 1bda97f99`. Not touched: `runtime/**`, `docs/**`, `frontend/electron/**`, `frontend/src/components/shell/**`, `package.json`/lockfiles, the decision register, prior receipts, any Root surface.

## 5. Fences and claims

- **F-APP-1:** no provider/network expansion; no new network destination (fixture hosts are RFC 2606 `.test`; the fake performs no I/O). The three postures are vocabulary and UI only.
- **F-APP-2/F-APP-4/F-APP-5:** no release, signing, notarization, distribution, lifecycle, or new standing surface. `_STATUS.md` untouched until closeout.
- **No live-account claim** (G3/G-WIRE/G-CSP/G4 not claimed); the not-connected state says so; the panel is not mounted.
- **K-KEY-1:** no secret persistence, no ambient `~/.codex` read (type-level `ambientCodexRead: false`; tests assert no `.codex` path and no email/token in fixtures or DOM).
- **A1 re-stage rule** applies (declaration in `STEP0_DISCOVERY.md` §3): `frontend/` is mutated, so the staged R20 procedure is invalidated for any future proof claim.
- Stale-map deltas (live tree wins; `STEP0_DISCOVERY.md` §6): the `Opt-in Preview` label's ruling source is the G0 record A8, not A11; the registered premerge command is `harness:validate:premerge` (both it and `validate:release-quality` were run).

## 6. Residual risks and follow-ups (reported, not taken silently)

1. **Mounting.** The panel is not in the shell; DEL-02-05-V3-03 mounts it beside `RuntimeSettings`/`ApiKeySettings` with the live port. If the owner prefers the explanatory copy and `Opt-in Preview` badge visible now (port `null` → not-connected state), that is a one-line change in `shell-frame.tsx` plus a mock line in `shell-frame.test.tsx`; not taken because it is a product-copy decision outside this fixture item.
2. **Port shape is App-authored.** The vocabulary is shaped from the K-CONSENT-1/K-NET-1 text; the Root-owned contract (Root DEL-02-09) may name fields differently. V3-03 adapts the live port to this shape or amends the shape; the fixtures and tests are the App-side expectation, not the accepted contract.
3. **Premerge** is PR-CI-owed (recorded class).
4. **Time display** in the panel is the raw ISO string from the snapshot (`resetsAt`, `revokedAt`, `lastDecision.at`); locale formatting is left to the live wiring.
5. Concurrent nodes G/H/I: no shared write path except the append-only receipts ledger at closeout (Parent-Receipt Receipt-212; next unused ID at rebase time).

## 7. Coordination notices

None owed beyond this return: no `agents/**`, corpus, register, or Root surface changed.

## 8. Closeout after REVIEW_PASS (2026-09-03)

- **Review:** `instances/F2_REVIEWER/REVIEW_01_2026-09-03_over_f5b936e78.md` — **PASS**, 0 blocking / 0 major / 4 minor / 6 notes; filed verbatim (byte-identical to the coordinator's copy). No product, test, or CSS byte changed after the freeze (coordinator disposition D1).
- **Rebase:** onto `origin/main` `774b7ba00b474ba2e5e341cdddab848167d275f1` (PR #688 merge) with no conflict; reviewed commits are now `0ebeecd94` (content) and `64547069b` (record). Post-rebase typecheck pass; full Vitest 165 files / 1554 tests pass (4 skipped); corpus no drift; APP-HOLD preflight ALLOW / scan PASS; `git diff --check`, change-scope (`--base 774b7ba00`), receipts validator — results in `CHECKS.json` round "closeout".
- **Receipt:** 215 (Receipt-213 node I on `main`; Receipt-214 node G in PR #688; no node H receipt on `origin`); Parent-Receipt `Receipt-212`; Gate-Outcome `EXECUTED` (validator vocabulary).
- **Residuals from the review (recorded, not fixed here):**
  - **F1** (`hosted-engine-consent-port.ts:216`) — the `configDigest` doc comment says the digest "includes the command-network posture"; the fake does not fold the posture in and K-CONSENT-1 says only "effective configuration digest". Whether the posture participates is Root-owned (DEP-02-05-008). V3-03 rewords the comment to the accepted contract (recorded as a V3-03 Note in `_STATUS.md`).
  - **F2** (`fake…:257-276`) — once consent is `stale`, the previously selected posture and session acceptances are retained and `resolveNetworkPrompt(id,'acceptForSession')` still succeeds at the port level; the panel fails closed (network fieldset disabled unless `granted`). Port-level guard and the stale→posture policy: **DEL-02-05-V3-04** (fake-only). Whether the live port drops a stale consent's posture to `off`: V3-03 Note.
  - **F3** (`account-consent-settings.tsx:145` vs fake) — after `revokeConsent → grantConsent` the fake keeps `privateHome: invalidated` while the copy says "a fresh consent creates a new one", and the account stays `loggedIn`. Fake-side self-consistency (fresh grant → `present`): **DEL-02-05-V3-04**. Whether invalidation logs the account out (K-KEY-1): V3-03 Note, Root-owned.
  - **F4** (`fake…:288-291`) — `control.enqueueNetworkPrompt` seeds a prompt under any posture; the view masks it and `resolveNetworkPrompt` rejects it. Guard: **DEL-02-05-V3-04**.
  - **F5–F10** — no action. F8 noted for future evidence bundles: anchor inventory paths at the repo root (or add a `# verify from:` first line) so one cwd verifies every manifest; this bundle's `EVIDENCE.md` §2/§6 state the cwd for each file.
- **Deliverable state:** `_STATUS.md` — V3-02 removed from Remaining with a History line carrying the A1 re-stage echo; V3-03 gate, dependencies, locus, checks, and return unchanged with a Notes line added (F1–F4 as live-port questions, Root-owned parts named); V3-04 seeded `SELECTABLE`; lifecycle `IN_PROGRESS` and Checking Approval SHA untouched. `MEMORY.md` one line.
- **Push/PR:** not performed by this instance (D1). PR body at `<scratchpad>/PR_BODY_NODE_F.md`; HELP_HUMAN pushes and opens the PR.
