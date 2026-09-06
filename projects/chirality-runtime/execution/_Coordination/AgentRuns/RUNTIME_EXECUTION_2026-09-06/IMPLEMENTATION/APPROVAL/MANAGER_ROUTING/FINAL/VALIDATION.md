# Observed validation

Commands executed in the Runtime workspace against the source hashes in this snapshot:

```text
npm run typecheck
npx --no-install vitest run tests/manager-approval-integration.test.ts tests/codex-manager.test.ts tests/delegated-runtime.test.ts tests/codex-supervisor.test.ts tests/manager-pi-integration.test.ts tests/standalone.test.ts tests/approval-store.test.ts packages/cli/test/cli.test.ts
```

Typecheck PASS. Vitest 8 test files passed, 139 tests passed, exit 0; start 23:32:55, duration 14.54s. This is a transcription of observed tool output (exec session 43315, final chunk c0da02), not a raw redirected log.

| Suite | Passed tests |
|---|---:|
| manager-approval-integration | 4 |
| codex-manager | 9 |
| delegated-runtime | 34 |
| codex-supervisor | 23 |
| manager-pi-integration | 4 |
| standalone | 11 |
| approval-store | 21 |
| CLI | 33 |

All transports/providers in these tests are controlled fixtures. Local Unix-socket/process tests ran with approved sandbox escalation. No live account, vendor process, or user provider traffic was invoked by this validation.
