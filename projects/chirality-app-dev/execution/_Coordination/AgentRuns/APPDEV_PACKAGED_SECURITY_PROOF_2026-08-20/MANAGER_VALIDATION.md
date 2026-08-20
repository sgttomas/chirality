# Manager validation

- Accepted basis: `357a58b56726feba49507534159c3fbc4656b818`;
  D-APP-97 C1; branch `codex/app-packaged-security-proof-20260820`; intended
  PR base `main`.
- N1 node revision: `605a0b7bc85e054d32221083e1f15a57b2d85dee`,
  published in PR #586. Product-source bytes are unchanged after this commit.
- CI attempt 01: governance run/job `32345362720 / 96352866416` failed only G4
  because the changed workflow had no newly added instruction-tranche
  manifest. See `CI_ATTEMPT_01.md`.
- Remediation 03: the new APP-DEL0906 manifest records D-APP-97 C1 authority
  and grants none; YAML/schema and stock full candidate-range G4 validation
  `PASS`: 108 changed paths from accepted base, exactly two on the instruction
  surface, checked against the one added manifest.
- APP-HOLD reliance: `ALLOW` for DEL-09-06 and DEL-09-04; both contracts
  `CLEAR` / `NOT_HELD`; register SHA-256
  `e7408516cb32ad4414f246b594bdc64a088773d7fd6e1c6629e2184c4ac82f7f`.
- Corrected frozen subject: `PASS`, 88/88 paths; 10 product and 78
  evidence/control; aggregate SHA-256
  `db85316f5f5d711e4aa3b248368c62e5448c01b6716fc2b284075dc0754f8bc4`.
- Review 02: `PASS` on v2, then superseded for final closeout identity only by
  remediation 02's six whitespace-only evidence/fan-in byte corrections.
- Review 03: `PASS` for the committed node candidate before the CI-manifest
  gap was exposed. Final adjacent-remediation review is recorded separately in
  `REVIEWER_RETURN_04.md` / `STATUS_REVIEW_04.json`; only its 100% `PASS` with
  zero actionable findings releases the updated CHANGE handoff.
- Focused proof regressions: `PASS`, 2 files / 11 tests.
- Full registered checks: `PASS`, 150 frontend files / 1158 tests; one
  accepted self-expiring precedence failure and four skips; typecheck, build,
  350 harness tests, and APP-HOLD integrity pass.
- Root self-check, instruction-root integrity (43/43), unsigned
  `desktop:dist`, source network proof, and packaged host proof: `PASS`.
- Packaged artifact identity:
  `3da8cbbbd5cd543dce0c400975cf42b2bdfadd0b8dc6ccd61aab6489c38acee5`.
- Packaged proof: encrypted safeStorage store/status/remove; provider
  isolation; complete Electron descendant capture; renderer blocked signal;
  zero non-allowlisted egress; post-operation artifact/log secret scan; and
  confirmed GUI/daemon/stream/temp-root cleanup all `PASS`.
- Secret scan: `PASS`, 5772 files / zero blocked findings.
- Manager JSON/NDJSON parse and exact declared-write containment: `PASS`.
  Adjacent remediation whitespace, including untracked files, is validated by
  staging all eight contained remediation paths, running
  `git diff --cached --check`, and restoring the clean index: `PASS`; no
  production runtime, lockfile, lifecycle,
  Remaining, memory, Approval-SHA, release, credential, owner-machine,
  shared-log, governance, or foreign-loop write is present.
- Accepted blocker: production Anthropic environment fallback precedence is
  reversed. Repair remains outside this node with DEL-02-05 R03 / DEL-04-05
  RQ-001 under the Agent-0 `RECORD/HOLD scope widening` disposition.
