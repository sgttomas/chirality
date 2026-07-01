---
title: "Governance Harness Audit and Remediation Instructions"
date: "2026-07-01"
status: "audit / successor-agent instruction packet"
authority: "generated audit artifact; not governance authority"
source_basis: "context.zip archive reviewed 2026-07-01"
---

# Governance Harness Audit and Remediation Instructions

## 0. Purpose

This document captures the findings from the archive review and converts them into concrete correction instructions for a successor agent.

The successor agent should use this audit with the revised plan:

- `governance_harness_detailed_plan_2026-07-01_revised.md`
- `chirality_architecture_explainer_governance_harness_2026-07-01.md`

The goal is not to “finish governance.” The goal is to make the first harness implementation safe, narrow, source-cited, and honest about authority.

## 1. Review scope and limitation

Reviewed archive: `context.zip`, excluding macOS metadata such as `__MACOSX` and `.DS_Store`.

Important limitation: the archive references live repo surfaces that are not included in the archive, including `AGENTS.md`, `agents/`, `skills/`, `tools/`, and live `projects/chirality-*` working roots. Treat references to those paths as documentary claims unless verified in the live repository.

## 2. Executive audit conclusion

The governance harness should be implemented as a **read-mostly practitioner bench tool**.

Do not implement the first release as:

- a database-owned control plane;
- an autonomous coordinator;
- a project-management system;
- a lifecycle transition tool;
- an approval engine;
- a domain-operation application layer.

The first release should compile existing state, generate candidate tranche briefs, check objective scope/evidence conditions, surface contradictions, and stop at human decision boundaries.

## 3. Findings register

### F-001 — Planning substrate conflict: bench tool vs control plane

**Severity:** `REVIEW`

**Evidence:**

- `context/governance_harness_integration_assessment_2026-06-23.md` proposes a richer local control-plane style architecture, including SQLite/event/log/control ideas.
- `context/governance_harness_detailed_plan_2026-06-23.html` correctly pulls toward a local, read-mostly, tranche-centered practitioner bench tool.

**Risk:** A future implementer may resurrect the heavier control plane because both planning directions remain in the corpus.

**Correction:** Add `docs/governance_harness/PLAN_INDEX.md` and a human decision record `D-GH-001_substrate_authority.md` stating that for MVP, git/versioned authored files are authority; harness outputs are generated views/candidates; SQLite is deferred and projection-only.

---

### F-002 — Root governance basis is draft/pending ratification

**Severity:** `REVIEW`; becomes `BLOCK` if the harness claims ratified enforcement from these docs.

**Evidence:**

- `context/docs/DIRECTIVE.md:3` says `Status: DRAFT pending human ratification`.
- `context/docs/CONTRACT.md:3` says `Status: DRAFT pending human ratification`.
- `context/docs/SPEC.md:3` says `Status: DRAFT pending human ratification`.
- `context/docs/TYPES.md:3` says `Status: DRAFT pending human ratification`.
- `context/docs/PLAN.md:3` says `Status: DRAFT skeleton pending human authoring`.

**Risk:** A harness could claim to enforce governance that the archive itself says is not ratified.

**Correction:** Add `D-GH-005_minimal_governance_basis.md` to ratify the minimal subset needed by the harness, or require generated reports to say `Governance basis: draft/advisory` until ratified.

---

### F-003 — `_DomainEngines/DOMAIN_ENGINE_INDEX.md` contains profile-status contradiction

**Severity:** `REVIEW`; becomes `BLOCK` if used as current authority without resolution.

**Evidence:**

- `context/_DomainEngines/DOMAIN_ENGINE_INDEX.md:7` says everything under the root is `PROPOSAL / unratified`, no profile is `ADOPTED`, no decision is ruled.
- `context/_DomainEngines/DOMAIN_ENGINE_INDEX.md:15` marks `open_pipe_stress` as `ADOPTED` and says validation + Gate 2 adoption completed on 2026-06-21.

**Risk:** A harness reading the file naively could report either “none adopted” or “adopted,” depending on parser target.

**Correction:** Either update the file to one current truth or mark line 7 as historical/superseded. Add a self-check rule that flags section/header/table conflicts.

---

### F-004 — `_DomainEngines/RULINGS_PUBLISHED.md` contains mutually exclusive current-state claims

**Severity:** `REVIEW`; becomes `BLOCK` if used as adoption authority without resolution.

