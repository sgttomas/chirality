# Source Pack: Skill pack: semantic-matrix-build

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/semantic-matrix-build/BRIEF_SCHEMA.md

### semantic-matrix-build — Brief Schema

This skill is consumed by `TASK`. The brief must make the TASK scope, semantic scope, status policy, and expected outputs explicit.

#### Required TASK fields

| Field | Requirement |
|---|---|
| `TaskSkill` | Must be `semantic-matrix-build`. |
| `ScopePath` | Absolute path to exactly one deliverable / production unit folder. This is the TASK local scope. |
| `Tasks` | Must request generation of `_SEMANTIC.md` for this one scope. |
| `ExpectedOutputs` | Must include `_SEMANTIC.md` and the TASK run record. |

#### Required semantic fields

Place these in `RuntimeOverrides` unless the local TASK convention passes them top-level.

| Field | Requirement |
|---|---|
| `deliverable_folder` | Absolute path to the same folder as `ScopePath`. |
| `decomposition_path` | Absolute path to the decomposition document, used for traceability only. |
| `DECOMP_VARIANT` | `PROJECT`, `SOFTWARE`, or `DOMAIN`. |
| `STATUS_POLICY` | `PRESERVE_CURRENT`, `ADVANCE_ON_PASS`, or `NO_STATUS_TOUCH`. Default for ORCHESTRATOR Phase 2.3 is `PRESERVE_CURRENT`. |

#### Normal ORCHESTRATOR Phase 2.3 brief

Use `ScopePath` as the TASK run/context anchor and provide `RuntimeOverrides.deliverable_folder` as the skill-local deliverable anchor. This skill must create or overwrite `_SEMANTIC.md`, so the brief must set `ApplyEdits: true` and authorize `_SEMANTIC.md` as a writable target.

```yaml
PURPOSE: Generate deliverable-local semantic lens
RequestedBy: ORCHESTRATOR
ScopePath: /absolute/path/to/PKG-XX/.../DEL-XX-YY_Name
TaskSkill: semantic-matrix-build
Tasks:
  - Generate _SEMANTIC.md for the single deliverable folder.
  - Read the deliverable-local truth set and production documents.
  - Adopt canonical matrices A and B.
  - Derive C, F, D, K, G, X, T, E in order with full interpretation work.
  - Run semantic audit and repo validator when available.
ApplyEdits: true
AllowedWriteTargets:
  - /absolute/path/to/PKG-XX/.../DEL-XX-YY_Name/_SEMANTIC.md
RuntimeOverrides:
  deliverable_folder: /absolute/path/to/PKG-XX/.../DEL-XX-YY_Name
  decomposition_path: /absolute/path/to/execution/_Decomposition/DECOMP.md
  DECOMP_VARIANT: SOFTWARE
  STATUS_POLICY: PRESERVE_CURRENT
CustomInstructions:
  - Run as sealed ORCHESTRATOR Phase 2.3 semantic matrix generation.
  - Do not author or repair production documents.
  - Do not change _STATUS.md state; preserve the current lifecycle state by runtime policy.
  - Use compact derivation tables for C, F, D, X, and E.
  - Step 1 axis anchors and Step 2 projections must resolve to semantic phrases.
  - Insert Matrix Z before Matrix Summary.
ExpectedOutputs:
  - _SEMANTIC.md
  - _run_records/TASK_RUN_*.md
```

#### Brief for status advancement on PASS

Use only when project policy says this skill owns `SEMANTIC_READY` advancement.

```yaml
ScopePath: /absolute/path/to/deliverable
TaskSkill: semantic-matrix-build
ApplyEdits: true
AllowedWriteTargets:
  - /absolute/path/to/deliverable/_SEMANTIC.md
  - /absolute/path/to/deliverable/_STATUS.md
RuntimeOverrides:
  deliverable_folder: /absolute/path/to/deliverable
  decomposition_path: /absolute/path/to/decomposition.md
  DECOMP_VARIANT: PROJECT
  STATUS_POLICY: ADVANCE_ON_PASS
CustomInstructions:
  - On audit PASS, set or verify Current State as SEMANTIC_READY and append History.
  - On audit FAIL, leave _STATUS.md state unchanged.
```

#### Variant behavior

