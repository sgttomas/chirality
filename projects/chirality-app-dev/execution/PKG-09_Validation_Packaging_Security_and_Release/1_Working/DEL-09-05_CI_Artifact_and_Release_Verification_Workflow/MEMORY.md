# MEMORY - DEL-09-05

## Decisions And Evidence

- 2026-09-03 - Node B (WP-09 preparation) landed the reviewed release runbook
  candidate and exact-candidate identity/custody checklist (V3-01, both
  `CANDIDATE — NOT ADOPTED`), the pinned-Syft SBOM and third-party notices
  tooling with tests and a notices evidence bundle (V3-02; SBOM
  `UNAVAILABLE_UNDER_BOUNDS` until an owner host act installs Syft `v1.18.1`),
  and the version-identity check with the staged, unapplied `3.0.0-rc.1` patch
  (V3-03). Three independent review rounds; round 3 PASS. Findings carried for
  later items: no UI/about or runtime surface prints the product version
  (AT-043), no script writes a release-manifest version field, 28 installed
  packages ship no license file, `build.mac` declares no explicit
  `identity: null`/entitlements/fuses/notarize keys (AT-038 config gap, G5
  input). No signing, notarization, Apple call, distribution, product version
  change, workflow change, lifecycle, or release-readiness claim.

- 2026-08-19 - PR #583 retained the external proof for D-APP-97 C1: Desktop
  run `32327128935`, job `96300526868` passed the unsigned macOS build,
  DMG-mounted identity/posture checks, and bounded CI artifact upload. The
  first governance attempt exposed missing instruction-tranche coverage; the
  adjacent manifest-only remediation passed governance run `32327623630`, job
  `96301949909`, without changing the reviewed workflow or regression hashes.
  DEL-09-05's applicable R4-P49 unsigned-artifact evidence scope is complete.
  No signing, notarization, publication, distribution, release authority,
  lifecycle transition, or professional claim follows.

- 2026-08-19 - D-APP-97 C1 product implementation replaced the inactive
  `.github/workflows/desktop-release-template.yml.disabled` with active
  `.github/workflows/desktop-release-template.yml`. The workflow is bounded to
  PR/manual macOS CI, uses `contents: read`, disables signing identity
  discovery, performs no signing/notarization/publication act, verifies the
  staged app, DMG, and mounted app identity/posture, preserves dependency and
  instruction-root JSON evidence, and uses `actions/upload-artifact` only.
  Focused policy tests, full Vitest, typecheck, YAML/Bash static validation,
  APP-HOLD, practitioner harness, and fresh review passed. Actual macOS
  artifact execution/upload remains PR-CI-owed; no release or lifecycle claim
  follows from the implementation evidence.

- 2026-06-16 - Human project authority advanced this deliverable lifecycle from SEMANTIC_READY to IN_PROGRESS because active code implementation is underway. This does not imply CHECKING, ISSUED, release readiness, dependency satisfaction, professional approval, certification, sealing, authentication, or code-compliance acceptance.
- 2026-06-21 - ADQ-14 added `docs/RELEASE_QUALITY_RUNBOOK.md` and a runtime-premerge wrapper summary at `frontend/artifacts/harness/release-quality/latest/summary.json` (generated, git-ignored). The DEL-09-05 local kit now distinguishes Section 8 premerge summary, Section 9 summary, release-quality wrapper summary, and instruction-root packaging summary. No CI provider/ruling, packaging output, signing/notarization/publication, lifecycle issuance, professional approval, certification, sealing, authentication, code-compliance acceptance, or release-readiness claim changed.
- 2026-06-21 - ADQ-15 produced fresh local packaging evidence: `npm run desktop:dist`, instruction-root integrity summaries for build-directory and mounted-DMG app resources, and scripted no-live packaged Agent SDK subprocess proofs for both layouts. The run records app/DMG artifacts, checksums, arm64/minimum-OS posture, and adhoc local-builder signing posture in `Evidence_ADQ-15_Packaging_Instruction_Root_Refresh.md`. Network-policy evidence remains assigned to ADQ-16; no CI provider/ruling, signing/notarization/publication, external distribution, lifecycle issuance, professional approval, certification, sealing, authentication, code-compliance acceptance, or release-readiness claim changed.
- 2026-06-21 - ADQ-16 added a repeatable secret-scan command and produced current secret/network evidence in `Evidence_ADQ-16_Secret_Network_Proof.md`. The final secret scan passed with 0 blocked findings across tracked app-dev files and generated harness artifacts; the scripted `agentSdk` network proof passed with 0 non-allowlisted endpoints. No CI provider/ruling, signing/notarization/publication, external distribution, lifecycle issuance, professional approval, certification, sealing, authentication, code-compliance acceptance, provider/network expansion, or release-readiness claim changed.
- 2026-07-12 - D-APP-56 R5 P40 executed UPD-075, UPD-078: REF-006 current-state kit/register wording now agrees with D-APP-38 MATCH; dated source-warning and assessment history is preserved. No lifecycle transition.

- 2026-07-12 - D-APP-56 R5 P45 executed UPD-146, UPD-147: current kit/register metadata now reflects live ruled state; dated history and genuine TBD/gates remain preserved. No lifecycle transition occurred.
- 2026-07-12 - D-APP-56 consolidated decision-application tranche recorded the applicable ruled ownership, mapping, gate-reaffirmation, or dated-deferral result for DEL-09-05; proposal-only source rows were not treated as human rulings, no unruled work was executed, and no lifecycle transition occurred.
- 2026-07-12 - D-APP-56 R4-P05 Option C executed under the owner's one-file root exception: the desktop-release template text is retained at `.github/workflows/desktop-release-template.yml.disabled`, outside active GitHub workflow discovery. No release, publication, signing, lifecycle, or product-runtime authority changed.
