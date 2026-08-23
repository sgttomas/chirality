# Coordination notice — Root SCA-004 v3 release-pathway DAG to App

Status: `COORDINATION_ONLY — ROOT_GATE_1_AWAITING_OWNER_ACCEPTANCE`

To: Chirality App-dev loop / SCA-APP-008 owner
From: Root SCOPE_CHANGE / SCA-004 Gate 1
Root basis: `main@6b0c5219b6a2653e2fc491b1d998abcf78fcf776`

## No authority effect

This notice records cross-loop dependencies and expected reciprocation. It is
not App authority, does not amend an App decision/decomposition/contract/SOW,
does not fire a Task Management trigger, does not lift a hold, and grants no
Root write into `projects/chirality-app-dev/**`. SCA-APP-008 adopts, amends, or
declines every App effect under its own instruments.

## Named notice edges

| Edge | Direction | Meaning | Gating |
|---|---|---|---|
| `ROOT_TO_APP_SCA_APP_008_REQUIREMENTS` | Root DEL-02-06 / DEL-04-04 -> App | Root runtime requirements, accepted affected-client classification, and ten-binding state | no — notice only |
| `APP_TO_ROOT_SCA_APP_008_RECIPROCAL` | App SCA-APP-008 -> Root DEL-02-06 | expected App carrier/impact/conformance routing response | no — notice only until separately accepted fan-in |

These edges form a candidate-layer reciprocal SCC with DEL-02-06. Root
proposes `DECOMPOSE`: one-way Root requirements notice, independently governed
App response, and a later G0.5 fan-in criterion. All cycle-participating edges
remain non-gating until that move is recorded in accepted state. A later
`CUT` or `MERGE` proposal would be human-gated.

## App mirror items from G0

SCA-APP-008 is expected to mirror, under App authority:

1. **A3 role parity.** Agent 0/1/2 role entry is always offered for Codex
   sessions. If G-ROLE cannot mechanically prove Agent-2/TASK
   non-delegation, explicit Agent 2/TASK remains offered labelled `role not
   mechanically enforced`; governed-workflow evidence is
   `instruction-asserted`. Hard filesystem/network/process containment is
   unchanged.
2. **A4 restart semantics.** Retirement/crash terminalizes active turns. The
   next action uses `thread/resume` only under canonical-root,
   account-identity, and policy-digest continuity with cwd fixed to the root;
   otherwise a fresh thread. No in-flight re-attach claim.
3. **A7 command network.** Each canonical root has three consented postures:
   no command network by default; ask per destination with routed
   `networkApprovalContext`, visible host/protocol and the caveat that one
   grant may unblock queued requests to the same destination, with
   `acceptForSession` only by explicit user act; or labelled command network
   on via `network_access = true`. OpenAI account/model/turn service endpoints
   remain separately enumerated under K-NET-1.

SCA-APP-008 is also expected to carry the prospective supersession of the
D-APP-74 tranche-scoped multi-child exclusion for the v3 carriers, without
retroactively editing D-APP-74, and to record D-APP-103 as deferred until the
post-SCA per-attempt packet covers both descendant classes once.

## Root runtime items requiring App-side carrier review

- the second purpose-limited daemon-to-supervisor Unix socket under Root/App
  K-CONTROL-1;
- K-ROLE-2 role-posture/effective-config digest without durable model
  assignment;
- Root approval API v2 with attributed request/decision and routed managed
  network prompts;
- closed HarnessEvent v2 with completed/failed/interrupted/cancelled
  terminals;
- `DelegatedHarnessProcessSupervisorPort`,
  `WorkerRetirementCoordinatorPort`, and `HostedEngineConsentPort`;
- two-job launchd install/migration/rollback and the G-HELPER bundle/cadence
  decision;
- root-private app-owned `CODEX_HOME`, account/consent, and restart continuity;
- App-owned conformance and later exact-release rerun.

## Ten held bindings

All remain `HELD_UNAVAILABLE`:

1. `2_source_and_release_identities.source_identity`;
2. `2_source_and_release_identities.release_identity`;
3. `4_conformance_or_migration_evidence.clients[0]` — App;
4. `4_conformance_or_migration_evidence.clients[1]` — Root CLI;
5. `5_root_semantic_and_regression_evidence`;
6. `6_census_relationship_routing_notice_and_findings.notice`;
7. `6_census_relationship_routing_notice_and_findings.tier_0_relationship`;
8. `8_accountable_human_acts.implementation_act`;
9. `8_accountable_human_acts.cutover_act`;
10. `8_accountable_human_acts.release_act`.

This notice is not binding 6's accepted release-fan-in notice and does not
populate any identity.

## Expected reciprocity

SCA-APP-008 is expected to return an App-owned coordination notice naming its
accepted or proposed carriers, the exact Root notice edges it recognizes, the
status of A3/A4/A7 mirrors, the held App conformance binding, and any blockers
or requested Root clarification. The response remains coordination until its
own gates are accepted and Root later accepts its fan-in use.
