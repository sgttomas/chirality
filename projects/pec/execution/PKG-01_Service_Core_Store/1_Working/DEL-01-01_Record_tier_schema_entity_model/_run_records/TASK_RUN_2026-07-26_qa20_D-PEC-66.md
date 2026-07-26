# TASK RUN — QA item 20 per-row disposition (DEL-01-01)

**Date:** 2026-07-26
**Authority:** D-PEC-66 act 3 (`execution/_Coordination/_DECISIONS/D-PEC-66_post_repair_followons.md`)
**Agent form:** sealed Agent 2, file-tool-only (Read/Write/Edit)
**Write scope:** this deliverable's `ScopeOfWork.md` and `_run_records/`
**Rule applied:** `skills/scope-of-work/QA_CHECKS.md` item 20 (both clauses) and
the `SKILL.md` row-semantics constraint.

## Flagged rows

Expected 2; found 2 (original matrix rows 1 and 2). No count discrepancy.
Row 3 (AC-012 | VER-012) is 1:1 and cannot violate item 20.

## Disposition summary

| Row (original position) | ACs | VERs | Disposition |
|---|---|---|---|
| Row 1 (OUT-001) | AC-001, AC-004, AC-006, AC-010 | VER-001, VER-004, VER-006, VER-010 | **OVER-LINKED** — split 1 → 4 |
| Row 2 (OUT-002) | AC-002, AC-003, AC-005, AC-007, AC-008, AC-009, AC-011 | VER-002, VER-003, VER-005, VER-007, VER-008, VER-009, VER-011 | **OVER-LINKED** — split 1 → 7 |

Both rows are exact 1:1 bundles: this contract's verification methods were
authored one per acceptance criterion, in the same order, and the evidence
expectation cell is a semicolon-separated list in that same order. Grouping them
made the row-scoped deriver assign 4 methods to each of 4 criteria and 7 methods
to each of 7 criteria — 12 and 42 spurious AC×VER assignments respectively.
Clause 1 of item 20 (union test) is satisfied in both rows; clause 2 — "the
derived checklist entry for each AC names no method that does not verify it" —
fails comprehensively.

## Row 1 — per-pair reasoning

Genuine pairs (diagonal):

| Pair | Genuine? | One-line reason |
|---|---|---|
| AC-001 × VER-001 | YES | VER-001 is the inventory check diffing delivered types against the fourteen CLM-005 names and eleven PRD §7.1 rows, asserting the per-type trace and REQ-002's compound-row decomposition. |
| AC-004 × VER-004 | YES | VER-004 is rebuild-and-compare with the non-reproducible-field inspection, which is AC-004 verbatim. |
| AC-006 × VER-006 | YES | VER-006 is the content-minimal type inspection that attempts the file-content/diff/prose fixture AC-006 requires to be inexpressible. |
| AC-010 × VER-010 | YES | VER-010 is the slice review against the CLM-007 envelope note, asserting one cohesive slice or a recorded-line split with seam evidence. |

Non-genuine pairs (all twelve off-diagonal), one line each:

- AC-001 × VER-004 — a rebuild-and-compare run does not count or trace entity types.
- AC-001 × VER-006 — field-content capacity inspection says nothing about type inventory or compound-row decomposition.
- AC-001 × VER-010 — artifact-slice structure is unrelated to which types exist.
- AC-004 × VER-001 — a name-level inventory diff cannot show that a rebuild reproduces every instance.
- AC-004 × VER-006 — content-capacity inspection does not test reproducibility.
- AC-004 × VER-010 — slice structure has no bearing on rebuild fidelity.
- AC-006 × VER-001 — the inventory diff does not examine field types for content capacity.
- AC-006 × VER-004 — rebuild-and-compare does not test whether a prose-bearing field exists.
- AC-006 × VER-010 — slice review does not test inexpressibility of file or diff content.
- AC-010 × VER-001 — type inventory does not measure how the DDL was sliced.
- AC-010 × VER-004 — rebuild fidelity is independent of slice line.
- AC-010 × VER-006 — field-type inspection does not evidence the seam that justified a split.

**Before:**

