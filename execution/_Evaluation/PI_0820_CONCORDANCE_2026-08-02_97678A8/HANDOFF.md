# Handoff — Pi 0.82.0 concordance evaluation

Status: `EVALUATION COMPLETE / DECISION AND VALIDATION HOLD REMAIN`
Recommended path: `CONTINUE D-APP-84 V1 AS CANDIDATE; DO NOT APPROVE YET`

## Accepted upstream basis

- Repository `97678a841ef58345c73d3470ed8de57c9b1405d2`.
- Root harvest ruling SHA-256
  `9fde04e411f1839c6b37ae09e7fba0e8b60a6dd54e434b2bbf2d570e854520d8`.
- D-APP-84 Root route SHA-256
  `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`.
- D-APP-72 SHA-256
  `c7dcbb5aaa0f82481fb76825c7099c4e355c4ada80232c51f3a3cf6ba2076577`.
- D-APP-84 REV2 packet/ruling SHA-256 values
  `59e3f668f742bc8e100630781da3be975c0c6861410d06ee2ed019d5c79cf5d9`
  and `f439c79e358ffaa1e30f897cd1be901195aa1b4b2a184e2c0465a8ee87461c58`.

## Derivative-package status

This directory is a derivative evaluation package. It cites and does not
replace the accepted Root/App authority above. Its report, findings, child
returns, and evidence are decision support only. It creates no version,
adapter, lifecycle, release, reliance, SCOPE_CHANGE, register, or Git effect.

## Decisions required

1. Human Root owner: choose the Root `0.82.0` candidate disposition and exact
   canonical adapter implementation identity. Recommendation: continue V1
   under evidence hold.
2. Human/App owner, after Root acceptance: issue a prospective D-APP-72
   successor and rule the App SCOPE_CHANGE; include or explicitly reject the
   adjacent Electron `43.2.0` prerequisite fact.
3. No `TM-ROOT-106` closure is available until the decision record and required
   validation evidence both exist.

## Remediation and evidence owners

| Owner | Required action |
|---|---|
| Root `SCOPE_CHANGE` / DEL-02-06 lane | Define canonical adapter implementation identity, package ownership, compatibility/fingerprint fields, supply boundary, and affected-client obligations; propagate only after applicable owner gates. |
| App affected-client SCOPE_CHANGE | After Root acceptance, supersede the exact `0.80.10` / `43.1.1` prospective facts across accepted App authority, decomposition, product docs, SCA maps, authority corpus, and affected-client evidence. |
| App build/release validation | Repair `run-packaged-pi-runtime-proof.mjs` so the advertised command launches the production-route child; preserve exact-source install, ASAR/unpacked inventories, asset hashes, direct-load and production-route results. |
| App validation | Rerun focused/full tests and repeat the opt-in live oMLX proof at the ruled candidate. |
| App release owner | Generate complete exact packaged-closure notices before redistribution. |
| Human owner | Decide; no agent may infer acceptance from passing bytes. |

## Blockers

- effective App authority remains Pi `0.80.10`;
- no Root `0.82.0` / canonical implementation-identity decision exists;
- no App successor/SCOPE_CHANGE exists;
- packaged production-route entrypoint is disconnected and no durable current
  package/native/WASM proof exists;
- live proof remains bound to `0.80.10`;
- full-closure redistribution notices are absent; and
- Electron `43.2.0` is executable evidence against a `43.1.1` authority fact.

## Rerun requirements

On the exact post-decision candidate:

1. isolated `npm ci` from the accepted lock, `npm ls --all`, Pi supply verifier,
   lifecycle-script capture, and 140-artifact SRI verification;
2. full runtime/frontend tests, typecheck, focused Pi adapter/wire/conformance,
   lock-integrity, and packaging-policy suites;
3. repaired macOS packaged proof with source SHA, ASAR/unpacked inventories,
   exact `.node`/`.wasm` paths and hashes, direct asset load, production-route
   fake-loopback turn, governed tool, canonical persistence, and redaction;
4. opt-in redacted live oMLX proof at the ruled Pi version;
5. governance concordance over Root decision, App successor/SCOPE_CHANGE,
   decomposition, product docs, authority corpus, descriptors, fingerprints,
   manifests, lock, notices, and accepted evidence; and
6. a final read-only evaluation rerun if any identity or candidate hash changes.

## Closure verdict

`NOT CLOSED`. Technical lock/integrity and source-regression evidence is strong,
but the decision, canonical identity, packaged execution, live proof, and App
supersession requirements remain. Task Management retains ownership of any
later register disposition.
