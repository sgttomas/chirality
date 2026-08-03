# Latest — revision pointer and handoff state

Latest: `execution/_Decomposition/SOFTWARE_DECOMP.md` **revision 1.4**
(**`current_basis`** — accepted 2026-08-03 as the SCA-004 successor under
D-PEC-78 O-A and the owner's SCA-004 Gate 5 execution direction).

## Handoff state

- **Basis:** accepted PRD v2.2; D-PEC-60 SOFTWARE_DECOMP revision 1.0;
  SCA-001 directed bootstrap; SCA-002 objective mapping; SCA-003 consumer
  interface/ADR-014 concordance; SCA-004 loop-registry disposition.
- **Package:** `SOFTWARE_DECOMP.md` revision 1.4 + `ScopeLedger.csv` (94 rows)
  + `Deliverables.csv` (64 rows) + unchanged `ContextBudgetQA.csv` (64 rows)
  + unchanged `Companion_Inventory.csv`.
- **Basis integrity:** decomposition SHA-256
  `7cca5cdbb1ba4bd866391abf00998bc80f587a23505a6f5b6bceb8df48b65c81`;
  Scope Ledger SHA-256
  `2103afa279bc7df8e75f830326462d7575cf69a403ee7ef07880e0e9fe969e25`;
  Deliverables SHA-256
  `49f904488a7402e2124359b59b2fc0df9103bef39ee53a5ce8b74f7dc6cc6b72`.
- **Semantic result:** SOW-077 is `IN` and maps reciprocally to
  `PKG-01 → DEL-01-06 → OBJ-004`; SOW-094 carries the settled D-PEC-78
  implementation basis; OI-003 is retained and resolved. Counts are 94 scope
  items (`72 IN / 14 OUT / 8 TBD`), 11 packages, 64 deliverables, six
  objectives, and 10 open / 3 resolved issues.
- **Closure verdict:** `CLOSED_FOR_SCOPE_CHANGE_ONLY`.
- **Audit:**
  `_Evaluation/DecompCoverage/COV_SCA004_POSTCHANGE_2026-08-03_1442/`;
  `WARNINGS`, 0 blockers / 1 unchanged unrelated DEL-08-02 warning / 69 info.
- **Scope-change snapshot:**
  `_ScopeChange/SCA-004_2026-08-02_2325/`.
- **Derivative state:** `INCOMPLETE`; `DownstreamRerunState = FROZEN`;
  `MetadataAlignmentState = NOT_STARTED`; `ReadyForNextPhase = NO`.
- **Stale populations:** 63 context provenance blocks; 64 reference packets;
  DEL-01-06 requirement anchor; four SOW contracts (DEL-01-06, DEL-02-07,
  DEL-03-01, DEL-04-01); DEL-00-03 accepted SPEC; and four ordinary PEC
  orientation/map surfaces. Exact owners and rerun obligations are in the
  SCA-004 `Handoff_State.md`.
- **Authority fence:** no downstream repair, source, lifecycle, artifact
  acceptance, release, professional reliance, or foreign-loop duty is
  implied by this pointer.