| Variant | Production documents read | Notes |
|---|---|---|
| `PROJECT` | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` | Standard four-document set. |
| `SOFTWARE` | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` | Same document set and terminology as PROJECT. |
| `DOMAIN` | All non-metadata `.md` files not prefixed with `_`, typically `Scoping.md` and `KA-*.md` | Invoke only when explicitly requested; standard ORCHESTRATOR DOMAIN setup may skip semantic lensing. |

#### Recommended CustomInstructions

Use these for format-sensitive runs:

- Generate exactly one `_SEMANTIC.md` for exactly one deliverable folder.
- Keep the lens deliverable-conditioned but not deliverable-literal.
- Final matrix cells must be category-level 2–5 word phrases.
- Step 2 projections must resolve semantic phrases, not just restate formulas.
- Matrix Summary must use compact markdown tables, not bullet lists.
- Include `Matrix Z — Summary Boundary` before Matrix Summary.
- Do not claim validator PASS unless the repo validator actually ran.

#### Not accepted

- Multi-deliverable scope.
- Cross-deliverable scanning or comparison.
- ORCHESTRATOR authoring `_SEMANTIC.md` inline instead of dispatching TASK.
- Missing `decomposition_path`.
- Missing `STATUS_POLICY` in an ORCHESTRATOR Phase 2.3 brief.
- A brief that asks the skill to edit production documents.
- A brief that asks for both `STATUS_POLICY=ADVANCE_ON_PASS` and omits `_STATUS.md` write authorization.

## Component: skills/semantic-matrix-build/QA_CHECKS.md

### semantic-matrix-build — QA Checks

#### Minimum checks for a valid run

1. `ScopePath` exists and is a directory.
2. `deliverable_folder` exists, is a directory, and resolves to `ScopePath`.
3. `_CONTEXT.md` exists in `deliverable_folder`.
4. `decomposition_path` is provided. If the file cannot be read, record that fact; do not invent decomposition content.
5. `_SEMANTIC.md` is written to `{deliverable_folder}/_SEMANTIC.md`.
6. Production documents are read-only.
7. No sibling deliverable folder is scanned.
8. No files outside the effective bounded task brief's write authorization are written.
9. All eight derived matrices appear in sequence: C, F, D, K, G, X, T, E.
10. Canonical matrices A and B are reproduced exactly and not re-derived.
11. Interpreted matrices C, F, D, X, and E include intermediate collections and all three interpretation steps for every cell.
12. Matrix Summary appears after `Matrix Z — Summary Boundary` and contains compact markdown tables for C, F, D, K, G, X, T, and E.
13. `STATUS_POLICY` is honored exactly.
14. Repo validator is run when available and permitted; if unavailable, the report says so.

#### Structural invariants

