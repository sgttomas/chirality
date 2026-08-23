# Chirality Root — Software Decomposition (SCA-004 CANDIDATE v1.3)

**Package Role:** `working surface`
**Agent Role:** `SOFTWARE_DECOMP` (Agent 1), under a sealed brief from Agent 0
**Method basis:** `docs/DECOMPOSITION_STANDARD.md` (RATIFIED) extended by `agents/AGENT_SOFTWARE_DECOMP.md`
**Revision:** v1.3 (SCA-004 Gate-3 candidate — not approved or applied) · **Date:** 2026-08-23
**Source-basis commit:** `602dd71b8c123d8a47a36644db1453f515c0f778` (Receipt-64 policy effect; PRD Revision 8)
**Predecessor (v1.1):** accepted by the SCA-001 Gate 5 owner confirmation, 2026-07-26; Git effect PR #366 merge `2db2c7128c32d32d197ae47660eb34ab2cef9660`
**v1.0 acceptance:** AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`; EffectiveSHA `ea0ad7a566ddb51d89297bfcf491636f1fc5dd15` (merge of PR #347); instrument `docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md`
**Run:** `ROOT_V3_PHASE0C_2026-08-23/N1`; predecessor lineage `GOV-STEP4-SCA-20260729`; origin run `ROOT-STEP8-DECOMP-20260725`
**Amendment:** `SCA-004` exact Gate-3 candidate over accepted revision 1.2 SHA-256 `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`; owner Gate-3 and Gate-4 approvals are pending; no candidate byte has live effect

> **Status: SCA-004 GATE-3 CANDIDATE — NOT APPROVED OR APPLIED.**
> Revision 1.2 at SHA-256
> `23f6ae0fd3088313d84b4f5bb2d36b207ba7a5442cfc5b776a3e4da2faa64f3d`
> remains the accepted live basis. These candidate bytes narrow DEL-02-06 to
> standing semantic integration/release assurance, add six bounded PKG-02
> runtime carriers and one PKG-04 Root receipt-validator carrier, and
> recompute the synchronized registers and telemetry. They take effect only
> after separate owner Gate-3 and Gate-4 approvals and a later authorized
> Gate-5 application. `_LATEST.md`, folders, SOWs, lifecycles, dependencies,
> runtime, tools, App truth, and all ten HELD_UNAVAILABLE bindings remain
> unchanged.
>
> **What the accepted amendment did.** SCA-002 restated the SOW-042 scope-ledger row
> and the DEL-04-06 deliverable-register row from the superseded Rev 6
> D-8 wording to the D-GOV-31 successor merge-gate policy (PRD Revision 7
> row D-8 and annex §5.3.1), and advanced the sole-scope-source pin to
> Revision 7. Receipt 64 subsequently simplified that accepted policy to
> owner direction recorded in ordinary closeout evidence and reconciled the
> two companion rows by PR review. No ID, status, mapping, package,
> deliverable, objective, count, or topology changed; no historical record
> is rewritten.
>
> **Lineage preservation.** D-GOV-25 (v1.0), the SCA-001 Gate 5
> confirmation (v1.1), the immutable SCA-002 candidate package, and its
> application append continue to identify and govern their respective
> states. This metadata reconciliation changes no historical ruling and
> reuses no stable ID.

---

## 1. Gate Log

| Gate | Name | Status | Ruling and evidence |
|---|---|---|---|
| Gate 1 | Intake understanding | `ACCEPTED` | Owner ruling 2026-07-25, D-GOV-25, AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`. Evidence: §4 Intake Summary and §2 References; the sole scope source is pinned by path, sha256, and basis commit. |
| Gate 2 | SSOW and vocabulary | `ACCEPTED` | Owner ruling 2026-07-25, D-GOV-25, AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`. Evidence: 103 atomic scope items with `IN\|OUT\|TBD` status in `chirality_root_scope_ledger_v1_0.csv`; §5 Vocabulary Map. |
| Gate 3 | Objectives | `ACCEPTED` | Owner ruling 2026-07-25, D-GOV-25, AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`. Evidence: §7 Objectives: OBJ-001..OBJ-007 derived one-to-one from PRD OBJ-1..OBJ-7; `chirality_root_objective_register_v1_0.csv`. Ruled with the OBJ-2 situated-working-root deferral of OI-013. |
| Gate 4 | Packages | `ACCEPTED` | Owner ruling 2026-07-25, D-GOV-25, AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`. Evidence: §8 Packages: six flat work-domain packages; every IN-scope item assigned to exactly one. |
| Gate 5 | Deliverables | `ACCEPTED` | Owner ruling 2026-07-25, D-GOV-25, AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`. Evidence: §9 Deliverables: 45 deliverables, each single-package, context-sized, with anticipated artifacts and write locus; the one `L` deliverable accepted as proposed. |
| Gate 6 | Coverage and context budget | `ACCEPTED` | Owner ruling 2026-07-25, D-GOV-25, AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`. Evidence: §11 and `chirality_root_coverage_telemetry_v1_0.md`: `UnassignedScopeItems` 0, `UnmappedObjectives` 0, no XL deliverable, F4 both directions closed with one recorded deferral (OBJ-2). |
| Gate 7 | Publish / final acceptance | `ACCEPTED` | Owner ruling 2026-07-25, D-GOV-25, AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`. **This decomposition is the accepted basis for downstream work.** The verbatim ruling is in D-GOV-25. |

**Acceptance vehicle, as exercised.** The owner ruled over the exact candidate
commit `ec62af0700e530c1640698fa406398cb1cb45d29` by merge-and-proceed
direction, with the ruling recorded verbatim in D-GOV-25 and bound to that SHA
(K-AUTH-2). The applied state is `ea0ad7a566ddb51d89297bfcf491636f1fc5dd15`.
Gate-by-gate review was the available alternative and was not the vehicle
used; all seven gates were ruled together against the one candidate.

---

## 2. References

### 2.1 Scope source (the only one)

