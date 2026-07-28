# Latest — revision pointer and handoff state

Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.3**
(**`current_basis`** — accepted 2026-07-28 as the SCA-003 successor under
the owner's standing completion approval after D-PEC-68).

## Handoff state

- **Basis:** D-PEC-60 SOFTWARE_DECOMP revision 1.0 over PRD v2.0; SCA-001
  directed-bootstrap reconciliation; SCA-002 objective mapping; SCA-003
  consumer-interface and ADR-014 historical-lineage concordance over accepted
  PRD v2.2. SCA-003 Gates 1–5 are owner-approved through the standing ruling
  recorded in
  `_ScopeChange/SCA-003_2026-07-28_0824/Decision_Log.md`.
- **Package:** working surface + `ScopeLedger.csv` (94 rows) +
  `Deliverables.csv` (64) + `ContextBudgetQA.csv` (unchanged) +
  `Companion_Inventory.csv` (unchanged).
- **Basis integrity (SHA-256, post-amendment):**
  `SOFTWARE_DECOMP.md`
  `3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787`;
  `ScopeLedger.csv`
  `3cca281f7019a4544b6d4e6ab631a30125429525106f5d65b16aac270ebd50f5`;
  `Deliverables.csv`
  `b27ff4631f4966931990bbf9c033d2593d3dd8ac51b09e0d5112002b98afbc40`.
- **Closure verdict: `CLOSED_FOR_SCOPE_CHANGE_ONLY`.** No package,
  deliverable, objective, scope item, product function, stable ID or
  dependency edge was added, removed, renamed or reclassified.
- **Semantic result:** C3/C15 and their direct statement/description mirrors
  now express pull-oriented consumer-owned use, no forced cadence or
  injection, P2-B use/non-use evidence, and ADR-014 historical lineage.
  DEL-10-12 retains its canonical label/path.
- **AuditState: `NON_BLOCKING_PASS`.** Pre-change baseline:
  `_Evaluation/DecompCoverage/COV_SCA003_PRECHANGE_2026-07-28_0817/`.
  Final post-change evidence:
  `_Evaluation/DecompCoverage/COV_SCA003_POSTCHANGE_FINAL_2026-07-28_0831/`
  (`OK`, 0 blockers / 0 warnings), copied to
  `_ScopeChange/SCA-003_2026-07-28_0824/Post_Change_Coverage.json`.
- **Supersession:** no `Supersession_Delta.csv` binding is owed. SCA-003
  consumes already-accepted PRD v2.2 and D-PEC-67/-68 facts; it does not
  override upstream authority.
- **Downstream completion:** PROJECT_SETUP re-pinned all 64
  `_REFERENCES.md`; `D-PEC-69` reconciled the complete
  execution-time-confirmed eleven-contract affected population. These are
  downstream acts and do not alter decomposition truth.
- **Reliance hold:** `PEC-HOLD-001` was released by `D-PEC-70` after
  full-corpus and independent validation. The SCA itself granted no reliance
  or implementation authority.
- **DownstreamRerunState: `COMPLETE`.**
- **ReadyForNextPhase: `OWNER_GATED_WORKING_ITEMS`.**
- **Fallback and authority:** file-native fallback remains operable. Consumer
  use is optional and separately authorized; no receiving-loop duty is
  created.
