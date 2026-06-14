# Source Pack: Skill pack: decomposition-package-review

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/decomposition-package-review/BRIEF_SCHEMA.md

### decomposition-package-review — Brief Schema

Use this skill with a generic TASK shell (no profile) like this:

```md
PURPOSE: Review the active DOMAIN decomposition package after a scope change.
RequestedBy: SCOPE_CHANGE

ScopePath: /abs/path/to/domain-root
TaskSkill: decomposition-package-review
AllowedWriteTargets:
  - /abs/path/to/domain-root/2_Checking/From/Decomposition_Package_Review.md
  - /abs/path/to/domain-root/2_Checking/From/Decomposition_Package_Findings.csv
  - /abs/path/to/domain-root/2_Checking/From/Decomposition_Package_Parity.csv

RuntimeOverrides:
  ROOT_PATH: /abs/path/to/domain-root
  DECOMPOSITION_ROOT: /abs/path/to/domain-root/_Decomposition
  SCOPE_CHANGE_ROOT: /abs/path/to/domain-root/_ScopeChange
  REVIEW_OUTPUT_PATH: /abs/path/to/domain-root/2_Checking/From/Decomposition_Package_Review.md
  FINDINGS_CSV_PATH: /abs/path/to/domain-root/2_Checking/From/Decomposition_Package_Findings.csv
  PARITY_MATRIX_PATH: /abs/path/to/domain-root/2_Checking/From/Decomposition_Package_Parity.csv
  MODE: REVIEW_ONLY
```

#### Required fields

| Field | Value | Notes |
|---|---|---|
| `TaskSkill` | `decomposition-package-review` | Must match skill folder name |
| `ScopePath` | Absolute path to one DOMAIN root | Normally equals `ROOT_PATH` |
| `AllowedWriteTargets` | Report paths and any explicitly authorized package-local repair targets | Keep narrow |
| `RuntimeOverrides.ROOT_PATH` | Absolute path to the root under review | One root only |
| `RuntimeOverrides.DECOMPOSITION_ROOT` | Absolute path to `_Decomposition/` | Required |
| `RuntimeOverrides.SCOPE_CHANGE_ROOT` | Absolute path to `_ScopeChange/` | Required |
| `RuntimeOverrides.REVIEW_OUTPUT_PATH` | Markdown report path | Must be inside `AllowedWriteTargets` |
| `RuntimeOverrides.MODE` | Review or bounded repair mode | `REVIEW_ONLY` or `REVIEW_AND_REPAIR` |

#### Optional fields

| Field | Default | Allowed values | Notes |
|---|---|---|---|
| `RuntimeOverrides.FINDINGS_CSV_PATH` | omitted | Absolute path | Optional structured findings log |
| `RuntimeOverrides.PARITY_MATRIX_PATH` | omitted | Absolute path | Optional parity matrix |
| `RuntimeOverrides.ACTIVE_SNAPSHOT_PATH` | autodetect via `_LATEST.md` | Absolute path | Use only when `_LATEST.md` should not decide |
| `RuntimeOverrides.MAX_FINDINGS` | `80` | Positive integer | Soft cap on findings |

#### TaskProfile

`NONE` — this skill runs in generic TASK shell mode without a profile.

#### Read boundary

The skill reads only:

- `{DECOMPOSITION_ROOT}/`
- `{SCOPE_CHANGE_ROOT}/_LATEST.md`
- the active `_ScopeChange/SCA-*` snapshot

Do not use this brief to authorize KTY-local, hypergraph, audit, or publication
reads.

#### Write boundary

The skill always writes:

- `REVIEW_OUTPUT_PATH`
- optional `FINDINGS_CSV_PATH`
- optional `PARITY_MATRIX_PATH`

Only when `MODE = REVIEW_AND_REPAIR`, the brief may additionally authorize
explicit package-local repair targets under `_Decomposition/` or `_ScopeChange/`.

#### Typical tasks

