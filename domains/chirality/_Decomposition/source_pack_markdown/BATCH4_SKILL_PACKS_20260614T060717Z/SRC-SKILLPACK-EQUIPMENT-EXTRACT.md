# Source Pack: Skill pack: equipment-extract

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/equipment-extract/BRIEF_SCHEMA.md

### equipment-extract — Brief Schema

Use this skill with a generic TASK shell (no profile) like this:

```md
PURPOSE: Extract equipment items from KTY-04-01 KA files
RequestedBy: ORCHESTRATOR

ScopePath: {EXECUTION_ROOT}
TaskSkill: equipment-extract

AllowedWriteTargets:
  - "{EXECUTION_ROOT}/_Aggregation/Equipment_Extract/"

RuntimeOverrides:
  KTY_PATH: /abs/path/to/KTY-04-01_Gas_Dehydration
  OUTPUT_ROOT: "{EXECUTION_ROOT}/_Aggregation/Equipment_Extract/"
```

#### Required fields

| Field | Value | Notes |
|---|---|---|
| `ScopePath` | `{EXECUTION_ROOT}` | Top-level execution root |
| `TaskSkill` | `equipment-extract` | Must match skill folder name |
| `AllowedWriteTargets` | `["{EXECUTION_ROOT}/_Aggregation/Equipment_Extract/"]` | Exactly this path |
| `RuntimeOverrides.KTY_PATH` | Absolute path to the KTY folder | Must contain `KA-*.md` files |
| `RuntimeOverrides.OUTPUT_ROOT` | `{EXECUTION_ROOT}/_Aggregation/Equipment_Extract/` | Must already exist |

#### Optional fields

None. This skill has no optional brief fields.

#### TaskProfile

`NONE` — this skill runs in generic TASK shell mode without a profile.

#### Read boundary

The skill reads only:

- `{KTY_PATH}/KA-*.md`
- `{KTY_PATH}/_CONTEXT.md`
- `{KTY_PATH}/_REFERENCES.md`

It must NOT read arbitrary files under `ScopePath`.

#### Write boundary

The skill writes only:

- `{OUTPUT_ROOT}/{KTY_ID}_Equipment_Extract.md`

`OUTPUT_ROOT` must already exist. The skill does not create the directory.

#### Notes

- `KTY_ID` is derived at runtime from `_CONTEXT.md` or from the folder name when `_CONTEXT.md` is unavailable.
- One invocation processes one KTY folder. ORCHESTRATOR spawns one task per in-scope KTY for parallelism.
- The brief does not include `AllowedTools` because this is a reasoning-only extraction skill with no deterministic tool dependencies.

## Component: skills/equipment-extract/QA_CHECKS.md

### equipment-extract — QA Checks

Minimum checks for a valid run:

1. `KTY_PATH` exists and contains at least one `KA-*.md` file (or absence is reported as `FAILED_INPUTS`).
2. `OUTPUT_ROOT` exists before the skill writes to it.
3. Every `KA-*.md` file in the KTY folder was read, or its absence was explicitly reported.
4. The output file `{KTY_ID}_Equipment_Extract.md` was written to `OUTPUT_ROOT`.
5. The output file contains all required sections: title, metadata block, Equipment Table, Package Notes, equipment count footer.
6. No files in `{KTY_PATH}` were written or modified.

#### Source traceability (required for every extracted item)

Every row in the Equipment Table must satisfy all of the following:

| Check | Requirement |
|---|---|
| KA source cited | The `KA Source` column names the specific `KA-*.md` file from which the item was extracted |
| Equipment exists in source | The equipment item appears in the cited KA file text; no invented items |
| Tag is verbatim | The `Equipment Tag` value is an exact match from the source text, or `No tag` when the source does not state one |
| Package assignment sourced | `Package Name` is a formal name from the source, a contextual name with `(indicated)` suffix, or `N/A` |

A run with even one untraceable equipment row is invalid.

#### Null-result validation

KTYs with zero physical equipment must still produce an output file containing:

- An empty Equipment Table (or single explanatory row)
- Package Notes explaining why no equipment was found
- An equipment count footer reading `0` with parenthetical explanation

#### Reporting groups

When issues are found during extraction, group them by:

- missing KA files (listed in folder but not on disk, or vice versa)
- ambiguous tags (tag partially stated or conflicting across KAs)
- scope boundary items (equipment where ownership is unclear)
- TBD items (equipment referenced as future or placeholder)
- package assignment uncertainty (formal vs. indicated vs. absent)

#### Success case

A clean run reports:

