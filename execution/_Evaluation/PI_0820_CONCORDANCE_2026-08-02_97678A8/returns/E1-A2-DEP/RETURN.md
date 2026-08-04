# E1-A2-DEP — Pi 0.82.0 dependency and supply-chain audit

RUN_STATUS: `PASS_WITH_DISTRIBUTION_AND_REPRODUCIBILITY_GAPS`

Repository basis: `97678a841ef58345c73d3470ed8de57c9b1405d2`.
This is read-only evaluation evidence. It does not approve Pi `0.82.0`,
supersede D-APP-72, authorize release, or close `TM-ROOT-106`.

## Executive finding

The committed App dependency state closes exactly on the published
`@earendil-works/pi-coding-agent@0.82.0` graph:

- all four App-declared Pi packages are exact `0.82.0` pins;
- the coding-agent subtree contains the same 139 nested entries as the
  package's cached, SRI-verified published `npm-shrinkwrap.json`, with zero
  missing entries and zero version or resolved-URL mismatches;
- the coding-agent plus its nested subtree is 140 unique package identities;
  all 140 resolve from `https://registry.npmjs.org/`, all 140 carry SHA-512
  lock integrity, and all 140 locally cached tarball bytes hash to the
  committed SRI;
- the three nested Pi sibling artifacts whose published shrinkwrap omits SRI
  are strengthened in the App lock with the identical SRI of their exact
  top-level pin; and
- the committed verifier passes with the expected two-package install-script
  allowlist.

This proves the committed lock and the cached artifacts reviewed here. It is
not a fresh-install proof. `frontend/node_modules/` is absent and the brief
forbids installation or other subject writes, so no `npm ci`, module import,
or packaged execution was performed. The present Pi notice also expressly
covers only the four Pi-owned packages, not the full redistribution closure.

## Root/App resolution boundary

| Surface | Observed state | Result |
|---|---|---|
| Root runtime | `runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts:10-11` names coding-agent `0.82.0`, but the package manifest depends only on `@chirality/runtime-contracts` (`runtime/packages/engine-pi-omlx/package.json:14-16`; mirrored in `runtime/package-lock.json:1740-1745`). | `QUALIFIED_PASS`: Root carries a descriptor/injected-runtime contract, not a standalone Pi package resolution. |
| App composition | The App links the Root engine package and directly pins the four Pi publications (`projects/chirality-app-dev/frontend/package.json:42,49-52`). Its production adapter imports coding-agent (`projects/chirality-app-dev/frontend/src/lib/harness/pi-agent-engine-adapter.ts:496-531`) and advertises `0.82.0` (`:23-24,654-660`). | `PASS`: the App lock is the executable Pi dependency owner in this snapshot. |

The distinction matters: Root's `0.82.0` constant does not independently
close a registry dependency. Executable package closure is supplied by the
App consumer lock. This is a dependency fact, not a judgment about whether
that composition is governed or approved.

## Exact graph, version, provenance, and integrity map

### Direct App declarations and exact artifacts

The App manifest and lock root declare all four Pi packages exactly at
`0.82.0` (`projects/chirality-app-dev/frontend/package.json:49-52`;
`projects/chirality-app-dev/frontend/package-lock.json:23-26`).

| Package | Declared | Resolved artifact | SHA-512 integrity |
|---|---:|---|---|
| `@earendil-works/pi-agent-core` | `0.82.0` | `https://registry.npmjs.org/@earendil-works/pi-agent-core/-/pi-agent-core-0.82.0.tgz` | `sha512-bnS9DpOKK5T/F/gQkaOnYdMsuuciWiScfAHHWC+k5OQ0HxjSqMFQvp8keurULLoT4+v8NHv4V14pNvd4hsfC0Q==` |
| `@earendil-works/pi-ai` | `0.82.0` | `https://registry.npmjs.org/@earendil-works/pi-ai/-/pi-ai-0.82.0.tgz` | `sha512-8MvW9+zno13sXDuT2kFMnWeTNUufUhPeZDRVO+igGoBRCDWgn7Xh2FkRQI1mRuet6QhF4ENQuLYdIAOyG6BhNw==` |
| `@earendil-works/pi-coding-agent` | `0.82.0` | `https://registry.npmjs.org/@earendil-works/pi-coding-agent/-/pi-coding-agent-0.82.0.tgz` | `sha512-Qnqgn9zhJFQ2HZ8R4iNuGhyCk93XX6+eUw9i+TjTuo47amzCy93ft3bB6yaUCleCrNO58dJDHYSGNHv/GAPWKg==` |
| `@earendil-works/pi-tui` | `0.82.0` | `https://registry.npmjs.org/@earendil-works/pi-tui/-/pi-tui-0.82.0.tgz` | `sha512-9IDjQOXne7t9l2s2YcjnIBxsVNVPE7qScVSB3YmFlXsBW4pfo2gOElTxggV84KrRiGqABnlFPBWbf0k54hszHQ==` |

