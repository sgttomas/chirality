---
title: "Chirality Architecture With Governance Harness — Corrected Explainer"
date: "2026-07-01"
status: "orientation / architecture explainer"
authority: "generated explanatory artifact; not governance authority"
source_basis: "context.zip archive reviewed 2026-07-01"
---

# Chirality Architecture With Governance Harness — Corrected Explainer

## 0. How to read this explainer

This document is an updated architecture explainer that integrates the proposed governance harness and corrects overstatements in the earlier visual explainer.

It is not a governance record. It is a map.

The most important correction is this:

> Chirality does not need a governance harness that becomes a new source of truth. It needs a small practitioner bench tool that reads governed files, reports contradictions, prepares bounded work briefs, checks objective scope/evidence conditions, and stops at human decision boundaries.

## 1. Corrections to the earlier explainer

The prior explainer was directionally useful, but it flattened several points that matter for implementation.

| Earlier simplification | Corrected architecture statement |
|---|---|
| “Everything is plain text in git; no hidden database.” | **No hidden authoritative database.** Rebuildable indexes and caches may exist, including SQLite-style local indexes, but they are not the source of authority. |
| “The harness writes nothing back.” | The harness should not write governed authority files. It may write generated reports, JSON projections, candidate briefs, and cache files, all labeled non-authoritative. |
| “The live repo contains AGENTS, agents, skills, tools, validators, and exact counts.” | The archive references those live surfaces, but the archive provided for review does not include all of them. A corrected explainer should distinguish archive evidence from live-repo claims. |
| “Status tells where a deliverable is.” | Status is necessary but insufficient. Lifecycle state, evidence completeness, approval SHA, staleness, scope conformance, warrant state, and human decision state must stay separate. |
| “Validation/checking is close to approval.” | Validation may support review. It is not approval, issue, authentication, professional sufficiency, or acceptance of residual risk. |
| “Current-state files can be read directly.” | Some current-state surfaces contradict each other. The harness must surface these conflicts instead of choosing silently. |

## 2. The architecture in one picture

```text
┌────────────────────────────────────────────────────────────────────┐
│ Human accountable authority                                         │
│ - approves, rules, seals, rejects, accepts risk                     │
│ - decides applicability and sufficiency                             │
└─────────────────────────────────────┬──────────────────────────────┘
                                      │ human-authored records
                                      ▼
┌────────────────────────────────────────────────────────────────────┐
│ Authored files and git history                                      │
│ - root governance docs                                              │
│ - project status / plans / decisions / dependencies                 │
│ - domain profiles / validation reports / published rulings          │
│ - evidence artifacts / run records / approval SHAs                  │
└─────────────────────────────────────┬──────────────────────────────┘
                                      │ read by adapters
                                      ▼
┌────────────────────────────────────────────────────────────────────┐
│ Governance harness — practitioner bench tool                        │
│ - status projections                                                │
│ - self-consistency checks                                           │
│ - candidate tranche briefs                                          │
│ - scope checks                                                      │
│ - evidence checks                                                   │
│ - generated reports only                                            │
└─────────────────────────────────────┬──────────────────────────────┘
                                      │ bounded brief + findings
                                      ▼
┌────────────────────────────────────────────────────────────────────┐
│ Bounded agent/tool work                                             │
│ - reads declared basis                                              │
│ - writes only inside declared scope                                 │
│ - records evidence                                                  │
│ - stops at human decision points                                    │
└────────────────────────────────────────────────────────────────────┘
```

The harness lives between the governed record and the next bounded intervention. It helps prepare work and check work. It does not replace the governed record.

## 3. Three kinds of artifacts

The system should classify files by reliance role.

### 3.1 Authority artifacts

These are authored, reviewed, and versioned records that carry project truth.

Examples:

- root governance documents;
- project-local status files;
- decision/ruling files;
- dependency registers;
- domain profiles;
- validation evidence that a governed artifact cites;
- approval SHAs in git history.

The harness reads these. It does not overwrite them as part of ordinary reporting.

### 3.2 Evidence artifacts

These record what happened.

Examples:

- run records;
- validation reports;
- command outputs;
- generated diffs;
- schema validation results;
- evidence bundles.

Evidence can support a human decision. Evidence does not make the decision.

### 3.3 Generated views and projections

These are convenience outputs.

Examples:

- one-page status summaries;
- self-check reports;
- candidate tranche briefs;
- scope/evidence findings;
- rebuildable JSON projections;
- optional local caches.

Generated views must say they are not authority. They should be disposable and rebuildable.

