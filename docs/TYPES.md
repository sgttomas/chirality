# TYPES — Domain Vocabulary and Hierarchy

> **Status: DRAFT pending human ratification.** This document re-establishes the monorepo-root governance layer (root `docs/` was hollowed out during the four-repo merge; see `plans/monorepo_root_governance_and_path_anchoring_2026-06-15.md`). It is authored from the prior root canon (`.archive/TYPES.md`), preserving the established §1–§10 numbering (referenced as `TYPES §4` and `§9.2` from `AGENTS.md`), and adds the root/path-token vocabulary (§1.4–§1.5), the reconciled `WRITE_SCOPE` enum (§4.2), and the domain-decomposition entities (§8.2). Not accepted governance until a human ratifies it (per `CONTRACT.md` / K-AUTH-1).

This document is the authoritative vocabulary reference for the Chirality agent operating system. It defines the canonical entities, stable identifier formats, enumerated types, agent roles, and lifecycle states.

All agents and governance documents use the terms defined here. Where a term is used differently elsewhere, this document governs.

---

## 1. Project Hierarchy

The project hierarchy is flat: **packages contain deliverables**. There are no phases, sub-packages, or task sub-levels within deliverables.

```
{EXECUTION_ROOT}/
└── PKG-XX_{PkgLabel}/          # Package (flat partition of scope)
    └── 1_Working/
        └── DEL-XX-YY_{DelLabel}/   # Deliverable (unit of production)
```

### 1.1 Package

A **package** is a flat partition of project scope. Packages do not nest.

- Every scope item belongs to exactly one package (no overlaps, no gaps).
- Packages are defined by PROJECT_DECOMP and confirmed by the human.

### 1.2 Deliverable

A **deliverable** is a unit of production within a package. Each deliverable:

- Belongs to exactly one package.
- Has a responsible party.
- Has a type (e.g., compliance document, design package, methodology narrative).
- Produces one or more anticipated artifacts.
- Occupies one folder under `{PKG}/1_Working/`.

### 1.3 Artifact

An **artifact** is a tangible output produced within a deliverable folder. Artifacts include the document kit (Datasheet, Specification, Guidance, Procedure) and any additional outputs appropriate to the deliverable type.

### 1.4 Roots and Working Surfaces

The path model is specified in `SPEC.md` §0.2. The entities it defines:

| Entity | Definition |
|---|---|
| **Repo Root** (`REPO_ROOT`) | The root of the active git checkout, resolved as `git rev-parse --show-toplevel`. Home of the shared instruction surface. In a git worktree it is the worktree's own root. |
| **Instruction Root** | The shared, release-managed agent operating system — `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`. `= REPO_ROOT` in this monorepo; the app bundle in desktop builds (see `DIRECTIVE.md` §2.6). |
| **Working Root** (`WORKING_ROOT`) | The active project or domain workspace — `projects/<name>/` or `domains/<name>/`, or a user-selected folder under the desktop harness. Where governed project truth lives. One instruction root serves many working roots. |
| **Execution Root** (`EXECUTION_ROOT`) | The execution-instance root within a working root; contains packages and tool roots. |
| **Tool Root** | A workspace-level directory for derived outputs under `{EXECUTION_ROOT}` (e.g. `_Decomposition/`, `_Reconciliation/`), isolated from source truth. The registry is `SPEC.md` §1.2. |

### 1.5 Path Tokens

Agent instructions and skills reference roots through `{*_ROOT}` tokens, each resolving against exactly one anchor. The authoritative registry — token → anchor → resolution — is `SPEC.md` §0.3. Key tokens: `{REPO_ROOT}`, `{INSTRUCTION_ROOT}`, `{WORKING_ROOT}`, `{EXECUTION_ROOT}`, `{COORDINATION_ROOT}`, `{DECOMP_ROOT}`, and the tool-root tokens (`{AGGREGATION_ROOT}`, `{RECONCILIATION_ROOT}`, `{ESTIMATES_ROOT}`, …). Instruction-surface tokens resolve `REPO_ROOT`-relative; workspace tokens resolve `WORKING_ROOT`-relative. Machine-absolute paths MUST NOT appear in instruction, coordination, or plan files (`SPEC.md` §0.2.4).

