# Coordination Notice — Piping TM-PIP-031 harvest-scanner marker-class elevation

**From:** Chirality Piping loop

**To:** Root loop, `execution/_Coordination/`

**Purpose:** elevate the shared harvest scanner's declared marker-class blind
spots for Root harvest; Piping performs no shared-tool repair

## Reciprocal citations

- Piping register row: `TM-PIP-031` in
  `projects/chirality-piping/execution/_Coordination/_TaskManagement/REGISTER.csv`.
- Inbound source notice:
  `projects/chirality-piping/execution/_Coordination/NOTICE_2026-08-03_TM_LAUNCHER_REMEDIATION.md`,
  SHA-256
  `5df971b70c8b15900081825af6bf372afcfe34500024116bb07cc25a1dbdbbd2`.
- Piping harvest report presenting the candidate (HC-PIP-20260803-001):
  `projects/chirality-piping/execution/_Coordination/_TaskManagement/CANDIDATE_HARVEST_REPORT_2026-08-03.md`,
  SHA-256
  `a05f0c8724d6186b8d4c6f2fa948d2403879d0d20134017ea6ea2fa72d3dd48d`.
- Piping owner ruling of record:
  `projects/chirality-piping/execution/_Coordination/_TaskManagement/OWNER_RULING_2026-08-03_HARVEST_SLATE.md`,
  SHA-256
  `b8bad0d61bc9b4851475a6c7d5ef65faa391b964305cdb749e6957fe3c48e38c`.
- Routed notice: this file. The Piping row's `NoticeRef` points back here.
- Receiving Root row: not yet assigned; no foreign register write or
  automatic receiving-row creation is performed.

## Concern

`taskmgmt scan` v0 declares and skips three PRD §5.1 candidate classes:
run-record markers (`TM-CANDIDATE:`, `NEEDS_HUMAN_RULING:`, `MISSING:`),
review-report sections, and per-document token mode. Every loop's harvest
must therefore compensate with an unvalidated manual sweep for exactly the
marker class designed to be the cheapest capture path.

The Piping 2026-08-03 sweep additionally proved a concrete detection gap in
the colon-form convention itself: three PKG-04 fan-in run records carry
heading-form `## NEEDS_HUMAN_RULING` markers that a colon-form grep misses.
They were recovered only by the widened pattern
`(^|##\s*)(NEEDS_HUMAN_RULING|MISSING)\b:?`. Two of the recovered markers
were substantive (already represented by a previously ruled candidate; no
new row resulted, but the recovery was manual, not deterministic). A scanner
implementation of the marker classes should treat heading-form markers as
first-class.

Piping has opened `TM-PIP-031` (`OPEN`, `ElevatedTo=Root`, Priority LOW)
under the owner's 2026-08-03 ruling. The row stays open while Root considers
the shared-tool concern through its own Task Management and governance
instruments.

## Coordination context (per owner ruling; information, not authority)

- The PEC loop's harvest this generation surfaced overlapping shared-scanner
  findings — the same heading-form gap, plus the scanner missing PEC's
  Markdown decision register and its `Review_Findings` filename, plus the
  `loop_of_source()` misattribution — and is routing its own notice to Root.
- `TM-PIP-030` (shared receipt-validator count-detector false positive,
  routed 2026-08-03) is also still awaiting Root harvest.
- Root may consolidate these into one shared-tool row at its discretion.

## Evidence refs

- Shared scanner: `tools/taskmgmt/taskmgmt.py`, SHA-256
  `9c5cdc562053b2cc2eeb6674b750d95cb7fa47971eb07acee010a404c221d101`
  (scan-exclusions declaration naming the unimplemented v0 classes).
- Heading-form marker files recovered manually (all judged
  historical/duplicate; zero live escalations):
  `projects/chirality-piping/execution/PKG-04_Solver Core and Numerical Methods/1_Working/_run_records/TASK_RUN_2026-06-05_2226_TP-DEL-04-03-04-06_REVIEW-READINESS_C_FANIN.md`,
  `.../TASK_RUN_2026-06-05_2238_TP-PKG04-SOLVER-COMPLETION_FANIN.md`, and
  `.../DEL-04-03_Linear support and restraint models/_run_records/TASK_RUN_2026-06-05_2221_TP-DEL-04-03-04-06_REVIEW-READINESS_A.md`.
- Sweep evidence of record: `CANDIDATE_HARVEST_REPORT_2026-08-03.md` §5
  (run-record marker verification), cited above with SHA-256.
- Piping receipt ledger before this notice's closeout receipt:
  `projects/chirality-piping/loop/LOOP_RECEIPTS.md`, SHA-256
  `c229dff38aed49a0275cb893bbf688de615f04edb060d07f1a1c5f4f98cadc79`.

## Requested Root treatment

Harvest this shared-tool concern and present any Root-register promotion or
repair instrument for owner disposition — optionally consolidated with the
PEC-routed findings and `TM-PIP-030` into one shared-tool row. The likely
repair boundary is the scanner's candidate-class coverage (marker classes
including heading form, review-report sections, per-document mode) and its
regression fixtures; this notice does not authorize that work or prescribe
its implementation.

## Boundary

Coordination, not authority. This notice creates no receiving row, repair,
scope, product, dependency, lifecycle, release, priority, or work obligation.
Piping performs no change to the shared scanner or its tests.