| RefID | Source | Role | sha256 | Basis |
|---|---|---|---|---|
| REF-001 | `docs/PRD_ROOT.md` | **Sole scope source.** Objectives (§3), categories (§4), stable commitments (§5), including O-11 continuing Root stewardship of generic runtime, self-application direction (§6), variant and promotion direction (§7), non-goals and falsifiers (§8), ruled owner decisions (§9), source-concordance obligations (§10). | `d4f97d7529f904ac46987eaf5ccaf751bfc73df35edd239166ca43170a275cc4` | Exact SCA-003 basis-reconciliation PRD candidate; Revision 8 policy effect `main@602dd71b8c123d8a47a36644db1453f515c0f778` (D-GOV-31 as simplified by Receipt 64) |

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

The PRD carries **7 objectives**, **43 stable commitments** (9 normative-basis
`N-*`, 11 operative `O-*`, 15 developmental `D-*` with `D-3` retired and never
reassigned, 8 evidence `E-*`), a v1 boundary, self-application and concurrency
direction, variant and promotion direction, non-goals, six falsifiers, five
ruled owner decisions with three concordance obligations, and four surfaced
conflicts. The product is one repository, and its own development is inside
its scope (D-12).

### Hard constraints captured

- **The PRD is the sole scope source.** Incorporated-by-reference documents
  are interpretive context and generate no scope of their own.
- **The original seven decomposition gates are accepted under D-GOV-25.** This
  amendment uses SCOPE_CHANGE's five separately human-gated decisions; no stage
  self-accepts.
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
- **This decomposition amendment creates no `PKG-*` or `DEL-*` directory**, writes nothing to
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
| `GOVERNANCE_TRANCHE` (deliverable type) | M2 tranche | Project-specific type equivalent reserved for a deliverable whose artifact is an instruction-surface change tranche. **Declared but unused in v1.1** — every candidate for it was expressible as `REQ_SLICE` or `DOC_UPDATE` with an instruction-surface write locus. |
| `ACCEPTED` (gate status) | — | Gate status meaning the owner ruled the gate. It replaced the candidate-era pending status, which meant staged and offered, never accepted. |

---

## 6. SSOW (structured scope of work)

The SSOW is **104 atomic scope items** (`SOW-001`..`SOW-104`), normalized from
REF-001 §3–§10. The authoritative surface is
`chirality_root_scope_ledger_v1_0.csv`; it is not restated here (the standard
forbids inflating the control surface with companion truth).

| Status | Count | Meaning |
|---|---:|---|
| `IN` | 95 | In scope for the root product's governed work. |
| `OUT` | 9 | Explicit boundary items — PRD non-goals and expressly-not-current-scope statements. Carried, not discarded, so later work cannot silently pull them in. |
| `TBD` | 0 | No source statement in the enumerated scope was unclassifiable. Unresolved *content* inside a classified item is flagged on that item (for example SOW-094). |

Derivation by source section, attributing each row to the first section named
in its `SourceRef`: §3 (6), §4 (5), §5 preamble (1), §5.1 (12), §5.2 (11),
§5.3 (16), §5.4 (8), §6 (7), §7 (7), §8 (14), §9 (10), §10 (7) — total 104.
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
| OBJ-001 | OBJ-1 | Coherent and discoverable normative authority — a reader can determine what governs, from the repository alone. | DEL-01-01, DEL-01-02, DEL-01-03, DEL-01-07, DEL-01-08, DEL-02-01, DEL-02-05, DEL-02-06, DEL-04-07, DEL-04-09, DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12 |
| OBJ-002 | OBJ-2 | Governed production of professional knowledge work — the product carries work to an issuance decision that an accountable human makes. | DEL-01-04, DEL-01-06, DEL-02-02, DEL-02-03, DEL-02-06, DEL-03-02, DEL-03-06, DEL-04-02, DEL-04-06, DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12 |
| OBJ-003 | OBJ-3 | The human evaluation and iteration loops close — linkage complete universally, retrievable within a pre-registered bound on a pre-registered sample. | DEL-01-04, DEL-04-01, DEL-04-03, DEL-04-04, DEL-04-05, DEL-04-08, DEL-04-10, DEL-05-02, DEL-05-03, DEL-05-04, DEL-05-05, DEL-05-07, DEL-05-08, DEL-06-03, DEL-04-11 |
| OBJ-004 | OBJ-4 | Safe self-application without self-authorization — F1–F3 unobserved, capabilities accepted before consumption, guards registered and passing. | DEL-02-04, DEL-02-06, DEL-03-01, DEL-03-04, DEL-03-05, DEL-03-06, DEL-05-06, DEL-06-01, DEL-06-04, DEL-06-07, DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12 |
| OBJ-005 | OBJ-5 | Situated specialization with governed convergence — one candidate reaches a complete promotion disposition; variant-derived changes used the governed path. | DEL-06-04, DEL-06-05, DEL-06-06, DEL-06-08 |
| OBJ-006 | OBJ-6 | Coordination remains intelligible as concurrent activity grows — ownership, dependencies, and gates reconstructible; stale runs detectable. | DEL-03-03, DEL-05-01, DEL-06-02 |
| OBJ-007 | OBJ-7 | File-native continuity and recoverability — nothing load-bearing lives outside the checkout. | DEL-01-05, DEL-02-06, DEL-03-01, DEL-02-07, DEL-02-08, DEL-02-09, DEL-02-10, DEL-02-11, DEL-02-12 |

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
| PKG-02_Operative_Instruction_Surface_and_Runtime_Layers | Operative Instruction Surface and Runtime Layers | The instruction surface and the three operative layers that do work: membership and release management, deterministic-tool and runtime-substrate boundaries, the delegation hierarchy and entry rules, declared write scope and capability-boundary controls, live registry discipline, and continuing stewardship and release assurance for the Root-owned generic runtime. | Execution-state structures, path anchoring, and containment guards (PKG-03); decision and change machinery (PKG-04). |
| PKG-03_Governed_Execution_Structure_and_Root_Containment | Governed Execution Structure and Root Containment | The path model and containment rule, execution-instance structure and lifecycle, dependency registers, the single governed root working-root exception with its M1–M7 mechanisms and G0–G4 guards, guard-state instantiation, and materialization readiness behind the §5.3 gate. | Agent-surface write-scope declarations (PKG-02); the concurrency-legibility demonstration (PKG-06); evidence artifacts produced by execution (PKG-05). |
| PKG-04_Developmental_Machinery_and_Change_Control | Developmental Machinery and Change Control | The governance harness by which the product changes itself: decision records and terminal-artifact discipline, identity attribution, validation severity, governance integration rules and routed notices, the governed loop and receipts, human-gated closeout, the export boundary, PRD amendment and attributable change control, the source-currency check, and decomposition-pipeline discipline with root coverage demonstration. | The normative content being changed (PKG-01); the operative surfaces being changed (PKG-02); evidence schemas and warrant machinery (PKG-05). |
| PKG-05_Evidence_Provenance_and_Audit | Evidence, Provenance, and Audit | The record that makes reliance answerable: run-record trees, snapshot / handoff / receipt discipline, distinct SHA roles, claim provenance and the warrant lifecycle, read-only audit and evaluation surfaces, validation-evidence mutation control, closure criteria, and evidence-linkage completeness with its retrieval evaluation. | The acts the evidence records (PKG-04); the execution structures the evidence describes (PKG-03). |
| PKG-06_Self_Application_Variants_and_Release | Self-Application, Variants, and Release | The product's reciprocal relations to itself and to situated working roots: self-application discipline and falsifier observation, concurrency legibility, the approval-vehicle practice record, downward variant service without weakening, the domain-engine truth boundary, the upward governed-promotion pathway, the release-authority gate, and situated-working-root convergence. | Guard and mechanism state surfaces themselves (PKG-03); the promotion machinery's record classes (PKG-04). |

