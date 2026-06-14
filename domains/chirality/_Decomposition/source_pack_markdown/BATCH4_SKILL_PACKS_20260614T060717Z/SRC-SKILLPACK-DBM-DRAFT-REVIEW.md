# Source Pack: Skill pack: dbm-draft-review

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/dbm-draft-review/BRIEF_SCHEMA.md

### BRIEF SCHEMA - dbm-draft-review

This file defines the INIT-TASK dispatch contract for `TASK + dbm-draft-review`.

#### Purpose

Use this skill to review a human-prepared draft DBM against the governed knowledge base. The skill builds a review substrate using deterministic tools, then uses agent judgment to prepare candidate findings for human disposition via REVIEW.

#### Scope model

- `ScopePath` should be the review output directory.
- `AllowedWriteTargets` must name exactly the 6 output files under REVIEW_OUTPUT_DIR.
- The brief must not grant write access to KTY folders, decomposition truth, publication planning artifacts, or the draft DBM file.

#### Required brief fields

| Field | Type | Meaning | Example |
|---|---|---|---|
| `PURPOSE` | string | Why review is being run | `Review colleague's draft DBM against governed Deepcut knowledge base.` |
| `ScopePath` | path | Review output directory | `/repo/.../_Publication/DBM/_Review/REVIEW-20260422-1400/` |
| `TaskSkill` | string | Must equal `dbm-draft-review` | `dbm-draft-review` |
| `AllowedWriteTargets` | list[path] | Exactly the 6 output files | `[/.../Evidence_Bundle_Summary.md, /.../Section_Coverage.csv, /.../Draft_Claims.csv, /.../Body_Thinness.csv, /.../TBD_Inventory.csv, /.../Candidate_Findings.csv]` |
| `RuntimeOverrides.DRAFT_DBM_PATH` | path | The draft document to review | `/repo/.../colleague_draft_dbm.md` |
| `RuntimeOverrides.REVIEW_OUTPUT_DIR` | path | Output directory for evidence bundle | `/repo/.../_Publication/DBM/_Review/REVIEW-20260422-1400/` |
| `RuntimeOverrides.DOMAIN_ROOT` | path | DOMAIN decomposition root | `/repo/.../West_Doe_Deepcut_DBM/` |
| `ExpectedOutputs` | list[path] | All 6 outputs | `[/.../Evidence_Bundle_Summary.md, /.../Section_Coverage.csv, /.../Draft_Claims.csv, /.../Body_Thinness.csv, /.../TBD_Inventory.csv, /.../Candidate_Findings.csv]` |

#### Optional brief fields

| Field | Type | Meaning | Example |
|---|---|---|---|
| `RuntimeOverrides.PUBLICATION_SCHEMA_PATH` | path | Approved publication schema | `/.../_Planning/Publication_Schema.md` |
| `RuntimeOverrides.SECTION_MAP_PATH` | path | Approved section map | `/.../_Planning/Section_Map.csv` |
| `RuntimeOverrides.PUBLICATION_RULES_PATH` | path | Approved publication rules | `/.../_Planning/Publication_Rules.md` |
| `RuntimeOverrides.SUPERSESSION_MAP_PATH` | path | Active supersession map | `/.../SCA-006/.../Supersession_Map.csv` |
| `RuntimeOverrides.SECTION_CONTEXT_ROOT` | path | Section context packets | `/.../_Planning/section-context/` |
| `RuntimeOverrides.EXISTING_PUBLISHED_DBM_PATH` | path | Previous published DBM for comparison | `/.../package/RUN-.../Rewritten_DBM.md` |
| `CustomInstructions` | string | Run-specific emphasis | `Focus on Utilities section (SEC-07) instrument air content.` |

#### Runtime-override guidance

- When `PUBLICATION_SCHEMA_PATH` is missing, section coverage scanning is skipped and `EvidenceBundleStatus` is `PARTIAL`.
- When `SECTION_MAP_PATH` is missing, body thinness density ratios and governed-truth KA comparison are degraded. The bundle is `PARTIAL`.
- When `SUPERSESSION_MAP_PATH` is missing, supersession compliance is not assessed. The bundle notes this as a dimension not assessed.
- The skill does not require all optional inputs to produce useful findings. It degrades honestly — recording what was and was not assessed.

#### Recommended CustomInstructions content

For format-critical defense-in-depth, orchestrators should include:

