# Source Pack: Skill pack: drawing-titleblock-page

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/drawing-titleblock-page/BRIEF_SCHEMA.md

### drawing-titleblock-page - Brief Schema

Use this skill with the TASK shell, dispatched by `DRAWING_EXTRACT` for one page of `DRAWING_SET/titleblock_index`.

#### Required fields

| Field | Requirement |
|---|---|
| `TaskSkill` | `drawing-titleblock-page` |
| `AllowedWriteTargets` | Exactly `[RuntimeOverrides.OUTPUT_PATH]` |
| `RuntimeOverrides.SOURCE_PDF_NAME` | Source PDF basename |
| `RuntimeOverrides.PAGE_NUM` | Positive integer |
| `RuntimeOverrides.TOTAL_PAGES` | Positive integer |
| `RuntimeOverrides.CORNER_CROP_PATHS` | Mapping with `tl`, `tr`, `bl`, `br` image paths |
| `RuntimeOverrides.THUMBNAIL_PATH` | Full-page thumbnail image path |
| `RuntimeOverrides.OUTPUT_PATH` | Target `.md` path |
| `RuntimeOverrides.CORNER_CROP_GEOMETRY` | Mapping with `width_ratio`, `height_ratio` |

#### Brief example

```md
PURPOSE: Extract drawing sheet titleblock metadata from page 8 of 94
RequestedBy: DRAWING_EXTRACT
ActingSurface: TASK+drawing-titleblock-page

ScopePath: /abs/path/to/work
TaskSkill: drawing-titleblock-page

AllowedWriteTargets:
  - "/abs/path/to/source/DRAWING_SET/titleblock_index/RUN-.../stem_page_0008_titleblock_stub.md"

RuntimeOverrides:
  SOURCE_PDF_NAME: MFS-242510_(3-25_Doe)_rA_IFI_(Permit_Application).pdf
  PAGE_NUM: 8
  TOTAL_PAGES: 94
  CORNER_CROP_PATHS:
    tl: /abs/path/to/work/page_0008_titleblock_tl.png
    tr: /abs/path/to/work/page_0008_titleblock_tr.png
    bl: /abs/path/to/work/page_0008_titleblock_bl.png
    br: /abs/path/to/work/page_0008_titleblock_br.png
  THUMBNAIL_PATH: /abs/path/to/work/page_0008_thumbnail.png
  OUTPUT_PATH: /abs/path/to/source/DRAWING_SET/titleblock_index/RUN-.../stem_page_0008_titleblock_stub.md
  CORNER_CROP_GEOMETRY:
    width_ratio: 0.25
    height_ratio: 0.25

ExpectedOutputs:
  - /abs/path/to/source/DRAWING_SET/titleblock_index/RUN-.../stem_page_0008_titleblock_stub.md
```

#### Recommended CustomInstructions

- Use the full-page thumbnail only to orient the sheet and identify whether a titleblock exists.
- Read all four corner crops before deciding the titleblock corner.
- `drawing_family_proposal` is a proposal, not final operator scope.
- Unknown fields are `TBD`; do not infer from page order.
- `confidence` must be `high`, `medium`, or `low`.
- `NO_TITLEBLOCK` is valid and must use `finding_count: 0`.

## Component: skills/drawing-titleblock-page/QA_CHECKS.md

### drawing-titleblock-page - QA Checks

#### Minimum checks

1. All four corner crop paths exist.
2. The thumbnail path exists.
3. `OUTPUT_PATH` has a `.md` extension and its parent exists.
4. Exactly one output file is written.
5. Frontmatter contains `drawing_type: DRAWING_SET` and `extraction_target: titleblock_index`.
6. `status` is one of `SUCCESS`, `NO_TITLEBLOCK`, `FAILED`, `FAILED_INPUTS`.
7. `finding_count` is `1` for `SUCCESS` and `0` for `NO_TITLEBLOCK`.
8. Body table columns match the canonical schema.
9. `confidence` is `high`, `medium`, or `low` when a row is emitted.

#### Failure posture

- Invalid inputs produce `FAILED_INPUTS` and a failure stub.
- A readable page without a titleblock produces `NO_TITLEBLOCK`, not `FAILED`.
- Unreadable fields are `TBD`.

## Component: skills/drawing-titleblock-page/SKILL.md

---
name: drawing-titleblock-page
description: Per-page titleblock extraction from drawing sheets using four corner crops and a full-page thumbnail; emits a governed sheet-inventory stub.
compatibility: Chirality TASK; dispatched by DRAWING_EXTRACT for DRAWING_SET/titleblock_index
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL - drawing-titleblock-page

#### Purpose

Extract titleblock metadata from one drawing page for the `DRAWING_SET/titleblock_index` workflow. This is a bounded per-page visual extraction skill. It does not inventory a full PDF, choose downstream page scope, or accept drawing-family classifications.

The output is a single markdown stub with YAML frontmatter and a one-row findings table.

#### Suitable agent shells

- `TASK` in generic shell mode, spawned by the `DRAWING_EXTRACT` orchestrator.

#### Inputs

##### Required

