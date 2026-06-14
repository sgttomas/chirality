# Source Pack: Skill pack: pandid-valve-tile

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/pandid-valve-tile/BRIEF_SCHEMA.md

### pandid-valve-tile - Brief Schema

Use this skill with TASK, dispatched by `DRAWING_EXTRACT` for one P&ID tile.

#### Required fields

| Field | Requirement |
|---|---|
| `TaskSkill` | `pandid-valve-tile` |
| `AllowedWriteTargets` | Exactly `[RuntimeOverrides.OUTPUT_PATH]` |
| `RuntimeOverrides.SOURCE_PDF_NAME` | Source PDF basename |
| `RuntimeOverrides.PAGE_NUM` | Positive integer |
| `RuntimeOverrides.TILE_ID` | `page_NNNN_rRRcCC` |
| `RuntimeOverrides.TILE_IMAGE_PATH` | Existing tile PNG |
| `RuntimeOverrides.OUTPUT_PATH` | Target `.md` path |
| `RuntimeOverrides.MODE` | `basic` or `detailed` |
| `RuntimeOverrides.TILE_GEOMETRY` | Geometry metadata from `tile_manifest.json` |

#### Optional fields

| Field | Meaning |
|---|---|
| `RuntimeOverrides.ALLOW_REFERENCE_SHEETS` | When true, do not self-skip reference sheets |
| `RuntimeOverrides.SCOPE_FILE` | Optional operator-selected page scope provenance |
| `RuntimeOverrides.BASIC_REFERENCE_RUN` | Optional detailed-mode provenance |
| `RuntimeOverrides.BASIC_COUNTS_CSV` | Optional detailed-mode provenance |

#### Recommended CustomInstructions

- Use the whole tile image for context.
- Emit rows only for valve symbols whose visual center is inside the solid emit-zone border.
- Candidates visible outside the emit zone belong in notes only.
- Use the 5x5 grid overlay for `approx_location_in_emit_box`.
- Do not emit pixel coordinates.
- `issue_flags` is a list; empty is `[]`.
- Unknown/unreadable classification fields are `TBD`.
- If the tile is from a legend/reference/symbol sheet and `ALLOW_REFERENCE_SHEETS` is false, return `NO_FINDINGS_REFERENCE`.

#### Brief example

```md
PURPOSE: Extract P&ID valve candidates from page 8 tile r02_c03
RequestedBy: DRAWING_EXTRACT
ActingSurface: TASK+pandid-valve-tile

ScopePath: /abs/path/to/work
TaskSkill: pandid-valve-tile

AllowedWriteTargets:
  - "/abs/path/to/source/P_AND_ID/valve_count_basic/RUN-.../stem_page_0008_tile_r02_c03_basic_stub.md"

RuntimeOverrides:
  SOURCE_PDF_NAME: MFS.pdf
  PAGE_NUM: 8
  TILE_ID: page_0008_r02_c03
  TILE_IMAGE_PATH: /abs/path/to/work/page_0008_tile_r02_c03.png
  OUTPUT_PATH: /abs/path/to/source/P_AND_ID/valve_count_basic/RUN-.../stem_page_0008_tile_r02_c03_basic_stub.md
  MODE: basic
  TILE_GEOMETRY:
    tile_grid: 5x4
    body_box_px: [100, 100, 6400, 4100]
    body_exclusions: [border, titleblock]
    read_box_px: [2300, 1000, 3900, 2300]
    emit_box_px: [2500, 1200, 3700, 2100]
    overlap_px: 200
    mini_grid: 5x5

ExpectedOutputs:
  - /abs/path/to/source/P_AND_ID/valve_count_basic/RUN-.../stem_page_0008_tile_r02_c03_basic_stub.md
```

## Component: skills/pandid-valve-tile/QA_CHECKS.md

### pandid-valve-tile - QA Checks

#### Minimum checks

