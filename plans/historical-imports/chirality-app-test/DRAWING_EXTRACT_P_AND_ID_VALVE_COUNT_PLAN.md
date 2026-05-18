# DRAWING_EXTRACT — P&ID Valve Count Extension Plan

**Status:** Draft for implementation
**Owner agent (design):** HELPS_HUMANS
**Implementing agents:** SKILLMAKER (skills), TOOLMAKER (tools), HELPS_HUMANS (agent instruction edits)
**Subordinate to:** `agents/AGENT_HELPS_HUMANS.md`, `agents/AGENT_DRAWING_EXTRACT.md` § Extension point

---

## 1. Context

DRAWING_EXTRACT today implements one drawing type (`PFD`) with two equipment-header extraction targets. `P_AND_ID`, `ISOMETRIC`, and `GA` are registered in `agents/AGENT_DRAWING_EXTRACT.md` as `stubbed (fail-fast)`. This plan adds the first non-PFD drawing type — `P_AND_ID` — implemented for **valve counting and classification**, plus a cross-cutting **sheet-inventory pass** that runs first so an operator can identify which pages of a mixed-deliverable PDF are P&IDs before dispatching the valve workflow.

The representative source is `domain-test/domains/West_Doe_Comp_and_Liquids_DBM/_Sources/MFS-242510_(3-25_Doe)_rA_IFI_(Permit_Application).pdf` — 94 pages, 11×17 landscape, ~6800×4400 px at 400 DPI, mixed deliverable (cover + PFDs + P&IDs + isometrics + GAs + lists). The P&ID candidates are pages in the 1X00, 2X00, and 7X00 series (~11–22, 67–72); their titleblocks fail the existing `tools/drawing_extract/extract_pdf_titleblock_text.py` regex extractor, confirming the need for VLM-driven titleblock extraction.

Intended outcome: an operator runs three governed passes against any new mixed-deliverable PDF —
1. **Sheet inventory** across the whole PDF, with a **human-accepted P&ID scope**.
2. **`valve_count_basic`** against the accepted scope; per-page totals accepted by a human.
3. **`valve_count_detailed`** against the same scope, **reconciled** against the accepted basic counts.

Architecture must follow the core-vs-repertoire split documented in `agents/AGENT_DRAWING_EXTRACT.md` § Extension point so future drawing types (ISOMETRIC, GA) plug in without core rewrites.

## 2. Scope of this work

**In scope (this plan):**
- Two new skills under `skills/` (`drawing-titleblock-page`, `pandid-valve-tile`).
- Roughly fifteen new deterministic tools under `tools/drawing_extract/` (enumerated in §10).
- Edits to `agents/AGENT_DRAWING_EXTRACT.md` (target registry, Phase 0 logic, target hook registry, acceptance gates, runtime parameters, dispatch table).
- Edits to `tools/REGISTRY.md` (append).
- A scope clarifier added to `skills/drawing-extract-page/SKILL.md` (PFD-equipment-only; new workflows live in their own skills).

**Out of scope (deferred to follow-on slice if ever):**
- A single-command CLI orchestrator. DRAWING_EXTRACT remains an agent-instruction contract dispatched by a persona/operator, not an executable. A `plan_drawing_extract_run.py` planner (which prints the resolved tool chain for a target) may be added later if dispatch confusion surfaces, but is not in this plan.
- ISOMETRIC and GA implementations — they remain `stubbed (fail-fast)` after this slice.
- Migration of existing PFD code paths into shared abstractions. PFD tools are explicitly NOT modified except for the SKILL.md scope clarifier.

## 3. Aligned Architectural Decisions

These decisions are settled through prior design discussion and govern everything in §6–§10. They are listed here as a single normative reference; downstream sections cite them by number.

### D1 — Three new targets in DRAWING_EXTRACT
- `(DRAWING_SET, titleblock_index)` — pre-extraction sheet inventory. `DRAWING_SET` is a new pseudo-drawing-type for cross-cutting whole-PDF passes (not type-specific extraction).
- `(P_AND_ID, valve_count_basic)` — per-tile valve candidate emission with category + tag + flags; no size/type/actuation classification.
- `(P_AND_ID, valve_count_detailed)` — per-tile valve candidate emission with full classification. Reconciled against an accepted basic pass over an accepted sheet scope.

### D2 — Two new skills, separate from `drawing-extract-page`
- `drawing-titleblock-page` — bounded reasoning over a single page's titleblock crops; emits sheet metadata.
- `pandid-valve-tile` — bounded reasoning over a single P&ID tile under the emit-zone contract. Used by both basic and detailed targets via a `mode` runtime override.
- `drawing-extract-page` stays PFD-equipment-scoped, untouched in body. A scope clarifier is added at the top of its `SKILL.md`.

### D3 — Counts are deterministic aggregations from candidate rows
Both basic and detailed pass emit candidate rows; per-page totals are computed by `aggregate_valve_counts.py`, never by the VLM. Per-page deltas between basic and detailed are QC signals, not VLM-reported numbers.

### D4 — Tile contract: body box → emit boxes → read boxes (load-bearing)
- The crop tool defines a **body box** = the page region in scope.
- **Default body-box exclusion is conservative: border + titleblock only.** Notes-column exclusion is opt-in per drawing set, because P&ID notes columns and inset details can contain valve symbols and aggressive exclusion will undercount.
- The body box is partitioned into M×N **emit boxes** that exactly tile the body box: `union(emit_boxes) == body_box`, `pairwise_overlap(emit_boxes) == 0`. Proven numerically by `validate_tile_partition.py`.
- Each tile's **read box** = its emit box expanded by `overlap_px` on each interior side, clipped to the page (or body box). Edge tiles' read boxes simply clip; emit boxes never shrink.
- Workers may use the full read zone for context. Workers may emit a row only when the valve symbol's visual center is **inside the emit box**. Candidates visible in the read zone but centered outside the emit box are mentioned in `notes` only.
- Per-page total = Σ per-tile rows by construction. The emit-zone rule is the primary double-count control.
- **Cross-tile duplicate-tag QA is a flag, not a verdict.** Duplicate non-empty `valve_tag` across tiles may indicate (a) a tile-boundary double count (geometry bug), (b) a legitimate inset/detail/continuation, (c) a reference callout, or (d) a repeated control-loop detail. The QA tool surfaces duplicates for human review without classifying cause.
- The crop tool draws a deterministic overlay on each tile image: a solid border around the emit box and a faint **5×5 mini-grid** (columns A–E, rows 1–5) inside the emit box for coarse location reference.

### D5 — Default tile geometry: 5 columns × 4 rows = 20 tiles per page
Documented baseline and **minimum** for production valve counts on D-size P&IDs. Reducing below 5×4 requires explicit human acceptance documented in the run's acceptance file. 6×4 or 6×5 may be used when QA flags persist after rerun. Default `overlap_px = 200` at 400 DPI (≈0.5").

### D6 — Tag handling
Extract `valve_tag` when visible, never required. `tag_basis ∈ {visible_near_symbol, inferred_from_designation, TBD}`. Tags support audit and dedupe; they never gate counting.

