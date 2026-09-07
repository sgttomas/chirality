# SCA-002 Gate 5 ledger-repair decision subject — successor v2

Status: `PASS_DECISION_READY_METADATA_REPAIR`; exact owner approval required before application.

This append-only subject supersedes `GATE5_REPAIR_DECISION_SUBJECT.md` for the requested decision. The earlier subject and author-v4/review-v4 evidence remain immutable history.

## Why this correction is required

The owner-approved SCA-002 patch was applied exactly. The first independent poststate audit dated 2026-09-07 verified its bytes, snapshot, pointer and conserved invariants but blocked Gate 5 closure because canonical ledger `DecisionRef` and `Notes` still described already completed approval/application as pending. Audit return SHA256: `912d287934e65e3d224194803f5f54f872a35868e673d47c220186a5282979f1`; audit manifest SHA256: `f2044a82fe16474865c6c1f99d66aa9c886851afedb1b72d22924f9ed7cc8369`.

The v5 successor addressed that finding and distinguished the owner-accepted `HOST-P1`, `POLICY-R1`, and `ACCOUNT-WIRE-V1` contract basis from the remaining implementation and evidence gates. Manager validation returned v5 only because its future canonical row called itself a `proposed exact postimage`, which would become stale at application. V6 changes only that self-reference and makes the accepted-contract evidence locators absolute. It introduces no new authority or semantic boundary.

## Exact independently reviewed correction

- Canonical preimage: `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Decomposition/RUNTIME_SCOPE_LEDGER.csv`, SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`.
- Exact one-file patch: `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/scope/author-v6-ledger-repair/CANDIDATE.patch`, SHA256 `9b2e2d0975cdacebb7aabd826bc339389afb3130284548b620346a8eb9a20855`.
- Complete postimage: `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/scope/author-v6-ledger-repair/POSTIMAGE/RUNTIME_SCOPE_LEDGER.csv`, SHA256 `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`.
- Author manifest: `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/scope/author-v6-ledger-repair/MANIFEST.json`, SHA256 `f98e20e7db16bcabfeed39329b1c65241bebd4171a7be1f75f5dc1b300d19f59`.
- Independent review return: `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/scope/review-v6-ledger-repair/RETURN.md`, SHA256 `710226fd44079818d937729fc08aa5763b461f62b27ea9d93aa2a645fff8bed0`, verdict `PASS_DECISION_READY_METADATA_REPAIR`.
- Independent review manifest: `/private/tmp/chirality-runtime-custody-amendment-20260906/projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/scope/review-v6-ledger-repair/MANIFEST.json`, SHA256 `721a73781e09672ddf49984278609c2cc1391436298a391f72a854aebd5ac7fe`.

Only `DecisionRef` and `Notes` change. The other twelve fields, including historical `CandidateState = GATE3_REVIEW_NOT_ACCEPTED`, remain byte-identical. The exact ledger state records the first audit blocker as dated history and its metadata inconsistency as resolved, while leaving the clean audit rerun and separate Gate 5 owner acceptance as future acts. It records the three accepted contract choices and retains the still-unmet source/implementation, supplier identity/qualification, signing/identity proof, paired Runtime/App/CLI conformance, recovery/lifecycle, protected-fixture, hold, hosted-readiness and release gates.

Under `agents/AGENT_SCOPE_CHANGE.md`, the exact corrective impact requires human confirmation at Gate 2 (lines 341–343), the exact amended text requires human approval at Gate 3 (lines 399–403), and the limited application/snapshot/pointer/audit plan requires human approval at Gate 4 (lines 475–485). This is one narrow exact-text repair decision, not a repeat decision on the already accepted account-only boundary or wire contract.

## Precise requested approval

> Approve exact Runtime ledger repair v6: apply patch SHA256 `9b2e2d0975cdacebb7aabd826bc339389afb3130284548b620346a8eb9a20855` to canonical preimage SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`, producing postimage SHA256 `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`. I confirm its corrective impact, approve its exact `DecisionRef` and `Notes` text, and approve only the one-file application, owning immutable repair snapshot, permitted `_ScopeChange/_LATEST.md` pointer update, and fresh independent `AUDIT_DECOMP` rerun. This does not repeat the accepted semantic or contract decisions and grants no Git publication, Root adoption, SOW, source, supplier, lifecycle, activation, hosted-readiness, protected-fixture, hold, or release authority. Gate 5 owner acceptance remains separate after a clean audit.

After exact application and the clean audit rerun, SCOPE_CHANGE must present the resulting postchange state for the separate Gate 5 confirmation required at `agents/AGENT_SCOPE_CHANGE.md` lines 590–597. Until that confirmation, closure and CHANGE publication remain held.
