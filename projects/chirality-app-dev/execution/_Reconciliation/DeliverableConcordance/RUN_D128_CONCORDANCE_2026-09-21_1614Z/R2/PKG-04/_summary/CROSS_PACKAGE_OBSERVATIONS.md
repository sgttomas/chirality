Manager observations drawn from the ledgers, reverse notes and verifier shards. Keys are cited so
that R3 can check each one. None of this is a ruling or a repair.

1. **PKG-04 is almost entirely a legacy-path package, so R4-Q1 dominates.** The SDK probe, the
   options builder, the message mapper, the persona composer and the Anthropic key bridge all live
   in `frontend/src/lib/harness/**` or `electron/api-key-*`. That code is LEGACY_ONLY or TEST_ONLY
   at `00115c719`. The live equivalents are Runtime `core`/`daemon` modules: `delegated-engine-adapter.ts`,
   `codex-supervisor.ts`, `runtime-method-service.ts` and `app-owned-composition.ts`.
   - 85 of 280 rows in the ledgers of record cite R4-Q1.
   - One owner answer to R4-Q1 (history, compatibility or obligation), applied at package level,
     would settle most PKG-04 non-ALIGNED rows. It would also settle whether PKG-04 is re-scoped
     to the live Runtime modules or retired under RETIRED_BY_RULING.
2. **The legacy-versus-live reading is the largest source of variance, and it moves the
   ALIGNED count.** DEL-04-03 has three independent attempts. The first two were superseded,
   and VERIFICATION.md §5 records why.
   - Attempt 1 judged mapper requirements on the live path. It had 9 ALIGNED rows and 20 R4-Q1
     rows.
   - Attempts 2 and 3 were reminded that CONVENTIONS §2.3 allows a module-level reading when the
     requirement's subject is the retained module. They had 19 and 16 ALIGNED rows, and 4 and 1
     R4-Q1 rows.
   - On the 21 base keys that none of the three attempts split, exact Disposition agreement is
     10/21, while ALIGNED-versus-non-ALIGNED agreement is 20/21.
   - DEL-04-02 read the builder requirements at module level. Its reverse notes list what each row
     would become on the live path.
   - For R3 and later waves: state the subject test (module versus product behaviour) explicitly,
     or fold it into R4-Q1. Until then, HumanDecisionNeeded counts in legacy-heavy packages depend
     on how each worker read this test and are soft.
3. **The App DIRECTIVE §2.8 was never amended for D-GOV-43.** It still names the Claude Agent SDK
   as the first adapter and Anthropic as the key-aware default. The PRD, CONTRACT and SPEC Codex-only
   preambles say the opposite, and DIRECTIVE §0 ranks the DIRECTIVE higher.
   - This yields AUTHORITY_CONFLICT at DEL-04-01#CLM-003 and DEL-04-05#CLM-024 (verifier CONFIRMED
     for both), with DEL-04-05#CLM-026 CONTESTED.
   - It is expected to recur wherever a deliverable restates §2.8 (PKG-02 DEL-02-05; PKG-03).
   - This is the R0 §8 finding 9 question, now sharpened: the preambles alone do not resolve it,
     because §0 places the DIRECTIVE above them.
4. **The evidence pack's REACHABILITY map has module-level false positives, which affect every
   wave.** Several modules show as LIVE in the map only because a barrel re-exports them or because
   a single helper is imported. They were retagged by errata (DEL-04-02: 3 rows; DEL-04-05: 8
   rows; DEL-04-03 attempts 1–2) and by the verifier correction at DEL-04-05#CLM-012:
   - `runtime/core/src/compatibility-session-policy.ts` is unreached;
   - `runtime/contracts/src/harness/engine-conformance.ts` is TEST_ONLY;
   - `frontend/electron/api-key-storage.ts` is live only in `isProviderCredentialId`; the store is
     TEST_ONLY;
   - `frontend/src/lib/harness/runtime-fingerprint.ts` is TEST_ONLY;
   - `scripts/validate-harness-section9.mjs` is TEST_ONLY.
   Verifiers confirmed every one. Later waves would benefit from a symbol-level exceptions list
   next to `_shared/EVIDENCE_PACK/REACHABILITY.csv`, or from telling workers to check barrels.
