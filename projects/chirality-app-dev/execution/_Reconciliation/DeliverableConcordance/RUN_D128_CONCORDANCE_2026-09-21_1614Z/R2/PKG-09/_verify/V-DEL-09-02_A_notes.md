# V-DEL-09-02_A verifier notes

Unit: DEL-09-02_A (worker A, ledger of record). Evidence read at the frozen tree `00115c719` only.
Worker B's folder and the double-blind comparison were not read.

## (i) Counts

| Class | Checked | CONFIRMED | REFUTED | CONTESTED |
|---|---|---|---|---|
| a (AUTHORITY_CONFLICT, LOW/self-flag, REMAINING_WORK) | 4 | 4 | 0 | 0 |
| a30 (30% of other non-ALIGNED) | 12 | 10 | 0 | 2 |
| b (ALIGNED sample) | 3 | 3 | 0 | 0 |
| c (reverse PARTIAL) | 1 | 1 | 0 | 0 |
| e (errata rows) | 6 | 6 | 0 | 0 |
| **Total** | **26** | **24** | **0** | **2** |

No verdict-field (Disposition / Response) refutations. The two CONTESTED items are field-only:
- CLM-004 AuthorityTier (NOT_APPLICABLE vs PRD: the Conditions unit also restates PRD 12.4 domain-profile gating).
- CLM-019 HumanDecisionNeeded (R4-Q1 on a row met partly by LIVE Section 9 scripts and partly only by LEGACY_ONLY harness modules. Rule 3 and Addendum 8 do not cover a legacy-plus-live split).

## (ii) Patterns

1. **All 6 errata are correct, and they fix real symbol-level REACH errors in the sealed ledger.**
   - `engine-conformance.ts` is called only from tests. It is LIVE only through the contracts barrel (CLM-010.2, CLM-010.10).
   - `core/src/descendant-tracker.ts` is reached only through `ProcessSupervisor`, which only tests instantiate (CLM-010.11, REM-1).
   - Class a was graded on the errata-applied rows.
   - This matches grading key 3: the module map over-reports LIVE for barrel re-exports.
2. **R4 citations are sound for a ledger sealed before Addendum 9.**
   - AUTHORITY_CONFLICT rows cite R4-Q1, which rule 3 requires because only LEGACY_ONLY code meets them.
   - CLM-010.2 adds R4-Q2 and CLM-010.10 adds R4-Q5; both fit.
   - Mapping note: CLM-010.6 (K-PERM-1..4) now also falls under R4-Q6. It is not REFUTED; R3 maps it.
3. **Section 9 script reach.**
   - Under key 4b, the ledger's REACH=LIVE on the Section 9, premerge and release-quality scripts is correct. The in-root `harness-premerge.yml:51-53` runs `harness:validate:premerge` on pull_request.
   - The BUILD capability file tags CAP-BUILD-024/025/027 REACH=TEST_ONLY, which conflicts with 4b. That is a capability-file issue, not a ledger error.
4. **Minor (no verdict change).**
   - CLM-010.10's stated compaction grep covered only core and daemon. It missed `contracts/src/events.ts:11` (a `compaction` RuntimeEventType that nothing emits).
   - Line anchors checked: SoW, manifest, CONTRACT, PRD, premerge, section9 and wrapper. All exact; no drift.

## (iii) Effort

About 30 file reads and greps across the unit files, the rulebook, RUN_BASIS §3/§5 and Addenda 1-9, the evidence pack (REACHABILITY, TOUCHED_PATHS, REFERENCE_HASHES and the D-APP-127 map) and the frozen tree. The frozen-tree reads were the SoW, _STATUS, _REFERENCES, Dependencies.csv, _SEMANTIC, CONTRACT, PRD, SPEC, the Section 9 manifest and scripts, the in-root workflow, and the runtime contracts, core and daemon sources and tests. There was one read-only `git blame -L` against the frozen tree. The context budget was comfortable.
