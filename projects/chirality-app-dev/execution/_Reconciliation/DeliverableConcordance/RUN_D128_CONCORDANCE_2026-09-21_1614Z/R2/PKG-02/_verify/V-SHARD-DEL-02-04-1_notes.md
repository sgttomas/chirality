# V-SHARD-DEL-02-04-1 — verifier notes (DEL-02-04)

Graded against CONVENTIONS.md (the adopted rulebook), including the section 2.4 R4-Q1 subject test and the section 2.6 tie-break, and RUN_BASIS §3, §5 and Addenda 1–7. I read only the frozen tree and used git read-only (`log`, `show`, `blame -L`). I ran no tests.

## (i) Counts

| Class | Items | CONFIRMED | REFUTED | CONTESTED |
|---|---:|---:|---:|---:|
| a | 5 | 4 | 0 | 1 |
| a30 | 15 | 8 | 4 | 3 |
| b | 4 | 4 | 0 | 0 |
| c | 6 | 6 | 0 | 0 |
| **Total** | **30** | **22** | **4** | **4** |

Two REFUTED items are on the verdict field (`Disposition`):

- DEL-02-04#CLM-003.4: DOCUMENTED_UNIMPLEMENTED should be PARTIALLY_IMPLEMENTED.
- DEL-02-04#CLM-005.5: DOCUMENTED_UNIMPLEMENTED should be PARTIALLY_IMPLEMENTED.

The other two REFUTED items are field-only (`LatestDecision`): DEL-02-04#CLM-003.1 and DEL-02-04#CLM-009. Their Dispositions hold.

Two of the 30 items are refuted on a verdict field (6.7%, under the 10% rerun trigger).

All four CONTESTED items are on `Disposition`: CLM-003.2, CLM-003.3, CLM-010.11 and REGISTER-7.

## (ii) Systematic patterns

1. **Live path partly covers a requirement, but the row says DOCUMENTED_UNIMPLEMENTED** (CLM-003.4, CLM-005.5).
   - On the live Runtime path, `turn-coordinator.ts` rebuilds `opts` from known keys only. Unknown keys are therefore dropped and change no behaviour, which is what the FR-024 acceptance text requires. Only the warning is missing.
   - Section 2.3 gives PARTIALLY_IMPLEMENTED when the live path covers part of a requirement.
   - The rows' own AssessmentEvidence (INSP-03 REQ-012 PARTIAL, marked STILL CURRENT) describes the same ignored-without-warning state.
   - R4-Q1 and `ALSO_MODULE:ALIGNED` are correctly applied: only the legacy `options.ts` meets the claim in full. The same fix probably applies to CLM-010.12 (REQ-012), which this shard does not cover.
2. **D-APP-108 marked `(context)` while the same row cites `GOV:D-APP-108` and applies the SCA-APP-010 control** (CLM-003.1, CLM-009; SEC-1 tolerated).
   - The D-APP-108 re-pin put in this SoW the section that explicitly controls every older clause.
   - MR-11 says to cite that ruling in LatestDecision as governing.
3. **"Deterministic fallback" rows judged against the FR-023 chain rather than the claim text** (CLM-003.3, CLM-010.11: CONTESTED).
   - The live chains are deterministic, and the row itself says so. The PRD's Codex-only preamble demotes default-provider rules to history.
   - For REQ-011 ("shall remain deterministic"), the ALIGNED reading is the stronger one.
4. **Mixed coverage of the Toolkit option categories** (CLM-003.2: CONTESTED).
   - Model, mode and persona move to the composer (implemented differently).
   - Tools, max turns and governance have no live control, because `OperatorToolkitPanel` renders only under `not-found`.
   - The sibling CLM-005.1, on the same evidence, is PARTIALLY_IMPLEMENTED.
5. **Checks that held:**
   - REACH tags match `REACHABILITY.csv`.
   - The worker's claim that OperatorToolkitPanel, contextReferences, focusedArtifact, dialogueAnchorId and chatRung are unreached as symbols is correct: they appear only in the state module or under `app/not-found.tsx`.
   - All cited test names exist.
   - PostReleaseBasis is NO everywhere:
     - `codex-supervisor.ts:104-112` blames to non-touched commits;
     - the touched lines of `session-store.ts` (the application-tool catalog) are not relied on.
   - REM-2:
     - The MechanicallyUnblocked YES holds: DEL-02-02-V3-03 was removed from Remaining after the PR733 merge, and DEP-02-04-015 and DEP-02-04-016 are SATISFIED.
     - REMAINING_STATE_MISMATCH holds.
   - NONE_FOUND spot-check: `_REGISTER.md` has no toolkit or unknown-option hits, and the APP_V3_* toolkit hits are only path or file copies.
6. **Convention gaps.**
   - REM-1: the MechanicallyUnblocked rule (section 2.5) does not cover a standing discipline with no gate. Read literally, it gives a vacuous YES; the worker's NO is defensible.
   - Class c: CAP-SHELL-004 → CLM-007 and CAP-HARNESS-019 → CLM-010.4 are both acceptable. Closer owners exist: CLM-010.1 and CLM-010.3.

## (iii) Effort

- I read about 25 files or ranges:
  - the SoW, `_STATUS`, `Dependencies.csv`, the INSP-03 assessment and `_CONTEXT` from the frozen tree;
  - the toolkit, options, chat-draft, workspace-state, shell and right-panel code;
  - turn-coordinator, delegated-engine-adapter and session-store;
  - the PRD and SPEC anchors;
  - `_REGISTER.md`;
  - the evidence pack.
- Git: one `show --stat` pair, and `blame` on two ranges.
- The context budget was comfortable.
