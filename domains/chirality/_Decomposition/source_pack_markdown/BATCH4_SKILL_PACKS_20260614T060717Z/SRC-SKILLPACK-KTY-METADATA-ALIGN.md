# Source Pack: Skill pack: kty-metadata-align

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/kty-metadata-align/BRIEF_SCHEMA.md

### kty-metadata-align — Brief Schema

Use this skill with a generic TASK shell (no profile) like this:

```md
PURPOSE: Align one KTY's metadata after DOMAIN regeneration.
RequestedBy: ORCHESTRATOR

ScopePath: /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist
TaskSkill: kty-metadata-align
AllowedWriteTargets:
  - /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist/_CONTEXT.md
  - /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist/_STATUS.md
  - /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist/_REFERENCES.md
  - /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist/2_Checking/From/KTY_Metadata_Alignment.md

RuntimeOverrides:
  KTY_PATH: /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist
  DECOMPOSITION_REF: /abs/path/to/_Decomposition
  SOURCES_ROOT: /abs/path/to/_Sources
  REVIEW_OUTPUT_PATH: /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist/2_Checking/From/KTY_Metadata_Alignment.md
  MODE: ALIGN_METADATA
  REWRITE_REFERENCES: true
  ALLOW_STATUS_APPEND: true
```

#### Required fields

| Field | Value | Notes |
|---|---|---|
| `TaskSkill` | `kty-metadata-align` | Must match skill folder name |
| `ScopePath` | Absolute path to one `KTY-*` folder | Normally equals `KTY_PATH` |
| `AllowedWriteTargets` | Narrow list of metadata files and optional report path | Single-KTY scope only |
| `RuntimeOverrides.KTY_PATH` | Absolute path to one KTY folder | Required |
| `RuntimeOverrides.DECOMPOSITION_REF` | Decomposition truth source | Required |
| `RuntimeOverrides.MODE` | Review or metadata-alignment mode | `REPORT_ONLY` or `ALIGN_METADATA` |

#### Optional fields

| Field | Default | Allowed values | Notes |
|---|---|---|---|
| `RuntimeOverrides.SOURCES_ROOT` | omitted | Absolute path | Used only to resolve authoritative source pointers |
| `RuntimeOverrides.REVIEW_OUTPUT_PATH` | omitted | Absolute path | Optional report output |
| `RuntimeOverrides.REWRITE_REFERENCES` | `true` | `true`, `false` | Set `false` to leave `_REFERENCES.md` untouched |
| `RuntimeOverrides.ALLOW_STATUS_APPEND` | `true` | `true`, `false` | Set `false` when `_STATUS.md` must remain read-only |
| `RuntimeOverrides.AUTHORITATIVE_STATUS_STATE` | omitted | Known lifecycle token | Use when the caller owns the lifecycle transition |

#### TaskProfile

`NONE` — this skill runs in generic TASK shell mode without a profile.

#### Read boundary

The skill reads:

- `{KTY_PATH}/_CONTEXT.md`
- `{KTY_PATH}/_STATUS.md`
- sibling `{KTY_PATH}/_MEMORY.md` / `{KTY_PATH}/MEMORY.md` when present,
  paired with `_STATUS.md` as non-authoritative operational context only
- `{KTY_PATH}/_REFERENCES.md`
- optional `Scoping.md` / `KA-*.md` for drift observation only
- decomposition material under `{DECOMPOSITION_REF}`
- source pointer paths under `{SOURCES_ROOT}` only when needed

#### Write boundary

The skill may write only:

- `{KTY_PATH}/_CONTEXT.md`
- `{KTY_PATH}/_STATUS.md`
- `{KTY_PATH}/_REFERENCES.md`
- optional `REVIEW_OUTPUT_PATH`

It must not write `Scoping.md`, `KA-*.md`, or any decomposition file.

#### Typical tasks

- align `_CONTEXT.md` after a KTY rename, category move, or scope change
- append a lifecycle correction to `_STATUS.md` when the invoking workflow owns
  the authoritative state
- refresh `_REFERENCES.md` after decomposition or source-pointer changes
- classify remaining stale `Scoping.md` / `KA-*` files as rerun work

#### Notes

- This skill is metadata-only by design.
- `REPORT_ONLY` is safe for audit follow-up.
- Use `domain-documents` for content regeneration, not this skill.

## Component: skills/kty-metadata-align/QA_CHECKS.md

### kty-metadata-align — QA Checks

Minimum checks for a valid run:

1. `KTY_PATH` exists and resolves to exactly one `KTY-*` folder.
2. The decomposition produced one unambiguous KTY truth row for the target
   folder.