### D7 — Coarse location buckets, not VLM pixel coordinates
Each emit zone has the deterministic 5×5 mini-grid overlay. The VLM emits `approx_location_in_emit_box ∈ {A1..E5}`. Pixel coordinates are not requested and not used for dedupe.

### D8 — `issue_flags` is a list with controlled vocabulary + warning-tolerant
- Per-row `issue_flags` is a list. A candidate can carry multiple flags simultaneously without lossy reporting.
- **Initial controlled vocabulary** (defined in `valve_stub_layout.py`):
  - Basic mode: `BOUNDARY_REVIEW`, `LOW_LEGIBILITY`, `AMBIGUOUS_SYMBOL`.
  - Detailed mode adds: `CLASSIFICATION_UNCERTAIN`, `SIZE_NOT_LEGIBLE`, `LINE_NUMBER_NOT_LEGIBLE`.
- **Unknown future flags accepted with a WARNING, not a validation error.** The validator records unknown flags in `flag_warnings.csv` so the operator can review and decide whether to formalize them in the next plan revision. Silent pass-through is forbidden.

### D9 — Tool dispatch discipline
The orchestrator (DRAWING_EXTRACT) is the only caller that resolves which Python tool to invoke. Operators specify `(DRAWING_TYPE, EXTRACTION_TARGET)`; the orchestrator's **target → tool-chain dispatch table** in `agents/AGENT_DRAWING_EXTRACT.md` resolves the chain. Tool names stay boring and target-specific (no `assemble_csv.py`, no `validate.py`).

### D10 — Schema layout files
Do not parameterize `tools/drawing_extract/normalize_equipment_stub_layout.py`. Add `valve_stub_layout.py` and `titleblock_stub_layout.py` as standalone schema modules. Extract a shared `stub_layout.py` only if duplication actually emerges during implementation — do not pre-build.

### D11 — `drawing_family_proposal` is non-authoritative
The titleblock-index pass labels each page with `drawing_family_proposal ∈ {PFD, P_AND_ID, ISOMETRIC, GA, OTHER, REFERENCE_OR_LEGEND, TBD}`. The operator accepts the inventory and decides scope.

### D12 — Two acceptance contracts; agents write templates, humans accept
See §5 for the full authority model. Two acceptance gates exist: **scope acceptance** (after sheet inventory) and **count acceptance** (after the basic valve pass). Detailed Phase 0 requires both.

### D13 — Reference/legend pages: pre-filter, don't error
- **Primary control:** the orchestrator pre-filters dispatch using `ACCEPTED_SCOPE.md`. Pages not in the accepted P&ID scope are not dispatched.
- **Defense in depth:** if a tile dispatch reaches a reference/legend page anyway (e.g., operator forced an out-of-scope page via `--pages`), the `pandid-valve-tile` skill returns `RUN_STATUS=NO_FINDINGS_REFERENCE` (a non-error status, parallel to `NO_FINDINGS`) with `reason=legend_or_reference_sheet`. It does NOT emit `FAILED_INPUTS`. Setting `ALLOW_REFERENCE_SHEETS=true` overrides the self-check.
- Aggregation treats `NO_FINDINGS_REFERENCE` pages as zero-count with explicit reason; they do not contaminate per-page totals or trigger reconciliation flags.

## 4. Run-folder layout and pointer contents

Every run folder follows a stable pattern. Implementers MUST use this pattern; assemblers/aggregators MUST emit `_LATEST.md` and the appropriate `*_TEMPLATE.md` files; **no agent or tool writes the final acceptance files or `_ACCEPTED.md` pointer** (see §5).

### 4.1 Run-folder path pattern

```
{SOURCE_DIR}/{DRAWING_TYPE}/{EXTRACTION_TARGET}/RUN-{YYYYMMDD-HHMMSS}-{PAGES_SPEC}/
```

Where `PAGES_SPEC` is the page range slug as already used by PFD tools (e.g., `0011-0022`, or `0001-0094` for the inventory). Timestamps are local time at run start, zero-padded, no separators inside the date or time block.

Examples:
- `{SOURCE_DIR}/DRAWING_SET/titleblock_index/RUN-20260427-141530-0001-0094/`
- `{SOURCE_DIR}/P_AND_ID/valve_count_basic/RUN-20260427-153045-0011-0022/`
- `{SOURCE_DIR}/P_AND_ID/valve_count_detailed/RUN-20260427-160212-0011-0022/`

### 4.2 Per-target run-folder contents

#### `(DRAWING_SET, titleblock_index)` run folder
```
RUN-{timestamp}-{pages}/
  RUN_CONTEXT.md                       # parameters used (PDF path, page range, DPI, corner crop ratios)
  RUN_SUMMARY.md                       # per-page status counts, per-family proposal counts, anomalies
  manifest.json                        # rasterized-page manifest (mirrors PFD pattern)
  {PDF_STEM}_page_NNNN_titleblock_stub.md     # one per page (target-aware path; see §6.1)
  {PDF_STEM}_titleblock_index_pages_{pages}.csv  # one row per page, drawing-family proposals
  {PDF_STEM}_titleblock_index_pages_{pages}.md   # human-readable mirror
  ACCEPTANCE_TEMPLATE.md               # template for human acceptance — see §5
  ACCEPTED_SCOPE_TEMPLATE.md           # template listing proposed P&ID page ranges — see §5
```

Pointers (sibling files outside the run folder):
- `{SOURCE_DIR}/DRAWING_SET/titleblock_index/_LATEST.md` — written by `assemble_titleblock_index_csv.py`; identifies the most recent run (whether accepted or not).
- `{SOURCE_DIR}/DRAWING_SET/titleblock_index/_ACCEPTED.md` — written ONLY by a human-invoked acceptance tool (§5).

#### `(P_AND_ID, valve_count_basic)` run folder
```
RUN-{timestamp}-{pages}/
  RUN_CONTEXT.md                       # parameters: tile_grid, overlap_px, body_box exclusion config
  RUN_SUMMARY.md                       # per-page status, per-tile finding counts, flag counts
  manifest.json                        # rasterized-page manifest
  tile_manifest.json                   # per-tile geometry registry across all pages in the run
  {PDF_STEM}_page_NNNN_tile_RRCC_basic_stub.md     # one per tile per page
  {PDF_STEM}_valve_candidates_pages_{pages}.csv    # one row per emitted candidate
  {PDF_STEM}_valve_counts_by_page_pages_{pages}.csv  # one row per page, totals
  {PDF_STEM}_valve_duplicate_tag_flags_pages_{pages}.csv  # QA backstop output
  flag_warnings.csv                    # unknown issue_flags surfaced by validator (D8)
  ACCEPTANCE_TEMPLATE.md               # template for human acceptance — see §5
```

Pointers:
- `{SOURCE_DIR}/P_AND_ID/valve_count_basic/_LATEST.md` — written by `aggregate_valve_counts.py`.
- `{SOURCE_DIR}/P_AND_ID/valve_count_basic/_ACCEPTED.md` — written ONLY by human-invoked acceptance tool.

