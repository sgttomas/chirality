# Implementation and mode inventory

## Source change

- Sole frontend write: `frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`.
- Diff size: `10` additions, `5` deletions.
- Preimage SHA-256: `6750655e8c7150bce8e6d12bf0e968de9129b80598309c317bea044b40c6ef18`.
- Candidate SHA-256: `7af5c15a48fea5c6f5255a57fc9a35fb7fee32a49badd44f1495f6d82c1eff4e`.
- Unchanged product proof-script SHA-256: `f2f886bdc9d1a296bb7851a5221448946b36bac54d83e426d0bd3ed6cd81f306`.

The fake packaged-install block now supplies `{ recursive: true, mode: 0o700 }` to both directory-creation calls and `{ mode: 0o600 }` to all three guarded file writes. Existing data, ordering, fake-install behavior, and guard expectations are unchanged.

## Guarded runtime-data inventory

| Fixture path | Creation site | Explicit resulting mode |
| --- | --- | --- |
| `runtime-data/runtime` | intermediate created by recursive `mkdir(.../runtime/logs)` | `0700` |
| `runtime-data/runtime/logs` | recursive `mkdir` | `0700` |
| `runtime-data/runtime/auth` | intermediate created by recursive `mkdir(.../auth/tokens)` | `0700` |
| `runtime-data/runtime/auth/tokens` | recursive `mkdir` | `0700` |
| `runtime-data/runtime/logs/daemon.stdout.log` | `writeFile` | `0600` |
| `runtime-data/runtime/logs/daemon.stderr.log` | `writeFile` | `0600` |
| `runtime-data/runtime/auth/tokens/operator.token` | `writeFile` | `0600` |

The corrected read-only source assertion found exactly two fixture `mkdir` calls and two explicit `0700` directory options, plus exactly three fixture `writeFile` calls and three explicit `0600` file options. No product or guard source changed.
