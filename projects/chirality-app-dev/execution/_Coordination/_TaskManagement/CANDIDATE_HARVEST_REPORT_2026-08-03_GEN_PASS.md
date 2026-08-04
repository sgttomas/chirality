# Candidate Harvest Report — Generational Pass

Date: `2026-08-03`

Mode: `candidate harvest / full PRD §5.1 sweep (deterministic scan + manual
marker-class sweep)`

Invoking register:
`projects/chirality-app-dev/execution/_Coordination/_TaskManagement/REGISTER.csv`

Examined committed state: `def4437d1586e730446a1537adfb8af1c512f626`

This report is decision support only. It creates no register, work, lifecycle,
acceptance, routing, or authority effect. Rows are written only on the owner's
promotion rulings.

## Federation preflight

`taskmgmt federation` returned `COMPLETE`: four canonical registers validated
(APP `OPEN=7 DEFERRED=4 ELEVATED=0 CLOSED=0`, archived 24; ROOT `5/32/0/0`,
archived 74; PIP `4/23/0/0`, archived 3; PEC `11/1/0/0`, archived 3). Zero
register writes, zero excluded tracked lookalikes, zero operational errors,
zero unresolved ambiguities. One `REMOTE_CLOSED_LOCAL_OPEN` finding program-
wide: local `TM-APP-002` (DEFERRED) links `TM-ROOT-036` (closed at Root) —
carried to the deferral review.

## Sweep coverage

- Deterministic: `taskmgmt scan` (v0 classes) over the four scan roots;
  327 candidates program-wide, **59 with sources inside this loop**
  (40 `evaluation-finding-open`, 18 `notice-not-in-ledger`,
  1 `handoff-blocker`). Projection: gitignored
  `_TaskManagement/.candidates/scan.json` (derived, never authority).
- Manual (classes the helper does not implement in v0): literal
  `TM-CANDIDATE:` / `NEEDS_HUMAN_RULING:` / `MISSING:` tokens across all
  3,936 tracked files under `projects/chirality-app-dev/` (13 hits);
  review-report ranked actions and held-open questions across 51
  review-named surfaces plus a heading sweep of all 2,446 tracked `.md`
  files; `Review_Findings.csv` (none exists in this loop; nearest analogues
  are two SCC `Task_Findings.csv`); HOLD registers (2 real surfaces; the
  canonical `APP_HOLD_REGISTER.csv` is header-only — zero active holds; the
  `_PROPOSALS/APP-HOLD-1_2026-07-26` copy is an immutable historical
  proposal, all six holds released by D-APP-81).
- Fence disclosure (PRD §5.5): deliverable `_STATUS.md` `## Remaining`
  sections and slate/work-graph surfaces were **not harvested**. A sweep
  agent tabulated them incidentally; that tabulation is disclosed as
  excluded, and no candidate below rests on a fenced surface alone.
- Dedupe basis: live register (11 rows), archive (24 rows),
  `CANDIDATE_HARVEST_REPORT_2026-08-02.md` + verbatim
  `OWNER_RULING_2026-08-02_APP_HARVEST_SLATE.md`,
  `CANDIDATE_HARVEST_REPORT_2026-08-03_POST_DAPP90.md` (whose screens are
  agent-proposed treatments accepted by merge; Receipt-113 records the
  owner direction as `CHAT_TRANSCRIPTION — EVIDENCE, NOT RULING`).

Of the 59 deterministic-scan candidates: 9 are live register rows
(TM-APP-002, 025, 027, 028, 029, 030, 031, 032, 033), 1 is closure-echo of
an archived row (TM-APP-026), 45 were screened by the 2026-08-02 owner
ruling or the post-D-APP-90 report, 1 carries pre-authorized unapplied row
maintenance (GP-08 below), and 3 are genuinely new (GP-01..03). The manual
sweep added GP-04..06; provenance review added GP-07 and GP-09..10.

## Candidate slate — awaiting owner promotion rulings

