# DRAWING_EXTRACT P&ID Valve Symbol-Instance Rewrite Plan

Status: Proposed

Date: 2026-04-28

Owner: DRAWING_EXTRACT / pandid-valve repertoire

Supersedes for future implementation: P&ID valve-count portions of `plans/DRAWING_EXTRACT_P_AND_ID_VALVE_COUNT_PLAN.md`

Does not supersede: DRAWING_SET/titleblock_index scope inventory workflow

## 1. Problem Statement

The current `P_AND_ID/valve_count_basic` workflow asks a single tile-level VLM pass to identify valve candidates, classify them, and extract nearby tags. In practice, that combined task permits a failure mode where the VLM treats nearby text as object evidence. Examples observed in the West Doe MFS run include line/spec/service text such as `27GA-A`, `60BA-S`, and `21GA-A` entering the `valve_tag` field. Some of those rows correspond to real visible valve symbols with bad tag text; others are false positives caused by text, instrumentation, reducers, off-page connectors, or other non-valve features being interpreted as valves.

Because the current row schema combines object identity, countability, and tag evidence, deterministic cleanup cannot reliably distinguish:

- real valve symbols with unreliable tag text,
- duplicate observations of the same visible symbol due to overlap,
- repeated line/spec labels adjacent to distinct real valves,
- non-valve graphics or text hallucinated as valve candidates.

The result is that page-level counts and duplicate-tag review can diverge sharply between two plausible runs. This is unacceptable for database compilation without full manual validation.

## 2. Design Goal

Redesign the P&ID valve workflow around pixel-anchored visible symbol instances.

The basic pass must answer one primary question:

> Is there a visible valve body symbol at this location?

Tag extraction, size/type enrichment, and actuation details are secondary metadata operations performed only after a visible symbol instance exists.

## 3. Key Design Principles

1. Symbol first, text second.
   A row cannot exist because text looks valve-like. A row exists only when there is a pixel-anchored candidate symbol.

2. Countability is separate from tag quality.
   A valve with no visible true tag can still count. A row with bad line/spec text in the tag area must not be silently deleted from quantity.

3. Tags are metadata, not row identity.
   Duplicate-tag review must operate on fields explicitly classified as `true_tag`, with tag-profile conflicts surfaced as review issues. A deterministic tag pattern must never decide whether a visible valve symbol exists or counts.

4. Geometry owns dedupe.
   Tile overlap duplicates are resolved by symbol center/bounding-box proximity, not by repeated text.

5. Human calibration gates production scale.
   Representative pages must be ground-truthed before the workflow is allowed to run across a full drawing set.

6. Review artifacts must be crop-first.
   A reviewer should inspect the exact crop used for a candidate row, not re-walk a full-size drawing for every CSV line.

7. Tiling survives as image preparation, not as counting authority.
   The existing 5x4 / 200px overlap model remains useful for manageable context and raster slicing, but tile membership must not define object uniqueness.

## 4. Scope

In scope:

- `P_AND_ID/valve_count_basic`
- `P_AND_ID/valve_count_detailed`
- `pandid-valve-tile` replacement or major revision
- valve stub schema and deterministic assembly/aggregation/duplicate tools
- review and calibration artifacts for P&ID valve extraction

Out of scope:

- DRAWING_SET/titleblock_index inventory and `scope_proposal.md`
- PFD equipment extraction
- drawing-titleblock-page skill
- generic PDF2MD conversion
- DBM publication workflows

## 5. Proposed Pipeline

Pipeline order: Stage A scope inventory -> Stage B raster/geometry prep -> Stage C candidate detection -> Stage D isolated-crop classification -> Stage E tag association -> Stage F geometric deduplication -> assembly/aggregation -> Stage G/G.5 calibration -> Stage H review-first outputs.

A row may exist only when an isolated symbol crop has been classified as a valve class. Text never produces rows; tag profiles never delete rows.

### Stage A — Scope Inventory

Keep the existing `DRAWING_SET/titleblock_index` workflow unchanged.

Outputs:

- titleblock inventory CSV/MD,
- `scope_proposal.md`,
- operator-selected P&ID page scope.

### Stage B — Page Rasterization and Geometry Prep

Keep deterministic PDF rasterization.

Keep P&ID tiling initially, but redefine its role:

- tiles provide bounded image context,
- emit/read boxes provide deterministic crop boundaries,
- tile rows do not define final object identity,
- final candidate ownership is based on pixel-centered symbol geometry.

The existing `prepare_pandid_tiles.py` can remain for the first implementation slice. A later slice may add full-page symbol pre-detection and direct crop generation that no longer depends on 5x4 tiles.

### Stage C — Symbol Candidate Detection

Create pixel-anchored symbol candidate rows.

The initial implementation may use VLM-assisted detection inside prepared tiles, but detection alone is not sufficient evidence for counting. A detector may propose candidate center/bounding-box geometry from a tile, but that candidate must be confirmed by a separate classification step on an isolated symbol crop before it can become `count_include=true`.

Detection output requirements:

- page-global pixel center,
- page-global bounding box,
- source tile id,
- source tile image path,
- symbol crop path or enough geometry to generate one,
- detector confidence if available.

Text alone is invalid. The detector should pre-filter obvious text-only observations and emit no candidate row. If the detector cannot determine whether the observation is text-only, it may emit a candidate with `count_include=false`, `review_status=manual_review`, and `review_reason=text_only_possible`; Stage D then confirms or rejects it from the isolated crop. This keeps telemetry focused on plausible symbol candidates while still preserving uncertain evidence.

Detection proposes candidates; classification decides countability. Stage C emits candidates with `count_include=false` and `review_status=manual_review` by default. Only Stage D classification on an isolated symbol crop may set `count_include=true`, and only when `symbol_class` is one of the valve classes with `symbol_confidence` at or above the configured floor.

Classical pre-detection remains optional. Add template/shape matching for bowties, check symbols, relief symbols, control valve bodies, and actuated valve symbols only after the schema, crop review artifacts, and calibration metrics exist.

### Stage D — Symbol Classification

Classify each detected symbol candidate independently from tag naming.

This is a mandatory second step, not a later optimization. The classifier must operate on a tight symbol crop that excludes surrounding line/spec/tag text as much as practical. The purpose is to mechanically prevent the original failure mode: inferring a valve from adjacent text instead of from a visible valve glyph.

The classifier may use a batch contact sheet of numbered isolated crops for cost control, but the prompt must answer per numbered crop and must not see broad drawing context during this classification step.

Valid `symbol_class` values:

- `manual_block`
- `manual_throttle`
- `check`
- `control`
- `esd_block`
- `relief`
- `specialty_valve`
- `instrument_only`
- `not_a_valve`
- `unknown`

Only the valve classes count by default.

`instrument_only`, `not_a_valve`, and `unknown` require either exclusion or manual review depending on confidence and operator policy.

Minimum classification output:

- `candidate_id`,
- `symbol_class`,
- `symbol_confidence`,
- `count_include`,
- `review_status`,
- `review_reason`.

Default countability floor: `symbol_confidence=medium`. A candidate classified below the active confidence floor must remain `count_include=false` with `review_status=manual_review` unless a human later accepts it.

### Stage E — Tag Association

For confirmed or probable valves only, associate nearby text.

The tag association contract must distinguish:

- actual valve/control-loop tag,
- line/spec/service text,
- equipment reference,
- off-page connector text,
- unreadable text,
- no tag visible.

The pipeline should not put probable line/spec text into the canonical true-tag field. Because project conventions vary, deterministic tools must treat tag-pattern conflicts as row-level review signals, not as grounds to delete a row or fail a visible-symbol count.

`nearby_line_text` is free text captured from the drawing context. It is not a controlled vocabulary and must not be enum-validated.

Recommended fields:

- `visible_tag_text`
- `tag_status`
- `nearby_line_text`
- `tag_confidence`

`tag_status` controlled values:

- `true_tag`
- `line_spec_only`
- `equipment_or_connector_text`
- `ambiguous`
- `none`
- `unreadable`

`tag_confidence` uses the same vocabulary as `symbol_confidence`: `high`, `medium`, `low`, `TBD`.

Tag profile rules are configurable, but Slice 1 must ship with a default true-tag grammar and line/spec heuristic profile.

Default true-tag grammar:

```text
^[A-Z]{1,6}-\d{2,5}(?:-\d{1,3})?$
```

This covers common examples such as `FCV-7211-1`, `PSV-5715-1`, `PSV-7250`, `SOV-7510-1`, `ESDV-3210-1`, `HV-1015-1`, `XV-5710-1`, `TCV-5725-1`, `LCV-7285-1`, `PCV-7510-1`, and `BDV-...` when present. Project-specific overrides may broaden or narrow this grammar, and the validator must always record which grammar/profile version was used.

Probable line/spec patterns such as numeric size + service/material class (`27GA-A`, `60BA-S`, `21CH-A`, `168BA-A`, `273ST-A`, `27x21NE-S`, etc.) should normally be assigned to `nearby_line_text` with `tag_status=line_spec_only` or `tag_status=ambiguous`, not to `visible_tag_text`.

Default line/spec heuristic examples for review warnings only:

```text
^\d+(?:x\d+)?(?:BA|GA|GL|CH|NE|ST)(?:-[A-Z])?(?:\s+\S+)?$
^\d+x\d+$
^\d+(?:BA|GA|GL|CH|NE|ST)-[A-Z]\s+\d{2}[A-Z]{1,3}(?:-[A-Z])?$
```

If a row has `tag_status=true_tag` and `visible_tag_text` fails the active true-tag grammar or matches the active line/spec heuristic profile, the validator must emit a row-level `TAG_PROFILE_REVIEW` warning. It must not drop the row, change the count, or fail the entire run solely for that tag-profile conflict.

These examples are not a universal denylist. They are seed heuristics for the observed drawing family and must remain operator-configurable per project.

### Stage F — Geometric Deduplication

Collapse duplicate observations only by geometry.

Tile ownership is deterministic:

1. The owning tile is the tile whose emit box contains the candidate's page-global center.
2. If a candidate center falls exactly on an emit-box boundary or inside a tolerance band, assign the owner by nearest emit-box center.
3. Candidate observations of the same geometric cluster from non-owning tiles are marked `superseded_duplicate` before final aggregation.

Two observations are duplicate candidates when:

- same source page,
- valve body centers are within a configured pixel tolerance, or bounding boxes overlap above a configured threshold,
- symbol class is compatible,
- crop evidence points to the same visible symbol.

Default geometry thresholds:

- center-distance tolerance: `20px` in page-global raster coordinates,
- bbox-overlap threshold: `0.50` IoU,
- both values are operator-configurable per run and must be recorded in run metadata.

`symbol_class` compatibility means either:

- the two rows have the same `symbol_class`, or
- one row has `symbol_class=unknown`.

Repeated text alone must not merge rows.

Cross-page duplicate tags must remain operator review items. They may represent legitimate continuation references, repeated control-loop details, or real duplicate tags.

### Stage G — Calibration Gate

Before production full-set extraction, select representative pages:

- one sparse page,
- one medium-density page,
- one dense page,
- optionally one known-problem page with repeated line/spec labels,
- optionally one known-problem page with dense instrumentation.

The operator supplies calibration pages explicitly via `--pages` or a run config file. Calibration tooling does not auto-select representative pages.

For each calibration page:

1. Run the candidate pipeline.
2. Emit review artifacts with crop images.
3. Human reviewer marks each candidate:
   - `accept`,
   - `reject`,
   - `manual_review`,
   - `missed_symbol` rows if applicable.
4. Compute precision, recall, and F1 against the human ground truth.
5. Do not scale until thresholds are met or explicitly waived.

Suggested initial production threshold:

- recall >= 0.95,
- precision >= 0.70,
- no systematic class of missed symbols,
- no systematic text-only false-positive class unresolved.

