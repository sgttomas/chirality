# Source Pack: Skill pack: equipment-costing-extract

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/equipment-costing-extract/BRIEF_SCHEMA.md

### equipment-costing-extract — Brief Schema

Use this skill with a generic TASK shell (no profile) like this:

```md
PURPOSE: Extract costing-relevant equipment specs from KTY-04-05
RequestedBy: WORKING_ITEMS

ScopePath: {DOMAIN_ROOT}
TaskSkill: equipment-costing-extract

AllowedWriteTargets:
  - "{DOMAIN_ROOT}/_Aggregation/Equipment_Extract/"

RuntimeOverrides:
  KTY_PATH: /abs/path/to/CAT-004_Process Description/1_Working/KTY-04-05_Inlet-Compressors
  OUTPUT_ROOT: /abs/path/to/_Aggregation/Equipment_Extract/
  EQUIPMENT_TYPES: "COMPRESSOR MODULE;SEPARATOR MODULE;STABILIZER MODULE;DEHYDRATION MODULE;FILTER COALESCER MODULE;ACCUMULATOR MODULE;EXPANSION TANK;FLARE KO DRUM MODULE;FLARE STACK;INSTRUMENT AIR MODULE;NEUTRAL GROUNDING RESISTOR;PROCESS PUMP MODULE;PROCESS HEAT MEDIUM HEATER MODULE;STORAGE TANK;VAPOUR RECOVERY UNIT MODULE"
  EQUIPMENT_EXTRACT_PATH: /abs/path/to/_Aggregation/Equipment_Extract/KTY-04-05_Equipment_Extract.md
```

#### Required fields

| Field | Value | Notes |
|---|---|---|
| `ScopePath` | `{DOMAIN_ROOT}` | Top-level domain execution root |
| `TaskSkill` | `equipment-costing-extract` | Must match skill folder name |
| `AllowedWriteTargets` | `["{DOMAIN_ROOT}/_Aggregation/Equipment_Extract/"]` | Exactly this path |
| `RuntimeOverrides.KTY_PATH` | Absolute path to the KTY folder | Must contain `KA-*.md` files |
| `RuntimeOverrides.OUTPUT_ROOT` | `{DOMAIN_ROOT}/_Aggregation/Equipment_Extract/` | Must already exist |
| `RuntimeOverrides.EQUIPMENT_TYPES` | Semicolon-delimited target module type list | Matching is case-insensitive |

#### Optional fields

| Field | Value | Notes |
|---|---|---|
| `RuntimeOverrides.EQUIPMENT_EXTRACT_PATH` | Absolute path to `{KTY_ID}_Equipment_Extract.md` | When provided, enriches `Subcomponents` column |

#### TaskProfile

`NONE` — this skill runs in generic TASK shell mode without a profile.

#### Recommended CustomInstructions

For format-critical defense-in-depth, orchestrators SHOULD include:

```md
CustomInstructions:
  - "Output CSV must have exactly 17 columns: Equipment_Module_Type, Match_Quality, Equipment_Instance, Equipment_Tag, Quantity_and_Sparing, Description, Capacity_Throughput, Power_Duty, Size_Dimensions, Design_Pressure, Design_Temperature, Fluid_Process_Service, Subcomponents, Key_Costing_Parameters, Source_KTY, Source_KA_Files, Notes"
  - "One row per distinct equipment service (not per tag when identical units share a costing basis)"
  - "Quote fields containing commas or semicolons"
  - "Use TBD for values stated as pending in the source; leave blank for values not addressed"
```

#### Read boundary

The skill reads only:

- `{KTY_PATH}/KA-*.md`
- `{KTY_PATH}/_CONTEXT.md`
- `{KTY_PATH}/_REFERENCES.md`
- `{EQUIPMENT_EXTRACT_PATH}` (when provided)

It must NOT read arbitrary files under `ScopePath`.

#### Write boundary

The skill writes only:

- `{OUTPUT_ROOT}/{KTY_ID}_Equipment_Costing_Extract.csv`

`OUTPUT_ROOT` must already exist. The skill does not create the directory.

#### Notes

