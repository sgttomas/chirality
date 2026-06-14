# Source Pack: Skill pack: kty-content-remediate

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/kty-content-remediate/BRIEF_SCHEMA.md

### kty-content-remediate - Brief Schema

Use this skill with a generic TASK shell (no profile) like this:

```md
PURPOSE: Retire active KTY content after accepted SCA disposition.
RequestedBy: SCOPE_CHANGE

ScopePath: /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist
TaskSkill: kty-content-remediate
AllowedWriteTargets:
  - /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist/.Archive/SCA-004_2026-04-21_1510/
  - /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist/Scoping.md
  - /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist/KA-01_Guidance__Example.md
  - /abs/path/to/domain-root/_ScopeChange/SCA-004_2026-04-21_1510/Evidence/KTY-03-02_Content_Remediation.md
  - /abs/path/to/domain-root/_ScopeChange/SCA-004_2026-04-21_1510/Evidence/KTY-03-02_Content_Disposition.csv

RuntimeOverrides:
  KTY_PATH: /abs/path/to/CAT-003_Operations/1_Working/KTY-03-02_Onboarding-Checklist
  MODE: RETIRE_KTY
  DECOMPOSITION_REF: /abs/path/to/domain-root/_Decomposition
  SCA_SNAPSHOT_PATH: /abs/path/to/domain-root/_ScopeChange/SCA-004_2026-04-21_1510
  AMENDMENT_ID: SCA-004
  SUPERSESSION_MAP_PATH: /abs/path/to/domain-root/_ScopeChange/SCA-004_2026-04-21_1510/Supersession_Map.csv
  SOURCE_ACTION_REF: D-003
  ENTITY_TYPE: KNOWLEDGE_TYPE
  ENTITY_ID: KTY-03-02_Onboarding-Checklist
  AFFECTED_SUBJECTS: "SUB-03-02-01_Example"
  AFFECTED_HBK: "HBK-0123"
  CANONICAL_ROOT_NAME: Example_Domain_Root
  FACILITY_ID: 03-25
  REVIEW_OUTPUT_PATH: /abs/path/to/domain-root/_ScopeChange/SCA-004_2026-04-21_1510/Evidence/KTY-03-02_Content_Remediation.md
  DISPOSITION_EVIDENCE_PATH: /abs/path/to/domain-root/_ScopeChange/SCA-004_2026-04-21_1510/Evidence/KTY-03-02_Content_Disposition.csv
  ARCHIVE_RUN_ID: SCA-004_2026-04-21_1510
  EXPECTED_DISPOSITION: ARCHIVE_AND_STUB
```

#### Required fields

| Field | Value | Notes |
|---|---|---|
| `TaskSkill` | `kty-content-remediate` | Must match skill folder name |
| `ScopePath` | Absolute path to one KTY folder | Normally equals `KTY_PATH` |
| `AllowedWriteTargets` | Archive path, tombstone paths for `RETIRE_KTY`, and evidence output paths | Keep single-KTY and snapshot-local |
| `RuntimeOverrides.KTY_PATH` | Absolute path to one KTY folder | Required |
| `RuntimeOverrides.MODE` | `RETIRE_KTY`, `VERIFY_KTY`, or `EMIT_DISPOSITION` | Required |
| `RuntimeOverrides.DECOMPOSITION_REF` | Admitted decomposition authority | Required |
| `RuntimeOverrides.SCA_SNAPSHOT_PATH` | Accepted SCOPE_CHANGE snapshot | Required |
| `RuntimeOverrides.AMENDMENT_ID` | `SCA-{NNN}` | Required |
| `RuntimeOverrides.REVIEW_OUTPUT_PATH` | Markdown evidence report | Required |

#### Required for factual checks

| Field | Value | Notes |
|---|---|---|
| `RuntimeOverrides.SUPERSESSION_MAP_PATH` | Path to accepted `Supersession_Map.csv` | Required when checking current factual validity |
| `RuntimeOverrides.SOURCE_ACTION_REF` | Amendment action or decision id | Required when emitting disposition evidence |

Do not infer supersessions from SCA prose. Structured SCA artifacts and
`Supersession_Map.csv` are the authority basis.

#### Optional fields