**Evidence:**

- `context/_DomainEngines/RULINGS_PUBLISHED.md:48-50` says the profile validator passed, Gate 2 adoption completed, and ProfileStatus is `ADOPTED`.
- `context/_DomainEngines/RULINGS_PUBLISHED.md:56` says the profile remains `DRAFT`, not `VALIDATED`, and not `ADOPTED`.

**Risk:** The file claims both adopted and not adopted.

**Correction:** Remove or supersede the stale line 56 statement, or move it into a historical note explicitly marked superseded. Add a self-check for contradictory terminal state claims in the same file.

---

### F-005 — OpenPipeStress profile filename/header/comments conflict with YAML field

**Severity:** `REVIEW`; becomes `BLOCK` if the profile is consumed without a conflict caveat.

**Evidence:**

- `context/_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml:1` says `DRAFT (NOT validated, NOT adopted)`.
- `context/_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml:3` says `Status: DRAFT`.
- `context/_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml:9-10` says no deterministic validator exists and nothing is adopted.
- `context/_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml:18` sets `profile_status: "ADOPTED"` and says the validator passed and Gate 2 was approved.

**Risk:** Tools can disagree depending on whether they parse comments, filename, or YAML fields.

**Correction:** Decide whether the filename remains historical or should be renamed. At minimum, update the header comments to say the filename is historical and `profile_status` is current. Better: add `D-GH-006_domain_profile_current_truth.md` and then normalize the profile header, filename, index, latest pointer, rulings, and validation report.

---

### F-006 — OpenPipeStress profile open issues contain stale/closed items

**Severity:** `REVIEW`

**Evidence:**

- `context/_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml:132-133` says the profile stays draft and no deterministic validator exists.
- `context/_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml:137` says `RES-RECONCILE` is resolved and no longer an open issue, but it is still located under `open_issues`.
- `context/_DomainEngines/profiles/_validation/open_pipe_stress.validation.json:6-8` says profile status is `ADOPTED` and validation result is `VALID`.

**Risk:** Stale open issues obscure current state and undermine trust in generated reports.

**Correction:** Split open issues into `open_issues` and `closed_or_superseded_notes`, or remove stale items after preserving them in an immutable historical snapshot.

---

### F-007 — D-T0 decision headers say proposal/TBD while bodies contain human rulings

**Severity:** `REVIEW`; becomes `BLOCK` for any claim that ruling SHA is bound if it remains `TBD`.

**Evidence examples:**

- `context/_DomainEngines/_DECISIONS/D-T0-01_precedence.md:1` says `PROPOSAL; HumanRuling: TBD`; line 20 contains a human ruling but `Ruling SHA: TBD`.
- `context/_DomainEngines/_DECISIONS/D-T0-02_profilestatus_enum.md:1` says `PROPOSAL; HumanRuling: TBD`; line 16 contains a human ruling but `Ruling SHA: TBD`.
- `context/_DomainEngines/_DECISIONS/D-T0-06_profile_adoption_lifecycle.md:1` says `PROPOSAL; HumanRuling: TBD`; lines 14-16 contain the ruling/progress to `ADOPTED` but the header remains proposal/TBD.

**Risk:** A parser or reviewer cannot tell whether the decision is current, ruled, published, SHA-bound, or still proposal.

**Correction:** Update headers/frontmatter to reflect current ruled/published state, or explicitly mark the body rulings as pending SHA binding. Add self-checks for header/body ruling conflicts and `Ruling SHA: TBD` in files claiming adoption/issuance.

---

### F-008 — Validation report contains machine-absolute path

**Severity:** `WARN`; may be `BLOCK` depending on file-class policy.

**Evidence:**

- `context/_DomainEngines/profiles/_validation/open_pipe_stress.validation.json:5` includes `/Users/ryan/ai-env/projects/chirality/_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml`.

**Risk:** Machine-local paths make validation artifacts less portable and can leak local environment details. Root `SPEC.md` permits absolute paths in run/evidence artifacts where they record what happened, but instruction, coordination, and plan files should remain repo-relative.

**Correction:** Define file-class path policy. For validation/evidence reports, either include both `profile_path_repo_relative` and `profile_path_local_observed`, or scrub absolute paths in generated portable reports.

---

### F-009 — Existing architecture explainer includes unverifiable live-surface and numeric claims