- `KTY_ID` is derived at runtime from `_CONTEXT.md` or from the folder name.
- One invocation processes one KTY folder. The orchestrator spawns one TASK per relevant KTY for parallelism.
- Equipment module type matching is case-insensitive. The output normalizes to the casing provided in `EQUIPMENT_TYPES`.
- KTYs with zero matches produce a header-only CSV with no data rows.

## Component: skills/equipment-costing-extract/QA_CHECKS.md

### equipment-costing-extract — QA Checks

Minimum checks for a valid run:

1. `KTY_PATH` exists and contains at least one `KA-*.md` file (or absence is reported as `FAILED_INPUTS`).
2. `OUTPUT_ROOT` exists before the skill writes to it.
3. `EQUIPMENT_TYPES` is non-empty and parseable.
4. Every `KA-*.md` file in the KTY folder was read, or its absence was explicitly reported.
5. The output file `{KTY_ID}_Equipment_Costing_Extract.csv` was written to `OUTPUT_ROOT`.
6. No files in `{KTY_PATH}` were written or modified.

#### CSV schema compliance (required)

The output CSV must satisfy:

| Check | Requirement |
|---|---|
| Column count | Exactly 17 columns |
| Column order | `Equipment_Module_Type`, `Match_Quality`, `Equipment_Instance`, `Equipment_Tag`, `Quantity_and_Sparing`, `Description`, `Capacity_Throughput`, `Power_Duty`, `Size_Dimensions`, `Design_Pressure`, `Design_Temperature`, `Fluid_Process_Service`, `Subcomponents`, `Key_Costing_Parameters`, `Source_KTY`, `Source_KA_Files`, `Notes` |
| Header row | Present as first row |
| Quoting | Fields containing commas, semicolons, or newlines are quoted |

#### Source traceability (required for every extracted row)

Every row in the CSV must satisfy all of the following:

| Check | Requirement |
|---|---|
| KA source cited | The `Source_KA_Files` column names the specific KA file(s) from which values were extracted |
| Equipment exists in source | The equipment item appears in the cited KA file text; no invented items |
| Tag is verbatim | The `Equipment_Tag` value is an exact match from KA source text or Equipment_Extract.md, or `No tag` when unstated in either source. Multiple tags use comma-space delimiter. |
| Parameters are sourced | All non-empty specification columns contain values from KA source text; `TBD` is used for values stated as pending in the source |
| Match quality is classified | `Match_Quality` is one of `Exact`, `Near`, or `Out_of_Scope` |
| Module type is from target list | `Equipment_Module_Type` matches one of the types provided in `EQUIPMENT_TYPES` |
| Out_of_Scope has Description | `Out_of_Scope` rows MUST have a non-blank `Description` stating the scope exclusion basis (e.g., "Excluded from 3-25 scope; shared 4-25 asset per DBM Table 1-8 Item 3") |

A run with untraceable equipment rows or invented parameter values is invalid.

#### Match coverage validation

- Every target module type in `EQUIPMENT_TYPES` should be checked against KTY content. Not every type will produce matches in every KTY — that is expected.
- KTYs with zero matches produce a header-only CSV. This is a valid result.
- The run record must state: (a) which module types produced matches, (b) which did not, and (c) total row count.

#### Null-result validation

KTYs with zero equipment matches must still produce:
- A CSV file with the 17-column header row and no data rows
- A run record stating no matches were found and listing the module types checked

#### Reporting groups

When issues are found during extraction, group them by:

- ambiguous match quality (equipment could map to multiple module types)
- TBD/TBC parameters (values pending detailed engineering)
- scope boundary items (equipment explicitly excluded from DBM scope)
- missing parameter data (KA file mentions equipment but lacks spec detail)
- subcomponent enrichment gaps (Equipment_Extract.md unavailable or incomplete)

#### Success case

A clean run reports:

- `RUN_STATUS=SUCCESS`
- Output file path
- Matched equipment count (integer)
- Module types matched (list)
- Module types with no matches (list)
- KA files read (list)
- No warnings (or explicit statement that none were encountered)

## Component: skills/equipment-costing-extract/SKILL.md

---
name: equipment-costing-extract
description: Extract costing-relevant design basis parameters for equipment matching a target module type list from KA files in a single KTY folder. Use when building equipment costing registers for cost estimation.
compatibility: Chirality TASK in generic shell mode (no profile); reasoning-only extraction.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — equipment-costing-extract

#### Purpose

