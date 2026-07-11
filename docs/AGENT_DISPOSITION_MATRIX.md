# Agent Suite Disposition Matrix

> **Status: CANDIDATE implementation analysis under D-GOV-10.** Dispositions
> are migration proposals, not retirement acts. A component remains live until
> its replacement, callers, compatibility posture, registry changes, and
> validation evidence are complete and accepted.

## 1. Basis and observation boundary

Basis:

- `docs/WORKFLOW_COMPONENT_STANDARD.md`
- D-GOV-10
- live `AGENTS.md`
- all 38 live `agents/AGENT_*.md` files at branch base `052b3c2b2`
- live skill folders and `skills/README.md`
- `tools/REGISTRY.md`
- deterministic `validate_agent_instructions.py` results

This is an instruction-architecture audit. It does not evaluate the quality of
project deliverables or the in-progress piping/app-dev reconciliation work.

Disposition vocabulary:

- `RETAIN` — agent contract is justified substantially as-is.
- `SLIM` — agent-level contract persists; method/tool detail moves downward.
- `MERGE` — authority/interaction surface joins another persona.
- `CONVERT_TO_SKILL` — bounded reasoning moves under TASK.
- `CONVERT_TO_TOOL` — deterministic behavior moves to tools.
- `RETIRE` — no live role remains after compatibility closure.

## 2. Suite summary

| Primary disposition | Count | Meaning for this tranche |
|---|---:|---|
| RETAIN | 3 | Preserve the actor/shell contract; align wording and references |
| SLIM | 15 | Preserve persona identity but move reusable method and deterministic detail down |
| MERGE | 6 | Consolidate overlapping Type 1 surfaces after target persona contracts are ready |
| CONVERT_TO_SKILL | 11 | Replace bespoke Type 2 method shells with TASK skills |
| CONVERT_TO_TOOL | 3 | Replace predominantly deterministic Type 2 behavior with tools, adding a skill only for residual reasoning |
| RETIRE | 0 | No direct deletion proposed before migration evidence exists |
| **Total** | **38** | |

The target is not “three agents.” The target is a small set of justified
personas, one canonical Type 2 shell, method skills, and deterministic tools.

## 3. Per-agent matrix

### 3.1 Standards and workflow-component maintenance

| Agent | Current contract evidence | Agent-level distinction | Primary disposition | Target and migration note | Confidence |
|---|---|---|---|---|---|
| HELPS_HUMANS | Type 1 chat; repo-wide component-design scope; five-phase classify/design/implement/handoff protocol | Owns human-facing architecture decisions, cross-layer classification, migration design, and standards-maintenance handoff | RETAIN | Candidate rewrite already separates persona from `WORKFLOW_COMPONENT_STANDARD.md` | High |
| DECOMP_BASE | Type 0 persona plus embedded seven-phase canonical decomposition protocol and I1–I10 | The protocol is normative; the conversational design function overlaps HELPS_HUMANS | MERGE | Move normative protocol to `docs/DECOMPOSITION_STANDARD.md`; merge decomposition-agent design/conformance conversation into HELPS_HUMANS; preserve I-IDs | Medium-high |
| SKILLMAKER | Type 1 chat; repo-wide skill subsystem; six-phase classify/design/implement/runtime-alignment protocol | Human design gates are real, but they are the skill-specific application of HELPS_HUMANS classification | MERGE | HELPS_HUMANS owns skill-design mode; retain `skills/README.md`, templates, validator, and a bounded skill-authoring workflow package | High |
| TOOLMAKER | Type 1 chat; repo-wide tools; five-phase candidate/design/implement/register protocol | Human design gates are real, but they duplicate HELPS_HUMANS component classification and implementation management | MERGE | HELPS_HUMANS owns tool-design mode; retain tool contract in docs/registry and deterministic implementation practices | High |
| CONTEXT_TRANSPOSE | Type 1 chat; seven-phase context inventory/contract/patch workflow; repo-metadata writes | Target-context rulings need a human, but the actor surface is workflow architecture/change design | MERGE | HELPS_HUMANS owns the human contract; create `context-transpose` TASK skill for bounded comparison/patch-plan reasoning plus tools for deterministic inventory | Medium-high |

### 3.2 Core human-facing project personas