- `RUN_STATUS=OK`
- Output file path
- Equipment count (integer)
- List of KA files read
- No warnings (or explicit statement that none were encountered)

## Component: skills/equipment-extract/SKILL.md

---
name: equipment-extract
description: Extract discrete physical equipment items from Knowledge Artifact files within a single DOMAIN Knowledge Type folder. Use when building per-KTY equipment registers from KA production documents.
compatibility: Chirality TASK in generic shell mode (no profile); reasoning-only extraction.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — equipment-extract

#### Purpose

Extract every discrete physical equipment item mentioned in the KA files of a single Knowledge Type folder and produce a normalized, source-traceable equipment register for that KTY.

This is a reasoning-first extraction skill. It reads KA markdown files and applies extraction logic directly; it does not invoke deterministic tooling.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

#### Inputs

##### Required

- `ScopePath` — `{EXECUTION_ROOT}`
- `AllowedWriteTargets` — `["{EXECUTION_ROOT}/_Aggregation/Equipment_Extract/"]`
- `RuntimeOverrides.KTY_PATH` — absolute path to the Knowledge Type folder to extract from
- `RuntimeOverrides.OUTPUT_ROOT` — `{EXECUTION_ROOT}/_Aggregation/Equipment_Extract/`

##### Derived at runtime

- `KTY_ID` — extracted from `{KTY_PATH}/_CONTEXT.md` or inferred from folder name

##### Optional

- None

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `KTY_PATH` | Absolute path to the KTY folder to extract from | **Required** | Valid directory path containing `KA-*.md` files |
| `OUTPUT_ROOT` | Output directory for extract files | **Required** | Must already exist; the skill does not create it |

#### Read boundary

Reads are limited to:

- `{RuntimeOverrides.KTY_PATH}/KA-*.md` — all Knowledge Artifact files
- `{RuntimeOverrides.KTY_PATH}/_CONTEXT.md` — KTY identity metadata
- `{RuntimeOverrides.KTY_PATH}/_REFERENCES.md` — reference context

The skill must NOT read arbitrary files under `ScopePath`. It does not read `Scoping.md`, `_STATUS.md`, or files outside the KTY folder.

#### Write boundary

Writes are limited to:

- `{RuntimeOverrides.OUTPUT_ROOT}/{KTY_ID}_Equipment_Extract.md`

`OUTPUT_ROOT` must already exist. The skill does not create the directory.

#### Tool usage

- No deterministic tools. This is a reasoning-first extraction skill.
- The `allowed-tools` frontmatter field is intentionally omitted.

Disallowed behavior:

- No writing outside `OUTPUT_ROOT`
- No modification of any file in `KTY_PATH`
- No widening scope beyond the designated KTY folder

#### Method

##### Step 0 — Preconditions

1. Validate `KTY_PATH` exists and is a directory. If not: report `RUN_STATUS=FAILED_INPUTS`.
2. Validate `OUTPUT_ROOT` exists. If not: report `RUN_STATUS=FAILED_INPUTS`.

##### Step 1 — Read KTY context

1. Read `{KTY_PATH}/_CONTEXT.md` (best-effort).
2. Extract: KTY ID, KTY name, parent Category ID and name.
3. If `_CONTEXT.md` is missing or ambiguous, fall back to folder name. Record the fallback in Package Notes.

##### Step 2 — Enumerate and order KA files

1. List all `KA-*.md` files in the KTY folder.
2. Build the read list ordered by KA number.

##### Step 3 — Extract equipment from each KA

For each KA file, extract every discrete physical equipment item:

**In scope (extract these):**

- Vessels, separators, drums, columns, towers
- Compressors, pumps, blowers, fans
- Heat exchangers, coolers, heaters, reboilers, condensers
- Tanks, storage vessels
- Filters, strainers, coalescers, scrubbers
- Control valves, PSVs, ESDVs, shutdown valves, blowdown valves
- Instruments, meters, analyzers (when named as discrete devices)
- Motors and drivers (when described as discrete tagged/named equipment)
- Any other physically instantiated, discrete named/tagged device

**Out of scope (do not extract):**

- Virtual machines, software instances
- Buildings or structures (but include equipment housed within them)
- Documents, procedures, specifications
- Non-physical items (data points, software licenses, network addresses)

For each item, record:

| Field | Rule |
|---|---|
| Equipment Tag | Exact tag from source text; `No tag` if unstated |
| Equipment Name | Descriptive name as stated, with key attributes in parentheses |
| Package Name | Formal name if stated; contextual name with `(indicated)` if implied; `N/A` if absent |
| Notes | Sparing, TBDs, conflicts, scope notes |
| KA Source | The KA file from which the item was extracted |

