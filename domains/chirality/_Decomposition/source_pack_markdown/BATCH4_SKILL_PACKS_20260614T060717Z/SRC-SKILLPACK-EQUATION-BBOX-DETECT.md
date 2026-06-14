# Source Pack: Skill pack: equation-bbox-detect

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/equation-bbox-detect/BRIEF_SCHEMA.md

### BRIEF SCHEMA — equation-bbox-detect

#### Brief structure

The brief is an INIT-TASK shape rendered by `tools/equation_audit/build_equation_bbox_brief.py`. The worker receives the brief verbatim via TASK.

```yaml
PURPOSE: Detect display-equation bounding boxes on page <N> and emit normalized coordinates for downstream cropping
RequestedBy: EQUATION_AUDIT
ActingSurface: TASK+equation-bbox-detect

ScopePath: <absolute path to the page-work directory>
TaskSkill: equation-bbox-detect

AllowedWriteTargets:
  - "<OUTPUT_PATH>"

RuntimeOverrides:
  IMAGE_PATH: <absolute path to page_NNNN.png>
  PAGE_MD_PATH: <absolute path to per-page Markdown>
  PAGE_NUM: <int>
  OUTPUT_PATH: <absolute path to page_NNNN_eq_bboxes.json>
  EXPECTED_EQUATION_HASHES:
    - <12-hex>
    - <12-hex>
    # ... or `[]` if not provided

CustomInstructions:
  - Identify each DISPLAY equation visible on the page raster (block-level math, typically set off from running prose).
  - Do NOT box inline equations or symbols inside running text.
  - Emit normalized coordinates [x0,y0,x1,y1] in [0,1] relative to the page raster's width/height.
  - Boxes should tightly enclose the display equation without including the surrounding paragraph text.
  - The 'index' field is 1-based, ordered top-to-bottom on the page.
  - Include a 'latex_excerpt' field with the first ~20 characters of the visible LaTeX/symbolic content for cross-check against expected hashes.
  - If a page has no display equations, write {"page": <num>, "equations": []} and return RUN_STATUS=NO_FINDINGS.

ExpectedOutputs:
  - <OUTPUT_PATH>
```

#### Required RuntimeOverrides

| Key | Type | Constraint |
|---|---|---|
| `IMAGE_PATH` | str | absolute path to existing `.png` file |
| `PAGE_MD_PATH` | str | absolute path to existing `.md` file |
| `PAGE_NUM` | int | ≥ 1; matches the `NNNN` in `IMAGE_PATH` |
| `OUTPUT_PATH` | str | absolute path; parent directory must exist; ends in `.json` |

#### Optional RuntimeOverrides

| Key | Type | Constraint |
|---|---|---|
| `EXPECTED_EQUATION_HASHES` | list[str] | each element is a 12-lowercase-hex string |

#### Output schema

The worker writes a single JSON object to `OUTPUT_PATH` matching the schema `tools/equation_audit/crop_equation_regions.py` consumes:

```json
{
  "page": 5,
  "equations": [
    {
      "index": 1,
      "bbox_norm": [0.12, 0.21, 0.85, 0.27],
      "latex_excerpt": "\\frac{2}{\\sqrt{3}} Y ="
    },
    {
      "index": 2,
      "bbox_norm": [0.18, 0.42, 0.78, 0.46],
      "latex_excerpt": "d\\epsilon/\\sigma ="
    }
  ]
}
```

When no display equations are found:

```json
{"page": 5, "equations": []}
```

On a failed run (inputs missing or malformed):

```json
{"page": 5, "equations": [], "error": "<short reason>"}
```

#### Coordinate conventions

- Origin `(0, 0)` is top-left of the page raster.
- `(1, 1)` is bottom-right.
- `bbox_norm = [x0, y0, x1, y1]` where `x0 < x1` and `y0 < y1`.
- All four values are floats in the closed interval `[0.0, 1.0]`.
- The downstream consumer (`crop_equation_regions.py`) adds a small padding ring (default 0.005) before cropping, so the worker's boxes should be visually-tight rather than padded.

