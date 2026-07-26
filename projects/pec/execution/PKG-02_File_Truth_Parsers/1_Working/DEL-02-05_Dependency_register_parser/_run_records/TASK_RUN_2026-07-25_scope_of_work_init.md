# TASK RUN RECORD — DEL-02-05 ScopeOfWork.md initialization

| Field | Value |
|---|---|
| Date | 2026-07-25 |
| Agent shell | TASK (sealed Agent 2), dispatched by PROJECT_SETUP |
| Decision | D-PEC-63, SOW initialization wave, batch B3 |
| TaskSkill | `scope-of-work` |
| Skill version | `chirality-skill-version: "1"`; `chirality-task-profile: NONE` |
| MODE | INIT |
| PHASE | PROJECT_SETUP_PHASE_2_2 |
| DECOMP_VARIANT | SOFTWARE |
| STATUS_POLICY | NO_STATUS_TOUCH |
| Engine/model | claude-opus-5 (1M context) |
| RUN_STATUS | **COMPLETED** |

## 1. Companion files loaded

- `skills/scope-of-work/SKILL.md`
- `skills/scope-of-work/BRIEF_SCHEMA.md`
- `skills/scope-of-work/TOOL_POLICY.md`
- `skills/scope-of-work/QA_CHECKS.md`

Skill-contract pre-ruling applied as briefed (D-PEC-63 §3.1): the companion
files are CONVERT-shaped in places. TOOL_POLICY steps 2–5 (converter,
evidence-candidate refinement, claim map, parity, finalizer) are inert for
`INIT`, which the policy itself types as "source-grounded authoring".
QA_CHECKS items 1–3 and 5–14 and 17 are CONVERT-scoped; the applicable INIT
invariant for item 3 is that `_STATUS.md` is byte-identical with its state
unchanged (`OPEN` stays `OPEN`), which held. Applicable INIT checks —
frontmatter/headings/IDs/references/matrix validity (4), `OUT-*` → scope and
objective refs (8), `AC-*` → `VER-*` or explicit human-review method (9),
checklist completeness and order (13), repeated derivation byte-identical
(18), return distinguishing finding classes (16) — all pass.

## 2. Grounding order actually followed

1. `ScopeLedger.csv` row `SOW-015` and its `SourceRef` into `projects/pec/docs/PRD.md` (§9.2 `PEC-RCN-002`; §7.1 `DependencyEdge` row).
2. `SOFTWARE_DECOMP.md` revision 1.2 (`@3623b958b`) §3 objectives, §4 `PKG-02` charter, §5 `PKG-02` row, §11 decision log `DL-4` and `DL-9`, §Open Issues `OI-010`; `Deliverables.csv` row `DEL-02-05`.
3. Deliverable-local control files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, `_STATUS.md`.
4. Upstream read: `PKG-01_Service_Core_Store/1_Working/DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md` (state `INITIALIZED`).
5. Warrant record: `execution/_ScopeChange/SCA-002_2026-07-25_1042/Amendment_Preview.md` (Q2 INDIRECT-8) and `Decision_Log.md` (`D-17`, Gate 3 ruling table).
6. Edge provenance: `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` edge register (`E-P07`, `E-P23`, `E-P73`, plus `E-P03` for the "(as E-P03)" back-reference); `execution/_Coordination/_DECISIONS/D-PEC-62_...md` §1(3) and §1(4).
7. Corpus census (own measurement, this checkout, 2026-07-25) recorded as `CLM-016`.

Basis-revision note (OI-B) applied: `_REFERENCES.md` still pins "revision 1.1";
the contract cites revision 1.2 per `DECOMPOSITION_BASIS` and `_CONTEXT.md`'s
supersession line, and names the 1.1 phrase as superseded provenance.

## 3. Upstream elements bound

`[E-P07]` (`DEL-01-01` → `DEL-02-05`, `PROPOSAL`, `Flag` empty, `RequiredMaturity`
`INITIALIZED`, register row `DEP-02-05-003`). `INITIALIZED` read as: the
upstream **contract** is the reliable input; no schema, entity model, or code
exists. Bound elements, all quoted verbatim in `CLM-009` under blockquote with
the ID carve-out sentence:

| Upstream element | Binds |
|---|---|
| `DEL-01-01/REQ-001` | The fourteen record-tier types incl. **DependencyEdge**, each traced to its `PRD.md` §7.1 row |
| `DEL-01-01/REQ-003` | Per-claim citation provenance on every record-tier type (`PEC-ORI-004`) |
| `DEL-01-01/REQ-005` | Full regenerability from file sources (`PEC-K-02`) |
| `DEL-01-01/REQ-007` | No field admits file/diff content; register-row prose inexpressible (`PEC-K-10`) |
| `DEL-01-01/AC-006` | The acceptance form of the same field-shape bound |

Also cited: `DEL-01-01/CLM-006`, which carries the `PRD.md` §7.1 `DependencyEdge`
purpose cell verbatim ("From `Dependencies.csv` registers and `WORK_GRAPH.json`").
No upstream artifact is asserted to exist anywhere in the contract.

## 4. Deliberate judgments (recorded for fan-in)

1. **Warrant.** `SOW-015` is a Q2 **INDIRECT-8** member. The group carries **no
   confidence label** and was **ruled** ("AFFIRM `OBJ-001;OBJ-002` for all eight
   (not N1, not N2)"), so **no owner-confirmation AC was minted** — that pattern
   belongs to open rated recommendations. `AC-012` routes the *fidelity* question
   (indirect `OBJ-002` leg stated no more strongly than the record states it) to
   the REVIEW gate, matching the accepted B2/B3 sibling pattern.
2. **`WORK_GRAPH.json` is in scope and cannot be dropped.** `DL-9` records that
   the file "was routed to the wrong entity" in the pre-verification draft; the
   `SOW-015` and `SOW-014` `Notes` cells are the two halves of that correction.
   `REQ-001` therefore names both file forms as non-droppable, and `CON-004`
   forbids dropping the work-graph form merely because the pec loop has none.
3. **Two feeds, one envelope-`S` deliverable → `CON-001`.** Recorded as a stated
   tension against the `PKG-02` exclusion "interpretation beyond declared
   grammars", not resolved. Grammar breadth is a production decision bounded by
   `REQ-002`/`REQ-006`; dropping a form or interpreting undeclared shapes is a
   scope-change question.
4. **`CON-002` (new, feed-specific).** Register edge identity (`EdgeID`,
   stratum, flag) lives inside the free-text `Notes` column, while `PEC-K-10`
   and the bound `DEL-01-01/REQ-007` forbid emitting register-row prose.
   Recorded as a genuine conflict; the structural fix (promoting edge identity
   to a column) is a register-schema amendment this deliverable does not own.
5. **`CLM-013` + `REQ-008` (edge-direction discipline).** The parser reads
   registers as a data feed and owns none of the dependency-register governance.
   Grounded in `D-PEC-62` §1(3) (owner's verbatim deliverable-local ruling),
   `_DEPENDENCIES.md` ("advisory visibility only — never work assignment";
   `C-10` "strata are provenance not authority"), and `PEC-K-06`. `VER-007`
   makes non-adjudication checkable with cycle / contradiction / unsatisfied-
   prerequisite / disputed-stratum fixtures.
6. **AC/VER mapping-range discipline.** `AC-011` ranges over `VER-001..VER-010`
   only, excluding the mapping check `VER-011` itself (DEL-01-06 `AC-006`
   pattern).
7. **Register-quote discipline.** The `SOW-015` ledger row is quoted in full
   including trailing empty `DecisionRef`; `DEP-02-05-003` is attributed field
   by field across all 29 `v3.1` columns; `DL-9` is quoted at its relevant
   clause with elisions marked; `D-17` cells are quoted separately and
   identified by column without elision.
8. **Phase staging** (`CLM-011`) checked against the `PhaseHint` column for all
   18 deliverables named in the contract's own voice: all `P1` except
   `DEL-01-02` (`P3`), which is cited only as an owner of untouched scope.

## 5. Corpus census method (basis of `CLM-016`)

Read-only measurement over this checkout on 2026-07-25, `node_modules` excluded:

- `Dependencies.csv`: 936 files; 13,452 data rows; `RegisterSchemaVersion` `v3.1` on every row; 2 distinct header tuples (930 × 29 cols, 6 × 31 cols adding `EstimateImpactClass`,`ConsumerHint`); 17 files quote every header cell; 64 files CRLF (exactly the `projects/pec` set); `DependencyClass` = `EXECUTION` 9,550 / `ANCHOR` 3,902; by loop root 728 / piping 93 / pec 64 / app-dev 51; 120 rows carry an `EdgeID=` token inside `Notes`.
- `WORK_GRAPH.json`: 35 files; all parse; 31 distinct top-level key sets; 82 distinct top-level keys; `nodes` in 35, `edges` in 10; version key spelled `schema` ×17, `schema_version` ×2, `schemaVersion` ×2, absent ×14; 9 distinct declared values; 220 distinct node-object keys; by loop piping 14 / root 11 / app-dev 10 / **pec 0**.

Recorded as observation, not specification.

## 6. Tool policy compliance

| Step | Tool | Status |
|---|---|---|
| 1 | Read + hash authoritative sources and `_STATUS.md` | Done |
| 2 | `convert_four_documents_to_scope_of_work.py` | **Not applicable** (INIT is source-grounded authoring) |
| 3 | Evidence-candidate refinement | **Inert for INIT** (no conversion candidate exists) |
| 4 | `map_scope_of_work_claims.py`, `report_scope_of_work_parity.py` | **Not applicable** (CONVERT-scoped; no source markers to map) |
| 5 | `finalize_scope_of_work.py` | **Not applicable** (no evidence candidate to finalize) |
| 6 | `validate_scope_of_work.py` | Run — **PASS** |
| 7 | `derive_review_checklist.py` | Run twice to stdout — byte-identical; not persisted |
| 8 | `render_scope_of_work.py` | Not run (`RENDER_HTML: false`) |

No `--force`. No write to legacy or underscore files. No HTML. No checklist
artifact persisted.

## 7. Results

```
PASS format=SOW_V1 target=projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser
```

| Artifact | Value |
|---|---|
| Production `ScopeOfWork.md` sha256 | `dfb2b1a598ad1ae30d2313ef897d830d23dccecd347871e8355d34f689fb10cd` |
| Checklist `item_count` | 12 (`AC-001`..`AC-012`) |
| Checklist `schema` / `tool_version` | `chirality-review-checklist/v1` / `1` |
| Checklist `source.sha256` | `dfb2b1a598ad1ae30d2313ef897d830d23dccecd347871e8355d34f689fb10cd` (binds the production contract) |
| Repeated derivation | Byte-identical (`43fa7198…0fad` on both runs) |
| `_STATUS.md` sha256 before = after | `5bec92422830374ea838b046aca53c858ed94500a511393f3698f456686ba4c0` |
| `_STATUS.md` state | `OPEN` → `OPEN` (untouched, per `STATUS_POLICY: NO_STATUS_TOUCH`) |

Checklist coverage: `AC-001`→`VER-001`, `AC-002`→`VER-002`, `AC-003`→`VER-003`,
`AC-004`→`VER-004`, `AC-005`→`VER-005`, `AC-006`→`VER-006`, `AC-007`→`VER-007`,
`AC-008`→`VER-008`, `AC-009`→`VER-009`, `AC-010`→`VER-010`, `AC-011`→`VER-011`,
`AC-012`→`HUMAN_REVIEW` (REVIEW gate). Every `AC-*` appears exactly once, in
source order.

## 8. Contract inventory

`OUT-001..002` · `CLM-001..016` · `TBD-001..005` · `REQ-001..012` ·
`AC-001..012` · `CON-001..004` · `VER-001..011` · `AX-001..011`. Matrix rows: 12,
one per `AC-*`; every defined `OUT`/`AC`/`VER` appears in the matrix; no `REM-*`
defined; every referenced ID is defined.

## 9. Write authorization — exact files written

1. `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/ScopeOfWork.md`
2. `projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-05_Dependency_register_parser/_run_records/TASK_RUN_2026-07-25_scope_of_work_init.md` (this file)

Nothing else was written. `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`,
`_DEPENDENCIES.md`, `Dependencies.csv`, and `_SEMANTIC.md` verified
byte-identical to `HEAD` after the run. Two scratch files were written to the
session scratchpad outside the repo (checklist stdout captures for the
byte-identity comparison); they are not repo artifacts.
