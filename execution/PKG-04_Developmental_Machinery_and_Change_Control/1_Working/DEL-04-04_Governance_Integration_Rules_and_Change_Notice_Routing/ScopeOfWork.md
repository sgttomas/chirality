---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-04
package_id: PKG-04
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-040, SOW-045]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-04-04

## Purpose and Objective Traceability

This Scope of Work is the production contract for `DEL-04-04`, "Governance
Integration Rules and Change-Notice Routing", a `REQ_SLICE`-type deliverable of
`PKG-04 Developmental Machinery and Change Control`. It serves project scope
items SOW-040 and SOW-045 and package objective OBJ-003.

Per its `_CONTEXT.md` Description, the deliverable exists to keep phase-crossing
work bound by the governance integration rules, and to keep tranches that touch
pinned or mirrored surfaces shipping routed coordination notices in the same
tranche, as coordination and never authority.

The accepted decomposition states no per-deliverable acceptance criteria;
`_CONTEXT.md` records that as unresolved rather than inferring criteria
(K-INVENT-1). The `AC-*` and `VER-*` records below are therefore **candidates**
proposed from the four authorized grounding sources — the deliverable register
row, `_CONTEXT.md`, the scope-ledger statements of SOW-040 and SOW-045, and the
adopted `docs/PRD_ROOT.md`. They assert no acceptance, no approval, and no
lifecycle state; the owner disposes of them at the review gate.

### Grounding sources

- Deliverable register row
  `DEL-04-04_Governance_Integration_Rules_and_Change_Notice_Routing` in
  `execution/_Decomposition/chirality_root_deliverable_register_v1_0.csv`.
- `_CONTEXT.md` of this deliverable.
- Scope-ledger rows SOW-040 and SOW-045 in
  `execution/_Decomposition/chirality_root_scope_ledger_v1_0.csv`.
- `docs/PRD_ROOT.md` §5.3, commitments D-6 and D-11.

## Deliverable Definition — Ontology

The anticipated artifacts named in the register row and in `_CONTEXT.md`
Anticipated Artifacts define three outputs.

- **OUT-001** — Integration-rule conformance checklist: a checklist covering the
  seven governance integration rules SOW-040 names, expressed as checks a
  phase-crossing unit of work can be held against.
- **OUT-002** — Notice routing map: a map from the surface classes that
  downstream loops pin or mirror to the coordination surface of each affected
  loop that a notice must reach.
- **OUT-003** — Notice templates: reusable coordination-notice forms carrying
  what changed, what follow-on remains for the receiving loop, and the statement
  that the notice is coordination and not authority.

Descriptive claims that fix what this deliverable is about:

- **CLM-001** — SOW-040 states that phase-crossing work is bound by the
  governance integration rules — derivative-package, snapshot, handoff-state,
  closure, sequencing, cycle-resolution, and change-notice routing —
  incorporated by reference. Source: scope-ledger SOW-040, `SourceRef` PRD §5.3
  D-6 [TRANSCRIBED].
- **CLM-002** — SOW-045 states that a tranche changing surfaces that downstream
  loops pin or mirror ships a routed coordination notice to each affected loop
  in the same tranche, as coordination rather than authority. Source:
  scope-ledger SOW-045, `SourceRef` PRD §5.3 D-11 [TRANSCRIBED].
- **CLM-003** — The rule set is incorporated by reference, not copied. PRD §5.3
  D-6 incorporates the rules by reference to `AGENTS.md` §Governance Integration
  Rules, and the adopted PRD's registry discipline holds that where a live
  registry and a narrative disagree, the live registry governs and the
  discrepancy is surfaced. This deliverable therefore maintains no parallel
  authoritative copy of the rule text.
- **CLM-004** — Per PRD §5.3 D-11, the notice is coordination and not authority:
  the receiving loop adopts, amends, or declines under its own instruments. A
  notice that reads as a directive to the receiving loop misstates its own
  status.
- **CLM-005** — The register row types this deliverable `REQ_SLICE` with
  `ContextEnvelope: M` and the note "One rule set plus a routing map over known
  downstream loops", bounding the work to one rule set and the loops known at
  the time the map is drawn.

## Completion and Reliance Basis — Epistemology

Requirements restate the covered scope obligations as checkable production
requirements. They are candidates for owner disposition, not accepted criteria.

- **REQ-001** — The checklist of OUT-001 shall enumerate exactly the seven rules
  SOW-040 names — derivative-package, snapshot, handoff-state, closure,
  sequencing, cycle-resolution, and change-notice routing — neither adding an
  eighth nor dropping one.
- **REQ-002** — Each checklist entry shall cite the live rule surface as its
  governing source rather than restating rule text on its own authority, so that
  a later amendment to the rule set does not leave a stale authoritative copy
  inside this deliverable.
- **REQ-003** — The checklist shall be expressed against phase-crossing work —
  the unit SOW-040 binds — so that each entry is checkable at a phase boundary
  rather than as general advice.
- **REQ-004** — The routing map of OUT-002 shall record, per surface class that
  downstream loops pin or mirror, the affected loop and the repo-relative
  coordination-surface path a notice must reach, and every recorded path shall
  resolve in the active checkout.
