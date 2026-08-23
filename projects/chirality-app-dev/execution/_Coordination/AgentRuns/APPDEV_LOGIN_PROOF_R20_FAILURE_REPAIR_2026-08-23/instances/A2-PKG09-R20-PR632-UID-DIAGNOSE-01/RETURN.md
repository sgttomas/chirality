# Return — PR #632 UID and host-entanglement diagnosis

- Status: `PASS_DIAGNOSIS`.
- Prompt diagnosis: independently confirmed from source.
- Scope result: complete static sweep of the focused 1,473-line test plus directly relevant product/helper paths and the complete captured fixture.
- Root cause: mocked UID `501` reaches `expectedUid`; real fixture filesystem metadata carries the runner UID; `assertSafeSnapshotMetadata()` correctly rejects the mismatch.
- Product disposition: correct and unchanged. The ownership guard must not be weakened.
- Accepted repair: focused-test-only coherent baseline derivation from `const REAL_UID = process.getuid()`, with deliberate non-root mismatches expressed as `REAL_UID + 1`, root `0` retained, and all structural/session/path mismatch semantics preserved.
- Whole-file non-findings: no GID entanglement; no hardcoded `/Users` or `/home` path compared with real state; no unsafe `/tmp` symlink equality; homedir values are fixture-derived; platform simulation is deliberate; real PIDs/session IDs are not consumed.
- R19 fixture control: 3,049 bytes; SHA-256 `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531`; must remain byte-identical.
- Product proof-script control: 56,144 bytes; SHA-256 `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`; must remain byte-identical.
- Focused test basis: 58,693 bytes; SHA-256 `7af5c15a48fea5c6f5255a57fc9a35fb7fee32a49badd44f1495f6d82c1eff4e`.
- Ambiguity/escalation: none. No source disagreement, ambiguous real-state comparison, required product change, fixture drift, missing category, or scope expansion found.
- Execution limits honored: no test, build, typecheck, supply, package, preflight, proof, network, private-root/Desktop read, operator action, frontend edit, or Git mutation was performed. No delegation occurred.
- CI calibration: this run makes no local UID-reproduction claim; CI is the arbiter for host-identity classes.

## Implementation acceptance criteria

1. Only `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` changes on the frontend source surface.
2. One real UID constant supplies every coherent baseline account, console, security-context, `gui/<uid>`, exact not-found, service, and command-expectation value enumerated in `HOST_ENTANGLEMENT_INVENTORY.md`.
3. Every deliberate non-root UID mismatch uses `REAL_UID + 1`; the root case remains exactly `0`; session/asid malformed and mismatch fixtures retain their original non-UID semantics.
4. R19 fixture SHA-256 remains `9d8f02e4ad602c149b22ce013d1bf33dfe054c9820d1ece09ba80ecb23c90531` and size remains 3,049 bytes.
5. Product proof script SHA-256 remains `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306` and size remains 56,144 bytes.
6. No product guard, daemon, supply, package, staged-procedure semantics, proof state, or operator/private state changes.
7. Authorized validation must demonstrate normal focused, one `umask 0002` focused, full local-socket suite, typecheck, syntax, and APP-HOLD results while explicitly recording that CI—not the UID-501 local host—is the UID-class proof.

Dependent node `WP-F2` may be released only after WORKING_ITEMS accepts this return.
