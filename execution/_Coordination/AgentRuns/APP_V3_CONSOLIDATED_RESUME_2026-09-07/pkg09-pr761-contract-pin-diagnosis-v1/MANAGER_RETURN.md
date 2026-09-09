# WORKING_ITEMS validation — PR761 packaged-security pin failure

Verdict: `ACCEPT_EXPERT_DIAGNOSIS__REPAIR_NOT_AUTHORIZED_OR_APPLIED`.

The manager independently rehashed the exact script and contract test, inspected the five pin declarations, verifier CLI/output-root/capture semantics, release-workflow invocation and workflow test, and read the retained external producer/control boundary. The expert's mixed verdict is supported:

- The five failed source substrings describe legacy producer behavior and are obsolete at the consume-only verifier locus.
- The release workflow has a real fail-closed integration defect because its three-argument invocation cannot satisfy the verifier's seven mandatory inputs and empty-output contract.
- The retained external producer demonstrates an intended governed producer boundary, but it is historical campaign control evidence rather than qualified PR761 CI wiring.
- The proposed five-locus envelope is the minimum coherent repair because changing the contract-pin manifest changes a source identity frozen inside the verifier and asserted by its test, while the workflow and its regression test must record the deferred qualification boundary truthfully.

No inert token insertion, test weakening, permissive release bypass, native qualification claim, source write, or execution is accepted. CHANGE must keep the script/tests/workflow held pending parent disposition. The recommended repair requires separate authorization, implementation, focused validation, Section 9, required PR gates, and independent review. Native/security qualification remains deferred and gating.

Exact subject: HEAD `e980f2ee773d32d1137646f437dc973126286e9b`; script SHA-256 `4fc0de92baaa01eb51fc897d7774c8f88aa75ac4a84dfe54cbf3912078faf466`; contract-pin test SHA-256 `4a498f4d2a7667346b1dc2cbfde9d01db0563f4febf07e7aef7a0c82d591e99c`.
