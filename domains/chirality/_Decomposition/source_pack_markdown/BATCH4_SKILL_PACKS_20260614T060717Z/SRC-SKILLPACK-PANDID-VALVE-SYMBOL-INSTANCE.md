# Source Pack: Skill pack: pandid-valve-symbol-instance

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/pandid-valve-symbol-instance/BRIEF_SCHEMA.md

### BRIEF_SCHEMA

Required fields:

- `SOURCE_PDF_NAME`
- `PAGE_NUM`
- `TILE_ID`
- `SOURCE_RASTER_PATH`
- `TILE_IMAGE_PATH`
- `OUTPUT_PATH`
- `MODE`: `basic` or `detailed`
- `TILE_GEOMETRY`: `tile_grid`, `body_box_px`, `body_exclusions`, `read_box_px`, `emit_box_px`, `overlap_px`, `mini_grid`

Optional fields:

- `ALLOW_REFERENCE_SHEETS`
- `SCOPE_FILE`
- `BASIC_REFERENCE_RUN`
- `BASIC_COUNTS_CSV`

The brief must include the canonical output template rendered by `build_pandid_valve_tile_brief.py`.

## Component: skills/pandid-valve-symbol-instance/QA_CHECKS.md

### QA_CHECKS

- Reject text-only observations as rows.
- Confirm every emitted row has integer page-global center and bounding-box coordinates.
- Confirm every counted row has a valve `symbol_class`, `count_include=true`, and `symbol_confidence` of `medium` or `high`.
- Keep tag evidence separate: `visible_tag_text` is only for `tag_status=true_tag`; line/spec text belongs in `nearby_line_text`.
- Treat tag-profile conflicts as review warnings only. They do not delete rows or alter symbol counts.
- Ensure `finding_count` equals the number of emitted rows for `SUCCESS`.

## Component: skills/pandid-valve-symbol-instance/SKILL.md

---
name: pandid-valve-symbol-instance
description: "Extract pixel-anchored P&ID valve symbol instances from prepared tiles using isolated-crop classification before any row may count."
compatibility: "TASK shell"
metadata:
  chirality-skill-version: "1.0.0"
  chirality-task-profile: DRAWING_EXTRACT
---
### pandid-valve-symbol-instance

#### Purpose

Extract visible P&ID valve body symbol instances from one prepared tile. A row may exist only after an isolated symbol crop has been classified as a valve class. Text never produces rows, and tag profiles never delete rows.

#### Protocol

1. Use the tile image only to detect plausible valve glyphs whose page-global center falls inside the emit box.
2. For each plausible glyph, reason from a tight isolated crop that excludes nearby line/spec/tag text as much as practical.
3. Emit one row per crop classified as a valve class. Use `count_include=true` only for valve classes with `symbol_confidence` of `medium` or `high`.
4. Do not emit text-only rows. Nearby line/spec text may populate `nearby_line_text` with `tag_status=line_spec_only` or `ambiguous` only after a valve row exists.
5. Use `visible_tag_text` only for actual valve/control-loop tags and set `tag_status=true_tag`.
6. Return `NO_FINDINGS_REFERENCE` for reference/legend sheets unless explicitly allowed by the brief.

#### Output Contract

The output file is a markdown stub using `valve_schema_version: symbol_instance_v1` and the canonical table columns from `tools/drawing_extract/valve_stub_layout.py`.

Required row evidence:

- page-global `center_x_px`, `center_y_px`
- page-global `bbox_*_px`
- `symbol_crop_path`
- `symbol_class`
- `symbol_confidence`
- `count_include`
- `review_status`
- `review_reason`

Valid valve classes are `manual_block`, `manual_throttle`, `check`, `control`, `esd_block`, `relief`, and `specialty_valve`.

## Component: skills/pandid-valve-symbol-instance/TOOL_POLICY.md

### TOOL_POLICY

Preferred deterministic tools:

- `tools/drawing_extract/build_pandid_valve_tile_brief.py`
- `tools/drawing_extract/validate_valve_tile_stub_format.py`
- `tools/drawing_extract/assemble_valve_candidates_csv.py`
- `tools/drawing_extract/assign_valve_symbol_geometry_duplicates.py`
- `tools/drawing_extract/aggregate_valve_counts.py`
- `tools/drawing_extract/flag_duplicate_valve_candidates.py`

Disallowed:

- Inferring a counted valve row from text patterns alone.
- Mutating raw candidate CSVs to encode later human review decisions.
- Auto-migrating legacy `pandid-valve-tile` stubs into `symbol_instance_v1`.
