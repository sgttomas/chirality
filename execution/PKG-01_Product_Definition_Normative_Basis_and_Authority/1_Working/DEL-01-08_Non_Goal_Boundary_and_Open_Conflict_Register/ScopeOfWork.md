---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-08
package_id: PKG-01
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-007, SOW-077, SOW-078, SOW-079, SOW-100, SOW-101]
package_objective_refs: [OBJ-001]
---

# Scope of Work — DEL-01-08

## Purpose and Objective Traceability

This is the candidate production contract for `DEL-01-08` — Non-Goal, Boundary,
and Open-Conflict Register — in package `PKG-01`. It covers project scope items
SOW-007, SOW-077, SOW-078, SOW-079, SOW-100, and SOW-101 and supports package
objective OBJ-001.

Traceability, transcribed and not inferred:

| Binding | Value | Source |
|---|---|---|
| Covered scope items | SOW-007, SOW-077, SOW-078, SOW-079 (boundary, `InOutStatus OUT`); SOW-100, SOW-101 (carried conflicts, `InOutStatus IN`) | `_CONTEXT.md` Scope Traceability; register `CoversScopeItems`; ledger `InOutStatus` |
| Supported objective | OBJ-001 | `_CONTEXT.md` Scope Traceability; register `SupportsObjectives` |
| Deliverable type | `REGISTER` | register `Type` |
| Context envelope | `S` — "Boundary bookkeeping over an enumerated list." | register `ContextEnvelope`/`ContextEnvelopeNotes` |
| Anticipated write locus | `execution-tree` | register `AnticipatedWriteLocus` |
| Responsible party | `Ryan Tufts` | D-GOV-27; current deliverable register `ResponsibleParty` |

Every `AC-*` and `VER-*` below is a **candidate**. The accepted decomposition
states no per-deliverable acceptance criteria (`_CONTEXT.md`); nothing here is
inferred beyond the register row, `_CONTEXT.md`, the six ledger statements, and
the adopted `docs/PRD_ROOT.md`. This document claims no acceptance and no
lifecycle state, and it rules on no conflict.

The outputs are OUT-001, OUT-002, and OUT-003, defined below.

## Deliverable Definition — Ontology

- **OUT-001** — Non-goal register: an execution-tree register holding the
  covered non-goals as an enforced boundary set, one entry per covered scope
  item, each citing its ledger statement and SourceRef.
- **OUT-002** — Retired-identifier note: an execution-tree note recording the
  retired `D-3` identifier, that it is deliberately absent, and that it is never
  reassigned.
- **OUT-003** — Open-conflict status table: an execution-tree table carrying the
  covered open conflicts with each entry's status re-checked at the checked
  basis rather than assumed, and with the ruling reserved to the owner.

- **CLM-001** — Covered boundary item (SOW-007, SourceRef `PRD §9.5
  [OWNER_DECLARED — ruled]`, `DecisionRef DEC-007`): the B and C stages of the
  ruled user-scope trajectory are declared trajectory, not v1 scope. The ledger
  note states why it is carried — so later work cannot silently pull B/C
  obligations into v1.
- **CLM-002** — Covered boundary item (SOW-077, SourceRef `PRD §8.1
  [TRANSCRIBED non-goal]`): no blanket authority for future root-structure
  changes.
- **CLM-003** — Covered boundary item (SOW-078, SourceRef `PRD §8.1
  [TRANSCRIBED non-goal]`): no change to the named human-authority, binding,
  gate, and sealed-context invariants, or to any invariant or clause not named
  in the authorizing packet.
- **CLM-004** — Covered boundary item (SOW-079, SourceRef `PRD §8.1
  [TRANSCRIBED / CLARIFIED non-goal]`): the PRD is not a roadmap; the roadmap
  surface remains separate, and no packages, deliverables, acceptance tests, or
  priority rankings are introduced by the PRD itself.
- **CON-001** — Closed-conflict trace (SOW-100, SourceRef `PRD §10.2 C-3
  [surfaced conflict]`, `DecisionRef DEC-009`): D-GOV-22 confirmed the owner
  testimony and closed C-3; PRD Revision 6 records that the earlier estimate is
  not load-bearing and is not to be repeatedly recited. The register preserves
  the discovery and closing pointers and does not reopen owner confirmation.
- **CON-002** — Closed-conflict trace (SOW-101, SourceRef `PRD §10.2 C-4
  [surfaced conflict]`, `DecisionRef DEC-009`): PR #345 (merge `ba2b80bf2`,
  Receipt 44) added `runtime/` to the README description and closed C-4 while
  preserving the live export profile as the boundary contract. The register
  retains a standing re-check without treating C-4 as open.
- **CLM-005** — Coverage boundary: `docs/PRD_ROOT.md` §10.2 also surfaces C-1
  and C-2, which are **not** among this deliverable's covered scope items. They
  are out of scope here and are neither carried nor closed by these outputs.
- **CLM-006** — Retired identifier (`docs/PRD_ROOT.md` §5.3, retired-identifier
  paragraph; register `AnticipatedArtifacts`): `D-3` is deliberately absent, the
  identifier is retired and never reassigned, and the surrounding identifiers
  keep their IDs so existing cross-references stay valid.
- **CLM-007** — Objective linkage (`docs/PRD_ROOT.md` §3 OBJ-1): OBJ-001 is
  satisfied when a reader can determine what governs from the repository alone,
  and no ratified clause has an unrecorded conflicting live variant. This
  register contributes the boundary and open-conflict half of that reader's
  answer; it does not discharge OBJ-001.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — OUT-001 shall hold one entry per covered boundary item
  (CLM-001..CLM-004), each transcribing its ledger statement and citing its
  SourceRef and `DecisionRef`, with no boundary item merged into another.
