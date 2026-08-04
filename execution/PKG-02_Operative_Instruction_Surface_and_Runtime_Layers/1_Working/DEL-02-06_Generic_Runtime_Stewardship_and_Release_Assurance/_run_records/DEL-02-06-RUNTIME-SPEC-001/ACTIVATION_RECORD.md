# DEL-02-06 first activation record — accepted-turn recovery planning

RunID: `DEL-02-06-RUNTIME-SPEC-001`
ParentRunID: `ROOT_FOUR_LANES_2026-08-02`
ManagerNode: `W6` (continuation of W1/W2/W3/W4/W5)
ManagerRole: `WORKING_ITEMS`
PackageID: `PKG-02`
SelectedDeliverables: `DEL-02-06` only
PlanVersion: `6` (parent plan version `12`; executed after plan-v13 current-main synchronization)
Posture: `MIXED`
ActivationState: `PLANNING_PACKAGE_COMPLETE_NOT_ADOPTED — HANDOFF_READY_FOR_HUMAN_GATE`

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

## Continuation amendment

Owner ruling SHA-256
`9b98fe3dc6f8d9abb53c5b087e666cd17d53569ea0f39f1dea489534c9ebf6b6`
authorizes a fresh current-basis packet candidate, preserves exact packet
acceptance, and orders fresh N0 only after the S2 basis repair is applied. The
accepted Scope of Work governs containment: the eventual live packet path is
this RunID root's `accepted_inputs/`. The erroneous deliverable-root path is
not authorized and neither location is written in the blueprint stage.

## W4 regeneration amendment — 2026-08-03

Parent plan 10 releases deterministic candidate regeneration against exact
corrected decomposition SHA-256 `23f6ae0f…64f3d`, fresh audit SHA-256
`ee10313f…20e1`, and Gate-1 confirmation record SHA-256
`05395c30…f40f`. W4 regenerated the exact six-file candidate and produced
CandidateSetManifestSHA256 `360f8f12…d508f`.

The prior W3 manifest `dd007522…53cf` was never accepted and remains stale
derivative history only. W4 does not accept the new packet, create or write
`accepted_inputs/`, dispatch N0, or expand implementation/lifecycle/register/
Git authority.

## W5 acceptance, live copy, and N0 amendment — 2026-08-03

Owner acceptance ruling SHA-256 `7ddbef04…a70f7` accepts exact manifest
`360f8f12…d508f`. The external acceptance record validates with exactly one
matching token. All six files were copied byte-identically into this RunID's
`accepted_inputs/` and revalidated.

Actual child session `/root/w1_del0206/n0_r2_w5` executed fresh N0-R2 under
the sealed two-file write boundary. WORKING_ITEMS accepts its 26/26 PASS,
no-finding return and `RELEASE_N1_N2_N3` recommendation. Parent plan 11
requires the manager to stop after N0, so N1–N6 remain held and undispatched.

## W6 post-N0 planning completion amendment — 2026-08-03

Parent plan 12 released the post-N0 graph after the C4 current-main guard.
W6 ran on repository HEAD `ba576264793deba0708397874414b7482c243f89`,
which contains `origin/main@379b8b19b12b29eda4fa307e497499d6fe414f8a`.
The 172-path synchronization restoration matched its pre-sync snapshot; frozen
W5/N0 evidence and all existing N1-N6 brief hashes reproduced exactly.

Actual bounded children `/root/w1_del0206/n1_w6`, `n2_w6`, and `n3_w6`
executed concurrently with disjoint writes and were manager-accepted. Sole
integration writer `n4_w6` produced seven candidate-only outputs. Fresh
read-only N5 returned one degraded-mode completeness finding; N4 attempt 2
resolved it. Fresh N5-R2 confirmed that resolution and returned one invalid
decision-reference finding; N4 attempt 3 made the exact owner-approved
`D1/D6/D16` to `D1/D6/TBD-016` correction. Fresh N5-R3 then reviewed 18/18
inputs and returned `ADMIT`, zero material findings, zero writes, and zero
repair.

N6 assembled the exact three-file `handoff/` package from accepted returns
only. `OWNER_GATE_HANDOFF.md` is SHA-256 `bf802046…d151`; its one-entry
manifest verifies and is SHA-256 `53d9a007…3770`. The current verdict is
`PLANNING_PACKAGE_COMPLETE_NOT_ADOPTED`; closure is `NOT_CLOSED`. The next
gate is accountable-human semantic review, followed only if accepted by a
separately sealed implementation gate. No implementation, executable test,
profile/check adoption, runtime/client/project write, lifecycle, release,
reliance, Task Management, Git, or foreign-loop effect occurred.

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