- **REQ-005** — The templates of OUT-003 shall carry, as fixed text, what
  changed, what follow-on remains for the receiving loop, and an explicit
  statement that the notice is coordination and not authority and that the
  receiving loop adopts, amends, or declines under its own instruments.
- **REQ-006** — The same-tranche obligation shall be preserved: a notice
  produced from these templates is shipped in the same tranche as the change it
  reports, not deferred to a later one.
- **REQ-007** — No output of this deliverable shall assert acceptance, approval,
  lifecycle transition, or a ruling, and no notice shall direct a receiving loop
  to act.
- **REQ-008** — Production shall write only under the execution tree.
  `_CONTEXT.md` records `AnticipatedWriteLocus: execution-tree;
  instruction-surface (M2) for rule text`. That locus is a planning note and not
  authorization: any act changing rule text on the instruction surface requires
  an independently authorized M2 tranche, which this Scope of Work does not
  grant and cannot grant.

Candidate acceptance criteria:

- **AC-001** — The OUT-001 checklist contains one entry per rule for all seven
  rules named in SOW-040, each entry citing the live rule surface and stating a
  check applicable at a phase boundary, with no additional or missing rule.
- **AC-002** — Every routing-map entry in OUT-002 names a surface class, an
  affected loop, and a repo-relative coordination-surface path that resolves in
  the active checkout.
- **AC-003** — Each template in OUT-003 contains the coordination-not-authority
  statement and the adopt/amend/decline sentence, and a tranche using the
  template records a routed notice disposition whose referenced notice path
  exists.

## Production and Verification Method — Praxeology

Production reads the four grounding sources and the live rule and coordination
surfaces, then writes the three outputs under the execution tree. Verification
separates what a deterministic pass settles from what a human reader must judge.

- **VER-001** — Deterministic notice-disposition check: run
  `python3 tools/validation/validate_instruction_tranche_manifest.py`. That
  registered validator reads the notice disposition recorded for a tranche and
  fails when the disposition is `routed` while no notice is named, when a named
  notice path is not repo-relative, or when a named notice path does not exist.
  It therefore settles the mechanical half of the SOW-045 obligation — that a
  routed notice is actually named and actually present — without judging whether
  the notice reached the right loop.
- **VER-002** — Deterministic path-resolution check over the routing map: for
  every coordination-surface path recorded in OUT-002, confirm by path
  inspection that the path is repo-relative and resolves in the active checkout.
  An unresolvable path is a finding, not a silently dropped row.
- **VER-003** — Boundary check on write locus: confirm by path inspection that
  every artifact produced by this deliverable resolves under the execution tree
  and that no file under the instruction surface — `AGENTS.md`, `agents/`,
  `skills/`, `tools/`, root `docs/`, `init/`, `.github/workflows/` — was written
  by this deliverable's production, consistent with REQ-008.

Whether a checklist entry faithfully expresses its rule, and whether the set of
affected loops in the routing map is complete for a given tranche, are judgments
no check settles; the matrix carries an explicit `HUMAN_REVIEW` method there
rather than a fabricated check.

## Governing Values and Decisions — Axiology

- **AX-001** — Coordination is not authority. Per SOW-045 and PRD §5.3 D-11, a
  notice informs; the receiving loop decides under its own instruments. This
  constrains the wording of every template produced here.
- **AX-002** — Live registries govern over narrative copies. The rule set is
  incorporated by reference; a conformance checklist that hardens into a
  competing rule text would invert that relationship and is out of scope.
- **AX-003** — The instruction surface is governed separately. `_CONTEXT.md`
  states that any locus naming the instruction surface requires an
  independently authorized M2 tranche. This Scope of Work grants no such
  authorization, and its acceptance would grant none — including for the rule
  text this deliverable is about.
- **AX-004** — Nothing is inferred beyond the authorized sources (K-INVENT-1).
  Where the accepted decomposition is silent — on per-deliverable acceptance
  criteria, and on `ResponsibleParty`, which is `Ryan Tufts` under D-GOV-27 and the current deliverable register — the accepted assignment is preserved, while the acceptance-criteria silence is surfaced.
- **AX-005** — Detection must not depend on the notice alone. The change-notice
  obligation exists so that a downstream loop is told directly rather than
  relying only on its own drift detection; a notice omitted because "the other
  loop will notice anyway" defeats the rule.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-040 OBJ-003 | CLM-001 CLM-003 CLM-005 REQ-001 REQ-002 REQ-003 REQ-007 | AC-001 | HUMAN_REVIEW: owner reading of each checklist entry against the live governance integration rules it cites, confirming the seven-rule set is complete and faithfully expressed | Checklist document with one entry per named rule, each carrying its citation to the live rule surface |
| OUT-002 | SOW-045 OBJ-003 | CLM-002 CLM-005 REQ-004 REQ-007 REQ-008 | AC-002 | VER-002 VER-003 | Routing map with resolved repo-relative coordination-surface paths, and the recorded path-resolution result including any unresolvable entry |
| OUT-003 | SOW-045 OBJ-003 | CLM-002 CLM-004 REQ-005 REQ-006 REQ-007 REQ-008 | AC-003 | VER-001 VER-003 | Template texts carrying the coordination-not-authority statement, plus the validator run output over the tranche manifest recording the notice disposition and existing notice path |
