# Workflow-Component Design Standard

> **Status: CANDIDATE IMPLEMENTATION of ruled direction D-GOV-10.** The
> architecture split is owner-ruled. This exact text remains reviewable and
> becomes authoritative only when accepted and published in the governed
> record. Until then, ratified `DIRECTIVE.md`, `CONTRACT.md`, `SPEC.md`,
> `TYPES.md`, and the live `AGENTS.md` govern on disagreement.

This document defines how Chirality agents, skills, deterministic tools,
briefs, and workflow packages are designed, classified, maintained, and
retired. It is the normative design standard applied by HELPS_HUMANS and the
subsystem-maintenance personas.

It replaces the standards content formerly embedded in
`agents/AGENT_HELPS_HUMANS.md`. The persona now applies and maintains this
standard; it is not itself the source of constitutional authority.

---

## 1. Purpose

Workflow components help humans complete complex work over long horizons by:

- making scope, authority, and write boundaries explicit;
- preserving provenance, claim calibration, and auditability;
- separating human decision rights from agent execution;
- producing durable, rerunnable filesystem artifacts where persistence is
  warranted;
- minimizing operator friction through bounded briefs and a small number of
  coherent persona interfaces; and
- making handoffs, closure, staleness, and remaining blockers inspectable.

The standard applies to the shared instruction surface and to working-root
overlays that extend it. A working-root design may specialize this standard
but must not weaken framework invariants.

---

## 2. Authority and precedence

### 2.1 Framework authority chain

Workflow-component design inherits the root authority chain:

1. `DIRECTIVE.md` — founding intent and governing principles.
2. `CONTRACT.md` — binding K-* invariants.
3. `SPEC.md` and `TYPES.md` — physical contracts and canonical vocabulary.
4. `AGENTS.md` — authoritative live governance surface, integration rules,
   registry, and canonical TASK-skill relationships.
5. This standard — workflow-component classification and design rules.
6. The applicable `AGENT_*.md`, skill contract, tool contract, or brief.

Accepted human decision records may amend governed direction. A transient
conversation does not silently rewrite the durable framework: when a human
ruling changes governed design, the ruling is recorded and SHA-bound through
the owning workflow.

Where live registries and narrative documents disagree, the live registry
governs operational discovery and the discrepancy is surfaced. Narrative
staleness is a finding, not an alternate registry.

### 2.2 Local runtime precedence

Within a TASK run, authorization is resolved by the TASK shell. A brief or
skill may narrow authority but may not relax the shell, K-* invariants,
ScopePath containment, or an owning workflow's accepted gate conditions.

Within an agent instruction file, required sections retain this precedence:

```text
PROTOCOL > SPEC > STRUCTURE > RATIONALE
```

RATIONALE is non-normative and cannot create permissions.

---

## 3. Workflow-component model

### 3.1 Agent

An agent is a governed actor surface. It qualifies only when it owns at least
one distinction that cannot be represented safely by TASK plus a skill:

- a distinct human interaction or gate lifecycle;
- a distinct decision-right or escalation contract;
- a distinct shell-level context, invocation, or authorization boundary;
- durable workflow-state ownership or handoff responsibility; or
- a write-scope posture whose enforcement cannot be expressed by a bounded
  TASK brief.

A different topic, output schema, tool recipe, or snapshot folder is not by
itself a reason to create an agent.

### 3.2 Skill

A skill is a reusable bounded reasoning method executed through TASK. It owns
method steps, method-specific inputs and outputs, tool composition guidance,
QA checks, and failure semantics. It does not own human decision rights,
shell authorization, or independent runtime identity.

### 3.3 Deterministic tool

A tool performs an LLM-independent operation with declared inputs, outputs,
scope, exit behavior, and idempotence posture. Parsing, validation,
scaffolding, graph algorithms, deterministic transformation, and report
rendering belong here when they require no semantic judgment.

### 3.4 Brief

A brief carries run-specific purpose, scope, paths, constraints, permissions,
runtime overrides, expected outputs, and acceptance checks. One-off guidance
does not become a skill or agent merely because it is detailed.

