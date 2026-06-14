# Source Pack: Skill pack: dbm-postauthor-concordance

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/dbm-postauthor-concordance/BRIEF_SCHEMA.md

### BRIEF SCHEMA - dbm-postauthor-concordance

This file defines the INIT-TASK dispatch contract for `TASK + dbm-postauthor-concordance`.

#### Purpose

Use this skill after DBM section synthesis and package assembly to build a post-authoring evidence bundle and prepare candidate findings for human readiness judgment.

#### Scope model

- `ScopePath` should be the review output directory within the package snapshot.
- `AllowedWriteTargets` must name exactly the 7 output files under REVIEW_OUTPUT_DIR.
- The brief must not grant write access to section output folders, planning artifacts, KTY folders, or source authority files.

#### Required brief fields

| Field | Type | Meaning | Example |
|---|---|---|---|
| `PURPOSE` | string | Why review is being run | `Post-authoring concordance review for package RUN-20260422-175550.` |
| `ScopePath` | path | Review output directory | `/repo/.../_Publication/DBM/package/RUN-20260422-175550/review/` |
| `TaskSkill` | string | Must equal `dbm-postauthor-concordance` | `dbm-postauthor-concordance` |
| `AllowedWriteTargets` | list[path] | Exactly the 7 output files | `[/.../Evidence_Bundle_Summary.md, /.../Section_Coverage.csv, /.../Draft_Claims.csv, /.../Body_Thinness.csv, /.../TBD_Inventory.csv, /.../Candidate_Findings.csv, /.../Publication_Review_Disposition.csv]` |
| `RuntimeOverrides.ASSEMBLED_DBM_PATH` | path | Assembled Rewritten_DBM.md | `/.../package/RUN-.../Rewritten_DBM.md` |
| `RuntimeOverrides.REVIEW_OUTPUT_DIR` | path | Output directory | `/.../package/RUN-.../review/` |
| `RuntimeOverrides.DOMAIN_ROOT` | path | DOMAIN root | `/repo/.../West_Doe_Deepcut_DBM/` |
| `RuntimeOverrides.PUBLICATION_SCHEMA_PATH` | path | Approved schema | `/.../_Planning/Publication_Schema.md` |
| `RuntimeOverrides.SECTION_MAP_PATH` | path | Approved section map | `/.../_Planning/Section_Map.csv` |
| `RuntimeOverrides.PUBLICATION_RULES_PATH` | path | Approved rules | `/.../_Planning/Publication_Rules.md` |
| `ExpectedOutputs` | list[path] | All 7 outputs | (same as AllowedWriteTargets) |

#### Optional brief fields

| Field | Type | Meaning | Example |
|---|---|---|---|
| `RuntimeOverrides.SUPERSESSION_MAP_PATH` | path | Active supersession map | `/.../SCA-006/.../Supersession_Map.csv` |
| `RuntimeOverrides.SECTION_CONTEXT_ROOT` | path | Section context packets | `/.../_Planning/section-context/` |
| `RuntimeOverrides.SECTIONS_ROOT` | path | Individual section output folders | `/.../_Publication/DBM/sections/` |
| `CustomInstructions` | string | Run-specific emphasis | `Pay special attention to shared utility cross-facility values.` |

#### Runtime-override guidance

- All required inputs are expected to be available in valid pipeline runs. If any are missing, the skill sets `EvidenceBundleStatus = PARTIAL`.
- `SECTIONS_ROOT` provides access to individual section QA artifacts from `dbm-section-publish`. When available, the agent can cross-reference section-level adequacy findings.
- `--section-map` is always passed to substrate tools in pipeline mode (Section_Map.csv is the run-specific authority).

#### Example INIT-TASK brief

