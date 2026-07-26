# TASK RUN — 2026-07-26 — QA item 20 per-row disposition (D-PEC-66 act 3)

**Deliverable:** `DEL-01-05` Zero-dependency & locality enforcement
**Authority:** `execution/_Coordination/_DECISIONS/D-PEC-66_post_repair_followons.md` act 3 (RULED 2026-07-26)
**Rule applied:** `skills/scope-of-work/QA_CHECKS.md` item 20 + `skills/scope-of-work/SKILL.md` row-semantics constraint. A row is *flagged* when it carries ≥2 `AC-*` and ≥2 `VER-*`; it *violates* item 20 only when some AC in the row would inherit a VER that does not genuinely verify it.
**Tool bound:** file-tool-only (Read/Write/Edit). No Bash, no git, no validator execution in this run; validation and checklist re-derivation are the dispatcher's at fan-in.
**Write scope:** this deliverable's `ScopeOfWork.md` (Output and Evaluation Matrix only) and this `_run_records/` file. `_STATUS.md` untouched.

**Standing-character note.** This contract is authored as a `C-08` standing assertion (see its Purpose section and AX-003): every requirement and every verification method binds *continuing* behaviour. That framing was read before judging, and it does not change the item-20 test — it makes each VER a repeated act rather than a one-shot one, but the question of whether a given VER produces evidence bearing on a given AC is unaffected. In particular the standing framing does **not** license grouping AC-004 (execution-per-state), AC-005 (blocking verdict) and AC-007 (registration stays armed) in one row merely because all three are facets of "the gate keeps running"; the checklist deriver would tell a reviewer to check the blocking-verdict demonstration as verification of the armed-registration criterion, which it is not.

## Flagged-row census

Expected 5 flagged rows (per `NOTICE_2026-07-25_helps_humans_p1_p7_applied.md` §5). Found 5. **No discrepancy.** The four unflagged rows are the OUT-002/AC-003 row (1 AC / 1 VER), the OUT-003/AC-009 row (1 AC / 1 VER), and the two `HUMAN_REVIEW` rows (AC-010, AC-011 — no `VER-*` refs at all).

## Per-row dispositions

| Row (pre-edit, in file order) | ACs | VERs | Disposition |
|---|---|---|---|
| 1 — OUT-001 | AC-001, AC-002 | VER-001, VER-002 | **OVER-LINKED** — split 1:1 |
| 2 — OUT-001 | AC-006, AC-008 | VER-006, VER-008 | **OVER-LINKED** — split 1:1 |
| 3 — OUT-002 | AC-003 | VER-003 | not flagged |
| 4 — OUT-002 | AC-006, AC-008 | VER-006, VER-008 | **OVER-LINKED** — split 1:1 |
| 5 — OUT-003 | AC-009 | VER-009 | not flagged |
| 6 — OUT-003 | AC-010 | HUMAN_REVIEW | not flagged |
| 7 — OUT-001 | AC-004, AC-005, AC-007 | VER-004, VER-005, VER-007 | **OVER-LINKED** — split 1:1 |
| 8 — OUT-002 | AC-004, AC-005, AC-007 | VER-004, VER-005, VER-007 | **OVER-LINKED** — split 1:1 |
| 9 — OUT-003 | AC-011 | HUMAN_REVIEW | not flagged |

### Row 1 — per-pair reasoning

| AC | VER-001 | VER-002 |
|---|---|---|
| AC-001 (pass on a conforming surface; fail naming dependency *and* importer) | genuine — VER-001 executes the assertion against conforming and violating (direct and transitive) fixtures and asserts the located failure | **not genuine** — VER-002 is a static read of the admitted-set configuration against the `PEC-SVC-001` wording; it executes nothing and can neither pass a conforming surface nor name an importer |
| AC-002 (admitted set enumerated in configuration; no wildcard or inferred default) | **not genuine** — executing the check against fixtures does not establish that the admitted set is *enumerated* rather than inferred; a wildcard default would pass VER-001's fixtures | genuine |

### Rows 2 and 4 — per-pair reasoning (identical criteria pair, once per output)

| AC | VER-006 | VER-008 |
|---|---|---|
| AC-006 (degraded input → reported failure, never pass/skip/empty success) | genuine — VER-006 is the fault injection that produces exactly those three degraded inputs | **not genuine** — VER-008 compares manifests and working tree before/after a *successful* full run and looks for network calls; it injects no fault |
| AC-008 (mechanism adds no dependency, makes no network call, modifies nothing) | **not genuine** — fault injection produces failures, not a before/after comparison of the manifest and working tree | genuine |

### Rows 7 and 8 — per-pair reasoning (identical criteria triple, once per output)