For calibration reporting, a systematic missed-symbol class is any `symbol_class` with recall below `0.85` across the calibration set, or any repeated visual pattern that produces two or more false negatives on the reviewed calibration pages.

Rationale: false positives are comparatively cheap for a reviewer to reject from crop evidence; false negatives force a human to rediscover missed valves on full drawings.

The operator may override thresholds for exploratory runs, but outputs must be labeled non-production.

### Stage G.5 — Calibration Failure Loop

If calibration fails:

1. Classify failures by type:
   - false-positive class,
   - missed-symbol class,
   - duplicate-geometry failure,
   - tag-association failure,
   - review-artifact usability failure.
2. Select a remediation:
   - detector prompt change,
   - isolated-crop classifier prompt change,
   - crop geometry change,
   - validator/schema change,
   - tag profile change,
   - escalation to classical detector prototype.
3. Re-run the same calibration pages.
4. Append the iteration to `calibration_log.md` with inputs, changes, metrics, and decision.
5. After three failed iterations, stop and require design review before scale-out.

After the third failed iteration, the calibration metrics tool exits non-zero and writes `STATUS: ESCALATE` as the final entry in `calibration_log.md`. The orchestrator must refuse production scale-out while `STATUS: ESCALATE` is the latest calibration status.

### Stage H — Review-First Outputs

Every candidate row must carry direct visual evidence:

- source page,
- source raster path,
- tile/crop path,
- symbol crop path if available,
- pixel center,
- bounding box,
- model classification,
- tag association result,
- review status.

`dwg_no` and `system_name` should be joined by `source_page` from the accepted titleblock inventory CSV or operator-selected scope file when available; otherwise they remain `TBD`.

Reviewer artifacts:

- CSV for spreadsheet review,
- Markdown contact sheet with embedded candidate crops,
- per-page summary with accepted/rejected/manual-review counts,
- optional calibration metrics report.

Review round trip:

- raw candidate CSVs are immutable extraction evidence,
- the human-edited review CSV is the source of truth for accepted/rejected/manual-review status after review,
- downstream aggregation must either read the reviewed CSV directly or consume a deterministic import tool that writes reviewed candidate outputs,
- raw candidate files must not be edited in place to encode human review decisions.

## 6. Proposed Schema

### 6.1 Symbol Candidate Row

Recommended unified candidate columns:

```text
candidate_id
source_page
dwg_no
system_name
source_raster_path
tile_id
tile_image_path
symbol_crop_path
context_crop_path
center_x_px
center_y_px
bbox_x0_px
bbox_y0_px
bbox_x1_px
bbox_y1_px
symbol_class
symbol_confidence
count_include
review_status
review_reason
visible_tag_text
tag_status
tag_confidence
nearby_line_text
valve_size_text
valve_type_code
valve_type_name
actuation
detail_confidence
issue_flags
notes
```

Detailed/enrichment columns are nullable from day one. Basic runs emit them as blank or `TBD`; detailed runs populate them where visible. This avoids a later validator/assembler schema rewrite when detailed enrichment is implemented.

`candidate_id` must be deterministic for resume safety. Default rule:

```text
sha1("{source_page}|{center_x_px}|{center_y_px}|{symbol_class}")[:12]
```

If bbox coordinates are materially more stable for a detector implementation, the implementation may include bbox values in the hash, but the rule must be recorded in run metadata.

### 6.2 Controlled Values

`symbol_confidence`:

- `high`
- `medium`
- `low`
- `TBD`

`count_include`:

- `true`
- `false`

`review_status`:

- `auto_accept`
- `manual_review`
- `human_accept`
- `human_reject`
- `superseded_duplicate`

`review_reason` examples:

- `visible_valve_symbol`
- `low_confidence_symbol`
- `ambiguous_symbol`
- `instrument_only`
- `text_only_false_positive`
- `text_only_possible`
- `geometry_duplicate`
- `tag_unreliable`
- `boundary_review`
- `manual_operator_decision`

