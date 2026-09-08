# Runtime SCOPE_CHANGE final prospective candidate handoff

Verdict: `PASS_DECISION_READY_PROSPECTIVE`. The exact three-file Runtime candidate is complete, independently reviewed and ready for the applicable Runtime Gate 2-4 owner disposition. It is `PROSPECTIVE / NOT EFFECTIVE`; no Runtime canonical file, SCA pointer, SOW, source or Git state has been changed.

## Exact reviewed candidate

Application basis: original Runtime checkout `/private/tmp/chirality-runtime-custody-amendment-20260906`, HEAD = `origin/main` = `e8cdc460cffccfe9e58ab4e5b9bbc05350c09327` after parent/CHANGE-verified safe synchronization. The two existing canonical target preimages and seven conserved inputs were unchanged by synchronization.

- Candidate patch: `author-v2/CANDIDATE.patch`, SHA256 `4be28f9e5929765c8666908e8895ffa2a8d75d2f0df66c133e1b383ee1e94395`.
- New supplement postimage: SHA256 `19baaea22ba3a5b2dc465c30f7e8273db7b1833fd4a9bf6c2de0fc6056dcdd9d`.
- Decomposition postimage: SHA256 `413687ca6a857f5464a3205e9f9c4b29ace512c8d2b67dfa095ef3640fab883e`.
- Scope-ledger postimage: SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`.
- Author manifest: SHA256 `54a94c193e0064ce2242c58dca2031959b8bca267593de90d2a9eed0574c005a`; manager rehashed all members and rechecked patch applicability/whitespace.
- Independent final review: `review-v2/RETURN.md`, SHA256 `9ec887392b6fd707932642899e54baffb46462feeebc4b4f5567382529bf25b4`, verdict `PASS_DECISION_READY_PROSPECTIVE`.
- Review manifest: SHA256 `f56e83895059b7b138a6d3c046430d1a8a95d78e425339ceaae165b0ca641665`; manager validated declared members and exact frozen inputs.

Root D36 is now published: live D36 SHA256 `2697862a31ee856ae923c91af38a5e07f8997115a4bd1baabf083afb069939b1`, PR #748 exact head `f3f68d744fc745996776cfbe8f30cbd2bb7b100a`, fetched main `e8cdc460cffccfe9e58ab4e5b9bbc05350c09327`. The candidate binds that identity and publication evidence while retaining its own Runtime prospective status.

## Scope and conservation

The amendment modifies authority interpretation for DEL-02-09 REQ-001/002 and DEL-02-06 CLM-003/REQ-010 only. The ledger changes only `DecisionRef` and `Notes` and retains `GATE3_REVIEW_NOT_ACCEPTED`. The decomposition update is append-only. One SOW row, PKG-02, seven carriers, OBJ-001/002/004/007, 66 qualified inherited requirement identities, nine holds plus separate R16-B, all seven full-wire gate rows, historical DEL-02-06/09 basis `9f21e4b86c304343b92ccd9ef10895b28c1a4f48`, and `root-runtime-1` epoch 1 are preserved.

Historical author-v1/review-v1 artifacts remain immutable evidence of the initial prospective identity and its single returned blocker. Author-v2 resolved that blocker by binding the live/published Root identity, applied review/manifest, publication evidence and Runtime sync evidence. No result is silently overwritten.

## Exact next owning decision

The already approved narrow semantic boundary does not need a repeat vote. The genuinely required next decision is Runtime's own combined Gate 2 impact confirmation, Gate 3 exact-amendment approval and Gate 4 propagation-plan approval over the concrete subjects in `DECISION_SUBJECT.md`.

Governing citations: `agents/AGENT_SCOPE_CHANGE.md` Gate 2 begins at line 268 and requires human impact confirmation at line 343; Gate 3 begins at line 347 and defines human confirmation as formal amendment approval at line 403; Gate 4 begins at line 407 and requires propagation confirmation at line 485. The exact proposed disposition is written verbatim in `DECISION_SUBJECT.md`.

That decision may authorize application/validation of exactly the three candidate files plus creation of the new immutable SCA snapshot and its owning pointer update. It does not accept future DEL-02-06/09 SOW postimages, because those must cite the actual accepted canonical Runtime commit produced later.

## Remaining gates after that decision

1. SCOPE_CHANGE applies the exact candidate and records the immutable SCA application state.
2. A new independent poststate AUDIT_DECOMP validates actual canonical state; owner provides Gate 5 acceptance.
3. CHANGE publishes the exact accepted Runtime canonical subject and records its actual commit/fetched-main identity.
4. Root performs required successor adoption for the exact Runtime transition.
5. A bounded author prepares full DEL-02-06 CLM-003/REQ-010 and DEL-02-09 REQ-001/002 SOW postimages using the actual canonical commit; separate review and owning propagation acceptance/application follow, then required Root adoption.
6. Affected App/CLI/client notices are routed as drafts until accepted identities exist. Complete wire/recipient delivery, durable lifecycle, successor recovery, source/synthetic activation, supplier qualification, rebuilt paired evidence, protected fixtures and owner release remain separate gates.

Agent execution record: author and independent reviewer were separate actual Agent 2 instances, both explicitly allocated `gpt-5.6-sol` with medium reasoning and instructed not to delegate. Their role/model/nondelegation evidence is instruction-asserted. Manager validated both returns and exact identities.

