# PKG-01 Scoped Concordance Notes — SCOPED_CONCORDANCE_2026-07-19 (instance G1)

- **Basis:** prior ledger `MANIFESTS/PKG-01_claims.csv` (89 rows, R2 W5) re-adjudicated against the live tree at HEAD `ff2f68c82`; drift window R6 basis `c313325b7` → HEAD.

## Counts

- In-scope selected: **89 / 89** prior rows (reason (a): every deliverable folder in the package manifest changed — the 2026-07-13 ScopeOfWork-v1 migration deleted the four-doc kits and created `ScopeOfWork.md` for all four deliverables; DEL-01-01 additionally received the seven D-APP-65-disposition-4 artifacts and a run record; reason (b) additionally applies to rows resting on `docs/harness/reliance_boundary_register.md`, the authority corpus docs, `frontend/package.json`, `persona-manager.ts`, `sdk-options-builder.ts`, `permission-overlay.ts` and other shared-manifest surfaces; reason (c) to rows the D-APP-56/D-APP-65 register records materially bear on).
- Confirmed (same disposition, DriftClass NONE): 49
- Confirmed ALIGNED with prior open item now closed (DriftClass RESOLVED, no disposition change): 6 (REQ-011, ACC-04, the four REMAINING-1 rows)
- Re-dispositioned: **32** (DEL-01-01: 6 — REQ-006/009/010, ACC-001/002, REGISTER-1; DEL-01-02: 17 — RBR-001/002/003/005/006/007/014/019/020/021/022/023/024/025, ACC-001/002, REGISTER-1; DEL-01-03: 5 — EXC-02, ACC-01/02/03, REGISTER-1; DEL-01-04: 4 — EXC-002, ACC-002/003/004). Every one is prior-drift-now-repaired → ALIGNED.
- Same-disposition PERSISTING: 2 (DEL-01-03-ACC-05 release-review record still absent, human-gated; DEL-01-04-ACC-001 narrowed to CLM-017 step 9)
- New rows: **5** (DEL-01-01-SCOPED-S01/S02; DEL-01-02-SCOPED-S01; DEL-01-03-SCOPED-S01; DEL-01-04-SCOPED-S01)

## Selection reasoning

The window contains three drift drivers for this package: (1) the 2026-07-13 SoW-v1 kit migration (all four deliverables); (2) the D-APP-65 accepted-recommendations tranche (DEL-01-01 artifacts + ResponsibleParty assignments); (3) shared-surface evolution (authority corpus v6→v9, reliance register updates, harness-contract/frontend refactors). All 89 rows are therefore in scope; adjudication traced each claim's substance into the migrated CLM cells and the live enforcement surfaces.

## Key findings

1. **The R5/R6 repair program held.** All 32 re-dispositioned rows are prior drift now verified repaired at HEAD (path refreshes, version-neutral corpus wording, lifecycle read-from-`_STATUS`, INSP-03 append-only supersessions UPD-085/086, P45 annotations UPD-100..104, CT-001 ruling, BR-005 rewrite, BR-006 addition, REF-007 repo-relative repair, DEP-01-03-011 note cleanup).
2. **New drift is concentrated in one class:** the SoW-v1 migration deleted `Datasheet.md`/`Specification.md`/`Guidance.md`/`Procedure.md` but carried over (a) verification/records cells asserting those files exist, and (b) `Dependencies.csv` `EvidenceFile`/`SourceRef` citations to them. Receipt-68 established the dated-migration-note repair pattern but applied it only to DEL-04-01's rows and mirrors. One SCOPED-S row per deliverable records this.
3. **D-APP-65 partial in-place updates** left internal contradictions in DEL-01-01 (`ResponsibleParty remains TBD` cells vs the recorded assignment; CLM-012 filename TBD vs resolved R004) — DEL-01-01-SCOPED-S02.
4. **DEL-01-04 CLM-017 step 9** still flatly asserts lifecycle CHECKING — the one surviving instance of the run-wide CHECKING-wording class in this package (ACC-001 PERSISTING).
5. **DEL-01-03-ACC-05** (no completed release copy review record) persists behind the human gate; DEL-01-03's ResponsibleParty remains TBD (not covered by the D-APP-65 three-field assignment).

## Human-decision rationale (HDN=YES rows)

Single underlying question, same as PKG-00: whether SoW-v1 CLM-quoted legacy text is a live normative surface (drift; repair-shaped) or preserved historical quotation under the SoW files' AC-001 preservation clause (no repair implied; convention note instead). In-place edits already applied inside CLM blocks (D-APP-65 assignment, RULED cells, P45 annotations) argue "live"; the preservation AC argues "quotation". Coded STALE_SPECIFICATION per MR-8 pending the owner's convention ruling. Applies to the four SCOPED-S01 rows, DEL-01-01-SCOPED-S01, and DEL-01-04-ACC-001.

## Ambiguities / limitations

- Tool fence: no Bash/Grep/Glob were available in this session (only Read/Write). Consequences: no hash recomputation (reference MATCH statuses taken as recorded), no repo-wide copy/absence greps (prior fac46e33f sweeps stand for REQ-02/REQ-05/REQ-005-class absence claims, cross-checked by reviewing the drift manifest for surfaces that could plausibly introduce such copy), and no test execution (behavioral rows rest on targeted live source reads plus the merged-PR gate discipline at HEAD).
- DEL-01-03's INSP-03 assessment annotation (ACC-01) was not re-read directly; RESOLVED rests on the R5 P43 class execution and the R6 255/255 backcheck record.
- `document-view.tsx` (changed, UI surface) was not line-audited for copy; no signal in the manifest suggests identity/approval copy changes.
- Minor residues noted but not minted as rows: DEL-01-02 CLM-007 line 114 keep-TBD condition wording; DEL-01-03 CLM-016 line 256 doubled-phrase typo.

## Not examined

Out-of-scope bulk stands on R3/R6. Not re-opened: `docs/BOUNDARY_REVIEW_CHECKLISTS.md` internals (unchanged in window), `pipeline-surface.tsx`/`permission-requests.tsx`/`layout.tsx`/`shell-frame.tsx` (unchanged), `domain-proposal-tools.ts`/`pec-bridge-client.ts` (unchanged), the D53A snapshot internals, and the full 16-ID Section 9 manifest contents (register test index taken at face value at HEAD).
