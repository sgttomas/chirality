# TASK RUN — DEL-00-03 AC-005 × VER-003 coverage-gap plug

**Date:** 2026-07-26
**Authorization:** D-PEC-66 Addendum act 4(b) (owner-ruled, post-closure) —
`projects/pec/execution/_Coordination/_DECISIONS/D-PEC-66_post_repair_followons.md`
**Agent:** sealed Agent 2, file-tool-only (Read/Write/Edit; no Bash, no Git)
**Write scope:** `ScopeOfWork.md` + `_run_records/` of this deliverable only
**Basis of the gap:** D-PEC-66 closure adversarial refutation finding **F6**

---

## 1. The gap

`AC-005` carries two clauses:

> The seed contains no requirement, invariant, objective, package, deliverable,
> or scope item that is absent from the accepted basis, **and no v1.0 or v0.4
> identifier family is used for a v2 identifier.**

The second clause was genuinely verified by `VER-003`, whose second clause reads:

> ... and no retired v1.0 or v0.4 identifier family appears as a live v2 identifier.

But `VER-003` was not linked to `AC-005` in the Output & Evaluation Matrix.
`AC-002` and `AC-005` sat together in one row whose verification set was the
**exact union** of the two ACs' methods as then recorded — `{VER-001, VER-002}`.
That grouping was CONFORMS-rated and retained during the QA-item-20 repair, so
the repair correctly declined to split it; the defect is upstream of the
grouping — `AC-005`'s own method set was short by one method.

## 2. Independent verification performed before editing

Read: full contract (frontmatter, all CLM/TBD/CON, REQ-001..REQ-012,
AC-001..AC-011, VER-001..VER-009, AX-001..AX-008, matrix).

1. **`VER-003` genuinely verifies `AC-005`'s identifier-family clause.**
   Confirmed. `VER-003`'s second clause is a near-literal restatement of
   `AC-005`'s second clause ("no retired v1.0 or v0.4 identifier family appears
   as a live v2 identifier" vs. "no v1.0 or v0.4 identifier family is used for a
   v2 identifier"). Both trace to `CLM-007` / `PRD.md` §14 and `REQ-005`.
   No other VER in the contract carries an identifier-family clause: `VER-002`
   is confined to `PKG-*`/`DEL-*`/`OBJ-*`/`SOW-*` tokens, and `VER-005` is the
   archived-baseline historical-marker check, not a family check.
2. **`AC-002`'s method set does NOT include `VER-003`.** Confirmed. `AC-002` is
   confined to "package, deliverable, objective, and scope item" tokens
   resolving to accepted register rows, plus the subset-with-reason clause —
   fully served by `VER-002`, with `VER-001` covering its `REQ-001`/`REQ-002`
   document-inspection side. `AC-002` says nothing about `PEC-K-*` /
   `PEC-{ORI,...}-NNN` citation resolution or retired identifier families, so
   attaching `VER-003` to `AC-002` would over-link it.

No discrepancy with the stated gap. Proceeded to edit.

## 3. Before / after

**Before (one row):**

```
| OUT-001 | SOW-089 OBJ-001 | REQ-001, REQ-002, REQ-012, CLM-002, CLM-004, CLM-005, CLM-006 | AC-002, AC-005 | VER-001, VER-002 | The published SPEC markdown and a register cross-check report resolving every PKG/DEL/OBJ/SOW token to an accepted row |
```

**After (two rows, in the same matrix position):**

```
| OUT-001 | SOW-089 OBJ-001 | REQ-001, REQ-002, CLM-002, CLM-004, CLM-005 | AC-002 | VER-001, VER-002 | The published SPEC markdown and a register cross-check report resolving every PKG/DEL/OBJ/SOW token to an accepted row |
| OUT-001 | SOW-089 OBJ-001 | REQ-001, REQ-002, REQ-012, CLM-004, CLM-005, CLM-006 | AC-005 | VER-001, VER-002, VER-003 | The published SPEC markdown and a register cross-check report resolving every PKG/DEL/OBJ/SOW token to an accepted row; Citation-resolution output listing every PEC-K / PEC-family and decomposition identifier in the seed with its resolved location |
```

Net linkage change: **exactly one AC×VER assignment added — `AC-005 × VER-003`**
(owner-authorized; the point of the act). No AC, VER, REQ, CLM, TBD, CON, AX, or
OUT was added, dropped, renamed, or reworded. Every other matrix row, every
definition section, and the frontmatter are byte-identical.

## 4. Requirement/claim ref redistribution — bearing notes

