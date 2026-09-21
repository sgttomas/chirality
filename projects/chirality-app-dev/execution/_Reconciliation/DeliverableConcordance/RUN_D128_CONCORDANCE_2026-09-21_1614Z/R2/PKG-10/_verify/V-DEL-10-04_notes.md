# V-DEL-10-04 verifier notes (DEL-10-04)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 6 | 3 | 1 | 2 |
| a30 | 14 | 11 | 1 | 2 |
| b | 2 | 1 | 0 | 1 |
| c | 2 | 2 | 0 | 0 |
| e | 1 | 1 | 0 | 0 |
| **Total** | **25** | **18** | **2** | **5** |

- No item is REFUTED on a verdict field (Disposition or Response). Addendum 3 verdict-field refutation rate: 0/24 distinct rows.
- Both REFUTED items are on `AuthorityTier` only (CLM-010.4, CLM-030). They go to CORRECTIONS.csv.
- The five CONTESTED items are all on `Disposition`: CLM-004.6, CLM-016.1, CLM-004.1, CLM-006 and CLM-004.4. In the first two, the worker had already self-flagged the other reading as LEAST-CONFIDENT.
- Erratum (CLM-016.1, ImplementationEvidence) is CONFIRMED:
  - `pec-scratch-server.mjs` is imported by the opt-in integration test (`pec-bridge.integration.test.ts:52`) and by two standalone scripts. No product entry reaches it, so `REACH=TEST_ONLY` agrees with the CAP-BUILD-038 notes.
  - `run-pec-bridge-rehearsal.ts` stays LEGACY_ONLY (UNREACHED). The Disposition is unaffected.

## (ii) Patterns

1. **Does an OpenPipeStress descriptor in `runtime-contracts` count as "core runtime"?** Keys: CLM-004.6, CLM-010.4 and CLM-028. The anchors check out: `tool-descriptor.ts:817-845`, `tool-catalog.ts:110-128` and the registry at 54-84 / 85-114 / 121-137.
   - The REACH tags match `REACHABILITY.csv`.
   - However, the CAP-RTCONTRACT-042 symbol-level notes say the descriptor registry is consumed only by legacy `lib/harness` files. D-APP-50 also authorized `domain_headless_preview_run` for `open_pipe_stress` by name.
   - That leaves both PARTIALLY_IMPLEMENTED and ALIGNED open for FR-114's "adapter layer, not core harness runtime" wording (grading key 3), so CLM-004.6 is CONTESTED.
   - CLM-028 is CONFIRMED because its text is narrower: "do not put OpenPipeStress concepts in public core runtime contracts". The descriptor is literally in `@chirality/runtime-contracts`, and the SoW does not acknowledge D-APP-50.
   - CLM-004.6 and CLM-028 carry different Dispositions on the same evidence. R3 may want to cluster them.
2. **AuthorityTier set to PRD where TYPES is cited or restated.** Keys: CLM-010.4 (the SoW cites TYPES §11.3) and CLM-030 (the row's own NormativeSource is TYPES §11.1 and no PRD source is named).
   - CLM-004.6 and CLM-028 keep PRD, because their SoW rows cite only FR-114.
3. **Staged-live state assertions under the reach rule versus the §2.6 flat-assertion rule.** Key: CLM-004.1.
   - "are live" is a flatly stated present fact, and it is false on the Codex path.
   - The rulebook's reach rule (PARTIALLY_IMPLEMENTED) and §2.6 rule 1 (STALE_SPECIFICATION) both apply.
4. **CONTEXT_CLAIM pointer with a now-false fact.** Key: CLM-006. The pointer "_REFERENCES.md … PRD hash warning" is false, since there is no warning. The adopted rule allows STALE_SPECIFICATION there, and the worker chose NOT_AUDITABLE.
5. **Ownership versus write fence.** Key: CLM-016.1.
   - D-APP-70 §9 (lines 157-159) makes DEL-10-04 primary for the PEC evidence paths and in the same breath keeps F-APP-3 binding. That supports reading "owns" as accountability rather than write authority.
   - AUTHORITY_CONFLICT with plain `R4` remains defensible, because D-APP-58 does not name R4-P27 and no named question fits.

Verified without issue:
- The PostReleaseBasis `NO` values: no cited path is in `TOUCHED_PATHS.csv`.
- The REFERENCE_HASHES PRD row (Match=NO), the Dependencies.csv 7/1 split, and the MEMORY.md:8 and _STATUS.md:17 anchors.
- That 87b3589b8 only appended the P45 note.
- The dates behind PRE_V3_DRIFT: TYPES snake_case canon came in fbd8e29fd on 2026-06-21, and D-APP-50 on 2026-07-04.

## (iii) Effort

- **Files read:** about 25, namely:
  - the SoW, `_STATUS`, MEMORY, `_REFERENCES`, Dependencies.csv, the INSP-03 assessment and the D53A evidence;
  - ruling records D-APP-37, 50, 56, 58 and 70;
  - PRD FR-114, TYPES §11, PLAN R7, SPEC §18 and DIRECTIVE §0;
  - the code anchors in `tool-descriptor.ts`, `tool-catalog.ts`, `domain-profile.ts`, `operation-proposal.ts` and `domain-profile-registry.ts`;
  - the integration test and scripts;
  - the evidence pack and the two capability rows.
- **Git (read-only, frozen tree):** log, show and blame.
- **Context budget:** comfortable.
