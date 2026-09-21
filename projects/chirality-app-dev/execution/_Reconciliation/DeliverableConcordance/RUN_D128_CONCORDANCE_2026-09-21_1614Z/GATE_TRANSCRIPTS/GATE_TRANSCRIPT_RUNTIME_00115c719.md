# Gate transcript — Runtime (projects/chirality-runtime) @ 00115c719

- Run: `RUN_D128_CONCORDANCE_2026-09-21_1614Z` (D-APP-128).
- Source state: `main` `00115c71931bcae79909602d653740d3bb72dfa1` (the D-APP-128 pinned basis).
- Environment: disposable full-repository detached worktree at that SHA, outside this repository; fresh `npm ci`; Node v24.5.0, npm 11.5.2; macOS (Darwin 25.6.0). Installs and build output never entered the evidence tree.
- Date: 2026-09-21 (UTC ~16:15–16:25).
- Commands: `npm ci` → `npm run build` (`tsc -b`) → `npm run typecheck` → `npx vitest run` (cwd `projects/chirality-runtime`)
- Result: install/build/typecheck exit 0; Vitest 42 files / 407 tests passed; exit 0
- R2 citation form: `GATE-TRANSCRIPT(RUNTIME@00115c719)` plus the named test file/case.

Epistemic status: immutable, source-state-bound evidence; not a release, readiness or acceptance claim.

## Verbatim log tail

```text
## runtime npm ci
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
npm warn deprecated glob@10.5.0: Old versions of glob are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me

added 430 packages in 5s
exit:0
## runtime build

> @chirality/runtime-workspace@0.1.0 build
> tsc -b

exit:0
## runtime typecheck

> @chirality/runtime-workspace@0.1.0 typecheck
> tsc -b --pretty false

exit:0
## runtime vitest
   ✓ Unix-domain runtime daemon > isolates late prior-generation iterator events after a successful forced stop and restart  2110ms
   ✓ Unix-domain runtime daemon > caps post-force transport settlement at 500 ms before reporting cleanup failure  2513ms
 ✓ tests/pi-packaging.test.ts (16 tests) 11905ms
   ✓ cjs consumer: real SDK offline success  1017ms
   ✓ cjs consumer: real SDK offline interrupt  700ms
   ✓ cjs consumer: real SDK offline close  650ms
   ✓ cjs consumer: real SDK offline release  691ms
   ✓ cjs consumer: real SDK offline deadline  620ms
   ✓ cjs consumer: real SDK offline capacity  973ms
   ✓ cjs consumer: real SDK offline snapshot  1092ms
   ✓ cjs consumer: real SDK offline load-error  561ms
   ✓ esm consumer: real SDK offline success  579ms
   ✓ esm consumer: real SDK offline interrupt  568ms
   ✓ esm consumer: real SDK offline close  587ms
   ✓ esm consumer: real SDK offline release  559ms
   ✓ esm consumer: real SDK offline deadline  583ms
   ✓ esm consumer: real SDK offline capacity  1050ms
   ✓ esm consumer: real SDK offline snapshot  946ms
   ✓ esm consumer: real SDK offline load-error  590ms

 Test Files  42 passed (42)
      Tests  407 passed (407)
   Start at  10:15:30
   Duration  18.47s (transform 1.09s, setup 0ms, collect 5.13s, tests 76.64s, environment 4ms, prepare 1.49s)

vitest-exit:0
```