`issue_flags` initial vocabulary:

- `BOUNDARY_REVIEW`
- `LOW_LEGIBILITY`
- `AMBIGUOUS_SYMBOL`
- `TAG_UNRELIABLE`
- `TAG_PROFILE_REVIEW`
- `LINE_SPEC_TEXT_ONLY`
- `POSSIBLE_INSTRUMENT_ONLY`
- `GEOMETRY_DUPLICATE_REVIEW`
- `CLASSIFICATION_UNCERTAIN`
- `SIZE_NOT_LEGIBLE`
- `ACTUATION_NOT_LEGIBLE`

### 6.3 Counting Rule

The per-page accepted count is:

```text
count rows where count_include=true
and review_status in {auto_accept, human_accept, manual_review}
minus rows where review_status=superseded_duplicate
```

For production-ready accepted counts, `manual_review` rows should be reported separately and either resolved by a human or explicitly included by operator policy.

Recommended per-page count fields:

```text
page
drawing
accepted_count
accepted_plus_manual_review_count
auto_accept_count
human_accept_count
manual_review_count
human_reject_count
superseded_duplicate_count
tagless_count
line_spec_only_tag_count
ambiguous_tag_count
by_symbol_class_counts_json
issue_flag_counts_json
reference_reason
```

## 7. Impacted Files

### 7.1 Agent Instruction

Rewrite P&ID valve portions:

- `agents/AGENT_DRAWING_EXTRACT.md`

Required changes:

- update target dispatch table,
- redefine `valve_count_basic` as symbol-instance extraction,
- redefine `valve_count_detailed` as enrichment of accepted/probable symbol instances,
- add calibration gate,
- add review artifact outputs,
- update Phase 3 assembly/aggregation language,
- update SPEC and STRUCTURE sections,
- update tool dependency table,
- preserve titleblock inventory flow.

### 7.2 Skill Contracts

Preferred transition path:

1. Retire or freeze current `skills/pandid-valve-tile/` as legacy.
2. Add narrower P&ID valve skills.

Recommended new skills:

- `skills/pandid-valve-symbol-instance/`
- `skills/pandid-valve-tag-context/`

Each new skill directory must include:

- `SKILL.md`
- `BRIEF_SCHEMA.md`
- `QA_CHECKS.md`
- `TOOL_POLICY.md`

Disposition for `skills/pandid-valve-tile/`:

- keep the directory in place for historical readability,
- add an `OBSOLETE` marker in its `SKILL.md` frontmatter/body during implementation,
- do not dispatch it from `AGENT_DRAWING_EXTRACT.md` for new symbol-instance runs,
- do not move or delete it in Slice 1 unless the operator explicitly asks for archive cleanup.

An in-place rewrite of `skills/pandid-valve-tile/` was considered and rejected for the initial implementation because it would make legacy and symbol-instance stubs too easy to confuse.

- Use new skill names to avoid silently treating legacy stubs as valid.

### 7.3 Deterministic Tooling

Rewrite or replace:

- `tools/drawing_extract/valve_stub_layout.py`
- `tools/drawing_extract/build_pandid_valve_tile_brief.py`
- `tools/drawing_extract/validate_valve_tile_stub_format.py`
- `tools/drawing_extract/assemble_valve_candidates_csv.py`
- `tools/drawing_extract/aggregate_valve_counts.py`
- `tools/drawing_extract/flag_duplicate_valve_candidates.py`

Likely update:

- `tools/drawing_extract/validate_valve_tile_resume_metadata.py`
- `tools/drawing_extract/reconcile_basic_vs_detailed.py`
- `tools/REGISTRY.md`

Keep initially:

- `tools/drawing_extract/prepare_pandid_tiles.py`
- `tools/drawing_extract/validate_tile_partition.py`

New tools recommended:

- `tools/drawing_extract/assign_valve_symbol_geometry_duplicates.py`
- `tools/drawing_extract/generate_valve_review_artifacts.py`
- `tools/drawing_extract/import_reviewed_valve_candidates.py`
- `tools/drawing_extract/compute_valve_calibration_metrics.py`
- `tools/drawing_extract/create_valve_ground_truth_template.py`

