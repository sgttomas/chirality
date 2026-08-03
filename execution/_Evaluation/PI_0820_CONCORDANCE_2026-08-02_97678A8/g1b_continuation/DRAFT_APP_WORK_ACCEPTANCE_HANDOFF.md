# DRAFT / UNROUTED — App work-acceptance handoff for G1-B

Status: `DRAFT ONLY — ROOT EVALUATION QUARANTINE — NOT ROUTED`

From: Root HELPS_HUMANS / H4

Prospective recipient: Chirality App Dev loop

Effect: none

## Root selection and its limit

The human Root owner selected `G1-B` for validation only: family
`chirality.app.pi-agent-engine-adapter` identifies App's currently executable
`PiAgentEngineAdapter` as the evidence target. The ruling is
`OWNER_RULING_2026-08-03_S2_APPLY_PI_G1B.md` at SHA-256
`12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129`.

The Root-local target envelope is `G1B_VALIDATION_TARGET.json` at SHA-256
`c5b2087e070cc92cc3daecd35460497be47b6f9dff3155bde5b1cbd0aef2db01`.
It binds exact frozen/current App source, host-composition, manifest, lock,
proof-launcher, verifier, and notice bytes. It also exposes the stable identity
fields that remain `TBD` pending separately accepted proof and contract
records.

Neither record approves Pi `0.82.0`, accepts G1-B as final architecture,
supersedes D-APP-72/SCA-APP-002 `0.80.10`, authorizes App work, or changes an
App surface.

## Prospective App decision requested

If this draft is later routed through an authorized coordination instrument,
the App loop may independently:

- `ACCEPT_EXACT_WORK_UNITS`;
- `AMEND_OR_SPLIT_WORK_UNITS`;
- `DECLINE_WORK_UNITS`; or
- `DEFER_WORK_UNITS`.

Silence, receipt, Root selection, file presence, or a Root validation result is
not App acceptance. Any acceptance must identify exact App write targets,
brief hashes, runtime/tool policy, dependencies, human gates, and integration
owner under App authority.

## Draft work slate for App consideration

The authoritative proposal rows remain PIA-U20 through PIA-U25 in
`OPTION_A_WORK_UNITS.csv` at SHA-256
`8b8b2ddaf8750bbb3e4ebb45e88452873f072bc373af104c53c8dca13ca51955`.
This handoff narrows their target to G1-B without changing their disposition:

| Unit | Proposed App-owned objective | G1-B-specific input/output obligation | Dependency / stop gate | Disposition |
|---|---|---|---|---|
| `PIA-U20` | Repair the packaged-Pi launcher and test both direct-asset and production-route children | Bind exact accepted repair/build recipe and prove production route observes `chirality.app.pi-agent-engine-adapter` | App accepts exact repair scope; stop at App acceptance of repair candidate | `DRAFT_UNROUTED` |
| `PIA-U21` | Exact-lock isolated install and supply/lifecycle closure | Preserve exact upstream package manifest, 140-entry closure, lifecycle and produced-file manifests | Exact App candidate frozen; disposable validation workspace only | `DRAFT_UNROUTED` |
| `PIA-U22` | Exact macOS build/package/native/WASM proof | Supply build/toolchain/artifact, packaging-policy, asset, platform, ASAR/unpacked, and production-route evidence needed by the identity | Accepted U20; U21 PASS; independent package acceptance | `DRAFT_UNROUTED` |
| `PIA-U23` | Final source regression and provider-neutral conformance | Bind the exact G1-B source/composition/manifest/lock set and identity-related test results | Exact accepted repair candidate; independent regression acceptance | `DRAFT_UNROUTED` |
| `PIA-U24` | Opt-in live oMLX validation | Persist exact G1-B family/digest/key with model, residency, failure, no-fallback, and redaction evidence | U22/U23 PASS plus explicit model/credential authorization | `DRAFT_UNROUTED` |
| `PIA-U25` | Complete packaged-closure notice provenance | Bind all packaged third-party artifacts; remain release-only | Exact U21 closure and U22 package inventory | `DRAFT_UNROUTED` |

