# SCA-002 Gate 5 ledger metadata repair author return

Verdict: **READY_FOR_INDEPENDENT_REVIEW**.

The complete one-file candidate repairs the authoritative ledger’s current account-control metadata while preserving its schema and every other value. `DecisionRef` now records published Root D36, Runtime Gate 2 acceptance, Gate 3 and Gate 4 approval, exact SCA-002 canonical application, the blocking Gate 5 audit, and the pending repair, clean audit rerun and owner acceptance. `Notes` records that the narrow supplement is applied canonical but remains ineffective for dependent reliance until Runtime publication/main identity and required Root successor adoption. Project authorization, consequential-work preconditions, all full-wire/source gates and no activation remain.

`CandidateState = GATE3_REVIEW_NOT_ACCEPTED` is byte-value unchanged and explicitly defined as the historical migration/decomposition candidate-stratum field, not current SCA-002 Gate 3 status.

## Exact candidate

- `projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/scope/author-v3-ledger-repair/POSTIMAGE/RUNTIME_SCOPE_LEDGER.csv`: SHA256 `c6e985bc25bf4f10ca8a8f27d82484736e0febbe85a95a6e3d9e2cc825c4cadc`
- `projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/scope/author-v3-ledger-repair/CANDIDATE.patch`: SHA256 `ecb1cb62c2b8bb1b060cca52e02867d777464eab9726b54849fc1f17064838fd`
- Canonical preimage: SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`

CSV parsing, exact field comparison, patch applicability, whitespace, conservation and overclaim checks pass. Only `DecisionRef` and `Notes` change.

This candidate has no effect until separate independent review, owner approval and governed application. It does not close Gate 5 or authorize publication, Root adoption, SOW propagation, source/wire activation, supplier/fixture use, lifecycle transition or release. No canonical, SCA-002, audit, SOW, source, Root, pointer, process or Git state was modified. Role and nondelegation are instruction-asserted.