| Check | Requirement |
|---|---|
| Header | Includes generated date, variant, perspective, framework, audit status, phase/status ruling, and Inputs Read. |
| Inputs Read | Lists `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `MEMORY.md`, and production documents as read, not present, or absent. |
| SourceRefs | Use path + best-effort heading anchor when possible. |
| Matrix A | Exact canonical 3×4 Orientation values. |
| Matrix B | Exact canonical 4×4 Conceptualization values. |
| Matrix order | A, B, C, F, D, K, G, X, T, E, Matrix Z, Matrix Summary. |
| Result tables | Every matrix section has a Result table. |
| Summary tables | Summary uses markdown tables, not bullets. |
| Matrix Z | Present between Matrix E and Matrix Summary; not counted as a semantic matrix. |
| Correct dimensions | C 3×4, F 3×4, D 3×4, K 4×3, G 3×4, X 4×4, T 4×4, E 4×4. |

#### Construction formulas

The section heading or construction note must show these formulas:

| Matrix | Required formula |
|---|---|
| C | `L_C(i,j) = Σ_k (A(i,k) * B(k,j)); C(i,j) = I(row_i, col_j, L_C(i,j))` |
| F | `L_F(i,j) = Σ_k (C(i,k) * B(k,j)); F(i,j) = I(row_i, col_j, L_F(i,j))` |
| D | `L_D(i,j) = A(i,j) + (resolution * F(i,j)); D(i,j) = I(row_i, col_j, L_D(i,j))` |
| K | `K(i,j) = D(j,i)` |
| G | remove `wisdom` row from B |
| X | `L_X(i,j) = Σ_k (K(i,k) * G(k,j)); X(i,j) = I(row_i, col_j, L_X(i,j))` |
| T | `T(i,j) = B(j,i)` |
| E | `L_E(i,j) = Σ_k (X(i,k) * T(k,j)); E(i,j) = I(row_i, col_j, L_E(i,j))` |

#### Interpretation validity

For every interpreted cell in C, F, D, X, and E:

| Check | Requirement |
|---|---|
| Intermediate collection | Contains every contributor product required by the formula. |
| Step 1 explicit | Shows `r * c = <resolved anchor phrase>`. |
| Step 1 resolved | Anchor phrase is semantic; it is not merely `<row>-<column> coordinate frame`. |
| Step 2 explicit | Shows every `p_n = a * t_n`. |
| Step 2 resolved | Every projection ends with a resolved semantic phrase. Formula-only projections are invalid. |
| Step 2 complete | Every contributor in `L` has exactly one projection. |
| Step 3 explicit | Says `centroid selects <final phrase>` or equivalent. |
| Step 3 single | Selects one final phrase only. |
| No shortcut | The working does not jump from Step 1 to Step 3. |
| Explicit products | Uses `*` for semantic products. Do not use `x` or prose-only joins. |

#### Semantic product validity

Final cells in Result tables and Matrix Summary must satisfy all checks.

| Check | Requirement |
|---|---|
| Populated | No empty final cells. |
| Single unit | Exactly one semantic unit, not a list. |
| Length | 2–5 words, except canonical inherited B/G/T values. |
| Dense | Prefer 2–3 words when complete. |
| No algebra leak | No `∩` or `Σ`. |
| No operator leak | No unresolved `+` flanked by semantic terms. |
| No long expansion | No final cell exceeds about 80 characters. |
| No axis tokens | Row/column labels for that cell do not appear literally in its final value. |
| No particulars | No exact code clauses, event-name lists, file paths, implementation paths, numeric requirements, equipment tags, or other instances. |
| No authority claims | No engineering correctness, recommendations, fitness judgments, or acceptance rulings. |

#### Deliverable-conditioning validity

The lens must be relevant to the deliverable without becoming a requirements summary.

| Failure pattern | Invalid example | Better pattern |
|---|---|---|
| Too generic | `adequate evidence` for many unrelated cells | `runtime proof`, `summary integrity`, `source assurance` |
| Too literal | exact API method, route, event name, or file path in a cell | category phrase such as `contract boundary`, `compatibility proof` |
| Requirement restatement | a SHALL-style or test-case phrase | semantic type/category phrase |
| Source warning ignored | perspective omits known source-state caveat category | perspective mentions unresolved source-state caveats without particulars |

#### Audit procedure

Audit after generating all Result tables and Matrix Summary.

Scan final cell values in:

- C Result and Summary C;
- F Result and Summary F;
- D Result and Summary D;
- K Result and Summary K;
- G Result and Summary G;
- X Result and Summary X;
- T Result and Summary T;
- E Result and Summary E.

Fail immediately if any final cell violates semantic product validity.

On audit FAIL:

1. Mark the run `FAIL`.
2. Do not repair, regenerate, or re-audit within the same run.
3. Do not advance status.
4. If `_SEMANTIC.md` is written, its header must show `Audit: FAIL`.
5. The run report must list matrix, cell, value, and reason.

On audit PASS:

1. Mark `_SEMANTIC.md` `Audit: PASS`.
2. Apply `STATUS_POLICY` exactly.
3. Run repo validator when available and permitted.
4. Report validator result or `validator not available`.

#### Status policy checks

| Policy | Required behavior |
|---|---|
| `PRESERVE_CURRENT` | Do not change lifecycle state. Header/run report says state preserved by runtime policy. |
| `ADVANCE_ON_PASS` | On audit PASS, set/verify `SEMANTIC_READY` only if `_STATUS.md` edit is authorized. On FAIL, unchanged. |
| `NO_STATUS_TOUCH` | Do not edit `_STATUS.md` at all. |

No status regression is ever allowed.

#### File-scope checks

| Check | Requirement |
|---|---|
| Production docs | Not modified. |
| `_CONTEXT.md` | Not modified. |
| `_REFERENCES.md` | Not modified. |
| `_DEPENDENCIES.md` | Not modified. |
| `MEMORY.md` | Not modified by this skill. |
| Sibling folders | Not read or written. |
| `_STATUS.md` | Modified only when status policy and TASK authorization allow it. |
| `_SEMANTIC.md` | Created/overwritten only inside `deliverable_folder`. |

#### Failure reporting

| Situation | Report |
|---|---|
| `deliverable_folder` missing/not directory | `FAILED_INPUTS` |
| `_CONTEXT.md` missing | `FAILED_INPUTS` |
| `decomposition_path` omitted | `FAILED_INPUTS` |
| `ScopePath` and `deliverable_folder` disagree | `FAILED_INPUTS` |
| Required write target unauthorized | `FAILED_INPUTS` or TASK authorization violation, according to TASK rules |
| Production doc missing | Record absent; continue |
| `_REFERENCES.md` missing | Record not present; continue |
| `MEMORY.md` missing | Record not present; continue |
| Audit fail | `FAIL`, with matrix/cell/reason |
| Validator unavailable | Report unavailable; do not claim validator PASS |

#### Success report

A clean run reports:

- `RUN_STATUS=SUCCESS` or the local TASK success token;
- deliverable ID/name;
- `DECOMP_VARIANT`;
- `_SEMANTIC.md` path;
- Audit PASS;
- validator PASS or validator unavailable;
- status policy and actual status action;
- no production document modifications;
- no out-of-scope writes;
- no failing cells.

## Component: skills/semantic-matrix-build/SKILL.md

---
name: semantic-matrix-build
description: Generate one deliverable-local semantic lens (_SEMANTIC.md) by adopting canonical matrices A and B and deriving C, F, D, K, G, X, T, and E with explicit semantic-algebra working.
compatibility: Chirality TASK generic shell; normally dispatched by ORCHESTRATOR setup pipeline Phase 2.3 with ScopePath set to one deliverable folder.
metadata:
  chirality-skill-version: "2"
  chirality-task-profile: NONE
---

### SKILL — semantic-matrix-build

#### Purpose

Generate `_SEMANTIC.md`, a deliverable-local semantic lens for one production unit.

The lens is **deliverable-conditioned**: `_CONTEXT.md` and production documents shape the vocabulary and perspective. The lens is **not deliverable-literal**: matrix cells are semantic categories, types, behaviors, and values, not restated requirements, implementation details, code clauses, file paths, event-name lists, numbers, or engineering judgments.

Each run starts from canonical Matrix A and Matrix B, then derives exactly these matrices in order:

`C, F, D, K, G, X, T, E`

The output is one file:

`{deliverable_folder}/_SEMANTIC.md`

#### Runtime shell

Use `TASK` in generic shell mode with `ScopePath` set to the deliverable folder. This skill is fully controlled by its brief and method contract.

Normal dispatch shape:

```yaml
TaskSkill: semantic-matrix-build
ScopePath: /absolute/path/to/one/deliverable-folder
RuntimeOverrides:
  deliverable_folder: /absolute/path/to/one/deliverable-folder
  decomposition_path: /absolute/path/to/decomposition.md
  DECOMP_VARIANT: SOFTWARE
  STATUS_POLICY: PRESERVE_CURRENT
