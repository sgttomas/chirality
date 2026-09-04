---
run-id: TASK_RUN_DEL-02-05_2026-09-03_NODE_A
timestamp: 2026-09-03
run-status: SUCCESS (frozen for independent review; closure recorded at closeout)
control-surface: FILE
scope-path: projects/chirality-app-dev/execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-05_API_Key_UI_and_Runtime_Feedback
task-profile: NONE
task-skill: software-bounded-implementation
resolved-skill-path: skills/software-bounded-implementation
resolved-skill-version: "1"
parent-run: execution/_Coordination/AgentRuns/APPDEV_V3_NODE_A_2026-09-03
executor: Claude Fable 5.1 (claude-fable-5-1), ephemeral Agent 2 under HELP_HUMAN
item: DEL-02-05-V3-01
basis: 0c683fb1657706316272951e4c3a0f7781b46009
---

## Requested Tasks

- Render `missing`, `storageUnavailable`, `decryptFailed`, `available` distinctly in
  `api-key-settings.tsx` with remediation copy and no key material in the DOM.
- react-test-renderer render tests for all four states (D-APP-36 render bar).

## Outputs Produced

- `frontend/src/components/settings/api-key-settings.tsx` (typed `storage` on
  `ApiKeyStatus`; `resolveStorageState`; state-specific labels, warnings, and controls;
  explicit removal offered for `decryptFailed`).
- Tests: `api-key-settings-storage-states.test.ts` (9, react-test-renderer),
  `api-key-settings.test.ts` (+4 static-markup cases).
- Evidence: `Evidence_TYPED_STORAGE_STATES_UI_2026-09-03.md`.

## Design decisions (recorded; inside the fence)

- Source-first labelling with the storage state as a second axis, so `env` +
  `decryptFailed` shows both. Rejected: storage-first labelling, which would hide that a
  working environment credential is in use.
- `storageUnavailable` hides entry (a save would fail) and tells the operator the
  stored key is left unread; `decryptFailed` keeps entry open and offers explicit
  removal. Rejected: auto-clearing an unreadable blob — silent loss.
- Product copy limited to the four states' remediation text; no other wording changed.

## Checks

See parent `CHECKS.json`: typecheck, full Vitest, focused 151, build pass; premerge
deferred (absent runtime-daemon bindings class); packaged proof pass.

## A1 re-stage declaration

Recorded in the parent run's `STEP0_DISCOVERY.md` §3 and applies to this item.

## Round 3 (independent review, MAJOR-2)

A bridge non-answer (daemon unreachable `unavailable: true`, denied sender, invalid
daemon status — all `encryptionAvailable: false` without `storage`) had been rendered as
`storageUnavailable` with the keychain remediation. `ApiKeyStatus` now carries
`unavailable?`/`error?`; such answers render `unknown` with a neutral line, the error
text, no keychain copy, and entry hidden as before; the legacy mapping applies only when
neither field is present. Three react-test-renderer cases and one static-markup case
added; the legacy-mapping test adjusted. Review: run record
`instances/A2_REVIEWER/REVIEW_01_2026-09-03_over_6ac51e99b.md`.
