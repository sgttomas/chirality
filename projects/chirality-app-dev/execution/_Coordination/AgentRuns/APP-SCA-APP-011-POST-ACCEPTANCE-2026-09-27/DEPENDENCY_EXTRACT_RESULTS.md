# SCA-APP-011 — dependency-extract results (setup Phase 5.6, FULL_GRAPH)

**Status: run and written.** The registers and indexes of the 9 modified
deliverables and the 16 FULL_GRAPH neighbours are updated. The owner confirmed
the incremental plan on 2026-09-27 (`CHAT_TRANSCRIPTION.md`).

## How it ran

- **Workflow.** Bundled `workflows/dependency-extract/` in `MODE=UPDATE` with
  `STRICTNESS=CONSERVATIVE` and `CONSUMER_CONTEXT=NONE`, one deliverable at a
  time. WORKING_ITEMS ran it directly, as the workflow allows.
- **Decomposition.** SHA-256 `cf6e56eb…1876`, as amended by SCA-APP-011.
- **Method.** Every existing ACTIVE row was re-checked against its cited current
  source. A row counts as seen only if its quote appears verbatim and not only
  inside a `[RETIRED` clause or a clause SCA-APP-011 declared history. Text
  added to the sources since the previous extraction (2026-09-22) was scanned
  for new explicit cross-deliverable relationships. Unchanged source text gives
  the rows already recorded.
- **Tools and evidence.** Row decisions that need judgment are explicit data
  in `dep_extract/apply_dependency_extract.py`. Function 4 is
  `dep_extract/refresh_dependency_indexes.py`, and Function 5 is
  `dep_extract/function5_checks.py`. The per-deliverable actions, source hashes
  and pre-images are in `dep_extract/EXTRACTION_LOG.json`.
- **Write boundary.** Only `Dependencies.csv` and `_DEPENDENCIES.md` of the 25
  deliverables were written. Each deliverable's `ScopeOfWork.md`,
  `_CONTEXT.md`, `_REFERENCES.md` and `_STATUS.md` hash is the same before and
  after.

## Result

Of the 337 ACTIVE rows, 311 were re-seen and got `LastSeen=2026-09-27`. The
rest:

| Action | Rows |
|---|---|
| Retired | DEP-02-02-005, 006, 007, 008, 009 (DX-01 to DX-05); DEP-02-01-007 (DX-06); DEP-02-01-008 (DX-07, owner's HGD-2 ruling) |
| Restated in place | DEP-07-05-025 (DX-08 to DX-10); DEP-08-03-010 (DX-11, DX-12); DEP-08-02-003 (DX-13); DEP-08-02-005 (DX-14); DEP-07-05-015 and DEP-02-01-013 (beyond DX, below) |
| Kept, with the tension noted | DEP-02-03-009 (DX-15) |
| Added | DEP-07-04-009 (beyond DX, below) |
| Held, `[WARNING] EVIDENCE_SOURCE_RETIRED` | DEP-02-02-021, 022; DEP-07-01-010; DEP-02-01-014; DEP-02-04-015, 016, 017, 018, 019; DEP-08-01-018, 019; DEP-08-04-013 (ESR-1, below) |

- **Registers with no change beyond `LastSeen`:** DEL-03-03, DEL-07-02,
  DEL-09-03, DEL-02-05, DEL-03-02, DEL-03-04, DEL-04-04, DEL-05-02, DEL-05-04,
  DEL-06-03, DEL-06-04, DEL-07-03, DEL-08-05 and DEL-09-02.
- **Integrity:** no row was deleted, and every existing `DependencyID` was kept.
- **Function 5** (`dep_extract/FUNCTION5_CHECKS.json`):
  - schema PASS for 25 of 25;
  - IDs unique;
  - exactly one ACTIVE parent anchor in each register;
  - every enum value written VALID;
  - ID format PASS for every ID (the old PROJECT_ID_FORMAT_PROFILE warning no
    longer reproduces);
  - index counts match the CSVs.
- **EVQ/DRB check** (report-only): EVQ-006 only, 652 rows project-wide, 27 of
  them on rows this run changed. The validator resolves `EvidenceFile` from the
  project root, while every App register cites it deliverable- or
  repository-relative, so this is a pre-existing convention finding. There is
  no EVQ-003, EVQ-004 or DRB-006 finding.
- **Graph after extraction** (analyzer): 54 nodes, 107 edges, 0 SCC, 0
  orphans. There are 4 edges fewer than before. The retired rows remove five
  distinct edges, and DEP-07-04-009 adds DEL-07-04 → DEL-06-03. See the
  closure snapshot for the full audit.

## Outcomes beyond the confirmed expected outcomes (DX-01 to DX-16)

These come from the straight-through method and are recorded here for review:

1. **DEP-07-05-015 restated.** This trace anchor to REQ-DEL-07-05-013 quoted
   "API surface MUST support GET/PUT", which is no longer in the source.
   SCA-APP-011 restated REQ-013 to the dependency library (CLM-012, line 218).
   The anchor is kept, and its label, statement and quote now follow the
   restated requirement. Neither retired-surface screen caught it; the re-seen
   check did.
2. **DEP-07-04-009 added.** DEL-07-04 → DEL-06-03, DOWNSTREAM INTERFACE. The
   text SCA-APP-011 added to DEL-07-04 (line 22) says live exposure of
   `status_read`, which wraps the status library, "is DEL-06-03's open work".
   The consumer is named explicitly, so the conservative method emits the row.
   The parallel DEL-07-05 edge already exists as DEP-06-03-007. The analyzer
   shows no cycle.
3. **DEP-02-01-013 re-evidenced.** Its former source (`_STATUS.md`
   `## Remaining`) was retired on 2026-09-23. The same handoff to DEL-09-04 is
   stated in its receiving clause APP-R016 (DEL-02-01 SOW line 373).
4. **Twelve rows held (ESR-1, below).**

## Owner proposal ESR-1 — twelve rows whose evidence source was retired

**What happened.** Twelve ACTIVE rows in five registers cite the former
`_STATUS.md` `## Remaining` sections. The owner-directed finite Task Management
account of 2026-09-23 retired those sections into APP-Rnnn receiving clauses.
Its closeout says "the accepted Dependencies.csv rows and source quotes remain
unchanged", and the current ScopeOfWork.md text does not restate these
relationships.

**What the workflow alone would do.** Mark the rows unseen, so `RETIRED`.

**Why they were held instead.** Several rows came from owner rulings:
- D-APP-109 emissions: DEP-02-02-022, DEP-02-04-017, DEP-08-01-018,
  DEP-08-04-013.
- D-APP-110 decompose outputs: DEP-02-04-017, 018, 019.

The accepted account preserved them explicitly, and none of this is an
SCA-APP-011 effect. So the run used the workflow's conservative,
non-destructive default:
- each row is kept `ACTIVE` with `LastSeen` unchanged;
- each row's `Notes` and its register's Run Notes carry the warning.

**Graph effect of retiring them.** Eight rows are deliverable edges:
- DEL-02-02 ← DEL-02-03;
- DEL-07-01 → DEL-04-04;
- DEL-02-01 ← DEL-01-03;
- DEL-02-04 ← DEL-02-02;
- DEL-02-04 ← DEL-02-03;
- DEL-08-01 ← DEL-06-03;
- DEL-08-01 ← DEL-07-01;
- DEL-08-04 ← DEL-03-02.

The other four target the DOCUMENT contract DEL-02-04-WORKSPACE_STATE_ADDITIVE_V1.
Retiring rows only removes edges, so no cycle can form.

**Options**
- **(a) Retire all twelve** as unseen. The dependency-extract rule supports
  this.
- **(b) Keep them** as accepted records until their owners restate them in a
  SOW.
- **(c) Decide row by row.**

**Recommended:** (a). The 2026-09-23 closeout already says the historical
Depends text "adds no prerequisite". An owner reply would be "ESR-1: retire the
twelve held rows."

## HGD-2 and HGD-3

- **HGD-2 is closed.**
  - DEP-02-01-007 is retired as accepted with SCA-APP-011.
  - DEP-02-01-008 is retired by the owner's ruling, quoted verbatim in its
    `Notes` and in DEL-02-01 `_DEPENDENCIES.md`: at the dated HGD line and in
    Downstream Handoff Notes.
- **HGD-3 is not decided.** Its premise changed: with DEP-02-02-005 and
  DEP-02-01-007 both retired, the four-node SCC it guarded against no longer
  arises. This is noted where HGD-3 is tracked (DEL-02-01 `_DEPENDENCIES.md`).
