# TASK RUN — QA item 20 per-row disposition (DEL-00-03)

**Date:** 2026-07-26
**Authority:** D-PEC-66 act 3 (`execution/_Coordination/_DECISIONS/D-PEC-66_post_repair_followons.md`)
**Agent form:** sealed Agent 2, file-tool-only (Read/Write/Edit)
**Write scope:** this deliverable's `ScopeOfWork.md` and `_run_records/`
**Rule applied:** `skills/scope-of-work/QA_CHECKS.md` item 20 (both clauses) and
the `SKILL.md` row-semantics constraint.

## Flagged rows

Expected 3; found 3 (original matrix rows 1, 2, and 4). No count discrepancy.
Original rows 5 (AC-006 | VER-003, VER-005) and 6 (AC-007 | VER-001) carry a
single AC and cannot violate item 20; row 3 is the HUMAN_REVIEW row.

## Disposition summary

| Row (original position) | ACs | VERs | Disposition |
|---|---|---|---|
| Row 1 (OUT-001) | AC-002, AC-005, AC-010 | VER-001, VER-002, VER-008 | **OVER-LINKED** — split 1 → 2 |
| Row 2 (OUT-001) | AC-001, AC-008, AC-009 | VER-006, VER-007, VER-009 | **OVER-LINKED** — split 1 → 3 |
| Row 4 (OUT-002) | AC-003, AC-004 | VER-002, VER-003, VER-004 | **OVER-LINKED** — split 1 → 2 |

In all three rows the union test (clause 1 of item 20) is satisfied — the row's
VER set equals the union of its criteria's own methods — while clause 2 fails:
the derived checklist entry for at least one AC would name a method that does
not verify it. The repairs are warranted by clause 2 and by SKILL.md's
"checklist derivation is row-scoped and cannot recover a finer pairing".

## Row 1 — per-pair reasoning

| Pair | Genuine? | One-line reason |
|---|---|---|
| AC-002 × VER-001 | YES | VER-001 names REQ-001 and REQ-002 — derive structure from the accepted registers, introduce nothing beyond the basis — which is AC-002's substance. |
| AC-002 × VER-002 | YES | VER-002 is the register cross-check that resolves every PKG/DEL/OBJ/SOW token and reports any unexplained subset, i.e. AC-002 verbatim. |
| AC-002 × VER-008 | NO | Vocabulary conformance against §9 tests terminology, not whether named registers entries resolve at the bound basis. |
| AC-005 × VER-001 | YES | REQ-002, inside VER-001's inspection list, is the "no requirement, invariant, objective, package, deliverable, or scope item beyond the basis" rule AC-005 restates. |
| AC-005 × VER-002 | YES | The register cross-check reports every non-register token, which is how AC-005's first clause is measured. |
| AC-005 × VER-008 | NO | The §9 vocabulary check governs the sense of "package", not whether a retired v1.0/v0.4 identifier family is used as a live v2 identifier. |
| AC-010 × VER-001 | NO | VER-001's inspection list is REQ-001, REQ-002, REQ-006, REQ-012 — REQ-011 (vocabulary map) is not in it, so VER-001 verifies nothing in AC-010. |
| AC-010 × VER-002 | NO | Token resolution against the registers says nothing about terminology conformance or the disambiguation of "package". |
| AC-010 × VER-008 | YES | VER-008 is the vocabulary conformance inspection with explicit attention to every occurrence of "package". |

**Before:**

```
| OUT-001 | SOW-089 OBJ-001 | REQ-001, REQ-002, REQ-011, REQ-012, CLM-002, CLM-004, CLM-005, CLM-006, CLM-010 | AC-002, AC-005, AC-010 | VER-001, VER-002, VER-008 | The published SPEC markdown, a register cross-check report resolving every PKG/DEL/OBJ/SOW token to an accepted row, and a vocabulary conformance record covering every use of "package" |
```

**After:**

```
| OUT-001 | SOW-089 OBJ-001 | REQ-001, REQ-002, REQ-012, CLM-002, CLM-004, CLM-005, CLM-006 | AC-002, AC-005 | VER-001, VER-002 | The published SPEC markdown and a register cross-check report resolving every PKG/DEL/OBJ/SOW token to an accepted row |
| OUT-001 | SOW-089 OBJ-001 | REQ-011, CLM-010 | AC-010 | VER-008 | A vocabulary conformance record covering every use of "package" |
```

AC-002 and AC-005 remain grouped because their method sets are identical
({VER-001, VER-002}), which is the exact-union case the standard permits.

## Row 2 — per-pair reasoning