The first three lock entries are at
`projects/chirality-app-dev/frontend/package-lock.json:720-784`; the top-level
TUI entry is at `:2603-2614`.

### Pi-owned dependency edges

The published and committed edges agree:

- `pi-coding-agent@0.82.0` declares
  `pi-agent-core@^0.82.0`, `pi-ai@^0.82.0`, `pi-tui@^0.82.0`,
  `photon-node@0.3.4`, `chalk@5.6.2`, `cross-spawn@7.0.6`,
  `diff@8.0.4`, `glob@13.0.6`, `highlight.js@10.7.3`,
  `hosted-git-info@9.0.3`, `ignore@7.0.5`, `jiti@2.7.0`,
  `minimatch@10.2.5`, `proper-lockfile@4.1.2`, `semver@7.8.0`,
  `typebox@1.1.38`, `undici@8.5.0`, and `yaml@2.9.0`, with optional
  `@mariozechner/clipboard@0.3.9`
  (`projects/chirality-app-dev/frontend/package-lock.json:781-815`).
- nested `pi-agent-core@0.82.0` resolves `pi-ai@^0.82.0`, `diff@8.0.4`,
  `ignore@7.0.5`, `typebox@1.1.38`, and `yaml@2.9.0`
  (`projects/chirality-app-dev/frontend/package-lock.json:1252-1266`).
- nested `pi-ai@0.82.0` resolves its exact provider/transport dependency set
  including Anthropic `0.91.1`, Bedrock `3.1048.0`, Google GenAI `1.52.0`,
  Mistral `2.2.6`, OpenAI `6.26.0`, and Smithy HTTP `4.7.3`
  (`projects/chirality-app-dev/frontend/package-lock.json:1268-1292`).
- nested `pi-tui@0.82.0` resolves `get-east-asian-width@1.6.0` and
  `marked@18.0.5` (`projects/chirality-app-dev/frontend/package-lock.json:1293-1304`).

### Complete transitive identity map

The exact map is the continuous coding-agent lock subtree beginning at
`projects/chirality-app-dev/frontend/package-lock.json:781` and ending at
`:2602`. It contains 140 resolved entries: the coding-agent root plus 139
nested entries. There are 140 unique package names and 140 unique
name/version pairs. For a reproducible compact identity of that full map, the
canonical serialization

```text
sort by lock path; for each entry emit:
<lock-path>\t<version>\t<resolved>\t<integrity>\n
```

has SHA-256:

```text
8fb3458ddafdbc861c5fc541775bddf2a2832d30476c78c2866535a4416fbc96
```

The cached published coding-agent tarball is itself bound by the coding-agent
SRI above. Its `npm-shrinkwrap.json` contains 139 non-root entries. A
field-by-field comparison to the App nested subtree returned:

```text
published nested entries:      139
App nested resolved entries:   139
missing entries:                 0
version mismatches:              0
resolved-URL mismatches:         0
integrity differences:           3
```

All three integrity differences are strengthening-only: the upstream
shrinkwrap omits SRI for nested `pi-agent-core`, `pi-ai`, and `pi-tui`, while
the App lock supplies the exact SRI from the identical top-level
version/resolved artifact (`projects/chirality-app-dev/frontend/package-lock.json:1252-1304`).
The normalizer encodes that equality and conflict check
(`projects/chirality-app-dev/frontend/scripts/normalize-pi-lock-integrity.mjs:29-51`).

The four direct lock paths plus 139 nested paths therefore produce 143
Pi-relevant lock paths but only 140 unique artifact identities; the three Pi
siblings are deliberately represented both top-level and nested with
identical URL and SRI.

## Integrity and provenance validation

