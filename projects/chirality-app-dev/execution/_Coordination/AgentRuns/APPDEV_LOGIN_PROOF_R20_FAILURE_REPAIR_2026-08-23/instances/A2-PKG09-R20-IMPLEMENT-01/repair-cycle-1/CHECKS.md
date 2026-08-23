# CHECKS — repair cycle 1 — A2-PKG09-R20-IMPLEMENT-01

Verdict: `BLOCKED`

| Command | Cwd | Exit | Exact result |
|---|---|---:|---|
| `node --check scripts/run-packaged-launchagent-login-proof.mjs` | `projects/chirality-app-dev/frontend` | 0 | PASS; no output |
| `./node_modules/.bin/vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | `projects/chirality-app-dev/frontend` | 1 | FAIL; 1 file failed; 15 failed / 57 passed / 72 total; duration 3.26 s |

Representative common failure:

```text
Failure-log identity or auth snapshot is unsafe; retained only in private runtime data: ENOENT: no such file or directory, lstat '/dev/fd/13/runtime'
```

The failed tests cover ordinary install cleanup, ordinary PASS, exact
never-exited PASS, PASS-only deletion failure, ordinary observation failure,
token detection, zero/one missing logs, later default protection, refusal
preservation, pid-less cleanup, and the distinct F-05 job-loaded case.

`npm run typecheck`, fixture fidelity, final candidate diff/whitespace,
containment, and index gates were not run after the required focused-test
failure. No result is inferred for them.

No full suite, build, package, network, Git integration, proof/operator/GUI,
launchd mutation, default-operator query, prohibited private-root traversal,
or Desktop evidence read occurred.
