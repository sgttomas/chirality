# TASK RUN — 2026-07-26 — QA item 20 per-row disposition (D-PEC-66 act 3)

**Deliverable:** `DEL-01-03` Store bootstrap & content-minimal guard
**Authority:** `execution/_Coordination/_DECISIONS/D-PEC-66_post_repair_followons.md` act 3 (RULED 2026-07-26)
**Rule applied:** `skills/scope-of-work/QA_CHECKS.md` item 20 + `skills/scope-of-work/SKILL.md` row-semantics constraint. A row is *flagged* when it carries ≥2 `AC-*` and ≥2 `VER-*`; it *violates* item 20 only when some AC in the row would inherit a VER that does not genuinely verify it.
**Tool bound:** file-tool-only (Read/Write/Edit). No Bash, no git, no validator execution in this run; validation and checklist re-derivation are the dispatcher's at fan-in.
**Write scope:** this deliverable's `ScopeOfWork.md` (Output and Evaluation Matrix only) and this `_run_records/` file. `_STATUS.md` untouched.

## Flagged-row census

Expected 2 flagged rows (per `NOTICE_2026-07-25_helps_humans_p1_p7_applied.md` §5). Found 2. **No discrepancy.**

## Per-row dispositions

| Row (pre-edit) | ACs | VERs | Disposition |
|---|---|---|---|
| OUT-001 (row 1) | AC-001, AC-002, AC-007, AC-008 | VER-001, VER-002, VER-007 | **OVER-LINKED** — split into 3 rows |
| OUT-002 (row 2) | AC-003, AC-004, AC-005, AC-006, AC-007, AC-009 | VER-003, VER-004, VER-005, VER-006, VER-007, VER-008 | **OVER-LINKED** — split into 6 rows |
| OUT-003 (row 3) | AC-010 | VER-009 | not flagged (1 AC / 1 VER) |

### Row 1 — OUT-001: per-pair reasoning

| AC | VER-001 | VER-002 | VER-007 |
|---|---|---|---|
| AC-001 (store path Git-ignored) | genuine — `git check-ignore`/`git status` over a populated store plus ignore-rule inspection is exactly this criterion | **not genuine** — delete-and-restart exercises lifecycle recreation, says nothing about ignore rules | **not genuine** — dependency/import/interface inspection does not touch ignore state |
| AC-002 (delete → valid empty store on next start) | **not genuine** — ignore-rule inspection does not exercise deletion | genuine — stopped and running deletion, restart, recreation without manual repair | **not genuine** |
| AC-007 (no third-party dep, no network call) | **not genuine** | **not genuine** | genuine — dependency-manifest and import-graph inspection for third-party deps and network calls |
| AC-008 (interface leaks no path/engine detail) | **not genuine** | **not genuine** | genuine — VER-007 inspects the consumer-facing interface signature for store-path or engine leakage |

AC-007 and AC-008 have identical own-method sets (`{VER-007}`), so they are kept together as an exact-union row; that row carries 1 VER and is therefore not flagged.

### Row 2 — OUT-002: per-pair reasoning

Own-method set of each AC is a singleton and the six pairs are strictly 1:1:

| AC | Its own method | Every other VER in the row |
|---|---|---|
| AC-003 (single ingest boundary) | VER-003 (write-surface / import-graph inspection) | not genuine — none of VER-004/005/006/007/008 inspects the write surface for bypass paths |
| AC-004 (content fixtures rejected, no residue) | VER-004 (fixture corpus ingest + persisted-field dump) | not genuine — the others do not ingest the content fixture corpus or dump persisted fields |
| AC-005 (explicit located rejection, no silent drop) | VER-005 (located-failure assertion + count reconciliation) | not genuine — no other method reconciles input against accepted-plus-rejected counts |
| AC-006 (identical behaviour across ingest shapes) | VER-006 (reconciler/presence/event-shaped ingest) | not genuine — no other method exercises multiple ingest shapes |
| AC-007 (no third-party dep, no network call) | VER-007 (manifest + import-graph inspection) | not genuine |
| AC-009 (admissibility rule documented per field class) | VER-008 (document review against §7.1/§7.2 field inventories) | not genuine — no other method reads the documented rule |

## Before / after

### Row 1 — before

```
| OUT-001 | SOW-056 OBJ-005 | REQ-001, REQ-002, REQ-007, REQ-008, CLM-005, CLM-010, TBD-002 | AC-001, AC-002, AC-007, AC-008 | VER-001, VER-002, VER-007 | Ignore-rule inspection and `git check-ignore`/`git status` output over a populated store; delete-and-restart transcripts for the stopped and running cases showing recreation without manual repair (the governed-workflow kill test is DEL-10-02's evidence under SOW-055, not this deliverable's); dependency-manifest and import-graph inspection records; the consumer-facing interface signature |
```

### Row 1 — after

