# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-07-02 Daemon SSE subscriber bridge |
| Package | PKG-07 Event Ingest & Bridges |
| Instrument | `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED 2026-07-25) |
| Agent | sealed ephemeral Agent 2 (file-tool-only), `TASK-repair/D-PEC-65` |
| Files written | `Dependencies.csv` (EXECUTION evidence cells only), this run record |

## Rows dispositioned

2 EXECUTION rows (both defect-bearing); 2 ANCHOR rows read-only and untouched.

| DependencyID | Class found | Disposition | EvidenceFile after |
|---|---|---|---|
| DEP-07-02-003 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| DEP-07-02-004 | EMPTY (EVQ-003/-004) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |

## Cells changed

**DEP-07-02-003** (→ DEL-00-02 Event-contract schema v1)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `SourceRef`: → `SOFTWARE_DECOMP.md §4 Packages table row PKG-07 (Scope Description)`
- `EvidenceQuote`: → `the daemon SSE / hooks CLI / cmux bridges, durable message store, the shared-runtime client seam — implementing the PKG-00 event contracts`
- Aptness: the §4 PKG-07 scope description names the daemon SSE bridge among the surfaces implementing the PKG-00 event contracts — the dependency the row asserts. Cell double-quoted (contains commas).

**DEP-07-02-004** (→ DEL-07-01 Idempotent event ingest + durable message store)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `location TBD` → `Deliverables.csv row DEL-07-01 (Description)`
- `EvidenceQuote`: (empty) → `every message durable and queryable; no ephemeral relay.`
- Aptness: DEL-07-01's register description establishes that every message is durable and there is no ephemeral relay path; a declared bridge therefore has nowhere to deliver except DEL-07-01's ingest endpoint / message store. Real evidence found — no waiver required.

## Statement edits (flagged)

None. Both seeded Statements state the actual dependency claim and were left byte-identical.

## Waivers declared

None.

## Notes

- Both rows previously cited the frozen D-PEC-62 PLAN exhibit as `EvidenceFile`; both are re-pointed at accepted decomposition truth (rev 1.2 `current_basis`).
- The DEL-07-01 quote used here is shared with DEL-07-03 and DEL-07-04, whose bridge→ingest dependency is the same claim under the same accepted text; the locus is identical because the warrant is identical, not by default.
- No rows added, deleted, or reordered; 29-column schema preserved.