| Agent | Current contract evidence | Agent-level distinction | Primary disposition | Target and migration note | Confidence |
|---|---|---|---|---|---|
| HELP_HUMAN | Read-only chat; intent classification, minimum questions, next-step cards, commitment support | General operator guidance and intent-to-brief translation are a distinct entry surface | SLIM | Retain entry persona; remove duplicated component taxonomy and rely on HELPS_HUMANS/ORCHESTRATOR for specialized design | Medium |
| ORCHESTRATOR | Type 1 chat; control-plane artifacts; setup gates, tier dispatch, and durable session handoff ownership | Owns project initialization, accepted setup sequence, control-loop state, and cross-phase handoff | SLIM | Retain; replace PREPARATION, DOMAIN_HYPERGRAPH, AGGREGATION, and scheduling/evaluation specialist dispatches with TASK skills/tools; move method recipes out | High |
| WORKING_ITEMS | Deliverable-local Type 1 chat; bounded work increments; conflicts; session-state handoff | Owns ongoing deliverable conversation, local decisions, and coordination-state update | SLIM | Retain; method-specific production moves to TASK skills; keep objective framing, human rulings, conflict interface, and handoff | High |
| RECONCILIATION | Type 1 chat; cross-deliverable tool root; plan/dispatch/validate/synthesize decision interface | Owns cross-scope human interpretation, conflict/closure decisions, and synthesis handoff | SLIM | Retain as the primary audit/evaluation/reconciliation persona; absorb EVALUATION and consume audit skills | High |
| CHANGE | Type 1 chat; Git/file-state evidence, worktree lanes, risky-action gates, routine closeout | Owns Git-state interpretation, integration/destructive-action gates, and lane/closeout handoff | SLIM | Retain; move deterministic state collection and checks to tools; align vocabulary with D-GOV-10 routine-closeout ruling | High |
| REVIEW | Type 1 chat; five formal gates; findings disposition and lifecycle transition | Owns candidate freeze/review conversation and human lifecycle decision | RETAIN | Preserve; update inherited standard references and artifact/handoff language | High |
| RESEARCH | Type 1 chat; question classification, retrieval choices, evidence synthesis, optional packet/handoff | Owns human question framing, source-bound synthesis choices, and action handoff | SLIM | Retain; replace RESEARCHER with TASK research skill and keep audit-time evidence semantics | High |

### 3.3 Decomposition and governed-change personas

| Agent | Current contract evidence | Agent-level distinction | Primary disposition | Target and migration note | Confidence |
|---|---|---|---|---|---|
| PROJECT_DECOMP | Type 1 chat; seven human-confirmed phases from intake through accepted decomposition | Owns project-specific partition/deliverable rulings and decomposition acceptance gates | SLIM | Retain persona; consume extracted decomposition standard; move atomization/coverage mechanics to skills/tools | High |
| SOFTWARE_DECOMP | Type 1 chat; seven gates plus software context-envelope decisions | Owns software-specific scope/package/deliverable and context-budget rulings | SLIM | Retain as a domain specialization unless later evidence supports a parameterized PROJECT_DECOMP mode; move mechanics down | Medium-high |
| DOMAIN_DECOMP | Type 1 chat; six gates plus source-review sub-gates, large-corpus dispatch, browser review, and accepted domain decomposition | Owns source-scope, category, KTY, coverage, and publication rulings across a long-lived corpus workflow | SLIM | Retain; large portions are already skills/tools; extract remaining method detail into a domain-decomposition workflow package | High |
| SCOPE_CHANGE | Type 1 chat; five gates for intake, impact, amendment, propagation, execution/validation | Owns change-scope rulings, decomposition amendment, propagation acceptance, and closure handoff | SLIM | Retain; move impact/remediation/audit methods to TASK skills; keep human gates and authoritative amendment ownership | High |
| DOMAIN_ENGINE | Type 1 chat; profile adoption, protected paths, operation proposals, domain-tool gates, external handoff | Owns unique domain-engine authority boundary and protected operation lifecycle | SLIM | Retain; move profile inspection, readiness scans, and proposal drafting methods into skills/tools while preserving gates | High |

### 3.4 Specialized publication and source-processing personas

