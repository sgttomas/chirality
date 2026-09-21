## §4 Patterns (hand-written by the PKG-05 manager from the shard notes)

1. **K-EVENT-1/K-EVENT-6 vs K-ENGINE-4 (the R4-Q5 subject) is the main source of verdict disagreement.** Three of the six
   verdict-field refutations (DEL-05-04#CLM-010.7, #CLM-003.2; DEL-05-05#CLM-012.7) and one CONTESTED item
   (DEL-05-02#CLM-010.12) turn on whether storing `codex.*` event types and raw Codex params is permitted (amended
   K-EVENT-1/K-EVENT-6, D-GOV-43) or forbidden (unamended K-ENGINE-4, SPEC §10.3). Verifiers read these as
   `AUTHORITY_CONFLICT` + R4-Q5; the workers had IMPLEMENTED_DIFFERENTLY or ALIGNED. DEL-05-02, 05-04 and 05-01 sealed before
   Addendum 7 existed; their plain `R4` rows are mapped by R3, not refuted. R3 should resolve this cluster once, as R4-Q5.
2. **Live persistence carries raw Codex params (gloss error, DEL-05-05).** Six DEL-05-05 rows glossed the adapter's tool events as
   carrying "only toolUseId, toolName, summary, status"; every event also carries `codex: base` with `params`
   (`delegated-engine-adapter.ts:263`), so full tool output is persisted inline and unbounded. Refuted on ImplementationEvidence
   (CORRECTIONS.csv); Dispositions held. **Unselected row DEL-05-05#CLM-010.4** (sealed IMPLEMENTED_DIFFERENTLY) rests on the same
   premise and likely reads DOCUMENTED_UNIMPLEMENTED — flagged for R3; not counted toward the threshold because it was not checked.
3. **Symbol-level reach below LIVE module tags.** Verifiers confirmed the wave-1 lesson: `redactJsonLike` in `run-logger.ts`
   (LIVE module) is imported only by LEGACY_ONLY modules (DEL-05-03#CLM-010.3, #CLM-023 refuted on ImplementationEvidence);
   `resultBudget` constants and the `harness-contract` tool-descriptor facade are LEGACY_ONLY / TEST_ONLY at symbol level (DEL-05-05
   errata, confirmed); `replayHarnessEvents` and `Agent1RunCoordinator` have no production caller. No row was found ALIGNED on an
   unreached symbol.
4. **Addendum 6 applied with small inconsistencies.** DEL-05-01 copied `ALSO_MODULE:ALIGNED` onto every R4-Q1 row; on CLM-003/004/006/018
   the module reading is STALE_SPECIFICATION (Notes refuted). DEL-05-04 omitted ALSO_MODULE on CLM-016 and REGISTER-2. Two verifiers read
   rule 3 ("rows met by LIVE code … do not cite R4-Q1") as applying to fully met rows only, accepting R4-Q1 on partly-live
   PARTIALLY_IMPLEMENTED rows (DEL-05-04 CLM-004.1/010.10/010.12; DEL-05-05 CLM-003/004/010.6/STATE-1). The strict reading would refute
   those R4-Q1 citations; **the rule text is ambiguous on part-wise legacy coverage** — a candidate clarification for HELP_HUMAN.
5. **DIRECTIVE §0 vs AUTHORITY_CONFLICT.** DEL-05-01#STATE-1 (decomposition row L322 "daemon sessions remain Root-owned" vs SPEC 25.1/25.4
   revised under D-GOV-43) was refuted to STALE_SPECIFICATION: DIRECTIVE §0 ranks SPEC above the decomposition.
6. **Tie-break (Addendum 5) cases.** DEL-05-02#REM-1 and #CLM-004 are CONTESTED between REMAINING_STATE_MISMATCH / STALE_SPECIFICATION
   and PARTIALLY_IMPLEMENTED (a Remaining item whose gate is met but whose content is only partly delivered; an unsplit table of mixed
   conditions). DEL-05-01#CLM-005 CONTESTED on tie-break point 3 (snapshot-tied past tense). No row was refuted for choosing the wrong
   side of the tie-break where it clearly decides.
7. **UNKNOWN where evidence is recoverable.** DEL-05-03#CLM-014.1 (legacy source parity) was refuted UNKNOWN → ALIGNED: parity is
   recomputable with permitted read-only `git show e9b9e302c^`.
8. **AuthorityTier drift** (DEL-05-04 ×5, DEL-05-03 ×1): LOCAL_DESIGN on rows restating SPEC/TYPES/CONTRACT, GOVERNANCE_INVARIANT on
   rows sourced only from an SCA, decomposition row or D-APP ruling, NOT_APPLICABLE on a REMAINING_WORK row. All in CORRECTIONS.csv.
9. **What held.** Every line anchor checked (drift ≤ 1 line), every named test case, every PostReleaseBasis `NO`
   (`session-store.ts` touched ranges 6-8 and 128-158 are never relied on), every REFERENCE_HASHES REGISTER row, and all 6 errata rows.

## §5 Rerun decisions and discipline

- **Denominator.** As in PKG-06, the Addendum 3 share is verdict-field REFUTED items / distinct items checked, counting ledger rows and
  reverse responses (both carry verdict fields). No ledger of record exceeds 10%: DEL-05-01 2/22 (9.1%), 05-02_A 0/22, 05-03 1/27 (3.7%),
  05-04 2/24 (8.3%), 05-05 1/23 (4.3%). **Borderline:** counting DEL-05-04 ledger rows only (excluding its 5 reverse responses) gives
  2/19 = 10.5%. Both of its refutations are the R4-Q5 cluster (pattern 1), which a rerun would not settle; the manager did not rerun.
  HELP_HUMAN may direct otherwise.
- **No structural failures**; no send-backs; no reruns.
- **Discipline deviation (verifier).** V-DEL-05-02_A disclosed read-only `git log`/`git status` on RUN_BASIS.md in the working repository
  and `git ls-files`/`git log -1` in the frozen tree, outside the allowance (only `git -C <frozen> log|show|blame -L`). Nothing was
  written. Its verdicts do not depend on those commands (they dated the seal against Addendum 7 and confirmed a file exists). Later
  verifier prompts restated the git restriction explicitly; no further deviation was reported.
- **Double-blind worker B** is compared, not verified (DOUBLE_BLIND_DEL-05-02.md).
