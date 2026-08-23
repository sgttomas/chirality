# Implementation inventory — PR #632 UID portability repair

## Scope and identity

- Sole frontend source change: `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`.
- Basis SHA-256: `7af5c15a48fea5c6f5255a57fc9a35fb7fee32a49badd44f1495f6d82c1eff4e` (`58,693` bytes).
- Candidate SHA-256: `77ff11055fa5c110001d37784e0a344a7f7874fcc3c69a2b62b5b7722c5e5bd7` (`59,162` bytes).
- Exact source diff: `44` insertions, `35` deletions in one file.
- Executing host UID: `501`. This local host therefore cannot prove the cross-UID class; Linux CI with a different UID remains the host-identity arbiter.

## Accepted change coverage

| Diagnosis row | Candidate implementation | Disposition |
| --- | --- | --- |
| UID-01 | Module load fails explicitly when `process.getuid` is unavailable; exactly one file-level `const REAL_UID = process.getuid();` supplies baseline console, security, account, and process UID values. | CHANGE complete |
| UID-02 | Loaded service, not-found stderr, top-level GUI route, and domain identifier interpolate `REAL_UID`. | CHANGE complete |
| UID-03 | Console/stat and security-context output retain state override points and inherit the `REAL_UID` defaults. | CHANGE complete |
| UID-04 | Every exact top-level `launchctl print` expectation now expects ``gui/${REAL_UID}``. | CHANGE complete |
| UID-05 | Username and absent-home cases use `REAL_UID`, preserving the named failure as the only intended defect. | CHANGE complete |
| UID-06 | Both records in the malformed console fixture interpolate `REAL_UID`; the two-record ambiguity remains. | CHANGE complete |
| UID-07 | Account, console, domain-identifier, and security-context non-root mismatches use the four and only four `REAL_UID + 1` expressions; the wrong-domain security UID remains coherent at `REAL_UID`. | DELIBERATE_MISMATCH complete |
| UID-08 | Unsafe-integer, duplicate-field, ambiguous-context, trailing-output, and unclosed-brace fixtures interpolate `REAL_UID` while parser defects remain byte-semantically unchanged. | CHANGE complete |
| UID-09 | Root-process case retains literal UID `0`. | RETAIN complete |
| UID-10 | Foreign-label cleanup service uses ``gui/${REAL_UID}/${label}.foreign`` so only the label is foreign. | CHANGE complete |
| UID-11 | Session IDs, handles, asids, unsafe integer `9007199254740992`, and redaction sentinel `1001` remain independent of host identity. | RETAIN complete |
| UID-12 | The sole remaining literal `501` is the exact inert R19 captured service string used by the parser fixture. | INERT_TEXT complete |
| PATH-01..06 | Canonical fixture-root, option sentinel, captured path vectors, fixture-derived homes, symlink adversaries, and foreign executable paths are unchanged. | RETAIN / INERT complete |
| PLATFORM-01 | Positive target simulation remains `darwin`; negative platform case remains `linux`; socket semantics remain macOS-specific. | RETAIN complete |
| PROC-01 | Simulated run counts, PIDs, nested handle, timestamps, and random ID are unchanged. | RETAIN complete |
| MODE-01 | Existing explicit `0700`/`0600` fixture-mode repair remains unchanged. | RETAIN complete |
| GID-01 | No GID path was introduced. | RETAIN / NON-FINDING |

## Static whole-file assertion

The authorized one-shot assertion passed all of these exact conditions:

- exactly one `const REAL_UID = process.getuid();`;
- exactly four `REAL_UID + 1` deliberate mismatches;
- exactly one literal `501`, on the accepted inert R19 service string;
- no literal `502`;
- the root case still contains `harness.deps.uid = () => 0;`;
- the immutable R19 fixture and product script have their exact required hashes and sizes.

## Immutable controls

| Artifact | Bytes | SHA-256 | Result |
| --- | ---: | --- | --- |
| R19 never-exited fixture | `3,049` | `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531` | exact / unchanged |
| Product proof script | `56,144` | `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306` | exact / unchanged |
