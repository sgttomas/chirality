# DEL-01-05 R0 claim coverage

Derivative sample calibration at `faf22452528b5ba895e88ba0ad3770855100de08`; no report acceptance or production application.

61 rows: all 60 stable local SOW identifiers (12 REQ, 11 AC, 9 VER, 10 CLM,
3 OUT, 5 TBD, 2 CON, 8 AX), plus the mapped lifecycle source claim below.
The output/evaluation matrix repeats IDs and creates no additional claims.
Each row preserves its production identifier as `DEL-01-05::<ID>` and includes
its complete source sentence in Notes. No REQ/AC/VER is omitted or handled as
non-claim. Quoted upstream SOW-052/053 and OBJ-005 are covered through CLM-001..005
and the corresponding behavioral contract; this is not a separate whole-project scope audit.

Disposition counts: `{"ALIGNED": 46, "LIFECYCLE_REASSESSMENT_REQUIRED": 1, "PARTIALLY_IMPLEMENTED": 7, "UNKNOWN": 7}`.
Assessment: **ASSESSED_WITH_RESIDUALS** (5 proposed residuals, including UNKNOWN
evidence/document-treatment rows); UNKNOWN prevents warranted NONE. Missing
`## Remaining` is recorded literally, not treated as empty or as closure.

## Fallback lifecycle mapping

ClaimID `DEL-01-05::STATUS-CHECKING`: source `projects/pec/execution/PKG-01_Service_Core_Store/1_Working/DEL-01-05_Zero_dependency_locality_enforcement/_STATUS.md`,
heading `Status: DEL-01-05`, exact quote `**Current State:** CHECKING`,
UTF-8 quote SHA-256 `83b6c0c6d0bb888280c2aebf4587d29735a4094dd668dec139f5d9f2bef6f3f6`. Full file hash is in READ_MANIFEST.json.
The new evidence creates an owner/REVIEW question, never an automatic demotion.

## Claim-class semantics and limits

Behavioral ALIGNED requires the mapped property in current inspected implementation
and current verification. PARTIALLY_IMPLEMENTED is assigned to OUT-001/002,
REQ-001/003/004, AC-001/003 because repeatable counterexamples violate the
explicit broad obligations: REQ-001 says fail whenever the runtime surface
contains a non-workspace package (read with the explicitly permitted standard
library and contract exceptions); REQ-003 says fail whenever the core initiates
external egress. AC-001/003 likewise quantify over violating states. The accepted
operative target and source rules contain no UDP or imported-callable-alias
exclusion. This is a static scanner, not a runtime sandbox: the counterexamples
show inadequate detection, and make no claim that live core has an actual
third-party dependency or network operation. Probe text is parsed, never executed.

The declared methods VER-001 and VER-003 pass their finite named fixture sets;
that does not prove the broader behavioral guarantees. Mechanical BLOCK production
is separate from completeness of detection. VER-004 explicitly requests a sequence
of core changes and at least one release candidate; registration/current hashes
and historical acceptance do not establish that sequence. Its uncertainty is
preserved with REQ-006, AC-004 and REQ-012, without inventing a release act.

Documentary ALIGNED means required note elements, exact definitions, scope
trace or recorded boundary exists coherently. Human-act ALIGNED on AC-010/011
means the later exact owner act is recorded, independent of tests. Provenance
ALIGNED permits the accepted SOW's historic revision-1.3 basis to remain dated
lineage; revision 1.4 is current upstream truth. UNKNOWN on CLM-010, CON-002
and AX-008 concerns whether the owner wants frozen present-state prose explicitly
dated or harmonized. It does not contest the known later owner acts. This is a
calibration convention requiring owner acceptance; decline of that documentation
proposal would not erase the two demonstrated behavioral gaps.

## Dependency, authority and false-positive controls

Dependencies.csv contains only three ACTIVE SATISFIED ANCHOR rows. All proposed
Depends values are NONE. Under LOOP_INIT Step 1 only ACTIVE PREREQUISITE rows
with TBD/PENDING/IN_PROGRESS satisfaction and a target named by the item's Depends
can block it. INTERFACE/HANDOVER/CONSTRAINT/ENABLES only order; SATISFIED/WAIVED/
NOT_APPLICABLE never block. The standing PEC release gate is not a successor edge.
No dependency change or unrelated TM-PEC-023 mapping gate is proposed.

AC-010 and AC-011 G-A are already confirmed on accepted mainline source. Keep
OI-009 open; keep TM-PEC-022 deferred to its DEL-08-02 lifecycle trigger and
TM-PEC-023 held for its dedicated mapping owner session. Ordinary SCA-004 currency
remains complete under the later August 9 evidence, despite older _LATEST prose.
PRD v2.3/D-PEC-79 remain adopted-not-applied; live PRD v2.2 governs. D-PEC-80
retires old plans as selectors. No source grant follows from those facts.

17 accepted artifact rows reproduce against current bytes; all 7 historical
D-PEC-77 manifest rows reproduce at historical merge 379b8b19b12b29eda4fa307e497499d6fe414f8a.
Moved historical paths and later owner updates to _REVIEW/_STATUS are not scanner
regressions. The old registered-check aggregate FAIL is an explicitly historical
harness-labeling finding, not a fresh DEL-01-05 source defect. Current checks are
recorded separately. CHECKING is preserved and no frozen target is edited.

All candidates are NON_SELECTABLE_PENDING_OWNER_APPLICATION. Owner acts must be
observable on origin/main; predecessor run-branch commit/checks/run records can
satisfy predecessor observability only, never a separate owner gate. The sealed
manager basis records fetched origin/main activation; local HEAD and origin/main
were independently equal to `faf22452528b5ba895e88ba0ad3770855100de08` during this worker run.
