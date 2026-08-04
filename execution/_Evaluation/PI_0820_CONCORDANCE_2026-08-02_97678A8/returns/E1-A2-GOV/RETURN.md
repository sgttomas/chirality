# E1-A2-GOV Return — Pi authority, identity, and supersession audit

Status: `COMPLETE / READ_ONLY / DECISION_REQUIRED`

Role: `AUDIT_GOVERNANCE`

Repository snapshot: `97678a841ef58345c73d3470ed8de57c9b1405d2`

Write effect: this `RETURN.md` only. No subject file was modified.

## Terminal verdict

The authority precedence itself is not ambiguous: the currently effective App
version authority remains D-APP-72 / SCA-APP-002 at Pi `0.80.10`. D-APP-84
selects Pi `0.82.0` only as a Root-conditioned prospective App compatibility
target and expressly says that it does not reconcile or release the
`0.80.10`/`0.82.0` conflict. The Root route notice is coordination, not
authority. The `0.82.0` source, manifest, lockfile, and notice bytes are
execution evidence only and are **not approval**.

Two blockers prevent an evidence-only acceptance of `0.82.0`:

1. no Root decision record accepts an exact `0.82.0` generic adapter identity,
   and no later App decision/SCOPE_CHANGE record prospectively supersedes the
   exact D-APP-72/SCA-APP-002 `0.80.10` fact; and
2. the current runtime identity schema does not uniquely identify the adapter
   implementation. Root's reference adapter and the App-local concrete adapter
   advertise the same nominal `pi` / `omlx` / Pi-package identity, while the
   Desktop composition root registers the App-local implementation rather than
   Root's `createPiOmlxEngineAdapter` implementation.

The governance disposition is therefore `HOLD FOR OWNER DECISION`. This return
does not choose retain, supersede, or reject/remediate.

## 1. Authority hierarchy and exact conflict map

