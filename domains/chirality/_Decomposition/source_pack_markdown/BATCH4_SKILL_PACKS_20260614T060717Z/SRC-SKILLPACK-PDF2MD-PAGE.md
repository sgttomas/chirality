# Source Pack: Skill pack: pdf2md-page

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/pdf2md-page/BRIEF_SCHEMA.md

### pdf2md-page — Brief Schema

Use this skill with `TASK` like this (typically spawned by the PDF2MD orchestrator, one invocation per page):

```md
PURPOSE: Convert one PDF page image to raw Markdown
RequestedBy: PDF2MD

ScopePath: /abs/path/to/pdf_work_dir
TaskSkill: pdf2md-page

Tasks:
  - Read the page image and transcribe its contents to Markdown per the 8 conversion rules

ApplyEdits: true

AllowedWriteTargets:
  - "/abs/path/to/pdf_work_dir/pages/page_003.md"

RuntimeOverrides:
  IMAGE_PATH: /abs/path/to/pdf_work_dir/pages/page_003.png
  OUTPUT_PATH: /abs/path/to/pdf_work_dir/pages/page_003.md
  PAGE_NUM: 3
  TOTAL_PAGES: 42

ExpectedOutputs:
  - /abs/path/to/pdf_work_dir/pages/page_003.md
```

#### Required fields

| Field | Value | Notes |
|---|---|---|
| `TaskSkill` | `pdf2md-page` | Must match skill folder name |
| `RuntimeOverrides.IMAGE_PATH` | Absolute path to the page PNG | Must exist, must have `.png` extension |
| `RuntimeOverrides.OUTPUT_PATH` | Absolute path to the page `.md` | Parent directory must exist |
| `RuntimeOverrides.PAGE_NUM` | 1-indexed page number | Positive integer |
| `RuntimeOverrides.TOTAL_PAGES` | Total pages in the document | Positive integer, >= `PAGE_NUM` |

#### Optional fields

None. This skill has no optional brief fields and no optional runtime overrides.

#### TaskProfile

`NONE` — this skill runs in generic TASK shell mode without a profile.

#### Read boundary

The skill reads only:

- `{IMAGE_PATH}`

It must NOT read any other file, including neighbouring page images, manifests, or sibling markdown.

#### Write boundary

The skill writes only:

- `{OUTPUT_PATH}`

The output filename is deterministic — it is precisely the `OUTPUT_PATH` supplied in the brief. The skill does not derive or modify the filename.

#### AllowedTools

Omit `AllowedTools`. This is a VLM-reasoning-only skill with no deterministic tool dependencies; the skill uses only the agent's native `Read` (multimodal) and `Write` tools.

#### Notes

- `ScopePath` should normally be the PDF working directory so that `IMAGE_PATH` and `OUTPUT_PATH` both resolve within scope.
- `ApplyEdits: true` is appropriate because this skill is expected to write the per-page Markdown artifact.
- One invocation processes one page. The PDF2MD orchestrator spawns one task per page for parallel fanout.
- The orchestrator is responsible for post-processing (`postprocess_page.py`), assembly (`assemble_markdown.py`), and final cleanup. This skill emits raw VLM Markdown only.
- On any failure, the skill still writes a placeholder line to `OUTPUT_PATH` so that the orchestrator's assembly step can account for the missing page.

## Component: skills/pdf2md-page/QA_CHECKS.md

### pdf2md-page — QA Checks

Minimum checks for a valid run:

1. `IMAGE_PATH` exists and has a `.png` extension (or `FAILED_INPUTS` is returned with a placeholder written to `OUTPUT_PATH`).
2. `OUTPUT_PATH` parent directory exists before the skill writes to it.
3. `OUTPUT_PATH` exists after the run and is non-empty.
4. No files other than `OUTPUT_PATH` were written.
5. No files other than `IMAGE_PATH` were read.
6. The output is raw VLM Markdown — no markdown fences, no commentary, no "Page X of Y" markers, no post-processing applied.

#### Output content checks

The written Markdown at `OUTPUT_PATH` should satisfy:

| Check | Requirement |
|---|---|
| Content fidelity | All visible text, tables, and structural elements from the page image are represented |
| No invention | No content appears that is not visible in the image (no hallucinated URLs, text, or structure) |
| Heading hierarchy | At most one `#` title per page; subsequent headings use `##`, `###`, `####` |
| Table format | Tables use GFM pipe format with alignment markers, or HTML `<table>` when pipe format is insufficient |
| Code fencing | Code blocks use triple-backtick fences with language identifier; inline code uses single backticks |
| Formulas | Mathematical expressions use LaTeX delimiters (`$inline$`, `$$display$$`) |
| No page chrome | Page numbers, repeated headers/footers, and decorative borders are omitted |
| No output fences | The output is NOT wrapped in ` ```markdown ``` ` fences |

