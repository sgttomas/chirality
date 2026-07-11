# Gate transcript — D-APP-55 R2 verification binding (MR-3, owner-ruled per-wave transcript)

- Source state: `main` = `fac46e33f` (frontend byte-identical to `4c8ed8907` and `61d70bdb0`; verified `git diff` empty)
- Environment: disposable full-repo local clone at `fac46e33f` (scratchpad), fresh `npm ci` per lockfile
- Date: 2026-07-11 (UTC run at 22:06Z)
- Commands: `npm ci` -> `npm run typecheck` -> `npx vitest run`
- Result: typecheck exit 0; Vitest **667 passed / 4 skipped (671)**, exit 0 — matches the Receipt 4 recorded pass at `61d70bdb0`
- Environment-fidelity note: a frontend-only copy is NOT a valid gate environment — 3 tests assert repo-root context (repo `agents/` roster; `docs/harness/reliance_boundary_register.md`; `.github/workflows/harness-premerge.yml`) and fail ENOENT there. Wave transcripts must use a full-repo clone.
- R2 citation form: `GATE-TRANSCRIPT(W1@fac46e33f)` + named test file/case per row (MR-3/MR-10).

## Vitest output (tail)
```
=== VITEST ===
 ✓ src/__tests__/docs/reliance-boundary-register.test.ts (1 test) 3ms
 ✓ src/__tests__/lib/loop-first.test.ts (4 tests) 2ms
 ✓ src/__tests__/scripts/harness-premerge-workflow.test.ts (1 test) 4ms
 ✓ src/__tests__/lib/agent-matrix-launch.test.ts (2 tests) 4ms
 ✓ src/__tests__/lib/tool-catalog.test.ts (2 tests) 7ms
 ✓ src/__tests__/lib/harness-sanitize.test.ts (5 tests) 1ms
 ✓ src/__tests__/lib/agent-engine-port.test.ts (1 test) 2ms
 ✓ src/__tests__/lib/ansi.test.ts (2 tests) 2ms
 ✓ src/__tests__/components/chat-markdown.test.ts (2 tests) 15ms

 Test Files  92 passed | 1 skipped (93)
      Tests  667 passed | 4 skipped (671)
   Start at  15:06:00
   Duration  4.02s (transform 1.63s, setup 0ms, collect 4.87s, tests 8.02s, environment 10ms, prepare 3.67s)

vitest-exit:0
```
