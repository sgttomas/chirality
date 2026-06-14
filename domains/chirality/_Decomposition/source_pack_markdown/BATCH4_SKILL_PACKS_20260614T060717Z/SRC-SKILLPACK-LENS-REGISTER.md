# Source Pack: Skill pack: lens-register

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/lens-register/BRIEF_SCHEMA.md

### lens-register — Brief Schema

#### Dispatch role

`lens-register` is the normal ORCHESTRATOR Phase 2.4 setup-pipeline skill for PROJECT / SOFTWARE semantic lensing. It is dispatched through TASK as a bounded method pack. It reads one deliverable folder, parses `_SEMANTIC.md`, scans production documents, and writes `_SEMANTIC_LENSING.md`.

Use TASK generic shell for normal ORCHESTRATOR dispatch. This skill supplies its own method contract and write-boundary requirements, and the brief must authorize `_SEMANTIC_LENSING.md` writes.

#### Required

- `ScopePath` — absolute path to one production unit folder; this is the TASK-normalized scope root.
- `TaskSkill` — `lens-register`.
- `RuntimeOverrides.deliverable_folder` — same absolute path as `ScopePath`; this is the skill's explicit scope anchor.
- `_SEMANTIC.md` must exist in the deliverable folder. If absent, the skill writes a blocking `_SEMANTIC_LENSING.md` header and stops.

#### Recommended

- `RuntimeOverrides.DECOMP_VARIANT` — `PROJECT` | `SOFTWARE` (default `PROJECT`).
- `RuntimeOverrides.STATUS_POLICY` — `NO_STATUS_TOUCH` for normal Phase 2.4.
- `AllowedWriteTargets` — include only:
  - `{deliverable_folder}/_SEMANTIC_LENSING.md`
  - `{deliverable_folder}/_run_records/` (TASK shell output)

#### Optional / compatibility aliases

- `deliverable_folder` may be provided as a top-level legacy field, but `RuntimeOverrides.deliverable_folder` is preferred.
- `DeliverablePath` is accepted only as a compatibility alias when an existing caller provides it. It does not affect TASK write authorization.
- `DECOMP_VARIANT` may be provided top-level or in `RuntimeOverrides`; runtime override wins.

#### Unsupported

- `DECOMP_VARIANT=DOMAIN` is not supported. DOMAIN pipelines skip semantic lensing. The skill refuses gracefully and does not write `_SEMANTIC_LENSING.md`.
- Multi-deliverable scope is not accepted.
- Cross-deliverable scanning is not accepted.
- Following external references from `_REFERENCES.md` is not accepted unless a separate explicitly authorized task provides those sources as in-scope inputs.

#### Canonical ORCHESTRATOR Phase 2.4 brief

```markdown
PURPOSE: Generate the deliverable-local semantic lensing register for one production unit.
RequestedBy: ORCHESTRATOR

ScopePath: {DELIVERABLE_PATH}
TaskSkill: lens-register

Tasks:
  - Load `skills/lens-register/SKILL.md` and companion files.
  - Read `_SEMANTIC.md` and the production documents for this deliverable.
  - Parse only primary Result tables for matrices A, B, C, F, D, X, E.
  - Generate or overwrite `{DELIVERABLE_PATH}/_SEMANTIC_LENSING.md`.
  - Run lens-register QA and validator when available.

ApplyEdits: true
AllowedWriteTargets:
  - {DELIVERABLE_PATH}/_SEMANTIC_LENSING.md
  - {DELIVERABLE_PATH}/_run_records/

RuntimeOverrides:
  DECOMP_VARIANT: {PROJECT|SOFTWARE}
  deliverable_folder: {DELIVERABLE_PATH}
  STATUS_POLICY: NO_STATUS_TOUCH

CustomInstructions:
  - Treat `_SEMANTIC.md` as a lens source, not an authority.
  - Ignore Matrix Summary, Matrix Z, derivation tables, and structural matrices K, G, T.
  - Keep production documents, `_SEMANTIC.md`, and `_STATUS.md` read-only.
  - Record only warranted items with SourcePath and SectionRef.
  - Use lens-specific `NO_ITEMS` notes; do not repeat boilerplate.
  - Do not follow external references outside the deliverable folder.
  - Do not claim `validate_lens_register.py` PASS unless the validator actually ran.

ExpectedOutputs:
  - `{DELIVERABLE_PATH}/_SEMANTIC_LENSING.md`
  - `{DELIVERABLE_PATH}/_run_records/TASK_RUN_*.md`
```

