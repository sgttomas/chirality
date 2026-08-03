# Candidate Schemas and Extraction Map

State: `NON-AUTHORITATIVE DESIGN EXAMPLES`

Values marked `<from committed Piping response>` cannot be filled while the
first-domain UI-delta lane is held.

## A candidate product profile

```yaml
schemaVersion: 1
targetId: desktop | domain-piping
display:
  productName: string
  shortName: string
  iconSetRef: repository-contained resource ref
  copyRef: repository-contained copy table ref
navigation:
  initialSurface: dialogue | work | pipeline | workbench
  visibleSurfaces: [surface-id]
slots:
  typedAgentPresentation: <module ref or none>
  structuredInformation: <module ref or none>
  workflowPresentation: <module ref or none>
  decisionGatePresentation: <module ref or none>
packaging:
  artifactKey: string
  identityKey: owner-gated symbolic key
  resourceSetRef: repository-contained resource ref
  dataNamespaceKey: owner-gated symbolic key
evidence:
  uiDeltaRef: <committed Piping response path + blob/SHA-256>
```

A may materialize this value as one governed configuration selected before
application bootstrap. It does not by itself prevent downstream target
conditionals, so the reconciled nine-path lower-bound set `P=9` in
`ARCHITECTURE_DEPENDENCY_MAPS.md` is mandatory.

## C candidate immutable product/slot schema

```yaml
schemaVersion: 1
profileId: desktop-v1 | domain-piping-v1
buildTarget: desktop | domain-piping
identity:
  displayName: string
  bundleIdentityKey: owner-gated symbolic key
  artifactNameTemplate: string
  dataNamespaceKey: owner-gated symbolic key
resources:
  iconSetRef: repository-contained resource ref
  copyTableRef: repository-contained resource ref
composition:
  defaultSurface: surface-id
  navigationAdapter: module ref conforming to NavigationSlot
  typedAgentAdapter: module ref conforming to TypedAgentSlot
  structuredInformationAdapter: module ref conforming to InformationSlot
  workflowAdapter: module ref conforming to WorkflowSlot
  decisionGateAdapter: module ref conforming to DecisionGateSlot
constraints:
  runtimeSwitching: false
  targetAdapterImports: declared shared public APIs only
evidence:
  uiDeltaRef: <committed Piping response path + blob/SHA-256>
```

Candidate slot contracts:

| Slot | Input boundary | Output boundary | Forbidden effect |
|---|---|---|---|
| `NavigationSlot` | fixed common surface IDs + profile | navigation items/default surface | route authority outside declared target |
| `TypedAgentSlot` | governed agent projection records | target presentation nodes | delegation/runtime capability grant |
| `InformationSlot` | accepted structured records | read/presentation components | domain calculation or verdict |
| `WorkflowSlot` | governed work/progress records | workflow presentation components | lifecycle transition |
| `DecisionGateSlot` | accepted proposal/ruling state | decision presentation components | owner selection |
| `ResourceSlot` | validated resource refs | display metadata/assets | filesystem discovery or network fetch |

## B candidate shared-core/shell extraction map

| Current surface | Candidate destination | Boundary |
|---|---|---|
| `src/components/woven-dialogue/**` | `packages/ui-core/woven/**` | common authority, projection, guarded selection, replay, accessibility |
| reusable `src/components/shell/**` | `packages/ui-core/shell/**` | common chrome primitives; no target copy/navigation literals |
| `src/components/workspace/**` | `packages/app-state-core/providers/**` | common state providers and project-root state |
| `src/lib/woven-dialogue/**`, `src/lib/shell/**`, `src/lib/workspace/**` | `packages/app-state-core/**` | common state/projection functions |
| `src/lib/runtime-client/**` and governed shared client adapters | `packages/app-client-core/**` | App affected-client behavior only; Root generic semantics excluded |
| `src/app/layout.tsx`, `src/app/page.tsx` | two shell-owned route/layout compositions | target-specific composition over shared packages |
| `electron/main.ts`, `electron/preload.ts` | target entries plus extracted common Electron helpers | identity/resources/process composition; generic runtime remains external |
| `package.json`, `next.config.mjs`, `build-electron.mjs` | workspace root plus two target build manifests | explicit target graph and output isolation |

B's extraction is invalid if it copies common Woven or accessibility behavior
into both shells, or if a shared package imports either target shell.

## Unresolved fields

The held Piping input prevents exact values for target navigation, typed-agent
views, structured-information views, workflow/gate slots, agent-facing API
equivalence, and any App-visible runtime affordance. Those fields remain
placeholders; they are not guessed from current App or Root material.
