# Agent 2 Return — Packaging, Identity, and Coexistence Review

Reviewer: bounded ephemeral Agent 2 generalist

Parent: `HELPS_HUMANS`
Verdict: `PASS WITH HARD CONDITIONS — DESIGN EVIDENCE ONLY; A/B/C REMAIN OPEN`

## 1. Scope and evidence basis

I reviewed the D-APP-90 packet and ruling, this run's activation and frozen
work graph, current App packaging/Electron/UI entry topology, the D-APP-87
packaging re-plan, and the D-APP-88 R2 blocked/rollback record. I did not run a
build or package command.

The material current-tree observations are:

- `frontend/package.json` (current-byte SHA-256
  `1f14df17d407b18949d5a7195a786574fa8f03eda731dbe7b77f3e91685fba53`)
  defines one package entry, one `appId`, one `productName`, one output
  directory, one icon, one `files` set, and one `extraResources` set.
- `frontend/next.config.mjs` (current-byte SHA-256
  `bbf85b81f8dbcbb26ebb2dd76fed99f1c179c454b2e22b8073b5868c6fdc1b66`)
  defines one Next graph. Its current direct-runtime-contract setting is part
  of the accepted D-APP-89 migration basis; it is not a product-profile seam.
- `frontend/scripts/build-electron.mjs` emits one Electron main, one preload,
  and one `chirality` CLI bundle into shared fixed output paths. It deletes the
  output directories before each run, so two target builds cannot safely share
  that output root concurrently without a later target-indexed build design.
- `frontend/electron/main.ts` (current-byte SHA-256
  `16ad6688abaebd0bb1bfe04921a7eb1d20601bf2f2af983153da3c734f44ad1f`)
  composes the full GUI, embedded Next server, IPC, project binding, daemon
  posture, runtime connection, resource root, and daemon mode in one entry.
- `frontend/electron/desktop-project-client.ts` fixes the App client to
  `chirality-app-dev`; `main.ts` and `runtime-host.ts` derive runtime state
  beneath Electron `userData`; `api-key-storage.ts` derives credentials there;
  and `cli-launcher.ts` installs one fixed `~/.local/bin/chirality` launcher
  pinned to the currently running bundle's executable and daemon posture.
- `frontend/src/app/layout.tsx` and `frontend/src/components/shell/shell-frame.tsx`
  carry common providers and Woven shell chrome, but also contain target-
  variable title, brand resource, copy, and navigation literals. The closed
  domain-engine registry is not a product-profile registry and must not be
  repurposed as one.
- D-APP-88 R2 established only diagnostic feasibility for a separately built
  Electron target. Its manager return SHA-256 is
  `4ed34171427ddb7edaee02495ce7e21b1b5c6ad6ba675fe42f53ee99ab56d2a5`;
  its handoff SHA-256 is
  `5ff048a4452e546c0b1b97481c1b8456eee2ad1a9d33cd219ab4d553f1d8c918`.
  The candidate was rolled back and the graceful-stop conjunct remains
  blocked. Those bytes are neither a product target nor reusable packaging
  authority.

These facts support a comparative design, not an implementation or identity
ruling.

## 2. Candidate A schema — one lightly skinned graph

The following is a non-authoritative shape example. Field values marked
`<owner-gated-ref>` are references, not proposed actual identifiers.

```yaml
schemaVersion: candidate.app-product-profile/v1
profileKey: <standalone-or-domain-profile-key>
buildBinding:
  targetKey: <immutable-build-target>
  artifactIdentityRef: <owner-gated-ref>
  executableIdentityRef: <owner-gated-ref>
presentation:
  displayNameRef: <owner-gated-ref>
  metadataTitleRef: <profile-copy-ref>
  initialRoute: <allowlisted-route-ref>
  primaryNavigation: [<allowlisted-route-ref>]
  brandResourceSet: <target-resource-manifest-ref>
slots:
  typedAgentViews: [<slot-ref>]
  structuredInformationViews: [<slot-ref>]
  workflows: [<slot-ref>]
  decisionGatePresentation: [<slot-ref>]
packaging:
  iconRef: <target-resource-manifest-ref>
  includedResources: [<allowlisted-resource-ref>]
  excludedTargetKeys: [<opposite-target-key>]
  updateChannelRef: <design-only-disabled-or-owner-gated-ref>
data:
  userDataNamespaceRef: <owner-gated-ref>
  rendererStorageNamespaceRef: <target-key-derived-ref>
  sessionCoexistencePolicyRef: <owner-gated-ref>
runtimeClient:
  appNeedProfileRef: <app-side-need-only>
security:
  mayGrantRuntimeCapability: false
```