`import_reviewed_valve_candidates.py` reads a human-edited review CSV and emits accepted/rejected/manual-review split CSVs, or a normalized reviewed candidate CSV, for downstream aggregation without mutating raw candidate outputs.

Optional later tools:

- `tools/drawing_extract/detect_valve_symbol_candidates.py`
- `tools/drawing_extract/generate_valve_symbol_crops.py`
- `tools/drawing_extract/generate_valve_tag_context_crops.py`

### 7.4 Plans and Indexes

Update after implementation:

- `AGENTS.md`
- `tools/REGISTRY.md`
- `plans/DRAWING_EXTRACT_P_AND_ID_VALVE_COUNT_PLAN.md` with a supersession note, or leave it historical and cross-reference this plan.
- `plans/DRAWING_EXTRACT_P_AND_ID_LINE_AND_INSTRUMENT_INDEX_PLAN.md` only if it shares tag/status vocabulary.

No expected change:

- `INIT.md`
- `agents/AGENT_HELPS_HUMANS.md`
- `skills/drawing-titleblock-page/*`
- `skills/drawing-extract-page/*`
- PFD equipment tools
- titleblock tools

## 8. Implementation Strategy

### Slice 1 — Schema and Skill Rewrite

Deliverables:

- new or rewritten valve symbol-instance schema,
- new skill contract for symbol-instance extraction,
- mandatory isolated-crop classification contract,
- new brief builders for candidate detection and isolated-crop classification,
- updated validator,
- minimal assembler,
- sample stub round-trip test.

Acceptance:

- validator rejects rows without pixel location,
- validator rejects `count_include=true` rows with `symbol_class in {instrument_only, not_a_valve}`,
- validator allows tagless visible valves,
- validator distinguishes `visible_tag_text` from `nearby_line_text`,
- validator emits row-level `TAG_PROFILE_REVIEW` warnings, without changing counts, when `tag_status=true_tag` conflicts with the active tag profile,
- classifier crop contract excludes surrounding line/spec/tag text as much as practical,
- brief explicitly forbids text-only rows.

### Slice 2 — Aggregation and Duplicate Geometry

Deliverables:

- assembler emits symbol-instance candidate CSV/MD,
- aggregator counts only `count_include=true`,
- duplicate tool flags or supersedes geometry duplicates,
- duplicate-tag tool only considers `tag_status=true_tag`,
- cross-page true-tag review CSV is emitted by the rewritten duplicate-tag review tool, considering only rows with `tag_status=true_tag` and surfacing tag-profile conflicts separately.

Acceptance:

- repeated line/spec text does not create duplicate-tag rows,
- repeated line/spec text is counted in tag-quality metrics,
- same symbol observed in adjacent tiles can be identified by geometry,
- page counts include accepted/manual-review/rejected/superseded categories.

### Slice 3 — Review Artifacts

Deliverables:

- per-page candidate review CSV,
- Markdown review sheet with crop links,
- human-editable reviewed CSV convention and deterministic import/aggregation path,
- operator instructions in agent protocol.

Acceptance:

- every candidate row links to visual evidence,
- reviewer can accept/reject without opening full page unless needed,
- aggregation can consume reviewed statuses without mutating raw candidate files.

### Slice 4 — Calibration Gate

Deliverables:

- ground truth template tool,
- calibration metrics tool,
- `CALIBRATION_REQUIRED` or equivalent status in run report,
- orchestrator protocol requiring calibration before production-scale extraction unless explicitly waived.

Acceptance:

- metrics include precision, recall, F1, false positives by reason, false negatives by symbol class,
- failed calibration iterations are recorded in `calibration_log.md`,
- full-scope run is labeled production-ready only after thresholds pass or waiver is recorded.

### Slice 5 — Optional Classical Detector

Deliverables:

- prototype shape/template detector,
- candidate crop generator,
- comparison against VLM-only detection on calibration pages.