| Pair | Genuine? | One-line reason |
|---|---|---|
| AC-001 × VER-007 | YES | VER-007 is the path-and-write-scope check: packet-recorded path exists, holds the SPEC, change set confined to PKG-00. |
| AC-001 × VER-006 | NO | An open-issue register cross-check cannot establish the artifact's path or the write boundary. |
| AC-001 × VER-009 | NO | The pre-P1 obligation and consumer check addresses timing and consumers, not path or write scope. |
| AC-008 × VER-006 | YES | VER-006 is the before/after register cross-check confirming unchanged dispositions and still-TBD §16 items. |
| AC-008 × VER-007 | NO | Path and write-scope checking cannot show that OI dispositions did not move. |
| AC-008 × VER-009 | NO | Pre-P1 timing and consumer naming have no bearing on register dispositions. |
| AC-009 × VER-009 | YES | VER-009 is exactly the pre-P1 completion, no-P1-or-later-dependency, no-unnamed-consumer check. |
| AC-009 × VER-006 | NO | The register cross-check does not measure completion timing or consumer naming. |
| AC-009 × VER-007 | NO | Path existence and write confinement do not establish pre-P1 completion or the absence of a consumer obligation. |

**Before:**

```
| OUT-001 | SOW-089 OBJ-001 | REQ-007, REQ-008, REQ-009, REQ-010, CLM-009, CLM-011, CLM-012, CLM-013, CON-001, TBD-002 | AC-001, AC-008, AC-009 | VER-006, VER-007, VER-009 | Packet-recorded docs path with the SPEC present at it, a change set confined to PKG-00, an open-issue register diff showing no disposition movement, and a pre-P1 completion record naming no P1-or-later dependency and no unnamed consumer |
```

**After:**

```
| OUT-001 | SOW-089 OBJ-001 | REQ-008, CLM-009, TBD-002 | AC-001 | VER-007 | Packet-recorded docs path with the SPEC present at it and a change set confined to PKG-00 |
| OUT-001 | SOW-089 OBJ-001 | REQ-007, CLM-011 | AC-008 | VER-006 | An open-issue register diff showing no disposition movement |
| OUT-001 | SOW-089 OBJ-001 | REQ-009, REQ-010, CLM-012, CLM-013, CON-001 | AC-009 | VER-009 | A pre-P1 completion record naming no P1-or-later dependency and no unnamed consumer |
```

The original evidence expectation was already a four-clause list in the pairing
order; it was redistributed clause by clause (the two path/write clauses stay
together on AC-001), with leading connectors dropped and the first letter of
each fragment capitalized.

## Row 4 — per-pair reasoning

| Pair | Genuine? | One-line reason |
|---|---|---|
| AC-003 × VER-003 | YES | VER-003 resolves every PEC-K / PEC-family token and rejects retired-family identifiers presented as live — AC-003's second clause. |
| AC-003 × VER-002 | YES | The register cross-check resolves the "accepted decomposition identifier" half of AC-003's citation requirement. |
| AC-003 × VER-004 | NO | A basis revision/commit binding check verifies nothing about whether individual specification claims carry resolvable citations. |
| AC-004 × VER-004 | YES | VER-004 is exactly the check that the revision and commit stated in the seed equal the bound basis or a named successor. |
| AC-004 × VER-002 | NO | Resolving tokens *at* the bound basis is the checking context, not verification that the seed states its basis in its own text. |
| AC-004 × VER-003 | NO | PRD identifier resolution says nothing about the basis-revision statement. |

**Before:**

```
| OUT-002 | SOW-089 OBJ-001 | REQ-003, REQ-004, CLM-005, CLM-006 | AC-003, AC-004 | VER-002, VER-003, VER-004 | Citation-resolution output listing every PEC-K / PEC-family and decomposition identifier in the seed with its resolved location, plus a basis-binding check against the SOFTWARE_DECOMP.md front matter and the Git commit object |
```

**After:**

```
| OUT-002 | SOW-089 OBJ-001 | REQ-003, CLM-005, CLM-006 | AC-003 | VER-002, VER-003 | Citation-resolution output listing every PEC-K / PEC-family and decomposition identifier in the seed with its resolved location |
| OUT-002 | SOW-089 OBJ-001 | REQ-004, CLM-005 | AC-004 | VER-004 | A basis-binding check against the SOFTWARE_DECOMP.md front matter and the Git commit object |
```

CLM-005 (the accepted basis, including its revision) is carried on both rows
because it bears on both criteria; no requirement or claim ref was dropped.

## Contract-wide effect

Matrix row count 6 → 10. Every AC-001..AC-011 still appears exactly once;
every VER-001..VER-009 still appears at least once. No frontmatter, heading,
ID, or non-matrix text changed; unflagged rows are byte-identical.

## Observation (not an item-20 finding, no edit made)

AC-005's second clause ("no v1.0 or v0.4 identifier family is used for a v2
identifier") is verified most directly by VER-003, which the matrix links to
AC-003 and AC-006 but not to AC-005. That is a coverage question, not
over-linkage; adding VER-003 to AC-005 would have added a verification ref,
which this brief forbids. Surfaced for the dispatcher.

## Rerun requirements for the dispatcher

- `validate_scope_of_work.py` (expect PASS).
- `derive_review_checklist.py` re-run: AC-002/AC-005 lose VER-008; AC-010 loses
  VER-001 and VER-002; AC-001 keeps only VER-007; AC-008 only VER-006; AC-009
  only VER-009; AC-003 loses VER-004; AC-004 keeps only VER-004. Nothing
  orphaned.
- New `ScopeOfWork.md` sha256 to be recorded at fan-in (no Bash in this run).
