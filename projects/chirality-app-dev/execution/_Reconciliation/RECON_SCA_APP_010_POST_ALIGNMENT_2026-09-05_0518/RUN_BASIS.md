# Run Basis — RECON_SCA_APP_010_POST_ALIGNMENT_2026-09-05_0518

> **Epistemic status:** derivative reconciliation package, not decomposition
> truth and not an independent authority. It records the read-only checks the
> RECONCILIATION manager would run before any activation (calibration-grade
> inventory and claim concordance over the applied pair and the thirteen
> SCA-APP-010 carriers). It is **not** an activated claim-level concordance run:
> no activation ruling exists, no convention set was calibrated with the
> human, and no `RUN_BASIS` freeze was accepted. Nothing here repairs a
> deliverable, moves a pointer, or claims closure.

- **RunID / node:** `APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05` · N5 ·
  `N5-RECONCILIATION` (DOWNSTREAM_HANDOFFS.csv row 5; ORCHESTRATION_PLAN.md
  row N5; WORK_GRAPH.json node `N5-RECONCILIATION`).
- **Dispatch:** HELP_HUMAN (Agent 0) → bounded ephemeral Agent 2 generalist
  acting for RECONCILIATION's read-only checks; no descendant launched; role
  not mechanically enforced.
- **Source state:** repository
  `/Users/ryan/dev/chirality/.claude/worktrees/task-management-gen-pass-518da2`,
  branch `claude/sca-app-010-dependency-closure`, `HEAD` =
  `d66395d101143df68d956984f7ab93f5027418ec` = `origin/main`; working tree
  carries the thirteen refreshed dependency registers (`Dependencies.csv`,
  `_DEPENDENCIES.md`) plus one new `_run_records/TASK_RUN_2026-09-05_*.md`
  per carrier and the untracked run packet; no other tracked path changed.
- **Accepted authorities consumed (read only):**
  - decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
    SHA-256 `c7c05169659bfab17b34440b818130e08a0dcb4660b6193c8bf7ea9285771e61`
    (content commit `dbd812a52d5ed0cb3ed173f3aaaa68703a914291`, an ancestor of
    `HEAD`);
  - companion `execution/_Decomposition/contract_invariant_coverage_register.csv`
    SHA-256 `63383f0467f5419be5c417df9adbf63212958782f13989663279bc8c863feaca`;
  - active pointer `execution/_ScopeChange/_LATEST.md` SHA-256
    `b297f43e16a7de13b782c0a3f30589733398406312c82b613977489bda223fc0`
    (`OPEN_PENDING_DERIVATIVE_CLOSURE`, SCA-APP-010);
  - authority corpus v20 (`execution/_Reconciliation/References/`), no drift;
  - owner ruling D-APP-108 (seating and WORKING_ITEMS alignment, PR #713);
  - SCA-APP-010 Gate-5 evidence (`Evidence/Gate5/RECONCILIATION_REPORT.md`)
    as the parity target for the applied-pair table;
  - N2 `REVIEW.md` (SHA-256 `ece7d8ff…`) and
    `Evidence/n3_reviewed_postimages.json` / `n3_postwrite_identities.json`
    as the parity target for the refreshed registers;
  - `loop/LOOP_INIT.md` section 6 (F-APP-1 to F-APP-5) as the fence text.
- **Corpus census (this pass):** thirteen carriers — DEL-02-01, DEL-02-02,
  DEL-02-04, DEL-02-05, DEL-03-02, DEL-04-04, DEL-05-02, DEL-06-03, DEL-07-01,
  DEL-07-03, DEL-08-01, DEL-08-03, DEL-08-04 — each read at `ScopeOfWork.md`,
  `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`, `Dependencies.csv`,
  `_DEPENDENCIES.md`; the decomposition objectives table (L258–L271), package
  rows (L280–L286), carrier rows (L307–L371), and Scope Ledger reverse view
  (L398–L490).
- **Concurrent work:** N4 (`AUDIT_DEP_CLOSURE`) and N6 (`AUDIT_DECOMP`) run
  concurrently on disjoint surfaces; N4's snapshot
  `execution/_Reconciliation/DepClosure/CLOSURE_SCA-APP-010-GATE5-POST-APPLICATION_2026-09-05_0518/`
  appeared during this pass and was still being written at read time; no N6
  surface existed at read time.
- **Fences honoured:** read-only on every deliverable and every authority;
  no `_LATEST.md` moved (`_Reconciliation/`, `DepClosure/`, `_ScopeChange/`);
  no git state-changing command; no network; helper scripts kept in a private
  scratchpad subfolder (their SHA-256 values are recorded in the evidence
  files that they produced).
- **Method revision:** `docs/DELIVERABLE_CONCORDANCE_METHOD.md` as pinned by
  `agents/AGENT_RECONCILIATION.md` at `HEAD`; only the R0/R1 read-only posture
  is exercised.

## Write set

`execution/_Reconciliation/RECON_SCA_APP_010_POST_ALIGNMENT_2026-09-05_0518/`
(`RUN_BASIS.md`, `RECONCILIATION_REPORT.md`, `CARRIER_CONCORDANCE.csv`,
`Evidence/*`, `MANIFEST.sha256`) and
`execution/_Coordination/AgentRuns/APP_SCA_APP_010_DEPENDENCY_CLOSURE_2026-09-05/instances/N5-RECONCILIATION/{RETURN.md,STATUS.json}`.
