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
- Owed proof: the PR-CI check `Desktop Unsigned Artifact Verification / Verify
  unsigned macOS artifact` must execute the macOS build, DMG mount/posture
  verification, and bounded artifact upload. No local or release pass is
  inferred.
- Boundaries: no dependency/lockfile, product provider/network, lifecycle,
  Checking Approval SHA, signing, notarization, publication, distribution,
  owner-machine deployment, release authority, commit, or receipt act.
