# Run Summary — COV_D101_POSTSETUP_2026-09-26_1651

`RUN_STATUS = WARNINGS`

The run is valid and complete. Every check produced a verdict and no input
failed. Warning-severity findings are present; no blocker is present.

## Headline

| Field | Value |
|---|---|
| Overall status | `WARNINGS` |
| Closure readiness | `WARN` (method-literal three-way verdict; not a lifecycle, readiness, acceptance or reliance judgement) |
| Issues | 0 BLOCKER / 3 WARNING / 73 INFO / 2 EXPECTED_CONSEQUENCE (78 rows) |
| Audited basis | revision 1.6 `current_basis` `9374c21f…08eb1`; registers and PRD v2.4 at the accepted hashes; D-PEC-101 K1 + K4 + C poststate at `43b60687b` (product bytes as at `62230fa46`) |
| Phase | D-PEC-101 post-setup re-audit (add-on V), after verification, before publication |
| Expected consequences cite | `D-PEC-101` (ruling question 4 (a); Administrative grant) |

## The prediction

| Brief expectation | Result |
|---|---|
| COV-003/004/073/074 (two absent folders) resolved | **Yes** |
| COV-075/076 (two stale quotes) resolved | **Yes** |
| COV-080 (SOW-097..100 untraced) resolved | **Yes** (74/74 IN items traced) |
| COV-077/078 (revision 1.5 re-pin) resolved with K4 | **Yes** (68/68 contexts and references at revision 1.6 / PRD v2.4; covers bullets equal the register) |
| Forward production-unit coverage 100 % (68/68) | **Yes** |
| The three pre-existing Check-6 warnings unchanged | **Yes**: prior COV-008 → COV-006 (DEL-01-03), COV-010 → COV-008 (DEL-01-05), COV-046 → COV-044 (DEL-08-02), text identical |
| 0 BLOCKER | **Yes** |

## Every WARNING

| Issue | Check | Entity | Reason |
|---|---|---|---|
| COV-006 | 6 | DEL-01-03 | `IN_PROGRESS`; anticipated set not in the folder (bytes under `projects/pec/v2/`). Carried |
| COV-008 | 6 | DEL-01-05 | Same pattern. Carried |
| COV-044 | 6 | DEL-08-02 | `CHECKING`; source-tree bytes outside the folder. Carried |

All three are pre-existing and unrelated to D-PEC-101.

## Every EXPECTED_CONSEQUENCE

| Issue | Check | Entity | Would be | Decision |
|---|---|---|---|---|
| COV-076 | 9 | `_COORDINATION.md` Notes L225–227 still say revision 1.5 is `current_basis` | WARNING | D-PEC-101 ruling question 4 (a): HELP_HUMAN's authorized replacement, not yet in the tree |
| COV-077 | 10 | `_Decomposition/_LATEST.md` ("no folders yet"), `_ScopeChange/_LATEST.md` and the SCA-006 state fields still call B1/B2/B3/B7 open | WARNING | D-PEC-101 Administrative grant: pointers and the SCA-006 folder not opened; the Lane B closeout goes to the run root's `HANDOFF_STATE.md`, which does not exist yet |

## DEFECT

None. All 161 D-PEC-101 product paths equal the proposal's postimages
(add-on C values where given). Every check over those bytes passed: register
schema, closure, mirror invariant, quote currency, trace coverage, context
fidelity and covers bullets.

## New findings (not DEFECT)

- **COV-072 (INFO, Check 8).** 26 XRG-013: every OUT/TBD ledger row lacks a
  `PackageID` under Root D-GOV-48. This is newly measured because the
  validator changed. The owner defers action, and D-PEC-101 forbids action.
- **COV-078 (INFO, Check 10).** SCA-006's state fields lack
  `AdjustedAuditState`. That field was added to the scope-change contract
  after SCA-006 bound its edition, so this is edition drift.
- **COV-075 (INFO, CHANGED from COV-083).** The `remaining-loop` basis text
  is now stale against live `loops.json`, because D-PEC-96 was applied. The
  owner carried the text knowingly at checkpoint 3. Kept INFO as a judgement
  (`Decision_Log.md` D-10).

## Pre/post headline

| Metric | Prior | This run |
|---|---|---|
| Forward deliverable coverage | 97.06 % (66/68) | 100 % (68/68) |
| Registers / rows | 66 / 263 | 68 / 285 |
| Strict validator | 0 E / 2 DRB-008 | 0 E / 0 DRB-008 / 26 XRG-013 (validator now carries D-GOV-48) |
| Closure edges / nodes / isolated | 111 / 66 / 6 | 127 / 68 / same 6; 0 SCC |
| Issues (B / W / I / EC) | 0 / 3 / 71 / 12 | 0 / 3 / 73 / 2 |

**Per-finding delta.** 64 carried, 8 changed, 14 resolved, 6 new; no new
BLOCKER or WARNING.

## For the caller

- The snapshot holds the method's files (`Brief.md`, `RUN_SUMMARY.md`,
  `QA_Report.md`, `Decision_Log.md`, `Decomp_Coverage_Report.md`,
  `Decomp_Coverage_IssueLog.csv`, `Decomp_Coverage_Matrix.csv`,
  `coverage_summary.json`). It also holds the structure tool's
  `structure.json`, its input `inventory.json`, and `PrePost_Comparison.md`.
- No `_LATEST.md` was touched. The run reports 0 BLOCKERs; whether to move
  the audit pointer is the manager's decision under the ruling.
- The run root's `HANDOFF_STATE.md`, `MANIFEST.md` and `VALIDATION.md`
  (Administrative grant) do not exist yet. COV-077 depends on the first of
  these.
- The worktree HEAD is `43b60687b`, not the brief's `fcc1cd26b`; the
  product bytes are the same (`Decision_Log.md` D-2).
- A `git fetch` during the run moved `refs/remotes/origin/main` from
  `bdae9d66b` to `efe938506` (`QA_Report.md` command 19). `origin/main`
  now also carries the D-PEC-100 ruling and a D-GOV-50 notice. Neither
  touches an audited input, but both are relevant to the act's containment
  check against `origin/main`.
- No independent review of this snapshot was performed.

This snapshot is derivative evidence. It accepts nothing and authorizes
nothing. It makes no CHECKING, ISSUED, acceptance, readiness or reliance
claim.