```

#### Method boundary

This skill is a method pack loaded by TASK. It is not a persona agent.

The skill may narrow runtime behavior but must not widen the effective bounded task brief's write authorization. If TASK and this skill disagree about write authorization or tool use, the narrower instruction wins and the run report must surface the contradiction.

#### Precedence

1. TASK hard authorization boundary and active brief
2. This SKILL.md method contract
3. QA_CHECKS.md validity contract
4. TOOL_POLICY.md tool contract
5. BRIEF_SCHEMA.md dispatch examples

If instructions conflict, do not silently reconcile. Report the contradiction.

#### Inputs

##### Required

- `ScopePath` — TASK local scope root; must resolve to the same folder as `deliverable_folder`.
- `deliverable_folder` — absolute path to exactly one deliverable / production unit folder.
- `decomposition_path` — absolute path to the decomposition document used for traceability only.

##### Required runtime override

- `DECOMP_VARIANT` — `PROJECT`, `SOFTWARE`, or `DOMAIN`.

If absent, default to `PROJECT`, but report the default in the run report.

##### Status policy runtime override

`STATUS_POLICY` controls `_STATUS.md` behavior.

| Value | Meaning |
|---|---|
| `PRESERVE_CURRENT` | Default for ORCHESTRATOR Phase 2.3. Do not change lifecycle state. Record the ruling in `_SEMANTIC.md` and the run report. |
| `ADVANCE_ON_PASS` | On audit PASS, set or verify `Current State: SEMANTIC_READY`, but only if TASK write authorization allows `_STATUS.md` edits. |
| `NO_STATUS_TOUCH` | Do not edit `_STATUS.md` at all. Record status untouched in `_SEMANTIC.md` and the run report. |

If `STATUS_POLICY=ADVANCE_ON_PASS` but `_STATUS.md` editing is not authorized by TASK/brief, do not edit status. Report `NEEDS_HUMAN_RULING` or `FAILED_INPUTS` according to TASK's run-report convention.

#### Files to read

Read only inside `deliverable_folder`, except the decomposition document used for traceability.

Read in this order when present:

1. `_CONTEXT.md` — required. If missing, fail with `FAILED_INPUTS`.
2. `_STATUS.md` — lifecycle state and phase history.
3. `_REFERENCES.md` — source corpus and source-state warnings.
4. `_DEPENDENCIES.md` — dependency notes; do not infer blockers from it.
5. `MEMORY.md` — if absent, record `not present` in Inputs Read.
6. Production documents:
   - `PROJECT` / `SOFTWARE`: `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`
   - `DOMAIN`: all non-metadata `.md` files not prefixed with `_`, typically `Scoping.md` and `KA-*.md`

Missing production documents are recorded as absent; they do not fail the run. Do not read sibling deliverable folders. Do not compare across deliverables.

#### Write scope

May write only inside `deliverable_folder`:

- `_SEMANTIC.md` — primary output; overwrite allowed.
- `_STATUS.md` — only if `STATUS_POLICY` requires it and TASK/brief authorizes it.

Never modify production documents, `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `MEMORY.md`, or files outside the scope.

