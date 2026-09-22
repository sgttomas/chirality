# Owner check — what did you see happen? (RUN_D128, R3)

For HELP_HUMAN to put to the owner **before any R4 packet is drafted** (RUN_BASIS Addendum 10; owner direction `r2_absence_not_evidence`: "a lack of evidence is not evidence of lack. Check with me first about what I did and didn't see happen").

- Answer each question **yes / no / don't know**. A "don't know" leaves the rows `UNKNOWN`.
- Nothing below says an event did or did not happen. "Evidence found" lists only what the run found inside its evidence roots; a missing record is not taken as a missing event.
- "Rows decided" lists the rows whose Disposition waits on the answer (`UNKNOWN` now); "rows noted" lists rows whose Disposition stands on code or other evidence but whose notes assert the event from absence.
- 20 questions over 63 rows. Built by `R3/_scripts/r3_owner_check.py` from every `OWNER_CHECK:` note in `CLAIM_CONCORDANCE.csv` and `EXTENSION_CONCORDANCE.csv`.

## A. Release act and candidate authorization

**OC-01.** Did you name and authorize the exact v3.0.0 and v3.0.1 candidates before they were signed, notarized and published?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (1): `DEL-09-05#CLM-016.3`
- Evidence found: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md` records your authorization of the 3.0.0 publication and notarization as relayed by the agent. No record for 3.0.1.

## B. Build and signing

**OC-02.** Did you see a v3.0.1 DMG built with `desktop:dist` and Developer ID signed? (If yes: is a build record — transcript, DMG checksum, integrity summary — kept anywhere?)  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (6): `DEL-09-04#CLM-005`, `DEL-09-04#CLM-011.1`, `DEL-09-04#CLM-011.2`, `DEL-09-04#CLM-011.3`, `DEL-09-04#CLM-011.7`, `DEL-09-04#CLM-018`
- Evidence found: 3.0.0-rc.1 and 3.0.0 build records exist (`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md`, `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_RELEASE_20260913.md`). For 3.0.1 the only trace is the version-bump commit `cf4653526` (2026-09-19).

## C. Notarization

**OC-03.** Did you see the v3.0.1 DMG notarized and stapled?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (1): `DOC:BUILDREL#9.3`
- Evidence found: 3.0.0: notarization Accepted, stapled, Gatekeeper "Notarized Developer ID" (`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md`). 3.0.1: no record in the evidence roots. **Statement to confirm (not applied to any row):** you stated "v3.0.1 was notarized, as v3.0.0 was" (OWNER_DIRECTION `r2_absence_not_evidence`, RUN_BASIS Addendum 10).

## D. Publication

**OC-04.** Did you see v3.0.1 published as a release? (If yes: is a record of its release steps kept anywhere?)  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (1): `DEL-09-05#CLM-016.6`
- Evidence found: 3.0.0 was published as latest stable on 2026-09-13 (`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/PUBLIC_RELEASE_20260913.md`). No 3.0.1 publication record in the evidence roots.

## E. CI and release jobs

**OC-05.** Did you see the full K-VALIDATE-1 local check set, including `desktop:dist`, pass before you accepted v3.0.0 and v3.0.1 for release?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (1): `DEL-09-05#CLM-010.8`
- Evidence found: 3.0.0: CI (Root and App) PASS and `desktop:dist` exit 0 before publication (`projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/BUILD_EVIDENCE_RELEASE_20260913.md`). 3.0.1: no record. R3 could not decide whether this row rests on absence (T3 UNDECIDED; Disposition kept).

**OC-06.** Since the Codex-host re-platform, did you run, or see run, a Section 8 harness premerge pass against the Codex-hosted Runtime (repository-root CI or local)?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (4): `DEL-09-01#CLM-009.8`, `DEL-09-01#CLM-011`, `DEL-09-01#CLM-023`, `DEL-09-01#REM-1`
- Evidence found: In-root CI runs only `harness:validate:premerge` (`projects/chirality-app-dev/.github/workflows/harness-premerge.yml:52`), which exercises the legacy harness. No Section 8 run against the Codex-hosted Runtime is recorded in the evidence roots.

