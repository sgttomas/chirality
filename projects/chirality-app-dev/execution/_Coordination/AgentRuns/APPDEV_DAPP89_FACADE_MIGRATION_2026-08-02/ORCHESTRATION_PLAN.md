# APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02 — Orchestration Plan

Status: `FROZEN — IMPLEMENTATION DISPATCH AUTHORIZED`

Parent: App `HELP_HUMAN`

Manager: `WORKING_ITEMS`, instance `WI-PKG03-DAPP89-B`

Package: `PKG-03 Runtime Engine Contract and Turn Lifecycle`

Selected deliverable: `DEL-03-01 AgentEnginePort and Engine Conformance Suite`

Accepted basis:

- branch `codex/appdev-planning-gates-20260802` at base HEAD `97678a841ef58345c73d3470ed8de57c9b1405d2`;
- D-APP-89 packet SHA-256 `7dc274ac9d8d081947420c2155954adef9e5f0d2987e8e0913c0b84f8eabb8dc`;
- D-APP-89 ruling SHA-256 `5b651cb41c3e69e59d26d12c32331d4c6918cc77e590e228dd90fbd8d5da0f22`;
- project software profile `projects/chirality-app-dev/software-workflow.json` under `docs/SOFTWARE_WORKFLOW_PROFILE.md`;
- pre-run DEL-03-01 `_STATUS.md` SHA-256 `328dd412f829f1cea44913449fb05df52165dbcd2cf927827dff8bd4bab6270b` and Checking Approval SHA `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.

## Objective

Execute D-APP-89 Option B as one bounded migration-only cycle: move every
executable App importer and App build/config dependency from the deprecated
`@chirality/harness-contract` facade to exact Root-owned
`@chirality/runtime-contracts` root/subpath exports while retaining the facade
intact and tested as a rollback/compatibility package.

## Work graph v1

Posture: `TERMINAL_FAN_OUT_IN`, serialized author then verifier.

Selection authority: exact owner ruling D-APP-89 Option B and the parent
activation brief.

| Node | Agent | Dependency | Write ownership | Required return | Gate |
|---|---|---|---|---|---|
| `A2-IMPL` | one `TASK + software-bounded-implementation` Agent 2 | accepted activation | enumerated App frontend, DEL-03-01 run record/status/memory, and run-local coordination artifacts | migration, census, mapping, manifests, registered-check evidence, rollback and handoff | manager validates write containment and completeness |
| `A2-VERIFY` | one fresh read-only Agent 2 | accepted `A2-IMPL` terminal return | none | independent 100% review of mapping, census, hashes, validation evidence, preservation boundaries, and residual | manager accepts or returns bounded remediation |
| `FAN-IN` | `WORKING_ITEMS` | accepted verifier | manager-owned DEL-03-01 state and run-local synthesis only | package return to App HELP_HUMAN | no false closure; later retirement gate stays open |

No concurrent shared writes are authorized. `A2-VERIFY` is evidence-only and
must not repair implementation outputs.

## Acceptance gates

1. Before and after census classify production, tests, config/scripts,
   lock/workspace, facade rollback, and documentary/historical strings.
2. All executable App reliance uses exact existing Root exports with no
   behavior or public-contract change.
3. The facade remains intact and buildable/testable but is not load-bearing
   for App execution/build.
4. The after census proves zero executable App references outside the retained
   facade and its dedicated rollback tests.
5. Export/subpath mapping is path-complete and invents no Root export.
6. Exact edited-path/rollback manifest and affected-client boundary are
   recorded.
7. D-APP-89 minimum validation is executed without weakening: Root runtime
   build/typecheck and focused contract tests; App full test/typecheck,
   contract-deps, build, and desktop pack; zero-consumer assertion; receipt,
   corpus, practitioner, self-check, diff, and containment checks.
8. DEL-03-01 lifecycle and Checking Approval SHA remain unchanged; six
   D-APP-81 UNKNOWN relations remain untouched.
9. Return records derivative status, hashes, blockers/reruns, and next owner.

## Exclusions

- no facade deletion or compatibility-export removal;
- no DEL-03-01 closure or later retirement ruling;
- no Root/runtime, Piping, PEC, authority-corpus, decomposition, scope-change,
  register, receipt, completion-log, or Git write;
- no generic-runtime, sandbox, identity, version, resume, Bash-capability,
  provider/network, release, distribution, publication, or reliance act;
- no change to the six D-APP-81 `HISTORICAL_RELATION_UNKNOWN` relations.

## Runtime telemetry

The run uses `RUNTIME_EVENTS.jsonl` and `RUNTIME_SUMMARY.json`. The runtime does
not expose per-child token/context occupancy to this manager, so that
measurement limitation will be recorded rather than inferred.
