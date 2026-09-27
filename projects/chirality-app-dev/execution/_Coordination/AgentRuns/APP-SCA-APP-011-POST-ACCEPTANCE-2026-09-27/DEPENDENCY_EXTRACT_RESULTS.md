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
  in `dep_extract/apply_dependency_extract.py` and, for the ESR-1 follow-up,
  `dep_extract/apply_esr1_reevidence.py`. Function 4 is
  `dep_extract/refresh_dependency_indexes.py`, and Function 5 is
  `dep_extract/function5_checks.py`. The per-deliverable actions, source hashes
  and pre-images are in `dep_extract/EXTRACTION_LOG.json`.
- **Write boundary.** Only `Dependencies.csv` and `_DEPENDENCIES.md` of the 25
  deliverables were written. Each deliverable's `ScopeOfWork.md`,
  `_CONTEXT.md`, `_REFERENCES.md` and `_STATUS.md` hash is the same before and
  after.

## Result

Of the 337 ACTIVE rows, 311 were re-seen and got `LastSeen=2026-09-27`. The
rest are below. The table includes the ESR-1 follow-up made after independent
review of `0ca5ffcca..1d5909491`.

| Action | Rows |
|---|---|
| Retired | DEP-02-02-005, 006, 007, 008, 009 (DX-01 to DX-05); DEP-02-01-007 (DX-06); DEP-02-01-008 (DX-07, owner's HGD-2 ruling); DEP-02-02-021, DEP-02-04-015, DEP-02-04-016, DEP-02-01-014 (owner's ESR-1 ruling) |
| Restated in place | DEP-07-05-025 (DX-08 to DX-10); DEP-08-03-010 (DX-11, DX-12); DEP-08-02-003 (DX-13); DEP-08-02-005 (DX-14); DEP-07-05-015 and DEP-02-01-013 (beyond DX, below) |
| Re-evidenced in place (ESR-1) | DEP-02-02-022; DEP-02-04-017, 018, 019; DEP-07-01-010; DEP-08-01-018, 019; DEP-08-04-013 |
| Kept, with the tension noted | DEP-02-03-009 (DX-15) |
| Added | DEP-07-04-009 (beyond DX, below) |

- **Registers with no change beyond `LastSeen`:** DEL-03-03, DEL-07-02,
  DEL-09-03, DEL-02-05, DEL-03-02, DEL-03-04, DEL-04-04, DEL-05-02, DEL-05-04,
  DEL-06-03, DEL-06-04, DEL-07-03, DEL-08-05 and DEL-09-02.
- **Integrity:** no row was deleted, and every existing `DependencyID` was kept.
- **Indexes.** Each `_DEPENDENCIES.md` is refreshed under the headings the file
  already uses (Function 4):
  - one current register section, under the file's existing
    `## Extracted Dependency Register` or `## Current Extracted Dependency
    Summary — <date>` heading;
  - in DEL-02-02 and DEL-03-02, which carried both, the dated summary points to
    the canonical section;
  - this run's notes are a `###` subsection of the existing `## Run Notes`;
  - human-owned sections are byte-identical to the pre-image.
- **Function 5** (`dep_extract/FUNCTION5_CHECKS.json`):
  - schema PASS for 25 of 25;
  - IDs unique;
  - exactly one ACTIVE parent anchor in each register;
  - every enum value written VALID;
  - ID format PASS for every ID;
  - index counts match the CSVs.
- **EVQ/DRB check** (report-only): EVQ-006 only, 644 rows project-wide.
  - Before this run the count was 651. The added row DEP-07-04-009 made it
    652, because it follows the registers' usual form.
  - The eight ESR-1 rows now cite project-relative paths that resolve, which
    brings it to 644.
  - 19 of the rows this run changed still carry the finding.
  - The validator resolves `EvidenceFile` from the project root, which almost
    no App register row does, so this is a pre-existing convention finding.
  - There is no EVQ-003, EVQ-004 or DRB-006 finding.
- **Graph after extraction** (analyzer): 54 nodes, 107 edges, 0 SCC, 0 orphans.
  - The retired rows remove five distinct edges, and DEP-07-04-009 adds
    DEL-07-04 → DEL-06-03.
  - The ESR-1 re-evidence changed no edge.
  - The owner's ESR-1 ruling removes four more edges, leaving 103 edges and
    0 SCC (closure snapshot `CLOSURE_SCA_APP_011_ESR1_RULING_2026-09-27_1739`).