- verify that a `DOMAIN` root's active decomposition package is internally
  consistent after `SCOPE_CHANGE`
- verify active snapshot completeness and `_LATEST.md` parity
- separate package-local repair work from downstream reruns
- produce root-level closure evidence before Phase 7 / publication gating

#### Notes

- One invocation reviews one DOMAIN root only.
- `REVIEW_ONLY` is the safe default.
- Use `kty-metadata-align` for KTY-local metadata drift; do not widen this
  review run into folder-local repair.

## Component: skills/decomposition-package-review/QA_CHECKS.md

### decomposition-package-review — QA Checks

Minimum checks for a valid run:

1. `ROOT_PATH`, `DECOMPOSITION_ROOT`, and `SCOPE_CHANGE_ROOT` exist.
2. The active snapshot was either resolved from `_LATEST.md` or explicitly
   provided, and the report says which one was used.
3. The report at `REVIEW_OUTPUT_PATH` exists and states one of:
   - `READY`
   - `READY_WITH_GAPS`
   - `BLOCKED`
4. Findings distinguish:
   - `DECOMP_LOCAL_REPAIR`
   - `SNAPSHOT_REPAIR`
   - `DOWNSTREAM_RERUN`
   - `HUMAN_DECISION_REQUIRED`
5. Every blocking or material-warning finding cites a local surface path.
6. `REVIEW_ONLY` runs modify no package-local truth.
7. `REVIEW_AND_REPAIR` runs modify only explicitly authorized files under
   `_Decomposition/` or `_ScopeChange/`.

#### Blocking conditions that must surface

A run is invalid if any of these occurred but were not reported:

- active snapshot resolution failed or was ambiguous
- duplicated package-local truth surfaces materially disagree
- the active snapshot is incomplete
- `RUN_SUMMARY.md` or `Handoff_State.md` claims a phase the package evidence
  does not support
- a write target falls outside the authorized package-local paths

#### Optional structured-output validation

If `FINDINGS_CSV_PATH` is provided:

- the file exists
- each row includes `Severity`, `FindingClass`, `SurfacePath`, and `Summary`

If `PARITY_MATRIX_PATH` is provided:

- the file exists
- each row includes `SurfacePath`, `ParityStatus`, and `RequiredAction`

#### Success case

A clean run reports:

- the reviewed root
- the active snapshot path
- package verdict
- whether any repairs were applied
- whether downstream reruns remain

If no material issues remain, the report must say so explicitly.

## Component: skills/decomposition-package-review/SKILL.md

---
name: decomposition-package-review
description: Review one DOMAIN decomposition package as a closed system for derivative parity, active snapshot completeness, and handoff-state readiness. Use when a root-level remediation or scope-change run needs package-level closure evidence before downstream work or phase advancement.
compatibility: Chirality TASK in generic shell mode (no profile); reasoning-first package review with optional bounded repair.
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — decomposition-package-review

#### Purpose

Review one bounded `DOMAIN` root as a closed decomposition package:

- `_Decomposition/`
- `_ScopeChange/_LATEST.md`
- the active `_ScopeChange/SCA-*` snapshot

The skill checks whether duplicated decomposition-local truth surfaces agree,
whether the active snapshot satisfies the current `SCOPE_CHANGE` contract, and
whether the recorded handoff state is consistent with the actual package state.

This skill supports two modes:

- `REVIEW_ONLY` — inspect and report only
- `REVIEW_AND_REPAIR` — perform only bounded, decomposition-local repairs that
  are explicitly authorized by `AllowedWriteTargets` and mechanically derivable
  from already authoritative package truth

This skill never repairs KTY-local content, hypergraph outputs, audit outputs,
or publication artifacts.

#### Suitable agent shells

- `TASK` (generic shell mode, no profile)

Typical dispatchers:

- `SCOPE_CHANGE` closeout
- root remediation closure steps
- follow-on review loops before Phase 7 / publication gating