```md
PURPOSE: Post-authoring concordance review for package RUN-20260422-175550.
ScopePath: /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/
TaskSkill: dbm-postauthor-concordance
AllowedWriteTargets:
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Evidence_Bundle_Summary.md
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Section_Coverage.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Draft_Claims.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Body_Thinness.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/TBD_Inventory.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Candidate_Findings.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Publication_Review_Disposition.csv
RuntimeOverrides:
  ASSEMBLED_DBM_PATH: /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/Rewritten_DBM.md
  REVIEW_OUTPUT_DIR: /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/
  DOMAIN_ROOT: /repo/domains/West_Doe_Comp_and_Liquids_DBM/
  PUBLICATION_SCHEMA_PATH: /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/_Planning/Publication_Schema.md
  SECTION_MAP_PATH: /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/_Planning/Section_Map.csv
  PUBLICATION_RULES_PATH: /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/_Planning/Publication_Rules.md
  SECTIONS_ROOT: /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/sections/
ExpectedOutputs:
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Evidence_Bundle_Summary.md
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Section_Coverage.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Draft_Claims.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Body_Thinness.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/TBD_Inventory.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Candidate_Findings.csv
  - /repo/domains/West_Doe_Comp_and_Liquids_DBM/_Publication/DBM/package/RUN-20260422-175550/review/Publication_Review_Disposition.csv
```

## Component: skills/dbm-postauthor-concordance/QA_CHECKS.md

### QA CHECKS - dbm-postauthor-concordance

#### Minimum output validity checks

The run is valid only when all of the following are true:

1. All 7 required outputs exist under REVIEW_OUTPUT_DIR:
   - `Evidence_Bundle_Summary.md`
   - `Section_Coverage.csv`
   - `Draft_Claims.csv`
   - `Body_Thinness.csv`
   - `TBD_Inventory.csv`
   - `Candidate_Findings.csv`
   - `Publication_Review_Disposition.csv`
2. All writes stayed inside REVIEW_OUTPUT_DIR.
3. No section outputs, planning artifacts, KTY files, or governed-pointer files were modified.
4. `Evidence_Bundle_Summary.md` contains all required H2 headings and both `EvidenceBundleStatus` and `ReviewStatus`.
5. `Candidate_Findings.csv` uses only controlled enum values for `FindingType` and `Severity`.
6. Every row in `Candidate_Findings.csv` has `Origin = AGENT_CHECK`.
7. Every row in `Candidate_Findings.csv` has a non-empty `Explanation` and `EvidenceSource`.
8. `Publication_Review_Disposition.csv` has exactly one row per `FindingID` in `Candidate_Findings.csv`.
9. Every row in `Publication_Review_Disposition.csv` has `HumanDisposition = TBD`.
10. `Section_Coverage.csv` has `AuthoritySource = SECTION_MAP` (pipeline review always uses section map).

#### Required Candidate_Findings.csv schema

Same as `dbm-draft-review`:

`FindingID, FindingType, Severity, Origin, DraftLocation, DraftLineNumber, DraftText, GovernedTruthRef, GovernedTruthValue, SectionID, KTYRef, KARef, SupersessionRef, Explanation, EvidenceSource`

#### Required Publication_Review_Disposition.csv schema

`FindingID, FindingType, Severity, SectionID, Explanation, EvidenceSource, ProposedDisposition, HumanDisposition, HumanNotes, DispositionDate`

- `FindingID`: must match a FindingID in Candidate_Findings.csv
- `ProposedDisposition`: agent-recommended disposition (free text)
- `HumanDisposition`: must be `TBD` at emission. Allowed values after human review: `ACCEPT_AS_IS`, `REVISE`, `WAIVE_WITH_RATIONALE`, `DEFER`, `NOT_APPLICABLE`
- `HumanNotes`: empty at emission
- `DispositionDate`: empty at emission

#### Required substrate CSV schemas

Same as `dbm-draft-review` QA_CHECKS.md — see that file for Section_Coverage.csv, Draft_Claims.csv, Body_Thinness.csv, and TBD_Inventory.csv column definitions.

#### Required Evidence_Bundle_Summary.md structure

Same as `dbm-draft-review` — 10 required H2 headings.

#### Failure reporting expectations

Use `FAILED_INPUTS` when:
- required runtime overrides are missing (ASSEMBLED_DBM_PATH, REVIEW_OUTPUT_DIR, DOMAIN_ROOT, PUBLICATION_SCHEMA_PATH, SECTION_MAP_PATH, PUBLICATION_RULES_PATH)
- output paths fall outside the package snapshot directory

Use `FAILED` when:
- required outputs cannot be written despite valid inputs
- a tool exits with code 1 (fatal error)

## Component: skills/dbm-postauthor-concordance/SKILL.md