| Rank / class | Surface | What it establishes | Concordance result |
|---|---|---|---|
| Accepted Root authority | `docs/governance_harness/_DECISIONS/D-GOV-20_shared_runtime_local_agent_pilot.md:18-29,40-53` | Root owns the provider-neutral runtime, daemon, contracts, and safe adapters; the initial local slice is one bounded read-only Pi/oMLX Agent 2; D-APP-72 must close before behavior-preserving promotion. It names no Pi package version. | Compatible with D-APP-72, but not an independent `0.82.0` approval. |
| Accepted App authority | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-72_RULING_2026-07-21.md:21-38,40-55` | Authorizes exact Pi `0.80.10`, in process, authenticated loopback oMLX, one governed read-only Agent 2, with Pi built-ins/native delegation/write/shell/network excluded. | **Direct version conflict** with executable `0.82.0` surfaces. |
| Accepted App scope snapshot | `projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-002_2026-07-21_Pi_oMLX_Second_Engine/Supersession_Map.csv:6-8`; `Handoff_State.md:5-28` | Records the prospective bounded exception as Pi `0.80.10` and identifies D-APP-72 as the authority. | Still `0.80.10`; no successor delta is present. |
| Accepted extraction/residency authority | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-73_RULING_2026-07-22.md:18-29,41-54` | Promotes the harness without behavior change and extends D-APP-72 only for oMLX status/load/unload and residency. | Does not change the Pi version or read-only child boundary. |
| Accepted App decomposition/product basis | `projects/chirality-app-dev/docs/CONTRACT.md:54-57,188-193`; `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md:85-109,126-131,579-580,605-606,633-635` | Product contract and accepted decomposition repeatedly fix the bounded exception at Pi `0.80.10` and assign generic runtime semantics to Root while App remains an affected client. | Internally concordant with D-APP-72; conflicts with present `0.82.0` bytes. |
| Selected proposal semantics, now carried by a ruling | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-84_RULING_PI_OMLX_AGENT2_CAPABILITY_EXPANSION_2026-08-02.md:23-48,99-113,127-135` | Selects B1/V1/P1/X1/H1/R1. Pi `0.82.0` is prospective and conditional on Root accepting the same adapter identity and evidence. Exact concordance precedes implementation; later App SCOPE_CHANGE is required. | Not a present version supersession. Lines 47-48 expressly preserve the conflict. |
| Preserved proposal evidence | `projects/chirality-app-dev/execution/_Coordination/_DECISIONS/D-APP-84_PACKET_PI_OMLX_AGENT2_CAPABILITY_EXPANSION_REVISION_2_2026-08-02.md:1-33,56-90,145-153,283-331` | Defines options, records the observed drift, and proposes the Root/App sequence. Its own no-effect fence and proposal status remain evidence of what was selected, not an implementation act. | No conflict: a preserved proposal may retain `AWAITING_RULING`; the separate ruling is the authority record. |
| Route notice | `execution/_Coordination/NOTICE_D-APP-84_REV2_APP_PI_SANDBOX_ROOT_ROUTE_2026-08-02.md:5-10,22-59,77-88` | Requests Root decisions, exact `0.82.0` concordance, SCOPE_CHANGE impact, and DEL-02-06 work; explicitly grants no Root authority. | Coordination only; cannot supersede either loop's authority. |
| Execution evidence | `projects/chirality-app-dev/frontend/package.json:39-52`; `package-lock.json:13-26,720-790`; `src/lib/harness/pi-agent-engine-adapter.ts:23-24,654-669`; `runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts:10-45` | Direct dependencies and both descriptors say `0.82.0`; the lock records registry resolution/integrity for the direct Pi packages. | Proves present bytes, not their approval. Supply-chain closure is assigned to the dependency-audit sibling. |

The accepted-basis hashes were independently reproduced:

- Root harvest ruling: `9fde04e411f1839c6b37ae09e7fba0e8b60a6dd54e434b2bbf2d570e854520d8`.
- D-APP-84 Root route: `2d61231689e78b414680aeac307c377ef3079b65cc7f60355b7c3942ad7c3e6a`.
- D-APP-72 ruling: `c7dcbb5aaa0f82481fb76825c7099c4e355c4ada80232c51f3a3cf6ba2076577`.
- D-APP-84 Revision 2 packet: `59e3f668f742bc8e100630781da3be975c0c6861410d06ee2ed019d5c79cf5d9`.
- D-APP-84 ruling: `f439c79e358ffaa1e30f897cd1be901195aa1b4b2a184e2c0465a8ee87461c58`.

Repository history corroborates, but does not authorize, the drift: `git blame`
attributes the `0.82.0` manifest and both descriptor changes to commit
`447f49cffd65350a9f743536a81ec8acff02012d` (`Harden desktop release
dependencies`). The scoped diff changes `0.80.10` to `0.82.0` in code and
dependency surfaces and contains no decision record or SCOPE_CHANGE successor.

## 2. Adapter identity map

| Layer | Observable identity | Actual implementation / use | Finding |
|---|---|---|---|
| Root contract | `EngineDescriptor = {adapterId, providerId, packageName?, packageVersion?, capabilities}` at `runtime/packages/contracts/src/harness/agent-engine-port.ts:14-20` | Contract has no adapter implementation ID, wrapper package/build hash, capability-profile ID, registration ID, or policy identity. | Insufficient to prove the D-APP-84 condition "same adapter identity." |
| Root reference adapter | `pi` / `omlx` / `@earendil-works/pi-coding-agent` / `0.82.0` at `runtime/packages/engine-pi-omlx/src/pi-omlx-engine.ts:34-48` | `createPiOmlxEngineAdapter` is an injected `PiTurnRuntimePort` wrapper. Its package is `@chirality/engine-pi-omlx@0.1.0` and depends only on `@chirality/runtime-contracts` (`runtime/packages/engine-pi-omlx/package.json:1-16`). | Nominal Pi identity is declared, but the Root package itself does not close or execute the Pi dependency. |
| App concrete adapter | Same nominal descriptor at `projects/chirality-app-dev/frontend/src/lib/harness/pi-agent-engine-adapter.ts:654-669` | Directly imports Pi types and dynamically constructs `createAgentSession`, `ModelRuntime`, `SessionManager`, and an isolated resource loader (`:488-586`). | Distinct implementation under the same nominal identity. |
| Desktop composition | Imports `OmlxClient` from Root but `PiAgentEngineAdapter` from App (`projects/chirality-app-dev/frontend/electron/runtime-host.ts:14-40`) | Instantiates and registers the App adapter at `runtime-host.ts:154-235`; no production import/use of `createPiOmlxEngineAdapter` was found. | Executed adapter identity is App-local even though generic runtime owns the registry/daemon. |
| Runtime key and evidence | Registry key is only `adapterId + providerId` (`runtime/packages/core/src/engine-registry.ts:3-29`); runtime fingerprint adds model and upstream package fields (`runtime/packages/core/src/runtime-service.ts:346-381`). | Both implementations would yield the same key/fingerprint fields for the same model. | Evidence cannot distinguish which implementation family produced a run. |

This is not necessarily an ownership violation: Root may own the generic
contract/daemon while App supplies an affected-client composition. The genuine
defect is that this project-specific divergence is not represented in the
identity contract, so it is presently impossible to prove exact cross-loop
adapter concordance or safe implementation-family continuity.

## 3. Genuine conflicts versus permitted/prospective divergence

### Genuine conflicts or gaps

1. **Version authority conflict (FACT / BLOCKER).** D-APP-72 and the accepted App
   product/decomposition surfaces say `0.80.10`; App dependencies, lockfile,
   notices, App adapter, and Root descriptor say `0.82.0`. D-APP-84 itself
   confirms this conflict at ruling lines 42-48.
2. **Missing supersession record (FACT / BLOCKER).** A scoped search of Root
   `docs/governance_harness/_DECISIONS/`, Root `execution/_Coordination/`, App
   `_DECISIONS/`, App `_ScopeChange/`, App decomposition, and App product docs
   found no Root `0.82.0` acceptance record and no App successor amendment that
   replaces the D-APP-72/SCA-APP-002 `0.80.10` fact. D-APP-84 requires both
   Root action and later App SCOPE_CHANGE (`D-APP-84` ruling lines 99-113).
3. **Adapter implementation identity ambiguity (FACT / BLOCKER FOR V1).** Two
   different implementations share one descriptor/fingerprint identity, and
   the actual Desktop path selects the App implementation. The condition
   "Root accepts the same adapter identity" is not mechanically or
   evidentially testable until the identity is defined beyond the upstream Pi
   package name/version.
4. **Adjacent prerequisite drift (FACT / ESCALATE).** D-APP-72 fixes Electron
   `43.1.1` (`D-APP-72` lines 23-26), while the current executable manifest
   pins Electron `43.2.0` (`projects/chirality-app-dev/frontend/package.json:60-68`).
   A scoped decision/SCOPE_CHANGE search found no exact `43.2.0` authority.
   The Pi version decision should classify this as an additional dependency-
   basis supersession or explicitly exclude it with rationale; do not silently
   treat the newer byte as approved.

### Project-specific or prospective divergence that is not presently a defect

- Root generic runtime ownership and App concrete composition are compatible
  with D-GOV-20/D-APP-73 provided the adapter implementation identity and
  affected-client boundary are made explicit.
- Current `noTools: 'all'`, one read-only Chirality tool, ambient-resource
  isolation, Agent-2-only checks, and `durableResume: false` remain consistent
  with D-APP-72 and with D-APP-84's held/no-effect posture
  (`pi-agent-engine-adapter.ts:488-586,654-698` and `runtime-host.ts:181-229`).
  They are not a failure to implement D-APP-84 because D-APP-84 explicitly
  blocks implementation pending Root and later App gates.
- D-APP-84's selected P1/X1/H1/R1 semantics are accepted prospective targets,
  not claims that native tools, OS sandboxes, narrow Bash, or durable resume
  already exist.

## 4. Gaps and unknowns requiring later evidence

1. `TBD`: the canonical adapter implementation identity tuple. At minimum the
   decision should distinguish upstream engine package/version from Chirality
   wrapper implementation family and bind a Root package/build/source hash,
   versioned capability profile/registration, and applicable policy identity.
2. `TBD`: whether Root intends the current reference
   `createPiOmlxEngineAdapter` to become the sole adapter implementation, or
   intends the App concrete adapter to remain an allowed host-injected
   implementation of the Root contract. Present files support both readings.
3. `TBD`: whether the direct Pi package closure belongs only to the App
   composition or must move under the Root adapter package. The Root package
   currently declares no Pi dependency while advertising a Pi package version.
4. `TBD`: exact supply-chain, lifecycle-script, native-module/WASM, notice,
   packaging, regression, and conformance verdicts. Those are intentionally
   assigned to the independent E1 dependency and structure audit children and
   must be fanned in before a version decision.
5. `TBD`: whether the Electron `43.2.0` drift is accepted in the same successor
   act or must be separately remediated.

## 5. Decision-ready lawful paths

### Option A — Explicitly supersede to Pi `0.82.0`

This best matches the owner-selected D-APP-84 V1 direction **if and only if**
the sibling validation returns satisfy the named gates.

Required sequence:

1. **Root owner:** issue a Root decision record accepting or rejecting one
   exact generic adapter identity tuple at Pi `0.82.0`, citing this evaluation's
   final evidence bundle and explicitly deciding the Root reference-adapter vs
   App host-injected-implementation relationship. This record must not purport
   to supersede App authority.
2. **Root SCOPE_CHANGE / DEL-02-06 as applicable:** propagate the accepted
   identity, package ownership, compatibility/fingerprint fields, supply-chain
   boundary, and affected-client conformance obligations into Root authority,
   decomposition, contracts, runtime, validators, and routed notices. Any
   implementation remains separately gated.
3. **App owner:** issue an explicit prospective successor to D-APP-72 for the
   exact version/prerequisite facts. D-APP-84 is the selected conditional target
   but says it does not itself release the conflict.
4. **App SCOPE_CHANGE:** amend SCA-APP-002's supersession delta/map, accepted
   decomposition, six product-governance docs, authority corpus, affected
   deliverable/status evidence, package/lock/notice surfaces, and App
   conformance route. Preserve D-APP-72 as immutable history.
5. **Root and App validation owners:** rerun exact dependency/integrity,
   lifecycle/native/WASM, notice, packaging, engine/Claude regression,
   conformance, fingerprint/identity, and affected-client tests on the ruled
   candidate. Record immutable evidence and fan in before reliance or release.

### Option B — Retain Pi `0.80.10`

Required sequence:

1. **Root owner:** record that `0.82.0` is not accepted as the generic identity.
2. **App owner + SCOPE_CHANGE/implementation lane:** reject D-APP-84 V1's
   conditional version target or record its non-satisfaction, restore exact
   `0.80.10` dependency/lock/descriptor/notice bytes (and address the Electron
   prerequisite drift), then rerun the full D-APP-72 baseline, packaging,
   supply-chain, security, and regression evidence.
3. Preserve all newer evidence as historical rejected/remediation evidence; do
   not rewrite D-APP-72.

### Option C — Reject or remediate `0.82.0` pending a later decision

If either sibling audit finds a supply-chain, lifecycle, packaging, notice, or
conformance blocker, the owner may reject the current candidate without
selecting `0.80.10` as the long-term answer. Name the defects, leave authority
at D-APP-72, remediate under the owning Root/App lanes, and commission a fresh
exact-version evaluation. No present byte gains interim approval.

## 6. Escalations, blockers, and rerun requirements

Escalate to the human owner at E1 fan-in:

- the missing exact Root `0.82.0` acceptance decision;
- the missing App supersession/SCOPE_CHANGE record;
- the Root reference-adapter versus App concrete-adapter identity choice;
- the adjacent Electron `43.2.0` authority drift; and
- any cross-loop propagation. Neither Root nor App may write the other's
  authority surface; use reciprocal notices and each loop's ordinary
  instruments.

Rerun this governance lens after an owner chooses an option and the exact
candidate records exist. The rerun must verify:

1. decision citations bind the final dependency/adapter candidate hashes;
2. supersession maps replace only the intended prospective facts and preserve
   immutable historical decisions;
3. Root and App identity fields distinguish upstream Pi version, Chirality
   implementation family/build, capability profile, and client composition;
4. product docs, accepted decomposition, authority corpus, manifests,
   descriptors, lockfile, notices, and runtime fingerprints are concordant; and
5. sibling validation evidence is cited, current, and does not claim release,
   reliance, or lifecycle approval.

## 7. Read-only checks executed

- `git rev-parse HEAD` ->
  `97678a841ef58345c73d3470ed8de57c9b1405d2`.
- `shasum -a 256` over the five accepted-basis records -> all exact expected
  SHA-256 values reproduced (listed in section 1).
- Scoped `rg` over Root/App decision, scope-change, decomposition, product,
  runtime, package, lockfile, notice, test, and run-evidence surfaces.
- `git blame` and `git show 447f49cffd...` over the three version-bearing
  implementation surfaces -> observed `0.80.10` to `0.82.0` source change;
  treated only as provenance, never authority.
- No validator or test that could write governed state was run.

## 8. Containment

The pre-write worktree already contained untracked parent-run/evaluation
directories. The post-write `git status --short` showed concurrent parent-run,
CI, DEL-02-06, and SCOPE_CHANGE work elsewhere in the shared worktree. A
targeted `git status --short --untracked-files=all --
execution/_Evaluation/PI_0820_CONCORDANCE_2026-08-02_97678A8/returns/E1-A2-GOV/RETURN.md`
showed only this new `RETURN.md`. The sibling `LAUNCH_BRIEF.md` was pre-existing;
this Agent 2 created or modified no other file.
