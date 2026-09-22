## 4. Patterns (manager synthesis of the shard notes; hand-written)

1. **Reach was taken from the module-level map instead of symbol level (GRADING_KEY 1).** This is
   the most frequent defect. `REACHABILITY.csv` marks a module LIVE when one symbol is live or when
   a barrel re-exports it. Affected modules:
   - `core/src/compatibility-session-policy.ts` (unreached);
   - `contracts/src/harness/engine-conformance.ts` and `PUBLIC_UI_EVENT_NAMES` (TEST_ONLY);
   - `electron/api-key-storage.ts` (only `isProviderCredentialId` is LIVE);
   - `lib/harness/runtime-fingerprint.ts` (TEST_ONLY).
   Workers fixed most of these through errata; verifiers confirmed all 19 errata rows, and
   caught the misses (DEL-04-05#CLM-012, DEL-04-03 attempt 2 #CLM-004.2). A wrong tag changed a
   Disposition only once: DEL-04-02#CLM-028, IMPLEMENTED_DIFFERENTLY → PARTIALLY_IMPLEMENTED, via
   errata.
2. **The subject test for legacy-versus-live (GRADING_KEY 2) is the main source of CONTESTED
   Dispositions.** A requirement whose subject is the retained module can be read at module level
   (often ALIGNED) or on the live path (IMPLEMENTED_DIFFERENTLY / PARTIALLY_IMPLEMENTED).
   - DEL-04-03 attempt 1: CLM-009.2, 009.3, 009.12, 018 were CONTESTED.
   - DEL-04-05: CLM-009.9 and CLM-009.14 were CONTESTED.
   Across three independent DEL-04-03 attempts, on the 21 base keys that none of them split:
   - exact Disposition agreement was 10/21;
   - ALIGNED-versus-non-ALIGNED agreement was 20/21.
   The Disposition core is stable only at the ALIGNED boundary.
3. **Ruling-undercuts-unamended-GOVERNING (§1).** App DIRECTIVE §2.8 is ranked above the Codex-only
   preambles and was never amended for D-GOV-43.
   - AUTHORITY_CONFLICT was CONFIRMED at DEL-04-01#CLM-003 and DEL-04-05#CLM-024.
   - CONTESTED at DEL-04-05#CLM-009.10 (K-NET-1), #CLM-009.14 (K-ENGINE-4 / K-EVENT-6), #CLM-026
     (the §2.8 ownership list), and at DEL-04-03 attempt 3 #CLM-004.6 (SPEC §10.3).
4. **Redaction on the live event path.** Two Dispositions were refuted, and both trace to the same
   fact: the live Runtime event path persists raw Codex params, although K-EVENT-6 requires
   redaction before every sink.
   - DEL-04-05#CLM-030: ALIGNED → PARTIALLY_IMPLEMENTED.
   - DEL-04-03#CLM-004.5: attempt 1 HumanDecisionNeeded refuted to NO; attempt 3 changed the
     Disposition through its own errata.
5. **Field-level slips.** DirectionEvidence cited declared-state carriers (Dependencies.csv) under
   `CTX:` (DEL-04-03 attempt 1). AuthorityTier was set without checking the row's own
   NormativeSource (DEL-04-01#CLM-017; DEL-04-03 attempt 2 #CLM-004.4 and #CLM-023). Rows that
   share a SEE target carried inconsistent AssessmentEvidence (DEL-04-01 CLM-001/004.2 against
   008/015/022, all CONTESTED). Under RUN_BASIS Addendum 3 these are corrections, not rerun
   triggers.
6. **CauseTag between CODEX_SOLE_ENGINE, RUNTIME_EXTRACTION and UNRECORDED_JUDGMENT on
   live-composition gaps.** DEL-04-04#CLM-010.7 and #CLM-010.11 are CONTESTED. This is the same
   ambiguity as R0 §4.
7. **Discipline.** One shard (DEL-04-03 attempt 2) had a recursive grep list file names under
   `projects/chirality-runtime/execution/**`, though it opened none. Later prompts told shards and
   workers to scope greps to explicit paths. No other boundary issue was reported.

## 5. Reruns (record)

- **DEL-04-03 attempt 1** (sealed `1a21af4a…`): 3 of 26 items REFUTED (11.5%), all field-level
  (HumanDecisionNeeded, DirectionEvidence ×2). Under the brief's original step 7, which counted any
  REFUTED field, this triggered a rerun by a fresh worker.
- **DEL-04-03 attempt 2** (sealed `f2e6c847…`): 3 of 21 REFUTED (14.3%), all field-level
  (AuthorityTier ×2, ImplementationEvidence). It triggered a second rerun under the same original
  rule.
- **RUN_BASIS Addendum 3** (owner direction `r2_rerun_rule`) was adopted while attempt 3 was
  running. Only verdict-field refutations now count.
  - Retrospectively, neither rerun would have been triggered: attempts 1 and 2 had 0 verdict-field
    refutations.
  - Attempt 3 finished and was verified under the new rule. It is the ledger of record because it
    is the most recent attempt that passes.
  - Attempts 1 and 2 are marked superseded in STATE.jsonl. Their files had already been moved to
    `_superseded/DEL-04-03_run1/` and `_run2/` before Addendum 3; `SHA256SUMS.txt` in each records
    them.
- **Confound.** The rerun prompts added reminders of existing rules: CTX versus declared state,
  HumanDecisionNeeded when GOVERNING decides, AuthorityTier, symbol-level REACH, and the
  legacy/live subject test. The large HumanDecisionNeeded swing across attempts (R4-Q1 on 20 → 4
  → 1 rows) is partly an effect of those reminders, not only of worker variance.
- No other ledger met either rerun criterion, and no structural failures occurred.