| # | SourceRef | SourceSha (SHA-256) | Concern and domain lenses | Proposed treatment |
|---|---|---|---|---|
| GP-01 | `execution/_Coordination/AgentRuns/APPDEV_PARITY_INSTRUMENT_2026-08-03/NOTICE_TO_HELP_HUMAN.md` | `bd3bd64f6498053f20545e8656d9a6388da7a6c0e46f025318bf6b7d4544ea1f` | D-APP-86 Option A parity evidence passed all three gates on one frozen snapshot; the notice requests ordinary package-local pointer/status review by three deliverable owners (DEL-02-02, DEL-08-02, DEL-05-04) and records that any later accepted D-APP-88 helper implementation is a mandatory non-blocking parity rerun trigger. Neither residue is represented by any row (TM-APP-002 covers the parity-instrument stand-up itself, not these two follow-ons). **Deliverables; Work; Planning; Checking.** | **PROMOTE — one OPEN row** carrying both residues (or two rows if the owner prefers the review request and the rerun trigger separated). |
| GP-02 | `execution/PKG-02_Desktop_Shell_Navigation_and_Operator_State/1_Working/DEL-02-02_Workbench_and_Pipeline_Selection_UX/_run_records/TASK_RUN_2026-08-02_1812.md` (restated in `execution/_Coordination/AgentRuns/APPDEV_UI_COMPAT_FANIN_2026-08-02/HANDOFF.md`, SHA-256 `e44d40deb0b3fc71ac32856f755cb36dccf7662082dcd93f08d4aee62e39c352`) | `b0a60edf1d44afec8285b761e2505fb5c63b6284402c240e3d2cf6118914561e` | Owner-reserved DEL-02-02 presentation question: total-per-Working-Root versus per-group `N` in the `All sessions (N)` control. Recurs across the run record, fan-in handoff, and R7/R8 reviews; represented by no row. Harvestable citations are the run record and handoff; its `_STATUS.md` restatement is fenced and not relied on. **Action Item; Deliverables; Approval; Decisions.** | **PROMOTE — one OPEN row** (owner-decision residue awaiting a presentation ruling). |
| GP-03 | `execution/PKG-00_DAG_Closure_and_Project_Control/1_Working/DEL-00-02_SCC-001_Runtime_SDK_Session_Tooling_Closure/scc-cases/CASE-SCC-001_Runtime_SDK_Session_Tooling/Open_Questions.md` (with `Task_Findings.csv`, SHA-256 `13b5b06c4a5792e89e7563e0422669d821c2cd7fd67732815be7f3b3a356fb2b`) | `20a8962a7b09aeff5179bdfa2ee400c12adfee2e51e39bf365d1039e336f6943` | CASE-SCC-001 shows 9 open questions (Q-SCC-001-001..009, all `Needed From: human ruling`) and 20 non-closed `Task_Findings.csv` rows (2 `READY_FOR_OWNER_WORKFLOWS`, 1 `HUMAN_RULINGS_PENDING`), while the owning deliverable's status surface reads `Remaining — None`. The contradiction (stale case surfaces vs. genuinely undischarged rulings) itself needs an owner determination; the `.md` question format is also invisible to `taskmgmt scan` (v0 reads only `Open_Questions.csv`). **Action Item; Approval; Checking; Decisions.** | **PROMOTE — one OPEN row** for the SCC-001 case-surface reconciliation ruling (not 29 rows; the case files remain the itemized truth). |
| GP-04 | `execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_CLOSEOUT_RECEIPT_RULE.md` | `266af9c9e2ab06742dcab6064000af6d63cb380b99c13a7dcc2fe8a520816e2f` | Root change notice: TM closeouts must append a receipt to the owning loop's receipts surface. Its "Follow-on for this loop" says none required; Receipt-113 shows the loop already complies. **Decisions.** | **NO ROW — `INFORMATIONAL_NO_ACTION`** (adopted in practice; this session's closeout also complies). |
| GP-05 | `execution/_Coordination/NOTICE_2026-08-02_TASK_MANAGEMENT_DEFERRAL_REVIEW_MODE.md` | `a358b455ab217e039f4443ca717816f37d63f4701200e9404c8222858e361b09` | Root change notice adopting deferral review as mode 5 plus launcher renames; no repin required (loop bundles `agents/` wholesale). The loop already ran a deferral review 2026-08-02. **Decisions.** | **NO ROW — `INFORMATIONAL_NO_ACTION`**. |
| GP-06 | `execution/_Coordination/NOTICE_2026-08-03_ROOT_RUNTIME_GRACEFUL_STOP_INVESTIGATION.md` line 119 `TM-CANDIDATE:` marker (drafts/quotes of the same marker in the D-APP-88 R2 run folder are duplicates) | `4f52ed537338ccb678da4a3ad9a5cb96459d1ed844ee67fd7c51c87442500656` | Root RuntimeDaemon graceful stop may block auditable D-APP-88 teardown proof. Screened `NO ROW` by the post-D-APP-90 report, but that screen is agent-proposed (Receipt-113 provenance), so it is re-presented once for an explicit ruling. **Deliverables; Work; Planning; Checking.** | **NO ROW — ratify prior screen** (Root-owned, already routed; App bundle-identity remains TM-APP-030; Root may harvest its own marker). |
| GP-07 | `execution/_Coordination/NOTICE_2026-08-03_ROOT_PI_G1B_APP_WORK_ACCEPTANCE_HANDOFF.md` | `618c5c3edbf55a04eeefbf513e08a566fa1ef751febb3f6dcbe2c07e453af6b4` | Root PI-G1B handoff: PIA-U20..U25 App-side work items are expressly unaccepted and undispatched; the post-D-APP-90 report screened NO ROW on the basis that future disposition "remains an explicit human act" — i.e., *not yet ruled*, not declined, and that screen is agent-proposed. **Action Item; Assignment; Planning; Approval.** | **OWNER CHOICE**: (a) ratify NO ROW (disposition will occur through the loop's ordinary acceptance instruments when reached), or (b) promote one OPEN row to hold the pending acceptance decision visible. No recommendation is forced; (a) preserves the fence against work discovery. |
| GP-08 | `execution/_Coordination/NOTICE_2026-08-02_ROOT_RESPONSE_DAPP84_DAPP85.md` | `b4c6e9a67437618de517616ab411bb411bb099f543663ab14362c745e901b328` | Not a promotion. The 2026-08-02 deferral-review ruling pre-authorized trigger maintenance on TM-APP-027/028/032 once the Root response landed; it landed (supplying TM-ROOT-105..109), and the post-D-APP-90 session recorded "No maintenance was applied because this closeout authorized no register write." The pre-authorized maintenance remains unapplied. **Planning; Decisions.** | **CARRY TO STEP 3** (deferral review), where trigger maintenance on 027/028/032 will be proposed with the exact Root IDs for confirmation in one place. |
| GP-09 | Structural observation: no notice ledger exists anywhere under `projects/chirality-app-dev/` (the only `*NOTICE_STATUS*.csv` ledgers repo-wide belong to the one-time 2026-07-28 Root remediation tranche) | n/a (absence claim at `def4437d1586e730446a1537adfb8af1c512f626`) | Every APP notice authored after 2026-07-28 is structurally "absent from every ledger", producing 18 of the 59 scan candidates and a permanent closure-echo on archived TM-APP-026. Whether the loop should adopt its own notice ledger has never been raised or ruled. **Action Item; Checking; Decisions.** | **OWNER CHOICE**: (a) NO ROW — accept the standing scan noise as harmless, or (b) promote one OPEN row to decide (adopt a ledger / amend the scanner's ledger scoping / explicitly accept the noise). |
| GP-10 | Bucket-C provenance note: the post-D-APP-90 screens of `NOTICE_2026-08-03_ROOT_SCA003_PRD_BASIS_RECONCILIATION.md`, `NOTICE_2026-08-03_TM_LAUNCHER_REMEDIATION.md`, and the PI-G1B/graceful-stop notices rest on merge-accepted agent proposals, not a verbatim owner ruling | see per-file SHAs in the post-D-APP-90 report | This slate re-presents the two substantive ones (GP-06, GP-07). The remaining two are Root-owned notices whose follow-on sections state no App action is required. **Decisions.** | **NO ROW — ratify prior screens** for the SCA-003 and TM-launcher notices in the same ruling. |

## Closure-echo findings (display only; no source-surface writes)

- **TM-APP-026** (archived, `RESOLVED_BY_DECISION`, closed 2026-08-02):
  its source `NOTICE_D-GOV-31_MERGE_GATE_POLICY_SUCCESSION.md` re-surfaces
  as `notice-not-in-ledger` every scan because the loop has no ledger
  (GP-09). Permanent echo until GP-09 is resolved or accepted.
- **33 evaluation findings** (OD6/V1/V1R/V1R2/V1R3/D49/F/V2-F/V3-F series)
  ruled to no-row dispositions on 2026-08-02 still carry open-reading
  `Status` tokens in their immutable `FINDINGS.csv` evidence and will
  re-appear verbatim in every future scan — 56% of this loop's scan volume.
  No action possible or proposed here (evidence is immutable); noted so
  future harvests can screen the block wholesale by citation to this
  report. Exact membership (all under
  `projects/chirality-app-dev/execution/_Evaluation/`):
  - `APP_RUNTIME_BASIS_OD6_2026-07-26_0F8349D/FINDINGS.csv`: OD6-001,
    OD6-002, OD6-003, OD6-004, OD6-005, OD6-006, OD6-007, OD6-008,
    OD6-009, OD6-010, OD6-011, OD6-014, OD6-016 (13; OD6-012/-013/-015/
    -017 are live rows TM-APP-027/028/029/030 and are not screened)
  - `CQF1_CONCORDANCE_57652BA1_2026-07-20/FINDINGS.csv`: V1-001..V1-005
    (5); `.../RECHECK_R1_CONTROL_REISSUE/FINDINGS.csv`: V1R3-001,
    V1R3-002 (2); `.../RECHECK_R1_REPAIR/FINDINGS.csv`: V1R-001..V1R-003
    (3); `.../RECHECK_R1_REPAIR2/FINDINGS.csv`: V1R2-001, V1R2-002 (2)
  - `DAPP49_CURRENT_LOCATION_AUDIT_2026-07-27_FB16E32/FINDINGS.csv`:
    D49-001, D49-002, D49-005, D49-007 (4; D49-003/-004/-006 are live
    rows TM-APP-031/032/033 and are not screened)
  - `DAPP50_HEADLESS_LIVE_BACKCHECK_F67D4470_2026-07-20/FINDINGS.csv`:
    F-001, F-002 (2);
    `DAPP50_HEADLESS_LIVE_FINAL_BACKCHECK_55A066FD_2026-07-20/FINDINGS.csv`:
    V3-F-001 (1);
    `DAPP50_HEADLESS_LIVE_REPAIR_BACKCHECK_FCF152B_2026-07-20/FINDINGS.csv`:
    V2-F-001 (1)
  Screen basis per ID: the 2026-08-02 owner ruling's CH-E dispositions
  (`OWNER_RULING_2026-08-02_APP_HARVEST_SLATE.md`), CH-E01..E11, E14, E16,
  E18..E31, E34, E36..E40.

## Markers verified tracked (no action)

- `TM-CANDIDATE:` in `NOTICE_2026-08-02_TM-APP-002_PARITY_NEXT_PLANNING.md`
  → live TM-APP-002 (also flagged: as an outbound TM-authored artifact
  carrying a literal marker, it will re-harvest itself in every marker
  sweep — screened here by citation to avoid a self-referential loop).
- `TM-CANDIDATE:` in SCA-APP-007 `Brief.md`/`RUN_SUMMARY.md` → live
  TM-APP-034.
- `## NEEDS_HUMAN_RULING` headings in the D-APP-89 facade returns → live
  TM-APP-031.
- Archived-marker echoes (TM-APP-003 in `RECONCILIATION_RETURN.md` and
  `REGISTER_CLOSED.csv`) and meta-references (launcher notice, prior
  harvest report, init prompt, frontend product error strings) — all
  historical/quoted; no action.

## Held-open-by-design review surfaces (no rows proposed)

Owner-gate lists that live correctly in their owning instruments: D-APP-87
replan returns (9 remaining gaps; `NOT_READY_FOR_IMPLEMENTATION`), D-APP-87
UI packaging return (§7.1 + §11 gaps for owner proposal), D-APP-90
measurement return (6 recommendations gated on the held first-domain UI
delta, itself screened owner-ruled resumable state), PI oMLX G5 security
residuals (4 standing), daemon-service Round-2 residuals (superseded by the
D-APP-88 line). Promoting these would convert gate lists into queue rows
against the PRD §4 posture.

## Owner-ruling addendum (2026-08-03)

The owner ruled the full slate; verbatim transcription and application
record: `OWNER_RULING_2026-08-03_GEN_PASS_HARVEST.md` (same folder).
Summary of effect:

- **Promoted:** GP-01 → `TM-APP-036` (MEDIUM); GP-02 → `TM-APP-037`
  (MEDIUM); GP-03 → `TM-APP-038` (HIGH — the `Remaining — None`
  contradiction corrupts the loop's discovery basis and can silently
  exclude live work from selection); GP-07 option (b) → `TM-APP-039`
  (MEDIUM, cross-related to Root `TM-ROOT-106`); GP-09 option (b) →
  `TM-APP-040` (LOW).
- **No row, ratified:** GP-04, GP-05 (`INFORMATIONAL_NO_ACTION`, satisfied
  in practice); GP-06 (premise: Root-owned and routed — coordination note:
  Root's register currently holds no graceful-stop row and the Root TM
  session of this generation is being directed to harvest it; **if Root's
  closeout does not mint a row, re-present GP-06 next generation**); GP-10.
- **Carry:** GP-08 confirmed into the Step 3 deferral review — apply the
  pre-authorized trigger maintenance to TM-APP-027/028/032 with the exact
  Root IDs from `NOTICE_2026-08-02_ROOT_RESPONSE_DAPP84_DAPP85.md`, trigger
  text presented for confirmation before writing.
- **Noise-block screen ratified:** the 33 immutable-`FINDINGS.csv`
  candidates enumerated under "Closure-echo findings" above are screened
  wholesale by owner ratification of 2026-08-03; future harvest sessions
  may cite this report section as the standing screen for exactly these 33
  (source path + FindingID as listed), re-presenting only findings files or
  IDs not in that enumeration.

## Provenance

Sweeps executed read-only by two dispatched opus-5 ephemeral generalists
(deterministic-scan dedupe/echo analysis; manual marker-class sweep) under
sealed briefs; findings validated at fan-in against the register, archive,
and ruling records by TASK_MANAGEMENT. Zero register writes have occurred
in this session as of this report.