```
Emit all 6 evidence bundle files. Set Origin = AGENT_CHECK on every Candidate_Findings.csv row.
Use only controlled enum values for FindingType and Severity.
If governed inputs are missing, set EvidenceBundleStatus = PARTIAL and list affected dimensions.
```

#### Example INIT-TASK brief

```md
PURPOSE: Review colleague's draft DBM against governed Deepcut knowledge base.
ScopePath: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/
TaskSkill: dbm-draft-review
AllowedWriteTargets:
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Evidence_Bundle_Summary.md
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Section_Coverage.csv
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Draft_Claims.csv
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Body_Thinness.csv
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/TBD_Inventory.csv
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Candidate_Findings.csv
RuntimeOverrides:
  DRAFT_DBM_PATH: /repo/domains/West_Doe_Deepcut_DBM/_Sources/colleague_draft_dbm.md
  REVIEW_OUTPUT_DIR: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/
  DOMAIN_ROOT: /repo/domains/West_Doe_Deepcut_DBM/
  PUBLICATION_SCHEMA_PATH: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Planning/Publication_Schema.md
  SECTION_MAP_PATH: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Planning/Section_Map.csv
  PUBLICATION_RULES_PATH: /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Planning/Publication_Rules.md
ExpectedOutputs:
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Evidence_Bundle_Summary.md
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Section_Coverage.csv
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Draft_Claims.csv
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Body_Thinness.csv
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/TBD_Inventory.csv
  - /repo/domains/West_Doe_Deepcut_DBM/_Publication/DBM/_Review/REVIEW-20260422-1400/Candidate_Findings.csv
```

## Component: skills/dbm-draft-review/QA_CHECKS.md

### QA CHECKS - dbm-draft-review

#### Minimum output validity checks

The run is valid only when all of the following are true:

1. All 6 required outputs exist under REVIEW_OUTPUT_DIR:
   - `Evidence_Bundle_Summary.md`
   - `Section_Coverage.csv`
   - `Draft_Claims.csv`
   - `Body_Thinness.csv`
   - `TBD_Inventory.csv`
   - `Candidate_Findings.csv`
2. All writes stayed inside REVIEW_OUTPUT_DIR.
3. No draft, knowledge base, publication, or governed-pointer files were modified.
4. `Evidence_Bundle_Summary.md` contains all required H2 headings.
5. `Evidence_Bundle_Summary.md` contains both `EvidenceBundleStatus` and `ReviewStatus` values from their respective controlled enums.
6. `Candidate_Findings.csv` uses only controlled enum values for `FindingType` (`INCORRECT`, `UNSUPPORTED`, `MISSING`, `FLATTENED`, `OUTDATED`, `INCOMPLETE`).
7. `Candidate_Findings.csv` uses only controlled enum values for `Severity` (`HIGH`, `MEDIUM`, `LOW`, `ADVISORY`).
8. Every row in `Candidate_Findings.csv` has `Origin = AGENT_CHECK`.
9. Every row in `Candidate_Findings.csv` has a non-empty `Explanation` and `EvidenceSource`.
10. `Section_Coverage.csv` has one row per expected section from the schema/section-map (when provided).

#### Required Candidate_Findings.csv schema

Required columns (in order):

- `FindingID` — sequential `F-001`, `F-002`, ...
- `FindingType` — controlled enum: `INCORRECT`, `UNSUPPORTED`, `MISSING`, `FLATTENED`, `OUTDATED`, `INCOMPLETE`
- `Severity` — controlled enum: `HIGH`, `MEDIUM`, `LOW`, `ADVISORY`
- `Origin` — `AGENT_CHECK` (required for REVIEW agent compatibility)
- `DraftLocation` — section heading or identifiable draft location
- `DraftLineNumber` — 1-based line number in draft (0 if not applicable)
- `DraftText` — relevant draft text excerpt (truncated to 200 chars)
- `GovernedTruthRef` — path to governing KA artifact or resource
- `GovernedTruthValue` — expected value from governed truth
- `SectionID` — section identifier (e.g., `SEC-07`)
- `KTYRef` — knowledge type reference (e.g., `KTY-05-02`)
- `KARef` — knowledge artifact reference (e.g., `KA-01`)
- `SupersessionRef` — supersession map reference (empty if not applicable)
- `Explanation` — agent rationale for the finding
- `EvidenceSource` — traces to substrate row (e.g., `Section_Coverage.csv:row-3`) or `AGENT_REVIEW:<description>`

