# Return — A2-PKG09-R20-PR632-FIXTURE-DIAGNOSE-01

- Status: `PASS` for diagnosis; the authorized reproduction itself failed as expected.
- Exact command: `umask 0002; ./node_modules/.bin/vitest run src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts` from `projects/chirality-app-dev/frontend`; invoked once only.
- Exact result: exit `1`; `1` failed file; `15` failed, `57` passed, `72` total.
- Exact first divergence: `Failure-log identity or auth snapshot is unsafe; retained only in private runtime data: Failure-log directory identity or permissions are unsafe`.
- Mechanism: fixture fake install creates `runtime`, `logs`, `auth`, and `tokens` without modes (`0775` under umask `0002`) and creates stdout/stderr/token without modes (`0664`); the first rejected path is `runtime-data/runtime`.
- Product conclusion: no product-owned runtime directory relevant to the guard lacks explicit `0700` plus safe chmod before reliance; product auth/state files use explicit/chmodded `0600`. Launchd, not product JS, creates stdout/stderr from plist paths; the product hardens their parent and the unchanged guard validates their resulting modes.
- Recommended implementation inventory: only `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-launchagent-login-proof.test.ts`; pin all fake-install guarded directories to `0700` and files to `0600`. No product source change and no guard weakening.
- Evidence: `ACTIVATION.md`, `focused-umask-0002.log`, `SOURCE_SITE_MATRIX.md`, `DIAGNOSIS.md`, `RETURN.md`.
- Fences: no frontend/shared-record edit, stage, commit, network, package, proof, daemon, launchd, operator, or Git mutation; no delegation; no test rerun.
- Blockers: none.