3. The run classifies observed issues into:
   - `REPAIRED_NOW`
   - `RERUN_LATER`
   - `UNRESOLVED`
4. `REPORT_ONLY` runs do not modify metadata files.
5. `ALIGN_METADATA` runs modify only files explicitly authorized in
   `AllowedWriteTargets`.
6. Any `_STATUS.md` edit is append-only and evidence-backed.
7. Whenever `_STATUS.md` is read, sibling `_MEMORY.md` / `MEMORY.md` is read
   when present as non-authoritative operational context only.
8. No files other than `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, and the
   optional report were modified.

#### `_CONTEXT.md` validation

When `_CONTEXT.md` is rewritten:

- the title matches `# Context: {KTY-ID}`
- the file contains `Name`, `Category`, `Discipline`, `Type`, `Responsible`,
  `CanonicalSchema`, `IntendedUsers`, `WhenUsed`, `Description`,
  `Anticipated Artifacts`, and `Decomposition Reference`
- missing decomposition values appear as `TBD`, not invented prose

#### `_STATUS.md` validation

When `_STATUS.md` is modified:

- the change is append-only
- the appended line identifies the authoritative status or alignment basis
- the skill did not invent a lifecycle state not supported by the brief or
  existing evidence

#### `_REFERENCES.md` validation

When `_REFERENCES.md` is rewritten:

- the file remains a references container
- authoritative references remain distinct from notes
- preserved manual notes, if any, are not silently promoted to authoritative
  pointers

#### Follow-on action validation

If the run observes drift in `Scoping.md` or `KA-*.md`, the report or task
output must:

- name the affected file(s)
- state that no content-file edits were performed
- classify the issue as `RERUN_LATER` or `UNRESOLVED`

#### Success case

A clean run reports:

- target KTY ID
- mode used
- files modified, if any
- whether any follow-on reruns remain

## Component: skills/kty-metadata-align/SKILL.md

---
name: kty-metadata-align
description: Review and optionally align one DOMAIN Knowledge Type folder's metadata surfaces to approved decomposition truth without rewriting Scoping.md or KA content. Use after regeneration or scope change when `_CONTEXT.md`, `_STATUS.md`, or `_REFERENCES.md` may have drifted.
compatibility: Chirality TASK in generic shell mode (no profile); reasoning-first KTY-local metadata review and bounded repair.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — kty-metadata-align

#### Purpose

Review and optionally align the metadata surface of one DOMAIN Knowledge Type
folder to approved decomposition truth and current lifecycle evidence.

In package-role terms: this skill aligns KTY-local derived metadata
(`_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`) to the authoritative
decomposition truth in the canonical working package, not the reverse. The
decomposition package (main document + authoritative companion registers +
`_ScopeChange` state) is the source of truth; KTY-local metadata is a
downstream consumer of that truth.

When this skill reads `_STATUS.md`, it also reads sibling `_MEMORY.md` or
`MEMORY.md` when present. Memory is non-authoritative operational context only:
it can explain prior local runs or caveats, but it must not override approved
decomposition truth or SCA state.

This skill supports two modes:

- `REPORT_ONLY` — inspect and report only
- `ALIGN_METADATA` — repair metadata-safe drift

Metadata-safe writes are limited to:

- `_CONTEXT.md`
- `_STATUS.md`
- `_REFERENCES.md`

This skill never rewrites:

- `Scoping.md`
- `KA-*.md`
- `_DEPENDENCIES.md`
- `_MEMORY.md`
- publication artifacts

If content files appear stale after metadata alignment, the skill reports a
follow-on rerun rather than widening scope.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

Typical dispatchers:

- root remediation loops after `domain-documents`
- `SCOPE_CHANGE` follow-on closure work
- targeted KTY metadata cleanup after audit findings

#### Inputs

##### Required

- `ScopePath` — absolute path to one `KTY-*` folder
- `AllowedWriteTargets` — report path plus any metadata files explicitly
  authorized for alignment in this run
- `RuntimeOverrides.KTY_PATH` — normally equal to `ScopePath`
- `RuntimeOverrides.DECOMPOSITION_REF` — decomposition root or document used as
  truth source
- `RuntimeOverrides.MODE` — `REPORT_ONLY` or `ALIGN_METADATA`

##### Optional

- `RuntimeOverrides.SOURCES_ROOT` — shared source/reference root for resolving
  authoritative source pointers
