# Final closeout frozen candidate manifest v3

- AcceptedBasis: `357a58b56726feba49507534159c3fbc4656b818`
- Supersedes: v2 only for final closeout identity; v1/v2 remain immutable review
  history.
- SubjectPathCount: `99`
- ProductSourcePathCount: `10`
- EvidenceControlPathCount: `89`
- CandidateIdentitySHA256:
  `9053d8e5ab8ecb74ca32b624aa34868fab4ad0df332dfdec863e7c082428b1fb`
- IdentityMethod: SHA-256 of the bytewise path-sorted 99 lines emitted as
  `<file-sha256><two spaces><repo-relative-path><newline>` by
  `git ls-files --modified --others --exclude-standard -z | sort -z | xargs -0 shasum -a 256`
  before this manifest and reviewer-03 controls were created.
- Reconstruction: run the same inventory while excluding exactly
  `FROZEN_DIFF_MANIFEST_V3.md`, `LAUNCH_BRIEF_REVIEWER_03.md`,
  `STATUS_REVIEW_03.json`, and later reviewer-03 return/status-only fan-in.
- CloseoutDelta: compared with v2, no product byte changed. Remediation 02
  removes exactly six whitespace defects across three evidence and three
  manager fan-in files, adds its brief/status/return, and calibrates manager
  records to the final candidate-wide staged whitespace check.
- CandidateWhitespace: all 99 paths were staged, `git diff --cached --check`
  returned `PASS`, and the repository index was restored clean before freeze.
- ParseAndContainment: JSON/NDJSON parse sweep and exact declared-write
  containment both `PASS` before freeze.

## Product-source subject

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

The accepted production API-key precedence defect remains outside scope. This
freeze asks whether every final candidate byte and the partial-progress CHANGE
handoff are valid, not whether DEL-09-06 or DEL-09-04 may close.
