# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

| Field | Value |
|---|---|
| Deliverable | DEL-07-01 Idempotent event ingest + durable message store |
| Package | PKG-07 Event Ingest & Bridges |
| Instrument | `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED 2026-07-25) |
| Agent | sealed ephemeral Agent 2 (file-tool-only), `TASK-repair/D-PEC-65` |
| Files written | `Dependencies.csv` (EXECUTION evidence cells only), this run record |

## Rows dispositioned

3 EXECUTION rows (all defect-bearing); 3 ANCHOR rows read-only and untouched.

| DependencyID | Class found | Disposition | EvidenceFile after |
|---|---|---|---|
| DEP-07-01-004 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |
| DEP-07-01-005 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` |
| DEP-07-01-006 | EMPTY (EVQ-003/-004) | REPAIRED | `execution/_Decomposition/ScopeLedger.csv` |

## Cells changed

**DEP-07-01-004** (→ DEL-00-02 Event-contract schema v1)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: → `Deliverables.csv row DEL-00-02 (Description)`
- `EvidenceQuote`: → `Published one phase ahead of its P3 consumers (DEL-07-01/-03) per the PKG-00 publish/consume mechanic.`
- Aptness: the cited Description names DEL-07-01 as a P3 consumer of DEL-00-02 under the PKG-00 publish/consume mechanic — exactly the dependency asserted.

**DEP-07-01-005** (→ DEL-01-04 Self-observability logging)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: → `Deliverables.csv row DEL-01-04 (Description)`
- `EvidenceQuote`: → `Reconcile-run and ingest-activity logging with an inspection command.`
- `Statement`: **EDITED — FLAGGED** (see below)
- Aptness: DEL-01-04's own register description states it provides ingest-activity logging, which is what DEL-07-01's ingest depends on.

**DEP-07-01-006** (→ DEL-01-03 Store bootstrap & content-minimal guard)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/ScopeLedger.csv`
- `SourceRef`: `location TBD` → `ScopeLedger.csv row SOW-056 (ScopeItemStatement)`
- `EvidenceQuote`: (empty) → `Keep the store at a gitignored path and enforce the content-minimal rule at ingest`
- Aptness: SOW-056 is the scope item DEL-01-03 covers (`DeliverableIDs = DEL-01-03`); its statement binds the gitignored store and the ingest-boundary guard, which is the boundary DEL-07-01's durable message store sits behind. Real evidence found — no waiver required.

## Statement edits (flagged)

| DependencyID | Before | After | Why |
|---|---|---|---|
| DEP-07-01-005 | `R3-F6: ingest-logging half is phase-staged to P3` | `DEL-07-01 ingest activity is logged by DEL-01-04's self-observability logging` | Seeded text was a D-PEC-62 refutation-round provenance note (round 3, finding 6) about phase staging; it stated no dependency claim, so it misstated the edge per D-PEC-65 §3.1. |

## Waivers declared

None. All three rows carry real verbatim evidence.

## Notes

- `EvidenceFile` on all three rows previously pointed at the frozen D-PEC-62 PLAN exhibit, which D-PEC-62 §3.3 ruled history-only. All three are now re-pointed at accepted decomposition truth (rev 1.2 `current_basis` companion registers).
- No rows added, deleted, or reordered; 29-column schema preserved; all non-evidence cells untouched.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MIN-4** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-07-01-005` | `Statement` | `DEL-07-01 ingest activity is logged by DEL-01-04's self-observability logging` | `DEL-07-01 ingest activity is logged by DEL-01-04's self-observability logging; ingest-logging half is phase-staged to P3` |

`EvidenceFile`, `SourceRef`, and `EvidenceQuote` are untouched; the evidence
repair recorded above stands unchanged.

Why: the earlier flagged `Statement` rewrite dropped the seeded qualifier
recording that the ingest-logging half is phase-staged to P3. The disposition
restores it inline by append, so the dependency claim and the phase qualifier now
stand together. `RequiredMaturity`, `Confidence`, and `Notes` are untouched.

**Integrity:** the appended text introduces no comma, so the cell remains a valid
unquoted CSV field. Row re-read post-edit: 29 columns intact.
