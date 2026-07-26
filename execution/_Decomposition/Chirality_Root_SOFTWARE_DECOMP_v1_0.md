# Chirality Root — Software Decomposition (CANDIDATE v1.0)

**Package Role:** `working surface`
**Agent Role:** `SOFTWARE_DECOMP` (Agent 1), under a sealed brief from Agent 0
**Method basis:** `docs/DECOMPOSITION_STANDARD.md` (RATIFIED) extended by `agents/AGENT_SOFTWARE_DECOMP.md`
**Revision:** v1.0 · **Date:** 2026-07-25
**Basis commit:** `24726a73c64a849909e3615c32ef1a888b3dfd36`
**Run:** `ROOT-STEP8-DECOMP-20260725`, node N1

> **Status: CANDIDATE — NOT ACCEPTED.** Every one of the seven gates is
> human-gated (I1) and **none is ruled in this run**. Every Gate Log row reads
> `PENDING_OWNER_RULING`. This document, its companion registers, and every
> count in them are **offered to the owner's ruling**, not asserted as an
> accepted basis for downstream work. No package or deliverable directory is
> created by this candidate, and none may be created from it until Gate 7 is
> ruled and the D-GOV-21 §5.3 materialization gate is separately satisfied.
> Authorship by an agent confers no authority (K-AUTH-1); existence,
> validation, and commit are not approval.

---

## 1. Gate Log

| Gate | Name | Status | Staged evidence offered to the ruling |
|---|---|---|---|
| Gate 1 | Intake understanding | `PENDING_OWNER_RULING` | §4 Intake Summary and §2 References; the sole scope source is pinned by path, sha256, and basis commit. |
| Gate 2 | SSOW and vocabulary | `PENDING_OWNER_RULING` | 103 atomic scope items with `IN\|OUT\|TBD` status in `chirality_root_scope_ledger_v1_0.csv`; §5 Vocabulary Map. |
| Gate 3 | Objectives | `PENDING_OWNER_RULING` | §7 Objectives: OBJ-001..OBJ-007 derived one-to-one from PRD OBJ-1..OBJ-7; `chirality_root_objective_register_v1_0.csv`. |
| Gate 4 | Packages | `PENDING_OWNER_RULING` | §8 Packages: six flat work-domain packages; every IN-scope item assigned to exactly one. |
| Gate 5 | Deliverables | `PENDING_OWNER_RULING` | §9 Deliverables: 45 deliverables, each single-package, context-sized, with anticipated artifacts and write locus. |
| Gate 6 | Coverage and context budget | `PENDING_OWNER_RULING` | §11 and `chirality_root_coverage_telemetry_v1_0.md`: `UnassignedScopeItems` 0, `UnmappedObjectives` 0, no XL deliverable, F4 both directions closed. |
| Gate 7 | Publish / final acceptance | `PENDING_OWNER_RULING` | This working surface plus six companion registers. **The acceptance phrase — that this decomposition is the accepted basis for downstream work — has not been said by anyone and is not claimed here.** |