#### Files the skill expects to find in scope

Required:
- `_SEMANTIC.md` — source of lens matrices A, B, C, F, D, X, E.

Recommended / contextual:
- `_CONTEXT.md` — deliverable identity.
- `_STATUS.md` — read-only lifecycle state.
- `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md` — standard production document set. Missing docs produce `[WARNING] MISSING_DOC`, not failure.
- `_REFERENCES.md` — deliverable-local metadata only; list pointers but do not expand them.

#### Output location

- `{deliverable_folder}/_SEMANTIC_LENSING.md` — overwritten each run.
- `{deliverable_folder}/_run_records/TASK_RUN_*.md` — TASK shell run record, not a skill-authored output.

## Component: skills/lens-register/QA_CHECKS.md

### lens-register — QA Checks

#### Minimum checks for a valid run

1. `ScopePath` exists and is a readable directory.
2. `deliverable_folder` resolves to the same directory as `ScopePath`.
3. `_SEMANTIC.md` is present in the deliverable folder, or the output is a blocking header file and the run stops.
4. `DECOMP_VARIANT` is `PROJECT`, `SOFTWARE`, or absent (default `PROJECT`). `DOMAIN` is refused.
5. `_SEMANTIC_LENSING.md` is written to `{deliverable_folder}/_SEMANTIC_LENSING.md` unless the run is refused before output or fails input validation.
6. No production documents were modified.
7. `_SEMANTIC.md` was not modified.
8. `_STATUS.md` was not modified (`STATUS_POLICY=NO_STATUS_TOUCH`).
9. No files outside `{deliverable_folder}/` were read or written, except TASK's own run-record handling inside `{deliverable_folder}/_run_records/`.
10. If `python3 tools/validation/validate_lens_register.py {deliverable_folder}` is available and permitted, it passes before the run reports validator PASS.
11. If the validator is unavailable or not permitted, the run reports `Validator: NOT_RUN` and does not claim validator PASS.

#### Structural invariants

| # | Check | Validation |
|---|---|---|
| 1 | **Matrix coverage complete** | Every cell of each lensed matrix A, B, C, F, D, X, E has a Lens Coverage entry. |
| 2 | **Structural matrices excluded** | K, G, and T are not lensed; they are transposes/truncations and would duplicate D/B coverage. |
| 3 | **Primary result tables only** | Lenses are parsed from primary Result tables, not derivation tables, Matrix Summary, Matrix Z, or compact summary duplicates. |
| 4 | **No invention** | Warranted items are grounded in production-document evidence or explicit absence. |
| 5 | **Provenance present** | Every warranted item has `SourcePath` + `SectionRef` or accepted absence wording. |
| 6 | **Conflicts surfaced** | Conflict items have two or more contenders and `HumanRuling=TBD`. |
| 7 | **Summary consistent** | Summary counts match the actual warranted items in the file. |
| 8 | **Schema followed** | Output uses the exact STRUCTURE schema and required column order. |
| 9 | **One deliverable per run** | The run processes exactly one deliverable folder; no cross-deliverable scanning. |
| 10 | **Read-only protected files** | Production docs, `_SEMANTIC.md`, and `_STATUS.md` are not modified. |
| 11 | **Lens-specific no-item notes** | `NO_ITEMS` rows explain the specific lens/document-role outcome; repeated boilerplate is invalid. |

A run failing any required invariant is invalid, except where failure behavior explicitly defines a blocking/refusal output.

