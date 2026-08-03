# DRAFT A2 Validation-Remediation Brief — D-APP-89 Option B

Status: `EFFECTIVE — DISPATCH AUTHORIZED`

RequestedBy: App `HELP_HUMAN` through `WORKING_ITEMS`

RunID: `APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02`

ParentInstanceID: `WI-PKG03-DAPP89-B`

ProposedChildInstanceID: existing `TASK-DAPP89-MIGRATION-01`, reactivated

Scope: validation-only remediation of the exact Attempt 01 candidate bytes.

## Dispatch precondition — satisfied by parent

The parent supplied the App dependency environment on 2026-08-02: exact
command `npm ci` completed successfully in
`projects/chirality-app-dev/frontend` from the current lockfile, adding 752
packages and auditing 760. The first sandboxed attempt failed `ENOTFOUND`; the
parent then supplied the successful exact-lockfile materialization. One
high-severity audit finding and allow-scripts notices are advisory evidence
only. Do not run `npm audit fix`, approve scripts, upgrade packages, rewrite
the lockfile, or otherwise modify dependencies.

The materialized frontend `node_modules` is read/execute-only for this node and
must remain present after return because later D-APP-88/D-APP-86 lanes will
consume it. Root checks may use only the dependency resolution naturally
provided by the materialized App tree and existing repository commands; do not
perform a second install or claim a missing Root command passed.

## Frozen candidate identities

- candidate implementation manifest SHA-256:
  `6c49f37dcecf62ef42eeb8d35b99b7df9f6773e1d61c8d8dc7316ea70e02f0c4`;
- candidate implementation return SHA-256:
  `8621e4b658b33eb433cbbc0c941c3d757237267b1c7da659458e94b4056a4ce5`;
- retained facade tree must remain byte-identical to Git base
  `97678a841ef58345c73d3470ed8de57c9b1405d2`;
- DEL-03-01 lifecycle stays `IN_PROGRESS`; Checking Approval SHA stays
  `8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.

## Objective

Obtain passing evidence for every previously blocked D-APP-89 check and
diagnose any genuine failure. If and only if a failure is caused by the
D-APP-89 migration, apply the minimum repair inside the original authorized
implementation paths, record it as Attempt 02 remediation, refresh affected
hashes/manifests/evidence, and rerun the failed check plus the complete required
set. Any unrelated or cross-boundary defect stops this node without repair.

## Proposed transient write boundary

The parent update authorizes read/execute-only use of:

- `projects/chirality-app-dev/frontend/node_modules/**`; do not modify or
  remove it;
- transient build/test/package outputs produced by the exact existing
  commands under the App frontend and Root runtime, to be inventoried; retain
  frontend `node_modules`, and remove other generated state only where doing
  so cannot disturb later concurrently authorized lanes;
- run-local validation evidence under
  `execution/_Coordination/AgentRuns/APPDEV_DAPP89_FACADE_MIGRATION_2026-08-02/**`.

Tracked writes are prohibited except for a minimum migration-caused repair
inside the original implementation brief's exact App frontend source/config/
validator/test targets and corresponding run-local evidence/manifests. The
lockfile, dependency versions, DEL-03-01 lifecycle/Checking Approval SHA,
facade exports, decision/register/receipt/authority/decomposition/foreign-loop
surfaces, and Git state remain unwritable. DEL-03-01 `_STATUS.md`/`MEMORY.md`
may be updated only if needed to truthfully reconcile the final validation
result, without changing lifecycle or the later retirement gate.

## Exact required checks

1. `npm --prefix runtime run build`
2. `npm --prefix runtime run typecheck`
3. focused Root runtime contract export/identity tests
4. App focused `harness-contract-rollback.test.ts`
5. from App frontend: `npm run test`
6. `npm run typecheck`
7. `npm run harness:validate:contract-deps`
8. `npm run build`
9. `npm run desktop:pack`
10. zero-consumer assertion, receipt, corpus, practitioner status/tests,
    self-check, App hold, diff, tracked/untracked containment, manifest hashes,
    lifecycle/Checking Approval SHA, facade tree, and six-UNKNOWN preservation.

All commands must use the repository's exact lockfiles and existing
`--publish never` posture. No additional install, lockfile update, package
drift, audit-fix, scripts approval, network proof, release, publication,
provider, or acceptance claim is permitted.

## Required return

- exact dependency-source identity and materialization commands;
- each command, exit code, and normalized output reference;
- pre/post candidate-manifest verification;
- inventory and verified cleanup of all transient state;
- exact failures, if any, with no weakened acceptance;
- derivative status, remaining reruns/blockers, and next owner.
