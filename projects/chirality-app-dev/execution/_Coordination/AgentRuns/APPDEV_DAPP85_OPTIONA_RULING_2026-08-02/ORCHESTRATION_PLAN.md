# Orchestration Plan — D-APP-85 Option-A Ruling Record

RunID: `APPDEV_DAPP85_OPTIONA_RULING_2026-08-02`

Manager: `HELPS_HUMANS`, managed by `HELP_HUMAN`

Basis: `codex/appdev-postpilot-status-reconcile@e5fe7e66cca66836f49980f50ad32816c8b96861`

## Objective

Record the owner's exact D-APP-85 Option-A ruling and transition only the
D-APP-85 register row to the lawful post-ruling, pre-main state. Preserve the
proposal packet bytes and stop before reconciliation dispatch.

## Frozen writes

1. `execution/_Coordination/_DECISIONS/D-APP-85_RULING_POSTPILOT_REMAINING_RECONCILIATION_2026-08-02.md`
2. only the D-APP-85 row in
   `execution/_Coordination/_DECISIONS/_REGISTER.md`
3. this AgentRun directory

No packet edit, receipt, discovery, repair, Task Management write, parity
selection, historical-UNKNOWN change, lifecycle/Checking-SHA change,
authority, decomposition, runtime/source/frontend, release, or Git action is
writable in this tranche.

## Work graph

1. HELPS_HUMANS verifies the exact owner token and selected packet hash.
2. HELPS_HUMANS writes the ruling record and the D-APP-85-only register
   transition to `RULED / ACTIVATION_PENDING_MAIN`.
3. HELPS_HUMANS verifies containment, preservation, packet identity, ruling
   transcription, register linkage, JSON, whitespace, and receipt non-write.
4. The tranche stops for CHANGE; RECONCILIATION remains blocked until the
   ruling/register merge is present on `main`.

No Agent 2 is required: this is exact transcription and bounded deterministic
validation, not a new semantic design or adversarial discovery stage.