## 4. The authority model

```text
Human decision
  └─ must be authored by a person when a record becomes binding

Framework/root governance
  └─ defines shared invariants, but in the archive several root docs are draft pending ratification

Working root governance
  └─ specializes the framework for a project or domain without weakening it

Harness output
  └─ generated view or candidate; never binding by itself
```

The harness can help enforce objective invariants only after the relevant basis has been ratified or explicitly adopted for the pilot.

Until then, the harness should say:

```text
Governance basis: draft/advisory unless a human decision record adopts it.
```

## 5. Actors and write boundaries

```text
Human
  - binding approvals and rulings
  - professional judgment
  - acceptance of residual risk

Type-0 / maintainer-facing agent
  - drafts or maintains framework-level material with human direction
  - cannot self-ratify governance

Type-1 persona
  - manages a lane such as domain integration, working items, toolmaking, change, audit, or evaluation
  - writes only where its role permits

Type-2 bounded task
  - executes one sealed tranche
  - reads declared basis
  - writes only inside declared write scope

Deterministic tools
  - check, validate, render, summarize, or project
  - may write generated outputs
  - do not write governed authority unless separately scoped and human-authorized

Governance harness
  - deterministic bench tool made of adapters, checks, renderers, and brief generators
  - produces reports and candidate briefs
  - stops at human decision points
```

The important question is not “how capable is the agent?” It is “what is this actor permitted to write, and what claim is it allowed to make?”

## 6. The lifecycle model has separate tracks

A corrected explainer should keep at least four tracks separate.

### 6.1 Project deliverable lifecycle

```text
OPEN → INITIALIZED → SEMANTIC_READY → IN_PROGRESS → CHECKING → ISSUED
```

Some working roots may omit or specialize states. The harness should read the local project convention rather than forcing a universal sequence.

### 6.2 Warrant/authentication lifecycle

```text
UNWARRANTED → CITED → REVIEWED → AUTHENTICATED
```

This is not the same thing as the deliverable lifecycle. A file can be checked but not authenticated. A claim can be cited but not professionally accepted.

### 6.3 Domain profile lifecycle

```text
NONE / UNKNOWN → DRAFT → VALIDATED → ADOPTED → STALE / INVALID
```

The exact enum requires the applicable domain-engine decision record. Validation can be deterministic. Adoption is human.

### 6.4 Tranche lifecycle

```text
CANDIDATE → HUMAN_ADOPTED → EXECUTED → CHECKED → HUMAN_REVIEWED → CLOSED / SUPERSEDED
```

A generated tranche brief begins as `CANDIDATE`. It becomes binding only if a human adopts it according to the project’s authority rule.

## 7. How one governed tranche flows

```text
1. Read current state
   - adapter reads status, plans, decisions, DAG/profile/evidence surfaces

2. Prepare candidate tranche
   - harness renders objective, basis, read scope, write scope, validations, evidence targets, stop conditions

3. Human adopts or edits the tranche
   - generated candidate becomes a governed work fence only through human adoption

4. Bounded work executes
   - agent/tool reads declared basis and writes only inside declared scope

5. Scope and evidence are checked
   - harness compares diff to write scope and evidence to brief requirements

6. Human reviews sufficiency and risk
   - evidence completeness is not professional sufficiency

7. Governed record is updated by the proper actor
   - closeout, issue, approval, or rejection stays in authored files and git history
```

The harness should make each step smaller and easier to inspect. It should not collapse the steps.

## 8. Where the harness fits in the repository

A practical implementation can live under:

```text
tools/practitioner_harness/
```

and produce generated outputs under project-local non-authoritative folders such as:

```text
<working-root>/_HarnessViews/
<working-root>/_HarnessBriefs/
<working-root>/_HarnessReports/
```

or an existing coordination-generated root if the project already has one.

The first implementation should not create or require a project-global database.

## 9. What the harness reads

The harness should read different roots through adapters.

```text
root_governance_adapter
  README.md
  CHIRALITY_FRAMEWORK.md
  PROFESSIONAL_ENGINEERING.md
  docs/DIRECTIVE.md
  docs/CONTRACT.md
  docs/SPEC.md
  docs/TYPES.md
  docs/PLAN.md

app_dev_adapter
  projects/chirality-app-dev local status, plan, coordination, decisions, validation surfaces

piping_adapter
  projects/chirality-piping PRD/DAG/status/decision/validation surfaces

domain_engines_adapter
  _DomainEngines/DOMAIN_ENGINE_INDEX.md
  _DomainEngines/_LATEST.md
  _DomainEngines/RULINGS_PUBLISHED.md
  _DomainEngines/_DECISIONS/**
  _DomainEngines/profiles/**
  _DomainEngines/profiles/_validation/**

git_adapter
  changed paths
  commit reachability
  approval SHA existence
  evidence age relative to changed files
```

