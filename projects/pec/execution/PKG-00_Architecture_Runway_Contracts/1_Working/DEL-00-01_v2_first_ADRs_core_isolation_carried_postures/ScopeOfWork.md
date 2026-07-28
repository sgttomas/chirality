---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-00-01
package_id: PKG-00
decomposition_basis: projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md@11a494e9a
project_scope_refs: [SOW-088]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-00-01 v2 first ADRs (core isolation + carried postures)

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-00-01` in package `PKG-00`
(Architecture Runway & Contracts). It covers project scope item `SOW-088` and
supports package objective `OBJ-005`.

`SOW-088` states: "Author v2's first ADRs: decide core isolation (OI-012);
re-cite ADR-002 as a live carried posture; cite ADR-014 as historical lineage
only while carrying forward the accepted v2 runtime/client and human-only-act
boundary" (`execution/_Decomposition/ScopeLedger.csv`, row `SOW-088`,
`SourceRef` = §13; D-PEC-67 L-A2;
mirrored at `execution/_Decomposition/SOFTWARE_DECOMP.md` §2.1 IN-scope items).

`OBJ-005` states: "Everything PEC holds can be deleted at any moment without
blocking any governed act" (`SOFTWARE_DECOMP.md` §Objectives, `SourceRef` = §3.5;
`projects/pec/docs/PRD.md` §3 outcome 5).

**Objective warrant.** The `DEL-00-01` → `OBJ-005` attribution was made by
`SCA-002` and accepted at `SOFTWARE_DECOMP.md` revision 1.2
(`session_authorization` D-PEC-64); it remains unchanged in revision 1.3, the
current successor basis. `OBJ-005`'s mapped scope items include
`SOW-088` and its mapped deliverables include `DEL-00-01`
(`SOFTWARE_DECOMP.md` §Objectives). The ruled attribution stands. This contract
does not restate it as a new derivation — and it records it at the strength the
Gate 3 record actually gives it, rather than at a strength the record does not
support.

That record is `execution/_ScopeChange/SCA-002_2026-07-25_1042/Amendment_Preview.md`,
per-row attribution 1, routed as question **Q1.1** and rated **MEDIUM**. Its
chain historically ran from PRD §13's still-present phrase "live postures
(ADR-002, ADR-014) re-cited in v2's first ADRs"; ADR-002 is the
zero-dependency core; the OI-012
core-isolation seam that the ADR settles is entity schema versus store
persistence; and "persistence separability underwrites PEC-K-02's deletability
→ `OBJ-005`". The same record states the counterargument: by the C1/C2
convention a "zero-dependency posture" is constraint-like, and "the chain to a
*product outcome* runs through two inferential steps". `OBJ-003` was the
considered alternative and was not adopted, on the ground that ADR-014's effect
"is to keep session ownership *out* of PEC, so it argues for absence, not
service". The record's own verdict is "`OBJ-005` recommended, weakly". This
contract carries the ruled attribution at that recorded strength and supplies
no stronger derivation for it. SCA-003 supersedes the historical chain's
two-live-posture interpretation: ADR-002 alone is re-cited as live, while
ADR-014 is historical lineage and the accepted v2 boundary is carried
independently.

**Basis provenance note.** `_REFERENCES.md` now names `SOFTWARE_DECOMP.md`
revision 1.3 as the accepted `current_basis` under the reference-parity
integration at `af62343d3`. `_CONTEXT.md` retains the revision-1.1 to
revision-1.2 supersession trace, while SCA-003 establishes revision 1.3 as the
current successor. The accepted basis bound in this contract's frontmatter is
revision 1.3 at merge `11a494e9a`. This contract cites revision 1.3.

- **OUT-001** — The v2 ADR recording the decided core isolation style for the PEC v2 service, explicitly identified as the resolution of open issue OI-012.
- **OUT-002** — The v2 ADR content re-citing ADR-002 as the live carried zero-dependency posture, citing ADR-014 as historical lineage only, and carrying the accepted v2 runtime/client and human-only-act boundary forward without the retired PEC-project-adapter allocation.

## Deliverable Definition — Ontology

### Identity

- **CLM-001** — `DEL-00-01` is named "v2 first ADRs (core isolation + carried postures)", Type `DOC_UPDATE`, Context Envelope `S` with no envelope notes, `PhaseHint` `pre-P1`, `ResponsibleParty` `TBD`; source `execution/_Decomposition/Deliverables.csv` row `DEL-00-01` and `SOFTWARE_DECOMP.md` §5 table for `PKG-00`.
- **CLM-002** — The deliverable description of record is: "ADR-v2 set: core isolation style resolving OI-012; ADR-002 re-cited as the live zero-dependency posture; ADR-014 cited as historical lineage only; accepted v2 runtime/client and human-only-act boundary carried forward"; source `Deliverables.csv` row `DEL-00-01`, restated in `_CONTEXT.md`.
- **CLM-003** — The anticipated artifact class of record is "ADR markdown entries under the v2 docs tree (path set by its packet)"; source `Deliverables.csv` `AnticipatedArtifacts` for `DEL-00-01`.
- **TBD-001** — The concrete v2 docs-tree path for the ADR markdown entries is not fixed by the accepted decomposition; it is set by this deliverable's own packet and remains unresolved in this contract.
- **TBD-002** — `ResponsibleParty` is unassigned; assignment happens at WORKING_ITEMS activation, not in this contract (`SOFTWARE_DECOMP.md` §5 preamble; `_CONTEXT.md`).

### Subject matter carried into the outputs

- **CLM-004** — ADR-002 as archived reads, in part: "One language (TypeScript) across core/server/web ... No server runtime dependencies"; its live carried form in v2 is the service rule `PEC-SVC-001` — "The service core has zero third-party runtime dependencies (carries ADR-002); workspace-internal runtime contracts packages are permitted" (`PRD.md` §10; `SOFTWARE_DECOMP.md` constraint C7 and `SOW-052`). Archived source: `projects/pec/docs/.archive/adr/ADR.md` §ADR-002.
- **CLM-005** — ADR-014 is preserved as historical evidence of the frozen v0.4 application. Its archived text allocated deterministic acts, RBAC, reporting, human-only acts, visibility, and data boundaries to a PEC project adapter, but that allocation is **not** a live carried posture for PEC v2: D-PEC-58 expressly states that the equivalent D-PEC-56 adapter-retention behavior did not survive retirement of the old product. The live carried boundary is limited to Root ownership of generic runtime semantics, PEC as an optional client with no second execution loop, and the surviving human-only-act restrictions. Sources: `projects/pec/docs/.archive/adr/ADR.md` §ADR-014; `execution/_Coordination/_DECISIONS/D-PEC-58_prd_v2_adoption.md`; `docs/PRD.md` §15.
- **CLM-006** — The recorded basis for the core-isolation decision is the Gate 4 exchange captured in `SOFTWARE_DECOMP.md` §Open Issues, row OI-012: the PRD invariants force the isolation properties under either candidate style (PEC-K-07 makes bridges disposable inputs; PEC-K-02 makes the store a throwaway projection; PEC-SVC-001 is the dependency-free-core rule); the package partition is congruent with a hexagonal grain (core: PKG-03/04/05 plus PKG-01 entities; driven edges: PKG-02/06 plus store; driving edges: PKG-07/08/09); nearly all §16 open decisions are adapter-level, so core isolation keeps them open cheaply; the lighter functional-core/imperative-shell variant fits a deterministic-derivation service with less ceremony; the one seam to keep crisp is entity schema (core) versus store persistence (adapter) inside PKG-01.
- **CON-001** — OI-012 (core isolation style: ports-and-adapters/hexagonal versus functional-core/imperative-shell) is **undecided** at the time of this contract. `ScopeLedger.csv` flags `SOW-088` with `OpenIssue=TRUE` at decision-log entry DL-14, and `SOFTWARE_DECOMP.md` §Open Issues dispositions OI-012 as "Decided in DEL-00-01's ADR; owner review at that ADR". This contract records the open issue and the decision's required form; it does not select a style, and no selection may be inferred from this document.

### Placement in the work graph

- **CLM-007** — `DEL-00-01` has no upstream predecessors and is a valid root node. Two downstream consumer relations are recorded against it, both at `PROPOSAL` stratum and neither `DECLARED`: `DEL-00-02` (Event-contract schema v1) `CONSUMES [E-N18]`, which additionally carries the `LOW_CONFIDENCE` flag with the recorded rationale "owner may prefer PKG-00 unordered"; and `DEL-01-01` (Record-tier schema and entity model) `CONSUMES [E-P01]`, unflagged. Sources: `_DEPENDENCIES.md` (downstream section, marked informational) and `Dependencies.csv` (v3.1, which holds only the two ANCHOR rows `DEP-00-01-001` and `DEP-00-01-002`), with stratum and flag read from the accepted gate exhibit `execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md` §4.1.
- **CLM-008** — Package mechanics constraint of record (DL-12): "PKG-00 deliverables publish artifacts that dependants consume as declared dependencies — a deliverable never writes into another package (disjoint write scopes preserved)"; source `SOFTWARE_DECOMP.md` §Decision Log, DL-12.

## Completion and Reliance Basis — Epistemology

The requirements below state what the future ADR authoring must satisfy. No ADR
exists for this deliverable at the time of writing; `_STATUS.md` records state
`INITIALIZED`. Nothing in this section asserts that any ADR has been written.

- **REQ-001** — The ADR set shall contain one decision record that names the selected v2 core isolation style and explicitly identifies that record as the resolution of OI-012.
- **REQ-002** — The core-isolation decision record shall state its context from the recorded Gate 4 basis (CLM-006) and shall not introduce product invariants, service rules, or scope items that are absent from the accepted PRD and decomposition.
- **REQ-003** — The ADR set shall re-cite ADR-002 as a live carried posture and shall bind it to its v2 carried form `PEC-SVC-001` and to scope item `SOW-052`, citing the archived source (CLM-004).
- **REQ-004** — The ADR set shall cite ADR-014 as historical lineage, not re-adopt its retired PEC adapter allocation. It shall carry forward only the accepted v2 boundary recorded in CLM-005: Root owns generic runtime semantics; PEC remains an optional client and starts no second execution loop; surviving human-only-act restrictions remain in force. It shall state explicitly that the archived allocation of deterministic acts, RBAC, reporting, visibility, and data boundaries to the old PEC project adapter is not a PEC v2 requirement.
- **REQ-005** — The ADR set shall cite `projects/pec/docs/.archive/adr/ADR.md` as historical baseline only. ADR-002 alone shall be re-cited as a live carried posture; ADR-014 shall be cited only as historical lineage while the accepted v2 runtime/client and human-only-act boundary is carried independently, and no other archived ADR shall be restored to live authority.
- **REQ-006** — The ADR set shall make explicit the seam identified as the one to keep crisp: entity schema (core) versus store persistence (adapter) inside `PKG-01`.
- **REQ-007** — The ADR set shall leave the §16 owner decisions OI-001 through OI-009 and the tooling follow-on OI-013 undecided; deciding any of them is out of this deliverable's scope. The recorded basis characterizes those §16 decisions as "nearly all ... adapter-level" (CLM-006), not uniformly so, and this requirement binds all nine regardless of that characterization.
- **REQ-008** — The ADR markdown entries shall be published at the v2 docs-tree path set by this deliverable's packet (TBD-001) and that path shall be recorded before the artifacts are treated as consumable.
- **REQ-009** — The published ADRs shall be consumable as dependency inputs by the two deliverables the accepted exhibit *proposes* as their consumers — `DEL-00-02` via `[E-N18]` and `DEL-01-01` via `[E-P01]` — so that if and when either proposed edge is taken up, no republication is needed. Consumability is stated relative to those proposed edges; this requirement asserts no accepted consumer obligation and no `DECLARED` stratum for either edge (CLM-007, AX-007). Production of this deliverable shall not write into any other package (CLM-008).
- **REQ-010** — No ADR in the set shall introduce a posture under which a governed act depends on PEC-held state, so that `OBJ-005` remains satisfiable.

- **AC-001** — The published ADR set contains exactly one decision record that names a single selected v2 core isolation style and states in its own text that it resolves OI-012.
- **AC-002** — That decision record's context section reproduces the recorded Gate 4 basis elements of CLM-006 and adds no invariant or service rule absent from the accepted PRD and decomposition.
- **AC-003** — The ADR set re-cites ADR-002 as the sole live carried posture, cites ADR-014 as historical lineage only, carries the accepted v2 runtime/client and human-only-act boundary without the retired PEC-project-adapter allocation, and asserts no other archived ADR as live authority.
- **AC-004** — The ADR set names itself in its own text as the resolution of OI-012, and that self-identification is consistent with the disposition the open-issue register already carries for OI-012 — "Decided in DEL-00-01's ADR; owner review at that ADR" — requiring no change to it. The set decides none of OI-001 through OI-009 or OI-013 and claims no register-side effect; any register-side update is an out-of-scope downstream act (SCOPE_CHANGE or coordination upkeep), not a completion condition of this deliverable.
- **AC-005** — The ADR set states the entity-schema versus store-persistence seam inside PKG-01 explicitly enough that a reader can classify a candidate PKG-01 change as core or adapter.
- **AC-006** — The v2 docs-tree path is recorded in the deliverable packet, the ADR markdown entries exist at that path, and the run produced no write outside `PKG-00`.
- **AC-007** — An accountable owner confirms the selected core isolation style at the ADR, consistent with the OI-012 disposition "owner review at that ADR", and confirms that nothing in the set makes a governed act depend on PEC-held state.

## Production and Verification Method — Praxeology

Production sequence expected of the future authoring run: read the accepted basis
row for `DEL-00-01` and the `SOW-088` ledger row; read the OI-012 record and the
archived ADR-002 and ADR-014 text; draft the core-isolation decision record; draft
the ADR-002 live re-citation and ADR-014 historical-lineage citation; record
the packet path; publish under `PKG-00`
only. All work is bounded to the deliverable folder and the `PKG-00` docs-tree
path it names; this contract authorizes no register, decomposition, or PRD edit.
Tests and deterministic checks implement verification methods below; they do
not create scope or acceptance criteria, and none of them may add a requirement
that is not already stated in this contract.

- **VER-001** — Document inspection of the published ADR set against `SOW-088`'s ledger statement, the `SOFTWARE_DECOMP.md` §5 row for `DEL-00-01`, and REQ-001, REQ-002, REQ-006, REQ-007.
- **VER-002** — Citation resolution check: the ADR-002 live re-citation and ADR-014 historical-lineage citation each resolve to a locatable heading in `projects/pec/docs/.archive/adr/ADR.md`; ADR-002 is the sole archived ADR treated as live authority, and ADR-014 is never treated as a v2 allocation.
- **VER-003** — Read-only cross-check of the published ADR set against `SOFTWARE_DECOMP.md` §10 Open Issues: confirm that the set's self-identified OI-012 resolution is consistent with the OI-012 disposition already recorded there, and that no statement in the set decides OI-001 through OI-009 or OI-013. The register is read, never written: this verification performs and expects no register edit, and any register-side update the owner later requires is a downstream act outside this deliverable's authority.
- **VER-004** — Path and dependency check: the packet-recorded v2 docs-tree path exists and holds the ADR entries, `DEL-00-02` and `DEL-01-01` could reference them as dependency inputs under the proposed edges `[E-N18]` and `[E-P01]` without republication, and the change set touches no path outside `PKG-00`.

## Governing Values and Decisions — Axiology

- **AX-001** — `OBJ-005` governs: everything PEC holds can be deleted at any moment without blocking any governed act. An ADR that makes any governed act depend on PEC-held state would defeat the objective this deliverable serves.
- **AX-002** — The accepted basis is `SOFTWARE_DECOMP.md` revision 1.3 at merge `11a494e9a`, accepted through `SCA-003`; revision 1.1 and revision 1.2 references are superseded provenance, not competing authority.
- **AX-003** — DL-12 governs package mechanics: PKG-00 publishes and dependants consume through declared dependency edges; contribution to another package is never a cross-package write.
- **AX-004** — The archived baseline is historical and retention under `docs/.archive/` is not reauthorization. ADR-002 alone is re-cited as live; ADR-014 is historical lineage only, while the accepted v2 runtime/client and human-only-act boundary is carried forward independently.
- **AX-005** — Unknowns remain marked. `TBD-001`, `TBD-002`, and `CON-001` are recorded rather than resolved by inference; OI-012 is the owner's decision at the ADR, and this contract's job is to fix the form that decision must take, not its content.
- **AX-006** — This contract is lifecycle-neutral. `_STATUS.md` remains the sole lifecycle authority and is untouched by this reconciliation; the deliverable is at `INITIALIZED` and no ADR has been authored.
- **AX-007** — `C-10` `STRATUM_RULE` is a register-wide non-gating constraint and its own text ends "strata are provenance not authority". Both downstream relations in CLM-007 are `PROPOSAL`, and `[E-N18]` additionally carries `LOW_CONFIDENCE` ("owner may prefer PKG-00 unordered"). `D-PEC-62` §1.4 accepted the exhibit's strata as presented while carrying that flag forward as a recorded-but-unresolved, non-gating annotation. This contract cites both edges at that status: they establish provenance for an expected consumption pattern, and they establish no obligation on this deliverable or on either named consumer.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-088 OBJ-005 | REQ-001 REQ-002 REQ-006 CLM-006 CON-001 | AC-001 AC-002 AC-005 | VER-001 | Published core-isolation ADR |
| OUT-001 | SOW-088 OBJ-005 | REQ-007 CON-001 | AC-004 | VER-001 VER-003 | The read-only cross-check record showing the ADR's self-identified OI-012 resolution consistent with the register's existing disposition, no register edit performed, and no other open issue decided |
| OUT-001 | SOW-088 OBJ-005 | REQ-010 AX-001 CON-001 | AC-007 | HUMAN_REVIEW: accountable owner review at the DEL-00-01 ADR, per the OI-012 disposition recorded in SOFTWARE_DECOMP.md | Dated owner ruling recorded against this deliverable, naming the selected style and confirming the graceful-absence posture |
| OUT-002 | SOW-088 OBJ-005 | REQ-003 REQ-004 REQ-005 CLM-004 CLM-005 | AC-003 | VER-002 | ADR text with a resolvable ADR-002 live citation, an ADR-014 historical-lineage citation, the accepted v2 boundary, and no retired allocation or additional live-posture claim |
| OUT-002 | SOW-088 OBJ-005 | REQ-008 REQ-009 CLM-003 CLM-007 CLM-008 TBD-001 AX-007 | AC-006 | VER-004 | Packet-recorded docs-tree path, ADR files present at that path, a change set confined to PKG-00, and the recorded PROPOSAL/LOW_CONFIDENCE status of the two proposed consumer edges |
