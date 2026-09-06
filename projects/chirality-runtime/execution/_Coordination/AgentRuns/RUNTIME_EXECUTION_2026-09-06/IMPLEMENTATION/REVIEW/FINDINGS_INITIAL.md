# Independent implementation review — initial findings

Reviewer: ephemeral Agent 2, OpenAI GPT-6; exact model ID unavailable. Role not mechanically enforced; native delegation instruction-asserted. No delegation or production writes. Write scope limited to this REVIEW directory. Read PLAN_V2, integration release, current contracts, supervisor, consent, retirement, broker, daemon/client/CLI and focused tests.

Verdict: REPAIR_REQUIRED, not product acceptance.

1. High: broker shutdown can return before an already-admitted operation acquires a worker. Awaited continuity/consent/journal work runs outside the close inventory fence. Reproduction returns acquiredAfterClose=true. Fence admission and acquisition; drain accepted operations with bounded shutdown and preserve daemon cleanup failure/retry states.
2. High: returned preflight is the same object stored as private admission authority; caller can mutate its operationId and admit another operation. Caller-owned map/binding/identity also remain mutable. Reproduction returns mutableNonceAccepted=true. Snapshot private configuration and issue separate immutable admission values, then test caller mutations.
3. Medium: compatibility regexes coerce untyped wire fields. A JSON object with toString:0 produces TypeError instead of a structured compatibility rejection. Reproduction records TypeError and no error code. Validate scalar fields and test malicious wire values.

Evidence: adversarial-repro.mjs imports the actual built implementation and uses explicitly controlled fake ports to expose scheduling/identity defects. It does not claim real provider or process proof. Independently ran four focused suites: first sandbox attempt had Unix-socket EPERM (14 failures, 25 passes); authorized escalated rerun passed all 39 tests. Existing tests did not cover the reproduced defects. Original logs preserved separately. Initial source hashes were captured during manager repairs and are observations, not an immutable pre-repair snapshot.

Additional reviewed limits: production evidence class is rejected; only controlled-worker mode is available; raw spawn has no hard sandbox, and off consent is not a containment proof. Consent/journal storage and controlled Unix-process tests cannot establish live hosted-provider behavior. No actual vendor conformance or hold release is claimed.
