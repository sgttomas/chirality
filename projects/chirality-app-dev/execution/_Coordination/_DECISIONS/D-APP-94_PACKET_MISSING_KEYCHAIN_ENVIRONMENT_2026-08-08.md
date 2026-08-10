# D-APP-94 — Missing-keychain environment decision packet, corrected surface

Status: `PROPOSAL — AWAITING_RULING — NO OPTION SELECTED`

Decision question: which environment posture, if any, should be prepared for a
future D-APP-93 owner-operated attempt after the sealed `HOME` caused macOS to
present a Keychain Not Found modal before fresh C1118?

This correction records the owner's recommendation to test
`--password-store=basic` on C1117, and possibly C1114, but does not adopt it.
The flag candidate fails the available macOS platform evidence and must not be
placed in an attempt-3 execution token without new primary or bounded runtime
evidence that overturns the findings below.

## Primary platform evidence

Electron v43.2.0's own `safeStorage` contract states that macOS storage uses
Keychain and that `isEncryptionAvailable()` returns true on macOS only when
Keychain is available. Its `setUsePlainTextEncryption()` and
`getSelectedStorageBackend()` controls, including the `basic_text` backend and
the `--password-store=basic` selection route, are Linux-only. Source:
<https://github.com/electron/electron/blob/v43.2.0/docs/api/safe-storage.md>.

Chromium's primary test-launcher contract excludes Windows, macOS, and ChromeOS
from consulting `kPasswordStore`; only the Linux branch appends
`--password-store=basic`. Source:
<https://chromium.googlesource.com/chromium/src/+/refs/heads/main/chrome/test/base/test_launcher_utils.cc>.

Electron's official v43.2.0 release metadata binds that Electron release to
Chromium `150.0.7871.129`. Source:
<https://releases.electronjs.org/release/v43.2.0>. The local package and lock
bytes independently pin Electron `43.2.0`; the successful attempt-2 package
evidence also records Electron `43.2.0` for both macOS arm64 bundles.

Decision-surface conclusions from those primary contracts:

1. macOS Electron v43.2.0 does not support `--password-store=basic` as a
   `safeStorage` backend selection or Keychain-modal suppression mechanism.
2. The flag cannot make `safeStorage.isEncryptionAvailable()` true when the
   sealed macOS environment lacks an available Keychain.
3. Adding the flag to C1117 is therefore unsupported. Adding it to C1114 is
   also unsupported on macOS, even though C1114 is the actual safeStorage
   consumer identified below.
4. Electron's `setUsePlainTextEncryption()` is not a macOS escape hatch.

These are static platform-contract findings, not a runtime claim that every
future macOS/Electron build behaves identically. They are sufficient to block
an execution token premised on the flag working.

## Exact local consumer path

C1114 launches the packaged `Chirality Runtime Service` Electron executable
with `--runtime-daemon`. In `electron/main.ts`, that mode calls
`initializeDaemon()`, which calls `startRuntimeHost()`. In
`electron/runtime-host.ts`, `startRuntimeHost()` constructs
`SafeStorageCredentialStore`; its `get()` and `status()` paths call
`retrieveProviderApiKey()`, which calls Electron
`safeStorage.isEncryptionAvailable()` and, when applicable,
`safeStorage.decryptString()`.

C1117 launches the GUI Electron process. Its main process registers API-key
IPC handlers backed by the runtime client, not a local
`SafeStorageCredentialStore`. The renderer's provider-status hydration invokes
those handlers; the handlers call the daemon's `credentialStatus`; the daemon
then invokes the C1114-owned `SafeStorageCredentialStore`. Therefore:

- C1114 is the actual Keychain/safeStorage consumer;
- C1117 can trigger the remote credential-status request that reaches C1114;
- the modal label implicating `Chirality Runtime Service` is consistent with
  this code path, but the label alone is not the proof;
- adding a flag only to C1117 could not configure the C1114 Electron process,
  even on a platform where that flag were meaningful.

The exact local source surfaces supporting this mapping are
`frontend/electron/main.ts`, `runtime-host.ts`, `api-key-storage.ts`,
`api-key-ipc.ts`, `preload.ts`, and
`src/components/settings/api-key-settings.tsx`. This packet reads those bytes;
it does not authorize changing them.

## Attempt-2 evidence and future C1118

The immutable attempt-2 GUI streams contain the historical
`Unknown project: chirality-app-dev` contact signature. C1118 was not entered.
That automatic record is supporting evidence only and cannot satisfy a future
attempt's fresh, per-attempt C1118 gate or earn D-APP-88 causal credit.

The accepted attempt-2 intake remains `STOP_INCOMPLETE`. Its step-14/step-15
deviations and the separately frozen cleanup addendum remain historical and are
not repaired by any D-APP-94 selection.

