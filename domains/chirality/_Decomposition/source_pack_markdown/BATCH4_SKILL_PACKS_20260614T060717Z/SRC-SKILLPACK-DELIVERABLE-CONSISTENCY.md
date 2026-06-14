# Source Pack: Skill pack: deliverable-consistency

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/deliverable-consistency/BRIEF_SCHEMA.md

### deliverable-consistency — Brief Schema

Use this skill with the generic TASK shell like this:

```md
PURPOSE: Run a deliverable-local consistency sweep
RequestedBy: WORKING_ITEMS

ScopePath: /abs/path/to/DEL-XXX_Name
TaskSkill: deliverable-consistency

Tasks:
  - Review the four documents for contradictions and unresolved placeholders
  - Flag unsourced numeric parameters
  - Propose minimal edits only where clearly warranted

ApplyEdits: false

RuntimeOverrides:
  DELIVERABLE_PATH: /abs/path/to/DEL-XXX_Name
  FocusDocs:
    - Datasheet.md
    - Specification.md
    - Guidance.md
    - Procedure.md
  Strictness: conservative
  MaxFindings: 12
  CheckIdentity: true
  CheckUnsourcedNumerics: true

AllowedTools:
  - tools/validation/scan_deliverable_consistency.py

EXCLUSIONS:
  - Procedure.md#Draft Notes
```

#### Required fields

- `ScopePath`
- `TaskSkill: deliverable-consistency`
- `RuntimeOverrides.DELIVERABLE_PATH`

#### Typical tasks

- contradiction sweep
- unresolved `TBD` / `ASSUMPTION` / `CONFLICT:` marker review
- identity normalization proposals
- source/evidence completeness review

#### Notes

- `ApplyEdits: false` is the normal safe default.
- Turn `ApplyEdits: true` on only when you want the task to apply minimal corrections directly, and provide either `AllowedWriteTargets` or explicit writable targets in the brief.

## Component: skills/deliverable-consistency/QA_CHECKS.md

### deliverable-consistency — QA Checks

Minimum checks for a valid run:

1. The deliverable path exists.
2. The deterministic scan completes successfully unless tool use was explicitly excluded.
3. The findings reference only files inside the deliverable.
4. Each significant finding includes best-effort evidence location.
5. Contradictions are surfaced as rulings-needed items, not silently resolved.
6. If edits were applied, they are limited to files authorized by the effective bounded task brief.
7. `MEMORY.md` captures durable decisions or accepted proposals only when the brief authorized that update.

Recommended reporting groups:

- identity mismatch
- unresolved markers
- contradiction
- unsourced numeric parameter
- missing artifact / missing reference

Success case with no findings:

- Explicitly state that no material consistency findings were discovered in scope.
- Mention residual risk if references are sparse or some artifacts were missing.

## Component: skills/deliverable-consistency/SKILL.md

---
name: deliverable-consistency
description: Run a deliverable-local consistency sweep across production documents in one deliverable. Use when checking for unresolved markers, missing core artifacts, identity-label mismatches, or candidate unsourced numeric statements.
compatibility: Chirality TASK generic shell; local repo tools only.
allowed-tools: python3 tools/validation/scan_deliverable_consistency.py:*
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — deliverable-consistency

#### Purpose

Run a deliverable-local consistency sweep across the production documents in one deliverable.

This skill is meant to work with generic `TASK` briefs that identify exactly one deliverable folder.

It helps the agent:
- surface contradictions,
- find unresolved `TBD` / `ASSUMPTION` / `CONFLICT:` markers,
- identify unsourced numeric parameters,
- spot identity mismatches across the document set,
- and propose minimal corrective edits when authorized.

#### Suitable agent shells

- `TASK` (generic shell, no profile)

#### Inputs

##### Required

- `ScopePath`
- `RuntimeOverrides.DELIVERABLE_PATH`

##### Optional