| Agent | Current contract evidence | Agent-level distinction | Primary disposition | Target and migration note | Confidence |
|---|---|---|---|---|---|
| DBM_PUBLISHER | Type 1 chat; seven gates freezing authority, schema, section map, synthesis, evidence review, acceptance/handoff | Owns publication-specific human freezes and acceptance interface over derivative packages | SLIM | Retain; skills already own section/package/concordance methods; reduce persona to gates, accepted-snapshot checks, and handoff | High |
| EQUATION_AUDIT | Type 1 chat; iterative human review, fix interpretation, backcheck, and close gates | Owns a genuine human adjudication loop and closure decision over equation corrections | SLIM | Retain; keep review loop and audit-state ownership, move bbox/interpret/apply mechanics to skills/tools | High |
| PDF2MD | Type 1 chat; resumable conversion phases, optional folio/assets, assembly, equation-audit handoff | Owns run-level source conversion state and downstream audit handoff, but few semantic gates are currently explicit | SLIM | Retain provisionally; extract a `pdf2md-workflow` package and reassess whether ORCHESTRATOR can own the remaining interaction after migration | Medium |
| DRAWING_EXTRACT | Type 1 chat; target-aware resume state, manual crop overrides, extraction dispatch, QA, optional merge | Owns operator review/override and run-state recovery across heterogeneous drawing targets | SLIM | Retain provisionally; move core phase mechanics to workflow skills/tools and re-test whether the remaining human interface is distinct | Medium |
| SCHEDULING | Type 1 chat; five gates from graph intake through duration/calendar choices and publication | Human scheduling choices are real, but project sequencing/control-loop ownership already sits with ORCHESTRATOR | MERGE | ORCHESTRATOR owns schedule gates; create scheduling TASK skill(s) plus deterministic graph/render tools | Medium-high |
| EVALUATION | Type 1 chat; scope/dimension selection, collection, scoring, synthesis | Human evaluation scope and judgment are real, but cross-scope audit synthesis overlaps RECONCILIATION | MERGE | RECONCILIATION owns evaluation mode; scoring/reporting methods move to TASK skills | High |

### 3.5 Canonical shell and Type 2 requalification

| Agent | Current contract evidence | Shell-level distinction | Primary disposition | Replacement and compatibility note | Confidence |
|---|---|---|---|---|---|
| TASK | Type 2 shell; brief normalization, authorization, skill hydration, run record, epistemic/failure controls | Canonical shell contract itself | RETAIN | Preserve; remove obsolete profile-file references and keep bounded compatibility labels inline | High |
| PREPARATION | Type 2 spawned; scaffolds known folders/templates/tool roots from structured task type | Predominantly deterministic file creation; no unique reasoning shell | CONVERT_TO_TOOL | Add/extend deterministic workspace scaffold tool(s); ORCHESTRATOR invokes them under bounded paths; retain compatibility adapter until callers migrate | High |
| AGGREGATION | Type 2 brief-driven cross-scope synthesis snapshot | Method/output differences only; authorization fits TASK | CONVERT_TO_SKILL | `cross-scope-aggregate` skill plus deterministic merge/pivot tools; ORCHESTRATOR/RECONCILIATION dispatch TASK | High |
| RESEARCHER | Type 2 dispatched evidence packet executor | Method and packet schema only; authorization fits TASK | CONVERT_TO_SKILL | `research-packet-execute` skill, reusing research-orchestration and retrieval tools; RESEARCH dispatches TASK | High |
| AUDIT_AGENTS | Type 2 audit snapshot using rubric and evidence excerpts | Audit method only; no unique shell | CONVERT_TO_SKILL | `agent-instruction-audit` skill; HELPS_HUMANS or RECONCILIATION dispatches TASK | High |
| AUDIT_DECOMP | Type 2 decomposition coverage audit | Audit method only; no unique shell | CONVERT_TO_SKILL | `decomposition-audit` skill; parameterize variant and accepted basis | High |
| AUDIT_DEP_CLOSURE | Type 2 dependency closure/hub/cycle audit | Audit method only; graph computations already tool-shaped | CONVERT_TO_SKILL | `dependency-closure-audit` skill plus deterministic graph tools; RECONCILIATION dispatches | High |
| AUDIT_EPISTEMIC | Type 2 evidence/warrant diagnostic audit | Audit-time semantic method under D-GOV-08; no unique shell | CONVERT_TO_SKILL | `epistemic-audit` skill; preserve observation-boundary and non-approval language | High |
| AUDIT_GOVERNANCE | Type 2 cross-document consistency/invariant/reference audit | Mix of semantic audit and deterministic scans; no unique shell | CONVERT_TO_SKILL | `governance-audit` skill consuming validators; HELPS_HUMANS/RECONCILIATION dispatches | High |
| AUDIT_HYPERGRAPH_CLOSURE | Type 2 closure audit over a hypergraph snapshot | Audit method only | CONVERT_TO_SKILL | `hypergraph-closure-audit` skill consuming accepted hypergraph snapshot | High |
| AUDIT_SCOPE_CLOSURE | Type 2 scope-change closure audit | Audit method only; distinct schema but no shell semantics | CONVERT_TO_SKILL | `scope-closure-audit` skill, reusing decomposition-package-review where compatible | High |
| DOMAIN_HYPERGRAPH | Type 2 builds a hypergraph snapshot from structured decomposition ledgers/maps | Core graph construction and validation are deterministic | CONVERT_TO_TOOL | Deterministic hypergraph builder/validator; optional thin TASK skill only for semantic gap commentary | Medium-high |
| EVALUATION_REPORT | Type 2 scored dimension report | Evaluation reasoning/output method only | CONVERT_TO_SKILL | `evaluation-report` skill dispatched by RECONCILIATION evaluation mode | High |
| EVALUATION_STRUCTURE_AUDIT | Type 2 structural validation report | Predominantly deterministic structure checking | CONVERT_TO_TOOL | Validator/report tool; optional TASK skill only if narrative interpretation remains | Medium-high |
| EVALUATION_DEPENDENCY_AUDIT | Type 2 dependency validation report | Mix of graph checks and bounded interpretation; no shell distinction | CONVERT_TO_SKILL | `evaluation-dependency-audit` skill consuming deterministic dependency checks | High |

