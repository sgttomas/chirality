# Source Pack: Skill pack: pdf2md-folio-extract

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/pdf2md-folio-extract/BRIEF_SCHEMA.md

### pdf2md-folio-extract - Brief Schema

Use this skill with `TASK` like this. It is normally spawned by the `PDF2MD` orchestrator after rasterization and before per-page asset fan-out:

```md
PURPOSE: Extract the visible printed folio label from one rasterized PDF page
RequestedBy: PDF2MD

ScopePath: /abs/path/to/pdf_work_dir
TaskSkill: pdf2md-folio-extract

Tasks:
  - Read one page raster
  - Identify the printed folio label visible on the page, if any
  - Emit a single folio JSON record per the skill contract

ApplyEdits: true

AllowedWriteTargets:
  - "/abs/path/to/pdf_work_dir/page_0047_folio.json"

RuntimeOverrides:
  IMAGE_PATH: /abs/path/to/pdf_work_dir/page_0047.png
  OUTPUT_PATH: /abs/path/to/pdf_work_dir/page_0047_folio.json
  PAGE_NUM: 47

ExpectedOutputs:
  - /abs/path/to/pdf_work_dir/page_0047_folio.json
```

#### Required fields

| Field | Value | Notes |
|---|---|---|
| `TaskSkill` | `pdf2md-folio-extract` | Must match skill folder name |
| `RuntimeOverrides.IMAGE_PATH` | Absolute path to the page PNG | Must exist, must have `.png` extension |
| `RuntimeOverrides.OUTPUT_PATH` | Absolute path to page folio JSON | Parent directory must exist |
| `RuntimeOverrides.PAGE_NUM` | 1-indexed physical PDF page number | Positive integer; echoed into JSON as `page` |

#### Optional fields

None. This skill takes no optional runtime overrides.

#### TaskProfile

`NONE` - this skill runs in generic TASK shell mode without a profile.

#### Read boundary

The skill reads only:

- `{IMAGE_PATH}`

It must not read neighbouring page images, sibling folio JSON, manifests, the source PDF, the page Markdown, or any TOC / outline artifact.

#### Write boundary

The skill writes only:

- `{OUTPUT_PATH}`

#### AllowedTools

Omit `AllowedTools`. This is a VLM-reasoning-only skill with no deterministic tool dependencies.

#### Output JSON shape

The skill writes exactly one JSON file with this shape:

```json
{
  "schema_version": "pdf2md-folio-extract/v1",
  "run_status": "SUCCESS",
  "page": 47,
  "page_label": "47",
  "page_label_source": "vlm",
  "location": "bottom-center",
  "confidence": "high",
  "rationale": "Arabic numeral 47 centered in footer."
}
```

##### Field-by-field rules

| Field | Type | Allowed values | Notes |
|---|---|---|---|
| `schema_version` | string | exactly `"pdf2md-folio-extract/v1"` | Literal — do not alter |
| `run_status` | string | `"SUCCESS"` / `"NO_FOLIO"` / `"FAILED"` / `"FAILED_INPUTS"` | Uppercase literals only |
| `page` | int | positive integer | Echo of runtime `PAGE_NUM`; field name is `page` (NOT `page_num`) |
| `page_label` | string OR null | exact visible glyph (`"47"`, `"xiv"`, `"B-3"`, ...) OR `null` | `null` iff no folio is printed; preserve case, Roman vs. Arabic, prefixes, hyphens |
| `page_label_source` | string | exactly `"vlm"` | Literal — identifies producer |
| `location` | string OR null | `"top-left"` / `"top-center"` / `"top-right"` / `"bottom-left"` / `"bottom-center"` / `"bottom-right"` OR `null` | `null` iff `page_label` is `null` |
| `confidence` | string | `"high"` / `"medium"` / `"low"` | Visual reading confidence |
| `rationale` | string | one short sentence | Plain English; one sentence |

##### Status semantics

| `run_status` | When to emit | `page_label` | `location` |
|---|---|---|---|
| `SUCCESS` | A folio is visibly printed and legible | string | one of six zone literals |
| `NO_FOLIO` | The page has no printed folio (blank page, cover, chapter opener with suppressed folio, untitled front-matter, full-bleed plate, etc.) | `null` | `null` |
| `FAILED` | The page image is unreadable, corrupt, or otherwise prevents inspection | `null` | `null` |
| `FAILED_INPUTS` | Required runtime overrides are missing, paths do not exist, or extensions are wrong | `null` | `null` |

#### CustomInstructions

Usually unnecessary. If used, keep them run-specific and do not restate the whole skill contract. Good examples:

- "Treat the leading section letter (e.g. `A-`, `B-`) as part of the folio; do not strip it."
- "On chapter-opener pages where this house style suppresses the folio, return `NO_FOLIO` even if a chapter number appears in display type."