#### `(P_AND_ID, valve_count_detailed)` run folder
```
RUN-{timestamp}-{pages}/
  RUN_CONTEXT.md                       # parameters + cited inventory_accepted_run + basic_accepted_run paths
  RUN_SUMMARY.md
  tile_manifest.json                   # MUST match basic's tile_manifest.json byte-for-byte (geometry locked)
  {PDF_STEM}_page_NNNN_tile_RRCC_detailed_stub.md
  {PDF_STEM}_valve_candidates_detailed_pages_{pages}.csv
  {PDF_STEM}_valve_counts_by_page_detailed_pages_{pages}.csv
  {PDF_STEM}_basic_vs_detailed_delta_pages_{pages}.csv      # reconciliation output
  RECONCILIATION_REPORT.md             # human-readable summary of deltas and recommended action per page
  flag_warnings.csv
  # NO ACCEPTANCE_TEMPLATE.md — detailed runs do not produce a downstream acceptance gate in this plan.
```

Pointers:
- `{SOURCE_DIR}/P_AND_ID/valve_count_detailed/_LATEST.md` — written by `aggregate_valve_counts.py`.
- No `_ACCEPTED.md` for detailed in this plan; detailed acceptance, if needed in the future, is a follow-on slice.

### 4.3 `_LATEST.md` schema (agent/tool-written, mutable)

```markdown
---
target: {DRAWING_TYPE}/{EXTRACTION_TARGET}
run_folder: RUN-{timestamp}-{pages}
written_by: {tool_name}
written_at: {ISO-8601 timestamp}
---

# Latest run pointer — {target}

**Run folder:** [`{run_folder}`](./{run_folder}/)
**Pages:** {pages_spec}
**Status:** {status_summary_one_line}
```

### 4.4 `_ACCEPTED.md` schema (human-written, mutable)

```markdown
---
target: {DRAWING_TYPE}/{EXTRACTION_TARGET}
accepted_run_folder: RUN-{timestamp}-{pages}
accepted_by: {human_name_or_role}
accepted_at: {ISO-8601 timestamp}
---

# Accepted run pointer — {target}

**Accepted run folder:** [`{accepted_run_folder}`](./{accepted_run_folder}/)
**Pages accepted:** {pages_spec}
**Acceptance evidence:** [`./{accepted_run_folder}/ACCEPTANCE.md`](./{accepted_run_folder}/ACCEPTANCE.md)
**Notes:** {free-form}
```

## 5. Acceptance authority model

This is a load-bearing contract. The plan distinguishes three artifact classes:

| Class | Filename(s) | Writer | Mutable? |
|---|---|---|---|
| Template | `ACCEPTANCE_TEMPLATE.md`, `ACCEPTED_SCOPE_TEMPLATE.md` | Agents/tools (assemblers) | Overwritten on each run |
| Acceptance | `ACCEPTANCE.md`, `ACCEPTED_SCOPE.md` | Humans only | Immutable once written into an accepted run folder |
| Pointer | `_ACCEPTED.md` | Humans only (via a human-invoked tool — see §5.3) | Mutable; new acceptances overwrite |

### 5.1 What templates contain

Each `ACCEPTANCE_TEMPLATE.md` includes:
- A header banner: *"This file is a TEMPLATE emitted by an agent. To accept this run, rename to `ACCEPTANCE.md`, complete the fields below, and update `../_ACCEPTED.md` via the human-invoked acceptance tool (see §5.3)."*
- Pre-filled `target`, `run_folder`, `pages` from the run.
- Empty `accepted_by`, `accepted_on`, `notes` for the human to complete.
- Citation back to `RUN_SUMMARY.md` and the combined CSV(s).

`ACCEPTED_SCOPE_TEMPLATE.md` (inventory only) additionally includes:
- A pre-filled `proposed_page_ranges` block grouped by `drawing_family_proposal`, derived from the inventory CSV. Each range is explicitly labeled as `proposal` until the human confirms or edits.

### 5.2 Why agents do not write final acceptance files

Acceptance is a human decision right (per `agents/AGENT_HELPS_HUMANS.md` § Step 3). If an agent silently elevated a template to acceptance, the workflow would have no way to distinguish agent-asserted acceptance from human-asserted acceptance — and the entire reconciliation gate for the detailed pass would be hollow.

### 5.3 Human-invoked acceptance tool

A tool `tools/drawing_extract/accept_run.py` is in scope for this plan as a thin convenience wrapper:

- **Inputs:** `--run-folder {path}`, `--accepted-by {name}`, optional `--notes {string}`.
- **Behavior:** verifies that `{run_folder}/ACCEPTANCE.md` exists and is non-empty (i.e., the human has filled it out). Atomically writes `{run_folder}/../_ACCEPTED.md` per §4.4.
- **Refuses to run** if `ACCEPTANCE.md` is absent, equals the template, or has empty `accepted_by`. Refusal exits with `2` and stderr message `acceptance evidence missing or unfilled`.
- **Idempotent:** rewriting `_ACCEPTED.md` to the same target run folder is a no-op (zero exit, no message). Pointing to a different run folder requires an explicit `--replace` flag (so accidental re-acceptance is avoided).

Pipeline tools (assemblers, aggregators, reconciler) are forbidden from writing `_ACCEPTED.md` directly. Only `accept_run.py`, invoked by a human, may write it.

## 6. Three new targets — per-target specs

### 6.1 Target 1: `(DRAWING_SET, titleblock_index)`

**Purpose.** Inventory every page of a PDF: page → `dwg_no`, `sheet_no`, `sheet_title`, `revision`, `area_or_module`, `drawing_family_proposal`, `titleblock_corner`.

**Skill:** `drawing-titleblock-page` (new — §8.1). Reasoning surface = four corner crops + a low-resolution full-page reference. The skill identifies which corner contains the titleblock and extracts canonical fields. `NO_TITLEBLOCK` is a valid outcome.

**Crop tool:** `prepare_titleblock_crops.py` (new — §10.A.1). Four corner crops per page + full-page thumbnail.

**Per-page stub path:**
`{SOURCE_DIR}/DRAWING_SET/titleblock_index/RUN-{ts}-{pages}/{PDF_STEM}_page_NNNN_titleblock_stub.md`

**Stub schema.** YAML frontmatter:
```yaml
drawing_type: DRAWING_SET
extraction_target: titleblock_index
source_pdf: {basename}
source_page: {int}
corner_crop_geometry:
  width_ratio: 0.25
  height_ratio: 0.25
finding_count: 0 | 1
```
Body table (single row when found):
```
| dwg_no | sheet_no | sheet_title | revision | area_or_module | drawing_family_proposal | titleblock_corner | confidence |
```

**Assembly:** `assemble_titleblock_index_csv.py` (§10.A.6) — one row per page; emits the run folder per §4.2; writes `_LATEST.md` and both templates.

### 6.2 Target 2: `(P_AND_ID, valve_count_basic)`

**Purpose.** Establish the authoritative per-page valve count via candidate rows.

**Skill:** `pandid-valve-tile` with `RuntimeOverride: mode=basic` (new — §8.2).