Extract costing-relevant design basis parameters for equipment items that match a target module type list, operating on one Knowledge Type (KTY) folder at a time. Produces a per-KTY CSV file with matched equipment rows containing capacity, power/duty, size, design conditions, fluid service, subcomponents, and key costing parameters.

This is a reasoning-first extraction skill. It reads KA markdown files and applies matching and extraction logic directly; it does not invoke deterministic tooling during extraction. A companion deterministic tool (`tools/reporting/merge_equipment_costing_csv.py`) is used downstream by the orchestrator to consolidate per-KTY outputs.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

#### Typical dispatcher

- `WORKING_ITEMS` (Type 1 persona) dispatches one TASK per relevant KTY for parallel extraction across a domain.

#### Inputs

##### Required

- `ScopePath` — `{DOMAIN_ROOT}` (top-level domain execution root)
- `AllowedWriteTargets` — `["{DOMAIN_ROOT}/_Aggregation/Equipment_Extract/"]`
- `RuntimeOverrides.KTY_PATH` — absolute path to the Knowledge Type folder to extract from
- `RuntimeOverrides.OUTPUT_ROOT` — `{DOMAIN_ROOT}/_Aggregation/Equipment_Extract/`
- `RuntimeOverrides.EQUIPMENT_TYPES` — semicolon-delimited list of target equipment module types to match against

##### Optional

- `RuntimeOverrides.EQUIPMENT_EXTRACT_PATH` — absolute path to the existing `{KTY_ID}_Equipment_Extract.md` file for subcomponent enrichment. When provided, the skill reads this file to populate the `Subcomponents` column for modular/packaged equipment.

##### Derived at runtime

- `KTY_ID` — extracted from `{KTY_PATH}/_CONTEXT.md` or inferred from folder name

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `KTY_PATH` | Absolute path to the KTY folder | **Required** | Valid directory path containing `KA-*.md` files |
| `OUTPUT_ROOT` | Output directory for CSV files | **Required** | Must already exist |
| `EQUIPMENT_TYPES` | Target module types to match | **Required** | Semicolon-delimited list (e.g., `"COMPRESSOR MODULE;SEPARATOR MODULE;STORAGE TANK"`) |
| `EQUIPMENT_EXTRACT_PATH` | Path to existing Equipment_Extract.md | `none` | Valid file path or omitted |

#### Read boundary

Reads are limited to:

- `{RuntimeOverrides.KTY_PATH}/KA-*.md` — all Knowledge Artifact files
- `{RuntimeOverrides.KTY_PATH}/_CONTEXT.md` — KTY identity metadata
- `{RuntimeOverrides.KTY_PATH}/_REFERENCES.md` — reference context
- `{RuntimeOverrides.EQUIPMENT_EXTRACT_PATH}` — existing equipment register (when provided)

The skill must NOT read arbitrary files under `ScopePath`. It does not read `Scoping.md`, `_STATUS.md`, `_MEMORY.md`, or files outside the KTY folder (except the optional Equipment_Extract.md).

#### Write boundary

Writes are limited to:

- `{RuntimeOverrides.OUTPUT_ROOT}/{KTY_ID}_Equipment_Costing_Extract.csv`

`OUTPUT_ROOT` must already exist. The skill does not create the directory.

#### Tool usage

- No deterministic tools during extraction. This is a reasoning-first skill.
- The `allowed-tools` frontmatter field is intentionally omitted.
- Downstream consolidation uses `tools/reporting/merge_equipment_costing_csv.py` (invoked by the orchestrator, not by this skill).

Disallowed behavior:

- No writing outside `OUTPUT_ROOT`
- No modification of any file in `KTY_PATH`
- No widening scope beyond the designated KTY folder

#### Method

##### Step 0 — Preconditions

1. Validate `KTY_PATH` exists and is a directory. If not: report `RUN_STATUS=FAILED_INPUTS`.
2. Validate `OUTPUT_ROOT` exists. If not: report `RUN_STATUS=FAILED_INPUTS`.
3. Parse `EQUIPMENT_TYPES` into a list of target module types. If empty: report `RUN_STATUS=FAILED_INPUTS`.

##### Step 1 — Read KTY context

1. Read `{KTY_PATH}/_CONTEXT.md` (best-effort).
2. Extract: KTY ID, KTY name, parent Category ID and name.
3. If `_CONTEXT.md` is missing or ambiguous, fall back to folder name.