---

## 2. Stable Identifiers

Identifiers are assigned once and persist across renames, path changes, and restructuring. Path is a physical projection of the decomposition, not identity itself (`CONTRACT.md` K-ID-1).

| Entity | Format | Example | Assigned By |
|---|---|---|---|
| Package | `PKG-XX` | `PKG-01` | PROJECT_DECOMP |
| Deliverable | `DEL-XX-YY` | `DEL-01-01` | PROJECT_DECOMP |
| Dependency | `DEP-XX-YY-NNN` | `DEP-01-01-001` | TASK+dependency-extract |
| Scope Item | `SOW-NNN` | `SOW-003` | PROJECT_DECOMP |
| Objective | `OBJ-NNN` | `OBJ-001` | PROJECT_DECOMP |

Conforming decomposition variants define additional stable-ID families in their own contracts (e.g. domain-knowledge identifiers; see §8.2 and `AGENT_DECOMP_BASE.md`). The ID rules below apply to all families.

### 2.1 ID Rules

- `XX` in package IDs is a zero-padded numeric sequence (e.g., `01`, `02`, ... `09`, `10`).
- `YY` in deliverable IDs is a zero-padded numeric sequence scoped to the package.
- `NNN` in dependency IDs is a zero-padded numeric sequence scoped to the deliverable.
- IDs MUST NOT change across revisions unless the human explicitly requests renumbering.
- Deliverable IDs use hyphen separators (`DEL-01-01`), not dot separators (`DEL-01.01`).

### 2.2 Folder Labels

Folder names combine the stable ID with a human-readable label:

- Package: `{PKG-ID}_{Sanitize(PackageName)}`
- Deliverable: `{DEL-ID}_{Sanitize(DeliverableName)}`

The canonical (unsanitized) name is recorded in `_CONTEXT.md`. Sanitization rules are defined in `SPEC.md` Section 10.

---

## 3. Dependency Vocabulary

Dependencies capture relationships between deliverables, definition nodes, and external entities. The dependency model distinguishes two fundamental classes of edges.

### 3.1 Dependency Classes

| Class | Meaning | Graph Role |
|---|---|---|
| **ANCHOR** | Connects a deliverable to a definition/traceability node (parent WBS, requirement) | Tree edge (vertical) |
| **EXECUTION** | Captures information flow, prerequisites, handoffs, and constraints between work items | DAG edge (horizontal) |

Together, ANCHOR (tree) and EXECUTION (DAG) form a **knowledge graph**: the tree preserves stable intent; the DAG captures execution couplings.

### 3.2 Anchor Types

| Value | Meaning |
|---|---|
| `IMPLEMENTS_NODE` | Parent definition node — exactly one per deliverable |
| `TRACES_TO_REQUIREMENT` | Requirement trace link — zero or more per deliverable |
| `NOT_APPLICABLE` | Used for EXECUTION rows only |

### 3.3 Direction

Direction is always relative to the host deliverable:

| Value | Meaning |
|---|---|
| `UPSTREAM` | This deliverable requires information FROM the target |
| `DOWNSTREAM` | This deliverable produces information FOR the target |

Legacy values `INBOUND` and `OUTBOUND` normalize to `UPSTREAM` and `DOWNSTREAM` respectively.

### 3.4 Dependency Types

| Value | Class | Meaning |
|---|---|---|
| `PREREQUISITE` | Execution | Required input or approval before work can proceed |
| `INTERFACE` | Execution | Explicit data/artifact exchange between deliverables |
| `HANDOVER` | Execution | Output of one deliverable consumed as input to another |
| `CONSTRAINT` | Execution | Explicit constraint or condition |
| `ENABLES` | Execution | This deliverable enables downstream work |
| `OTHER` | Both | Default for ANCHOR rows; catch-all for EXECUTION rows |

