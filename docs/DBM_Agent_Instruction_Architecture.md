# DBM — Workflow-Component Architecture

> **Status: CANDIDATE AMENDMENT implementing D-GOV-10.** This memorandum is
> explanatory, not an independent registry or invariant catalog. On
> disagreement, `DIRECTIVE.md`, `CONTRACT.md`, `SPEC.md`, `TYPES.md`,
> `AGENTS.md`, and `WORKFLOW_COMPONENT_STANDARD.md` govern in that order.

## Purpose and scope

This design-basis memorandum explains how Chirality's workflow-component
layers fit together:

1. normative governance documents;
2. human-facing personas and the canonical TASK shell;
3. repo-native skills;
4. deterministic tools;
5. briefs and workflow packages; and
6. runtime artifacts, snapshots, handoffs, and generated views.

It does not define live membership. `AGENTS.md` owns the live agent registry,
live `skills/*/SKILL.md` folders own skill membership, and
`tools/REGISTRY.md` owns deterministic-tool discovery. This memorandum must be
updated when it no longer explains those surfaces accurately, but a stale DBM
cannot create or preserve a component.

## Governing documents

| Document | Authority |
|---|---|
| `DIRECTIVE.md` | Founding intent, professional posture, and authority chain |
| `CONTRACT.md` | Binding K-* invariants |
| `SPEC.md` | Filesystem, schema, path, snapshot, and instruction-file contracts |
| `TYPES.md` | Canonical entities, identifiers, enums, and type semantics |
| `AGENTS.md` | Live agent registry, governance integration rules, and canonical TASK-skill dispatch relationships |
| `WORKFLOW_COMPONENT_STANDARD.md` | Component classification, design, lifecycle, and conformance rules |
| `AGENT_DECOMP_BASE.md` | Type 0 decomposition protocol standard (I1–I10 and decomposition gates) |

`PLAN.md` records direction rather than binding requirements. Working-root
governance may specialize the framework but may not weaken root invariants.

---

## 1. Architectural principles

### 1.1 Filesystem authority

Authoritative governance and project state live in git-tracked files, subject
to the domain-engine exception in K-DOMAIN-1. Generated views and rebuildable
projections do not become authority by being convenient or current-looking.

### 1.2 Human semantic authority

Humans own acceptance, issuance, authentication, scope boundaries, conflict
rulings, baseline integration, destructive actions, and professional
judgment. Agents prepare evidence, proposals, changes, and records. A tool or
agent PASS is structural evidence within a declared observation boundary, not
semantic or professional approval.

### 1.3 Evidence-first operation

Claim-producing components provide extrinsic provenance, expose gaps and
conflicts, and calibrate claim strength to warrant strength. Warrant lifecycle
labels are audit-time diagnostics under D-GOV-08; producers are not required
to emit FACT or warrant-state tags on every claim.

### 1.4 Separation of instruction and execution

The release-managed instruction root defines behavior; working roots hold
project/domain state. TASK write targets must resolve inside the active
checkout. This permits one instruction system to serve many isolated working
roots and git worktrees.

### 1.5 Least sufficient structure

Structure exists to reduce error, preserve authority, and make reruns and
handoffs safe. It is not a goal in itself. A design covers all applicable
contracts without manufacturing empty artifacts or new personas.

---

## 2. Component layers

```text
Root governance and standards
        │ constrain
        ▼
Type 1 personas ── compose briefs / hold gates / own handoffs
        │ dispatch
        ▼
TASK shell ── resolves context, authorization, hydration, run record
        │ loads                       │ invokes
        ▼                             ▼
Skills (reasoning methods)      Tools (deterministic operations)
        │                             │
        └──────── produce governed/evidence/derivative artifacts ────────┐
                                                                          │
Human review, rulings, acceptance, and next-phase authorization ◀─────────┘
```

### 2.1 Normative standards

Normative standards live in governed documents. D-GOV-10 moved the general
workflow-component standard out of HELPS_HUMANS so the applying persona no
longer doubles as its own constitution.

`AGENT_DECOMP_BASE.md` remains a Type 0 protocol standard during this
transition. Its eventual disposition is assessed independently; D-GOV-10
does not silently reclassify it.

### 2.2 Type 1 personas

Type 1 personas provide a human interaction surface where the workflow needs
distinct gates, decision support, authority translation, state ownership, or
handoff responsibility. They may compose and dispatch bounded TASK briefs.

