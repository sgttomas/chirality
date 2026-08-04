# E1-A2-STRUCT Return — Pi 0.82.0 lifecycle, packaging, and conformance

Dispatch: `E1-A2-STRUCT`
Role: `EVALUATION_STRUCTURE_AUDIT`
Repository snapshot: `97678a841ef58345c73d3470ed8de57c9b1405d2`
Posture: `COMPLETE / READ-ONLY EVALUATION / NOT APPROVAL`

## Verdict

The frozen source proves exact Pi `0.82.0` declarations, SHA-512-protected npm
closure metadata, a two-package install-script allowlist, explicit native/WASM
ASAR-unpack patterns, a packaged Pi-owned notice, App-side Pi adapter identity,
and CI execution of the supply-chain verifier plus the full frontend test suite.
The fresh read-only supply-chain verifier passed over 140 closure artifacts.

It does **not** prove a frozen-head `0.82.0` packaged production turn or exact
native/WASM asset loadability. The advertised
`harness:validate:pi-packaged-proof` command enters `runParent()`, whose child
spawn selects `--legacy-asset-child`; the separate `runChild()` production-route
proof is present but is never spawned by that command. No packaged app or
packaged-Pi summary exists in this worktree. Historical production-route proof
is explicitly for Pi `0.80.10`; later packaged-daemon evidence exposes a
`0.82.0` descriptor but does not execute a Pi turn. The four-package Pi notice
also explicitly says the full packaged dependency-closure notice remains owed.

Consequently, lifecycle/packaging/conformance evidence is **PARTIAL** and cannot
support approval, reliance, release, or supersession of the governing
`0.80.10` decision.

## Commands and results

| Command / inspection | Result | Classification |
|---|---|---|
| `git rev-parse HEAD` | `97678a841ef58345c73d3470ed8de57c9b1405d2` | Frozen-head identity proven. |
| `npm run pi:supply-chain` from `projects/chirality-app-dev/frontend` | **PASS**: `@earendil-works/pi-coding-agent@0.82.0`; 140 closure artifacts; install scripts `@google/genai`, `protobufjs`; SHA-512 enforced; explicit native/WASM policy; Pi notice present. | Fresh frozen-head structural evidence. The verifier reads manifests/lock/notice only; it does not install, package, load assets, or run Pi. |
| Node read-only lock inspection | Exactly two closure entries have `hasInstallScript: true`: nested `@google/genai@1.52.0` and `protobufjs@7.6.5`; both use HTTPS npm URLs and SHA-512 lock integrity. | Fresh frozen-head metadata evidence, not script-body or execution evidence. |
| Static entrypoint inspection of `run-packaged-pi-runtime-proof.mjs` | `runParent()` spawns `--legacy-asset-child`; `runChild()` is reachable only through an explicit `--child` invocation and has no parent spawn. | Fresh frozen-head proof-command defect/gap. |
| Filesystem inspection | `frontend/node_modules`, `frontend/dist/mac-arm64/Chirality.app`, and `frontend/artifacts/harness/packaged-pi/latest/summary.json` are absent. | No local frozen-head package or packaged proof is available. |
| Focused Vitest attempt over Pi lock, packaging, adapter, mapper, runtime, conformance, and wire-integration suites | **NOT RUN**. `npm exec vitest` found no local binary and attempted a registry fetch, which failed with `ENOTFOUND`. No install was authorized or performed. | Blocked rerun, not a product failure and not a PASS. |
| `git status --short` containment check | Only concurrent parent-run lane changes and the parent evaluation/run directories are visible; this child wrote only this `RETURN.md`. | Write containment held. |

Relevant frozen-file SHA-256 values:

| File | SHA-256 |
|---|---|
| `projects/chirality-app-dev/frontend/package.json` | `1e62d22ec4a07fb225352c90ddfa5ce41d736d3d169e04cf7bd3684e54557c9c` |
| `projects/chirality-app-dev/frontend/package-lock.json` | `674fe2dab74572f21d26455498461d62eaa4218560e45024ed2a31e00c635ab8` |
| `projects/chirality-app-dev/frontend/THIRD_PARTY_NOTICES_PI.md` | `0195b5ce8b7be8b6bff6de3e50f6a38b3d9d4919c075e7c93ca8118b7e866328` |
| `projects/chirality-app-dev/frontend/scripts/verify-pi-supply-chain.mjs` | `912a07d5db0d574c3de3acd69898b6567612fbc456807902b83c0a5c38165b7e` |
| `projects/chirality-app-dev/frontend/scripts/run-packaged-pi-runtime-proof.mjs` | `7354e0af73f40e308a5204fe04621a4db0c6e68c964065bb1f029d0aeec5674f` |
| `projects/chirality-app-dev/frontend/src/lib/harness/pi-agent-engine-adapter.ts` | `34c8fd0978741720e74ba36beb3fdc7c9a06f31ed55b7da87c86525ac39c47ca` |
| `runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts` | `531f69c42c87d799b2b9aecec4bbfb96e2a1210dcd17135542c3483b48a9c208` |
| `.github/workflows/harness-premerge.yml` | `7cdceb88c454dd077b2111398978191762ed2c78018122782219046843932d73` |

## Evidence matrix

| Lens | Frozen-head evidence | Proven | Historical / weaker evidence | Missing or blocked |
|---|---|---|---|---|
| Exact Pi identity | `frontend/package.json:49-52`; `frontend/package-lock.json:720-790,1293-1305,2603-2614`; `frontend/src/lib/harness/pi-agent-engine-adapter.ts:23-24,654-669`; `runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts:10-11,34-48` | Four direct Pi packages and both App/Root descriptors say `0.82.0`. | The daemon-service packaged status records expose `packageVersion: 0.82.0` at `APPDEV_DAEMON_SERVICE_2026-07-25/.../V-PACKAGED-DRILLS/evidence/v2/daemon-status.json:48-60`, but only as descriptor inventory. | Descriptor agreement is not package execution or approval. |
| Lock closure and integrity | `frontend/scripts/verify-pi-supply-chain.mjs:22-53`; lock entries beginning at `frontend/package-lock.json:781` | Fresh verifier PASS: 140 resolved closure artifacts, all HTTPS npm and SHA-512 protected. | `frontend/src/__tests__/scripts/pi-lock-integrity.test.ts:18-67` defines normalization and whole-closure assertions. | Focused test rerun blocked by absent installed dependencies. |
| Install/lifecycle scripts | `verify-pi-supply-chain.mjs:55-62`; `package-lock.json:1306-1320,2374-2395` | The lock metadata allowlist is exactly nested `@google/genai` and `protobufjs`. | Prior `0.80.10` audit describes the same allowlist, but does not prove `0.82.0`. | No installed package manifests/script bodies and no install execution were inspected; allowlist membership alone does not prove lifecycle behavior or absence of runtime-generated effects. |
| Native/WASM policy | `frontend/package.json:88-100`; `verify-pi-supply-chain.mjs:64-75`; `frontend/src/__tests__/scripts/dmg-packaging-policy.test.ts:98-113` | Explicit ASAR-unpack patterns cover nested Pi `.node`/`.wasm`, Pi TUI native modules, clipboard binaries, and Photon WASM. | `APPDEV_DAEMON_SERVICE_2026-07-25/.../AGENT1-VALIDATOR/ROUND1_REVIEW.md:254-263` records an older packaged-app PASS, and its daemon descriptor names `0.82.0`; it does not record a Pi asset import/turn. | No frozen-head package, unpacked asset inventory, checksums, or actual native/WASM load proof. |
| Notices | `frontend/THIRD_PARTY_NOTICES_PI.md:1-38`; `frontend/package.json:113-117`; `dmg-packaging-policy.test.ts:116-125` | Pi-owned MIT notice exists, names all four Pi packages at `0.82.0`, and is configured as an extra resource. | The lock closure contains 140 entries spanning MIT, Apache-2.0, BSD-3-Clause, ISC, 0BSD, and BlueOak-1.0.0 metadata. | The notice itself states at lines 36-38 that complete packaged-closure notices remain required before redistribution. No complete closure notice/provenance artifact exists. |
| Package inclusion | `frontend/package.json:104-123`; `scripts/verify-packaged-dependency-boundary.mjs:22-109`; `scripts/build-electron.mjs:80-89` | Source policy includes `node_modules/**/*`, externalizes Pi from the Electron bundle, requires Pi in `app.asar`, and excludes monorepo-only packages. | Older package validation reports Pi present in `app.asar`. | No frozen-head ASAR exists; the verifier checks package presence but not exact Pi version or individual native/WASM asset paths/checksums. |
| Packaged runtime proof | `frontend/package.json:26`; `scripts/run-packaged-pi-runtime-proof.mjs:67-232,234-417,420-488,490-514` | The file contains both a direct Pi SDK asset child and a stronger production-route child with `0.82.0` assertions. | Historical production-route PASS is explicitly Pi `0.80.10` (`PI_OMLX_SECOND_ENGINE_2026-07-21/RETURN_G5_SECURITY_REVIEW.md:38-39`). | The npm command's parent spawns only `--legacy-asset-child` at lines 441-449. No path in `runParent()` spawns `--child`; therefore the advertised command does not execute lines 234-417. No `0.82.0` frozen-head summary exists. |
| App regression/conformance | `pi-agent-engine-adapter.test.ts:154-519`; `pi-event-mapper.test.ts:7-84`; `pi-omlx-wire.integration.test.ts:273-620`; `harness-runtime.test.ts:126-157`; `engine-conformance.test.ts:269-707` | Current source defines exact-version attribution, canonical event, isolation, tool, failure, interruption, timeout, recovery, and engine-conformance tests. | `APPDEV_DEL0903_C04_FANIN_2026-08-02/HANDOFF.md:5-7,22-37,50-57` records focused/full PASS. Its accepted shared-daemon test SHA `1da250...45be` exactly matches the frozen file, and relevant adapter/runtime files are unchanged since its integration commit; this supports, but does not replace, a fresh frozen-head rerun. | No fresh tests ran in this worktree because dependencies are absent. Historical PASS cannot establish all frozen-head suites. |
| Root/App adapter identity | `runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts:34-93`; `frontend/electron/runtime-host.ts:16,39-40,154-235`; `frontend/src/lib/harness/runtime.ts:9-16,221-263` | Root defines a generic Pi engine factory; the executable App harness/daemon registers `PiAgentEngineAdapter`. Runtime host imports only `OmlxClient` from the Root Pi package and casts App adapters into the promoted contract. | `APPDEV_PI_AGENT2_CAPABILITY_PACKET_2026-08-01/.../A2-RUNTIME-SEAMS/RETURN.md:14-17` independently records that the Root factory has no caller and the packaged daemon uses the App compatibility adapter. | No single executable adapter implementation is established across Root and App. The duplicate descriptors agree on version but do not remove implementation-identity ambiguity. |
| CI coverage | `.github/workflows/harness-premerge.yml:90-104,239-240`; `validate-release-quality-evidence.mjs:371-373` | PR CI installs locked dependencies, runs the Pi supply-chain verifier, then runs full frontend Vitest and typecheck through the release-quality wrapper. | Historical run reports exist but are not frozen-head CI results supplied to this audit. | CI does not invoke `harness:validate:pi-packaged-proof`, build a macOS package, or inspect packaged native/WASM assets. |