For A to remain genuinely “lightly skinned,” all target variation must enter
through one validated, immutable build-bound profile object. Product checks
should reject direct target-key conditionals outside an explicit small seam.
The profile must not be loaded from a mutable file at runtime and must not
grant tools, runtime authority, provider/network access, or sandbox policy.

Current fit: A can parameterize the literals now embedded in `layout.tsx`,
`shell-frame.tsx`, the package manifest, resource selection, initial route,
and Electron data-root initialization. It does not by itself solve the fixed
project binding, fixed launcher destination, fixed LaunchAgent posture, or
shared output-directory collisions; those are mandatory target-indexed seams,
not optional copy changes.

## 3. Candidate C schema — immutable profile plus bounded slots/adapters

C needs a stricter two-part contract than A: an immutable product manifest and
a closed build-time adapter registry. This is also a non-authoritative example.

```yaml
schemaVersion: candidate.app-build-product/v1
productKey: <standalone-or-domain-product-key>
identity:
  artifactIdentityRef: <owner-gated-ref>
  displayNameRef: <owner-gated-ref>
  executableIdentityRef: <owner-gated-ref>
resources:
  manifestRef: <target-resource-manifest-ref>
  iconRef: <target-resource-manifest-ref>
composition:
  shell: woven-shared
  adapters:
    brand: <closed-adapter-id>
    navigation: <closed-adapter-id>
    initialSurface: <closed-adapter-id>
    typedAgentViews: <closed-adapter-id>
    structuredInformationViews: <closed-adapter-id>
    workflows: <closed-adapter-id>
    decisionGates: <closed-adapter-id>
packaging:
  outputNamespace: <target-key-derived-ref>
  updateChannelRef: <design-only-disabled-or-owner-gated-ref>
data:
  userDataNamespaceRef: <owner-gated-ref>
  sessionCoexistencePolicyRef: <owner-gated-ref>
guards:
  runtimeProfileSwitching: forbidden
  crossTargetAdapterImport: forbidden
  adapterCapabilityGrant: forbidden
```

Candidate registry rules:

1. exact product keys and adapter IDs are closed at build time;
2. the build resolves them to generated constants/direct imports and packages
   no mutable profile loader;
3. each adapter implements a narrow shared slot interface and may import the
   shared interface and target-local resources, not another target's adapter
   or private shell internals;
4. the shared shell never branches on a product key; and
5. the package proof inventories the resolved manifest and shows the opposite
   target's adapters/resources are absent.

This separates C from A: A permits one bounded profile object to configure the
same graph, whereas C allows explicitly registered variation only at named
slots and produces a target-closed graph before packaging. If C needs broad
conditionals or adapters that reach arbitrary shell internals, it has become A
with hidden leakage or an unacknowledged B and should be eliminated.

## 4. B shared-core / target-shell extraction review

Candidate boundary direction: `target shell -> shared core`; the shared core
must never import a target shell, target manifest, or target resource tree.

| Current surface | Candidate B treatment | Boundary reason |
|---|---|---|
| `src/components/woven-dialogue/**` and invariant layout/accessibility primitives | shared core | D-APP-87 treats Woven/authority/accessibility invariants as common |
| workspace, deliverables, toolkit, harness-events, and runtime-connectivity providers | shared core, behind stable interfaces | provider behavior is common; target shells compose it |
| reusable shell panels and state helpers | shared core | avoid duplicating state, accessibility, and security behavior |
| `layout.tsx`, route entry, initial navigation, metadata, brand/copy | thin target shell | these currently mix common providers with target-variable presentation |
| `shell-frame.tsx` | split invariant frame from a target-supplied presentation/navigation descriptor | the current file hard-codes brand resource, wordmark, and navigation |
| shared API/runtime-client adapters | shared core only where target-neutral | target access/exposure decisions stay in shell composition; no generic runtime semantics are invented |
| `electron/main.ts` | extract common Electron services; keep one thin entry/composer per target | current monolith joins target identity, resource/data roots, renderer, IPC, daemon, and client binding |
| preload and IPC registration | shared implementations with explicit target allowlists | target shell selects exposure but cannot grant new capability |
| package/builder configuration, icon/resource manifest, output path | one manifest per target shell | artifact identity and resource exclusion must be independently provable |
| project binding, `userData`, launcher ownership, LaunchAgent relationship | explicit target-shell policy referencing separately ruled contracts | current fixed literals collide; Root-owned runtime semantics remain outside this proof |