- **REQ-002** — OUT-001 shall record each entry as an enforced boundary — a
  statement later work must not cross — rather than as background narrative.
- **REQ-003** — OUT-002 shall record the retired `D-3` identifier, its
  deliberate absence, and the never-reassigned rule.
- **REQ-004** — OUT-003 shall carry CON-001 and CON-002 as closed-conflict
  traces with, per entry: the historical conflict, closing act, status at the
  checked basis, basis commit, and method used to re-check current agreement.
- **REQ-005** — OUT-003 shall not treat a ledger note's hedged wording
  ("recorded as", "appears") as a determination. The recorded closing acts govern
  C-3 and C-4; a newly observed disagreement is recorded as a new finding and
  routed to the owner (`docs/PRD_ROOT.md` §5.1 N-4).
- **REQ-006** — No output shall reopen, rerule, or silently reinterpret a
  closed conflict. Standing re-checks produce evidence; ruling remains the
  owner's (`docs/PRD_ROOT.md` §8.1, §10.2).
- **REQ-007** — OUT-003 shall state its coverage boundary per CLM-005, so a
  reader can tell which surfaced conflicts this register carries and which it
  does not.

- **AC-001** — OUT-001 holds one distinct, cited entry per covered boundary item
  and states each as an enforced boundary.
- **AC-002** — OUT-002 records the retired `D-3` identifier with its deliberate
  absence and the never-reassigned rule.
- **AC-003** — Every OUT-003 entry carries its closing act and a current status
  determined at a recorded basis with a recorded method; any new disagreement
  is surfaced without this register reopening or reruling the conflict.

## Production and Verification Method — Praxeology

Production sequence: transcribe the six ledger statements with SourceRefs and
`DecisionRef`s; assemble the non-goal register; write the retired-identifier
note; then re-check each carried conflict against the live surfaces at a
recorded basis and fill the status table from what the check returns.

- **VER-001** — Deterministic retired-identifier check: search
  `docs/PRD_ROOT.md` for a `D-3` commitment row (`grep -n` from the repository
  root over §5.3) and confirm the identifier appears only in the retirement
  statement and not as a live commitment. Any reassignment found is a finding.
- **VER-002** — Deterministic C-4 re-check (CON-002): compare the public-export
  section of `README.md` against the root-directory allowlist in
  `exports/chirality-app/export_public.py` and record whether the described set
  and the allowlisted set agree at the checked commit. The live profile governs;
  neither file is edited by this deliverable.
- **VER-003** — `HUMAN_REVIEW: reviewer confirms that CON-001 cites D-GOV-22
  as the C-3 closing act, does not repeatedly recite the earlier estimate, and
  does not reopen owner confirmation.`
- **VER-004** — `HUMAN_REVIEW: reviewer compares OUT-001 entry by entry against
  the SOW-007, SOW-077, SOW-078, and SOW-079 ledger statements and confirms no
  boundary is weakened, merged, or restated as narrative.`

## Governing Values and Decisions — Axiology

- **AX-001** — Candidate status. Nothing here is accepted; `AC-*` and `VER-*` are
  candidates for owner review (K-AUTH-1).
- **AX-002** — Write-locus boundary. The register's `AnticipatedWriteLocus` is
  `execution-tree`, a planning note rather than authorization (`_CONTEXT.md`).
  Any act touching the instruction surface — `AGENTS.md`, `agents/`, `skills/`,
  `tools/`, root `docs/`, `init/`, or `.github/workflows/` — requires an
  independently authorized M2 tranche, and **this Scope of Work grants none**.
  `README.md`, `exports/chirality-app/export_public.py`, and `docs/PRD_ROOT.md`
  are read-only inputs to the checks above; a propagation finding is routed, not
  applied.
- **AX-003** — Trace, not reruling. SOW-100 and SOW-101 retain their discovery
  history, while D-GOV-22 and PR #345/Receipt 44 govern their closed status.
  Any new disagreement is surfaced to the owner as new evidence.
- **AX-004** — Re-checked, not assumed. `_CONTEXT.md` requires each entry's
  status to be re-checked rather than assumed; a ledger note is an input to the
  re-check, never its result.
- **AX-005** — A non-goal is enforced, not archival. The boundary set exists so
  later work cannot import an out-of-scope obligation by silence.
- **AX-006** — `ResponsibleParty` is `Ryan Tufts` under D-GOV-27 and the current deliverable register
  (`_CONTEXT.md` Source Authority).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-007 SOW-077 SOW-078 SOW-079 OBJ-001 | CLM-001 CLM-002 CLM-003 CLM-004 CLM-007 REQ-001 REQ-002 | AC-001 | VER-004 | One cited entry per covered boundary item, each stated as an enforced boundary with SourceRef and DecisionRef |
| OUT-002 | SOW-079 OBJ-001 | CLM-006 REQ-003 | AC-002 | VER-001 | Retired-identifier record with the deliberate absence, the never-reassigned rule, and the recorded search result |
| OUT-003 | SOW-100 SOW-101 OBJ-001 | CON-001 CON-002 CLM-005 CLM-007 REQ-004 REQ-005 REQ-006 REQ-007 | AC-003 | VER-002 VER-003 | Per-conflict closing act and current status with basis commit and method, plus any newly surfaced disagreement and the stated coverage boundary |
