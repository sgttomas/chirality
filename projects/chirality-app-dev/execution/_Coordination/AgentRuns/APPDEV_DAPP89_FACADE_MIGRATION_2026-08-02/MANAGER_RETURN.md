# WORKING_ITEMS Manager Return — D-APP-89 Option B

RunID: `APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02`

InstanceID: `WI-PKG03-DAPP89-B`

Package: `PKG-03 Runtime Engine Contract and Turn Lifecycle`

Selected deliverable: `DEL-03-01 AgentEnginePort and Engine Conformance Suite`

Status: `PASS — MIGRATION-ONLY TRANCHE ACCEPTED FOR APP HELP_HUMAN FAN-IN`

## Accepted basis

- base HEAD `97678a841ef58345c73d3470ed8de57c9b1405d2` on
  `codex/appdev-planning-gates-20260802` plus the preserved planning/ruling
  tranche;
- D-APP-89 packet SHA-256
  `7dc274ac9d8d081947420c2155954adef9e5f0d2987e8e0913c0b84f8eabb8dc`;
- D-APP-89 Option B ruling SHA-256
  `5b651cb41c3e69e59d26d12c32331d4c6918cc77e590e228dd90fbd8d5da0f22`;
- project software profile under `docs/SOFTWARE_WORKFLOW_PROFILE.md`.

## Work graph and accepted child returns

The serialized graph completed as:

`TASK implementation Attempt 01 candidate → held dependency gate → same TASK validation Attempt 02 → fresh read-only verifier → manager fan-in`.

Accepted returns:

| Return | Disposition | SHA-256 |
|---|---|---|
| `A2_IMPLEMENTATION_RETURN.md` | preserved Attempt 01 candidate/failure history; not final fan-in | `8621e4b658b33eb433cbbc0c941c3d757237267b1c7da659458e94b4056a4ce5` |
| `A2_IMPLEMENTATION_RETURN_ATTEMPT02.md` | accepted implementation plus complete validation | `24c37ac9babef12766925efe616b2cc408f26678b0afad691df0142df9a1234c` |
| `A2_VERIFIER_RETURN.md` | fresh read-only `PASS / ACCEPT_FAN_IN` | `fcb647bad6447a3a3484f7bb721b44f73e6cbe5fe14a95f000953147e893fd97` |

The manager independently recalculated the 114-file manifest, hashes,
zero-consumer counts, facade/base diff, Root diff, validator result, lifecycle,
Checking Approval SHA, and diff check before releasing the verifier.

## Accepted implementation

- 67 production and 39 ordinary test files moved by one-for-one import
  specifier replacement from `@chirality/harness-contract` to exact
  `@chirality/runtime-contracts` root/subpaths.
- Root App facade dependency, root lock dependency, two TypeScript aliases,
  and Next facade transpile target were removed/migrated.
- The facade remains intact with all 13 code exports and is no longer
  load-bearing for App execution/build.
- A dedicated rollback identity test probes all 13 facade/Root export
  identities.
- The strengthened dependency validator makes zero ordinary consumer and
  config/build reliance reproducible.
- Fresh implementation manifest SHA-256:
  `353977870953eef45a1366cb6bc039560a56605aac7d3a8436c5b3f38f411d4c`,
  verified 114/114 by author, manager, and independent verifier.

## Census and mapping

- Base: 67 production files / 118 occurrences; 39 ordinary test files / 58
  occurrences; 106 files / 176 source occurrences total.
- After: 0 ordinary executable facade occurrences; exactly 13 dedicated
  rollback probes.
- Retained strings are limited to facade/workspace rollback identity, two
  workspace lock strings, validator negative assertions, one historical
  script comment, and enumerated documentary/history evidence.
- All 11 used and all 13 retained facade code exports have exact existing Root
  counterparts; no Root export was invented.

## Validation accepted

