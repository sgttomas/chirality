# Plan - Extend P&ID Tile Workflows to Line Numbers and Instrument Tags

## Context

The new P&ID valve-count workflow introduces a reusable page-tiling strategy for dense P&ID drawings:

- a body box defining the drawing region in scope
- non-overlapping emit boxes that exactly tile the body box
- larger read boxes that provide overlap/context
- a visual emit-zone border and 5x5 mini-grid
- per-tile VLM dispatch
- deterministic schema validation, assembly, aggregation, and review reports

That geometry is useful beyond valves. Line numbers and instrumentation tags are also spatially distributed across the P&ID body, need local visual context, and can suffer from double-counting when overlapping crops are used. The tile contract should therefore become a shared P&ID extraction substrate, while each extraction target keeps its own schema, identity model, QA rules, and assembly outputs.

## Recommendation

Add line-number and instrumentation-tag workflows as sibling P&ID targets, not as extra columns inside valve extraction.

New targets:

- `(P_AND_ID, line_number_index)`
- `(P_AND_ID, instrument_tag_index)`

Keep these separate from:

- `(P_AND_ID, valve_count_basic)`
- `(P_AND_ID, valve_count_detailed)`

Reasoning:

- The tile geometry is reusable, but the rows mean different things.
- A repeated line number may be legitimate across many locations; a repeated instrument tag is often a stronger review signal.
- Forcing valves, line numbers, and instruments into one prompt would increase cognitive load and likely increase invented associations.
- Cross-target relationships may be useful later, but this plan intentionally avoids valve-to-line-number association.

## Shared P&ID Tile Substrate

The following pieces should remain shared across P&ID targets:

- `tools/drawing_extract/prepare_pandid_tiles.py`
- `tools/drawing_extract/validate_tile_partition.py`
- tile manifest schema
- read-zone / emit-zone rule
- 5x5 mini-grid location buckets
- resume tuple fields:
  - `source_pdf`
  - `source_page`
  - `tile_id`
  - `tile_grid`
  - `body_box_px`
  - `body_exclusions`
  - `read_box_px`
  - `emit_box_px`
  - `overlap_px`
  - `mini_grid`
  - `mode` or `target`

Default geometry remains:

- `tile_grid=5x4`
- `overlap_px=200`
- `body_exclusions=border,titleblock`
- `mini_grid=5x5`

The same tile set can be reused for multiple P&ID targets in a run when the geometry tuple matches exactly.

## Target 1 - `(P_AND_ID, line_number_index)`

### Purpose

Extract visible line-number labels and line-number occurrences from P&ID tiles.

This is an index, not a deduplicated line list. The same line number may appear multiple times on the same page or across pages.

### Candidate Row Schema

Recommended columns:

- `line_index`
- `line_number`
- `line_size_text`
- `service_text`
- `spec_or_class_text`
- `insulation_or_tracing_text`
- `from_context`
- `to_context`
- `approx_location_in_emit_box`
- `issue_flags`
- `notes`

Controlled values:

- `issue_flags`: list, initially:
  - `LOW_LEGIBILITY`
  - `PARTIAL_LINE_NUMBER`
  - `BOUNDARY_REVIEW`
  - `AMBIGUOUS_ASSOCIATION`
  - `DUPLICATE_OCCURRENCE_REVIEW`

### Identity and Dedupe

Do not dedupe line numbers by default.

Repeated `line_number` values should produce an occurrence report, not a duplicate-error report. A high occurrence count can be useful because line labels repeat along a process line and across continuations.

Recommended QA output:

- `line_number_occurrence_report.csv`
  - `line_number`
  - `occurrence_count`
  - `pages`
  - `tile_ids`
  - `review_reason`

### Skill Behavior

The worker should emit a row only when the visible line-number text or its leader/line-label visual center is inside the emit box. It may use the read zone to understand context, but visible line numbers centered outside the emit box go in notes only.