#### Matrix parsing rules

The skill must parse `_SEMANTIC.md` as follows:

- Process only these matrices: A, B, C, F, D, X, E.
- Ignore structural matrices K, G, T.
- Ignore `Matrix Z — Summary Boundary` if present.
- Ignore `Matrix Summary` and all compact summary tables/lists.
- Ignore derivation-work tables and intermediate collections.
- Use the first complete `### Result` table inside each required matrix section as the authoritative lens table.
- If a matrix Result table is missing, malformed, or has empty cells, create `MATRIX_ERROR` coverage rows and `Type=MatrixError` items referencing `_SEMANTIC.md`.

#### Schema compliance

- **File header:** present with `Generated`, `Deliverable Folder`, `DECOMP_VARIANT`, `StatusPolicy`, `Validator`, `Inputs Read`, `Purpose`, and `Warnings` when applicable.
- **Summary block:** present before any matrix section. Counts are integers (0 permitted).
- **Matrix sections:** one per matrix in fixed order A, B, C, F, D, X, E. Each contains:
  - a **Lens Coverage** table with one row per matrix cell, row-major;
  - a **Warranted Items** table only when at least one item exists for that matrix.
- **Lens Coverage columns:** `LensKey`, `RowLabel`, `ColLabel`, `LensValue`, `ItemCount`, `CoverageStatus`, `Notes`.
- **Warranted Items columns:** `ItemID`, `LensKey`, `Type`, `AppliesToDoc`, `SuggestedEditDoc`, `CandidateInfo`, `WhyWarranted`, `SourcePath`, `SectionRef`, `Contenders`, `ProposedAuthority (PROPOSAL)`, `HumanRuling`.
- **CoverageStatus enum:** `NO_ITEMS` | `HAS_ITEMS` | `MATRIX_ERROR`.
- **Type enum:** `MissingSlot` | `WeakStatement` | `Conflict` | `VerificationGap` | `RationaleGap` | `Normalization` | `TBD_Question` | `MatrixError`.

#### NO_ITEMS note discipline

Every `NO_ITEMS` row must contain a lens-specific note. Invalid boilerplate includes:

- `No warranted items found.`
- `No issues.`
- `N/A.`

Valid examples:

- `Requirement and verification roles already align under this lens.`
- `Datasheet attributes already cover the descriptive role; no gap detected.`
- `Guidance rationale is present and consistent with procedure checks.`
- `No production document presented a conflict or missing slot for this lens.`

#### No-invention rule

- Every warranted item must cite evidence from production documents or explicitly record absence.
- Speculative or unsupported content must become `Type=TBD_Question`.
- The skill must not introduce new numeric values, new normative requirements, or acceptance claims.
- The skill must not claim compliance with a standard whose text is not present.
- `_SEMANTIC.md` and `_SEMANTIC_LENSING.md` are not evidence sources for engineering facts.

#### Human decision rights

- Conflicts are surfaced, not resolved.
- `HumanRuling` is always `TBD` unless a pre-existing human ruling is citable.
- `ProposedAuthority` is always `PROPOSAL`; never authoritative.

#### Unsupported variants

`DECOMP_VARIANT=DOMAIN` is not supported. If passed:

- Do not write `_SEMANTIC_LENSING.md`.
- Do not modify any file.
- Return `RUN_STATUS=REFUSED` with the message: `DECOMP_VARIANT=DOMAIN is not supported by lens-register; DOMAIN pipelines skip the semantic lensing step.`

#### Failure reporting

- If `_SEMANTIC.md` is missing: write `_SEMANTIC_LENSING.md` with a blocking header: `Missing _SEMANTIC.md; run semantic-matrix-build first (ORCHESTRATOR Phase 2.3)` and stop. Report `RUN_STATUS=BLOCKED`.
- If `{deliverable_folder}` does not exist or is not readable: report `RUN_STATUS=FAILED_INPUTS`; do not write.
- If a production document is missing: record `[WARNING] MISSING_DOC: <filename>` in the output header and continue.
- If a matrix cell is empty or malformed: set `CoverageStatus=MATRIX_ERROR`, add a `Type=MatrixError` item, and continue.
- If validator is unavailable: report `Validator: NOT_RUN`; do not call the run validator-passed.
- If validator fails: report `RUN_STATUS=FAILED` with validator errors.

