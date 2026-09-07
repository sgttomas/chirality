# SCA-003 Gate 5 poststate decision subject

Status: `DECISION_READY_WITH_EXPLICIT_TEMPORAL_DISPOSITION`; owner confirmation required.

## Applied and validated state

The owner-approved SCA-003 repair changed only `RUNTIME_SCOPE_LEDGER.csv` `DecisionRef` and `Notes`, from SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920` to exact approved postimage SHA256 `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`. The immutable SCA-003 snapshot manifest is SHA256 `ce84376323a5d213c8a6dadcbf47534ecba407a9128543250f55e4b13eaaaa48`, with 16/16 members verified and exact scope-pointer parity.

Fresh independent `AUDIT_DECOMP` completed at `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Evaluation/DecompCoverage/COV_SCA003_LEDGER_REPAIR_POSTSTATE_2026-09-07_2227/`. Its structural/application-state verdict is `NON_BLOCKING_PASS`; `OUTPUT_MANIFEST.json` SHA256 is `93e17c03c0091b16abbf9b8a8d31c06dcce33f7048b2e1f6f215bd097bf79012`, and all 11 members and audit-pointer parity verify. It found zero blockers and zero warnings; 40 INFO rows are lifecycle-appropriate absent outputs while all seven carriers remain `INITIALIZED`.

Manager validation identified that the ledger's statement that a fresh audit and Gate 5 acceptance `remain future acts` was accurate at application but became temporally incomplete after the audit finished. The independent temporal recheck, return SHA256 `5542e84d47c61eb6cfda107c1e502204c941bd4a74fa6149ed8fa6f8f8630536`, confirmed this narrow issue. It also confirmed that no repository rule requires another canonical edit: the final append-only Gate 5 disposition may qualify the sentence as application-time state and make immutable audit/acceptance records and their permitted pointers the owners of later workflow status.

## Exact temporal disposition included in acceptance

For canonical `RUNTIME_SCOPE_LEDGER.csv` SHA256 `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`, the phrase `a fresh independent audit rerun and separate Gate 5 owner acceptance remain future acts` records the application-time state at SCA-003 application `2026-09-07T22:16:40Z`. Later audit status and Gate 5 disposition are owned by their immutable `AUDIT_DECOMP` and `SCOPE_CHANGE` records and permitted pointers; the ledger phrase is not relied on as current workflow status. The fresh audit completed at `COV_SCA003_LEDGER_REPAIR_POSTSTATE_2026-09-07_2227`, manifest SHA256 `93e17c03c0091b16abbf9b8a8d31c06dcce33f7048b2e1f6f215bd097bf79012`. This disposition supersedes only that application-time temporal status and changes no decomposition semantics, SOW, source, lifecycle, hold, activation, publication, adoption, hosted-readiness, supplier, fixture, or release state.

## Conserved boundaries and downstream decision

One SOW, one package, seven carriers, four objectives, 66 qualified inherited requirements, nine holds plus R16-B, historical basis `9f21e4b86c304343b92ccd9ef10895b28c1a4f48`, `root-runtime-1` epoch 1, project authorization, security/exclusion boundaries, and no activation are conserved. `HOST-P1`, `POLICY-R1`, and `ACCOUNT-WIRE-V1` remain accepted contract basis; implementation/source, supplier identity/qualification, signing/identity proof, paired Runtime/App/CLI conformance, recovery/lifecycle, protected-fixture, hold, hosted-readiness, Root-adoption, SOW-propagation, and release gates remain separate.

Recommended downstream disposition: trigger no SOW, source, supplier, process, credential, lifecycle, activation, hold, protected-fixture, hosted-readiness, Root-adoption, or release work through this confirmation. After acceptance, seal the immutable Gate 5 acceptance record and permitted scope pointer, then hand the exact accepted Runtime poststate to CHANGE for controlled staging/publication under the existing standing Git grant. Future SCA-002 DEL-02-06/09 propagation remains separately governed and must bind the accepted Runtime publication identity.

## Precise requested decision

> Accept the exact SCA-003 Gate 5 poststate and temporal disposition. I confirm that only ledger `DecisionRef` and `Notes` changed to SHA256 `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`; accept SCA-003 snapshot manifest SHA256 `ce84376323a5d213c8a6dadcbf47534ecba407a9128543250f55e4b13eaaaa48` and the fresh audit evidence manifest SHA256 `93e17c03c0091b16abbf9b8a8d31c06dcce33f7048b2e1f6f215bd097bf79012`; and adopt the stated application-time temporal qualification so immutable audit/acceptance records and permitted pointers own later status. Trigger no other downstream rerun through this decision. Authorize the immutable Gate 5 acceptance record, permitted scope pointer update, and handoff to CHANGE for controlled Git staging/publication under the existing standing grant. This is not product release and grants no SOW, source, supplier, process, credential, lifecycle, activation, hold, protected-fixture, hosted-readiness, Root-adoption, or release authority.

This is the separate postchange confirmation required by `agents/AGENT_SCOPE_CHANGE.md` lines 590–597.
