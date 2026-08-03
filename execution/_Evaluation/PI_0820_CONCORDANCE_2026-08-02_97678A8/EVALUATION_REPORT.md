# Evaluation report — Pi 0.82.0 authority, adapter, and supply-chain concordance

Run ID: `PI_0820_CONCORDANCE_2026-08-02_97678A8`
Parent: `ROOT_FOUR_LANES_2026-08-02`, node `E1`
Verdict: `HOLD FOR OWNER DECISION — V1 CANDIDATE TECHNICALLY SUPPORTABLE, NOT YET APPROVABLE`
Repository basis: `97678a841ef58345c73d3470ed8de57c9b1405d2`

## Basis

This evaluation executes item 3 of the Root harvest ruling / `TM-ROOT-106`.
The accepted basis and exact SHA-256 values are frozen in
`EVALUATION_PROTOCOL.md`. The controlling rule is that package, source,
lockfile, test, package, and runtime bytes are evidence only; none is approval.

The authority hierarchy is decisive:

1. Root D-GOV-20 accepts a Root-owned provider-neutral runtime and one bounded
   read-only Pi/oMLX Agent 2 slice, but names no Pi package version.
2. App D-APP-72 and SCA-APP-002 authorize exact Pi `0.80.10` and preserve that
   value across accepted product and decomposition surfaces.
3. App D-APP-84 selects V1 only as a Root-conditioned prospective `0.82.0`
   target. Its ruling expressly says it does not reconcile or release the
   `0.80.10`/`0.82.0` conflict.
4. The Root route notice is coordination, not authority.
5. Current Root/App executable surfaces say `0.82.0`; those bytes therefore
   conflict with, but do not supersede, the governing App basis.

No score was requested or produced.

## Method

The accepted toolbelt combined deterministic read-only repository and lockfile
inspection with three independently sealed Agent 2 lenses:

- `E1-A2-DEP`: exact dependency graph, registry provenance, SRI, cached artifact,
  shrinkwrap, and lifecycle-script analysis;
- `E1-A2-STRUCT`: lifecycle/native/WASM/notice/package/regression/conformance
  structure and evidence currency; and
- `E1-A2-GOV`: authority, adapter implementation identity, genuine conflicts,
  and lawful supersession paths.

The manager additionally reran the committed supply verifier, inspected the
current source and package policy, and read the latest applicable GitHub Actions
log. No install, package build, source repair, authority write, dependency or
lockfile edit, decision, SCOPE_CHANGE, register, or Git operation was performed.

## Coverage

Covered:

- all four direct Pi pins, the coding-agent published shrinkwrap, 140 unique
  closure artifacts, registry URLs, SHA-512 locks, and cached tarball bytes;
- install-script identities and SRI-bound static script bodies;
- native/WASM ASAR policy, package inclusion rules, Pi and complete-closure
  notice posture;
- Root reference and App executable adapter descriptors/implementations;
- current source-tree regression, Pi wire integration, conformance, lock, and
  packaging-policy evidence;
- packaged and live proof currency; and
- Root/App authority and required supersession sequence.

Not executed in this read-only checkout:

- an isolated clean install;
- a macOS package build, ASAR/unpacked asset execution, or packaged Pi turn;
- a live `0.82.0` oMLX turn; or
- any owner decision or SCOPE_CHANGE action.

These are explicit reruns, not silent assumptions.

## Validated-return inventory

| Dispatch | SHA-256 | Fan-in verdict |
|---|---|---|
| `E1-A2-DEP` | `5b60267d91ad58f4a81dc9d4c9f562d5455ee61a60da46ce1b04eb744d593b9f` | `VALIDATED WITH LIMITS`: complete required graph/integrity/lifecycle output, evidence in frozen scope, write containment held; clean install/package execution explicitly unknown. |
| `E1-A2-STRUCT` | `5f0b25a33247ee0234dabf4c03240f1f5cb27ecb9f2f82db8a86d3f26049c49f` | `VALIDATED WITH LIMITS`: complete lifecycle/package/conformance matrix and reruns; its unexecuted-test limitation is superseded only for source tests by the manager's current-tree-equivalent CI evidence, not for packaging. |
| `E1-A2-GOV` | `df3ea827324da9420ffa3a270877f7eb637c29cfe9c2ad6bc4f111614820e873` | `VALIDATED`: authority hierarchy, hashes, conflict map, identity ambiguity, decision paths, and containment all satisfy the brief. |

No return was repaired or waived. The dependency and structure returns differ
only in evidence available to each child: the dependency lens inspected
SRI-verified cached lifecycle-script bytes, so static behavior is accepted;
neither child executed a clean install, so realized lifecycle execution remains
unknown.