Acceptance:

- detector improves recall on calibration pages by at least 5 percentage points without dropping precision below the active threshold, or materially reduces review effort with no loss in recall,
- no mandatory adoption unless it beats VLM-only workflow.

## 9. Migration and Backward Compatibility

Legacy valve stubs should not be silently accepted as symbol-instance stubs.

Required:

- add schema version frontmatter, e.g. `valve_schema_version: symbol_instance_v1`,
- include `valve_schema_version` in per-stub frontmatter and assembled-output frontmatter/metadata,
- validator rejects missing or legacy schema version for new runs,
- assemblers refuse to mix legacy and new schema rows in one output,
- `_LATEST.md` should identify schema version.

Legacy runs remain historical evidence only. They may be used for comparison, but not as production-ready symbol-instance outputs.

Auto-migration is forbidden. Legacy stubs lack pixel-anchored symbol evidence and must not be mechanically converted into symbol-instance stubs or ingested by new-schema assemblers under any best-effort conversion path.

## 10. Detailed vs Basic Reinterpretation

Do not drop staged operation entirely.

Recommended terminology:

- `valve_count_basic`: symbol-instance count and coarse class only.
- `valve_count_detailed`: enrichment of accepted or probable symbol instances with size/type/actuation and tag context.

Detailed extraction should consume a basic candidate CSV or accepted review CSV, not re-detect all valves from scratch unless explicitly requested.

This preserves the operator workflow:

1. run inventory,
2. run basic count,
3. review/calibrate,
4. only then run detailed enrichment.

## 11. QA and Acceptance Criteria

A production-ready implementation must satisfy:

1. Titleblock inventory still runs unchanged.
2. P&ID basic emits symbol-instance rows with pixel evidence.
3. Text-only rows are never counted; they are omitted or carried as `count_include=false` review evidence.
4. Aggregation reports accepted/manual-review/rejected/superseded counts separately.
5. Duplicate-tag review excludes `line_spec_only`, `ambiguous`, `none`, and `unreadable` tags.
6. Geometry duplicate review exists and does not depend on tag text.
7. Calibration pages can be ground-truthed and scored.
8. Full-run outputs identify calibration status.
9. Legacy stubs are not accepted by new assemblers and are never auto-migrated.
10. The operator can inspect candidate crops without re-walking the whole PDF.
11. Rows with `tag_status=true_tag` whose `visible_tag_text` conflicts with the active tag profile are surfaced with `TAG_PROFILE_REVIEW`; this affects tag authority/review status, not symbol count.

## 12. Testing Plan

Add focused tests for:

- `valve_stub_layout.py` parse/render round trip,
- invalid text-only candidate rejection,
- tag profile warnings for true-tag grammar mismatch and probable line/spec text,
- aggregation with `count_include=false`,
- aggregation with `manual_review`,
- duplicate geometry matching,
- duplicate true-tag review,
- repeated line/spec text not treated as duplicate valve tags,
- schema-version mismatch rejection,
- reviewed status import if implemented.
- a real-valve fixture adjacent to confounding line/spec-like text, asserting `count_include=true`, `tag_status=line_spec_only` or `ambiguous`, and no authoritative true-tag value unless the active project profile supports it.

Fixture strategy:

- create small synthetic stubs rather than relying on large PDF assets,
- include at least one fixture with repeated `nearby_line_text`,
- include at least one fixture with a real valve glyph adjacent to a confounding line/spec-like label,
- include at least one fixture with true duplicate tag,
- include at least one fixture with same symbol observed by adjacent tiles.

## 13. Operator Policy Decisions

1. Should the first implementation use new skill names or rewrite `pandid-valve-tile` in place?

   Decision: use new skill names to avoid legacy ambiguity.

2. What is the human acceptance threshold for production use?

   Decision: default recall >= 0.95 and precision >= 0.70. Operator may override by explicit waiver for exploratory/non-production runs.

3. Should `manual_review` rows count in preliminary totals?

   Decision: report both `accepted_count` and `accepted_plus_manual_review_count`; do not hide uncertainty.

