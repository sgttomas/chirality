# R18 — Electron supply freeze and offline evidence build

Date: 2026-08-22
Branch: `codex/app-login-proof-r18-staging`
Exact synchronized basis: `f59105ddb606bd46397c3b1aafa41b50ab4e9e8d`
Basis parents: `166efa82748133e90674be62304b81f8a0a8c1b4`,
`b143444bd497eae1b1b638670a33e6df756d9084`
Disposition: `SUPPLY-FREEZE PRECURSOR / OFFLINE BUILD EVIDENCE ONLY`
Deliverable state: `IN_PROGRESS`, unproved

## Claim boundary

This record freezes the Electron 43.2.0 arm64 supply input, implements a
fail-closed verifier and argv-safe Electron Builder wrapper, and preserves one
successful offline package-command transcript. The ignored package output is
not adopted, package-identified, staged as a proof procedure, or accepted as
proof. R19 is a separate owner-authorized post-merge tranche. No GUI, prepare,
capture, logout/login, bootstrap, kickstart, operator/default job, plist or
launcher action, signing, notarization, deployment, distribution, publication,
release-readiness, proof acceptance, Receipt 189, stage, commit, push, PR, or
merge occurred in this executor run.

## Prior attempts and accepted network evidence

1. The first exact `npm run desktop:pack` attempt at
   `166efa82748133e90674be62304b81f8a0a8c1b4`, with npm offline mode in the
   ordinary restricted sandbox, completed source builds and then failed at
   Electron Builder packaging with exit 1 and `getaddrinfo ENOTFOUND
   github.com`. Its intended full log was not persisted because the evidence
   directory initialization failed first; only the governed transcript,
   bounded failure summary, and exit record survive. No retry occurred in that
   attempt.
2. Attempt 2 made one authorized GitHub request with redirects disabled. It
   received terminal HTTP 302, zero body bytes, and a redirect host of
   `release-assets.githubusercontent.com`; it stopped before implementation or
   build. Its sanitized response evidence retains no signed query.
3. Accepted attempt 3 made one curl invocation and exactly two HTTPS requests:
   `github.com` returned 302 and `release-assets.githubusercontent.com`
   returned 200. Exactly one redirect was followed. The 7,610-byte ASCII body
   has SHA-256
   `823ec97893f00c3ab2a4d44811bc75f7dd582ff6086407109a179c2184c5702d`
   and contains exactly once the official line:

```text
ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28 *electron-v43.2.0-darwin-arm64.zip
```

The official source URL is
`https://github.com/electron/electron/releases/download/v43.2.0/SHASUMS256.txt`.
No artifact request or other host was used. The synchronized merge basis named
above was then owner-authorized and completed non-rewriting; its second-parent
App delta is empty.

## Active local cause

Electron Builder 26.15.3 resolves its active downloader through
`frontend/node_modules/app-builder-lib/node_modules/@electron/get`, version
3.1.0. Its local CJS source
`dist/cjs/index.js`, SHA-256
`d81c9a2354bb2769b4d8205b04c991aef2e93b79e7e3d1e792663aee5813ac4f`,
lines 59–70 downloads `SHASUMS256.txt` and explicitly sets
`cacheMode: ElectronDownloadCacheMode.Bypass`, with the adjacent comment that
checksums are loaded fresh every time. This explains the first attempt's
GitHub contact despite an Electron archive cache hit. The top-level
`frontend/node_modules/@electron/get` is version 5.0.0 and is not Electron
Builder's active nested path.

## Staged archive gates

The owner-staged default directory is
`/Users/ryan/Library/Caches/chirality/electron-dist`. Read-only inspection and
the production verifier establish that the directory is a non-symlink
directory and that `electron-v43.2.0-darwin-arm64.zip` is a regular,
non-symlink 122,090,802-byte file with streaming SHA-256
`ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28`.
The archive identity exactly matches the official line above.

## Supply-freeze implementation

- `frontend/scripts/verify-electron-dist.mjs` pins Electron 43.2.0, the exact
  filename, byte size, hash, official line, and source URL. It requires the
  exact package devDependency version, resolves a literal
  `CHIRALITY_ELECTRON_DIST_DIR` or the fixed home-relative default, rejects
  empty/NUL/non-absolute/non-normalized/root paths, requires lstat/realpath-safe
  directory and archive containment, streams the hash, exposes no CLI pin
  override, prints only the resolved directory on success, and fails nonzero
  on stderr.
- `frontend/scripts/pack-electron-with-supply.mjs` obtains the verified
  directory before spawning Electron Builder with `shell: false` and exactly
  one `-c.electronDist=<directory>` argv entry. A path containing spaces stays
  one argument. It preserves unsigned packaging through
  `CSC_IDENTITY_AUTO_DISCOVERY=false`.
