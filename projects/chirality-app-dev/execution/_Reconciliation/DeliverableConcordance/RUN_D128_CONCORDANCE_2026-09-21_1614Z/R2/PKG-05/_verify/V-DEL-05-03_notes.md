# V-DEL-05-03: verifier notes (DEL-05-03)

The ledger was sealed after both Addendum 6 (subject test) and Addendum 7 (R4-Q5) reached its worker. R4-Q1/ALSO_MODULE (key 4a) and R4-Q5 citations are graded against both.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a (LOW / self-flag / UNKNOWN / REMAINING_WORK) | 6 | 2 | 1 | 3 |
| a30 | 13 | 9 | 3 | 1 |
| b (ALIGNED) | 2 | 2 | 0 | 0 |
| c (reverse) | 5 | 5 | 0 | 0 |
| e (errata) | 2 | 2 | 0 | 0 |
| **Total** | **28** | **20** | **4** | **4** |

Verdict-field refutations (Addendum 3): **1 of 28 distinct rows**, CLM-014.1 (Disposition UNKNOWN -> ALIGNED). The other three REFUTED items are field-only: CLM-010.3 and CLM-023 on ImplementationEvidence, and CLM-010.12 on AuthorityTier. Three CONTESTED items are on Disposition (the PEC cluster) and one is on CauseTag (CLM-009).

## (ii) Patterns

1. **Symbol-level reach for `run-logger.ts` (key 3).** Rows citing `run-logger.ts:64-111` tag `redactJsonLike` as `REACH=LIVE`. Its only importers are harness-ui-bridge, session-events, sdk-message-mapper, tool-evidence and tool-result-artifacts, and all of them are LEGACY_ONLY. Only `readConfiguredApiKeyVariants` and `redactConfiguredApiKeys` are live, through `chat-organization.ts`. This is refuted on CLM-010.3 and CLM-023. The same text appears on CLM-010.1 and CLM-010.11, but those were graded here only as class c. No Disposition changes. CLM-006 cites the range without naming symbols and was accepted, with a note.
2. **PEC hygiene cluster (CLM-010.14, CLM-014.2 SEE, CLM-028 SEE).** The live path has no PEC transport at all. §2.3 admits two readings: IMPLEMENTED_DIFFERENTLY (exclusion by absence) or DOCUMENTED_UNIMPLEMENTED (the live path lacks the construction). Both are graded CONTESTED. R4-Q1 and ALSO_MODULE are correctly applied under key 4a.
3. **Recoverable evidence treated as UNKNOWN (CLM-014.1, AC-001).** Legacy source parity can be recomputed with permitted read-only `git show e9b9e302c^`. All 220 non-heading legacy lines are present verbatim. The only later change is R14, made by D-APP-68 ruling 7, which names DEL-05-03 (MR-11). VER-001 (CLM-020.1) has no recoverable output, so UNKNOWN stands there.
4. **Minor points.**
   - CLM-010.12 tiers PRD although its source cites CONTRACT K-EVENT-6. The same ledger tiers the parallel CLM-006 as GOVERNANCE_INVARIANT.
   - CLM-009's CauseTag is contestable. The divergence dates from 16f7ed612 on 2026-07-27, before v3.
   - CauseTag use is uneven across sibling rows: A2_TOPOLOGY on CLM-010.13, RUNTIME_EXTRACTION elsewhere.
   - REM-1's R4-Q5 citation fits: the gate rests on a translated, closed schema-v2 vocabulary. MOOT:D-APP-127 is correct (D-APP-127 retires APP-HOLD-1 and the closed event vocabulary).
   - Both errata are correct. The `api-key-storage.ts` storage symbols are unreached, so the tag is LEGACY_ONLY with UNREACHED.

Anchors checked at the frozen tree and found correct (drift at most 1 line):
- session-store.ts
- delegated-engine-adapter.ts
- codex-app-server-client.ts
- desktop-log.ts
- runtime-connectivity.ts
- turn-coordinator.ts
- events route
- decomposition L211/L338
- `_STATUS.md` 11-18 and 38

All cited test cases exist. PostReleaseBasis NO holds: session-store.ts is touched only at lines 6-8 and 128-158.

## (iii) Effort

About 30 file reads or greps, plus read-only git: `log -S`, `show --stat`, and `show <rev>:path` for the legacy parity recompute. The context budget was adequate. Nothing outside the brief's read scope was opened.