##### Step 4 — Assemble equipment table

Combine all per-KA items into one ordered table with columns:

`#` | `CAT` | `KTY` | `KA Source` | `Equipment Tag` | `Equipment Name` | `Package Name` | `Notes`

Rows ordered by KA source (read-list order), then by order of appearance within each KA. Sequential row numbers starting at 1.

##### Step 5 — Write Package Notes

Contextual observations about:

- Formal vs. implied package/module assignments
- Notable groupings or splits
- Scope boundary ambiguities
- Items excluded with rationale
- Active conflicts or TBDs affecting equipment identification
- Null-result explanation for KTYs with zero physical equipment

##### Step 6 — Write output file

Write `{OUTPUT_ROOT}/{KTY_ID}_Equipment_Extract.md` containing, in order:

1. **Title**: `# Equipment Extract — {KTY_ID} {KTY Name}`
2. **Metadata block**: Category, Knowledge Type, Source KA files, Extraction date
3. **Equipment Table**: the assembled markdown table
4. **Package Notes**: the bulleted observations
5. **Equipment count footer**: `**{KTY_ID} Equipment Count: {N}**`

For KTYs with zero physical equipment: the table is empty or contains a single explanatory row; the count footer reads `0` with a parenthetical explanation; an informational inventory (e.g., virtual machines) may be included for traceability, clearly marked as excluded.

#### Outputs

- `{KTY_ID}_Equipment_Extract.md` in `OUTPUT_ROOT`

#### Non-negotiable constraints

- **Read-only on KTY folders.** Never modify any file in `{KTY_PATH}`.
- **No invention.** Only extract equipment explicitly mentioned in KA files.
- **Exact tags.** Equipment tags must be verbatim from source text, never inferred or constructed.
- **Sourced package assignments.** Package names come from KA text, are marked `(indicated)` when contextually implied, or are `N/A`.
- **Complete coverage.** Every `KA-*.md` in the folder must be read. Missing files must be reported.
- **Null results documented.** KTYs with zero physical equipment still produce an extract file with explanation.
- **Source traceability.** Every table row must cite the specific KA file from which it was extracted.

#### QA expectations

- All KA files in the folder were read (or absence reported).
- Every equipment table row cites a specific KA source file.
- No equipment items appear that are not in the KA source text.
- Equipment tags are verbatim from source.
- Package assignments are sourced, marked `(indicated)`, or `N/A`.
- Output file contains all required sections: title, metadata, table, Package Notes, count footer.
- No files in `{KTY_PATH}` were written or modified.
- Null-result KTYs have an extract file with explanation.

#### Downstream consumer

This skill does not produce the consolidated `Equipment_Master_List.csv`. That is a separate assembly step that concatenates per-KTY extract tables after all extractions are complete.

## Component: skills/equipment-extract/TOOL_POLICY.md

### equipment-extract — Tool Policy

#### Preferred tool order

Reasoning-first: this skill is LLM-driven; no deterministic tool ordering applies. The agent reads KA markdown files within a single Knowledge Type folder and applies extraction logic directly, producing a normalized, source-traceable equipment register.

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- None — no TASK-enforced deterministic allowlist (the `allowed-tools` frontmatter field is intentionally omitted)

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None — no operational helpers declared (SKILL.md states: "No deterministic tools. This is a reasoning-first extraction skill")

#### Expected use of reasoning

This is a reasoning-first extraction skill. The agent reads `_CONTEXT.md`, `_REFERENCES.md`, and all `KA-*.md` files in the KTY folder, then applies extraction logic directly to identify discrete physical equipment items per the in-scope / out-of-scope rules, records the required fields (Equipment Tag, Equipment Name, Package Name, Notes, KA Source), assembles the ordered equipment table, writes Package Notes, and produces the final per-KTY extract file. Reasoning governs every phase: preconditions, KTY context read, KA enumeration and ordering, per-KA equipment extraction, table assembly, Package Notes, and output file composition.

#### Disallowed use

- No writing outside `OUTPUT_ROOT`.
- No modification of any file in `KTY_PATH`.
- No widening scope beyond the designated KTY folder.
- No hidden reliance on tools outside the declared list unless the human expands AllowedTools. No writes outside declared scope.

#### Write boundary

Writes are limited to:

- `{RuntimeOverrides.OUTPUT_ROOT}/{KTY_ID}_Equipment_Extract.md`

`OUTPUT_ROOT` must already exist. The skill does not create the directory. No files in `{KTY_PATH}` may be written or modified.
