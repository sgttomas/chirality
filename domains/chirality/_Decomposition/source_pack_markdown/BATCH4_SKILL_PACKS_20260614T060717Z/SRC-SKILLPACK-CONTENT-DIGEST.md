# Source Pack: Skill pack: content-digest

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/content-digest/BRIEF_SCHEMA.md

### BRIEF SCHEMA — content-digest

This file defines the INIT-TASK dispatch contract for `TASK + content-digest`.

#### Purpose

Use this skill when EVALUATION needs one structured digest for one deliverable folder.

#### Scope model

- `ScopePath` should normally be the execution root.
- `AllowedWriteTargets` should be limited to the intended digest output path under `_Evaluation/content-digests/`.

#### Required brief fields

| Field | Type | Meaning | Example |
|---|---|---|---|
| `PURPOSE` | string | Why this digest run exists | `Produce a content digest for DEL-014-03.` |
| `ScopePath` | path | Execution root | `/repo/execution/` |
| `TaskSkill` | string | Must equal the skill folder/name | `content-digest` |
| `AllowedWriteTargets` | list[path] | Digest output path | `[/repo/execution/_Evaluation/content-digests/PKG-014/DEL-014-03.md]` |
| `RuntimeOverrides.DELIVERABLE_PATH` | path | Target deliverable folder | `/repo/execution/PKG-014/DEL-014-03_Compressor-Controls/` |
| `RuntimeOverrides.OUTPUT_PATH` | path | Digest output file | `/repo/execution/_Evaluation/content-digests/PKG-014/DEL-014-03.md` |
| `ExpectedOutputs` | list[path] | Expected single digest file | `[/repo/execution/_Evaluation/content-digests/PKG-014/DEL-014-03.md]` |

#### Optional brief fields

This skill currently defines no optional runtime overrides.

#### Runtime-override guidance

- `DELIVERABLE_PATH` must identify exactly one deliverable folder.
- `OUTPUT_PATH` must already have an existing parent directory under `_Evaluation/content-digests/`.
- The run must remain single-deliverable and read-only on production files.

## Component: skills/content-digest/QA_CHECKS.md

### QA CHECKS — content-digest

#### Minimum output validity checks

1. Exactly one digest file is written to `OUTPUT_PATH`.
2. The digest contains all seven required sections in the required order.
3. Identity fields come from `_CONTEXT.md` or are explicitly marked absent; they are not invented.
4. Dependency counts and key upstream/downstream items are derived from deliverable-local files only.
5. Quality observations are specific factual flags rather than vague judgments.
6. No file in `DELIVERABLE_PATH` is modified.
7. No file outside the specified deliverable folder is read.

#### Failure reporting expectations

Use `FAILED_INPUTS` when:
- `DELIVERABLE_PATH` is missing or not a directory,
- the parent directory of `OUTPUT_PATH` does not exist.

Absent deliverable-local files should not fail the run by themselves; they should be reported as missing in the digest.

## Component: skills/content-digest/SKILL.md

---
name: content-digest
description: Read one deliverable folder and produce a structured 7-section content digest summarizing identity, scope, document kit, dependencies, references, semantic framework, and quality observations.
compatibility: Chirality TASK; dispatched by EVALUATION for per-deliverable evidence aggregation
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — content-digest

#### Purpose

Read the contents of a single deliverable folder and produce a structured content digest summarizing the deliverable's identity, scope, document kit, dependencies, references, semantic framework, and quality observations.

This is a bounded, semantic-matching extraction skill. It reads deliverable-local files and extracts structured information directly; it does not perform engineering judgment or cross-deliverable analysis.

Each invocation is dispatched by EVALUATION (Type 1) with a brief specifying the deliverable path and output location. One digest file is produced per run.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

Typical dispatcher: `EVALUATION` (batched by package, one dispatch per deliverable).

#### Inputs

##### Required

- `ScopePath` — `{EXECUTION_ROOT}`
- `AllowedWriteTargets` — `["{EXECUTION_ROOT}/_Evaluation/content-digests/"]`
- `RuntimeOverrides.DELIVERABLE_PATH` — absolute path to the deliverable folder
- `RuntimeOverrides.OUTPUT_PATH` — absolute path to write the digest file (including filename `{DEL-ID}.md`)

