# Agent 2 Return — Source, Dependency, and Measurement Review

Reviewer construction: bounded ephemeral Agent 2 generalist

Parent: `HELPS_HUMANS`
Result: `PASS WITH EXPLICIT PLANNING UNCERTAINTY — NO A/B/C SELECTION`

## 1. Scope and evidence calibration

I inspected the current App frontend tree read-only under the sealed brief. The
architecture maps, schemas, and costs below are derivative planning evidence,
not product requirements, package authority, runtime semantics, or an
implementation decision.

Evidence basis:

- `D-APP-90_PACKET_DUAL_TARGET_ARCHITECTURE_POSTURE_2026-08-03.md`, preserved
  proposal SHA-256
  `eda5303254f5d1fdf624bf49c1f6652735235f7ee59e899af6f284107d7b3c57`;
- `D-APP-90_RULING_BOUNDED_COMPARATIVE_ARCHITECTURE_PROOF_2026-08-03.md`;
- this run's `ACTIVATION.md` and `WORK_GRAPH.md`;
- prior derivative re-plan
  `APPDEV_DAPP87_DUAL_TARGET_REPLAN_2026-08-03/ARCHITECTURE_ALTERNATIVES.md`;
- repository `HEAD` and `origin/main` both observed at
  `7249281e1f84ba5abee3c31c2fea3736b22000d3`; and
- current working-tree frontend bytes. Those bytes included concurrent,
  unstaged D-APP-89-related changes, so the filesystem measurement is bound to
  the fingerprint below and must not be mistaken for a committed snapshot.

The measured source/config corpus is the 185 files selected by the command in
section 5. Its ordered `(file SHA-256, path)` digest was:

`ad262802ab4dfd98475121a06eae49e76d461d71b172e860459e3be775392aa4`

The contemporaneous `git status --porcelain -- frontend` digest was:

`000738ad4b88597c0dc0c5639fd74071c6219d3e530f1dda437f64fa57bdb3c9`

## 2. Current entry points and composition seams

### Executable and package entry

- `frontend/package.json` declares one workspace, one Electron entry
  (`dist-electron/main.js`), one `appId` (`com.chirality.app`), one
  `productName` (`Chirality`), and one macOS DMG target.
- `frontend/electron/main.ts` starts one packaged Next server
  (`startPackagedRendererServer`, lines 447-493), creates one renderer window
  (`createMainWindow`, lines 501-523), and loads one renderer URL.
- `frontend/next.config.mjs` contains one Next configuration and no target
  selector.
- `frontend/packages/harness-contract/package.json` is the only internal
  package root under `frontend/packages/`; it is explicitly a deprecated
  compatibility facade, not a UI/core/shell package boundary.

### Renderer entry and shared composition

- `frontend/src/app/layout.tsx` is the global composition root. It owns product
  metadata, local fonts/theme bootstrap, and the single provider chain:
  `RuntimeConnectivityProvider -> WorkspaceProvider -> DeliverablesProvider ->
  ToolkitProvider -> HarnessEventsProvider`.
- Six UI route/client entry files exist:
  `src/app/page.tsx`, `src/app/chat/page.tsx`,
  `src/app/pipeline/page.tsx`, `src/app/pipeline/pipeline-client.tsx`,
  `src/app/workbench/page.tsx`, and
  `src/app/workbench/workbench-client.tsx`. There are also 18 API
  `route.ts` files under `src/app/api/`.
- All four visible route families (`/`, `/chat`, `/pipeline`, `/workbench`)
  converge on
  `src/components/woven-dialogue/woven-dialogue-route.tsx`. That seam selects
  the common `WovenDialogueShell` or an existing `legacy=1` compatibility
  composition; it is not a product-target selector.
- `src/components/woven-dialogue/woven-dialogue-shell.tsx` is the primary
  common composition seam. It mounts `ShellFrame`, `ChatPanel`,
  `PipelineSurface`, `WorkbenchSurface`, `Navigator`, `CoordinationPanel`, and
  `ActivityShelf` and consumes shared workspace, harness, connectivity, and
  recorded-agent/session libraries.
- `src/components/shell/shell-frame.tsx` owns the common top-level navigation,
  title/subtitle, workspace state, settings, connectivity presentation, and
  theme control. The legacy shells
  `portal-loop-shell.tsx`, `loop-shell.tsx`, and
  `loop-tertiary-shell.tsx` also converge on it.
- `src/components/shell/tertiary-sidebar-tabs.tsx` composes the shared
  Pipeline and Workbench surfaces. Thus merely forking route files without an
  extraction rule would not isolate target composition.

