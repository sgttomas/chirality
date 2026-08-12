# Receipt-162-ready facts — D-APP-93 owner trace evidence

- Parent receipt: `Receipt-161`.
- Examined base: `f1e311fb7ab1c2a0800b1d32c59445368428dee9`.
- RunID: `APPDEV_DAPP93_OWNER_TRACE_2026-08-11`.
- Gate outcome: `RECORDED — owner-executed D-APP-93 packet evidence landed; disposition reserved to owner`.
- Owner-frozen/executed aggregate packet SHA-256: `db704c969143dad9ddfe832fa630748e091cb8a9b1524bb3d30d28dc74c56f83`.
- Imported payload: 11 files, 1,002,581 bytes, all exact.
- Verifier: `PASS_DAPP93_OWNER_TRACE_EVIDENCE`; return SHA-256 `99f2357445dcb1d87dd3761d279e1753cdbf6bdc4fc9d4d8fd866b4944eeb5f0`.
- Headline facts: SIGTERM reached `CrBrowserMain` at `mach_msg2_trap` under AppKit while two client connections were live; no Node/libuv/V8 signal-handler frames appeared; helper remained alive after debugger detach and daemon continued serving.
- Scope limit: LLDB intercepted the signal with `PASS=false`; packet trace did not test unintercepted processing.
- Deliverable effect: DEL-09-04 handoff surfaces updated; state remains `IN_PROGRESS`; Checking Approval SHA unchanged.
- No decision-register, closure, lifecycle, D-APP-88 disposition/remedy/acceptance, product/runtime/source, packet-byte, foreign-loop, receipt, or Git act.
- Checks: exact imported identities; required-paragraph exactness; fresh semantic verifier PASS; receipt validator; corpus v18/no drift; practitioner status; diff/containment. Clean-checkout self-check and combined 660-test suite remain a CHANGE closeout obligation because this worktree carries the known ignored harness clone.
- Final inventory identity and terminal artifact hashes: compute from `FINAL_INVENTORY.sha256` after all manager records are frozen.