#### Status reporting

The worker returns one of:

- `RUN_STATUS=SUCCESS` — at least one display equation detected; bboxes emitted
- `RUN_STATUS=NO_FINDINGS` — no display equations on this page; empty `equations` list emitted
- `RUN_STATUS=FAILED_INPUTS` — required inputs missing or malformed; partial JSON emitted with `error`
- `RUN_STATUS=FAILED` — unexpected failure

Plus: `PAGE_NUM`, `EQUATION_COUNT`.

#### Cross-check semantics

When `EXPECTED_EQUATION_HASHES` is non-empty, the worker is expected to surface its findings in an order that allows the persona to cross-check `latex_excerpt` against the corresponding extracted equation:

- The persona pairs `equations[i].latex_excerpt` against the `i`-th equation in `equations.jsonl` for the page (both are top-to-bottom ordered).
- The persona does NOT require an exact match (page rasters are often slightly different from MD-extracted LaTeX), but flags large mismatches for human review.

The worker does NOT need to compute hashes itself. The `EXPECTED_EQUATION_HASHES` list is for the persona's cross-check after the dispatch completes.

## Component: skills/equation-bbox-detect/QA_CHECKS.md

### QA CHECKS — equation-bbox-detect

#### Output presence

- Exactly one file exists at `OUTPUT_PATH` after the run.
- No other files outside the declared write boundary were created or modified.

#### Output JSON schema

The output file is a single JSON object (not a list, not a JSON-lines stream) with this shape:

| Field | Type | Required | Constraint |
|---|---|---|---|
| `page` | int | yes | Equals `PAGE_NUM` from the brief; ≥ 1 |
| `equations` | list[obj] | yes | Possibly empty; one entry per detected display equation |
| `error` | str | conditional | Present only on `FAILED_INPUTS` runs |

##### `equations[*]` entry schema

| Field | Type | Required | Constraint |
|---|---|---|---|
| `index` | int | yes | 1-based; strictly increasing within `equations` |
| `bbox_norm` | list[float] | yes | Exactly 4 elements: `[x0, y0, x1, y1]`; each in `[0.0, 1.0]`; `x0 < x1`; `y0 < y1` |
| `latex_excerpt` | str | optional | First ~20 chars of visible math content; freeform hint, not authoritative |

#### Coordinate invariants

For every `bbox_norm = [x0, y0, x1, y1]`:

- `0.0 ≤ x0 < x1 ≤ 1.0`
- `0.0 ≤ y0 < y1 ≤ 1.0`
- The four values are floats (not ints, not strings).
- The box is reasonably "tight" around the equation: width and height should each be at least ~1% of the page (extremely small boxes are likely detection errors).
- The box width should be at most ~95% of the page width (a display equation spanning nearly the full width is plausible, but spanning 100% suggests the box accidentally included surrounding prose).
- The box height should be at most ~25% of the page height for typical single-line display equations; multi-line equations may go higher but are bounded by ~50% of the page.

#### Ordering invariants

- `equations[*].index` is 1-based and strictly increasing: `1, 2, 3, ...` with no gaps.
- Boxes are ordered top-to-bottom on the page: for any two consecutive entries `e[i]` and `e[i+1]`, `e[i].bbox_norm[1] ≤ e[i+1].bbox_norm[1]` (entries earlier in the list start no lower than entries later in the list).

#### Non-overlap invariants

- Two distinct entries should not significantly overlap. Compute pairwise IoU (intersection-over-union) on `bbox_norm`. Any pair with IoU > 0.1 is a detection error — the worker should have merged them into one box.
- A display equation may have an equation number (e.g., `(1.5)`) at the far-right margin. The worker may include the number inside the box OR exclude it — both are acceptable, but the choice must be consistent across the page.

#### Cross-check semantics

When `EXPECTED_EQUATION_HASHES` is non-empty:

- `len(equations)` SHOULD equal `len(EXPECTED_EQUATION_HASHES)`. A mismatch is non-fatal (the worker emits whatever it sees on the raster, which is the source of truth for cropping), but the persona surfaces the discrepancy for human review at Gate 2.
- The persona pairs `equations[i].latex_excerpt` against the `i`-th equation hash by position; a wildly different excerpt suggests the worker's top-to-bottom ordering disagreed with the MD's order, OR the page contains equations that didn't appear in the MD's display-equation extraction.

The worker is NOT responsible for resolving cross-check mismatches. It emits its bbox findings; the persona reconciles.

#### Failure reporting

The worker reports a structured `RUN_STATUS`:

- `SUCCESS` — at least one display equation detected; bboxes emitted; all invariants pass
- `NO_FINDINGS` — page contains no display equations; `equations` is `[]`; valid for some pages
- `FAILED_INPUTS` — required inputs were missing or malformed; `equations: []` with an `error` field
- `FAILED` — unexpected failure (image unreadable, write-boundary violation, etc.)

The worker also reports:

- `PAGE_NUM`
- `EQUATION_COUNT`

#### Defects that block downstream

These defects block `crop_equation_regions.py` from emitting valid crops (the persona must re-dispatch this skill or surface the entry for human attention):

