---
run-id: TASK_RUN_DEL-02-05_2026-09-03_NODE_F
timestamp: 2026-09-03
run-status: SUCCESS (frozen for independent review; closure recorded at closeout)
control-surface: FILE
scope-path: projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback
task-profile: NONE
task-skill: software-bounded-implementation
resolved-skill-path: skills/software-bounded-implementation
resolved-skill-version: "1"
parent-run: execution/_Coordination/AgentRuns/APPDEV_V3_NODE_F_2026-09-03
executor: Claude Fable 5.1 (claude-fable-5-1), ephemeral Agent 2 under HELP_HUMAN
item: DEL-02-05-V3-02
basis: e59efa4830fb54143c86e511ec35a6d1a476f72e
---

## Requested Tasks

- Static WP-07 account/consent UX fixtures behind a fake `HostedEngineConsentPort`
  shaped by K-CONSENT-1 / K-NET-1: per-root login explanation, root-private app-owned
  `CODEX_HOME` copy, login/logout/account and consent/revocation states, the three
  command-network postures (default off; ask per destination with host/protocol and the
  queued-request caveat, `acceptForSession` only as an explicit user act; on with
  `network_access = true` labelled), rate-limit/approval status, the `Opt-in Preview`
  label, and role entry with the `role not mechanically enforced` label.
- D-APP-36 render tests (react-test-renderer) plus static-markup copy pins; durable
  evidence per the workplan Evidence contract.

## Outputs Produced

- `frontend/src/lib/consent/hosted-engine-consent-port.ts` — UI-facing vocabulary and the
  `HostedEngineConsentPort` shape (postures, decisions, identities, private home, roles,
  scope + `compareConsentScopes`, consent states, rate-limit/approvals, snapshot, port).
- `frontend/src/lib/consent/consent-ux-fixtures.ts` — thirteen static snapshots.
- `frontend/src/lib/consent/fake-hosted-engine-consent-port.ts` — in-memory fake adapter
  with test-only controls (`enqueueNetworkPrompt`, `rotatePolicy`, `setConfigDigest`,
  `setRateLimit`, `setApprovals`, `setRoleEnforcement`, `setNextLoginIdentity`,
  `failNextAct`, `admit`, `actLog`).
- `frontend/src/components/settings/account-consent-settings.tsx` — container +
  pure `AccountConsentSettingsView` (settings-panel pattern of `api-key-settings.tsx`).
- `frontend/src/app/globals.css` — appended `.consent-*` block only.
- Tests: `src/__tests__/lib/consent/fake-hosted-engine-consent-port.test.ts` (35),
  `src/__tests__/components/account-consent-settings-states.test.ts` (24, react-test-renderer),
  `src/__tests__/components/account-consent-settings.test.ts` (6, static markup).
- Evidence: `Evidence/V3-02_consent_ux_fixtures_2026-09-03/` (`EVIDENCE.md`,
  `FIXTURE_INVENTORY.sha256`, `ENVIRONMENT.json`, `focused_vitest_stdout.txt`,
  `focused_vitest_results.json`, `MANIFEST.sha256`).

## Design decisions (recorded; inside the fence; D-APP-60/64 per-instance latitude)

- **Not mounted in the product shell.** The panel accepts an injected port and is
  rendered only by tests with the fake. Rejected: mounting it in `shell-frame.tsx` behind
  the fake — that would show fabricated account state to a real operator (a live-account
  claim the item forbids) and is exactly what the live DEL-02-05-V3-03 wiring would have
  to undo. Rejected: mounting it with `port = null` — honest, but it adds Codex
  sign-in copy to the shipped shell before the adapter exists; left to V3-03 together with
  the live port.
- **Fake and fixtures beside the vocabulary under `src/lib/consent/`**, named `fake-…` and
  `…-fixtures`, so one import root carries the contract shape, the fixtures the evidence
  cites, and the double the tests drive; nothing under `src/components/shell/**` imports
  them, so the Next bundle excludes them. Rejected: `src/__tests__/fixtures/consent/` —
  the item's Return contract names the fixture bytes as deliverable outputs, not test
  support.
- **Stale is sticky.** Once a granted consent's scope stops matching (account, policy,
  role, config, generation, root, project, adapter) it is `stale` and only a fresh explicit
  `grantConsent()` returns it to `granted`, even if the original account signs back in.
  Rejected: auto-reviving on scope re-match — a reuse across an account change.
- **Posture selection requires `granted` consent** (K-NET-1 "under explicit consent");
  revocation drops the posture to `off` and clears session acceptances; leaving
  ask-per-destination drops a pending prompt unanswered (fail closed), never as a grant.
- **Role change after a grant makes the consent stale** (K-CONSENT-1 validates the selected
  role posture; K-ROLE-2 lets the posture participate in worker identity).
- **Identity display is a digest suffix or the epoch**, never the full digest or an email.

## Checks

See parent `CHECKS.json`: typecheck, full Vitest (165 files / 1554 tests, 4 skipped),
focused 65, build pass; premerge fail in the absent-runtime-daemon-bindings class (8/8
HTTP 503; deferred to PR CI, Receipts 172/177 precedent); diff --check, change-scope,
harness self-check, pytest 350, APP-HOLD, corpus, receipts validator pass.

## A1 re-stage declaration

Recorded in the parent run's `STEP0_DISCOVERY.md` §3 and applies to this item.