## Component: skills/pdf2md-folio-extract/QA_CHECKS.md

### pdf2md-folio-extract - QA Checks

Minimum checks for a valid run:

1. `IMAGE_PATH` exists and has a `.png` extension, or the skill returns `FAILED_INPUTS`.
2. `OUTPUT_PATH` parent directory exists before write.
3. `OUTPUT_PATH` exists after the run and is non-empty.
4. `OUTPUT_PATH` parses with `json.loads`.
5. No files other than `IMAGE_PATH` were read.
6. No files other than `OUTPUT_PATH` were written.

#### JSON shape checks

The output JSON must include exactly these top-level fields:

| Field | Requirement |
|---|---|
| `schema_version` | Exactly `"pdf2md-folio-extract/v1"` |
| `run_status` | One of `"SUCCESS"`, `"NO_FOLIO"`, `"FAILED"`, `"FAILED_INPUTS"` |
| `page` | Integer; equals runtime `PAGE_NUM` (field name is `page`, NOT `page_num`) |
| `page_label` | JSON string when `run_status == "SUCCESS"`, JSON `null` otherwise |
| `page_label_source` | Exactly `"vlm"` |
| `location` | One of `"top-left"`, `"top-center"`, `"top-right"`, `"bottom-left"`, `"bottom-center"`, `"bottom-right"` when `page_label` is a string; JSON `null` otherwise |
| `confidence` | One of `"high"`, `"medium"`, `"low"` |
| `rationale` | Non-empty string; one short sentence |

#### Field-value strictness

- `schema_version` is a literal — `"pdf2md-folio/v1"`, `"v1"`, or other shortened forms are rejected.
- `run_status` uppercase literals only — `"ok"`, `"success"`, `"none"`, `"done"` are rejected.
- `page_label` MUST be the verbatim visible glyph; downstream tools rely on the exact surface form:
  - Roman numerals stay Roman (`"xiv"`, not `"14"`).
  - Case is preserved (`"xiv"` vs. `"XIV"`).
  - Section prefixes are kept (`"B-3"`, not `"3"`).
  - No zero-padding (`"7"`, not `"007"`).
- `page_label_source` is always the literal `"vlm"` from this skill, including on failure rows.
- `location` and `page_label` co-vary: both are `null` together, or both are non-null together. A `null` `page_label` with a non-null `location` is invalid, and vice versa.

#### Folio-invention guard

The most important QA invariant for this skill:

- A `SUCCESS` row's `page_label` MUST be visible on the page image.
- It MUST NOT be derived from `PAGE_NUM` (the physical sequence index).
- It MUST NOT be inferred from neighbouring pages' numbering.
- When no folio is visibly printed, the correct emission is `NO_FOLIO` with `page_label: null` and `location: null` — never a fabricated label.

#### Failure posture

| Failure mode | Required output |
|---|---|
| Missing or wrong-extension `IMAGE_PATH` | `run_status: "FAILED_INPUTS"`, `page_label: null`, `location: null`, rationale naming the missing input |
| `OUTPUT_PATH` parent directory missing | `run_status: "FAILED_INPUTS"`, `page_label: null`, `location: null`, rationale naming the issue |
| No folio printed on the page | `run_status: "NO_FOLIO"`, `page_label: null`, `location: null`, rationale explaining (blank page / cover / chapter opener / etc.) |
| Page image unreadable or corrupt | `run_status: "FAILED"`, `page_label: null`, `location: null`, rationale explaining the problem |

#### Orchestrator-side checks

These checks belong to `PDF2MD`, not this skill:

- Running the folio-extract skill across every page in parallel.
- Aggregating per-page folio JSON into a document-level folio map.
- Reconciling Roman-numeral front matter against Arabic body numbering.
- Detecting suspicious jumps in the folio sequence and surfacing them for review.
- Propagating `page_label` into downstream per-page asset records.
- Treating unresolved or contradictory folio reports as degraded output requiring human acknowledgment before downstream use.

## Component: skills/pdf2md-folio-extract/SKILL.md

---
name: pdf2md-folio-extract
description: Read one rasterized PDF page and emit the visible printed folio label (page number as it appears on the page itself — "47", "xiv", "B-3", or null when no folio is printed).
compatibility: Chirality TASK; invoked by PDF2MD asset-enabled mode after rasterization, before per-page asset fan-out.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL - pdf2md-folio-extract

#### Purpose

Read one rasterized PDF page image and emit the printed folio label that is visible on the page itself — the page number as the document prints it, not the physical PDF sequence position.

Examples of valid folio labels:

- Arabic numerals: `"47"`, `"128"`
- Roman numerals: `"xiv"`, `"iii"`, `"XLII"`
- Compound/prefixed labels: `"B-3"`, `"A-12"`, `"3-7"`
- Section-prefixed labels: `"Ch1-4"`, `"App-2"`

