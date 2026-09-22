# D1 notes — R4 packets P-01, P-02, P-03, P-23, P-24, P-EX (RUN_D128)

TASK D1 (Type 2), dispatched by the R4 WORKING_ITEMS packet manager. Drafts only; no rulings.

## Method

- Read: D_COMMON_DRAFTER and D1 briefs; CONVENTIONS §1, §2.4, §2.6, §4; RUN_BASIS §5 and Addenda 4–13; OWNER_DIRECTION (`done_and_four_way`, `r3_owner_check_answers`); R3_SUMMARY §6–8; CLUSTERS CL-01/02/03/23/24/EX; RUNWIDE_CALLS (f) and (g); R3_SPOT_CHECK (S2-031, with `R3/_work/T8C_VERDICTS.csv` for both readings); OWNER_CHECK.md; OWNER_CHECK_APPLIED.md; fact sheets P-01, 02, 03, 23, 24, EX; the done-declaration candidate §4; D-APP-128 ruling §5.5.3–5.5.4 and D-APP-129 ruling B (working-repo register, both newer than the frozen basis).
- Rows read only through scripts in `R4/_work/D1_scripts/`:
  - `d1_dump.py`: row fields by key or packet.
  - `d1_xref.py`: other-packet membership, and mentions of D-APP-116..119.
  - `d1_qmap.py`: Q-01..Q-13 mentions in any field.
  - `d1_grep.py`: regex search across rows.
  - `d1_subq_p02.py`, `d1_subq_p03.py`, `d1_subq_p23.py`: sub-question files.
  - `d1_check.py`: self-check against the r4_qa C4/C5 rules.
- Worker B's DEL-06-02 ledger was read with `r3lib.read_csv`.
- Verified at the frozen tree:
  - App docs: CONTRACT.md:17 and :138; PRD.md:339-346, :697, :1202, :1389-1400; SPEC.md:1197-1211; DIRECTIVE.md §0.
  - Decisions: D-APP-97 ruling line 20; D-APP-99 ruling line 18; decomposition v3_2 line 382 (G6a); register D-APP-50; `loop/LOOP_INIT.md` §3 (F-APP-2).
  - Deliverable text: DEL-06-02 ScopeOfWork CLM-005, CLM-032, CLM-034.
  - Code and tests: tool-pool.ts:36-111; runtime-method-service.ts:505-519; delegated-engine-adapter.ts:228-231; tool-names.ts:16-22; pack-electron.mjs:86-95; preload.ts:77; validate-release-quality-evidence.mjs:430-446; frontend/package.json:29, :44.
  - Build and CI: repository-root `.github/workflows/desktop-release-template.yml:39-43`; line counts of the four DEL-09-06 secret-scan summaries.
  - Git: commit 718b0d47a (`git log -1`).
- The next free D-APP ID in the working register is D-APP-130. The packets say "the next free D-APP ID" and do not hardcode it.

## Things the manager should know

1. **Path correction.** `desktop-release-template.yml` is at the repository root (`.github/workflows/`), not in the App project, as OWNER_CHECK.md OC-08 says. P-02 cites the root path.
2. **Tag for deliverable text.** Deliverable text (declared state) has no evidence tag of its own. I tagged bullets that restate what a ScopeOfWork or release document says `[run finding]`, since the run extracted those claims.
   - `loop/LOOP_INIT.md` is execution protocol. It is also cited as `[run finding]` (P-03), and labelled in the text as creating no scope.
3. **Sub-questions.** Rules are in each script's docstring.
   - P-02: a = 16 (unknown, OC-20); b = 6 (other unknown); c = 41.
   - P-03: a = 19 (signing posture); b = 3 (G6a/WP-11). `DEL-09-05#CLM-016.3` and `#CLM-016.6` are also G6a rows, but are PRIMARY in P-02.
   - P-23: a = 8 (text out of date); b = 4 (difference already permitted); c = 14 (open gate); d = 12 (DEL-03-02/08-04/08-05/09-02, depending on Q-11).
   - P-01, P-24 and P-EX have no split. P-24 has no PRIMARY rows. P-EX has one row per question.
4. **Held row.** `DEC:D-APP-101` (P-23.c) names an owner ruling on D-APP-118, so it is held from R5 until D-APP-118 is ruled (D-APP-128 §5.5.4). No other D1 PRIMARY row mentions D-APP-116..119.
5. **Q-01..Q-13 coverage.** Rows name Q-01, 02, 04, 06, 07, 11 and 13 in Notes or DirectionEvidence. No row names Q-03, 05, 08, 09, 10 or 12. P-24 gives the nearest related rows found by search: `DOC:BUILDREL#13`, `DEL-09-05#REM-1`, `DEL-05-01#REM-1`, P-16.
   - Q-07 hits on 20 DEL-07-01 rows come from their DirectionEvidence (`CTX:...DONE-05 and Q-07`).
6. **Out-of-packet inconsistency.** `SOW:SOW-072` is graded ALIGNED and reads K-RELEASE-1's unsigned target as unamended (call f). It is not in any D1 packet. Under P-03 option A or C it would need a follow-up.
7. **P-01 third reading.** Option C applies the Addendum 6 subject test to both keys: both rows become "built differently", with R4-Q1, and the stale parts recorded as secondary. That is my construction from the adopted rule, not either worker's verdict.
8. **Length.** P-02, P-03 and P-24 run to about 1,150–1,250 words, because the briefs require the full "rows for R4 attention" list (P-02), both spot-check readings (P-03) and all 13 questions (P-24). The rest are within about 1,050 words.