The archive reviewed for this explainer does not contain the full live `projects/chirality-*`, `agents/`, `skills/`, or `tools/` trees. The harness must therefore degrade gracefully: report missing/unavailable surfaces as such, not invent their state.

## 10. What the harness produces

The harness produces four main generated artifact families.

| Output | Use | Authority status |
|---|---|---|
| Status projection | Current readable digest with source paths and caveats. | Generated view. |
| Self-check report | Contradictions, stale fields, path leaks, missing disclaimers, unresolved references. | Generated findings. |
| Candidate tranche brief | Proposed bounded work fence for a selected tranche. | Candidate until human adopted. |
| Scope/evidence findings | Objective comparison of work to brief and declared validations. | Check results, not approval. |

Every output should be source-cited and disposable.

## 11. What the harness must never claim

The harness must not say:

- “approved” unless a human-authored approval artifact says so;
- “issued” unless the governed lifecycle artifact says so;
- “professionally accepted”;
- “certified”;
- “sealed”;
- “ready for construction”;
- “safe”;
- “validation passed, therefore engineering correctness is established”;
- “closed” unless the governed record says closed.

Instead, it should say narrower things:

- “required validation artifact is present”;
- “approval SHA field is missing/TBD/reachable/unreachable”;
- “diff paths are within/outside the declared write scope”;
- “source hash matches/does not match”;
- “two current-state sources conflict”;
- “human review required.”

## 12. Domain-engine integration

The domain-engine integration boundary should look like this:

```text
Domain engine owns domain truth
  - model state
  - solver outputs
  - protected schemas
  - domain computation

Chirality governance records the boundary
  - profile
  - protected paths
  - readable artifacts
  - proposal paths
  - adoption/ruling state

Harness reads and checks
  - profile consistency
  - validation report presence
  - protected-path diff violations
  - stale open issues
  - human gate status

Human decides
  - adoption
  - apply authorization
  - professional reliance
```

For MVP, the harness should be **read-only** against `_DomainEngines` and protected project-domain paths. It can report whether a domain profile says `ADOPTED`, whether the validation report says valid, and whether other files contradict those claims. It cannot resolve the contradiction.

## 13. The self-check loop

The harness should audit the governance corpus itself.

Useful first checks:

- root governance basis is draft/pending;
- profile filename/header/status disagree;
- validation report says valid while profile comments say no validator exists;
- published rulings file contains mutually exclusive current-state statements;
- decision-record title says `PROPOSAL; HumanRuling: TBD` while the body contains a ruling;
- machine-absolute paths appear where portable governance requires repo-relative paths;
- generated outputs lack disclaimers;
- claims cite source paths that do not exist in the checkout/archive.

This is the difference between a real governance harness and governance theater: the harness must be willing to report uncomfortable contradictions in the governance corpus itself.

## 14. Storage rule

Use this rule everywhere:

> Authored files and git history are authority. Generated views and local caches are disposable projections. A projection may accelerate review, but deletion of the projection must not delete the governed truth.

SQLite is acceptable only under this rule.

## 15. One-sentence architecture summary

Chirality keeps reliance in authored files and human decisions, lets bounded agents propose and execute inside explicit scopes, and uses the governance harness as a deterministic bench tool to compile state, surface contradictions, prepare tranches, and check scope/evidence without ever becoming the authority.

## 16. Glossary

**Authority artifact** — A governed file or git-bound record that carries project truth.

**Evidence artifact** — A record of what happened: validation output, run record, command log, or evidence bundle.

**Generated view** — A rebuildable report or projection produced by the harness; not authority.

**Tranche** — A bounded intervention with an objective, basis, read/write scope, validations, evidence targets, and stop conditions.

**Scope check** — Comparison of changed paths to the adopted write/evidence scope.

**Evidence check** — Comparison of required validations/artifacts to what actually exists.

**Self-check** — Audit of the governance corpus for contradictions, stale fields, unresolved references, path leaks, and missing disclaimers.

**Approval SHA** — Git commit identifier that binds an approval/ruling to specific content.

**Warrant** — Evidence and reasoning that supports a claim.

**Authentication** — Human professional acceptance of responsibility for a claim/work product. It cannot be produced by the harness.
