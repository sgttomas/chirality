# Sealed brief — self-current ledger metadata repair

Role: bounded nondelegating ephemeral Agent 2 author under Runtime SCOPE_CHANGE. Model: `gpt-5.6-sol`, medium reasoning. Role and nondelegation are instruction-asserted. Do not delegate.

Objective: produce an append-only successor to author-v4 that changes only the proposed `DecisionRef` and `Notes` fields of canonical `projects/chirality-runtime/execution/_Decomposition/RUNTIME_SCOPE_LEDGER.csv`. Do not edit canonical, SCA snapshots/pointers, audit output, prior evidence, SOWs, source, or Git state.

Read the applicable Runtime instructions, current canonical ledger, `scope/author-v4-ledger-repair/`, `scope/review-v4-ledger-repair/`, the blocking SCA-002 audit, and these exact accepted-contract records:

- `/Users/ryan/.codex/worktrees/aed8/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/pkg02/OWNER_DECISIONS/DECISIONS.md`, SHA256 `ff389e47a48386aeabe344496acf509386301aa0b72868a690ba5b4190bfe67c`.
- `/Users/ryan/.codex/worktrees/aed8/chirality/projects/chirality-runtime/execution/_Coordination/AgentRuns/APP_V3_CONSOLIDATED_RESUME_2026-09-07/pkg02/OWNER_DECISIONS/MANIFEST_v2.json`, SHA256 `f4fcbe92c15c3a9803f6835dfa1d9dc1563101ec3a6e7308b251b0570c314872`.

Required correction to author-v4 only:

1. Make the audit blocker a dated historical fact: the first postapplication audit blocked on the then-current ledger metadata. State that this proposed exact postimage resolves that metadata inconsistency. Do not say the metadata repair remains pending or that Gate 5 remains blocked pending the repair, because those statements would become stale immediately if the postimage were applied. Preserve that a fresh independent audit rerun and separate Gate 5 owner acceptance remain future acts.
2. Record that the owner accepted `HOST-P1`, `POLICY-R1`, and `ACCOUNT-WIRE-V1` as contract basis. Distinguish those accepted contract choices from still-unmet source/implementation, supplier identity/qualification, signing/identity proof, paired Runtime/App/CLI conformance evidence, recovery/lifecycle, protected-fixture, hold, hosted-readiness, and release gates. Do not say all full-wire gates remain unresolved.
3. Preserve all accurate author-v4 facts, including completed SCA-001 Stage 1 and locally validated Stage 2, pending SCA-001 publication/adoption, actual SCA-002 Gates 2–4 and application, future SCA-002 SOW propagation, historical CandidateState interpretation, one SOW/seven carriers/four objectives/66 requirements/nine holds plus R16-B, historical basis, root-runtime-1 epoch 1, and no activation/effect overclaim.

Write only under `scope/author-v5-ledger-repair/`: complete postimage, exact patch, pre/postimage indexes, checks, return, and manifest. Recompute all hashes. Verify CSV parsing, only `DecisionRef` and `Notes` change, patch strict applicability, self-current wording after hypothetical application, accepted-contract evidence, and all conservation boundaries. Status remains candidate/not applied. Return `READY_FOR_FINAL_REVIEW` or a concrete blocker.
