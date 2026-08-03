# D-APP-89 Option B — Census, Mapping, and Rollback Evidence

Basis: `97678a841ef58345c73d3470ed8de57c9b1405d2` plus the preserved
uncommitted planning/ruling tranche. This is derivative execution evidence,
not authority or a retirement ruling.

## Before census

The execution-time snapshot is `BEFORE_CENSUS.txt` (289 matching lines).

| Category | Files | Exact occurrences | Disposition |
|---|---:|---:|---|
| Production `frontend/src/**`, excluding tests | 67 | 118 | migrated mechanically |
| Ordinary `frontend/src/__tests__/**` | 39 | 58 | migrated mechanically |
| Package/config/lock | 4 | 7 | root dependency, two TS aliases, and Next transpile target migrated; two workspace-retention lock strings remain |
| Script comment | 1 | 1 | historical explanatory comment; script already executes the Root import and is outside the write fence |
| Retained facade package | 1 | 1 | package identity retained by ruling |
| Coordination, deliverable, plan, evaluation, reconciliation, and historical/docs | snapshot remainder | 104 matching lines | historical/source references preserved, not executable reliance |

The 176 source import occurrences covered exactly 106 files: 67 production and
39 tests. The seven config occurrences were `package.json` (1),
`package-lock.json` (3), `tsconfig.json` (2), and `next.config.mjs` (1).

## Path-complete mapping

Every specifier used by an executable consumer at the before boundary maps to
the identically suffixed, existing Root export:

| Facade specifier | Root specifier | Root export exists |
|---|---|---|
| `@chirality/harness-contract` | `@chirality/runtime-contracts` | yes |
| `@chirality/harness-contract/agent-engine-port` | `@chirality/runtime-contracts/agent-engine-port` | yes |
| `@chirality/harness-contract/engine-conformance` | `@chirality/runtime-contracts/engine-conformance` | yes |
| `@chirality/harness-contract/errors` | `@chirality/runtime-contracts/errors` | yes |
| `@chirality/harness-contract/event-schema` | `@chirality/runtime-contracts/event-schema` | yes |
| `@chirality/harness-contract/mcp/tool-names` | `@chirality/runtime-contracts/mcp/tool-names` | yes |
| `@chirality/harness-contract/sdk-version` | `@chirality/runtime-contracts/sdk-version` | yes |
| `@chirality/harness-contract/tool-catalog` | `@chirality/runtime-contracts/tool-catalog` | yes |
| `@chirality/harness-contract/tool-descriptor` | `@chirality/runtime-contracts/tool-descriptor` | yes |
| `@chirality/harness-contract/transcript-replay` | `@chirality/runtime-contracts/transcript-replay` | yes |
| `@chirality/harness-contract/types` | `@chirality/runtime-contracts/types` | yes |

The dedicated rollback test additionally probes the retained facade's two
currently unused code subpaths, `domain-profile` and `operation-proposal`, so
all 13 facade code exports are compared with their exact Root counterparts.
`runtime/packages/contracts/package.json` declares each mapped root/subpath,
and each facade source file is a direct `export *` from that counterpart.

## After census and zero-consumer assertion

- Ordinary production/test executable references outside the rollback test: `0`.
- Direct App dependency in `package.json`: absent.
- Root-package dependency in `package-lock.json`: absent.
- TypeScript facade aliases: absent.
- Next facade transpile target: absent; canonical Root package is the target.
- Dedicated rollback test: exactly 13 facade imports, one per code export.
- Retained facade package identity: one package-name string.
- Retained lock/workspace identity: two strings, the workspace symlink and the
  workspace package name. They are required to keep rollback resolution
  installable and are not a root App dependency.
- Script: one historical comment in `scripts/generate-tool-catalog.mjs`; the
  executable import on that surface already uses the Root package.
- Every remaining documentary/historical/coordination string is enumerated in
  `REMAINING_REFERENCES_AFTER.txt` (snapshot excludes only itself). Those
  strings do not establish executable reliance.

`scripts/assert-harness-contract-deps.mjs` now makes the assertion
reproducible: it rejects any ordinary source import, root package/lock
dependency, TS alias, or Next config reference, while requiring exactly 13
rollback-test probes and retaining the existing facade-purity checks.

## Exact rollback boundary and sequence

Rollback is file-bounded and does not delete or reconstruct the facade:

1. Revert the 106 mechanical source/test specifier edits listed in
   `IMPLEMENTATION_MANIFEST.sha256` from `@chirality/runtime-contracts` back to
   the same-suffix facade specifier.
2. Restore the root App facade dependency in `frontend/package.json` and its
   root dependency entry in `frontend/package-lock.json`.
3. Restore the two facade aliases in `frontend/tsconfig.json` and the facade
   target in `frontend/next.config.mjs`.
4. Revert the strengthened zero-consumer portion of
   `scripts/assert-harness-contract-deps.mjs` and remove the dedicated rollback
   identity test if rolling back the migration itself.
5. Re-run Root build/typecheck/focused tests and the complete App validation
   set before accepting rollback bytes.

The facade directory is unchanged by the migration, so rollback never depends
on reconstructing deleted bytes. The source replacement is one-for-one and
preserves imported symbol lists and public shapes.

## Affected clients and non-effects

- App: all known executable clients in the before census were migrated; the
  retained workspace package remains available only for rollback proof.
- Root: read-only evidence establishes the already-existing exports; no Root
  source byte changed and no new generic runtime capability is claimed.
- Piping and PEC: no write occurred and no consumer-state claim is made.
- External/provider clients: no registry publication, release, distribution,
  network access, or external-consumer inference occurred.
- Historical D-APP/decomposition/evaluation references remain history and were
  not rewritten as current location authority.
- The six D-APP-81 `HISTORICAL_RELATION_UNKNOWN` relations were untouched.

## Release/no-reliance disposition

This migration creates no release, publication, distribution, provider,
professional-reliance, acceptance, or facade-retirement authority. Final
facade removal remains a later owner gate after a fresh landed-tree census and
full rerun evidence.
