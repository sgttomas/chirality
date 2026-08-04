# Root Pi 0.82.0 implementation-identity options

Status: **PIA-U10 PROPOSAL — HUMAN G1 SELECTION REQUIRED — NO OPTION SELECTED**

This derivative proposal resolves no authority question. D-GOV-20 remains
version-neutral, D-APP-72/SCA-APP-002 Pi `0.80.10` remains operative, and Pi
`0.82.0` remains only the preferred evidence candidate under the owner's
Option A hold. A G1 choice below selects one target for validation; it neither
approves Pi nor supersedes App authority.

## Why the present identity collides

Root's `createPiOmlxEngineAdapter` and App's `PiAgentEngineAdapter` both
advertise `pi` / `omlx` / `@earendil-works/pi-coding-agent` / `0.82.0` with the
same capability booleans. The current registry key is only
`adapterId + providerId`; the current runtime fingerprint adds model and
package name/version but still omits implementation family, source/build,
registration, policy, client composition, package closure, and rollback
identity. App's Desktop composition registers the App implementation; the Root
wrapper is not the observed executable family.

`CANDIDATE_IDENTITY.schema.json` therefore separates upstream identity from
Chirality implementation identity. Its `registry_key` is the SHA-256 of the
RFC 8785 canonical `stable_identity` object. `mutable_evidence` is attributable
validation state and is expressly excluded from that digest and key.

## G1-A — Root-wrapper canonical

Validation target: Root's existing `createPiOmlxEngineAdapter` family becomes
the sole public Pi/oMLX implementation family. App supplies a governed
`PiTurnRuntimePort`, provider/model resolution, credential boundary, tool
composition, and package closure without registering a second public adapter
family.

- Proposed family ID: `chirality.root.engine-pi-omlx.reference-wrapper`.
- Compatibility: retains the provider-neutral `AgentEnginePort` descriptor and
  the current Agent-2/read-only pilot boundary. It does not establish that the
  Root wrapper already reproduces all App behavior.
- Ownership: Root owns the adapter contract/family and registry identity; App
  remains affected-client composition and executable dependency owner unless a
  later ruling moves that boundary.
- Migration: separately gated App work would replace direct registration of
  `PiAgentEngineAdapter` with a `PiTurnRuntimePort` composition consumed by the
  Root wrapper. No such source migration is authorized here.
- Evidence needed: source/build identity for both wrapper and supplied port;
  registry/fingerprint collision tests; Root/App conformance; exact package,
  production-route, and live evidence showing the wrapper path actually ran.
- Rollback: preserve D-GOV-20 plus the operative App `0.80.10` authority and
  pre-migration App composition as the attributable restoration basis; never
  rewrite prior evidence.
- Later instruments: Root SCOPE_CHANGE and DEL-02-06 proposal/activation;
  App affected-client SCOPE_CHANGE and implementation gate; PIA-U30 and later
  EVALUATION. Every instrument retains its own human gate.
- Tradeoff: strongest single-family Root ownership, but requires the largest
  behavior-preserving App composition migration short of convergence.

## G1-B — App-host implementation explicitly registered

Validation target: App's current `PiAgentEngineAdapter` remains the executable
family and is explicitly registered as an App-owned affected-client
implementation under the Root identity schema. Root's reference wrapper is a
different, non-executed family and cannot share the registration key.

- Proposed family ID: `chirality.app.pi-agent-engine-adapter`.
- Compatibility: matches the currently observed Desktop composition and App
  lock ownership while requiring expanded Root registry, fingerprint, event,
  session, and evidence fields.
- Ownership: App owns the concrete implementation, dependency closure, and
  client composition; Root owns the generic schema and conformance contract.
- Migration: Root contracts/registry/fingerprint surfaces would gain the
  stable identity fields; App would register an exact family/source/build/
  composition identity. No source or registry write is authorized here.
- Evidence needed: exact App source/build/package identity, Root collision
  tests proving the wrapper cannot resolve under the App key, package/live
  evidence, and generic conformance against the explicit affected-client ID.
- Rollback: restore the operative D-APP-72 `0.80.10` App composition under an
  explicit prior identity; Root remains version-neutral.