**Why six and not four.** §4.3 forbids reading the four categories as a
partition, and §11.2 shows the result: every category spans four or more of
these packages, and no package is coextensive with any category —
participation ranges from two categories (PKG-02) to all four (PKG-01,
PKG-04, PKG-06). The partition is a work-domain judgment accepted at Gate 4
(DEC-003).

---

## 9. Deliverables

53 deliverables, each belonging to exactly one package, each sized for a
bounded Agent 2 execution. `ResponsibleParty` is `Ryan Tufts` for every
deliverable: D-GOV-27 assigned the original 45, SCA-001 carried that
assignment to DEL-02-06, and the seven SCA-004 candidate rows carry the
same assignment. OI-011 therefore remains closed for all 53 deliverables. Descriptions, anticipated
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
| DEL-01-04_Human_Authority_and_Three_Judgment_Gate_Model | Human Authority and Three-Judgment Gate Model | REQ_SLICE | M | execution-tree | OBJ-002, OBJ-003 |
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
| DEL-02-06_Generic_Runtime_Stewardship_and_Release_Assurance | Generic Runtime Stewardship and Release Assurance | REQ_SLICE | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/**; client implementation only through separately authorized client-owned tranches | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |
| DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control | Process Supervisor and Purpose-Limited Control | BACKEND_FEATURE_SLICE | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-07_Process_Supervisor_and_Purpose_Limited_Control/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |
| DEL-02-08_Exact_Supply_and_Protocol_Pinning | Exact Supply and Protocol Pinning | API_CONTRACT | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-08_Exact_Supply_and_Protocol_Pinning/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |
| DEL-02-09_Hosted_Account_and_Consent_Boundary | Hosted Account and Consent Boundary | SECURITY_CONTROL | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-09_Hosted_Account_and_Consent_Boundary/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |
| DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2 | Adapter Event Schema and Approval API v2 | API_CONTRACT | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-10_Adapter_Event_Schema_and_Approval_API_v2/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |
| DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation | Worker Retirement, Restart, and Terminal Reconciliation | BACKEND_FEATURE_SLICE | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-11_Worker_Retirement_Restart_and_Terminal_Reconciliation/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |
| DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in | Runtime Conformance Evidence and Shared-Release Fan-in | TEST_SUITE | M | runtime/**; execution/PKG-02_Operative_Instruction_Surface_and_Runtime_Layers/1_Working/DEL-02-12_Runtime_Conformance_Evidence_and_Shared_Release_Fan_in/** | OBJ-001, OBJ-002, OBJ-004, OBJ-007 |

### PKG-03_Governed_Execution_Structure_and_Root_Containment

| DeliverableID | Name | Type | ContextEnvelope | AnticipatedWriteLocus | SupportsObjectives |
|---|---|---|---|---|---|
| DEL-03-01_Path_Model_and_ScopePath_Containment_Conformance | Path Model and ScopePath Containment Conformance | SECURITY_CONTROL | M | execution-tree; tools/ (M2) if a check must change | OBJ-004, OBJ-007 |
| DEL-03-02_Execution_Structure_and_Lifecycle_Conformance | Execution Structure and Lifecycle Conformance | REQ_SLICE | M | execution-tree | OBJ-002 |
| DEL-03-03_Dependency_Register_and_Derived_Graph_Boundary | Dependency Register and Derived-Graph Boundary | REQ_SLICE | S | execution-tree | OBJ-006 |
| DEL-03-04_Root_Working_Root_Exception_Conformance | Root Working-Root Exception Conformance | REQ_SLICE | M | execution-tree | OBJ-004 |
| DEL-03-05_Guard_State_Instantiation_and_Registration | Guard State Instantiation and Registration | DATA_MODEL_CHANGE | M | execution/_harness (root Project Setup; authorized separately) | OBJ-004 |
| DEL-03-06_Root_Materialization_Readiness_and_Deliverable_Stream | Root Materialization Readiness and First Deliverable Stream | REQ_SLICE | M | execution-tree (gated) | OBJ-002, OBJ-004 |

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
| DEL-04-11_Root_Loop_Receipt_Validator | Root Loop Receipt Validator | TEST_SUITE | M | tools/** (M2); execution/PKG-04_Developmental_Machinery_and_Change_Control/1_Working/DEL-04-11_Root_Loop_Receipt_Validator/** | OBJ-003 |

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
| DEL-06-04_Downward_Variant_Service_and_Non_Weakening | Downward Variant Service and Non-Weakening | REQ_SLICE | M | execution-tree | OBJ-004, OBJ-005 |
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

- **Every scope item carries exactly one `PackageID`** (hard rule; 104/104).
- **Every IN-scope item maps to at least one deliverable** (95/95); mappings
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
| ScopeItemCount | 104 (IN 95 / OUT 9 / TBD 0) |
| PackageCount | 6 |
| DeliverableCount | 53 |
| ObjectiveCount | 7 |
| **UnassignedScopeItems** | **0** |
| ScopeItemsWithoutDeliverableMapping | 0 |
| UnmappedObjectives | 0 |
| ContextEnvelopeCounts | S=14, M=38, L=1, XL=0 |
| OpenIssuesByType | SOURCE_CURRENCY=2, FRAMING_STRAIN=3, UNBUILT_CAPABILITY=1, OWNER_RULING_PENDING=1, PARTITION_BOUNDARY=1, GATE_SEQUENCING=1, SCOPE_TBD=1, CONTEXT_ENVELOPE=1, RESPONSIBILITY_UNASSIGNED=1, OBJECTIVE_GRANULARITY=1 (total 13: 10 closed, 3 carried open) |
| Revision / Date | v1.3 SCA-004 candidate / 2026-08-23 |

### 11.1 Context Budget QA

No `XL` deliverable is proposed. One `L` deliverable —
`DEL-04-09_PRD_Source_Currency_Check_Capability` — was accepted as
large-but-single-domain under D-GOV-25 and retains its envelope notes; it is splittable by check class if implementation review finds
churn (OI-010). Every other deliverable is `S`
or `M`, single-package, and focused on one primary artifact shape. The seven
SCA-004 additions are `M`; each remains a single PKG-02 or PKG-04 slice.

### 11.2 D-15 — four-category coverage demonstration

Each §4.1 category has decomposition coverage. **No category is deferred, so
no reasoned deferral is recorded.**

| §4.1 category | Scope items | Packages participating | Deliverables | Status |
|---|---:|---|---:|---|
| Normative basis | 41 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-05, PKG-06 | 21 | COVERED |
| Operative product | 27 | PKG-01, PKG-02, PKG-03, PKG-04, PKG-06 | 25 | COVERED |
| Developmental machinery | 59 | PKG-01, PKG-03, PKG-04, PKG-05, PKG-06 | 26 | COVERED |
| Evidence | 19 | PKG-01, PKG-02, PKG-04, PKG-05, PKG-06 | 24 | COVERED |

The spread is the point: the categories are non-exclusive functions, and the
partition is not derived from them (§4.3, DEC-003). D-12 is honoured directly
— developmental machinery is decomposed as product scope (PKG-04, 11
deliverables), not exempted as overhead.

### 11.3 F4 — bidirectional traceability

| Direction | Register | Population | Result |
|---|---|---:|---|
| PRD item → decomposition | `chirality_root_prd_coverage_forward_v1_0.csv` | 85 | 84 COVERED, 1 COVERED_WITH_RECORDED_DEFERRAL (OBJ-2), 0 UNCOVERED |
| decomposition unit → PRD | `chirality_root_trace_reverse_v1_0.csv` | 59 | 59 TRACED, 0 UNTRACED |

The forward population is every addressable PRD item in the enumerated scope
source: OBJ-1..OBJ-7; N-1..N-9; O-1..O-11; D-1, D-2, D-4..D-16; E-1..E-8; the
§3 v1 boundary and objective discipline; the §4 category, loop, judgment, and
non-prescription statements; §5 registry discipline; the four §6 directions;
the two §7 directions; §8.1 non-goals; F1..F6; §8.3 release authority;
RD-1..RD-5; §9.1 obligations (a), (b), (c); the §10.1 annex obligation;
C-1..C-4; and §10.3 adoption mechanics. `D-3` is deliberately absent and never
reassigned.

**F4 at the accepted basis.** The units are now accepted (D-GOV-25), so F4
applies in full — and is **not tripped**: every accepted package and
deliverable traces back, and every PRD requirement and objective has coverage
or, in the single case of OBJ-2's situated-working-root clause, an
owner-ruled **recorded deferral** (§12.1, OI-013). F4 distinguishes a recorded
deferral from a silent gap; this is the former, and it is machine-visible in
the forward register's `CoverageStatus`/`DeferralReason`.

---

## 12. Open Issues

**Status after the D-GOV-25 ruling: 9 closed, 4 carried open.** Acceptance did
not close every issue, and the four that remain open are part of what was
accepted. Closure states are `CLOSED_*` where the ruling or a ruled gate
satisfied the issue's own stated resolution condition, and `OPEN` where it did
not. Every closure cites its basis; none is inferred from acceptance in
general.

| IssueID | Status | Type | Affected | Description | Disposition |
|---|---|---|---|---|---|
| OI-001 | `CLOSED_CONFIRMED` — owner decision 2, D-GOV-25 | SOURCE_CURRENCY | SOW-060, SOW-089, SOW-090, SOW-091, SOW-098, SOW-099, SOW-100, SOW-101 | Several PRD statements describe the repository as it stood at the PRD's own `SourceCorpusBasis`, and accepted acts recorded in the governance register at the current basis appear to have discharged them — the §9.1 concordance obligations and the §10.2 conflicts. This decomposition **does not adjudicate that**: it derives the scope items from the source as written and sets their coverage to standing verification and maintenance rather than re-performance. | **Ruled (owner decision 2, D-GOV-25).** The standing-verification-and-maintenance reading stands; the currency finding is recorded as ruled on rather than left outstanding. The adopted PRD bytes remain untouched (D-13) — the ruling disposes of the finding, it does not amend the source. |
| OI-002 | `CLOSED_CONFIRMED` — owner decision 2, D-GOV-25 | SOURCE_CURRENCY | SOW-085, SOW-102, and every PROPOSED-labelled row | The adopted bytes state that PROPOSED items are inert until the adoption instrument's ruling, while the governance register records that the ruling occurred and the PROPOSED items take effect. The ledger therefore carries **the source label** plus a note, and claims no label change. | **Ruled (owner decision 2, D-GOV-25) — labels updated as warranted, by annotation.** The registers keep the PRD's own source label and gain the effect annotation "in effect per the D-GOV-22 adoption ruling; confirmed at the D-GOV-25 ruling". **No source label was overwritten**: F6 discipline is that a label does not change without an instrument, so the instrument is cited alongside the label rather than replacing it. |
| OI-003 | `CLOSED_ACCEPTED_AS_STAGED` — owner decision 3, D-GOV-25 | FRAMING_STRAIN | whole package | `SOFTWARE_DECOMP`'s intake framing is a software development SOW. The root product's scope is predominantly normative corpus, governance machinery, and evidence; "artifacts" are largely governance records, registers, and validators rather than code. The standard was conformed to rather than adapted, and the strain is recorded here rather than silently smoothed. | **Ruled (owner decision 3, D-GOV-25) — accepted as staged.** `SOFTWARE_DECOMP` remains the conforming variant for this decomposition; no root-specific variant is directed. **The strain stays on record** rather than being retired by acceptance: it is the reason a future revision might revisit the manager choice, and deleting it would erase the reasoning behind an accepted structure. |
| OI-004 | `CLOSED_ACCEPTED_AS_STAGED` — owner decision 3, D-GOV-25 | FRAMING_STRAIN | 33 TRANSCRIBED and 5 CLARIFIED commitments | A commitment already in force generates **conformance and verification** work, not construction. Deliverables against such commitments are written as conformance slices; that is a defensible reading of N-9 ("the running system continues to satisfy the invariants") but it makes many deliverables recurring controls rather than one-shot productions. | **Ruled (owner decision 3, D-GOV-25) — accepted as staged.** Standing conformance stays inside the package/deliverable lifecycle as decomposed; no separate standing-controls surface is directed. **The strain stays on record**: it is the largest judgment call in the package and remains the live reason a later revision might move recurring controls elsewhere. |
| OI-005 | `OPEN` — not ruled on; carried forward | UNBUILT_CAPABILITY | SOW-049, DEL-04-09 | D-14's source-currency check is not built — no generator, schema, or executable check exists — and four of its nine classes require semantic judgment. Reliance on D-14 before the build is unwarranted. | Unchanged and **carried into the accepted basis**: build through DEL-04-09, or record an explicit deferral. Until then, currency findings are produced by human reading, as OI-001 was. Acceptance of the decomposition is not the building of the check. |
| OI-006 | `CLOSED_BY_RULING` — D-GOV-25, all seven gates | OWNER_RULING_PENDING | all seven gates | Recorded while the package was a candidate: nothing was accepted and every gate was staged pending the owner's ruling. | **Closed by the fact it asked for.** All seven gates are ruled ACCEPTED (§1) by the owner against AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`. The issue is retained rather than deleted so the candidate posture stays legible in the record. |
| OI-007 | `CLOSED_CONFIRMED_AT_GATE_4` — D-GOV-25 | PARTITION_BOUNDARY | SOW-065, SOW-066 vs SOW-034 | The §6.3 concurrency mechanisms are implemented as state surfaces owned by PKG-03 but demonstrated for legibility by PKG-06. The scope items are split so each lands in exactly one package, with the relation recorded at DEC-008. | **Closed by the Gate 4 acceptance, which is exactly the confirmation this issue asked for.** The PKG-03 / PKG-06 ownership split is the accepted boundary. |
| OI-008 | `OPEN_STANDING` — reaffirmed, not closed | GATE_SEQUENCING | SOW-001, SOW-061, SOW-103, DEL-03-06 | Materialization of root packages sits behind the D-GOV-21 §5.3 gate, and this decomposition authorizes none of it. DEL-03-06 is readiness and evidence only. | **Reaffirmed by the ruling, not discharged by it.** Acceptance of the decomposition is a precondition of materialization, never the authorization for it; step 9 remains behind the §5.3 gate. This issue stays standing for as long as that gate does. |
| OI-009 | `OPEN` — not ruled on; carried forward | SCOPE_TBD | SOW-094 | The referent of the database-backed attribution interface named in the RD-2 evolution path is `TBD` in the source. It is carried as an OUT boundary item without being resolved (I2). | Unchanged: the owner fixes the referent if and when that scope is opened. Acceptance did not resolve it and did not need to — the item is OUT. |
| OI-010 | `CLOSED_ACCEPTED_AT_GATE_5` — D-GOV-25 | CONTEXT_ENVELOPE | DEL-04-09 | One `L` deliverable was proposed: a checker plus a regenerable derivative package. It is single-domain but multi-component. | **Closed by the Gate 5 acceptance**, which took the deliverable as proposed. `DEL-04-09` stands at `L` with its envelope notes; no split was directed. A split by check class remains available at revision if implementation review finds churn. |
| OI-011 | `CLOSED_ASSIGNED_BY_D-GOV-27` | RESPONSIBILITY_UNASSIGNED | all 53 deliverables | `ResponsibleParty` is assigned to Ryan Tufts across the original 45, SCA-001 DEL-02-06, and the seven SCA-004 candidate rows. | D-GOV-27 assigned the original 45 deliverables; SCA-001 carried the assignment to DEL-02-06; SCA-004 carries the same assignment to its seven new rows, preserving complete assignment coverage across all 53 deliverables. |
| OI-012 | `CLOSED_CONFIRMED_AT_GATE_4` — D-GOV-25 | FRAMING_STRAIN | 9 OUT items | REF-002 permits a blank partition for OUT units; REF-003 requires every scope item to carry exactly one `PackageID`. The stricter rule was applied (no weakening of the base) and the divergence is surfaced rather than reconciled. | **Closed by the Gate 4 acceptance**, which took the ledger with every OUT item assigned. The instruction-file divergence stays surfaced; no change to either instruction file was proposed or directed. |
| OI-013 | `CLOSED_DEFERRED_BY_RULING` — owner decision 1, D-GOV-25 | OBJECTIVE_GRANULARITY | OBJ-002 (PRD OBJ-2) | PRD §3 OBJ-2's success condition ends "Demonstrated at root and in at least one situated working root." No deliverable covers the situated-working-root half: `DEL-03-06` carries the deliverable stream **at root only**, and `DEL-06-08` — the one situated-root deliverable — is mapped to OBJ-005, covers only SOW-003, and concerns a *recorded convergence path* (v1 boundary (c)) rather than a deliverable stream reaching an issuance decision in a variant. F4 is not formally tripped, because objectives are traced as whole units and OBJ-2 has coverage at objective granularity; the gap is inside the objective, where the registers cannot see it. Raised by the adversarial verification of this candidate (V1, MAJOR-1). | **Ruled: reasoned deferral (owner decision 1, D-GOV-25).** See §12.1 for the recorded deferral and its rationale. The forward register's OBJ-2 row now reads `COVERED_WITH_RECORDED_DEFERRAL`, so F4 is satisfied by a **recorded deferral** rather than by a silent gap — which is the distinction F4 draws. No scope item and no deliverable was added. |

### 12.1 Recorded deferral — OBJ-2's situated-working-root demonstration

**Ruled by the owner, 2026-07-25, decision 1 of the ruling recorded verbatim in
`docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md`,
against AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`.**

**What is deferred.** The situated-working-root half of PRD §3 OBJ-2's success
condition — "demonstrated at root **and in at least one situated working
root**". The root half is not deferred and is carried by
`DEL-03-06_Root_Materialization_Readiness_and_Deliverable_Stream`.

**Deferred to.** The stage at which a situated working root runs its own
deliverable stream to an issuance decision.

**Rationale (three reasons, recorded so a later reader can test them):**

1. **Sequence.** The v1 root demonstration proceeds first, through
   `DEL-03-06`. A situated-root demonstration that preceded it would have
   nothing to converge on.
2. **Cadence is not root's to set.** A situated-root demonstration depends on a
   variant loop's own cadence and instruments. PRD §7.1 has one instruction
   root serving many working roots without per-workspace drift; root cannot
   schedule a variant's deliverable stream without reaching into a working root
   it does not own.
3. **F4 discipline.** Recording the deferral now keeps F4 satisfied by an
   explicit **recorded deferral** rather than by a silent gap. F4 is tripped by
   a requirement or objective that has *neither* coverage nor a recorded
   deferral; this clause now has one, and it is visible in the forward register
   rather than only in prose.

**What this deferral is not.** It is not a claim that the clause is satisfied,
and it is not a removal of the clause from OBJ-2. OBJ-2 remains partly
undemonstrated until the deferred stage runs, and the accepted basis says so.

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

**Ruling-application entries.** DEC-014..DEC-020 record the owner's ruled
dispositions as applied in the publication tranche. Each cites the verbatim
ruling in
`docs/governance_harness/_DECISIONS/D-GOV-25_root_decomposition_acceptance.md`,
against AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`
(EffectiveSHA `ea0ad7a566ddb51d89297bfcf491636f1fc5dd15`). **None of them
changes scope**: no scope item, package, deliverable, objective, or identifier
was added, removed, or renumbered.

| DecisionRef | Date | Decision | Rationale |
|---|---|---|---|
| DEC-014 | 2026-07-25 | All seven Gate Log rows move from the candidate-era pending status to `ACCEPTED`, and the status banner moves from candidate posture to accepted basis, each citing the owner ruling of 2026-07-25, D-GOV-25, and the AcceptedCandidateSHA. | The owner ruled, by merge-and-proceed direction against the exact candidate SHA, with the ruling recorded verbatim in D-GOV-25 and bound to that SHA (K-AUTH-2). The verbatim ruling is not restated here; this file points to the instrument that carries it (D-1: the decision record governs, the pointer is navigational). |
| DEC-015 | 2026-07-25 | OI-013 is closed `CLOSED_DEFERRED_BY_RULING`: the situated-working-root half of OBJ-2's success condition is deferred, with the reasoned deferral recorded at §12.1 and the forward register's OBJ-2 row set to `COVERED_WITH_RECORDED_DEFERRAL`. | Owner decision 1. F4 distinguishes a recorded deferral from a silent gap; recording it in the register schema — which already carries `CoverageStatus` and `DeferralReason` — makes the deferral machine-visible instead of prose-only. No scope item or deliverable was added, because the ruling chose deferral over coverage. |
| DEC-016 | 2026-07-25 | OI-001 is closed `CLOSED_CONFIRMED`: the standing-verification-and-maintenance reading of the discharged §9.1 obligations and C-1..C-4 stands, and the currency finding is recorded as ruled on. | Owner decision 2. The finding was raised as a D-14-class REVIEW finding routed to the owner; a ruling is the disposition that closes it. The adopted PRD bytes remain untouched (D-13) — closure disposes of the finding, it does not amend the source. |
| DEC-017 | 2026-07-25 | OI-002 is closed `CLOSED_CONFIRMED` by **annotation, not overwrite**: rows carrying the PRD's PROPOSED source label gain the effect annotation "in effect per the D-GOV-22 adoption ruling; confirmed at the D-GOV-25 ruling", while the source-label field keeps the PRD's own label. | Owner decision 2 ("update the labels as warranted"). F6 is tripped by a provenance label that changes without a superseding instrument; citing the instrument beside the label satisfies the ruling without performing the act F6 forbids. The annotation is additive and reversible; overwriting would not have been. |
| DEC-018 | 2026-07-25 | OI-003 and OI-004 are closed `CLOSED_ACCEPTED_AS_STAGED`, and both strains remain on record. | Owner decision 3. Acceptance settles that the staged framing is the accepted one; it does not make the strain untrue. Deleting the strains would erase the reasoning behind an accepted structure and hide the live reasons a later revision might revisit the manager choice or move standing conformance elsewhere. |
| DEC-019 | 2026-07-25 | OI-006, OI-007, OI-010, and OI-012 are closed on the ruled gates that satisfied their own stated resolution conditions (all seven gates; Gate 4; Gate 5; Gate 4). OI-005, OI-008, OI-009, and OI-011 remain open and are carried into the accepted basis. | Each closed issue named a specific gate confirmation as its resolution, and that gate is now ruled; each open issue asked for something the ruling did not do. Closure is claimed per-issue against its own condition, never inferred from acceptance in general. OI-008 in particular is *reaffirmed* by acceptance rather than discharged by it: materialization stays behind the D-GOV-21 §5.3 gate. |
| DEC-020 | 2026-07-25 | The filename stays `Chirality_Root_SOFTWARE_DECOMP_v1_0.md` and no revision number is bumped. The acceptance binds the content at AcceptedCandidateSHA `ec62af0700e530c1640698fa406398cb1cb45d29`; the edits in DEC-014..DEC-019 are **the ruled dispositions applied in the publication tranche**, not new decomposition content. | Bumping the revision would imply the accepted content changed. It did not: scope, partition, deliverables, objectives, identifiers, and every count are byte-equivalent in substance to the accepted candidate, and the diff is confined to gate status, ruled dispositions, and cited annotations. Decision IDs continue from DEC-013 rather than restarting at DEC-012, because I5 forbids reusing an assigned identifier. |

| DEC-021 | 2026-07-25 | **Additive objective propagation, ruled by D-GOV-27.** The four ledger/register objective divergences surfaced at initialization fan-in (Receipt 51) are resolved additively: the ledger's item-level mappings stand (SOW-010→OBJ-003; SOW-020, SOW-001, SOW-061, SOW-069→OBJ-004), and the deliverable register's `SupportsObjectives` aggregates gain the missing objective (DEL-01-04 +OBJ-003; DEL-03-01, DEL-03-06, DEL-06-04 +OBJ-004), with the objective register's `MappedDeliverables`, the forward register's `DeliverableIDs` (OBJ-3, OBJ-4), and this surface's two tables updated to match. The telemetry restates no per-objective mapping, so no regeneration was required. | The companion registers are the amendment surface; every item-level mapping was ruled correct on the merits, so the deliverable-level aggregates were incomplete, not wrong — the amendment adds coverage (three of four additions are OBJ-004 safety coverage) and removes none. No scope item, deliverable, or identifier changed. Record: `docs/governance_harness/_DECISIONS/D-GOV-27_initialization_closing_rulings.md`. |

| DEC-022 | 2026-07-26 | **SCA-001 adds one standing Root runtime-stewardship carrier.** Add SOW-104 and DEL-02-06 under PKG-02; preserve DEL-02-02 unchanged; map the carrier to OBJ-001, OBJ-002, OBJ-004, and OBJ-007; classify the scope item as Operative Product and Evidence; use REQ_SLICE with Context Envelope M; and declare `runtime/**` plus the carrier's execution/evidence tree as its anticipated Root write locus. | O-11 requires a standing Root carrier and declared locus. A separate deliverable preserves the accepted distinction between three-layer boundary conformance and consequential runtime stewardship. The carrier is activated one bounded change tranche at a time and creates no implementation or release authority. Requested by Ryan Tufts and approved through SCA-001 Gates 2–3. |

| DEC-023 | 2026-07-29 | **SCA-002 restates SOW-042 and DEL-04-06 to the D-GOV-31 successor merge-gate policy.** The SOW-042 `ScopeItemStatement` and the DEL-04-06 `Description` and `AnticipatedArtifacts` cells are restated from the superseded Rev 6 D-8 wording to the adopted successor: the shared change-management role with human-gated PRs as the standing default; a bounded owner grant, recorded before or at exercise per PRD annex §5.3.1, may authorize merge execution; K-MERGE-1 and the four closeout identities (semantic approval, approved source SHA, merge authorization, effective merge SHA) are preserved; each loop's stricter local merge discipline remains controlling until adopted under its own instruments. The SOW-042 `SourceRef` bracket retains its historical `[TRANSCRIBED]` label per the drafting brief; the live D-8 row is labeled PROPOSED (Rev 7), and the label disposition is surfaced to the owner in the SCA-002 snapshot rather than changed here (F6 discipline). No ID, status, mapping, count, or other cell changes. | D-GOV-31 adopted PRD Revision 7 (subject SHA-256 `15fba9c36a197b36b281297af123115bcd3f282fe6c6f2fae05cd703b3743748`; effective merge `ea3db3607fbcbb7ce5f65bab31268a7eca431adb`); its POLICY_DELTA §4 row 1 obligates this restatement through SCOPE_CHANGE. Candidate only: these bytes take effect only upon the SCA-002 owner gate confirmations. Owner acceptance is pending and is a separate act. |

| DEC-024 | 2026-08-02 | **SCA-003 basis reconciliation aligns current-facing acceptance and source-control metadata without changing decomposition truth.** The title, header, status block, REF-001 pin, and downstream acceptance notes are reconciled to the already-recorded facts that SCA-002 revision 1.2 was accepted/applied and that Receipt 64 produced Root PRD Revision 8. DEC-023 and the original SCA-002 candidate Change Log entry remain unchanged as time-scoped proposal history. | SCA-002 `Decision_Log.md`, `Handoff_State.md`, `Applied_File_Hashes.json`, `_ScopeChange/_LATEST.md`, Receipt 63, Receipt 64, and the Root loop handoff agree on the current state. This is metadata-only: no scope item, package, deliverable, objective, ID, mapping, status row, count, topology, or substantive requirement changes. The exact SCA-003 candidate was accepted and applied under owner ruling SHA-256 `12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129`, with applied-file evidence SHA-256 `f2781dd2c33f01cbaf014b2bb97fbff0bcdf1db3c46a8969f195a7d320501cc8`; human confirmation status is recorded only in `execution/_ScopeChange/SCA-003_2026-08-02_2212/Decision_Log.md`. |

| DEC-025 | 2026-08-23 | **SCA-004 Gate-3 candidate narrows the standing runtime carrier and adds seven bounded leaf carriers.** Preserve DEL-02-06 and SOW-104 with OBJ-001/002/004/007 continuity; allocate implementation and conformance slices to DEL-02-07 through DEL-02-12 under PKG-02; add DEL-04-11 under PKG-04 as a TEST_SUITE mapped to SOW-041, SOW-053, and OBJ-003; retain every existing ID, package, scope item, objective, REQ-027 boundary, and ten-binding hold. | R2-A accepted Gate 2 drafting only. The split preserves package discipline and artifact-kind granularity, keeps all runtime work in PKG-02, separates executable receipt validation from DOC_UPDATE DEL-04-05, and creates no live authority until exact Gate-3 and Gate-4 approvals plus later Gate-5 application. |

### Change Log

- 2026-07-25 — v1.0 candidate authored from `docs/PRD_ROOT.md` at basis
  `24726a73c64a849909e3615c32ef1a888b3dfd36` under run
  `ROOT-STEP8-DECOMP-20260725`. First root decomposition; no prior revision
  exists, so no renumbering question arises. All gates staged pending the
  owner's ruling.
- 2026-07-25 — fan-in corrections applied after independent adversarial
  verification (node V1): one false quantitative claim about category
  participation corrected in §8 and the telemetry, the §6 section tally
  reconciled to the ledger, and OI-013 opened to carry the OBJ-2
  situated-working-root gap to the gate unresolved. Committed as the candidate
  at `ec62af0700e530c1640698fa406398cb1cb45d29`.
- 2026-07-25 — **owner ruling applied (publication tranche).** All seven gates
  ACCEPTED per D-GOV-25 against that candidate SHA; OI-013 closed by reasoned
  deferral (§12.1); OI-001 and OI-002 confirmed, with PROPOSED source labels
  annotated rather than overwritten; OI-003 and OI-004 accepted as staged with
  the strains retained; OI-006, OI-007, OI-010, OI-012 closed on their ruled
  gates; OI-005, OI-008, OI-009, OI-011 carried open. **No scope, partition,
  deliverable, objective, or identifier changed** (DEC-014..DEC-020).
- 2026-07-25 — **D-GOV-27 additive objective propagation applied (DEC-021).**
  Four deliverable-register `SupportsObjectives` aggregates gained the
  objective their covered ledger items already carried; the objective and
  forward registers and this surface's tables updated to match. The scope
  ledger is untouched; no scope item, deliverable, or identifier changed.
  In the same tranche, `ResponsibleParty` was assigned (`Ryan Tufts`, owner
  ruling of the initialization phase plan) across the deliverable register
  and all 45 `_CONTEXT.md` files.

- 2026-07-26 — **SCA-001 revision 1.1 successor.** D-GOV-28 advanced the sole
  scope source to Root PRD Revision 6 and adopted O-11. The amendment adds
  SOW-104 and DEL-02-06 under PKG-02, maps OBJ-001/2/4/7, adds the bounded
  `runtime/**` planning locus, and reconciles both trace registers and telemetry.
  DEL-02-02 and every existing stable ID remain unchanged. These bytes become
  current basis only upon the SCA-001 Gate 5 owner confirmation.

- 2026-07-29 — **SCA-002 revision 1.2 candidate.** D-GOV-31 adopted PRD
  Revision 7: the D-8 successor row and merge-gate policy annex §5.3.1
  (shared change-management role; human-gated PRs as the standing default;
  bounded owner grants recorded before or at exercise; K-MERGE-1 and the
  four closeout identities preserved). This candidate restates SOW-042
  (scope ledger) and DEL-04-06 (deliverable register) to the successor
  policy and advances the sole-scope-source pin to Revision 7 at the
  D-GOV-31 effective merge (DEC-023). No topology, ID, status, mapping,
  or count changes; no grant is issued; frozen records are untouched.
  These bytes become the current basis only upon the SCA-002 owner gate
  confirmations; revision 1.1 remains the accepted basis until then.

- 2026-08-02 — **SCA-003 current-facing basis-reconciliation candidate.**
  The immutable SCA-002 candidate entry above is retained as proposal
  history. Current control metadata is aligned to the later recorded facts:
  SCA-002 was accepted and applied (Receipt 63; PR #417), Receipt 64 produced
  PRD Revision 8 and reconciled the two companion rows, and revision 1.2 is
  the accepted current decomposition. REF-001 pins the exact paired PRD
  candidate SHA-256. No scope, topology, mapping, count, lifecycle, or
  substantive requirement changes. Exact SCA-003 candidate acceptance and
  application are recorded by owner ruling SHA-256
  `12f7c46e86ca19c1e065e96b05e09814b9806cd5b0742f74d8cce405ef389129`
  and applied-file evidence SHA-256
  `f2781dd2c33f01cbaf014b2bb97fbff0bcdf1db3c46a8969f195a7d320501cc8`;
  human confirmation status is recorded only in
  `execution/_ScopeChange/SCA-003_2026-08-02_2212/Decision_Log.md`.

- 2026-08-23 — **SCA-004 revision 1.3 Gate-3 candidate.** Against the
  accepted revision 1.2 bytes, preserve DEL-02-06 as the standing
  semantic-integration and release-assurance carrier, add six bounded
  PKG-02 runtime carriers and one PKG-04 Root receipt-validator carrier,
  and recompute all companion mappings and telemetry. R2-A authorizes
  drafting only; owner Gate-3 and Gate-4 approvals and a later Gate-5
  application remain required. No folder, SOW, lifecycle, dependency,
  pointer, implementation, App truth, or held binding changes.

---

## 14. Downstream Execution Notes

- **Gate 7 is ruled and revision 1.2 is the accepted current basis.** D-9
  remains non-waivable: packages and deliverables come only from an accepted
  decomposition, and every downstream activation remains separately gated by
  its owning instrument.
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
- **Materialization stays gated.** This amendment creates no `PKG-*` or
  `DEL-*` directory. Directory creation is step 9 behind the D-GOV-21 §5.3
  gate and is out of scope for both this run and this document.
- **Executors** should take one deliverable at a time, treat `ContextEnvelope`
  as a work-sizing constraint, preserve the D-GOV-27 `ResponsibleParty` assignment unless a human
  changes it, and read the companion register for the deliverable's full
  description, artifacts, and covered scope items.
- **Reviewers** should check: package flatness and the absence of phases;
  every scope item carrying exactly one package; both F4 registers still
  closing after any amendment; the D-15 category table regenerated rather than
  hand-edited; no XL deliverable introduced; and every acceptance claim
  matching the cited owner decision, applied hash evidence, and current
  pointer.
- **On amendment**, the companion registers are the amendment surface for
  their data and the telemetry is regenerated from them; the working surface
  is updated to match. Any single-file render assembled later is a `derived
  publication artifact` and never the amendment surface.
