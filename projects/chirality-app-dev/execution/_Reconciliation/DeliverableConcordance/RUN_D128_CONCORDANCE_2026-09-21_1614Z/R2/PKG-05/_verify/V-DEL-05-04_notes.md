# V-DEL-05-04 — verifier notes (DEL-05-04)

STATE: the ledger was sealed after Addendum 6 (it is graded against the subject test, key 4a) and before Addendum 7 (plain `R4` on the R4-Q5 subject is not refuted; the mapping is noted).

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a | 5 | 2 | 3 | 0 |
| a30 | 12 | 7 | 5 | 0 |
| b | 2 | 1 | 1 | 0 |
| c | 5 | 5 | 0 | 0 |
| **Total** | **24** | **15** | **9** | **0** |

- **Verdict-field refutations (Addendum 3):** 2 of 19 distinct ledger rows. Both are on Disposition: CLM-010.7 and CLM-003.2, each ALIGNED or IMPLEMENTED_DIFFERENTLY that should be AUTHORITY_CONFLICT. None are on Response.
- **Field-only refutations:** 7.
  - AuthorityTier: REM-1, REM-3, CLM-004.1, CLM-010.15 and CLM-023.
  - Notes (ALSO_MODULE missing): CLM-016 and REGISTER-2.
- **Contested sub-findings** are recorded inside the REFUTED lines:
  - REM-3 Disposition: REMAINING_STATE_MISMATCH or PARTIALLY_IMPLEMENTED.
  - CLM-010.15 CauseTag: V3_RELEASE_SCOPE or UNRECORDED_JUDGMENT.

## (ii) Patterns

1. **The R4-Q5 subject is under-classified.**
   - The unit states "provider names only as adapter metadata; replay must not be SDK-shaped" (REQ-007, and the CLM-003 UI/runtime separation attribute; K-ENGINE-4 and SPEC 10.3 are unamended).
   - The live code follows the amended K-EVENT-1/K-EVENT-6 (D-GOV-43): `codex.*` types sit in the public `HarnessEventType`.
   - Under grading key 4 this is AUTHORITY_CONFLICT. The worker wrote IMPLEMENTED_DIFFERENTLY at CLM-010.7 and ALIGNED at CLM-003.2, with the earlier unit deferring to the later one without a `SEE:` token (MR-4).
   - Plain `R4` maps to R4-Q5.
2. **AuthorityTier is mis-set in both directions.**
   - Too low: LOCAL_DESIGN on rows that restate SPEC, TYPES or CONTRACT (CLM-004.1, CLM-023).
   - Too high: GOVERNANCE_INVARIANT on rows whose only source is an SCA, a decomposition row or a D-APP ruling (CLM-010.15, REM-3).
   - Not allowed: NOT_APPLICABLE on a REMAINING_WORK row (REM-1).
3. **ALSO_MODULE is applied unevenly.**
   - CLM-013.2 carries it.
   - CLM-016 and REGISTER-2 do not. Both carry R4-Q1 for the same legacy-only redaction guarantee.
4. **Part-wise R4-Q1 is accepted.** Rows with mixed LIVE and LEGACY_ONLY evidence cite R4-Q1 because a named sub-part is met only by legacy code. Those rows are CLM-004.1, CLM-010.12 and CLM-010.10. I accepted this reading and did not grade it as "met by LIVE code".
5. **The evidence holds up.** Every line anchor checked at the frozen tree shows the claimed content, with no drift beyond one line. Every named test case exists. The REACH tags agree with REACHABILITY.csv and with symbol-level checks:
   - `replayHarnessEvents` has no production caller; only the test fake port uses it.
   - The harness-contract re-export is imported only by a test.
   - The live replay path has no redaction.
   - No Runtime test covers malformed lines.
   - PostReleaseBasis NO holds, because none of the cited ranges overlap the TOUCHED_PATHS ranges.

## (iii) Effort

- **Read:** about 30 files or ranges. They cover:
  - the SoW, `_STATUS`, `Dependencies.csv`, and CONTRACT, SPEC and DIRECTIVE excerpts;
  - Runtime contracts, session-store and daemon;
  - App routes, the port, the legacy parser, the woven shell, the lens, the right panel and chat-panel;
  - the section 9 manifest, the test fake, the register rows and one CONTEXT run file.
- **Git:** read-only `log` and `show` against the frozen tree only.
- **Budget:** the context budget was comfortable.