##### Derived at runtime

- `DEL-ID` — from `_CONTEXT.md` or inferred from the deliverable folder name
- `DEL Name` — from `_CONTEXT.md`
- `PKG-ID` — from `_CONTEXT.md`

##### Optional

- None.

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `DELIVERABLE_PATH` | Absolute path to the deliverable folder | **Required** | Valid directory path containing `_CONTEXT.md` |
| `OUTPUT_PATH` | Absolute path to write the digest file | **Required** | Must be under `_Evaluation/content-digests/{PKG-ID}/`; parent directory must already exist |

#### Read boundary

Reads are limited to files within the specified deliverable folder:

| File | Read scope | Purpose |
|---|---|---|
| `_CONTEXT.md` | Full | Identity, description, acceptance criteria, scope traceability |
| `_DEPENDENCIES.md` | Full | Tracking mode, upstream/downstream summary, register statistics |
| `_REFERENCES.md` | Full | Source document pointers |
| `Datasheet.md` | First 80 lines | Key parameters, structured metadata |
| `Specification.md` | First 80 lines | Requirements, scope definition |
| `Guidance.md` | First 80 lines | Design rationale, principles, considerations |
| `Procedure.md` | First 80 lines | Execution workflow |
| `_SEMANTIC.md` | First 40 lines | Framework type, perspective |

The skill must NOT read files outside the specified deliverable folder. It must NOT cross into adjacent deliverable folders or scan package/project-level registers.

#### Write boundary

Writes are limited to:

- `{RuntimeOverrides.OUTPUT_PATH}` — exactly one file per run

The parent directory of `OUTPUT_PATH` must already exist. The skill does not create the directory.

#### Tool usage

- No deterministic tools. This is a reasoning-first, semantic-matching extraction skill.
- The `allowed-tools` frontmatter field is intentionally omitted.

Disallowed behavior:

- No writing outside `OUTPUT_PATH`
- No modification of any file in `DELIVERABLE_PATH`
- No reading files outside the specified deliverable folder
- No cross-deliverable scanning or comparison

#### Method

##### Step 0 — Preconditions

1. Validate `DELIVERABLE_PATH` exists and is a directory. If not: report `RUN_STATUS=FAILED_INPUTS`.
2. Validate parent directory of `OUTPUT_PATH` exists. If not: report `RUN_STATUS=FAILED_INPUTS`.

##### Step 1 — Read deliverable files

Read each file listed in the Read Boundary table, respecting the specified read scope (full or line-limited). If a file is absent, record that fact; do not fail.

##### Step 2 — Extract structured information

From the files read, extract:

- **Identity** (from `_CONTEXT.md`): Package (PKG-ID and name), Discipline, Type, Responsible
- **Scope** (from `_CONTEXT.md`): Description (1-2 sentence summary), Acceptance Criteria (bulleted list), SOW Traceability IDs, Objective Traceability IDs
- **Document Kit Summary** (from first 80 lines of each kit document): one-sentence focus summary for Datasheet, Specification, Guidance, Procedure
- **Dependencies** (from `_DEPENDENCIES.md`): Tracking mode (`NOT_TRACKED`/`DECLARED`/`TRACKED`), upstream count, downstream count, key upstream (top 3-5 by name), key downstream (top 3-5 by name)
- **References** (from `_REFERENCES.md`): list of all referenced documents
- **Semantic** (from first 40 lines of `_SEMANTIC.md`): whether present (`YES`/`NO`), framework type if identifiable

##### Step 3 — Note quality observations

Scan the read content for and record specific items:

- TBD items and their resolution authority
- ASSUMPTION labels and their rationale
- Placeholder text or incomplete sections
- Conflict Table entries with HumanRuling status
- Enrichment markers (e.g., `A-001`, `B-001`)
- Inconsistencies between documents within the folder

Quality observations are factual flags, not evaluative judgments.

##### Step 4 — Write digest

