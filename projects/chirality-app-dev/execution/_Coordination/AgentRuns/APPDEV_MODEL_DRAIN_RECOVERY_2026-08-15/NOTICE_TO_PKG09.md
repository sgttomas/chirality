# Cross-package notice — DEL-09-03 verification input

- Claim status: `VERIFIED_APP_INTEGRATION_EVIDENCE`.
- Evidence: `frontend/src/__tests__/integration/runtime-desktop-cli-shared-daemon.integration.test.ts` proves a correlated accepted turn held during model drain receives exactly one durable `turn.interrupted` outcome after graceful daemon stop and fresh-service restart.
- Validation: focused and full frontend Vitest PASS; worktree-correct typecheck PASS; fresh read-only review PASS.
- Requested action: PKG-09 / DEL-09-03 may consume and independently disposition this evidence under its verification ownership. No PKG-09 state was changed here.
- Blocking posture: non-blocking coordination notice. Rerun if Root daemon/client/session or residency contracts change.