- `RuntimeOverrides.REVIEW_OUTPUT_PATH` — optional markdown report path
- `RuntimeOverrides.REWRITE_REFERENCES` — `true` | `false`; default `true`
- `RuntimeOverrides.ALLOW_STATUS_APPEND` — `true` | `false`; default `true`
- `RuntimeOverrides.AUTHORITATIVE_STATUS_STATE` — optional lifecycle state to
  append when the invoking workflow owns the state transition

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `KTY_PATH` | Knowledge Type folder to review/align | **Required** | Absolute path to one `KTY-*` folder |
| `DECOMPOSITION_REF` | Decomposition truth source | **Required** | Absolute path |
| `MODE` | Report or metadata alignment mode | **Required** | `REPORT_ONLY`, `ALIGN_METADATA` |
| `SOURCES_ROOT` | Source-material root for reference-path resolution | omitted | Absolute path |
| `REVIEW_OUTPUT_PATH` | Optional report path | omitted | Path inside `AllowedWriteTargets` |
| `REWRITE_REFERENCES` | Rewrite `_REFERENCES.md` | `true` | `true`, `false` |
| `ALLOW_STATUS_APPEND` | Permit append-only `_STATUS.md` corrections | `true` | `true`, `false` |
| `AUTHORITATIVE_STATUS_STATE` | Explicit lifecycle state supplied by caller | omitted | `OPEN`, `INITIALIZED`, `SEMANTIC_READY`, `IN_PROGRESS`, `CHECKING`, `ISSUED`, `RETIRED` |

#### Read boundary

Reads are limited to:

- `{KTY_PATH}/_CONTEXT.md`
- `{KTY_PATH}/_STATUS.md`
- `{KTY_PATH}/_MEMORY.md` or `{KTY_PATH}/MEMORY.md` when present, paired with
  `_STATUS.md` as non-authoritative operational context only
- `{KTY_PATH}/_REFERENCES.md`
- optional `{KTY_PATH}/Scoping.md` and `{KTY_PATH}/KA-*.md` for drift
  observation only
- decomposition materials under `{DECOMPOSITION_REF}`
- source pointers under `{SOURCES_ROOT}` only when needed

This skill must not scan sibling KTY folders or infer truth from unrelated
roots.

#### Write boundary

Writes are limited to:

- optional `{REVIEW_OUTPUT_PATH}`
- `{KTY_PATH}/_CONTEXT.md`
- `{KTY_PATH}/_STATUS.md`
- `{KTY_PATH}/_REFERENCES.md`

Only files explicitly authorized in `AllowedWriteTargets` may be modified.

#### Tool usage

- Reasoning-first only.
- The `allowed-tools` frontmatter field is intentionally omitted.

Disallowed behavior:

- No edits to `Scoping.md`, `KA-*.md`, `_DEPENDENCIES.md`, `_MEMORY.md`, or any
  decomposition file.
- No invention of source paths, lifecycle state, or decomposition fields.
- No silent deletion of human-authored reference notes unless the brief
  explicitly authorizes replacement.

#### Method

##### Step 0 — Preconditions

1. Validate `KTY_PATH` exists and resolves to exactly one `KTY-*` folder.
2. Resolve the matching KTY row from `DECOMPOSITION_REF`.
3. Validate every repair target is explicitly authorized by
   `AllowedWriteTargets`.
4. If the KTY row cannot be identified uniquely: `RUN_STATUS=FAILED_INPUTS`.

##### Step 1 — Derive canonical metadata

Extract from decomposition truth, without invention:

- `KnowledgeTypeID`
- `Knowledge Type Name`
- `Category ID`
- `Category Name`
- `Discipline`
- `Type`
- `Responsible`
- `Description`
- `AnticipatedArtifacts`
- `CanonicalSchema`
- `IntendedUsers`
- `WhenUsed`
- decomposition reference path
- any authoritative source pointer or `SourceSpan` available for the KTY

If a field is absent in decomposition truth, use `TBD` rather than inferring it.

##### Step 2 — Review current metadata state

Review:

- `_CONTEXT.md` for identity / category / description drift
- `_STATUS.md` for append-only lifecycle validity and any obvious contradiction
  with `AUTHORITATIVE_STATUS_STATE`, when provided
- `_MEMORY.md` / `MEMORY.md`, when present, for non-authoritative operational
  caveats paired with `_STATUS.md`
- `_REFERENCES.md` for stale or contradictory authoritative pointers
- `Scoping.md` / `KA-*.md` only to decide whether content regeneration follow-up
  is still needed

Classify each observed issue as:

- `REPAIRED_NOW`
- `RERUN_LATER`
- `UNRESOLVED`

##### Step 3 — Optional metadata alignment

Only when `MODE = ALIGN_METADATA`:

1. Rewrite `_CONTEXT.md` to aligned decomposition truth.
2. If `REWRITE_REFERENCES=true`, normalize `_REFERENCES.md` so authoritative
   pointers are current and preserved notes stay clearly non-authoritative.
3. If `ALLOW_STATUS_APPEND=true` and a status correction is unambiguous:
   - append a correction line to `_STATUS.md`
   - never invent a new lifecycle state
   - if `AUTHORITATIVE_STATUS_STATE` is absent and the correction would require
     judgment, do not edit `_STATUS.md`; report it instead

##### Step 4 — Surface follow-on work

If `Scoping.md` or any `KA-*.md` appear inconsistent with aligned metadata:

- do not edit them
- report the exact files
- classify them as `RERUN_LATER`

##### Step 5 — Write outputs

If `REVIEW_OUTPUT_PATH` is provided, write a report containing:

1. Title: `# KTY Metadata Alignment — {KTY-ID}`
2. Metadata block: KTY path, decomposition ref, mode, review date
3. Summary sections:
   - repaired now
   - rerun later
   - unresolved
4. Files modified in this run, if any
5. Explicit `RUN_STATUS`

#### Outputs

- optional report at `REVIEW_OUTPUT_PATH`
- optionally updated `_CONTEXT.md`
- optionally updated `_STATUS.md`
- optionally updated `_REFERENCES.md`

#### Non-negotiable constraints

- **Single-KTY scope.** One invocation aligns one KTY folder only.
- **Metadata-only writes.** No `Scoping.md` or `KA-*` edits.
- **Decomposition authority.** `_CONTEXT.md` aligns to approved decomposition
  truth (the canonical working package), not existing draft prose. The
  direction of truth flow is always: authoritative decomposition package ->
  KTY-local metadata, never the reverse.
- **Append-only lifecycle safety.** `_STATUS.md` changes must be append-only and
  authority-backed.
- **No invention.** Missing source pointers or lifecycle evidence remain
  reported, not guessed.
- **Downstream scope only.** This skill operates on KTY-local metadata surfaces
  only. It must not modify the canonical working package, authoritative
  companion registers, `_ScopeChange` state, or any derived publication
  artifacts. It must not become a loophole for compensating for poor
  decomposition package structure upstream.

#### QA expectations

- The target KTY ID is explicit.
- The run separates `REPAIRED_NOW`, `RERUN_LATER`, and `UNRESOLVED`.
- Any `_STATUS.md` modification is append-only and evidence-backed.
- Any stale `Scoping.md` or `KA-*` content is surfaced as follow-on work, not
  silently rewritten.

## Component: skills/kty-metadata-align/TOOL_POLICY.md

### kty-metadata-align — Tool Policy

#### Preferred tool order

Reasoning-first:

1. read decomposition truth for the target KTY
2. read existing `_CONTEXT.md`, `_STATUS.md`, sibling `_MEMORY.md` / `MEMORY.md`
   when present as non-authoritative operational context, and `_REFERENCES.md`
3. classify observed drift into `REPAIRED_NOW`, `RERUN_LATER`, or `UNRESOLVED`
4. in `ALIGN_METADATA` mode only, repair authorized metadata files
5. write the optional report and any follow-on recommendations

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill
load time._

- None — no TASK-enforced deterministic allowlist (the `allowed-tools`
  frontmatter field is intentionally omitted)

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None — no deterministic helpers declared

#### Expected use of reasoning

This skill is a bounded metadata-normalization pass. Reasoning governs:

- matching the folder to one decomposition KTY row
- determining whether lifecycle drift is actually unambiguous
- preserving human-authored reference notes while keeping authoritative pointers
  current
- deciding when content drift requires rerun rather than metadata editing

#### Disallowed use

- No edits outside `_CONTEXT.md`, `_STATUS.md`, `_REFERENCES.md`, and the
  optional report path.
- No rewriting `Scoping.md`, `KA-*.md`, `_DEPENDENCIES.md`, `_MEMORY.md`, or
  lifecycle semantics that are not authority-backed.
- No use of `_MEMORY.md` / `MEMORY.md` as decomposition truth or lifecycle
  authority. It is context only and is read only when paired with `_STATUS.md`.
- No invented `SourceSpan`, source paths, or lifecycle states.
- No silent deletion of human-authored notes unless the brief explicitly
  authorizes replacement.

#### Write boundary

Writes are limited to:

- `{KTY_PATH}/_CONTEXT.md`
- `{KTY_PATH}/_STATUS.md`
- `{KTY_PATH}/_REFERENCES.md`
- optional `{REVIEW_OUTPUT_PATH}`

No other files may be created or modified by this skill.