## Outcomes beyond the confirmed expected outcomes (DX-01 to DX-16)

1. **DEP-07-05-015 restated.** This trace anchor to REQ-DEL-07-05-013 quoted
   "API surface MUST support GET/PUT", which is no longer in the source.
   SCA-APP-011 restated REQ-013 to the dependency library (CLM-012, line 218).
   The anchor is kept, and its label, statement and quote follow the restated
   requirement. Neither retired-surface screen caught it; the re-seen check
   did.
2. **DEP-07-04-009 added.** DEL-07-04 → DEL-06-03, DOWNSTREAM INTERFACE. The
   text SCA-APP-011 added to DEL-07-04 (line 22) says live exposure of
   `status_read`, which wraps the status library, "is DEL-06-03's open work".
   The consumer is named explicitly. The parallel DEL-07-05 edge already
   exists as DEP-06-03-007. No cycle.
3. **DEP-02-01-013 re-evidenced.** Its former source was retired on
   2026-09-23. Its receiving clause APP-R016 (DEL-02-01 SOW line 373) states
   the same handoff to DEL-09-04.
4. **DEP-08-02-003 `TargetName`** is the name "Active dialogue/persona and
   right-panel session views". The Statement carries the SOW-006 description.

## ESR-1 — rows whose evidence source was retired on 2026-09-23

### Basis

- **Why the evidence is gone.** Twelve ACTIVE rows cited the former
  `_STATUS.md` `## Remaining` sections. The owner-directed finite Task
  Management account of 2026-09-23 retired those sections into APP-Rnnn
  receiving clauses.
- **The instrument preserved the rows.**
  - Its closeout (`_TaskManagement/APP_REMAINING_RETIREMENT_2026-09-22/FINAL_CLOSEOUT.md`)
    says "the accepted `Dependencies.csv` rows and source quotes remain
    unchanged".
  - The 2026-09-23 current-source note at the top of each affected
    `_DEPENDENCIES.md` says: "For current work and dependency gating, read
    `Dependencies.csv` … The historical Depends text adds no prerequisite;
    this note does not change the accepted register rows."
  - The note makes the register rows, not the retired Depends text, the gating
    authority. That is how the rows survive.
- **Correction.** An earlier version of this record attributed "adds no
  prerequisite" to the closeout and used it to support retiring the rows. The
  phrase is from the current-source note, and it supports keeping them. It is
  no longer used as support for retirement.
- **Why the rows were not retired.** The workflow's own default for an unseen
  row is to retire it. The rows are held because the accepted owner-directed
  2026-09-23 instrument explicitly preserved them, and that instrument takes
  precedence.
- **What the extraction then did.** Re-anchoring a preserved row's evidence to
  a current source is ordinary UPDATE-mode work, and it changes no edge. So
  each row was re-evidenced wherever a current source states its dependency.
  The sources checked were:
  - the SOWs, including the "Remaining items seated under D-APP-108" lines;
  - the decomposition;
  - the D-APP-109 and D-APP-110 ruling records;
  - the APP-Rnnn receiving clauses.

  Each new `EvidenceQuote` is a verbatim single-line substring of its source,
  and the warning is cleared on every re-evidenced row.

### Per-row outcome