HELPS_HUMANS is now a Type 1 architect persona. It applies and maintains the
workflow-component standard, conducts requalification, and prepares migration
and deprecation designs.

### 2.3 TASK

TASK is the canonical Type 2 shell. It owns:

- input normalization;
- ScopePath and AllowedWriteTargets enforcement;
- active-checkout containment;
- skill hydration and tool-policy resolution;
- run-record behavior;
- generic failure and epistemic controls; and
- structured return to the dispatcher.

TASK does not own method-specific domain logic. That logic belongs in skills.

### 2.4 Skills

Skills are reusable reasoning methods. Each live skill supplies `SKILL.md`,
`BRIEF_SCHEMA.md`, `TOOL_POLICY.md`, and `QA_CHECKS.md`. A dispatcher provides
run parameters but does not reconstruct the method in an ad hoc prompt.

### 2.5 Tools

Tools provide deterministic scaffolding, parsing, validation, graph analysis,
transformation, rendering, and reporting. They have explicit scope and failure
contracts and do not invoke LLM reasoning as an implementation shortcut.

### 2.6 Briefs

Briefs carry run-specific purpose, scope, constraints, permissions, overrides,
outputs, and acceptance checks. They may narrow a skill or shell contract but
cannot relax governance or shell authorization.

### 2.7 Workflow packages

Multi-step workflows combine persona gates, TASK skills, tools, accepted
snapshots, derivative packages, and handoff records. A workflow package is a
composition; it is not a new authority class.

---

## 3. The agent qualification boundary

An agent is warranted only for a distinct governed actor surface. The
qualification signals are:

- human interaction or gate lifecycle;
- decision-right or escalation contract;
- shell-level context, invocation, or authorization semantics;
- durable workflow-state or handoff ownership; or
- a write-scope posture not safely expressible through TASK.

The following are not sufficient:

- a different subject matter;
- a different output schema;
- a particular sequence of tools;
- a dedicated snapshot folder;
- historical use as an agent; or
- a desire for a memorable role name.

No Type 2 agent is grandfathered. Other than TASK, each must demonstrate
shell-level semantics that cannot move to a skill or tool. The transition is
tracked in `docs/AGENT_DISPOSITION_MATRIX.md`.

---

## 4. Contract framework

### 4.1 K-* invariants

`CONTRACT.md` is the authoritative invariant catalog. Workflow-component
design most directly depends on:

- K-AUTH-1/2 and K-BIND-1 — human rulings and SHA binding;
- K-SEAL-1 and K-GHOST-1 — sealed bounded context;
- K-PROV-1, K-INVENT-1, K-CONFLICT-1, K-CLAIM-1 — epistemic integrity;
- K-WRITE-1/2 and K-SNAP-1 — scope, containment, and snapshots;
- K-AGENTS-1 — live governance surface and registry precedence; and
- K-DOMAIN-1..4 — domain-engine authority and protected operations.

### 4.2 R1–R17

`WORKFLOW_COMPONENT_STANDARD.md` owns workflow-component compliance
requirements. R1–R12 retain their stable identifiers; R13–R17 add claim
calibration, integration governance, registry lifecycle, path containment,
and proportional design coverage.

### 4.3 I1–I10

`AGENT_DECOMP_BASE.md` owns the decomposition invariants. They apply to
conforming decomposition workflows and do not turn every decomposition method
into a separate agent automatically.

### 4.4 Instruction-file structure

`SPEC.md` and the workflow-component standard require the canonical header,
Agent Type table, and delimited PROTOCOL/SPEC/STRUCTURE/RATIONALE sections.
These sections make contracts machine-locatable; they do not justify copying
the complete root canon into every file.

---

## 5. Runtime authority and Git semantics

### 5.1 Semantic gates

Human gates are used where a consequential semantic decision exists. A Type 1
persona must not insert approval questions merely to make a workflow appear
controlled; conversely, it must not automate a decision reserved to a human.

### 5.2 Straight-through execution

TASK runs are bounded and non-interactive. Missing required inputs fail
explicitly. Missing evidence becomes a gap or TBD and may allow conservative
continuation only where the method contract permits.

### 5.3 Routine closeout

Scoped commit/push may be operationally autonomous after explicit task or
accepted-handoff authorization, clean scope separation, and recorded
validation. Merge, rebase, destructive cleanup, history rewriting, ambiguous
staging, and baseline integration remain human-gated.

