# TASK RUN — D-PEC-65 register evidence repair (DEL-04-01)

| Field | Value |
|---|---|
| Instrument | `D-PEC-65_register_evidence_repair.md` (RULED 2026-07-25, §3.1) |
| Actor | sealed ephemeral Agent 2 (file-tool-only), `TASK-repair/D-PEC-65` |
| Date | 2026-07-25 |
| Package | PKG-04 Orientation Services |
| File touched | `Dependencies.csv` |
| Rows in file | 5 (2 ANCHOR read-only + 3 EXECUTION) |

## Row dispositions

| DependencyID | Defect class | Disposition | EvidenceFile after |
|---|---|---|---|
| DEP-04-01-003 | EVQ-001 duplication (quote-shaped text in both cells; the duplicated value also embedded a quoted span and an ellipsis) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |
| DEP-04-01-004 | EVQ-001 duplication (locus-shaped text in both cells) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |
| DEP-04-01-005 | EVQ-003/EVQ-004 empty quote with `SourceRef` = `location TBD` | REPAIRED (real evidence found; no waiver) | `docs/PRD.md` |

## Cells changed

**DEP-04-01-003** (E-A27, DEL-10-01 → DEL-04-01, SEQUENCING)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: (duplicated quote text) → `ScopeLedger.csv row SOW-058 Notes column`
- `EvidenceQuote`: (duplicated, elided) → `Sequencing obligation, pre-P1; baselines SOW-004/041`
- Aptness: SOW-058 is DEL-10-01's covered scope item; its Notes cell declares the pre-P1 sequencing obligation and names SOW-004 (DEL-04-01's covered item) as what it baselines.

**DEP-04-01-004** (E-P11, DEL-01-01 → DEL-04-01, CONSUMES)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `DEL-01-01 envelope note (as E-P10)` → `Deliverables.csv row DEL-01-01 ContextEnvelopeNotes column`
- `EvidenceQuote`: (duplicate of the above) → `the schema every derivation package depends on`
- Aptness: PKG-04 is the orientation *derivation* package (`SOFTWARE_DECOMP.md` §4); DEL-01-01's own envelope note declares it the dependency of every derivation package.

**DEP-04-01-005** (E-P32, DEL-03-01 → DEL-04-01, CONSUMES)
- `EvidenceFile`: PLAN exhibit → `docs/PRD.md`
- `SourceRef`: `location TBD` → `PRD.md §6 invariant PEC-K-07`
- `EvidenceQuote`: (empty) → `the reconciler over file truth is the source of every record-tier fact`
- Aptness: the Statement claims orientation derives from a populated record tier; PEC-K-07 makes the reconciler (DEL-03-01) the sole source of every record-tier fact.

## Statement edits

None in this deliverable. All three seeded `Statement` cells carry the exhibit
`Rationale` but state the dependency claim without misstating it, so the §3.1
edit condition was not met.

## Waivers declared

None. Every row was repaired against accepted live truth; no
`Dependencies_EvidenceWaivers.csv` sidecar was created.

## Integrity

29 columns preserved; no rows added, deleted, or reordered; ANCHOR rows
untouched; no repaired `SourceRef` contains a quoted span (EVQ-002 clean).
Every repaired quote is a single-line contiguous verbatim span of its cited
file.