#### Required Section_Coverage.csv schema

- `SectionID`
- `SectionTitle`
- `SectionType`
- `SectionOrder`
- `CoverageStatus` — `COVERED`, `PARTIAL`, `MISSING`, `EXTRA`
- `DraftHeading`
- `DraftLineNumber`
- `AuthoritySource` — `SECTION_MAP` or `SCHEMA_ONLY`

#### Required Draft_Claims.csv schema

- `ClaimID` — sequential `C-001`, `C-002`, ...
- `SectionHeading`
- `DraftLineNumber`
- `RawText`
- `ExtractedValue`
- `Unit`
- `ContextType` — `TABLE_CELL`, `PROSE_VALUE`, `CONFIGURATION`, `TBD_VALUE`
- `NearestTerm`

#### Required Body_Thinness.csv schema

- `SectionID`
- `SectionHeading`
- `DraftLineNumber`
- `TotalLines`
- `NonBlankLines`
- `TableRows`
- `HeadingCount`
- `MappedPrimaryKAs`
- `MappedSupportingKAs`
- `DensityRatio`
- `ExpectedTableClasses`
- `FoundTableCount`
- `Signals`

#### Required TBD_Inventory.csv schema

- `MarkerID` — sequential `M-001`, `M-002`, ...
- `MarkerType` — `TBD`, `TBC`, `ASSUMPTION`
- `DraftLineNumber`
- `DraftContext` — full line text, truncated to 200 chars
- `NearestSectionID`
- `KBResolutionStatus` — `RESOLVED`, `UNRESOLVED`, `NOT_IN_KB`, `NO_KB_PROVIDED`
- `KBResolutionRef`
- `Notes`

#### Required Evidence_Bundle_Summary.md structure

Required H2 headings (in order):

1. `## Bundle Status`
2. `## Input Provenance`
3. `## Tool Run Results`
4. `## Review Dimensions`
5. `## Section Coverage Summary`
6. `## Body Adequacy Observations`
7. `## TBD and Open-Item Assessment`
8. `## Accuracy and Completeness Assessment`
9. `## Supersession Compliance`
10. `## Recommendations`

#### Failure reporting expectations

Use `FAILED_INPUTS` when:
- `DRAFT_DBM_PATH` is missing or unreadable
- `REVIEW_OUTPUT_DIR` cannot be created or falls outside allowed scope
- `DOMAIN_ROOT` does not exist

Use `FAILED` when:
- Required outputs cannot be written despite valid inputs
- A tool exits with code 1 (fatal error) and cannot be skipped

Do NOT use `FAILED` for missing optional governed inputs — use `EvidenceBundleStatus = PARTIAL` instead.

## Component: skills/dbm-draft-review/SKILL.md

---
name: dbm-draft-review
description: Review a human-prepared draft DBM against the governed knowledge base — build review substrate, prepare candidate findings for human disposition.
compatibility: Chirality TASK; dispatched by WORKING_ITEMS or ORCHESTRATOR
allowed-tools: python3 tools/review/scan_section_coverage.py:*, python3 tools/review/extract_claims.py:*, python3 tools/review/scan_tbd_markers.py:*, python3 tools/review/check_body_thinness.py:*
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL - dbm-draft-review

#### Purpose

Review a human-prepared draft DBM document against the governed knowledge base (decomposed KTY/KA artifacts, accepted SCA/supersession state, frozen publication planning artifacts). Build a structured evidence bundle using deterministic substrate tools, then use agent judgment to prepare candidate findings for human disposition via the REVIEW agent.

This skill is a reviewer only. It does not modify the draft, the knowledge base, publication planning artifacts, or governed pointers.

The evidence bundle is not a quality gate. Hard gates are limited to process validity (inputs exist, tools ran, schemas valid, provenance present). Engineering judgment about materiality, adequacy, and significance stays with the reviewing agent and human.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

Typical dispatchers: `WORKING_ITEMS` for interactive human-draft review sessions. `ORCHESTRATOR` for batch review.

#### Inputs

##### Required

- `DRAFT_DBM_PATH` — path to the draft DBM document (markdown)
- `REVIEW_OUTPUT_DIR` — output directory for the evidence bundle
- `DOMAIN_ROOT` — absolute path to the DOMAIN root (e.g., `West_Doe_Deepcut_DBM`)