**Acceptance vehicle.** The vehicle is the owner's to choose. The run was
staged for a ruling over the exact candidate commit (the pattern of
`docs/PRD_ROOT.md`'s own adoption), with gate-by-gate review available as an
alternative. This document takes no position on which is used and records
neither as having occurred.

---

## 2. References

### 2.1 Scope source (the only one)

| RefID | Source | Role | sha256 | Basis |
|---|---|---|---|---|
| REF-001 | `docs/PRD_ROOT.md` | **Sole scope source.** Objectives (§3), categories (§4), stable commitments (§5), self-application direction (§6), variant and promotion direction (§7), non-goals and falsifiers (§8), ruled owner decisions (§9), source-concordance obligations (§10). | `e98031c14b4c6c9b2602545e6f80abd5019ead0af1ff460b3e4ea26135bb63eb` | `24726a73c64a849909e3615c32ef1a888b3dfd36` |

Nothing outside REF-001 created scope. Where REF-001 is silent or ambiguous,
this decomposition records `TBD` and an open issue rather than inventing (I2,
K-INVENT-1).

### 2.2 Method sources (binding on how, not on what)

| RefID | Source | Role | sha256 |
|---|---|---|---|
| REF-002 | `docs/DECOMPOSITION_STANDARD.md` | Ratified 7-gate protocol, I1–I10 invariants, package architecture, required sections | `9e356ea11d4ab09264b3526e368b7acdb59fd0accaa70a21808da796b5252cea` |
| REF-003 | `agents/AGENT_SOFTWARE_DECOMP.md` | Conforming manager: entity bindings, ID formats, deliverable type taxonomy, Context Envelope discipline | `ad849d9a927485d8749713070579cf072663a2efab63abef2b7db16efeb43409` |
| REF-004 | `docs/SPEC.md` §1, §10 | Canonical identifier formats and filesystem-safe label rules used for `PKG-XX_{PkgLabel}` / `DEL-XX-YY_{DelLabel}` | `aa43e93235867f5b11c6aab3c27baffc7a3b2a028e4599c22e0ff0dcd0621f64` |

### 2.3 Interpretive context — **non-source, generates no scope**

The PRD incorporates these by reference. They were read only to understand
what a PRD commitment requires. **No scope item derives from them**, and where
one of them says something the PRD does not, that thing is absent from this
decomposition by design:

`AGENTS.md`; `docs/DIRECTIVE.md`; `docs/CONTRACT.md`; `docs/TYPES.md`;
`docs/governance_harness/_DECISIONS/D-GOV-21_root_working_root_exception.md`
§5; the live registries the PRD cites (`skills/README.md`,
`tools/REGISTRY.md`, the export profile).

### 2.4 Structural precedent — **non-source**

`projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
was read for section structure and register conventions only. None of its
content was carried over.

---

## 3. Companion inventory and authoritative surfaces

This decomposition is a **canonical working package**, not a monolithic
document. Heavy machine truth lives in companion registers, which are
authoritative for their data.

| File | Package role | Authoritative for |
|---|---|---|
| `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` (this file) | `working surface` | Gates, references, partition, deliverable topology, decisions, open issues |
| `chirality_root_scope_ledger_v1_0.csv` | `authoritative companion register` | The scope ledger — one row per scope item |
| `chirality_root_deliverable_register_v1_0.csv` | `authoritative companion register` | Full deliverable fields (description, artifacts, covered scope items, envelope notes, write locus) |
| `chirality_root_objective_register_v1_0.csv` | `authoritative companion register` | Objectives and their mappings |
| `chirality_root_prd_coverage_forward_v1_0.csv` | `authoritative companion register` | **F4 forward** — every PRD item's coverage or deferral |
| `chirality_root_trace_reverse_v1_0.csv` | `authoritative companion register` | **F4 reverse** — every package and deliverable's PRD trace |
| `chirality_root_coverage_telemetry_v1_0.md` | `authoritative companion register` | Counts, context budget QA, D-15 demonstration, F4 result, open-issue taxonomy |

**No derived publication artifact is produced by this run.** If one is later
assembled it must be labelled `derived publication artifact` and must not
become the amendment surface.

---

## 4. Intake Summary

The product decomposed here is **Chirality Root** — the repository root
product as defined by REF-001. Under the ruled genus it is the canonical
human-governed application environment and generative operating form for
governed professional knowledge work, containing a filesystem-native agent
operating system together with the normative basis, developmental machinery,
evidence, and human judgment by which that operating system is formed and
governed. It is constituted by four functional categories — normative basis,
operative product, developmental machinery, evidence — related by a generative
loop whose closing step is a human judgment no agent can perform.

The PRD carries **7 objectives**, **42 stable commitments** (9 normative-basis
`N-*`, 10 operative `O-*`, 15 developmental `D-*` with `D-3` retired and never
reassigned, 8 evidence `E-*`), a v1 boundary, self-application and concurrency
direction, variant and promotion direction, non-goals, six falsifiers, five
ruled owner decisions with three concordance obligations, and four surfaced
conflicts. The product is one repository, and its own development is inside
its scope (D-12).

### Hard constraints captured

- **The PRD is the sole scope source.** Incorporated-by-reference documents
  are interpretive context and generate no scope of their own.
- **Nothing is accepted here.** All seven gates are human-gated (I1); this run
  rules on none of them.
- **Packages are flat work domains, not phases** and not the four PRD
  categories, which §4.3 expressly forbids reading as a partition.
- **Deliverables are the smallest unit** and must be executable by a bounded
  Agent 2 within its Context Envelope; there is no task sub-level.
- **Identifiers follow `PKG-XX_{PkgLabel}` and `DEL-XX-YY_{DelLabel}`**, with
  the deliverable's first pair mechanically equal to its package number (I6),
  and stay stable across revisions unless the owner requests renumbering (I5).
- **Provenance labels are carried, not flattened.** Where a commitment is
  labelled PROPOSED in the source, the ledger says so wherever it is relied on.
- **Unknowns are `TBD` plus an open issue**, never invention (I2).
- **No machine-absolute path appears anywhere** in this package (O-6).
- **This candidate creates no `PKG-*` or `DEL-*` directory**, writes nothing to
  the instruction surface, and instantiates no guard state. Anticipated write
  loci recorded per deliverable are **planning notes, not authorization**.
- **Most commitments are standing obligations already in force**, not
  greenfield build work. Deliverables against them are conformance,
  verification, and register work — recorded as a framing strain at OI-004.

---

## 5. Vocabulary Map

| CanonicalTerm | Synonyms | Notes |
|---|---|---|
| Chirality Root | the root product, root | The product decomposed here: the repository root product of REF-001, not the agent operating system it contains. |
| Agent operating system | filesystem-native agent OS | The **contained level** of the ruled two-level genus. Not a synonym for Chirality Root. |
| Scope Item (`SOW-NNN`) | atomic unit, requirement statement | The unit of coverage checking, normalized from REF-001. Binds the standard's Atomic Unit. |
| Package (`PKG-XX_{PkgLabel}`) | work domain, partition | Flat partition by category of work. Binds the standard's Partition. Never a phase, never nested. |
| Deliverable (`DEL-XX-YY_{DelLabel}`) | production unit | Smallest unit of production, sized for one bounded Agent 2 execution. Binds the standard's Production Unit. |
| Objective (`OBJ-NNN`) | success condition | Derived one-to-one from PRD `OBJ-n`; see §7 for the binding table. |
| PRD item | source item | An addressable commitment, objective, direction, ruling, obligation, falsifier, or conflict in REF-001; the unit of the F4 forward register. |
| Functional category | §4.1 category | One of normative basis, operative product, developmental machinery, evidence. Classifies functions and authority relationships; **not** a package. |
| Normative basis | ratified corpus | Category, and the subject of PKG-01. The two are not identical — see §11.2. |
| Instruction surface | shared instruction root | `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/` — changing it is a governance action (M2), not ordinary execution. |
| Working root | `WORKING_ROOT`, workspace | Where governed project truth lives. For the root product only, it is the repository root. |
| Guard state | G0–G4 state surfaces | The files the root guards read; instantiated by root Project Setup, not by decomposition. |
| Context Envelope | size class | `S\|M\|L\|XL` sizing for bounded Agent 2 execution; `XL` must be split or explicitly accepted. |
| Write locus | anticipated write target | Planning note recording where a deliverable would write. **Not authorization.** |
| `REGISTER` (deliverable type) | companion register slice | Project-specific type equivalent: a deliverable whose primary artifact is an authoritative companion register of machine truth. Permitted by REF-003's "or project-specific equivalents". |
| `GOVERNANCE_TRANCHE` (deliverable type) | M2 tranche | Project-specific type equivalent reserved for a deliverable whose artifact is an instruction-surface change tranche. **Declared but unused in v1.0** — every candidate for it was expressible as `REQ_SLICE` or `DOC_UPDATE` with an instruction-surface write locus. |
| `PENDING_OWNER_RULING` | — | Gate status meaning staged and offered, never accepted. |

---

## 6. SSOW (structured scope of work)

The SSOW is **103 atomic scope items** (`SOW-001`..`SOW-103`), normalized from
REF-001 §3–§10. The authoritative surface is
`chirality_root_scope_ledger_v1_0.csv`; it is not restated here (the standard
forbids inflating the control surface with companion truth).

| Status | Count | Meaning |
|---|---:|---|
| `IN` | 94 | In scope for the root product's governed work. |
| `OUT` | 9 | Explicit boundary items — PRD non-goals and expressly-not-current-scope statements. Carried, not discarded, so later work cannot silently pull them in. |
| `TBD` | 0 | No source statement in the enumerated scope was unclassifiable. Unresolved *content* inside a classified item is flagged on that item (for example SOW-094). |

Derivation by source section, attributing each row to the first section named
in its `SourceRef`: §3 (6), §4 (5), §5 preamble (1), §5.1 (12), §5.2 (10),
§5.3 (16), §5.4 (8), §6 (7), §7 (7), §8 (14), §9 (10), §10 (7) — total 103.
SOW-007 sits positionally in the §3 block but carries `SourceRef` §9.5 (the
RD-5 ruling), which is why §3 is 6 and §9 is 10.

Three PRD commitments were **split** into more than one scope item because
their clauses have different maintenance loci (DEC-004, DEC-005): N-1 into the
file-native substrate rule (SOW-014) and the domain-engine exception
(SOW-015); N-5 into declared write scope (SOW-019), path containment
(SOW-020), and tool-root snapshot immutability (SOW-021); D-14 into the
currency obligation (SOW-048) and the "check is not built" precondition
(SOW-049). Splitting is the standard's preferred resolution when a unit would
otherwise straddle partitions.

**Every `OUT` item is still assigned to exactly one package.** REF-002 permits
a blank partition for OUT units while REF-003 requires every scope item to
carry exactly one `PackageID`; REF-003 is stricter and does not weaken the
base, so the stricter rule is applied and the divergence is surfaced rather
than silently reconciled (DEC-007, OI-012).

---

## 7. Objectives

Objectives are **derived, not invented**: each is a one-to-one restatement of
a PRD objective, renumbered to the standard's `OBJ-NNN` format while the PRD's
own identifier is preserved in the binding column (I5, I7). All seven carry
the source label **PROPOSED**.

| ObjectiveID | PRD objective | Objective | Primary supporting deliverables |
|---|---|---|---|
| OBJ-001 | OBJ-1 | Coherent and discoverable normative authority — a reader can determine what governs, from the repository alone. | DEL-01-01, DEL-01-02, DEL-01-03, DEL-01-07, DEL-01-08, DEL-02-01, DEL-02-05, DEL-04-07, DEL-04-09 |
| OBJ-002 | OBJ-2 | Governed production of professional knowledge work — the product carries work to an issuance decision that an accountable human makes. | DEL-01-04, DEL-01-06, DEL-02-02, DEL-02-03, DEL-03-02, DEL-03-06, DEL-04-02, DEL-04-06 |
| OBJ-003 | OBJ-3 | The human evaluation and iteration loops close — linkage complete universally, retrievable within a pre-registered bound on a pre-registered sample. | DEL-04-01, DEL-04-03, DEL-04-04, DEL-04-05, DEL-04-08, DEL-04-10, DEL-05-02, DEL-05-03, DEL-05-04, DEL-05-05, DEL-05-07, DEL-05-08, DEL-06-03 |
| OBJ-004 | OBJ-4 | Safe self-application without self-authorization — F1–F3 unobserved, capabilities accepted before consumption, guards registered and passing. | DEL-02-04, DEL-03-04, DEL-03-05, DEL-05-06, DEL-06-01, DEL-06-07 |
| OBJ-005 | OBJ-5 | Situated specialization with governed convergence — one candidate reaches a complete promotion disposition; variant-derived changes used the governed path. | DEL-06-04, DEL-06-05, DEL-06-06, DEL-06-08 |
| OBJ-006 | OBJ-6 | Coordination remains intelligible as concurrent activity grows — ownership, dependencies, and gates reconstructible; stale runs detectable. | DEL-03-03, DEL-05-01, DEL-06-02 |
| OBJ-007 | OBJ-7 | File-native continuity and recoverability — nothing load-bearing lives outside the checkout. | DEL-01-05, DEL-03-01 |

`UnmappedObjectives` is **0**. Full statements, notes, and scope-item mappings
are in `chirality_root_objective_register_v1_0.csv`.

---

## 8. Packages

Six flat work-domain packages. **No nesting, no phases, no overlap, no gaps.**
Each package is a cohesive context set: the boundary is *where the work of
keeping a commitment true happens*, not which PRD section the commitment
appears in (DEC-002).

| PackageID | Name | ScopeDescription | Exclusions |
|---|---|---|---|
| PKG-01_Product_Definition_Normative_Basis_and_Authority | Product Definition, Normative Basis, and Authority | The ratified normative corpus as a constituent of the product: ruled genus and its concordance, invariant-catalog conformance, authority chain, epistemic discipline, the human-authority and three-judgment gate model, the professional-responsibility model, jurisdiction and accountability, v1 user scope, and the non-goal / open-conflict boundary. | Live agent, skill, and tool registries (PKG-02); execution structures and guards (PKG-03); the change machinery itself (PKG-04); evidence machinery (PKG-05). |
| PKG-02_Operative_Instruction_Surface_and_Runtime_Layers | Operative Instruction Surface and Runtime Layers | The instruction surface and the three operative layers that do work: membership and release management, deterministic-tool and runtime-substrate boundaries, the delegation hierarchy and entry rules, declared write scope and capability-boundary controls, and live registry discipline. | Execution-state structures, path anchoring, and containment guards (PKG-03); decision and change machinery (PKG-04). |
| PKG-03_Governed_Execution_Structure_and_Root_Containment | Governed Execution Structure and Root Containment | The path model and containment rule, execution-instance structure and lifecycle, dependency registers, the single governed root working-root exception with its M1–M7 mechanisms and G0–G4 guards, guard-state instantiation, and materialization readiness behind the §5.3 gate. | Agent-surface write-scope declarations (PKG-02); the concurrency-legibility demonstration (PKG-06); evidence artifacts produced by execution (PKG-05). |
| PKG-04_Developmental_Machinery_and_Change_Control | Developmental Machinery and Change Control | The governance harness by which the product changes itself: decision records and terminal-artifact discipline, identity attribution, validation severity, governance integration rules and routed notices, the governed loop and receipts, human-gated closeout, the export boundary, PRD amendment and attributable change control, the source-currency check, and decomposition-pipeline discipline with root coverage demonstration. | The normative content being changed (PKG-01); the operative surfaces being changed (PKG-02); evidence schemas and warrant machinery (PKG-05). |
| PKG-05_Evidence_Provenance_and_Audit | Evidence, Provenance, and Audit | The record that makes reliance answerable: run-record trees, snapshot / handoff / receipt discipline, distinct SHA roles, claim provenance and the warrant lifecycle, read-only audit and evaluation surfaces, validation-evidence mutation control, closure criteria, and evidence-linkage completeness with its retrieval evaluation. | The acts the evidence records (PKG-04); the execution structures the evidence describes (PKG-03). |
| PKG-06_Self_Application_Variants_and_Release | Self-Application, Variants, and Release | The product's reciprocal relations to itself and to situated working roots: self-application discipline and falsifier observation, concurrency legibility, the approval-vehicle practice record, downward variant service without weakening, the domain-engine truth boundary, the upward governed-promotion pathway, the release-authority gate, and situated-working-root convergence. | Guard and mechanism state surfaces themselves (PKG-03); the promotion machinery's record classes (PKG-04). |

**Why six and not four.** §4.3 forbids reading the four categories as a
partition, and §11.2 shows the result: every category spans four or more of
these packages, and no package is coextensive with any category —
participation ranges from two categories (PKG-02) to all four (PKG-01,
PKG-04, PKG-06). The partition is a work-domain judgment offered under Gate 4
(DEC-003).

---

## 9. Deliverables

45 deliverables, each belonging to exactly one package, each sized for a
bounded Agent 2 execution. `ResponsibleParty` is `TBD` for every deliverable —
this run holds no assignment authority (OI-011). Descriptions, anticipated
artifacts, covered scope items, and envelope notes are in
`chirality_root_deliverable_register_v1_0.csv`.

**`AnticipatedWriteLocus` is a planning note, not authorization.** It exists so
that a later G2 ownership register and G3 work graph can be derived without
reinterpreting this decomposition. Any locus naming the instruction surface
(`AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`,
`.github/workflows/`) requires an independently authorized M2 tranche;
`execution/_harness` is written by root Project Setup, not by a deliverable
executor.

### PKG-01_Product_Definition_Normative_Basis_and_Authority

| DeliverableID | Name | Type | ContextEnvelope | AnticipatedWriteLocus | SupportsObjectives |
|---|---|---|---|---|---|
| DEL-01-01_Genus_Concordance_Closure_and_Standing_Map | Genus Concordance Closure and Standing Bidirectional Map | REQ_SLICE | M | execution-tree; instruction-surface (M2) only if residual drift requires an exact-prose act | OBJ-001 |
| DEL-01-02_Invariant_Catalog_Conformance_Register | Invariant Catalog Conformance Register | REGISTER | M | execution-tree | OBJ-001 |
| DEL-01-03_Authority_Chain_and_Conflict_Surfacing_Conformance | Authority Chain and Conflict-Surfacing Conformance | REQ_SLICE | M | execution-tree; instruction-surface (M2) if a chain statement must change | OBJ-001 |
| DEL-01-04_Human_Authority_and_Three_Judgment_Gate_Model | Human Authority and Three-Judgment Gate Model | REQ_SLICE | M | execution-tree | OBJ-002 |
| DEL-01-05_File_Native_Authority_Substrate_Conformance | File-Native Authority Substrate Conformance | REQ_SLICE | S | execution-tree | OBJ-007 |
| DEL-01-06_Four_Pillars_and_Professional_Responsibility_Conformance | Four Pillars and Professional-Responsibility Conformance | DOC_UPDATE | S | execution-tree | OBJ-002 |
| DEL-01-07_Jurisdiction_Accountability_and_v1_User_Scope_Register | Jurisdiction, Accountability, and v1 User Scope Register | REGISTER | S | execution-tree | OBJ-001 |
| DEL-01-08_Non_Goal_Boundary_and_Open_Conflict_Register | Non-Goal, Boundary, and Open-Conflict Register | REGISTER | S | execution-tree | OBJ-001 |

### PKG-02_Operative_Instruction_Surface_and_Runtime_Layers

| DeliverableID | Name | Type | ContextEnvelope | AnticipatedWriteLocus | SupportsObjectives |
|---|---|---|---|---|---|
| DEL-02-01_Instruction_Surface_Membership_and_Release_Management | Instruction Surface Membership and Release Management | DOC_UPDATE | M | instruction-surface (M2) | OBJ-001 |
| DEL-02-02_Three_Layer_Authority_Boundary_Conformance | Three-Layer Authority Boundary Conformance | REQ_SLICE | M | execution-tree; instruction-surface (M2) if a layer statement must change | OBJ-002 |
| DEL-02-03_Delegation_Hierarchy_and_Entry_Rules | Delegation Hierarchy and Entry Rules | DOC_UPDATE | M | instruction-surface (M2) | OBJ-002 |
| DEL-02-04_Declared_Write_Scope_and_Capability_Boundary_Controls | Declared Write Scope and Capability-Boundary Controls | SECURITY_CONTROL | M | instruction-surface (M2); execution-tree for audit evidence | OBJ-004 |
| DEL-02-05_Live_Registry_Discipline_for_Skills_and_Tools | Live Registry Discipline for Skills and Tools | REGISTER | S | instruction-surface (M2); execution-tree for drift reports | OBJ-001 |

### PKG-03_Governed_Execution_Structure_and_Root_Containment

| DeliverableID | Name | Type | ContextEnvelope | AnticipatedWriteLocus | SupportsObjectives |
|---|---|---|---|---|---|
| DEL-03-01_Path_Model_and_ScopePath_Containment_Conformance | Path Model and ScopePath Containment Conformance | SECURITY_CONTROL | M | execution-tree; tools/ (M2) if a check must change | OBJ-007 |
| DEL-03-02_Execution_Structure_and_Lifecycle_Conformance | Execution Structure and Lifecycle Conformance | REQ_SLICE | M | execution-tree | OBJ-002 |
| DEL-03-03_Dependency_Register_and_Derived_Graph_Boundary | Dependency Register and Derived-Graph Boundary | REQ_SLICE | S | execution-tree | OBJ-006 |
| DEL-03-04_Root_Working_Root_Exception_Conformance | Root Working-Root Exception Conformance | REQ_SLICE | M | execution-tree | OBJ-004 |
| DEL-03-05_Guard_State_Instantiation_and_Registration | Guard State Instantiation and Registration | DATA_MODEL_CHANGE | M | execution/_harness (root Project Setup; authorized separately) | OBJ-004 |
| DEL-03-06_Root_Materialization_Readiness_and_Deliverable_Stream | Root Materialization Readiness and First Deliverable Stream | REQ_SLICE | M | execution-tree (gated) | OBJ-002 |

### PKG-04_Developmental_Machinery_and_Change_Control

| DeliverableID | Name | Type | ContextEnvelope | AnticipatedWriteLocus | SupportsObjectives |
|---|---|---|---|---|---|
| DEL-04-01_Decision_Record_and_Terminal_Artifact_Discipline | Decision Record and Terminal-Artifact Discipline | REGISTER | M | execution-tree; instruction-surface (M2) for the register itself | OBJ-003 |
| DEL-04-02_Identity_Attribution_and_Refusal_Controls | Identity Attribution and Refusal Controls | SECURITY_CONTROL | S | execution-tree; tools/ (M2) if a check must change | OBJ-002 |
| DEL-04-03_Validation_Severity_and_Override_Controls | Validation Severity and Override Controls | CI_CD_CHANGE | M | tools/ (M2); execution-tree for evidence | OBJ-003 |
| DEL-04-04_Governance_Integration_Rules_and_Change_Notice_Routing | Governance Integration Rules and Change-Notice Routing | REQ_SLICE | M | execution-tree; instruction-surface (M2) for rule text | OBJ-003 |
| DEL-04-05_Root_Governed_Loop_and_Receipt_Discipline | Root Governed Loop and Receipt Discipline | DOC_UPDATE | M | execution-tree | OBJ-003 |
| DEL-04-06_Change_Management_and_Human_Gated_Closeout | Change Management and Human-Gated Closeout | CI_CD_CHANGE | S | execution-tree | OBJ-002 |
| DEL-04-07_Public_Export_Boundary_Conformance | Public Export Boundary Conformance | SECURITY_CONTROL | S | execution-tree; exports/ (M2) if the profile must change | OBJ-001 |
| DEL-04-08_PRD_Amendment_and_Attributable_Change_Control | PRD Amendment and Attributable Change Control | REQ_SLICE | M | execution-tree; instruction-surface (M2) for any PRD amendment | OBJ-003 |
| DEL-04-09_PRD_Source_Currency_Check_Capability | PRD Source-Currency Check Capability | TEST_SUITE | L | tools/ (M2); execution-tree for the annex and reports | OBJ-001 |
| DEL-04-10_Decomposition_Pipeline_and_Root_Coverage_Demonstration | Decomposition Pipeline and Root Coverage Demonstration | REGISTER | M | execution-tree | OBJ-003 |

### PKG-05_Evidence_Provenance_and_Audit

| DeliverableID | Name | Type | ContextEnvelope | AnticipatedWriteLocus | SupportsObjectives |
|---|---|---|---|---|---|
| DEL-05-01_Run_Record_Tree_Conformance | Run Record Tree Conformance | REQ_SLICE | M | execution-tree | OBJ-006 |
| DEL-05-02_Snapshot_Handoff_and_Receipt_Discipline | Snapshot, Handoff, and Receipt Discipline | REQ_SLICE | M | execution-tree | OBJ-003 |
| DEL-05-03_SHA_Role_Register | SHA Role Register | REGISTER | S | execution-tree | OBJ-003 |
| DEL-05-04_Claim_Provenance_and_Warrant_Lifecycle | Claim Provenance and Warrant Lifecycle | REQ_SLICE | M | execution-tree | OBJ-003 |
| DEL-05-05_Audit_and_Evaluation_Surface_Governance | Audit and Evaluation Surface Governance | DOC_UPDATE | S | execution-tree; instruction-surface (M2) if the index must change | OBJ-003 |
| DEL-05-06_Validation_Evidence_Mutation_Control | Validation Evidence Mutation Control | SECURITY_CONTROL | M | tools/ (M2); execution-tree for evidence | OBJ-004 |
| DEL-05-07_Closure_Criteria_Conformance | Closure Criteria Conformance | REQ_SLICE | S | execution-tree | OBJ-003 |
| DEL-05-08_Evidence_Linkage_Completeness_and_Retrieval_Evaluation | Evidence Linkage Completeness and Retrieval Evaluation | OBSERVABILITY | M | execution-tree | OBJ-003 |

### PKG-06_Self_Application_Variants_and_Release

| DeliverableID | Name | Type | ContextEnvelope | AnticipatedWriteLocus | SupportsObjectives |
|---|---|---|---|---|---|
| DEL-06-01_Self_Application_Discipline_and_Falsifier_Observation | Self-Application Discipline and Falsifier Observation | REQ_SLICE | M | execution-tree | OBJ-004 |
| DEL-06-02_Concurrency_Mechanism_Legibility_and_Run_State_Reconstruction | Concurrency Mechanism Legibility and Run-State Reconstruction | OBSERVABILITY | M | execution-tree | OBJ-006 |
| DEL-06-03_Approval_Vehicle_Practice_Record | Approval Vehicle Practice Record | DOC_UPDATE | S | execution-tree | OBJ-003 |
| DEL-06-04_Downward_Variant_Service_and_Non_Weakening | Downward Variant Service and Non-Weakening | REQ_SLICE | M | execution-tree | OBJ-005 |
| DEL-06-05_Domain_Engine_Truth_Boundary | Domain Engine Truth Boundary | REQ_SLICE | S | execution-tree | OBJ-005 |
| DEL-06-06_Governed_Promotion_Pathway | Governed Promotion Pathway | REQ_SLICE | M | execution-tree | OBJ-005 |
| DEL-06-07_Release_Authority_Gate | Release Authority Gate | REQ_SLICE | M | execution-tree | OBJ-004 |
| DEL-06-08_Situated_Working_Root_Convergence_Demonstration | Situated Working Root Convergence Demonstration | REQ_SLICE | M | execution-tree | OBJ-005 |

---

## 10. Scope Ledger

The Scope Ledger is `chirality_root_scope_ledger_v1_0.csv` — one row per scope
item, with columns `ScopeItemID`, `InOutStatus`, `ScopeItemStatement`,
`SourceRef`, `PackageID`, `DeliverableIDs`, `ObjectiveIDs`, `PRDItem`,
`Categories`, `DecisionRef`, `OpenIssue`, `Notes`. It is authoritative; this
section states the structural contract it satisfies.

- **Every scope item carries exactly one `PackageID`** (hard rule; 103/103).
- **Every IN-scope item maps to at least one deliverable** (94/94); mappings
  may cross packages, because a scope item's owning package is a partition
  fact while its deliverable mapping is a coverage fact (DEC-010).
- **`SourceRef` names a PRD section and the item's provenance label**, so the
  PROPOSED status of D-13, D-14, D-15, D-16, the objectives, §7.2, §8.3, and
  F4–F6 is visible on every row that relies on them.
- **`Categories`** records which §4.1 functional categories a unit
  participates in; it is the input to the D-15 demonstration and is
  deliberately many-valued.

---

## 11. Coverage and Telemetry

Full telemetry is `chirality_root_coverage_telemetry_v1_0.md`. Summary:

| Metric | Value |
|---|---:|
| ScopeItemCount | 103 (IN 94 / OUT 9 / TBD 0) |
| PackageCount | 6 |
| DeliverableCount | 45 |
| ObjectiveCount | 7 |
| **UnassignedScopeItems** | **0** |
| ScopeItemsWithoutDeliverableMapping | 0 |
| UnmappedObjectives | 0 |
| ContextEnvelopeCounts | S=14, M=30, L=1, XL=0 |
| OpenIssuesByType | SOURCE_CURRENCY=2, FRAMING_STRAIN=3, UNBUILT_CAPABILITY=1, OWNER_RULING_PENDING=1, PARTITION_BOUNDARY=1, GATE_SEQUENCING=1, SCOPE_TBD=1, CONTEXT_ENVELOPE=1, RESPONSIBILITY_UNASSIGNED=1, OBJECTIVE_GRANULARITY=1 (total 13) |
| Revision / Date | v1.0 candidate / 2026-07-25 |

### 11.1 Context Budget QA

No `XL` deliverable is proposed. One `L` deliverable —
`DEL-04-09_PRD_Source_Currency_Check_Capability` — is **proposed** as
large-but-single-domain with envelope notes, for the owner to accept or split
at Gate 5/6; it is splittable by check class if implementation review finds
churn (OI-010). Every other deliverable is `S`
or `M`, single-package, and focused on one primary artifact shape.

### 11.2 D-15 — four-category coverage demonstration

Each §4.1 category has decomposition coverage. **No category is deferred, so
no reasoned deferral is recorded.**

| §4.1 category | Scope items | Packages participating | Deliverables | Status |
|---|---:|---|---:|---|
| Normative basis | 41 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06 | 21 | COVERED |
| Operative product | 26 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 18 | COVERED |
| Developmental machinery | 59 | PKG-01, PKG-03, PKG-04, PKG-05, PKG-06 | 25 | COVERED |
| Evidence | 18 | PKG-01, PKG-04, PKG-05, PKG-06 | 16 | COVERED |

The spread is the point: the categories are non-exclusive functions, and the
partition is not derived from them (§4.3, DEC-003). D-12 is honoured directly
— developmental machinery is decomposed as product scope (PKG-04, 10
deliverables), not exempted as overhead.

### 11.3 F4 — bidirectional traceability

| Direction | Register | Population | Result |
|---|---|---:|---|
| PRD item → decomposition | `chirality_root_prd_coverage_forward_v1_0.csv` | 84 | 84 COVERED, 0 DEFERRED, 0 UNCOVERED |
| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 51 | 51 TRACED, 0 UNTRACED |

The forward population is every addressable PRD item in the enumerated scope
source: OBJ-1..OBJ-7; N-1..N-9; O-1..O-10; D-1, D-2, D-4..D-16; E-1..E-8; the
§3 v1 boundary and objective discipline; the §4 category, loop, judgment, and
non-prescription statements; §5 registry discipline; the four §6 directions;
the two §7 directions; §8.1 non-goals; F1..F6; §8.3 release authority;
RD-1..RD-5; §9.1 obligations (a), (b), (c); the §10.1 annex obligation;
C-1..C-4; and §10.3 adoption mechanics. `D-3` is deliberately absent and never
reassigned.

**This is a candidate result.** F4 speaks to *accepted* scope units; nothing
here is accepted, so this is evidence offered to the gate, not a closure
claim.

---

## 12. Open Issues

| IssueID | Type | Affected | Description | Required resolution |
|---|---|---|---|---|
| OI-001 | SOURCE_CURRENCY | SOW-060, SOW-089, SOW-090, SOW-091, SOW-098, SOW-099, SOW-100, SOW-101 | Several PRD statements describe the repository as it stood at the PRD's own `SourceCorpusBasis`, and accepted acts recorded in the governance register at the current basis appear to have discharged them — the §9.1 concordance obligations and the §10.2 conflicts. This decomposition **does not adjudicate that**: it derives the scope items from the source as written and sets their coverage to standing verification and maintenance rather than re-performance. | Owner disposition. Under D-14 this is precisely a currency finding — a REVIEW finding routed to the owner, never an automatic amendment, and never an agent edit to adopted bytes (D-13). |
| OI-002 | SOURCE_CURRENCY | SOW-085, SOW-102, and every PROPOSED-labelled row | The adopted bytes state that PROPOSED items are inert until the adoption instrument's ruling, while the governance register records that the ruling occurred and the PROPOSED items take effect. The ledger therefore carries **the source label** plus a note, and claims no label change. | Owner confirmation of the operative status of the PROPOSED set. F6 exists precisely to catch a label treated as changed without an instrument. |
| OI-003 | FRAMING_STRAIN | whole package | `SOFTWARE_DECOMP`'s intake framing is a software development SOW. The root product's scope is predominantly normative corpus, governance machinery, and evidence; "artifacts" are largely governance records, registers, and validators rather than code. The standard was conformed to rather than adapted, and the strain is recorded here rather than silently smoothed. | Owner ruling at Gate 1 / Gate 5 on whether this manager remains the right conforming variant for the root product, or whether a root-specific conforming variant should be proposed through the component-design path. |
| OI-004 | FRAMING_STRAIN | 33 TRANSCRIBED and 5 CLARIFIED commitments | A commitment already in force generates **conformance and verification** work, not construction. Deliverables against such commitments are written as conformance slices; that is a defensible reading of N-9 ("the running system continues to satisfy the invariants") but it makes many deliverables recurring controls rather than one-shot productions. | Owner ruling on whether standing conformance belongs inside the package/deliverable lifecycle or in a separate standing-controls surface. |
| OI-005 | UNBUILT_CAPABILITY | SOW-049, DEL-04-09 | D-14's source-currency check is not built — no generator, schema, or executable check exists — and four of its nine classes require semantic judgment. Reliance on D-14 before the build is unwarranted. | Build through DEL-04-09, or record an explicit deferral. Until then, currency findings are produced by human reading, as OI-001 was. |
| OI-006 | OWNER_RULING_PENDING | all seven gates | Nothing in this package is accepted. Every gate reads `PENDING_OWNER_RULING`. | Owner ruling. No agent may close a gate (I1, K-AUTH-1). |
| OI-007 | PARTITION_BOUNDARY | SOW-065, SOW-066 vs SOW-034 | The §6.3 concurrency mechanisms are implemented as state surfaces owned by PKG-03 but demonstrated for legibility by PKG-06. The scope items are split so each lands in exactly one package, with the relation recorded at DEC-008. | Owner confirmation at Gate 4 that the split is the intended ownership boundary. |
| OI-008 | GATE_SEQUENCING | SOW-001, SOW-061, SOW-103, DEL-03-06 | Materialization of root packages sits behind the D-GOV-21 §5.3 gate, and this decomposition authorizes none of it. DEL-03-06 is readiness and evidence only. | Keep materialization behind its own gate; the acceptance of this decomposition is a precondition, not the authorization. |
| OI-009 | SCOPE_TBD | SOW-094 | The referent of the database-backed attribution interface named in the RD-2 evolution path is `TBD` in the source. It is carried as an OUT boundary item without being resolved (I2). | Owner fixes the referent if and when that scope is opened. |
| OI-010 | CONTEXT_ENVELOPE | DEL-04-09 | One `L` deliverable is proposed: a checker plus a regenerable derivative package. It is single-domain but multi-component. | Accept as `L` with notes, or direct a split by check class (five mechanical, four semantic) at Gate 5. |
| OI-011 | RESPONSIBILITY_UNASSIGNED | all 45 deliverables | `ResponsibleParty` is `TBD` throughout; this run holds no assignment authority. | Owner or a later planning act assigns responsibility. |
| OI-012 | FRAMING_STRAIN | 9 OUT items | REF-002 permits a blank partition for OUT units; REF-003 requires every scope item to carry exactly one `PackageID`. The stricter rule was applied (no weakening of the base) and the divergence is surfaced rather than reconciled. | Owner confirmation at Gate 4; no change is proposed to either instruction file by this candidate. |
| OI-013 | OBJECTIVE_GRANULARITY | OBJ-002 (PRD OBJ-2) | PRD §3 OBJ-2's success condition ends "Demonstrated at root and in at least one situated working root." No deliverable covers the situated-working-root half: `DEL-03-06` carries the deliverable stream **at root only**, and `DEL-06-08` — the one situated-root deliverable — is mapped to OBJ-005, covers only SOW-003, and concerns a *recorded convergence path* (v1 boundary (c)) rather than a deliverable stream reaching an issuance decision in a variant. **No scope item states the missing clause and no reasoned deferral is recorded.** F4 is not formally tripped, because objectives are traced as whole units and OBJ-2 has coverage at objective granularity; the gap is inside the objective, where the registers cannot see it. Raised by the adversarial verification of this candidate (V1, MAJOR-1). | **`PENDING_OWNER_RULING`.** The disposition is the owner's: either cover the clause (a new scope item mapped to an extended `DEL-03-06` or a new PKG-06 deliverable) or record an explicit reasoned deferral to a post-v1 stage. **This candidate chooses neither** — no scope item, deliverable, or deferral is added here, so that the choice reaches Gate 3 / Gate 6 unmade. |

---

## 13. Decision Log / Change Log

| DecisionRef | Date | Decision | Rationale |
|---|---|---|---|
| DEC-001 | 2026-07-25 | `docs/PRD_ROOT.md` is the sole scope source; incorporated-by-reference documents are interpretive context only. | The sealed brief's binding source discipline and the PRD's own D-9 posture. Prevents the ratified corpus from silently re-entering as scope. |
| DEC-002 | 2026-07-25 | A scope item is assigned to the package that owns **the work of keeping the commitment true**, not to the package matching the PRD section it appears in. | Produces cohesive context sets (REF-003's stated purpose for work-domain packages) instead of mirroring the source's table of contents. |
| DEC-003 | 2026-07-25 | The partition is **not** the four §4.1 categories; six work-domain packages are proposed instead, and category coverage is demonstrated by a many-to-many mapping. | §4.3 expressly forbids reading the categories as a partition; D-15 constrains coverage demonstration only. §11.2 evidences the non-identity. |
| DEC-004 | 2026-07-25 | N-1 is split into the file-native substrate rule (SOW-014) and the domain-engine exception (SOW-015). | The exception's maintenance locus is the variant/domain boundary (PKG-06), not the normative corpus. The standard prefers splitting over forcing a straddling unit. |
| DEC-005 | 2026-07-25 | N-5 is split into declared write scope (SOW-019, PKG-02), path containment (SOW-020, PKG-03), and tool-root snapshot immutability (SOW-021, PKG-05). | Three clauses with three distinct enforcement loci; keeping them as one unit would have forced an arbitrary single-package assignment. |
| DEC-006 | 2026-07-25 | The v1 boundary's three conditions are carried as separate scope items rather than one. | They are separately testable and land in different packages; the boundary note is carried as a fourth item so a redefinition of v1 remains traceable. |
| DEC-007 | 2026-07-25 | `OUT` boundary items are retained in the ledger and assigned to an owning package, rather than dropped. | REF-003 requires exactly one `PackageID` per scope item; retaining boundary items gives later work a place to check that a non-goal has not been silently pulled in. Divergence from REF-002's permissive rule surfaced at OI-012. |
| DEC-008 | 2026-07-25 | PKG-03 owns the concurrency mechanisms' state surfaces; PKG-06 owns the concurrency-legibility demonstration. | Avoids two packages claiming the same work while keeping §6.3's own framing (legibility as an emergent property of declared ownership) intact. Recorded at OI-007. |
| DEC-009 | 2026-07-25 | Scope items derived from §9.1 obligations and §10.2 conflicts are carried IN with coverage expressed as **standing verification and maintenance**, not as re-performance of one-time acts. | The source states the obligations; the register at the current basis records accepted acts that appear to discharge them. Neither fact is adjudicated by an agent: the items stay, the observation is recorded at OI-001, and F5 remains the standing test. |
| DEC-010 | 2026-07-25 | A scope item may map to deliverables in more than one package; only its `PackageID` is exclusive. | I4's exclusivity is a partition property. Coverage mapping is best-effort and cross-cutting by nature; the app-dev precedent does the same. |
| DEC-011 | 2026-07-25 | Two project-specific deliverable types are added — `REGISTER` and `GOVERNANCE_TRANCHE` — and recorded in the Vocabulary Map. `GOVERNANCE_TRANCHE` is declared but unused at v1.0. | REF-003's taxonomy is explicitly suggestive and admits project-specific equivalents. Register-shaped and tranche-shaped deliverables are the root product's characteristic output and had no honest fit in the software taxonomy. |
| DEC-012 | 2026-07-25 | Objectives are renumbered to `OBJ-001`..`OBJ-007` with the PRD identifier preserved in a binding column. | REF-002/REF-003 specify `OBJ-NNN`; renumbering without preserving the source ID would have broken traceability, and reusing `OBJ-1` would have broken the format. |
| DEC-013 | 2026-07-25 | Heavy machine truth lives in six companion registers; the working surface stays a control surface carrying the full identifier set. | REF-002's modular-package default, plus the G2 literal-containment requirement that every `PKG-*`/`DEL-*` identifier appear verbatim in the decomposition surface. |

### Change Log

- 2026-07-25 — v1.0 candidate authored from `docs/PRD_ROOT.md` at basis
  `24726a73c64a849909e3615c32ef1a888b3dfd36` under run
  `ROOT-STEP8-DECOMP-20260725`. First root decomposition; no prior revision
  exists, so no renumbering question arises. All gates `PENDING_OWNER_RULING`.

---

## 14. Downstream Execution Notes

- **Nothing downstream may proceed on this document until Gate 7 is ruled.**
  D-9 makes the decomposition pipeline non-waivable: packages and deliverables
  come only from an accepted decomposition.
- **G2 readiness.** Every `PKG-*` and `DEL-*` identifier in this package
  appears verbatim in this working surface (§8, §9), so a later
  surface-ownership register may use them as literal `decomposition_ref`
  values against this file. Identifiers are stable under I5 and must not be
  renumbered without an explicit owner instruction.
- **G3 readiness.** `AnticipatedWriteLocus` per deliverable is recorded so a
  first work graph can declare write targets without reinterpreting this
  document. It records intent, not permission: instruction-surface loci need
  independently authorized M2 tranches, and `execution/_harness` is root
  Project Setup's surface.
- **Materialization stays gated.** This candidate creates no `PKG-*` or
  `DEL-*` directory. Directory creation is step 9 behind the D-GOV-21 §5.3
  gate and is out of scope for both this run and this document.
- **Executors** should take one deliverable at a time, treat `ContextEnvelope`
  as a work-sizing constraint, preserve `ResponsibleParty: TBD` until a human
  assigns it, and read the companion register for the deliverable's full
  description, artifacts, and covered scope items.
- **Reviewers** should check: package flatness and the absence of phases;
  every scope item carrying exactly one package; both F4 registers still
  closing after any amendment; the D-15 category table regenerated rather than
  hand-edited; no XL deliverable introduced; and no claim of acceptance
  appearing anywhere in the package.
- **On amendment**, the companion registers are the amendment surface for
  their data and the telemetry is regenerated from them; the working surface
  is updated to match. Any single-file render assembled later is a `derived
  publication artifact` and never the amendment surface.