| Field | Default | Allowed values | Notes |
|---|---|---|---|
| `RuntimeOverrides.DISPOSITION_EVIDENCE_PATH` | omitted | Absolute path | Optional structured evidence CSV |
| `RuntimeOverrides.ENTITY_TYPE` | omitted | Known manifest entity type | Triggering entity type for SCOPE_CHANGE evidence |
| `RuntimeOverrides.ENTITY_ID` | omitted | Stable id or term string | Triggering entity id |
| `RuntimeOverrides.AFFECTED_SUBJECTS` | omitted | Semicolon-separated `SUB-*` ids | Subject-level traceability |
| `RuntimeOverrides.AFFECTED_HBK` | omitted | Semicolon-separated `HBK-*` ids | Handbook-unit traceability |
| `RuntimeOverrides.CANONICAL_ROOT_NAME` | omitted | Canonical root token | Multi-root disambiguation |
| `RuntimeOverrides.FACILITY_ID` | omitted | Facility id or blank | Facility-scope disambiguation |
| `RuntimeOverrides.ARCHIVE_RUN_ID` | `{AMENDMENT_ID}_{timestamp}` | Filesystem-safe token | Archive subfolder name |
| `RuntimeOverrides.EXPECTED_DISPOSITION` | `UNKNOWN` | `ARCHIVE_AND_STUB`, `VERIFY_ONLY`, `NO_ACTION`, `UNKNOWN` | Used to detect mismatched dispatch |
| `RuntimeOverrides.MAX_FILES` | `100` | Positive integer | Soft cap on `KA-*.md` inspection |

#### TaskProfile

`NONE` - this skill runs in generic TASK shell mode without a profile.

#### Mode write rules

| Mode | Write behavior |
|---|---|
| `RETIRE_KTY` | May write `.Archive/{ARCHIVE_RUN_ID}/`, tombstone stubs at original `Scoping.md` / `KA-*.md` paths, and evidence outputs. |
| `VERIFY_KTY` | May write only evidence outputs. |
| `EMIT_DISPOSITION` | May write only evidence outputs. |

#### Read boundary

The skill reads:

- root-level `{KTY_PATH}/Scoping.md`
- root-level `{KTY_PATH}/KA-*.md`
- `{KTY_PATH}/.Archive/` only for archive-collision and prior-evidence checks
- `DECOMPOSITION_REF`
- `SCA_SNAPSHOT_PATH`
- `SUPERSESSION_MAP_PATH`

It must not scan sibling KTY folders. `.Archive/` is excluded from current
content enumeration.

#### Write boundary

The skill may write only:

- `{KTY_PATH}/.Archive/{ARCHIVE_RUN_ID}/...`
- original `{KTY_PATH}/Scoping.md` and `{KTY_PATH}/KA-*.md` tombstone stubs in
  `RETIRE_KTY`
- `REVIEW_OUTPUT_PATH`
- optional `DISPOSITION_EVIDENCE_PATH`

It must not write active factual KTY content, metadata files, decomposition
files, SCOPE_CHANGE manifests, or publication outputs.

#### Typical tasks

- retire a KTY's current active content after its scope is removed or replaced
- verify that current KTY content agrees with admitted SCA/decomposition truth
- emit disposition evidence for `KTY_Remediation_Manifest.csv`

#### Notes

- SCOPE_CHANGE owns manifest updates; this skill emits evidence only.
- `domain-documents` owns active content regeneration.
- `.Archive/` scanner exclusion must be preserved by every consumer.

## Component: skills/kty-content-remediate/QA_CHECKS.md

### kty-content-remediate - QA Checks

Minimum checks for a valid run.

#### Non-negotiable invariants

| Invariant | Requirement |
|---|---|
| One KTY per run | `KTY_PATH` resolves to exactly one KTY folder |
| Supported mode | `MODE` is `RETIRE_KTY`, `VERIFY_KTY`, or `EMIT_DISPOSITION` |
| One-writer rule | `domain-documents` remains the only writer of active `Scoping.md` and `KA-*.md` factual content |
| No active factual edits | This skill never modifies active factual content; `RETIRE_KTY` writes only tombstone stubs after archive |
| No metadata edits | `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`, `_MEMORY.md` / `MEMORY.md`, and `_SEMANTIC.md` are untouched |
| No manifest edits | `KTY_Remediation_Manifest.csv` is not updated by this skill |
| Structured authority only | Supersession decisions come from structured SCA artifacts and `Supersession_Map.csv` |
| No prose supersession inference | Do not infer supersessions from SCA prose |
| Archive non-authority | `.Archive/` is history/evidence only, not factual authority |
| .Archive/ scanner exclusion | `.Archive/` scanner exclusion is recorded and respected |