**Severity:** `WARN`

**Evidence:**

- `context/chirality_architecture_explainer_2026-06-23.html` describes `AGENTS.md`, `agents/`, `skills/`, `tools/`, role counts, validator counts, and live working-root counts.
- Those surfaces and counts are not present in the provided archive.

**Risk:** A handoff based only on the archive could repeat live-repo claims as verified facts.

**Correction:** Replace or supplement the explainer with the corrected architecture explainer in this packet. It should explicitly distinguish archive evidence from live-repo claims and avoid unsupported counts.

---

### F-010 — Existing architecture explainer says the harness writes nothing

**Severity:** `WARN`

**Evidence:**

- `context/chirality_architecture_explainer_2026-06-23.html` states the harness is a read-only inspector and writes nothing back.

**Risk:** Too strict if interpreted literally: the useful harness should write generated reports, candidate briefs, and cache/projection files. The actual boundary is not “writes nothing”; it is “does not write governed authority.”

**Correction:** Use the corrected architecture statement: the harness may write generated views and candidate briefs, but not authority files unless separately scoped and human-adopted.

---

### F-011 — Status flattening remains a major implementation risk

**Severity:** `REVIEW`

**Evidence:**

- The existing detailed plan already warns that `CHECKING` and `IN_PROGRESS` have project-local meanings and should not be flattened.
- Root `TYPES.md` defines vocabulary/lifecycle concepts, but local roots can specialize state usage.

**Risk:** A UI or report could produce a single green/yellow/red badge that implies approval or readiness.

**Correction:** Require separate fields for lifecycle, evidence, approval basis, staleness, scope conformance, human decision state, and warrant/authentication state.

---

### F-012 — Domain-engine work could swallow the MVP

**Severity:** `REVIEW`

**Evidence:**

- `_DomainEngines` contains profile validation, integration levels, protected paths, data residency rulings, OperationProposal concepts, risk-class concepts, bridge artifacts, and live-build gates.

**Risk:** Building domain operation application or MCP integration inside the first harness would make the MVP too broad and could violate authority boundaries.

**Correction:** Treat `_DomainEngines` as read-only in MVP. The harness may report status, contradictions, protected paths, and validation posture. It must not apply domain operations or advance domain lifecycle.

## 4. Required corrections

### 4.1 Create plan classification and governance-harness decision records

Add:

```text
docs/governance_harness/PLAN_INDEX.md
docs/governance_harness/D-GH-001_substrate_authority.md
docs/governance_harness/D-GH-002_verifier_severity.md
docs/governance_harness/D-GH-003_pilot_scope.md
docs/governance_harness/D-GH-004_human_actor_identity.md
docs/governance_harness/D-GH-005_minimal_governance_basis.md
docs/governance_harness/D-GH-006_domain_profile_current_truth.md
```

The decision records can start as drafts requiring owner/human ruling, but they must make the unresolved decisions visible.

### 4.2 Replace or supersede the existing detailed harness plan

Use `governance_harness_detailed_plan_2026-07-01_revised.md` as the new MVP candidate.

Do not silently delete the old plan. Either:

- keep it as historical planning material and add a supersession note; or
- move it into an archive path with a plan index entry.

### 4.3 Add the corrected architecture explainer

Add `chirality_architecture_explainer_governance_harness_2026-07-01.md` or equivalent.

It must correct:

- no hidden authoritative DB, not no DB anywhere;
- harness may write generated outputs, but not governed authority;
- archive evidence vs live-repo claims;
- status vs evidence vs warrant vs approval;
- domain-engine MVP read-only boundary.

### 4.4 Normalize `_DomainEngines` current truth

Implement one of two acceptable strategies.

**Preferred strategy — normalize current files:**

- update `DOMAIN_ENGINE_INDEX.md` so the top status paragraph and table agree;
- update `RULINGS_PUBLISHED.md` so it does not claim both adopted and not adopted;
- update `open_pipe_stress.DRAFT.yaml` header/open issues to match the authoritative status field, or rename the file after a human ruling;
- update `_DECISIONS/D-T0-*` headers to reflect ruled/progress state or explicitly mark SHA-binding gaps;
- preserve historical contradictory statements in snapshot/history files if needed.

**Fallback strategy — add a single current-truth pointer:**