##### Step 2 — Read reference context

1. Read `{KTY_PATH}/_REFERENCES.md` (best-effort) for source document context.

##### Step 3 — Enumerate and read KA files

1. List all `KA-*.md` files in the KTY folder.
2. Read each KA file in order by KA number.

##### Step 4 — Match equipment to target module types

For each KA file, identify equipment items whose function or type matches or near-matches one of the target module types from `EQUIPMENT_TYPES`.

**Match quality rules:**

| Quality | Criteria |
|---|---|
| `Exact` | Equipment name/type directly corresponds to a target module type (e.g., "Inlet Compressor" matches "COMPRESSOR MODULE") |
| `Near` | Equipment serves a similar function, is a recognizable variant, or has its specification explicitly stated as assumed from another item (e.g., "Condensate Dehydrator Reflux Accumulator" near-matches "ACCUMULATOR MODULE"; truck unloading pump specified as "assumed equivalent to loading pump" is Near to PROCESS PUMP MODULE) |
| `Out_of_Scope` | Equipment is explicitly excluded from DBM scope (e.g., shared asset per exclusion table). The `Description` column MUST still be populated with a brief scope exclusion note (e.g., "Excluded from 3-25 scope; shared 4-25 asset per DBM Table 1-8 Item 3"). Other spec columns may be left blank. |

Items with no match to any target type are NOT included in the output.

##### Step 5 — Extract costing parameters for matched items

For each matched equipment item, extract from the KA file(s):

| Column | Extraction guidance |
|---|---|
| `Equipment_Module_Type` | The target module type this item matches (from `EQUIPMENT_TYPES`) |
| `Match_Quality` | `Exact`, `Near`, or `Out_of_Scope` |
| `Equipment_Instance` | Specific equipment name as stated in the KA text |
| `Equipment_Tag` | Exact tag from KA source text or Equipment_Extract.md; `No tag` if unstated in either source. When one row covers multiple identical units, list tags comma-space delimited (e.g., `V-1600-2, V-1700-2`) |
| `Quantity_and_Sparing` | Sparing philosophy (e.g., "2x50%", "1x100% with bypass", "3x50% lead-lag") |
| `Description` | Brief functional description (1-2 sentences) |
| `Capacity_Throughput` | Primary capacity metric with units stated inline (e.g., "80 MMSCFD total / 40 per unit", "3800 bbl", "103 m³/h"). Units vary by equipment type — always include them. |
| `Power_Duty` | Motor power or thermal duty (e.g., "5000 HP", "25 MMBTU/h", "7327 kW") |
| `Size_Dimensions` | Physical dimensions or volume (e.g., "9 ft ID x 40 ft S/S", "200 BBL") |
| `Design_Pressure` | Design/MAWP pressure with units (e.g., "4963 kPag", "950 psig") |
| `Design_Temperature` | Design temperature range (e.g., "4-48 C / 40-120 F") |
| `Fluid_Process_Service` | Service description including sour/sweet, composition notes (e.g., "Sour gas H2S 0.296 mol%") |
| `Subcomponents` | Semicolon-delimited list of major sub-items for modular equipment; `N/A` for standalone items |
| `Key_Costing_Parameters` | Free text: material spec, MAWP, internal coating, sour service rating, area classification, modular/building-enclosed, CSA/ASME code, VFD, etc. |
| `Source_KTY` | KTY ID (e.g., `KTY-04-05`) |
| `Source_KA_Files` | Comma-delimited list of KA files used (e.g., `KA-01, KA-02, KA-04`) |
| `Notes` | Match quality notes, TBD counts, scope notes, conflicts |

##### Step 6 — Enrich subcomponents (optional)

If `EQUIPMENT_EXTRACT_PATH` is provided and the file exists:
1. Read the Equipment_Extract.md file.
2. For modular/packaged equipment, extract the subcomponent list from the equipment table.
3. Populate the `Subcomponents` column with a semicolon-delimited list of sub-items.

##### Step 7 — Write output CSV