#### Failure posture

If the input image cannot be read or its content cannot be interpreted, the skill still writes a placeholder to `OUTPUT_PATH`:

| Failure mode | Placeholder written | RUN_STATUS |
|---|---|---|
| `IMAGE_PATH` missing or not a `.png` | `*[Page {PAGE_NUM}: image not found]*` | `FAILED_INPUTS` |
| Image unreadable (blank page, unreadable scan, VLM cannot extract) | `*[Page {PAGE_NUM}: content not extractable]*` | `FAILED` |
| Conversion succeeded | (raw Markdown content) | `SUCCESS` |

`OUTPUT_PATH` is never left unwritten. The orchestrator relies on every per-page output existing so that assembly can account for the full page range.

#### Success case

A clean run reports:

- `RUN_STATUS=SUCCESS`
- `PAGE_NUM` (the page number processed)
- `CHARS` (approximate character count of the output Markdown)
- `OUTPUT_PATH` (the exact file written)

#### Orchestrator-side considerations

These checks are out of scope for this skill but are expected of the PDF2MD orchestrator that spawns it:

- Aggregating `RUN_STATUS` across all per-page invocations
- Reporting partial-success runs explicitly (listing pages with `FAILED` / `FAILED_INPUTS`)
- Running `postprocess_page.py` on raw per-page Markdown after fanout completes
- Running `assemble_markdown.py` to stitch per-page files into the final document
- Producing the final `manifest.json`

A `pdf2md-page` invocation is valid on its own merits when the checks above pass, regardless of the orchestrator's downstream handling.

## Component: skills/pdf2md-page/SKILL.md

---
name: pdf2md-page
description: Convert a single PDF page PNG to raw Markdown via multimodal vision. Use when PDF2MD orchestrator spawns per-page fanout; one image in, one markdown file out, no post-processing.
compatibility: Chirality TASK; invoked by PDF2MD orchestrator for per-page fanout (sibling to skills/pdf2md/ which excludes page-level fanout)
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — pdf2md-page

#### Purpose

Convert **one PDF page image** to clean, well-structured Markdown using the agent's multimodal Read tool (VLM vision). Spawned by the PDF2MD orchestrator as per-page fanout. Reads one PNG, writes one `.md` file, returns a status.

This skill is intentionally minimal: its entire value is the multimodal perception step — reading a page image and transcribing its contents to Markdown. All cleanup, coordination, and assembly are the PDF2MD orchestrator's responsibility.

#### Suitable agent shells

- `TASK` in generic shell mode, spawned by the PDF2MD orchestrator

Not the right fit for:
- whole-PDF conversion (use `skills/pdf2md/` or the full PDF2MD persona instead)
- post-processing, cleanup, or assembly (PDF2MD handles those in its own phases)
- any task that needs cross-page context

#### Relationship to `skills/pdf2md/`

This skill is the **per-page fanout companion** to `skills/pdf2md/`.

- `skills/pdf2md/` handles whole-PDF orchestration (rasterization, post-processing, assembly) in a single bounded run and explicitly excludes page-level fanout.
- `skills/pdf2md-page/` (this skill) handles exactly one page per invocation, spawned in parallel by the PDF2MD orchestrator.

The two skills compose: the PDF2MD persona rasterizes the PDF, spawns one `TASK` + `pdf2md-page` invocation per page image, collects the per-page Markdown outputs, then runs its own post-processing and assembly phases.

#### Inputs

##### Required

- `RuntimeOverrides.IMAGE_PATH` — absolute path to the page PNG file
- `RuntimeOverrides.OUTPUT_PATH` — absolute path where the page Markdown will be written
- `RuntimeOverrides.PAGE_NUM` — 1-indexed page number
- `RuntimeOverrides.TOTAL_PAGES` — total pages in the document

##### Optional

- None. This skill has no optional runtime overrides.

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `IMAGE_PATH` | Absolute path to the page PNG file | **Required** | Must exist and have `.png` extension |
| `OUTPUT_PATH` | Absolute path to write the page Markdown | **Required** | Parent directory must exist |
| `PAGE_NUM` | 1-indexed page number | **Required** | Positive integer |
| `TOTAL_PAGES` | Total pages in the document | **Required** | Positive integer, >= `PAGE_NUM` |

#### Read boundary

Reads are limited to exactly one file:

- `{RuntimeOverrides.IMAGE_PATH}` — the single page PNG

The skill must NOT read any other file. Zero cross-page context.

#### Write boundary

Writes are limited to exactly one file:

- `{RuntimeOverrides.OUTPUT_PATH}` — the page Markdown (or a failure placeholder)

The output filename is deterministic: it is precisely `OUTPUT_PATH` as provided in the brief.

#### Tool usage