The skill reads exactly one page image and writes exactly one JSON file naming the visible folio. It does not assemble a folio map across pages, reconcile front-matter Roman numbering against body Arabic numbering, or interact with the PDF outline / TOC. Those are orchestrator-level concerns.

#### Suitable agent shells

- `TASK` in generic shell mode, spawned by the `PDF2MD` orchestrator

Not the right fit for:

- whole-PDF folio map assembly
- TOC / outline cross-referencing
- inferring a folio from neighbouring pages
- assigning final asset filenames or any non-folio metadata

#### Inputs

Required runtime overrides:

- `IMAGE_PATH` - absolute path to the page PNG
- `OUTPUT_PATH` - absolute path for the folio JSON
- `PAGE_NUM` - 1-indexed physical PDF page number

#### Read boundary

Reads are limited to exactly one file:

- `{IMAGE_PATH}`

Do not read neighbouring pages, manifests, sibling Markdown, the source PDF, or any other folio JSON. This preserves page-level parallelism and prevents folio invention by inference from neighbours.

#### Write boundary

Writes are limited to exactly one file:

- `{OUTPUT_PATH}`

The output filename is supplied by the orchestrator and must not be derived or changed by the skill.

#### Tool usage

- No deterministic tools.
- The `allowed-tools` frontmatter field is intentionally omitted.
- The agent uses native multimodal reading for `IMAGE_PATH` and native writing for `OUTPUT_PATH`.

Disallowed behavior:

- Do not crop images.
- Do not write PNG, CSV, or XLSX files.
- Do not read neighbouring page images or any other file.
- Do not invent a folio from the physical sequence (e.g. do NOT return `"47"` just because `PAGE_NUM` is 47).
- Do not infer a folio from neighbouring pages' numbering.
- Do not consult outlines, TOCs, or sibling JSON.

#### Method

##### Step 1 - Validate inputs

1. Confirm `IMAGE_PATH` exists and has a `.png` extension.
2. Confirm `OUTPUT_PATH` parent directory exists.
3. If required inputs are missing or malformed, write a valid JSON file with `run_status: "FAILED_INPUTS"`, `page_label: null`, `location: null`, and a rationale naming the missing input.

##### Step 2 - Inspect the page

1. Read `IMAGE_PATH` and inspect the page visually.
2. Scan the typical folio zones in order: bottom-center, bottom-outer (left/right), top-outer (left/right), top-center.
3. Identify the printed folio if and only if it is visibly present as a page-number marking — typically a short numeric / Roman / alphanumeric token isolated in a header or footer, not part of running prose, figure captions, equation numbers, or section headings.
4. If no folio is printed (blank page, cover page, chapter-opener page where the folio is suppressed, front-matter without numbering, full-bleed plate without page furniture, etc.), record that there is no folio. Do NOT invent one.

##### Step 3 - Emit JSON

Write only JSON, with no Markdown fences or commentary.

**REQUIRED EXACT VALUES — do not substitute synonyms or restructure.** Downstream consumers rely on these exact field names, types, and string literals:

- Top-level field names are exactly: `schema_version`, `run_status`, `page`, `page_label`, `page_label_source`, `location`, `confidence`, `rationale`.
- `schema_version` MUST be the literal string `"pdf2md-folio-extract/v1"`.
- `run_status` MUST be one of the four uppercase literals: `"SUCCESS"`, `"NO_FOLIO"`, `"FAILED"`, `"FAILED_INPUTS"`. Do NOT use `"ok"`, `"success"`, `"done"`, etc.
- `page` MUST be the integer 1-indexed physical PDF page number — i.e. echo `PAGE_NUM`. The field name is `page` (NOT `page_num`).
- `page_label` is a JSON string OR JSON `null`. Use `null` when no folio is visibly printed.
- `page_label_source` MUST be the literal string `"vlm"` on every successful skill run. On `FAILED` / `FAILED_INPUTS` / `NO_FOLIO` runs, set it to `"vlm"` as well — it identifies the producer of this record.
- `location` is one of the six zone literals: `"top-left"`, `"top-center"`, `"top-right"`, `"bottom-left"`, `"bottom-center"`, `"bottom-right"`, or JSON `null` when there is no folio.
- `confidence` is one of: `"high"`, `"medium"`, `"low"`.
- `rationale` is one short sentence in plain English describing what was visually observed (or, on failure, what went wrong).

Example - folio present:

```json
{
  "schema_version": "pdf2md-folio-extract/v1",
  "run_status": "SUCCESS",
  "page": 47,
  "page_label": "47",
  "page_label_source": "vlm",
  "location": "bottom-center",
  "confidence": "high",
  "rationale": "Arabic numeral 47 centered in footer."
}
```

