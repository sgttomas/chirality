# A/B/C Source and Package Dependency Maps

State: `DERIVATIVE COMPARATIVE PROOF — NO VARIANT SELECTED`

Basis: `CURRENT_TREE_SNAPSHOT.md` and `BASIS_MANIFEST.csv`.

## Current graph

```text
package.json / next.config / build-electron
  -> one Next renderer graph
     -> app/layout (global providers)
     -> app/page (route composition)
        -> WovenDialogueRoute
           -> WovenDialogueShell
              -> ShellFrame + Navigator + Pipeline + Workbench + Dialogue
           -> PortalLoopShell (legacy compatibility)
     -> app/api routes
        -> lib/harness + lib/runtime-client + lib/workspace
  -> one Electron graph
     -> electron/main
        -> renderer host + runtime client/host + process/data policy
     -> electron/preload
  -> one electron-builder manifest
     -> one appId/productName/icon/resource set
```

The target architecture must preserve the common Woven authority,
projection, guarded-selection, replay, and accessibility behavior. Product
target configuration must not be confused with the closed runtime-engine
registry in `src/lib/harness/mcp/domain-profile-registry.ts`.

## A — One lightly skinned application graph

```text
product-profile build input
  -> current package/build config
  -> current Electron main/preload
  -> current app/layout provider stack
  -> current app/page + Woven route
  -> current Woven/Shell graph
       -> profile-selected copy/resources/navigation/default surface
       -> bounded target slots
  -> distinct artifact output parameters
```

Shared implementation remains in place. Static review identified this
nine-path lower-bound product/profile seam set `P`:

1. `frontend/package.json`;
2. `frontend/next.config.mjs`;
3. `frontend/electron/main.ts`;
4. `frontend/src/app/layout.tsx`;
5. `frontend/src/app/globals.css`;
6. `frontend/src/app/icon.svg`;
7. `frontend/src/components/shell/shell-frame.tsx`;
8. `frontend/src/components/woven-dialogue/navigator.tsx`; and
9. `frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx`.

Three additional governing seams require explicit audit but need not become
target-aware modules: `frontend/scripts/build-electron.mjs`,
`frontend/src/app/page.tsx`, and
`frontend/src/components/woven-dialogue/woven-dialogue-route.tsx`.

`P` is a lower-bound integration census, not permission for nine arbitrary
conditionals. A later mock must declare its exact allowlist and achieve zero
target-aware files outside it. A's primary failure mode is target conditionals
leaking beyond that boundary or a target slot importing arbitrary App internals.

## B — Shared core with target-specific shells

```text
internal shared packages
  ui-core
    -> Woven components + shell primitives + accessibility behavior
  app-state-core
    -> workspace providers + Woven/shell/workspace libraries
  app-client-core
    -> runtime-client + governed harness/API adapters
  validation-core
    -> shared conformance fixtures

apps/desktop-shell                 apps/domain-piping-shell
  -> own Next route/layout           -> own Next route/layout
  -> own navigation composition      -> own domain navigation composition
  -> own Electron process entry      -> own Electron process entry
  -> own package manifest/resources  -> own package manifest/resources
           \                         /
            -> import only shared package public APIs
```

Candidate extraction census, measured as current immediate directory members:

| Shared-package candidate surface | Current files |
|---|---:|
| `src/components/woven-dialogue` | 9 |
| `src/components/shell` | 23 |
| `src/components/workspace` | 4 |
| `src/components/pipeline` | 1 |
| `src/components/workbench` | 1 |
| `src/lib/woven-dialogue` | 6 |
| `src/lib/shell` | 8 |
| `src/lib/workspace` | 6 |
| `src/lib/pipeline` | 1 |
| `src/lib/runtime-client` | 2 |
| **Candidate extraction census** | **61** |

The 61-file census is a boundary-review population, not a claim that all 61
must move. B succeeds only if target shells compose common behavior through
public shared APIs without copying Woven authority/accessibility logic.

## C — Build-time product profiles over a shared shell

```text
immutable product manifest (targetId fixed at build)
  -> schema validation + generated typed profile
  -> bounded adapter registry
       -> identity/resources adapter
       -> navigation/default-surface adapter
       -> typed-agent/info/workflow/gate slots
  -> current shared app/layout + Woven shell
  -> current Electron main/preload via generated build constants
  -> two separately validated immutable artifact outputs
```

C permits target awareness in three new boundary modules only:

1. manifest loader/generated profile;
2. bounded slot/adapter registry; and
3. build/package profile resolver.

Current shell, Woven, workspace, client, and harness internals may consume
typed boundary values or slot interfaces but must not branch on raw target IDs
or import target adapters. Runtime skin switching is excluded.

## Fixed common dependencies

All variants preserve these directions:

- target composition may depend on shared Woven/shell/client contracts;
- shared modules may not depend on a target implementation;
- product profile does not grant runtime-engine registration;
- App clients may consume Root-owned contracts but cannot define generic
  runtime, sandbox, identity, version, resume, or Bash semantics; and
- the absent D-APP-88 helper is not a second product target and is not reused
  as domain-shell packaging authority.
