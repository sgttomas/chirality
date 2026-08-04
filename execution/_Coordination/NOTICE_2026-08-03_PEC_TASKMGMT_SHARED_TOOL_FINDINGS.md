# Routed Coordination Notice — PEC Task Management shared-tool findings

Date: `2026-08-03`
From: PEC loop (TASK_MANAGEMENT generational pass, owner-ruled closeout)
To: Root loop (owner of `tools/taskmgmt/taskmgmt.py` per K-AGENTS-1 tool
ownership)
Notice class: coordination, never authority. Root adopts, amends, declines,
or defers under its own instruments and cadence; reading this notice creates
no duty (K-TM-3/K-TM-4). No PEC row tracks these items — they are Root's to
disposition; this notice is the reciprocal citation trail.

## Findings (observed against `tools/taskmgmt/taskmgmt.py`, SHA-256 `9c5cdc562053b2cc2eeb6674b750d95cb7fa47971eb07acee010a404c221d101`)

1. **`loop_of_source()` attribution (already carried by Root).** The helper
   derives loop identity from the first two path segments, so
   `projects/pec/execution/**` attributes to a loop with no register while
   PEC's register lives at `_DomainEngines/pec/_TaskManagement/`. Already
   carried as item 5 of Root's own
   `execution/_Coordination/NOTICE_2026-08-03_SESSION_RECON_TM_CANDIDATES.md`
   (SHA-256 `05e6ee1c1efd8d8c798ef4104850446a1c9754d4b783b25cd6bef37962e28901`);
   cited here for consolidation, not re-raised.
2. **`decision-non-ruled` class blind to Markdown-table decision registers.**
   PEC's `projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md`
   (SHA-256 `54ba10922d063d29b49c614a69ffc8ae473ba3f2c3bc823ef3fe39644f93ad2a`)
   holds 79 rows as a Markdown table; the scan reported zero non-ruled
   decision rows program-wide while two non-ruled rows exist (`D-PEC-02`,
   `D-PEC-03`). Additional parser hazard: row `D-PEC-22` contains a literal
   `\|` escape that shifts naive pipe-splitting by one column.
3. **`evaluation-finding-open` class blind to the `Review_Findings.csv`
   filename.** The scanner keys on `FINDINGS.csv`; PEC's live review
   findings live in per-deliverable `Review_Findings.csv` files, so the open
   `RF-002` (DEL-01-06, SHA-256
   `a5e15e978e970bf76ce8497bd622ee41d73334366aeae9716c7424de96130a32`) was
   found only by manual sweep.

## Reciprocal citations

- Evidence: PEC harvest report
  `_DomainEngines/pec/_TaskManagement/HARVEST_CANDIDATES_2026-08-03.md`
  (SHA-256 `f14b1d86c357b2f1cb7f880a720fbb208be823323f017df4c655d4581b010ca1`),
  §Method and coverage and §Observations item 7; owner ruling of 2026-08-03
  recorded verbatim in
  `_DomainEngines/pec/_TaskManagement/PROMOTION_RULING_2026-08-03_CAND-PEC-2026-08-03-06--16.md`
  ("Shared-tool findings: RULED — ship the draft routed notice to Root in
  the closeout tranche").
- **Cross-reference for consolidation (per PEC owner ruling):** the Piping
  loop is elevating overlapping scanner findings this same generation — its
  harvest candidate `HC-001`, plus the already-routed `TM-PIP-030`
  (`execution/_Coordination/NOTICE_2026-08-03_PIPING_TM-PIP-030_RECEIPT_COUNT_DETECTOR_ELEVATION.md`)
  — so Root can consolidate the shared-tool concerns into one shared-tool
  register row rather than several.

## Boundary

No register write, promotion, priority, elevation effect, or repair is
performed or requested by this notice; sibling-register counts and rows are
displayed by citation only. Any Root register row, repair, or decline is
Root's own act under its own instruments.
