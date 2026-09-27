# SCA-APP-012 — dependency-extract results (setup Phase 5.6, FULL_GRAPH)

**Status: run and written.** The registers and indexes of the 8 modified
deliverables and the 16 FULL_GRAPH neighbours are updated. The owner confirmed
the incremental plan on 2026-09-27 (`CHAT_TRANSCRIPTION.md`).

## How it ran

- **Workflow.** Bundled `workflows/dependency-extract/` in `MODE=UPDATE` with
  `STRICTNESS=CONSERVATIVE` and `CONSUMER_CONTEXT=NONE`, one deliverable at a
  time, straight through. WORKING_ITEMS ran it directly, as the workflow
  allows.
- **Decomposition.** SHA-256 `6ac78118…a577`, as amended by SCA-APP-012.
- **Method.** Every existing ACTIVE row was re-checked against its cited current
  source. A row counts as seen only if its quote appears verbatim and not only
  inside a `[RETIRED` clause. Text added to the sources since each register's
  previous extraction was scanned for new explicit cross-deliverable
  relationships:
  - for the eight modified deliverables, the accepted SCA-APP-012 scope text
    (previous extraction 2026-09-27, the SCA-APP-011 run);
  - for DEL-05-03, DEL-06-01, DEL-06-02 and DEL-09-04, which the SCA-APP-011
    run did not cover, the 2026-09-23 retired-status clauses (previous
    extraction 2026-09-22);
  - the other twelve neighbours have no source change since the SCA-APP-011
    run.

  Unchanged source text gives the rows already recorded.
- **Tools and evidence.** Row decisions that need judgment are explicit data
  in `dep_extract/apply_dependency_extract.py`; every other ACTIVE row had to
  be re-seen or the run would stop. Function 4 is
  `dep_extract/refresh_dependency_indexes.py`, and Function 5 is
  `dep_extract/function5_checks.py`. The per-deliverable actions, source hashes
  and pre-images are in `dep_extract/EXTRACTION_LOG.json`.
- **Write boundary.** Only `Dependencies.csv` and `_DEPENDENCIES.md` of the 24
  deliverables were written. Each deliverable's `ScopeOfWork.md`,
  `_CONTEXT.md`, `_REFERENCES.md` and `_STATUS.md` hash is the same before and
  after.

## Result

Of the 315 ACTIVE rows, 310 were re-seen and got `LastSeen=2026-09-27`. 266
of them already carried that date from the SCA-APP-011 run, so their bytes are
unchanged; the other 44 are the rows of DEL-05-03 (13), DEL-06-01 (11),
DEL-06-02 (11) and DEL-09-04 (9). The five rows not counted above, plus DX-04,
are below. Arrows in this table are in register direction (owning
deliverable → target); line-level production-direction edges appear under the
closure section.

| Action | Rows | Expected outcome |
|---|---|---|
| Retired | DEP-02-03-009 (DEL-02-03 → DEL-08-03) | DX-01 (group 1 R-b) |
| Retired | DEP-02-03-008 (DEL-02-03 → DEL-07-05), confirmed by the owner | DX-07 |
| Re-evidenced in place | DEP-02-03-004 (→ REF-003): quote from the restated CLM-003 row, line 63 | DX-02 |
| Re-evidenced in place | DEP-02-03-007 (DEL-02-03 → DEL-07-04): quote from the restated DEL-02-03-REQ-010, line 153; Statement without the transition-control wording | DX-06 |
| Restated in place | DEP-08-03-007 (→ REF-003): `TargetName` "docs/SPEC.md Section 17.2 deliverable scan API" | DX-03 |
| Unchanged | DEP-08-02-013 | DX-04 does not apply (P-keep) |

- **Retired rows** follow the registers' convention: `Status=RETIRED`,
  `SatisfactionStatus=NOT_APPLICABLE`, the ID kept, no row deleted, and the
  prior values with the SCA-APP-012 basis in `Notes`. DEP-02-03-008's `Notes`
  quote the owner's act verbatim.
