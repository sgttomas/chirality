# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-07-04 cmux socket adapter (optional) |
| Package | PKG-07 Event Ingest & Bridges |
| Instrument | `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED 2026-07-25) |
| Agent | sealed ephemeral Agent 2 (file-tool-only), `TASK-repair/D-PEC-65` |
| Files written | `Dependencies.csv` (EXECUTION evidence cells only), this run record |

## Rows dispositioned

2 EXECUTION rows (both defect-bearing); 2 ANCHOR rows read-only and untouched.

| DependencyID | Class found | Disposition | EvidenceFile after |
|---|---|---|---|
| DEP-07-04-003 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |
| DEP-07-04-004 | EMPTY (EVQ-003/-004) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |

## Cells changed

**DEP-07-04-003** (→ DEL-00-02 Event-contract schema v1)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: → `ScopeLedger.csv row SOW-034 (ScopeItemStatement)`
- `EvidenceQuote`: → `Define versioned event contract types consumable by daemon, hooks CLI, and adapters`
- Aptness: SOW-034 is the scope item DEL-00-02 covers (`DeliverableIDs = DEL-00-02`), and its statement names *adapters* as a consumer class of the versioned event contract — the cmux socket adapter being that class. The locus therefore both resolves to the target deliverable and carries the warrant. Cell double-quoted (contains commas).

**DEP-07-04-004** (→ DEL-07-01 Idempotent event ingest + durable message store)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `location TBD` → `Deliverables.csv row DEL-07-01 (Description)`
- `EvidenceQuote`: (empty) → `every message durable and queryable; no ephemeral relay.`
- Aptness: DEL-07-01's register description establishes that every message is durable and there is no ephemeral relay path; the optional cmux enricher therefore has nowhere to deliver except DEL-07-01's ingest endpoint / message store. Real evidence found — no waiver required.

## Statement edits (flagged)

None. Both seeded Statements state the actual dependency claim and were left byte-identical.

## Waivers declared

None.

## Notes

- Both rows previously cited the frozen D-PEC-62 PLAN exhibit as `EvidenceFile`; both are re-pointed at accepted decomposition truth (rev 1.2 `current_basis`).
- DEL-07-04's optionality (`absence changes nothing`) does not weaken the edge: the dependency is conditional on the adapter being built at all, which is what an EXECUTION prerequisite row records.
- No rows added, deleted, or reordered; 29-column schema preserved.