| Ref | Placement | Ground |
|---|---|---|
| `REQ-001` | both | "derive structure from the accepted registers … rather than inventing content" bears on `AC-002`'s resolve-to-a-row test and on `AC-005`'s nothing-absent-from-basis test. Genuinely shared. |
| `REQ-002` | both | Its two halves split across the ACs: "introduce no new … package, deliverable, objective, scope item" bears on both ACs; "only `PRD.md` v2.1 requirement families and invariants as requirement source" bears on `AC-005` only. Genuinely shared. |
| `REQ-012` | `AC-005` only | Weakest assignment in the split; disclosed. `REQ-012` ("specify, not implement; assert no implementation state; create no obligation belonging to a consuming package") has no strong bearing on either AC — it is in this row because `VER-001` explicitly enumerates it. `AC-002` is confined to register-row resolution and cannot bear it at all; `AC-005`'s "contains no … that is absent from the accepted basis" is the nearer reading (asserted implementation state / invented obligation is content beyond the basis). Both rows retain `VER-001`, so `REQ-012` remains verified either way and is not orphaned. |
| `CLM-002` | `AC-002` only | Deliverable description of record ("born from this decomposition … from the accepted packages/deliverables") — grounds `REQ-001`'s derivation-from-registers, i.e. `AC-002`. |
| `CLM-004` | both | Envelope justification cites "an accepted basis (46 requirements / 64 deliverables) rather than inventing content" — spans both the register side (`AC-002`) and the requirement/invariant side (`AC-005`). |
| `CLM-005` | both | Enumerates the accepted basis (11 packages / 64 deliverables / 6 objectives / 94 scope items) — the referent of `AC-002`'s subset clause and of `AC-005`'s absent-from-basis clause. |
| `CLM-006` | `AC-005` only | Requirement source of record (`PRD.md` v2.1 alone: the 46 `PEC-*-NNN` requirements and 11 `PEC-K` invariants). `AC-002` does not cover requirements or invariants — only package/deliverable/objective/scope item — so this bears on `AC-005` exclusively, and is the claim `VER-003` operates against. |

Objective refs (`SOW-089 OBJ-001`) are unchanged and duplicated as before.

## 5. Evidence-expectation redistribution

The original cell had two clauses: *(a)* "The published SPEC markdown" and
*(b)* "a register cross-check report resolving every PKG/DEL/OBJ/SOW token to an
accepted row". Because **both** resulting rows retain `VER-001` and `VER-002`,
both clauses are carried verbatim into both rows — the `AC-002` row's cell is
byte-identical to the original.

The `AC-005` row additionally needs evidence for its newly linked `VER-003`.
Per the dispatch constraint, **no new evidence prose was written.** The sentence
was **reused verbatim from the existing `OUT-002` / `AC-003` / `VER-002 VER-003`
row**, joined with "; ":

> Citation-resolution output listing every PEC-K / PEC-family and decomposition
> identifier in the seed with its resolved location

**Disclosure:** this is a verbatim reuse, not an authored clause. It is retained
with its original sentence-initial capital `C` after the semicolon rather than
being re-cased, so that the reuse is exact and visibly traceable to its source
row. The same evidence artifact now appears in two rows; it is one artifact
serving two linkages (`AC-003 × VER-003` and `AC-005 × VER-003`), not a new
production obligation.

## 6. Post-edit re-read check

Re-read the matrix after editing:

- 11 rows, header + separator intact.
- Every row has exactly 6 columns.
- Column 0 of every row is a bare `OUT-NNN` (`OUT-001` ×7, `OUT-002` ×3, `OUT-003` ×1).
- No orphaned refs: every token in the pre-edit row (`REQ-001`, `REQ-002`,
  `REQ-012`, `CLM-002`, `CLM-004`, `CLM-005`, `CLM-006`, `AC-002`, `AC-005`,
  `VER-001`, `VER-002`) appears in at least one post-edit row.
- Neither resulting row is multi-AC **and** multi-VER, so the deriver's
  multi-AC/multi-VER stderr warning for this contract should drop 1 → 0.

## 7. Anomalies / residuals (observed, not acted on — outside this act's scope)

- **`CLM-001` is not referenced anywhere in the Output & Evaluation Matrix.**
  Pre-existing condition, present before this edit and unchanged by it (the
  contract was validating PASS in that state). Recorded for the dispatcher, not
  repaired here: touching it would exceed "nothing else may change linkage".
- No other anomaly. `_STATUS.md` untouched; the deliverable remains `OPEN`.
