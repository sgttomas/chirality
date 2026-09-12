# Status: DEL-09-07 Two-Job Runtime-Control Installer Migration and Rollback

**Current State:** OPEN
**Last Updated:** 2026-09-12
**Retirement basis:** D-GOV-43 item 7 and IMPACT.md chain 2 (family 1), applied by `execution/_Coordination/_DECISIONS/D-APP-127_RULING_APPLICATION_D-GOV-43_CODEX_HOST_REPLATFORM_A2_2026-09-12.md`

## Retirement

Retired 2026-09-12 with `APP-HOLD-1`. The two-job runtime-control installer, migration and rollback served the per-user LaunchAgent daemon, which D-GOV-43 retires from the App path: the App starts, owns and stops the Runtime service as a child process, so no installer, staging, effective-state inspection or rollback transaction exists to build. The live `APP-HOLD-1-INIT-DEL-09-07` row was removed from `execution/_Coordination/APP_HOLD_REGISTER.csv` (the loop's retirement mechanism, as D-APP-107 retired the D-APP-104 row); no ordinary hold replaces it. `ScopeOfWork.md`, the four-document kit, D-APP-104 and D-APP-107 are preserved unchanged as history. No implementation, lifecycle promotion, release or Root act.

## History
- 2026-09-12 — Retired in place under D-GOV-43 item 7 (D-APP-127); lifecycle state unchanged (OPEN), no work is seated and none will be.
- 2026-09-04 — State set to OPEN (PREPARATION)
