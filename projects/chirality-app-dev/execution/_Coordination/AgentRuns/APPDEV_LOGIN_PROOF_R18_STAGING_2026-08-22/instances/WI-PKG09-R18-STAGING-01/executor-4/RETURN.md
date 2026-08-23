# A2-PKG09-R18-IMPLEMENT-04 return

RUN_STATUS: `FAILED — OFFLINE BUILD PASS; FULL-SUITE LOCAL-BIND VALIDATION BLOCKED`

## Basis and scope

- Parent: `WI-PKG09-R18-STAGING-01`
- Branch / HEAD: `codex/app-login-proof-r18-staging` /
  `f59105ddb606bd46397c3b1aafa41b50ab4e9e8d`
- HEAD parents: `166efa82748133e90674be62304b81f8a0a8c1b4`,
  `b143444bd497eae1b1b638670a33e6df756d9084`
- Current `origin/main`: `b143444bd497eae1b1b638670a33e6df756d9084`
- Index: empty
- Write containment: all executor-owned paths are under
  `projects/chirality-app-dev/`

## Source evidence

The active Electron Builder downloader is the nested
`frontend/node_modules/app-builder-lib/node_modules/@electron/get` version
3.1.0. Its CJS `dist/cjs/index.js`, SHA-256
`d81c9a2354bb2769b4d8205b04c991aef2e93b79e7e3d1e792663aee5813ac4f`,
lines 59–70 retrieves `SHASUMS256.txt` with
`cacheMode: ElectronDownloadCacheMode.Bypass`. The top-level `@electron/get`
5.0.0 is unrelated to the active Electron Builder path.

The accepted official SHASUMS response is 7,610 bytes with SHA-256
`823ec97893f00c3ab2a4d44811bc75f7dd582ff6086407109a179c2184c5702d`
and contains exactly once:

```text
ad4a0ae3c37ee05aa06c7e2ed0627608389790f0505a2b0d20319efbe33ffe28 *electron-v43.2.0-darwin-arm64.zip
```

The staged archive is a regular non-symlink 122,090,802-byte file with that
same SHA-256. The production verifier passed against the exact default
`/Users/ryan/Library/Caches/chirality/electron-dist`.

## Implementation and frozen hashes

| Path | SHA-256 |
|---|---|
| `frontend/scripts/verify-electron-dist.mjs` | `e4e9aa12c5a8898b010a4ea38a2c8854a6315db3eff02f2e9f3d87560f8d8457` |
| `frontend/scripts/pack-electron-with-supply.mjs` | `08f56566dc2436f0d9968c3d71ea792c4cc7782ed6a98e892fd4113136a4b3db` |
| `frontend/src/__tests__/scripts/verify-electron-dist.test.ts` | `c9c4af600a703afa995f8316ee04eb3160d72ef7f8cba8ec2ce53c7f952cb38d` |
| `frontend/src/__tests__/scripts/pack-electron-with-supply.test.ts` | `a66af130420412e5a3d9cf48856c1b416234fea5aa78e14e3867b4adfd7664e2` |
| `frontend/package.json` | `17c87d523d5291b52ed0c4a57ad2695b9c50df76cf4c11e4d25e5a4fd02ad0cc` |
| `DEL-09-04/_run_records/R18_ELECTRON_SUPPLY_FREEZE_AND_OFFLINE_BUILD_2026-08-22.md` | `f8a8c800bfdbadb27cac19582e749390c422614abfe59982f903317d02569659` |
| `DEL-09-04/_STATUS.md` | `fbf0cdb1cf3338dc6765a6f5157b349736edeef08703b0327478ffbcd343244e` |
| `executor-4/desktop-pack.full.log` | `e7f1ec32a50444c260697ca5bd9e4b10325cf4a1e61d95831331173f84f49b9f` |
| `executor-4/desktop-pack.exit-status.txt` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` |
| `executor-4/prebuild-dist-inventory.md` | `2d40368f69343e54dc303cf79a4fa04f18909f4f0673e1a677c2cd71cde6a093` |

`frontend/package-lock.json` remained unchanged; its SHA-256 is
`717d541fe6ee090aae79d4a386bbde1c8ff6ee136a50242d956500d76e80a458`.

## Single offline package command

Evidence was initialized first. Exactly one new post-implementation command
ran in the ordinary network-denied sandbox, without escalation or retry:

```text
npm run desktop:pack
```

Exit was 0. The complete log records `using custom electronDist directory`,
the exact staged path, dependency-boundary `PASS`, instruction-root `pass`, 43
files, and exact basis SHA. A case-insensitive log scan found no `download`,
`github.com`, or `release-assets.githubusercontent.com`. The build allowance
is consumed; no second package attempt is permitted.

The ignored output is derivative evidence only and is not adopted as package
identity or proof. Observed main/CLI hashes remain
`79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`
and
`0503c40afde2e3bc2522405305893698f5742687139d00e2fda7995a567af989`.

## Checks

| Check | Result |
|---|---|
| syntax | PASS |
| focused supply/argv tests | PASS — 9/9 |
| typecheck | PASS |
| production supply verifier | PASS |
| offline package JSON/lock dry run | PASS — up to date |
| instruction-root integrity | PASS |
| APP-HOLD | PASS — 53 contracts |
| practitioner self-check | PASS — exit 0 at current non-blocking baseline |
| practitioner pytest | PASS — 350/350 |
| prior-ledger receipt validator | PASS; Receipt ledger unchanged |
| tracked diff whitespace / empty index / App containment | PASS |
| full frontend Vitest, ordinary sandbox | ENVIRONMENT-LIMITED — 1,246 passed / 4 skipped; 21 local TCP/Unix-socket tests failed only with `listen EPERM` |

## Blocker, reruns, and handoff

The only blocker is the full-suite local-bind restriction. No product failure
was observed, but the executor had absolute no-network authority and did not
escalate to an unsandboxed rerun. Manager fan-in must hold or obtain an
authorized local-socket-only validation path; the package command must not be
repeated. Any source/test/R18/status/return repair requires affected checks,
new hashes, and a fresh evidence-only reviewer after final bytes freeze.

DEL-09-04 remains `IN_PROGRESS` and unproved. R18 is a supply-freeze precursor
and offline build record only. R19 remains a separate post-merge owner act.
No Receipt 189, staging, commit, push, PR, merge, proof procedure, proof act,
operator mutation, signing, notarization, deployment, distribution, or release
claim occurred.