#### Input validation

| Check | Validation |
|---|---|
| KTY path exists | `KTY_PATH` exists and is readable |
| SCA snapshot exists | `SCA_SNAPSHOT_PATH` exists and contains accepted SCOPE_CHANGE artifacts |
| Decomposition authority exists | `DECOMPOSITION_REF` resolves to admitted decomposition truth |
| Evidence output authorized | `REVIEW_OUTPUT_PATH` and optional `DISPOSITION_EVIDENCE_PATH` are in `AllowedWriteTargets` |
| Factual authority present | Factual checks have `SUPERSESSION_MAP_PATH` and `SOURCE_ACTION_REF` |
| No sibling scan | The run did not inspect unrelated KTY folders |

#### RETIRE_KTY checks

| Check | Validation |
|---|---|
| Active file enumeration | Only root-level `Scoping.md` and `KA-*.md` were considered active candidates |
| Archive created | `{KTY_PATH}/.Archive/{ARCHIVE_RUN_ID}/` exists when files were retired |
| Files preserved | Every retired active-looking file has an archived copy |
| Tombstone stubs | Every retired original path begins with `[RETIRED]` and includes amendment id, source action ref, archive path, and non-authority statement |
| No content rewrite | No regenerated factual sections were written by this skill |
| Evidence emitted | Report lists archived files, tombstone paths, authority basis, and blockers |

#### VERIFY_KTY checks

| Check | Validation |
|---|---|
| Report only | No KTY files were modified |
| Current-content boundary | `.Archive/` was excluded from current factual assessment |
| SCA comparison | Observed content state was compared against admitted decomposition and SCA artifacts |
| Factual-use gate | Report states whether current content is allowed, blocked, retired, or regeneration-only |
| Blockers surfaced | Missing authority, ambiguous disposition, or contradictions are not silently resolved |

#### EMIT_DISPOSITION checks

| Check | Validation |
|---|---|
| Evidence fields present | Output includes `CONTENT_DISPOSITION_STATE`, `FACTUAL_USE_GATE`, `AUTHORITY_BASIS`, `SOURCE_ACTION_REF`, and `LAST_VERIFIED_AT` |
| Trigger fields present | Output includes `EntityType`, `EntityID`, `AffectedSubjects`, `AffectedHBK`, `CanonicalRootName`, and `FacilityID` fields, with blanks only when not applicable |
| Archive path explicit | `ARCHIVE_AND_STUB` evidence includes `ArchivePath` |
| Manifest untouched | SCOPE_CHANGE remains responsible for manifest row updates |
| Evidence paths resolvable | Every listed evidence path exists or is marked `location TBD` with blocker notes |

#### Success case

A clean run reports:

- `RUN_STATUS=OK`
- `KTY_PATH`
- `MODE`
- `AMENDMENT_ID`
- `SOURCE_ACTION_REF`
- expected and observed disposition
- files archived or verified
- evidence outputs written
- .Archive/ scanner exclusion status
- no blockers, or explicit blocker list

#### Failure reporting

| Condition | Report |
|---|---|
| Missing KTY path | `RUN_STATUS=FAILED_INPUTS` |
| Unsupported mode | `RUN_STATUS=FAILED_INPUTS` |
| Missing SCA snapshot | `RUN_STATUS=FAILED_INPUTS` |
| Missing structured supersession authority for factual checks | `RUN_STATUS=FAILED_INPUTS` |
| Dispatch does not match expected disposition | `RUN_STATUS=BLOCKED_EXPECTATION_MISMATCH` |
| Archive write target not authorized | `RUN_STATUS=BLOCKED_WRITE_SCOPE` |
| Existing archive collision cannot be resolved safely | `RUN_STATUS=BLOCKED_ARCHIVE_COLLISION` |

#### Invalid states

A run is invalid when:

- active factual content was rewritten instead of archived or verified
- `_STATUS.md`, `_CONTEXT.md`, or `_REFERENCES.md` was modified
- `KTY_Remediation_Manifest.csv` was modified by this skill
- `.Archive/` content was treated as current factual authority
- supersession was inferred from SCA prose instead of structured artifacts
- findings lacked evidence paths or explicit `location TBD`

## Component: skills/kty-content-remediate/SKILL.md

