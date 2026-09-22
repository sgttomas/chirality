# V-DEL-06-05 verifier notes (DEL-06-05)

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 16 | 13 | 0 | 3 |
| a30 | 11 | 8 | 0 | 3 |
| b | 1 | 1 | 0 | 0 |
| c | 3 | 3 | 0 | 0 |
| e | 3 | 3 | 0 | 0 |
| **Total** | **34** | **28** | **0** | **6** |

## (ii) Systematic patterns

1. **The AUTHORITY_CONFLICT + R4-Q1 cluster holds** (CLM-003, -008, -009.1/.2/.3/.12/.13,
   -013, -018, -022, -024, -026, -029). D-GOV-43 item 4 (see the proposal at lines 187-195, adopted
   as written) makes approval and sandbox policy the user's choice. It never names K-BASH-1,
   K-PERM-3/4/5/6, K-HOOK-1 or K-PATH, and App CONTRACT lines 92-102 are unamended. Under grading
   key 4 that is AUTHORITY_CONFLICT. R4-Q1 fits: it names K-HOOK, K-PATH and SPEC §15.2
   explicitly, and the question of legacy harness versus live Codex covers the K-BASH and K-PERM
   rows. The live-code anchors are exact at the frozen tree (`delegated.ts:320-330`,
   `codex-supervisor.ts:104-110`, `delegated-engine-adapter.ts:265-298,329`). The REACH tags
   match REACHABILITY.csv. None of the relied-on lines fall in a TOUCHED_PATHS range. The
   DIRECTIVE anchor (338-340) is off by one line, which is immaterial.
   - **Exception, CLM-009.4 (CONTESTED).** K-PERM-3 is worded in Claude SDK terms. App CONTRACT
     lines 13-15, the Codex-only MVP preamble, arguably resolve it as compatibility history.
2. **MATCH-restatement rows (CLM-004.1 and CLM-027, CONTESTED).** "Listed as / has MATCH in
   `_REFERENCES.md`" is literally true of the register at the frozen basis. The now-false fact
   belongs to REGISTER-1 (MR-5, MR-8 iv). The worker graded the same reading LOW on CLM-027 and
   HIGH on CLM-004.1, which is inconsistent. CLM-001, -006 and -007 are CONFIRMED: they flatly
   assert current MATCH, or recompute it.
   - Provenance of the recorded PRD hash 8649ccba: it is the PRD at `23b3879b3` (the D-GOV-43
     tranche, 2026-09-12). `9eaddb596` changed the PRD the same day.
3. **Mixed or lumped rows.**
   - CLM-004.2 lumps condition rows 2-6. Its timeout, capture and interrupt conditions are
     partly live, which supports a PARTIALLY_IMPLEMENTED reading.
   - CLM-012's Notes ("nothing corresponds on the live path") point to DOCUMENTED_UNIMPLEMENTED
     under the §2.3 reach rule. Both rows are CONTESTED on Disposition.
   - CLM-016's Disposition holds. Its Notes claim a contradiction with the 8 ACTIVE rows, but the
     SoW text itself acknowledges those rows, so the row is CONTESTED on Notes.
4. **Errata are sound.** All 3 are CONFIRMED.
   - `chat-panel.tsx:136` sets `DEFAULT_OPERATOR_MODE = 'workspaceWrite'` and is LIVE.
   - `delegated.ts:325` maps it to approval `never` + `workspace-write`.
   - The sealed "default ask/undefined" gloss was therefore wrong. The CLM-009.1
     ImplementationEvidence erratum fills an omission; the sealed value was not wrong in content.
   - Class `a` rows CLM-003 and CLM-009.1 were graded on their errata-applied values.
   - Side observation: D-GOV-43 item 4 recommends `on-request` + `workspace-write` for new
     projects. The App's default `workspaceWrite` maps to `never` + `workspace-write`.
5. **Class c.** All 3 PARTIAL responses are CONFIRMED. HARNESS-043 is the Bash mode gating in
   the overlay, HARNESS-047 is hook fail-closed, and HARNESS-048 is the output artifacts.

## (iii) Effort

About 25 file or range reads:
- the brief and the rulebook;
- the ledger, errata and reverse files;
- the evidence pack;
- the SoW, `_REFERENCES`, `_CONTEXT`, Dependencies and INSP-03;
- 4 runtime and 5 legacy harness sources, plus 4 test files;
- App CONTRACT and DIRECTIVE, Root DIRECTIVE, and the D-GOV-43 record and proposal.

Git use was read-only `log` and `show` on PRD.md at the frozen tree. The context budget was
adequate.
