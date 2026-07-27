# A2-DAPP48-49 terminal return

- **Basis:** `0f8349d90f58c1e6b3339263f5aafaf36e783a7e`
- **Mode:** read-only ephemeral Agent 2
- **Repository writes:** none

## D-APP-48 conflict and validator boundary

D-APP-48's ruling says the pull contract pins
`ee290e22a8c19d46fb8004114d2ede55b805fba4`; the live JSON pins
`55a066fdff6877d8aa2a49ce08a545ac98872848`. Both commits resolve and the
latter descends from the former. The live JSON was repinned after the ruling.
This is an authority-record versus live-contract conflict, not an
unreachable-object defect.

The pull-only validator passes because it reads and validates the historical
bytes at the JSON's pinned commit. It does not compare the contract with the
current working tree. Substituting the accepted basis in memory produced 19
errors: package dependency, export-key, export-checksum, target, and literal
constant mismatches. Therefore a green pull-only validation proves the
historical package matches its manifest; it does not prove current carrier
synchronization.

## Piping consumption

Piping D-30 still pins `ee290e22…`, package version `0.0.0-private`, and tool
registry `harness-tools.v6.mutating-mcp`. The live D-APP-48 JSON uses
`55a066fd…` and `harness-tools.v14.headless-preview-live`.

```text
pull contract only: PASS
pull contract + Piping D-30: FAIL
reason: consumption source.commitSha mismatch
```

Piping has no installed runtime/source dependency and D-30 declares
`runtimeDependencyInstalled: false`. This blocks reliance on D-30 as a current
synchronized consumption record, not the Piping product as a whole. The stale
claim also remains in Piping decision D-31 and decomposition DEC-063.

## D-APP-49 continuity and audit status

D-APP-49's two source modules migrated byte-identically to Root:

| Module | Original/migrated/current SHA-256 |
|---|---|
| `domain-profile.ts` | `a99637becbb1eaea79a25aee7a383630ce3293fd6810eb594e51ff23623a034a` |
| `operation-proposal.ts` | `90ba567890f6793f0fd93d4ebeb8f74c2b83eb071923e5667830c604258af9ab` |

Root now carries the implementation under `@chirality/runtime-contracts`.
App carries deprecated two-line compatibility re-exports. App tests import
the facade and therefore exercise Root transitively, not the facade source
itself.

No admitted current-location D-APP-49 audit was found. Thirty-four focused
tests exist, but current execution was unavailable because the clean worktree
lacks installed dependencies (`vitest: command not found`). Byte continuity
is established; current executable audit status is UNKNOWN.

## Version identity and degraded mode

Current version notions are:

- Flow-A semantic value: `flow-a.contract.v0.1.0`
- Root package: `@chirality/runtime-contracts@0.1.0`
- runtime protocol: `RUNTIME_API_VERSION = "v1"`

No evidence establishes negotiated Flow-A compatibility, incompatible API
rejection, an old-client/new-daemon matrix, or a new-client/old-daemon matrix.
The daemon emits `apiVersion: "v1"`, while `RuntimeClient.health()` does not
enforce runtime equality. A Root/Tier-0 disposition is needed; the evidence
does not justify inventing a new version value.

The App is broadly fail-closed when the daemon is unavailable: no in-process
runtime fallback, 503/`ENGINE_UNAVAILABLE` behavior, and connectivity
supervision. Incompatible-version behavior, feature downgrade, and complete
user-facing degraded-mode obligations remain UNKNOWN. `RUNTIME-OPEN-002`
already records this gap.

## Consumer census highlights

- App production files importing the compatibility facade: 67
- App test files importing the compatibility facade: 39
- App production files directly importing Root contracts: 4
- PEC production files directly importing Root contracts: 1
- Piping runtime/source imports: 0; governed metadata only

## Recommended alternatives

1. Prefer superseding D-APP-48 as an App-era mechanism with a Root-owned
   contract/version act, after consumer evidence is accepted. Disposition
   Piping's records in its own loop. Do not invent a repin target.
2. If D-APP-48 remains live, explicitly rule whether a dependency-bearing
   compatibility facade can satisfy its original dependency-free pull
   contract.
3. Treat D-APP-73 as the prospective D-APP-49 location successor, preserve
   D-APP-49 as historical authority for the two shapes, and run a first
   current-location audit against Root plus facade behavior.
4. Decide facade retirement separately; elapsed time does not establish the
   end of a migration cycle.
5. Route Flow-A/package/protocol identity and incompatibility behavior to
   Root/Tier-0. Preserve degraded-mode unknowns until tested.
