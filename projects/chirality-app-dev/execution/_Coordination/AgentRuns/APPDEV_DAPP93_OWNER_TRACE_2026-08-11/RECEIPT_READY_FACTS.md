# Receipt-162-ready facts — D-APP-93 owner trace evidence

- Parent receipt: `Receipt-161`.
- Examined base: `f1e311fb7ab1c2a0800b1d32c59445368428dee9`.
- RunID: `APPDEV_DAPP93_OWNER_TRACE_2026-08-11`.
- Gate outcome: `RECORDED — owner-executed D-APP-93 packet evidence landed; disposition reserved to owner`.
- Owner-frozen/executed aggregate packet SHA-256: `db704c969143dad9ddfe832fa630748e091cb8a9b1524bb3d30d28dc74c56f83`.
- Source-ingest payload: 11 files, 1,002,581 bytes, all exact; original
  manifest SHA-256
  `3bae2915dd21a0701ea4159dc5e60f4d26fd70d0e4cf12e74e78bb897b778888`.
- Repository normalization: exactly two evidence copies canonically normalized
  under `NORMALIZATION_AMENDMENT.md`; raw external sources untouched; current
  normalized identities are
  `314ee96db7d73552a1e41d1b88e6d5d32fcd8aa7ed9c19411c3e2e56844e6ef1`
  (`EVIDENCE_CAPTURE.md`, 14,458 bytes) and
  `358228ac79541b829f2c61f3bcd3e89983f150ea020a2e692c02d8e27623f522`
  (`LLDB_TRANSCRIPT.txt`, 970,530 bytes).
- Verifier: `PASS_DAPP93_OWNER_TRACE_EVIDENCE`; return SHA-256 `99f2357445dcb1d87dd3761d279e1753cdbf6bdc4fc9d4d8fd866b4944eeb5f0`.
- Headline facts: SIGTERM reached `CrBrowserMain` at `mach_msg2_trap` under AppKit while two client connections were live; no Node/libuv/V8 signal-handler frames appeared; helper remained alive after debugger detach and daemon continued serving.
- Scope limit: LLDB intercepted the signal with `PASS=false`; packet trace did not test unintercepted processing.
- Deliverable effect: DEL-09-04 handoff surfaces updated; state remains `IN_PROGRESS`; Checking Approval SHA unchanged.
- No decision-register, closure, lifecycle, D-APP-88 disposition/remedy/acceptance, product/runtime/source, packet-byte, foreign-loop, receipt, or Git act.
- Checks: exact raw source-ingest identities; normalized-manifest 11/11 replay;
  deterministic 2/2 reproduction; zero-CR and zero-trailing-whitespace checks;
  required-paragraph exactness; fresh pre-normalization semantic verifier PASS;
  post-normalization manager semantic check; receipt validator; corpus v18/no
  drift; practitioner status; zero-exception diff/containment. Clean-checkout
  self-check, full candidate-range whitespace check, and combined 660-test suite
  remain CHANGE closeout obligations because this worktree carries the known
  ignored harness clone.
- Terminal pointers before final inventory regeneration: normalization amendment
  `76b80e7672445f00c855c34750019d4af7cfc0c979a3226e34393e492493cc83`;
  normalized-repository manifest
  `d48fbf1d604753cbbc2be91cc136f4b3cb31456dcd4b769d85821240a0f2afb7`;
  owner execution record
  `339ac6f11bef919b0a33f77e6252654c2a015d075e74e5ed5e1ab64abc54c829`;
  handoff `0326a0f7f3fba80342b40fd9041e433ced03770e4e14ea3b6d3d0d437d63c581`;
  manager return
  `6f61260d9a2948bb24386aaf32676337691bd1191775f10b255a399d137d0f6b`;
  closeout validation
  `720e98c3700e2443838b2553d42b8bc99ed5f5c7c3743298f62e4587f37914be`.