Current non-test TypeScript/TSX counts are 26 `src/app` files, 41 component
files, 88 library files, and 13 Electron files: 168 files total. The one
internal compatibility package contributes 13 more TypeScript files; the four
root configs make the measured corpus 185. Within components, the largest
composition families are `shell/` (23 files), `woven-dialogue/` (9), and
`workspace/` (4). Exact selector search found **0** files containing any of
`CHIRALITY_PRODUCT_TARGET`, `productProfile`, `product_profile`,
`targetProfile`, or `target_profile`. This is evidence of no existing product
target contract, not evidence that target concerns are absent.

## 3. A/B/C dependency maps

These maps preserve the fixed two targets and the domain-first requirement.
They deliberately do not choose one.

### A — One lightly skinned application graph

```text
target build invocation
  -> candidate product profile (standalone | first-domain)
  -> existing package/Next/Electron graph
  -> RootLayout provider chain
  -> existing route entries
  -> WovenDialogueRoute
  -> WovenDialogueShell + ShellFrame
  -> shared Pipeline / Workbench / Dialogue / Workspace / Harness clients
```

The profile may supply data to named presentation points, but every target
still traverses the same module graph. The minimum existing target-sensitive
set is the nine-file set `P` in section 5. Any target import or conditional
outside the ruled profile boundary is leakage. Runtime switching would change
the variant and is excluded by the packet.

### B — Shared core plus target-specific shells

```text
standalone package root                    first-domain package root
  -> standalone layout/routes/Electron      -> domain layout/routes/Electron
  -> standalone identity/resources           -> domain identity/resources
             \                                  /
              -> extracted shared UI/client core
                   -> Woven Dialogue contracts/components
                   -> workspace/providers and common shell primitives
                   -> Pipeline + Workbench surfaces/libraries
                   -> App runtime-client/harness adapters
```

Candidate extraction seams, without moving anything now:

1. **Shared Woven core:** `src/components/woven-dialogue/**` (9 files) plus
   `src/lib/woven-dialogue/**` (6 files).
2. **Shared workspace/surface core:** `src/components/workspace/**` (4),
   `src/lib/workspace/**` (6), `src/components/pipeline/**` (1),
   `src/lib/pipeline/**` (1), `src/components/workbench/**` (1), and common
   settings components (2).
3. **Shared shell primitives:** reusable files under `src/components/shell/**`,
   but not target navigation/identity composition. `shell-frame.tsx` must be
   split into a target-owned frame wrapper and common frame primitives rather
   than copied wholesale.
4. **Target shell roots:** independent layout/route composition, Electron
   entry, resources, and package manifest for standalone and first-domain.
5. **Shared App client boundary:** existing `src/lib/runtime-client/**` and
   applicable harness/client modules remain App affected-client code; this map
   does not define generic runtime behavior.

The 20-file `P union R` set in section 5 is the lower-bound existing seam
audit for B. It is not a claim that all other files move unchanged: the exact
first-domain UI delta may enlarge it.

### C — Build-time profiles over one shared shell

```text
immutable target build input
  -> validated product manifest
  -> generated selected-profile module + allowlisted target adapter modules
  -> existing package/Next/Electron graph
  -> RootLayout -> WovenDialogueShell -> named slots only
  -> two separately packaged artifacts
```

C differs from A by admitting no runtime target choice: a build selects one
manifest and one allowlisted adapter set, and the output must contain no
opposite-target resources or adapter imports. It differs from B because route
and shell composition remains shared. The minimum existing integration set is
again `P`; adapter imports from arbitrary App internals, or adapter ownership
of route-level state, would invalidate C's boundary.

## 4. Candidate schema and extraction fields

These are candidate field names for the later proof/packet, not accepted
product or packaging values.

### Common A/C product profile

- `schemaVersion`, `targetId`, `targetKind` (`standalone` or `domain`), and
  `domainProfileRef` (nullable for standalone);
- `displayName`, `shortName`, `boundaryCopy`, `iconResourceRef`,
  `themeTokenRef`, and `helpResourceRefs`;
- `defaultSurface`, `routeAllowlist`, and ordered `navigationItems`;
- named `typedAgentView`, `structuredInformationView`, `workflowView`, and
  `decisionGateView` descriptors, each with evidence/source reference fields;
- unavailable/stale/conflict/empty/permission-denied presentation policies;
- candidate packaging placeholders `bundleId`, `productName`,
  `executableName`, `artifactName`, and `resourceManifestRef`;
- `dataNamespacePolicyRef`, `sessionCompatibilityPolicyRef`, and
  `validationProfileRef`; and
- explicit `capabilityNonGrant` and `runtimeContractNonSelection` guards.

### Additional C-only slot/build fields

- `buildTarget`, `manifestSha256`, `adapterModuleAllowlist`, and
  `oppositeTargetDenylist`;