---
name: dbm-postauthor-concordance
description: Post-authoring evidence bundle and review for pipeline-produced DBM sections — build review substrate, prepare candidate findings for human readiness judgment.
compatibility: Chirality TASK; dispatched by DBM_PUBLISHER Gate 6
allowed-tools: python3 tools/review/scan_section_coverage.py:*, python3 tools/review/extract_claims.py:*, python3 tools/review/scan_tbd_markers.py:*, python3 tools/review/check_body_thinness.py:*
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL - dbm-postauthor-concordance

#### Purpose

Post-authoring review for pipeline-produced DBM sections. Build a structured evidence bundle using deterministic substrate tools, then use agent judgment to read governed truth alongside the authored DBM and prepare candidate findings for human readiness judgment.

This skill replaces the pre-authoring concordance model (Gates 3-4 concordance freeze). Concordance is now extracted and validated *after* authoring rather than constraining authoring. The evidence bundle is not a quality gate — findings are candidates for human disposition, not automatic blockers.

This skill is a reviewer only. It does not modify section outputs, the knowledge base, publication planning artifacts, or governed pointers.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

Typical dispatcher: `DBM_PUBLISHER` during Gate 6 after section synthesis and package assembly.

#### Inputs

##### Required

- `ASSEMBLED_DBM_PATH` — path to the assembled Rewritten_DBM.md (or sections root)
- `REVIEW_OUTPUT_DIR` — output directory for the evidence bundle
- `DOMAIN_ROOT` — absolute path to the DOMAIN root
- `PUBLICATION_SCHEMA_PATH` — approved Publication_Schema.md
- `SECTION_MAP_PATH` — approved Section_Map.csv
- `PUBLICATION_RULES_PATH` — approved Publication_Rules.md

##### Optional

- `SUPERSESSION_MAP_PATH` — Supersession_Map.csv from active SCA
- `SECTION_CONTEXT_ROOT` — directory containing SEC-##_Context.md packets
- `SECTIONS_ROOT` — individual section output folders (for section-level QA artifact access)

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `ASSEMBLED_DBM_PATH` | Assembled DBM to review | **Required** | Absolute path to Rewritten_DBM.md |
| `REVIEW_OUTPUT_DIR` | Evidence bundle output root | **Required** | Path under `_Publication/DBM/package/<run-id>/review/` |
| `DOMAIN_ROOT` | DOMAIN decomposition root | **Required** | Absolute path to domain directory |
| `PUBLICATION_SCHEMA_PATH` | Publication schema | **Required** | Markdown path under `_Planning/` |
| `SECTION_MAP_PATH` | Section map | **Required** | CSV path under `_Planning/` |
| `PUBLICATION_RULES_PATH` | Publication rules | **Required** | Markdown path under `_Planning/` |
| `SUPERSESSION_MAP_PATH` | Supersession map | unset | CSV path under active SCA |
| `SECTION_CONTEXT_ROOT` | Section context packets | unset | Directory path |
| `SECTIONS_ROOT` | Section output folders | unset | Path under `_Publication/DBM/sections/` |

#### Two-level status model

##### EvidenceBundleStatus (process validity)

| Status | Meaning |
|---|---|
| `COMPLETE` | All tools ran, all governed inputs available, all substrate artifacts written |
| `PARTIAL` | One or more governed inputs unavailable; substrate is incomplete |
| `TOOL_ERROR` | A tool failed; substrate is unreliable |

Expected to be `COMPLETE` in valid pipeline runs, but the skill must still handle `PARTIAL` and `TOOL_ERROR` — files can be missing, malformed, stale, or unreadable.

##### ReviewStatus (agent candidate-finding result)

| Status | Meaning |
|---|---|
| `NO_FINDINGS` | Agent review produced no candidate findings |
| `FINDINGS_FOR_DISPOSITION` | Agent prepared candidate findings for human disposition |
| `REVIEW_INCOMPLETE` | Agent could not complete review |

#### Finding taxonomy (controlled enum)

| Type | Meaning |
|---|---|
| `INCORRECT` | Authored content contradicts governed KTY/SCA/supersession truth |
| `UNSUPPORTED` | Authored content makes a claim not warranted by the knowledge base |
| `MISSING` | Governed material exists but is absent from the authored content |
| `FLATTENED` | Authored content converts TBD/conflict/assumption into a firm fact |
| `OUTDATED` | Authored content uses superseded source DBM content |
| `INCOMPLETE` | Authored content has the right topic but lacks required engineering detail |