#### Success case

A clean run reports:

- `RUN_STATUS=OK`
- Deliverable ID/name
- `_SEMANTIC.md` was present and parsed from primary Result tables
- Count of warranted items total + by document + by matrix + by type
- Matrix parsing errors, missing docs, and conflicts, if any
- Path to `_SEMANTIC_LENSING.md`
- `Validator: PASS` or `Validator: NOT_RUN — <reason>`
- `_STATUS.md` unchanged
- No production documents modified

#### Evidence required for each item

| Type | Minimum evidence |
|---|---|
| `Conflict` | Two+ `path#section` entries in `Contenders`; `HumanRuling=TBD`. |
| `VerificationGap` | Citation of the normative requirement whose acceptance is missing/ambiguous. |
| `MissingSlot` | Doc(s) searched in `SourcePath`; section or `entire document scanned` in `SectionRef`. |
| `WeakStatement` | Doc+section citation for ambiguous language. |
| `RationaleGap` | Doc+section citation for decision/requirement lacking rationale. |
| `Normalization` | Two+ locations where terminology diverges. |
| `TBD_Question` | Rationale and who/what to consult in `CandidateInfo`. |
| `MatrixError` | Reference to the affected cell in `_SEMANTIC.md`. |

## Component: skills/lens-register/SKILL.md

---
name: lens-register
description: Generate a matrix-organized, coverage-complete semantic lensing register (_SEMANTIC_LENSING.md) from _SEMANTIC.md + production documents. Setup-pipeline companion to the interactive semantic-lensing skill.
compatibility: Chirality TASK; dispatched by ORCHESTRATOR setup pipeline (Phase 2.4).
metadata:
  chirality-skill-version: "2"
  chirality-task-profile: NONE
---

### SKILL — lens-register

#### Purpose

Produce a **matrix-organized lensing register** (`_SEMANTIC_LENSING.md`) that:

1. Uses each primary Result-table cell of matrices **A, B, C, F, D, X, E** from `_SEMANTIC.md` as a lens,
2. Applies each lens to the deliverable-local production documents, and
3. Records only warranted enrichment inputs with provenance, without rewriting the documents.

This is the **setup-pipeline, coverage-complete** contract in the semantic-lensing family. It is the normal ORCHESTRATOR Phase 2.4 skill. Its interactive counterpart is `semantic-lensing`, which produces human-facing proposals or reviews existing register entries. `lens-register` creates the register; `four-documents` Pass 3 consumes the register.

#### Suitable agent shells

- `TASK` generic shell, no profile.

Typical dispatcher: ORCHESTRATOR Phase 2.4 dispatches TASK with `TaskSkill: lens-register`, `ScopePath={DELIVERABLE_PATH}`, `RuntimeOverrides.deliverable_folder={DELIVERABLE_PATH}`, and write authorization for `_SEMANTIC_LENSING.md`.

#### Inputs

##### Required

- `ScopePath` — absolute path to one production unit folder.
- `deliverable_folder` — absolute path to the same folder, normally supplied in `RuntimeOverrides`.
- `_SEMANTIC.md` in the deliverable folder.

##### Optional

- `DECOMP_VARIANT` — `PROJECT` | `SOFTWARE` (default `PROJECT`). `DOMAIN` is not supported.
- `STATUS_POLICY` — default `NO_STATUS_TOUCH`.
- `DeliverablePath` — compatibility alias only; does not affect TASK write authorization.

##### Files read

Required:
- `{deliverable_folder}/_SEMANTIC.md` — source for lenses.