| Row | Edge | Outcome | Current source |
|---|---|---|---|
| DEP-02-02-022 | DEL-02-02 ← additive v1 contract (DOCUMENT) | Re-evidenced | D-APP-110 ruling, §Ruling as applied item 2, line 52 (SD-003 decompose names the row) |
| DEP-02-04-017 | DEL-02-04 → additive v1 contract (DOCUMENT) | Re-evidenced | D-APP-110 ruling, line 50 |
| DEP-02-04-018 | DEL-02-04 → additive v1 contract (DOCUMENT) | Re-evidenced | D-APP-110 ruling, line 52 |
| DEP-02-04-019 | DEL-02-04 → additive v1 contract (DOCUMENT) | Re-evidenced | D-APP-110 ruling, line 51 |
| DEP-07-01-010 | DEL-07-01 → DEL-04-04 | Re-evidenced, IMPLICIT/MEDIUM | Decomposition Scope Ledger SOW-084, line 492 |
| DEP-08-01-019 | DEL-07-01 → DEL-08-01 | Re-evidenced, IMPLICIT/MEDIUM | Decomposition Scope Ledger SOW-084, line 492 |
| DEP-08-01-018 | DEL-06-03 → DEL-08-01 | Re-evidenced, IMPLICIT/MEDIUM | Decomposition Scope Ledger SOW-082, line 490 |
| DEP-08-04-013 | DEL-03-02 → DEL-08-04 | Re-evidenced, IMPLICIT/MEDIUM | Decomposition Scope Ledger SOW-083, line 491 (also DEL-08-04 SOW acceptance obligation 2) |
| DEP-02-02-021 | DEL-02-03 → DEL-02-02 | Retired (owner ruling) | None. The SOW's seated line names only the item IDs. APP-R022 says DEL-02-03 provides the view switcher, but no source says the Workflows view mounts in it |
| DEP-02-04-015 | DEL-02-02 → DEL-02-04 | Retired (owner ruling) | None. The item gate "not selectable until DEL-02-02-V3-03 landed" is stated nowhere current |
| DEP-02-04-016 | DEL-02-03 → DEL-02-04 | Retired (owner ruling) | None, as for DEP-02-02-021 (Activity view) |
| DEP-02-01-014 | DEL-01-03 → DEL-02-01 | Retired (owner ruling) | None. No current source states the professional-boundary copy constraint on DEL-02-01's copy pass |

**Notes on the re-evidenced rows**
- **D-APP-110 record.** It lies outside the workflow's default read boundary.
  It was read because it is the accepted ruling that names these rows.
- **Ledger-based rows.** Their target comes from the ledger's deliverable
  allocation, not a named Depends line. So Explicitness is IMPLICIT and
  Confidence MEDIUM; the prior values are kept in `Notes`.
- **Integrity.** No edge, target, status or satisfaction changed.

### Owner ruling: the four retire candidates (applied; ESR-1 closed)

Retiring these rows has no gating cost:
- **Blockers do not change.** Each row requires SEMANTIC_READY and each target
  is IN_PROGRESS. DEP-02-02-021, DEP-02-04-015 and DEP-02-04-016 are already
  SATISFIED prerequisites of items that have landed; DEP-02-01-014 is TBD.
- **No cycle can form.** Retiring only removes edges.
- **D-APP-110 structure.** DEP-02-04-015 and 016 were the strict halves of the
  DEL-02-04 bidirectional and mutual pairs. D-APP-110 kept them as strict
  PREREQUISITE edges while decomposing DEP-02-04-018 and 019 to the DOCUMENT
  contract. Retiring them removes the last deliverable edges DEL-02-02 →
  DEL-02-04 and DEL-02-03 → DEL-02-04. The SD-003 decompose itself (the
  DOCUMENT-target rows) is unaffected.
- **Lowest impact.** DEP-02-02-021 removes the last DEL-02-03 → DEL-02-02 edge,
  because DEP-02-02-006 is retired. DEP-02-02-021, DEP-02-04-015 and
  DEP-02-04-016 are already-SATISFIED prerequisites, so they are the lowest
  impact of all.
- **DEP-02-01-014** removes DEL-01-03 → DEL-02-01.

**Owner ruling**, typed in chat on 2026-09-27 (verbatim;
`CHAT_TRANSCRIPTION_ESR-1_2026-09-27.md`):

> ESR-1: retire DEP-02-02-021, DEP-02-04-015, DEP-02-04-016 and DEP-02-01-014.

**Applied** (`dep_extract/apply_esr1_ruling.py`), using the registers'
retired-row convention:
- `Status=RETIRED` and `SatisfactionStatus=NOT_APPLICABLE`;
- the prior value and the ruling, verbatim, in `Notes`;
- the ID kept, no row deleted, and every other field unchanged.

The three affected `_DEPENDENCIES.md` files record ESR-1 as closed. **ESR-1 is
closed.**

## HGD-2 and HGD-3

- **HGD-2 is closed.**
  - DEP-02-01-007 is retired as accepted with SCA-APP-011.
  - DEP-02-01-008 is retired by the owner's ruling, quoted verbatim in its
    `Notes` and in DEL-02-01 `_DEPENDENCIES.md`: at the dated HGD line and in
    Downstream Handoff Notes.
- **HGD-3 is not decided.** Its premise changed: with DEP-02-02-005 and
  DEP-02-01-007 both retired, the four-node SCC it guarded against no longer
  arises. This is noted where HGD-3 is tracked (DEL-02-01 `_DEPENDENCIES.md`).
