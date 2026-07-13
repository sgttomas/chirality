# Stage-1 Identity

- Accepted Stage-1 commit `31c35ea9798c29cd0af16b7089186f3942dcfcb1` exists with subject `pilot: complete PKG-13 frozen scope wave`.
- The workspace candidate, P4 extraction, and exact commit blob at the live DEL-13-03 `ScopeOfWork.md` path are byte-identical at SHA-256 `cde7f4b4332c5e89dbe72afca11f1dbc907b06a459f56962b1c1cd35fad0df4c`.
- All eight files in `stage1_evidence/` are byte-identical to the matching committed Stage-1 run-record artifacts.
- The reproduced claim map is byte-identical to Stage 1 at SHA-256 `8655dfbcee182cc4e97a348f0816068c5160d759dfc8b29fe47f7b02a946759c`.
- The reproduced parity Markdown is byte-identical to Stage 1 at SHA-256 `c67141790d454364a5cc0f31d2a7cc0da196143b80d2e0e265a3784410c704d7`. Parity JSON is semantically identical after excluding only the expected `scope_of_work` location field.
- The candidate retains the historical D-GOV-15 pilot-variance marker and contains no D-GOV-16 marker, exactly as directed by `PILOT-VALIDATION-001`; no marker was inserted.

Verdict: `PASS`.