```
| OUT-001 | SOW-001 OBJ-001 OBJ-002 | REQ-001, REQ-002, REQ-005, REQ-007, REQ-011, CLM-005, CLM-006, CLM-007, TBD-002 | AC-001, AC-004, AC-006, AC-010 | VER-001, VER-004, VER-006, VER-010 | Type inventory diffed against the fourteen register names and the eleven PRD §7.1 rows with per-type traces; rebuild-and-compare transcript over fixture sources with the non-reproducible-field inspection; field-type inspection record plus the rejected content fixture; the delivered slice structure against the envelope note, with recorded seam evidence if a split was taken |
```

**After:**

```
| OUT-001 | SOW-001 OBJ-001 OBJ-002 | REQ-001, REQ-002, CLM-005, CLM-006 | AC-001 | VER-001 | Type inventory diffed against the fourteen register names and the eleven PRD §7.1 rows with per-type traces |
| OUT-001 | SOW-001 OBJ-001 OBJ-002 | REQ-005 | AC-004 | VER-004 | Rebuild-and-compare transcript over fixture sources with the non-reproducible-field inspection |
| OUT-001 | SOW-001 OBJ-001 OBJ-002 | REQ-007 | AC-006 | VER-006 | Field-type inspection record plus the rejected content fixture |
| OUT-001 | SOW-001 OBJ-001 OBJ-002 | REQ-011, CLM-007, TBD-002 | AC-010 | VER-010 | The delivered slice structure against the envelope note, with recorded seam evidence if a split was taken |
```

Requirement/claim redistribution: REQ-001, REQ-002 (fourteen types, compound
rows) with CLM-005 and CLM-006 to AC-001; REQ-005 (regenerable from sources) to
AC-004; REQ-007 (`PEC-K-10` content-minimal) to AC-006; REQ-011 with CLM-007
(envelope note) and TBD-002 (engine/dialect choice, which REQ-011 governs) to
AC-010. Evidence expectation split at its existing semicolons, verbatim, with
the first letter of each fragment capitalized.

## Row 2 — per-pair reasoning

Genuine pairs (diagonal):

| Pair | Genuine? | One-line reason |
|---|---|---|
| AC-002 × VER-002 | YES | VER-002 resolves each type's recorded citation provenance to a live file source by path, anchor, and/or SHA. |
| AC-003 × VER-003 | YES | VER-003 builds two OrientationSnapshots, compares them, and asserts a DriftFinding with no judgment input. |
| AC-005 × VER-005 | YES | VER-005 is the tier-boundary inspection that attempts the daemon-user-data RunRecord fixture AC-005 requires to be rejected. |
| AC-007 × VER-007 | YES | VER-007 models the `D-APP-57` and prose-structured shapes against the Receipt type and asserts per-loop availability is readable. |
| AC-008 × VER-008 | YES | VER-008 inspects the type/persistence dependency direction and runs the core-or-adapter classification exercise. |
| AC-009 × VER-009 | YES | VER-009 reviews the dependency manifest and import graph for third-party dependencies and network calls. |
| AC-011 × VER-011 | YES | VER-011 confirms consumability by the eleven recorded consumers and confinement of the change set to PKG-01. |

Non-genuine: all forty-two off-diagonal pairs. Each verification method names a
distinct artifact-level exercise bound to one criterion's subject matter, and
none of the seven subjects overlaps another. Representative reasons, one per
criterion, covering the class:

- Provenance resolution (VER-002) tests citation carriers only — it does not compare snapshots, probe the tier boundary, model Receipt availability, inspect the seam, read the dependency manifest, or check write scope (so AC-003/005/007/008/009/011 do not take it).
- The snapshot exercise (VER-003) is read-only over two source states and asserts nothing about provenance carriers, presence-tier exclusion, Receipt shapes, the persistence seam, third-party dependencies, or consumability.
- Tier-boundary inspection (VER-005) asserts only that no presence-tier type exists and that daemon state is unrepresentable.
- Receipt availability review (VER-007) is confined to the Receipt type's per-loop availability representation.
- Seam inspection (VER-008) examines the import/dependency graph and classification, not provenance, snapshots, tiers, Receipts, manifests, or write scope.
- Dependency and locality inspection (VER-009) reads the manifest and import graph for third-party dependencies and network calls, and nothing else.
- Consumability and write-scope check (VER-011) confirms reference-ability and path confinement only.

