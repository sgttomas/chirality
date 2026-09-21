# Gate transcript — App frontend (projects/chirality-app-dev/frontend) @ 00115c719

- Run: `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128).
- Source state: `main` `00115c71931bcae79909602d653740d3bb72dfa1` (the D-APP-128 pinned basis).
- Environment: disposable full-repository detached worktree at that SHA, outside this repository; fresh `npm ci`; Node v24.5.0, npm 11.5.2; macOS (Darwin 25.6.0). Installs and build output never entered the evidence tree.
- Date: 2026-09-21 (UTC ~16:15–16:25).
- Commands: Runtime built first (above); then `npm ci` → `npm run typecheck` → `npx vitest run` (cwd `projects/chirality-app-dev/frontend`)
- Result: install exit 0; typecheck exit 0; Vitest 222 files passed + 1 skipped (223); 2,285 tests passed + 4 skipped (2,289); exit 0
- R2 citation form: `GATE-TRANSCRIPT(APP@00115c719)` plus the named test file/case.

Epistemic status: immutable, source-state-bound evidence; not a release, readiness or acceptance claim.

## Verbatim log tail

```text
## frontend npm ci
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
npm warn deprecated rimraf@2.6.3: Rimraf versions prior to v4 are no longer supported

added 848 packages in 20s
exit:0
## frontend typecheck

> chirality-frontend@3.0.1 typecheck
> tsc --noEmit --incremental false && tsc -p tsconfig.electron.json --noEmit --incremental false

exit:0
## frontend vitest

 RUN  v4.1.10 <abs-path>


 Test Files  222 passed | 1 skipped (223)
      Tests  2285 passed | 4 skipped (2289)
   Start at  10:16:16
   Duration  11.00s (transform 6.50s, setup 0ms, import 18.83s, tests 33.91s, environment 12ms)

vitest-exit:0
```
