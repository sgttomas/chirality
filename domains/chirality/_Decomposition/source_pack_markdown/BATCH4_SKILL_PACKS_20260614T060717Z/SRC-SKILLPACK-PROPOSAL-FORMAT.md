# Source Pack: Skill pack: proposal-format

BatchID: `BATCH4_SKILL_PACKS_20260614T060717Z`

Source truth remains the original repo component files listed under each component heading.
This generated markdown is a DOMAIN_DECOMP review and worker substrate only.

## Component: skills/proposal-format/BRIEF_SCHEMA.md

### BRIEF_SCHEMA — proposal-format

#### Required fields

| Field | Source | Notes |
|---|---|---|
| `ScopePath` | Brief | Run/context anchor, normally the deliverable folder |
| `TaskSkill` | Brief | `proposal-format` |
| `RuntimeOverrides.DELIVERABLE_PATH` | Brief | Absolute path to the deliverable folder |

#### Optional fields

| Field | Default | Notes |
|---|---|---|
| `Tasks` | (baseline scan) | Specific asks; if omitted, skill runs baseline assessment |
| `ApplyEdits` | `false` | Whether to apply proposed changes; edits require explicit brief write authorization |
| `UseSemanticLensing` | `false` | Whether to include `Lens:` tags |
| `RuntimeOverrides.MaxProposals` | `10` | Soft cap on proposals |
| `RuntimeOverrides.FocusDocs` | all | Restrict to named docs |
| `RuntimeOverrides.ProposalDepth` | `full` | `summary` or `full` |
| `RuntimeOverrides.IncludeLensTags` | `false` | Lens tags without full lensing |

#### Example brief (targeted)

```markdown
PURPOSE: Review Specification.md for verification gaps
RequestedBy: WORKING_ITEMS
ScopePath: /path/to/DEL-02.01_Pipeline-Design-Basis
TaskSkill: proposal-format
Tasks:
  - Identify requirements without verification methods
  - Propose verification approaches for unmatched requirements
ApplyEdits: false
RuntimeOverrides:
  DELIVERABLE_PATH: /path/to/DEL-02.01_Pipeline-Design-Basis
  FocusDocs: Specification.md
  MaxProposals: 5
```

#### Example brief (baseline scan)

```markdown
PURPOSE: Baseline assessment of deliverable quality
RequestedBy: WORKING_ITEMS
ScopePath: /path/to/DEL-08.01_Steam-line
TaskSkill: proposal-format
ApplyEdits: false
RuntimeOverrides:
  DELIVERABLE_PATH: /path/to/DEL-08.01_Steam-line
```

## Component: skills/proposal-format/QA_CHECKS.md

### QA_CHECKS — proposal-format

#### Minimum output validity

| Check | Validation |
|---|---|
| PROPOSAL blocks complete | Every block contains Evidence, Change, Why, Risk, Status |
| Evidence grounded | Evidence cites file + section/heading (or `location TBD`) |
| Change specific | Change descriptions are actionable without further interpretation |
| Status correct | PROPOSED (default), APPLIED (only when edit was made), NEEDS_HUMAN_RULING (contradictions/trade-offs) |
| No unsupported proposals | No proposal lacks evidence |
| Decision interface present | MISSING, NEEDS_HUMAN_RULING, DEPENDENCY_NOTES sections all present (may be `none`) |
| Scope respected | All proposals reference content within the single deliverable |

#### Failure reporting

- If no production documents exist: report in `MISSING`
- If no meaningful issues are found: state this explicitly — do not pad output
- If `Tasks` specified work that could not be completed: report in `MISSING` with reason

#### Baseline scan checks (when Tasks omitted)

- At least one category of proposals was assessed (completeness, consistency, verification, source fidelity, or identity)
- TBD items are reported separately from proposals
- Dependency notes are reported when cross-deliverable interfaces are visible

## Component: skills/proposal-format/SKILL.md

