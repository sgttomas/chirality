# V-SHARD-DEL-08-01-1 — verifier notes (R2 PKG-08, DEL-08-01 rerun)

This shard graded the sealed rerun ledger as sealed. For class e it graded the errata ProposedValue. It did not read the `_ORIGINAL/` ledger or its verification.

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 4 | 1 | 0 | 3 |
| a30 | 13 | 9 | 1 | 2 |
| b | 2 | 1 | 1 | 0 |
| e | 2 | 2 | 0 | 0 |
| c | 4 | 4 | 0 | 0 |
| **Total** | **25** | **17** | **2** | **5** |

- A class `a` item is counted once, even when the same ClaimKey also appears in class e or c.
- **Disposition-level REFUTED:** none.
- **Field-level REFUTED:** both on `ImplementationEvidence`:
  - **CLM-009.3.** The gloss says `REQUIRED_DOC_FILES` is used on the "legacy fixture path only". It also gates split-root detection on every default run.
  - **CLM-009.6.** It cites `method-catalog.ts:628-629` as evidence of naming enforcement. Those lines only check that the instruction path is contained and is a file.
- **CONTESTED:**
  - CLM-009.14 on Disposition. The row already records this alternative at LOW confidence.
  - CLM-009.11 on CauseTag.
  - CLM-011 on CauseTag.
  - REM-1 on RemainingWork.

## (ii) Patterns

1. **`OTHER:V3_ROLE_ADOPTION` against the §4 vocabulary.**
   - The tag is justified where the residual is the role-file format or bundle change: CLM-003, 005.1, 006, 009.3, 009.7 and 009.9.
   - **No vocabulary tag names that mechanism.**
     - `CODEX_SOLE_ENGINE` and `NATIVE_DELEGATION` describe the engine and delegation.
     - `V3_RELEASE_SCOPE` describes scope inclusion.
     - The validator was never product-wired, even before v3 (introduced in e612674eb with fixtures only), so `CODEX_SOLE_ENGINE` does not explain CLM-005.1.
   - **Where the tag is contestable, a vocabulary mechanism is arguably primary:**
     - CLM-009.11: `NATIVE_DELEGATION`. The sibling CLM-009.12 uses it for the same Type 2 bridge.
     - CLM-011: `CODEX_SOLE_ENGINE`. The stated residual is "legacy modules only", and the row carries it as CAUSE2.
     - CLM-009.14: `CODEX_SOLE_ENGINE` is also arguable.
   - **Recommendation for the manager:** report the token. Consider whether it should become a vocabulary tag rather than stay OTHER. It recurs on 18 rows, and every other role-format row in PKG-08 will need it.
2. **The same CONTEXT gloss is reused on about 12 rows.** The gloss is "App lane adopted the user-approved v3 role/skill/workflow basis".
   - It paraphrases the whole folder. `HANDOFF_STATE.md` names only the "user-approved Chirality v3 plan"; the role wording is in `MANAGER_RETURN.md`.
   - The prefix and class are correct. I did not refute it.
   - It explains the adoption as a whole, not the specific drops. The PLAN.md removal (CLM-009.3) has no record of its own; the row states this honestly.
3. **Function-level reach under module-level LIVE.**
   - The sealed CLM-009.12 and CLM-009.14 tag `native-role-config.ts` as `REACH=LIVE`. That matches `REACHABILITY.csv`, but the cited functions have no product caller.
   - The errata re-tag them `TEST_ONLY` and add `product-native-role-config.ts` as the live path.
   - I verified the errata from code: the only live caller is at `delegated-engine-adapter.ts:213` (from `app-owned-composition.ts:214`), and `loadTrustedNativeRoleConfiguration` is only re-exported through `index.ts:26`.
   - The sealed rows are CONFIRMED under the §2.3 nuance, because no Disposition changes.

Minor points, which did not change any verdict:

- **CLM-004:** DEP-08-01-020's table row is at `_DEPENDENCIES.md:121`; the ledger cites L46.
- **CLM-009.3 Notes:** "DOC_FILES dropped PLAN.md in 9b005c23a" is imprecise. The prepare script was created in that commit, and the removal was from `build-electron.mjs`.
- **CLM-005.4:** the NONE_FOUND search is loosely phrased. `grep WRITE_SCOPE` does hit files, but only with valid values.
- **REM-1:** Root `AGENTS.md:229-232` carries a generalized instruction-change notice rule, and the G4 validators exist. Only `skills/` → `.agents/skills/` is clearly retired.
- **PostReleaseBasis:** NO on all rows is correct. No cited path appears in `TOUCHED_PATHS.csv`.

## (iii) Effort

- About 30 file reads or greps against the frozen tree, plus a few read-only `git log`/`show` calls: d1166698d, 9b005c23a, e612674eb and `-S` pickaxes.
- The context budget was comfortable. The shared evidence (role files, `agent-instruction.ts`, prepare/verify scripts, `method-catalog.ts`, native-role modules) was opened once and reused.
