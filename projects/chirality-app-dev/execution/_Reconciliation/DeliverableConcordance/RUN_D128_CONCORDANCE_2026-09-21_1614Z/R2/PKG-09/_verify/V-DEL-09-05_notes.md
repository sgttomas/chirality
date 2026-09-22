# V-DEL-09-05 — verifier notes (DEL-09-05, merged P1+P2 ledger)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (LOW / self-flag / AUTHORITY_CONFLICT / REMAINING_WORK) | 7 | 5 | 1 (REM-2 HumanDecisionNeeded) | 1 (CLM-026 Disposition) |
| a30 (sample of other non-ALIGNED) | 15 | 13 | 1 (CLM-010.15 Notes) | 1 (CLM-010.13 CauseTag) |
| b (ALIGNED sample) | 3 | 3 | 0 | 0 |
| c (reverse) | 6 | 5 | 0 | 1 (CAP-BUILD-023 → CLM-007) |
| e (errata) | 3 | 3 | 0 | 0 |
| **Total** | **34** | **29** | **2** | **4** |

No verdict-field REFUTED results (Disposition or reverse Response). Both refutations are field-only (HumanDecisionNeeded, Notes). One CONTESTED item is on a Disposition (CLM-026), and one is on a reverse ClaimKey (CAP-BUILD-023).

## (ii) Patterns and the cross-part differences

**1. Unsigned/unnotarized release target (K-RELEASE-1): P1 CLM-010.7 and STATE-1 (STALE_SPECIFICATION, LOW) against P2 CLM-026 (AUTHORITY_CONFLICT, R4).**

The rulebook supports P1's reading.
- App CONTRACT.md:17 was added by the governed D-GOV-43 tranche `23b3879b3` (blame checked). It names K-RELEASE-1 explicitly ("read with D-GOV-43 items 1 and 4") and lists bundle signing and notarization.
- SPEC §19.4 (SPEC.md:1203, same commit) and PRD §12.8 name the signed and notarized consolidated candidate.
- D-APP-127 names DEL-09-05 as revised.
- Under MR-11, a ruling that explicitly addresses the clause means the stale SoW wording takes STALE_SPECIFICATION. The K-RELEASE-1 row text itself says "unless amended".
- DIRECTIVE §0 does not need to rank the preamble against the row. Both are CONTRACT text, and the preamble is the amendment.

The residual argument for AUTHORITY_CONFLICT:
- The K-RELEASE-1 row (CONTRACT.md:138, blame 2026-05-20) is unamended.
- D-APP-97 F-APP-2 still says "artifacts are unsigned". D-APP-127 names neither.

Because of that residue, CLM-026 is graded CONTESTED, not REFUTED. CLM-010.7 and STATE-1 are CONFIRMED: they chose the reading the rulebook supports and recorded the alternative in LEAST-CONFIDENT. CLM-003 depends on the same reading.

**2. Retired G6a gate: P1 CLM-016.3 (AUTHORITY_CONFLICT, R4) against P2 REGISTER-52 (STALE_SPECIFICATION, MOOT:D-APP-127).**

The rulebook supports P1's reading (grading key 4).
- The GOVERNING decomposition row (v3_2:382) still requires G6a and keeps D-APP-97/F-APP-2 active.
- The D-APP-127 record never mentions G6a. It retires "the Stage 9 to 13 packaging spine" and names DEL-09-05 as revised.
- The G6a retirement appears only in the deliverable's own `_STATUS.md:21` carrier text. That is declared state, not authority.
- A ruling that undercuts an unamended GOVERNING clause without naming it gives AUTHORITY_CONFLICT. DIRECTIVE §0 does not resolve it: CONTRACT:17 says only that publication remains separately human-authorized.

CLM-016.3 is CONFIRMED, with plain R4 correct: no named R4-Qn covers G6a. REGISTER-52 is outside this selection. Its MOOT/STALE_SPECIFICATION reading relies on carrier text and should be reviewed against CLM-016.3 at R3.

**3. Q-02 routed into HumanDecisionNeeded (REM-2).**
- REM-2 is a REMAINING_STATE_MISMATCH row. Its only stated basis for `R4` is "Q-02 (release act and F-APP-2 lift)".
- Ruling B and grading key 4b make Q-01..Q-13 CONTEXT only, never HumanDecisionNeeded tokens. The value should be NO, with Q-02 kept in Notes.
- CLM-016.3 and CLM-026 also mention Q-02, but there R4 comes from AUTHORITY_CONFLICT, so it is correct.

**4. Search glosses and cause for the v3 evidence gaps.**
- CLM-010.15's Notes say PACKAGING_PROCEDURE "list[s] no secret or network inspection". In fact PACKAGING_PROCEDURE.md:62-72 lists `proof:network-policy` and `proof:secret-scan` as conditional post-build repeats. The procedure requires rather than waives them, so NONE_FOUND and the Disposition hold. The Notes are REFUTED on the gloss.
- CLM-010.13 tags A2_TOPOLOGY for a gap that INSP-03 already recorded on 2026-06-21 (REQ013 PARTIAL). PRE_V3_DRIFT is the grading-key-8 default, and A2_TOPOLOGY names a different mechanism. Graded CONTESTED.

**5. Other observations (no verdict change).**
- **REACH for manual npm proof scripts.** `scan-secret-evidence.mjs`, `run-network-policy-proof.mjs`, `generate-sbom.mjs` and `verify-version-identity.mjs` are tagged `LIVE (manual)`. Under grading key 4b they are not in a release or packaging default path. No Disposition or R4-Q1 depends on these tags. Accepted as the worker's recorded reading; R3 should settle one label.
- **Relative paths.** Paths such as `execution/_Decomposition/…` and `_STATUS.md:21` are App-relative, not repo-relative.
- **DirectionEvidence for the REF-006 MATCH note.** For the same note, P1 gives `NONE_FOUND` (CLM-001, CLM-008) and P2 gives `GOV:D-APP-38` (REGISTER-56). D-APP-38 does not explain the drift, so NONE_FOUND is the better value.
- **Errata.** All three errata are exact: the SealedValue matches the ledger byte for byte. The SEE target REGISTER-51 exists with the same Disposition.
- **Line anchors.** Every line anchor checked in package.json, pack-electron.mjs, the verify-* and validate-* scripts, electron/main.ts, the in-root harness-premerge.yml, CONTRACT, SPEC and PRD shows the cited content. There is no drift beyond 1 line.
- **PostReleaseBasis.** NO holds: no cited file appears in TOUCHED_PATHS.csv.

## (iii) Effort

- **Files read:** about 30 files or excerpts from the frozen tree, plus the run inputs (brief, CONVENTIONS, RUN_BASIS, ledger, errata, reverse, reverse notes, evidence pack, BUILD capabilities).
- **Git:** read-only git on the frozen tree only (log, show, blame -L).
- **Context budget:** moderate, not tight.
- **Out-of-root evidence:** none was relied on. The repo-root `.github/workflows/harness-premerge.yml` would decide only the artifact-name element of CLM-015 and CLM-023.3, and those rows state that.