- `frontend/package.json` adds `electron:supply-chain` and retains the
  `desktop:pack` name, production build, dependency-boundary gate, and
  instruction-root gate. `desktop:dist` is unchanged. The package lock needed
  no mechanical update.
- Focused fixture tests cover success stdout-only, missing archive, archive
  symlink, wrong size before hashing, wrong hash, Electron version drift,
  unsafe paths, no CLI pin bypass, and exact path-with-spaces argv behavior
  without repeatedly hashing the 122 MB archive.

## Single offline evidence build

Executor-4 initialized its return, full log, exit record, and a pre-build
ignored-dist inventory before executing exactly once, from `frontend`:

```text
npm run desktop:pack
```

The command ran in the ordinary network-denied sandbox without escalation or
retry and exited 0. The complete log is
`execution/_Coordination/AgentRuns/APPDEV_LOGIN_PROOF_R18_STAGING_2026-08-22/instances/WI-PKG09-R18-STAGING-01/executor-4/desktop-pack.full.log`,
SHA-256
`e7f1ec32a50444c260697ca5bd9e4b10325cf4a1e61d95831331173f84f49b9f`.
It records Electron Builder 26.15.3, Electron 43.2.0 arm64, and:

```text
using custom electronDist directory  electronDist=/Users/ryan/Library/Caches/chirality/electron-dist
```

The log has no case-insensitive `download`, `github.com`, or
`release-assets.githubusercontent.com` indicator. Embedded packaged-dependency
boundary returned `PASS`; instruction-root integrity returned `pass` for 43
checked files and exact Git SHA
`f59105ddb606bd46397c3b1aafa41b50ab4e9e8d`.

The output remains ignored derivative evidence only. The main executable hash
`79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
and runtime CLI hash
`0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`
are recorded only as post-command observations and are not an adopted package
identity or proof basis.

## Validation matrix

| Check | Result |
|---|---|
| verifier/wrapper syntax | PASS |
| focused supply and argv tests | PASS — 9/9 |
| frontend typecheck | PASS |
| production verifier against staged default | PASS |
| package JSON/lock dry-run consistency | PASS — offline and up to date |
| instruction-root integrity | PASS — 43 files; exact synchronized basis |
| APP-HOLD `scan --require-register-match` | PASS — 53 contracts |
| repository practitioner `self-check` | PASS — exit 0 at current calibrated non-blocking baseline |
| practitioner-harness pytest | PASS — 350/350 |
| prior-ledger App receipt validator | PASS; ledger unchanged |
| full frontend Vitest diagnostic in ordinary sandbox | `ENVIRONMENT_SANDBOX_SOCKET_DENIAL`, not PASS — exit 1; 21 failed / 1,246 passed / 4 skipped; local TCP/Unix-socket `listen EPERM` only |
| exact owner-authorized `npm test` cure with local test-socket permission | PASS — exit 0; 1,267 passed / 4 skipped |

The diagnostic log remains preserved at `review-1/full-vitest.log`, SHA-256
`8e10b2cab4a156f7254c5555ccf1eb823af24e57f8b6e6f86ed1cd677496ca19`,
and is not upgraded to PASS. The exact cure command ran once from `frontend`
with local loopback/Unix-socket bind permission and network forbidden. Its
complete whitespace-normalized 485-byte log is
`repair-cycle-1/full-suite-cure/npm-test.unrestricted.log`, SHA-256
`f7313d0e79460d09de5b09f055e75c7a7fc8d9561a6ed238ce1a4ae6bf68cb92`.
The five semantic candidate hashes and complete 16,238-byte frontend candidate
diff, SHA-256
`12d4ccf9e4de7b0924cfdbf7af6db2e3da9fcf2761eaa5cc49f9dd20d8568b1e`,
are exact before/after matches, proving no source, test, or package-script
change between runs. The PR pre-merge release-quality wrapper's `full_test`
plus typecheck remains future independent confirmation of record and has not
yet been observed. No second package attempt is permitted or required.
Candidate whitespace, diff, containment, inventory, hash, and empty-index
checks run after all record bytes freeze.

## Status and handoff

R17 repair is merged. This R18 candidate is a supply-freeze precursor and one
offline evidence build, not a login-proof attempt or owner procedure. DEL-09-04
remains `IN_PROGRESS` and unproved. Fresh evidence-only review is required
after final byte freeze; it consumes the retained diagnostic and cure evidence
without an additional unrestricted test run. R19 requires separate owner
authorization after this tranche merges. Any change to the supply constants,
package dependency, verifier/wrapper/tests, build log, R18/status, or
synchronized basis requires the affected deterministic checks and a fresh
review; the package command may not be repeated under this tranche.
