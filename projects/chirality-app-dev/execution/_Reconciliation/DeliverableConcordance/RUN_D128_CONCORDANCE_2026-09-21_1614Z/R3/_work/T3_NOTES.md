# T3 notes: Addendum 10 candidate confirmation

Input `R3/_work/CAND_ADD10.csv` (112 rows). Output `R3/_work/T3_ADD10_VERDICTS.csv`, written by
`R3/_work/T3_scripts/t3_verdicts.py`. The script checks that each candidate is covered once and that
REMAP_UNKNOWN, NOTE_ONLY and UNDECIDED rows carry an OwnerCheck and NO_CHANGE rows do not.

## Counts

- REMAP_UNKNOWN 12: MANUAL_STEPS 9, PACKAGED_PROOFS 3.
- NOTE_ONLY 36: PACKAGED_PROOFS 11, MANUAL_STEPS 7, RELEASE_ACT 7, CI_AND_RELEASE_JOBS 5,
  ATTESTATION 4, PUBLICATION 1, NOTARIZATION 1.
- UNDECIDED 1: CI_AND_RELEASE_JOBS. NO_CHANGE 63: OTHER 52, PACKAGED_PROOFS 5, SIGNING 3, RELEASE_ACT 1, PUBLICATION 1, CI_AND_RELEASE_JOBS 1.

NO_CHANGE rows are mostly code-presence findings or text defects, or rest on positive evidence that a
proof cannot pass (packaged SDK/Pi proofs under the A2 boundary). `DOC:BUILDREL#9.5` was sealed
UNKNOWN; it is counted REMAP_UNKNOWN only to add its OWNER_CHECK.

## Distinct OwnerCheck questions (row count); exact shared strings are in the CSV

1 SoW VER-001 checks and human review for the migrated ScopeOfWork (5) · 2 boundary-copy release
review, checklist step 8 (2) · 3 Section 8 premerge pass on the Codex-hosted Runtime since the
re-platform (4) · 4 premerge with the full 16-ID Section 9 manifest (1) · 5 v3.0.1 DMG built and
signed, with a build record (6) · 6 packaged App spawning codex app-server with secret/network checks
(2) · 7 LSMinimumSystemVersion inspected (1) · 8 arm64 architecture inspected (1) · 9 packaged
network or security proof on a Codex-hosted build (6) · 10 DEL-09-04 V3-01 Return produced (1) ·
11 manual DMG checklist run (1) · 12 full K-VALIDATE-1 set incl. desktop:dist passed before release
acceptance (1, UNDECIDED row) · 13 secret/network inspection of v3 CI logs, build records or packaged
App (2) · 14 requirement-to-evidence matrix, ten-step CI review or checklist status made anywhere (6)
· 15 exact v3.0.0/v3.0.1 candidates named and authorized before signing, notarization, publication
(1) · 16 v3.0.1 released, with a record kept (1) · 17 v3.0.1 notarized and stapled (1) · 18 packaged
S-6, S-8 and disconnect checks on the stapled App (3) · 19 attestation, SBOM publication or a
non-arm64 build for v3.0.0/v3.0.1 (4).

## Positive evidence bearing on several rows

- v3.0.0 was Developer ID signed, notarized (submission Accepted), stapled, passed Gatekeeper as
  "Notarized Developer ID", and was published as latest stable on 2026-09-13
  (`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md`).
  The same record relays the owner's authorization to publish and direction to notarize.
- The desktop:dist stage and exit tables, signature checks, Codex pin and integrity verdicts for
  3.0.0-rc.1 and 3.0.0 are in `.../APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md`
  and `.../APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_RELEASE_20260913.md`. Raw logs are kept
  outside the repository.
- `.../APP_V3_USER_JOURNEYS_20260912/JOURNEY_RESULTS.md:3`: J01 ran actual Codex sessions on the
  "installed signed App" (build not named); bears on question 6.
- `.github/workflows/desktop-release-template.yml:39-43` exits 1 before its lipo (:171) and
  LSMinimumSystemVersion (:177) steps; a manual inspection is still possible.
- v3.0.1: no build, signing, notarization or publication record in `projects/chirality-app-dev`;
  only commit `cf4653526` (2026-09-19, version bump).

## Owner-reported fact to confirm (not applied)

The owner stated that "v3.0.1 was notarized, as v3.0.0 was" (direction `r2_absence_not_evidence`,
RUN_BASIS Addendum 10, CONTEXT). It changes no row. Question 17 asks the owner to confirm it.

## Undecided

`DEL-09-05#CLM-010.8` has two readings. A (REMAP_UNKNOWN): the claim is about local checks; the
3.0.0 records show CI and desktop:dist passing before publication, and 3.0.1 has no record.
B (NO_CHANGE): the Disposition stands on code, because no in-root or pinned gate runs desktop:dist.