---
name: kty-content-remediate
description: Archive, tombstone, verify, and emit disposition evidence for DOMAIN KTY content after an approved scope change without rewriting active Knowledge Artifact content.
compatibility: Chirality TASK in generic shell mode (no profile); SCOPE_CHANGE-dispatched KTY content disposition evidence pass.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL - kty-content-remediate

#### Purpose

Apply a bounded content-disposition pass for one DOMAIN Knowledge Type folder
after an approved scope-change amendment.

This skill exists to keep the one-writer rule intact:

- `domain-documents` is the only writer of active `Scoping.md` and `KA-*.md`
  factual content.
- `kty-content-remediate` never modifies active factual content. It only
  archives retired active-looking files, leaves non-factual `[RETIRED]`
  tombstone stubs, verifies the current content state, and emits evidence for
  SCOPE_CHANGE.

`.Archive/` is a derivative retirement store. It preserves history and evidence,
but it is never factual authority and must be excluded from downstream scanners,
allowlists, section maps, publication inputs, and regeneration inputs.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

Typical dispatcher: `SCOPE_CHANGE` Gate 5 KTY remediation orchestration.

#### Supported modes

| Mode | Behavior |
|---|---|
| `RETIRE_KTY` | Move active-looking `Scoping.md` and `KA-*.md` files into `{KTY_PATH}/.Archive/`, leave `[RETIRED]` tombstone stubs at the original paths, and emit evidence. |
| `VERIFY_KTY` | Inspect current `Scoping.md` and `KA-*.md` files against admitted decomposition and SCA artifacts. Emit a report only. |
| `EMIT_DISPOSITION` | Emit disposition evidence for SCOPE_CHANGE manifest update. Do not update the manifest directly. |

#### Inputs

##### Required

- `ScopePath` - absolute path to one KTY folder; normally equals `KTY_PATH`
- `TaskSkill` - `kty-content-remediate`
- `RuntimeOverrides.KTY_PATH` - absolute path to one KTY folder
- `RuntimeOverrides.MODE` - `RETIRE_KTY`, `VERIFY_KTY`, or
  `EMIT_DISPOSITION`
- `RuntimeOverrides.DECOMPOSITION_REF` - admitted decomposition package or
  snapshot that governs the KTY
- `RuntimeOverrides.SCA_SNAPSHOT_PATH` - accepted SCOPE_CHANGE snapshot path
- `RuntimeOverrides.AMENDMENT_ID` - `SCA-{NNN}`
- `RuntimeOverrides.REVIEW_OUTPUT_PATH` - markdown report path

##### Required for SCA-driven factual checks

- `RuntimeOverrides.SUPERSESSION_MAP_PATH` - path to the accepted
  `Supersession_Map.csv`
- `RuntimeOverrides.SOURCE_ACTION_REF` - `Amendment_Actions.csv` row or
  decision reference that required this KTY disposition

##### Optional

- `RuntimeOverrides.DISPOSITION_EVIDENCE_PATH` - optional CSV evidence output
- `RuntimeOverrides.ENTITY_TYPE` - triggering entity type from manifest row
- `RuntimeOverrides.ENTITY_ID` - triggering entity id from manifest row
- `RuntimeOverrides.AFFECTED_SUBJECTS` - semicolon-separated affected `SUB-*`
  ids, when known
- `RuntimeOverrides.AFFECTED_HBK` - semicolon-separated affected `HBK-*` ids,
  when known
- `RuntimeOverrides.CANONICAL_ROOT_NAME` - root disambiguator for multi-root
  projects
- `RuntimeOverrides.FACILITY_ID` - facility scope token, when applicable
- `RuntimeOverrides.ARCHIVE_RUN_ID` - stable run id used under `.Archive/`;
  default `{AMENDMENT_ID}_{YYYY-MM-DD}_{HHMM}`
- `RuntimeOverrides.EXPECTED_DISPOSITION` - expected manifest action:
  `ARCHIVE_AND_STUB`, `VERIFY_ONLY`, `NO_ACTION`, or `UNKNOWN`