Legacy types such as `COORDINATION` / `INFORMATION`, and project-specific labels such as `ARCHITECTURE_BASIS`, `DOMAIN_MODEL`, `*_PREDECESSOR`, or `*_CONTRACT`, are read-only migration inputs. Current v3.1 registers MUST emit only the canonical values above and preserve the legacy label in provenance notes or documented extension fields.

### 3.5 Target Types

| Value | Meaning |
|---|---|
| `DELIVERABLE` | Another deliverable in the project |
| `PACKAGE` | A package |
| `WBS_NODE` | Work breakdown structure or scope node |
| `REQUIREMENT` | A specific requirement (SOW item, objective) |
| `DOCUMENT` | An external or reference document |
| `EQUIPMENT` | Physical equipment or asset |
| `EXTERNAL` | External entity (organization, standard) |
| `UNKNOWN` | Target cannot be confidently resolved |

### 3.6 Provenance and Confidence

| Dimension | Values | Meaning |
|---|---|---|
| `Explicitness` | `EXPLICIT`, `IMPLICIT` | Whether the dependency is directly stated in source text |
| `Confidence` | `HIGH`, `MEDIUM`, `LOW` | Strength of evidence supporting the dependency |
| `Origin` | `DECLARED`, `EXTRACTED` | Human-declared vs. agent-extracted |

### 3.7 Satisfaction and Status

| Dimension | Values | Tracks |
|---|---|---|
| `SatisfactionStatus` | `TBD`, `PENDING`, `IN_PROGRESS`, `SATISFIED`, `WAIVED`, `NOT_APPLICABLE` | Closure lifecycle (has the dependency been fulfilled?) |
| `Status` | `ACTIVE`, `RETIRED` | Extraction lifecycle (is the dependency currently observed in sources?) |

Candidate/non-gating graph dispositions are governance worklist states, not dependency `Status` values. They MUST NOT be represented as `Status=CANDIDATE` in current v3.1 registers.

---

## 4. Agent Roles

Agents are classified into three types following the 0-1-2 model. See `AGENTS.md` for the live agent matrix and index.

### 4.1 Agent Types

| Type | Name | Role | Scope |
|---|---|---|---|
| **Type 0** | Architect | Defines and maintains standards, contracts, and role boundaries | Project-wide |
| **Type 1** | Manager | Interprets intent, decomposes work, routes to specialists, merges results | Package or project scope |
| **Type 2** | Specialist | Executes bounded briefs with minimal context; returns outputs + evidence | Single deliverable or narrow task |

`TASK` is the canonical Type 2 execution shell; it hydrates reusable methods through `TaskSkill: <name>` rather than proliferating bespoke task agents.

### 4.2 Classification Properties

| Property | Values | Meaning |
|---|---|---|
| `AGENT_CLASS` | `PERSONA`, `TASK` | Persona agents run interactive sessions; Task agents run straight-through pipelines |
| `INTERACTION_SURFACE` | `chat`, `INIT-TASK`, `spawned`, `both` | How the agent is invoked |
| `WRITE_SCOPE` | base values: `repo-wide`, `deliverable-local`, `tool-root-only`, `workspace-scaffold-only`, `repo-metadata-only`, `project-level`, `bounded-task-brief`, `none` | What the agent is allowed to write |
| `BLOCKING` | `never`, `allowed` | Whether the agent may pause for human input |

A `tool-root-only` scope MAY be parameterized to a registered tool root or subtree — `tool-root-only ({EXECUTION_ROOT}/_Reconciliation/<subtree>/)`. `bounded-task-brief` is the `TASK` shell's scope: writes are authorized only by the effective bounded task brief and are always subject to ScopePath containment (`SPEC.md` §0.2.3, §9.5). The full enumeration and parameterization rules live in `SPEC.md` §9.5.

### 4.3 Authority Model

- Type 0 proposes rules (what "correct" means).
- Type 1 prepares workspaces and orchestrates (what the specialist can see).
- Type 2 does the work (within bounded scope).
- Human approves at gates.

