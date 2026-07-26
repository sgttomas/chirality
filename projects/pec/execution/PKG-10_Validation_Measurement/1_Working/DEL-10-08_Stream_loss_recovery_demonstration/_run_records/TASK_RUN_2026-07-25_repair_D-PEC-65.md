# TASK RUN — 2026-07-25 — register evidence repair (D-PEC-65)

**Deliverable:** DEL-10-08 · **Package:** PKG-10 · **Instrument:** D-PEC-65 §3.1
**Agent:** sealed ephemeral Agent 2 (file-tool-only) · **File touched:** `Dependencies.csv`

## Rows dispositioned

| DependencyID | Class found | Disposition |
|---|---|---|
| DEP-10-08-001 | ANCHOR (read-only) | untouched |
| DEP-10-08-002 | ANCHOR (read-only) | untouched |
| DEP-10-08-003 | EVQ-001 duplication | REPAIRED |
| DEP-10-08-004 | EVQ-001 duplication | REPAIRED |

EXECUTION rows inspected: 2. Repaired: 2. Waived: 0. Blocked: 0.

## Cells changed

**DEP-10-08-003** (→ DEL-03-05; E-A20)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `Deliverables.csv DEL-03-05: "the P4 exit demonstration is DEL-10-08"; SOW-063 note: "Tests SOW-038"` → `Deliverables.csv row DEL-03-05 Description column`
- `EvidenceQuote`: same duplicated text → `Reconcile supremacy: no record-tier fact rests on a stream event alone; recovery path after stream gaps. Lands with the first ingest (DEL-07-01, P3) so ingest is never live without its safety invariant; the P4 exit demonstration is DEL-10-08.`
- Aptness: the target deliverable's own register description states both the recovery guarantee and that DEL-10-08 is its P4 exit demonstration — exactly the `Statement`. The seeded locus already named this text; the repair restores it as a contiguous verbatim span at a real locus in the register it actually lives in.

**DEP-10-08-004** (→ DEL-07-01; E-P78)
- `EvidenceFile`: PLAN exhibit → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `SOW-063: stream loss requires a live stream to lose` → `Deliverables.csv row DEL-03-05 Description column`
- `EvidenceQuote`: same duplicated text (which was the seeder's own reasoning, not a quotation from any source) → `Lands with the first ingest (DEL-07-01, P3) so ingest is never live without its safety invariant`
- Aptness: the register ties the recovery guarantee to DEL-07-01's ingest going live; a demonstration of stream loss therefore requires that ingest, which is the `Statement`'s claim. Real source text replaces an unsourced inference.

## Statement edits

None.

## Waivers declared

None. Both rows were class (a); no EVQ-003/EVQ-004 finding exists in this register.

## Notes

No rows added, deleted, or reordered; 29-column schema and quoting conventions preserved.
