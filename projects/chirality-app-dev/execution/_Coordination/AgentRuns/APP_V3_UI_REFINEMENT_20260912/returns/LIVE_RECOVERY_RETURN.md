# Recovery author returns

Type 2: `/root/live_reconnect_diagnosis`, gpt-6-astra, medium. The parent
directly tested the App and supplied the failures. Author did not operate the
live App. Initial source work is described in the Git diff and live record.

## Tests-only follow-up return (verbatim)

Tests-only repair complete; production bytes unchanged.

Updated the three authorized test files:

- Known rejection fixtures now use typed HTTP errors; all restoration assertions remain.
- Added ambiguous transport coverage: one send, retained message, empty composer, Outcome unknown.
- Route tests assert the transport frame plus their original event and cancellation expectations.

Focused run: **3 suites, 57 tests passed**. No commit.

## Final cause-propagation return (verbatim)

Fixed cause propagation in `packages/core/src/turn-coordinator.ts`: supplier-provided interrupted terminals now retain supplier details and receive the Runtime-known reason before persistence and emission.

Strengthened `tests/app-owned-composition.test.ts`:
- Reproduced missing `service-shutdown` before the fix.
- Verified one terminal, preserved supplier outcome, identical persisted event, and one turn start.
- Verified explicit Stop carries no shutdown reason.

Runtime dist rebuilt. Focused client/daemon/registry/coordinator checks passed. Composition passed **10/10** alone; its restart-simulation test failed once in the combined run with `STOPPED_DEGRADED`, then passed on the diagnostic rerun. That intermittent shutdown issue is not claimed fixed.

No further frontend changes or commits. Source is ready for the next live service-loss trial.

## Parent validation

The complete production-path recheck subsequently reported Failed for a real
service SIGTERM. Final full-suite logs report 320 Runtime tests and 2175 App
tests passed, with four App tests skipped. The isolated restart-simulation
failure above remains a residual observation, not a resolved defect claim.
Independent review remains separate from this author return.