**OC-07.** Did you run, or see run, a harness premerge with the full 16-ID Section 9 manifest, with its summary kept?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (1): `DEL-09-02#CLM-020.2`
- Evidence found: The in-root CI uploads only the Section 8 summary. No Section 9 run summary is recorded.

## F. Attestation, SBOM and build matrix

**OC-08.** For v3.0.0 or v3.0.1, did you, or a job you saw, produce a build attestation or publish an SBOM?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (4): `DOC:BUILDREL#11`, `DOC:BUILDREL#12`, `DOC:RQGATES#12`, `DOC:VALSTRAT#7`
- Evidence found: The hosted release job exits 1 at its S0 block step (`.github/workflows/desktop-release-template.yml:39-43`, App project) before `desktop:dist`; local signing, notarization and publication are recorded for 3.0.0. No attestation or SBOM publication record.

**OC-09.** For v3.0.0 or v3.0.1, did you, or a job you saw, produce a build for any target other than macOS arm64?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (4): `DOC:BUILDREL#11`, `DOC:BUILDREL#12`, `DOC:RQGATES#12`, `DOC:VALSTRAT#7`
- Evidence found: arm64 only is configured and stated for 3.0.0 (`BUILD_EVIDENCE_RELEASE_20260913.md:12`). No other-target build record.

## G. Packaged proofs and inspections of the built App

**OC-10.** Did you, or an agent you saw, inspect the binary architecture (arm64, e.g. with `lipo` or `file`) of the built v3.0.0 or v3.0.1 App?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (1): `DEL-09-04#CLM-011.5`
- Rows noted (0): —
- Evidence found: arm64 is configured and stated; no `lipo`/`file` output recorded. The scripted lipo step (`desktop-release-template.yml:171`) sits after a step that exits 1.

**OC-11.** Did you, or an agent you saw, inspect `LSMinimumSystemVersion` (15.0.0 or later) in the built v3.0.0 or v3.0.1 App?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (1): `DEL-09-04#CLM-011.4`
- Rows noted (0): —
- Evidence found: Configuration pins 15.0.0 (`frontend/package.json:158`). No inspection record; the scripted step (`desktop-release-template.yml:177`) sits after a step that exits 1.

**OC-12.** Did you run, or see run, the packaged v3.0.0 or v3.0.1 App with its Runtime service spawning the bundled `codex app-server` while secret and network checks were taken?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (2): `DEL-09-04#CLM-009.8`, `DEL-09-04#CLM-011.8`
- Evidence found: The packaged probe proves only `codex --version` (`frontend/scripts/verify-codex-pin.mjs:99-178`). `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_USER_JOURNEYS_20260912/JOURNEY_RESULTS.md:3` records actual Codex sessions on "the installed signed App" (build not named); no secret or network check recorded with it.

**OC-13.** Did you run, or see run, a packaged network or security proof on a Codex-hosted build (v3.0.0 or v3.0.1)?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (6): `DEL-09-04#CLM-012.1`, `DEL-09-04#CLM-017`, `DEL-09-06#CLM-016`, `DEL-09-06#CLM-021`, `DOC:RELIANCE#8`, `DOC:VALSTRAT#4.11`
- Evidence found: The proof scripts target `api.anthropic.com` (legacy-provider shaped; code finding stands). No run on a Codex-hosted build is recorded.

**OC-14.** Did you run the packaged checks S-6 (quit and relaunch continuation), S-8 (Chirality-scoped sign-in and sign-out) and the renderer-disconnect check on the stapled v3.0.0 or v3.0.1 App?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (1): `DOC:BUILDREL#9.5`
- Rows noted (2): `DOC:RELIANCE#11.1`, `DOC:VALSTRAT#8`
- Evidence found: `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/BUILD_EVIDENCE_20260912.md:53-62` leaves packaged S-6/S-8 to your native verification; no outcome recorded.