**Before:**

```
| OUT-002 | SOW-001 OBJ-001 OBJ-002 | REQ-003, REQ-004, REQ-006, REQ-008, REQ-009, REQ-010, REQ-012, CLM-009, CLM-010, CLM-011, CLM-012, CON-001, CON-002 | AC-002, AC-003, AC-005, AC-007, AC-008, AC-009, AC-011 | VER-002, VER-003, VER-005, VER-007, VER-008, VER-009, VER-011 | Per-type provenance resolution records; the two-snapshot comparison producing a classified DriftFinding with no judgment input; tier-boundary inspection with the rejected daemon-state fixture; the Receipt availability matrix covering the D-APP-57 and prose-structured shapes with no OI-008 outcome assumed; the type-versus-persistence dependency graph and the core-or-adapter classification exercise; dependency-manifest and network-call inspection; consumability confirmation for the eleven recorded consumers and a change set confined to PKG-01 |
```

**After:**

```
| OUT-002 | SOW-001 OBJ-001 OBJ-002 | REQ-003, CLM-012 | AC-002 | VER-002 | Per-type provenance resolution records |
| OUT-002 | SOW-001 OBJ-001 OBJ-002 | REQ-004, CLM-012 | AC-003 | VER-003 | The two-snapshot comparison producing a classified DriftFinding with no judgment input |
| OUT-002 | SOW-001 OBJ-001 OBJ-002 | REQ-006, CLM-011 | AC-005 | VER-005 | Tier-boundary inspection with the rejected daemon-state fixture |
| OUT-002 | SOW-001 OBJ-001 OBJ-002 | REQ-008, CON-002 | AC-007 | VER-007 | The Receipt availability matrix covering the D-APP-57 and prose-structured shapes with no OI-008 outcome assumed |
| OUT-002 | SOW-001 OBJ-001 OBJ-002 | REQ-009, CLM-009, CON-001 | AC-008 | VER-008 | The type-versus-persistence dependency graph and the core-or-adapter classification exercise |
| OUT-002 | SOW-001 OBJ-001 OBJ-002 | REQ-010, CLM-012 | AC-009 | VER-009 | Dependency-manifest and network-call inspection |
| OUT-002 | SOW-001 OBJ-001 OBJ-002 | REQ-012, CLM-010 | AC-011 | VER-011 | Consumability confirmation for the eleven recorded consumers and a change set confined to PKG-01 |
```

Requirement/claim redistribution follows each requirement's own subject:
REQ-003 → AC-002; REQ-004 → AC-003; REQ-006 with CLM-011 (`PEC-K-05` tier
boundary) → AC-005; REQ-008 with CON-002 (Receipt availability, `OI-008`) →
AC-007; REQ-009 with CLM-009 (`DEL-00-01`'s seam obligations) and CON-001
(`OI-012` undecided) → AC-008; REQ-010 → AC-009; REQ-012 with CLM-010 (the
eleven consumers) → AC-011. CLM-012 ("the acts that consume this model are
owned by other deliverables") is carried on the AC-002, AC-003, and AC-009 rows
because REQ-003, REQ-004, and REQ-010 each cite it. No ref dropped.

## Contract-wide effect

Matrix row count 3 → 12. Every AC-001..AC-012 appears exactly once; every
VER-001..VER-012 appears exactly once. No frontmatter, heading, ID, or
non-matrix text changed; the OUT-003 row is byte-identical.

## Rerun requirements for the dispatcher

- `validate_scope_of_work.py` (expect PASS).
- `derive_review_checklist.py` re-run: each AC-001..AC-011 checklist entry now
  names exactly its one verification method (AC-012 unchanged). 54 spurious
  method assignments removed; nothing orphaned.
- New `ScopeOfWork.md` sha256 to be recorded at fan-in (no Bash in this run).