## 14. Fixed Design Decisions

These are no longer open questions for Slice 1.

1. Coordinate frame:

   Page-global pixel coordinates are authoritative. Tile-local coordinates may be stored as debug fields only.

2. Tag profile:

   Slice 1 ships a configurable default true-tag grammar plus a default line/spec heuristic profile. The validator records the active profile version and emits row-level `TAG_PROFILE_REVIEW` warnings for conflicts. The profile is a review aid, not an authority that can suppress a visible-symbol count.

3. Classification separation:

   Candidate detection and symbol classification are separate steps. Classification must use isolated symbol crops or numbered crop contact sheets, not broad context tiles containing surrounding text.

4. Production scale-out:

   No production full-set extraction may be run until calibration tooling exists and calibration has passed or been explicitly waived.

## 15. Cost and Performance Considerations

The new workflow intentionally spends more work per candidate to reduce missed valves and text-driven false positives. Implementation must make the cost visible before scale-out.

Expected call patterns:

- Legacy tile pass: roughly one VLM call per tile, e.g. 20 calls/page for a 5x4 grid.
- Symbol-instance pass, unbatched: detection calls per tile plus classification calls per candidate plus optional tag-context calls per accepted candidate.
- Symbol-instance pass, batched: detection calls per tile plus numbered crop contact sheets for classification and tag-context batches.

Cost controls:

- batch isolated symbol crops into numbered contact sheets where practical,
- run tag-context only for confirmed/probable valves,
- run detailed enrichment only after basic review/calibration,
- require operator approval before full-scope scale-out when projected call count or cost exceeds the operator's threshold,
- include projected and actual call counts in run reports.

The first implementation should prefer correctness and reviewability over minimizing calls. Cost optimization must not reintroduce broad-context classification where surrounding text can drive the valve decision.

## 16. Telemetry and Production Monitoring

Every calibration or production run should emit per-page telemetry so model drift and drawing-style mismatch are visible early.

Recommended telemetry fields:

```text
page
drawing
candidate_count
auto_accept_count
manual_review_count
human_reject_count
superseded_duplicate_count
vlm_calls_count
vlm_calls_by_stage_json
auto_accept_rate
manual_review_rate
text_only_rejection_rate
tagless_valve_rate
line_spec_only_tag_rate
mean_symbol_confidence
calibration_status
```

Telemetry should be written as CSV under the immutable run folder alongside other run artifacts and summarized in the run report. A production run with unusually high manual-review, text-only rejection, or tagless rates should be flagged for operator review before database import.

## 17. Future Instance Implementation Prompt

Use the prompt below to start implementation from this plan. Do not paste the full plan into the prompt; the file path is sufficient.

```text
Read INIT.md, AGENTS.md, agents/AGENT_HELPS_HUMANS.md, agents/AGENT_DRAWING_EXTRACT.md, and plans/DRAWING_EXTRACT_P_AND_ID_SYMBOL_INSTANCE_REWRITE_PLAN.md.

Implement the plan incrementally, starting with Slice 1 and Slice 2 only. Preserve the existing DRAWING_SET/titleblock_index and PFD equipment workflows. Do not rewrite unrelated files.

Goal for this pass: introduce the P_AND_ID valve symbol-instance schema and basic deterministic tooling so a basic run can emit pixel-anchored visible-symbol rows, validate them, assemble candidates, aggregate count_include=true rows, and avoid treating line/spec text as duplicate valve tags.

Do not run production extraction in this pass. The calibration gate must be implemented and exercised in a later pass before any full drawing set is processed with the new tooling.

Subsequent passes implement Slice 3 review artifacts, then Slice 4 calibration gate including ground-truth template, calibration metrics, and calibration_log.md. Production extraction is permitted only after Slice 4 has passed calibration on representative pages or an operator waiver has been recorded.

After edits, run the relevant unit/fixture tests or add focused tests if none exist. Report changed files, commands run, and any deferred slices.
```
