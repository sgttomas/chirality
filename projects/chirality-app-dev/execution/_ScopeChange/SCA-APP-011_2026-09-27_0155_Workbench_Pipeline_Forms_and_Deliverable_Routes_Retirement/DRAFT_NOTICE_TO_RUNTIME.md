# DRAFT — Informational notice to the Runtime loop: the App no longer calls the Runtime scaffold API

**Status:** DRAFT for checkpoint group 2. It is sent only after checkpoint group 3
of SCA-APP-011 is accepted. At that point it is copied, without the draft
header, to `projects/chirality-runtime/execution/_Coordination/NOTICE_{APPLICATION_DATE}_APP_SCA-APP-011_SCAFFOLD_API.md`.
Runtime keeps its inbound notices at `execution/_Coordination/NOTICE_*.md`.
**From:** App loop, SCA-APP-011 (owner Ryan Tufts, direction and acceptance 2026-09-27)
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
- The App still uses the `deps_read`, `status_transition` and `deps_write`
  descriptors. SCA-APP-011 also retires the App's three deliverable HTTP
  routes, which Runtime never called.

## Decision left to the Runtime loop

Whether to keep, deprecate or remove its scaffold API and types is the
Runtime loop's decision. The App amendment does not change Runtime scope.