- No deterministic tools. This is a VLM-reasoning-only skill.
- The `allowed-tools` frontmatter field is intentionally omitted.
- The agent uses its native `Read` tool for multimodal PNG input and its native `Write` tool for the single output file.

Disallowed behavior:

- MUST NOT run `postprocess_page.py` or any other cleanup tool. Post-processing is PDF2MD's responsibility.
- MUST NOT read any file other than `IMAGE_PATH`.
- MUST NOT write any file other than `OUTPUT_PATH`.
- MUST NOT widen scope beyond the designated page.

#### Method

##### Step 1 — Validate inputs

1. Confirm `IMAGE_PATH` exists and is a `.png` file.
2. Confirm `OUTPUT_PATH` parent directory exists.
3. If `IMAGE_PATH` does not exist: write `*[Page {PAGE_NUM}: image not found]*` to `OUTPUT_PATH` and return `RUN_STATUS=FAILED_INPUTS`.

##### Step 2 — Read and convert the page image

1. Use the `Read` tool to load `IMAGE_PATH`. The `Read` tool handles PNG images as multimodal (vision) input.
2. Examine the page image and convert its contents to Markdown following these rules precisely:

**RULE 1 — TEXT PRESERVATION**
- Preserve ALL text content completely and accurately.
- Maintain the reading order as a human would read the page.
- Correct obvious OCR-like errors only if you are completely certain.

**RULE 2 — STRUCTURE**
- Use `#` for the main page title (at most one per page).
- Use `##` for major sections, `###` for subsections, `####` for minor headings.
- Use `-` for unordered lists and `1. 2. 3.` for ordered lists.
- Preserve list nesting with indentation.
- Use `**bold**` and `*italic*` to match the visual emphasis.

**RULE 3 — TABLES**
- Convert tables to GFM pipe format.
- Add alignment markers (`:---`, `:---:`, `---:`) matching visual alignment.
- If a table is too complex for pipe format, use HTML `<table>` markup.
- Also emit a `[TABLE: <visible caption>]` placeholder line immediately above the GFM/HTML transcription, per RULE 8. The inline GFM and the placeholder are both required.

**RULE 4 — CODE**
- Wrap code blocks in triple backticks with language identifier.
- Wrap inline code in single backticks.

**RULE 5 — FORMULAS**
- Render mathematical expressions using LaTeX: `$inline$` and `$$display$$`.

**RULE 6 — WHAT TO IGNORE**
- Page numbers (bottom/top of page).
- Repeated headers/footers that appear on every page.
- Decorative borders and lines that carry no content meaning.

**RULE 7 — OUTPUT FORMAT**
- Output ONLY the Markdown content.
- Do NOT wrap in ` ```markdown ``` ` fences.
- Do NOT add commentary or explanations.
- Do NOT add "Page X of Y" markers.
- Start directly with the page content.

**RULE 8 — ASSET PLACEHOLDERS**

Every visible figure, table, or non-text image on the page MUST be marked with a deterministic placeholder so downstream tooling (`tools/pdf2md/rewrite_inline_asset_refs.py`) can rewrite each placeholder to a working asset link. Placeholders are part of the Markdown content (RULE 7 still applies — no external commentary), and they appear in document reading order at the position of the asset on the page.

Required placeholder formats:

- **Figures (captioned plots, diagrams, charts, schematics, illustrations):**
  - Format: `[FIGURE: <full visible caption text including the figure number>]`
  - Example: `[FIGURE: Fig. 1.1 Yield stress-strain curve of copper in compression. After Cook and Larke [1].]`
  - One placeholder per visible figure. If a caption spans multiple lines on the page, join them into one line inside the brackets.
  - The leading `FIGURE:` token is REQUIRED — it is what the downstream rewriter keys on. Do not substitute `Figure:` (camelcase), `FIG:`, or omit it. Citations like `[1]` inside the caption are fine; the rewriter handles one level of nested brackets.

- **Tables (any tabular data, captioned or not):**
  - Format: `[TABLE: <full visible caption text, OR a brief summary if no caption>]`
  - Example: `[TABLE: Table 4.2 Comparison of stress values - Guided Cantilever vs General Analytical]`
  - The placeholder appears IMMEDIATELY ABOVE the GFM/HTML transcription required by RULE 3. Both surfaces are required: the placeholder for the asset rewriter, the GFM/HTML for human readability.
  - The leading `TABLE:` token is REQUIRED.

- **Non-figure non-table images (cover logos, decorative emblems, photographs, equation plates, etc.):**
  - Format: `[<short descriptor> logo]` / `[<descriptor> emblem]` / `[<descriptor> seal]` / `[<descriptor> cover]` / `[<descriptor> photograph]` / `[<descriptor> photo]` / `[<descriptor> image]`.
  - Example: `[Kellogg logo]`, `[Cover image]`, `[ASME emblem]`.
  - Use the trailing keyword that best describes the asset. The rewriter recognizes `logo`, `emblem`, `seal`, `cover`, `photograph`, `photo`, and `image`.