```
| OUT-001 | SOW-056 OBJ-005 | REQ-001, CLM-005, TBD-002 | AC-001 | VER-001 | Ignore-rule inspection and `git check-ignore`/`git status` output over a populated store |
| OUT-001 | SOW-056 OBJ-005 | REQ-002, CLM-005, CLM-010 | AC-002 | VER-002 | Delete-and-restart transcripts for the stopped and running cases showing recreation without manual repair (the governed-workflow kill test is DEL-10-02's evidence under SOW-055, not this deliverable's) |
| OUT-001 | SOW-056 OBJ-005 | REQ-007, REQ-008, TBD-002 | AC-007, AC-008 | VER-007 | Dependency-manifest and import-graph inspection records; the consumer-facing interface signature |
```

### Row 2 — before

```
| OUT-002 | SOW-056 OBJ-005 | REQ-003, REQ-004, REQ-005, REQ-006, REQ-007, REQ-009, CLM-004, CLM-007, CLM-008, CON-001 | AC-003, AC-004, AC-005, AC-006, AC-007, AC-009 | VER-003, VER-004, VER-005, VER-006, VER-007, VER-008 | Write-surface and import-graph inspection showing a single guard entry point; the rejection fixture corpus with per-fixture outcomes; a full persisted-field dump showing no content residue; rejection transcripts naming record and field; input-versus-accepted-plus-rejected count reconciliation; the documented admissibility rule with per-field-class decisions and citations |
```

### Row 2 — after

```
| OUT-002 | SOW-056 OBJ-005 | REQ-003 | AC-003 | VER-003 | Write-surface and import-graph inspection showing a single guard entry point |
| OUT-002 | SOW-056 OBJ-005 | REQ-004, CLM-004, CLM-007 | AC-004 | VER-004 | The rejection fixture corpus with per-fixture outcomes; a full persisted-field dump showing no content residue |
| OUT-002 | SOW-056 OBJ-005 | REQ-005 | AC-005 | VER-005 | Rejection transcripts naming record and field; input-versus-accepted-plus-rejected count reconciliation |
| OUT-002 | SOW-056 OBJ-005 | REQ-006, CLM-008 | AC-006 | VER-006 | The rejection fixture corpus with per-fixture outcomes |
| OUT-002 | SOW-056 OBJ-005 | REQ-007 | AC-007 | VER-007 | Dependency-manifest and import-graph inspection records |
| OUT-002 | SOW-056 OBJ-005 | REQ-009, CON-001 | AC-009 | VER-008 | The documented admissibility rule with per-field-class decisions and citations |
```

## Content-preservation record

- No `AC-*`, `VER-*`, `REQ-*`, `CLM-*`, `TBD-*`, `CON-*` or `OUT-*` reference was added or dropped. All 10 AC and all 9 VER definitions remain matrix-linked; every requirement/claim reference from the two source rows reappears at least once.
- Output↔AC linkage preserved: AC-007 remains linked to both OUT-001 and OUT-002 (it was in both source rows).
- Requirement/claim refs were partitioned to the split row they bear on, and duplicated only where they genuinely bear on more than one: `CLM-005` (store identity — gitignored *and* safe to delete) in the AC-001 and AC-002 rows; `TBD-002` (path/filename/engine undecided; bounded by REQ-001, REQ-007, REQ-008) in the AC-001 and AC-007/AC-008 rows.
- Evidence text redistributed verbatim at its existing `;` clause boundaries. Two formatting-only adjustments: the leading word of a clause promoted to sentence case where it became the first clause of its cell (`delete-and-restart` → `Delete-and-restart`, `dependency-manifest` → `Dependency-manifest`, `the rejection` → `The rejection`, `rejection transcripts` → `Rejection transcripts`, `write-surface` unchanged, `the documented` → `The documented`). No substantive word was changed.
- Two evidence clauses are reused verbatim in a second row where the same artifact is the evidence for that row's method: "The rejection fixture corpus with per-fixture outcomes" (AC-004/VER-004 and AC-006/VER-006 — VER-006 exercises *the same fixture corpus*), and "Dependency-manifest and import-graph inspection records" (OUT-001's AC-007/AC-008 row and OUT-002's AC-007 row — AC-007 is the same criterion under both outputs). Reuse, not new text.
- Nothing outside the matrix was touched: frontmatter, all five preceding sections, headings, IDs, and definition text are byte-identical.

## Post-state expectations for the dispatcher

- `validate_scope_of_work.py` → PASS expected: 6 canonical columns preserved, every row's cell 0 is a defined `OUT-*`, every row carries an objective ref from frontmatter, and no defined `OUT`/`AC`/`VER` is missing from the matrix.
- `derive_review_checklist.py` → 0 multi-AC/multi-VER WARNINGs for this contract (was 2). Derived checklist changes: AC-001 `{VER-001,002,007}` → `{VER-001}`; AC-002 → `{VER-002}`; AC-007 `{VER-001,002,003,004,005,006,007,008}` → `{VER-007}`; AC-008 → `{VER-007}`; AC-003 → `{VER-003}`; AC-004 → `{VER-004}`; AC-005 → `{VER-005}`; AC-006 → `{VER-006}`; AC-009 → `{VER-008}`. AC-010 unchanged. `output_refs` unchanged for every AC. The `source.sha256` and each item's `source_identity.sha256` change (matrix bytes changed); AC/VER definition line numbers are unchanged because the matrix is the last section.
