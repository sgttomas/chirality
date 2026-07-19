# PKG-00 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (instance G1)

- **Basis:** prior ledger `MANIFESTS/PKG-00_claims.csv` (27 rows, R2 W7) re-adjudicated against the live tree at HEAD `ff2f68c82`; drift window R6 basis `c313325b7` → HEAD.

## Counts

- In-scope selected: **27 / 27** prior rows (reason (a): every DEL-00-01 and DEL-00-02 kit file in the package manifest changed in the window — the 2026-07-13 ScopeOfWork-v1 migration deleted `Datasheet.md`/`Guidance.md`/`Procedure.md`/`Specification.md` and created `ScopeOfWork.md`, plus `_STATUS.md` edits and the D-APP-65 assignment).
- Confirmed (same disposition, DriftClass NONE): 12
- Confirmed with drift RESOLVED (disposition unchanged ALIGNED, prior open item closed): 3 (REMAINING rows, DEL-00-02 REMAINING-1)
- Re-dispositioned: **7** (DEL-00-01 REQ-003, ACC-001, REGISTER-1; DEL-00-02 REQ-005, REQ-010, ACC-001, REGISTER-1 — all prior-drift-repaired → ALIGNED)
- Same-disposition PERSISTING (narrowed residue): 2 (DEL-00-01 REQ-001, DEL-00-02 REQ-002)
- New rows: **1** (DEL-00-02-SCOPED-S01)

## Selection reasoning

All 27 rows selected under scope rule (a). Additionally rule (c) applies to DEL-00-02 REMAINING-1 (D-APP-65 register row / ruling record materially bears on it).

## Key findings

1. **The four-doc kits no longer exist.** Both PKG-00 deliverables' `Datasheet.md`, `Guidance.md`, `Procedure.md`, `Specification.md` were deleted by the 2026-07-13 "ScopeOfWork-v1 migrations" (named in loop Receipt-68's Stale-Map-Delta) and replaced by a single `ScopeOfWork.md` (`schema: chirality-deliverable-sow/v1`) quoting the legacy content as CLM-nnn blocks. Every prior claim's NormativeSource line anchor is therefore stale as a pointer; claim substance was traced into the corresponding CLM cells.
2. **Superseded-snapshot pointer class persists in migrated Procedure text.** R5 (UPD-081/082/083) repaired the surfaces named in the R2 repair proposals (Spec/Datasheet/README/`_REFERENCES.md`/`DAG_CLOSURE_CONTROL.md`), but the Procedure-derived CLM cells carried into `ScopeOfWork.md` still call `CLOSURE_SCC_SAFE_MOVES_001` the current accepted snapshot (DEL-00-01 CLM-015/CLM-016; DEL-00-02 CLM-005/CLM-017). Coded as PERSISTING on DEL-00-01-REQ-001 and DEL-00-02-REQ-002.
3. **D-APP-65 discharged the owner-gated ResponsibleParty item for DEL-00-02** (assignment to Ryan Tufts, demonstrator scope), but the in-place update is partial: CLM-006 A-001 and CLM-028 still assert TBD (new row DEL-00-02-SCOPED-S01).

## Human-decision rationale (HDN=YES rows)

One underlying question covers all YES rows in this package: **is the quoted legacy text inside SoW-v1 CLM blocks a live normative surface (drift to repair) or preserved historical quotation (no repair implied)?** The SoW files' AC-001 declares legacy-content preservation, yet in-place edits (D-APP-65 assignment, D53A rewording, RULED cells) show the project also maintains these blocks as live. Until the owner states the convention, flatly-false quoted cells are coded STALE_SPECIFICATION per MR-8 with HDN=YES.

## Ambiguities / limitations

- No `Bash`/`Grep`/`Glob` tooling was available; discovery was by direct file reads. Hash recomputation (shasum) was not possible; reference MATCH statuses were taken as recorded (RUN-INSPECTION documentary basis).
- The authorizing record for the 2026-07-13 SoW-v1 migration itself was not located in the decision register (D-APP-57..67 do not name it); Receipt-68 references "the 2026-07-13 ScopeOfWork-v1 migrations" as accepted fact. Surface for owner awareness, not a fence finding.
- DEL-00-01/DEL-00-02 INSP-03 assessment files were not re-read this run; UPD-084/annotation execution is evidenced by `_STATUS.md`/`MEMORY.md` history lines and the R6 255/255 backcheck.

## Not examined

Out-of-scope bulk stands on R3/R6: DepClosure snapshot internals (D53A, SAFE_MOVES) were not re-opened (unchanged in window); PKG-10 owning registers (DEP-10-02-004 / DEP-10-03-006) were not re-read (not in any drift manifest); the SCC-001 case-folder archive was not re-inventoried.
