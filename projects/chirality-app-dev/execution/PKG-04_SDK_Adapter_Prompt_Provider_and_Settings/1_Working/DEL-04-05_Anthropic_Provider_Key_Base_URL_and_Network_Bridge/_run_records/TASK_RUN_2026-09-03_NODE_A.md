---
run-id: TASK_RUN_DEL-04-05_2026-09-03_NODE_A
timestamp: 2026-09-03
run-status: SUCCESS (frozen for independent review; closure recorded at closeout)
control-surface: FILE
scope-path: projects/chirality-app-dev/execution/PKG-04_SDK_Adapter_Prompt_Provider_and_Settings/1_Working/DEL-04-05_Anthropic_Provider_Key_Base_URL_and_Network_Bridge
task-profile: NONE
task-skill: software-bounded-implementation
resolved-skill-path: skills/software-bounded-implementation
resolved-skill-version: "1"
parent-run: execution/_Coordination/AgentRuns/APPDEV_V3_NODE_A_2026-09-03
executor: Claude Fable 5.1 (claude-fable-5-1), ephemeral Agent 2 under HELP_HUMAN
item: DEL-04-05-V3-01
basis: 0c683fb1657706316272951e4c3a0f7781b46009
---

## Requested Tasks

- Extend `api-key-storage.ts` and the bridge types so status distinguishes exactly
  `missing`, `storageUnavailable`, `decryptFailed`, `available` beside the preserved
  `ui | env | none` source.
- Never expose plaintext, never silently delete/overwrite a ciphertext on decrypt
  failure, never fall back to a plaintext or alternate store; daemon stays the owner.
- Corrupt-ciphertext and unavailable-store fixtures with byte-identical proof.

## Outputs Produced

- `frontend/src/lib/credential-storage-state.ts` (shared vocabulary + guard);
  `frontend/electron/api-key-storage.ts` (`readProviderCredential`,
  `probeProviderCredentialStorage`, `ProviderCredentialStatus.storage`);
  `frontend/electron/api-key-ipc.ts` (validated projection, `ApiKeyStatusResult.storage`).
- Tests: `api-key-storage.test.ts` (29, incl. the non-destructive fixture block),
  `api-key-ipc.test.ts` typed-state block; contract pins on the non-destructive read path.
- Evidence: `Evidence_TYPED_STORAGE_STATES_2026-09-03.md`.

## Design decisions (recorded; D-APP-60 disposition-class, inside the fence)

- Source precedence unchanged: a `decryptFailed` or `storageUnavailable` blob does not
  block the accepted environment fallback; the state travels beside the source so the
  UI can show both. Rejected alternative: making a bad blob suppress env — it would
  regress the 2026-08-20 accepted precedence and lock an operator out.
- Empty decrypted plaintext classifies as `missing` (nothing usable stored; decrypt did
  not fail). Rejected: `decryptFailed`, which would misdescribe a successful decrypt.
- Pre-typed-state daemon answers map to `ui → available`, else `missing`, with a
  comment; rejected: failing closed, which would break a dev GUI against an older
  packaged daemon for no security gain (the mapping is exactly the old daemon's own
  distinguishing power).

## Checks

See parent `CHECKS.json`: typecheck, full Vitest, focused 151, build, desktop:pack,
packaged security proof, diff --check, self-check, pytest, APP-HOLD, scope validation
pass; premerge deferred (absent runtime-daemon bindings class).

## A1 re-stage declaration

Recorded in the parent run's `STEP0_DISCOVERY.md` §3 and applies to this item.