- bounded slots `brand`, `navigation`, `typedAgents`, `structuredInformation`,
  `workflow`, `decisionGates`, and `help`;
- per-slot `moduleRef`, `inputSchemaRef`, `outputSchemaRef`, and
  `allowedSharedImports`; and
- `graduationToSeparateShellReasons`, recording evidence that would force a
  later B decision rather than allowing adapter sprawl.

### B extraction contract fields

- `sharedModule`, `publicExports`, `forbiddenTargetImports`, and
  `stateOwnership`;
- `standaloneShellConsumer` and `domainShellConsumer`;
- `compatibilityRouteOwner`, `accessibilityEvidenceOwner`, and
  `targetParityEvidenceRefs`;
- `resourceOwner`, `packageManifestOwner`, and `data/sessionPolicyRef`; and
- `extractionBackcheck`, `duplicateCompositionCheck`, and
  `crossShellDependencyCheck`.

No field grants tools, Agent-2 Bash, generic runtime semantics, or packaging
identity authority.

## 5. Reproducible comparative measurements

### 5.1 Exact current-tree commands

Run from repository root:

```sh
find projects/chirality-app-dev/frontend/src/app \
  projects/chirality-app-dev/frontend/src/components \
  projects/chirality-app-dev/frontend/src/lib \
  projects/chirality-app-dev/frontend/electron \
  projects/chirality-app-dev/frontend/packages/harness-contract/src \
  -type f \( -name '*.ts' -o -name '*.tsx' \) | sort | wc -l

find projects/chirality-app-dev/frontend/src/app -type f \
  \( -name 'page.tsx' -o -name '*-client.tsx' \) | wc -l

find projects/chirality-app-dev/frontend/src/app/api -type f \
  -name 'route.ts' | wc -l

rg -l 'CHIRALITY_PRODUCT_TARGET|productProfile|product_profile|targetProfile|target_profile' \
  projects/chirality-app-dev/frontend/src \
  projects/chirality-app-dev/frontend/electron \
  projects/chirality-app-dev/frontend/packages \
  projects/chirality-app-dev/frontend/package.json \
  projects/chirality-app-dev/frontend/next.config.mjs \
  -g '*.ts' -g '*.tsx' -g '*.json' -g '*.mjs' | wc -l
```

Observed results: 181 TypeScript/TSX files before the four root configs; six UI
route/client entries; 18 API routes; zero exact architecture-selector files.

To reproduce the 185-file content fingerprint, append the four config paths
(`package.json`, `next.config.mjs`, `tsconfig.json`,
`tsconfig.electron.json`) to the sorted TypeScript/TSX path stream, run
`xargs shasum -a 256`, then hash that ordered output again with
`shasum -a 256`.

### 5.2 Declared lower-bound seam sets

`P` (identity/build/profile-sensitive, 9 existing files):

1. `frontend/package.json`
2. `frontend/next.config.mjs`
3. `frontend/electron/main.ts`
4. `frontend/src/app/layout.tsx`
5. `frontend/src/app/globals.css`
6. `frontend/src/app/icon.svg`
7. `frontend/src/components/shell/shell-frame.tsx`
8. `frontend/src/components/woven-dialogue/navigator.tsx`
9. `frontend/src/components/woven-dialogue/woven-dialogue-shell.tsx`

`R` (route/full-shell composition, 11 additional existing files):

1. `frontend/src/app/page.tsx`
2. `frontend/src/app/chat/page.tsx`
3. `frontend/src/app/pipeline/page.tsx`
4. `frontend/src/app/pipeline/pipeline-client.tsx`
5. `frontend/src/app/workbench/page.tsx`
6. `frontend/src/app/workbench/workbench-client.tsx`
7. `frontend/src/components/woven-dialogue/woven-dialogue-route.tsx`
8. `frontend/src/components/shell/portal-loop-shell.tsx`
9. `frontend/src/components/shell/loop-shell.tsx`
10. `frontend/src/components/shell/loop-tertiary-shell.tsx`
11. `frontend/src/components/shell/tertiary-sidebar-tabs.tsx`

These sets are auditable lower bounds. A and C begin at `P=9`; B begins at
`P union R=20`. The held first-domain UI input is an explicit unknown `U`, so
all migration totals are `lower bound + U`, never final estimates.

### 5.3 Target leakage

Current actual selector count is zero because no target contract exists.
For a run-local prototype define:

`TL = count(unique target-aware source files outside the variant allowlist)`

- A allowlist: the ruled profile loader and the nine `P` seams; every
  target-conditioned file outside it is leakage.
- B allowlist: target-specific shell roots only; any shared-core import of a
  target shell/profile is leakage.
- C allowlist: generated selected-profile binding and named target adapters;
  any target conditional in shared shell code, or adapter import outside the
  public allowlist, is leakage.

