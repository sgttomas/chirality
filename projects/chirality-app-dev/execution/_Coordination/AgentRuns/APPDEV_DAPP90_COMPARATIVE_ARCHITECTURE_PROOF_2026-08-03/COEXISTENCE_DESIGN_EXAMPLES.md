# Two-Artifact Identity, Resource, and Data-Coexistence Examples

State: `DESIGN EXAMPLES ONLY — NO IDENTITY SELECTED`

These examples apply to A, B, or C. Symbolic values deliberately avoid
creating actual bundle, signing, update, release, runtime-daemon, or data-
migration authority.

## Current collision inventory

The examples must address, rather than conceal, these current one-target
facts:

- `package.json` has one `appId`, `productName`, icon, resource set, and `dist`
  output;
- `build-electron.mjs` deletes/reuses the same `.next`, `dist-electron`,
  `dist-runtime`, and downstream package outputs, so parallel target builds
  would collide without target-indexed roots;
- Electron `userData` currently anchors preferences, credentials, logs, and
  runtime-related state;
- the App client currently has a fixed `chirality-app-dev` project binding;
- the CLI installer owns one `~/.local/bin/chirality` launcher; and
- current LaunchAgent/runtime endpoint ownership is not a product-profile
  decision and remains blocked behind separate contracts.

No variant survives if it merely changes display copy while retaining these
collisions for two artifacts.

## Example 1 — Fully separated local artifacts

| Dimension | Standalone Desktop | Piping control plane |
|---|---|---|
| Artifact key | `desktop-local` | `domain-piping-local` |
| Display label | `Chirality` candidate | `Chirality — Piping` candidate |
| Bundle identity key | `BUNDLE_DESKTOP` owner-gated symbol | `BUNDLE_DOMAIN_PIPING` owner-gated symbol |
| Icon/resource set | `resources/desktop/**` candidate | `resources/domain-piping/**` candidate |
| Build output | `out/desktop/**` candidate | `out/domain-piping/**` candidate |
| App-data namespace key | `DATA_DESKTOP` owner-gated symbol | `DATA_DOMAIN_PIPING` owner-gated symbol |
| App preferences/cache/session index | separate | separate |
| User-selected working project root | may point to a project selected by user | may point to a Piping project selected by user |
| Update channel | none / local proof only | none / local proof only |

Coexistence rule: artifact-level preferences, cache, credentials references,
logs, and UI session indexes must not share a namespace. Both applications may
open an owner-selected project root only through existing governed project-root
controls. This example does not decide whether their runtime endpoint/process
is shared; generic runtime identity/version/resume remain `BLOCKED_BY_ROOT`.

Failure probes for a later implementation:

1. install/launch both artifacts without LaunchServices identity collision;
2. change theme/last surface in one and prove the other is unchanged;
3. create local app-session metadata in one and prove it is absent in the
   other's data namespace;
4. select the same project root in both and prove App metadata remains separate
   while governed project files are not duplicated or mutated implicitly; and
5. uninstall one local artifact and prove the other's resources/data remain.

## Example 2 — Shared read-only resources, isolated mutable state

Both artifacts may embed byte-identical versioned common resources (agent
instructions, common docs, fonts, Woven assets) while carrying distinct target
resource overlays and mutable data namespaces.

```text
artifact desktop                   artifact domain-piping
  Resources/common/vN  <same hash>   Resources/common/vN
  Resources/desktop                  Resources/domain-piping
  Data/DESKTOP                       Data/DOMAIN_PIPING
  projectRoot -> user choice         projectRoot -> user choice
```

The common resource directory is immutable after packaging and verified by a
manifest hash. Target overlays may reference only declared common assets and
cannot overwrite them. Mutable application state never writes into packaged
resources or the other target's data namespace.

Failure probes for a later implementation:

1. common-resource manifests are byte-identical in both artifacts;
2. target overlays contain no same-path shadow of protected common files;
3. each artifact resolves its own display resources after relocation;
4. writable-path census contains no other-target namespace; and
5. a corrupt/missing target overlay fails closed without falling back to the
   other target.

## Explicit exclusions

- No actual application identifier, entitlement, signature, notarization,
  update URL, release channel, or distribution name is selected.
- No D-APP-88 helper is produced or assumed present.
- No shared daemon, socket, session-resume, credential, sandbox, or version
  semantics are selected.
- No product source or package configuration is changed by these examples.
