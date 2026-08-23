# Whole-file host-entanglement inventory

The sweep covered all 1,473 lines of `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`, its imported proof script and directly imported launchctl-not-found helper, and the complete R19 never-exited fixture. Findings are classified as `CHANGE`, `RETAIN`, `DELIBERATE_MISMATCH`, or `INERT_TEXT`.

| ID | Source sites | Finding | Classification | Accepted disposition |
| --- | --- | --- | --- | --- |
| UID-01 | test `:47-48,195-196` | Baseline console/security/account/process UIDs are hardcoded `501`; the account values become `expectedUid` for real metadata. | CHANGE | Add one file-level `const REAL_UID = process.getuid();`; use it for all coherent baseline identity values. |
| UID-02 | test `:60,94,140,147` | Loaded service, exact not-found stderr, top-level GUI route, and domain identifier embed `501` and are semantically checked against derived services/account UID. | CHANGE | Interpolate `REAL_UID` everywhere in this coherent fixture family. |
| UID-03 | test `:107,153` | Console and security UID output is state-driven; defaults are the hardcoded values in UID-01. | CHANGE | Changing the state defaults to `REAL_UID` fixes these outputs; retain state override points. |
| UID-04 | test `:251,322,331` | Assertions expect exact `launchctl print gui/501`. | CHANGE | Expect `gui/${REAL_UID}` so assertions continue to verify the exact command. |
| UID-05 | test `:374,377,380,598` | Username and absent-home cases use `uid: 501` although UID is not the intended failure in those rows. | CHANGE | Use `REAL_UID` to isolate the named username/home behavior. |
| UID-06 | test `:390` | Malformed two-record console text embeds `501`; ambiguity, not identity, is the intended failure. | CHANGE | Interpolate `REAL_UID` in both records so the fixture remains malformed for exactly one reason. |
| UID-07 | test `:369,402,424,435` | Account, console, domain-identifier, and security-context mismatch cases use `502`. | DELIBERATE_MISMATCH | Replace each mismatch with `REAL_UID + 1`; in the wrong-domain literal keep its security UID coherent at `REAL_UID`. |
| UID-08 | test `:447-515` | Unsafe-integer, duplicate-field, ambiguous-context, trailing-output, and unclosed-brace fixtures embed baseline `gui/501`/`uid = 501`. | CHANGE | Interpolate `REAL_UID`; retain the unsafe integer, duplicates, trailing text, and missing braces unchanged so each row still isolates its parser defect. |
| UID-09 | test `:364` | Root-process case deliberately returns UID `0`. | DELIBERATE_MISMATCH | Retain literal `0`; it is the semantic root boundary, not a host surrogate. |
| UID-10 | test `:1312` | Foreign-label cleanup case embeds `gui/501` even though the intended mismatch is the label suffix. | CHANGE | Use `gui/${REAL_UID}/${label}.foreign` to isolate the label mismatch. |
| UID-11 | test `:45,141,149,154,319,426-515` | Session IDs, handles, asids, unsafe integer `9007199254740992`, and digest-redaction sentinel `1001` are not Unix UIDs except where separately listed above. | RETAIN | Keep all session/asid values and their deliberate mismatch `1002`; they are protocol fixtures independent of host identity. |
| UID-12 | test `:259-270`; R19 fixture whole file | The verified R19 text contains `gui/501`, `/Users/ryan`, `/private/tmp`, pid `34924`, and other captured host output. `parseCleanupLaunchctlJob` uses the supplied exact `realService`; it does not compare the text to current filesystem/account state. | INERT_TEXT | Keep the fixture and `realService` byte-identical. Do not parameterize captured evidence. |
| PATH-01 | test `:29` | Fixture root starts at `/tmp` but is immediately canonicalized with `realpath`; all later real-state paths derive from that returned canonical root. This is not a raw `/tmp` equality or symlink assumption on the supported POSIX test hosts. | RETAIN | No change required. |
| PATH-02 | test `:345` | `/tmp/forbidden` is an option sentinel in a preflight call that must reject all options before inspection. It is never accessed. | INERT_TEXT | Retain. |
| PATH-03 | test `:581-592` | R16/R13 `/private/tmp/...` strings are byte-length regression vectors with `inspectRootAbsence: false`; they are never traversed or compared with current real state. | INERT_TEXT | Retain exact strings. |
| PATH-04 | test `:31-40,194-195,596-598,1424-1431` | Home, `HOME`, LaunchAgents, and tampered runtime-root values all derive from the canonical fixture root. No `/Users` or `/home` literal is compared to real state. | RETAIN | Retain harness-derived homes; only replace the UID in the absent-home override per UID-05. |
| PATH-05 | test `:993-1061` | Symlinked-ancestor and final-file-substitution cases intentionally create symlinks under the canonical fixture tree. | RETAIN | Preserve these adversarial tests unchanged; they validate product no-follow/canonical-identity behavior and contain no host path constant. |
| PATH-06 | test `:1367-1381` | Foreign executable paths derive from `harness.root`; comparisons are deliberate identity mismatches. | DELIBERATE_MISMATCH | Retain. |
| PLATFORM-01 | test `:193,360-361,542` | The positive harness intentionally simulates target platform `darwin`; the negative row deliberately uses `linux`; the socket guard explicitly tests macOS semantics. | RETAIN | Do not bind these to `process.platform`; doing so would skip target-OS behavior on Linux CI. |
| PROC-01 | test `:65-76,157,165,200,269` | Run counts, PIDs, nested handle `999999`, timestamps, and random ID are deterministic simulated process/session values, not real-host comparisons. | RETAIN | Retain. |
| MODE-01 | test `:83-89,121-133` | Fixture-created runtime directories/files now have explicit security modes; executable mode is explicitly set. | RETAIN | Preserve the prior fixture-mode repair. No product guard weakening. |
| GID-01 | whole test/product guard | No GID literal, mocked GID, `metadata.gid` comparison, or group-identity path exists. Group/other write bits are checked through `mode & 0o022`, not a host GID. | RETAIN / NON-FINDING | No GID repair. |

## Accepted implementation change list

The implementation owner may edit only the focused test and should make exactly this semantic repair:

1. Define `REAL_UID` once from `process.getuid()`.
2. Replace every coherent baseline/mock UID and UID-bearing semantic fixture route/output/assertion listed in UID-01 through UID-06, UID-08, and UID-10 with `REAL_UID` interpolation/value use.
3. Replace deliberate non-root mismatch values listed in UID-07 with `REAL_UID + 1`; retain literal root UID `0` and all non-UID session/asid values.
4. Leave the R19 fixture, the product proof script, parser/guard logic, temporary-path semantics, symlink tests, platform simulation, modes, daemon/supply/procedure behavior, and all files other than the focused test unchanged.

No other host-entanglement change is accepted by this diagnosis.

## Frozen identities

| Artifact | Bytes | SHA-256 | Git blob |
| --- | ---: | --- | --- |
| Focused test before repair | 58,693 | `7af5c15a48fea5c6f5255a57fc9a35fb7fee32a49badd44f1495f6d82c1eff4e` | `95107f38662058751563ea1f06f39f0bc5839b48` |
| R19 never-exited fixture | 3,049 | `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531` | `db1e4b6ca97c8e7b17bf182d04dab5d5d4287114` |
| Product login-proof script | 56,144 | `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306` | `bb1d5325cafe4b3a692bba3bae41791dd7b8d2c4` |

At diagnosis completion, `git diff -- projects/chirality-app-dev/frontend` was empty. The fixture and product identities above are hard acceptance controls for implementation and review.
