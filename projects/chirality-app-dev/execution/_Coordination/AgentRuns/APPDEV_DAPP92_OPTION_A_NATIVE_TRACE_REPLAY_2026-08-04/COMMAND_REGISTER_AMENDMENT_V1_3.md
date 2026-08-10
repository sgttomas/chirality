# Command-register amendment v1.3 — dependency/runtime discovery

Status: `FROZEN BEFORE C086 INVOCATION`

C078 reproduced all three corrected candidate test hashes. C082 confirmed
`test`, `typecheck`, `build`, and `desktop:pack` scripts. C083 confirmed
`CHIRALITY_USER_DATA` as the public isolated-state selector. C084–C085 bound
the prior public launch-evidence form without reading token values.

| ID | Class | State | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C086 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/which node` | Bind Node executable path. |
| C087 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/which npm` | Bind npm executable path. |
| C088 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/opt/homebrew/bin/node --version` | Bind Node version; stop if the discovered path differs. |
| C089 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/opt/homebrew/bin/npm --version` | Bind npm version; stop if the discovered path differs. |
| C090 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/bin/test -d /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/node_modules` | Prove accepted dependency source exists. |
| C091 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/bin/test ! -e projects/chirality-app-dev/frontend/node_modules` | Prove worktree dependency target absent before copy. |
| C092 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/usr/bin/shasum -a 256 /Users/ryan/dev/chirality/projects/chirality-app-dev/frontend/package-lock.json projects/chirality-app-dev/frontend/package-lock.json` | Prove source/target lockfile identity before dependency projection. |
| C093 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/bin/test -d /Users/ryan/dev/chirality/runtime/packages/contracts -a -d /Users/ryan/dev/chirality/runtime/packages/policy -a -d /Users/ryan/dev/chirality/runtime/packages/daemon` | Prove exact Root projection sources exist. |

After C086–C093 pass, v1.4 freezes the corrected reconstruction, dependency,
preflight, build, package-manifest, rollback, and cleanup commands. No runtime
launch or special-authority command is released by this amendment.
