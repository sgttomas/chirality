# V-DEL-03-04 — verifier shard notes (PKG-03, DEL-03-04)

This shard graded the sealed ledger against CONVENTIONS as amended by RUN_BASIS Addenda 4
(R4-Q4) and 5 (the §2.6 tie-break). Evidence was read at the frozen tree `00115c719`. There is
no errata file for this unit.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (LOW / self-flag / AUTHORITY_CONFLICT) | 7 | 3 | 1 | 3 |
| a30 (30% of other non-ALIGNED) | 13 | 9 | 2 | 2 |
| b (15% of ALIGNED) | 4 | 3 | 1 | 0 |
| c (reverse) | 4 | 4 | 0 | 0 |
| **Total** | **28** | **19** | **4** | **5** |

- **Verdict-field refutations (Addendum 3):** 0. All 4 REFUTED items are field-only:
  - AssessmentEvidence on CLM-009.12;
  - AuthorityTier on CLM-005 and CLM-004.1;
  - Notes on CLM-006.
- **CONTESTED:**
  - Disposition on CLM-013.1, CLM-031, STATE-3 and CLM-003;
  - CauseTag on CLM-002.
- **Reverse responses:** all 4 confirmed.
- **Line anchors:** every anchor checked resolves to the cited content at the frozen basis
  (SoW, `_REFERENCES.md`, `MEMORY.md`, the Runtime and App code, and the decision records).
- **PostReleaseBasis:** `NO` holds. No cited line range overlaps a `TOUCHED_PATHS.csv` range.

## (ii) Systematic patterns

1. **Dated history notes vs present-state claims (§2.6 tie-break 3, MR-8 iv).** Dated
   reconciliation notes and MEMORY log entries were judged STALE_SPECIFICATION:
   - CLM-013.1 and CLM-031 (the 2026-07-12 UPD-117 note);
   - STATE-3 (MEMORY entries dated 2026-08-15 and 2026-07-10).

   The worker self-flagged each one. The tie-break leaves both readings open:
   - present fact now false (the basis is LEGACY_ONLY, and the test file was deleted by
     `39c0bb6ab`);
   - snapshot or history true of its date.

   So these are graded CONTESTED. R3 should settle this once for the corpus.
2. **AuthorityTier inflation on rows that cite only PRD or App rulings, and the reverse.**
   - CLM-004.1 cites PRD FR-019, PRD 7.4 and D-APP-40 but is tiered GOVERNANCE_INVARIANT. It
     should be PRD.
   - CLM-005 restates SPEC 9.2 but is tiered LOCAL_DESIGN. It should be GOVERNANCE_INVARIANT.
3. **Inconsistent handling of the unamended TurnEngine clauses (SPEC 10.4, PRD FR-070/071).**
   - CLM-010.4 correctly treats them as AUTHORITY_CONFLICT with R4-Q1. SPEC 17.1 and 25.1
     were amended under D-GOV-43, but 10.4 was not, and D-GOV-43 / D-APP-127 do not name it.
   - CLM-003 restates the same attribute but folds it into a single STALE_SPECIFICATION row.
     This is CONTESTED; splitting the table row would resolve it.
   - CLM-003 Notes also list the PRD source-state attribute as stale, but it is true at
     `00115c719`: the `REFERENCE_HASHES` PRD `Match` is `NO`.
4. **AssessmentEvidence consistency.**
   - CLM-009.10 correctly marks an INSP-03 PASS that rested on LEGACY_ONLY code as OVERTAKEN.
   - CLM-009.12 keeps the REQ-011 PASS, which rested on `turn-engine.ts` (LEGACY_ONLY), as
     STILL CURRENT, although its cancel-release conclusion no longer holds on the live path.
     REFUTED.
5. **Minor tokens and CauseTag.**
   - **Tie-break 3 token:** CLM-006 points to REGISTER-1 in prose rather than with
     `SEE:DEL-03-04#REGISTER-1`, as tie-break 3 requires.
   - **CauseTag date rule (CLM-002):** the divergence dates to SCA-APP-005 (2026-07-27,
     `16f7ed612`), before 2026-08-22, so PRE_V3_DRIFT competes with RUNTIME_EXTRACTION.
     Graded CONTESTED.

What held up well:

- **MR-11 on the disconnect rule.** CLM-004.2, CLM-009.12 and CLM-022.3 apply MR-11
  correctly. D-APP-127's governing facts say a renderer disconnect no longer interrupts a turn,
  and the ruling names the DEL-03-04 clauses. SPEC §11 and PRD FR-017/019 were revised to
  match.
- **CLM-022.4 (AUTHORITY_CONFLICT, plain R4).** Amended K-EVENT-6 conflicts with unamended
  K-ENGINE-4 and SPEC 10.3. No named question fits, including R4-Q4.
- **Live-path redaction gap.** CLM-004.6 and CLM-009.10 hold. A grep of the Runtime
  `core`, `daemon`, `contracts` and `client` sources found only the e-mail redaction of
  app-server stderr. The App's live redaction covers chat labels only
  (`chat-organization.ts`).

## (iii) Effort

- **Files read:** about 25 targeted reads, by line range and grep:
  - the rulebook, RUN_BASIS, the brief and SELECTION;
  - the ledger and reverse files, read by script;
  - the evidence pack (REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES, D-APP-127 map);
  - the DEL-03-04 SoW, `_STATUS`, `MEMORY`, `_REFERENCES` and INSP-03 assessment;
  - SPEC §10.3–§11, §17.1 and §25.1; CONTRACT K-ENGINE-4, K-EVENT-4 and K-EVENT-6;
    DIRECTIVE §0; PRD FR-017/019/070/071;
  - D-APP-127 and D-APP-40;
  - about 12 Runtime and App source files;
  - 13 test-name lookups.
- **Git:** read-only `log` and `blame -L` only.
- **Context budget:** comfortable.
