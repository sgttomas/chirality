# Coordination Notice — D-APP-85 C06 Daemon-Recovery Root Route

**Date:** 2026-08-02

**From:** Chirality App Dev loop

**To:** Root `HELP_HUMAN`; Root `TASK_MANAGEMENT` for optional harvest only

**Status:** ordinary coordination notice; not authority

## Verified App finding

The post-closeout read-only D-APP-85 audit reverified the surviving C06 claim
against current generic-runtime bytes. `TurnCoordinator.run()` persists
`turn.accepted` before terminal evidence. `ResidencyCoordinator` tracks active
turns only in process memory, and daemon startup/model activation does not
reconcile accepted turns lacking terminal evidence before admission or
activation. A daemon restart can therefore lose the drain count and leave an
accepted turn unterminated while later admission or model activation proceeds.

The inspected evidence is:

- `runtime/packages/core/src/turn-coordinator.ts`;
- `runtime/packages/core/src/session-store.ts`;
- `runtime/packages/core/src/residency-coordinator.ts`; and
- `runtime/packages/daemon/src/runtime-daemon.ts`.

This is a verified contradiction of the C06 follow-on claim that model-drain
paths preserve exactly one terminal outcome across daemon recovery. It does
not alter the already-executed D-APP-85 ruling or exact Gate-2 manifest.

## Root ownership and return posture

Root DEL-02-06 owns any generic runtime repair. App may add affected-client
proof only after Root fan-in returns the accepted generic behavior and
evidence basis. Root should use its own instruments and owner gates to decide
whether and how to activate that work.

## Task Management harvest candidate

This line is harvest emphasis only. It neither creates nor updates a Root
register row; Root `TASK_MANAGEMENT` may present it for owner promotion under
its own on-demand process.

TM-CANDIDATE: Recover accepted turns lacking terminal evidence idempotently before daemon admission/model activation | D-APP-85 C06; runtime/packages/core/src/{turn-coordinator,session-store,residency-coordinator}.ts; runtime/packages/daemon/src/runtime-daemon.ts

## No-effect boundary

This ordinary notice creates no register write, authority, scope,
decomposition, dependency, lifecycle, implementation, runtime, source,
frontend, release, issuance, publication, professional-reliance, commit, push,
or merge effect.