Do not infer missing parts of a line number unless the visible designation convention makes the inference explicit; otherwise emit `TBD` for uncertain fields. Do not associate line numbers to valves in this workflow.

## Target 2 - `(P_AND_ID, instrument_tag_index)`

### Purpose

Extract visible instrument tags, instrument bubbles, control valve instrument tags, and instrumentation callouts from P&ID tiles.

This is an instrument occurrence index. It can later support loop-register creation, but should not require complete loop reconciliation in the first pass.

### Candidate Row Schema

Recommended columns:

- `instrument_index`
- `instrument_tag`
- `tag_basis`
- `instrument_type_prefix`
- `loop_number`
- `suffix`
- `instrument_symbol_type`
- `signal_or_connection_type`
- `associated_equipment_or_valve`
- `approx_location_in_emit_box`
- `issue_flags`
- `notes`

Controlled values:

- `tag_basis`: `visible_inside_symbol | visible_near_symbol | inferred_from_callout | TBD`
- `instrument_symbol_type`: `bubble | shared_bubble | control_valve_callout | analyzer | local_indicator | panel_indicator | unknown`
- `signal_or_connection_type`: `pneumatic | electrical | hydraulic | software | capillary | process_connection | unknown | TBD`
- `issue_flags`: list, initially:
  - `LOW_LEGIBILITY`
  - `PARTIAL_TAG`
  - `BOUNDARY_REVIEW`
  - `AMBIGUOUS_SYMBOL`
  - `AMBIGUOUS_ASSOCIATION`
  - `DUPLICATE_TAG_REVIEW`

### Identity and Dedupe

For instrumentation, repeated non-empty `instrument_tag` values are stronger review candidates than repeated line numbers, but still should not be automatically collapsed.

Recommended QA output:

- `flag_duplicate_instrument_tags.py`
  - flags repeated non-empty instrument tags
  - preserves all rows
  - classifies as review evidence, not an error

### Skill Behavior

The worker should emit one row per visible instrument tag/symbol whose visual center is inside the emit box.

For multi-bubble clusters, emit one row per tag if each tag is readable. If a cluster is visible but unreadable, emit one row with `instrument_tag=TBD` and an appropriate issue flag rather than inventing tags.

Associated lines, equipment, and valves are best-effort fields only. Unknown associations should remain `TBD`.

## Cross-Target QA, Deferred Until Individual Targets Work

Once valves and instruments can each be extracted independently, add deterministic cross-target review tools. Keep line-number extraction independent unless a later workflow is specifically designed and validated for line association.

Useful QA checks:

- control valves should often have a nearby instrument tag
- instruments should often have an associated line, valve, or equipment context
- line-number occurrences should cluster along connected process paths
- instrument tags repeated across pages may indicate continuation, repeated detail, or duplicate extraction
- valves with `valve_category=control` but no nearby instrument candidate should be reviewed
- instrument tags with no associated line/equipment/valve should be reviewed

Recommended deferred tool:

- `crosscheck_pandid_registers.py`

Inputs:

- valve candidates CSV
- instrument-tag candidates CSV
- tile manifest

Outputs:

- `pandid_cross_target_review.csv`
- `pandid_cross_target_summary.md`

Important constraint: cross-target QA should flag possible issues; it should not rewrite or auto-merge candidate rows.

## Files to Modify

### `agents/AGENT_DRAWING_EXTRACT.md`

Add the two new targets to the registry and target dispatch table:

- `(P_AND_ID, line_number_index)`
- `(P_AND_ID, instrument_tag_index)`

Document that both reuse the P&ID tile substrate and produce occurrence indexes rather than authoritative registers.

### `tools/REGISTRY.md`

Register the new tools listed below under the P&ID drawing extraction section.

## Files to Create

### New Skills

- `skills/pandid-line-number-tile/`
  - `SKILL.md`
  - `BRIEF_SCHEMA.md`
  - `TOOL_POLICY.md`
  - `QA_CHECKS.md`