---
name: proposal-format
description: Structured recommendation output using PROPOSAL blocks with evidence, change, risk, and status fields. Use for any deliverable-local task that surfaces actionable findings.
compatibility: Chirality TASK generic shell; reasoning-only (no deterministic tools).
metadata:
  chirality-skill-version: "1"
  chirality-task-profile: NONE
---

### SKILL — proposal-format

#### Purpose

Produce structured, evidence-grounded recommendations for deliverable-local work using the PROPOSAL: block format. This skill standardizes how findings are expressed so they are reviewable, actionable, and traceable.

The PROPOSAL: pattern is the canonical recommendation format for deliverable-local tasks. It separates evidence from judgment, makes risk explicit, and preserves human authority over acceptance.

#### Suitable agent shells

- `TASK` (generic shell, no profile)

#### Inputs

##### Required

- `ScopePath`
- `RuntimeOverrides.DELIVERABLE_PATH`

##### Optional

- `Tasks` — specific asks; if omitted, the skill produces a baseline scan (see Method: baseline scan)
- `RuntimeOverrides.MaxProposals` — soft cap on proposals generated
- `RuntimeOverrides.FocusDocs` — restrict analysis to named production docs
- `RuntimeOverrides.IncludeLensTags` — whether to include `Lens:` tags (default: only when `UseSemanticLensing: true`)

#### Runtime overrides

| Key | Meaning | Default |
|---|---|---|
| `MaxProposals` | Soft cap on proposals returned | `10` |
| `FocusDocs` | Limit analysis to named docs (e.g., `Specification.md,Guidance.md`) | all production docs |
| `IncludeLensTags` | Add `Lens:` tags even when semantic lensing is not active | `false` |
| `ProposalDepth` | `summary` (title + status only) or `full` (all fields) | `full` |

#### Tool usage

This is a reasoning-only skill. No deterministic tools are required.

When combined with other skills that use deterministic tools (e.g., deliverable-consistency), the tool output provides the evidence base; this skill provides the output structure.

Disallowed behavior:
- no inventing evidence to justify a proposal
- no widening scope beyond the single deliverable
- no edits outside the effective bounded task brief's write authorization
- no silent conflict resolution — contradictions go in `NEEDS_HUMAN_RULING`

#### Method: PROPOSAL block format

Every recommendation MUST be expressed as a PROPOSAL: block with these fields:

```
- PROPOSAL: <short title>
  - Evidence: <_REFERENCES.md item(s) and/or Source: <Doc> §<Heading>>
  - Change: <precise change — what to add, modify, or remove>
  - Why: <what it improves — clarity, completeness, verification, consistency, etc.>
  - Risk: <downstream impact, dependency impacts, or conflicts>
  - Status: <PROPOSED | APPLIED | NEEDS_HUMAN_RULING>
```

Optional field (when semantic lensing is active or `IncludeLensTags: true`):
```
  - Lens: <Matrix.Row.Column> (or Lens: UNKNOWN if _SEMANTIC.md is missing)
```

##### Field rules

- **Evidence** must cite a file and best-effort section/heading. If exact location is unknown, use `location TBD`. Never cite `_SEMANTIC_LENSING.md` as evidence — it is a worklist, not authority.
- **Change** must be precise enough to apply without further interpretation. "Improve the specification" is not acceptable; "Add REQ-12: minimum wall thickness per CSA Z662 §7.1" is.
- **Why** must name the improvement category (clarity, completeness, verification, consistency, source fidelity, etc.), not just restate the change.
- **Risk** must name concrete downstream effects. "Low risk" without explanation is not acceptable; "Low — additive requirement; no existing content contradicted" is.
- **Status** rules:
  - `PROPOSED` — default; the human has not yet decided
  - `APPLIED` — only when `ApplyEdits: true` and the edit was made
  - `NEEDS_HUMAN_RULING` — when the proposal involves a genuine trade-off, contradiction, or scope decision

