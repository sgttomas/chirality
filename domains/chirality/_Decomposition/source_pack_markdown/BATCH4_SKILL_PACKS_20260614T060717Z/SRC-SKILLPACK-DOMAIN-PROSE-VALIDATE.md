# Source Pack: Skill pack: domain-prose-validate

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/domain-prose-validate/BRIEF_SCHEMA.md

### domain-prose-validate - Brief Schema

Use this skill with `TASK` like this. It is normally spawned by the Gate 1.5-P Stage 1 orchestration helper (one TASK per page, fanned out in parallel):

```md
PURPOSE: Independently re-extract one PDF page's prose, equations, and asset placeholders for Gate 1.5-P comparison
RequestedBy: DOMAIN_DECOMP (Gate 1.5-P Stage 1)

ScopePath: /abs/path/to/_Sources/BookX
TaskSkill: domain-prose-validate

Tasks:
  - Read one page raster and the asset bbox hints for that page
  - Produce an independent Markdown re-extract: prose, $$...$$ display equations, and [FIGURE:]/[TABLE:]/[IMAGE:] placeholders in reading order
  - Do not read any pre-existing per-page Markdown or the assembled book Markdown

ApplyEdits: true

AllowedWriteTargets:
  - "/abs/path/to/_Sources/BookX/audit/prose_validation_extracts/page_0047.reextract.md"

RuntimeOverrides:
  IMAGE_PATH: /abs/path/to/_Sources/BookX_pdf2md_work/page_0047.png
  ASSET_BBOX_HINTS_PATH: /abs/path/to/_Sources/BookX/audit/prose_validation_extracts/page_0047.hints.json
  OUTPUT_PATH: /abs/path/to/_Sources/BookX/audit/prose_validation_extracts/page_0047.reextract.md
  PAGE_NUM: 47

ExpectedOutputs:
  - /abs/path/to/_Sources/BookX/audit/prose_validation_extracts/page_0047.reextract.md
```

#### Required fields

| Field | Value | Notes |
|---|---|---|
| `TaskSkill` | `domain-prose-validate` | Must match skill folder name |
| `RuntimeOverrides.IMAGE_PATH` | Absolute path to the page PNG | Must exist, must have `.png` extension |
| `RuntimeOverrides.ASSET_BBOX_HINTS_PATH` | Absolute path to the per-page bbox-hints JSON | Must exist, must have `.json` extension |
| `RuntimeOverrides.OUTPUT_PATH` | Absolute path to the `.reextract.md` file | Parent directory must exist |
| `RuntimeOverrides.PAGE_NUM` | 1-indexed page number | Positive integer |

#### Optional fields

None. Stage 1 has no policy knobs; all knobs (canonicalization version, noise floor, equation-content threshold) live in Stage 2's deterministic comparator.

#### TaskProfile

`NONE` - this skill runs in generic TASK shell mode without a profile.

#### Read boundary

The skill reads only:

- `{IMAGE_PATH}`
- `{ASSET_BBOX_HINTS_PATH}`

It must **not** read any pre-existing `page_*.md`, the assembled `<book>.md`, neighbouring page images, sibling manifests, or audit sidecars. Reading the original extract would defeat the confirmation-bias break that is the entire point of Gate 1.5-P Stage 1.

#### Write boundary

The skill writes only:

- `{OUTPUT_PATH}`

#### Output format

`OUTPUT_PATH` is a Markdown file containing the page body only (no frontmatter, no `# Page N` heading, no metadata):

- Prose paragraphs in reading order, preserving printed line breaks within paragraphs.
- Display equations as `$$...$$` blocks on their own line(s) at the reading-order position.
- Inline equations as `$...$` within prose.
- Asset placeholders on their own line in the canonical form:
  - `[FIGURE: <caption text as printed>]`
  - `[TABLE: <caption text as printed>]`
  - `[IMAGE: <one-line visual description>]`
- File ends with a single trailing newline.

#### `ASSET_BBOX_HINTS_PATH` shape

```json
{
  "page": 47,
  "assets": [
    {"kind": "fig", "asset_id": "BookX_p0047_fig01", "bbox_norm": [0.1, 0.2, 0.9, 0.5]},
    {"kind": "tbl", "asset_id": "BookX_p0047_tbl01", "bbox_norm": [0.1, 0.55, 0.9, 0.85]}
  ]
}
```