#### Finding severity (controlled enum)

| Severity | Meaning |
|---|---|
| `HIGH` | Significant technical or governance concern |
| `MEDIUM` | Notable gap or inconsistency |
| `LOW` | Minor quality observation |
| `ADVISORY` | Noted for record; no action expected |

#### Method

##### Tool-first: build review substrate

1. **Validate inputs and write boundary.** Confirm all required paths exist. Create output directory if absent. If any required input is missing or unreadable, set `EvidenceBundleStatus = PARTIAL` and record the gap.

2. **Run `scan_section_coverage.py`.** Pass `--section-map` (required for pipeline review — Section_Map.csv is the run-specific authority after Gate 4). Write output to `{REVIEW_OUTPUT_DIR}/Section_Coverage.csv`.

3. **Run `extract_claims.py`.** Extract engineering values, parameters, configuration statements from assembled DBM. Write output to `{REVIEW_OUTPUT_DIR}/Draft_Claims.csv`.

4. **Run `scan_tbd_markers.py`.** Scan assembled DBM for TBD/TBC/ASSUMPTION markers with KB cross-reference. Write output to `{REVIEW_OUTPUT_DIR}/TBD_Inventory.csv`.

5. **Run `check_body_thinness.py`.** Pass `--section-map` and `--schema`. Write output to `{REVIEW_OUTPUT_DIR}/Body_Thinness.csv`.

##### Agent judgment: review governed truth against authored content

6. **Read authored sections against mapped KA artifacts.** Use Section_Map.csv to identify PRIMARY-role KA artifacts per section. For each section, judge materiality, accuracy, and completeness. This is the core engineering judgment step.

7. **Check supersession compliance.** When SUPERSESSION_MAP_PATH is provided, verify authored content uses current values.

8. **Classify candidate findings.** Every finding must set `Origin = AGENT_CHECK`, cite governed-truth evidence, and trace to substrate where applicable.

9. **Emit evidence bundle and disposition artifact.** Write all outputs to REVIEW_OUTPUT_DIR. Write `Publication_Review_Disposition.csv` with `HumanDisposition = TBD` for all rows.

#### Outputs

All outputs are written to REVIEW_OUTPUT_DIR. 7 files total:

| File | Purpose |
|---|---|
| `Evidence_Bundle_Summary.md` | `EvidenceBundleStatus`, `ReviewStatus`, tool run results, input provenance |
| `Section_Coverage.csv` | Structural coverage |
| `Draft_Claims.csv` | Values, parameters, terms located in authored text |
| `Body_Thinness.csv` | Section body underdevelopment signals |
| `TBD_Inventory.csv` | TBD/TBC/ASSUMPTION markers with KB cross-reference |
| `Candidate_Findings.csv` | Agent-prepared findings for human disposition |
| `Publication_Review_Disposition.csv` | Disposition artifact for human decision recording |

#### Candidate_Findings.csv schema

Same as `dbm-draft-review`:

`FindingID, FindingType, Severity, Origin, DraftLocation, DraftLineNumber, DraftText, GovernedTruthRef, GovernedTruthValue, SectionID, KTYRef, KARef, SupersessionRef, Explanation, EvidenceSource`

#### Publication_Review_Disposition.csv schema

`FindingID, FindingType, Severity, SectionID, Explanation, EvidenceSource, ProposedDisposition, HumanDisposition, HumanNotes, DispositionDate`

- `FindingID`: matches `Candidate_Findings.csv` FindingID
- `ProposedDisposition`: agent-recommended disposition
- `HumanDisposition`: `TBD` until human rules. Allowed values: `ACCEPT_AS_IS`, `REVISE`, `WAIVE_WITH_RATIONALE`, `DEFER`, `NOT_APPLICABLE`
- `HumanNotes`: empty until human fills in
- `DispositionDate`: empty until human fills in

DBM_PUBLISHER does not update acceptance pointers until all `HumanDisposition` values are recorded (no `TBD` remaining).

#### Evidence_Bundle_Summary.md structure

Same required H2 headings as `dbm-draft-review`.

#### Non-negotiable constraints