| Check | Result | Evidence |
|---|---|---|
| Registry provenance | `PASS` — 140/140 coding-agent closure entries use HTTPS npm registry URLs. | Lock subtree `projects/chirality-app-dev/frontend/package-lock.json:781-2602`; verifier rule at `scripts/verify-pi-supply-chain.mjs:37-53`. |
| Lock integrity | `PASS` — 140/140 closure entries have `sha512-` SRI; all four exact direct pins also have registry SHA-512 locks. | Verifier output and rules at `scripts/verify-pi-supply-chain.mjs:22-53`. |
| Cached artifact bytes | `PASS` — 140/140 content-addressed cached tarballs were present and recomputed SHA-512 matched the committed SRI; 0 missing, 0 mismatched. | Offline read of `/Users/ryan/.npm/_cacache/content-v2/sha512/`, addressed from each lock SRI; no registry request or cache write. |
| Published graph concordance | `PASS` — 139/139 shrinkwrap entries reproduced; no version/resolution mismatch. | Cached coding-agent tarball bound by lock SRI; App lock subtree cited above. |
| Normalization convergence | `PASS` — pure `normalizePiLockIntegrity(lock)` returned `changes: []`. | Pure function at `scripts/normalize-pi-lock-integrity.mjs:26-53`; file-writing wrapper at `:56-67` was not invoked. |
| Source notice | `PASS_WITH_LIMIT` — the notice binds the four Pi packages to the tagged upstream license URL. | `projects/chirality-app-dev/frontend/THIRD_PARTY_NOTICES_PI.md:3-10,34`. |

Relevant committed file hashes at the frozen snapshot:

| File | SHA-256 |
|---|---|
| `runtime/package.json` | `499cb55afb26bdbaa36f85178c28d392bfa2527b60a002e4eb0ae0e076402071` |
| `runtime/package-lock.json` | `4105799bbdb8a1b5025a71a0098e460281f8e6db62b1a912d37aade2935a7c0f` |
| `runtime/packages/engine-pi-omlx/package.json` | `e6ab3d1bac2683779f5e568f65ef9f83c1b255e9f8beb0ee1a6136fc9f871fcc` |
| `runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts` | `531f69c42c87d799b2b9aecec4bbfb96e2a1210dcd17135542c3483b48a9c208` |
| `projects/chirality-app-dev/frontend/package.json` | `1e62d22ec4a07fb225352c90ddfa5ce41d736d3d169e04cf7bd3684e54557c9c` |
| `projects/chirality-app-dev/frontend/package-lock.json` | `674fe2dab74572f21d26455498461d62eaa4218560e45024ed2a31e00c635ab8` |
| `projects/chirality-app-dev/frontend/scripts/verify-pi-supply-chain.mjs` | `912a07d5db0d574c3de3acd69898b6567612fbc456807902b83c0a5c38165b7e` |
| `projects/chirality-app-dev/frontend/THIRD_PARTY_NOTICES_PI.md` | `0195b5ce8b7be8b6bff6de3e50f6a38b3d9d4919c075e7c93ca8118b7e866328` |

## Install lifecycle review

The lock flags exactly two install-script packages inside the coding-agent
closure, matching the committed allowlist
(`projects/chirality-app-dev/frontend/package-lock.json:1306-1328,2374-2395`;
`projects/chirality-app-dev/frontend/scripts/verify-pi-supply-chain.mjs:55-62`):

| Package | Locked lifecycle | Offline static result |
|---|---|---|
| `@google/genai@1.52.0` | `preinstall` | `echo 'preinstall: no-op'`; no operation beyond shell output. |
| `protobufjs@7.6.5` | `postinstall` | Shipped `scripts/postinstall.js` reads package manifests and may write an API-compatibility warning to stderr; no network, subprocess, or file write is present in the reviewed script. |

The inspected package manifests and postinstall source came from cached
tarballs whose bytes passed the SRI check above. No lifecycle script was
executed.

## Commands and results

All commands below were read-only. The first attempted analysis command used
an incorrect cwd-relative lock path and failed `ENOENT`; it changed nothing
and was rerun with `package-lock.json`.

1. `git rev-parse HEAD` ->
   `97678a841ef58345c73d3470ed8de57c9b1405d2`.
2. Static `find`, `rg`, `nl`, `shasum -a 256`, and Node JSON reads inventoried
   the Root/App manifests, lockfiles, adapter, verifier, normalizer, notice,
   and prior audit evidence.
3. `node scripts/verify-pi-supply-chain.mjs` from `frontend/` ->
   `PASS`, package `@earendil-works/pi-coding-agent@0.82.0`, 140 closure
   artifacts, install-script allowlist `[@google/genai, protobufjs]`,
   `sha512-enforced`, explicit ASAR native/WASM policy, notice present.