Contextual, read when present:
- `{deliverable_folder}/_CONTEXT.md`
- `{deliverable_folder}/_STATUS.md`
- `{deliverable_folder}/Datasheet.md`
- `{deliverable_folder}/Specification.md`
- `{deliverable_folder}/Guidance.md`
- `{deliverable_folder}/Procedure.md`
- `{deliverable_folder}/_REFERENCES.md` — metadata only; do not follow external paths.

Missing production documents produce warnings, not failure.

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `deliverable_folder` | Skill-local scope anchor | required | absolute path equal to `ScopePath` |
| `DECOMP_VARIANT` | Decomposition pipeline variant | `PROJECT` | `PROJECT`, `SOFTWARE` |
| `STATUS_POLICY` | Lifecycle handling | `NO_STATUS_TOUCH` | `NO_STATUS_TOUCH` |

`DECOMP_VARIANT=DOMAIN` is refused because DOMAIN pipelines skip semantic lensing.

#### Tool usage

Reasoning-first generation. Deterministic validation is optional but expected when the validator exists and the brief permits it.

- No deterministic tool is required to generate `_SEMANTIC_LENSING.md`.
- Optional validators may be used after generation:
  - `python3 tools/validation/validate_lens_register.py {deliverable_folder}`
  - `python3 tools/validation/validate_semantic_pipeline_scope.py {deliverable_folder} --step lens`
- Do not claim validator PASS unless the validator actually ran and passed.

The `allowed-tools` frontmatter field is intentionally omitted; TASK may still enforce a brief-provided allowlist.

#### Outputs

Skill-authored output:

- `{deliverable_folder}/_SEMANTIC_LENSING.md` — overwritten each run.

TASK shell output:

- `{deliverable_folder}/_run_records/TASK_RUN_*.md` — TASK run record.

#### Non-negotiable invariants

- **One deliverable per run.** Operate on exactly one folder.
- **Read-only production documents.** Do not edit `Datasheet.md`, `Specification.md`, `Guidance.md`, or `Procedure.md`.
- **Read-only `_SEMANTIC.md`.** It is a lens source, not an output target or engineering authority.
- **Read-only `_STATUS.md`.** Normal Phase 2.4 policy is `NO_STATUS_TOUCH`.
- **No external expansion.** Do not follow `_REFERENCES.md` paths or read outside the deliverable folder.
- **Use lenses, not authority.** Matrix cells shape what to look for; they do not justify inventing content.
- **No invention.** Unknowns become `TBD_Question`; gaps become `MissingSlot`; conflicts become `Conflict`.
- **Provenance required.** Every warranted item has `SourcePath` and `SectionRef` or explicit absence provenance.
- **Conflicts surfaced, not resolved.** `HumanRuling=TBD` unless a prior human ruling is cited.
- **Matrix coverage complete.** Every cell in A, B, C, F, D, X, E appears in Lens Coverage.
- **Structural matrices excluded.** K and T are transposes; G is a truncation. They are not lensed because doing so duplicates D/B coverage.
- **Parser hygiene.** Ignore derivation tables, Matrix Summary, and Matrix Z. Parse only primary Result tables.
- **No boilerplate NO_ITEMS.** Notes must be lens-specific.

#### Precedence

1. **PROTOCOL** governs sequencing and run behavior.
2. **SPEC** governs validity.
3. **STRUCTURE** defines output schema.
4. **RATIONALE** governs interpretation when ambiguity remains.

If instructions conflict, flag the conflict and return it to the invoker.

#### Glossary

| Term | Meaning |
|---|---|
| Lens | A matrix Result-table cell used as a question-shaping perspective. |
| LensKey | Canonical identifier: `M:[RowLabel]:[ColLabel]`. |
| Warranted item | A grounded gap, conflict, weak statement, normalization risk, rationale gap, verification gap, or TBD question. |
| Production documents | `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`. |
| Structural matrices | K, G, T; excluded from lensing because they duplicate predecessor content. |

---

#### PROTOCOL — Straight-through lens-register procedure

##### Step 0 — Safety checks