B fails its own purpose if separate shells copy the current root layout,
Electron initialization, IPC registration, or Woven shell wholesale. The
extraction should first isolate common compositional functions, then leave the
standalone and domain entries as declarative assembly plus target-owned
presentation/resources. A dependency check must reject any `shared -> target`
edge and any target-to-target import.

## 5. Two-artifact coexistence design examples

These examples intentionally use symbolic identity references. They do **not**
select actual bundle identifiers, executable names, release channels, project
registrations, or runtime contracts.

### Example 1 — isolated local product state (safer default candidate)

| Property | Standalone artifact | First-domain artifact |
|---|---|---|
| Bundle identity | `<BUNDLE_ID_STANDALONE_OWNER_GATED>` | `<BUNDLE_ID_FIRST_DOMAIN_OWNER_GATED>` |
| Display name | `<DISPLAY_NAME_STANDALONE_OWNER_GATED>` | `<DISPLAY_NAME_FIRST_DOMAIN_OWNER_GATED>` |
| Executable identity | `<EXECUTABLE_STANDALONE_OWNER_GATED>` | `<EXECUTABLE_FIRST_DOMAIN_OWNER_GATED>` |
| Resources | `resources/standalone.manifest` allowlist | `resources/first-domain.manifest` allowlist |
| Update channel | disabled for unsigned local proof; later separate owner-gated reference | disabled for unsigned local proof; later separate owner-gated reference |
| Electron application-data root | `<appData>/<standalone-userData-key>` | `<appData>/<first-domain-userData-key>` |
| Renderer storage/cache/logs/credentials | beneath standalone namespace | beneath first-domain namespace |
| Runtime/session root | isolated target reference pending Root/App contract | isolated target reference pending Root/App contract |
| Operator working root | explicit user selection only | explicit user selection only |

This design prevents accidental sharing. Sharing a user-selected working root
does not imply sharing Electron profile state, credentials, caches, logs,
sockets, tokens, daemon jobs, or session stores. A later accepted migration can
allow specific interoperability; absence of such a ruling keeps the stores
isolated.

### Example 2 — shared Root runtime, isolated product state (conditional design)

| Property | Standalone artifact | First-domain artifact |
|---|---|---|
| Bundle/display/executable identity | distinct symbolic standalone references | distinct symbolic first-domain references |
| Resources | standalone-only allowlist plus common hashed resources | first-domain-only allowlist plus the same common hashed resources |
| Update channel | separate design-only reference | separate design-only reference |
| Electron application-data root | isolated standalone UI/preferences/cache/log root | isolated first-domain UI/preferences/cache/log root |
| Runtime endpoint | same external `<ROOT_RUNTIME_ENDPOINT_REF>` | same external `<ROOT_RUNTIME_ENDPOINT_REF>` |
| Project/session storage | shared only through a later accepted Root contract and explicit project registration | same; no direct filesystem sharing by the renderer |
| Concurrent session behavior | later contract must define ownership/locking/resume | same contract; one artifact cannot infer permission from the other |

This design is viable only after Root supplies the generic identity/version/
resume contract and App separately adopts it. The artifacts remain clients;
neither derives a private daemon or session semantic from its bundle identity.
Until that authority exists, Example 2 is a design question, not a deployable
configuration.

## 6. Collision and failure modes

1. **Package identity collision:** two outputs inherit the current single
   `appId`, `productName`, executable, icon, or output path and overwrite or
   LaunchServices-alias each other.
2. **Data-root collision:** distinct bundles resolve the same `userData` and
   silently share Chromium profiles, preferences, credentials, logs, runtime
   sockets, tokens, or adapter events.
3. **CLI collision:** both apps install `~/.local/bin/chirality`; the later
   launch silently repins the one launcher to its executable. A later design
   must assign sole ownership, distinct names, or an owner-gated neutral
   multiplexer.
4. **LaunchAgent collision:** both clients install/uninstall or repin the same
   default job/executable without a ruled single-daemon ownership policy.
5. **Fixed project-binding collision:** the domain artifact is treated as
   `chirality-app-dev` merely because the current Desktop client is fixed to
   that ID, bypassing the missing domain-product/runtime input.
6. **Resource leakage:** `public`, `build`, `extraResources`, or Next output
   includes the opposite target's icon, copy, adapters, domain information, or
   configuration.
7. **Build-output collision:** target builds delete or reuse the same
   `.next`, `dist-electron`, `dist-runtime`, or `dist` path, yielding a mixed
   or source-misaligned artifact.
8. **Runtime skin switching:** a mutable profile, query parameter, local
   storage value, environment value visible to the renderer, or downloaded
   file switches target identity after build.
9. **Capability smuggling:** a product profile/adapter changes tools,
   provider/network behavior, sandbox policy, runtime identity, or Agent-2 Bash.