**Phase 0 scope gate.** The orchestrator reads `{SOURCE_DIR}/DRAWING_SET/titleblock_index/_ACCEPTED.md` and resolves the accepted run folder. If `_ACCEPTED.md` is missing OR the resolved folder lacks `ACCEPTED_SCOPE.md` (the human-completed file), Phase 0 rejects with `inventory scope not accepted; run accept_run.py against the inventory before dispatching valve_count_basic`. The accepted scope filters the page list before tile dispatch.

**Crop tool:** `prepare_pandid_tiles.py` (new — §10.B.1). 5×4 default grid (D5); conservative body-box default (border + titleblock excluded only — D4); emit-box overlay + 5×5 mini-grid drawn on each tile image; per-page and run-level tile manifests.

**Per-tile stub path:**
`{SOURCE_DIR}/P_AND_ID/valve_count_basic/RUN-{ts}-{pages}/{PDF_STEM}_page_NNNN_tile_RRCC_basic_stub.md`

Where `RRCC` is two-digit row + two-digit column (e.g., `r02c03`).

**Stub schema.** YAML frontmatter:
```yaml
drawing_type: P_AND_ID
extraction_target: valve_count_basic
mode: basic
source_pdf: {basename}
source_page: {int}
tile_id: page_NNNN_r{RR}c{CC}
tile_grid: "5x4"
body_box_px: [x0, y0, x1, y1]                  # body-box used for partition
body_exclusions: [border, titleblock]          # which exclusions were active
read_box_px: [x0, y0, x1, y1]
emit_box_px: [x0, y0, x1, y1]
overlap_px: 200
mini_grid: "5x5"
dwg_no: TBD                                    # post-process inherit from titleblock-index
system_name: TBD
finding_count: {int}
```
Body table (one row per emitted candidate):
```
| valve_index | valve_category | valve_tag | tag_basis | approx_location_in_emit_box | issue_flags | notes |
```
- `valve_category ∈ {manual_block, manual_throttle, check, control, esd_block, relief, unknown}`.
- `tag_basis ∈ {visible_near_symbol, inferred_from_designation, TBD}`.
- `approx_location_in_emit_box ∈ {A1..E5}` (5×5 mini-grid).
- `issue_flags`: list serialized as `[FLAG_A, FLAG_B]` (empty = `[]`).

**Run statuses:** `SUCCESS | NO_FINDINGS | NO_FINDINGS_REFERENCE | FAILED | FAILED_INPUTS`.

**Assembly:** `assemble_valve_candidates_csv.py` (§10.B.7), `aggregate_valve_counts.py` (§10.B.8), `flag_duplicate_valve_candidates.py` (§10.B.9). Run folder per §4.2; aggregator writes `_LATEST.md` and `ACCEPTANCE_TEMPLATE.md`.

### 6.3 Target 3: `(P_AND_ID, valve_count_detailed)`

**Purpose.** Add classification (size, type, actuation) to the valve candidates. Reconciled against a basic pass.

**Skill:** `pandid-valve-tile` with `RuntimeOverride: mode=detailed`.

**Phase 0 acceptance gate.** Reads two `_ACCEPTED.md` pointers (inventory and basic). Each must resolve to a run folder containing the human-completed acceptance file (`ACCEPTANCE.md` for basic; `ACCEPTANCE.md` + `ACCEPTED_SCOPE.md` for inventory). Either missing → reject with explicit message naming the missing pointer.

**Crop tool:** Same `prepare_pandid_tiles.py`. **Tile geometry MUST match the basic run byte-for-byte:** the orchestrator passes the basic run's `tile_manifest.json` as `--tile-manifest-reference` and the crop tool refuses to run if regenerated geometry would differ. This guarantees row alignment between basic and detailed candidates.

**Per-tile stub path:**
`{SOURCE_DIR}/P_AND_ID/valve_count_detailed/RUN-{ts}-{pages}/{PDF_STEM}_page_NNNN_tile_RRCC_detailed_stub.md`

**Stub schema.** Same frontmatter as basic plus:
```yaml
mode: detailed
inventory_accepted_run: {path to inventory accepted run folder}
basic_accepted_run: {path to basic accepted run folder}
```
Body table extends basic columns with: `valve_size_text, valve_type_code, valve_type_name, actuation`. Unreadable evidence → `TBD`.

**Reconciliation:** `reconcile_basic_vs_detailed.py` (§10.B.10) emits `*_basic_vs_detailed_delta.csv` and `RECONCILIATION_REPORT.md`. Default thresholds: `flag=RECONCILE_REVIEW` when `|delta| > 2` AND `abs_delta_pct > 10%`. Pages classified `NO_FINDINGS_REFERENCE` in either pass are excluded from reconciliation. **`reconcile_basic_vs_detailed.py` does NOT emit any `ACCEPTANCE_TEMPLATE.md`** (the basic acceptance template was emitted in Slice 4 by the basic aggregator; detailed has no downstream acceptance gate in this plan).

## 7. Files to MODIFY

### 7.1 `agents/AGENT_DRAWING_EXTRACT.md`
Edits required:
- **Drawing-type + extraction-target registry table** (currently lines ~36–48): move `P_AND_ID` from `stubbed (fail-fast)` to `implemented` with two targets (`valve_count_basic`, `valve_count_detailed`). Add a new row for the pseudo-type `DRAWING_SET` with target `titleblock_index`.
- **Phase 0 step 2** (currently lines ~150–153): remove `P_AND_ID` from the stubbed-types reject set; add `DRAWING_SET` as a known pseudo-type.
- **New § Target → tool-chain dispatch table.** Keyed on `(drawing_type, extraction_target)`. Each row lists the crop tool, the dispatched skill, the brief-builder, the stub-format validator, the resume-metadata validator, the assembler, and the aggregator/reconciler. Implementers MUST consult this table when wiring Phase 1.5 / 2 / 3 hooks for the new targets. Existing PFD rows must remain unchanged.
- **Repertoire Hook Registry table** (currently lines ~415–434): rename to "Implemented Type Hook Registry" and add columns/rows for `DRAWING_SET, titleblock_index`, `P_AND_ID, valve_count_basic`, `P_AND_ID, valve_count_detailed`.
- **New § Acceptance gates.** Documents §4–§5 of this plan: run-folder pattern, pointer schemas, template-vs-acceptance authority, the `accept_run.py` tool, and the inventory + basic gates that the detailed target consults at Phase 0.
- **New § Reference/legend page handling.** Documents D13: orchestrator pre-filter via `ACCEPTED_SCOPE.md`; skill-side `NO_FINDINGS_REFERENCE` defense in depth; aggregator handling.
- **New runtime parameters** in the appropriate Runtime Parameters subsection: `BASIC_REFERENCE_PATH` (resolved via `_ACCEPTED.md`), `INVENTORY_REFERENCE_PATH` (likewise), `ALLOW_REFERENCE_SHEETS`, `TILE_GRID` (default `5x4`), `OVERLAP_PX` (default `200`), `BODY_EXCLUSIONS` (default `[border, titleblock]`).

### 7.2 `tools/REGISTRY.md`
Append entries under two new subsections:
- "drawing extract — sheet inventory"
- "drawing extract — P&ID valve count"

