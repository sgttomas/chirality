# Runtime conformance admission return

OpenAI GPT-6; exact serving model ID unavailable. Agent2 instruction-asserted, not mechanically enforced. No delegation, canary execution, hosted accounts, owner act or hold lift.

## Reachable production behavior

CodexSupervisor.acquireInternal now rejects missing conformance before production account reads or launch. Both regular and manager workers use this same path. Configured admission validates actual account/consent/native policy, then verifyConfiguredRuntimeConformance before launch. Login and consent-management preflight remain separate. Explicit controlledForTests factory remains structurally excluded from production conformance and hosted-boundary admission.

Standalone hosted worker optionally carries conformance:{recordPath,acceptancePath,ownerActPath,ownerActSha256,activationId,gateIdentity}. Record/acceptance paths are relative to its private runtime root and outside worker-private storage; they are converted to canonical absolute paths for the supervisor. Owner-act path is canonical absolute external evidence. Missing configuration does not silently enable workers. Existing managed/network-approval wiring retained.

## Verifier and fingerprints

RuntimeConformanceVerifier.verify checks a closed record, full attempted/passed evidence limbs, exact accepted supply SHA/size/version, expiry, and exact root/cwd/policy/config/account/consent/activation/gate/source/package bindings. Source and package digests hash actual ordered canonical file bytes, sizes and paths. Production inventory derives every first-party Runtime package dist tree plus package manifests and workspace lockfile; public callers cannot substitute an innocuous artifact subset. The exact accepted vendor payload is independently rehashed. Source/record hashes and external acceptance are rechecked across verification. No cache and no expensive model probes are run during admission.

The first-party closure and lockfile are not proof of installed third-party dependency bytes. Source acceptance must retain that calibration; this helper does not claim broader installed-byte attestation.

codexRuntimeConformanceConfigDigest fingerprints model, executable, full continuity identity, private home/directory, protected paths, actual account digest, attributed provider-network consent, command-network posture, effective timeout/worker bounds, generated native config and exact expected permissions. Conformance record/acceptance locations and external act pins are excluded to avoid a self-referential hash fixed point. Actual activation/gate identity is separately bound. consentVersion is SHA256 of the actual consent record, not an invented numeric counter.

## Authority boundary

RuntimeConformanceFileAcceptancePort reloads a private exact acceptance record and verifies the externally configured owner-act content pin. Acceptance record binds exact conformance SHA, computed source digest, activation/gate, expiry and accepted/revoked state. The host-selected owner-act pin is externally asserted authority: hashing its bytes does not mechanically prove a human approved the text. Public client requests cannot select or mint this port. Pure inspectRuntimeConformanceRecord is explicitly mechanical only and cannot issue admission. A branded result is an in-process observation; every subsequent admission must verify again.

No test record self-authorizes production: even a controlled accepted lookup fails against fixture executable bytes. No actual owner acceptance record was created. Source acceptance and all owning release/hold acts remain separate.

## Source mapping and limitations

Release plan §6.1/6.2 lines544–553 and sentinel cadence lines345/357 require actual turn-path primary/descendant attempts, missing attempt/denial failure, owner-live native descent, policy readback, protected read/file-change/shell-write, network/process boundaries and the same role/approval/environment gates. The 18 limb names are a derived verifier checklist for these accepted requirements, not newly ruled requirements. Role checks test the accepted posture including instruction-asserted/not-mechanically-enforced labels; they do not silently demand a mechanical non-delegation guarantee. Network/approval expected outcomes are those of the exact configured accepted posture. The external acceptance process evaluates the referenced fixture evidence; the helper cannot infer genuine observations from booleans alone.

Canonical root/policy/config/pin/package/activation/G4/G7 changes invalidate bindings. GateIdentity must be updated by the owning activation/release workflow; the helper does not invent or perform that act. DEL12 CLM004/005 and held bindings preserve exact source acceptance and the separation between evidence completeness and release authority.

## Validation

Workspace build passes. Conformance40 tests, supervisor23 tests and standalone11 tests pass (74 total). They cover missing/failed/unattempted limbs, all binding drift, expiry, aliases/permissions, actual source bytes/order, revoked external acceptance, fixed-supply exclusion, whole first-party inventory, and missing-conformance regular/manager rejection before launch. Existing controlled approval and native-policy fixture behavior retained; network_proxy fixture readback matches its explicit command posture. No live canaries or provider execution occurred in this tranche.