Write `{OUTPUT_ROOT}/{KTY_ID}_Equipment_Costing_Extract.csv` with:
1. Header row with all 17 columns
2. One row per matched equipment item, following this row granularity rule:
   - **Merge** identical units that share a costing basis into one row with quantity in `Quantity_and_Sparing` (e.g., "2x50% Inlet Compressors" = one row)
   - **Split** into separate rows when units serve distinct locations or services even if the same equipment type (e.g., "HP Flare KO Drum — Compressor Station area" and "HP Flare KO Drum — Liquids Hub area" = two rows because they serve different areas with different header configurations)
3. CSV quoting: quote any field containing commas, semicolons, or newlines

For KTYs with zero matches: write a CSV with header only and no data rows. Report in the run record that no matches were found.

#### Outputs

- `{KTY_ID}_Equipment_Costing_Extract.csv` in `OUTPUT_ROOT`

#### Non-negotiable constraints

- **Read-only on KTY folders.** Never modify any file in `{KTY_PATH}`.
- **No invention.** Only extract parameters explicitly stated in KA files. Use `TBD` for values mentioned as pending.
- **Exact tags.** Equipment tags must be verbatim from KA source text or Equipment_Extract.md. Multiple tags for identical units in one row use comma-space delimiter.
- **Complete KA coverage.** Every `KA-*.md` in the folder must be read.
- **Match-only output.** Only include equipment that matches a target module type. Do not produce rows for unmatched equipment.
- **Source traceability.** Every row must cite specific KA source files.
- **CSV schema compliance.** Output must have exactly 17 columns in the specified order.

#### QA expectations

- All KA files in the folder were read (or absence reported).
- Every CSV row cites specific KA source files.
- No equipment rows appear for items not in the KA source text.
- Equipment tags are verbatim from source.
- Match quality is correctly classified (Exact/Near/Out_of_Scope).
- CSV has exactly 17 columns with correct headers.
- No files in `{KTY_PATH}` were written or modified.

#### Downstream consumer

Per-KTY CSV outputs are consolidated by `tools/reporting/merge_equipment_costing_csv.py` into a single `Equipment_Costing_Extract.csv`. The orchestrator (WORKING_ITEMS) invokes the merge tool after all per-KTY TASK runs complete.

## Component: skills/equipment-costing-extract/TOOL_POLICY.md

### equipment-costing-extract — Tool Policy

#### Preferred tool order

Reasoning-first: this skill is LLM-driven; no deterministic tool ordering applies during extraction. The agent reads KA markdown files within a single Knowledge Type folder and applies matching and extraction logic directly, producing a per-KTY CSV with costing-relevant design parameters.

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- None — no TASK-enforced deterministic allowlist (the `allowed-tools` frontmatter field is intentionally omitted)

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None — no operational helpers declared during extraction (SKILL.md states: "No deterministic tools during extraction. This is a reasoning-first skill.")

**Downstream note:** The orchestrator (not this skill) invokes `tools/reporting/merge_equipment_costing_csv.py` after all per-KTY extractions complete. This tool is not part of the skill's execution scope.

#### Expected use of reasoning

This is a reasoning-first extraction skill. The agent:

1. Reads `_CONTEXT.md` and `_REFERENCES.md` for KTY identity and source context.
2. Reads all `KA-*.md` files in the KTY folder in order.
3. Applies matching logic to identify equipment items corresponding to target module types from `EQUIPMENT_TYPES`.
4. Extracts costing-relevant parameters (capacity, power/duty, size, design pressure, temperature, fluid service, subcomponents, key costing parameters) from markdown tables and prose.
5. Optionally reads an existing `Equipment_Extract.md` for subcomponent enrichment.
6. Assembles and writes the per-KTY CSV output.

Reasoning governs every phase: preconditions, context read, KA enumeration, equipment matching, parameter extraction, CSV composition, and output file writing.

#### Disallowed use

- No writing outside `OUTPUT_ROOT`.
- No modification of any file in `KTY_PATH`.
- No widening scope beyond the designated KTY folder (plus optional Equipment_Extract.md).
- No hidden reliance on tools outside the declared list.
- No invention of parameter values not stated in KA source text.

#### Write boundary

Writes are limited to:

- `{RuntimeOverrides.OUTPUT_ROOT}/{KTY_ID}_Equipment_Costing_Extract.csv`

`OUTPUT_ROOT` must already exist. The skill does not create the directory. No files in `{KTY_PATH}` may be written or modified.