1. Resolve `ScopePath` and `deliverable_folder`; they must identify the same readable directory.
2. If `DECOMP_VARIANT=DOMAIN`, refuse gracefully and do not write files.
3. Confirm `_SEMANTIC.md` exists.
   - If missing, write `_SEMANTIC_LENSING.md` with a blocking header and stop.
4. Confirm production documents exist.
   - Missing production documents produce `[WARNING] MISSING_DOC: <filename>` and the run proceeds with available documents.
5. Confirm no write target outside `_SEMANTIC_LENSING.md` and TASK `_run_records/` is required.

##### Step 1 — Read context and inputs

Read, in order:

1. `_CONTEXT.md` if present.
2. `_STATUS.md` if present; record state but do not change it.
3. `_SEMANTIC.md`.
4. Existing production documents.
5. `_REFERENCES.md` if present; list as metadata only and do not follow external paths.

##### Step 2 — Parse matrices into a lens inventory

For each matrix `M ∈ {A, B, C, F, D, X, E}`:

1. Locate the matrix section.
2. Locate the first primary `### Result` table in that section.
3. Extract row labels, column labels, and cell values.
4. Create one Lens Coverage row per cell, row-major:
   - `LensKey = M:[RowLabel]:[ColLabel]`
   - `LensValue = cell value`
   - `ItemCount=0`
   - `CoverageStatus=NO_ITEMS`
   - `Notes=<lens-specific initial note>`

Ignore:

- derivation/intermediate work tables;
- Matrix Summary;
- Matrix Z;
- structural matrices K, G, T.

If a required matrix or cell is malformed, record `MATRIX_ERROR` and continue.

##### Step 3 — Apply lenses and record warranted items

For each `LensKey`:

1. Scan the production documents.
2. Ask: what gap, conflict, ambiguity, missing verification, missing rationale, or terminology risk becomes salient under this lens?
3. Record an item only when it meets the warranted threshold.
4. Update `ItemCount`, `CoverageStatus`, and `Notes`.

Warranted item types:

- `Conflict`
- `VerificationGap`
- `MissingSlot`
- `WeakStatement`
- `RationaleGap`
- `Normalization`
- `TBD_Question`
- `MatrixError`

Tight filter:

- Do not record restatements.
- Do not pad the register for coverage.
- Do not create items simply because a lens exists.
- If documents are already clear and aligned under a lens, record `NO_ITEMS` with a specific note.

##### Step 4 — Write `_SEMANTIC_LENSING.md`

Write or overwrite `{deliverable_folder}/_SEMANTIC_LENSING.md` using the STRUCTURE schema.

##### Step 5 — QA and optional validation

1. Confirm protected files were not modified.
2. Confirm coverage completeness and schema compliance.
3. Run `validate_lens_register.py` if available and permitted.
4. Report validator status as `PASS`, `FAILED`, or `NOT_RUN`.
5. Return run report to TASK/ORCHESTRATOR.

---

#### SPEC — Validity requirements

##### S1 — Coverage completeness

Every cell of A, B, C, F, D, X, and E must appear in Lens Coverage. Zero-item cells are valid when their notes are lens-specific.

##### S2 — No invention

A warranted item must be grounded in production-document evidence or explicit absence. Use `TBD_Question` when required information is absent or external.

##### S3 — Provenance

Every warranted item includes:

- `SourcePath`;
- `SectionRef`;
- `Contenders` when conflict exists.

##### S4 — Human decision rights

The skill must not choose a winner, introduce requirements, or assert compliance. Human rulings remain `TBD` unless already citable.

##### S5 — Output stability

Output must use stable ordering and exact table schemas.

##### S6 — Scope discipline

The run must not read sibling deliverables or external references; `_REFERENCES.md` is metadata only.

##### S7 — Status discipline

`_STATUS.md` is not changed by `lens-register`.

---

#### STRUCTURE — Output file schema

##### File header