Write the structured digest to `OUTPUT_PATH` using the 7-section structure defined below. The file is overwritten if it already exists.

#### Output structure

The digest file contains exactly seven sections, in this order:

```markdown
#### {DEL-ID} — {Name}

##### Identity
- Package: {PKG-ID and name}
- Discipline: {from _CONTEXT}
- Type: {from _CONTEXT}
- Responsible: {from _CONTEXT}

##### Scope
- Description: {1-2 sentence summary from _CONTEXT}
- Acceptance Criteria: {bulleted list from _CONTEXT}
- SOW Traceability: {SOW-IDs}
- Objective Traceability: {OBJ-IDs}

##### Document Kit Summary
- Datasheet focus: {1 sentence}
- Specification focus: {1 sentence}
- Guidance focus: {1 sentence}
- Procedure focus: {1 sentence}

##### Dependencies
- Tracking mode: {NOT_TRACKED/DECLARED/TRACKED}
- Upstream count: {N}
- Downstream count: {N}
- Key upstream: {top 3-5 by name}
- Key downstream: {top 3-5 by name}

##### References
- {list all referenced documents}

##### Semantic
- _SEMANTIC.md present: {YES/NO}
- Framework type: {if identifiable}

##### Quality Observations
- {TBDs, placeholders, inconsistencies — specific items with IDs where available}
```

Missing information is noted as `not present` or `TBD in source`. Do not leave placeholder braces in the output.

#### Outputs

- One digest file at `{RuntimeOverrides.OUTPUT_PATH}`, containing the seven required sections.

#### Non-negotiable constraints

- **Read-only on deliverable production documents.** Never modify any file in `DELIVERABLE_PATH`.
- **Single-deliverable scope.** Each run processes exactly one deliverable folder. No cross-deliverable scanning.
- **No invention.** Report what the files contain. Do not infer, speculate, or fill gaps. Missing information is noted explicitly.
- **Semantic matching, not deep reasoning.** Extract structured information from document patterns. Flag quality observations but do not perform engineering judgment.
- **One digest per run.** Each invocation produces exactly one digest file at `OUTPUT_PATH`.
- **Seven-section structure preserved.** The output must contain all seven sections (Identity, Scope, Document Kit Summary, Dependencies, References, Semantic, Quality Observations) in the specified order.
- **No engineering judgments.** Evaluative assessment of deliverable correctness is EVALUATION_REPORT's responsibility, not this skill's.

#### QA expectations

- All seven sections present in the output digest.
- Identity fields populated from `_CONTEXT.md` (not invented).
- SOW and OBJ traceability IDs listed (or explicitly marked absent).
- Dependency counts stated with key upstream/downstream named.
- Quality Observations are specific items (TBDs, assumptions, conflicts) with IDs where available — not vague assessments.
- No files in `DELIVERABLE_PATH` were written or modified.
- The digest was written to the specified `OUTPUT_PATH`.
- No files outside the deliverable folder were read.

#### Downstream consumer

This skill produces one digest per deliverable. EVALUATION synthesizes digests across packages; EVALUATION_REPORT applies evaluative reasoning when scoring dimensions. This skill does not perform scoring or cross-deliverable synthesis.

## Component: skills/content-digest/TOOL_POLICY.md

### TOOL POLICY — content-digest

#### Preferred tool order

1. Read the bounded deliverable-local files listed in the skill contract.
2. Use direct reasoning to extract and summarize structured information into the seven-section digest.

#### Allowed deterministic tools

##### TASK-enforced

None. The `allowed-tools` frontmatter field is intentionally omitted.

##### Operationally invoked

None.

#### Expected use of reasoning

This skill performs bounded extraction and summarization only. It should identify specific quality-observation signals from the deliverable-local files without crossing into engineering judgment or cross-deliverable synthesis.

#### Disallowed use

- No writes outside `OUTPUT_PATH`.
- No modification of any file in `DELIVERABLE_PATH`.
- No reading files outside the specified deliverable folder.
- No cross-deliverable scanning or comparison.

#### Write boundary

The skill may write exactly one file at `RuntimeOverrides.OUTPUT_PATH`.
