# Expert return — PR761 packaged-security contract drift

Verdict: `MIXED_CONTRACT_DRIFT_AND_REAL_CALLER_INTEGRATION_DEFECT`.

Attribution: fresh nondelegating Agent 2 `/root/app_pkg09/pr761_contract_expert`, `gpt-6-astra`, high reasoning. The review was read-only. No test, build, fixture, native, network, supplier, account, Git, or source operation ran.

## Five failed pins

All five literals are obsolete at `scripts/run-packaged-security-proof.mjs`, which is now a consume-only verifier rather than the legacy launcher/producer:

- `chirality-packaged-security-proof/v1` must become the truthful v2 summary contract. Both fail and completed summaries emit `chirality-packaged-security-proof/v2` with `mode: consume-only` at lines 1387 and 1464.
- `CHIRALITY_USER_DATA: userDataRoot` remains a producer obligation for isolated credential mutation. The verifier retains the coordinator-supplied credential helper at lines 1301–1350 and consumes credential mutation/secret-scan records at lines 1419–1433.
- `CHIRALITY_SKIP_CLI_LAUNCHER: '1'` remains a producer launch restriction. The verifier launches no process, so adding it here would be inert.
- `CHIRALITY_RENDERER_SECURITY_PROBE: '1'` remains a producer obligation. The verifier still requires renderer-security success in the aggregate pass at line 1292 and derives it from retained logs.
- `CHIRALITY_EGRESS_LAYER_PROBE_URL: EGRESS_PROBE_DECOY_URL` remains a producer negative control. The application uses the fixed `:8443` destination, while the verifier rejects unexpected destinations; the fixed-destination log alone cannot prove the decoy was supplied.

Adding inert strings or environment assignments to the verifier would be invalid.

## Real integration defect

The verifier requires seven values at lines 213–220: captured input, accepted source binding, output root, app path, source revision, S0 evidence, and S0 run ID. Its five path arguments must be absolute, and output root must already exist, be a nonsymlink directory, and be empty.

`frontend/package.json` exposes the verifier as `proof:packaged-security`, but `.github/workflows/desktop-release-template.yml` lines 154–157 still supplies only app path, output root, and source revision. It supplies no captured input, accepted source binding, S0 evidence, or run ID and does not establish the verifier's empty-output precondition. Therefore the release workflow cannot lawfully produce the proof it later reads.

An external producer exists in the retained candidate-v4 coordination controls: `plan_factory.py` supplies the four required producer environment assignments and all seven verifier arguments; `S0_PRODUCER.mjs` invokes the credential helper; `capture_builder.py` requires independently reviewed measurements before capture assembly. That producer is bespoke to the deferred, governed S0 qualification campaign, bound to its historical base/root, and is neither CI-integrated nor qualified for PR761.

## Recommendation

Use option (a): synchronize the verifier contract and place an explicit fail-closed release-workflow hold at the unavailable S0 qualification boundary. Do not skip the proof, synthesize inputs, or claim the external producer is operational CI support.

Minimum exact source/config loci:

1. `frontend/src/__tests__/contract-pins.manifest.ts`: describe the consume-only verifier, pin v2, remove the four legacy launcher literals, and preserve the obligations with semantic tests at their actual producer/security boundaries.
2. `frontend/scripts/run-packaged-security-proof.mjs`: update only the frozen hash/byte identity for the changed contract-pin manifest.
3. `frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`: update the exact manifest identity expectation and retain the semantic verifier tests.
4. `.github/workflows/desktop-release-template.yml`: fail closed with an explicit deferred-S0 qualification hold before build/native release work instead of invoking the verifier with incomplete inputs.
5. `frontend/src/__tests__/scripts/desktop-release-workflow.test.ts`: assert the hold and ordering; remove assertions for the obsolete invocation. A successful skip or permissive fallback is forbidden.

The generic `contract-pins.test.ts` evaluator does not need modification. Preserve the accepted S0 snapshot/binding; publish a separately reviewed successor identity rather than rewriting prior evidence.

Required validation after an authorized repair: focused contract-pin, verifier, renderer-policy, and workflow tests; registered typecheck; `npm run harness:validate:section9`; then required PR gates.

Static repair does not qualify packaged behavior. Accepted exact-source/control/input provenance, package review, native admission, actual two-lifecycle S0 UI/HTTP/component/security observations, credential isolation, decoy activation, process/endpoint cleanup, and independent evidence review remain gating. S1 remains `INAPPLICABLE_OWNER_DEFERRED`; signing, distribution, and release remain outside this diagnosis.

If the coordinated five-locus correction cannot be accepted, use option (b): hold the affected App source component and publish only preserved candidate/evidence plus unaffected completed work.
