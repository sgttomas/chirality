# D-APP-94 Option C — isolated-keychain feasibility-probe packet

Status: `FROZEN CANDIDATE — OWNER APPROVAL AND FRESH VERIFIER PASS REQUIRED`

Purpose: measure only whether a hash-bound bare Electron 43.2.0 process can use
macOS safeStorage in a temporary keychain boundary without exposing or changing
owner/provider credentials or launching Chirality product bytes.

This packet is wholly separate from D-APP-93 attempt 3, packaging, trace,
C1114/C1117, and C196/C197. It makes no product, causal, release, or reliance
claim.

## Exact accepted basis

- owner-attested input record:
  `OWNER_INPUT_CAPTURE_RECORD.md`;
- default and complete ordered search-list restoration operand:
  `/Users/ryan/Library/Keychains/login.keychain-db`;
- accepted host basis: macOS `26.6` build `25G72`, Darwin `25.6.0`, arm64;
- local public Electron archive:
  `/Users/ryan/Library/Caches/electron/9c4e224684594fb9a8cbda18d3e2b7bf0c3c023d1462402a4031f8b4cc25e621/electron-v43.2.0-darwin-arm64.zip`,
  byte count `122090802`, SHA-256
  `ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`;
- archive member `Electron.app/Contents/MacOS/Electron`, byte count `33968`,
  SHA-256
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`;
- probe source SHA-256
  `920de6ffe2554d6f19462b9791ef16200489b1f2c52ca49ea70500dea197a453`;
- owner driver SHA-256
  `35ceb467a30bd3736c15958b3f99203a385b5f2e8a153c80478d3663dbd481f0`.

The driver re-observes host/version, archive, executable, probe-source, default,
and search-list identities before any keychain mutation. Any mismatch stops
before mutation. It also requires the literal owner restoration target
`/Users/ryan/Library/Keychains/login.keychain-db` to exist before mutation.

## Fixed isolated namespace

- root: `/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809`;
- HOME: `/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/home`;
- userData: `/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/user`;
- keychain:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/home/Library/Keychains/dapp94-option-c.keychain-db`;
- extracted public Electron distribution:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/electron`;
- raw source evidence:
  `/private/tmp/chirality-dapp94-option-c-keychain-probe-20260809/evidence`;
- immutable return destination:
  `execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/returned`.

Both the fixed root and return destination must be absent at invocation.

## Exact owner-personal operation

From repository root, the owner may invoke only:

`/bin/zsh projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP94_OPTION_C_ISOLATED_KEYCHAIN_FEASIBILITY_PROBE_PREPARATION_2026-08-08/prepared/run-dapp94-option-c-probe.zsh`

The frozen driver visibly contains every security/process/file operation. Its
security mutations are limited to:

1. `security create-keychain -p ''` at the exact isolated path;
2. `security unlock-keychain -p ''` for that path;
3. `security list-keychains -d user -s <isolated-path>`;
4. `security default-keychain -d user -s <isolated-path>`;
5. exact restoration, first search list then default, to the sole literal owner
   path `/Users/ryan/Library/Keychains/login.keychain-db`;
6. `security delete-keychain <isolated-path>` only after restoration is
   independently re-observed, byte-compared, and all then-produced source
   evidence is copied and hashed.

The driver never enumerates keychain items. Before mutation it repeats default
and search-list observations under the isolated `HOME` and requires them to
match the owner-session input, mechanically recording that filesystem `HOME`
alone is not the isolation boundary. The operative temporary boundary is the
user security-domain default/search list.

## No-credential classification

Literal `-p ''` passes a zero-length public argument. It has no secret bytes or
entropy and is non-secret keychain mechanics, not an owner password, provider
credential, or user credential. No password prompt is requested or answered.

Electron may generate one disposable cryptographic safeStorage key item inside
the isolated keychain when encrypting the public constant
`DAPP94_OPTION_C_PUBLIC_CONSTANT_V1`. That item is generated cryptographic probe
state, not an owner/provider credential. Neither its bytes nor any Keychain item
is enumerated or exported. The fixed public plaintext is not credential
material, and only its SHA-256, ciphertext byte count, and round-trip boolean
are emitted.

## Prompt and GUI rule

The bare Electron probe sets macOS activation policy to `prohibited` and creates
no window. If any SecurityAgent, Keychain, credential, or other system prompt
appears, the owner approves nothing, enters nothing, and selects Cancel only.
After the Electron call returns, the owner records `SHOWN_CANCELLED`; the driver
then restores the owner default/search-list state and stops with all isolated
keychain/temp evidence retained. `NONE` is the only prompt observation that can
continue to successful cleanup.

If cancellation does not return control to the driver, the owner performs no
signal, retry, process inspection, or alternate action and reports the held
state for a separately governed recovery. No success or cleanup claim follows.

## Measurement and pass meaning

The probe records:

- exact Electron and Chromium version strings;
- platform;
- `safeStorage.isEncryptionAvailable()`;
- one encrypt/decrypt round trip of the public constant;
- ciphertext byte count and public-constant SHA-256;
- owner prompt observation.

Successful output must state Electron `43.2.0`, platform `darwin`, encryption
available `true`, round trip `true`, and prompt observation `NONE`. This is only
a narrow environment-feasibility observation. It does not prove Chirality,
C1114/C1117, D-APP-88, D-APP-92, D-APP-93, product, trace, release, or reliance
behavior.

## Restoration, failure retention, and cleanup

Every post-creation failure takes the exact restoration function before exit.
Restoration sets the one-element user-domain search list and default to
`/Users/ryan/Library/Keychains/login.keychain-db`, re-observes both, and requires
byte identity with the owner-attested inputs. Restoration failure exits `90`
and retains the isolated keychain, fixed root, and raw evidence.

Any failed or cancelled probe retains the isolated keychain and fixed-root
evidence after successful owner-state restoration. It performs no deletion.
The driver also binds the same idempotent restoration function to shell
`EXIT`, `INT`, `TERM`, and `HUP`: it runs only while `MUTATED=1`,
`RESTORED=0`, and no restoration is already active; it records the trigger,
restoration result, and fixed retained root and never deletes retained state.
Only the fully passing path copies all raw evidence to `returned/`, creates an
adjacent whole-file SHA-256 sidecar for every returned primary, deletes only the
isolated keychain, proves its absence, removes only the fixed temporary root,
proves root absence, and hashes the cleanup evidence.

No owner login keychain is opened, unlocked, deleted, item-enumerated, or used as
the probe default/search target. Its path and the default/search-list responses
are the only owner-keychain information captured.

## Exclusions

No environment or memory dump, Keychain item dump, credential, network,
Chirality source/binary/package, application GUI, C1114/C1117, C196/C197,
debugger, causal trace, product repair, acceptance, release, reliance, Git, Task
Management, foreign-loop, or other authority is included.