### 3.5 Workflow package

A workflow package combines personas, TASK skills, tools, briefs, governed
artifacts, and handoff contracts into a multi-step lifecycle. A package does
not acquire authority beyond the authority class of its constituent records.

---

## 4. Requalification and anti-proliferation rule

Agent status is not grandfathered. Every existing or proposed agent must pass
this classification sequence:

1. Does it own a distinct human interaction, gate, decision, shell, context,
   authorization, or handoff contract?
   - **Yes:** an agent may be warranted.
   - **No:** continue.
2. Does it require recurring LLM reasoning under a bounded brief?
   - **Yes:** use TASK plus a skill.
   - **No:** continue.
3. Is it deterministic?
   - **Yes:** use a tool.
   - **No:** continue.
4. Is it run-specific?
   - **Yes:** keep it in the brief.
   - **No:** surface the unresolved classification rather than minting a
     component by default.

Type 2 identity is exceptional. TASK is the canonical Type 2 execution shell.
Another Type 2 agent persists only when its shell-level behavior cannot be
lawfully or coherently represented by TASK hydration and bounded write
authorization.

---

## 5. Human authority and operational execution

### 5.1 Human-owned semantic decisions

The following remain human decisions:

- acceptance, authentication, issuance, or release for reliance;
- conflict and contradiction rulings;
- scope inclusion, exclusion, and boundary changes;
- governing-code, design-basis, hazard, and residual-risk decisions;
- adoption of a governed brief or profile;
- merge/integration decisions that change an accepted baseline;
- destructive or history-rewriting Git actions; and
- exceptions or overrides to objective governance blocks.

Agents may prepare evidence, options, proposals, and decision records. They
must not represent their own execution as a human ruling.

### 5.2 Routine Git closeout

Ordinary scoped `git add`, `git commit`, and `git push` may be executed without
a second approval token when an explicit human request, project-local rule, or
accepted owning-workflow handoff already authorizes closeout and all of the
following are true:

- the tranche and writable paths are bounded;
- required validation or an explicit skipped-check rationale is recorded;
- unrelated dirty files can be excluded;
- no merge, rebase, reset, cleanup, force operation, or history rewrite is
  involved; and
- the push target is already established or explicitly named.

The Git act records and transports candidate or accepted work. It is not
acceptance, issuance, authentication, professional approval, or a substantive
ruling. Ambiguous staging, integration, or risky actions stop for human
direction.

---

## 6. Artifact authority classes

Every workflow design must identify the authority class of its outputs.

| Class | Meaning | Typical examples |
|---|---|---|
| Authoritative truth | Accepted state owned by the governing workflow or domain engine | accepted decomposition snapshot, `_STATUS.md`, human ruling, adopted profile |
| Candidate governed record | Proposed or working record that may become authoritative only through its gate | candidate brief, proposed amendment, review candidate |
| Derivative package | Regenerated or synthesized package built from accepted upstream truth; never a substitute for that truth | `_Aggregation`, hypergraph, audit, concordance, publication package |
| Factual evidence artifact | Observed run facts with declared boundary; never approval | validation evidence, run log, scope-check record |
| Generated view | Rebuildable presentation or report; never read as authority | status report, dashboard export, rendered review surface |
| Convenience state | Non-authoritative local/runtime preference | UI state, local cache where permitted |

Generated views and evidence artifacts must not silently feed back as
authority. A derivative package cites the accepted upstream snapshot(s) from
which it was produced.

---

## 7. Write scope, containment, snapshots, and pointers

### 7.1 Write scope

Every agent declares a write scope. Every TASK run resolves explicit
`AllowedWriteTargets`; `ScopePath` alone does not grant writes. All writes are
subject to K-WRITE-2: normalized real paths must remain under the active
checkout, with symlink and traversal escapes rejected.

### 7.2 Snapshot applicability

Snapshots are required when:

- a phase-boundary decision changes or validates governed state;
- an owning workflow requires an immutable audit/evidence bundle;
- a tool-root analysis or derivative package must remain reproducible; or
- later phases need a stable accepted input rather than mutable working state.

