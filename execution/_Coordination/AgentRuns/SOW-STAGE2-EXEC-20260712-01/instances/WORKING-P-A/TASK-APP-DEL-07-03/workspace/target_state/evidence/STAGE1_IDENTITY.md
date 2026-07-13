# Stage-1 Identity Check

Verdict: `PASS`

- Stage-1 App evidence commit `fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26` exists.
- Its six DEL-07-03 blobs (four sources, `_STATUS.md`, and `ScopeOfWork.md`) reproduce the accepted hashes exactly.
- The candidate hash is `6fa7732954b95314176d81045edeb9492405785cf4568acf210968f903cc9ab0` in the Stage-1 commit, extracted P4 candidate, and seeded target.
- The reproduced claim map is byte-identical to Stage-1 (`84b6eab1115d88a537331a3e2ac5cec9cbbe7e7e2cef5d489c7899049e9da2a5`).
- The reproduced parity report is semantically identical to Stage-1 after removing only the run-local absolute `scope_of_work` path.
- Both reproduced renders are byte-identical to Stage-1 (`81e618d2542d1d3b62528fed92f9b140ea09f092046bb72773d13e84d5604ee6`).
- The repeated current checklist is byte-identical (`4d54f77bd3859cc87d2d8784b65ae494f8a6e116f904ffb58a274d0e1e7ef152`). Its criterion, verification, source identity, and output linkage are identical to Stage-1 after excluding only Stage-1's retired `PILOT_DUAL`/D-GOV-15 variance metadata and the current corrected `SOW_V1` format metadata.
- Candidate frontmatter binds decomposition commit `2770fda4...`; the decomposition blob at that commit is byte-identical to accepted basis `0d260eb...` (`a907cda33835ebf06187331c1c5937a9ae9949923c5465b17519cbd8fcaba6d4`), and `2770fda4...` is an ancestor of `0d260eb...`.