What MUST NOT happen:

- Do NOT describe a figure or table only in prose ("As shown in Fig. 1.4, the curve...") without also emitting the bracketed placeholder. The asset would land in a trailing "Unmatched Page Assets" block at downstream assembly, which produces noisier final Markdown.
- Do NOT use `![Fig. ...](...)` markdown-image syntax for figures — those are not the canonical placeholder shape. Use `[FIGURE: ...]`.
- Do NOT skip the placeholder for the cover-page logo or other oddball images on the assumption that they are "decorative" (RULE 6 ignores page numbers and repeating headers/footers, NOT one-off images).
- Do NOT invent placeholders for assets that are not visible on the page.

##### Step 3 — Write output and return status

1. Write the Markdown to `OUTPUT_PATH` using the `Write` tool.
2. If conversion succeeded: return `RUN_STATUS=SUCCESS` with the page number and a brief note (e.g., "Page 3/42: 1,247 chars").
3. If the image could not be interpreted (blank page, unreadable scan): write `*[Page {PAGE_NUM}: content not extractable]*` to `OUTPUT_PATH` and return `RUN_STATUS=FAILED`.

#### Outputs

- `{OUTPUT_PATH}` — Markdown text for one page (or a failure placeholder)

#### Return value

The skill returns to the caller:

- `RUN_STATUS`: `SUCCESS` | `FAILED` | `FAILED_INPUTS`
- `PAGE_NUM`: the page number processed
- `CHARS`: approximate character count of the output

#### Non-negotiable constraints

- **Single-page scope.** One page in, one markdown snippet out. No cross-page context.
- **OUTPUT_PATH-only writes.** Write scope is strictly the designated `OUTPUT_PATH` for this page.
- **Single-file reads.** Read scope is strictly `IMAGE_PATH`. No other files may be read.
- **Raw VLM output only.** No post-processing, no cleanup rules applied. PDF2MD handles that.
- **No invention.** The agent does not add content that is not visible in the image. No hallucinated text, URLs, or structural elements.
- **Content fidelity.** All visible text, tables, and structural elements from the page image must be represented. Missing content is a defect.
- **Deterministic output filename.** The output is written to exactly `OUTPUT_PATH` as provided in the brief; the skill does not derive or modify the filename.
- **Failure placeholders.** On read failure or extraction failure, write a placeholder line to `OUTPUT_PATH` and return the appropriate failure status. Never leave `OUTPUT_PATH` unwritten.

#### QA expectations

- `OUTPUT_PATH` exists after the run and is non-empty.
- No files other than `OUTPUT_PATH` were written.
- No files other than `IMAGE_PATH` were read.
- Output is raw VLM Markdown (no post-processing applied, no fences, no commentary).
- All visible page content is represented in the Markdown.
- No invented content beyond what is visible in the image.
- Failure cases produce a placeholder line at `OUTPUT_PATH` and an explicit `FAILED` or `FAILED_INPUTS` status.

## Component: skills/pdf2md-page/TOOL_POLICY.md

### pdf2md-page — Tool Policy

#### Preferred tool order

Reasoning-first: this skill is LLM-driven; no deterministic tool ordering applies. The agent uses its native Read tool to load the page PNG as multimodal (vision) input, performs VLM transcription of the image contents to Markdown, and uses its native Write tool to produce the single output file.

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- None — no TASK-enforced deterministic allowlist (the `allowed-tools` frontmatter field is intentionally omitted)

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None — no operational helpers declared (SKILL.md states: "No deterministic tools. This is a VLM-reasoning-only skill"; post-processing is PDF2MD's responsibility)

#### Expected use of reasoning

This is a VLM-reasoning-only skill. The agent's entire value is the multimodal perception step: reading a page image and transcribing its contents to Markdown. Reasoning governs input validation, image examination, Markdown structuring per the declared rules (text preservation, structure, tables, code, formulas, ignore-list, output format), and failure-placeholder handling. All cleanup, coordination, and assembly belong to the PDF2MD orchestrator and are out of scope for this skill.

#### Disallowed use

- MUST NOT run `postprocess_page.py` or any other cleanup tool. Post-processing is PDF2MD's responsibility.
- MUST NOT read any file other than `IMAGE_PATH`.
- MUST NOT write any file other than `OUTPUT_PATH`.
- MUST NOT widen scope beyond the designated page.
- No hidden reliance on tools outside the declared list unless the human expands AllowedTools. No writes outside declared scope.

#### Write boundary

Writes are limited to exactly one file:

- `OUTPUT_PATH` — the page Markdown (or a failure placeholder)

The output filename is deterministic: it is precisely `OUTPUT_PATH` as provided in the brief. The skill does not derive or modify the filename.