10. **Common-invariant drift:** B duplicates Woven, accessibility, authority,
    IPC, or security composition in both shells and fixes land in only one.
11. **Hidden adapter divergence:** C adapters import private shell modules or
    each other until the manifest is only a label over two ungoverned shells.
12. **Update/release collision:** one feed/channel can replace the other
    artifact or an unsigned proof is described as release-ready. No updater
    or release authority exists here.
13. **D-APP-88 contamination:** the rolled-back helper bundle, its identifiers,
    or its candidate builder config is reused as evidence that domain-product
    identity or coexistence has been accepted.

## 7. Measurement suggestions

The comparative proof can measure these without building a product:

- count target-condition branches outside the single allowed profile seam
  (A) or outside registered slots (C); target goal: zero;
- count `shared -> target` and target-to-target import edges (B/C); target goal:
  zero;
- count duplicated composition modules/LOC for root layout, Electron startup,
  IPC registration, Woven shell, accessibility, and security policy (B);
- enumerate, per variant, files moved, files parameterized, new entry/config
  surfaces, build cells, and target-specific validation cells;
- enumerate every package-identity field, resource include/exclude rule,
  output directory, `userData`/renderer-store root, runtime endpoint, project
  binding, LaunchAgent relation, and launcher destination that lacks a
  target-indexed decision;
- compute resource-manifest intersection and opposite-target leakage count;
  shared resources must be explicitly classified and hash-identical;
- compute resolved-package dependency sets and opposite-target adapter/resource
  presence from frozen mock graphs; and
- record the number of Root-blocked assumptions required by each coexistence
  example rather than treating them as solved.

A later authorized package drill should additionally validate two clean
sequential and parallel builds, independent artifact identity/resource
manifests, simultaneous launch, independent application-data state, explicit
shared-or-isolated session behavior, launcher/job non-interference, and
uninstall/upgrade isolation. Those are suggestions for a later gate; none was
executed here.

## 8. Elimination tests

### Eliminate A if any is true

- target identity can change after build;
- a target branch exists outside the one governed profile boundary;
- opposite-target resources/configuration are present in either artifact;
- two outputs cannot be made identity-, data-, resource-, and output-distinct
  without post-build mutation; or
- profile fields grant capability or assume blocked generic runtime semantics.

### Eliminate B if any is true

- the shared core imports either target shell;
- target shells duplicate common Woven/accessibility/authority/security or
  Electron/IPC composition rather than compose shared implementations;
- the extraction creates a shared-core/target-shell dependency cycle;
- the measured first-domain migration requires changing common semantics
  before the first-domain delta is known; or
- independent shell packaging still collides on outputs, data roots, CLI, or
  daemon ownership.

### Eliminate C if any is true

- the product manifest is interpreted or switchable at runtime;
- an adapter imports another target's adapter or arbitrary private shell
  implementation;
- a slot can grant runtime/tool/network/sandbox capability;
- the packaged graph contains opposite-target adapters/resources; or
- target divergence requires so many private-shell exceptions that the closed
  slot boundary is no longer truthful.

### Eliminate any variant if any is true

- it treats the D-APP-88 helper as present or accepted;
- it selects actual release/signing/publication/update semantics in this proof;
- it invents a generic runtime, identity, version, resume, sandbox, or Bash
  contract; or
- it cannot demonstrate two independently identifiable artifacts without
  silently sharing or overwriting product-local state.

## 9. Authority separations and no-effect confirmation

- The examples are derivative candidates, not actual bundle identifiers,
  display-name rulings, packaging manifests, update channels, application-data
  paths, project registrations, or runtime/session contracts.
- D-APP-88 remains blocked/absent. Its candidate source and package evidence
  are diagnostic only and no helper byte or identifier is incorporated here.
- Signing, notarization, publication, distribution, upgrade, release channel,
  lifecycle, and release-readiness work remain out of scope.
- Generic runtime, sandbox, identity, version, resume, and Bash remain
  `BLOCKED_BY_ROOT`; no Agent-2 Bash or product-profile capability grant is
  proposed.
- I did not delegate, build, package, execute product code, or alter source,
  configuration, PRD, decomposition, SCOPE_CHANGE, deliverable/status, Task
  Management, foreign-loop, receipt/corpus, completion-log, Git, release, or
  historical-relation state.
- The only path written by this reviewer is this required return:
  `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APPDEV_DAPP90_COMPARATIVE_ARCHITECTURE_PROOF_2026-08-03/reviews/A2_PACKAGING_IDENTITY_COEXISTENCE_RETURN.md`.
