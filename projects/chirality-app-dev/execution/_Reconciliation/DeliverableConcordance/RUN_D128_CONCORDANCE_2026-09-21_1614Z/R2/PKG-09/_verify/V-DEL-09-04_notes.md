# V-DEL-09-04: verifier notes (PKG-09 R2)

Shard `V-DEL-09-04`, unit `DEL-09-04` (merged ledger, 76 rows). Evidence was read at frozen basis `00115c719`. The ledger parts were sealed before Addendum 9 (R4-Q6).

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (AUTHORITY_CONFLICT, LOW/self-flag, REMAINING_WORK) | 6 | 1 | 2 | 3 |
| a30 (sampled non-ALIGNED) | 14 | 12 | 2 | 0 |
| b (sampled ALIGNED) | 5 | 5 | 0 | 0 |
| c (reverse) | 10 | 9 | 0 | 1 |
| e (errata) | 2 | 2 | 0 | 0 |
| **Total** | **37** | **29** | **4** | **4** |

- **REFUTED, Disposition:** CLM-022 and CLM-023.3.
- **REFUTED, field only:**
  - CLM-001, on Notes;
  - CLM-019, on AuthorityTier.
- **CONTESTED:**
  - CLM-024, CLM-025.4 and REM-2: the workers' own LOW self-flags, where the rulebook admits both readings;
  - CAP-BUILD-013: CLAIMED_BY versus PARTIAL.

## (ii) Patterns

1. **The signing-posture split between parts. The rulebook supports P1.**
   - P1 marks CLM-003.1, CLM-004.3 and CLM-011.6 STALE_SPECIFICATION. P2 marks CLM-022 and CLM-023.3 AUTHORITY_CONFLICT with R4.
   - The App CONTRACT preamble (`docs/CONTRACT.md:17`) explicitly names K-RELEASE-1: "K-NET-1 and K-RELEASE-1 are read with D-GOV-43 items 1 and 4". It lists bundle signing and notarization as ordinary integrity.
   - K-RELEASE-1 (`:138`) is itself conditional ("unless amended").
   - SPEC §19.4 (`:1203`) and PRD §7.12/§12.8/NFR-030 carry the two-tier posture.
   - The only unamended text is PRD §6.2, and DIRECTIVE §0 places it below CONTRACT and SPEC.
   - So no GOVERNING clause is undercut without being named, and DIRECTIVE §0 resolves what remains. Under grading key 4, AUTHORITY_CONFLICT is wrong.
   - P2's argument was that the §0 order ranks documents, not clauses within one document. It does not hold here, because the CONTRACT amends K-RELEASE-1 by naming it.
   - Correct reading for both rows: STALE_SPECIFICATION with HumanDecisionNeeded NO. CLM-023.3 should carry SEE:CLM-003.1 (MR-4). CLM-022 should keep ALSO:PARTIALLY_IMPLEMENTED for its unrecorded code-manifest vs SPEC 1.1 difference (bullet 1).
   - The same fix affects rows outside my sample: CLM-016 and CLM-017 carry R4 "via CLM-022", and R3 should re-read them.
   - R4-Q6 mapping: none. R4-Q6 covers DIRECTIVE §2.8/§2.10/§4.1/§4.2 and K-PERM-1/6, not K-RELEASE-1. The plain R4 on these rows was the Disposition error, not a missed named question.
   - The Q-02 notes (release act vs F-APP-2) are correctly left as CONTEXT.
2. **Seams from the split and merge.**
   - CLM-001 lacks the `SEE:DEL-09-04#REGISTER-51` link that tie-break rule 3 requires. P1 could not write it across parts, and the merge did not add it.
   - CLM-019 (P2) tiers the same non-normative REF-006 note LOCAL_DESIGN, while CLM-001 (P1) tiers it NOT_APPLICABLE.
   - Both are field-level repairs a manager can make at merge time. Neither changes a Disposition.
3. **Minor, not refuted.**
   - SoW anchors drift by 2 lines on CLM-023.3 and CLM-023.4 (the trade-off rows are at :349 and :350). This is immaterial.
   - CLM-023.4's gloss "no desktop/DMG/upload step" understates `harness-premerge.yml:58-64`, which uploads the section8 summary (not a DMG).
   - CLM-022 tags `sign-electron-runtime-v2.mjs` REACH=LIVE without the DISABLED_BY_DEFAULT qualifier that P1 rows carry (key 4b).
4. **Errata are correct.**
   - Blame on `codex-supervisor.ts:109` gives `1cb09c09d`.
   - `app-owned-composition.ts:118-125` (called at `:159`) is a LIVE service-side pin gate outside the TOUCHED_PATHS ranges.
   - Neither erratum changes a Disposition.
5. **R4-Q1 use is clean.** In my sample, no row cites R4-Q1, and none needs it. REM-2's `generate-macos-icon.mjs` is LEGACY_ONLY/UNREACHED, but the claim is met by LIVE config (`package.json:153`).

## (iii) Effort

- **Read:** about 30 files or ranges:
  - the brief, CONVENTIONS in full, RUN_BASIS §3/§5/Add. 9;
  - the ledger rows, both parts' notes, reverse, errata and reverse notes;
  - the capability rows;
  - SoW L1-120 and L300-372, `_STATUS.md` and `Dependencies.csv`;
  - CONTRACT preamble and K-RELEASE-1, SPEC §19.4, PRD §6.2/§7.12/§12.8/NFR-030, DIRECTIVE §0;
  - the D-APP-127 and D-APP-72 rulings;
  - PACKAGING_PROCEDURE, PA-2 and TRIAL_FINDINGS;
  - `package.json` and seven packaging scripts (ranges);
  - `main.ts`, `codex-supervisor.ts` and `app-owned-composition.ts` ranges;
  - the test names and `harness-premerge.yml`.
- **Git:** read-only `blame -L` on `codex-supervisor.ts` 104-109 and 259-261, `log` on `icon.icns`, and `show --stat b2b32669c`.
- **Evidence roots:** no out-of-root evidence was needed. `.github/workflows/desktop-release-template.yml` (repository root) was not read.
- **Context budget:** adequate.