Hints are consumed for **guidance only** — to set expectations about which placeholder kinds appear and where. `asset_id` MUST NOT appear in the output Markdown. Caption text comes from the raster, not the hints file.

#### AllowedTools

Omit `AllowedTools`. This is a VLM-reasoning-only skill with no deterministic tool dependencies.

#### CustomInstructions

Usually unnecessary. If used, keep them run-specific and do not restate the whole skill contract. Good examples:

- "Two-column page: emit left column fully before right column."
- "Page has a marginal footnote rule — emit footnote text as a final paragraph after the body prose."
- "If a table caption is in a non-Latin script, transliterate inside the `[TABLE: ...]` placeholder and add `(transliterated)`."

## Component: skills/domain-prose-validate/QA_CHECKS.md

### domain-prose-validate - QA Checks

Minimum checks for a valid run:

1. `IMAGE_PATH` exists and has a `.png` extension, or the skill aborts without writing.
2. `ASSET_BBOX_HINTS_PATH` exists and has a `.json` extension, or the skill aborts without writing.
3. `OUTPUT_PATH` parent directory exists before write.
4. `OUTPUT_PATH` exists after the run and is non-empty.
5. `OUTPUT_PATH` ends with a single trailing newline (`\n`).
6. No files other than `IMAGE_PATH` and `ASSET_BBOX_HINTS_PATH` were read. **In particular, no `page_*.md`, no assembled `<book>.md`, and no audit sidecar was opened.** This is the load-bearing anti-confirmation-bias invariant of Gate 1.5-P Stage 1.
7. No files other than `OUTPUT_PATH` were written.

#### Output body checks

The output Markdown body must satisfy:

| Check | Requirement |
|---|---|
| No frontmatter | The file must not begin with a YAML frontmatter block (`---`). The body is page content only. |
| No metadata heading | The file must not include a `# Page N`, `## Page N`, or other page-identifying heading. |
| Display equations | Standalone equations appear as `$$...$$` blocks on their own line(s), surrounded by blank lines. |
| Inline equations | Equations embedded in prose appear as `$...$` (single-dollar). |
| Asset placeholder syntax | Each asset placeholder is on its own line, surrounded by blank lines, and uses exactly one of: `[FIGURE: <text>]`, `[TABLE: <text>]`, `[IMAGE: <text>]`. The prefix is uppercase, followed by a colon and a single space. |
| No image / link syntax for assets | The output must not contain `![alt](path)` image syntax or `[XLSX](path)` link syntax. Asset references use the bracketed placeholder form only. |
| No asset IDs | The output must not contain `asset_id` values copied from `ASSET_BBOX_HINTS_PATH` (e.g. `BookX_p0047_fig01`). |

#### Placeholder-count consistency

Compare the placeholder counts in `OUTPUT_PATH` against `ASSET_BBOX_HINTS_PATH`:

| Hints entry kind | Placeholder form | Expected relationship |
|---|---|---|
| `kind == "fig"` | `[FIGURE: ...]` | Count should match within reasonable tolerance |
| `kind == "tbl"` | `[TABLE: ...]` | Count should match within reasonable tolerance |
| `kind == "img"` | `[IMAGE: ...]` | Count should match within reasonable tolerance |

Note: a count mismatch is **not** a skill-level failure — it is exactly the signal Gate 1.5-P Stage 2 needs to surface as a structural fail for the page. The QA check exists so the orchestrator can flag implausibly large drift (e.g. zero placeholders emitted when the hints file lists four assets) for orchestrator-side review before invoking the comparator.

#### Failure posture

| Failure mode | Required behavior |
|---|---|
| Missing input file (`IMAGE_PATH` or `ASSET_BBOX_HINTS_PATH`) | Abort without writing. The orchestrator will treat the absent re-extract as a Stage 2 structural fail for the page. |
| Unreadable page raster | Abort without writing, or write only the legible portion with no fabricated content. Do not paraphrase or summarize unreadable regions. |
| Confirmation-bias breach (asked to read a `page_*.md` or `<book>.md`) | Refuse the read. The skill MUST NOT consult any prior extract under any circumstance. |
| Hints file is empty or has zero assets | Emit prose + equations only. Do not synthesize asset placeholders to match an imagined manifest. |
| Hints file references kinds not in `{fig, tbl, img}` | Ignore the unknown kind. Stage 2 will surface the mismatch. |

#### Orchestrator-side checks

These checks belong to the Gate 1.5-P orchestration, not this skill:

- Building the per-page `ASSET_BBOX_HINTS_PATH` from the asset manifest before dispatch.
- Verifying `OUTPUT_PATH` was created and is non-empty after each TASK completes.
- Confirming no `page_*.md` was opened during the TASK (audit-log inspection where available).
- Running `tools/source_audit/compare_extracts.py` against each `(page_NNNN.md, page_NNNN.reextract.md)` pair to produce `prose_validation.json` (Stage 2).
- Dispatching `pdf2md-page-assets` re-extraction for pages flagged with structural fails (Stage 3).
- Dispatching `equation-flag-interpret` for equation-content proposals before writing to `equations_backcheck.json` with `source: "1.5-P-machine"` (Stage 3).

## Component: skills/domain-prose-validate/SKILL.md

---
name: domain-prose-validate
description: Independently re-extract one rasterized PDF page's prose, equations, and asset placeholders for downstream extraction-reproducibility comparison (Gate 1.5-P Stage 1).
compatibility: Chirality TASK; invoked by DOMAIN_DECOMP Gate 1.5-P orchestration as the first stage of the three-stage prefilter.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL - domain-prose-validate

#### Purpose

Produce an **independent** Markdown re-extract of one rasterized PDF page so that a downstream deterministic comparator (Gate 1.5-P Stage 2) can detect divergences against the original `pdf2md` extract. This skill is the perception stage of the Gate 1.5-P extraction-reproducibility prefilter described in `agents/AGENT_DOMAIN_DECOMP.md`.

The skill reads one page image plus a bbox-hints JSON describing where assets are expected, and writes one Markdown file containing:

- Prose paragraphs in reading order.
- Display equations as `$$...$$` blocks at their reading-order position.
- Asset placeholders inline at their reading-order position, in the canonical bracketed form (`[FIGURE: ...]`, `[TABLE: ...]`, `[IMAGE: ...]`).

It does **not** crop assets, transcribe table cells, assign asset IDs, write JSON, or emit a manifest. Those responsibilities belong to other skills and to the Stage 2 comparator.

#### Suitable agent shells

- `TASK` in generic shell mode, spawned by the Gate 1.5-P Stage 1 orchestration helper

Not the right fit for:

- whole-PDF re-extraction
- cross-page reasoning
- comparator/diff logic (Stage 2 is deterministic, not VLM)
- adjudicating equation differences (Stage 3 dispatches `equation-flag-interpret`)
- asset materialization, manifest aggregation, or filename assignment

#### Inputs

Required runtime overrides:

- `IMAGE_PATH` - absolute path to the page PNG
- `ASSET_BBOX_HINTS_PATH` - absolute path to a JSON file listing expected asset bboxes + kinds for this page
- `OUTPUT_PATH` - absolute path for the re-extract `.md` file
- `PAGE_NUM` - 1-indexed page number

Optional runtime overrides:

- none

##### `ASSET_BBOX_HINTS_PATH` shape

The hints file is consumed for **guidance only** — it tells the skill *where* placeholders are expected so the agent can be deliberate about emitting them. It is not authoritative; the page raster remains the source of truth for caption text and reading order.

```json
{
  "page": 47,
  "assets": [
    {"kind": "fig", "asset_id": "BookX_p0047_fig01", "bbox_norm": [0.1, 0.2, 0.9, 0.5]},
    {"kind": "tbl", "asset_id": "BookX_p0047_tbl01", "bbox_norm": [0.1, 0.55, 0.9, 0.85]}
  ]
}
```

Each entry's `kind` is one of `fig`, `tbl`, or `img`. The `asset_id` is informational only and MUST NOT appear in the output Markdown.

#### Read boundary

Reads are limited to exactly two files:

- `{IMAGE_PATH}`
- `{ASSET_BBOX_HINTS_PATH}`

**Anti-confirmation-bias clause (cornerstone of Gate 1.5-P):**

The skill MUST NOT read, peek at, infer, or reference any pre-existing per-page Markdown extract (e.g. `page_NNNN.md` under `_Sources/<book>_pdf2md_work/`), the assembled `<book>.md`, sibling pages, the audit sidecars, or any other materialized extraction artifact. The entire point of Stage 1 is to produce a re-extract that is causally independent of the original pdf2md output — reading the original would defeat the comparator and silently collapse Gate 1.5-P. If any path matching `page_*.md` or the book-level assembled Markdown is encountered, the skill MUST refuse to read it.