4. `npm ls @earendil-works/pi-coding-agent @earendil-works/pi-agent-core
   @earendil-works/pi-ai @earendil-works/pi-tui --all --package-lock-only
   --json` -> all direct and nested Pi identities resolve at `0.82.0`; no
   dependency problem was reported. `--package-lock-only` avoided an install.
5. Imported the normalizer and invoked only
   `normalizePiLockIntegrity(JSON.parse(package-lock))` -> `changes: []`.
   The CLI wrapper can write `package-lock.json`, so it was deliberately not
   invoked.
6. Offline Node SHA-512 pass over all 140 SRI-derived cacache paths ->
   `cached=140`, `missingFromCache=0`, `hashMismatch=0`.
7. `tar -xOf` reads of the SRI-verified coding-agent, Google GenAI, and
   protobufjs cached tarballs supplied the shrinkwrap and lifecycle evidence;
   no extraction to disk occurred.
8. Final containment check: this dispatch wrote only this `RETURN.md`.
   Other modified/untracked paths reported by `git status --short` belong to
   concurrent parent/sibling lanes and were neither read as mutable authority
   nor modified by this child.

## Findings

### DEP-082-F01 — `PASS` — exact Pi dependency closure

The App declares four exact `0.82.0` Pi pins, resolves the coding-agent's full
published 139-entry nested graph without version or source drift, and has no
ambiguous Pi package identity. The Root engine descriptor and App package
owner agree on `0.82.0`, while remaining distinct resolution surfaces.

### DEP-082-F02 — `PASS` — lock and cached-byte integrity

Every unique artifact in the 140-entry coding-agent closure has registry
SHA-512 enforcement and the locally cached bytes match. The prior class of
three missing nested Pi SRIs is closed in the committed App lock by a
deterministic equality-checked normalization.

### DEP-082-F03 — `PASS` — bounded install-script set

The closure has exactly the two allowlisted lifecycle packages. Offline static
inspection found only a no-op preinstall and a manifest-reading,
stderr-warning postinstall. This finding is version-bound to the exact SRIs
above.

### DEP-082-F04 — `FAIL_FOR_DISTRIBUTION` — full-closure notices absent

The verifier's `notice: present` result is intentionally narrower than release
readiness. It checks the four Pi names and upstream copyright only
(`projects/chirality-app-dev/frontend/scripts/verify-pi-supply-chain.mjs:77-87`).
The notice itself says it covers only those four packages and requires a full
packaged-dependency notice before redistribution
(`projects/chirality-app-dev/frontend/THIRD_PARTY_NOTICES_PI.md:36-38`). No
complete 140-artifact notice inventory was found in the declared context.

### DEP-082-F05 — `UNKNOWN` — clean-install reproducibility

All necessary tarballs are present and SRI-valid in this machine's cache, but
no isolated `npm ci --offline` was run because it would write an install tree.
Accordingly, this audit does not claim install lifecycle success, realized
module topology, source-tree import, Electron ABI fitness, packaged loading,
or runtime behavior.

### DEP-082-F06 — `NOT_APPROVAL`

Package bytes, manifests, lock entries, cached hashes, and passing scripts are
technical evidence only. They cannot settle the conflict between App's
governing `0.80.10` decision basis and present `0.82.0` executable state.
The manager must combine this return with the governance child and obtain the
required supersession/retention/rejection decision.

## Gaps, blockers, and reruns

- **Decision blocker:** an accepted decision record is still required before
  present `0.82.0` bytes can be relied on as approved state.
- **Distribution blocker:** generate and verify notices/license texts for the
  exact packaged production closure, not only the four Pi-owned packages.
- **Reproducibility rerun:** in a disposable checkout or other expressly
  authorized write target, run an isolated `npm ci --offline` from the frozen
  lock/cache, preserve its log and resulting `npm ls --all`, then rerun
  `npm run pi:supply-chain`. Confirm the subject checkout remains unchanged.
- **Artifact rerun:** repeat the 140-entry SRI-derived cache-byte check if the
  lock hash changes; the current full-map digest and source hashes then cease
  to apply.
- **Lifecycle rerun:** re-audit the install-script allowlist and exact script
  bytes whenever any closure identity changes.
- **Packaging/runtime boundary:** consume the independent structure/runtime
  evidence before claiming ASAR/native/WASM or packaged-turn fitness; this
  child did not execute those surfaces.

No source repair, lock edit, install, network resolution, cache mutation,
decision write, register change, or Git operation was performed.
