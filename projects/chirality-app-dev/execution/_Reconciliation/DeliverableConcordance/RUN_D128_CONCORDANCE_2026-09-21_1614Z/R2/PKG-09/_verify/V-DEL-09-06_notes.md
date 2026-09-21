# V-DEL-09-06 verifier notes (DEL-09-06)

Shard V-DEL-09-06, 50 items from `SELECTION.csv`. I read the evidence at the frozen tree `00115c719`. The graded ledger was sealed before Addendum 9, and no row needed an R4-Q6 mapping. The class `a30` rows are graded on their values after errata are applied. Where a sealed defect is already corrected by a CONFIRMED erratum, the class `e` item carries that correction.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (REMAINING_WORK) | 4 | 2 | 0 | 2 |
| a30 | 13 | 12 | 0 | 1 |
| b (ALIGNED sample) | 2 | 2 | 0 | 0 |
| c (reverse) | 11 | 11 | 0 | 0 |
| e (errata) | 20 | 12 | 0 | 8 |
| **Total** | **50** | **39** | **0** | **11** |

- No field is REFUTED, so nothing is added to CORRECTIONS.
- No Disposition or Response is REFUTED.
- One Disposition is CONTESTED: REGISTER-2.

## (ii) Patterns

1. **Tag for the proof scripts: TEST_ONLY or LEGACY_ONLY + UNREACHED.** This covers 8 class `e` items: the ImplementationEvidence errata on CLM-016, CLM-020, CLM-021, REM-3 and REM-4, and the Notes errata on CLM-016, CLM-021 and REM-4.
   - The tests import `run-packaged-security-proof.mjs` and `run-network-policy-proof.mjs`, and the R1b file tags CAP-BUILD-029/030 as TEST_ONLY.
   - The manual npm entries `proof:*` also invoke them (`frontend/package.json:32-34`), so they are not invoked "only by a test". The worker brief's UNREACHED rule and Addendum 1 item 4 therefore also fit.
   - The rulebook has no tag for a manual operator script. Neither reading changes a Disposition or an R4-Q1 citation.
   - Suggest that R3 or the owner pick one reading for manual `proof:*` scripts, for example "not live for release proof", as the worker proposed in its friction note.
2. **Errata correctly retag the api-key-storage symbols from LEGACY_ONLY to TEST_ONLY.** This covers 11 CONFIRMED errata, including CLM-003, CLM-010.1, CLM-010.3 and STATE-2.
   - `SafeStorageCredentialStore`, `storeProviderApiKey` and `readProviderCredential` have no non-test importer. `api-key-ipc.ts:2` imports only `isProviderCredentialId`.
   - As a result, CLM-010.3's R4-Q1 correctly becomes `NO` under Addendum 8: no LEGACY_ONLY code meets REQ-003.
   - The erratum on CLM-010.1 also fixes a sealed misreading. `getProviderApiKey` is called in production only by `getOmlxApiKey`. The legacy Anthropic precedence is `readAnthropicApiKey`, at `anthropic-agent-sdk-manager.ts:265-271`.
3. **MechanicallyUnblocked `UNKNOWN` for gates carried by other App deliverables.** This covers REM-2, which depends on DEL-04-05 and DEL-02-05, and REM-3, whose gate is DEL-05-03-V3-01.
   - §2.5 reserves UNKNOWN for status that no App surface records. These carriers are App surfaces, but they sit outside the worker's and the verifier's read roots.
   - The field is graded CONTESTED, not REFUTED. The Dispositions hold.
4. **REGISTER-2 Disposition is CONTESTED between two tie-break rules.**
   - Rule 1: STALE_SPECIFICATION, because DEP-008/009 say "currently TBD" although the commands and paths are located.
   - Rule 2(b): REMAINING_STATE_MISMATCH, because the rule names a register TBD placeholder as its example. The "no accepted dependency edges" statement may also be literally true: the 11 rows are EXTRACTED/ACTIVE, not accepted.
5. **Minor anchor issue in CLM-010.13 (graded CONFIRMED).** The row cites `chat-panel.tsx:1531-1537`, which is where `definitelyNotStarted` is set. The restore itself is at 1610-1627. The restore in the same chat depends on the binding generation, not on `definitelyNotStarted`, so the Notes gloss is slightly too narrow.

Other anchors, REACH tags and PostReleaseBasis values that I checked all hold at the frozen tree:

- **Anchors:** main.ts:133-134/248/292/666/990/599, codex-supervisor.ts:104-108/470-490, app-owned-composition.ts:180/225/226, attachment-copy.ts:10-13, runtime-attachment-resolver.ts:32-48, turn-coordinator.ts:58, turn-engine.ts:218, preload.ts:77 and codex-app-server-client.ts:41-46.
- **PostReleaseBasis:** the cited lines fall outside the TOUCHED_PATHS ranges.
- **D-APP-127:** it names DEL-09-06 as revised and retires identity binding, supplier containment evidence and per-root consent. This supports SEC-1 as MR-11 STALE_SPECIFICATION.

## (iii) Effort

- **Read:** about 30 files or line ranges. These were the rulebook, RUN_BASIS, both briefs, the unit ledger, errata, reverse file and notes, the evidence pack rows, five capability rows, and the DEL-09-06 SoW, `_STATUS`, `_REFERENCES`, `_DEPENDENCIES`, `Dependencies.csv`, INSP-03 and the Evidence summary. I also read D-APP-127, App SPEC §16, CONTRACT K-NET-1, and about 15 code and test files by line range.
- **Git:** 2 read-only `git -C <frozen> log` calls.
- **Budget:** the context budget was adequate.
- **Out-of-root:** nothing out of root was read. REM-2 and REM-3 would be decided by other packages' `_STATUS.md` files.