- add `_DomainEngines/_CURRENT.md` stating current profile status, integration level, validation status, adoption/ruling state, remaining gates, and superseded contradictions;
- make the harness prefer `_CURRENT.md` as current summary while still reporting conflicts in legacy files.

Do not hide contradictions without a human ruling.

### 4.5 Add self-check fixtures and tests

Use the archive contradictions as fixtures.

Required fixtures:

- profile filename/header says draft while YAML says adopted;
- index paragraph says no profile adopted while table says adopted;
- rulings file says adopted and later says not adopted;
- D-T0 decision header says proposal/TBD while body says ruled;
- validation JSON has machine-absolute path;
- generated output missing disclaimer;
- out-of-scope diff path;
- protected domain path touched by unauthorized diff.

### 4.6 Add the initial harness skeleton

Add:

```text
tools/practitioner_harness/README.md
tools/practitioner_harness/chirality_harness.py
tools/practitioner_harness/adapters/root_governance.py
tools/practitioner_harness/adapters/domain_engines.py
tools/practitioner_harness/checks/status_consistency.py
tools/practitioner_harness/checks/path_policy.py
tools/practitioner_harness/checks/profile_consistency.py
tools/practitioner_harness/checks/source_refs.py
tools/practitioner_harness/render/markdown.py
tools/practitioner_harness/render/json.py
```

The first commands should be:

```bash
chirality-harness status --domain-engines --format md
chirality-harness self-check --root . --format md
```

Then add `app-dev` and `piping` adapters when the live project roots are available.

## 5. Successor-agent implementation instructions

Use these instructions verbatim or adapt minimally.

```text
You are implementing corrections to the Chirality governance harness planning surface.

Primary objective:
Create a narrow practitioner bench tool plan and supporting architecture docs. Do not create a database-owned governance control plane, autonomous coordinator, approval engine, or domain-operation application layer.

Authority rule:
Authored files and git history remain authority. Harness outputs are generated views, candidate briefs, or cache/projections only. The harness must not approve, issue, seal, certify, authenticate, or accept residual risk.

First actions:
1. Add or update docs/governance_harness/PLAN_INDEX.md.
2. Add draft decision records D-GH-001 through D-GH-006.
3. Supersede the earlier detailed harness plan with the 2026-07-01 revised plan.
4. Add the corrected architecture explainer.
5. Normalize or explicitly current-mark the _DomainEngines status contradictions.
6. Add self-check fixtures for the contradictions listed in this audit.
7. Add a minimal tools/practitioner_harness skeleton with status and self-check commands.

Hard constraints:
- Do not modify governed authority files silently.
- Every generated output must include a non-authority disclaimer.
- Every material report finding must cite source paths.
- Treat root docs marked DRAFT pending ratification as advisory unless a human decision record adopts the relevant subset.
- Treat the OpenPipeStress profile status as conflicted until D-GH-006 or equivalent resolves current truth.
- SQLite, if discussed, must be projection/cache only and deferred from MVP.
- Do not implement MCP/domain-operation writes in the MVP.

Stop conditions:
- If a correction would decide whether a profile is ADOPTED vs DRAFT, stop and require human ruling unless an existing human decision record unequivocally resolves it.
- If a correction would ratify root governance, stop and require human ruling.
- If a correction would authorize private-data egress, domain operation apply, or professional reliance, stop and require human ruling.
```

## 6. Acceptance criteria for corrected planning/docs

The corrected planning/docs are acceptable when:

- the current MVP plan clearly says practitioner bench tool, not control plane;
- earlier heavier proposals are marked historical/superseded/deferred;
- generated views are explicitly non-authoritative;
- SQLite is projection-only and deferred;
- root draft governance status is acknowledged;
- harness outputs distinguish lifecycle, evidence, approval basis, staleness, scope, human decision state, and warrant/authentication state;
- `_DomainEngines` contradictions are either resolved by human ruling or explicitly reported as unresolved current-truth conflicts;
- `D-GH-001` through `D-GH-006` exist or are queued as required human decisions;
- self-check is part of MVP;
- domain-engine integration is read-only for MVP;
- no generated report claims approval, issue, certification, sealing, professional acceptance, release readiness, or construction readiness.

## 7. Acceptance criteria for first harness code PR

The first code PR is acceptable when:

