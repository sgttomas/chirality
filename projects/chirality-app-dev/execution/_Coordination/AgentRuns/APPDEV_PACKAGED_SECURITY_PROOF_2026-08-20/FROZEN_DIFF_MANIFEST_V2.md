# Corrected frozen diff and evidence manifest v2

- FrozenAt: `2026-08-20T07:07:59Z`
- AcceptedBasis: `357a58b56726feba49507534159c3fbc4656b818`
- Supersedes: `FROZEN_DIFF_MANIFEST.md` for final candidate review; v1 and R1 remain immutable attempt history.
- SubjectPathCount: `88`
- ProductSourcePathCount: `10`
- EvidenceControlPathCount: `78`
- CandidateIdentitySHA256: `db85316f5f5d711e4aa3b248368c62e5448c01b6716fc2b284075dc0754f8bc4`
- IdentityMethod: SHA-256 of the bytewise path-sorted 88 lines emitted as `<file-sha256><two spaces><repo-relative-path><newline>` by `git ls-files --modified --others --exclude-standard -z | sort -z | xargs -0 shasum -a 256` before this v2 manifest and reviewer-02 controls were created.
- Reconstruction: compute the same inventory over current changed/untracked files while excluding exactly `FROZEN_DIFF_MANIFEST_V2.md`, `LAUNCH_BRIEF_REVIEWER_02.md`, `STATUS_REVIEW_02.json`, and any later reviewer-02/manager fan-in records. The result must contain 88 lines and hash to the candidate identity above.
- RemediationDelta: the v1 product subject changed only in both proof scripts and `run-packaged-security-proof.test.ts`, with new `run-network-policy-proof.test.ts`; all other product paths are byte-preserved. New remediation evidence/records close R1's five findings without rewriting prior evidence.

## Complete product-source subject

1. `.github/workflows/desktop-release-template.yml`
2. `projects/chirality-app-dev/frontend/package.json`
3. `projects/chirality-app-dev/frontend/scripts/run-network-policy-proof.mjs`
4. `projects/chirality-app-dev/frontend/scripts/run-packaged-security-proof.mjs`
5. `projects/chirality-app-dev/frontend/src/__tests__/contract-pins.manifest.ts`
6. `projects/chirality-app-dev/frontend/src/__tests__/electron/api-key-storage.test.ts`
7. `projects/chirality-app-dev/frontend/src/__tests__/lib/harness-attachment-resolver.test.ts`
8. `projects/chirality-app-dev/frontend/src/__tests__/scripts/desktop-release-workflow.test.ts`
9. `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-network-policy-proof.test.ts`
10. `projects/chirality-app-dev/frontend/src/__tests__/scripts/run-packaged-security-proof.test.ts`

The accepted API-key environment-precedence defect remains outside scope and
keeps packaged-security acceptance failed. This v2 freeze asks whether the
candidate proof implementation and its partial-progress landing posture are
valid, not whether the deliverables may close.
