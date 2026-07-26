# TASK RUN — 2026-07-26 — QA item 20 per-row disposition (D-PEC-66 act 3)

**Deliverable:** `DEL-01-04` Self-observability logging
**Authority:** `execution/_Coordination/_DECISIONS/D-PEC-66_post_repair_followons.md` act 3 (RULED 2026-07-26)
**Rule applied:** `skills/scope-of-work/QA_CHECKS.md` item 20 + `skills/scope-of-work/SKILL.md` row-semantics constraint. A row is *flagged* when it carries ≥2 `AC-*` and ≥2 `VER-*`; it *violates* item 20 only when some AC in the row would inherit a VER that does not genuinely verify it.
**Tool bound:** file-tool-only (Read/Write/Edit). No Bash, no git, no validator execution in this run; validation and checklist re-derivation are the dispatcher's at fan-in.
**Write scope:** this deliverable's `ScopeOfWork.md` (Output and Evaluation Matrix only) and this `_run_records/` file. `_STATUS.md` untouched.

## Flagged-row census

Expected 2 flagged rows (per `NOTICE_2026-07-25_helps_humans_p1_p7_applied.md` §5). Found 2. **No discrepancy.**

## Per-row dispositions

| Row (pre-edit) | ACs | VERs | Disposition |
|---|---|---|---|
| OUT-001 (row 1) | AC-001, AC-002, AC-003, AC-005, AC-006 | VER-001, VER-002, VER-003, VER-005, VER-006 | **OVER-LINKED** — split into 5 rows (strict 1:1) |
| OUT-002 (row 2) | AC-004, AC-005, AC-006 | VER-004, VER-005, VER-006 | **OVER-LINKED** — split into 3 rows (AC-004 keeps two genuine methods) |
| OUT-003 (row 3) | AC-007 | VER-007 | not flagged (1 AC / 1 VER) |

### Row 1 — OUT-001: per-pair reasoning

The five criteria have singleton own-method sets in strict 1:1 order, so every off-diagonal pair is an inherited method:

| AC | Its own method | Every other VER in the row |
|---|---|---|
| AC-001 (one durable event per reconcile run; suppressed emission detected) | VER-001 (fixture reconcile run + suppression fixture) | not genuine — VER-002/003/005/006 never execute a reconcile run against the emission assertion |
| AC-002 (ingest events validate against the reconcile-run schema; no reconcile-only assumption) | VER-002 (fixture ingest emitter + schema/interface inspection) | not genuine — no other method drives an ingest emitter or inspects the schema for reconcile-only fields |
| AC-003 (content-minimal fields only; mutation and deletion refused) | VER-003 (content-minimality check + mutation/deletion attempts) | not genuine — no other method inspects recorded field classes or attempts mutation |
| AC-005 (deleted/unwritable/absent log → reconcile unblocked; absence reported explicitly) | VER-005 (three degraded log states + reconcile + inspection) | not genuine — no other method degrades the log store |
| AC-006 (no third-party dep, no network call, writes only under the gitignored path) | VER-006 (manifest + import-graph inspection + write-path check) | not genuine — no other method reads the dependency manifest or resolves write paths |

### Row 2 — OUT-002: per-pair reasoning

| AC | VER-004 | VER-005 | VER-006 |
|---|---|---|---|
| AC-004 (inspection command: recorded order, identity, timestamp, explicit empty-or-absent report) | genuine — VER-004 runs the command over populated, single-event and empty fixtures and asserts order, identity, timestamp, and a distinguishable empty-or-absent report | **genuine** — VER-004's fixture set stops at *empty*; VER-005 is the only method that produces an *absent/deleted/unwritable* log and asserts "an explicit inspection-command absence report in each case", which is the other half of AC-004's absence limb | **not genuine** — dependency/import/write-path inspection says nothing about command output |
| AC-005 (reconcile unblocked under degraded log; absence reported) | **not genuine** — VER-004 runs no reconcile and uses no absent-log fixture | genuine | **not genuine** |
| AC-006 (no third-party dep, no network call, gitignored write path) | **not genuine** | **not genuine** | genuine |

AC-004 therefore keeps `{VER-004, VER-005}` — an exact-union pairing, and that row carries a single AC so it is not flagged. The repair removes only the four inherited pairs in this row: AC-005×VER-004, AC-005×VER-006, AC-006×VER-004, AC-006×VER-005. AC-004×VER-006 is likewise removed — five inherited pairs in total.

## Before / after

### Row 1 — before

```
| OUT-001 | SOW-057 OBJ-006 | REQ-001, REQ-002, REQ-003, REQ-004, REQ-006, REQ-007, CLM-005, CLM-007, CON-001 | AC-001, AC-002, AC-003, AC-005, AC-006 | VER-001, VER-002, VER-003, VER-005, VER-006 | Event-schema documentation, recorded fixture events for both subject classes, suppressed-emission and mutation/deletion refusal transcripts, content-minimality check output, and dependency-manifest plus import-graph inspection records |
```

### Row 1 — after