5. **D-APP-72 (Pi/oMLX) work is recorded as delivered, but no SoW covers it.** This is the Pi event
   mapping in DEL-04-03 and the authenticated loopback oMLX bridge in DEL-04-05. The second is the
   same gap R0 found, reproduced independently. Both are LEGACY_ONLY and appear only in
   reverse_notes, because an erratum cannot add a row. R3 needs a route for missing forward rows,
   for example a manager-level supplementary register, since the sealed ledgers cannot take them.
6. **SOW-079 (SCA-APP-009) was assigned to DEL-04-01 and never transcribed.** The live Codex
   `0.154.0` pin and host (CAP-BUILD-012, CAP-RTCORE-002/004) are therefore owned by no deliverable
   requirement: DEL-04-01#STATE-1 and REGISTER-3, and the reverse notes. This bears on the
   extension ledger item 5 (SOW), where SOW-079 needs checking against it.
7. **The live event path persists raw Codex params with no redaction.** CONTRACT K-EVENT-6 requires
   redaction before every sink. This is DEL-04-03#CLM-004.5 (attempt 1: HumanDecisionNeeded
   refuted to NO; attempt 3: its own errata change DOCUMENTED_UNIMPLEMENTED to
   PARTIALLY_IMPLEMENTED) and DEL-04-05#CLM-030 (Disposition refuted: ALIGNED to
   PARTIALLY_IMPLEMENTED).
   The owner is likely in the Runtime/session packages (PKG-03, PKG-05), so R3 should check that
   those ledgers carry it.
8. **Credential custody.** The App's Runtime composition wires a stub credential store
   (`app-owned-composition.ts:225`), `SafeStorageCredentialStore` is TEST_ONLY, and the settings
   UI is hidden in the hosted shell (DEL-04-05#CLM-009.3/.4, STATE-3). This is consistent with
   CREDENTIAL_CUSTODY (D-APP-126/127), but the DEL-04-05 carriers still describe daemon custody,
   and REM-1 (V3-02) is gated on a retired consent contract (MOOT:D-APP-127). PKG-02 (DEL-02-05
   REM-1 depends on it) should match.
9. **GOVERNING text drifted from code.**
   - SPEC §13.1 and PRD FR-023 still require the `CHIRALITY_GLOBAL_MODEL`/frontmatter fallback
     tiers that commit `9b005c23a` removed (DEL-04-02#CLM-010.1, CLM-028).
   - SPEC §13.1 makes WORKING_ITEMS the default persona, while the code and SoW use HELP_HUMAN.
   - TYPES §3.4 role aliases do not match the four-role resolver (DEL-04-04).
   These are governing-document findings. Under Ruling D, R2 does not audit the governing documents,
   so they are routed to R3/R4 as evidence only.
10. **Corpus-wide hygiene, confirmed again.** All 15 PKG-04 `_REFERENCES.md` MATCH hashes fail to
    reproduce, there is one REGISTER row per deliverable, and no PKG-04 carrier cites D-APP-127 or
    D-GOV-43 (pack item 5). This supports R0 §8 finding 7's suggestion of a single corpus-wide
    repair.
11. **Seal and errata mechanics worked.** No sealed ledger changed. There are 19 errata rows across
    4 units. Two change a Disposition: DEL-04-02#CLM-028 and DEL-04-03#CLM-004.5. Verifiers
    graded every errata row. Under RUN_BASIS Addendum 3, non-verdict refutations go to
    `CORRECTIONS.csv` rather than triggering reruns.
12. **Candidates for R4-Q4 (Addendum 4), mapped by R3 because the ledgers are sealed.** Several
    rows were sealed before Addendum 4 and turn on the 2026-09-09 four-role adoption (`9b005c23a`):
    - DEL-04-04#CLM-004: plain `R4`; SPEC §13.1 has WORKING_ITEMS as the default, the code has
      HELP_HUMAN.
    - DEL-04-04#CLM-010.5: plain `R4`; the resolver is bounded to the four-role registry.
    - Possibly DEL-04-04#CLM-010.4 and #CLM-003.
    - DEL-04-02#CLM-003 and #CLM-010.1: they cite `R4-Q1`, but the fallback tiers were dropped by
      `9b005c23a`.
    No sealed row was edited. The Addendum 5 tie-break also arrived after every PKG-04 ledger had
    been sealed and verified; R3 applies it to the 83 STALE_SPECIFICATION and 27
    REMAINING_STATE_MISMATCH rows.