- `skills/pandid-instrument-tag-tile/`
  - `SKILL.md`
  - `BRIEF_SCHEMA.md`
  - `TOOL_POLICY.md`
  - `QA_CHECKS.md`

### New Deterministic Tools

Line-number target:

- `tools/drawing_extract/line_number_stub_layout.py`
- `tools/drawing_extract/build_pandid_line_number_tile_brief.py`
- `tools/drawing_extract/validate_line_number_tile_stub_format.py`
- `tools/drawing_extract/validate_line_number_tile_resume_metadata.py`
- `tools/drawing_extract/assemble_line_number_candidates_csv.py`
- `tools/drawing_extract/report_line_number_occurrences.py`

Instrumentation target:

- `tools/drawing_extract/instrument_tag_stub_layout.py`
- `tools/drawing_extract/build_pandid_instrument_tag_tile_brief.py`
- `tools/drawing_extract/validate_instrument_tag_tile_stub_format.py`
- `tools/drawing_extract/validate_instrument_tag_tile_resume_metadata.py`
- `tools/drawing_extract/assemble_instrument_tag_candidates_csv.py`
- `tools/drawing_extract/flag_duplicate_instrument_tags.py`

Deferred cross-target QA:

- `tools/drawing_extract/crosscheck_pandid_registers.py`

## Workflow

### Line Numbers

1. Run sheet inventory if scope is unknown.
2. Use an operator-selected P&ID scope file or explicit page range.
3. Rasterize pages.
4. Run `prepare_pandid_tiles.py` with the standard 5x4 geometry.
5. Dispatch `pandid-line-number-tile` workers per tile.
6. Validate tile stubs.
7. Assemble line-number candidates.
8. Emit occurrence report.

### Instrumentation Tags

1. Use the same P&ID scope and tile geometry.
2. Dispatch `pandid-instrument-tag-tile` workers per tile.
3. Validate tile stubs.
4. Assemble instrument-tag candidates.
5. Emit duplicate-tag review report.

### Combined Optional Run

If valves, line numbers, and instruments are all needed for the same pages, prepare the tile set once and run all three target workflows against the same `tile_manifest.json`.

## Validation

Minimum deterministic validation:

- `prepare_pandid_tiles.py` creates exactly 20 tiles per page by default.
- `validate_tile_partition.py` exits 0.
- resume validators reject changed tile geometry.
- line-number and instrument-tag stub validators enforce:
  - valid status
  - valid body columns
  - `finding_count` equals parsed row count for `SUCCESS`
  - `approx_location_in_emit_box` is `A1..E5`
  - `issue_flags` round-trip as a list
- assemblers preserve:
  - `source_page`
  - `tile_id`
  - `dwg_no`
  - `system_name`
  - target-specific candidate columns

Manual spot checks:

- select two dense P&ID pages
- inspect all 20 tiles for one page
- verify no adjacent tiles both emit the same centered symbol/tag/label
- hand-check a few repeated line numbers and instrument tags against source imagery

## Open Questions

1. Should line-number extraction emit only labels, or also unlabeled visible pipe segments? Initial recommendation: labels only.
2. Should instrument tags include valve tags such as `XV` and `FV`, or should those stay valve-only? Initial recommendation: include instrument/control tags when they appear as instrument designations, but keep valve physical counting in the valve target.
3. Should line and instrument targets be run before detailed valve extraction to provide context? Initial recommendation: no hard dependency. Use them later for QA enrichment once individual targets are reliable.
4. Should there be one shared `pandid-symbol-tile` skill with modes? Initial recommendation: no. Keep separate skills until prompts and schemas stabilize.

## Implementation Order

1. Add `line_number_index` end to end.
2. Run it on 2 to 3 representative P&ID pages.
3. Adjust schema and prompt based on review.
4. Add `instrument_tag_index` end to end.
5. Run it on the same 2 to 3 pages.
6. Only after both are stable, consider `crosscheck_pandid_registers.py`.