Example - Roman numeral front-matter:

```json
{
  "schema_version": "pdf2md-folio-extract/v1",
  "run_status": "SUCCESS",
  "page": 9,
  "page_label": "xiv",
  "page_label_source": "vlm",
  "location": "bottom-center",
  "confidence": "high",
  "rationale": "Lowercase Roman numeral xiv centered in footer of preface page."
}
```

Example - no folio printed:

```json
{
  "schema_version": "pdf2md-folio-extract/v1",
  "run_status": "NO_FOLIO",
  "page": 3,
  "page_label": null,
  "page_label_source": "vlm",
  "location": null,
  "confidence": "high",
  "rationale": "Chapter-opener page; folio suppressed per house style."
}
```

Example - missing input:

```json
{
  "schema_version": "pdf2md-folio-extract/v1",
  "run_status": "FAILED_INPUTS",
  "page": 47,
  "page_label": null,
  "page_label_source": "vlm",
  "location": null,
  "confidence": "low",
  "rationale": "IMAGE_PATH does not exist."
}
```

#### Output rules

- `page_label` MUST be the exact string visible on the page — preserve case, Roman vs. Arabic form, hyphens, and any section prefix. Do NOT normalize `"xiv"` to `"14"`, do NOT strip a `"B-"` prefix, do NOT zero-pad.
- `page_label` is `null` only when no folio is visibly printed.
- `location` MUST reflect the zone where the folio was observed; it is `null` if and only if `page_label` is `null`.
- `page_label_source` is always `"vlm"`.
- `confidence` should be `"high"` when the folio is clearly legible in a conventional folio zone, `"medium"` when the glyph is partially obscured or the zone is unusual, and `"low"` when the reading is a best guess.
- `rationale` is one sentence; do not include multi-paragraph explanations.

#### Non-negotiable constraints

- Single page in, one JSON out.
- No cross-page context.
- No folio invention from the physical sequence or from neighbours.
- The emitted `page_label` must be visible on the page image.
- The JSON must parse with standard `json.loads`.

#### QA expectations

- `OUTPUT_PATH` exists and is non-empty.
- JSON parses successfully.
- `run_status` is one of `SUCCESS`, `NO_FOLIO`, `FAILED`, or `FAILED_INPUTS`.
- `page` equals the runtime `PAGE_NUM`.
- `page_label` is a string when `run_status == "SUCCESS"`, and `null` otherwise.
- `location` is one of the six zone literals when `page_label` is a string, and `null` otherwise.
- `page_label_source` is the literal `"vlm"`.

## Component: skills/pdf2md-folio-extract/TOOL_POLICY.md

### pdf2md-folio-extract - Tool Policy

#### Preferred tool order

Reasoning-first: this skill is VLM-driven. The agent reads the page PNG as multimodal input and writes one JSON file. There are no deterministic helpers inside this skill.

Deterministic tools run outside this skill, under the `PDF2MD` orchestrator (folio-map assembly, reconciliation against the physical sequence, propagation into per-page asset records, etc.).

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- None - no TASK-enforced deterministic allowlist. The `allowed-tools` frontmatter field is intentionally omitted.

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None inside this skill. Operational deterministic tools are invoked by `PDF2MD`, not by the folio-extract worker.

#### Expected use of reasoning

Reasoning is limited to:

- Locating the printed folio in conventional folio zones on the page image.
- Transcribing the visible glyph verbatim (Arabic / Roman / prefixed / hyphenated forms) without normalization.
- Naming the zone (`top-left`, `top-center`, `top-right`, `bottom-left`, `bottom-center`, `bottom-right`).
- Assigning a confidence label based on legibility and zone conventionality.
- Recognizing when no folio is printed and emitting `NO_FOLIO` rather than inventing a value.

The page image is the sole authority for folio existence and form.

#### Disallowed use

- MUST NOT crop images.
- MUST NOT write PNG, CSV, or XLSX files.
- MUST NOT rewrite Markdown.
- MUST NOT assemble or aggregate folio maps.
- MUST NOT read files outside `IMAGE_PATH`.
- MUST NOT write files outside `OUTPUT_PATH`.
- MUST NOT consult neighbouring page images, sibling folio JSON, manifests, the source PDF, the page Markdown, or any TOC / outline artifact.
- MUST NOT invent a folio from the physical PDF sequence (`PAGE_NUM`).
- MUST NOT infer a folio from neighbouring pages' numbering.
- MUST NOT normalize Roman numerals to Arabic, strip section prefixes, or zero-pad.
- MUST NOT assign final stable filenames.

#### Write boundary

Writes are limited to exactly one file:

- `OUTPUT_PATH` - page-level folio JSON

The output filename is deterministic from the orchestrator brief. The skill must not derive or modify it.