Do not read neighbouring pages, manifests, sibling Markdown files, asset XLSX files, or previously materialized assets. This preserves page-level parallelism and prevents cross-page priming.

#### Write boundary

Writes are limited to exactly one file:

- `{OUTPUT_PATH}`

The output filename is supplied by the orchestrator and must not be derived or changed by the skill.

#### Tool usage

- No deterministic tools.
- The `allowed-tools` frontmatter field is intentionally omitted.
- The agent uses native multimodal reading for `IMAGE_PATH`, native text reading for `ASSET_BBOX_HINTS_PATH`, and native writing for `OUTPUT_PATH`.

Disallowed behavior:

- Do not read any pre-existing per-page Markdown or the assembled book Markdown (see anti-confirmation-bias clause).
- Do not crop images.
- Do not write PNG, CSV, JSON, or XLSX files.
- Do not transcribe table cells — emit a `[TABLE: ...]` placeholder.
- Do not assign asset filenames or asset IDs.
- Do not emit Markdown frontmatter, page numbers, or any metadata header in the output.
- Do not widen read or write scope beyond the declared two inputs and one output.

#### Method

##### Step 1 - Validate inputs

1. Confirm `IMAGE_PATH` exists and has a `.png` extension.
2. Confirm `ASSET_BBOX_HINTS_PATH` exists and has a `.json` extension.
3. Confirm `OUTPUT_PATH` parent exists.
4. If any required input is missing or unreadable, abort without writing a partial file. (Stage 2 will treat the missing re-extract as a structural fail for the page.)

##### Step 2 - Read the hints file

1. Parse `ASSET_BBOX_HINTS_PATH` as JSON.
2. Note, for each entry, the `kind` (`fig` / `tbl` / `img`) and the approximate `bbox_norm` region of the page where that asset sits. This is to set expectations only — do not copy `asset_id`, captions, or any other text from the hints into the output. Caption text comes from reading the raster.

##### Step 3 - Re-extract the page from the raster

This step is performed **without** consulting any prior extract. The page image is the sole authority for textual content.

1. Read `IMAGE_PATH` as multimodal input.
2. Transcribe prose paragraphs in document reading order.
3. When a display equation appears in reading order, emit it as a `$$...$$` block on its own line(s) at that position.
4. Inline equations remain inline as `$...$` (single-dollar). Only standalone display equations use `$$...$$`.
5. When an asset region appears in reading order (cross-referenced against `ASSET_BBOX_HINTS_PATH` for expected placement), emit a placeholder on its own line using the exact syntax in the "Output format" section below. The caption / description text inside the placeholder is what the VLM reads from the raster — not what the hints file says.
6. Preserve printed line breaks within paragraphs as they appear on the page. The Stage 2 comparator handles whitespace normalization (NFKC, whitespace collapse, line-break-hyphen repair) before strict-compare.
7. Do not invent content. If a region is unreadable, transcribe what is legible and stop; do not paraphrase or summarize.

##### Step 4 - Write the output

Write `OUTPUT_PATH` containing the page body only. No frontmatter, no `# Page N` heading, no metadata footer. End the file with a single trailing newline.

#### Output format

The re-extract is plain Markdown with three kinds of structural elements:

##### Prose

Plain Markdown paragraphs. Preserve printed line breaks within a paragraph. Separate paragraphs with a blank line.

##### Equations

- **Display equations** appear on their own line(s) as `$$...$$` blocks at the reading-order position where they print.
- **Inline equations** remain inline within prose as `$...$`.

Example:

```
The Reynolds number is defined as

$$Re = \frac{\rho v L}{\mu}$$

where $\mu$ is the dynamic viscosity.
```

##### Asset placeholders

When an asset region appears in reading order, emit exactly one of the following placeholder forms on its own line:

- `[FIGURE: <caption text as printed on the page>]` — for `kind: "fig"`
- `[TABLE: <caption text as printed on the page>]` — for `kind: "tbl"`
- `[IMAGE: <one-line visual description>]` — for `kind: "img"` (uncaptioned images, logos, photographs)

Rules:

- The prefix is uppercase and must be exactly `FIGURE:` / `TABLE:` / `IMAGE:` followed by a single space.
- The placeholder is on its own line, surrounded by blank lines (so it is a structural block, not part of a prose paragraph).
- The caption text comes from reading the raster. Do **not** copy text from `ASSET_BBOX_HINTS_PATH` (which only carries `kind`, `asset_id`, and `bbox_norm`).
- Do not include the `asset_id` from the hints file. Do not emit Markdown image syntax (`![alt](path)`) or link syntax (`[XLSX](...)`) — those are Stage 2's responsibility to align against.
- If a figure or table has no visible caption, emit a concise visual description in the placeholder body (e.g. `[FIGURE: schematic of two-stage compressor with intercooler]`).

