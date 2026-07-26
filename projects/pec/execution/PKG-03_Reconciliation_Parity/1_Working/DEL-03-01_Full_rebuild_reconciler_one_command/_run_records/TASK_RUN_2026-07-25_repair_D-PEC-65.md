# TASK RUN — 2026-07-25 — Register evidence repair (D-PEC-65)

**Deliverable:** DEL-03-01 Full-rebuild reconciler (one command)
**Instrument:** `execution/_Coordination/_DECISIONS/D-PEC-65_register_evidence_repair.md` (RULED 2026-07-25)
**Agent:** sealed ephemeral Agent 2, file-tool-only (no Bash, no Git, no scripts)
**File touched:** `Dependencies.csv` (EXECUTION rows only; 3 ANCHOR rows untouched)

## Rows dispositioned

| DependencyID | Class found | Disposition | EvidenceFile after | SourceRef after |
|---|---|---|---|---|
| DEP-03-01-004 | DUP (EVQ-001) | REPAIRED | `docs/PRD.md` | PRD.md §10 requirement PEC-SVC-006 |
| DEP-03-01-005 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` | Deliverables.csv row DEL-01-01 ContextEnvelopeNotes |
| DEP-03-01-006 | EMPTY (EVQ-003/004) | REPAIRED | `execution/_Decomposition/SOFTWARE_DECOMP.md` | SOFTWARE_DECOMP.md §11 Decision Log row DL-11 |
| DEP-03-01-007 | DUP (EVQ-001) | REPAIRED | `execution/_Decomposition/Deliverables.csv` | Deliverables.csv row DEL-01-06 Description |
| DEP-03-01-008 | DUP (EVQ-001) | REPAIRED | `docs/PRD.md` | PRD.md §9.2 requirement PEC-RCN-002 |
| DEP-03-01-009 | DUP (EVQ-001) | REPAIRED | `docs/PRD.md` | PRD.md §9.2 requirement PEC-RCN-002 |
| DEP-03-01-010 | DUP (EVQ-001) | REPAIRED | `docs/PRD.md` | PRD.md §9.2 requirement PEC-RCN-002 |
| DEP-03-01-011 | DUP (EVQ-001) | REPAIRED | `docs/PRD.md` | PRD.md §9.2 requirement PEC-RCN-002 |
| DEP-03-01-012 | DUP (EVQ-001) | REPAIRED | `docs/PRD.md` | PRD.md §9.2 requirement PEC-RCN-002 |
| DEP-03-01-013 | DUP (EVQ-001) | REPAIRED | `docs/PRD.md` | PRD.md §9.2 requirement PEC-RCN-002 |
| DEP-03-01-014 | DUP (EVQ-001) | REPAIRED | `docs/PRD.md` | PRD.md §9.2 requirement PEC-RCN-002 |

11 EXECUTION rows, 11 REPAIRED, 0 WAIVED, 0 BLOCKED. Pre-repair finding load: 12
(10 EVQ-001 + 1 EVQ-003 + 1 EVQ-004).

## Cells changed

`EvidenceFile`, `SourceRef`, `EvidenceQuote` on all eleven rows. Every row's prior
`EvidenceFile` was the frozen D-PEC-62 PLAN exhibit
(`execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`), which
D-PEC-62 §3.3 rules history-only; all eleven are re-pointed to live accepted
sources. No other cell touched. No rows added, deleted, or reordered.

## Repair basis (grounding order: accepted decomposition truth, then PRD v2.1)

- **-004** (DEL-01-04 → DEL-03-01): PEC-SVC-006 names PEC's own reconcile runs as
  the logged subject, so the logging facility precedes the reconciler that emits
  into it.
- **-005** (DEL-01-01 → DEL-03-01): DEL-01-01's Context Envelope note states the
  record-tier schema is the one every derivation package depends on; PKG-03 is a
  derivation package.
- **-006** (DEL-01-03 → DEL-03-01): DL-11 records the Phase 4 forced boundary —
  the one-command rebuild went to PKG-03 while the store-path rule (SOW-056,
  covered by DEL-01-03) stayed in PKG-01, so the reconciler's store is owned
  upstream. Repaired with real evidence; no waiver required.
- **-007** (DEL-01-06 → DEL-03-01): DEL-01-06's description defines the loop
  registry as naming the loops PEC serves, one loop at P1 — the scoping input the
  P1 reconciler consumes.
- **-008..-014** (DEL-02-01..-07 → DEL-03-01): PEC-RCN-002 is the feed list the
  seeder gestured at with `PEC-RCN-002 feed list (DL-4)`. Each row now carries a
  contiguous verbatim span of that requirement running from
  `The reconciler shall ingest, at minimum:` through its own feed, so each quote
  names both the ingesting subject and the specific feed. No ellipsis, no reflow.

## Statement edits

**None.** All eleven `Statement` cells carry the D-PEC-62 exhibit `Rationale`
verbatim, but none misstates the dependency claim, so the packet's edit condition
is not met.

One observation flagged for the dispatcher rather than edited: DEP-03-01-005's
Statement (`Reconciler entry point of PKG-03`) names the successor's role rather
than asserting a relation. It under-specifies but does not misstate. The same
terse `... entry point of PKG-XX` pattern appears corpus-wide on the E-P10/-P11/
-P12/-P13 sibling rows in PKG-04 and PKG-05, so normalizing it is a corpus-level
call, not a package-local one.

## Waivers declared

**None.** No `Dependencies_EvidenceWaivers.csv` sidecar was created for this
deliverable: every row, including the single empty-evidence row (-006), had real
quotable source text.

## Tooling note

Validator and quote-verification runs are the dispatcher's acts at fan-in per
D-PEC-65 §3.1/§3.3; this child ran none.

## Revision (closure-refutation remediation, 2026-07-25)

Sealed Agent 2 REVISION dispatch under `D-PEC-65` §3.1 (file-tool-only), applying
closure-refutation disposition **MIN-2** exactly as specified. No other cell in
this file changed.

| DependencyID | Cell | Before | After |
|---|---|---|---|
| `DEP-03-01-005` | `EvidenceQuote` | `L: 14 entity types and the schema every derivation package depends on` | `14 entity types and the schema every derivation package depends on` |

`EvidenceFile` and `SourceRef` unchanged
(`execution/_Decomposition/Deliverables.csv`; `Deliverables.csv row DEL-01-01
ContextEnvelopeNotes`).

Why: the leading `L: ` was the Context Envelope size code prefixing the note cell,
not part of the sentence being cited; carrying it into the quote presented a
column marker as prose. Stripped so the span matches the clean form siblings
`DEP-04-01-004` and `DEP-05-01-004` already use for the same locus.

**Verbatim check:** the new quote is a contiguous single-line substring of
`projects/pec/execution/_Decomposition/Deliverables.csv`, row `DEL-01-01`,
`ContextEnvelopeNotes` column, and is byte-identical to the span at
`DEP-05-01-004`. `SourceRef` carries no quoted span. Row re-read post-edit: 29
columns intact.
