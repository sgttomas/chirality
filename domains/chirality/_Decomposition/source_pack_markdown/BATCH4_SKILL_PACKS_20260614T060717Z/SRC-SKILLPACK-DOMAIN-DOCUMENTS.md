# Source Pack: Skill pack: domain-documents

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/domain-documents/BRIEF_SCHEMA.md

### domain-documents — Brief Schema

Use this skill with a generic TASK shell (no profile) like this:

```md
PURPOSE: Draft Knowledge Artifacts for KTY-01 (Pressure Vessel Design)
RequestedBy: ORCHESTRATOR

ScopePath: /abs/path/to/KTY-01_Pressure-Vessel-Design
TaskSkill: domain-documents

RuntimeOverrides:
  KTY_PATH: /abs/path/to/KTY-01_Pressure-Vessel-Design
  DECOMPOSITION_REF: /abs/path/to/_Decomposition
  DECOMP_VARIANT: DOMAIN
  AUTHORITY_MODE: SOURCE_FIDELITY
  RUN_PASSES: FULL
  ALLOW_OVERWRITE_STATES: "OPEN, INITIALIZED"
  SOURCES_ROOT: /abs/path/to/_Sources
  COMBINED_SOURCE_AUTHORITY_PATH: /abs/path/to/shared/source/root
```

#### Required fields

| Field | Value | Notes |
|---|---|---|
| `TaskSkill` | `domain-documents` | Must match skill folder name |
| `ScopePath` | Absolute path to the Knowledge Type folder | Normally equals `KTY_PATH` |
| `RuntimeOverrides.KTY_PATH` | Absolute path to one Knowledge Type folder | Must contain (or expect) `_CONTEXT.md`, `_STATUS.md` |
| `RuntimeOverrides.DECOMPOSITION_REF` | Path to DOMAIN decomposition folder or doc(s) | Used to locate `KnowledgeTypes.csv`, `HandbookUnits.csv`, `DomainLedger.csv` |

#### Optional fields

| Field | Default | Allowed values | Notes |
|---|---|---|---|
| `RuntimeOverrides.DECOMP_VARIANT` | `DOMAIN` | `DOMAIN` only | **Fixed to DOMAIN.** This skill is DOMAIN-only; PROJECT/SOFTWARE variants use `four-documents` |
| `RuntimeOverrides.AUTHORITY_MODE` | `SOURCE_FIDELITY` | `SOURCE_FIDELITY`, `SCA_DRIVEN` | Authority policy for factual content |
| `RuntimeOverrides.RUN_PASSES` | `FULL` | `FULL`, `P1_P2`, `P3_ONLY` | See pass semantics below |
| `RuntimeOverrides.ALLOW_OVERWRITE_STATES` | `OPEN, INITIALIZED` | Comma-separated state list | Safe-update gate for `_STATUS.md` |
| `RuntimeOverrides.SCA_SNAPSHOT_PATH` | omitted | Absolute path | Required when `AUTHORITY_MODE: SCA_DRIVEN` |
| `RuntimeOverrides.SUPERSESSION_MAP_PATH` | omitted | Absolute path | Required and valid only when `AUTHORITY_MODE: SCA_DRIVEN` |
| `RuntimeOverrides.ROOT_NAME` | omitted | String | Canonical root name used to filter supersession rows such as `AppliesToRoots` |
| `RuntimeOverrides.FACILITY_ID` | omitted | String | Facility identifier used to filter supersession rows such as `AppliesToFacilities` |
| `RuntimeOverrides.ALLOW_OVERWRITE_OVERRIDE` | omitted | `SCA_AUTHORIZED` | Permits active content overwrite for the dispatched KTY only when SCA inputs are present |
| `RuntimeOverrides.UNIT_SCOPE` | `EXAMPLES_ONLY` | `EXAMPLES_ONLY`, `ALL_MAPPED` | Which handbook units form the evidence set |
| `RuntimeOverrides.ARTIFACT_NAMING` | `PREFIXED_TYPED_SLUG` | `PREFIXED_TYPED_SLUG`, `TYPED_SLUG`, `PREFIXED_SLUG` | Artifact file naming policy |
| `RuntimeOverrides.MAX_ARTIFACTS` | `25` | Positive integer | Hard cap on artifact file count |
| `RuntimeOverrides.SOURCES_ROOT` | Provided by ORCHESTRATOR | Absolute path | Shared source/reference file root |
| `RuntimeOverrides.COMBINED_SOURCE_AUTHORITY_PATH` | omitted | Absolute path | Additional admitted source authority root for combined/cross-root source packages; source material remains subordinate to structured SCA supersession in `SCA_DRIVEN` mode |
| `RuntimeOverrides.REPORT_TO` | `ORCHESTRATOR` | Free-form | Where to report run outcome |

#### TaskProfile

`NONE` — this skill runs in generic TASK shell mode without a profile.

#### DECOMP_VARIANT

**This skill is DOMAIN-only.** `DECOMP_VARIANT` is fixed to `DOMAIN`. Any other value halts the run with `RUN_STATUS=UNSUPPORTED_VARIANT`. The PROJECT and SOFTWARE variants use the `four-documents` skill (fixed 4-document kit), not this skill.

#### AUTHORITY_MODE

`SOURCE_FIDELITY` is the default and preserves existing behavior: source
material bounded by `SourceSpan` is factual authority, while decomposition data
scopes and routes the work.

`SCA_DRIVEN` is used only when SCOPE_CHANGE dispatches regeneration after an
accepted amendment. In this mode, admitted decomposition state, structured SCA
artifacts, and `SUPERSESSION_MAP_PATH` are current factual authority. Source
material is provenance verification only and must not override accepted
SCA/decomposition truth.

`SUPERSESSION_MAP_PATH` without `AUTHORITY_MODE: SCA_DRIVEN` fails input
validation. `ALLOW_OVERWRITE_OVERRIDE: SCA_AUTHORIZED` is accepted only with
`AUTHORITY_MODE: SCA_DRIVEN`, `SCA_SNAPSHOT_PATH`, and
`SUPERSESSION_MAP_PATH`, and only for active `Scoping.md` / `KA-*.md` files in
the dispatched `KTY_PATH`.

Do not infer supersessions from SCA prose.

##### SCA-driven example

```md
PURPOSE: Regenerate KTY content from accepted SCA authority.
RequestedBy: SCOPE_CHANGE

ScopePath: /abs/path/to/KTY-03-02_Onboarding-Checklist
TaskSkill: domain-documents

RuntimeOverrides:
  KTY_PATH: /abs/path/to/KTY-03-02_Onboarding-Checklist
  DECOMPOSITION_REF: /abs/path/to/domain-root/_Decomposition
  DECOMP_VARIANT: DOMAIN
  AUTHORITY_MODE: SCA_DRIVEN
  SCA_SNAPSHOT_PATH: /abs/path/to/domain-root/_ScopeChange/SCA-004_2026-04-21_1510
  SUPERSESSION_MAP_PATH: /abs/path/to/domain-root/_ScopeChange/SCA-004_2026-04-21_1510/Supersession_Map.csv
  ROOT_NAME: Example_Domain_Root
  FACILITY_ID: FAC-001
  ALLOW_OVERWRITE_OVERRIDE: SCA_AUTHORIZED
  RUN_PASSES: FULL
  SOURCES_ROOT: /abs/path/to/_Sources
  COMBINED_SOURCE_AUTHORITY_PATH: /abs/path/to/shared/source/root
```

#### RUN_PASSES semantics

| Value | Steps run | Use case |
|---|---|---|
| `FULL` | Steps 1–7 (Pass 1 drafting + Pass 2 consistency + Pass 3 source-fidelity + status) | Default single-run completion |
| `P1_P2` | Steps 1–5 + Step 7 (drafting + cross-artifact consistency only) | When source-fidelity check must be deferred |
| `P3_ONLY` | Step 1 (full reads incl. source) + Step 6 (source-fidelity) + Step 7 | Re-verify existing drafts against source; requires existing KA-*.md files and accessible source |

#### UNIT_SCOPE values

- `EXAMPLES_ONLY` → use `KnowledgeTypes.csv.ExampleUnitIDs` (default, bounded)
- `ALL_MAPPED` → use all `UnitID` values from `DomainLedger.csv` where `KnowledgeTypeID(s)` includes this KTY (best-effort; may be large)

#### ARTIFACT_NAMING values

- `PREFIXED_TYPED_SLUG` (default) → `KA-01_{Type}__{Slug}.md`
- `TYPED_SLUG` → `{Type}__{Slug}.md`
- `PREFIXED_SLUG` → `KA-01_{Slug}.md`

Where:
- `Type` = base archetype (`Reference|Guidance|Checklist|Procedure`) from `CanonicalSchema`
- `Slug` = filesystem-safe slug from the Knowledge Subject name (letters/numbers/hyphen; collapse whitespace)