- `Tasks`
- `RuntimeOverrides.FocusDocs`
- `RuntimeOverrides.Strictness`
- `RuntimeOverrides.MaxFindings`
- `RuntimeOverrides.CheckIdentity`
- `RuntimeOverrides.CheckUnsourcedNumerics`

#### Runtime overrides

| Key | Meaning | Default |
|---|---|---|
| `FocusDocs` | Limit the sweep to named production docs | all production docs |
| `Strictness` | `conservative` or `aggressive` finding posture | `conservative` |
| `MaxFindings` | Soft cap on reported findings | `10` |
| `CheckIdentity` | Check folder/document naming consistency | `true` |
| `CheckUnsourcedNumerics` | Flag numeric statements needing evidence review | `true` |

#### Tool usage

Preferred deterministic helper:
- `tools/validation/scan_deliverable_consistency.py`

Preferred method:
- run the deterministic scan first
- read only the flagged deliverable-local files and nearby context
- compare files directly where the deterministic scan cannot decide
- produce recommendation-first output unless edits are explicitly authorized by the brief

Disallowed behavior:
- no widening scope beyond the single deliverable
- no edits outside the effective bounded task brief's write authorization
- no silent conflict resolution

#### Outputs

- `PROPOSAL:` blocks for consistency issues
- `MISSING:` items where files or references are absent
- `NEEDS_HUMAN_RULING:` items for true contradictions
- optional applied minimal edits if `ApplyEdits: true`
- optional `MEMORY.md` update only when the brief explicitly authorizes it

#### Non-negotiable constraints

- Every finding must cite a file and best-effort section/heading.
- Unknowns remain `TBD`.
- Conflicts must be surfaced, not reconciled silently.
- Proposed edits should be minimal and reversible.

#### QA expectations

- Findings are scoped to one deliverable.
- The deterministic scan should be run first unless the brief explicitly forbids tool use.
- Findings are grouped by issue type where practical.
- Identity mismatches and unresolved markers are explicitly reported when found.
- If no meaningful issues are found, the run should say so explicitly rather than padding output.

## Component: skills/deliverable-consistency/TOOL_POLICY.md

### deliverable-consistency — Tool Policy

#### Preferred tool order

This skill is tool-first for the initial sweep, then reasoning-first for adjudication.

1. run `tools/validation/scan_deliverable_consistency.py` against the deliverable
2. read the flagged production docs and nearby context from `RuntimeOverrides.DELIVERABLE_PATH`
3. compare files directly where the scan surfaces a plausible inconsistency
4. emit evidence-backed proposals
5. apply minimal edits only if authorized

Normal invocation shape:

```sh
python3 tools/validation/scan_deliverable_consistency.py "$DELIVERABLE_PATH"
```

Use the optional flags only when the brief calls for them: `--focus-doc`, `--strictness`, `--max-findings`, `--check-identity`, `--check-unsourced-numerics`.

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- `python3 tools/validation/scan_deliverable_consistency.py:*`

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None — no additional operational helpers declared beyond the TASK-enforced scanner.

#### Expected use of reasoning

The tool is a first-pass detector, not a final judge:
- unresolved markers are deterministic findings
- identity mismatches are candidate inconsistencies until checked in context
- unsourced numeric lines are review prompts, not automatic defects

Reasoning takes over after the deterministic sweep: the agent reads flagged production docs and nearby context, compares files directly where the scan cannot decide, and produces evidence-backed PROPOSAL blocks and human-ruling items.

#### Disallowed use

- No hidden reliance on tools outside the declared list unless the human expands AllowedTools. No writes outside declared scope.
- no project-wide scanning
- no widening scope beyond the single deliverable
- no edits outside the effective bounded task brief's write authorization
- no silent conflict resolution
- no dependency register edits unless separately authorized by the brief

#### Write boundary

Writes are limited to the effective bounded task brief's write authorization for the single deliverable under `RuntimeOverrides.DELIVERABLE_PATH`. Optional applied minimal edits require `ApplyEdits: true`. `MEMORY.md` updates and dependency register edits require explicit brief authorization.
