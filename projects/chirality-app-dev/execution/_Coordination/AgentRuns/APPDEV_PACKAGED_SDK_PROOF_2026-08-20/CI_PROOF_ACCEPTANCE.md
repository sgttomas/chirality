# Post-CI proof acceptance

- PR: `#585`
- Exact source revision:
  `3a02eeedeb3561748d96b10f57a1aa7f5546eeb5`
- Desktop Unsigned Artifact Verification: run `32332985341`, job
  `96317050414`, `PASS`
- Harness: run `32332985346`, job `96317050162`, `PASS`
- Governance: run `32332985350`, job `96317050220`, `PASS`, including
  committed candidate-range G4

## Inspected unsigned artifact evidence

The uploaded evidence was downloaded to temporary derivative path
`/tmp/chirality-del0904-proof.6V7NQg` for local inspection. That directory is
not committed and is not authority. The CI run/job and uploaded artifact are
the external proof surface.

- Aggregate summary: `status: pass`, `scope: ci-artifact-only`.
- DMG SHA-256:
  `a6e9e43ae5f92d45967bc1871f918bc18f6be0088d9cab3166398e7e1f1ca916`.
- Staged and mounted executable SHA-256:
  `79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874`;
  `mountedIdentityMatches: true`.
- Staged packaged-SDK summary: `status: pass`,
  `proofMode: scripted-no-live-provider`, bundle root
  `/Users/runner/work/chirality/chirality/projects/chirality-app-dev/frontend/dist/mac-arm64/Chirality.app/Contents/Resources`.
- Mounted packaged-SDK summary: `status: pass`,
  `proofMode: scripted-no-live-provider`, bundle root
  `/Users/runner/work/_temp/chirality-dmg.E27rKg/Chirality.app/Contents/Resources`.
  The workflow mounts this app read-only under `RUNNER_TEMP`; a `/Volumes`
  mount is neither required nor expected.
- The two summaries are separately retained under
  `artifacts/release-verification/packaged-agent-sdk/{staged,mounted}/summary.json`.
- Signing posture is unsigned/ad-hoc with no authority. No valid stapled
  notarization ticket exists.

## Acceptance boundary

This evidence closes the exact selected D-APP-97 packaged-SDK/DMG and
release-quality premerge engineering gap. It does not prove live-provider or
outbound-network behavior, login-time `RunAtLoad`, owner-machine LaunchAgent
deployment, signing, notarization, distribution, publication, release
readiness, or lifecycle advancement. DEL-09-04 remains `IN_PROGRESS`; its
Checking Approval SHA remains
`8c6d55d3e8b07d8d3c8d98c510cf6672766d7bec`.
