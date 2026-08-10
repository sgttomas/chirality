# Option C feasibility-probe packet R8 — no explicit unlock

Status: `FROZEN CANDIDATE — EXECUTION TOKEN WITHHELD`

## Accepted evidence and disposition

`R7_UNLOCK_STOP_INTAKE.md` binds 49 raw evidence objects totaling 1,557
bytes. R7 create returned rc0 and produced a 20,460-byte
`login.keychain-db`; explicit empty-passphrase unlock returned rc51 with exact
bad-passphrase stderr; the raw named STOP is unlock-keychain; owner state
matched and no backstop write ran. Process exit 42 is owner-reported and
branch-consistent, not raw exit-status evidence. The R7 root and occupied empty
`returned_r7/` remain immutable. R8 uses only new, absent root
`/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809` and sibling
`returned_r8/`.

## Primary-platform calibration and decision

Apple's `SecKeychainCreate` documentation states that the API creates an empty
keychain and expressly describes automatic unlock only when creation posts
user interaction. That does not establish that this noninteractive
`security create-keychain -p ''` invocation leaves the keychain unlocked.
Apple's installed macOS SDK `Security.framework/Headers/SecKeychain.h`
describes direct `SecKeychainUnlock` as generally unnecessary because Keychain
Manager operations requiring unlock invoke it automatically, while recommending
status inspection when an application needs to verify unlock state. Apple
[TN3137, On Mac keychains](https://developer.apple.com/documentation/technotes/tn3137-on-mac-keychains)
is used only to calibrate keychain model/file-context claims, not to infer a
universal login-basename or unlock rule.

Therefore R8 omits the known-failing explicit unlock command entirely. It does
not demote or retry it and makes no create-leaves-unlocked claim. Unlock state
remains unknown until gated operations produce direct empirical evidence.

## R8 candidate

Driver `run-dapp94-option-c-probe-r8.zsh`, SHA-256
`d183572fadb5d67d8716858ae3b589acd60535433aea8239f0acf65b53738afd`,
is the R7 driver with only R8 namespace substitutions, matching evidence-name
substitutions, and exact removal of the explicit unlock command/status/gate.

After isolated-HOME create succeeds and the file exists, R8 requires exact
isolated-HOME default and search readbacks to equal the one-element R8
`Library/Keychains/login.keychain-db` path. This is a host/session hypothesis
under test, not established universal behavior. Only then may the bare,
hash-bound Electron 43.2.0 safeStorage probe run. Feasibility requires no
uncancelled prompt, `isEncryptionAvailable() === true`, and a disposable public
constant encrypt/decrypt roundtrip. Those are direct gates; no unlocked-state
assumption substitutes for them.

Owner pre/post drift observation, mismatch-only non-reentrant backstop, signal
continuity, failure retention, public-empty-password classification, prompt
Cancel-only rule, no fallback signal/retry/inspection, R6 feasibility-PASS
commit before isolated deletion, truthful cleanup COMPLETE/INCOMPLETE, and all
product/package/trace/C1114/C1117/C196/C197/network/GUI-window/credential/
reliance/Git/Task-Management/foreign-loop exclusions remain unchanged.

Primary references:

- Apple SDK header:
  `/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/System/Library/Frameworks/Security.framework/Headers/SecKeychain.h`,
  `SecKeychainCreate` and `SecKeychainUnlock` documentation;
- Apple [SecKeychainCreate documentation](https://developer.apple.com/documentation/security/seckeychaincreate);
- Apple [TN3137](https://developer.apple.com/documentation/technotes/tn3137-on-mac-keychains).

No preparation command executed the candidate, Security, or Electron.
