# CHECKS — A2-PKG09-R20-IMPLEMENT-01

Final verdict: `PASS`

## Required commands and results

| Command | Cwd | Exit | Result |
|---|---|---:|---|
| `node --check scripts/run-packaged-launchagent-login-proof.mjs` | `projects/chirality-app-dev/frontend` | 0 | PASS; no output |
| `./node_modules/.bin/vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | `projects/chirality-app-dev/frontend` | 0 | PASS; 1 file, 64 tests passed, duration 2.09 s |
| `npm run typecheck` | `projects/chirality-app-dev/frontend` | 0 | PASS; `tsc --noEmit --incremental false` and Electron tsconfig both passed |
| `test -f /private/tmp/ch-r19-fixture/launchctl-print-r19-never-exited.txt && test ! -L /private/tmp/ch-r19-fixture/launchctl-print-r19-never-exited.txt && /usr/bin/stat -f 'mode=%HT bytes=%z' /private/tmp/ch-r19-fixture/launchctl-print-r19-never-exited.txt && /usr/bin/shasum -a 256 /private/tmp/ch-r19-fixture/launchctl-print-r19-never-exited.txt` | repository root | 0 | PASS; source regular/non-symlink, 3,049 bytes, required SHA-256 |
| `test -f projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt && test ! -L projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt && cmp -s /private/tmp/ch-r19-fixture/launchctl-print-r19-never-exited.txt projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt && /usr/bin/stat -f '%z %N' /private/tmp/ch-r19-fixture/launchctl-print-r19-never-exited.txt projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt && /usr/bin/shasum -a 256 /private/tmp/ch-r19-fixture/launchctl-print-r19-never-exited.txt projects/chirality-app-dev/frontend/src/__tests__/scripts/fixtures/launchctl-print-r19-never-exited.txt` | repository root | 0 | PASS; source and target both 3,049 bytes with identical required SHA-256 |
| `git diff --check` | repository root | 0 | PASS |
| `python3 tools/software_workflow/validate_change_scope.py . --allowed projects/chirality-app-dev` | repository root | 0 | PASS; all dirty/untracked paths App-contained |
| `git diff --cached --name-only` | repository root | 0 | PASS; empty output/index |

The focused Vitest assertions cover the verified real fixture, exact sentinel
and malformed variants, integer/crash-loop continuity, exact-owned running
bootout, proof-observation failure copies, mutation refusal, bootout failure,
loaded-job and live-process preservation, token detection with copy-neither
private retention, and a later default-protection failure retaining the
pre-removal copies.

## Explicitly not run

No full `npm test`, build, package, network, Git integration, proof procedure,
GUI, launchd/plist mutation, default operator query, or prohibited evidence
read was performed.
