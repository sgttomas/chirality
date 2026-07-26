# Latest — revision pointer and handoff state

Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.2**
(**`current_basis`** — accepted 2026-07-25 as the SCA-002 successor under
`D-PEC-64`).

## Handoff state

- **Basis:** D-PEC-60 SOFTWARE_DECOMP revision 1.0 over PRD v2.0, amended by
  SCA-001 (PRD v2.1 directed-bootstrap reconciliation, D-PEC-61) and by
  SCA-002 (deliverable→objective mapping for the Phase 2.2 wave scope,
  D-PEC-64). SCOPE_CHANGE Gates 1–5 were separately owner-confirmed.
- **Package:** working surface + `ScopeLedger.csv` (94 rows) +
  `Deliverables.csv` (64) + `ContextBudgetQA.csv` (unchanged) +
  `Companion_Inventory.csv` (unchanged).
- **Basis integrity (md5, post-amendment):** `SOFTWARE_DECOMP.md`
  961e8e959b7d1965cd1d4153c69a9c43; `Deliverables.csv` 3f807d502df3ed1f35326baed890832a;
  `ScopeLedger.csv` 9ece6f49fb5fc7f83f72fa897d01a325.
- **Closure verdict: `CLOSED_FOR_SCOPE_CHANGE_ONLY`.** Revision 1.2 is the
  accepted decomposition basis. No package, deliverable, objective, scope
  item, product function, stable ID, or dependency edge was added or removed.
- **Verification:** deterministic pre/post register comparison confirms
  topology unchanged (94 scope items — 71 IN / 14 OUT / 9 TBD; 11 packages;
  64 deliverables; 6 objectives; Context Envelope S 28 / M 34 / L 2 / XL 0);
  union invariant 0 violations; exactly 20 ledger rows and 17 deliverable
  rows changed, in the `ObjectiveIDs` / `SupportsObjectives` columns only;
  the 11 residue IN rows and 9 residue deliverables byte-identical.
- **Mapping state:** IN items without objective mapping 31 → 11; deliverables
  without objective mapping 26 → 9. All 32 Phase 2.2 wave members carry a
  non-empty `SupportsObjectives` set.
- **AuditState: `NON_BLOCKING_PASS`.** Pre-change baseline
  `_Evaluation/DecompCoverage/COV_SCA002_PRECHANGE_2026-07-25_1040/`;
  post-change baseline `_Evaluation/DecompCoverage/COV_SCA002_POSTCHANGE_FINAL_2026-07-25_1257/` (final pass;
  interim pass `COV_SCA002_POSTCHANGE_2026-07-25_1252`, superseded). OI-013 remains the durable
  register-validator follow-on.
- **Supersession:** no `Supersession_Delta.csv` binding owed (attributions
  consume PRD anchors; no upstream authority fact is overridden).
  `Supersession_Map.csv` carries SCA-001's accepted rows forward unchanged.
- **Blockers / open issues:** OI-B — all 64 deliverable `_REFERENCES.md` still
  pin "revision 1.1"; that surface is excluded by `D-PEC-64` §3.3 and the
  refresh is a deferred obligation owned by resumed `PROJECT_SETUP`.
  `_CONTEXT.md` basis pointers: refreshed for all 64 at revision 1.2 (Gate 4
  ruling (i), P-supersede variant). OI-001..009 remain the §16 owner
  decisions; OI-012 the core-isolation ADR; OI-013 the validator follow-on.
- **DownstreamRerunState: `FROZEN`** — released, not executed by SCOPE_CHANGE.
- **ReadyForNextPhase: `REGEN_ONLY`.** `PROJECT_SETUP` is the next owner and
  resumes per `D-PEC-64` §2.4: SCA-002 receipt, closure commit, the D-PEC-63
  re-pins (three points + the DAG-exhibit §1 annotation), and the
  `projects/pec/AGENTS.md` pointer refresh.
- **Fallback and authority:** unchanged from revision 1.1 — the full DAG is
  PEC's initial file-native self-ingestion corpus; observed friction may
  generate evidence-linked candidates or amendment requests but changes no
  accepted scope and grants no authority. File-native fallback remains
  operable.
