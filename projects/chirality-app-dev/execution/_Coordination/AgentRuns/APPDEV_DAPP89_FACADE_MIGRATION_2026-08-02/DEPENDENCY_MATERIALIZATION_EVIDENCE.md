# Parent-provided dependency materialization evidence

Date: `2026-08-02`

Evidence status: `PARENT-PROVIDED ENVIRONMENT EVIDENCE`

The App `HELP_HUMAN` parent reported and authorized the following environment
state for the D-APP-89 validation-remediation node:

1. An initial sandboxed `npm ci` attempt in
   `projects/chirality-app-dev/frontend` failed with `ENOTFOUND`.
2. The exact same `npm ci` command then completed successfully from the
   current `package-lock.json` under the parent-supplied execution route.
3. Result: 752 packages added and 760 packages audited.
4. Output included one high-severity audit finding and allow-scripts notices.
   They are advisories only for this tranche.
5. The parent expressly prohibited `npm audit fix`, scripts approval, package
   upgrade, and any dependency modification beyond the already ruled
   migration.
6. The materialized `frontend/node_modules` is read/execute-only for D-APP-89
   and must remain present because later D-APP-88/D-APP-86 lanes will consume
   it.

Subsequent parent-provided environment evidence:

- After the first Amendment 03 projection was restored, the parent reran the
  exact App full test unsandboxed. Result: 13 suites failed, 4 tests failed,
  1009 passed, and 42 skipped.
- The failures were package-resolution failures for built Root workspace
  packages (`@chirality/runtime-contracts` / `@chirality/runtime-client`)
  because the original `.vite`-only `runtime/node_modules` had been restored.
- This proves the temporary verified projection must remain active through the
  App dependency-backed tests and Desktop pack; it does not identify a
  D-APP-89 source-mapping defect.

Manager observation after the parent update confirmed executable
`frontend/node_modules/.bin/vitest`, `.bin/tsc`, and `.bin/next` exist. This
record is derivative runtime evidence; it is not dependency, release,
security-risk-acceptance, or publication authority.