## Validation commands and results

| Check | Result |
|---|---|
| `git rev-parse HEAD` / `git rev-parse origin/main` | Both `97678a841ef58345c73d3470ed8de57c9b1405d2`. |
| Five accepted-basis `shasum -a 256` checks | All matched the frozen protocol. |
| `node projects/chirality-app-dev/frontend/scripts/verify-pi-supply-chain.mjs` | `PASS`: Pi `0.82.0`, 140 artifacts, SHA-512 enforced, install-script allowlist `@google/genai` and `protobufjs`, explicit native/WASM policy, notice present. |
| Full-map/SRI/cached-byte checks in `E1-A2-DEP` | 139/139 published nested entries reproduced; 140/140 registry HTTPS; 140/140 SRI; 140/140 cached tarballs hash-match; full-map SHA-256 `8fb3458ddafdbc861c5fc541775bddf2a2832d30476c78c2866535a4416fbc96`. |
| `git diff --quiet 8e156cfb...97678a841 -- runtime projects/chirality-app-dev/frontend .github/workflows/harness-premerge.yml` | Exit `0`: the tested PR #486 head and frozen basis have identical relevant trees. |
| GitHub Actions run `30778037021` | `PASS`: locked installs; Pi supply verifier; runtime tests; 141 frontend test files passed, 1 skipped; 1098 tests passed, 4 skipped; typecheck; Section 8/9 and release-quality gates passed. Focused log lines show Pi wire 11/11, Pi adapter 15/15, lock integrity 3/3, packaging policy 5/5. |

The CI run is current for the evaluated app/runtime/workflow tree, but its Linux
workflow does not build or inspect the macOS package and does not invoke the
packaged-Pi proof.

## Findings

The authoritative row set is `FINDINGS.csv`. In decision order:

1. **Authority conflict — blocker.** D-APP-72/App authority is `0.80.10`; Root
   and App executable bytes are `0.82.0`; D-APP-84 V1 is conditional, not a
   supersession.
2. **Exact dependency closure — pass.** The App lock is internally exact and
   integrity-complete for the Pi `0.82.0` candidate. Root's engine package is a
   descriptor/injected-runtime package and does not independently resolve Pi;
   the App lock owns executable closure.
3. **Install lifecycle — static pass, execution gap.** The two exact
   SRI-bound scripts are bounded on static inspection. No isolated install was
   executed, so realized install topology/effects require a candidate rerun.
4. **Native/WASM/package proof — high non-conformance.** Policy patterns exist,
   but `harness:validate:pi-packaged-proof` launches only
   `--legacy-asset-child`; the stronger production-route `runChild()` is never
   spawned. No frozen-head packaged evidence artifact is preserved.
5. **Notices — distribution blocker.** The Pi notice covers four Pi-owned
   packages. It explicitly leaves the full 140-artifact packaged-closure notice
   outstanding.
6. **Source regression/conformance — pass.** Current-tree CI proves actual Pi
   `0.82.0` source-tree wire behavior, adapter constraints, broad regression,
   lock integrity, and packaging policy.
7. **Adapter identity — blocker for D-APP-84 V1.** Root's
   `createPiOmlxEngineAdapter` and App's executable `PiAgentEngineAdapter`
   advertise the same descriptor but are different implementation families;
   the Desktop registers the App implementation. Current identity/fingerprint
   fields cannot distinguish them.
8. **Live proof — stale.** The only preserved live proof is explicitly
   `0.80.10`; the accepted reliance register requires it to be repeated when
   the Pi pin changes.
9. **Electron prerequisite — adjacent authority conflict.** D-APP-72 says
   Electron `43.1.1`; the manifest says `43.2.0`. The successor act must include
   or explicitly separate that fact instead of silently accepting it.

## Exact conflict map

| Concern | Governing/accepted state | Present evidence state | Required reconciliation |
|---|---|---|---|
| Pi version | App D-APP-72/SCA-APP-002/product/decomposition: `0.80.10` | App manifest/lock/adapter and Root descriptor: `0.82.0` | Root decision over exact generic identity, then App successor decision and App SCOPE_CHANGE. |
| Adapter implementation | Root owns generic runtime/safe adapters; App is affected client | Root and App define two same-descriptor adapter implementations; App one executes | Select a canonical implementation-family identity and encode it in contract/evidence. |
| Supply chain | Exact version-bound evidence required | Lock/integrity/cache/static lifecycle evidence passes at `0.82.0` | Preserve in decision bundle; rerun after any candidate hash changes. |
| Package/native/WASM | Version-bound packaged proof required | Source policy exists; production-route proof entrypoint is disconnected; no current artifact | Repair proof, build exact candidate, inventory/checksum/load assets, execute direct and production-route proof. |
| Conformance/regression | Exact candidate evidence required | Current source-tree CI is green and relevant tree is identical | Rerun on final post-decision candidate; retain current evidence as strong precursor. |
| Live oMLX | Repeat on Pi pin change | Preserved proof is `0.80.10` only | Repeat opt-in redacted proof at ruled candidate. |
| Notices | Four Pi packages plus full closure before distribution | Four-package notice present; full closure missing | Generate/verify full exact packaged-closure notices before release/distribution. |
| Electron prerequisite | D-APP-72: `43.1.1` | Manifest: `43.2.0` | Include in App successor/SCOPE_CHANGE or restore and revalidate. |

