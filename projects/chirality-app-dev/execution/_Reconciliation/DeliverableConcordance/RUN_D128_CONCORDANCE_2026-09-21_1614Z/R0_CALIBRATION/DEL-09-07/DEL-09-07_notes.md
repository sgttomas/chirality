# DEL-09-07 — forward-pass notes (R0 calibration, unit F-09)

Deliverable: Two-Job Runtime-Control Installer Migration and Rollback (PKG-09).
Lifecycle state: OPEN, retired in place 2026-09-12 under D-GOV-43 item 7 via
D-APP-127 (`_STATUS.md`). Files present: `ScopeOfWork.md`, `_STATUS.md`,
`_CONTEXT.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, `_REFERENCES.md`,
`_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `_run_records/`. Absent: `MEMORY.md` and
any `Assessment_INSP-03_*`, so every row carries `AssessmentEvidence = NOT APPLICABLE`.
`_SEMANTIC*.md` were not needed and were not read.

## 1. Census

The index holds 4 units (SEC-1..SEC-4). Each was split per SoW item, giving 27
sub-rows, plus 4 run-local rows (STATE-1, STATE-2, REGISTER-1, REGISTER-2).
Total: 31 rows. Split rate: 4 of 4 indexed units were split, averaging 6.75
sub-rows per unit.

| ClaimType | n | Disposition | n |
|---|---|---|---|
| REQUIREMENT | 9 | ACCEPTED_DIVERGENCE | 24 |
| ACCEPTANCE | 8 | ALIGNED | 4 |
| STATE_ASSERTION | 5 | STALE_SPECIFICATION | 3 |
| EXCLUSION | 3 | | |
| REMAINING_WORK | 3 | | |
| REGISTER_DEFECT | 2 | | |
| CONTEXT_CLAIM | 1 | | |

Confidence: 2 HIGH, 25 MEDIUM and 4 LOW.

## 2. Least-confident rows

- **SEC-2.5 (REQ-004 owner boundary).** Recorded as ACCEPTED_DIVERGENCE because A2 hands Runtime supervision to the App. Alternative reading: ALIGNED, because this deliverable did nothing and so kept the boundary vacuously.
- **SEC-2.13 (OI-003/OI-007 gate paragraph).** Recorded as ACCEPTED_DIVERGENCE because the transaction-verification gate is moot. Alternative reading: the release-gate half (F-APP-2, D-APP-97, G6a) is still true App-wide and should be split out as ALIGNED.
- **SEC-4.4 (AX-004 cites D-APP-107).** D-APP-107 is superseded in whole. Alternative reading: STALE_SPECIFICATION, a repair-shaped citation, rather than preserved history.
- **STATE-2 (`_CONTEXT.md` live-scope description).** Recorded as STALE_SPECIFICATION. Alternative reading: the "four-document kit preserved as history" in `_STATUS.md` covers it, which would make it ACCEPTED_DIVERGENCE.

## 3. Register-defect summary

- **REGISTER-1.** `Dependencies.csv` and `_DEPENDENCIES.md` still show 8 ACTIVE rows, and all 6 EXECUTION rows are unsatisfied: 003, 004, 006, 007 and 008 are PENDING, and 005 is TBD. The retirement was never reflected in the register; extraction was 2026-09-05 and retirement 2026-09-12.
- **REGISTER-2.** The decomposition `_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` still lists SOW-080 as IN, and still carries DEL-09-07 and OI-003 as live. The App PRD, SPEC and CONTRACT (K-RUNTIME-1) already transcribe the retirement, so the decomposition lags them. MR-11 applies: D-APP-127 governs.
- **Carrier discrepancy (not a deliverable defect; noted on STATE-1).** `execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/tranche/APP_EXECUTION_RETURN.md:42` reports `_STATUS.md` Current State as `RETIRED`. The frozen file says `OPEN`, retired in place. D-APP-127 and `_STATUS.md` agree with each other; the carrier return is wrong. This is CARRIER_PROPAGATION.
- **Stale code comment outside this deliverable.** `projects/chirality-app-dev/frontend/electron/api-key-ipc.ts:131` still reasons about a LaunchAgent running a previous build.
- **Stale test comment outside this deliverable.** `projects/chirality-app-dev/frontend/src/__tests__/electron/runtime-connectivity.test.ts:182` says "launchd restarts it".
- **Routing of the stale comments.** Both are DOC_HYGIENE, for the owning code deliverables.

## 4. Direction and cause

- **CauseTags.** The dominant tag is A2_TOPOLOGY (24 rows). DOC_HYGIENE covers 3 rows. No OTHER tokens were used.
- **Governing basis.** D-APP-127 (application of D-GOV-43), in two sections: "Governing facts applied" (the LaunchAgent and installer are retired) and "D-APP-107 … in whole" (DEL-09-07 is retired, APP-HOLD-1 is removed, and the SoW is kept as immutable history).
- **CONTEXT record used as DirectionEvidence.** `projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_V3_CODEX_HOST_REPLATFORM_20260912/HANDOFF.md` §2.
- **Implementation evidence.** No installer, journal, inspector or fixture code was found; the grep for `launchagent|launchctl|launchd` over both evidence roots returned only retirement comments and negative guards. `runtime-control-ipc.ts:12` states that the LaunchAgent verbs are retired. `runtime-service-host.ts` implements the App-owned child that replaces the daemon.
- **Tests confirming absence.** `runtime-control-ipc.test.ts` ("exposes only the service restart channel") and `cli.test.ts:339` (usage excludes LaunchAgent and daemon install).
- **Why ACCEPTED_DIVERGENCE.** Most SoW rows use it because (a) `_STATUS.md` acknowledges the retirement, and (b) a GOVERNING ruling (D-APP-127) explicitly directs the difference and keeps the SoW unchanged as history.

## 5. Method friction

- **No disposition fits a retired deliverable.** A SoW kept deliberately unchanged "as history" under a ruling is neither STALE_SPECIFICATION (not repair-shaped, since the ruling forbids editing it) nor a clean ACCEPTED_DIVERGENCE. MR-8 expects the text itself to acknowledge the gate, but here only `_STATUS.md` does. Proposed revision: add `RETIRED_BY_RULING`, or state that a sibling `_STATUS.md` acknowledgement satisfies MR-8 for retired deliverables. Either would also collapse this ledger's 27 SoW rows to about 4 without losing information.
- **Split granularity.** Splitting per item on a retired deliverable adds rows with no extra signal. Proposed revision: allow a whole-section row when a single ruling governs every item.
- **PostReleaseBasis.** This cannot be verified without git ancestry, and git is forbidden. It is set to `NO` on the basis that D-APP-127 and the A2 code are dated 2026-09-12, which is presumed to precede the post-v3.0.1 commits. Proposed revision: have the manager supply a file list for those four commits.
- **REMAINING_WORK rows for moot TBDs.** `MechanicallyUnblocked=NO` is technically correct but misleading, since the gate can never be satisfied. Proposed revision: allow a `MOOT` value, or define NO to cover it.

## 6. Effort

- **Files read.** About 22, all as partial or line-range reads: 5 conventions, basis and transcript files; 7 deliverable files; the D-APP-127 ruling and register rows; the HANDOFF and APP_EXECUTION_RETURN excerpts; about 6 code and test files; and greps over the decomposition, PRD, SPEC, CONTRACT and hold register.
- **Context budget.** Not tight. The deliverable is small, and retirement makes the evidence search a negative-presence check.