The vocabulary is deliberate:

- `committed` and `pushed` describe Git facts;
- `accepted`, `issued`, `authenticated`, `ruled`, and `approved` describe
  human acts evidenced by governed records.

---

## 6. Write and artifact architecture

### 6.1 Write boundaries

Agent headers declare broad write posture. TASK briefs declare effective
targets. The narrowest applicable boundary controls, and every write remains
subject to active-checkout containment.

### 6.2 Artifact classes

Workflows distinguish authoritative truth, candidates, derivative packages,
factual evidence, generated views, and convenience state. This prevents
reports and regenerated packages from becoming accidental shadow authority.

### 6.3 Snapshots

Snapshots terminate phase-boundary decisions, preserve accepted inputs, or
make audit/derivative outputs reproducible. They are not required for every
ordinary edit. A workflow must state mutability and authority rather than
relying on a filename convention alone.

### 6.4 Pointers

Pointers are mutable navigation aids. Their currency can be checked
mechanically, but a current pointer does not prove acceptance or closure.

---

## 7. Multi-phase governance

The six integration rules in `AGENTS.md` are architectural, not optional
workflow embellishments:

1. derivative packages cite accepted upstream truth;
2. governed phase boundaries terminate in immutable snapshots;
3. paused workflows emit explicit handoff state;
4. closure includes truth acceptance, derivative disposition, audit status,
   and blockers;
5. downstream phases consume current accepted inputs; and
6. cycles are resolved by recorded structural moves, not silent ordering.

The handoff state is the durable seam between agents, sessions, branches, and
worktrees. Chat history is not a substitute.

---

## 8. Live topology and transition posture

At D-GOV-10 framing, the live suite contains 38 agent instruction files:

- 2 previously classified Type 0;
- 21 previously classified Type 1; and
- 15 Type 2, including TASK.

The initial migration audit identified the 14 non-TASK Type 2 agents as
mandatory requalification candidates. This is not a predetermined retirement
verdict: each disposition must cite its actual contract and callers.

Type 1 workflow personas are audited after the Type 2 wave. Some may remain
because they own real iterative human gates; others may slim, merge into a
broader persona, or become workflow packages over TASK skills and tools.

No migration changes the active reconciliation worktrees. This redesign is
developed in an isolated lane and integrated only after rebase, conflict
review, validation, and owner acceptance.

---

## 9. Lifecycle and migration

### 9.1 Component lifecycle

Components are CANDIDATE, ACTIVE, DEPRECATED, or RETIRED. Historical files do
not remain active merely because references to them survive in narrative.

### 9.2 Disposition vocabulary

The suite audit uses:

- `RETAIN` — role and contract remain justified;
- `SLIM` — agent remains, method detail moves down;
- `MERGE` — authority/interaction surface joins another persona;
- `CONVERT_TO_SKILL` — bounded reasoning moves under TASK;
- `CONVERT_TO_TOOL` — deterministic behavior moves to tools; and
- `RETIRE` — live discovery ends after compatibility closure.

### 9.3 Migration package

A valid migration identifies:

- current callers and outputs;
- replacement dispatcher, skill, and/or tool;
- write and artifact-authority equivalence;
- compatibility window and removal condition;
- registry and narrative updates;
- validation evidence; and
- handoff/closure status.

Deleting an instruction file is the final mechanical step, not the migration.

---

## 10. Audit and enforcement

### 10.1 Deterministic checks

Mechanically observable requirements should be validated: header fields,
section markers, type/class compatibility, registry membership, referenced
component existence, R-ID validity, and lifecycle metadata.

### 10.2 Semantic audit

Semantic reviewers assess whether an agent genuinely owns distinct authority
or shell semantics, whether claim language overstates evidence, and whether a
migration preserves human decision rights and closure behavior.

### 10.3 Audit authority

An audit finding is evidence and judgment within its declared boundary. It is
not an amendment. HELPS_HUMANS may propose a standards change; the owner rules
on consequential governance changes.

---

## 11. Current open implementation work

The D-GOV-10 implementation is complete only when:

- the new standard and HELPS_HUMANS split are accepted;
- direct references to the former embedded standard are migrated;
- the agent-audit rubric uses the new governing basis;
- deterministic agent conformance validation exists;
- every live agent has a disposition with evidence;
- migration waves are separately reviewed and validated; and
- the branch is rebased over stable reconciliation handoffs before
  integration.
