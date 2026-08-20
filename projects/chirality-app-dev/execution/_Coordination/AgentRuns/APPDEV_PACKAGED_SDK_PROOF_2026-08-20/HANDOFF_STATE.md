# Handoff state — initial proof-loop CHANGE commit

- Accepted upstream snapshot: repository basis `d8c47d9fbc459b32c053c844be0fa789fd1ffab2`; D-APP-97 C1.
- Current closure: `IMPLEMENTED_AND_REVIEWED_PRE_CI / EXTERNAL_PROOF_REQUIRED`.
- Child closure: implementer `SUCCESS`; fresh read-only reviewer `PASS`, 100% frozen coverage, zero actionable findings.
- Derivative package: current and internally validated against the accepted basis; not authoritative decomposition truth.
- DEL-09-04: `IN_PROGRESS`; packaged-SDK/R4-P49 Remaining stays open; lifecycle and Checking Approval SHA unchanged.

## CHANGE handoff

Create the initial node commit from the exact current contained diff. Do not add `projects/chirality-app-dev/loop/LOOP_RECEIPTS.md` or `projects/chirality-app-dev/plans/PLAN_COMPLETION_LOG.md` in this initial commit. Do not merge.

After the commit exists, run with the configured Python environment:

`python3 tools/validation/validate_instruction_tranche_manifest.py --base d8c47d9fbc459b32c053c844be0fa789fd1ffab2 --head HEAD --added-manifests-only`

Then push/open the PR so `.github/workflows/desktop-release-template.yml` job `verify-unsigned-macos` runs on `macos-15`. Required acceptance evidence is:

1. job success for actual unsigned `desktop:dist`, staged app verification, read-only DMG mount verification, and upload;
2. uploaded `chirality-desktop-macos-arm64-unsigned` artifact contains both
   `artifacts/release-verification/packaged-agent-sdk/staged/summary.json` and
   `artifacts/release-verification/packaged-agent-sdk/mounted/summary.json`;
3. each parses with `status: pass` and `proofMode: scripted-no-live-provider`;
4. `bundleRoot` identities distinguish staged and mounted Resources and the mounted proof completed before detach;
5. governance candidate-range G4 passes on the committed PR range.

Only after that proof returns may Agent 0 perform after-the-fact shared fan-in state/receipt/completion-log work and reconsider removal/narrowing of the packaged-SDK Remaining scope. No signing, notarization, distribution/publication, release-readiness, lifecycle, owner-machine deployment, provider/network, credential, dependency/lockfile, or merge authority is created.

Remaining blockers: external PR-CI proof and committed candidate-range G4 only. No owner decision is presently required.
