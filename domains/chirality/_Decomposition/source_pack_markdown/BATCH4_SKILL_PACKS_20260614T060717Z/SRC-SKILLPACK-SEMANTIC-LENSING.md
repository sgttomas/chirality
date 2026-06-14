# Source Pack: Skill pack: semantic-lensing

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/semantic-lensing/BRIEF_SCHEMA.md

### BRIEF_SCHEMA — semantic-lensing

#### Required fields

| Field | Source | Notes |
|---|---|---|
| `ScopePath` | Brief | Run/context anchor, normally the deliverable folder |
| `TaskSkill` | Brief | `semantic-lensing` |
| `RuntimeOverrides.DELIVERABLE_PATH` | Brief | Absolute path to the deliverable folder |

#### Optional fields

| Field | Default | Notes |
|---|---|---|
| `UseSemanticLensing` | `true` | Compatibility flag accepted by existing dispatchers |
| `ActiveMatrices` | all | Comma-separated matrix letters (e.g., `A,B,F`) |
| `FocusLensTags` | all | Restrict to specific `Matrix.Row.Column` tags |
| `ApplyEdits` | `false` | Whether to apply authorized writes |
| `AllowLensLogUpdate` | `false` | Whether the brief intends to create/update `_SEMANTIC_LENSING.md`; also requires write authorization |
| `AllowTransferableContextUpdate` | `false` | Whether the brief intends to create/update `_TRANSFERABLE_CONTEXT.md`; also requires write authorization |

#### Example brief

```markdown
PURPOSE: Apply semantic lensing analysis to identify gaps and inconsistencies
RequestedBy: WORKING_ITEMS
ScopePath: /path/to/DEL-02.01_Pipeline-Design-Basis
TaskSkill: semantic-lensing
UseSemanticLensing: true
ActiveMatrices: A,B,F
Tasks:
  - Analyze production documents through the lens framework
  - Surface gaps and weak statements
ApplyEdits: false
AllowLensLogUpdate: false
RuntimeOverrides:
  DELIVERABLE_PATH: /path/to/DEL-02.01_Pipeline-Design-Basis
```

#### RuntimeOverrides example

```markdown
RuntimeOverrides:
  DELIVERABLE_PATH: /path/to/DEL-02.01_Pipeline-Design-Basis
  ActiveMatrices: A,B
  FocusLensTags: A.2.3,B.1.1
  LensDepth: shallow
```

If `AllowLensLogUpdate` or `AllowTransferableContextUpdate` is true, the brief must also set `ApplyEdits: true` and authorize the target file(s), either through `AllowedWriteTargets` or explicit writable-target text.

## Component: skills/semantic-lensing/QA_CHECKS.md

### QA_CHECKS — semantic-lensing

#### Minimum output validity

| Check | Validation |
|---|---|
| Lens tags present | Every proposal includes `Lens: <Matrix.Row.Column>` |
| Lens tags valid | Matrix letter exists in `_SEMANTIC.md` |
| Evidence grounded | Proposals cite production documents or accessible sources, not lensing entries |
| No invention | Content not supported by evidence is `TBD`, not fabricated |
| Conflicts surfaced | Contradictions between lensing entries and source material are in `NEEDS_HUMAN_RULING` |
| Scope respected | Only matrices in `ActiveMatrices` were processed (when specified) |
| `_SEMANTIC.md` unmodified | Read-only constraint honored |

#### Failure reporting

- If `_SEMANTIC.md` is missing: report in `MISSING` — the skill cannot operate without it
- If `_SEMANTIC_LENSING.md` is missing and the brief expects enrichment processing: report in `MISSING` — skill falls back to initial lens analysis only
- If no meaningful lens findings exist: state this explicitly rather than padding output

#### Evidence requirements

- Each incorporated lensing entry must trace to a source or production document location
- The lensing entry itself (`_SEMANTIC_LENSING.md` row) is a worklist pointer, not evidence
- Record which lensing entries were processed and their disposition (incorporated, converted to TBD, discarded)

## Component: skills/semantic-lensing/SKILL.md

---
name: semantic-lensing
description: Apply semantic lensing analysis to deliverable documents using _SEMANTIC.md matrices. Treats lensing entries as a candidate worklist, tags proposals with matrix coordinates, and optionally updates lens artifacts.
compatibility: Chirality TASK generic shell; reasoning-only (no deterministic tools).
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — semantic-lensing