Snapshots are not mandatory for every file edit. Deliverable-local edits,
generated scratch projections, transient rendering, and deterministic
regeneration may use their owning contracts instead. The design must state
which outputs are immutable, mutable, rebuildable, or authoritative.

### 7.3 Pointers

Pointers are mutable conveniences. They may reference the latest or accepted
snapshot only where the owning workflow permits pointer updates. A pointer is
not the snapshot and cannot establish acceptance by itself.

---

## 8. Epistemic controls

All claim-producing components inherit:

- **K-PROV-1:** non-trivial governed claims cite a source path and
  best-effort section reference, or carry explicit `location TBD`.
- **K-INVENT-1:** unknown values become `TBD`; missing evidence is surfaced.
- **K-CONFLICT-1:** incompatible warranted claims are exposed for human
  adjudication rather than silently resolved.
- **K-CLAIM-1:** claim strength must not exceed warrant strength. Necessity,
  sufficiency, universality, completeness, exclusivity, safety, compliance,
  and regulatory conclusiveness require evidence supporting that strength.

Per D-GOV-08, warrant-state ladders and FACT labeling are audit-time
diagnostics, not mandatory producer-emitted fields. Producing components must
provide concrete provenance and calibrated language; they need not decorate
every claim with an epistemic token.

---

## 9. Handoff, closure, sequencing, and cycles

Every multi-phase workflow must implement the governance integration rules in
`AGENTS.md`:

1. Later phases consume accepted upstream snapshots, not mutable working state
   alone.
2. A workflow that stops with later work remaining emits a handoff state that
   names accepted upstream snapshots, derivative-package currency, closure
   verdict, rerun requirements, blockers, and the next lawful owner.
3. Closure requires accepted truth, current or explicitly deferred derivative
   packages, recorded audit status, and surfaced blockers. File creation alone
   is not closure.
4. Strongly connected dependency components are not silently linearized.
   Cycle-participating edges remain non-gating until a recorded
   decompose/invert/merge/cut move resolves the ordering; merge and cut remain
   human-gated.

---

## 10. Agent instruction contract

Every `AGENT_*.md` file must contain:

1. YAML frontmatter with at least `description`.
2. `[[DOC:AGENT_INSTRUCTIONS]]`.
3. `# AGENT INSTRUCTIONS — <ROLE> (<descriptor>)`.
4. `AGENT_TYPE: 0|1|2` in the body.
5. An Agent Type table containing:
   `AGENT_TYPE`, `AGENT_CLASS`, `INTERACTION_SURFACE`, `WRITE_SCOPE`,
   `BLOCKING`, and `PRIMARY_OUTPUTS`.
6. Explicit precedence and inherited governance references.
7. Non-negotiable invariants proportionate to the role.
8. Delimited `PROTOCOL`, `SPEC`, `STRUCTURE`, and `RATIONALE` sections.
9. Inputs, outputs, failure posture, and handoff behavior where applicable.
10. Compatibility/deprecation notes when replacing an earlier surface.

Type 1 personas use conversation and human gates only where a consequential
decision exists. Type 2 shells run straight through; invalid required inputs
fail explicitly, while absent evidence becomes a surfaced gap rather than an
invented value.

---

## 11. Skill contract

A live skill folder contains:

- `SKILL.md` — authoritative method and output contract;
- `BRIEF_SCHEMA.md` — required and optional dispatch fields;
- `TOOL_POLICY.md` — preferred, optional, and prohibited tools plus fallback
  conditions; and
- `QA_CHECKS.md` — method-specific invariants and validity checks.

Folder name, skill name, metadata version, TASK compatibility, and any
`allowed-tools` declaration must pass the skill metadata validator. Skills do
not reconstruct shell authorization and dispatchers do not reconstruct the
skill contract in ad hoc prompts.

---

## 12. Tool contract

A deterministic tool must provide:

- a registry entry in `tools/REGISTRY.md`;
- declared inputs, outputs, scope, exit codes, and error posture;
- an idempotence posture (`idempotent`, `one-shot`, or explicitly stateful);
- fail-fast handling for invalid required inputs;
- tests proportionate to mutation and governance risk; and
- no dependence on LLM interpretation at execution time.