- `chirality-harness self-check --root .` detects the OpenPipeStress draft/adopted contradiction fixture;
- it detects the adopted/not-adopted contradiction in `RULINGS_PUBLISHED.md`;
- it detects `PROPOSAL; HumanRuling: TBD` headers with ruled bodies;
- it detects machine-absolute path leakage and classifies it according to file class;
- it detects missing generated-output disclaimers;
- it emits Markdown and JSON;
- it modifies no authority files;
- every finding includes source paths;
- objective `BLOCK` findings return nonzero only where the severity taxonomy says they should;
- reports contain the structural-check disclaimer.

## 8. Proposed file patch map

| Path | Action | Notes |
|---|---|---|
| `docs/governance_harness/PLAN_INDEX.md` | Add | Classify old/current plans and their authority status. |
| `docs/governance_harness/D-GH-001_substrate_authority.md` | Add draft/ruling | Files/git authority; SQLite projection-only. |
| `docs/governance_harness/D-GH-002_verifier_severity.md` | Add draft/ruling | Defines severity and exit behavior. |
| `docs/governance_harness/D-GH-003_pilot_scope.md` | Add draft/ruling | MVP roots and exclusions. |
| `docs/governance_harness/D-GH-004_human_actor_identity.md` | Add draft/ruling | Human approval/ruling metadata. |
| `docs/governance_harness/D-GH-005_minimal_governance_basis.md` | Add draft/ruling | Minimal ratified basis for harness. |
| `docs/governance_harness/D-GH-006_domain_profile_current_truth.md` | Add draft/ruling | Resolves OpenPipeStress status. |
| `plans/governance_harness_detailed_plan_2026-07-01_revised.md` | Add | Replacement planning artifact. |
| `docs/architecture/chirality_architecture_explainer_governance_harness_2026-07-01.md` | Add | Corrected explainer. |
| `_DomainEngines/DOMAIN_ENGINE_INDEX.md` | Update after ruling | Make top status and table agree. |
| `_DomainEngines/RULINGS_PUBLISHED.md` | Update after ruling | Remove/supersede stale not-adopted claim. |
| `_DomainEngines/profiles/open_pipe_stress.DRAFT.yaml` | Update after ruling | Align header/comments/open issues with current status or mark filename historical. |
| `_DomainEngines/_DECISIONS/D-T0-*.md` | Update after ruling/publish | Align header/frontmatter with body rulings and SHA-binding status. |
| `tools/practitioner_harness/**` | Add | Read-only status/self-check first. |

## 9. Minimal decision-record templates

### `D-GH-001_substrate_authority.md`

```markdown
# D-GH-001 — Governance harness substrate authority

Status: PROPOSED / PENDING HUMAN RULING

Decision:
For the governance harness MVP, are authored git/versioned files the sole authority, with harness outputs treated only as generated views/candidate briefs and SQLite deferred as projection/cache only?

Recommended ruling:
Yes. Authored files and git history remain authority. Harness outputs are non-authoritative unless separately adopted by a human record. SQLite may be introduced later only as rebuildable projection/cache.

HumanRuling: TBD
RuledBy: TBD
Ruling SHA: TBD
Date: TBD
```

### `D-GH-006_domain_profile_current_truth.md`

```markdown
# D-GH-006 — OpenPipeStress domain profile current truth

Status: PROPOSED / PENDING HUMAN RULING

Decision:
Resolve the current status of _DomainEngines/profiles/open_pipe_stress.DRAFT.yaml given conflicting claims across index, latest pointer, profile comments, profile_status field, validation JSON, published rulings, and D-T0 decisions.

Options:
A. Current truth is ADOPTED; filename/header/open issues are stale/historical and must be updated.
B. Current truth is VALIDATED but not ADOPTED; adoption claims are premature and must be corrected.
C. Current truth is DRAFT; validation/adoption claims are not accepted authority and must be corrected.
D. Current truth is historically draft but currently adopted; preserve filename as historical but update comments/index/rulings to make the current-truth rule explicit.

Recommended ruling:
D or A, depending on whether filename retention is intentional. In either case, the current-truth surfaces must be made consistent.

HumanRuling: TBD
RuledBy: TBD
Ruling SHA: TBD
Date: TBD
```

## 10. Final instruction

Do not let the harness become the project.

Make it excellent at reading the project, finding contradictions, preparing bounded work, and reporting evidence. Leave authority, approval, professional judgment, and current-truth rulings where the architecture says they belong: with the human and the governed record.