- **Registers whose `Dependencies.csv` changed:** DEL-02-03 (four rows),
  DEL-08-03 (one row), and DEL-05-03, DEL-06-01, DEL-06-02 and DEL-09-04
  (`LastSeen` only). The other 18 registers are byte-identical. No register
  changed beyond `LastSeen` outside the DX rows, as expected.
- **Added:** none. The new-text scan found no new explicit relationship:
  - DEL-02-03's controlling section cites DEL-08-03-REQ-010 for the scan
    surface and says no summary widget routes to a dispatch intent; it names
    no dependency.
  - DEL-07-02's bullet naming DEL-06-03 for the scaffold preview is marked
    `[RETIRED — SCA-APP-012]` and states ownership.
  - DEL-02-01 keeps the route/query question with DEL-08-02, unchanged
    (DEP-02-01-006 and DEP-08-02-013, P-keep).
  - **Observation (not a row):** DEL-09-04's 2026-09-23 clause APP-R078 says
    "Preserve source artwork and the renderer removal direction with
    DEL-02-01". It states no direction, and the relationship is already
    recorded from the supplier side as DEP-02-01-013 (DEL-02-01 → DEL-09-04).
    Under CONSERVATIVE no DEL-09-04 row is emitted; the DEL-09-04 index notes
    it for the register owner.
- **Integrity:** no row was deleted, and every existing `DependencyID` was kept.
- **Indexes.** Each `_DEPENDENCIES.md` is refreshed under the headings the file
  already uses (Function 4):
  - one current register section, under the file's existing
    `## Extracted Dependency Register` or `## Current Extracted Dependency
    Summary — <date>` heading; where a file carries both, the dated summary
    already points to the canonical section and is left as it is;
  - this run's notes are a `###` subsection of the existing `## Run Notes`;
  - one Run History entry each;
  - human-owned sections are byte-identical to the pre-image.
- **DEL-08-03.** The current run notes do not report the 2026-09-05
  source-endpoint label conflict: the SOW no longer names the retired scope
  route (DX-03).
- **Function 5** (`dep_extract/FUNCTION5_CHECKS.json`):
  - schema PASS for 24 of 24;
  - IDs unique;
  - exactly one ACTIVE parent anchor in each register;
  - every enum value written VALID;
  - ID format PASS for every ID;
  - index counts match the CSVs.
- **EVQ/DRB check** (report-only): EVQ-006 only, 84 rows project-wide,
  unchanged. The current validator does not resolve the repository-relative
  `projects/chirality-app-dev/...` `EvidenceFile` form some App rows use. This
  run changed no `EvidenceFile`, and no row whose evidence fields this run
  changed carries the finding (two `LastSeen`-only rows, DEP-05-03-001 and
  DEP-06-01-001, carry the pre-existing finding). There is no EVQ-003, EVQ-004
  or DRB-006 finding.
- **Graph after extraction** (analyzer, SCOPE ALL): 54 nodes, 102 edges,
  0 SCC, 0 orphans, 7 isolates (the same seven as before).
  - DEP-02-03-009 and DEP-02-03-008 each removed one distinct edge
    (DEL-02-03 → DEL-08-03 and DEL-07-05 → DEL-02-03, in production
    direction); DX-02, DX-03 and DX-06 changed no edge.
  - Closure snapshot:
    `execution/_Evaluation/DepClosure/CLOSURE_SCA_APP_012_POST_EXTRACTION_2026-09-27_2234/`.

## Expected outcomes DX-01 to DX-07

Each outcome's recorded check in `DEPENDENCY_EXTRACT_EXPECTED_OUTCOMES.csv` is
evaluated against the extracted rows by the post-setup `audit-scope-closure`
(`DX_Verification.csv` in its snapshot). DX-04 does not apply and is checked as
"unchanged apart from `LastSeen`".