A tool may render a brief from structured parameters, but it must derive from
authoritative templates/contracts rather than duplicating drifting prompt
text.

---

## 13. Workflow design outputs

Design output is proportional to novelty and risk. A new or materially changed
workflow must cover every applicable concern below, but need not manufacture a
separate artifact for inapplicable concerns:

- system and authority map;
- human agency and permission map;
- component classification and dispatch graph;
- filesystem and artifact-authority contracts;
- briefs and runtime inputs;
- snapshot, pointer, handoff, and closure contracts;
- schemas and controlled vocabularies;
- provenance, conflict, and claim-calibration controls;
- QA, failure, rerun, and deprecation behavior;
- publication/integration behavior; and
- open issues and human decisions still required.

The least complete package that makes these concerns explicit is preferred
over ceremony that merely repeats inherited rules.

---

## 14. Compliance requirements

The established R1–R12 identifiers remain stable for compatibility. R13–R17
extend the catalog for the ratified governance added after the original
standard.

| ID | Requirement |
|---|---|
| R1 | Human decision rights are explicit and preserved. |
| R2 | Bounded task execution runs straight through without mid-run human decisions. |
| R3 | Every agent and run has an explicit write boundary; tool-root outputs do not silently modify source truth. |
| R4 | Snapshot requirements match artifact authority and phase-boundary needs; immutable snapshots are never overwritten. |
| R5 | Non-trivial governed claims carry schema-appropriate provenance or explicit `location TBD`. |
| R6 | Missing information is represented as `TBD` or a gap, never invented. |
| R7 | Conflicts and duplicates are surfaced; semantic resolution remains human-owned. |
| R8 | Reusable bounded execution is brief-driven with explicit inputs, permissions, outputs, and failure posture. |
| R9 | Publication and Git operations are reviewable and non-destructive; operational closeout is never represented as semantic approval. |
| R10 | Every skill has an explicit tool policy. |
| R11 | Every deterministic tool has an explicit input/output, scope, error, test, and idempotence contract. |
| R12 | Agent, shell, skill, tool, and brief responsibilities do not cross silently. |
| R13 | Claim strength is calibrated to warrant strength under K-CLAIM-1. |
| R14 | Multi-phase workflows implement derivative-package, accepted-snapshot, handoff, closure, sequencing, and cycle rules. |
| R15 | Live registry membership and lifecycle status are explicit; narrative drift is surfaced and deprecated surfaces are not silently treated as active. |
| R16 | All task writes satisfy active-checkout containment under K-WRITE-2. |
| R17 | Workflow-design artifacts are proportional but cover every applicable authority, execution, QA, handoff, and retirement concern. |

---

## 15. Lifecycle and deprecation

Workflow components use these lifecycle labels in design and migration
records:

| Label | Meaning |
|---|---|
| `CANDIDATE` | Proposed; not available for canonical dispatch. |
| `ACTIVE` | Discoverable in the live registry and supported. |
| `DEPRECATED` | Still available for bounded compatibility; replacement and removal condition are named. |
| `RETIRED` | Removed from live discovery; retained only in history/archive where required. |

Deprecation requires:

- named replacement or explicit no-replacement rationale;
- compatibility scope and sunset/removal condition;
- dispatcher and registry updates;
- preserved provenance for historical runs; and
- validation that active surfaces no longer depend on the retired component.

No component is retired merely by deleting its instruction file.

---

## 16. Maintenance and audit

HELPS_HUMANS maintains this standard through governed proposals and owner
review. SKILLMAKER and TOOLMAKER maintain their subordinate subsystem
contracts. AUDIT mechanisms assess conformance but do not amend the standard.

Every suite-wide audit records:

- the standard and governing SHAs used;
- live registry membership at audit time;
- per-component disposition and evidence;
- conflicts between narrative and live surfaces;
- compatibility obligations; and
- whether findings are structural, semantic, or human-decision dependent.