#### Read boundary

The skill reads:
- Files within `{KTY_PATH}`: `_CONTEXT.md`, `_REFERENCES.md`, `_STATUS.md`, sibling `_MEMORY.md` / `MEMORY.md` whenever `_STATUS.md` is read, existing `KA-*.md` + `Scoping.md` (for Pass 2/3)
- Decomposition data under `{DECOMPOSITION_REF}`: `KnowledgeTypes.csv`, `HandbookUnits.csv`, `DomainLedger.csv`, or root-specific equivalent register names
- Authoritative source files under `{SOURCES_ROOT}`, `COMBINED_SOURCE_AUTHORITY_PATH`, or paths listed in `_REFERENCES.md` (referenced by `SourceSpan`)
- In `AUTHORITY_MODE: SCA_DRIVEN`, structured SCA artifacts under `SCA_SNAPSHOT_PATH` and `SUPERSESSION_MAP_PATH`

When `ROOT_NAME` or `FACILITY_ID` is provided, supersession rows with scoping fields such as `AppliesToRoots` or `AppliesToFacilities` must be filtered to the dispatched root/facility before being applied.

`_MEMORY.md` / `MEMORY.md` is never factual authority. It is read only as
non-authoritative operational context paired with `_STATUS.md`.

#### Write boundary

The skill writes only within `{KTY_PATH}`:
- `Scoping.md` (Pass 1 always; Pass 3 updates the Source-Fidelity Log)
- Variable `KA-*.md` Knowledge Artifact files (Pass 1 creates; Pass 3 may correct)
- `_STATUS.md` (safe-update only: `OPEN → INITIALIZED` when Pass 1/2 ran)

`ALLOW_OVERWRITE_OVERRIDE: SCA_AUTHORIZED` may bypass
`ALLOW_OVERWRITE_STATES` only in `AUTHORITY_MODE: SCA_DRIVEN` with complete SCA
snapshot inputs, and only for the dispatched KTY. It does not authorize
metadata edits or cross-KTY writes.

The skill does NOT modify:
- `_CONTEXT.md`
- `_REFERENCES.md`
- `_MEMORY.md` / `MEMORY.md`
- `_SEMANTIC.md`

#### Lifecycle states

DOMAIN lifecycle: `OPEN → INITIALIZED → IN_PROGRESS`

This skill handles the `OPEN → INITIALIZED` transition (during Pass 1/2 runs). The `IN_PROGRESS` transition is handled downstream by `WORKING_ITEMS`.

**Note:** `SEMANTIC_READY` is NOT a valid state in the DOMAIN lifecycle. It belongs to PROJECT/SOFTWARE (four-documents pipeline) only.

#### Notes

- One invocation processes one Knowledge Type folder. ORCHESTRATOR dispatches one task per in-scope KTY.
- The brief does not include `AllowedTools` because this is a reasoning-first drafting skill. Safe-update of `_STATUS.md` uses `tools/scaffolding/write_status.sh` if available.
- Authoritative source access is mandatory — runs that cannot read the source file halt with `FAILED_INPUTS`.

## Component: skills/domain-documents/QA_CHECKS.md

### domain-documents — QA Checks

Minimum checks for a valid run and the non-negotiable invariants preserved from the source agent.

#### Non-negotiable invariants

These invariants MUST hold for every run. Violating any of them makes the run invalid.

| Invariant | Requirement |
|---|---|
| **DOMAIN pipeline only** | `DECOMP_VARIANT` must be `DOMAIN`; otherwise halt with `UNSUPPORTED_VARIANT`. This skill is not called by PROJECT or SOFTWARE variants |
| **Variable Knowledge Artifact schema** | Artifact count and names derive from `KnowledgeSubjects` in the decomposition. No fixed 4-doc kit |
| **Subject-to-Artifact bijection** | Each Knowledge Subject maps to exactly one Knowledge Artifact file. No splitting or merging |
| **Maximally comprehensive KAs** | The KA set captures all material source-backed facts, parameters, scope boundaries, interfaces, assumptions, exceptions, open issues, and current-state authority notes within the approved KTY/Subject scope |
| **KA-* naming convention** | Default `KA-01_{Type}__{Slug}.md`; configurable via `ARTIFACT_NAMING`. Stable ordinal prefix when `PREFIXED_*` |
| **One deliverable per run** | Each invocation processes exactly one Knowledge Type folder (`KTY_PATH`). No cross-Knowledge-Type scanning |
| **No human input** | The skill works from folder contents, references, and decomposition. Human interacts with ORCHESTRATOR/WORKING_ITEMS, not this skill |
| **Respect human work** | `_STATUS.md` `Current State` must be within `ALLOW_OVERWRITE_STATES` (default `OPEN, INITIALIZED`) before any overwrite. Halt with `SKIPPED_PROTECT_HUMAN_WORK` otherwise |
| **Authority mode default** | `AUTHORITY_MODE` defaults to `SOURCE_FIDELITY`; non-SCA behavior remains unchanged |
| **SCA authority mode** | `AUTHORITY_MODE: SCA_DRIVEN` requires admitted decomposition state, structured SCA artifacts, and `SUPERSESSION_MAP_PATH`; source material is provenance verification only |
| **Supersession map gate** | `SUPERSESSION_MAP_PATH` without `AUTHORITY_MODE: SCA_DRIVEN` fails input validation |
| **Supersession applicability filter** | When `ROOT_NAME` or `FACILITY_ID` is provided, supersession rows are filtered by `AppliesToRoots` / `AppliesToFacilities` before application |
| **Additional source authority root** | `COMBINED_SOURCE_AUTHORITY_PATH`, when provided, is used only as admitted source material and remains subordinate to structured SCA supersession in `SCA_DRIVEN` mode |
| **SCA overwrite override** | `ALLOW_OVERWRITE_OVERRIDE: SCA_AUTHORIZED` is valid only with `AUTHORITY_MODE: SCA_DRIVEN`, `SCA_SNAPSHOT_PATH`, and `SUPERSESSION_MAP_PATH`, and only for the dispatched KTY |
| **No metadata modification** | Never modify `_CONTEXT.md`, `_REFERENCES.md`, `_MEMORY.md`/`MEMORY.md`, or `_SEMANTIC.md`. Metadata drift discovered during regeneration must be surfaced as a follow-on alignment action, not fixed inside this skill |
| **Status-memory paired read** | Whenever `_STATUS.md` is read, sibling `_MEMORY.md` / `MEMORY.md` is read when present as non-authoritative operational context only |
| **No invention** | Missing information marked `TBD`; inferences labeled `ASSUMPTION`. Do not fabricate source excerpts when source is inaccessible |
| **Authoritative source required in default mode** | In `SOURCE_FIDELITY` mode, all passes require the source file(s) bounded by `SourceSpan` to be accessible. Halt with `FAILED_INPUTS` if source cannot be read |
| **Structured supersession only** | Do not infer supersessions from SCA prose; use structured SCA artifacts and `SUPERSESSION_MAP_PATH` |
| **Authority fidelity is the quality gate** | Pass 3 verifies artifact-to-source fidelity in `SOURCE_FIDELITY` mode and artifact-to-SCA fidelity in `SCA_DRIVEN` mode. No semantic lensing / semantic enrichment is used in the DOMAIN pipeline |
| **Safe-update status only** | `_STATUS.md` transitions `OPEN → INITIALIZED` only when Pass 1/2 ran. Never regress state |
| **No SEMANTIC_READY state** | DOMAIN lifecycle is `OPEN → INITIALIZED → IN_PROGRESS`; `SEMANTIC_READY` is NOT a valid DOMAIN state |

#### Structural checks (Pass 1)

| Check | Validation |
|---|---|
| Scoping exists | `Scoping.md` present in `{KTY_PATH}` |
| Scoping identity | Contains KTY identity, Category, CanonicalSchema, intended users, when-used context |
| Scoping context | Records Subject coverage, active authority basis, and SCA/supersession impact summary when available |
| Evidence set table | Table present with UnitID → AtomicStatement → SourceRef columns |
| Artifact plan table | Table present with ArtifactID → SubjectID → SubjectName → BaseType → AddOns → Filename |
| Conflict Table | Present with stable schema (Conflict ID, Conflict, Source A, Source B, Impacted artifacts, Proposed authority, Human ruling) |
| Artifacts created | Every artifact listed in the plan table exists as a `.md` file in `{KTY_PATH}` |
| Default sections present | Each Knowledge Artifact contains all default schema sections for its base type (Reference/Guidance/Checklist/Procedure) |
| Metadata block present | Each `KA-*.md` has an Artifact Metadata block with Knowledge Type, Category, Knowledge Subject, Artifact ID, Base Type, Add-ons, Evidence Units |
| KA comprehensiveness | Each KA captures the material subject-scope facts, values, interfaces, assumptions, exceptions, open issues, and current-state authority notes available from the accepted authority inputs |
| No invented content | TBDs used for missing info; ASSUMPTION label for inferences |
| Conflicts surfaced | Contradictions logged in Scoping.md Conflict Table with evidence pointers |

