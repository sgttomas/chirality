## Verifier-driven reading for R3 (not applied to the sealed figures above)

- `DEL-00-02#CLM-014.2` Disposition is REFUTED. The sealed value is `UNKNOWN`; the verifier reads `ALIGNED`, or `PARTIALLY_IMPLEMENTED` as the alternative.
  - This is a verdict field, so it is not in `CORRECTIONS.csv` and is not applied above.
  - It is 1 of 15 checked rows (6.7%), which is below the Addendum 3 rerun threshold, so there was no rerun.
- `DEL-00-01#CLM-018.2` is CONTESTED: `DOCUMENTED_UNIMPLEMENTED` or `UNKNOWN`.
- See `VERIFICATION.md` §3.

## Coverage gaps (no forward row any worker could own)

Both workers reported the same gap independently: the **package-level PKG-00 control surfaces** have no indexed claim units. Neither ledger audits them. They are cited only as evidence, apart from DEL-00-02 `STATE-3`, which covers only DEL-00-02's own readiness row. The DEL-00-01 worker reports all four records below as stale at the frozen basis:

1. `1_Working/CONTROL_REGISTER.csv` **PKG-00-CTRL-004** (`CURRENT_DEPCLOSURE_SNAPSHOT`) still names `CLOSURE_SCC_SAFE_MOVES_001_2026-06-16_0325Z` as current. It was moved neither for D53A (D-APP-56/68) nor for the 1034 snapshot (D-APP-111).
2. **PKG-00-CTRL-005 and CTRL-006**, together with the readiness table in `DAG_CLOSURE_CONTROL.md` (lines 33–36), record both deliverables as `SEMANTIC_READY`. `_STATUS.md` says `IN_PROGRESS` (D-APP-54).
3. The **PKG-00 `README.md`** §Current Readiness (lines 23–27) says both deliverables are `SEMANTIC_READY` and that the work "does not make the strict product graph acyclic". Both statements are now false.
4. **`DAG_CLOSURE_CONTROL.md:64`** (Current Queue) says to "proceed with the D-APP-19 inspection queue", a convention D-APP-54 superseded.

DEL-00-02 also cites `scc-cases/CASE-SCC-001_*` and three `scope-change-packets/` as history, without auditing them unit by unit, because the index has no units for them.

## Cross-package observations for R3 (evidence, not rulings)

1. **The stale DepClosure pointer is a corpus-level carrier gap.**
   - D-APP-111 moved `_Reconciliation/DepClosure/_LATEST.md` to `CLOSURE_SCC-DECOMPOSE-SCA-APP-010_2026-09-05_1034`. D-APP-114 repointed only `DAG_CLOSURE_CONTROL.md`.
   - Neither ruling names DEL-00-01 or DEL-00-02, so MR-11 was not applied and the stale text is `STALE_SPECIFICATION`.
   - The stale text is in both deliverables' SoW, `_REFERENCES.md` and `CONTROL.md`, and in `CONTROL_REGISTER.csv`.
   - Other packages whose `_REFERENCES.md` or SoW names a "current" DepClosure snapshot probably show the same pattern. R3 can cluster them under one repair.
   - This bears on RUN_BASIS §5's known basis defect: the 1034 snapshot says the pointer was not moved, but the pointer was moved later.
2. **SoW-conversion parity claims (AC-001 and VER-001, D-APP-68 / Root D-GOV-16) have no consistent disposition.**
   - Within this package, the four rows split three ways: ALIGNED, UNKNOWN (refuted to ALIGNED) and DOCUMENTED_UNIMPLEMENTED / PARTIALLY_IMPLEMENTED.
   - The preservation half can be checked inside the roots with read-only `git show` of the pre-migration files.
   - The parity-record half would sit in Root D-GOV-16 tooling, outside the evidence roots.
   - Every migrated deliverable probably carries the same AC and VER items, so R3 may want one clustered rule.
3. **The package is outside the v3 re-platform.**
   - The package has no code surface: there are 0 REACH tags and 0 R4-Qn citations, PostReleaseBasis is NO throughout, and the reverse passes answered 450 capability rows `NOT_MINE`.
   - D-APP-127 and D-GOV-43 are absent from every carrier (pack item 5: all `NO`). No row cites either as governing, and no CauseTag names a v3 mechanism.
   - The divergences are DOC_HYGIENE, CARRIER_PROPAGATION and PRE_V3_DRIFT, not the v3 mechanisms.
4. **Method friction for control packages.**
   - The reverse-pass area selection comes from HINTS token hits. For a code-free control deliverable those hits are noise: 117 BUILD hits for DEL-00-01 came from generic tokens such as "Boundary". The selection produced 261 and 189 capability rows, all of them `NOT_MINE`.
   - The strict roots exclude the PKG-10 `Dependencies.csv` registers that DEL-00-01 treats as its own source registers. The worker used in-root proxies: snapshot `edge_list.csv`, `coverage.csv` and the R6 backcheck. The verifier judged these sound.
   - The DEL-00-01 worker proposes read-only access to the specific foreign register rows that a control deliverable names.
