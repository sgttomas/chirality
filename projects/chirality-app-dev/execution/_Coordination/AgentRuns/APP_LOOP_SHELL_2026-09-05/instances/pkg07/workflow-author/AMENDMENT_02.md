# Brief amendment 02 — focused registered-test invocation

Parent authorizes `node node_modules/vitest/vitest.mjs run src/__tests__/lib/governed-workflow.test.ts` from WORKING_ROOT/frontend, as a bounded invocation of existing frontend-test, only after parent dependency-ready notice. Capture stdout/stderr, runtime versions, command/cwd/env/exit and preserve test fixture/source hashes in own evidence. Global checks remain parent-owned. No write-scope expansion.
