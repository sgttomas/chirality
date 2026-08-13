# WORKING_ITEMS brief amendment v3 — native quit race remediation

Authorized by HELP_HUMAN under the owner's original product-source/test scope after fresh review returned `BLOCK`.

Serialize one remediation Agent 2 owning exactly:

- `projects/chirality-app-dev/frontend/electron/runtime-shutdown-policy.ts`
- `projects/chirality-app-dev/frontend/electron/main.ts`
- `projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-daemon-signal-integration.test.ts` (or one exact sibling behavioral test if necessary)
- its run record under this run root.

Objective: implement a pure testable policy so a native `before-quit` remains prevented while binder-started teardown is in flight, and only the owned final `app.exit()` after teardown is allowed. Acceptance requires a behavioral binder-first then before-quit test, no double stop, no GUI regression, focused tests, frontend typecheck, and a new fresh read-only review over complete bytes. No other scope changes; all original exclusions remain.