## Findings

### E1-STRUCT-01 — PASS: frozen-head dependency/policy structure is internally consistent

The exact pins, lock integrity, closure size, install-script allowlist, native/WASM
patterns, Pi notice presence, and descriptor version agree at `0.82.0`, and the
fresh manifest-only verifier passes. Evidence:
`frontend/package.json:33-35,49-52,88-117`;
`frontend/scripts/verify-pi-supply-chain.mjs:5-102`;
`frontend/package-lock.json:720-790,1293-1311,2374-2379,2603-2607`.

This is structural supply-chain evidence only. It is not an approval or a
packaged-runtime verdict.

### E1-STRUCT-02 — OPEN / HIGH: the advertised packaged proof does not run its production-route child

`harness:validate:pi-packaged-proof` calls the script without arguments
(`frontend/package.json:26`). Its parent spawns `--legacy-asset-child`
(`run-packaged-pi-runtime-proof.mjs:420-482`), while the production route is
implemented in `runChild()` (`:234-417`) and selected only when the already
running process receives `--child` (`:501-511`). No parent spawn supplies that
argument. Thus the command can prove direct packaged Pi SDK/assets, but not the
production route, registry, App adapter, provider preflight, governed tool
bridge, or canonical persistence. Historical production-route evidence is for
`0.80.10`, not `0.82.0`.

