# Work graph amendment 07 — owner-directed integrated remediation

- Superseding owner direction: **“Push through failures.”** This immediately
  supersedes the prior Agent 0 stop/rollback disposition.
- Product restoration: exact frozen diff 04 bytes are restored to the two live
  frontend candidate paths at their reviewed hashes.
- Node state: `ACTIVE_INTEGRATED_REMEDIATION`; implementation preparation is
  complete, but package acceptance/publication remains pending integrated gates.
- App-side remediation boundary: Agent 0 owns routing of the App-side
  `RUNTIME_INSTRUCTION_ROOT_ENV` alignment needed to clear the integrated
  failures. PKG-09 retains the login-proof product/test and its records.
- Forbidden writes: no root-runtime surface, unrelated App mock, `node_modules`,
  PKG-08/TM, receipt, or Git write by this WORKING_ITEMS instance.
- Dependency edge: `Agent 0 App-side remediation -> integrated frontend
  Vitest/typecheck/build -> fresh 100% login-proof rereview -> manager fan-in`.
- Acceptance gate: all three mandatory integrated checks and fresh rereview must
  pass before publication/closeout; no waiver is inferred.
- Owner-act boundary: logout/login and capture remain unexecuted and reserved to
  the owner only after integrated acceptance.
