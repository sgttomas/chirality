# TASK RUN — QA item 20 per-row disposition (DEL-00-01)

**Date:** 2026-07-26
**Authority:** D-PEC-66 act 3 (`execution/_Coordination/_DECISIONS/D-PEC-66_post_repair_followons.md`)
**Agent form:** sealed Agent 2, file-tool-only (Read/Write/Edit)
**Write scope:** this deliverable's `ScopeOfWork.md` and `_run_records/`
**Rule applied:** `skills/scope-of-work/QA_CHECKS.md` item 20 (both clauses) and
`skills/scope-of-work/SKILL.md` row-semantics constraint ("a row's verification
references apply to every acceptance criterion in that row … Checklist
derivation is row-scoped and cannot recover a finer pairing").

## Flagged rows

Expected 1; found 1. No count discrepancy.

## Disposition

| Row (original matrix position) | ACs | VERs | Disposition |
|---|---|---|---|
| Row 1 (OUT-001, first row) | AC-001, AC-002, AC-004, AC-005 | VER-001, VER-003 | **OVER-LINKED** — repaired by split |

### Per-pair reasoning

| Pair | Genuine? | One-line reason |
|---|---|---|
| AC-001 × VER-001 | YES | VER-001 inspects the ADR set against REQ-001, which is exactly "one decision record naming the selected style and identifying it as the OI-012 resolution". |
| AC-001 × VER-003 | NO | VER-003 asserts consistency between the set's self-identification and the register disposition; it asserts nothing about "exactly one record" or "a single selected style", which is AC-001's whole content. |
| AC-002 × VER-001 | YES | VER-001 names REQ-002, the context/no-added-invariant requirement AC-002 restates. |
| AC-002 × VER-003 | NO | An open-issue register cross-check cannot verify that the ADR's context section reproduces the CLM-006 Gate 4 basis or that it adds no invariant. |
| AC-004 × VER-001 | YES | VER-001 names REQ-007, which verifies AC-004's second half (decides none of OI-001..OI-009 or OI-013). |
| AC-004 × VER-003 | YES | VER-003 is the register-consistency and no-other-issue-decided check AC-004's first half requires. |
| AC-005 × VER-001 | YES | VER-001 names REQ-006, the entity-schema versus store-persistence seam requirement AC-005 restates. |
| AC-005 × VER-003 | NO | The register cross-check says nothing about whether the seam is stated explicitly enough to classify a PKG-01 change. |

### Note on which clause of item 20 fails

Clause 1 (union test) **passes**: the union of the four criteria's own methods is
{VER-001, VER-003}, equal to the row's VER set, because AC-004 legitimately owns
VER-003. Clause 2 **fails**: the derived checklist entries for AC-002 and AC-005
(and AC-001) would name VER-003, which does not verify them. The repair is
warranted by clause 2 and by the SKILL.md rationale; recorded here so the
dispatcher can see the union proxy alone would have missed it.

## Repair — before / after

**Before (1 row):**

```
| OUT-001 | SOW-088 OBJ-005 | REQ-001 REQ-002 REQ-006 REQ-007 CLM-006 CON-001 | AC-001 AC-002 AC-004 AC-005 | VER-001 VER-003 | Published core-isolation ADR plus the read-only cross-check record showing the ADR's self-identified OI-012 resolution consistent with the register's existing disposition, no register edit performed, and no other open issue decided |
```

**After (2 rows):**

```
| OUT-001 | SOW-088 OBJ-005 | REQ-001 REQ-002 REQ-006 CLM-006 CON-001 | AC-001 AC-002 AC-005 | VER-001 | Published core-isolation ADR |
| OUT-001 | SOW-088 OBJ-005 | REQ-007 CON-001 | AC-004 | VER-001 VER-003 | The read-only cross-check record showing the ADR's self-identified OI-012 resolution consistent with the register's existing disposition, no register edit performed, and no other open issue decided |
```

Content preservation:

- Acceptance refs: AC-001, AC-002, AC-004, AC-005 each appear exactly once in
  the matrix, as before. None added, dropped, or reworded.
- Verification refs: VER-001 now appears on both split rows (it verifies every
  AC of the original row); VER-003 is confined to AC-004. No VER added or
  dropped.
- Requirement/claim refs redistributed verbatim by linkage: REQ-001/REQ-002/
  REQ-006/CLM-006 to the VER-001-only row; REQ-007 to the AC-004 row; CON-001
  (OI-012 undecided) carried on both rows because it bears on both.
- Evidence expectation split verbatim at the original "plus" connector; the
  second fragment's leading "the" capitalized to "The". No other prose change.
- Objective refs, Output, column headers, and every other row unchanged.

## Contract-wide effect

No frontmatter, heading, ID, or non-matrix section changed. Rows 2–4 of the
original matrix are byte-identical (they became rows 3–5). Matrix row count
4 → 5.

## Rerun requirements for the dispatcher

- `validate_scope_of_work.py` on this contract (expect PASS).
- `derive_review_checklist.py` re-run: AC-002 and AC-005 lose VER-003 from their
  checklist entries; AC-001 loses VER-003; AC-004 unchanged. No AC or VER is
  orphaned.
- New `ScopeOfWork.md` sha256 to be recorded at fan-in (no Bash in this run).
