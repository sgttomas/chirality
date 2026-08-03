# DEL-02-06 first activation record — accepted-turn recovery planning

RunID: `DEL-02-06-RUNTIME-SPEC-001`
ParentRunID: `ROOT_FOUR_LANES_2026-08-02`
ManagerNode: `W1`
ManagerRole: `WORKING_ITEMS`
PackageID: `PKG-02`
SelectedDeliverables: `DEL-02-06` only
PlanVersion: `2`
Posture: `MIXED`
ActivationState: `HELD_AT_N0`

## Objective

Take the `TM-ROOT-108` accepted-turn recovery concern through the accepted
first-activation lane: exact specification, read-only consumer and
implementation-surface inventory, evidence-matrix design, and change planning.
The concern is that a persisted `turn.accepted` without terminal evidence can
survive daemon loss and remain unreconciled before new admission or model
activation.

## Accepted basis

- Repository basis: `origin/main@97678a841ef58345c73d3470ed8de57c9b1405d2`.
- Accepted Scope of Work SHA-256:
  `dc78196e96ec79d74b80b712bbc2e3d047a2e322e8c588497603ec426fbb0146`.
- Scope-of-Work decomposition pin:
  `2db2c712825af13d6b5425c34d31ff9daf470c89`.
- Owner-routed concern:
  `execution/_Coordination/_TaskManagement/DEL-02-06_HANDOFF_TM-ROOT-108_2026-08-02.md`
  at SHA-256
  `da191f8c12207398c676531daf8941148797dc4f206c33ad58797a1e74a77fbc`.
- Inbound App evidence:
  `execution/_Coordination/NOTICE_D-APP-85_C06_DAEMON_RECOVERY_ROOT_ROUTE_2026-08-02.md`
  at SHA-256
  `0b34cefdc9abd5927db1b6bdda07225c37c42806ff5b3f946bb182227f08dc41`.
- Owner ruling:
  `execution/_Coordination/_TaskManagement/RULING_2026-08-02_ROOT_HARVEST_SLATE.md`
  at SHA-256
  `9fde04e411f1839c6b37ae09e7fba0e8b60a6dd54e434b2bbf2d570e854520d8`.
- Sealed parent activation:
  `execution/_Coordination/AgentRuns/ROOT_FOUR_LANES_2026-08-02/ORCHESTRATION_PLAN.md`,
  plan version 2, owner selection authority `HUMAN`.

## Authority and exclusions

The owner direction opens this first planning activation. It does not
authorize runtime or client implementation, contract repinning, dependency
declaration, lifecycle transition, release, publication, issuance, reliance,
or Task Management register closure. `ScopeOfWork.md`, `_STATUS.md`, all
governance and decomposition surfaces, `runtime/**`, App, PEC, Piping, Tier-0,
and product/release files remain read-only.

The sole writable root is this run root. N1 through N6 remain held if N0 does
not prove basis currency, source availability, lifecycle, profile absence,
dependency truth, and write containment.

## Initial inspection

- Deliverable representation: `SOW_V1`.
- Lifecycle: `INITIALIZED`; no prior production activation is recorded.
- Root-local software-workflow profile: absent; project-local profiles are not
  borrowed.
- Deliverable-local declared dependencies: none.
- Runtime/client implementation: expressly excluded in this activation.
- Runtime telemetry: this is a one-deliverable bounded planning activation,
  not a representation-migration batch or adopted long-running activation.
  The collaboration runtime does not expose reliable token/context occupancy;
  that limitation is recorded rather than inferred.

## Read-scope amendment

Plan version 2 adds the read-only paths listed in
`READ_SCOPE_AMENDMENT_1.md`. The parent objective requires an exact recovery
surface and replay-evidence plan, and the original read item 4 cannot locate
the accepted-turn persistence/admission implementation. The amendment changes
no write, implementation, lifecycle, or acceptance authority.