## Conflicts / unknowns

- No Root decision presently accepts Pi `0.82.0` or the required same adapter
  identity.
- No App successor/SCOPE_CHANGE replaces the exact D-APP-72/SCA-APP-002
  `0.80.10` and Electron `43.1.1` facts.
- It is undecided whether Root's wrapper becomes the sole executable adapter or
  the App adapter remains an explicitly registered affected-client
  implementation family.
- Clean-install realized topology, current packaged native/WASM loadability,
  production-route packaged behavior, and live `0.82.0` behavior remain
  unproven by durable candidate evidence.
- D-APP-84 P1/X1/H1/R1 native primitives, sandbox, Bash, and durable resume are
  prospective held work. This evaluation does not validate or implement them.

## Decision-ready options

### Option A — Continue V1 under an explicit evidence hold (recommended)

Retain D-APP-72 `0.80.10` as operative authority while naming `0.82.0` the
preferred decision candidate only. Repair and run the package proofs, repeat
the live proof, decide the canonical adapter implementation identity, then
issue the Root version/identity decision citing the exact candidate hashes and
this evidence. Route the accepted result to App for its own successor decision
and SCOPE_CHANGE. This best matches the already selected D-APP-84 V1 direction
without laundering bytes into approval.

### Option B — Approve `0.82.0` immediately with waivers (not recommended)

The owner could explicitly waive the missing packaged production-route, live,
identity, and adjacent prerequisite evidence, but that would contradict the
recorded TM-ROOT-106 closure criterion and D-APP-84's evidence-conditioned V1
semantics. The evaluation does not support this option.

### Option C — Restore `0.80.10`

Reject the `0.82.0` candidate, restore exact dependency/lock/descriptor/notice
state through App's governed change lane, reconcile Electron, and rerun the
entire D-APP-72 baseline. This is lawful but conflicts with the selected V1
direction and discards a technically sound 0.82 lock/test basis; no evidence
finding presently requires it.

### Option D — Reject/remediate without selecting a version

Keep D-APP-72 operative, remediate the package proof and adapter identity, and
commission a fresh exact-version evaluation. This is appropriate if the owner
does not wish to retain V1 as the preferred candidate.

## Recommendations

1. Select Option A.
2. Treat the exact candidate identity as at least: upstream Pi package/version,
   Chirality adapter implementation family/source hash, capability-profile or
   registration ID, provider/model policy identity, client composition, and
   package/lock hashes.
3. Have Root SCOPE_CHANGE / DEL-02-06 carry the generic identity and
   affected-client conformance obligations; do not let this evaluation amend
   those surfaces.
4. Have App repair the packaged-proof launcher, produce current candidate
   install/package/native/WASM/production-route/live evidence, and generate
   full-closure notices before any distribution claim.
5. After Root accepts the exact generic identity, route it to App for an
   explicit D-APP-72 successor and App SCOPE_CHANGE over decomposition, product
   docs, authority corpus, SCA maps, dependency/notice/package surfaces, and
   affected deliverables.

## Decision queue

1. Human owner: continue V1 under evidence hold, restore `0.80.10`, or reject
   the candidate?
2. Human Root owner: which adapter implementation family and identity tuple is
   the generic Root acceptance candidate?
3. Human/App owner: after Root acceptance, does the App successor explicitly
   supersede both Pi `0.80.10` and Electron `43.1.1` facts?
4. Build/validation owners: what exact immutable package and live evidence
   bundle satisfies the decision gate?

## Handoff summary

The evaluation is complete as decision support, not as `TM-ROOT-106` closure.
The lock/integrity/source-regression portion supports continued evaluation of
Pi `0.82.0`; packaged execution, live proof, canonical adapter identity, Root
acceptance, and App supersession remain open. `HANDOFF.md` names owners,
blockers, exact reruns, and derivative-package status.
