## §4 Patterns (hand-written by the PKG-07 manager from the shard notes; evidence, not rulings)

1. **REF-006 hash drift is post-v3, not pre-v3 (V-DEL-07-02_A; also V-DEL-07-06).** The recorded PRD
   hash `8649ccba…` was written by `23b3879b3` on 2026-09-12 (the D-GOV-43 application tranche) and
   the PRD changed later that day in `9eaddb596` (#778). DEL-07-02_A tagged the REF-006 restatements
   `PRE_V3_DRIFT`; the verifier refuted five of them on CauseTag (`DOC_HYGIENE`). Other PKG-07 ledgers
   already use `DOC_HYGIENE` for the same drift, so this is a per-ledger inconsistency, now in
   CORRECTIONS.csv. The same drift carries `GOV:D-GOV-43` DirectionEvidence on some DEL-07-01 rows and
   `NONE_FOUND` on others (V-DEL-07-01 notes).
2. **Symbol-level reach inside `scaffold.ts` (V-DEL-07-02_A).** Worker A tagged the parser/plan code
   `TEST_ONLY`; the verifier found that `previewScaffoldExecutionRoot` executes the parser and the
   path check from the retained legacy `scaffold_preview` tool, so those lines are `LEGACY_ONLY`
   (four ImplementationEvidence refutations, in CORRECTIONS.csv). The writer
   `scaffoldExecutionRoot` stays `TEST_ONLY`. The verifier judged that mixed TEST_ONLY/LEGACY_ONLY
   evidence does not trigger R4-Q1 rule 3 ("the only code meeting the claim"); worker B tagged the
   same module `LEGACY_ONLY` and cited R4-Q1 on 22 rows. This is the main source of the double-blind
   R4-Q1 split (`DOUBLE_BLIND_DEL-07-02.md` §9). R3 needs one reading of rule 3 for claims met partly
   by legacy code and partly by test-only code.
3. **Rule 3 on partly-live rows (V-DEL-07-05).** DEL-07-05 cites R4-Q1 on rows met partly by live
   code, for the part only legacy code meets (MCP tools, hooks, instruction-root check). The verifier
   graded this correct but flagged that R3 needs one reading of grading key 5a for such rows.
   DEL-07-01 and DEL-07-04 follow the same practice.
4. **Snapshot-tied context text (V-DEL-07-04).** DEL-07-04#CLM-032 ("no source conflict identified
   during P1/P2 drafting") was refuted on Disposition: tied to a named drafting snapshot and true
   then, so `NOT_AUDITABLE`, not `STALE_SPECIFICATION` (MR-8(iv), tie-break rule 3). The worker had
   recorded that alternative as LEAST-CONFIDENT.
5. **Fixture existence (V-DEL-07-03).** DEL-07-03#CLM-009.1 was refuted on Disposition: the route test
   does create `DEL-07-99_No_Status` and `D07-03_Invalid_Folder`, so REQ-001 is `ALIGNED`. The
   verifier notes CLM-017, CLM-023 and CAP-WORKSPACE-011 may share the error; they were not in the
   sample. CLM-014 RemainingWork is corrected accordingly.
6. **Addendum 6 bookkeeping.** One product-behaviour row met only by legacy code lacked
   `ALSO_MODULE:` (DEL-07-04#CLM-013.7, refuted on Notes). Otherwise every sampled R4-Q1 row carried
   the token. One SEE-token omission: DEL-07-01#CLM-006 used prose "cf. REGISTER-1" (tie-break rule 3
   requires `SEE:`).
7. **AUTHORITY_CONFLICT boundary (V-DEL-07-01).** The six DEL-07-01 AUTHORITY_CONFLICT rows (unamended
   K-ROOT-2, K-PATH-2/3, K-HOOK-1 and DIRECTIVE §2.9 against D-GOV-43 items 4 and 10) were confirmed.
   Two rows restating the same obligations with other verdicts (CLM-004, unsplit table;
   CLM-011.9, IMPLEMENTED_DIFFERENTLY, LOW) are CONTESTED.
8. **CauseTag for pre-v3 garbling (V-DEL-07-06).** Text garbled by the D-APP-56 substitution on
   2026-07-14 is `PRE_V3_DRIFT` (+ `CAUSE2:CARRIER_PROPAGATION`), not `CARRIER_PROPAGATION`
   (CLM-028 refuted; CLM-027 contested because its first row went stale only on 2026-09-12).
9. **Reach confirmations.** Every sampled LIVE/LEGACY tag other than pattern 2 held. Workers and
   verifiers agree the status and dependency API routes are served LIVE but have no rendered caller
   (their only UI callers are unmounted Pipeline/Workbench/LoopShell surfaces); the pack map's LIVE
   tag for those surfaces is wrong at symbol level. V-DEL-07-06 doubts DEL-07-06#CLM-010.11's
   `REACH=LIVE` for the same reason (recorded, not graded).
10. **Verifier process note.** V-DEL-07-05's first return and notes reported a CONTESTED item the CSV
    did not contain; on send-back the verifier confirmed the CSV (18/18 CONFIRMED) and corrected the
    notes. Its CLM-012.15 CauseTag observation concerns a forward row outside the shard's selection
    and is carried to R3 as an observation only.

## §5 Rerun and acceptance record

- **Structural:** every ledger, reverse file (once per capability file) passes with 0 errors and 0
  warnings; no errata files were written; no absolute paths in any output.
- **Verdict-field refutations** (RUN_BASIS Addendum 3): DEL-07-03#CLM-009.1 (1 of 19 distinct items
  checked, 5.3%) and DEL-07-04#CLM-032 (1 of 27, 3.7%). No ledger exceeds 10%, so **no rerun**.
- **Field-only refutations:** 15 items across DEL-07-01, 02_A, 03, 04 and 06, written by script to
  `CORRECTIONS.csv` (15 rows). DEL-07-02_A has the highest field-refutation share (9 of 18 checked),
  concentrated in two systematic errors (patterns 1 and 2); no verdict field was refuted there.
- **Accepted ledgers of record:** DEL-07-01, DEL-07-02_A, DEL-07-03, DEL-07-04, DEL-07-05, DEL-07-06.
  DEL-07-02_B is kept for the double-blind comparison only and is not verified.
- **Process deviation:** the DEL-07-03 worker ran one read-only `git merge-base` against the frozen
  tree (outside the permitted log/show/blame set); it self-reported it and no finding relies on it.
