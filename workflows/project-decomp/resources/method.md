# project-decomp — method

## Method

### Operational — "How to do?"

This section defines the conversational procedure for project decomposition.

### Output Target
The agent maintains a **canonical working package** during the conversation (a living draft consisting of the main decomposition document and any companion registers), and repeatedly revises it after user feedback until it passes the validation gates in SPEC.

### Phases

#### Phase 1 — Intake (capture the messy reality)

**Goal:** Receive whatever the user provides and reflect it back faithfully.

**Actions:**
- Collect all input material: notes, requirements docs, constraints, objectives (if provided), prior decompositions (if any).
- Ask clarifying questions only when required to prevent structural ambiguity (scope boundaries, stakeholders, contract mode, major systems).
- Begin a **References** list (what inputs were used).

**Output (in draft):**
- Project title (TBD if unknown)
- Intake summary (high-level)
- References list (with whatever anchors are available)

**Gate 1 (confirm intake understanding):**
User confirms: “Yes, that is the project / context as I mean it.”

---

#### Phase 2 — Define Scope (SSOW + vocabulary)

**Goal:** Convert messy SOW into a normalized SSOW that can be partitioned without losing meaning.

**Actions:**
- Normalize scope into atomic **Scope Items** (short, testable statements).
- Identify boundaries explicitly:
  - what is in-scope
  - what is out-of-scope
  - what is uncertain (TBD)
- Start a **Vocabulary Map**:
  - canonical terms (preferred)
  - synonyms / alternate labels observed in user inputs
  - notes (why canonical)

**Output (in draft):**
- SSOW list (atomic scope items)
- Initial objective candidates (derived, not invented)
- Vocabulary Map (initial)

**Gate 2 (confirm SSOW):**
User confirms: “Yes, that SSOW reflects the scope (including in/out/TBD), and the vocabulary choices are acceptable.”

---

#### Phase 3 — Define Objectives (derived from SSOW)

**Goal:** Produce a set of high-level success criteria derived from the SSOW.

**Actions:**
- Derive objectives from scope intent and success conditions embedded in SSOW.
- Ensure objectives are:
  - few enough to be meaningful
  - specific enough to be testable as success criteria
- Map objectives to SSOW scope items (best-effort).

**Output (in draft):**
- Objective list with stable `OBJ-###` IDs
- Best-effort mapping notes (including unmapped objectives, if any)

**Gate 3 (confirm objectives):**
User confirms: “Yes, those objectives represent success as intended.”

---

#### Phase 4 — Define Packages (flat partition)

**Goal:** Partition SSOW scope items into flat Packages with no overlap and no gaps.

**Actions:**
- Propose packages (flat list) with:
  - Package ID `PKG-XXX` (stable)
  - name and scope description
  - discipline assignment for design packages (exactly one discipline)
  - inclusion criteria
- Assign each Scope Item to exactly one Package.
- If a proposed design package spans multiple disciplines, split it into separate discipline-specific packages before Gate 4.
- If an item appears to belong to multiple packages, keep it atomic and force a user decision (or split into smaller scope items, user-confirmed).

**Output (in draft):**
- Package list
- Package scopes
- ScopeItem→Package assignment (in the Scope Ledger)

**Gate 4 (confirm packages):**
User confirms: “Yes, packages are correct, and each scope item belongs to exactly one package.”

---

#### Phase 5 — Define Deliverables (within each package)

**Goal:** Define deliverables that operationalize scope into units of production.

**Actions:**
- `DEL-XXX-YY_{shortDescription}` ID (stable, hyphenated package/deliverable pair (mechanically coupled to `ParentPackageID`) plus descriptive suffix)
- name
- description
- responsible party (TBD allowed)
- deliverable type (e.g., Datasheet/Spec/Guidance/Procedure bundle; or engineering artifact type)
- For design packages, define deliverables by distinct knowledge-artifact kinds; do not create one deliverable per individual artifact instance.
- anticipated artifacts (one or many; same type as deliverable)
- best-effort objective linkage (`SupportsObjectives`)
- best-effort scope-item linkage (`CoversScopeItems`)

**Output (in draft):**
- Deliverable list grouped by Package
- Deliverable attribute tables
- ScopeItem→Deliverable mapping in the Scope Ledger (best-effort; gaps surfaced)

**Gate 5 (confirm deliverables):**
User confirms: “Yes, deliverables and responsibilities/types are acceptable.”

---

#### Phase 6 — Verify Coverage (anti-fragile checks)

**Goal:** Prove that decomposition covers scope and make gaps visible and trackable.

**Actions:**
- Verify every Scope Item is:
  - assigned to exactly one Package (required)
  - mapped to at least one Deliverable (best-effort; missing mappings are open issues)
- Verify each Deliverable belongs to exactly one Package (required).
- Verify objective mapping is best-effort complete:
  - each objective is supported by at least one deliverable, or is flagged as open issue.
- Produce **Coverage & Telemetry** summary (required).

**Output (in draft):**
- Coverage & Telemetry section with counts and open issues
- Open Issues list referencing stable IDs (ScopeItemID, OBJ-ID, etc.)

**Gate 6 (confirm verification):**
User confirms: “Coverage and mappings are acceptable; open issues list is correct.”

---

#### Phase 7 — Publish the Decomposition (finalize)

**Goal:** Produce the final decomposition document as a single coherent artifact suitable for downstream agents.

**Actions:**
- Ensure the document includes:
  - Scope Ledger (required)
  - Coverage & Telemetry (required)
  - Vocabulary Map (required)
  - Packages, Deliverables, Artifacts, Objectives
  - Decision log / change log (required)
- Summarize what changed since last revision.

**Gate 7 (final acceptance):**
User confirms: “This decomposition is the accepted basis for downstream work.”

---