#### Inputs

##### Required

- `ScopePath` — absolute path to one DOMAIN root
- `AllowedWriteTargets` — explicit list of report paths and any
  decomposition-local files authorized for repair in this run
- `RuntimeOverrides.ROOT_PATH` — normally equal to `ScopePath`
- `RuntimeOverrides.DECOMPOSITION_ROOT` — absolute path to the root's
  `_Decomposition/`
- `RuntimeOverrides.SCOPE_CHANGE_ROOT` — absolute path to the root's
  `_ScopeChange/`
- `RuntimeOverrides.REVIEW_OUTPUT_PATH` — markdown review report path
- `RuntimeOverrides.MODE` — `REVIEW_ONLY` or `REVIEW_AND_REPAIR`

##### Optional

- `RuntimeOverrides.FINDINGS_CSV_PATH` — optional structured findings log
- `RuntimeOverrides.PARITY_MATRIX_PATH` — optional structured parity matrix
- `RuntimeOverrides.ACTIVE_SNAPSHOT_PATH` — explicit snapshot path; autodetect
  from `_LATEST.md` when omitted
- `RuntimeOverrides.MAX_FINDINGS` — soft cap on reported findings; default `80`

#### Runtime overrides

| Key | Meaning | Default | Allowed values |
|---|---|---|---|
| `ROOT_PATH` | DOMAIN root under review | **Required** | Absolute directory path |
| `DECOMPOSITION_ROOT` | `_Decomposition/` path | **Required** | Absolute directory path |
| `SCOPE_CHANGE_ROOT` | `_ScopeChange/` path | **Required** | Absolute directory path |
| `REVIEW_OUTPUT_PATH` | Markdown report path | **Required** | Path inside `AllowedWriteTargets` |
| `MODE` | Review or bounded repair mode | **Required** | `REVIEW_ONLY`, `REVIEW_AND_REPAIR` |
| `FINDINGS_CSV_PATH` | Optional structured findings log | omitted | Path inside `AllowedWriteTargets` |
| `PARITY_MATRIX_PATH` | Optional structured parity matrix | omitted | Path inside `AllowedWriteTargets` |
| `ACTIVE_SNAPSHOT_PATH` | Explicit active snapshot path | autodetect | Absolute directory path |
| `MAX_FINDINGS` | Soft cap on findings | `80` | Positive integer |

#### Read boundary

Reads are limited to:

- `{DECOMPOSITION_ROOT}/`
- `{SCOPE_CHANGE_ROOT}/_LATEST.md`
- the active snapshot under `{SCOPE_CHANGE_ROOT}/`

The skill must not widen to KTY-local folders, `_Aggregation/`,
`_Reconciliation/`, hypergraph outputs, or publication outputs.

#### Write boundary

Writes are limited to:

- `{REVIEW_OUTPUT_PATH}`
- optional `{FINDINGS_CSV_PATH}`
- optional `{PARITY_MATRIX_PATH}`
- in `REVIEW_AND_REPAIR` mode only: explicitly authorized files under
  `{DECOMPOSITION_ROOT}/` or `{SCOPE_CHANGE_ROOT}/`

The skill must never write:

- KTY-local folders
- `_Aggregation/`
- `_Reconciliation/`
- hypergraph outputs
- publication outputs

#### Tool usage

- Reasoning-first only.
- The `allowed-tools` frontmatter field is intentionally omitted.

Disallowed behavior:

- No use of this skill for cross-root conformity review.
- No KTY-local metadata repair; use `kty-metadata-align` for that.
- No silent repair of ambiguous truth conflicts.
- No invention of missing snapshot artifacts, missing decomposition rows, or
  phase-completion claims that are not supported by package evidence.

#### Method

##### Step 0 — Preconditions

