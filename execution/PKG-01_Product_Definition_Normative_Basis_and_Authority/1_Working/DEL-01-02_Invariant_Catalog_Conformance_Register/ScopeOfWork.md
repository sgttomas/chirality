---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-02
package_id: PKG-01
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-016, SOW-025, SOW-099]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-01-02

## Purpose and Objective Traceability

This Scope of Work defines the production contract for DEL-01-02, *Invariant
Catalog Conformance Register*, in package PKG-01. Its declared basis is the
accepted root decomposition named in `decomposition_basis`; its covered
project scope is SOW-016, SOW-025, SOW-099; its package objective is OBJ-001.

Per the accepted register row, the deliverable exists to *"maintain the
register showing that the running system continues to satisfy the invariant
catalog: every K-* invariant mapped to a live enforcement point, with
index-arithmetic consistency checked rather than asserted."* The accepted
`Type` is `REGISTER`; the accepted `ContextEnvelope` note reads *"register-
shaped machine truth over one catalog; bounded read set (CONTRACT plus
enforcement surfaces)."*

**Write-locus boundary.** The accepted `AnticipatedWriteLocus` for this
deliverable is `execution-tree`. `AnticipatedWriteLocus` is a planning note,
not authorization. The covered conflict C-2 (CLM-003) concerns the ratified
instruction surface `docs/CONTRACT.md`; the adopted PRD records that it is
*"not amended here — ratified instruction surface"* and recommends an M2
correction tranche. Any act touching the instruction surface — `AGENTS.md`,
`agents/`, `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/` —
**requires an independently authorized M2 tranche. This Scope of Work grants
none, and this deliverable reports the arithmetic rather than correcting it.**

No lifecycle state, acceptance, or reliance is asserted by this document. The
definitions below are candidate content for owner review.

## Deliverable Definition — Ontology

### Expected outputs

- **OUT-001** — Invariant conformance register (CSV): one row per `K-*`
  invariant in the catalog, each mapped to its live enforcement point or
  carrying an explicit `TBD`.
- **OUT-002** — Enforcement-point index: the resolved list of enforcement
  surfaces cited by OUT-001, each bound to a path in the checkout at a named
  basis revision.
- **OUT-003** — Arithmetic check output: the recorded comparison between the
  catalog's stated invariant and subsection counts and its defined membership,
  produced as machine output rather than as an assertion.

### Covered scope statements

- **CLM-001** — SOW-016 (`PRD §5.1 N-2 [TRANSCRIBED]`) states that the
  invariant catalog is the binding constraint set the product must continue to
  satisfy; it governs its own membership and no parallel invariant list is
  maintained. The adopted PRD sources this to `docs/CONTRACT.md` §1 and the
  K-AGENTS-1 live-registry principle.
- **CLM-002** — SOW-025 (`PRD §5.1 N-9 [CLARIFIED]`) states that the normative
  basis is a constituent of the product rather than documentation about it:
  the requirement is that the running system continue to satisfy the
  invariants, not that it describe them. The adopted PRD labels this an
  interpretation of `docs/CONTRACT.md` §2 — every invariant has a live
  enforcement point.
- **CLM-003** — SOW-099 preserves the discovery record for `PRD §10.2 C-2
  [surfaced conflict]`: invariant-index arithmetic between the catalog's stated
  count and its defined membership. PR #345 (merge `ba2b80bf2`, Receipt 44)
  corrected the index to 34 invariants across 13 subsections, and PRD Revision
  6 records C-2 as closed without reopening it. `DecisionRef` remains DEC-009
  for historical traceability. This deliverable performs standing verification
  against the current catalog and surfaces any new disagreement as new evidence;
  it does not carry C-2 as an open owner decision.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — The register in OUT-001 shall take its membership from the
  catalog itself and shall not mint a parallel list of `K-*` identifiers
  (CLM-001). Membership is read, never authored here.
- **REQ-002** — Every register row shall carry either a named live enforcement
  point or an explicit `TBD` (CLM-002). An unmapped invariant is recorded as
  `TBD`, never inferred or omitted.
- **REQ-003** — The enforcement points cited in OUT-001 shall be resolvable in
  the checkout: OUT-002 shall bind each to a path at a named basis revision
  (CLM-002).