Each entry uses the existing schema (`Name | Category | Language | Purpose | Inputs | Outputs`). Tool-list authority is the registry; this plan's §10 is the design source.

### 7.3 `skills/drawing-extract-page/SKILL.md`
**Body unchanged.** Add a one-paragraph scope clarifier at the top, immediately under the frontmatter:

> **Scope.** This skill extracts equipment-header data from PFD pages. It is PFD-equipment-scoped. Per-page titleblock extraction lives in `skills/drawing-titleblock-page/`. P&ID valve-tile extraction lives in `skills/pandid-valve-tile/`. Do not extend this skill to handle non-PFD or non-equipment-header workflows — add a new skill instead.

### 7.4 Files explicitly NOT modified
- `tools/drawing_extract/prepare_header_crops.py` — stays PFD-only and continues to fail for `P_AND_ID`. Implemented/stubbed status lives in `agents/AGENT_DRAWING_EXTRACT.md` per D9, not in every crop tool.
- `tools/drawing_extract/normalize_equipment_stub_layout.py` — equipment-only.
- `tools/drawing_extract/build_page_worker_brief.py` — PFD-only. New brief-builders are added per skill (§10).
- `tools/drawing_extract/extract_pdf_titleblock_text.py` — PFD cross-check aid only.
- `tools/drawing_extract/validate_resume_stub_metadata.py`, `validate_stub_format.py`, `validate_detailed_schema.py` — PFD/equipment-only. New target-specific validators are added.

## 8. New skills

Both skills follow the `skills/SKILL_TEMPLATE.md` skeleton and must pass `python3 tools/validation/validate_skill_metadata.py skills` after authoring.

### 8.1 `skills/drawing-titleblock-page/`

**Purpose.** Per-page titleblock extraction across drawing types. Reads four corner crops + a low-resolution full-page reference; identifies which corner contains the titleblock; extracts canonical sheet metadata.

**Files (per `agents/AGENT_SKILLMAKER.md` Phase 4):**
- `SKILL.md` — purpose, suitable shells (TASK), inputs, runtime overrides, tool usage, canonical output template, non-negotiable constraints, QA expectations.
- `BRIEF_SCHEMA.md` — required dispatch fields: `source_pdf, source_page, corner_crop_paths (4), full_page_thumbnail_path, output_path`. Recommended `CustomInstructions` reinforce the canonical template and "no invention → TBD" rule.
- `TOOL_POLICY.md` — preferred: VLM image read; optional: none; disallowed: web access, deterministic OCR (we want VLM authority for these titleblocks since pdftotext is known to fail on the target series).
- `QA_CHECKS.md` — every `SUCCESS` stub has `finding_count=1` AND a populated `dwg_no` OR an explicit `dwg_no=TBD` with `confidence=low`. `NO_TITLEBLOCK` stubs have `finding_count=0` and an empty body table.

**Non-negotiable constraints (in `SKILL.md`):**
- The skill MUST classify each page's `drawing_family_proposal` as a *proposal*, not as ground truth (D11). The literal string `proposal` appears in the skill prompt.
- Unreadable fields → `TBD`. The skill MUST NOT guess `dwg_no` or `sheet_no`.
- `confidence ∈ {high, medium, low}`.

### 8.2 `skills/pandid-valve-tile/`

**Purpose.** Per-tile valve candidate emission under the emit-zone contract (D4). Same skill serves basic and detailed targets via a `mode` runtime override.

**Files:**
- `SKILL.md` — see Non-negotiable constraints below; canonical output template per §6.2 / §6.3; both modes documented.
- `BRIEF_SCHEMA.md` — required: `source_pdf, source_page, tile_id, tile_image_path, tile_geometry (read_box_px, emit_box_px, mini_grid, overlap_px), mode ∈ {basic, detailed}, output_path`. Recommended `CustomInstructions` reinforce the emit-zone rule, the legend self-check, and the `issue_flags` controlled vocabulary.
- `TOOL_POLICY.md` — preferred: VLM image read on the tile + optional full-page reference; disallowed: web, deterministic OCR.
- `QA_CHECKS.md` — every `SUCCESS` stub has `finding_count` matching parsed body rows; `NO_FINDINGS_REFERENCE` stubs have `finding_count=0` and explicit `reason=legend_or_reference_sheet`; `issue_flags` values fall within the controlled vocabulary OR are surfaced in `flag_warnings.csv` with a WARNING (D8).

**Non-negotiable constraints (in `SKILL.md`):**
- The emit-zone rule is a hard contract: a candidate's visual center MUST be inside the emit box (the rectangle outlined in the overlay) for the candidate to be emitted as a row. Visible-but-outside candidates are documented in `notes` only.
- Pixel coordinates are NOT requested or used; `approx_location_in_emit_box` MUST be one of the 25 mini-grid cells `A1..E5` (D7).
- Reference-sheet self-check: if the tile evidently belongs to a legend, symbol-key, or reference page (e.g., titled "LEGEND", "SYMBOLS", "ABBREVIATIONS"), the skill returns `RUN_STATUS=NO_FINDINGS_REFERENCE` UNLESS `ALLOW_REFERENCE_SHEETS=true` is set. It does NOT emit `FAILED_INPUTS` (D13).
- `issue_flags` is a list and uses the controlled vocabulary in §6.2/§6.3 (D8). The skill MAY emit a flag outside the vocabulary, but the validator will warn and surface it for operator review.

## 9. New deterministic tools — overview

Tools are listed in §10 with full Purpose / Inputs / Outputs / Example / Idempotence specs, ready for TOOLMAKER to implement against `agents/AGENT_TOOLMAKER.md` Phase 3 (§ STRUCTURE / Tool file template).

Sheet-inventory tools — §10.A:
1. `prepare_titleblock_crops.py`
2. `titleblock_stub_layout.py`
3. `build_titleblock_page_brief.py`
4. `validate_titleblock_stub_format.py`
5. `validate_titleblock_resume_metadata.py`
6. `assemble_titleblock_index_csv.py`

P&ID valve tools — §10.B:
1. `prepare_pandid_tiles.py`
2. `validate_tile_partition.py`
3. `valve_stub_layout.py`
4. `build_pandid_valve_tile_brief.py`
5. `validate_valve_tile_stub_format.py`
6. `validate_valve_tile_resume_metadata.py`
7. `assemble_valve_candidates_csv.py`
8. `aggregate_valve_counts.py`
9. `flag_duplicate_valve_candidates.py`
10. `reconcile_basic_vs_detailed.py`

Cross-cutting acceptance tool — §10.C:
1. `accept_run.py`

Optional shared primitive (build only if duplication actually emerges):
- `stub_layout.py`

## 10. Tool specs

Each spec follows `agents/AGENT_TOOLMAKER.md` § STRUCTURE: Purpose, Inputs, Outputs, Example, Idempotence, Scope boundary. Implementers fill in the body and register in `tools/REGISTRY.md`.

### 10.A — Sheet-inventory tools

