# TASK RUN — D-PEC-65 register evidence repair (DEL-04-05)

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
| DEP-04-05-003 | EVQ-001 duplication (quote-shaped text in both cells, embedded quoted span) | REPAIRED + Statement edit | `execution/_Decomposition/ScopeLedger.csv` |
| DEP-04-05-004 | EVQ-001 duplication (quote-shaped text in both cells, embedded quoted span) | REPAIRED + Statement edit | `docs/PRD.md` |
| DEP-04-05-005 | EVQ-003/EVQ-004 empty quote with `SourceRef` = `location TBD` | REPAIRED (real evidence found; no waiver) | `docs/PRD.md` |

## Cells changed

**DEP-04-05-003** (E-N03, DEL-02-03 → DEL-04-05, CONSUMES, DECLARED/EXPLICIT)
- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: (duplicated quote text) → `ScopeLedger.csv row SOW-013 Notes column`
- `EvidenceQuote`: (duplicate of the above) → `Per-loop coverage limits stated (SOW-009)`
- `Statement`: **EDITED — see below**
- Aptness: SOW-013 is DEL-02-03's covered scope item; its Notes cell is the
  ID-explicit cross-link declaring that the receipts parser's per-loop
  coverage limits are stated under SOW-009, which DEL-04-05 covers.

**DEP-04-05-004** (E-N17, DEL-04-03 → DEL-04-05, CONSUMES)
- `EvidenceFile`: PLAN exhibit → `docs/PRD.md`
- `SourceRef`: (duplicated quote text) → `PRD.md §6 invariant PEC-K-04`
- `EvidenceQuote`: (duplicate of the above) → `Every response carries the examined-through commit SHA and per-feed freshness; consumers detect staleness structurally.`
- `Statement`: **EDITED — see below**
- Aptness: DEL-04-05 must state limitations where a feed is *stale*
  (PEC-ORI-006 / SOW-009). PEC-K-04 establishes that staleness is detected
  from the per-feed freshness carried on every response — the artifact
  DEL-04-03 stamps (PEC-ORI-003 / SOW-006). The invariant is the single
  coherent locus that ties the dependent's staleness input to the upstream's
  output.

**DEP-04-05-005** (E-P36, DEL-04-01 → DEL-04-05, CONSUMES)
- `EvidenceFile`: PLAN exhibit → `docs/PRD.md`
- `SourceRef`: `location TBD` → `PRD.md §9.1 requirement PEC-ORI-006`
- `EvidenceQuote`: (empty) → `Where a feed is unparseable or stale, the response shall state the measurement limitation explicitly; silent omission is prohibited.`
- Aptness: the Statement claims limitation honesty is a property of
  orientation responses. PEC-ORI-006 is DEL-04-05's own requirement and
  locates the obligation in "the response" — the orientation response
  produced by DEL-04-01.

## Statement edits (flagged per §3.1)

Both edited cells held the D-PEC-62 exhibit's `Rationale` verbatim, and in
both cases that `Rationale` was a **refutation-round finding tag** carrying no
statement of the dependency claim at all. These meet the §3.1 "misstates the
dependency claim" condition; the other seven EXECUTION rows in this package
did not, and were left untouched.

| DependencyID | Before | After |
|---|---|---|
| DEP-04-05-003 | `R1-F7: ID-explicit cross-link` | `DEL-04-05 states the per-loop coverage limits of the receipts ledger parser (SOW-013 note cross-links SOW-009)` |
| DEP-04-05-004 | `R3-F14` | `Staleness limitations under SOW-009 depend on the per-feed freshness stamped by DEL-04-03` |

## Waivers declared

None. No `Dependencies_EvidenceWaivers.csv` sidecar was created.

## Integrity

29 columns preserved; no rows added, deleted, or reordered; ANCHOR rows
untouched; no repaired `SourceRef` contains a quoted span (EVQ-002 clean).
Every repaired quote is a single-line contiguous verbatim span of its cited
file.