## Exact inbound candidate facts to reproduce

| Role | Path | SHA-256 |
|---|---|---|
| App implementation | `projects/chirality-app-dev/frontend/src/lib/harness/pi-agent-engine-adapter.ts` | `34c8fd0978741720e74ba36beb3fdc7c9a06f31ed55b7da87c86525ac39c47ca` |
| App composition | `projects/chirality-app-dev/frontend/electron/runtime-host.ts` | `2e02f592e7e8a6c0008a50cb427044d95aa908e6276b6a9cd8bfe6a1dce248c8` |
| App manifest | `projects/chirality-app-dev/frontend/package.json` | `1e62d22ec4a07fb225352c90ddfa5ce41d736d3d169e04cf7bd3684e54557c9c` |
| App lock | `projects/chirality-app-dev/frontend/package-lock.json` | `674fe2dab74572f21d26455498461d62eaa4218560e45024ed2a31e00c635ab8` |
| Current proof launcher | `projects/chirality-app-dev/frontend/scripts/run-packaged-pi-runtime-proof.mjs` | `7354e0af73f40e308a5204fe04621a4db0c6e68c964065bb1f029d0aeec5674f` |
| Supply verifier | `projects/chirality-app-dev/frontend/scripts/verify-pi-supply-chain.mjs` | `912a07d5db0d574c3de3acd69898b6567612fbc456807902b83c0a5c38165b7e` |
| Current Pi notice | `projects/chirality-app-dev/frontend/THIRD_PARTY_NOTICES_PI.md` | `0195b5ce8b7be8b6bff6de3e50f6a38b3d9d4919c075e7c93ca8118b7e866328` |

The upstream candidate is
`@earendil-works/pi-coding-agent@0.82.0` with lock SRI
`sha512-Qnqgn9zhJFQ2HZ8R4iNuGhyCk93XX6+eUw9i+TjTuo47amzCy93ft3bB6yaUCleCrNO58dJDHYSGNHv/GAPWKg==`.
The prior 140-entry frozen closure-map digest is
`8fb3458ddafdbc861c5fc541775bddf2a2832d30476c78c2866535a4416fbc96`;
it is precursor evidence, not a substitute for U21 exact-install evidence.

If any accepted starting byte differs, App must stop and return drift; it must
not silently update the Root target. Any App-approved repair creates a new
exact candidate hash set that Root must explicitly ingest before PIA-U30.

## Immutable return contract

Each accepted unit must use a unique App run ID and immutable evidence path and
return the outputs listed in `OPTION_A_WORK_UNITS.csv`, including `BASIS.json`,
`COMMANDS.jsonl`, `RESULTS.json`, `ARTIFACT_MANIFEST.csv`, `RETURN.md`, and
`STATUS.json`. Commands and environments must be attributable and redacted;
secrets and raw credentials must be absent. A rerun creates a new bundle and
does not overwrite prior evidence.

Root requests returned evidence hashes and exact candidate facts. Root does
not request an App authority, decomposition, lifecycle, release, reliance,
register, or Git change through this draft.

## Preserved App gates

- D-APP-72/SCA-APP-002 Pi `0.80.10` and Electron `43.1.1` remain operative.
- App decides whether proof work, any source repair, the `43.2.0` executable
  prerequisite, or later adoption requires its own SCOPE_CHANGE or successor
  ruling.
- No native Read/Write/Edit/Bash capability, sandbox activation, remote
  provider, fallback, ambient Pi resource, or durable resume is authorized.
- `durableResume: false` remains part of the target.
- PIA-U24 requires a separate explicit owner authorization for model and
  credential use.
- PIA-U25 remains release-only and grants no distribution authority.
- Root PIA-U30 remains held until exact PIA-U22 and PIA-U23 evidence is
  independently accepted and a separate Root launch is authorized.

## Draft disposition

Retain this file only inside the Root G1-B continuation package. H4 does not
write an App coordination surface, send a notice, dispatch work, or presume a
receipt. A later authorized router must preserve this draft and its hashes,
record the routing act separately, and leave App free to accept, amend, split,
decline, or defer.