- Root build and typecheck: PASS.
- Root focused contract suite: 8/8 PASS.
- App rollback identity suite: 13/13 PASS.
- App full suite: 1,111 passed / 4 skipped; 142 files passed / 1 skipped.
- App typecheck and contract-dependency validator: PASS.
- App production/Electron/runtime CLI build: PASS.
- App Desktop pack: PASS with existing `--publish never`; packaged dependency
  boundary PASS; instruction-root integrity PASS over 43 files.
- Receipt, corpus v18 8/8, practitioner status, self-check, App hold,
  practitioner pytest 349, diff, containment, lifecycle/approval, facade,
  Root-diff, and six-UNKNOWN guards: PASS.
- Standing-check evidence SHA-256:
  `336c31df31a174f8d6b71a2df5e683341361e0a8e40c096f86134d3e36d9f2f2`.

Attempt 01 missing-binary failures, the parent post-restoration resolution
failure, sandbox `listen EPERM`, and Desktop-pack `ENOTFOUND` remain preserved
as environment history. The complete Amendment 04 run passed without weakening
any check or changing product source.

## Validation environment and restoration

The parent materialized the App dependency tree by exact-current-lockfile
`npm ci`; initial sandbox `ENOTFOUND`, successful 752-package/760-audit result,
one high-severity audit advisory, and allow-scripts notices are recorded in
`DEPENDENCY_MATERIALIZATION_EVIDENCE.md` at SHA-256
`fe0fc6241725ac292ce8c676db0833b95aabacf40915e058ad6c9950890f4aea`.
No audit fix, scripts approval, upgrade, or dependency edit occurred.

The temporary Root dependency projection was identity-gated, removed after
the complete pass set, and the original `.vite`-only real
`runtime/node_modules` directory restored with exact inode/metadata/tree/link
identity. Backup is absent and Root tracked diff is zero. Parent-directed App
dependency and ignored build/package outputs remain for later D-APP-88/86
lanes and are derivative only.

## Deliverable effects and residual

- DEL-03-01 remains `IN_PROGRESS`.
- Checking Approval SHA remains
  `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.
- Dependency files and dispositions are unchanged.
- `_STATUS.md` and `MEMORY.md` record Attempt 01 and the superseding complete
  Attempt 02 evidence.
- Remaining now truthfully states the only D-APP-89 residual: land the
  migration, repeat a fresh landed-tree zero-consumer census, and obtain the
  later D-APP-76 owner ruling before facade retirement.

No DEL-03-01 closure, retirement readiness/selection, lifecycle transition,
release, publication, distribution, professional reliance, Root/Piping/PEC
consumer claim, or D-APP-48 successor-identity act is made.

## Notices, waivers, blockers, reruns

- Cross-package notices: none; no foreign-loop action was requested or taken.
- Waivers: none.
- D-APP-89 migration blockers: none.
- Required migration reruns: none before Git fan-in; normal PR/CI checks remain
  the Git gate.
- Advisory only: instruction-root integrity passes, while its independent
  source-completeness field remains `needs_remediation`; not caused or changed
  by this migration.

## Preservation and derivative status

No PRD/authority corpus, decomposition, scope change, Task Management,
receipt, completion log, decision register, Root source, Piping, PEC, or Git
surface belongs to this tranche. The six D-APP-81
`HISTORICAL_RELATION_UNKNOWN` relations remain untouched.

All run-local census, mapping, manifests, validation, telemetry, and return
artifacts are derivative evidence of D-APP-89 and live source. They do not
replace decomposition truth or constitute owner acceptance.

Runtime telemetry is bound at `RUNTIME_EVENTS.jsonl` and
`RUNTIME_SUMMARY.json`; native child token/context occupancy was unavailable
and is recorded as a measurement limitation.

## Requested App HELP_HUMAN action

Accept this WORKING_ITEMS fan-in into the wider D-APP-86..89 session tranche
and route ordinary Git closeout through CHANGE when the full session is ready.
Do not retire the facade or close DEL-03-01/TM-APP-031 in this act.