#### 10.A.1 `tools/drawing_extract/prepare_titleblock_crops.py`
- **Purpose.** Generate four corner crops + a low-resolution full-page thumbnail for each page in scope.
- **Inputs.** `WORK_DIR` (positional), `--pages {start-end}`, `--corner-width-ratio 0.25`, `--corner-height-ratio 0.25`, `--thumbnail-width-px 1600`.
- **Outputs.** Per page: `page_NNNN_titleblock_tl.png`, `_tr.png`, `_bl.png`, `_br.png`, `page_NNNN_thumbnail.png`. Updates `manifest.json`.
- **Example.** `python3 tools/drawing_extract/prepare_titleblock_crops.py {WORK_DIR} --pages 1-94`
- **Idempotence.** Idempotent. Reuses existing crops when SHA-256 of the source page image and the geometry parameters match.
- **Scope boundary.** Writes only inside `WORK_DIR`.

#### 10.A.2 `tools/drawing_extract/titleblock_stub_layout.py`
- **Purpose.** Library: parse, render, and validate `(DRAWING_SET, titleblock_index)` per-page stubs.
- **Public functions.** `parse(stub_path) -> StubModel`, `render(stub_model) -> str`, `render_template_for_brief(runtime_params) -> str`, `BASE_COLUMNS`, `KNOWN_FRONTMATTER_KEYS`.
- **Imports.** Standalone — does not import `normalize_equipment_stub_layout.py` (D10).

#### 10.A.3 `tools/drawing_extract/build_titleblock_page_brief.py`
- **Purpose.** Emit a valid INIT-TASK brief targeting `drawing-titleblock-page` for one page, including canonical output template rendered from `titleblock_stub_layout.render_template_for_brief()`.
- **Inputs.** `--source-dir`, `--pdf-stem`, `--source-pdf-name`, `--work-dir`, `--page`, `--total-pages`, `--output-path`.
- **Outputs.** Brief markdown to stdout (consumed by orchestrator dispatch).
- **Idempotence.** Pure; same inputs → byte-identical output.

#### 10.A.4 `tools/drawing_extract/validate_titleblock_stub_format.py`
- **Purpose.** Per-stub schema/format validator. Confirms frontmatter keys + types, body-table column header conformance, finding_count vs row count.
- **Inputs.** `--source-dir, --pdf-stem, --start-page, --end-page, --pages {csv list, optional}`.
- **Outputs.** Exit 0 = all stubs in scope valid; exit 1 = format failures (per-file diff to stderr).
- **Idempotence.** Read-only.

#### 10.A.5 `tools/drawing_extract/validate_titleblock_resume_metadata.py`
- **Purpose.** Confirm existing per-page stubs match the current run's parameter tuple. Resume tuple keys: `source_pdf, source_page, corner_crop_geometry`.
- **Inputs.** Same shape as `validate_resume_stub_metadata.py` for parity, plus `--corner-width-ratio`, `--corner-height-ratio`.
- **Outputs.** Exit codes per existing convention (0 = OK, 1 = mismatch with diff, 2 = setup error).

#### 10.A.6 `tools/drawing_extract/assemble_titleblock_index_csv.py`
- **Purpose.** Combine per-page titleblock stubs into a sheet-inventory CSV + Markdown mirror; create the run folder per §4.2; write `_LATEST.md`, `ACCEPTANCE_TEMPLATE.md`, `ACCEPTED_SCOPE_TEMPLATE.md`.
- **Inputs.** `--source-dir, --pdf-stem, --start-page, --end-page, --output-csv, --output-md`. Discovers stubs from the target-aware folder.
- **Outputs.** CSV with columns `page, dwg_no, sheet_no, sheet_title, revision, area_or_module, drawing_family_proposal, titleblock_corner, confidence, run_status`. Markdown mirror. `_LATEST.md` per §4.3. Both templates per §5.1.
- **Idempotence.** Re-running on the same stub set produces byte-identical CSV/MD; `_LATEST.md` and templates are overwritten.
- **MUST NOT** write `_ACCEPTED.md`, `ACCEPTANCE.md`, or `ACCEPTED_SCOPE.md` (§5).

### 10.B — P&ID valve tools

#### 10.B.1 `tools/drawing_extract/prepare_pandid_tiles.py`
- **Purpose.** Compute body box, partition into emit boxes, expand to read boxes, render tile images with deterministic emit-box border + 5×5 mini-grid overlay, and emit per-page + run-level tile manifests.
- **Inputs.** `WORK_DIR` (positional), `--pages {start-end}`, `--tile-grid 5x4`, `--overlap-px 200`, `--body-exclusions border,titleblock` (comma list), `--mini-grid 5x5`, `--page-overrides {path-to-yaml}` (optional, per-page geometry overrides), `--tile-manifest-reference {path}` (optional, used by detailed runs to lock geometry to basic).
- **Outputs.** Per page per tile: `page_NNNN_tile_rRRcCC.png`. Per page: `page_NNNN_tile_manifest.json`. Run-level: `tile_manifest.json` aggregating all pages. Each tile-manifest entry: `{tile_id, source_page, body_box_px, body_exclusions, read_box_px, emit_box_px, mini_grid_px, overlap_px, image_path, image_sha256}`.
- **Self-check.** Calls `validate_tile_partition.py` after rendering; non-zero exit fails the run.
- **Example.** `python3 tools/drawing_extract/prepare_pandid_tiles.py {WORK_DIR} --pages 11-22 --tile-grid 5x4 --overlap-px 200 --body-exclusions border,titleblock`
- **Idempotence.** Idempotent on the run-level manifest. With `--tile-manifest-reference`, refuses to run if regenerated geometry would differ from the reference (exit 1, diff to stderr).
- **Scope boundary.** Writes only inside `WORK_DIR`.

#### 10.B.2 `tools/drawing_extract/validate_tile_partition.py`
- **Purpose.** Numerically prove the tile-contract invariants (D4): `union(emit_boxes) == body_box`, `pairwise_overlap(emit_boxes) == 0`, `read_box ⊇ emit_box ∀ tile`.
- **Inputs.** `--tile-manifest {path}`.
- **Outputs.** Exit 0 = all invariants hold; exit 1 = invariant failure with which tile(s) and which invariant.
- **Idempotence.** Read-only.

#### 10.B.3 `tools/drawing_extract/valve_stub_layout.py`
- **Purpose.** Library: parse, render, validate `(P_AND_ID, valve_count_*)` per-tile stubs. Knows basic vs detailed column sets and the `issue_flags` controlled vocabulary.
- **Public functions.** `parse(stub_path) -> StubModel`, `render(stub_model) -> str`, `render_template_for_brief(runtime_params, mode) -> str`, `BASIC_BODY_COLUMNS`, `DETAILED_BODY_COLUMNS`, `BASIC_ISSUE_FLAGS`, `DETAILED_ISSUE_FLAGS`, `is_known_flag(flag, mode) -> bool`.
- **Imports.** Standalone (D10).