#### Cross-artifact consistency checks (Pass 2)

| Check | Validation |
|---|---|
| Plan-to-file closure | Every plan-table entry has a file; every `KA-*.md` file has a plan-table entry |
| No duplicate filenames | File names unique across the KTY folder |
| Identity consistency | KTY ID, Name, Category consistent across `Scoping.md` and every `KA-*.md` metadata block |
| Subject-Artifact mapping | `SubjectID ↔ ArtifactID` mappings in artifact metadata match `Scoping.md` plan table |
| Cross-artifact value consistency | Parameters, design values, equipment tags, operating conditions identical or non-contradictory across artifacts |
| Evidence traceability | Every non-trivial claim cites a UnitID, SourceRef, or is marked TBD/ASSUMPTION |
| UnitID presence | UnitIDs referenced in artifacts exist in the evidence set table in `Scoping.md` |
| SourceRef syntax | SourceRef pointers syntactically consistent across all docs |
| Terminology consistency | Same terms used consistently across artifacts; synonym drift flagged as Conflict Table entries |

#### Source-fidelity checks (Pass 3)

| Check | Validation |
|---|---|
| Source file accessed in `SOURCE_FIDELITY` | Source file(s) bounded by `SourceSpan` successfully read for this KTY |
| SCA authority checked | In `AUTHORITY_MODE: SCA_DRIVEN`, admitted decomposition state, structured SCA artifacts, and `SUPERSESSION_MAP_PATH` were read before source provenance checks |
| Coverage verified | Every substantive source statement compared against artifact content |
| Accuracy verified | Every non-TBD, non-ASSUMPTION artifact claim traced to a specific source location |
| Corrections logged | Each artifact correction recorded in `Scoping.md` `## Source-Fidelity Log` section |
| Gaps logged | Source content not captured in any artifact recorded as a gap with source location |
| Unverified flagged | Claims not traceable to source marked `UNVERIFIED` or downgraded to `ASSUMPTION` |
| Source reread evidence | Each correction/enrichment records which source slice was re-read before the change was applied |
| Structural sweep re-run | After corrections, Pass 2 structural completeness checks (items 1–3) re-verified |

#### Audit-on-write retrieval check (Pass 4 — when retrieval index present)

In domains where a merged Atomic_Domain_Ledger and a retrieval index over it
exist, each authored KA runs a post-draft self-audit of its claim sentences
against the retrieval index. This is independent of Pass 3 (which is per-claim
trace to source span) and serves as a corpus-grounded sanity check that the
right cited HBAs were actually selected.

**Index discovery.** The dispatcher specifies the index via the
`RETRIEVAL_INDEX_PATH` runtime override. The value is a V2 source database
snapshot directory or a `_LATEST.md` pointer, normally
`<domain-root>/_LocalIndexes/_LATEST.md`. If omitted, the skill looks for a
domain-local `_LocalIndexes/_LATEST.md`; if neither is present the skill
records `PASS_4_SKIPPED_INDEX_UNAVAILABLE` and does not run the check.

**Staleness check.** The skill reads the snapshot `meta.json` and treats the
source database as stale if source/audit/decomposition inputs have changed
since the snapshot was built. If stale, it records
`PASS_4_SKIPPED_INDEX_STALE` and does not run.

**Procedure.** Build `claims.csv` (one row per claim sentence in the KA
draft), then invoke the query tool specified by `RETRIEVAL_QUERY_TOOL`
(default `tools/retrieval/query_source_index.py`):

```
python3 {RETRIEVAL_QUERY_TOOL} --snapshot {RETRIEVAL_INDEX_PATH} --batch claims.csv --k 5 --json
```

Per-claim verdict (judged on **source spans**, not on cosine score — cosine is a
sanity check on retrieval quality, not the audit verdict):