- Later instruments: Root SCOPE_CHANGE/DEL-02-06 for the generic identity
  contract; App successor and SCOPE_CHANGE only after a later Root acceptance;
  App proof units, PIA-U30, and later EVALUATION.
- Tradeoff: least executable-source migration and most faithful to present
  composition, but deliberately retains App ownership of the concrete Pi
  family and dependency closure.

## G1-C — Converged Root concrete adapter

Validation target: a future concrete Pi session implementation is moved or
recreated under the Root engine package and App consumes that Root-owned
family. This target does not yet have selectable source/build bytes.

- Proposed family ID: `chirality.root.engine-pi-omlx.concrete-session`.
- Compatibility: intended to combine Root ownership with App's concrete
  behavior; equivalence is unproven and cannot be inferred from the proposal.
- Ownership: Root would own the concrete adapter and executable dependency
  boundary selected by later rulings; App would own its affected-client host,
  credentials, packaging, and product adoption.
- Migration: requires design, SCOPE_CHANGE, a separately sealed implementation
  activation, affected-client migration, and fresh exact-source evidence. G1
  may select this design target, but validation cannot begin until materialized
  candidate hashes are presented and accepted.
- Evidence needed: behavior/conformance comparison against both present
  implementations; exact dependency and build ownership; collision tests;
  package/native/WASM, production-route, and live proof on the new bytes.
- Rollback: keep the pre-convergence Root wrapper and operative App `0.80.10`
  composition as separately named historical identities with explicit
  compatibility epochs.
- Later instruments: Root SCOPE_CHANGE, DEL-02-06 design and implementation
  activation, App affected-client SCOPE_CHANGE, PIA-U30, and later EVALUATION.
- Tradeoff: clearest long-term Root concrete ownership, but broadest scope,
  greatest migration risk, and no present implementation identity to hash.

## G1-D — Continue hold

Select no validation target. Retain Option A's evidence hold, amend these
options/schema, or gather only non-implementation evidence that does not
presuppose a family.

- Compatibility and ownership: current facts remain exactly as observed; the
  Root/App descriptor collision remains open and App `0.80.10` remains
  operative authority.
- Migration: none.
- Evidence: only work that is independently useful without choosing an
  implementation family may be considered under a later lawful instrument;
  H2 dispatches none.
- Rollback: not applicable because no prospective identity is selected.
- Later instruments: another HELPS_HUMANS proposal or owner-directed
  continuation. App, runtime, and decision surfaces remain untouched.
- Tradeoff: avoids premature migration choice but blocks PIA-U30 and the
  identity-dependent proof sequence.

## Collision cases the selected target must pass

| Case | Required distinction | Expected result |
|---|---|---|
| Root and App advertise the same upstream descriptor | `implementation.family_id`, source/build, registration, and client composition | Different identity digests and registry keys |
| Same family ID but source bytes change | source commit/file hashes and build artifact manifest | Different digest; all dependent evidence reruns |
| Same implementation bytes under different capability or policy | capability-profile and policy-bundle IDs/hashes | Different digest; no silent capability widening |
| Same implementation under different App/Root host or dependency owner | client-composition ID/hash and packaging hashes | Different digest; affected client remains explicit |
| Same stable identity is rerun with a new model, residency epoch, runtime fingerprint, or timestamp | `mutable_evidence` only | Same registry key; new evidence bundle remains attributable |
| Rollback target or compatibility epoch changes | rollback identity and authority refs | Different digest; restoration basis is never implicit |
| Historical manifest/lock/build evidence changes | stable packaging/build hashes | Different digest and mandatory evidence rerun |

The future PIA-U30 validator must recompute the canonical digest, reject a
declared `registry_key` that does not match it, and prove all cases above. JSON
Schema validates shape and field discipline; it is not a digest calculator.

## Human G1 decision request

DecisionID: `PIA-U10-G1`

Question: Which one target should later validation test: `G1-A`, `G1-B`,
`G1-C`, or `G1-D` continue hold?

Allowed result: select one target for validation, amend this proposal, or
continue the hold. H2 makes no recommendation weighting and selects nothing.
No result at G1 is Pi `0.82.0` approval, D-APP-72 supersession, App work
authorization, implementation activation, release, reliance, or Task
Management closure.