##### Optional (governed inputs — when unavailable, bundle status is PARTIAL)

- `PUBLICATION_SCHEMA_PATH` — approved Publication_Schema.md
- `SECTION_MAP_PATH` — approved Section_Map.csv
- `PUBLICATION_RULES_PATH` — approved Publication_Rules.md
- `SUPERSESSION_MAP_PATH` — Supersession_Map.csv from active SCA
- `SECTION_CONTEXT_ROOT` — directory containing SEC-##_Context.md packets
- `EXISTING_PUBLISHED_DBM_PATH` — previous pipeline-produced Rewritten_DBM.md for comparative review

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `DRAFT_DBM_PATH` | Draft to review | **Required** | Absolute path to markdown file |
| `REVIEW_OUTPUT_DIR` | Evidence bundle output root | **Required** | Path under `_Publication/DBM/_Review/<review-id>/` |
| `DOMAIN_ROOT` | DOMAIN decomposition root | **Required** | Absolute path to domain directory |
| `PUBLICATION_SCHEMA_PATH` | Publication schema | unset | Markdown path under `_Planning/` |
| `SECTION_MAP_PATH` | Section map | unset | CSV path under `_Planning/` |
| `PUBLICATION_RULES_PATH` | Publication rules | unset | Markdown path under `_Planning/` |
| `SUPERSESSION_MAP_PATH` | Supersession map | unset | CSV path under active SCA |
| `SECTION_CONTEXT_ROOT` | Section context packets | unset | Directory path |
| `EXISTING_PUBLISHED_DBM_PATH` | Published DBM for comparison | unset | Markdown path under `package/` |

#### Two-level status model

##### EvidenceBundleStatus (process validity)

| Status | Meaning |
|---|---|
| `COMPLETE` | All tools ran, all governed inputs available, all substrate artifacts written |
| `PARTIAL` | One or more governed inputs unavailable; substrate is incomplete — affected review dimensions listed in summary |
| `TOOL_ERROR` | A tool failed; substrate is unreliable |

##### ReviewStatus (agent candidate-finding result)

| Status | Meaning |
|---|---|
| `NO_FINDINGS` | Agent review produced no candidate findings |
| `FINDINGS_FOR_DISPOSITION` | Agent prepared candidate findings for human disposition |
| `REVIEW_INCOMPLETE` | Agent could not complete review (substrate was PARTIAL or TOOL_ERROR) |

#### Finding taxonomy (controlled enum)

| Type | Meaning |
|---|---|
| `INCORRECT` | Draft contradicts governed KTY/SCA/supersession truth |
| `UNSUPPORTED` | Draft makes a claim not warranted by the knowledge base |
| `MISSING` | Governed material exists but is absent from the draft |
| `FLATTENED` | Draft converts TBD/conflict/assumption into a firm fact |
| `OUTDATED` | Draft uses superseded source DBM content |
| `INCOMPLETE` | Draft has the right topic but lacks required engineering detail |

#### Finding severity (controlled enum)

| Severity | Meaning |
|---|---|
| `HIGH` | Significant technical or governance concern |
| `MEDIUM` | Notable gap or inconsistency |
| `LOW` | Minor quality observation |
| `ADVISORY` | Noted for record; no action expected |

#### Method

##### Tool-first: build review substrate

1. **Validate inputs and write boundary.** Confirm DRAFT_DBM_PATH exists and is readable. Confirm REVIEW_OUTPUT_DIR resolves to an acceptable path. Create output directory if absent. If governed inputs (schema, section map, rules) are missing, set `EvidenceBundleStatus = PARTIAL` and record exactly what is unavailable and which review dimensions are affected. Do not improvise a weaker hidden standard.

2. **Run `scan_section_coverage.py`.** When PUBLICATION_SCHEMA_PATH is available, compare draft section headings against the schema. When SECTION_MAP_PATH is also available, pass it as `--section-map` for run-specific authority. Write output to `{REVIEW_OUTPUT_DIR}/Section_Coverage.csv`.

3. **Run `extract_claims.py`.** Extract engineering values, parameters, configuration statements, and controlled terms from draft text. Write output to `{REVIEW_OUTPUT_DIR}/Draft_Claims.csv`.

