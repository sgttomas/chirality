# Stage-1 Identity

Verdict: `PASS`.

- Current basis is exact `main@0d260eb024d8b8dada0df477b70ac880a6906ffa`.
- Accepted Stage-1 commit `31c35ea9798c29cd0af16b7089186f3942dcfcb1` exists and binds the DEL-13-02 candidate.
- `workspace/ScopeOfWork.md`, the P4 extracted candidate, and the Stage-1 commit blob are byte-identical at SHA-256 `43d9ea2fa0e4fa95c4906fb8f7abffabe7c23a92d7bbc6ea4a4c9f430293c6d8`.
- All eight files in `stage1_evidence/` are byte-identical to the corresponding Stage-1 commit evidence blobs.
- The P4 manifest row binds the same source/status hashes, candidate hash, lifecycle `IN_PROGRESS`, Stage-1 commit, and current basis.
- The candidate retains the historical D-GOV-15 pilot-variance marker and contains no D-GOV-16 marker, exactly as required by `PILOT-VALIDATION-001`; no marker was inserted.

This proves identity only. It does not elevate the Stage-1 derivative to accepted deliverable truth or migration authority.