1. Validate `ROOT_PATH`, `DECOMPOSITION_ROOT`, and `SCOPE_CHANGE_ROOT`.
2. Resolve the active snapshot:
   - use `ACTIVE_SNAPSHOT_PATH` when provided, otherwise read `_LATEST.md`
   - if `_LATEST.md` is missing, empty, or resolves ambiguously, report it
3. Validate `REVIEW_OUTPUT_PATH` is inside `AllowedWriteTargets`.
4. If `MODE = REVIEW_AND_REPAIR`, validate every non-report write target is
   inside `_Decomposition/` or `_ScopeChange/`.

##### Step 1 — Inventory the active decomposition package

Inventory, at minimum:

- the main decomposition markdown
- decomposition-local derivatives and annexes under `_Decomposition/`
- `_ScopeChange/_LATEST.md`
- active snapshot artifacts

Treat the package as a closed system. If a local derivative surface carries
duplicated counts, mappings, status, open-issue state, validation evidence, or
handoff state, it is in scope for comparison.

##### Step 2 — Classify package roles

Before building the parity matrix, classify every major surface by package role:

| Label | Meaning |
|---|---|
| `working surface` | The main decomposition document; the primary human-facing control surface |
| `authoritative companion register` | A companion file holding heavy machine-truth as the primary working surface for that data |
| `snapshot / handoff artifact` | An immutable amendment snapshot or handoff-state record |
| `derived publication artifact` | A render, bundle, or review document assembled from the modular package; not the amendment surface |

For each reviewed surface, record:

- the assigned package-role label
- whether the main decomposition document is overly monolithic relative to companion truth (heavy ledger/telemetry embedded inline when companion registers already carry the same truth)
- whether any companion register should be promoted (it carries authoritative truth not reflected in the main doc) or demoted (it duplicates main-doc truth without adding value)
- whether any artifact is ambiguously labeled or unlabeled

Package-role classification findings feed into Step 3.

##### Step 3 — Build the package parity matrix

Compare the authoritative surfaces for:

- top-level telemetry and counts
- category / knowledge-type / subject parity
- objective support parity
- open-issue parity
- mapping-table parity
- validation-check parity
- active snapshot artifact completeness
- handoff-state consistency

For each reviewed surface, classify package state as:

- `MATCH`
- `DRIFT`
- `MISSING`
- `NOT_APPLICABLE`

##### Step 4 — Classify findings

Every finding must land in exactly one class:

- `DECOMP_LOCAL_REPAIR`
- `SNAPSHOT_REPAIR`
- `DOWNSTREAM_RERUN`
- `HUMAN_DECISION_REQUIRED`

Typical examples:

- stale duplicated annex rows -> `DECOMP_LOCAL_REPAIR`
- wrong `_LATEST.md` or incomplete active snapshot -> `SNAPSHOT_REPAIR`
- KTY-local content drift implied by package truth -> `DOWNSTREAM_RERUN`
- contradictory authoritative package surfaces with no clear winner ->
  `HUMAN_DECISION_REQUIRED`

##### Step 5 — Optional bounded repair

Only when `MODE = REVIEW_AND_REPAIR`:

1. Repair only files explicitly authorized by `AllowedWriteTargets`.
2. Repair only when the fix is mechanically derivable from already accepted
   package truth.
3. Allowed repair classes:
   - duplicated decomposition-local derivative parity
   - active snapshot pointer parity
   - handoff-state or run-summary state fields that are stale relative to the
     already accepted artifact state
4. Disallowed repair classes:
   - substantive decomposition truth changes requiring human judgment
   - missing snapshot artifacts whose contents would need to be invented
   - KTY-local metadata or content repair

##### Step 6 — Write outputs

Write `{REVIEW_OUTPUT_PATH}` containing, in order:

1. Title: `# Decomposition Package Review — {ROOT_NAME}`
2. Metadata block: root path, active snapshot, mode, review date
3. Package verdict:
   - `READY`
   - `READY_WITH_GAPS`
   - `BLOCKED`