### E1-STRUCT-03 — OPEN / HIGH: no frozen-head 0.82.0 package/native/WASM execution proof

The policy patterns exist, but the audited worktree has no installed closure,
packaged app, ASAR inventory, unpacked asset inventory, asset checksums, or
packaged-Pi summary. The July 25 daemon evidence shows the `0.82.0` adapter
descriptor, not a Pi turn or native/WASM load. Required evidence is a package
built from the exact accepted revision plus inventory and both direct asset-load
and production-route execution results.

### E1-STRUCT-04 — OPEN / MEDIUM: redistribution notices cover only the four Pi-owned packages

`THIRD_PARTY_NOTICES_PI.md:3-8` names the four Pi packages and carries their MIT
notice, but `:36-38` explicitly requires notices for the complete packaged
dependency closure before redistribution. The current closure has 140 resolved
artifacts and multiple license families. The verifier checks only four package
names plus one copyright string (`verify-pi-supply-chain.mjs:77-87`), so its
PASS cannot be read as complete-closure notice provenance.

### E1-STRUCT-05 — OPEN / MEDIUM: install-script policy proves names, not behavior

The lock and verifier constrain `hasInstallScript` entries to `@google/genai`
and `protobufjs`, but neither surface records or validates the actual script
commands, produced files, network behavior, or frozen-environment execution.
This is a valid change-detection gate, not lifecycle-behavior proof.

### E1-STRUCT-06 — OPEN / MEDIUM: executable adapter identity remains split

Root exports `createPiOmlxEngineAdapter`, but the App harness and packaged daemon
construct the App-local `PiAgentEngineAdapter`; the runtime host imports only
`OmlxClient` from the Root package and documents a temporary structural cast
(`frontend/electron/runtime-host.ts:231-235`). Both descriptors say `0.82.0`,
but descriptor equality does not establish one implementation identity. This
must be resolved or explicitly accepted in the generic-contract/supersession
decision; present bytes do not decide it.

### E1-STRUCT-07 — RERUN REQUIRED: current test source is substantial, but frozen-head execution was unavailable

The current suites cover exact Pi attribution, resource isolation, read-only
tool enforcement, redirect and diagnostic guards, canonical events,
interruption, timeout, provider restart, concurrent session isolation, and
provider-neutral conformance. A preserved August 2 fan-in records PASS for one
exactly matching test file and a full suite, but this audit did not execute the
frozen head because the declared read-only environment has no installed test
runner. Treat the preserved result as historical supportive evidence and rerun
after an authorized lockfile install.

## Blockers and required reruns

1. **Authorized dependency environment:** perform `npm ci` for the frozen or
   later decision-candidate revision; then rerun the focused Pi suites and full
   frontend suite. Installation was outside this read-only child brief.
2. **Repair/choose the packaged proof entrypoint:** make the advertised command
   execute the production-route `runChild()` path (while retaining the direct
   asset child if both lenses are required), and add a test that proves which
   child modes the parent launches.
3. **Exact-source package proof:** build the macOS package from the accepted
   revision, record source SHA, ASAR/unpacked inventories, exact Pi package
   identity, `.node`/`.wasm` paths and checksums, and run the direct asset-load
   plus production-route fake-loopback proof. Preserve the resulting summary;
   do not infer it from source policy.
4. **Install-script validation:** capture installed package manifests and exact
   lifecycle scripts for the two allowlisted packages, record whether they ran,
   and verify their produced files/network posture under the chosen install
   policy.
5. **Complete notice provenance:** generate and verify license/copyright notices
   for the exact packaged closure, not only the four Pi-owned packages.
6. **Adapter identity decision:** explicitly select or sequence Root generic
   engine adoption versus the App compatibility adapter; rerun conformance and
   packaged proofs against the selected executable path.
7. **CI extension:** retain the existing Pi supply-chain/full-suite gates and
   add a package/asset/production-route proof where the selected runner can
   produce and inspect the target package. A source-only Linux job cannot prove
   macOS packaged native/WASM loadability.

None of these reruns may be treated as authority to select Pi `0.82.0`, release
it, broaden the Pi capability boundary, or close `TM-ROOT-106`. The required
decision record remains a separate human act.