| Verdict | Condition |
|---|---|
| **PASS** | At least one cited HBA appears in retrieval top-5 AND the cited source span supports the claim with full qualifiers preserved (Pass-3 confirmed). |
| **WARN** | A cited HBA appears in top-5 but a higher-ranked uncited HBA also appears with cosine ≥ `RETRIEVAL_COSINE_THRESHOLD` (default `0.75`). The agent opens the uncited HBA's source span and decides whether to add the citation, demote the existing one, or note the alternative. |
| **FAIL** | No cited HBA in top-5 (retrieval doesn't even surface the cited evidence for this claim text), OR re-read of the cited source span shows the claim has lost a qualifier or scope. Resolve before run-closure. |

The cosine threshold is empirical and may be tuned per domain via
`RETRIEVAL_COSINE_THRESHOLD` based on observed false-positive / false-negative
rates after the first batch of KAs.

#### SPEC-level validity

A `domain-documents` skill run is **valid** when:
- `Scoping.md` exists and contains identity, canonical schema, evidence table, artifact plan table, conflict table.
- `Scoping.md` contains Subject coverage, active authority basis, and SCA/supersession impact summary when those inputs are available.
- Each planned Knowledge Artifact file exists and includes the default section schema for its base type.
- Each planned Knowledge Artifact is comprehensive for its Knowledge Subject within the accepted source/SCA authority boundaries.
- Missing information is represented as `TBD`, not fabricated.
- `_MEMORY.md` / `MEMORY.md`, when present, was read with `_STATUS.md` and
  not used as factual authority.
- Cross-artifact consistency checks were run (Pass 2) or explicitly skipped by directive.
- Source-fidelity verification was run (Pass 3) against the authoritative source, or explicitly skipped by directive.
- `_STATUS.md` is updated only under safe-update rules (`OPEN → INITIALIZED` only when Pass 1/2 ran).

A `domain-documents` skill run is **invalid** when:
- Files are overwritten while `Current State` is outside `ALLOW_OVERWRITE_STATES`.
- `ALLOW_OVERWRITE_OVERRIDE` is used without `SCA_AUTHORIZED` or without complete SCA inputs.
- `SUPERSESSION_MAP_PATH` is provided without `AUTHORITY_MODE: SCA_DRIVEN`.
- In `SCA_DRIVEN` mode, source material overrides accepted SCA/decomposition truth.
- `_CONTEXT.md`, `_REFERENCES.md`, or `_SEMANTIC.md` are modified.
- Identity is ambiguous and not reported as `FAILED_INPUTS`.
- Content is invented rather than marked `TBD` / `ASSUMPTION`.
- No authoritative source file was read for any pass (run should have returned `FAILED_INPUTS`).
- Pass 3 ran but the source file was not actually read (source fidelity cannot be claimed without source access).
- Pass 3 corrections were applied without recording source reread evidence in the Source-Fidelity Log.
- `SEMANTIC_READY` state was introduced (not a valid DOMAIN lifecycle state).

#### Failure reporting

| Condition | Report |
|---|---|
| `DECOMP_VARIANT != DOMAIN` | `RUN_STATUS=UNSUPPORTED_VARIANT` |
| `Current State` outside `ALLOW_OVERWRITE_STATES` | `RUN_STATUS=SKIPPED_PROTECT_HUMAN_WORK` + observed state |
| `SUPERSESSION_MAP_PATH` without `AUTHORITY_MODE: SCA_DRIVEN` | `RUN_STATUS=FAILED_INPUTS` |
| `ALLOW_OVERWRITE_OVERRIDE` without complete SCA authority inputs | `RUN_STATUS=FAILED_INPUTS` |
| Source file inaccessible in `SOURCE_FIDELITY` mode | `RUN_STATUS=FAILED_INPUTS` (no pass should proceed without source access) |
| Multiple KTY rows match identity | `RUN_STATUS=FAILED_INPUTS` (ambiguous identity) with evidence |
| `P3_ONLY` with no existing `KA-*.md` files | `RUN_STATUS=FAILED_INPUTS` |
| `_CONTEXT.md` missing or listed references inaccessible | Record as missing; treat content as `TBD`; do not fail |
| Decomposition CSVs missing | Best-effort; do not fail unless identity becomes ambiguous |

#### Success case

A clean run reports:
- `RUN_STATUS=OK`
- `KTY_PATH` processed
- Count of Knowledge Artifacts created/updated
- `_STATUS.md` state transition (or explicit note that update was skipped)
- `AUTHORITY_MODE` used, including whether `SCA_DRIVEN` authority and `SUPERSESSION_MAP_PATH` were applied
- Passes executed (per `RUN_PASSES` directive)
- Pass 3 Source-Fidelity Log entry counts (corrections, gaps, unverified) when Pass 3 ran
- Count of Conflict Table entries awaiting human ruling (may be zero)
- No warnings (or explicit statement of any encountered)

#### QA Contract summary

After completing the pass directive, the skill verifies:

| Check | Validation |
|---|---|
| Scoping exists | `Scoping.md` present |
| Artifacts exist | All artifacts listed in Scoping exist as `.md` files |
| Default sections present | All default schema headings exist in each Knowledge Artifact |
| Authoritative source read | Source file(s) referenced by `SourceSpan` were successfully accessed and read |
| Substantive claims source-grounded | Artifact content grounded in source slices, not only decomposition summaries |
| KA set comprehensive | KTY-local KA set captures the full approved Knowledge Subject scope, not merely a source summary |
| TBDs for unknowns | Missing information is `TBD`, not invented |
| Assumptions labeled | Inferred content is labeled `ASSUMPTION` |
| Sources cited | Non-trivial values/requirements cite sources (or are marked `location TBD`) |
| Decomposition not overstated | Decomposition-derived claims do not exceed what the source material supports |
| Cross-doc consistency | Identity/evidence pointers consistent, or conflicts recorded |
| Source fidelity verified (Pass 3) | Every substantive source claim compared against artifact; corrections logged in Source-Fidelity Log |
| Pass 3 source rereads evidenced | Each correction/enrichment records which source slice was re-read |
| Status update safe | `_STATUS.md` only modified per safe-update rules |

## Component: skills/domain-documents/SKILL.md

---
name: domain-documents
description: Draft knowledge-artifact document set for a DOMAIN Knowledge Type deliverable. Produces KA-* files per the variable artifact schema. DOMAIN pipeline only.
compatibility: Chirality TASK; dispatched by ORCHESTRATOR setup pipeline for DOMAIN variant (Phase 2.2).
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — domain-documents

#### Purpose

Draft and iteratively enrich a **schema-driven, variable document set** for one DOMAIN Knowledge Type folder. This skill is the DOMAIN replacement for the `four-documents` skill (PROJECT/SOFTWARE), which generates a fixed four-document kit. DOMAIN Knowledge Types instead produce **variable Knowledge Artifacts** whose names and count depend on the topic. The skill derives those artifacts **from decomposition Knowledge Subjects** and grounds them in authoritative source material.

Invariant: each decomposition Knowledge Subject maps to exactly one Knowledge Artifact file.

Comprehensiveness invariant: the set of `KA-*.md` files in a KTY is expected to be maximally comprehensive for that KTY's approved Knowledge Subjects. "Maximally comprehensive" means every material source-backed fact, parameter, scope boundary, interface, assumption, exception, open issue, and current-state authority note that belongs to the Knowledge Subject is captured in the corresponding KA. The skill must not treat KAs as summaries of the source; they are contextual knowledge artifacts for downstream engineering use.

**Two-layer model:**
- **Knowledge Subject (`SUB-*`)** = the decomposition-layer topic identity inside the Knowledge Type
- **Knowledge Artifact (`KA-*`)** = the document-layer file materialized from exactly one Knowledge Subject
- `Scoping.md` = the Knowledge-Type-level entrypoint that records the `SubjectID -> ArtifactID -> Filename` mapping; it is not itself a Knowledge Subject

**DOMAIN pipeline only.** This skill is NOT called by PROJECT or SOFTWARE variants. The DOMAIN pipeline chain is `PREPARATION → TASK+domain-documents → WORKING_ITEMS` (no `semantic-matrix-build`, no `lens-register`, no `four-documents`). The quality gate is **source fidelity** (does the extraction faithfully represent the authoritative source?), not semantic enrichment.

##### Relationship to the HBA / atomic-ledger layer (runtime-use framing)

In domains where a merged **Atomic_Domain_Ledger** (HBA layer) and a retrieval index over it exist (e.g., piping-design v1.1+), KAs operate as **contextual enrichment** for HBA-anchored retrieval, not as exhaustive enumerations of the HBA pool. End-user queries hit HBAs directly via semantic retrieval; the KA's job at runtime is to provide synthesized framing, adjacent context, cross-source equivalence judgments, reconciliation notes, and scope qualifiers for whatever HBAs the retrieval surfaces.

Implication for authoring:
- A KA citing 17 well-chosen HBAs from a 1,000-HBA pool can serve its runtime purpose as well as one citing 1,000 mechanically — *provided* the cited HBAs and synthesized narrative span the topic-space coherently.
- **Coverage of the HBA pool is not the goal; coherent thematic coverage of the KTY's topic is.** Citation count is not a target.
- The defects that matter are **missing KAs** (no contextualization layer at all for that KTY's topic) and **orphan HBAs** (HBAs semantically distant from any cited HBA). These are the only coverage-shape signals the skill should optimize against.

This refines the "Maximally comprehensive" invariant above: comprehensive in *narrative substance* (every material source-backed fact captured at the prose level), not in *citation enumeration* (citing every HBA in the parent KTY's ledger pool). Use the diagnostic preflight (`tools/diagnostics/ka_coverage_audit.py` in domains where present) before authoring to surface missing/lean/orphan defects for the human's awareness.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

Typical dispatcher: ORCHESTRATOR Phase 2.2 (DOMAIN variant) dispatches TASK with `TaskSkill: domain-documents`.

#### Inputs

##### Required

- `KTY_PATH` — absolute path to one Knowledge Type folder
- `DECOMPOSITION_REF` — path to DOMAIN decomposition folder or doc(s)

##### Optional

- `DECOMP_VARIANT` — must be `DOMAIN` (this skill is DOMAIN-only); default `DOMAIN`
- `RUN_PASSES` — `FULL` | `P1_P2` | `P3_ONLY`; default `FULL`
- `ALLOW_OVERWRITE_STATES` — which `_STATUS.md` states permit overwrite; default `OPEN, INITIALIZED`
- `AUTHORITY_MODE` — `SOURCE_FIDELITY` | `SCA_DRIVEN`; default `SOURCE_FIDELITY`
- `SCA_SNAPSHOT_PATH` — accepted SCOPE_CHANGE snapshot path; required when `AUTHORITY_MODE: SCA_DRIVEN`
- `SUPERSESSION_MAP_PATH` — accepted supersession map; valid only when `AUTHORITY_MODE: SCA_DRIVEN`
- `ROOT_NAME` — canonical execution root name for supersession applicability filtering
- `FACILITY_ID` — facility identifier for supersession applicability filtering
- `ALLOW_OVERWRITE_OVERRIDE` — `SCA_AUTHORIZED` permits active content writes for the dispatched KTY only when SCA snapshot inputs are present
- `UNIT_SCOPE` — `EXAMPLES_ONLY` | `ALL_MAPPED`; default `EXAMPLES_ONLY`
- `ARTIFACT_NAMING` — `PREFIXED_TYPED_SLUG` | `TYPED_SLUG` | `PREFIXED_SLUG`; default `PREFIXED_TYPED_SLUG`
- `MAX_ARTIFACTS` — hard cap on artifact files; default `25`
- `SOURCES_ROOT` — path to shared source/reference files
- `COMBINED_SOURCE_AUTHORITY_PATH` — optional additional admitted source authority root for combined/cross-root source packages

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `KTY_PATH` | Path to one Knowledge Type folder | **Required** | Absolute directory path |
| `DECOMPOSITION_REF` | Path to DOMAIN decomposition folder or doc(s) | **Required** | Absolute path |
| `DECOMP_VARIANT` | Variant this skill supports | `DOMAIN` | `DOMAIN` only |
| `RUN_PASSES` | Which enrichment passes to run | `FULL` | `FULL`, `P1_P2`, `P3_ONLY` |
| `ALLOW_OVERWRITE_STATES` | Safe-update gate | `OPEN, INITIALIZED` | Comma-separated state list |
| `AUTHORITY_MODE` | Factual authority policy | `SOURCE_FIDELITY` | `SOURCE_FIDELITY`, `SCA_DRIVEN` |
| `SCA_SNAPSHOT_PATH` | Accepted SCOPE_CHANGE snapshot | omitted | Required when `AUTHORITY_MODE: SCA_DRIVEN` |
| `SUPERSESSION_MAP_PATH` | Accepted cumulative supersession map | omitted | Required and valid only when `AUTHORITY_MODE: SCA_DRIVEN` |
| `ROOT_NAME` | Canonical execution root name | omitted | String |
| `FACILITY_ID` | Facility identifier | omitted | String |
| `ALLOW_OVERWRITE_OVERRIDE` | SCA-controlled content write override | omitted | `SCA_AUTHORIZED` only |
| `UNIT_SCOPE` | Which handbook units to use as evidence | `EXAMPLES_ONLY` | `EXAMPLES_ONLY`, `ALL_MAPPED` |
| `ARTIFACT_NAMING` | How to name artifact files | `PREFIXED_TYPED_SLUG` | `PREFIXED_TYPED_SLUG`, `TYPED_SLUG`, `PREFIXED_SLUG` |
| `MAX_ARTIFACTS` | Hard cap on artifact count | `25` | Positive integer |
| `SOURCES_ROOT` | Root-local source/reference files | Provided by dispatcher | Absolute path |
| `COMBINED_SOURCE_AUTHORITY_PATH` | Additional admitted source authority root for combined/cross-root source packages | omitted | Absolute path |
| `RETRIEVAL_INDEX_PATH` | Path to a V2 source database snapshot or `_LATEST.md` pointer used by the Pass 4 audit-on-write check | omitted | Absolute path to `<domain-root>/_LocalIndexes/_LATEST.md` or a `SRCIDX_*` snapshot containing `catalog.sqlite`, `bm25/`, and optional `embeddings_norm.npy` |
| `RETRIEVAL_QUERY_TOOL` | Path to the V2 source retrieval query CLI invoked for batch/single queries | omitted (default: `tools/retrieval/query_source_index.py`) | Path to an executable Python CLI accepting `--snapshot`, `--query`, `--batch`, `--k`, filter flags, and `--json` |
| `RETRIEVAL_COSINE_THRESHOLD` | Cosine score above which an uncited HBA in retrieval top-K triggers a WARN verdict in Pass 4 | `0.75` | Float in `[0.0, 1.0]` |
| `UNIT_SCOPE` values | `EXAMPLES_ONLY` → use `KnowledgeTypes.csv.ExampleUnitIDs`; `ALL_MAPPED` → use all units mapped to this KTY in `DomainLedger.csv` (best-effort) | — | — |
| `ARTIFACT_NAMING` values | `PREFIXED_TYPED_SLUG` → `KA-01_{Type}__{Slug}.md`; `TYPED_SLUG` → `{Type}__{Slug}.md`; `PREFIXED_SLUG` → `KA-01_{Slug}.md` | — | — |

#### Tool usage

- No deterministic tools for drafting. This is a reasoning-first extraction + authoring skill.
- Preferred utility script (for safe status updates):
  - `tools/scaffolding/write_status.sh` — update `_STATUS.md` under safe-update rules only.
- The `allowed-tools` frontmatter field is intentionally omitted.

Disallowed behavior:
- No modification of metadata files: `_CONTEXT.md`, `_REFERENCES.md`, `_MEMORY.md`/`MEMORY.md`, `_SEMANTIC.md`.
- `_MEMORY.md` / `MEMORY.md` may be read only as non-authoritative operational
  context when `_STATUS.md` is read.
- No overwriting Knowledge Artifact files when `Current State` is outside `ALLOW_OVERWRITE_STATES`.
- No cross-Knowledge-Type scanning — one Knowledge Type folder per run.
- No fabrication of source excerpts when the source file is inaccessible.

#### Outputs

- `Scoping.md` in `{KTY_PATH}` — stable entrypoint with identity, canonical schema, evidence table, artifact plan table, conflict table, source-fidelity log
- Variable `KA-*.md` Knowledge Artifact files in `{KTY_PATH}` (one per Knowledge Subject)
- `_STATUS.md` updated (OPEN → INITIALIZED only when Pass 1/2 ran)

##### Conditional outputs (when domain artifacts indicate)

- **`Contradictions_Register.csv` rows** — when the authoring agent surfaces a cross-source contradiction (different rule, different threshold, different formula on the same topic from different source documents) while drafting a KA, append a row to `{DECOMPOSITION_ROOT}/Contradictions_Register.csv` with columns `CitationA, CitationB, Topic, ScopeDifference, Disposition, FoundByKA` (create the file if it does not yet exist; same authoring authority as `Coverage_Gaps_Register.csv` under AOP-08). The KA's "Reconciliation Notes" appendix references these rows. `Disposition` is the agent's recommendation; the human or SCOPE_CHANGE rules.

#### Authority hierarchy

##### `AUTHORITY_MODE: SOURCE_FIDELITY` (default)

When drafting or revising Knowledge Artifact content, consult sources in this order of authority:

1. **Authoritative source material** — original source file(s) referenced by `SourceSpan` in the decomposition and/or listed in `_REFERENCES.md`, located under `{SOURCES_ROOT}`, `COMBINED_SOURCE_AUTHORITY_PATH`, or local `_Sources/`
2. **KTY-local reference pointers** — `_REFERENCES.md` (additional cited sources relevant to this Knowledge Type)
3. **Decomposition data** — `KnowledgeTypes.csv`, `HandbookUnits.csv`, `DomainLedger.csv` (scope, structure, evidence pointers)
4. **Existing drafted files** — prior versions of Knowledge Artifacts and `Scoping.md` (context only, not authority)

When source material and decomposition data disagree, source material is authoritative. Decomposition scopes and routes; source determines what the artifact must say. Record discrepancies in the Conflict Table. Do not treat decomposition summaries, atomic statements, or prior draft wording as if they were the source.

**Source slice:** the smallest local source region that preserves meaning for a cited claim. Includes the cited heading or section, its opening prose, embedded tables or lists, and the immediate parent heading when it frames scope. Adjacent exception or exclusion material should be included when it qualifies the claim.

##### `AUTHORITY_MODE: SCA_DRIVEN`

Use this mode only when SCOPE_CHANGE dispatches this skill to regenerate active
KTY content after an accepted amendment.

In SCA-driven mode, current factual authority is:

1. admitted decomposition state,
2. structured SCA artifacts in `SCA_SNAPSHOT_PATH`, especially
   `Amendment_Actions.csv`, `KTY_Remediation_Manifest.csv`, and
   `Supersession_Delta.csv`,
3. `SUPERSESSION_MAP_PATH`.

Source material is provenance verification only. It must not override accepted
SCA/decomposition truth. If source material conflicts with structured SCA
truth, preserve the SCA-driven fact, cite the relevant supersession binding,
and record the source conflict in the Conflict Table or Source-Fidelity Log.
Do not infer supersessions from SCA prose; supersession authority comes only
from structured SCA artifacts and `SUPERSESSION_MAP_PATH`.

When `ROOT_NAME` or `FACILITY_ID` is provided, filter supersession rows by
applicability fields such as `AppliesToRoots` and `AppliesToFacilities` before
applying them. A supersession row that does not apply to the dispatched
root/facility is context only and must not modify KTY content.

`SUPERSESSION_MAP_PATH` without `AUTHORITY_MODE: SCA_DRIVEN` fails input
validation. `ALLOW_OVERWRITE_OVERRIDE: SCA_AUTHORIZED` permits writing active
`Scoping.md` and `KA-*.md` only for the dispatched `KTY_PATH`, only when
`AUTHORITY_MODE: SCA_DRIVEN`, `SCA_SNAPSHOT_PATH`, and
`SUPERSESSION_MAP_PATH` are present.

#### Method

##### Step 0 — Preconditions & Safety Checks

1. Read `{KTY_PATH}/_STATUS.md` (if present) to determine `Current State`.
   When `_STATUS.md` is read, also read sibling `_MEMORY.md` or `MEMORY.md`
   when present as non-authoritative operational context. Memory may explain
   local continuity or caveats, but it is never factual authority and must not
   override decomposition, SCA, supersession, or source authority.
2. Resolve `AUTHORITY_MODE`:
   - omitted or `SOURCE_FIDELITY` → existing source-fidelity behavior
   - `SCA_DRIVEN` → require `SCA_SNAPSHOT_PATH` and `SUPERSESSION_MAP_PATH`
   - `SUPERSESSION_MAP_PATH` without `AUTHORITY_MODE: SCA_DRIVEN` → return `RUN_STATUS=FAILED_INPUTS`
3. Resolve overwrite authority:
   - If `Current State` is in `ALLOW_OVERWRITE_STATES`, continue under normal safe-update rules.
   - If `Current State` is not in `ALLOW_OVERWRITE_STATES` and `ALLOW_OVERWRITE_OVERRIDE: SCA_AUTHORIZED` is not present:
     - Do not overwrite or create Knowledge Artifact documents.
     - Return `RUN_STATUS=SKIPPED_PROTECT_HUMAN_WORK` + the observed state.
   - If `ALLOW_OVERWRITE_OVERRIDE: SCA_AUTHORIZED` is present, continue only when `AUTHORITY_MODE: SCA_DRIVEN`, `SCA_SNAPSHOT_PATH`, and `SUPERSESSION_MAP_PATH` are all present. The override applies only to active `Scoping.md` / `KA-*.md` files in the dispatched `KTY_PATH`.
   - `ALLOW_OVERWRITE_OVERRIDE` with any other value, or without complete SCA inputs, returns `RUN_STATUS=FAILED_INPUTS`.
4. Interpret `RUN_PASSES`:
   - `FULL` → run Steps 1–7 as written.
   - `P1_P2` → run Steps 1–5 and then Step 7 (status update).
   - `P3_ONLY` → run Step 1 (full reads including source files), Step 6 (source-fidelity verification), and Step 7; do not re-run Pass 1 drafting.
5. If `DECOMP_VARIANT` is not `DOMAIN`: return `RUN_STATUS=UNSUPPORTED_VARIANT`. This skill is DOMAIN-only; PROJECT/SOFTWARE use the `four-documents` skill.

**Additional preconditions for `P3_ONLY`:**
- At least one Knowledge Artifact `.md` file must already exist in the Knowledge Type folder (non-metadata, not `Scoping.md`).
- In `SOURCE_FIDELITY` mode, the authoritative source file(s) referenced in `_REFERENCES.md` and/or `SourceSpan` fields in the decomposition data must be accessible.
- In `SCA_DRIVEN` mode, structured SCA authority must be accessible; source access gaps are reported as provenance gaps and must not override SCA truth.
- If required authority for the selected mode is missing: return `RUN_STATUS=FAILED_INPUTS` (do not modify files).

##### Step 1 — Read Context & Decomposition Data (always)

1. Read `{KTY_PATH}/_CONTEXT.md` (best-effort). Extract: KnowledgeType ID, name, parent category, description, decomposition pointer.
2. Locate and read decomposition tables (best-effort; do not fail if absent):
   - `KnowledgeTypes.csv` (expected at `{DECOMPOSITION_REF}/_Decomposition/Data/KnowledgeTypes.csv` or nearby)
   - `HandbookUnits.csv` (expected at `{DECOMPOSITION_REF}/_Decomposition/Data/HandbookUnits.csv` or nearby)
   - Optional: `DomainLedger.csv` (expected at `{DECOMPOSITION_REF}/_Decomposition/Data/DomainLedger.csv` or nearby)
3. Identify the KTY decomposition row:
   - Prefer exact match by `KnowledgeTypeID` from `_CONTEXT.md`.
   - If `_CONTEXT.md` is missing/ambiguous, infer `KnowledgeTypeID` from folder name token `KTY-*`.
   - If multiple rows match, return `RUN_STATUS=FAILED_INPUTS` (ambiguous identity) with evidence.
4. Extract these KTY fields (do not infer):
   - `CanonicalSchema`
   - `KnowledgeSubjects` (ordered set driving the artifact plan)
   - `ExampleUnitIDs`
   - `Description`, `IntendedUsers`, `WhenUsed`
   - `ParentCategoryID`, `ParentCategoryName`
5. Read `{KTY_PATH}/_REFERENCES.md` (best-effort) to identify accessible reference materials. Do not dereference URLs. If listed references cannot be accessed, record as missing and treat content as `TBD`.
6. Resolve authority files for this Knowledge Type:
   - Extract `SourceSpan` from the KTY row in `KnowledgeTypes.csv` (format: `{filename}:{startLine}-{startLine} -> {filename}:{endLine}-{endLine}`).
   - Parse the source filename and line ranges.
   - Locate the source file under `{SOURCES_ROOT}`, `COMBINED_SOURCE_AUTHORITY_PATH`, or the path specified in `_REFERENCES.md`.
   - In `SOURCE_FIDELITY` mode: read the source file section(s) bounded by `SourceSpan`. If the source file cannot be accessed, return `RUN_STATUS=FAILED_INPUTS` (no pass should proceed without source access).
   - In `SCA_DRIVEN` mode: read structured SCA artifacts and `SUPERSESSION_MAP_PATH` first. Apply `ROOT_NAME` / `FACILITY_ID` filters when present. Read source slices when available for provenance verification only; if inaccessible, record a provenance gap rather than inventing or overriding facts.

##### Step 2 — Parse Draft Plan (Pass 1 only)

1. Parse `KnowledgeSubjects` for this KTY into an ordered subject list:
   - Each Knowledge Subject represents one discrete domain topic and drives exactly one artifact file.
   - Do not split a single Knowledge Subject across multiple artifact files.
   - Do not merge multiple Knowledge Subjects into one artifact file.
   - Keep ordering stable (use SubjectID order when available).
   - If no Knowledge Subjects are found: create a single fallback artifact spec: `Overview (TBD)`.
2. Parse `ExampleUnitIDs` into a unit list (accept JSON list, Python list string, or semicolon-delimited; best-effort).
3. Build the evidence set based on `UNIT_SCOPE`:
   - `EXAMPLES_ONLY` → use `ExampleUnitIDs`
   - `ALL_MAPPED` → use all `UnitID` values from `DomainLedger.csv` where `KnowledgeTypeID(s)` includes this KTY (best-effort)
4. For each unit in the evidence set, look up in `HandbookUnits.csv`:
   - `AtomicStatement`
   - `SourceRef`
   - If a unit cannot be found: record it as missing and include `TBD` placeholders.
5. Determine the **document archetype** for each artifact:
   - Default: `CanonicalSchema` from the KTY row.
   - Additive "artifact-specific add-ons" (structural only) based on keywords in the Subject name or description:
     - contains `checklist` → add `CHECKLIST_BLOCK`
     - contains `template` or `log` or `form` → add `TEMPLATE_BLOCK`
     - contains `procedure` or `steps` → add `PROCEDURE_BLOCK`
     - contains `glossary` or `terms` → add `REFERENCE_BLOCK`
   - Record any add-ons in `Scoping.md` and the `Decision_Log` section inside `Scoping.md`.
   - Do not treat add-ons as evidence; they are scaffolding conveniences.
6. Determine output filenames using `ARTIFACT_NAMING` policy:
   - `Slug` = filesystem-safe slug from the Knowledge Subject name (letters/numbers/hyphen; collapse whitespace).
   - `Type` = base archetype (`Reference|Guidance|Checklist|Procedure`) from `CanonicalSchema`.
   - If the slug is empty, use `TBD`.
   - Apply a stable ordinal prefix when policy includes `PREFIXED_*`.

**Output:** A deterministic artifact plan: ordered list of `{ArtifactID, SubjectID, SubjectName, BaseType, AddOns, Filename}` plus evidence unit table.
- `SubjectID` is the decomposition-layer identifier.
- `ArtifactID` / `Filename` are the document-layer identifiers derived from that subject.

##### Step 3 — Establish Default Section Schemas (Pass 1 only)

**Default schema sections (keep stable):**

| Base Type (`CanonicalSchema`) | Default Schema Sections |
|---|---|
| Reference | Identification, Scope, Definitions, Reference Content, Exceptions/Addenda, References |
| Guidance | Purpose, Applicability, Guidance Statements, Rationale, Examples, References |
| Checklist | Purpose, Applicability, Checklist, Evidence/Records, Notes, References |
| Procedure | Purpose, Prerequisites, Steps, Verification, Records, References |

Sections may be added if the artifact spec requires it, but defaults must not be removed.

**Artifact-specific add-on blocks (structural only):**
- `CHECKLIST_BLOCK` → add a checklist table section
- `TEMPLATE_BLOCK` → add a template/form fields section
- `PROCEDURE_BLOCK` → add a step table section
- `REFERENCE_BLOCK` → add a term/definition table section

Add-ons are **additive** and do not change the base type.

##### Step 4 — Generate Documents (Pass 1)

Using the draft plan + evidence set, generate documents in `{KTY_PATH}`.

**Source-grounding rule (`SOURCE_FIDELITY`):** When the authoritative source file is accessible, artifact prose MUST be grounded in the relevant source slices — not only in decomposition summaries, atomic statements, or prior draft wording. Decomposition scopes and structures; the source determines what the artifact must say.

**SCA-grounding rule (`SCA_DRIVEN`):** Artifact prose MUST be grounded in admitted decomposition state, structured SCA artifacts, and `SUPERSESSION_MAP_PATH`. Source material may verify provenance but must not override accepted SCA/decomposition truth.

###### 4a) `Scoping.md` (stable entrypoint; always generated in Pass 1)

Create/overwrite `Scoping.md` with:
- Identity (KTY + Category) — from decomposition row / `_CONTEXT.md`
- `CanonicalSchema`
- Intended users and when-used context
- Category / KTY / Knowledge Subject coverage summary — what the KTY exists to cover and which subjects are materialized as KAs
- Active authority basis — source-fidelity mode or SCA-driven mode, including admitted SCA snapshot and supersession map when applicable
- SCA / supersession impact summary — required in `AUTHORITY_MODE: SCA_DRIVEN`; records what changed at a current-state level without turning SCA process history into body prose
- Evidence set table (UnitID → AtomicStatement → SourceRef)
- Artifact plan table (ArtifactID → SubjectID → SubjectName → BaseType → AddOns → Filename)
- Treat the Artifact plan table as the authoritative bridge between the decomposition layer (`SubjectID`) and the document layer (`ArtifactID`, `Filename`).
- Open questions / `TBD` list
- Conflict Table (for human ruling)

Conflict Table schema (keep stable):

`## Conflict Table (for human ruling)`

Columns:
- Conflict ID
- Conflict (short statement)
- Source A (file + section)
- Source B (file + section)
- Impacted artifacts
- Proposed authority (PROPOSAL)
- Human ruling (TBD)

###### 4b) Knowledge Artifact docs (`KA-*.md` as planned)

For each planned artifact, create/overwrite the target file with:

1. Title: `# {ArtifactSpec}`
2. Artifact Metadata block:
   - Knowledge Type: ID + Name
   - Category: ID + Name
   - Knowledge Subject: SubjectID + Name (decomposition layer)
   - Artifact ID: `KA-##` (document layer)
   - Base Type: `{Reference|Guidance|Checklist|Procedure}`
   - Add-ons: list (if any)
   - Evidence Units: list (UnitIDs)
3. Default sections for the Base Type (Step 3 table)
4. Populate content comprehensively for that Knowledge Subject. Each KA should cover, when available and in scope:
   - subject purpose and applicability,
   - current-state factual basis,
   - design values, operating conditions, capacities, limits, and specifications,
   - relevant interfaces and dependencies,
   - assumptions, exceptions, exclusions, and open issues,
   - source-fidelity notes or SCA/supersession basis required to understand the current state.
5. Populate content **only** from:
   - decomposition fields (`Description`, `IntendedUsers`, `WhenUsed`)
   - `HandbookUnits.csv.AtomicStatement` (and `SourceRef` pointers)
   - accessible references listed in `_REFERENCES.md` (best-effort)
   - in `SCA_DRIVEN` mode, admitted structured SCA artifacts and `SUPERSESSION_MAP_PATH`
6. Use `TBD` when information is missing; do not invent values.
7. Label inferences as **ASSUMPTION**.
8. If contradictions appear:
   - add a row to `Scoping.md` Conflict Table with evidence pointers,
   - reference the Conflict ID in the affected artifact doc(s).

**Source excerpt rule (optional, best-effort):**
- If the source file referenced in `SourceRef` is accessible under the workspace's sources root, a short excerpt may be included.
- Always include the pointer (`SourceRef`) and never fabricate excerpt text if the source cannot be accessed.

##### Step 5 — Cross-Artifact Consistency Check (Pass 2)

**Purpose:** Verify that the generated Scoping.md and Knowledge Artifact files form a coherent, internally consistent document set. This pass reads all generated content; it does not compare against the authoritative source (that is Pass 3).

1. Read every generated artifact file in `{KTY_PATH}` (Scoping.md + all KA-*.md files).
2. **Structural completeness:**
   - Every artifact listed in `Scoping.md` artifact plan table exists as a `.md` file.
   - Every KA-*.md file in the folder appears in the artifact plan table.
   - No duplicate filenames.
   - Each artifact contains all default schema sections for its base type.
3. **Identity consistency:**
   - KTY ID, Name, and Category are consistent across Scoping.md and all artifact metadata blocks.
   - SubjectID ↔ ArtifactID mappings in artifact metadata match the Scoping.md plan table.
4. **Cross-artifact value consistency:**
   - Where multiple artifacts reference the same parameter, design value, equipment tag, or operating condition, verify the values are identical or non-contradictory.
   - Where a value appears in both a "design basis" artifact and a "component detail" artifact, verify agreement.
5. **Evidence traceability:**
   - Every non-trivial claim in an artifact cites a UnitID, SourceRef, or is marked TBD/ASSUMPTION.
   - UnitIDs referenced in artifacts exist in the evidence set table in Scoping.md.
   - SourceRef pointers are syntactically consistent across all docs.
6. **Terminology consistency:**
   - Same terms used consistently across artifacts (prefer VocabularyMap.csv canonical terms if available).
   - Flag synonym drift (e.g., "inlet separator" vs "inlet knock-out drum") as Conflict Table entries unless resolved by VocabularyMap.
7. Fix inconsistencies when resolvable from the generated documents themselves or from the decomposition data.
8. Re-open authoritative source slices when:
   - values differ across artifacts and the correct value is not obvious from drafts alone,
   - identity or terminology inconsistencies cannot be resolved from draft text,
   - claims appear to overstate what the decomposition supports and may need source verification,
   - contradictions between Scoping.md and artifact content cannot be resolved locally.
9. If not resolvable:
   - prefer `TBD` over guessing,
   - add Conflict Table entries in `Scoping.md` with pointers to both artifacts.

##### Step 6 — Source-Fidelity Verification (Pass 3)

**Purpose:** Verify and enrich the generated Knowledge Artifacts against the active authority mode. For ordinary DOMAIN drafting, the source document (e.g., the DBM) is the ground truth — not a semantic lensing register. For `AUTHORITY_MODE: SCA_DRIVEN`, admitted decomposition state, structured SCA artifacts, and `SUPERSESSION_MAP_PATH` are the current factual authority.

> **Design note:** The `four-documents` skill (PROJECT/SOFTWARE) uses semantic enrichment (`semantic-matrix-build` → `lens-register` → Pass 3 lensing). `domain-documents` does not. Domain Knowledge Types are extracted from a specific authoritative source, so the quality gate is source fidelity: does the extraction faithfully and completely represent the source?

###### 6a) Preconditions
- The selected authority inputs must be accessible (resolved in Step 1, item 6).
- At least one Knowledge Artifact `.md` file must exist.
- In `SOURCE_FIDELITY` mode, if the source file cannot be read: return `RUN_STATUS=FAILED_INPUTS`.
- In `SCA_DRIVEN` mode, if structured SCA authority cannot be read: return `RUN_STATUS=FAILED_INPUTS`; source access gaps are recorded as provenance gaps.

###### 6b) Read source sections
1. In `SOURCE_FIDELITY` mode, read the source file section(s) bounded by `SourceSpan` for this KTY. In `SCA_DRIVEN` mode, read admitted decomposition rows, structured SCA artifacts, and `SUPERSESSION_MAP_PATH` first; source slices are secondary provenance checks.
2. For each Knowledge Subject within this KTY, identify the corresponding source section using the Subject-level `SourceSpan` (from the Knowledge Subject Register) or by locating the subject anchor within the KTY source span.

###### 6c) Verify coverage (source → artifacts)
For each substantive statement, requirement, design value, or parameter in the source section:
1. Locate the corresponding content in the generated KA file(s).
2. If the source content is present and faithfully represented: no action.
3. If the source content is present but the artifact misrepresents it (wrong value, wrong context, incomplete): correct the artifact and record the correction in Scoping.md under a `## Source-Fidelity Log` section.
4. If the source content is not captured in any artifact: add it to the appropriate KA file (or flag as a gap in Scoping.md if the content falls outside all Subject boundaries).

###### 6d) Verify accuracy (artifacts → source)
For each non-TBD, non-ASSUMPTION claim in the generated artifacts:
1. Confirm it traces to a specific source location (SourceRef or line range).
2. If a claim cannot be traced to the source: mark it as `UNVERIFIED` or downgrade to `ASSUMPTION`.
3. If a claim contradicts the source: correct it and log the correction.

###### 6e) Update Scoping.md
- Add or update `## Source-Fidelity Log` with:
  - Corrections made (artifact, section, what changed, source evidence)
  - Gaps found (source content not captured, with source location)
  - Unverified claims (artifact content that could not be traced to source)
  - **Source reread evidence:** for each correction or enrichment, record which source slice was re-read before the change was applied
- Update the Conflict Table if source-artifact contradictions require human ruling.

###### 6f) Final structural sweep
After source-fidelity corrections, re-run the Step 5 structural completeness checks (items 1–3) to ensure no artifacts were broken by corrections.

##### Step 7 — Update Status (safe update only)

- Read `_STATUS.md` and identify the current state.
- Whenever `_STATUS.md` is read in this step, read sibling `_MEMORY.md` or
  `MEMORY.md` when present as non-authoritative operational context only.
- If `RUN_PASSES` includes Pass 1 or Pass 2 (i.e., `FULL` or `P1_P2`):
  - If (and only if) current state is `OPEN`, update: `tools/scaffolding/write_status.sh {kty_folder} INITIALIZED TASK+domain-documents`
- If current state is not `OPEN`, do not modify `_STATUS.md` (no state regression). Report that the status update was skipped.

**Output:** Knowledge Type folder contains `Scoping.md` and the planned Knowledge Artifact documents updated per pass directive, and `_STATUS.md` updated only when safe/applicable.

#### Non-negotiable constraints

- **DOMAIN pipeline only.** This skill is invoked exclusively for DOMAIN Knowledge Types. If `DECOMP_VARIANT != DOMAIN`, halt with `UNSUPPORTED_VARIANT`. PROJECT/SOFTWARE variants use the `four-documents` skill.
- **One deliverable per run.** Each invocation processes exactly one Knowledge Type folder (`KTY_PATH`). No cross-Knowledge-Type scanning.
- **No human input.** The skill works from folder contents, references, and decomposition data. The human does not directly interact with this skill.
- **Respect human work.** `_STATUS.md` state must be within `ALLOW_OVERWRITE_STATES` (default: `OPEN, INITIALIZED`) before overwriting any Knowledge Artifact file. Otherwise halt with `SKIPPED_PROTECT_HUMAN_WORK`.
- **SCA overwrite override is narrow.** `ALLOW_OVERWRITE_OVERRIDE: SCA_AUTHORIZED` is valid only with `AUTHORITY_MODE: SCA_DRIVEN`, `SCA_SNAPSHOT_PATH`, and `SUPERSESSION_MAP_PATH`; it applies only to active `Scoping.md` / `KA-*.md` files for the dispatched `KTY_PATH`.
- **No metadata modification.** Never modify `_CONTEXT.md`, `_REFERENCES.md`, `_MEMORY.md`/`MEMORY.md`, or `_SEMANTIC.md`. If regenerated content reveals metadata drift (e.g., `_CONTEXT.md` name or description no longer matches the regenerated `Scoping.md`), surface it as a follow-on alignment action in the skill output — do not fix it inside this skill.
- **Memory is context, not authority.** Read sibling `_MEMORY.md` / `MEMORY.md`
  whenever `_STATUS.md` is read. Use it only to preserve operational
  continuity and surface caveats; never use memory as factual source authority.
- **Subject-to-Artifact bijection.** Each Knowledge Subject maps to exactly one Knowledge Artifact file. No splitting or merging.
- **Variable artifact schema.** The artifact set is topic-dependent (no fixed 4-doc kit). Count and names derive from `KnowledgeSubjects`.
- **`KA-*` naming convention.** Default is `KA-01_{Type}__{Slug}.md`; configurable via `ARTIFACT_NAMING`. Stable ordinal prefix when policy includes `PREFIXED_*`.
- **No invention.** Missing information is `TBD`, inferences are labeled `ASSUMPTION`. Do not fabricate source excerpts when the source is inaccessible.
- **Authority fidelity is the quality gate.** Pass 3 verifies artifact-to-source fidelity in `SOURCE_FIDELITY` mode and artifact-to-SCA fidelity in `SCA_DRIVEN` mode. No semantic lensing / semantic enrichment in this pipeline.
- **Authoritative source required in default mode.** In `SOURCE_FIDELITY` mode, if the source file(s) referenced by `SourceSpan` cannot be accessed, halt with `FAILED_INPUTS` before drafting.
- **SCA authority required when selected.** In `SCA_DRIVEN` mode, admitted decomposition state, structured SCA artifacts, and `SUPERSESSION_MAP_PATH` are required. Source material is provenance verification only and must not override accepted SCA truth.
- **Structured supersession only.** Do not infer supersessions from SCA prose.
- **Safe-update status only.** `_STATUS.md` transitions `OPEN → INITIALIZED` only when Pass 1/2 ran. Never regress state.
- **No SEMANTIC_READY state.** The DOMAIN lifecycle is `OPEN → INITIALIZED → IN_PROGRESS`; `SEMANTIC_READY` is not a valid state for DOMAIN Knowledge Types.

#### QA expectations

See `QA_CHECKS.md` for the full invariant set. Summary:

- `Scoping.md` present with identity, canonical schema, evidence table, artifact plan table, conflict table.
- Every artifact listed in the plan table exists as a `.md` file; every `KA-*.md` file appears in the plan table.
- All default schema sections present per base type.
- The KA set is comprehensive for the KTY's Knowledge Subjects, with material source-backed facts, interfaces, assumptions, exceptions, and current-state authority notes captured in the appropriate artifact.
- Authoritative source file(s) accessed and read.
- Substantive claims grounded in source slices (not only decomposition summaries).
- Missing information marked `TBD`; inferences labeled `ASSUMPTION`; conflicts recorded in Conflict Table.
- Pass 3 (when run): source-fidelity corrections logged in `Source-Fidelity Log` with source reread evidence.
- `_STATUS.md` updated only under safe-update rules.

#### See also

- `agents/AGENT_ORCHESTRATOR.md` — dispatches this skill via TASK during Phase 2.2 (DOMAIN variant)
- `agents/AGENT_DOMAIN_DECOMP.md` — DOMAIN decomposition (upstream; produces KnowledgeSubjects)
- `agents/AGENT_PREPARATION.md` — creates Knowledge Type folders this skill populates
- `skills/four-documents/` — PROJECT/SOFTWARE counterpart (fixed 4-doc kit)
- `tools/EXTERNAL_TOOLS.md` — DOMAIN pipeline overview
- `.Archive/SEMANTIC_PIPELINE_ARCHITECTURE.md` — pipeline architecture context

## Component: skills/domain-documents/TOOL_POLICY.md

### domain-documents — Tool Policy

#### Preferred tool order

Reasoning-first: extraction and authoring of `Scoping.md` plus variable `KA-*.md` Knowledge Artifact files is LLM-driven across Steps 0-6. Whenever `_STATUS.md` is read, sibling `_MEMORY.md` / `MEMORY.md` must also be read when present as non-authoritative operational context. The sole operational tool invocation is at Step 7 (safe `_STATUS.md` update) when `RUN_PASSES` includes Pass 1 or Pass 2 and the current state is `OPEN`:

1. `tools/scaffolding/write_status.sh {kty_folder} INITIALIZED TASK+domain-documents` — invoked only to transition `OPEN → INITIALIZED`.

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- None — no TASK-enforced deterministic allowlist (the `allowed-tools` frontmatter field is intentionally omitted).

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- `tools/scaffolding/write_status.sh` — preferred utility script for safe `_STATUS.md` updates under safe-update rules only.

#### Expected use of reasoning

This is a reasoning-first extraction + authoring skill. No deterministic tools are used for drafting. Steps 0-6 (preconditions, context + decomposition reads, draft-plan parsing, default-schema establishment, document generation, cross-artifact consistency check, and source-fidelity verification) are all LLM-driven.

Default `AUTHORITY_MODE` is `SOURCE_FIDELITY`: artifact prose must be grounded in authoritative source slices bounded by `SourceSpan`; decomposition summaries, atomic statements, and prior draft wording are not authority.

When `AUTHORITY_MODE: SCA_DRIVEN`, admitted decomposition state, structured SCA artifacts, and `SUPERSESSION_MAP_PATH` are current factual authority. Source material is provenance verification only and must not override accepted SCA/decomposition truth. Do not infer supersessions from SCA prose. Deterministic tooling is only invoked at Step 7 for the safe status update.

#### Disallowed use

- No modification of metadata files: `_CONTEXT.md`, `_REFERENCES.md`, `_MEMORY.md`/`MEMORY.md`, `_SEMANTIC.md`. Metadata drift discovered during regeneration must be surfaced as a follow-on alignment action, not fixed inside this skill.
- No use of `_MEMORY.md` / `MEMORY.md` as factual authority. It may be read
  only as non-authoritative operational context paired with `_STATUS.md`.
- No overwriting Knowledge Artifact files when `Current State` is outside `ALLOW_OVERWRITE_STATES`.
- No use of `SUPERSESSION_MAP_PATH` unless `AUTHORITY_MODE: SCA_DRIVEN` is explicitly set; this combination otherwise fails input validation.
- No use of `ALLOW_OVERWRITE_OVERRIDE` unless it equals `SCA_AUTHORIZED` and complete SCA inputs (`AUTHORITY_MODE: SCA_DRIVEN`, `SCA_SNAPSHOT_PATH`, and `SUPERSESSION_MAP_PATH`) are present.
- No cross-Knowledge-Type scanning — one Knowledge Type folder per run.
- No fabrication of source excerpts when the source file is inaccessible.
- No hidden reliance on tools outside the declared list unless the human expands AllowedTools. No writes outside declared scope.

#### Write boundary

- Write scope: `{KTY_PATH}` only.
- Files produced/overwritten: `Scoping.md` (stable entrypoint with identity, canonical schema, evidence table, artifact plan table, conflict table, source-fidelity log) and variable `KA-*.md` Knowledge Artifact files (one per Knowledge Subject) in `{KTY_PATH}`.
- Safe-update only: `{KTY_PATH}/_STATUS.md` may transition `OPEN → INITIALIZED` when Pass 1/2 ran and current state is `OPEN`; no state regression.
- `ALLOW_OVERWRITE_OVERRIDE: SCA_AUTHORIZED` may authorize active `Scoping.md` / `KA-*.md` writes only for the dispatched KTY when `AUTHORITY_MODE: SCA_DRIVEN`, `SCA_SNAPSHOT_PATH`, and `SUPERSESSION_MAP_PATH` are present. It does not authorize metadata edits or writes outside `{KTY_PATH}`.
- One Knowledge Type folder per run; no cross-Knowledge-Type scanning.