- **REQ-004** — OUT-003 shall be produced as recorded machine output — command
  and result — rather than as a narrative assertion (CLM-003), and shall state
  the counted membership, the catalog's stated count, and whether they agree.
- **REQ-005** — This deliverable shall not amend `docs/CONTRACT.md`. C-2 is
  recorded as closed by PR #345 and Receipt 44; any new disagreement is surfaced
  with pointers and any correction remains a separately authorized M2 tranche
  (CLM-003).

- **AC-001** — OUT-001 contains exactly one row per `K-*` invariant defined in
  the catalog, contains no `K-*` identifier absent from the catalog, and every
  row carries either a named enforcement point or an explicit `TBD`.
- **AC-002** — Every enforcement point cited in OUT-001 resolves to an
  existing path in the checkout at the basis revision recorded in OUT-002, or
  is recorded in OUT-002 as unresolved.
- **AC-003** — OUT-003 records the invocation and its output, states the
  counted membership alongside the catalog's stated count and subsection
  count, and states agreement or disagreement without amending
  `docs/CONTRACT.md`.

## Production and Verification Method — Praxeology

Production sequence for this deliverable:

1. Read the invariant catalog at a recorded basis revision and extract its
   defined `K-*` membership and its stated counts (REQ-001).
2. Read the enforcement map and the enforcement surfaces it cites, and build
   OUT-001 one row per invariant (REQ-002).
3. Resolve each cited enforcement point to a checkout path and record the
   result as OUT-002 (REQ-003).
4. Run the recount and record command plus output as OUT-003 (REQ-004).
5. Surface any disagreement as a carried conflict with pointers; do not amend
   the catalog (REQ-005).

- **VER-001** — Deterministic recount, recorded as command and output: extract
  the defined `K-*` identifiers and subsection headings from
  `docs/CONTRACT.md` §1.1 through §1.13 and compare the counts against the
  counts the catalog states for itself. Reproducible from the checkout at the
  recorded revision; produces the evidence for OUT-003, not a ruling on C-2.
- **VER-002** — Deterministic path-resolution check over OUT-002: assert that
  every enforcement-point path cited by OUT-001 exists in the checkout at the
  recorded revision, and record each unresolved citation explicitly rather
  than dropping it.

No registered deterministic tool judges whether a given enforcement point
actually enforces its invariant. That mapping judgment carries a named
human-review method in the matrix rather than a fabricated tool reference.

## Governing Values and Decisions — Axiology

- **AX-001** — The live registry governs. The catalog governs its own
  membership and this register mirrors it; where register and catalog
  disagree, the catalog controls and the discrepancy is surfaced (CLM-001).
- **AX-002** — Conformance is a property of the running system, not of prose.
  The register exists to show that the system continues to satisfy the
  invariants, not to restate them (CLM-002).
- **AX-003** — Arithmetic is checked, not asserted. The count comparison is
  machine output that a reader can re-run (CLM-003, REQ-004).
- **AX-004** — Conflicts are surfaced, not silently resolved. C-2 is closed
  by PR #345 and Receipt 44; standing verification preserves those pointers and
  surfaces any new disagreement. The ratified instruction surface is corrected
  only through an independently authorized M2 tranche (CLM-003, REQ-005).
- **AX-005** — Nothing in this contract asserts acceptance, lifecycle state,
  or professional reliance. `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-016 SOW-025 OBJ-001 | CLM-001 CLM-002 REQ-001 REQ-002 | AC-001 | HUMAN_REVIEW: Owner or delegated reviewer reads each register row against the catalog entry and its cited enforcement surface and confirms the mapping is real rather than nominal | The register CSV, the catalog at the recorded revision, and the reviewer's recorded confirmation |
| OUT-002 | SOW-025 OBJ-001 | CLM-002 REQ-003 | AC-002 | VER-002 | The enforcement-point index, the recorded basis revision, and the recorded resolution result for every cited path |
| OUT-003 | SOW-099 OBJ-001 | CLM-003 REQ-004 REQ-005 | AC-003 | VER-001 | The recorded command, its output, the closed C-2 trace, and any newly surfaced disagreement |
