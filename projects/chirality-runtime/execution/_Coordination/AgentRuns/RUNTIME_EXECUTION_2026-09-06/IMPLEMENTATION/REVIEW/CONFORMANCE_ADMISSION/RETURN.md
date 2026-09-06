# Independent conformance admission review — initial verdict

OpenAI GPT-6; serving model ID unavailable. Actual ephemeral Agent2, instruction-asserted and not mechanically enforced. Read-only product review; no vendor execution, account use, owner acceptance, product edits or delegation.

## Verdict: changes required

C1 (P2): admission hashes the current disk bundle without binding it to the daemon generation. A running process loaded under A can admit an externally accepted B record after an ordinary in-place update, while Node still executes cached A modules. `packages/core/src/runtime-conformance.ts:179` inventories current disk files and `:201` consumes that inventory for each admission; there is no process-start baseline. This is an operational restart gap, not a claim of an atomic launch race. Parent accepted it and dispatched a repair. Require a module/process-start disk inventory baseline, fail closed after observed generation drift, and require process restart. Retain the explicit limit that startup disk bytes do not prove loaded-module or dependency-resolution bytes.

`generation-repro.mjs` uses the actual built computeRuntimeArtifactDigest helper against an evidence-local module. Repeated import retains A after disk replacement by B while the actual digest changes. It passed (`GENERATION_REPRO.log`). This is a controlled cache/digest reproduction plus source-path inference; it does not create production acceptance or perform hosted admission. Initial script import-path error was corrected before the recorded successful run.

## Confirmed boundaries

Regular acquire and startManager both enter acquireInternal; the real path rejects missing configuration before account reads and calls verifyConfiguredRuntimeConformance before launch. Explicit controlledForTests is the only fixture-launcher assignment; hosted-boundary preflight rejects that factory, and standalone closed configuration cannot select it. Login/preflight is separate from execution admission.

Verifier checks all 18 attempted/passed limbs, exact binding values, expiry, fixed supply metadata and actual supply bytes, actual ordered disk artifact/manifests/lock hashes, and externally configured owner-act content hash plus a private accepted/revoked record. Acceptance and source are rechecked per admission, with no reusable launch token or admission cache. Activation/gate identity is host supplied: its required update remains an owning workflow responsibility. The owner-act hash is asserted external authority, not machine interpretation of human intent; limb evidence hashes require external review, not inferred successful canaries.

On-disk first-party inventory includes every package dist tree; it does not establish already-loaded module bytes, module-resolution links, installed third-party bytes, or atomicity with subsequent launch. Read-before/after checks narrow observable mutation windows but do not eliminate all races. No true tool-path conformance, owner acceptance, release or hold lift is established by these tests.

## Validation

Focused conformance/supervisor/standalone run: 73 passed, 1 failed of 74. Failure at tests/codex-supervisor.test.ts:126 expected account-binding-unavailable but received compiled-policy digest mismatch. Reported to parent for coherent build/backcheck; not silently counted as a pass or yet classified as a conformance defect. See TESTS.log and SOURCE_DRIFT.json. A later immutable repair record must supersede this verdict; this initial record does not review ongoing manager ask routing.
