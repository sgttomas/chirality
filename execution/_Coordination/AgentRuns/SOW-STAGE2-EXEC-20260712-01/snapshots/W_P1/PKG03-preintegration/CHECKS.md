# PKG-03 Preintegration Reconciliation Checks

Technical reproduction verdict: `PASS_PENDING_REQUIRED_AGENT2_FANIN`.

- 8/8 members reproduced across both numeric batches.
- All four upstream terminal child returns reproduced: author `PASS`, verifier
  `PASS_UNCHANGED` for each batch.
- 100% of five current upstream manifests rehashed: 3,610/3,610 rows; every
  path portable, contained, present, unique within its manifest, byte-sized,
  hash-correct, and self-excluding.
- 234 mappings and 1,966/1,966 source lines reproduced.
- Eight evidence candidates, eight distinct clean production candidates, and
  eight external finalization reports reproduce their exact hashes and schema
  bindings.
- Fresh clean and isolated-dual validation, maps, parity, deterministic
  checklist, deterministic offline render, and content/preservation assertions
  PASS for all eight members.
- Negative partial and unauthorized-dual probes: 16/16 fail closed.
- Exact replacement manifest: 40/40 rows, byte-identical to upstream.
- Exact inverse rollback manifest: 40/40 rows, byte-identical to upstream.
- Apply/target/control-preservation/rollback simulations: 8/8 PASS.
- Practitioner self-check: PASS.
- Practitioner harness: 264/264 PASS in 67.95 seconds.
- Piping project tree: 191,240 files before and after; SHA-256
  `974fe2fad26880ba85c0359ee18f9ee87a404fd097a83bb6248cc6348b391a92`
  before and after; zero project writes.
- Live Piping Git status: clean, including untracked non-ignored state.

Verdict classes remain separate: schema `PASS`, content/authority `PASS`,
preservation/containment `PASS`, execution substrate `PASS` for the manager
reproduction. Package acceptance remains blocked solely because the required
fresh governed Agent 2 verifier session could not be launched.