Required pass value is `TL=0` for all variants. Also report
`TA = count(unique target-aware shared files)` as exposure: A may intentionally
have nonzero `TA` within `P`; B's target is zero; C's target is one generated
binding, with adapters excluded because they are target-owned. This is a
budget/test, not a measured implementation result.

### 5.4 Duplicate composition

Define:

`DC = count(target-owned route/shell files whose normalized component/import tree is equivalent across both targets)`

The current one-target baseline is `DC=0`. A and C plan one shared shell, so
their intended `DC=0`. B must measure this after a run-local extraction mock.
The seven route-entry files in `R` (six route/client entries plus
`woven-dialogue-route.tsx`) are the first duplicate-risk audit set; the four
legacy shell-composition files are the second. A naive full fork therefore has
11 exact candidate duplicate sites. The proposed B extraction avoids counting
thin target entry wrappers as duplicates only when their imports/configuration
actually differ and all equivalent bodies remain in the shared core.

### 5.5 Build matrix

Use four logical evidence stages per target: TypeScript/source contract,
renderer production build, Electron compile/package, and packaged launch/smoke.

`BM = targets (2) * logical stages (4) = 8 target-specific cells`

All variants have eight mandatory cells; shared tests may be additional common
evidence but cannot subtract a target cell. A and C execute one application
graph under two immutable configurations; B executes two shell graphs. Report
wall time and artifact bytes per cell only after run-local prototypes exist.
The present scripts expose one product path (`build`, `desktop:pack`, and
`desktop:dist`), so they do not yet satisfy the eight-cell matrix.

### 5.6 Migration-cost vector and transparent index

Use the vector `(E,N,Pkg,DeltaBM)`:

- `E`: existing seam files in the lower-bound map;
- `N`: new conceptual schema/profile/config nodes enumerated by the map;
- `Pkg`: new package roots; and
- `DeltaBM`: target-specific logical build cells beyond the present
  one-target four-cell baseline (`8-4=4`).

For cross-option sorting only, define the transparent structural index:

`MCI = E + N + 3*Pkg + DeltaBM`

The factor 3 makes a new package root account for its manifest, public
boundary, and independent consumer validation. It is not an hours estimate.

| Variant | E | N | Pkg | DeltaBM | MCI lower bound | Composition basis |
|---|---:|---:|---:|---:|---:|---|
| A | 9 | 5 | 0 | 4 | 18 + U | schema + two profiles + two packaging overrides |
| B | 20 | 4 | 3 | 4 | 37 + U | workspace/config changes plus shared, standalone, and domain roots |
| C | 9 | 9 | 0 | 4 | 22 + U | schema, two manifests, generated binding, slot contract, two adapters, two packaging overrides |

The ordering is a map-derived planning signal only. It does not incorporate
the unknown first-domain UI delta, LOC changed, build duration, package size,
or long-term conditional growth and therefore cannot select A, B, or C.

## 6. Uncertainty and elimination-test recommendations

1. **Sequenced input:** the exact first-domain UI delta is absent from this
   review by brief. Keep `U` unknown and do not issue an architecture selection
   from these counts.
2. **A test:** eliminate A if a run-local mock cannot achieve `TL=0`, if any
   target-conditioned import reaches generic harness/runtime implementation,
   or if a first-domain requirement replaces route/state composition rather
   than filling a named presentation field.
3. **B test:** eliminate or defer B if the extraction mock leaves shared-core
   imports pointing back to either shell, if `DC>0` after thin wrappers are
   excluded, or if compatibility routes/accessibility behaviors lack a common
   evidence owner.
4. **C test:** eliminate C if target adapters import non-public App internals,
   own cross-slot state or route orchestration, require runtime target
   switching, or bundle any opposite-target adapter/resource. Any of these is
   evidence for reconsidering B, not permission to weaken C.
5. **All variants:** eliminate the prototype if two artifacts cannot pass all
   eight target-specific build cells, if target identity/resources are mutable
   at runtime, or if either target changes capability/runtime authority.
6. **Cost backcheck:** once the Piping-derived UI delta is lawfully available,
   append its exact affected file/module set as `U`, rerun `TL`, `DC`, `BM`, and
   the cost vector, and record actual prototype LOC/build-time/artifact-size
   values separately from these lower bounds.

## 7. No-effect confirmation

I did not run a build or test, did not modify product/build outputs, did not
delegate, and did not infer first-domain UI requirements, generic runtime
semantics, packaging identity authority, or Agent-2 Bash. My sole write is this
return file. No source, PRD, decomposition, SCOPE_CHANGE, deliverable/status,
Task Management, receipt/corpus, Root/Piping/PEC, completion-log, Git,
release/lifecycle/publication, or D-APP-81 UNKNOWN-relation surface was written.
