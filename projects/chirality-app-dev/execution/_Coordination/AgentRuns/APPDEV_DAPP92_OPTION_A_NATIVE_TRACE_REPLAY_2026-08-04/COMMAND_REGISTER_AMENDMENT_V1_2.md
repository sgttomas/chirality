# Command-register amendment v1.2 — corrected snapshot paths and preflight inspection

Status: `FROZEN BEFORE C078 INVOCATION`

C072 proved that the immutable R2 snapshot stores the three test files under
`candidate-source/tests/`, not their product-relative directories. C073–C077
proved all five product additions absent. This amendment supersedes uninvoked
C030–C032 only; every other v1 outcome remains historical.

| ID | Class | State | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C078 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/shasum -a 256 projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/cli-launcher.test.ts projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-helper-packaging.test.ts` | Bind corrected immutable paths to the three expected candidate hashes; stop on mismatch. |
| C079 | temporary product reconstruction/runtime | AUTHORIZED_UNPRIVILEGED | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/cli-launcher.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/cli-launcher.test.ts` | Corrected exact test reconstruction; supersedes C030. |
| C080 | temporary product reconstruction/runtime | AUTHORIZED_UNPRIVILEGED | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-control-ipc.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-control-ipc.test.ts` | Corrected exact test reconstruction; supersedes C031. |
| C081 | temporary product reconstruction/runtime | AUTHORIZED_UNPRIVILEGED | `/bin/cp -p projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/tests/runtime-helper-packaging.test.ts projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-helper-packaging.test.ts` | Corrected exact test reconstruction; supersedes C032. |
| C082 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/grep -n '"test"\|"typecheck"\|"build"\|"desktop:pack"' projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source/package.json` | Bind exact npm script names before invoking them. |
| C083 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/grep -R -n 'CHIRALITY_USER_DATA\|CHIRALITY_RUNTIME\|user-data-dir\|runtime.sock\|runtime.owner' projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_R2_2026-08-02/instances/A2-DAPP88-R2-IMPLEMENT-01/evidence/candidate-source` | Identify only public runtime path selectors; no token/credential patterns or values. |
| C084 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/find projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/instances/A2-DAPP88-R3-DIAGNOSE-02-R2/evidence/arms -type f -maxdepth 3 -print` | Enumerate retained public replay evidence filenames for exact launch/timing reconstruction. |
| C085 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/grep -R -n 'HOME=\|userData\|--runtime-daemon\|--user-data-dir\|daemon_executable\|launch.command\|signal_command' projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP88_HELPER_BUNDLE_RESUME_R3_2026-08-04/instances/A2-DAPP88-R3-DIAGNOSE-02-R2/evidence/arms` | Inspect public command/path evidence only; stop if any output surface would expose a token value. |

After C078 and C082–C085, the manager must issue a v1.3 amendment fixing the
exact dependency, npm working-directory, launch, registration/contact, and PID
capture commands before any reconstruction or runtime invocation.
