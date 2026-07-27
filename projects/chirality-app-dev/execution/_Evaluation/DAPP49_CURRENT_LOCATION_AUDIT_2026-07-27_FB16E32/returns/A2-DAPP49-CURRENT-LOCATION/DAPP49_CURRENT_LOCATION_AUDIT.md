# D-APP-49 current-location executable audit

## Verdict

`SUPPORTED_WITH_SUCCESSOR_QUALIFICATION`

At accepted basis `fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`, the two
D-APP-49 implementations are byte-identical to their original App landing
bytes, build and typecheck in the Root-owned `@chirality/runtime-contracts`
package, pass all 34 focused guard tests through the App compatibility barrel,
and resolve through both Root and App subpath exports. The App subpath exports
return the same function and constant objects as their Root counterparts.

This proves current executable continuity of the two inert type-and-guard
contracts under D-APP-73's prospective rehome. It does not make the original
D-APP-49 statement that the App package is the semantic implementation home
true today. The App package is now a deprecated, dependency-bearing
compatibility facade; D-APP-73 is the location successor.

## Isolation and basis

- Disposable clone:
  `/private/tmp/chirality-dapp49-audit-d9HnC5/repo`
- Accepted commit:
  `fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae`
- Commit subject:
  `Merge pull request #371 from sgttomas/codex/od7-maintenance-evaluation`
- Tree:
  `65f1ca55329a091ca9759a483ec40c41e27fdd23`
- Final Git state: clean (`git status --porcelain=v1` empty; tracked and
  staged diffs both empty)
- Repository writes: none
- Node: `v24.18.0`
- npm: `11.16.0`

## Lockfile identities

| Lockfile | SHA-256 | lockfileVersion | package entries |
|---|---|---:|---:|
| `runtime/package-lock.json` | `4105799bbdb8a1b5025a71a0098e460281f8e6db62b1a912d37aade2935a7c0f` | 3 | 118 |
| `projects/chirality-app-dev/frontend/package-lock.json` | `674fe2dab74572f21d26455498461d62eaa4218560e45024ed2a31e00c635ab8` | 3 | 848 |

## Carrier inventory and identities

| Surface | Path | SHA-256 / result |
|---|---|---|
| Root implementation | `runtime/packages/contracts/src/harness/domain-profile.ts` | `a99637becbb1eaea79a25aee7a383630ce3293fd6810eb594e51ff23623a034a` |
| Root implementation | `runtime/packages/contracts/src/harness/operation-proposal.ts` | `90ba567890f6793f0fd93d4ebeb8f74c2b83eb071923e5667830c604258af9ab` |
| App facade | `projects/chirality-app-dev/frontend/packages/harness-contract/src/domain-profile.ts` | `5836be2fb166093e5e9bb56989732dfd351cde3d298dc2f265e8b4fcaf588b92` |
| App facade | `projects/chirality-app-dev/frontend/packages/harness-contract/src/operation-proposal.ts` | `b471fc0ae4ab4a32a304aaf4a719409c51d6615c7d6a125dc3416a56bd99ff9d` |
| Root export map | `runtime/packages/contracts/package.json` | exports `./domain-profile` and `./operation-proposal` to built JS and declarations |
| App export map | `projects/chirality-app-dev/frontend/packages/harness-contract/package.json` | exports both subpaths to two-line deprecated source facades |
| Root barrels | `runtime/packages/contracts/src/harness/index.ts`, `src/index.ts` | re-export both modules through package root |
| App barrel | `projects/chirality-app-dev/frontend/packages/harness-contract/src/index.ts` | re-exports `@chirality/runtime-contracts` |

The D-APP-49 landing commit `fe15cfe68` contains the same two implementation
SHA-256 values. The mirror-source commit
`77a327727605f05da5f304288f1ddd87dc09659d` resolves. Neither Root
implementation contains an import statement.

## Commands and results

| Command | Exit | Evidence |
|---|---:|---|
| `npm --prefix runtime ci` | 0 | `added 61 packages` |
| `npm --prefix runtime run build --workspace @chirality/runtime-contracts` | 0 | `@chirality/runtime-contracts@0.1.0 build`; `tsc -b` |
| `npm --prefix projects/chirality-app-dev/frontend ci` (sandboxed first attempt) | 1 | `ENOTFOUND registry.npmjs.org` for lockfile-pinned `@earendil-works/pi-tui` |
| same App `npm ci`, approved network retry | 0 | `added 752 packages, and audited 760 packages`; one high-severity audit notice |
| `npm --prefix projects/chirality-app-dev/frontend test -- src/__tests__/lib/domain-profile.test.ts src/__tests__/lib/operation-proposal.test.ts` | 0 | `Test Files 2 passed (2)`; `Tests 34 passed (34)` |
| first `npm --prefix projects/chirality-app-dev/frontend run typecheck` | 2 | linked Root sibling package declarations absent because only `runtime-contracts` had been built |
| `npm --prefix runtime run build` | 0 | full Root workspace `tsc -b` |
| repeated App `npm run typecheck` | 0 | both browser and Electron TypeScript checks passed |
| `npm --prefix runtime run typecheck` | 0 | Root workspace `tsc -b --pretty false` passed |
| `npm --prefix projects/chirality-app-dev/frontend run harness:validate:contract-deps` | 0 | `harness contract dependency lint passed` |
| Root direct subpath import probe | 0 | both subpaths PASS; 7 profile statuses and 5 lifecycle states; representative guards PASS |
| App facade direct subpath import/identity probe | 0 | both subpaths PASS; function and constant object identities equal Root exports |

The initial App typecheck failure was an execution-order artifact: the App
workspace has local-file dependencies on multiple Root packages whose
declaration output is required. Building the complete Root workspace made the
unchanged App typecheck pass.

## Claim-by-claim disposition

| D-APP-49/current-successor claim | Result |
|---|---|
| Two canonical source shapes and type guards remain executable | `SUPPORTED` |
| Current Root implementations preserve the accepted original bytes | `SUPPORTED` |
| Root package root and subpath exports work | `SUPPORTED` |
| App compatibility barrel and both App subpath exports work | `SUPPORTED` |
| App facade resolves to the same executable exports as Root | `SUPPORTED` |
| Root implementations remain inert apart from guards, with no imports/I/O/persistence/UI | `SUPPORTED_BY_SOURCE_AND_BYTE_IDENTITY` |
| Original App package remains the semantic implementation owner/home | `NOT_CURRENT`; prospectively rehomed by D-APP-73 |
| App compatibility package remains dependency-free | `NOT_CURRENT`; it deliberately depends on Root |
| Broader domain-engine behavior, MCP operation application, persistence, UI, or protected-path writes | `NOT_TESTED_AND_NOT_GRANTED` |

## Limitations and observations

- This is a focused current-location audit, not the full App premerge suite.
- No UI, daemon, PEC, Piping, domain engine, network protocol, persistence, or
  protected-path behavior was started.
- The 34 tests import the App package barrel. Separate direct probes cover the
  Root and App subpath export maps.
- Direct Node import of the App `.ts` facade subpaths passes under Node
  `v24.18.0` but emits `MODULE_TYPELESS_PACKAGE_JSON` because
  `@chirality/harness-contract/package.json` lacks `"type": "module"`.
  This is a warning, not a failed import or identity mismatch.
- `npm ci` reported one high-severity dependency audit finding. No audit fix
  was attempted because that would change lockfile-governed state and is
  outside this evidence-only audit.
- The audit supports evidence-gated disposition of D-APP-49 but does not rule
  facade retirement, decide D-APP-48, change version identity, or authorize
  implementation.