Authority flows downward; escalation flows upward. A Type 2 agent cannot modify rules set by Type 0. A Type 1 agent cannot approve deliverables for external reliance.

---

## 5. Deliverable Lifecycle States

### 5.1 State Definitions

```
OPEN → INITIALIZED → SEMANTIC_READY → IN_PROGRESS → CHECKING → ISSUED
```

| State | Meaning |
|---|---|
| `OPEN` | Folder exists with minimum viable fileset; no content yet |
| `INITIALIZED` | Document kit (Datasheet, Specification, Guidance, Procedure) has been drafted |
| `SEMANTIC_READY` | Semantic lens (`_SEMANTIC.md`) has been generated |
| `IN_PROGRESS` | Active human + agent work underway |
| `CHECKING` | Under review |
| `ISSUED` | Released for use |

### 5.2 Stage Gates vs. Lifecycle

**Lifecycle states** are tracked in `_STATUS.md` and represent the deliverable's production status.

**Stage gates** (30%, 60%, 90%, IFC, etc.) are human-managed milestones that represent project-level progress checkpoints. Stage gates are NOT lifecycle states and are tracked separately in coordination records.

### 5.3 Semantic Step

The `INITIALIZED → SEMANTIC_READY` transition is optional. If the semantic lensing step is skipped, deliverables may transition directly from `INITIALIZED → IN_PROGRESS`.

---

## 6. Coordination Representations

The framework separates **how teams coordinate** (schedule-first, declared dependencies, or full graph) from **how the system tracks dependencies** (always maintains deliverable-local registers).

| Representation | Meaning |
|---|---|
| `SCHEDULE_FIRST` | Gantt drives sequencing; dependency tracking active for blocker detection and audit |
| `DEPENDENCY_TRACKED` | Dependency graph drives sequencing |
| `HYBRID` | Combination of schedule-first and dependency-tracked |

The coordination representation is recorded in `_COORDINATION.md` and chosen per project instance.

---

## 7. Document Kit Types

Each deliverable contains a standard four-document kit:

| Document | Purpose |
|---|---|
| `Datasheet.md` | Key parameters, identification, structured metadata |
| `Specification.md` | Technical requirements, scope definition, acceptance criteria |
| `Guidance.md` | Design guidance, rationale, best practices, contextual direction |
| `Procedure.md` | Step-by-step execution workflow, sequencing, checklists |

---

## 8. Decomposition Entities

### 8.1 Project Decomposition Entities

The project decomposition document (produced by PROJECT_DECOMP) defines these entities:

| Entity | ID Format | Purpose |
|---|---|---|
| **Scope Item** | `SOW-NNN` | Atomic, testable scope statement from the Structured Scope of Work |
| **Objective** | `OBJ-NNN` | Success criterion derived from scope; mapped to supporting deliverables |
| **Vocabulary Map** | (table) | Canonical terms and synonyms to prevent semantic drift |
| **Scope Ledger** | (table) | Machine-checkable mapping of every scope item to packages and deliverables |
| **Coverage & Telemetry** | (summary) | Metrics (counts, gaps, open issues) that make decomposition quality measurable |

### 8.2 Domain Decomposition Entities

The decomposition protocol is shared across variants by `AGENT_DECOMP_BASE.md`; `DOMAIN_DECOMP` binds its abstract entities to domain-knowledge names. The handbook/domain variant defines:

| Entity | ID Format | Purpose |
|---|---|---|
| **Category** | `CAT-###` | A flat partition of in-scope handbook units (no nesting, no overlaps, no gaps) |
| **Knowledge Type** | `KTY-CC-TT_{shortDesc}` | A reusable kind of knowledge object within a Category (Procedure, Checklist, Template, Guidance, Reference) |
| **Knowledge Subject** | `SUB-CC-TT-SS_{shortDesc}` | A specific domain topic within a Knowledge Type |
| **Handbook Unit (Atom)** | `HBA-<SOURCE_PREFIX>-NNNNN` | An atomic instruction/concept extracted from a source; the unit of coverage checking |
| **Section Node** | `SEC-<SOURCE_PREFIX>-NNNN` | A source section in the reviewed skeleton; the section-level retrieval substrate |