```markdown
### Semantic Lensing Register: [Production Unit ID] [Name]

**Generated:** [YYYY-MM-DD]
**DECOMP_VARIANT:** [PROJECT|SOFTWARE]
**Deliverable Folder:** [path]
**StatusPolicy:** NO_STATUS_TOUCH
**Validator:** PASS | FAILED | NOT_RUN — [reason]
**Warnings:** [optional warning list]

**Inputs Read:**
- _CONTEXT.md — [SourceRef or not present]
- _STATUS.md — [SourceRef or not present]
- _SEMANTIC.md — [SourceRef]
- Datasheet.md — [SourceRef or missing]
- Specification.md — [SourceRef or missing]
- Guidance.md — [SourceRef or missing]
- Procedure.md — [SourceRef or missing]
- _REFERENCES.md — [SourceRef or not present / not read]

**Purpose:** Apply semantic-matrix-build Result-table cells as lenses over production documents, capturing warranted enrichment inputs for a later enrichment pass.
```

##### Summary block

```markdown
#### Summary

- Total warranted items: N
- By document:
  - Datasheet: n
  - Specification: n
  - Guidance: n
  - Procedure: n
  - Multi: n
  - NA: n
- By matrix:
  - A: n
  - B: n
  - C: n
  - F: n
  - D: n
  - X: n
  - E: n
- By type:
  - Conflict: n
  - VerificationGap: n
  - MissingSlot: n
  - WeakStatement: n
  - RationaleGap: n
  - Normalization: n
  - TBD_Question: n
  - MatrixError: n
- Notable conflicts: n
- Matrix parse errors: n
```

##### Matrix sections

For each matrix in order: A, B, C, F, D, X, E.

```markdown
#### Matrix M — [Matrix Name]

##### Lens Coverage
| LensKey | RowLabel | ColLabel | LensValue | ItemCount | CoverageStatus | Notes |
|---|---|---|---|---:|---|---|
| M:[r]:[c] | r | c | ... | 0 | NO_ITEMS | lens-specific note |

##### Warranted Items
| ItemID | LensKey | Type | AppliesToDoc | SuggestedEditDoc | CandidateInfo | WhyWarranted | SourcePath | SectionRef | Contenders | ProposedAuthority (PROPOSAL) | HumanRuling |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | A:[r]:[c] | VerificationGap | Specification | Specification | Add acceptance criteria for ... | ... | ... | ... | ... | PROPOSAL | TBD |
```

Omit `### Warranted Items` for a matrix only when no warranted items exist for that matrix.

###### Lens Coverage columns

- `LensKey`: `M:[RowLabel]:[ColLabel]`
- `RowLabel`: row label from matrix Result table
- `ColLabel`: column label from matrix Result table
- `LensValue`: cell value
- `ItemCount`: integer count of warranted items for the lens
- `CoverageStatus`: `NO_ITEMS` | `HAS_ITEMS` | `MATRIX_ERROR`
- `Notes`: lens-specific note; no boilerplate

###### Warranted Items columns

- `ItemID`: unique within file, recommended `{Matrix}-{000}`.
- `LensKey`: matching Lens Coverage key.
- `Type`: one allowed item type.
- `AppliesToDoc`: `Datasheet` | `Specification` | `Guidance` | `Procedure` | `Multi` | `NA`.
- `SuggestedEditDoc`: best-fit later enrichment target, or `TBD` / `NA`.
- `CandidateInfo`: short enrichment-ready phrasing; not full prose.
- `WhyWarranted`: 1–2 sentence rationale.
- `SourcePath`: file path(s) searched or cited.
- `SectionRef`: heading anchor, `location TBD`, or `entire document scanned`.
- `Contenders`: two or more `path#section` entries for conflicts; blank otherwise.
- `ProposedAuthority (PROPOSAL)`: always `PROPOSAL` for proposed authority placement.
- `HumanRuling`: `TBD` unless a prior human ruling is cited.

##### SuggestedEditDoc heuristic