##### Grouping

When practical, group proposals by issue type:
- Completeness gaps (missing content)
- Consistency issues (cross-document conflicts)
- Verification gaps (requirements without verification methods)
- Source fidelity issues (content that may not match source)
- Identity/terminology issues

#### Method: decision interface

After all PROPOSAL: blocks, always include:

```
- MISSING: <items where files or references are absent>
- NEEDS_HUMAN_RULING: <items requiring human decision — contradictions, trade-offs, scope questions>
- DEPENDENCY_NOTES: <cross-deliverable interfaces, blockers, mismatches>
```

Each section may be `none` if empty.

#### Method: baseline scan

When `Tasks` is omitted from the brief, produce a baseline assessment:
- Top proposals (up to `MaxProposals`) — the highest-value recommendations based on a sweep of the production documents
- Top `TBD` items — the most impactful unresolved markers
- Top dependency notes — cross-deliverable issues visible from this deliverable's content

This baseline scan is the default behavior, not a separate mode. It is what the skill does when given no specific direction.

#### Outputs

- `PROPOSAL:` blocks (structured per the format above)
- `MISSING:` items
- `NEEDS_HUMAN_RULING:` items
- `DEPENDENCY_NOTES:` items
- Optional applied edits (when `ApplyEdits: true`)
- Optional `MEMORY.md` update only when explicitly authorized by the brief

#### Non-negotiable constraints

- Every proposal must cite evidence from production documents or accessible sources
- Unknowns remain `TBD` — do not invent content to fill gaps
- Conflicts must be surfaced in `NEEDS_HUMAN_RULING`, not reconciled silently
- Proposed changes must be minimal and reversible
- The human decides acceptance — proposals are recommendations, not directives

#### QA expectations

- Every PROPOSAL: block contains all required fields (Evidence, Change, Why, Risk, Status)
- Evidence fields cite file + section/heading (or `location TBD`)
- No proposal is unsupported by evidence
- Change descriptions are specific enough to apply without interpretation
- Status is correctly assigned (PROPOSED unless edits were applied or human ruling is needed)
- If no meaningful issues are found, the run says so explicitly rather than padding output

## Component: skills/proposal-format/TOOL_POLICY.md

### proposal-format — Tool Policy

#### Preferred tool order

Reasoning-first: this skill is LLM-driven; no deterministic tool ordering applies. When combined with other skills that use deterministic tools (e.g., deliverable-consistency), the other tool's output provides the evidence base; this skill provides the output structure.

#### Allowed deterministic tools

##### TASK-enforced
_Tools from the `allowed-tools` frontmatter; enforced by TASK shell at skill load time._

- None — no TASK-enforced deterministic allowlist.

##### Operationally invoked
_Tools named in `## Tool usage` body; agent-guided, not TASK-enforced._

- None — no operational helpers declared (this is a reasoning-only skill).

#### Expected use of reasoning

This is a reasoning-only skill. All phases — evidence gathering, PROPOSAL block authoring, status assignment, grouping, baseline scan, and the MISSING / NEEDS_HUMAN_RULING / DEPENDENCY_NOTES decision interface — are performed by direct LLM reasoning against deliverable-local content under `RuntimeOverrides.DELIVERABLE_PATH`. No deterministic tools are required.

#### Disallowed use

- No hidden reliance on tools outside the declared list unless the human expands AllowedTools. No writes outside declared scope.
- No inventing evidence to justify a proposal.
- No widening scope beyond the single deliverable.
- No edits outside the effective bounded task brief's write authorization.
- No silent conflict resolution — contradictions go in `NEEDS_HUMAN_RULING`.

#### Write boundary

Writes are limited to the effective bounded task brief's write authorization for the single deliverable under `RuntimeOverrides.DELIVERABLE_PATH`. Optional applied edits require `ApplyEdits: true`; `MEMORY.md` updates require explicit brief authorization.