The base specification's abstract entities (Atomic Unit, Partition, Production Unit, Decomposition Ledger, Coverage & Telemetry, Vocabulary Map) and the seven-gate protocol are defined in `AGENT_DECOMP_BASE.md`; PROJECT_DECOMP, SOFTWARE_DECOMP, and DOMAIN_DECOMP bind them to domain-specific names and ID widths.

---

## 9. UI Navigation Vocabulary

The agent matrix and pipeline categories below are framework-level governance grammar (referenced by `AGENTS.md`); the desktop frontend uses them for matrix routing and pipeline selection. Deployment-specific selector and API details are owned by the runtime project's docs.

### 9.1 Matrix Axes

| Type | Values | Meaning |
|---|---|---|
| `MatrixRow` | `NORMATIVE`, `OPERATIVE`, `EVALUATIVE` | Epistemic-posture lane; also routes to WORKBENCH or PIPELINE |
| `MatrixColumn` | `GUIDING`, `APPLYING`, `JUDGING`, `REVIEWING` | Functional-role matrix column shared across all rows |

The matrix is both a routing view and a governance grammar: NORMATIVE defines rules and standards, OPERATIVE executes bounded work within them, and EVALUATIVE audits, reconciles, and judges results (see `AGENTS.md`).

### 9.2 Pipeline Selectors

| Type | Values | Meaning |
|---|---|---|
| `PipelineCategory` | `DECOMP*`, `PREP*`, `TASK*`, `AUDIT*` (and other live task families) | Top-level pipeline grouping; wildcard cells in the agent matrix expand to agent groups by this category |
| `TaskScopeMode` | `DELIVERABLES`, `KNOWLEDGE_TYPES` | Dynamic scope mode used when the category is `TASK*` |

### 9.3 Knowledge Decomposition Terms

| Term | Meaning |
|---|---|
| **Knowledge decomposition marker** | A decomposition-document signal (headings/phrases such as `Knowledge Categories`, `Knowledge Types`, or equivalent) that enables knowledge-type scope in TASK selectors. |
| **Knowledge type option** | A canonical file-type bucket (Datasheet, Specification, Guidance, Procedure, Dependencies, References, Context, Status, Semantic, Memory) selectable in TASK scope mode. |

---

## 10. Epistemic Ontology

The epistemology pillar (see `DIRECTIVE.md` §2) operates on a set of formally defined entities. These entities constitute the ontology of the epistemic layer — the things that the epistemic mechanisms (mandatory provenance, no invention, conflict surfacing, epistemic labeling) act upon.

### 10.1 Epistemic Primitives

| Primitive | Definition | Canonical Location |
|---|---|---|
| **Claim** | An assertion that something is the case. The atomic unit of the epistemology. Every non-trivial assertion produced by an agent in a governed workflow is a claim. | Dependency rows, document content, agent outputs |
| **Warrant** | The justification for believing a claim. Always extrinsic — a source citation (file + section + quote) — never intrinsic (model confidence or plausibility). | `EvidenceFile`, `SourceRef`, `EvidenceQuote` columns in `Dependencies.csv` (`SPEC.md` §6.5) |
| **Status** | The epistemic classification of a claim's certainty, expressed as one of four labels. | `Notes` fields, dependency records, agent output prose |
| **Gap** | The explicit, positive assertion that a warrant has not been found. A gap is not the absence of information — it is an entity representing that absence, making it visible and actionable. | `TBD` markers, `location TBD` in provenance fields, open issues |
| **Conflict** | Two or more claims with incompatible warrants about the same key. The existence of a conflict is itself an epistemic entity that must be resolved before the deliverable can advance. | Conflict Tables (`ConflictID`, `Key`, `Contenders`, `ProposedAuthority`, `HumanRuling`) |
| **Ruling** | A human decision that resolves a gap or conflict, transforming epistemic status. Rulings are binding and recorded in versioned files. | `HumanRuling` column in Conflict Tables, finding dispositions in REVIEW, gate decisions |

