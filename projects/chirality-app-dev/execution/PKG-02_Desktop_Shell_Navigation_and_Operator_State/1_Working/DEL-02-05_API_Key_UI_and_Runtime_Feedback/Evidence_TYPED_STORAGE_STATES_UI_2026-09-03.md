# Evidence — DEL-02-05-V3-01: typed storage states in the API key and account settings panel (2026-09-03)

> Derivative evidence (App AGENTS.md derivative-package rule). Accepted upstream:
> `main` at `0c683fb1657706316272951e4c3a0f7781b46009` (PR #681 merge). Run record:
> `execution/_Coordination/AgentRuns/APPDEV_V3_NODE_A_2026-09-03/`. Executed by
> Claude Fable 5.1 (`claude-fable-5-1`) as ephemeral Agent 2 under HELP_HUMAN. No
> release, signing, lifecycle, live-account, or reliance claim; G-KEY not claimed.

## 1. Claim (REQ-002, REQ-005, AC-002, VER-002 typed-storage portion; CLM-028)

`frontend/src/components/settings/api-key-settings.tsx` renders the four typed
storage states from the bridge (`ApiKeyStatus.storage`, consumed via the unchanged
`preload.ts` channels) distinctly, with remediation copy where the operator can act,
and never places key material in the rendered tree:

| State | `data-storage` | Status label (source `none`) | Remediation copy (`p.api-key-warning[data-storage-state]`) | Controls |
|---|---|---|---|---|
| `missing` | `missing` | "No API key configured" | none | input, Reveal, Save Key |
| `storageUnavailable` | `storageUnavailable` | "Secure storage is unavailable" | "Secure storage is not available on this platform. Chirality cannot read or save a stored key until the operating system keychain is available, and any previously stored key is left in place unread. To continue now, set the `<ENV>` environment variable and restart Chirality." | none (entry hidden) |
| `decryptFailed` | `decryptFailed` | "Stored key cannot be read" | "The stored key could not be decrypted, so it cannot be used. The previous encrypted entry has been kept unchanged and nothing was deleted. Re-enter the key below to replace it, or remove the stored entry explicitly." + (when `source: env`) " Until then, Chirality is using the `<ENV>` environment variable." | input, Reveal, Save Key, Remove Stored Key |
| `available` | `available` | "Key configured (stored in secure storage)" | none | input, Reveal, Save Key, Remove Stored Key |

Source-first labelling is preserved: `source: ui` / `env` keep their existing labels,
so an environment credential in use beside a `decryptFailed` blob shows both facts.

**Non-answers are not storage states (round 3, review MAJOR-2).** The bridge also
returns answers that say nothing about the keychain — daemon unreachable
(`unavailable: true` + `error`), a denied sender, or an invalid daemon status (both
`error`) — all with `encryptionAvailable: false` and no `storage`. `ApiKeyStatus` now
carries `unavailable?` and `error?`; such an answer renders `data-storage="unknown"`,
`data-answer="unavailable"`, the neutral line "Cannot determine credential status right
now", the bridge's error text in a `p[data-status-error]`, **no** keychain remediation,
and entry hidden as before the typed states (the daemon is routinely not yet bound when
the window first asks). Only a legacy answer with neither field and
`encryptionAvailable: false` maps to `storageUnavailable`; a typed `storage` always wins.
Removal remains an explicit user act; nothing is deleted silently. The DEL-02-05 write
was confined to `frontend/src/**`; `frontend/electron/api-key-ipc.ts` was written only
under the DEL-04-05-V3-01 / DEL-09-06-V3-01 integration ownership of the same run.

## 2. Identities (SHA-256 at freeze)

| File | SHA-256 |
|---|---|
| `frontend/src/components/settings/api-key-settings.tsx` | `3c8ceae7bbfd880b2024ecc35c9a68da5121cf11261f31bca284719c91c56f4d` |
| `frontend/src/lib/credential-storage-state.ts` | `b9a9e171ae8de26845d1868fe03510e3f4b8737a177460538127ba7376441e43` |
| `frontend/src/__tests__/components/api-key-settings-storage-states.test.ts` (new, react-test-renderer) | `e081c0ed7aacd658468bed34a3df88d0e219cad9d2d70cf4f3447aaa39352b69` |
| `frontend/src/__tests__/components/api-key-settings.test.ts` (static markup) | `c687ed323c452ca6f959eeea411a478774f3ec73e931eba94dee3dcd11f43371` |

## 3. Render evidence (D-APP-36 render bar; react-test-renderer 18.3.1; Vitest 4.1.10)

`src/__tests__/components/api-key-settings-storage-states.test.ts` — 12 tests, header
cites D-APP-36 in the `chat-panel-empty-state.test.ts` style:

1. all four states render with four distinct `data-storage` markers and no fixture
   secret in `JSON.stringify(renderer.toJSON())`;
2. `missing`: no warning, no removal, entry offered;
3. `storageUnavailable`: one warning with the five remediation phrases, no input, no
   buttons;
4. `storageUnavailable` names the provider-specific variable (`CHIRALITY_OMLX_API_KEY`
   without `ANTHROPIC_API_KEY`);
5. `decryptFailed`: label, one warning with "could not be decrypted", "cannot be used",
   "kept unchanged", "nothing was deleted", "Re-enter the key", "remove the stored
   entry explicitly", no environment sentence; input plus Reveal/Save/Remove;
6. `decryptFailed` with `source: env`: env label, `data-source="env"`,
   `data-storage="decryptFailed"`, the environment sentence, Remove offered;
7. `available`: secure-storage label, no warning, Remove offered;
8. key material appears only as the masked `input` `value` (`type="password"`), exactly
   once in the tree;
9. legacy answers map conservatively (`encryptionAvailable:false` with neither
   `unavailable` nor `error` → `storageUnavailable`; typed-less known → `unknown`;
   `null` → "Checking..." with entry available);
10. unreachable daemon (`unavailable: true`, ENOENT operator-token error): `unknown`,
    `data-answer="unavailable"`, the neutral line, the error text, no warning, no
    "Secure storage is not available", no "keychain", no input, no buttons;
11. denied and invalid answers (`error` only) render the same neutral line;
12. a typed state wins over a stray `error` field.

`src/__tests__/components/api-key-settings.test.ts` — 13 tests (8 existing unchanged,
a 4-case static-markup matrix asserting `data-storage`, label, and warning presence per
state, and the unreachable-daemon static case); the existing secret-absence guard runs
on every render.

## 4. Commands, environment, rerun

cwd `projects/chirality-app-dev/frontend`; node v24.18.0. `npx vitest run
src/__tests__/components/api-key-settings.test.ts
src/__tests__/components/api-key-settings-storage-states.test.ts` → 25 passed, exit 0;
`npm run typecheck` exit 0; `npm test` 1431 passed / 4 skipped, exit 0; `npm run build`
exit 0. Full table: run record `CHECKS.json`. Rerun: same commands after `npm ci`
(frontend) and `npm ci && npm run build` (runtime). Targeted visual review of the copy
in a running app is not claimed here; the UI/claims gate wording review is the
independent reviewer's and the owner's.
