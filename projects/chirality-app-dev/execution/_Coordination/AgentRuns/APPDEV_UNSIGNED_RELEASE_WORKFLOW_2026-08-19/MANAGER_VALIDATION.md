# Manager validation

- Accepted basis / authority: `57803893d1eb161f395e0574c256dd27920bf1d4`, D-APP-97 C1, APP-HOLD ALLOW with register match.
- Product/build diff: active unsigned Desktop CI workflow, retired disabled predecessor, and focused static regression only.
- Focused policy regression: PASS, 2 files / 9 tests.
- Final full Vitest after remediation/review convergence: PASS, 148 files plus one skipped; 1143 tests pass / four skip.
- Final frontend/Electron typecheck: PASS.
- Workflow static proof: YAML parse PASS; all run blocks Bash syntax PASS; forbidden tag/write/secrets/Windows/release-publication scan PASS.
- Repository gates: practitioner harness 350 PASS; self-check exit 0 at existing baseline; APP-HOLD 53 clear/register match; `git diff --check` PASS.
- Independent review: attempt 01 FAIL drove two evidence remediations; attempt 02 was interrupted on an invalidated hash; final fresh attempt 03 PASS with no actionable findings.
- Product-node containment: only the authorized workflow replacement, one frontend test, DEL-09-05 state/memory/one run record, and this RunID root changed. No dependency/lockfile, lifecycle, Checking Approval SHA, decision/register, release, or unrelated path changed; the shared receipt is updated only now at after-the-fact fan-in.
- PR CI: PASS on PR #583. Product-node run `32327128935`, job `96300526868` proved the actual macOS build, DMG mount/identity/posture checks, and bounded CI artifact upload. The manifest-only attempt-02 head also passed run `32327623672`, job `96301950103`; no new product conclusion is inferred from the records-only change.
- CI attempt 01 governance result: FAIL at G4, run `32327128948`, job `96300527118`, because the two changed workflow instruction-surface paths had no added tranche manifest. Remediation adds `APP-DEL0905-UNSIGNED-CI-20260819.yaml`; G4 corpus, named-diff, and live-validator candidate-range simulation checks PASS for all three covered paths; G4 tests 44 PASS; self-check and whitespace PASS. The then-owed committed candidate-range proof passed in attempt 02 below.
- Review continuity: workflow SHA-256 `8d386efef470aecae418b977c14488b03301dff43229720ee20875fdaef63186` and regression SHA-256 `ab2a45eba5c8560ebab3cfc3dc791511f1aa5d7e28ffbdf609f9a11d551f0a39` are unchanged; review 03 remains valid.
- CI attempt 02: PASS. Governance `harness` run `32327623630`, job `96301949909`; Harness pre-merge run `32327623713`, job `96301950424`; retriggered Desktop run `32327623672`, job `96301950103`. The accepting Agent 0 M6 survey found no cross-loop notice obligation for the App-specific workflow manifest.
