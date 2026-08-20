# CI-remediated complete candidate manifest v4

- AcceptedBasis: `357a58b56726feba49507534159c3fbc4656b818`
- NodeRevision: `605a0b7bc85e054d32221083e1f15a57b2d85dee`
- PullRequest: `#586`
- SubjectPathCount: `108`
- ProductSourcePathCount: `10`
- EvidenceControlPathCount: `98`
- CandidateIdentitySHA256:
  `b7982f121238d743867e8cb9bea0c2e2c6a5ca6220aca6179d73e234d3a08e72`
- IdentityMethod: take the sorted union of paths changed in
  `357a58b56726feba49507534159c3fbc4656b818..HEAD` and current modified/untracked
  paths, emit `<file-sha256><two spaces><repo-relative-path><newline>` for each
  current byte sequence, then SHA-256 the 108-line stream.
- Reconstruction: apply the same method while excluding exactly
  `FROZEN_DIFF_MANIFEST_V4.md`, `LAUNCH_BRIEF_REVIEWER_04.md`,
  `STATUS_REVIEW_04.json`, and later reviewer-04 output/status-only fan-in.
- RemediationDelta: compared with committed node revision, no product byte
  changed. Exactly one root tranche manifest was added; CI attempt/remediation
  records and manager validation/handoff/status were added or calibrated.
- G4: stock validator `PASS` over accepted base through the staged candidate
  tree: 108 changed paths, exactly two instruction-surface paths, checked
  against the one added APP-DEL0906 manifest. Live 36-manifest schema `PASS`.
- Whitespace/parse/containment: eight adjacent remediation paths staged and
  `git diff --cached --check` passed; JSON/NDJSON parse and exact containment
  passed; index restored clean.

## Product-source subject

The ten product paths are unchanged byte-for-byte from node commit
`605a0b7bc85e054d32221083e1f15a57b2d85dee`: the desktop workflow,
`frontend/package.json`, both proof scripts, and the six registered test/contract
files listed in v3. Remediation 03 changes governance/evidence/control bytes
only.

The accepted production API-key precedence defect remains outside scope and
keeps both selected packaged-security residuals open.