- `VerificationGap` → `Specification` and/or `Procedure`.
- `RationaleGap` → `Guidance`.
- `Normalization` → `Guidance` plus affected documents as needed.
- `WeakStatement` → same document where the ambiguity appears unless role placement suggests otherwise.
- `MissingSlot` → best-fit document role or `TBD`.
- `Conflict`, `TBD_Question`, `MatrixError` → `NA` or `TBD`.

##### SourceRef convention

Use file path + best-effort heading anchors, or `location TBD`. SourceRefs record traceability; they do not make matrices authoritative.

---

#### RATIONALE

`_SEMANTIC.md` partitions the deliverable's semantic space. `lens-register` turns those partitions into a bounded, evidence-linked worklist for later enrichment without editing the production documents.

Value hierarchy:

1. Provenance and no invention
2. Scope discipline
3. Coverage completeness
4. Register usability
5. Semantic density

#### QA expectations

See `QA_CHECKS.md`.

#### See also

- `skills/semantic-matrix-build/SKILL.md` — produces `_SEMANTIC.md`
- `skills/semantic-lensing/SKILL.md` — interactive proposal workflow consuming this register
- `skills/four-documents/SKILL.md` — Pass 3 consumer of `_SEMANTIC_LENSING.md`
- `agents/AGENT_ORCHESTRATOR.md` — dispatches this skill via TASK in Phase 2.4

## Component: skills/lens-register/TOOL_POLICY.md

### lens-register — Tool Policy

#### Preferred tool order

Reasoning-first generation, validator-last when available.

1. Read deliverable-local inputs inside `ScopePath` / `deliverable_folder`.
2. Generate `_SEMANTIC_LENSING.md` by reasoning over `_SEMANTIC.md` lenses and production documents.
3. Run optional validation tools when present and permitted by the TASK brief.
4. Report validator status honestly.

#### Allowed deterministic tools

##### TASK-enforced

No `allowed-tools` frontmatter is declared. TASK may still enforce an allowlist supplied by the brief.

##### Operationally invoked

No deterministic tools are required for generation.

Optional validators / read-only checkers may be used when they exist in the repository and are permitted by the brief, especially:

- `python3 tools/validation/validate_lens_register.py {deliverable_folder}`
- `python3 tools/validation/validate_semantic_pipeline_scope.py {deliverable_folder} --step lens`

Do not claim validator PASS unless the validator actually ran and returned PASS. If the validator is unavailable or not allowed, report `Validator: NOT_RUN — <reason>`.

#### Expected use of reasoning

This is an LLM-driven lensing-register skill. The agent reasons over:

- `_SEMANTIC.md` primary Result tables for matrices A, B, C, F, D, X, E;
- deliverable-local production documents;
- `_CONTEXT.md`, `_STATUS.md`, and `_REFERENCES.md` as local metadata only.

The skill treats matrix cells as lenses, not authorities. It records warranted gaps, conflicts, weak statements, normalization risks, and questions; it does not rewrite production documents.

#### Disallowed use

- Do not modify production documents (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`).
- Do not modify `_SEMANTIC.md`.
- Do not modify `_STATUS.md`; normal policy is `STATUS_POLICY=NO_STATUS_TOUCH`.
- Do not read, compare, or scan sibling deliverables.
- Do not follow external source paths from `_REFERENCES.md` during normal runs.
- Do not treat `_SEMANTIC.md` as engineering authority.
- Do not invent facts, numeric values, requirements, or acceptance claims.
- Do not claim validator PASS unless the validator actually ran.

#### Write boundary

Skill-authored output:

- `{deliverable_folder}/_SEMANTIC_LENSING.md` only.

TASK shell output:

- `{deliverable_folder}/_run_records/TASK_RUN_*.md` may be created or updated by TASK. This is not a skill-authored output and is allowed when TASK executes the skill.

Read-only:

- `_SEMANTIC.md`
- `_STATUS.md`
- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md` / `Dependencies.csv` if present
- all production documents

No other writes are allowed unless a future human-approved skill revision explicitly changes the contract.