4. Package-role classification per reviewed surface
5. Parity summary
6. Findings grouped by the four required classes
7. Repairs applied in this run, if any
8. Required downstream reruns, if any
9. Explicit `RUN_STATUS`

Decomposition-local drift repair (classes `DECOMP_LOCAL_REPAIR` and
`SNAPSHOT_REPAIR`) is authoritative work: this skill may fix it directly when
`MODE = REVIEW_AND_REPAIR`. Observations about derived publication artifacts
(e.g., stale monolithic renders or publication bundles) are for reporting only
and must not be repaired by this skill.

If `PARITY_MATRIX_PATH` is provided, write a structured matrix with at least:

- `SurfacePath`
- `SurfaceType`
- `ComparisonBasis`
- `ParityStatus`
- `AuthorityBasis`
- `RequiredAction`

If `FINDINGS_CSV_PATH` is provided, write a CSV with minimum columns:

- `FindingID`
- `Severity`
- `FindingClass`
- `SurfacePath`
- `Summary`
- `AuthorityBasis`
- `RecommendedAction`

#### Outputs

- `Decomposition_Package_Review.md` at `REVIEW_OUTPUT_PATH`
- optional findings CSV at `FINDINGS_CSV_PATH`
- optional parity matrix at `PARITY_MATRIX_PATH`

#### Non-negotiable constraints

- **One root per run.** Review exactly one DOMAIN root.
- **Package-bounded.** Treat `_Decomposition/` + active `_ScopeChange/` as the
  full scope; do not widen into KTY folders.
- **No silent truth selection.** If authoritative surfaces disagree and no
  clear authority basis exists, escalate instead of repairing.
- **Repair is opt-in.** `REVIEW_AND_REPAIR` may repair only explicitly approved,
  mechanically derivable package-local drift.
- **Evidence-backed findings.** Every material finding cites a local surface.

#### QA expectations

- The reviewed root and active snapshot are explicit.
- The report states one of `READY`, `READY_WITH_GAPS`, or `BLOCKED`.
- Findings distinguish decomposition-local repair, snapshot repair, downstream
  rerun, and human-decision classes.
- `REVIEW_ONLY` runs modify no package-local truth.
- `REVIEW_AND_REPAIR` runs list every repaired file explicitly.

## Component: skills/decomposition-package-review/TOOL_POLICY.md

### decomposition-package-review — Tool Policy

#### Preferred tool order

Reasoning-first:

1. read `_Decomposition/`
2. resolve the active `_ScopeChange` snapshot from `_LATEST.md`
3. enumerate package-local derivative surfaces
4. build the parity matrix and classify findings
5. in `REVIEW_AND_REPAIR` mode only, apply explicitly authorized,
   mechanically derivable package-local repairs
6. write the report and optional structured outputs

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill
load time._

- None — no TASK-enforced deterministic allowlist (the `allowed-tools`
  frontmatter field is intentionally omitted)

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None — no deterministic helpers declared

#### Expected use of reasoning

This skill is a bounded package-level review. Reasoning governs:

- which local surfaces count as duplicated package truth
- whether a finding belongs to package repair, snapshot repair, rerun, or human
  escalation
- whether a repair is genuinely mechanical and authorized
- whether handoff-state claims are supported by actual package evidence

#### Disallowed use

- No KTY-local reads or writes outside what the brief explicitly authorizes for
  package review artifacts.
- No use as a substitute for cross-root conformity review.
- No repairs to hypergraph, audit, or publication outputs.
- No silent synthesis of missing snapshot artifacts.
- No repair when the authority basis is ambiguous.

#### Write boundary

Writes are limited to:

- `{REVIEW_OUTPUT_PATH}`
- optional `{FINDINGS_CSV_PATH}`
- optional `{PARITY_MATRIX_PATH}`
- explicit package-local repair targets under `_Decomposition/` or
  `_ScopeChange/` when `MODE = REVIEW_AND_REPAIR`

No other files may be created or modified by this skill.