#### Deliverable perspective

Write a 1–3 sentence Perspective near the top of `_SEMANTIC.md`.

The Perspective must:

- name what the deliverable is for at a semantic level;
- identify the kinds of knowledge the lens must carry;
- include relevant source-state caveats at a category level when present;
- avoid engineering correctness claims;
- avoid exact code clauses, exact event-name lists, exact file paths, line numbers, implementation paths, and other particulars.

Good pattern:

> This deliverable frames the runtime boundary as a product-owned contract that keeps adapter behavior replaceable while preserving product-owned turn semantics. Its knowledge must carry API shape, adapter quarantine, event compatibility, conformance expectations, and unresolved source-state caveats without treating provider-specific details as public authority.

Bad patterns:

- Too generic: “This deliverable creates a semantic lens for knowledge work.”
- Too literal: “This deliverable validates `session:init`, `chat:delta`, and `/api/...` by implementing file X.”

#### Semantic product style

Final matrix cells must be:

- deliverable-conditioned;
- category-level, not requirement-level;
- one phrase only;
- 2–5 words;
- preferably 2–3 words when meaning remains complete;
- free of row/column axis labels;
- free of `∩`, `Σ`, unresolved `+`, or raw formula text.

Target style examples:

| Too generic | Too literal | Better |
|---|---|---|
| adequate evidence | SDK-backed adapter test output | runtime proof |
| complete record | route/SSE event preservation checklist | compatibility record |
| quality review | acceptance of exact PRD hash warning | source-state assurance |
| process audit | Section 8 harness CI premerge summary | summary integrity check |

#### Semantic algebra

##### Multiplication `*`

Semantic multiplication combines two semantic units into their intersection.

Examples:

- `sufficient * reason = justification`
- `necessary * condition = prerequisite`
- `practical * knowledge = skill`

##### Addition `+`

Semantic addition groups terms into a collection. It must not leak into final cell values.

##### Interpretation `I(r, c, L)`

Every list-valued cell must be interpreted into one atomic semantic unit.

For every interpreted cell, show exactly these three steps.

###### Step 1 — Axis anchor

Compute and resolve the axis product:

`a = r * c = <resolved anchor phrase>`

The anchor phrase should be semantic, not merely `<row>-<column> coordinate frame`.

Example:

`normative * necessity = binding need`

###### Step 2 — Projected contributors

For every contributor `t_n` in `L`, compute and resolve:

`p_n = a * t_n = <anchor phrase> * <contributor phrase> = <resolved projection phrase>`

A projection that only restates the formula is incomplete. Each projection must have a resolved phrase before Step 3.

Good:

`p1 = binding need * policy fact = rule entry`

Bad:

`p1 = (normative * necessity) * (policy threshold * essential fact)`

###### Step 3 — Centroid attractor

Select one final cell phrase:

`centroid selects <final phrase>`

The phrase must capture the shared semantic core of all resolved projections. It must not enumerate contributors.

#### Matrix construction rules

##### Matrix A — Orientation (canonical, 3×4)

Use these exact values. Do not derive or edit them.

| | **guiding** | **applying** | **judging** | **reviewing** |
|---|---|---|---|---|
| **normative** | prescriptive direction | mandatory practice | compliance determination | regulatory audit |
| **operative** | procedural direction | practical execution | performance assessment | process audit |
| **evaluative** | value orientation | merit application | worth determination | quality appraisal |

##### Matrix B — Conceptualization (canonical, 4×4)

Use these exact values. Do not derive or edit them.

| | **necessity** | **sufficiency** | **completeness** | **consistency** |
|---|---|---|---|---|
| **data** | essential fact | adequate evidence | comprehensive record | reliable measurement |
| **information** | essential signal | adequate context | comprehensive account | coherent message |
| **knowledge** | fundamental understanding | competent expertise | thorough mastery | coherent understanding |
| **wisdom** | essential discernment | adequate judgment | holistic insight | principled reasoning |

##### Matrix C — Formulation (3×4)

Columns: `necessity`, `sufficiency`, `completeness`, `consistency`  
Rows: `normative`, `operative`, `evaluative`

Formula:

`L_C(i,j) = Σ_k (A(i,k) * B(k,j))`  
`C(i,j) = I(row_i, col_j, L_C(i,j))`

##### Matrix F — Requirements (3×4)

Columns: `necessity`, `sufficiency`, `completeness`, `consistency`  
Rows: `normative`, `operative`, `evaluative`

Formula:

`L_F(i,j) = Σ_k (C(i,k) * B(k,j))`  
`F(i,j) = I(row_i, col_j, L_F(i,j))`

##### Matrix D — Objectives (3×4)

Columns: `guiding`, `applying`, `judging`, `reviewing`  
Rows: `normative`, `operative`, `evaluative`

Formula:

`L_D(i,j) = A(i,j) + (resolution * F(i,j))`  
`D(i,j) = I(row_i, col_j, L_D(i,j))`

For D, use exactly two contributors in `L_D`: the A cell and the resolution-transformed F cell.

##### Matrix K — Transpose of D (4×3)

Formula:

`K(i,j) = D(j,i)`

Rows: `guiding`, `applying`, `judging`, `reviewing`  
Columns: `normative`, `operative`, `evaluative`

##### Matrix G — Truncation of B (3×4)

Formula:

Remove the `wisdom` row from B.

Rows: `data`, `information`, `knowledge`  
Columns: `necessity`, `sufficiency`, `completeness`, `consistency`

##### Matrix X — Verification (4×4)

Rows: `guiding`, `applying`, `judging`, `reviewing`  
Columns: `necessity`, `sufficiency`, `completeness`, `consistency`

Formula:

`L_X(i,j) = Σ_k (K(i,k) * G(k,j))`  
`X(i,j) = I(row_i, col_j, L_X(i,j))`

##### Matrix T — Transpose of B (4×4)

Formula:

`T(i,j) = B(j,i)`

Rows: `necessity`, `sufficiency`, `completeness`, `consistency`  
Columns: `data`, `information`, `knowledge`, `wisdom`

##### Matrix E — Evaluation (4×4)

Rows: `guiding`, `applying`, `judging`, `reviewing`  
Columns: `data`, `information`, `knowledge`, `wisdom`

Formula:

`L_E(i,j) = Σ_k (X(i,k) * T(k,j))`  
`E(i,j) = I(row_i, col_j, L_E(i,j))`

#### Output format

Write `_SEMANTIC.md` in this order.