1. `TILE_IMAGE_PATH` exists.
2. `OUTPUT_PATH` has a `.md` extension and parent directory exists.
3. `MODE` is `basic` or `detailed`.
4. `TILE_GEOMETRY` includes body, read, and emit boxes.
5. Exactly one output file is written.
6. Frontmatter matches runtime parameters.
7. `finding_count` equals emitted row count.
8. `approx_location_in_emit_box` is one of `A1..E5`.
9. `issue_flags` serializes as `[]` or `[FLAG_A, FLAG_B]`.
10. Basic mode does not emit detailed columns.
11. Detailed mode includes `valve_size_text`, `valve_type_code`, `valve_type_name`, and `actuation`.

#### Reference-sheet handling

Reference, legend, symbol, and abbreviation pages return `NO_FINDINGS_REFERENCE` with `finding_count: 0` unless `ALLOW_REFERENCE_SHEETS=true`.

#### Failure posture

- Invalid runtime inputs produce `FAILED_INPUTS`.
- Unreadable tile content produces `FAILED`.
- No valve candidates in the emit zone produces `NO_FINDINGS`.
- Unknown issue flags are warnings for deterministic validators, not page-worker failures.

## Component: skills/pandid-valve-tile/SKILL.md

---
name: pandid-valve-tile
description: OBSOLETE legacy per-tile P&ID valve candidate extraction retained for historical readability; new runs use pandid-valve-symbol-instance.
compatibility: Historical only; not dispatched by DRAWING_EXTRACT for new P_AND_ID valve_count_basic or valve_count_detailed runs
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL - pandid-valve-tile

OBSOLETE: This legacy skill is retained only to read historical stubs. New P&ID valve runs must dispatch `pandid-valve-symbol-instance` and must not auto-migrate legacy rows into `symbol_instance_v1`.

#### Purpose

Extract valve candidate rows from one P&ID tile image. The tile contains a larger read zone and a smaller emit zone drawn by deterministic preprocessing. The skill may use the read zone for context, but it emits rows only for valve symbols whose visual center lies inside the emit zone.

This skill supports two modes:

- `basic` - count-oriented candidate rows with coarse valve category, visible tag, location bucket, and issue flags.
- `detailed` - basic columns plus valve size, valve type, and actuation where visible.

#### Suitable agent shells

- `TASK` in generic shell mode, spawned by the `DRAWING_EXTRACT` orchestrator.

#### Inputs

##### Required

- `RuntimeOverrides.SOURCE_PDF_NAME`
- `RuntimeOverrides.PAGE_NUM`
- `RuntimeOverrides.TILE_ID`
- `RuntimeOverrides.TILE_IMAGE_PATH`
- `RuntimeOverrides.OUTPUT_PATH`
- `RuntimeOverrides.MODE` - `basic` or `detailed`
- `RuntimeOverrides.TILE_GEOMETRY` - `tile_grid`, `body_box_px`, `body_exclusions`, `read_box_px`, `emit_box_px`, `overlap_px`, `mini_grid`

##### Optional

- `RuntimeOverrides.ALLOW_REFERENCE_SHEETS` - default `false`.
- `RuntimeOverrides.SCOPE_FILE` - optional operator-selected page scope provenance.
- `RuntimeOverrides.BASIC_REFERENCE_RUN` - optional detailed-pass provenance for the basic run used for reconciliation.
- `RuntimeOverrides.BASIC_COUNTS_CSV` - optional detailed-pass provenance for the basic counts CSV used for reconciliation.

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `MODE` | Extraction mode | Required | `basic`, `detailed` |
| `TILE_IMAGE_PATH` | Tile image with emit-zone overlay | Required | Existing image path |
| `TILE_ID` | Page/tile identifier | Required | `page_NNNN_rRRcCC` |
| `TILE_GEOMETRY` | Tile geometry metadata | Required | See plan schema |
| `ALLOW_REFERENCE_SHEETS` | Process legend/reference tiles | `false` | Boolean |

#### Tool usage

No deterministic tools are invoked by this skill. Tile preparation, validation, assembly, aggregation, duplicate flagging, and reconciliation belong to deterministic tools invoked by the orchestrator.