4. **Run `scan_tbd_markers.py`.** Scan draft for TBD/TBC/ASSUMPTION markers. When SECTION_MAP_PATH and DOMAIN_ROOT are available, pass them for KB cross-reference. Write output to `{REVIEW_OUTPUT_DIR}/TBD_Inventory.csv`.

5. **Run `check_body_thinness.py`.** Compute section body underdevelopment signals. Pass `--section-map` and `--schema` when available. Write output to `{REVIEW_OUTPUT_DIR}/Body_Thinness.csv`.

##### Agent judgment: review governed truth against authored content

6. **Read draft sections against mapped KA artifacts.** When SECTION_MAP_PATH is available, read the Section_Map.csv to identify PRIMARY-role KA artifacts mapped to each section. For each section, read the draft section text and the mapped KA artifacts. Judge:
   - Is the governed design-basis content materially represented?
   - Are configurations, operating modes, interfaces, and design parameters accurately stated?
   - Are tables present where the source material warrants them?
   - Use publication rules and section-type expectations as the review standard.
   - This is the core engineering judgment step — it cannot be replaced by deterministic tools.

7. **Check supersession compliance.** When SUPERSESSION_MAP_PATH is provided, verify that the draft uses current design-basis values, not superseded source wording. Flag OUTDATED findings for any use of superseded content.

8. **Classify candidate findings.** Assign each finding a type from the 6-type taxonomy and a severity. Every finding must:
   - Cite governed-truth evidence (KA path, section, line) and draft location
   - Set `Origin = AGENT_CHECK` (required for REVIEW compatibility)
   - Trace to its substrate source where applicable (e.g., `Section_Coverage.csv:row-3`)

9. **Emit evidence bundle.** Write all outputs to REVIEW_OUTPUT_DIR. Set `EvidenceBundleStatus` and `ReviewStatus` in the summary.

#### Outputs

All outputs are written to REVIEW_OUTPUT_DIR. Exactly 6 files:

| File | Purpose |
|---|---|
| `Evidence_Bundle_Summary.md` | `EvidenceBundleStatus`, `ReviewStatus`, tool run results, input provenance, dimensions assessed vs. not assessed |
| `Section_Coverage.csv` | Structural coverage (expected vs. found sections) |
| `Draft_Claims.csv` | Values, parameters, terms located in draft |
| `Body_Thinness.csv` | Section body underdevelopment signals |
| `TBD_Inventory.csv` | TBD/TBC/ASSUMPTION markers with KB cross-reference |
| `Candidate_Findings.csv` | Agent-prepared findings for human disposition |

#### Candidate_Findings.csv schema

Required columns:

`FindingID, FindingType, Severity, Origin, DraftLocation, DraftLineNumber, DraftText, GovernedTruthRef, GovernedTruthValue, SectionID, KTYRef, KARef, SupersessionRef, Explanation, EvidenceSource`

- `FindingID`: sequential `F-001`, `F-002`, ...
- `FindingType`: controlled enum from finding taxonomy
- `Severity`: controlled enum from finding severity
- `Origin`: `AGENT_CHECK` for all findings (required for REVIEW agent compatibility)
- `EvidenceSource`: traces to substrate row (e.g., `Section_Coverage.csv:row-3`, `Body_Thinness.csv:row-7`) or `AGENT_REVIEW:<brief description>` for pure-judgment findings

#### Evidence_Bundle_Summary.md structure

Required H2 headings:

1. `## Bundle Status` — `EvidenceBundleStatus` and `ReviewStatus` with explanation
2. `## Input Provenance` — paths consumed, which governed inputs were available vs. missing
3. `## Tool Run Results` — per-tool: ran/skipped, exit code, output path, row count
4. `## Review Dimensions` — which review dimensions were assessed (structural coverage, claim accuracy, supersession compliance, body adequacy, TBD fidelity) and which could not be assessed due to missing inputs
5. `## Section Coverage Summary` — narrative interpretation of Section_Coverage.csv
6. `## Body Adequacy Observations` — narrative interpretation of Body_Thinness.csv signals
7. `## TBD and Open-Item Assessment` — narrative interpretation of TBD_Inventory.csv
8. `## Accuracy and Completeness Assessment` — per-section assessment from agent judgment (step 6)
9. `## Supersession Compliance` — assessment from step 7 (or "not assessed" when no supersession map)
10. `## Recommendations` — actionable recommendations for the draft author, organized by severity

#### Non-negotiable constraints