```
| OUT-001 | SOW-057 OBJ-006 | REQ-001, CLM-005 | AC-001 | VER-001 | Recorded fixture events for both subject classes, suppressed-emission transcripts |
| OUT-001 | SOW-057 OBJ-006 | REQ-002, CLM-005, CON-001 | AC-002 | VER-002 | Event-schema documentation, recorded fixture events for both subject classes |
| OUT-001 | SOW-057 OBJ-006 | REQ-003, REQ-004, CLM-007 | AC-003 | VER-003 | Mutation/deletion refusal transcripts, content-minimality check output |
| OUT-001 | SOW-057 OBJ-006 | REQ-006 | AC-005 | VER-005 | Reconcile-run transcripts under deleted, unwritable, and absent log stores showing unblocked completion (the kill-test transcript is DEL-10-02's evidence under SOW-055, not this deliverable's) |
| OUT-001 | SOW-057 OBJ-006 | REQ-007, CLM-007 | AC-006 | VER-006 | Dependency-manifest plus import-graph inspection records |
```

### Row 2 — before

```
| OUT-002 | SOW-057 OBJ-006 | REQ-005, REQ-006, REQ-007, CLM-006, CLM-009, TBD-003 | AC-004, AC-005, AC-006 | VER-004, VER-005, VER-006 | Inspection-command output over populated, single-event, empty, and absent log fixtures, showing recorded order, per-event identity and timestamp, and the explicit absence report; reconcile-run transcripts under deleted, unwritable, and absent log stores showing unblocked completion (the kill-test transcript is DEL-10-02's evidence under SOW-055, not this deliverable's) |
```

### Row 2 — after

```
| OUT-002 | SOW-057 OBJ-006 | REQ-005, CLM-006, TBD-003 | AC-004 | VER-004, VER-005 | Inspection-command output over populated, single-event, empty, and absent log fixtures, showing recorded order, per-event identity and timestamp, and the explicit absence report |
| OUT-002 | SOW-057 OBJ-006 | REQ-006, CLM-009 | AC-005 | VER-005 | Reconcile-run transcripts under deleted, unwritable, and absent log stores showing unblocked completion (the kill-test transcript is DEL-10-02's evidence under SOW-055, not this deliverable's) |
| OUT-002 | SOW-057 OBJ-006 | REQ-007 | AC-006 | VER-006 | Dependency-manifest plus import-graph inspection records |
```

## Content-preservation record

- No `AC-*`, `VER-*`, `REQ-*`, `CLM-*`, `TBD-*`, `CON-*` or `OUT-*` reference was added or dropped. All 7 AC and all 7 VER definitions remain matrix-linked; every requirement/claim reference from the two source rows reappears at least once.
- Output↔AC linkage preserved: AC-005 and AC-006 remain linked to both OUT-001 and OUT-002 (they were in both source rows).
- Requirement/claim refs partitioned to the split row they bear on, duplicated only where they genuinely bear on more than one: `CLM-005` (the two logged subject classes) in the AC-001 and AC-002 rows; `CLM-007` (append-only + content-minimal + gitignored store path) in the AC-003 and AC-006 rows.
- Evidence text redistributed verbatim at its existing comma clause boundaries. The compound clause "suppressed-emission and mutation/deletion refusal transcripts" was decomposed at its own coordination into "suppressed-emission transcripts" (AC-001) and "mutation/deletion refusal transcripts" (AC-003) — both are the coordinated halves of the source phrase with its shared head noun, no new word. Formatting-only sentence-case promotions where a clause became the first in its cell: `recorded fixture events` → `Recorded fixture events`; `content-minimality check output` retained lowercase position after "Mutation/deletion refusal transcripts,"; `dependency-manifest plus` → `Dependency-manifest plus`; `reconcile-run transcripts` → `Reconcile-run transcripts`. The joining word "and" before the manifest clause was dropped as a list connective.
- Two clauses are reused verbatim across rows where the same artifact is the evidence for that row's method: "recorded fixture events for both subject classes" (AC-001 and AC-002 rows — the phrase names both classes); "Reconcile-run transcripts under deleted, unwritable, and absent log stores …" and "Dependency-manifest plus import-graph inspection records" appear under both OUT-001 and OUT-002 because AC-005 and AC-006 are linked to both outputs. Reuse, not new text.
- Nothing outside the matrix was touched: frontmatter, all five preceding sections, headings, IDs, and definition text are byte-identical.

## Post-state expectations for the dispatcher

- `validate_scope_of_work.py` → PASS expected: 6 canonical columns preserved, every row's cell 0 is a defined `OUT-*`, every row carries an objective ref from frontmatter, and no defined `OUT`/`AC`/`VER` is missing from the matrix.
- `derive_review_checklist.py` → 0 multi-AC/multi-VER WARNINGs for this contract (was 2). Derived checklist changes: AC-001 `{VER-001,002,003,005,006}` → `{VER-001}`; AC-002 → `{VER-002}`; AC-003 → `{VER-003}`; AC-004 `{VER-004,005,006}` → `{VER-004, VER-005}`; AC-005 `{VER-001,002,003,004,005,006}` → `{VER-005}`; AC-006 → `{VER-006}`. AC-007 unchanged. `output_refs` unchanged for every AC. The `source.sha256` and each item's `source_identity.sha256` change (matrix bytes changed); AC/VER definition line numbers are unchanged because the matrix is the last section.