- `RuntimeOverrides.MAX_FILES` - soft cap on `KA-*.md` files inspected;
  default `100`

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `KTY_PATH` | KTY folder to remediate or verify | **Required** | Absolute path to one `KTY-*` folder |
| `MODE` | Remediation mode | **Required** | `RETIRE_KTY`, `VERIFY_KTY`, `EMIT_DISPOSITION` |
| `DECOMPOSITION_REF` | Admitted decomposition authority | **Required** | Absolute path |
| `SCA_SNAPSHOT_PATH` | Accepted SCOPE_CHANGE snapshot | **Required** | Absolute directory path |
| `AMENDMENT_ID` | Amendment identifier | **Required** | `SCA-{NNN}` |
| `SUPERSESSION_MAP_PATH` | Accepted supersession map | Required for factual checks | Absolute path |
| `SOURCE_ACTION_REF` | Amendment action or decision reference | Required for factual checks | Stable action/decision id |
| `REVIEW_OUTPUT_PATH` | Markdown report output | **Required** | Path in `AllowedWriteTargets` |
| `DISPOSITION_EVIDENCE_PATH` | Structured evidence CSV | omitted | Path in `AllowedWriteTargets` |
| `ENTITY_TYPE` | Triggering entity type | omitted | `KNOWLEDGE_TYPE`, `KNOWLEDGE_SUBJECT`, `HANDBOOK_UNIT`, `CATEGORY`, `VOCAB_TERM`, `OTHER` |
| `ENTITY_ID` | Triggering entity id | omitted | Stable id or term string |
| `AFFECTED_SUBJECTS` | Affected subject ids | omitted | Semicolon-separated `SUB-*` ids |
| `AFFECTED_HBK` | Affected handbook unit ids | omitted | Semicolon-separated `HBK-*` ids |
| `CANONICAL_ROOT_NAME` | Root disambiguator | omitted | Canonical root token |
| `FACILITY_ID` | Facility scope token | omitted | Facility id or blank |
| `ARCHIVE_RUN_ID` | Archive subfolder token | `{AMENDMENT_ID}_{timestamp}` | Filesystem-safe token |
| `EXPECTED_DISPOSITION` | Expected action from manifest draft | `UNKNOWN` | `ARCHIVE_AND_STUB`, `VERIFY_ONLY`, `NO_ACTION`, `UNKNOWN` |
| `MAX_FILES` | Soft cap on KA file count | `100` | Positive integer |

#### Read boundary

The skill reads only:

- `{KTY_PATH}/Scoping.md`
- `{KTY_PATH}/KA-*.md`
- `{KTY_PATH}/.Archive/` for archive-collision and prior-evidence checks only
- admitted decomposition material under `{DECOMPOSITION_REF}`
- accepted SCOPE_CHANGE artifacts under `{SCA_SNAPSHOT_PATH}`, including
  `Amendment_Actions.csv`, `KTY_Remediation_Manifest.csv` when present,
  `Supersession_Delta.csv`, and `Supersession_Map.csv`

This skill must not scan sibling KTY folders. It must not treat `.Archive/` as
current content.

#### Write boundary

Writes are limited to:

- `{KTY_PATH}/.Archive/{ARCHIVE_RUN_ID}/...` in `RETIRE_KTY`
- original `{KTY_PATH}/Scoping.md` and `{KTY_PATH}/KA-*.md` paths only to
  replace retired factual content with non-factual tombstone stubs in
  `RETIRE_KTY`
- `REVIEW_OUTPUT_PATH`
- optional `DISPOSITION_EVIDENCE_PATH`

This skill does not write `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`,
decomposition files, SCOPE_CHANGE manifests, `_Aggregation`, hypergraph outputs,
or publication outputs.

#### Tool usage

- Reasoning-first only.
- No deterministic helpers are declared.
- The `allowed-tools` frontmatter field is intentionally omitted.

#### Authority rules

In all modes, current factual authority is the accepted upstream state supplied
by SCOPE_CHANGE:

1. admitted decomposition state,
2. structured SCA artifacts, especially `Amendment_Actions.csv` and
   `KTY_Remediation_Manifest.csv` when present,
3. `Supersession_Map.csv`,
4. source material only as provenance evidence.

Source material does not override accepted SCA or decomposition truth during
this skill. Do not infer supersessions from SCA prose. Supersession decisions
must come from structured SCA artifacts and `Supersession_Map.csv`.

#### Method

##### Step 0 - Preconditions

1. Confirm `KTY_PATH` is one KTY folder.
2. Confirm `MODE` is supported.
3. Confirm `DECOMPOSITION_REF`, `SCA_SNAPSHOT_PATH`, and `AMENDMENT_ID` are
   readable.
