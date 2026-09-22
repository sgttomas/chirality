# V-SHARD-DEL-08-05-1 — verifier notes (RUN_D128, R2 PKG-08, DEL-08-05 rerun ledger)

## (i) Counts

There are 43 items. Sealed rows were graded as sealed; for class e, the ProposedValue was graded.

| Class | CONFIRMED | REFUTED | CONTESTED | Total |
|---|---|---|---|---|
| a | 12 | 2 | 1 | 15 |
| a30 | 11 | 0 | 1 | 12 |
| b | 2 | 0 | 0 | 2 |
| e | 11 | 0 | 0 | 11 |
| c | 3 | 0 | 0 | 3 |
| **Total** | **39** | **2** | **2** | **43** |

- **Disposition-level REFUTED:** none.
- **Field-level REFUTED:**
  - CLM-037 Notes (class a);
  - CLM-018.2 Notes (class a).
  - Both sealed Notes say the native-child association and the configured-role history are "observed live". The errata ProposedValues already correct both. The Dispositions hold.
- **CONTESTED:**
  - CLM-012.12 on Disposition. The row's DOCUMENTED_UNIMPLEMENTED is one reading. The alternative is AUTHORITY_CONFLICT under SEE CLM-006: REQ-012 cites TYPES §10 for `status: denied`, but the TYPES §10 v2 status set has no `denied`. That is the same conflict that CLM-012.2 carries. The row's own vacuous-ALIGNED reading is a third option.
  - CLM-021 on LatestDecision. The row gives governing D-APP-40, but the DeclaredState concerns only the DEL-08-04 edge. It may be `D-APP-40 (context)`.

## (ii) Systematic patterns

1. **The live nativeChild path is not executed; the errata are correct.**
   - A grep of `projects/chirality-runtime/packages/*/src` finds only the consumer, at `runtime-method-service.ts:454-455`.
   - The callback bridge (`delegated.ts:245-256`) is declared but has no implementation or caller.
   - So all 11 errata rows are CONFIRMED.
   - In the sealed rows, the error is treated as follows:
     - Where only a module-level `REACH=LIVE` tag carries it (CLM-004, 012.3, 018.1, 018.3, 018.6, 022, REM-1), it is the permitted "LIVE module, not executed" nuance, noted under ConventionIssue.
     - Where the prose makes an explicit "observed live" claim (CLM-037 and CLM-018.2 Notes), it is REFUTED on Notes.
2. **The TYPES §10 v2 vs D-APP-40/56 conflict is handled consistently** (CLM-006, 012.1, 012.2), with one exception: REQ-012 (CLM-012.12) also depends on the TYPES §10 status set, but it is dispositioned DOCUMENTED_UNIMPLEMENTED with no conflict note.
   - Blame supports the chronology in CLM-006: the v2 lines date from 2026-07-11, D-APP-40 from 2026-06-21 and D-APP-56 from 2026-07-12.
3. **Evidence spot-checks held.** These all matched the frozen tree:
   - reach tags against `REACHABILITY.csv`;
   - PostReleaseBasis=NO, since the cited `codex-supervisor.ts` lines 515-520 and 588-592 and the cited `session-store.ts` ranges lie outside TOUCHED_PATHS;
   - SoW and `_STATUS` line anchors;
   - that GovernedAgent1RunCoordinator is never constructed (`runtime-service.ts:664-670`);
   - REM-1's verbatim gate, and DEL-08-04 `_STATUS.md:17`, which is still pending.
   - The only drift, within tolerance, is event-schema 56-62 → 56-65.
4. **CLM-012.9 (LOW):** the verifier's grep found no structural redaction before `appendEvent` in the runtime src. The only redaction is e-mail redaction of stderr in `codex-app-server-client.ts:44`. So the LEAST-CONFIDENT alternative (ALIGNED for events) is not supported, and PARTIALLY_IMPLEMENTED stands.
5. **STATE-1 (LOW):** `D-APP-127_RULING…:128-130` states "There is no packaged daemon". That supports STALE_SPECIFICATION over the alternative reading.

**Convention ambiguities**

- AuthorityTier has no class for restating a D-APP ruling (CLM-009).
- RUN_BASIS §1 routes D-APP-11x rows to HumanDecisionNeeded. REM-1 is arguably touched by D-APP-117, which names "DEL-08-05 persistence" as separately activated. The worker excluded it with a stated reason, and the verifier accepts that.

## (iii) Effort

- **Read:** CONVENTIONS; RUN_BASIS; the unit ledger, errata, reverse and reverse_notes; the evidence pack (REACHABILITY, TOUCHED_PATHS, DECISION_HITS, the D-APP-127 map, REFERENCE_HASHES).
- **Frozen tree:** about 15 files in targeted line ranges: SoW, `_STATUS` (08-05 and 08-04), `_CONTEXT`, `_DEPENDENCIES`/`Dependencies.csv`, TYPES §10, CONTRACT K-EVENT/K-SUBAGENT, DIRECTIVE §0, and the register rows. The runtime files were `codex-supervisor`, `delegated-engine-adapter`, `runtime-method-service`, `role-policy`, `delegated-runtime`, `session-store`, `agent1-run-coordinator`, `runtime-service`, `delegated.ts` and `event-schema`. The legacy harness files were `agent-runtime-contract`, `run-logger`, `session-events`, `sdk-message-mapper` and `tool-result-artifacts`.
- **Git:** two read-only `blame -L` runs (TYPES §10, CONTRACT K-EVENT-4).
- **Context budget:** adequate, not tight.
