# software-decomp — method

## Method

### Operational — \"How to do?\"

This section defines the gate-controlled conversational procedure for software development decomposition.

### Output Target

The agent maintains a **canonical working package** (living draft consisting of the main decomposition document and any companion registers) and revises it after human feedback until it passes the gates in SPEC.

### Phases

#### Phase 1 — Intake (capture the messy reality)

**Goal:** Receive software scope inputs and reflect them back faithfully.

**Actions:**
- Collect all input material (requirements docs, tickets, notes, architecture, constraints, non-functional requirements, target platforms, rollout expectations).
- Identify hard constraints early (security/compliance, performance/SLOs, data residency, backwards compatibility, deadlines, approved libraries).
- Begin a **References** list (what inputs were used).

**Output (draft):**
- Project title (TBD if unknown)
- Intake summary (high-level)
- References list

**Gate 1 (confirm intake understanding):**
Human confirms: “Yes, that is the project/context as intended.”

---

#### Phase 2 — Define Scope (SSOW + vocabulary + domain signals)

**Goal:** Convert messy software scope into atomic scope items that can be partitioned by work domain.

**Actions:**
- Normalize scope into atomic **Scope Items** (short, testable statements).
- Classify each scope item as `IN | OUT | TBD`.
- Identify **domain signals** for later partitioning (without planning implementation):
  - user experience vs. backend behavior vs. data model vs. infra vs. tests vs. docs
  - runtime surfaces (frontend/backend/mobile/CLI), persistence surfaces (DB/queue/cache), platform surfaces (CI/CD/deploy/observability)
- Start a **Vocabulary Map**:
  - canonical terms (preferred)
  - synonyms observed in input
  - notes

**Output (draft):**
- SSOW list (atomic scope items)
- Vocabulary Map (initial)
- Initial objective candidates (derived, not invented)

**Gate 2 (confirm SSOW):**
Human confirms: “Yes, that SSOW reflects the scope (in/out/TBD) and the vocabulary choices are acceptable.”

---

#### Phase 3 — Define Objectives (derived from SSOW)

**Goal:** Produce high-level success criteria derived from the SSOW.

**Actions:**
- Derive objectives from SSOW intent and explicit success conditions (e.g., acceptance criteria, KPIs, SLOs).
- Ensure objectives are few, meaningful, and testable.
- Map objectives to SSOW scope items (best-effort).

**Output (draft):**
- Objective list with stable `OBJ-NNN` IDs
- Mapping notes (including unmapped objectives)

**Gate 3 (confirm objectives):**
Human confirms: “Yes, those objectives represent success as intended.”

---

#### Phase 4 — Define Packages (flat partition by work domain)

**Goal:** Partition SSOW scope items into flat Packages by **category/domain of work**, optimizing for small-context execution later.

**Actions:**
- Propose packages as **work domains**, not phases. A package is a “cohesive context set”.
- Package choices MUST be supported by SSOW domain signals. (Do not invent packages “because software usually has them.”)
- Assign each Scope Item to exactly one Package.
- If a scope item appears to belong to multiple packages, either:
  1) split it into smaller scope items (preferred), then reassign, or
  2) surface ambiguity and force a human decision.

**Output (draft):**
- Package list (IDs, names, scope descriptions, inclusion/exclusion criteria)
- ScopeItem → Package assignment (in the Scope Ledger)

**Gate 4 (confirm packages):**
Human confirms: “Yes, packages are correct, and each scope item belongs to exactly one package.”

---

#### Phase 5 — Define Deliverables (agent-executable units within each package)

**Goal:** Define deliverables that are small enough for specialist execution and that produce concrete software artifacts.

**Core rule (software):** because deliverables have no internal task sub-level, deliverables MUST be “agent-executable” within a bounded context window.

**Actions:**
- Define deliverables within each Package with:
  - `DEL-XX-YY` ID (stable; coupled to parent `PKG-XX`)
  - name, description, responsible party (`TBD` allowed)
  - deliverable type (software-oriented)
  - anticipated artifacts (one or more)
  - best-effort objective linkage and scope-item linkage
  - **Context Envelope** (`S | M | L | XL`) with justification
- Enforce deliverable sizing:
  - Each deliverable MUST be single-domain (belongs to exactly one package).
  - Each deliverable SHOULD focus on a single primary “artifact shape” (e.g., one endpoint + tests; one UI view + tests; one migration + rollback plan).
  - If a deliverable touches multiple runtime surfaces (e.g., frontend + backend + infra), it is likely `XL` and MUST be split unless the human explicitly accepts the risk as an open issue.

**Output (draft):**
- Deliverable list grouped by Package (tables)
- ScopeItem → Deliverable mapping in the Scope Ledger (best-effort; gaps surfaced)

**Gate 5 (confirm deliverables):**
Human confirms: “Yes, deliverables (granularity, responsibilities, types, envelopes) are acceptable.”

---

#### Phase 6 — Verify Coverage + Context Budget (anti-fragile checks)

**Goal:** Prove scope coverage and ensure deliverables are executable in bounded context.

**Actions:**
- Verify every scope item is assigned to exactly one package.
- Verify every deliverable belongs to exactly one package.
- Verify best-effort mappings:
  - each scope item maps to ≥1 deliverable, or is flagged as open issue
  - each objective is supported by ≥1 deliverable, or is flagged
- Run **Context Budget QA**:
  - count deliverables by `ContextEnvelope`
  - any `XL` deliverable must be either split OR explicitly listed as an accepted open issue (with why it cannot be split)
- Produce **Coverage & Telemetry** summary.

**Output (draft):**
- Coverage & Telemetry
- Open Issues list referencing stable IDs
- Context Budget QA summary

**Gate 6 (confirm verification):**
Human confirms: “Coverage, mappings, and context-budget posture are acceptable; open issues list is correct.”

---

#### Phase 7 — Publish the Decomposition (finalize)

**Goal:** Produce the final decomposition document as a single coherent artifact suitable for downstream work.

**Actions:**
- Ensure the document includes:
  - Scope Ledger (required)
  - Coverage & Telemetry (required)
  - Vocabulary Map (required)
  - Packages, Deliverables, Artifacts, Objectives
  - Context Budget QA section
  - Decision log / change log
- Summarize what changed since last revision.

**Gate 7 (final acceptance):**
Human confirms: “This decomposition is the accepted basis for downstream work.”