#### 10.B.4 `tools/drawing_extract/build_pandid_valve_tile_brief.py`
- **Purpose.** Emit a valid INIT-TASK brief targeting `pandid-valve-tile` for one tile. Mode-aware (basic vs detailed). Includes canonical template via `valve_stub_layout.render_template_for_brief()`.
- **Inputs.** `--source-dir, --pdf-stem, --source-pdf-name, --work-dir, --page, --tile-id, --mode {basic|detailed}, --output-path, [--allow-reference-sheets]`.
- **Outputs.** Brief markdown to stdout. CustomInstructions include the emit-zone rule, the legend self-check, the `issue_flags` controlled vocabulary, and a completion checklist.
- **Idempotence.** Pure.

#### 10.B.5 `tools/drawing_extract/validate_valve_tile_stub_format.py`
- **Purpose.** Per-stub schema/format validator. Mode-aware: basic stubs reject detailed-only columns; detailed stubs require detailed-only columns. Validates `issue_flags` list serialization; unknown flags → WARNING, written to `flag_warnings.csv` rather than exit-1 (D8).
- **Inputs.** `--source-dir, --target {valve_count_basic|valve_count_detailed}, --pdf-stem, --start-page, --end-page, --pages {csv list, optional}, --warnings-csv {path}`.
- **Outputs.** Exit 0 = all stubs format-valid (warnings allowed); exit 1 = format failures.

#### 10.B.6 `tools/drawing_extract/validate_valve_tile_resume_metadata.py`
- **Purpose.** Confirm per-tile stubs match the current run's parameter tuple. Resume tuple: `target, mode, source_pdf, source_page, tile_id, tile_grid, body_box_px, body_exclusions, read_box_px, emit_box_px, overlap_px, mini_grid`.
- **Inputs / Outputs.** Same shape and exit-code conventions as the existing PFD validator.

#### 10.B.7 `tools/drawing_extract/assemble_valve_candidates_csv.py`
- **Purpose.** Combine per-tile stubs into a candidate-row CSV across the run.
- **Inputs.** `--source-dir, --target, --mode, --pdf-stem, --start-page, --end-page, --output-csv`.
- **Outputs.** CSV: `source_page, tile_id, valve_index, valve_category, valve_tag, tag_basis, approx_location_in_emit_box, issue_flags, notes` (plus detailed columns when `mode=detailed`).
- **Idempotence.** Pure aggregation.

#### 10.B.8 `tools/drawing_extract/aggregate_valve_counts.py`
- **Purpose.** Compute per-page totals from candidate rows. Mode-agnostic. Writes `_LATEST.md` for the run. For `mode=basic` ONLY, also writes `ACCEPTANCE_TEMPLATE.md` to the run folder. For `mode=detailed`, does NOT write any acceptance template.
- **Inputs.** `--candidates-csv, --target, --mode, --output-csv, --run-folder`.
- **Outputs.** CSV: `page, drawing, total_count, by_category_counts_json, boundary_review_count, low_legibility_count, no_findings_reference_pages_excluded`. Plus `_LATEST.md` and (basic only) `ACCEPTANCE_TEMPLATE.md`.
- **MUST NOT** write `_ACCEPTED.md` or `ACCEPTANCE.md`.

#### 10.B.9 `tools/drawing_extract/flag_duplicate_valve_candidates.py`
- **Purpose.** QA backstop. Surfaces non-empty `valve_tag` values appearing in more than one tile across the run, for human review. Does NOT classify cause (D4).
- **Inputs.** `--candidates-csv, --output-csv`.
- **Outputs.** CSV: `valve_tag, occurrence_count, occurrences (list of {source_page, tile_id, valve_index})`. Empty CSV (header only) when no duplicates.

#### 10.B.10 `tools/drawing_extract/reconcile_basic_vs_detailed.py`
- **Purpose.** Page-level delta report between accepted basic counts and detailed counts. Emits delta CSV + `RECONCILIATION_REPORT.md`.
- **Inputs.** `--basic-counts-csv, --detailed-counts-csv, --output-csv, --output-md, --delta-threshold 2, --pct-threshold 10`.
- **Outputs.** CSV: `page, basic_count, detailed_count, delta, abs_delta_pct, flag` where `flag ∈ {OK, RECONCILE_REVIEW}`. Pages flagged `NO_FINDINGS_REFERENCE` in either pass are excluded.
- **MUST NOT** emit any `ACCEPTANCE_TEMPLATE.md` (this is a corrected scope vs an earlier draft of this plan; basic acceptance template lives with the basic aggregator).

### 10.C — Cross-cutting acceptance tool

#### 10.C.1 `tools/drawing_extract/accept_run.py`
- **Purpose.** Human-invoked atomic write of `_ACCEPTED.md`, gated on the existence of a non-empty human-completed `ACCEPTANCE.md` (and, for inventory, `ACCEPTED_SCOPE.md`).
- **Inputs.** `--run-folder {path}, --accepted-by {name}, --notes {string, optional}, [--replace]`.
- **Behavior.**
  - Resolve target from the run folder's parent path (`{SOURCE_DIR}/{DRAWING_TYPE}/{EXTRACTION_TARGET}/`).
  - Verify `{run_folder}/ACCEPTANCE.md` exists, is non-empty, is not byte-identical to `ACCEPTANCE_TEMPLATE.md`, and has a non-empty `accepted_by` field.
  - For `(DRAWING_SET, titleblock_index)` runs, additionally verify `{run_folder}/ACCEPTED_SCOPE.md` exists, is non-empty, and is not byte-identical to `ACCEPTED_SCOPE_TEMPLATE.md`.
  - Atomically write `{run_folder}/../_ACCEPTED.md` per §4.4.
  - If `_ACCEPTED.md` already points elsewhere, refuse without `--replace`.
- **Outputs.** Stdout one-line `accepted: {target} -> {run_folder}` on success. Exit 0 success, exit 2 acceptance evidence missing/unfilled, exit 3 already accepted (no `--replace`).
- **Idempotence.** Re-pointing `_ACCEPTED.md` at the same run folder is a no-op (zero exit, no message).
- **Scope boundary.** Writes ONLY `_ACCEPTED.md` next to the run folder. Never modifies the run folder itself.

## 11. Implementation sequencing

Build incrementally. Each slice ends with a runnable demonstration against the representative PDF, a registry update, and a commit boundary. **Detailed valve extraction does not merge until inventory, tiling, and basic counts are proven on the representative PDF.**

### Slice 1 — Sheet inventory
- Skill: `drawing-titleblock-page` (§8.1).
- Tools: `prepare_titleblock_crops.py`, `titleblock_stub_layout.py`, `build_titleblock_page_brief.py`, `validate_titleblock_stub_format.py`, `validate_titleblock_resume_metadata.py`, `assemble_titleblock_index_csv.py`, `accept_run.py` (cross-cutting).
- Agent edits: Phase 0 accepts `DRAWING_SET`; target hook registry rows for `titleblock_index`; new acceptance-gate § (templated for future basic/detailed gates); runtime parameters.
- Demo: run against the full 94-page representative PDF; operator inspects inventory CSV; operator hand-completes `ACCEPTANCE.md` + `ACCEPTED_SCOPE.md`; operator runs `accept_run.py`; `_ACCEPTED.md` exists.

