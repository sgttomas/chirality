# V-DEL-05-05: verifier notes (DEL-05-05)

The ledger was sealed after Addendum 6 (the subject test) and Addendum 7 (R4-Q5) reached its worker. R4-Q1, ALSO_MODULE and R4-Q5 are graded against both addenda.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (REMAINING_WORK) | 1 | 1 | 0 | 0 |
| a30 | 16 | 11 | 5 | 0 |
| b (ALIGNED) | 1 | 0 | 1 | 0 |
| c (reverse) | 4 | 3 | 1 | 0 |
| e (errata) | 4 | 4 | 0 | 0 |
| **Total** | **26** | **19** | **7** | **0** |

- **Verdict-field refutations (Addendum 3).** One: `CLM-012.7` Disposition.
- **Other refutations.** Five are on ImplementationEvidence and one is on a reverse-file Rationale. For `CLM-010.4`/`CAP-RTCORE-025` the `PARTIAL` Response holds; only the Rationale is wrong.

## (ii) Systematic patterns

1. **Wrong gloss on the adapter's tool events (ImplementationEvidence).**
   - **The ledger's claim.** Six rows repeat the same gloss: `delegated-engine-adapter.ts:265-275` is said to emit `tool.started/completed/failed` "carrying only toolUseId, toolName, summary, status", with a 64 KiB cap on progress deltas.
   - **What the code does.** Every such event also carries `codex: base`, and `base` includes `params: event.params` (`delegated-engine-adapter.ts:263`). So the persisted `events.jsonl` line holds the raw Codex notification: the full `item`, including `aggregatedOutput`, and the uncapped delta. The 512-character and 64 KiB caps bound only the derived fields. Evidence: `turn-coordinator.ts:289` persists `received.data` unchanged, and `native-event-adapter.test.ts:41` asserts that params are preserved.
   - **Items refuted on this ground.** `CLM-003`, `CLM-004`, `CLM-005` and `STATE-1`. Their Dispositions still hold.
   - **Rows outside this shard's selection.** The gloss also appears on two rows that were not selected, and on one of them it matters more:
     - `CLM-010.4` (sealed `IMPLEMENTED_DIFFERENTLY`) rests on "bounds persisted fields by fixed truncation". The live path in fact persists large tool output inline and unbounded, with no artifact metadata. That is what REQ-004 forbids, so the reading points to `DOCUMENTED_UNIMPLEMENTED`. The manager may want this row checked.
     - `CLM-010.2`'s RemainingWork ("deltas of up to 64 KiB each") is inaccurate for the same reason.
   - **Related reverse row.** The `CAP-RTCORE-025` rationale repeats the error.
2. **R4-Q5 not applied to the provider-neutrality verification row.**
   - `CLM-012.7` (REQ-011) is `ALIGNED` with HumanDecisionNeeded `NO`.
   - The live `HARNESS_EVENT_TYPES` include `codex.notification`, `codex.request` and related types (`event-schema.ts:44-47`), and the adapter persists raw Codex params.
   - Whether that is permitted (amended K-EVENT-1 and K-EVENT-6) or forbidden (unamended K-ENGINE-4) is exactly the question R4-Q5 names. The cited test's regex checks only `sdk|claude|anthropic`, so it does not show neutrality.
   - **Correct reading:** `AUTHORITY_CONFLICT` / `R4-Q5`, with `STALE_VERIFICATION` as the alternative.
   - The ledger does cite R4-Q5 correctly on `CLM-010.2` and `CLM-010.4`.
3. **Reach tags on the threshold constants and the facade. The errata are correct.**
   - The `harness-contract` `tool-descriptor.ts` facade is imported only by `harness-contract-rollback.test.ts`, so its reach is `TEST_ONLY`.
   - `resultBudget` constants are consumed only by legacy `lib/harness` files (`tool-result-artifacts.ts:66`, `chirality-hooks.ts:520`, `chirality-tool-bridge.ts:319`), with no consumer in the runtime packages. So the constants are `LEGACY_ONLY` at symbol level, although the module map tags them `LIVE`.
   - All four errata rows are CONFIRMED. The sealed `CLM-010.12` ImplementationEvidence is refuted and is already corrected by errata.
   - The `CLM-003` erratum fixes the tag but keeps the pattern-1 gloss in its ProposedValue. That residual is graded on the a30 item.
4. **R4-Q1 on partially live rows.**
   - `CLM-003`, `CLM-004`, `CLM-010.6` and `STATE-1` are met partly by LIVE code. For each, the remaining part is met only by LEGACY_ONLY code.
   - I read rule 3's "row met by LIVE code" as a fully met row, so R4-Q1 on these PARTIALLY_IMPLEMENTED rows stands. If the rule is read strictly, a row counts as met by LIVE code once any LIVE code partly meets it. On that reading, R4-Q1 would be refuted on these four rows.
5. **Checks that passed.**
   - Documentary and register rows: `CLM-006`, `CLM-007`, `CLM-032` and `REGISTER-1`. The three MATCH hashes do not reproduce; DIRECTIVE, TYPES and PLAN recompute equal; `Specification.md` and `Procedure.md` are absent.
   - `CLM-009`: MR-11 on SCA-APP-005 applies, since the SCA names DEL-05-05.
   - `REM-1`: D-APP-116 is `AWAITING_RULING` at register line 132.
   - PostReleaseBasis: no relied-on line falls in the `session-store.ts` touched ranges, 6-8 and 128-158.

## (iii) Effort

- **Material read:** about 30 files or line ranges from the frozen tree, plus the unit ledger, the errata and reverse files, four capability rows and the evidence pack.
- **Git:** one `git log` on PRD, one on CONTRACT, and `git show -s 7e3e2ebe2`, all against the frozen tree only.
- **Context budget:** comfortable.