- `RuntimeOverrides.SOURCE_PDF_NAME` - source PDF basename.
- `RuntimeOverrides.PAGE_NUM` - 1-indexed page number.
- `RuntimeOverrides.TOTAL_PAGES` - total pages in the PDF.
- `RuntimeOverrides.CORNER_CROP_PATHS` - paths for `tl`, `tr`, `bl`, and `br` titleblock crops.
- `RuntimeOverrides.THUMBNAIL_PATH` - low-resolution full-page thumbnail.
- `RuntimeOverrides.OUTPUT_PATH` - path for the output markdown stub.
- `RuntimeOverrides.CORNER_CROP_GEOMETRY` - `width_ratio` and `height_ratio` used for the crops.

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `SOURCE_PDF_NAME` | PDF basename for provenance | Required | String |
| `PAGE_NUM` | Page number | Required | Positive integer |
| `TOTAL_PAGES` | Total pages | Required | Positive integer |
| `CORNER_CROP_PATHS` | Four corner crop paths keyed by `tl,tr,bl,br` | Required | Existing image paths |
| `THUMBNAIL_PATH` | Full-page thumbnail path | Required | Existing image path |
| `OUTPUT_PATH` | Stub output path | Required | `.md` file path |
| `CORNER_CROP_GEOMETRY` | Crop ratios | Required | `width_ratio`, `height_ratio` |

#### Tool usage

No deterministic tools are invoked by this skill. The parent orchestrator prepares crops, validates stubs, and assembles the index.

#### Method

1. Validate that all required image paths and `OUTPUT_PATH` are present.
2. Read the full-page thumbnail to understand page orientation and whether a titleblock is present.
3. Read all four corner crops and identify the titleblock corner.
4. Extract visible metadata:
   - `dwg_no`
   - `sheet_no`
   - `sheet_title`
   - `revision`
   - `area_or_module`
   - `drawing_family_proposal`
   - `titleblock_corner`
   - `confidence`
5. If no titleblock is visible, emit `NO_TITLEBLOCK` with `finding_count: 0`.
6. Write exactly one markdown stub at `OUTPUT_PATH`.

#### Drawing-family proposal

`drawing_family_proposal` is not authoritative. It is a proposal for the human to review during scope acceptance. Use one of:

- `PFD`
- `P_AND_ID`
- `ISOMETRIC`
- `GA`
- `OTHER`
- `REFERENCE_OR_LEGEND`
- `TBD`

#### No-invention rule

Unreadable fields are `TBD`. Do not infer a drawing number or sheet number from surrounding page order. Do not convert a proposal into final operator scope.

#### Output format

Every stub begins with YAML frontmatter:

```yaml
---
drawing_type: DRAWING_SET
extraction_target: titleblock_index
source_pdf: <SOURCE_PDF_NAME>
source_page: <PAGE_NUM>
corner_crop_geometry:
  width_ratio: 0.25
  height_ratio: 0.25
status: SUCCESS | NO_TITLEBLOCK | FAILED | FAILED_INPUTS
finding_count: 0 | 1
---
```

The body table columns are:

```text
dwg_no | sheet_no | sheet_title | revision | area_or_module | drawing_family_proposal | titleblock_corner | confidence
```

`confidence` is `high`, `medium`, or `low`.

#### Outputs

- Exactly one markdown stub at `OUTPUT_PATH`.
- Structured return values: `RUN_STATUS`, `PAGE_NUM`, `DWG_NO`, `DRAWING_FAMILY_PROPOSAL`, `CONFIDENCE`.

#### Non-negotiable constraints

- One invocation handles one page.
- The skill reads only declared crop and thumbnail images.
- The skill writes only `OUTPUT_PATH`.
- `drawing_family_proposal` is always a proposal.
- Unknown or unreadable fields are `TBD`.
- `NO_TITLEBLOCK` is a valid non-error outcome.

#### QA expectations

- Output file exists at `OUTPUT_PATH`.
- Frontmatter matches the run parameters.
- `finding_count=1` only when the body row contains a detected titleblock.
- `finding_count=0` for `NO_TITLEBLOCK`.
- `confidence` is one of `high`, `medium`, `low`.
- Table columns match the canonical schema.

## Component: skills/drawing-titleblock-page/TOOL_POLICY.md

### drawing-titleblock-page - Tool Policy

#### Preferred tool order

Reasoning-first. The orchestrator prepares deterministic crops before dispatch. The skill reads only the provided images and writes one stub.

#### Allowed deterministic tools

##### TASK-enforced

- None. The skill has no `allowed-tools` frontmatter.

##### Operationally invoked

- None. Crop preparation, validation, and assembly are orchestrator responsibilities.

#### Expected use of reasoning

Use visual reasoning over the four corner crops and the full-page thumbnail to identify a titleblock and extract visible metadata. Leave unreadable values as `TBD`.

#### Disallowed use

- No shell commands.
- No web access.
- No deterministic OCR invocation.
- No reading images outside the declared runtime overrides.
- No writing outside `OUTPUT_PATH`.

#### Write boundary

The skill writes exactly one file: `RuntimeOverrides.OUTPUT_PATH`.