#### Purpose

Apply semantic lensing analysis to deliverable-local production documents using `_SEMANTIC.md` as the lens reference and `_SEMANTIC_LENSING.md` as the enrichment worklist.

This skill provides the structured method for interactive semantic lensing analysis. When loaded, it supplies the matrix interpretation, tagging conventions, and proposal workflow.

This skill is the **optional interactive proposal/review tool**, not the regular ORCHESTRATOR enrichment step. In the regular PROJECT/SOFTWARE setup workflow:

- `skills/lens-register/` is the pipeline producer of `_SEMANTIC_LENSING.md`.
- `skills/four-documents/` Pass 3 is the pipeline consumer that applies `_SEMANTIC_LENSING.md` as an enrichment worklist.
- `skills/semantic-lensing/` is loaded only when a WORKING_ITEMS or TASK run needs human-facing `PROPOSAL:` blocks, focused review, or optional lens artifact updates.

Put another way, `_SEMANTIC_LENSING.md` becomes useful to the four documents through `four-documents` Pass 3. This skill may also consume the same file, but only for interactive review. Both paths treat lensing entries as candidates, not evidence.

This skill is the **interactive, proposal-producing** contract in the semantic-lensing family. Its setup-time counterpart is `skills/lens-register/`, which generates the matrix-organized register (`_SEMANTIC_LENSING.md`) consumed by `four-documents` Pass 3 and optionally by this skill. Both skills are documented in `.Archive/SEMANTIC_PIPELINE_ARCHITECTURE.md`.

#### Suitable agent shells

- `TASK` (generic shell, no profile)

#### Inputs

##### Required

- `ScopePath`
- `RuntimeOverrides.DELIVERABLE_PATH`
- `_SEMANTIC.md` must exist in the deliverable folder (read-only)

##### Optional

- `_SEMANTIC_LENSING.md` — enrichment worklist (if absent, skill generates initial lens analysis only)
- `ActiveMatrices` — restrict analysis to named matrices (default: all matrices found in `_SEMANTIC.md`)
- `FocusLensTags` — restrict processing to specific `Matrix.Row.Column` tags
- `AllowLensLogUpdate` — permit creating/updating `_SEMANTIC_LENSING.md`
- `AllowTransferableContextUpdate` — permit creating/updating `_TRANSFERABLE_CONTEXT.md`
- `UseSemanticLensing` — accepted compatibility flag; loading this skill is the actual method selector

#### Runtime overrides

| Key | Meaning | Default |
|---|---|---|
| `ActiveMatrices` | Restrict to named matrices (e.g., `A,B,F`) | all matrices in `_SEMANTIC.md` |
| `FocusLensTags` | Process only entries matching these tags | all entries |
| `LensDepth` | `shallow` (tag only) or `deep` (tag + cross-document analysis) | `deep` |

#### Tool usage

This is a reasoning-only skill. No deterministic tools are required or allowed.

Preferred method:
- read `_SEMANTIC.md` to understand the matrix structure and question framework
- read the production documents under `RuntimeOverrides.DELIVERABLE_PATH`
- if `_SEMANTIC_LENSING.md` exists, read each entry as a candidate improvement
- generate proposals with `Lens:` tags grounded in evidence from the production documents
- do not treat lensing entries as evidence — they are candidates only

Disallowed behavior:
- no treating `_SEMANTIC.md` or `_SEMANTIC_LENSING.md` as evidence authority
- no inventing facts to fill lens-identified gaps — use `TBD`
- no widening scope beyond the single deliverable
- no edits to `_SEMANTIC.md` under any circumstances

#### Outputs

- `PROPOSAL:` blocks with `Lens: <Matrix.Row.Column>` tags for each finding
- `MISSING:` items where lens-identified content gaps exist
- `NEEDS_HUMAN_RULING:` items where lensing surfaces contradictions
- optionally updated `_SEMANTIC_LENSING.md` (when `AllowLensLogUpdate: true`)
- optionally updated `_TRANSFERABLE_CONTEXT.md` (when `AllowTransferableContextUpdate: true`)
- optional `MEMORY.md` update only when explicitly authorized by the brief

#### Method: matrix interpretation

Matrices in `_SEMANTIC.md` (commonly A, B, C, F, D, X, E) are a tagging and analysis convention, not a requirement for completion. Each matrix cell is a question-shaping lens:

- **Use matrices to identify** what questions the deliverable should answer
- **Use matrix coordinates** (`Matrix.Row.Column`) to tag proposals so findings are traceable to the analysis framework
- **Do not require** every matrix cell to yield a finding — empty cells are normal
- **Do not invent** content to fill matrix gaps; use `TBD` and note the lens coordinate

#### Method: enrichment workflow (when `_SEMANTIC_LENSING.md` exists)

Each row in `_SEMANTIC_LENSING.md` is a candidate improvement with an item type. Process each entry:

1. Read the entry and identify the target document section(s)
2. Read the target section(s) in the production documents
3. If the entry is supported by evidence from sources or production documents: generate a `PROPOSAL:` with the lens tag, evidence, and proposed change
4. If the entry identifies a real gap: generate a `PROPOSAL:` with `TBD` content and the lens tag
5. If the entry conflicts with source material: add to `NEEDS_HUMAN_RULING`
6. If the entry cannot be grounded: convert to `TBD` or discard with a note

Item types and their handling:
- `Conflict` — surface with both contenders cited; do not resolve silently
- `WeakStatement` — propose strengthening with source evidence, or mark `TBD`
- `Normalization` — propose terminology/format alignment across documents
- `MissingSlot` — propose content grounded in source, or mark `TBD`
- `RationaleGap` — propose rationale from source guidance, or mark `TBD`
- `VerificationGap` — propose verification approach tied to requirements
- `TBD_Question` — attempt resolution from accessible sources; if unresolvable, retain as `TBD`

#### Non-negotiable constraints

- `_SEMANTIC.md` is read-only — never modify it
- Lensing entries are candidates, not evidence — they cannot authorize new facts
- Every proposal must cite evidence from production documents or accessible sources
- Lens tags must use the `Matrix.Row.Column` format
- Unknowns remain `TBD`
- Conflicts must be surfaced, not reconciled silently

#### QA expectations

- Every proposal includes a `Lens:` tag with a valid matrix coordinate
- Proposals that incorporate lensing entries cite the underlying source, not the lensing entry itself
- `_SEMANTIC_LENSING.md` entries that were processed are noted as incorporated, converted to TBD, or discarded with reason
- No content was invented from lensing entries alone
- If `ActiveMatrices` or `FocusLensTags` were set, only the specified scope was processed

## Component: skills/semantic-lensing/TOOL_POLICY.md

### semantic-lensing — Tool Policy

#### Preferred tool order
Reasoning-first: this skill is LLM-driven; no deterministic tool ordering applies.

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- None — no TASK-enforced deterministic allowlist

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None — no operational helpers declared (this is a reasoning-only skill; no deterministic tools are required or allowed)

#### Expected use of reasoning
This is a reasoning-only skill. All phases are reasoning-driven: reading `_SEMANTIC.md` to understand the matrix structure and question framework, reading production documents under `RuntimeOverrides.DELIVERABLE_PATH`, reading `_SEMANTIC_LENSING.md` entries as candidate improvements (not evidence), and generating `PROPOSAL:` blocks with `Lens:` tags grounded in evidence from the production documents.

#### Disallowed use
From SKILL.md's "Disallowed behavior" section:
- no treating `_SEMANTIC.md` or `_SEMANTIC_LENSING.md` as evidence authority
- no inventing facts to fill lens-identified gaps — use `TBD`
- no widening scope beyond the single deliverable
- no edits to `_SEMANTIC.md` under any circumstances

No hidden reliance on tools outside the declared list unless the human expands AllowedTools. No writes outside declared scope.

#### Write boundary
Per SKILL.md's Outputs section:
- `PROPOSAL:` blocks with `Lens: <Matrix.Row.Column>` tags for each finding
- `MISSING:` items where lens-identified content gaps exist
- `NEEDS_HUMAN_RULING:` items where lensing surfaces contradictions
- optionally updated `_SEMANTIC_LENSING.md` (when `AllowLensLogUpdate: true` and the brief authorizes the write)
- optionally updated `_TRANSFERABLE_CONTEXT.md` (when `AllowTransferableContextUpdate: true` and the brief authorizes the write)
- optional `MEMORY.md` update only when explicitly authorized by the brief

`_SEMANTIC.md` is read-only and must never be modified. Writes are limited to the effective bounded task brief's authorization for the single deliverable under `RuntimeOverrides.DELIVERABLE_PATH`.