| AC | VER-004 | VER-005 | VER-007 |
|---|---|---|---|
| AC-004 (execution exists per state, bound to that state, no result reused) | genuine — VER-004 inspects the gate record across a change sequence and a release candidate for exactly this | **not genuine** — a blocking-verdict demonstration produces one verdict; it does not establish per-state execution or non-reuse | **not genuine** — the mutation check disables the registration; it asserts nothing about state binding |
| AC-005 (explicit blocking verdict on a failing candidate and on a withheld check) | **not genuine** — inspecting the gate record shows executions, not the verdict returned for a violating candidate | genuine — VER-005 submits a candidate violating each rule and one with the assertion withheld | **not genuine** |
| AC-007 (disable/remove/bypass is visible in gate configuration and reports a gate failure, not a silent no-op) | **not genuine** | **not genuine (near miss, ruled strictly)** — VER-005's withheld-check case does show a non-silent outcome, but that consequence is already AC-005's own text ("on one against which either assertion was not executed … an explicit blocking verdict"); AC-007's assertion is that the *gate configuration diff* makes the change visible, and VER-005 never inspects the gate configuration | genuine — VER-007 is the mutation check that disables then removes the registration and asserts both the reported missing enforcement and configuration-diff visibility |

## Before / after

### Rows 1–2 — before

```
| OUT-001 | SOW-052 OBJ-005 | REQ-001, REQ-002, REQ-004, REQ-009, CLM-003, CLM-008, TBD-003, TBD-004, TBD-005 | AC-001, AC-002 | VER-001, VER-002 | Fixture set with expected verdicts, check output naming each offending dependency and importer, and the admitted-set configuration read against the PEC-SVC-001 wording |
| OUT-001 | SOW-052 OBJ-005 | REQ-005, REQ-008, REQ-012 | AC-006, AC-008 | VER-006, VER-008 | Fault-injection transcripts showing failure on every degraded input, plus before/after manifest and working-tree comparison for a full run |
```

### Rows 1–2 — after

```
| OUT-001 | SOW-052 OBJ-005 | REQ-001, REQ-004, REQ-009, CLM-003, CLM-008, TBD-003, TBD-004, TBD-005 | AC-001 | VER-001 | Fixture set with expected verdicts, check output naming each offending dependency and importer |
| OUT-001 | SOW-052 OBJ-005 | REQ-002, CLM-003 | AC-002 | VER-002 | The admitted-set configuration read against the PEC-SVC-001 wording |
| OUT-001 | SOW-052 OBJ-005 | REQ-005, REQ-012 | AC-006 | VER-006 | Fault-injection transcripts showing failure on every degraded input |
| OUT-001 | SOW-052 OBJ-005 | REQ-008, REQ-012 | AC-008 | VER-008 | Before/after manifest and working-tree comparison for a full run |
```

### Row 4 — before

```
| OUT-002 | SOW-053 OBJ-005 | REQ-005, REQ-008, REQ-012 | AC-006, AC-008 | VER-006, VER-008 | Fault-injection transcripts for the locality assertion and the same self-inspection record showing no added runtime dependency, no network call, and no modified service-core file |
```

### Row 4 — after

```
| OUT-002 | SOW-053 OBJ-005 | REQ-005, REQ-012 | AC-006 | VER-006 | Fault-injection transcripts for the locality assertion |
| OUT-002 | SOW-053 OBJ-005 | REQ-008, REQ-012 | AC-008 | VER-008 | The same self-inspection record showing no added runtime dependency, no network call, and no modified service-core file |
```

### Rows 7–8 — before

```
| OUT-001 | SOW-052 OBJ-005 | REQ-006, REQ-007, CLM-006, CLM-007, AX-003, CON-002 | AC-004, AC-005, AC-007 | VER-004, VER-005, VER-007 | Registration records for the dependency assertion binding each execution to the state it evaluated, blocking-verdict demonstrations for the dependency rule and for a withheld check, and a mutation run showing the disabled registration reported rather than silently skipped |
| OUT-002 | SOW-053 OBJ-005 | REQ-006, REQ-007, CLM-006, CLM-007, AX-003, CON-002 | AC-004, AC-005, AC-007 | VER-004, VER-005, VER-007 | Registration records for the locality assertion on the same terms, with blocking-verdict demonstrations for the egress rule and for a withheld check |
```

### Rows 7–8 — after