#### Method

1. Validate runtime inputs.
2. Read `TILE_IMAGE_PATH`.
3. If the tile clearly belongs to a legend, symbols, abbreviation, or reference sheet and `ALLOW_REFERENCE_SHEETS` is not true, emit `NO_FINDINGS_REFERENCE` with `reason=legend_or_reference_sheet`.
4. Inspect the read zone for context.
5. Emit only valve candidates whose visual center is inside the outlined emit zone.
6. Use the 5x5 overlay to set `approx_location_in_emit_box` (`A1` through `E5`).
7. In `detailed` mode, fill size/type/actuation fields only when visible. Otherwise emit `TBD`.
8. Write exactly one markdown stub at `OUTPUT_PATH`.

#### Controlled values

`valve_category`:

- `manual_block`
- `manual_throttle`
- `check`
- `control`
- `esd_block`
- `relief`
- `unknown`

`tag_basis`:

- `visible_near_symbol`
- `inferred_from_designation`
- `TBD`

`issue_flags` initial vocabulary:

- `BOUNDARY_REVIEW`
- `LOW_LEGIBILITY`
- `AMBIGUOUS_SYMBOL`
- `CLASSIFICATION_UNCERTAIN`
- `SIZE_NOT_LEGIBLE`
- `LINE_NUMBER_NOT_LEGIBLE`

Unknown future flags may be emitted, but validators will record warnings.

#### Output format

Every output stub begins with YAML frontmatter matching the runtime geometry. Body columns:

Basic:

```text
valve_index | valve_category | valve_tag | tag_basis | approx_location_in_emit_box | issue_flags | notes
```

Detailed adds:

```text
valve_size_text | valve_type_code | valve_type_name | actuation
```

`issue_flags` is serialized as `[FLAG_A, FLAG_B]`; empty is `[]`.

#### Run statuses

- `SUCCESS` - one or more candidates emitted.
- `NO_FINDINGS` - no valve candidates in the emit zone.
- `NO_FINDINGS_REFERENCE` - reference/legend page detected and not overridden.
- `FAILED` - tile could not be interpreted.
- `FAILED_INPUTS` - missing or invalid runtime inputs.

#### Non-negotiable constraints

- One invocation handles one tile.
- The emit-zone rule is mandatory.
- Visible-but-outside candidates are not emitted as rows.
- Pixel coordinates are not requested or used.
- `approx_location_in_emit_box` must be one of `A1..E5`.
- Tags are extracted when visible but are never required.
- Unknown values are `TBD`.
- The skill writes only `OUTPUT_PATH`.

#### QA expectations

- Frontmatter geometry matches the run.
- `finding_count` equals the number of emitted body rows.
- `NO_FINDINGS` and `NO_FINDINGS_REFERENCE` have `finding_count: 0`.
- Basic mode does not emit detailed columns.
- Detailed mode includes detailed columns.
- Every emitted candidate has a non-empty `valve_index`, `valve_category`, `approx_location_in_emit_box`, and `issue_flags`.

## Component: skills/pandid-valve-tile/TOOL_POLICY.md

### pandid-valve-tile - Tool Policy

#### Preferred tool order

Reasoning-first. Deterministic tile preparation happens before dispatch. The skill reads one prepared tile image and writes one stub.

#### Allowed deterministic tools

##### TASK-enforced

- None. The skill has no `allowed-tools` frontmatter.

##### Operationally invoked

- None. All deterministic operations are orchestrator/tool responsibilities.

#### Expected use of reasoning

Use visual reasoning over the tile image to identify valve candidates, respect the emit-zone contract, and classify candidate fields according to the active mode.

#### Disallowed use

- No shell commands.
- No web access.
- No deterministic OCR invocation.
- No reading images outside the declared tile input.
- No writing outside `OUTPUT_PATH`.
- No sub-agent fanout.

#### Write boundary

The skill writes exactly one file: `RuntimeOverrides.OUTPUT_PATH`.
