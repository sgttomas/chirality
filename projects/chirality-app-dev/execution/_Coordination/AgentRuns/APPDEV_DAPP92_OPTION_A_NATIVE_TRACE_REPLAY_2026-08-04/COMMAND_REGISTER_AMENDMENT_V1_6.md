# Command-register amendment v1.6 — dependency projection repair discovery

Status: `FROZEN BEFORE C147 INVOCATION`

The first unprivileged preparation attempt stopped at C126 because the copied
dependency tree could not resolve `@chirality/runtime-cli`. C136–C146 then
completed exact rollback: all baseline/lockfile hashes match, additions and
generated/dependency trees are absent, and frontend Git status is empty.

The failure shows the v1.5 three-package projection was narrower than the
accepted R3 substrate. No build/package or GUI/trace command receives credit.
These commands inspect only public package names/projection records before a
repaired attempt.

| ID | Class | State | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C147 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/find projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/instances/A2-DAPP88-R3-DIAGNOSE-02-R2/evidence/source -maxdepth 2 -type f -print` | Enumerate accepted exact-matrix dependency/source records. |
| C148 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/grep -R -n 'node_modules/@chirality\|runtime-cli\|runtime-host\|projection' projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/instances/A2-DAPP88-R3-DIAGNOSE-02-R2/evidence/source projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/instances/A2-DAPP88-R3-IMPLEMENT-02/evidence` | Recover accepted public projection map only. |
| C149 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/find /Users/ryan/dev/chirality/runtime/packages -mindepth 1 -maxdepth 2 -name package.json -print` | Enumerate available Root package manifests. |
| C150 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/grep -R -n '"name": "@chirality/' /Users/ryan/dev/chirality/runtime/packages/*/package.json` | Bind public Root package names to directories. |
| C151 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/find /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules/@chirality -mindepth 1 -maxdepth 1 -print` | Enumerate accepted source dependency entries. |

No reconstruction or dependency target write is authorized until a v1.7
amendment freezes the complete exact projection map.