**OC-15.** Did you see the DEL-09-04 V3-01 Return (offline network-denied package evidence, nested signature inventory) produced for the landed Codex-hosted package?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (1): `DEL-09-04#REM-1`
- Evidence found: A2 packaging code is live and 3.0.0 was published; no V3-01 Return is recorded.

**OC-16.** Did you, or an agent you saw, run the manual DMG checklist (arm64, minimum OS, signing posture, instruction root, working-root selector, network safeguards) on the v3.0.0 or v3.0.1 package?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (1): `DEL-09-05#CLM-010.6`
- Evidence found: Amended SPEC §19.4 / PRD §12.8 define the checklist; no outcome of a packaged checklist run is recorded.

## H. Manual reviews, checklists and records

**OC-17.** Did you, or an agent you saw, run a secret-redaction and network-scope inspection over the v3 CI logs, the v3 build records or the packaged App?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (0): —
- Rows noted (2): `DEL-09-05#CLM-010.9`, `DEL-09-05#CLM-010.15`
- Evidence found: The scanner patterns cover no Codex/OAuth material (`frontend/scripts/scan-secret-evidence.mjs:50-51`; code finding stands). No such inspection is recorded for v3.

**OC-18.** For the v3.0.0 or v3.0.1 release, did you make, or see made, a requirement-to-evidence matrix, the ten-step CI review, or a manual-checklist status record anywhere outside the DEL-09-05 folder?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (4): `DEL-09-05#CLM-010.13`, `DEL-09-05#CLM-010.14`, `DEL-09-05#CLM-016.5`, `DEL-09-05#CLM-023.1`
- Rows noted (2): `DEL-09-05#CLM-021`, `DEL-09-05#CLM-022`
- Evidence found: The DEL-09-05 folder holds only the pre-v3 INSP-03 matrix.

**OC-19.** Did you carry out, or see carried out, a boundary-copy release review (BOUNDARY_REVIEW_CHECKLISTS step 8) for the shipped v3.0.0 or v3.0.1 App?  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (1): `DEL-01-03#CLM-017`
- Rows noted (1): `DEL-01-03#CLM-011`
- Evidence found: No completed Review Evidence Template in the App docs or execution tree.

**OC-20.** For the July 2026 ScopeOfWork conversion (D-GOV-16 Stage 2), did you see the VER-001 checks (validator, claim map, parity report, review checklist) and a human or verifier review done for the deliverables listed? (A per-deliverable answer is fine.)  
Answer: ☐ yes ☐ no ☐ don't know

- Rows decided (16): `DEL-00-01#CLM-018.2`, `DEL-00-02#CLM-021.2`, `DEL-01-01#CLM-018`, `DEL-01-02#CLM-038.4`, `DEL-01-03#CLM-022`, `DEL-01-04#CLM-020.2`, `DEL-02-01#CLM-023.2`, `DEL-02-02#CLM-021.2`, `DEL-02-03#CLM-023.2`, `DEL-02-04#CLM-021.2`, `DEL-02-05#CLM-020.1`, `DEL-05-03#CLM-020.1`, `DEL-05-04#CLM-019.2`, `DEL-10-01#CLM-022.2`, `DEL-10-04#CLM-023.2`, `DEL-10-05#CLM-020.1`
- Rows noted (3): `DEL-03-02#CLM-018`, `DEL-05-05#CLM-020.2`, `DEL-10-02#CLM-019.2`
- Evidence found: The conversion wave run is in Root `execution/`, outside the evidence roots; App AgentRuns hold only the frontend activation. Some rows carry positive partial records (validator PASS 2026-07-19; parity markers in git history), noted on the row. R3 recomputed AC-001 line parity for DEL-00-02 and DEL-05-03 (both kept).

## Recording the answers

The owner's answers are recorded verbatim as owner direction; the affected rows are then dispositioned from them (RUN_BASIS Addendum 10). An answer the owner cannot give stays `UNKNOWN`.
