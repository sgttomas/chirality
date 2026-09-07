# Final self-current SCA-002 ledger metadata repair remediation

Verdict: **READY_FOR_FINAL_REVIEW**.

This append-only author-v6 successor changes only the proposed canonical ledger's `DecisionRef` and `Notes`. The canonical field text no longer calls the row or postimage proposed/candidate. It records the first postapplication audit dated 2026-09-07 as a historical finding on the then-current metadata, states that the exact ledger state records resolution of that inconsistency, and preserves a fresh independent audit rerun and separate Gate 5 owner acceptance as future acts.

The accepted-contract citations now use exact absolute aed8 evidence paths. `DECISIONS.md` rehashes to `ff389e47a48386aeabe344496acf509386301aa0b72868a690ba5b4190bfe67c`; `MANIFEST_v2.json` rehashes to `f4fcbe92c15c3a9803f6835dfa1d9dc1563101ec3a6e7308b251b0570c314872`. `HOST-P1`, `POLICY-R1` and `ACCOUNT-WIRE-V1` remain accepted contract basis, distinct from the specified still-unmet implementation, evidence, recovery, fixture, hold, readiness and release gates.

Exact candidate identities:

- canonical preimage `projects/chirality-runtime/execution/_Decomposition/RUNTIME_SCOPE_LEDGER.csv`: SHA256 `e3621b3cef4f58644c26d830e5f991e699e955413e15842b4f615dcb67a61920`
- complete postimage `POSTIMAGE/RUNTIME_SCOPE_LEDGER.csv`: SHA256 `bffda2701dea3667a63f72194404db72b20520802a7d840af13ac456fb1f149d`
- one-file patch `CANDIDATE.patch`: SHA256 `9b2e2d0975cdacebb7aabd826bc339389afb3130284548b620346a8eb9a20855`

Both CSVs parse as one row with 14 fields. Only `DecisionRef` and `Notes` change. Strict applicability and whitespace checks pass with numstat 1/1, all cited evidence identities verify, and all v5 conservation boundaries remain intact.

Status remains candidate/not applied. Fresh independent review and separate owner approval of the exact v6 bytes remain required before governed application. No author-v5, canonical, SCA, audit, SOW, source, process or Git state was modified. Role and nondelegation are instruction-asserted; no delegation performed.
