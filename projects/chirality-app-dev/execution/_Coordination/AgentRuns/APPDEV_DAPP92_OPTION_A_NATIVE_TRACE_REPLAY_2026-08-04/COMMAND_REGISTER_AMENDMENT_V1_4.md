# Command-register amendment v1.4 — corrected Node path

Status: `FROZEN BEFORE C094 INVOCATION`

C086–C087 discovered Node/npm under the exact mise Node-24 installation, not
`/opt/homebrew`. C088–C089 failed without executing Node/npm because their
enumerated paths were absent. C090–C093 otherwise passed: dependency source
exists, target is absent, source/target lockfiles both match SHA-256
`5c8fce2a3c0e2e7b55730ac673ccb07424dcae1e4bbbb408260b1090040c1a56`,
and all three Root projection sources exist.

| ID | Class | State | Exact tool/command | Purpose / stop condition |
|---|---|---|---|---|
| C094 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/Users/ryan/.local/share/mise/installs/node/24/bin/node --version` | Bind actual Node version. |
| C095 | read-only/unprivileged | AUTHORIZED_UNPRIVILEGED | `/Users/ryan/.local/share/mise/installs/node/24/bin/npm --version` | Bind actual npm version. |

No reconstruction/build/runtime command is released until C094–C095 pass and
v1.5 freezes commands with the corrected absolute tool paths.
