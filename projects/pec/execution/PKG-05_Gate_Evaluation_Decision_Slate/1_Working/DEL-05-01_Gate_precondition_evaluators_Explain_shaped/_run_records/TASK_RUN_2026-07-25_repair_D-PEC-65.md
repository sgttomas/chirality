# TASK RUN — 2026-07-25 — D-PEC-65 register evidence repair (DEL-05-01)

**Actor:** sealed ephemeral Agent 2 (file-tool-only) under D-PEC-65 §3.1
**Package:** PKG-05 Gate Evaluation & Decision Slate
**Deliverable:** DEL-05-01 Gate precondition evaluators (Explain-shaped)
**Register:** `Dependencies.csv` (5 rows = 3 ANCHOR + 2 EXECUTION)

## Rows dispositioned

| DependencyID | Class found | Disposition |
|---|---|---|
| DEP-05-01-001 | ANCHOR (read-only) | untouched |
| DEP-05-01-002 | ANCHOR (read-only) | untouched |
| DEP-05-01-003 | ANCHOR (read-only) | untouched |
| DEP-05-01-004 | DUP (EVQ-001) | REPAIRED |
| DEP-05-01-005 | EMPTY (EVQ-003 + EVQ-004) | REPAIRED |

EXECUTION rows inspected: 2. Repaired: 2. Waived: 0. Already-clean: 0. Blocked: 0.

## Cells changed

### DEP-05-01-004 (target DEL-01-01; exhibit EdgeID E-P12)

Both `SourceRef` and `EvidenceQuote` carried the byte-identical locus-shaped
string `DEL-01-01 envelope note (as E-P10)` (the exhibit's `BasisCitation`
back-reference), and `EvidenceFile` pointed at the frozen D-PEC-62 PLAN
exhibit.

- `EvidenceFile`: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md`
  → `execution/_Decomposition/Deliverables.csv`
- `SourceRef`: `DEL-01-01 envelope note (as E-P10)`
  → `Deliverables.csv row DEL-01-01 (ContextEnvelopeNotes)`
- `EvidenceQuote`: `DEL-01-01 envelope note (as E-P10)`
  → `14 entity types and the schema every derivation package depends on`

Verbatim source: `projects/pec/execution/_Decomposition/Deliverables.csv`,
row `DEL-01-01`, `ContextEnvelopeNotes` cell. Aptness: PKG-05 is a derivation
package (SOFTWARE_DECOMP.md §4 / OI-012 hexagonal-grain note places PKG-05 in
the derivation core), so the record-tier schema is a prerequisite of the gate
evaluators. This is also the accepted-truth original of what the seeder was
paraphrasing (exhibit E-P10 basis), re-pointed from the frozen exhibit to the
live register per D-PEC-65 §3.1 grounding order.

### DEP-05-01-005 (target DEL-03-01; exhibit EdgeID E-P37)

`EvidenceQuote` empty, `SourceRef` = `location TBD`; the exhibit row E-P37
carried an empty `BasisCitation`, so the seeder had no citation at all.
Honest search of accepted truth found a warranting invariant, so this row is
repaired, not waived.

- `EvidenceFile`: PLAN exhibit → `docs/PRD.md`
- `SourceRef`: `location TBD` → `PRD.md §6 Product invariants (PEC-K-07)`
- `EvidenceQuote`: (empty) →
  `the reconciler over file truth is the source of every record-tier fact`

Verbatim source: `projects/pec/docs/PRD.md` §6, invariant `PEC-K-07` row.
Aptness: the `Statement` claims gate preconditions evaluate record-tier facts
(PEC-GAT-001 / SOW-022 include `register-row status`, a record-tier DecisionRow
fact). PEC-K-07 establishes that every record-tier fact originates in the
reconciler, which is the necessity that makes DEL-03-01 (the one-command
full-rebuild reconciler, SOW-010) a PREREQUISITE of DEL-05-01.

## Statement edits

**None.** Both EXECUTION `Statement` cells verbatim-duplicate the D-PEC-62
exhibit `Rationale` (E-P12, E-P37), but neither misstates the dependency
claim, so the narrow §3.1 edit authority was not exercised. Noted for the
dispatcher: `Gate-evaluation derivation entry point of PKG-05`
(DEP-05-01-004) is a terse rationale fragment rather than a full claim
sentence — under-stated, not wrong.

## Waivers declared

None. `Dependencies_EvidenceWaivers.csv` was not created for this deliverable
(no honest-empty row remains).

## Integrity

29 columns preserved on both edited rows; no cell required quoting (no commas
or double quotes introduced); no rows added, deleted, or reordered; ANCHOR
rows untouched; all other columns untouched.