```markdown
### Semantic Lens: [ID] [Name]

**Generated:** [YYYY-MM-DD]
**DECOMP_VARIANT:** [PROJECT|SOFTWARE|DOMAIN]
**Perspective:** [1–3 sentences]
**Framework:** Chirality Semantic Algebra
**Audit:** [PASS|FAIL]
**Phase 2.3 Ruling:** [status policy statement]
**Inputs Read:**
- _CONTEXT.md — [SourceRef]
- _STATUS.md — [SourceRef or not present]
- _REFERENCES.md — [SourceRef or not present]
- _DEPENDENCIES.md — [SourceRef or not present]
- MEMORY.md — [SourceRef or not present]
- Datasheet.md — [SourceRef or absent]
- Specification.md — [SourceRef or absent]
- Guidance.md — [SourceRef or absent]
- Procedure.md — [SourceRef or absent]
- [DOMAIN files if applicable] — [SourceRef]

#### Matrix A — Orientation (3x4) — Canonical
[canonical table]

#### Matrix B — Conceptualization (4x4) — Canonical
[canonical table]

#### Matrix C — Formulation (3x4)
##### Construction: Dot product A · B
Intermediate collection and interpretation work for `L_C(i,j) = Σ_k (A(i,k) * B(k,j))`.
[work table]
##### Result
[result table]

#### Matrix F — Requirements (3x4)
...

#### Matrix D — Objectives (3x4)
...

#### Matrix K — Transpose of D (4x3)
...

#### Matrix G — Truncation of B (3x4)
...

#### Matrix X — Verification (4x4)
...

#### Matrix T — Transpose of B (4x4)
...

#### Matrix E — Evaluation (4x4)
...

---

#### Matrix Z — Summary Boundary

This delimiter prevents summary tables from being parsed as part of Matrix E result work. It is not a semantic matrix.

#### Matrix Summary

[All eight matrices C, F, D, K, G, X, T, E as compact markdown tables. No bullets. No derivation.]
```

##### Work table format

Use this table shape for C, F, D, X, and E:

| Cell | Intermediate collection | Step 1 - Axis anchor | Step 2 - Projected contributors | Step 3 - Centroid attractor |
|---|---|---|---|---|
| C[normative,necessity] | ... | `normative * necessity = binding need` | `p1 = binding need * directive fact = source mandate`; ... | centroid selects `policy threshold` |

Requirements:

- The Cell label may contain row and column names.
- The final Result cell value must not contain row or column names.
- Step 2 must resolve every projected contributor into a phrase.
- Step 3 must name exactly one final phrase.

#### SourceRef convention

Each `Inputs Read` line must use one of:

- absolute path + best-effort heading anchor;
- relative path + heading anchor when absolute path is unavailable;
- `not present`;
- `absent`;
- `location TBD` only when the file was read but no anchor can be determined.

Do not claim an input was read unless it was actually read.

#### Audit before acceptance

Before reporting success, audit all final cell values in:

- every Result table for C, F, D, K, G, X, T, and E;
- every Matrix Summary table.

Fail the run if any final cell:

1. is empty;
2. is not one phrase;
3. is under 2 words or over 5 words, except canonical B/G/T cells inherited from B;
4. exceeds about 80 characters;
5. contains `∩` or `Σ`;
6. contains unresolved `+` between semantic terms;
7. contains a literal row or column axis token for that cell;
8. contains implementation particulars, exact event names, file paths, code clauses, numeric requirements, equipment tags, or engineering correctness claims.

If audit fails:

- mark `_SEMANTIC.md` Audit as `FAIL` if the file is written;
- do not advance status;
- do not repair and re-audit in the same run;
- report failing matrix/cell/reason in the TASK run report.

#### Status handling

After audit:

- `STATUS_POLICY=PRESERVE_CURRENT`: do not change current lifecycle state. If `_STATUS.md` history edits are authorized, append a history note that semantic matrix was generated/validated and state was preserved by runtime policy. Otherwise only record this in `_SEMANTIC.md` and the run report.
- `STATUS_POLICY=ADVANCE_ON_PASS`: on audit PASS, set/verify `SEMANTIC_READY` only when `_STATUS.md` editing is authorized. On audit FAIL, leave state unchanged.
- `STATUS_POLICY=NO_STATUS_TOUCH`: do not edit `_STATUS.md`.

Never regress status.

#### Run report

TASK's normal run report must include:

- `RUN_STATUS`
- deliverable ID/name
- resolved `deliverable_folder`
- `DECOMP_VARIANT`
- `_SEMANTIC.md` path
- audit PASS/FAIL
- status policy and actual status action
- validator result if the repo validator was available and run
- missing inputs
- failing cells, if any
- confirmation that production documents were not modified

#### Validator

When running inside a repo that contains the validator and tool use is permitted, run:

```sh
python3 tools/validation/validate_semantic_matrix.py "{deliverable_folder}"
```

If the validator is unavailable, do not claim validator PASS. Report `validator not available`.

#### DOMAIN variant note

The skill can run on `DOMAIN` folders only when explicitly dispatched. Standard ORCHESTRATOR DOMAIN setup may skip semantic lensing entirely. If invoked for DOMAIN, read the Knowledge Type's non-metadata markdown documents and use DOMAIN terminology in the header and perspective. The matrix algebra remains unchanged.

## Component: skills/semantic-matrix-build/TOOL_POLICY.md

### semantic-matrix-build — Tool Policy

#### Tool posture

Reasoning-first. The semantic derivation is LLM-driven. Deterministic tools are used only for validation and filesystem safety when available.

The `allowed-tools` frontmatter field is intentionally omitted in `SKILL.md`. TASK and the run brief decide whether tool execution is restricted.

#### Preferred tool sequence

1. Read files inside `ScopePath` needed by the skill.
2. Generate `_SEMANTIC.md` by reasoning from the skill contract.
3. Run the semantic audit specified in `QA_CHECKS.md`.
4. If available and permitted, run:

```sh
python3 tools/validation/validate_semantic_matrix.py "{deliverable_folder}"
```

5. If available and permitted, run the semantic pipeline scope validator used by the project for Phase 2.3.
6. Write/update the TASK run record according to `AGENT_TASK.md`.

#### Allowed deterministic tools

##### TASK-enforced

None declared by this skill frontmatter. If the brief supplies `AllowedTools`, TASK enforces that list.

##### Operational helpers

| Tool | Use | Required? |
|---|---|---|
| `python3 tools/validation/validate_semantic_matrix.py` | Validate `_SEMANTIC.md` structure and matrix invariants. | Required in normal repo runs when available and permitted. |
| `python3 tools/validation/validate_semantic_pipeline_scope.py` | Confirm Phase 2.3 touched only allowed semantic-scope files. | Required when project ORCHESTRATOR policy calls for it and the tool is available. |

If a validator is unavailable, do not claim validator PASS. Report `validator not available`.

#### Expected use of reasoning

Reasoning is required for:

- deriving the deliverable perspective;
- choosing deliverable-conditioned but non-literal semantic phrases;
- resolving each axis anchor;
- resolving every projected contributor in Step 2;
- selecting centroid attractors;
- auditing final cells for semantic product validity.

#### Disallowed use

Do not use tools or scripts to bypass the semantic reasoning work. A generated table of formulas without resolved semantic phrases is invalid.

Do not:

- edit production documents;
- edit `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, or `MEMORY.md`;
- write outside the effective bounded task brief's authorization;
- scan sibling deliverables;
- claim cross-deliverable conclusions;
- claim engineering correctness;
- claim validator PASS unless the validator actually ran;
- hide conflicts between TASK write authorization, brief instructions, and skill requirements.

#### Write boundary

Allowed write target:

- `{deliverable_folder}/_SEMANTIC.md`

Conditional write target:

- `{deliverable_folder}/_STATUS.md` only when both conditions are true:
  1. the brief/runtime override requires a status action; and
  2. TASK/brief write authorization allows `_STATUS.md` edits.

Normal ORCHESTRATOR Phase 2.3 uses `STATUS_POLICY=PRESERVE_CURRENT`; it may write only `_SEMANTIC.md` unless the brief explicitly authorizes a history note.

#### Fallback rules

| Situation | Required fallback |
|---|---|
| Validator unavailable | Complete semantic audit manually; report validator unavailable. |
| `_CONTEXT.md` missing | Fail with `FAILED_INPUTS`. |
| Production document missing | Record as absent in Inputs Read; continue. |
| Status edit requested but unauthorized | Do not edit `_STATUS.md`; report the contradiction. |
| Tool output contradicts the file content | Report discrepancy; do not hide it. |
| Brief asks for out-of-scope writes | Refuse those writes and report scope violation. |