- The skill does NOT modify section outputs, knowledge base, publication artifacts, or governed pointers.
- Write boundary is exactly the 7 output files under REVIEW_OUTPUT_DIR.
- No finding is treated as accepted truth. Findings are candidates for human disposition.
- `Origin = AGENT_CHECK` on every finding row.
- No automatic readiness verdicts, PASS/FAIL judgments, or blocking decisions.
- `Publication_Review_Disposition.csv` is emitted with `HumanDisposition = TBD` — the skill does not pre-fill human decisions.

#### QA expectations

- All 7 required outputs exist under REVIEW_OUTPUT_DIR.
- All writes stayed inside REVIEW_OUTPUT_DIR.
- `Candidate_Findings.csv` uses only controlled enum values for FindingType and Severity.
- Every finding has `Origin = AGENT_CHECK`, non-empty Explanation and EvidenceSource.
- `Publication_Review_Disposition.csv` has one row per finding, with `HumanDisposition = TBD`.
- `Evidence_Bundle_Summary.md` contains both `EvidenceBundleStatus` and `ReviewStatus`.

## Component: skills/dbm-postauthor-concordance/TOOL_POLICY.md

### TOOL POLICY - dbm-postauthor-concordance

#### Preferred tool order

1. Run `tools/review/scan_section_coverage.py` with `--section-map` (required in pipeline mode).
2. Run `tools/review/extract_claims.py` — value/parameter/term extraction.
3. Run `tools/review/scan_tbd_markers.py` — TBD/TBC/ASSUMPTION marker scan with KB cross-ref.
4. Run `tools/review/check_body_thinness.py` with `--section-map` and `--schema`.
5. Read substrate outputs and authored sections alongside mapped KA artifacts for agent judgment.
6. Emit the 7 output files (6 evidence bundle + disposition artifact).

#### Allowed deterministic tools

##### TASK-enforced

- `python3 tools/review/scan_section_coverage.py:*`
- `python3 tools/review/extract_claims.py:*`
- `python3 tools/review/scan_tbd_markers.py:*`
- `python3 tools/review/check_body_thinness.py:*`

##### Operationally invoked

- `tools/review/scan_section_coverage.py` — compare authored section headings against Publication_Schema.md, enriched by Section_Map.csv (run-specific authority).
- `tools/review/extract_claims.py` — locate engineering values, parameters, configuration statements, and controlled terms in authored text.
- `tools/review/scan_tbd_markers.py` — locate TBD/TBC/ASSUMPTION markers with KB cross-reference via Section_Map.csv Scoping.md discovery.
- `tools/review/check_body_thinness.py` — compute section body underdevelopment signals with mapped-artifact density ratios.

#### Expected use of reasoning

- **Governed-truth comparison:** Read mapped KA artifacts (PRIMARY role) alongside authored sections. Judge whether governed design-basis content is materially represented.
- **Supersession compliance:** Verify authored content uses current values when Supersession_Map.csv is provided.
- **Materiality judgment:** Distinguish material engineering concerns from formatting variations.
- **Finding classification:** Assign 6-type taxonomy and severity. Cite governed evidence and trace to substrate.
- **Completeness assessment:** Judge section adequacy at the level expected for a senior-engineer Design Basis Memorandum.
- **Disposition preparation:** Write `Publication_Review_Disposition.csv` with agent-proposed dispositions and `HumanDisposition = TBD`.
- **Section QA cross-reference:** When SECTIONS_ROOT is available, cross-reference section-level QA artifacts from `dbm-section-publish` for additional context.

#### Disallowed use

- No modification of section outputs, knowledge base, publication artifacts, or governed pointers.
- No dispatching other agents or skills.
- No inline reimplementation of deterministic checks that belong in the tool layer.
- No reading of raw source DBM files except through structured supersession map comparisons.
- No invention of engineering facts not present in the governed knowledge base.
- No automatic readiness verdicts, PASS/FAIL judgments, or blocking decisions.
- No pre-filling of `HumanDisposition` values — all rows emit as `TBD`.

#### Write boundary

Writes are limited to the 7 output files, all under the REVIEW_OUTPUT_DIR specified in the brief:

- `Evidence_Bundle_Summary.md`
- `Section_Coverage.csv`
- `Draft_Claims.csv`
- `Body_Thinness.csv`
- `TBD_Inventory.csv`
- `Candidate_Findings.csv`
- `Publication_Review_Disposition.csv`

No other file may be created, modified, or deleted.