## Options

| Option | Decision posture | Authority and exposure | Validation consequence |
|---|---|---|---|
| **A — add `--password-store=basic` to C1117 and/or C1114** | **Unsupported / do not select for attempt 3.** This records the owner's proposed mechanism without claiming it works. | A launch-byte change would require a fresh packet, but the primary platform contract says the flag is Linux-only and cannot supply a macOS Keychain. | Cannot truthfully pass modal-suppression or `isEncryptionAvailable()` gates. No execution token may be issued on this premise. |
| **B — prepare an isolated sealed-HOME login-keychain plan** | Fidelity alternative; recommended only for preparation if the owner accepts the added security surface. | Requires separately owner-gated `security` commands and explicit handling of securityd session state, login-keychain creation/unlock, default/search-list binding, access-control prompts, password lifecycle, redaction, teardown, and recovery. No credential is to be stored merely to make Keychain available. | A fresh verifier must prove exact commands, isolated paths, session/search-list behavior, no owner-keychain exposure, cleanup/failure retention, and fresh C1118. Preparation does not establish feasibility or authorize keychain action. |
| **C — prepare a narrow feasibility probe** | Lower-commitment alternative when B's securityd/search-list behavior is not yet established. | Separately owner-gated, diagnostic-only probe over an isolated temporary HOME/keychain; no product/package/trace attempt, no credential material, and no reuse as execution authority. | May observe only Keychain availability, prompt behavior, process ownership, and reversible cleanup. Its result returns to a new ruling before any attempt-3 packet. |
| **D — defer** | Fail-closed. | No new authority or exposure. | D-APP-94 stays unresolved and no attempt-3 environment token issues. |

## Explicitly rejected product-byte route

A candidate/product patch that disables, bypasses, mocks, or changes
`safeStorage`, credential status, or credential retrieval is not recommended
for this causal attempt. It would change the diagnostic subject, weaken
source-aligned replay fidelity, and require independent product/source scope,
tests, packaging, review, and reliance decisions. D-APP-94 grants none of
those. This rejection does not make Option B safe or approved; it only keeps
product bytes out of this environment decision.

## Recommendation and blockers

Recommendation: select **B for preparation only** if the owner accepts its
security-command and session-state exposure; otherwise select **C** or **D**.
Do not select A and do not request an attempt-3 execution token yet.

Current blockers to attempt 3 are:

- D-APP-94 has no owner ruling;
- the `--password-store=basic` confirmations are `FAIL`, `FAIL`, and
  `C1114_CONSUMER / C1117_TRIGGER`, not three PASS results;
- Option B has no exact keychain/security command packet or verifier;
- Option C has no separately authorized probe packet or result;
- every future attempt still needs fresh C1118 and a newly frozen execution
  packet appropriate to the ruled environment.

## Exact owner-return tokens

- Record rejection of the unsupported flag route:
  `REJECT D-APP-94 OPTION A — MACOS ELECTRON 43.2.0 DOES NOT SUPPORT --PASSWORD-STORE=BASIC AS A SAFESTORAGE/KEYCHAIN BYPASS — ISSUE NO ATTEMPT-3 EXECUTION TOKEN ON THAT PREMISE`
- Select isolated-keychain preparation:
  `APPROVE D-APP-94 OPTION B — PREPARE AN ISOLATED SEALED-HOME LOGIN-KEYCHAIN PLAN WITH EXACT OWNER-GATED SECURITYD SESSION, DEFAULT/SEARCH-LIST, CREATION, UNLOCK, REDACTION, FAILURE-RETENTION, CLEANUP, AND FRESH C1118 GATES — PREPARATION ONLY; NO KEYCHAIN, CREDENTIAL, EXECUTION, PRODUCT, OR GIT AUTHORITY`
- Select a feasibility-probe preparation:
  `APPROVE D-APP-94 OPTION C — PREPARE A NARROW OWNER-GATED ISOLATED-KEYCHAIN FEASIBILITY PROBE WITH NO CREDENTIAL MATERIAL, PRODUCT/PACKAGE/TRACE ATTEMPT, OR RELIANCE EFFECT — PREPARATION ONLY; NO KEYCHAIN OR EXECUTION AUTHORITY`
- Defer:
  `APPROVE D-APP-94 OPTION D — DEFER THE MISSING-KEYCHAIN ENVIRONMENT DECISION AND ISSUE NO ATTEMPT-3 EXECUTION TOKEN`

No token above is a ruling until the owner returns it and the App loop records
that act. This packet authorizes no runtime, GUI, keychain, credential, package,
product, execution, Git, Task Management, or foreign-loop action.