### 10.2 Epistemic Relationships

| Relationship | Description |
|---|---|
| A claim HAS a status | Exactly one of FACT, ASSUMPTION, PROPOSAL, or TBD |
| A claim MAY HAVE a warrant | Source file + section reference + optional quote; absence is structurally visible |
| A claim WITHOUT a warrant | Is a gap; status is TBD or uncited PROPOSAL; the absence of warrant is itself a finding |
| Two claims may be IN CONFLICT | Same key, incompatible values, different sources |
| A conflict REQUIRES a ruling | HumanRuling = TBD until the licensed professional adjudicates |
| A ruling TRANSFORMS status | Resolves gaps (TBD → FACT or ASSUMPTION), accepts or rejects proposals, and resolves conflicts (competing claims → one accepted) |

### 10.3 Epistemic Labels

The four epistemic labels classify the certainty status of claims:

| Label | Meaning | Reviewer Action |
|---|---|---|
| `FACT` | Directly observed in source text with citation | Verify citation; accept if source is authoritative |
| `ASSUMPTION` | Reasonable inference grounded in cited material; not directly stated and still requiring validation | Validate or reject; document decision |
| `PROPOSAL` | Suggested interpretation, action, or design move; may cite supporting context, but requires human decision to become binding | Decide; record rationale |
| `TBD` | Unknown; placeholder requiring resolution | Resolve before reliance |

### 10.4 Warrant Lifecycle

Claims within a deliverable progress through a warrant lifecycle that tracks their epistemic state, interleaved with the deliverable lifecycle (`§5`) that tracks production state:

```
UNWARRANTED → CITED → REVIEWED → AUTHENTICATED
```

| Warrant State | Meaning | Transition Mechanism |
|---|---|---|
| `UNWARRANTED` | Claim exists but has no source citation; status is TBD or uncited PROPOSAL | Agent produces claim; K-INVENT-1 requires TBD marking for gaps |
| `CITED` | Claim has a source citation; status is FACT, ASSUMPTION, or cited PROPOSAL | Agent attaches provenance; K-PROV-1 enforces |
| `REVIEWED` | Claim has been examined by a licensed professional; findings dispositioned | REVIEW gates; human rules on findings |
| `AUTHENTICATED` | Claim is part of an authenticated PWP; the professional warrants it under duty of care | Authentication binds to git SHA; K-AUTH-2 enforces |

The deliverable lifecycle asks: *what state is this work product in?* The warrant lifecycle asks: *what state is our knowledge about this work product in?* A deliverable is ready for issuance when its warrants are sufficient — when the licensed professional has determined that the epistemic state of the claims supports authentication under professional responsibility.

The two lifecycles are correlated but not identical. A deliverable in `IN_PROGRESS` contains a mixture of warranted and unwarranted claims. The transition to `CHECKING` requires that critical claims have been warranted (all CRITICAL findings must have non-TBD human disposition). The transition to `ISSUED` requires that the professional has authenticated the work — the act of warranting the deliverable's claims under professional responsibility.

### 10.5 Enforcing Invariants

| Invariant | Epistemic Primitive Governed |
|---|---|
| K-PROV-1 (mandatory provenance) | Warrant — every claim must have an extrinsic warrant or explicit `location TBD` |
| K-INVENT-1 (no invention) | Gap — missing data must be represented as a gap (TBD), not filled with a fabrication |
| K-CONFLICT-1 (conflict surfacing) | Conflict — disagreements must be exposed as conflicts, not silently resolved |
| K-AUTH-1 (human authority) | Ruling — only humans may author binding rulings and approval records |
| K-AUTH-2 (SHA-bound approval) | Authentication — the warrant-to-content binding is mechanically verifiable |