- The skill does NOT modify the draft, knowledge base, publication artifacts, or governed pointers.
- Write boundary is exactly the 6 output files under REVIEW_OUTPUT_DIR.
- Deterministic tool outputs feed reasoning; the skill does not reinvent mechanical checks inline.
- No finding is treated as accepted truth. Findings are candidates for human disposition.
- `Origin = AGENT_CHECK` on every finding row.
- When governed inputs are missing, the skill emits `EVIDENCE_INCOMPLETE` / `PARTIAL` — it does not silently downgrade the review standard.

#### QA expectations

- All 6 required outputs exist under REVIEW_OUTPUT_DIR.
- All writes stayed inside REVIEW_OUTPUT_DIR.
- `Candidate_Findings.csv` uses only controlled enum values for FindingType and Severity.
- Every finding has a non-empty Explanation and EvidenceSource.
- `Evidence_Bundle_Summary.md` contains all required H2 headings.

## Component: skills/dbm-draft-review/TOOL_POLICY.md

### TOOL POLICY - dbm-draft-review

#### Preferred tool order

1. Run `tools/review/scan_section_coverage.py` — structural coverage substrate.
2. Run `tools/review/extract_claims.py` — value/parameter/term extraction substrate.
3. Run `tools/review/scan_tbd_markers.py` — TBD/TBC/ASSUMPTION marker substrate.
4. Run `tools/review/check_body_thinness.py` — body underdevelopment signal substrate.
5. Read substrate outputs and draft sections alongside mapped KA artifacts for agent judgment.
6. Emit the 6 evidence bundle files.

#### Allowed deterministic tools

##### TASK-enforced

- `python3 tools/review/scan_section_coverage.py:*`
- `python3 tools/review/extract_claims.py:*`
- `python3 tools/review/scan_tbd_markers.py:*`
- `python3 tools/review/check_body_thinness.py:*`

##### Operationally invoked

- `tools/review/scan_section_coverage.py` — compare draft section headings against Publication_Schema.md section table, optionally enriched by Section_Map.csv.
- `tools/review/extract_claims.py` — locate engineering values, design parameters, configuration statements, and controlled terms in draft text.
- `tools/review/scan_tbd_markers.py` — locate TBD/TBC/ASSUMPTION markers with line numbers and optional KB cross-reference.
- `tools/review/check_body_thinness.py` — compute section body underdevelopment signals (line counts, density ratios, table presence).

#### Expected use of reasoning

- **Governed-truth comparison:** Read mapped KA artifacts (from Section_Map.csv, PRIMARY role) alongside draft sections. Judge whether governed design-basis content is materially represented — configurations, operating modes, interfaces, design parameters, tables.
- **Supersession compliance:** When Supersession_Map.csv is provided, verify draft uses current design-basis values, not superseded source wording.
- **Materiality judgment:** Decide which substrate signals represent material engineering concerns versus harmless formatting variations. A tool can extract "2 x 100%" from the draft; the agent decides whether it matches the governed "2 × 100% capacity air compressors in lead-lag operation."
- **Finding classification:** Assign the 6-type taxonomy and severity to each candidate finding. Provide rationale and evidence citations.
- **Completeness assessment:** Judge whether sections adequately represent their mapped KTY content at the level expected for a senior-engineer Design Basis Memorandum.
- **Evidence bundle assembly:** Write the Evidence_Bundle_Summary.md with narrative interpretation of substrate results and agent findings.

#### Disallowed use

- No modification of the draft, knowledge base, publication artifacts, or governed pointers.
- No dispatching other agents or skills.
- No inline reimplementation of deterministic checks that belong in the tool layer (e.g., do not manually regex-scan for TBD markers when `scan_tbd_markers.py` does this).
- No reading of raw source DBM files except through structured supersession map comparisons.
- No invention of engineering facts not present in the governed knowledge base.
- No automatic readiness verdicts, PASS/FAIL judgments, or blocking decisions. Findings are candidates for human disposition.

#### Write boundary

Writes are limited to the 6 evidence bundle files, all under the REVIEW_OUTPUT_DIR specified in the brief:

- `Evidence_Bundle_Summary.md`
- `Section_Coverage.csv`
- `Draft_Claims.csv`
- `Body_Thinness.csv`
- `TBD_Inventory.csv`
- `Candidate_Findings.csv`

No other file may be created, modified, or deleted.