## 4. Target topology

The provisional target after all waves is:

### Normative documents

- Workflow-Component Standard
- Decomposition Standard (extracted from DECOMP_BASE)
- root K-* / SPEC / TYPES governance

### Core personas

- HELP_HUMAN — entry guidance
- HELPS_HUMANS — workflow-component architecture and subsystem design
- ORCHESTRATOR — setup, control loops, schedule/setup/evaluation dispatch
- WORKING_ITEMS — deliverable-local production conversation
- RECONCILIATION — cross-scope audit, evaluation, and coherence decisions
- CHANGE — Git/file-state integration
- REVIEW — formal lifecycle review
- RESEARCH — evidence-grounded inquiry

### Specialized governed personas

- PROJECT_DECOMP, SOFTWARE_DECOMP, DOMAIN_DECOMP
- SCOPE_CHANGE
- DOMAIN_ENGINE
- DBM_PUBLISHER
- EQUATION_AUDIT
- provisionally PDF2MD and DRAWING_EXTRACT pending post-slim requalification

### Canonical execution

- TASK only, with skills for bounded methods and tools for deterministic work

This target would reduce the live agent count from 38 to approximately 16–18,
depending on the final PDF2MD/DRAWING_EXTRACT and decomposition-specialization
decisions. The reduction is a consequence of contract classification, not a
numerical goal.

## 5. Migration waves

### Wave 0 — Foundation

- Record D-GOV-10.
- Split the workflow-component standard from HELPS_HUMANS.
- Repair the DBM, rubric, and deterministic validator.
- Accept this disposition matrix.

### Wave 1 — Non-TASK Type 2 agents

1. PREPARATION and deterministic DOMAIN_HYPERGRAPH/EVALUATION structure work.
2. Audit agents as TASK skills, grouped by shared audit contract.
3. AGGREGATION and RESEARCHER methods.
4. Evaluation report/dependency methods.
5. Dispatcher, registry, compatibility, and narrative updates.

Wave 1 closes only when no live dispatcher requires a removed Type 2 file.

### Wave 2 — Overlapping Type 1 managers

- Merge SKILLMAKER and TOOLMAKER into HELPS_HUMANS modes.
- Merge CONTEXT_TRANSPOSE into HELPS_HUMANS plus a bounded skill.
- Merge EVALUATION into RECONCILIATION.
- Merge SCHEDULING into ORCHESTRATOR.

### Wave 3 — Decomposition standard extraction

- Move DECOMP_BASE normative content into `docs/DECOMPOSITION_STANDARD.md`.
- Merge its conversational architect function into HELPS_HUMANS.
- Slim PROJECT/SOFTWARE/DOMAIN decomposition personas against the extracted
  standard without changing accepted decomposition truth.

### Wave 4 — Specialized persona slimming

- Slim DBM_PUBLISHER, EQUATION_AUDIT, DOMAIN_ENGINE, SCOPE_CHANGE, PDF2MD, and
  DRAWING_EXTRACT.
- Requalify PDF2MD and DRAWING_EXTRACT again after method extraction.

## 6. Required validation per wave

- agent instruction validator: zero errors;
- skill metadata validator: all live skills valid;
- agent registry currency: zero drift;
- no unresolved live agent-file references;
- relevant skill/tool unit tests;
- dispatcher search proving no removed caller remains;
- K-CLAIM-1 language review for PASS/approval/closure terms;
- path-containment validation;
- migration handoff with accepted upstream basis, compatibility status,
  rerun requirements, and blockers.

## 7. Decisions still requiring review

The following are implementation-level review points, not unruled architecture
forks:

1. Whether SOFTWARE_DECOMP remains a separate persona after the shared
   decomposition standard is extracted.
2. Whether PDF2MD and DRAWING_EXTRACT retain enough human interaction/state
   ownership after slimming to remain personas.
3. Whether DOMAIN_HYPERGRAPH needs a residual interpretation skill or can be
   entirely deterministic.
4. Whether EVALUATION_STRUCTURE_AUDIT has any semantic content that warrants a
   thin skill above its validator.
5. Compatibility duration for historical `TaskProfile: DELIVERABLE_TASK` and
   other retired names.
