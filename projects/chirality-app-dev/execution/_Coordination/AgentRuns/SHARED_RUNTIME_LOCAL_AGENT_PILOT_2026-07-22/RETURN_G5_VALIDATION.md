# G5 Return — Validation and Live Pilot

Status: `COMPLETED`

Automated acceptance:

- runtime: 43/43 tests;
- app-dev: 894 passed, 4 skipped; typecheck and production build passed;
- PEC: 74 core, 172 server, 110 adapter tests; typecheck and web build passed;
- Section 8: 8/8 and Section 9: 16/16 premerge checks;
- dependency boundary, Pi supply-chain, secret scan, instruction-root integrity,
  and short independent network-policy proof passed;
- packaged Claude SDK and offline packaged Pi SDK proofs passed;
- the packaged CLI queried the daemon using Electron's embedded Node runtime.

Live oMLX acceptance exercised both installed models, explicit 35B → 122B →
35B residency transitions, a successful bounded read on each model,
interruption, fail-closed missing tool evidence, and a final successful governed
35B Agent 1 → Agent 2 run.
