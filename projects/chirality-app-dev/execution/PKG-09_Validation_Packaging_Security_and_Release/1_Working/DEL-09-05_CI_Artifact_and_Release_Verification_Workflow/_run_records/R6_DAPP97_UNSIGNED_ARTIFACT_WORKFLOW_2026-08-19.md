# DEL-09-05 D-APP-97 unsigned-artifact workflow implementation

- Basis: `57803893d1eb161f395e0574c256dd27920bf1d4`, D-APP-97 C1, APP-HOLD ALLOW.
- Product result: active `.github/workflows/desktop-release-template.yml`
  replaces the retired `.disabled` template with a PR/manual, macOS-only,
  read-only-permission unsigned CI-artifact proof and upload path.
- Verification design: `desktop:dist`; staged app/DMG/mounted app identity and
  signing/notarization-posture checks; stable packaged-dependency,
  instruction-root, and release-verification JSON; `upload-artifact` only.
- Deterministic evidence: focused 2 files / 9 tests PASS; final full Vitest 148
  files plus one skipped, 1143 tests pass / four skip; typecheck PASS; YAML and
  every workflow run-block Bash syntax PASS; practitioner harness 350 PASS;
  APP-HOLD and whitespace PASS.
- Independent review: review 01 FAIL identified two evidence gaps; both were
  remediated. Review 02 was interrupted when a literal command-argument typo
  invalidated its hash. Fresh review 03 PASS with no actionable findings over
  active workflow SHA-256
  `8d386efef470aecae418b977c14488b03301dff43229720ee20875fdaef63186`
  and regression SHA-256
  `ab2a45eba5c8560ebab3cfc3dc791511f1aa5d7e28ffbdf609f9a11d551f0a39`.
- PR-CI proof: PR #583 `Desktop Unsigned Artifact Verification / Verify
  unsigned macOS artifact` passed in run `32327128935`, job `96300526868`,
  proving the macOS build, DMG mount/posture verification, and bounded artifact
  upload. The same check passed again after the manifest-only remediation in
  run `32327623672`, job `96301950103`; the product-node run remains the cited
  product proof.
- Governance proof: attempt 01 failed G4 because the workflow rename lacked an
  instruction-tranche manifest. Adjacent remediation commit
  `295f060783ac4c4fac9104a7d72f9d81b1af48d6` added coverage without changing
  product hashes; governance run `32327623630`, job `96301949909` and Harness
  pre-merge run `32327623713`, job `96301950424` passed.
- Boundaries: no dependency/lockfile, product provider/network, lifecycle,
  Checking Approval SHA, signing, notarization, publication, distribution,
  owner-machine deployment, release authority, or professional claim.