### Slice 2 — Tile prep + manifest
- Tools only: `prepare_pandid_tiles.py`, `validate_tile_partition.py`. No skill yet.
- Demo: run on 1–3 P&ID pages identified in Slice 1; visual inspection of all 20 tile images per page; `validate_tile_partition.py` exits 0 on each page.

### Slice 3 — Basic valve pass on 1–3 pages
- Skill: `pandid-valve-tile` with basic-mode contract (§8.2).
- Tools: `valve_stub_layout.py`, `build_pandid_valve_tile_brief.py`, `validate_valve_tile_stub_format.py`, `validate_valve_tile_resume_metadata.py`.
- Agent edits: Phase 0 accepts `P_AND_ID`; target hook rows for `valve_count_basic`; orchestrator pre-filter via `ACCEPTED_SCOPE.md` is wired up; reference/legend handling documented.
- Demo: run on 1–3 pages from Slice 2; spot-check counts manually; force-dispatch a known legend page via `--pages` and confirm `NO_FINDINGS_REFERENCE`.

### Slice 4 — Full basic aggregation + acceptance pointer
- Tools: `assemble_valve_candidates_csv.py`, `aggregate_valve_counts.py`, `flag_duplicate_valve_candidates.py`. Aggregator emits basic `ACCEPTANCE_TEMPLATE.md`.
- Demo: run across the full accepted P&ID range; operator hand-completes basic `ACCEPTANCE.md`; runs `accept_run.py`; basic `_ACCEPTED.md` exists.

### Slice 5 — Detailed valve pass + reconciliation
- Skill: `pandid-valve-tile` detailed-mode contract added.
- Tools: `reconcile_basic_vs_detailed.py`. `prepare_pandid_tiles.py` extended to consume `--tile-manifest-reference` from the basic accepted run.
- Agent edits: target hook rows for `valve_count_detailed`; Phase 0 acceptance gate (both pointers required); reconciliation phase documented in PROTOCOL.
- Demo: run detailed against the same range as Slice 4; review `RECONCILIATION_REPORT.md` flags; iterate on tile geometry where flagged.

## 12. Verification

End-to-end after all five slices. Each item is independently checkable.

1. **Sheet-inventory pass.** `(DRAWING_SET, titleblock_index)` against pages 1–94 of the representative PDF. Inventory CSV proposes `drawing_family_proposal=P_AND_ID` for the 1X00/2X00/7X00 series with sensible `dwg_no`/`sheet_title`. Run folder contains `ACCEPTANCE_TEMPLATE.md` and `ACCEPTED_SCOPE_TEMPLATE.md`. `_LATEST.md` written; `_ACCEPTED.md` does not exist yet. Spot-check 5 pages against rendered images.
2. **Inventory acceptance gate.** Dispatch `valve_count_basic` before writing `ACCEPTED_SCOPE.md` → reject with explicit message. Hand-complete acceptance + scope; run `accept_run.py`; re-dispatch; confirm orchestrator pre-filter honors the scope (out-of-scope pages are not dispatched).
3. **Tile partition proof.** `validate_tile_partition.py` exits 0 on each P&ID page in scope.
4. **Tile prep visual sanity.** Inspect all 20 tile images for one P&ID page; emit-box overlay visible; 5×5 mini-grid faint but legible; read box clipped at page edges.
5. **Basic valve pass.** Hand-count valves on 2–3 pages; ±1 valve per page acceptable VLM noise. `flag_duplicate_valve_candidates.py` surfaces any cross-tile duplicate tags as QA flags (not errors); inspect each manually.
6. **Emit-zone regression.** Pick a page with valves near tile boundaries; verify adjacent tiles' body tables do not both list the same valve.
7. **Reference/legend handling.** Force-dispatch a single legend page via `--pages` override (bypassing scope filter). Confirm `RUN_STATUS=NO_FINDINGS_REFERENCE` (not `FAILED_INPUTS`); confirm aggregator records the page as zero-count with reason and does not flag reconciliation. Re-dispatch with `ALLOW_REFERENCE_SHEETS=true`; confirm normal processing.
8. **Issue-flag list.** Confirm a single candidate row can carry multiple flags (e.g., `[BOUNDARY_REVIEW, LOW_LEGIBILITY]`) round-tripping through assembler and aggregator. Inject an unknown flag (e.g., `EXPERIMENTAL_FLAG`) and confirm `flag_warnings.csv` records it without failing the validator (D8).
9. **Basic-count acceptance gate.** Dispatch `valve_count_detailed` before basic `ACCEPTANCE.md` exists → reject. Hand-complete basic `ACCEPTANCE.md`; run `accept_run.py`; re-dispatch; confirm acceptance.
10. **Tile geometry lock for detailed.** Dispatch `valve_count_detailed` with a different `--tile-grid` than the basic run; confirm `prepare_pandid_tiles.py` refuses to run because the regenerated geometry differs from `--tile-manifest-reference`.
11. **Detailed pass + reconciliation.** Run detailed; `reconcile_basic_vs_detailed.py` produces a delta CSV + `RECONCILIATION_REPORT.md`. Pages within threshold show `flag=OK`; an artificially shifted detailed re-run flags `RECONCILE_REVIEW`. `NO_FINDINGS_REFERENCE` pages are excluded from reconciliation.
12. **Resume-safety per target.** Re-run any target with identical parameters → `validate_*_resume_metadata.py` exits 0. Re-run with `tile_grid=6x4` → exit 1 with field-diff message. Re-run with a different `body_box_px` or `body_exclusions` → exit 1.
13. **Stubbed-type fail-fast preserved.** `DRAWING_TYPE=ISOMETRIC` rejects at Phase 0 with the existing message.
14. **Skill validator.** `python3 tools/validation/validate_skill_metadata.py skills` exits 0.
15. **Acceptance authority.** Confirm no pipeline tool writes `ACCEPTANCE.md`, `ACCEPTED_SCOPE.md`, or `_ACCEPTED.md`. Confirm `accept_run.py` refuses to run when `ACCEPTANCE.md` is missing or byte-identical to its template.

## 13. Cross-references

- `agents/AGENT_HELPS_HUMANS.md` — workflow design standard governing this plan.
- `agents/AGENT_DRAWING_EXTRACT.md` — orchestrator instruction; primary edit target.
- `agents/AGENT_SKILLMAKER.md` — governs the two new skills.
- `agents/AGENT_TOOLMAKER.md` — governs the new deterministic tools.
- `agents/AGENT_TASK.md` — TASK shell that loads the skills at runtime.
- `skills/SKILL_TEMPLATE.md` — skeleton for the two new skills.
- `skills/drawing-extract-page/` — pattern source; receives a scope clarifier only.
- `tools/drawing_extract/` — destination for all new tools; existing tools serve as patterns (cited in §10).
- `tools/REGISTRY.md` — append-only registry update.
- `tools/validation/validate_skill_metadata.py` — must exit 0 after skills land.
- `domain-test/domains/West_Doe_Comp_and_Liquids_DBM/_Sources/MFS-242510_(3-25_Doe)_rA_IFI_(Permit_Application).pdf` — representative source for verification.
