# D-APP-94 R8 isolated-keychain feasibility result

Status: `PASS_FEASIBILITY_ONLY_NO_RELIANCE`

Accepted derivative basis: the 134-file R8 evidence set bound by `R8_PROBE_PASS_INTAKE_MANIFEST.md`; R8 preparation freeze `575b4731db717a884d02d4edb57bfa1d7b30a034115184f147e7533a47e50054`; fresh R8 verifier PASS `87314710f599411f5064dc11fcdf2c0fb761dd7e20727fd7bae7cd90852572aa`; R8 driver `d183572fadb5d67d8716858ae3b589acd60535433aea8239f0acf65b53738afd`.

## Derived result

- Prompt observation: exact `NONE`.
- Synthesized default: exactly one element, `/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809/home/Library/Keychains/login.keychain-db`.
- Synthesized search list: exactly one element, the same exact R8 login keychain path.
- Probe JSON: Electron `43.2.0`; Chrome `150.0.7871.129`; platform `darwin`; `isEncryptionAvailable: true`; `roundTrip: true`; `ciphertextBytes: 51`; public-constant SHA-256 `a85a62ad9d0e893fa7d85d110384baabdc11f7167dbf605978f498920e6a696f`.
- Owner state: `OWNER_STATE_MATCH_NO_BACKSTOP_WRITE`; backstop action `NOT_NEEDED`.
- PASS was committed before destructive cleanup: `PASS_COMMITTED_BEFORE_DESTRUCTIVE_CLEANUP`.
- Cleanup: `PASS_COMMITTED_CLEANUP_COMPLETE`.
- Fixed R8 temp root `/private/tmp/chirality-dapp94-option-c-keychain-probe-r8-20260809` is absent; returned evidence records absence status `0`, and intake-time read-only observation independently returned absent.

This result establishes only bounded feasibility of the isolated sealed-HOME login-keychain recipe in the observed host/session. It grants no reliance, attempt-3, C1118, execution-token, runtime, security, keychain, credential, Electron, product, package, trace, acceptance, Git, or Task Management authority.
