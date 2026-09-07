# SCA-003 ledger-repair poststate decomposition coverage report

Overall verdict: **NON_BLOCKING_PASS** for presentation to the accountable human at separate Gate 5. The authoritative ledger repair, filesystem coverage, conserved boundaries, immutable SCA-003 snapshot, active scope pointer and historical evidence all verify. This audit is derivative evidence tied to `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_ScopeChange/SCA-003_2026-09-07_1616/SNAPSHOT_MANIFEST.json`; it does not replace decomposition truth or grant Gate 5 acceptance, closure, publication or any later act.

## Exact poststate result

The live canonical hashes are:

- `ACCOUNT_CONTROL_AUTHORITY_DISPOSITION.md`: `19baaea22ba3a5b2dc465c30f7e8273db7b1833fd4a9bf6c2de0fc6056dcdd9d`
- `Chirality_Runtime_SOFTWARE_DECOMP_v1_0.md`: `413687ca6a857f5464a3205e9f9c4b29ace512c8d2b67dfa095ef3640fab883e`
- `RUNTIME_SCOPE_LEDGER.csv`: `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`

The ledger is byte-identical to the approved author-v6 postimage. Patch SHA256 `9b2e2d0975cdacebb7aabd826bc339389afb3130284548b620346a8eb9a20855` has one removed row and one inserted row; CSV parsing confirms that only `DecisionRef` and `Notes` changed from preimage SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`. The other twelve fields, including `CandidateState`, are identical.

The SCA-003 snapshot manifest is SHA256 `ce84376323a5d213c8a6dadcbf47534ecba407a9128543250f55e4b13eaaaa48`. All 16 members match their declared hashes and byte counts. `_ScopeChange/_LATEST.md` is SHA256 `941753dfbe4ebedd9385aa8934acefe7c4a46360fbf126648ba93a3d233b3972` and is byte-identical to SCA-003 `LATEST_POSTIMAGE.md`.

## Check verdicts

| Check | Verdict | Evidence |
| --- | --- | --- |
| 1 Package forward coverage | PASS | One declared `PKG-02_Runtime_Product`; exact folder exists. |
| 2 Deliverable forward coverage | PASS | Seven declared deliverables; seven exact folders exist. |
| 3 Reverse folder coverage | PASS | No undeclared package or deliverable folder exists in scope. |
| 4 ID consistency | PASS | Package and all seven full deliverable slugs match the authoritative register and filesystem. |
| 5 Context fidelity | PASS | Seven contexts match name, package, type, responsible party, description and `ContextEnvelope = M`. |
| 6 Artifact presence | PASS with INFO | All seven live contracts validate as `SOW_V1`; 40 anticipated production outputs remain absent at `INITIALIZED` and are not inferred complete. |
| 7 Objective mapping | PASS | `OBJ-001`, `OBJ-002`, `OBJ-004` and `OBJ-007` each map to all seven existing, non-retired deliverables. |
| 8 Ledger integrity | PASS | The mapping is valid. The first blocked audit is dated history, the inconsistency is recorded resolved, current SCA state is explicit, and Gate 5 remains pending. |
| 9 Derivative package parity | SKIPPED | Variant-owned DOMAIN check; exact SOFTWARE canonical/snapshot parity is evaluated in Checks 8 and 10. |
| 9b Package-shape conformance | PASS | The working surface names authoritative registers and labels `TRACE_PREVIEW.csv` and `COVERAGE_PREVIEW.json` as derived publication artifacts. |
| 10 Active snapshot and handoff | PASS | All 16 SCA-003 members verify; pointer equality passes; the handoff claims no audit, Gate 5, publication, adoption or release completion. |
| 11 Lifecycle distribution | PASS | Seven `INITIALIZED`; no lifecycle mutation. |

## Resolved blocker and state meaning

The first postapplication audit remains immutable history at `COV_SCA002_ACCOUNT_AUTH_POSTSTATE_2026-09-07_2050/`. Its manifest, return and issue log retain SHA256 values `f2044a82fe16474865c6c1f99d66aa9c886851afedb1b72d22924f9ed7cc8369`, `912d287934e65e3d224194803f5f54f872a35868e673d47c220186a5282979f1`, and `130ae0490e693ee92a2774b88efb08297bdc2d9b7660a8c5b4a7a23fa9e59af7`. The current ledger calls that blocker a historical finding, states that the exact ledger state records resolution of the metadata inconsistency, and leaves this fresh audit plus separate Gate 5 owner acceptance as future acts. Its changed fields contain no repair-pending, Gate-5-blocked-pending-repair, or proposed/candidate self-label.

`CandidateState = GATE3_REVIEW_NOT_ACCEPTED` is unchanged. The current `Notes` explicitly defines it as preserved historical migration/decomposition candidate-stratum metadata rather than the current SCA-002 Gate 3 or SCA-003 state. The same row records SCA-002 Gate 2 accepted, Gates 3–4 approved and canonical application executed.

## Contract distinction and conservation

The absolute external owner evidence rehashes exactly: `DECISIONS.md` is SHA256 `ff389e47a48386aeabe344496acf509386301aa0b72868a690ba5b4190bfe67c`; `MANIFEST_v2.json` is SHA256 `f4fcbe92c15c3a9803f6835dfa1d9dc1563101ec3a6e7308b251b0570c314872`. It records `HOST-P1`, `POLICY-R1`, and `ACCOUNT-WIRE-V1` as accepted contract basis. The ledger separately retains unmet source/implementation, supplier identity/qualification, signing/identity proof, paired Runtime/App/CLI conformance, recovery/lifecycle, protected-fixture, hold, hosted-readiness and release gates.

One `SOW-104` IN row, one package, seven carriers, four objectives, 66 unique qualified inherited requirements, nine held bindings plus separate R16-B, historical basis `9f21e4b86c304343b92ccd9ef10895b28c1a4f48`, `root-runtime-1` epoch 1, project authorization, security/exclusion/REQ-027 boundaries and no activation remain. The protected deliverable directory has no diff from basis `579015fab0c121e702d10c255d2824a86bcad58d`. This audit introduced no SOW, source, context, status, dependency, supplier, process, credential, fixture, hold, Git, hosted-readiness, Root-adoption, publication or release act.

## What remains

No audit remediation is required. The next lawful act is the separate Gate 5 owner presentation required by `agents/AGENT_SCOPE_CHANGE.md` lines 590–597: summary of the exact ledger-only change; this postchange validation result; recommended downstream reruns; handoff-state and closure verdict; and any handoff to CHANGE for Git staging. The human must confirm the postchange state and decide which downstream reruns to trigger.
