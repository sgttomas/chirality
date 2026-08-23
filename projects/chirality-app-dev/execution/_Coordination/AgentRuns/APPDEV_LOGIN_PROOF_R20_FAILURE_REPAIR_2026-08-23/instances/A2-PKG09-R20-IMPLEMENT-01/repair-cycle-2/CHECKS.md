# CHECKS — final repair cycle 2 — A2-PKG09-R20-IMPLEMENT-01

Verdict: `PASS`

The required gates ran in the sealed order.

| Order | Command | Cwd | Exit | Exact result |
|---:|---|---|---:|---|
| 1 | `node --check scripts/run-packaged-launchagent-login-proof.mjs` | `projects/chirality-app-dev/frontend` | 0 | PASS; no output |
| 2 | `./node_modules/.bin/vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` | `projects/chirality-app-dev/frontend` | 0 | PASS; 1 file, 72 tests passed, duration 3.26 s |
| 3 | `npm run typecheck` | `projects/chirality-app-dev/frontend` | 0 | PASS; frontend and Electron TypeScript configurations |
| 4 | source/target `test -f`, `test ! -L`, `cmp -s`, `stat`, and `shasum -a 256` | repository root | 0 | PASS; both fixtures regular/non-symlink, 3,049 bytes, identical required SHA-256 |
| 5 | `shasum`, `stat`, `git diff --stat`, and `git diff --numstat` over the three frontend targets | repository root | 0 | PASS; candidate identities and 754-insertion/28-deletion two-file tracked diff frozen |
| 6 | `git diff --check` | repository root | 0 | PASS; no output |
| 7 | `python3 tools/software_workflow/validate_change_scope.py . --allowed projects/chirality-app-dev` | repository root | 0 | PASS; zero violations |
| 8 | `git diff --cached --name-only` | repository root | 0 | PASS; empty output/index |

No full `npm test`, build, package, network, Git integration, proof procedure,
GUI, launchd/plist mutation, default-operator query, prohibited private-root
traversal, or Desktop evidence read occurred.
