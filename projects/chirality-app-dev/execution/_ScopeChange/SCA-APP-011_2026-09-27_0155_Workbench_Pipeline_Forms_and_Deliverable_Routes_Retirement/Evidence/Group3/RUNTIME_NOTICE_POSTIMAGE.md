# Informational notice to the Runtime loop: the App no longer calls the Runtime scaffold API

**From:** App loop, SCA-APP-011 (owner Ryan Tufts; direction 2026-09-27; checkpoint group 3 accepted on {APPLICATION_DATE}, `projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_{APPLICATION_DATE}/`)
**Kind:** informational. It asks for no action and grants nothing.

## What changed in the App

SCA-APP-011 retires the App HTTP route `POST /api/harness/scaffold`, the client
function `scaffoldHarnessExecutionRoot` (`frontend/src/lib/harness/client.ts`),
and the App-side `scaffold` member of `DaemonHarnessPort` /
`RuntimeDaemonHarnessPort` (`frontend/src/lib/runtime-client/`). The App scaffold
library (`frontend/src/lib/harness/scaffold.ts`) stays. Execution roots are
scaffolded through the Root `project-setup` workflow and the packaged
`tools/scaffolding` scripts.

## What this means for Runtime

- The App was the only client of the Runtime scaffold API:
  - `RUNTIME_ROUTES.scaffold` (`/v1/projects/{id}/scaffold`);
  - `RuntimeClient.scaffold`;
  - the daemon handler;
  - `RuntimeService.scaffold` and `ProjectScaffoldPort`;
  - `ScaffoldRequest` / `ScaffoldResponse`.

  After this change nothing in the repository calls that API.
- No `ProjectScaffoldPort` is composed in any Runtime composition. The
  production composition (`packages/daemon/src/app-owned-composition.ts`)
  passes `undefined`, so the API answered `ENGINE_UNAVAILABLE` (501). App
  Task Management row APP-R058 tracked this gap. The App closes it by
  removing its route.
- The shared types `ScaffoldExecutionRootRequest/Response`
  (`packages/contracts/src/harness/types.ts`) are no longer used by the App.
- The `scaffold_preview` tool descriptor is unchanged. The App's retained
  `scaffold_preview` implementation is unchanged.
- The `status_read`, `deps_read`, `status_transition` and `deps_write`
  descriptors are unchanged. The App uses them only on its retained SDK path
  (`frontend/src/lib/harness/mcp/read-tools.ts`); none is registered on the
  live Codex path. Live exposure of the read tools is the App's DEL-06-03 open
  work, and any live registration of `status_transition` or `deps_write` is
  governed by the App's DEL-06-04-REQ-010. SCA-APP-011 also retires the App's
  three deliverable HTTP routes, which Runtime never called.

## Decision left to the Runtime loop

Whether to keep, deprecate or remove its scaffold API and types is the
Runtime loop's decision. The App amendment does not change Runtime scope.
