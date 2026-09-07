# Self-current SCA-002 ledger metadata repair author return

Verdict: **READY_FOR_FINAL_REVIEW**.

This append-only author-v5 successor corrects only the proposed canonical ledger's `DecisionRef` and `Notes`. The first postapplication audit dated 2026-09-07 is now a historical fact: it blocked on the then-current ledger metadata. The proposed exact postimage states that it resolves that inconsistency if applied, while a fresh independent audit rerun and separate Gate 5 owner acceptance remain future acts. It does not say that metadata repair remains pending or that Gate 5 remains blocked pending repair.

The candidate also records the owner's accepted `HOST-P1`, `POLICY-R1` and `ACCOUNT-WIRE-V1` contract basis using `DECISIONS.md` SHA256 `ff389e47a48386aeabe344496acf509386301aa0b72868a690ba5b4190bfe67c` and `MANIFEST_v2.json` SHA256 `f4fcbe92c15c3a9803f6835dfa1d9dc1563101ec3a6e7308b251b0570c314872`. It distinguishes those accepted choices from still-unmet source/implementation, supplier identity/qualification, signing/identity proof, paired Runtime/App/CLI conformance evidence, recovery/lifecycle, protected-fixture, hold, hosted-readiness and release gates.

Exact candidate identities:

- canonical preimage `projects/chirality-runtime/execution/_Decomposition/RUNTIME_SCOPE_LEDGER.csv`: SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`
- complete postimage `POSTIMAGE/RUNTIME_SCOPE_LEDGER.csv`: SHA256 `ea49773b7385473bd068144d40dfcb5a8be7fbba61aa5565302d4fcef62874be`
- one-file patch `CANDIDATE.patch`: SHA256 `4be2ef41f8f622d31835f0e4e3d6e9d5f9740a1a283a598ff12fff284474e80a`

Both CSVs parse as one data row with 14 fields. Only `DecisionRef` and `Notes` change, and the patch passes strict applicability and whitespace checks with numstat 1/1. The candidate preserves completed SCA-001 Stage 1 and locally validated Stage 2, pending SCA-001 publication/adoption, actual SCA-002 Gates 2–4 and application, future SCA-002 SOW propagation, historical `CandidateState`, one SOW, seven carriers, four objectives, 66 requirements, nine holds plus R16-B, historical basis `9f21e4b86c304343b92ccd9ef10895b28c1a4f48`, `root-runtime-1` epoch 1, project authorization, and no activation or effect overclaim.

Status remains candidate/not applied. Fresh independent final review and separate owner approval of the exact v5 bytes are required before governed application. No canonical, SCA snapshot or pointer, audit, prior evidence, SOW, source, process, Git or other state was modified. Role and nondelegation are instruction-asserted; no delegation performed.
