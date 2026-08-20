# Manager direct implementation record

- Implemented the active unsigned macOS CI-artifact workflow at `.github/workflows/desktop-release-template.yml` and retired the `.disabled` predecessor.
- Added the focused static regression at `projects/chirality-app-dev/frontend/src/__tests__/scripts/desktop-release-workflow.test.ts`.
- Review-01 hashes (superseded by remediation): active workflow `9caf6cc503e6c90c6efcf2244017c6de4d135c6017604505816c67b588feae12`; test `46250c73585cc0c8bf55a225845f586861bd0deb09d3e59cd4aad44309353173`.
- Frozen review-02 hashes: active workflow `b846cf1d580710e8660763386ad356d7dc3253b07c794cead494b7225f36a271`; test `8e131c286112662fca271c9e3a9ace2d2bbe74fe181e8ab399430724539bbda1`; retired predecessor at accepted basis `c3b41f8559f870af47110c4431e1bfd44da8109c156f179e4da69dddbe778255`.
- Review-02 was invalidated before return by the confirmed literal `+` dependency-command defect. Frozen review-03 hashes after repair: active workflow `8d386efef470aecae418b977c14488b03301dff43229720ee20875fdaef63186`; test `ab2a45eba5c8560ebab3cfc3dc791511f1aa5d7e28ffbdf609f9a11d551f0a39`.
- Focused policy tests: PASS, 2 files / 9 tests.
- YAML parser: PASS.
- Full frontend Vitest: initial sandbox run failed only because loopback/Unix socket binds returned `EPERM`; exact escalated rerun PASS, 148 files plus one skipped, 1143 tests pass / four skip.
- Frontend typecheck: PASS.
- Practitioner harness: PASS, 350 tests.
- Repository self-check: exit 0 at existing REVIEW/WARN baseline.
- APP-HOLD integrity: PASS, 53 clear, register match; fingerprint `3e0e6d795e53efe6bfc1bb738a5d9159f6bd64f442600bfff90a39c583382a45`.
- Whitespace/static forbidden-release-path scan: PASS.
- Review-01 remediation focused tests, YAML parse, workflow run-block Bash syntax, and whitespace: PASS.
- PR CI owed: actual `Desktop Unsigned Artifact Verification / Verify unsigned macOS artifact` macOS build, posture verification, and artifact upload. No local artifact pass is inferred.