4. Confirm `REVIEW_OUTPUT_PATH` and optional `DISPOSITION_EVIDENCE_PATH` are in
   `AllowedWriteTargets`.
5. For factual checks, confirm `SUPERSESSION_MAP_PATH` and
   `SOURCE_ACTION_REF` are present. If not, return `RUN_STATUS=FAILED_INPUTS`.
6. Enumerate only root-level `Scoping.md` and `KA-*.md` files under
   `KTY_PATH`. Exclude `.Archive/` from current-content enumeration.

##### Step 1 - Resolve Expected Disposition

1. Read `Amendment_Actions.csv` and, when present,
   `KTY_Remediation_Manifest.csv` from `SCA_SNAPSHOT_PATH`.
2. Match this KTY by `KTY_PATH`, KTY id, or `SOURCE_ACTION_REF`.
3. Record the expected action:
   - `ARCHIVE_AND_STUB`
   - `REGENERATE_CONTENT`
   - `VERIFY_ONLY`
   - `NO_ACTION`
   - `UNKNOWN`
4. If `MODE` conflicts with the expected action, do not improvise. Emit
   `RUN_STATUS=BLOCKED_EXPECTATION_MISMATCH`.

##### Step 2 - RETIRE_KTY

Run only when `MODE = RETIRE_KTY`.

1. Identify active-looking content files:
   - `Scoping.md`
   - `KA-*.md`
   - exclude files whose first substantive line begins with `[RETIRED]`
2. Create `{KTY_PATH}/.Archive/{ARCHIVE_RUN_ID}/`.
3. Move each active-looking file into the archive subfolder, preserving the
   original filename.
4. At each original path, write a tombstone stub:
   - first line: `[RETIRED]`
   - amendment id
   - source action reference
   - archive path
   - statement that the stub is not factual authority
5. Do not alter `_STATUS.md`, `_CONTEXT.md`, or `_REFERENCES.md`.
6. Emit report and evidence listing archived files, tombstone paths, archive
   paths, authority basis, and unresolved blockers.

###### Tombstone Format

Use this exact markdown structure for every tombstone stub:

```md
### [RETIRED] {OriginalTitleOrFilename}

This file is a non-factual tombstone stub. It is not current KTY factual
authority and must not be used as source material for downstream generation,
allowlists, section maps, publication inputs, or factual current-content scans.

| Field | Value |
|---|---|
| KTY ID | {KTYID or TBD} |
| Original Path | {original path} |
| Archive Path | {KTY_PATH}/.Archive/{ARCHIVE_RUN_ID}/{original filename} |
| Amendment ID | {AMENDMENT_ID} |
| Source Action Ref | {SOURCE_ACTION_REF} |
| Authority Basis | {DECOMPOSITION_REF}; {SCA_SNAPSHOT_PATH}; {SUPERSESSION_MAP_PATH or N/A} |
| Retired At | {timestamp} |
| Factual Use Gate | RETIRED_NO_FACTUAL_USE |

See the SCA evidence report for disposition details.
```

##### Step 3 - VERIFY_KTY

Run only when `MODE = VERIFY_KTY`.

1. Read current root-level `Scoping.md` and `KA-*.md` files.
2. Compare observed files to the expected disposition and admitted
   decomposition/SCA state.
3. Verify that tombstoned files are not treated as current factual content.
4. Verify that active files do not contradict structured SCA and supersession
   decisions for the target KTY.
5. Emit findings only. Do not modify content.

##### Step 4 - EMIT_DISPOSITION

Run only when `MODE = EMIT_DISPOSITION`.

1. Inspect the current KTY content state.
2. Emit evidence fields suitable for SCOPE_CHANGE manifest update:
   `EntityType`, `EntityID`, `AffectedSubjects`, `AffectedHBK`,
   `CanonicalRootName`, `FacilityID`, `CONTENT_DISPOSITION_STATE`,
   `FACTUAL_USE_GATE`, `AUTHORITY_BASIS`, `SOURCE_ACTION_REF`, `ArchivePath`,
   `LAST_VERIFIED_AT`, evidence paths, and blocker notes.
3. Do not update `KTY_Remediation_Manifest.csv` directly.

#### Output expectations

Every run emits a markdown report at `REVIEW_OUTPUT_PATH` containing:

- `RUN_STATUS`
- `KTY_PATH`
- `MODE`
- `AMENDMENT_ID`
- `SOURCE_ACTION_REF`
- expected disposition
- observed current-content files, excluding `.Archive/`
- evidence paths
- blocker notes
- whether .Archive/ scanner exclusion was respected

When `DISPOSITION_EVIDENCE_PATH` is provided, emit CSV rows with:

```csv
AmendmentID,SourceActionRef,EntityType,EntityID,KTYPath,AffectedSubjects,AffectedHBK,CanonicalRootName,FacilityID,Mode,ObservedFile,DispositionState,FactualUseGate,AuthorityBasis,EvidencePath,ArchivePath,LastVerifiedAt,BlockerNotes
```

#### Non-negotiable constraints

- One KTY folder per run.
- This skill never modifies active factual content.
- Only `domain-documents` may write regenerated active `Scoping.md` or
  `KA-*.md` factual content.
- Do not edit `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`,
  decomposition files, SCOPE_CHANGE manifests, `_Aggregation`, hypergraph
  outputs, or publication outputs.
- Do not dispatch other skills.
- Do not treat `.Archive/` as factual authority.
- .Archive/ scanner exclusion is non-negotiable for every downstream
  scanner, allowlist, section map, publication input, and regeneration input.
- Do not infer supersessions from SCA prose.
- Missing or ambiguous authority is a blocker, not a reason to guess.

#### See also

- `agents/AGENT_SCOPE_CHANGE.md` - Gate 5 dispatcher and manifest owner
- `skills/domain-documents/` - sole writer of active KTY factual content
- `skills/kty-metadata-align/` - metadata-only KTY alignment

## Component: skills/kty-content-remediate/TOOL_POLICY.md

### kty-content-remediate - Tool Policy

#### Preferred tool order

Reasoning-first:

1. read the accepted SCOPE_CHANGE snapshot and admitted decomposition authority
2. enumerate root-level `Scoping.md` and `KA-*.md` under the target KTY
3. exclude `.Archive/` from current-content enumeration
4. in `RETIRE_KTY`, archive active-looking files and write tombstone stubs
5. in `VERIFY_KTY` or `EMIT_DISPOSITION`, report current disposition only
6. emit report and optional structured evidence

#### Allowed deterministic tools

##### TASK-enforced

_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill
load time._

- None - no TASK-enforced deterministic allowlist. The `allowed-tools`
  frontmatter field is intentionally omitted.

##### Operationally invoked

_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None - no deterministic helpers declared.

Do not list or invoke `tools/scaffolding/write_status.sh`; this skill does not
write `_STATUS.md`.

#### Expected use of reasoning

This skill is a bounded disposition and evidence pass. Reasoning governs:

- whether a file is active-looking or already tombstoned
- whether the observed state matches structured SCA disposition expectations
- whether authority is sufficient to claim factual-use safety
- how to classify blocker notes for SCOPE_CHANGE

#### Disallowed use

- No active content rewriting. The skill never modifies active factual content.
- No dispatching other skills.
- No edits to `_STATUS.md`, `_CONTEXT.md`, `_REFERENCES.md`,
  `_MEMORY.md` / `MEMORY.md`, `_SEMANTIC.md`, decomposition files, SCOPE_CHANGE
  manifests, `_Aggregation`, hypergraph outputs, or publication outputs.
- No treatment of `.Archive/` as factual authority.
- No hidden source override of accepted SCA/decomposition truth.
- Do not infer supersessions from SCA prose.

#### Write boundary

Writes are limited by `MODE` and `AllowedWriteTargets`:

- `RETIRE_KTY`: `{KTY_PATH}/.Archive/{ARCHIVE_RUN_ID}/...`, tombstone stubs at
  original `Scoping.md` / `KA-*.md` paths, `REVIEW_OUTPUT_PATH`, and optional
  `DISPOSITION_EVIDENCE_PATH`.
- `VERIFY_KTY`: `REVIEW_OUTPUT_PATH` and optional
  `DISPOSITION_EVIDENCE_PATH`.
- `EMIT_DISPOSITION`: `REVIEW_OUTPUT_PATH` and optional
  `DISPOSITION_EVIDENCE_PATH`.

No other files may be created or modified.

#### .Archive/ scanner exclusion

`.Archive/` scanner exclusion is mandatory. Downstream scanners, allowlists,
section maps, publication inputs, and regeneration inputs must consume only
root-level current content unless explicitly performing historical audit.