- Output file missing or unparseable as JSON
- Top-level `page` ≠ `PAGE_NUM` (would cause the crop tool to write to the wrong page's filename)
- Any `bbox_norm` not in [0,1] or violating `x0 < x1` / `y0 < y1`
- Non-monotonic or gapped `index` values
- Two entries with IoU > 0.5 (severe overlap implies the same equation got boxed twice)
- Output written to a path other than `OUTPUT_PATH`

#### Required evidence

- Worker stdout / `RUN_STATUS` captured by TASK is sufficient evidence for routine success.
- For `FAILED` and `FAILED_INPUTS` runs, the explanation accompanying `RUN_STATUS` is the evidence; the persona decides whether to re-dispatch with corrected inputs.
- For `NO_FINDINGS` runs (page has no display equations), the empty `equations` list is the evidence — the persona simply skips cropping for that page.
- For visual-quality checks (boxes too tight / too loose / cropping body text), the produced PNG crops under `audit/equations/working/crops/` are the evidence; the persona reviews them at Gate 2 alongside the audit HTML.

## Component: skills/equation-bbox-detect/SKILL.md

---
name: equation-bbox-detect
description: Detect display-equation bounding boxes on one rasterized page PNG using multimodal vision and emit normalized coordinates for downstream cropping. Per-page bounded dispatch invoked by EQUATION_AUDIT during Phase 1 when per-equation crops are enabled.
compatibility: Chirality TASK; invoked by EQUATION_AUDIT for per-page bbox detection in Phase 1
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — equation-bbox-detect

#### Purpose

Look at one rasterized page PNG, identify every DISPLAY equation visible on the page (block-level math, set off from running prose), and emit normalized bounding-box coordinates as `page_NNNN_eq_bboxes.json` — the schema `tools/equation_audit/crop_equation_regions.py` already consumes.

This skill is the missing producer for `crop_equation_regions.py`. That tool has been functional in the repo but had no upstream — the per-page bbox JSONs it expected were never generated. This skill closes that gap: one TASK dispatch per page, normalized coordinates in [0,1], cross-checked against the per-page Markdown's equation list when expected hashes are provided.

#### Suitable agent shells

- `TASK` in generic shell mode, spawned by the `EQUATION_AUDIT` persona during Phase 1 when per-equation crops are enabled.

Not the right fit for:
- per-equation interpretation of human notes (use `equation-flag-interpret`)
- whole-document figure/table bounding-box detection (use `pdf2md-page-assets`)
- inline-equation detection (this skill targets DISPLAY equations only)
- cross-page reasoning (one page per invocation)

#### Inputs

##### Required (via `RuntimeOverrides`)

- `IMAGE_PATH` — absolute path to `page_NNNN.png`
- `PAGE_MD_PATH` — absolute path to the per-page Markdown (provides context: which equations to look for)
- `PAGE_NUM` — 1-indexed page number; must match the `NNNN` in `IMAGE_PATH`
- `OUTPUT_PATH` — absolute path to write `page_NNNN_eq_bboxes.json`

##### Optional

- `EXPECTED_EQUATION_HASHES` — list of 12-hex hashes the persona expects to find on this page (extracted by `audit_equations.py`). The skill cross-checks its findings against this list and notes mismatches in the `latex_excerpt` field.

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `IMAGE_PATH` | Path to page PNG | **Required** | Existing `.png` file |
| `PAGE_MD_PATH` | Path to per-page Markdown | **Required** | Existing `.md` file |
| `PAGE_NUM` | Page number | **Required** | Positive integer |
| `OUTPUT_PATH` | Path to write bbox JSON | **Required** | Parent dir exists; `.json` |
| `EXPECTED_EQUATION_HASHES` | Expected hash cross-check list | `[]` | List of 12-hex strings |

#### Read boundary

Reads are limited to:

- `IMAGE_PATH` — the single page PNG, multimodal load.
- `PAGE_MD_PATH` — the per-page Markdown, text load.

No other reads. The skill MUST NOT:

- read other pages
- read `equations.jsonl` or any audit artifact
- read other source files (skeleton, assets, sidecars)

#### Write boundary

Writes are limited to exactly one file:

- `OUTPUT_PATH` — `page_NNNN_eq_bboxes.json` matching the schema `crop_equation_regions.py` consumes

No other side effects.

#### Tool usage

- No deterministic tools are invoked. This is a VLM-vision skill.
- The `allowed-tools` frontmatter field is intentionally omitted.
- The agent uses its native `Read` tool for multimodal PNG input and text MD input, and its native `Write` tool for the single output JSON.

Disallowed behavior:

- MUST NOT shell out to any subprocess or external command.
- MUST NOT widen scope beyond the assigned page.
- MUST NOT modify the page Markdown or any audit artifact.
- MUST NOT re-OCR text outside display equations (transcription is `pdf2md-page`'s job).
- MUST NOT write any file other than `OUTPUT_PATH`.

#### Method

##### Step 1 — Validate inputs

1. Confirm `IMAGE_PATH` exists and is a `.png` file.
2. Confirm `PAGE_MD_PATH` exists.
3. Confirm `OUTPUT_PATH` parent directory exists.
4. If any required input is invalid, write `{"page": <PAGE_NUM>, "equations": [], "error": "<reason>"}` to `OUTPUT_PATH` and return `RUN_STATUS=FAILED_INPUTS`.

##### Step 2 — Read the page Markdown for expected equation list

1. Use the `Read` tool to load `PAGE_MD_PATH` (text).
2. Scan for `$$...$$` blocks to know which equations the page is expected to contain. This is context for Step 4's cross-check, NOT ground truth for bbox extraction (bbox extraction is vision-only).

##### Step 3 — Load the page raster

1. Use the `Read` tool to load `IMAGE_PATH` (multimodal PNG).

##### Step 4 — Identify display equations on the page

1. Find every block of typeset mathematics that is **set off from the surrounding running prose** — typically:
   - Centered or visually offset from the column body
   - Preceded and followed by paragraph spacing
   - Often labeled with equation numbers (e.g., `(1.5)`, `(2.3a)`) at right margin
2. DO NOT box inline equations (math symbols embedded in running sentences).
3. DO NOT box section headings, table cells, figure labels, or page numbers.
4. For each display equation, determine its tightest enclosing rectangle on the page raster.

##### Step 5 — Normalize coordinates

For each detected display equation:

1. Compute normalized coordinates `[x0, y0, x1, y1]` where:
   - `x0`, `y0` is the top-left corner (image origin convention: `(0,0)` at top-left)
   - `x1`, `y1` is the bottom-right corner
   - All values are floats in `[0.0, 1.0]` relative to the page raster's width × height
2. Order detected equations top-to-bottom on the page; assign 1-based `index`.
3. Capture the first ~20 characters of the visible LaTeX/symbolic content as `latex_excerpt` for cross-check against `EXPECTED_EQUATION_HASHES`. This is a freeform string — DO NOT attempt full LaTeX transcription (that's `pdf2md-page`'s job).

##### Step 6 — Write outputs

Write `OUTPUT_PATH` as a single JSON object matching the consumer's schema:

```json
{
  "page": <PAGE_NUM>,
  "equations": [
    {
      "index": 1,
      "bbox_norm": [0.12, 0.21, 0.85, 0.27],
      "latex_excerpt": "\\frac{2}{\\sqrt{3}} Y ="
    },
    {
      "index": 2,
      "bbox_norm": [0.18, 0.42, 0.78, 0.46],
      "latex_excerpt": "d\\epsilon/\\sigma ="
    }
  ]
}
```

When the page has no display equations:

```json
{"page": <PAGE_NUM>, "equations": []}
```

##### Step 7 — Return status

Return one of:

- `RUN_STATUS=SUCCESS` — at least one display equation detected; bboxes emitted.
- `RUN_STATUS=NO_FINDINGS` — no display equations on this page (empty `equations` list).
- `RUN_STATUS=FAILED_INPUTS` — required inputs were missing or malformed.
- `RUN_STATUS=FAILED` — bbox detection failed for an unexpected reason.

Also return: `PAGE_NUM`, `EQUATION_COUNT`.

#### Non-negotiable constraints

- **Display-equation-only.** Do NOT detect inline math inside running prose.
- **Normalized coordinates.** All bbox values in [0.0, 1.0]. Pixel coordinates are forbidden.
- **Top-to-bottom ordering.** `index` is 1-based and increases top-to-bottom on the page.
- **No transcription.** The skill does not produce LaTeX — `latex_excerpt` is at most a ~20-char hint for cross-check, not authoritative.
- **No cross-page state.** One page per invocation; no carryover.
- **Output-path-only writes.** Exactly one file is written per invocation. No other side effects.

#### QA expectations

- Exactly one file exists at `OUTPUT_PATH` after the run.
- The file is valid JSON; top-level is a single object with `page` (int) and `equations` (list).
- Each `equations[*]` entry has `index` (int ≥ 1), `bbox_norm` (4-tuple of floats in [0,1]).
- `index` is 1-based and strictly increasing.
- No `bbox_norm` overlaps with another `bbox_norm` by more than ~10% area (two display equations should not share a region — overlap is a detection error).
- `x0 < x1` and `y0 < y1` for every box.
- `RUN_STATUS` is one of: `SUCCESS`, `NO_FINDINGS`, `FAILED_INPUTS`, `FAILED`.

#### Relationship to EQUATION_AUDIT

This skill is the per-page worker invoked by the `EQUATION_AUDIT` persona during Phase 1 when per-equation crops are enabled. The persona:

- runs `tools/equation_audit/audit_equations.py` to extract every display equation per page into `equations.jsonl` (text only; no bboxes),
- for each page that has display equations, renders one INIT-TASK brief via `tools/equation_audit/build_equation_bbox_brief.py`, optionally embedding `EXPECTED_EQUATION_HASHES` derived from the JSONL,
- dispatches one `TASK + equation-bbox-detect` invocation per page,
- collects the per-page `page_NNNN_eq_bboxes.json` files into the page work-dir,
- runs `tools/equation_audit/crop_equation_regions.py` to produce per-equation PNG crops under `audit/equations/working/crops/`,
- embeds the crops in the audit HTML for visual review.

This skill is a sibling of `pdf2md-page-assets` (per-page figure/table bbox detection) and `drawing-extract-page` (per-page drawing-element detection) — same per-page VLM fanout pattern, narrowed to display equations.

## Component: skills/equation-bbox-detect/TOOL_POLICY.md

### TOOL POLICY — equation-bbox-detect

#### Preferred tool order

This skill is VLM-vision-reasoning over the page raster, optionally cross-checked against the per-page Markdown's equation list. There is no deterministic tool the worker runs from inside the dispatch. The surrounding pipeline runs deterministic tools (rasterization, equation extraction, brief building, cropping) outside the worker, on the orchestrator side.

#### Allowed deterministic tools

##### TASK-enforced

None. The `allowed-tools` frontmatter field is intentionally omitted from `SKILL.md`. TASK does not whitelist any tool for this skill.

##### Operationally invoked

The agent's native tools are available implicitly:

- `Read` — used to load `IMAGE_PATH` (multimodal PNG input) AND `PAGE_MD_PATH` (text input).
- `Write` — used to write the single `OUTPUT_PATH` JSON file.

No `Bash`, no shell-outs, no subprocess invocations.

#### Surrounding deterministic tools (orchestrator-side, NOT worker-side)

| Tool | Owner | When |
|---|---|---|
| `tools/pdf2md/rasterize_pdf.py` | TOOLMAKER | PDF2MD Phase 1 — produces `page_NNNN.png` |
| `tools/equation_audit/audit_equations.py` | TOOLMAKER | EQUATION_AUDIT Phase 1 — extracts every display equation per page (text) and populates `EXPECTED_EQUATION_HASHES` |
| `tools/equation_audit/build_equation_bbox_brief.py` | TOOLMAKER | EQUATION_AUDIT Phase 1 — produces this skill's brief |
| `tools/equation_audit/crop_equation_regions.py` | TOOLMAKER | EQUATION_AUDIT Phase 1 — consumes this skill's output JSONs and emits per-equation PNG crops |

The worker never invokes any of the above. It writes its single JSON output; the persona feeds it to `crop_equation_regions.py`.

#### Expected use of reasoning

The worker uses VLM/text reasoning to:

1. **Read the page raster.** Use the multimodal `Read` tool to load `IMAGE_PATH`.
2. **Read the per-page Markdown for context.** Use the text `Read` tool to load `PAGE_MD_PATH`. The MD's `$$...$$` blocks indicate which equations to expect on this page.
3. **Identify display equations on the raster.** Distinguish display equations (centered, offset, often with equation numbers) from inline math (embedded in running prose). Display equations get boxed; inline math does NOT.
4. **Determine tight bounding rectangles.** For each display equation, find the smallest axis-aligned rectangle that fully encloses the equation's typeset content (including superscripts, subscripts, integral signs, etc.) but excludes surrounding paragraph text and equation numbers (when those appear in the far-right margin separately).
5. **Normalize coordinates.** Compute `[x0, y0, x1, y1]` as fractions of the page raster's width × height.
6. **Order top-to-bottom.** Assign 1-based `index` in vertical reading order.
7. **Capture a short excerpt.** Read the first ~20 characters of visible math content as `latex_excerpt` — for the persona's cross-check against `EXPECTED_EQUATION_HASHES`. This is a hint, not authoritative transcription.

#### Disallowed use

- No deterministic tool invocation from inside the worker (no `Bash`, no `python3`, no shell-out, no subprocess).
- No writing outside `OUTPUT_PATH`.
- No reading outside `IMAGE_PATH` and `PAGE_MD_PATH`.
- No full transcription of equation content (that's `pdf2md-page`'s job).
- No boxing inline equations or symbols embedded in running prose.
- No boxing section headings, table cells, figure labels, page numbers, or running headers.
- No cross-page reasoning (one TASK = one page).
- No emission of pixel coordinates (normalized [0,1] only).
- No re-OCR of body text.

#### Write boundary

Exactly one write per invocation:

```
<OUTPUT_PATH>
```

The path is absolute. Parent directory must exist; this skill does not create directories.

If a write would violate the boundary, the worker returns `RUN_STATUS=FAILED` with an explanatory note and does NOT attempt a workaround.