#### Non-negotiable constraints

- One page raster + one hints JSON in; one Markdown re-extract out.
- No reading of prior extracts. Confirmation bias defeats Gate 1.5-P.
- No cross-page context.
- No invented prose, equations, or asset placeholders.
- Asset placeholders are emitted in the canonical bracketed form only. No Markdown image / link syntax.
- The output file body contains no frontmatter and no page-number metadata.
- The file ends with a single trailing newline.

#### QA expectations

- `OUTPUT_PATH` exists and is non-empty.
- File ends with a newline.
- Count of `[FIGURE:` / `[TABLE:` / `[IMAGE:` placeholders is consistent with the number of `kind=="fig"` / `kind=="tbl"` / `kind=="img"` entries in `ASSET_BBOX_HINTS_PATH`, within reasonable tolerance. Mismatch is not a hard skill failure (it is exactly the signal Stage 2 needs to surface), but a large drift should be noted as an issue by the orchestrator.
- No file other than `IMAGE_PATH` and `ASSET_BBOX_HINTS_PATH` was read. In particular, no `page_*.md` or assembled book Markdown was opened.
- No file other than `OUTPUT_PATH` was written.

## Component: skills/domain-prose-validate/TOOL_POLICY.md

### domain-prose-validate - Tool Policy

#### Preferred tool order

Reasoning-first: this skill is VLM-driven. The agent reads the asset bbox hints (text JSON) to set expectations, then reads the page PNG as multimodal input, then writes one Markdown file.

Deterministic tools run **outside** this skill, under the Gate 1.5-P orchestration in `DOMAIN_DECOMP`:

1. The Stage 1 orchestrator builds the per-page hints JSON from the asset manifest and dispatches one TASK per page.
2. `tools/source_audit/compare_extracts.py` (Stage 2) deterministically aligns the original `page_NNNN.md` against this skill's `page_NNNN.reextract.md` and emits `prose_validation.json`.
3. Stage 3 (persona) consolidates findings, dispatches `pdf2md-page-assets` re-dispatch for structural fails, and dispatches `equation-flag-interpret` for equation-content proposals.

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- None - no TASK-enforced deterministic allowlist. The `allowed-tools` frontmatter field is intentionally omitted.

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None inside this skill. Operational deterministic tools are invoked by the Gate 1.5-P orchestration, not by the page-level re-extraction worker.

#### Expected use of reasoning

Reasoning is limited to: prose transcription from the page raster, reading-order interpretation, display- vs. inline-equation classification, LaTeX transcription of display equations, and choosing the correct `[FIGURE:]` / `[TABLE:]` / `[IMAGE:]` placeholder form at each asset position. The bbox hints provide expected placement only; the page image remains the sole authority for textual content and caption text.

#### Disallowed use

- MUST NOT read any pre-existing per-page Markdown (`page_*.md`), the assembled `<book>.md`, audit sidecars, or any other materialized extraction artifact. This is the cornerstone of Gate 1.5-P — reading the original extract collapses the comparator.
- MUST NOT read neighbouring page rasters, manifests, sibling Markdown, or asset XLSX files.
- MUST NOT crop images.
- MUST NOT write PNG, CSV, JSON, or XLSX files.
- MUST NOT transcribe table cells (emit a `[TABLE: ...]` placeholder instead).
- MUST NOT emit Markdown image syntax (`![alt](path)`) or link syntax (`[XLSX](...)`) — those are Stage 2's responsibility to align against.
- MUST NOT emit asset IDs, asset filenames, or any text copied from `ASSET_BBOX_HINTS_PATH` other than the implicit choice of placeholder kind.
- MUST NOT emit Markdown frontmatter, `# Page N` headings, or any metadata wrapping in the output.
- MUST NOT read files outside `IMAGE_PATH` and `ASSET_BBOX_HINTS_PATH`.
- MUST NOT write files outside `OUTPUT_PATH`.

#### Write boundary

Writes are limited to exactly one file:

- `OUTPUT_PATH` - the per-page Markdown re-extract

The output filename is deterministic from the orchestrator brief. The skill must not derive or modify it.