```
| OUT-001 | SOW-052 OBJ-005 | REQ-006, CLM-006, CLM-007, AX-003 | AC-004 | VER-004 | Registration records for the dependency assertion binding each execution to the state it evaluated |
| OUT-001 | SOW-052 OBJ-005 | REQ-007, CLM-006, CON-002 | AC-005 | VER-005 | Blocking-verdict demonstrations for the dependency rule and for a withheld check |
| OUT-001 | SOW-052 OBJ-005 | REQ-006, CLM-007 | AC-007 | VER-007 | A mutation run showing the disabled registration reported rather than silently skipped |
| OUT-002 | SOW-053 OBJ-005 | REQ-006, CLM-006, CLM-007, AX-003 | AC-004 | VER-004 | Registration records for the locality assertion on the same terms |
| OUT-002 | SOW-053 OBJ-005 | REQ-007, CLM-006, CON-002 | AC-005 | VER-005 | Blocking-verdict demonstrations for the egress rule and for a withheld check |
| OUT-002 | SOW-053 OBJ-005 | REQ-006, CLM-007 | AC-007 | VER-007 | A mutation run showing the disabled registration reported rather than silently skipped |
```

Row order is preserved: each source row was expanded in place, so rows 3, 5, 6 and 9 sit between the expansions exactly where they were.

## Content-preservation record

- No `AC-*`, `VER-*`, `REQ-*`, `CLM-*`, `TBD-*`, `CON-*`, `AX-*` or `OUT-*` reference was added or dropped. All 11 AC and all 9 VER definitions remain matrix-linked; every requirement/claim reference from the five source rows reappears at least once.
- Output↔AC linkage preserved: AC-004, AC-005, AC-006, AC-007 and AC-008 each remain linked to both OUT-001 and OUT-002, exactly as before.
- Requirement/claim refs partitioned to the split row they bear on, duplicated only where they genuinely bear on more than one: `CLM-003` (the two PRD anchors; AC-002 reads the `PEC-SVC-001` wording directly) in the AC-001 and AC-002 rows; `REQ-012` (tests implement the declared methods) in both halves of rows 2 and 4; `REQ-006` (registration as a standing gate) in the AC-004 and AC-007 rows; `CLM-006` (the `C-08` standing-node row, incl. "owner confirmation requested") in the AC-004 and AC-005 rows; `CLM-007` (zero-edge node — "gates releases rather than successors") in the AC-004 and AC-007 rows.
- `CON-002` and `REQ-007` were placed on the AC-005 rows because AC-005's own text routes the gating-authority question there ("Whether that verdict binds the release is CON-002 and AC-011"). `AX-003` was placed on the AC-004 rows because AC-004 is the criterion that forbids carrying a passing run forward — the standing-shape value it states. Neither ref left the matrix.
- Evidence text redistributed verbatim at its existing comma clause boundaries. Formatting-only sentence-case promotions where a clause became the first in its cell: `the admitted-set` → `The admitted-set`; `before/after manifest` → `Before/after manifest`; `the same self-inspection record` → `The same self-inspection record`; `blocking-verdict demonstrations` → `Blocking-verdict demonstrations` (twice); `a mutation run` → `A mutation run`. Dropped list connectives only: the `and` before "the admitted-set configuration", the `plus` before "before/after manifest", the `and` before "the same self-inspection record", the `and` before "a mutation run", the `with` before "blocking-verdict demonstrations". No substantive word was changed.
- One clause is reused verbatim in a second row: "A mutation run showing the disabled registration reported rather than silently skipped" now also carries the OUT-002/AC-007 row, which the source row 8 left without evidence text of its own. That is the correct artifact for VER-007 under OUT-002 — OUT-002's own definition states it is delivered "together with the same wiring into the service-core change path and the release gate, on the same terms as OUT-001", so the mutation run is the same run. Reuse, not new text.
- Nothing outside the matrix was touched: frontmatter, all five preceding sections, headings, IDs, and definition text are byte-identical.

## Post-state expectations for the dispatcher

- `validate_scope_of_work.py` → PASS expected: 6 canonical columns preserved, every row's cell 0 is a defined `OUT-*`, every row carries an objective ref from frontmatter, both `HUMAN_REVIEW:` cells untouched and still full-cell matches, and no defined `OUT`/`AC`/`VER` is missing from the matrix.
- `derive_review_checklist.py` → 0 multi-AC/multi-VER WARNINGs for this contract (was 5). Derived checklist changes: AC-001 `{VER-001, VER-002}` → `{VER-001}`; AC-002 → `{VER-002}`; AC-004 `{VER-004,005,007}` → `{VER-004}`; AC-005 → `{VER-005}`; AC-006 `{VER-006, VER-008}` → `{VER-006}`; AC-007 → `{VER-007}`; AC-008 → `{VER-008}`. AC-003, AC-009, AC-010, AC-011 unchanged. `output_refs` unchanged for every AC. The `source.sha256` and each item's `source_identity.sha256` change (matrix bytes changed); AC/VER definition line numbers are unchanged because the matrix is the last section.
- Nothing in this run touches `CON-002`'s substance: whether the enforcement carries release-gating authority remains the open owner question routed at AC-011.
