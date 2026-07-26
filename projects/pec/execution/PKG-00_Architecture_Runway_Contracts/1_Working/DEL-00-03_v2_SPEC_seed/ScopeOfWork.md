---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-00-03
package_id: PKG-00
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@3623b958b
project_scope_refs: [SOW-089]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-00-03 v2 SPEC seed

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-00-03` — "v2 SPEC seed" —
in package `PKG-00` (Architecture Runway & Contracts) of the PEC v2 build. It
covers project scope item `SOW-089` and supports package objective `OBJ-001`.

`SOW-089` states: "Author the v2 SPEC from the accepted decomposition"
(`execution/_Decomposition/ScopeLedger.csv`, row `SOW-089`; `InOutStatus` `IN`,
`SourceRef` `§13`, `PackageID` `PKG-00`, `DecisionRef` `DL-12`, `OpenIssue`
`FALSE`, note: "v2 SPEC is born from the decomposition"). The same row is
mirrored at `SOFTWARE_DECOMP.md` §2.1 (IN-scope items); §6 Scope Ledger is a
pointer-only section that names `ScopeLedger.csv` as the authoritative register
and carries no rows.

The `SourceRef` resolves into `projects/pec/docs/PRD.md` §13 (Prototype
disposition), whose row for the surface "SPEC / TRACEABILITY / PILOT /
ADR-001..014" reads: "Historical baseline retained under `docs/.archive/` with
existing disclaimers; v2 SPEC is born from the decomposition; live postures
(ADR-002, ADR-014) re-cited in v2's first ADRs."

`OBJ-001` states: "Orientation for any loop is a sub-second query with per-claim
citations, not a session-length prose derivation" (`SOFTWARE_DECOMP.md` §3
Objectives, `SourceRef` §3.1; `PRD.md` §3 outcome 1).

**Objective warrant.** The `DEL-00-03` → `OBJ-001` attribution is
`SCA-002`-qualified, not register-direct, and it is qualified weakly. At
revision 1.1 the ledger row for `SOW-089` carried no objective.
`SCA-002` proposed `OBJ-001` and the Gate 3 owner ruling of 2026-07-25
accepted all seven per-row attributions as recommended, placing `DEL-00-03` in
`OBJ-001`'s mapped-deliverable set at accepted revision 1.2. The same Gate 3
record rates this specific row **LOW** confidence and calls it "the weakest in
the set", on the stated ground that the SPEC "specifies the whole product and
serves no single outcome" and that its PRD anchor "is about prototype
disposition, not any outcome"; the recommended reading — that the SPEC's primary
subject is the orientation product — is recorded as "thin but non-arbitrary",
with a full five-objective set and `OBJ-006` recorded as the considered and
unadopted alternatives. This contract records that accepted attribution at its
recorded strength. It does not restate it as a strong derivation, and nothing
below may be read as supplying one.

**Basis provenance note.** `_REFERENCES.md` still names `SOFTWARE_DECOMP.md`
"revision 1.1, accepted working surface". That phrase is superseded provenance
awaiting a deferred pointer sweep; `_CONTEXT.md` already records revision 1.1 as
"superseded by revision 1.2 (`current_basis`, SCA-002 successor)". The accepted
basis bound in this contract's frontmatter, and cited throughout, is
`SOFTWARE_DECOMP.md` **revision 1.2** at commit `3623b958b`, accepted through
`SCA-002` under `D-PEC-64`.

- **OUT-001** — The seeded v2 SPEC markdown document: the PEC v2 product specification, structured from the accepted decomposition's packages, deliverables, objectives, and scope items, published under `PKG-00`.
- **OUT-002** — The seed's per-claim traceability binding: the citation apparatus by which every specification claim in OUT-001 resolves to a `PRD.md` v2.1 requirement or invariant identifier and/or an accepted decomposition identifier, together with the explicit binding of the accepted basis revision and commit.
- **OUT-003** — The seed's declared governed-amendment provision: the statement, carried in the seed's own text, that it is seeded before P1 and amended per phase under governed updates, and of what it does not acquire between those amendments.

## Deliverable Definition — Ontology

### Identity

- **CLM-001** — `DEL-00-03` is named "v2 SPEC seed", Type `DOC_UPDATE`, Context Envelope `M`, `PhaseHint` `pre-P1`, `CoversScopeItems` `SOW-089`, `SupportsObjectives` `OBJ-001`, `ResponsibleParty` `TBD`; sources `execution/_Decomposition/Deliverables.csv` row `DEL-00-03` and `SOFTWARE_DECOMP.md` §5 table for `PKG-00`.
- **CLM-002** — The deliverable description of record is: "The v2 SPEC born from this decomposition: seeded before P1 from the accepted packages/deliverables, amended per phase under governed updates"; source `Deliverables.csv` row `DEL-00-03`, restated in `_CONTEXT.md`.
- **CLM-003** — The anticipated artifact class of record is "SPEC markdown"; source `Deliverables.csv` `AnticipatedArtifacts` for `DEL-00-03`.
- **CLM-004** — The recorded envelope justification is: "M because the seed derives structure from an accepted basis (46 requirements / 64 deliverables) rather than inventing content; grows per phase under governed updates"; source `Deliverables.csv` `ContextEnvelopeNotes` for `DEL-00-03`.
- **TBD-001** — `ResponsibleParty` is unassigned; the register records `TBD`, with assignment at WORKING_ITEMS activation and not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).
- **TBD-002** — The live on-disk path and filename for the SPEC markdown are not fixed by any accepted source. The archived baseline occupies `projects/pec/docs/.archive/SPEC.md`, and `projects/pec/docs/` currently holds only `PRD.md` and `STATUS.md`; the live path is set by this deliverable's own packet and remains unresolved here.

### Subject matter carried into the outputs

- **CLM-005** — The accepted basis this seed derives from comprises: 11 packages `PKG-00`..`PKG-10`, 64 deliverables, 6 objectives, and 94 scope items (71 `IN` / 14 out-of-scope / 9 `TBD`), per `SOFTWARE_DECOMP.md` §7 Coverage & Telemetry at revision 1.2.
- **CLM-006** — The requirement source of record is `PRD.md` v2.1 alone: "The 46 PEC-\*-NNN requirements, 11 PEC-K invariants, §3 outcomes, §11 metrics/falsification clause, §5 modes ladder, and §12 exit tests are the scope-item source. Governance instruments (workplan, fences, D-GOV/D-T0 rulings) enter as constraints, not scope; the frozen corpus enters as reference, not scope" (`SOFTWARE_DECOMP.md` §1.4 intake posture 1, confirmed at Gate 1).
- **CLM-007** — `PRD.md` §14 rules that no identifier is reused: "v2 identifiers are `PEC-K-*` (invariants) and `PEC-{ORI,RCN,GAT,PRS,STR,API,DSH,SVC}-NNN` (requirements); no family overlaps v1.0 or v0.4, so a bare ID is always unambiguous." §13 retains the archived baseline `SPEC.md`, `TRACEABILITY.md`, `PILOT.md`, and `ADR-001..014` under `projects/pec/docs/.archive/` "with existing disclaimers", and the frozen corpus is "quarried by citation", never restored.
- **CLM-008** — `SOFTWARE_DECOMP.md` §2.4 records "Authoring surfaces: ADRs and the v2 SPEC as governed product records (amended at Phase 6, DL-14)". `DL-14` also moved `DEL-00-03` from `P1` to `pre-P1` with the stated reason "PKG-00 publishes ahead of consumers".
- **CLM-009** — `PKG-00`'s recorded role is "Published specifications others consume: v2's first ADRs (incl. the OI-012 core-isolation decision), the v2 SPEC born from this decomposition, and the versioned event-contract types shared by daemon, hooks CLI, and adapters", with recorded exclusions "Implementation of any contract (consuming packages); cross-package edits — PKG-00 publishes, dependants consume" (`SOFTWARE_DECOMP.md` §4). `DL-12` states the same mechanics constraint: "PKG-00 deliverables publish artifacts that dependants consume as declared dependencies — a deliverable never writes into another package (disjoint write scopes preserved)."
- **CLM-010** — `SOFTWARE_DECOMP.md` §9 Vocabulary Map is the accepted terminology surface for this package, including the `work-domain package` entry, which disambiguates the decomposition sense of "package" from the retired product's `*-PKG-*` tokens and from v2's own record-tier `Package (entity)`.
- **CLM-011** — The owner decisions that remain open at the accepted basis are `OI-001` through `OI-009` (§16 owner rulings), `OI-012` (core isolation style, decided in `DEL-00-01`'s ADR), and `OI-013` (no durable register validator); `OI-010` and `OI-011` are resolved at Gate 2. Intake posture 3 rules that "§16 open decisions enter the SSOW as `TBD` items with open issues attached, so their eventual rulings amend the decomposition through the scope-change machinery instead of being silently pre-decided" (`SOFTWARE_DECOMP.md` §1.4, §10).

### Placement in the work graph

- **CLM-012** — `DEL-00-03` is a root node **and** a zero-edge node of the accepted dependency DAG: `_DEPENDENCIES.md` records "no upstream predecessors (root node)", `Dependencies.csv` (v3.1) carries only the two ANCHOR rows (`DEP-00-03-001` package anchor, `DEP-00-03-002` `SOW-089` requirement trace), and the accepted DAG exhibit §4.3 lists `DEL-00-03` among the nine roots and as a zero-edge node under `C-05`/`C-06`.
- **CLM-013** — `C-05` `PRE_P1_OBLIGATION` binds `DEL-00-01`, `DEL-00-03`, and `DEL-10-01`: "All three complete before any P1 node starts", from the declared text "DEL-00-03 'seeded before P1'". `C-04` `PHASE_PRECEDENCE` and `C-10` `STRATUM_RULE` are register-wide non-gating constraints; `PhaseHint` is sequencing metadata, not authority, and dependency stratum is provenance, not authority.
- **CON-001** — `C-06` `UNRESOLVED_CONSUMERS` applies to `DEL-00-03` alone: "The v2 SPEC seed has declared dependants; the accepted text names none at deliverable level", recorded as a deliberate no-edge record with consumers "resolvable at WORKING_ITEMS activation or by owner ruling". This is an unresolved question at the time of writing. This contract names no consuming deliverable and creates no consumer obligation; no consumer edge may be inferred from anything below, and nothing here resolves `C-06`.

### Lifecycle position

- **CLM-014** — The deliverable is at lifecycle state `OPEN` (`_STATUS.md`, set 2026-07-25 by PREPARATION) and no v2 SPEC has been authored. Every requirement, acceptance criterion, and verification method below states a contract that future SPEC authoring must satisfy; none asserts that any SPEC exists.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The seed shall be authored from the accepted decomposition at the basis revision and commit bound in this contract's frontmatter, deriving its structure from the accepted packages, deliverables, objectives, and scope items rather than inventing content (CLM-002, CLM-004, CLM-005).
- **REQ-002** — The seed shall specify the product using only `PRD.md` v2.1's requirement families and invariants as its requirement source, and shall introduce no new requirement, invariant, objective, package, deliverable, or scope item beyond the accepted basis (CLM-006).
- **REQ-003** — Every specification claim in the seed shall carry a resolvable citation: a `PRD.md` v2.1 requirement or invariant identifier, and/or an accepted decomposition identifier (`SOW-*`, `OBJ-*`, `PKG-*`, `DEL-*`).
- **REQ-004** — The seed shall state, in its own text, the accepted basis revision and commit it was born from, so that a later reader can determine which decomposition state it derives from without consulting an external index.
- **REQ-005** — The seed shall identify itself as the v2 SPEC and shall not restore the archived baseline `SPEC.md`, `TRACEABILITY.md`, `PILOT.md`, or `ADR-001..014` to live authority; every reference to them shall be marked historical, and no retired v1.0 or v0.4 identifier family shall be used for a v2 identifier (CLM-007).
- **REQ-006** — The seed shall record its own amendment provision: that it is seeded before P1 from the accepted basis, that it is amended per phase under governed updates, and that between governed amendments it acquires no scope of its own (CLM-002, CLM-008).
- **REQ-007** — The seed shall leave every open owner decision open. It shall decide none of `OI-001`..`OI-009`, `OI-012`, or `OI-013`, and shall carry the §16-derived `TBD` scope items as unresolved rather than pre-deciding them (CLM-011).
- **REQ-008** — The seed shall be published as SPEC markdown at the path recorded in this deliverable's packet (TBD-002); production shall write under `PKG-00` only and shall not edit any other package's scope (CLM-009).
- **REQ-009** — The seed shall be complete before any P1 node starts, and its completion shall not be made to depend on any P1 or later deliverable (CLM-013).
- **REQ-010** — The seed shall name no consuming deliverable that the accepted text does not name, and shall be publishable without a declared consumer edge (CON-001).
- **REQ-011** — The seed shall use the accepted vocabulary map's canonical terms, including the `work-domain package` disambiguation against the retired `*-PKG-*` token families and against v2's record-tier `Package (entity)` (CLM-010).
- **REQ-012** — The seed shall specify, not implement. It shall assert no implementation state and shall create no obligation that belongs to a consuming package's deliverable (CLM-009, CLM-014).

- **AC-001** — The SPEC markdown exists at the packet-recorded path, that path is recorded in this deliverable's packet before the artifact is treated as consumable, and the change set that produced it touches no path outside `PKG-00`.
- **AC-002** — Every package, deliverable, objective, and scope item named in the seed resolves to a row of the accepted registers at the bound basis; the seed introduces none that is absent from that basis, and any scoped subset of the 11 packages or 64 deliverables it carries is stated as a subset with its reason.
- **AC-003** — Every specification claim in the seed carries a citation that resolves to a `PRD.md` v2.1 requirement or invariant identifier or to an accepted decomposition identifier; a citation-resolution pass finds no unresolvable, invented, or retired-family identifier presented as live.
- **AC-004** — The seed states the accepted basis revision and commit in its own text, and that statement equals the basis bound in this contract's frontmatter or a later accepted successor named as such.
- **AC-005** — The seed contains no requirement, invariant, objective, package, deliverable, or scope item that is absent from the accepted basis, and no v1.0 or v0.4 identifier family is used for a v2 identifier.
- **AC-006** — Wherever the seed references the archived baseline `SPEC.md`, `TRACEABILITY.md`, `PILOT.md`, or `ADR-001..014`, the reference is marked historical, and none of them is cited as live authority.
- **AC-007** — The seed's own text states that it was seeded before P1 from the accepted basis, that it is amended per phase under governed updates, and what it does not acquire between amendments.
- **AC-008** — After publication, the open-issue register still shows `OI-001`..`OI-009`, `OI-012`, and `OI-013` with their pre-publication dispositions, and the §16-derived `TBD` scope items remain `TBD`.
- **AC-009** — The seed is complete before any P1 node starts, it declares no dependency on a P1 or later deliverable, and it asserts no consumer obligation on any deliverable the accepted text does not name.
- **AC-010** — Terminology in the seed conforms to the accepted vocabulary map, and every use of "package" is disambiguated in the sense §9 requires.
- **AC-011** — An accountable owner confirms that the published seed is the v2 SPEC of record born from the accepted decomposition, and confirms that the seed's single-objective attribution to `OBJ-001` remains acceptable given the recorded LOW-confidence qualification and the unadopted alternatives.

## Production and Verification Method — Praxeology

Production sequence expected of the future authoring run: read the accepted
basis at the bound revision and commit; read the `SOW-089` ledger row and its
§13 anchor; read `PRD.md` v2.1's requirement families and invariants; derive the
seed's structure from the accepted registers; attach the citation apparatus;
record the amendment provision; record the packet path; publish under `PKG-00`
only. All work is bounded to this deliverable folder and the packet-recorded
docs path; this contract authorizes no register, decomposition, or PRD edit, and
no lifecycle write. Tests and deterministic checks may implement the
verification methods below; they may never create scope, requirements, or
acceptance criteria, and none may add a criterion absent from this contract.

- **VER-001** — Document inspection of the published seed against the `SOW-089` ledger row, the `SOFTWARE_DECOMP.md` §5 `PKG-00` row, the `Deliverables.csv` description and envelope note, and REQ-001, REQ-002, REQ-006, REQ-012.
- **VER-002** — Register cross-check: enumerate every `PKG-*`, `DEL-*`, `OBJ-*`, and `SOW-*` token in the seed and resolve each against `Deliverables.csv`, `ScopeLedger.csv`, and `SOFTWARE_DECOMP.md` §3/§4/§5 at the bound basis; report every unresolved or non-register token, and report any subset of the 11 packages or 64 deliverables that is carried without a stated reason.
- **VER-003** — Citation-resolution check: every `PEC-K-*` and `PEC-{ORI,RCN,GAT,PRS,STR,API,DSH,SVC}-NNN` token in the seed resolves to a locatable requirement or invariant in `projects/pec/docs/PRD.md`, and no retired v1.0 or v0.4 identifier family appears as a live v2 identifier.
- **VER-004** — Basis-binding check: the revision and commit stated in the seed equal the basis bound in this contract's frontmatter, or a named accepted successor, verified against `SOFTWARE_DECOMP.md` front matter and the Git commit object.
- **VER-005** — Archived-baseline check: every reference in the seed to `projects/pec/docs/.archive/SPEC.md`, `TRACEABILITY.md`, `PILOT.md`, or `ADR-001..014` carries a historical marker, and none is cited as live authority.
- **VER-006** — Open-issue register cross-check before and after publication, confirming the dispositions of `OI-001`..`OI-009`, `OI-012`, and `OI-013` are unchanged and that the §16-derived `TBD` scope items are still `TBD`.
- **VER-007** — Path and write-scope check: the packet-recorded docs path exists and holds the SPEC markdown, the path is recorded in the packet, and the production change set is confined to `PKG-00`.
- **VER-008** — Vocabulary conformance inspection of the seed against `SOFTWARE_DECOMP.md` §9, with explicit attention to every occurrence of "package".
- **VER-009** — Pre-P1 obligation and consumer check: confirm the seed is complete and published before any P1 node starts, that it declares no dependency on a P1 or later deliverable, and that it names no consumer the accepted text does not name (`C-05`, `C-06`).

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-001` governs the deliverable's service: orientation for any loop is a sub-second query with per-claim citations, not a session-length prose derivation. The seed's per-claim citation discipline (OUT-002) is the document-level form of that same value; a SPEC whose claims cannot be resolved to their sources would work against the objective it is attributed to.
- **AX-002** — The `DEL-00-03` → `OBJ-001` attribution is `SCA-002`-qualified and rated LOW at the Gate 3 record, which names the alternatives — the full five-objective set, and `OBJ-006` — as considered and unadopted. This contract carries the attribution at that recorded strength. It is not evidence that the SPEC serves `OBJ-001` more than it serves the other objectives, and `AC-011` puts the qualification in front of an accountable owner rather than burying it.
- **AX-003** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.2 at commit `3623b958b`, accepted through `SCA-002` under `D-PEC-64`. The "revision 1.1" phrase in `_REFERENCES.md` is superseded provenance from a deferred pointer sweep, not a competing authority.
- **AX-004** — `DL-12` governs package mechanics: `PKG-00` publishes and dependants consume through declared dependency edges; contribution to another package is never a cross-package write. `DL-14` set `pre-P1` for the same reason — PKG-00 publishes ahead of consumers.
- **AX-005** — Open decisions stay open. Intake posture 3 requires §16 rulings to reach the decomposition through the scope-change machinery; a SPEC that settled an open issue in passing would pre-decide by prose what the governed instrument reserves to the owner.
- **AX-006** — The archived baseline is historical. Retention under `docs/.archive/` is not reauthorization, the frozen corpus is quarried by citation and never restored, and `PRD.md` §14's no-identifier-reuse rule keeps a bare identifier unambiguous.
- **AX-007** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and was untouched by the run that authored this document; the deliverable is at `OPEN` and no SPEC exists.
- **AX-008** — Unknowns remain marked. `TBD-001`, `TBD-002`, and `CON-001` are recorded rather than resolved by inference; `C-06`'s missing consumer edges are a deliberate no-edge record, and this contract's job is to fix the form the seed must take, not to supply the decisions the accepted text withholds.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-089 OBJ-001 | REQ-001, REQ-002, CLM-002, CLM-004, CLM-005 | AC-002 | VER-001, VER-002 | The published SPEC markdown and a register cross-check report resolving every PKG/DEL/OBJ/SOW token to an accepted row |
| OUT-001 | SOW-089 OBJ-001 | REQ-001, REQ-002, REQ-012, CLM-004, CLM-005, CLM-006 | AC-005 | VER-001, VER-002, VER-003 | The published SPEC markdown and a register cross-check report resolving every PKG/DEL/OBJ/SOW token to an accepted row; Citation-resolution output listing every PEC-K / PEC-family and decomposition identifier in the seed with its resolved location |
| OUT-001 | SOW-089 OBJ-001 | REQ-011, CLM-010 | AC-010 | VER-008 | A vocabulary conformance record covering every use of "package" |
| OUT-001 | SOW-089 OBJ-001 | REQ-008, CLM-009, TBD-002 | AC-001 | VER-007 | Packet-recorded docs path with the SPEC present at it and a change set confined to PKG-00 |
| OUT-001 | SOW-089 OBJ-001 | REQ-007, CLM-011 | AC-008 | VER-006 | An open-issue register diff showing no disposition movement |
| OUT-001 | SOW-089 OBJ-001 | REQ-009, REQ-010, CLM-012, CLM-013, CON-001 | AC-009 | VER-009 | A pre-P1 completion record naming no P1-or-later dependency and no unnamed consumer |
| OUT-001 | SOW-089 OBJ-001 | AX-002, CLM-014, TBD-001 | AC-011 | HUMAN_REVIEW: accountable owner confirmation that the published seed is the v2 SPEC of record born from the accepted decomposition, and that the SCA-002 LOW-confidence single-objective attribution to OBJ-001 stands | Dated owner ruling recorded against this deliverable, naming the confirmed seed and explicitly addressing the LOW-confidence objective qualification |
| OUT-002 | SOW-089 OBJ-001 | REQ-003, CLM-005, CLM-006 | AC-003 | VER-002, VER-003 | Citation-resolution output listing every PEC-K / PEC-family and decomposition identifier in the seed with its resolved location |
| OUT-002 | SOW-089 OBJ-001 | REQ-004, CLM-005 | AC-004 | VER-004 | A basis-binding check against the SOFTWARE_DECOMP.md front matter and the Git commit object |
| OUT-002 | SOW-089 OBJ-001 | REQ-005, CLM-007 | AC-006 | VER-003, VER-005 | Archived-baseline reference audit showing a historical marker on every citation into docs/.archive/ and no live-authority claim on any archived document |
| OUT-003 | SOW-089 OBJ-001 | REQ-006, CLM-003, CLM-008 | AC-007 | VER-001 | The seed's own amendment-provision text, inspected against the register description and envelope note, stating pre-P1 seeding, per-phase governed amendment, and what is not acquired between amendments |
