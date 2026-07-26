---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-02
package_id: PKG-03
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-032]
package_objective_refs: [OBJ-002]
---

# Scope of Work — DEL-03-02

## Purpose and Objective Traceability

This deliverable keeps governed work structured the way the accepted basis
requires: as execution instances containing flat packages and deliverables with
stable IDs, a canonical lifecycle state file, and human-triaged staleness
propagation. It is conformance work over an existing structure, not a redesign
of it.

It covers one project scope item and supports one package objective, exactly as
declared in `_CONTEXT.md` "Scope Traceability" and the companion deliverable
register:

- SOW-032 — "Governed work is structured as execution instances containing flat
  packages and deliverables with stable IDs, a canonical lifecycle state file,
  and human-triaged staleness propagation." SourceRef: PRD §5.2 O-7
  (transcribed).
- OBJ-002 — governed production of professional knowledge work, in which a
  complete deliverable stream runs from decomposition through package and
  deliverable to a checking and issuance decision, with every consequential
  judgment made by an accountable human. Structural and lifecycle conformance is
  what makes that stream legible: without a flat structure, stable IDs, and one
  canonical state file, there is no reliable answer to what state any piece of
  work is in.

This document is a production contract, not an acceptance record. Every
definition below is a candidate grounded in the accepted decomposition, this
deliverable's `_CONTEXT.md`, the scope-ledger statement of SOW-032, and the
adopted PRD. Nothing here asserts a lifecycle state or an acceptance judgment.

## Deliverable Definition — Ontology

Three anticipated artifacts, transcribed from the register and `_CONTEXT.md`.

- **OUT-001** — Structure conformance report. A record of whether the execution
  instance holds flat packages and deliverables at the expected layout, whether
  each deliverable carries its required metadata fileset, and whether the
  identifiers in use are stable and internally consistent with their folders.
- **OUT-002** — Lifecycle-state conformance notes. A per-deliverable note on
  whether `_STATUS.md` exists, parses to exactly one state drawn from the
  canonical set, and remains the sole state-bearing surface, with any competing
  state assertion elsewhere named.
- **OUT-003** — Staleness triage record. A record of staleness signals raised
  against governed work and the human triage disposition of each, preserving
  that propagation is triaged rather than automatic.

- **CLM-001** — The structure in scope is flat: packages contain deliverables
  without an intervening hierarchy, and stable IDs rather than folder position
  carry identity. This restates SOW-032 (PRD §5.2 O-7).
- **CLM-002** — Exactly one file is canonical for lifecycle state. A second
  surface asserting state is a conformance defect, not an alternative reading.
  This restates SOW-032 (PRD §5.2 O-7).
- **CLM-003** — Staleness propagation is human-triaged. An automatic cascade
  that dispositions staleness without a human decision would not satisfy
  SOW-032; the triage step is part of the obligation, not an implementation
  preference.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — Governed work shall be structured as execution instances
  containing flat packages and deliverables, each deliverable carrying its
  required metadata fileset. Obligation restated from SOW-032, SourceRef PRD
  §5.2 O-7.
- **REQ-002** — Identifiers shall be stable and consistent between a
  deliverable's declared identity and its folder identity. Obligation restated
  from SOW-032, SourceRef PRD §5.2 O-7.
- **REQ-003** — Each deliverable shall carry one canonical lifecycle state file
  resolving to exactly one state from the canonical set, and no other file shall
  determine that state. Obligation restated from SOW-032, SourceRef PRD §5.2
  O-7.
- **REQ-004** — Staleness propagation shall be triaged by a human, with the
  disposition recorded. Obligation restated from SOW-032, SourceRef PRD §5.2
  O-7.

- **AC-001** — OUT-001 covers every deliverable in the execution instance and
  records, for each, the fileset result and the identity-consistency result,
  with each failure named rather than summarized away.
- **AC-002** — OUT-002 records, for every deliverable, a lifecycle state that
  parses to exactly one canonical value, and names any competing state assertion
  found outside the canonical file.
- **AC-003** — Every staleness signal in OUT-003 carries a named human
  disposition; no signal is closed by tool action alone.

Reliance basis: OUT-001 rests partly on deterministic tool output and partly on
human review, because the repository's structural checks are per-deliverable and
do not by themselves establish instance-wide coverage. OUT-002 and OUT-003 rest
on human review; see CON-002. No artifact here carries acceptance until a human
accepts it.

## Production and Verification Method — Praxeology

Production is: enumerate the execution instance, run the existing per-deliverable
checks across it, record results including failures, and take the lifecycle and
staleness questions to human review where no deterministic surface exists.

- **VER-001** — For each deliverable folder, execute
  `bash tools/validation/check_min_viable_fileset.sh <deliverable folder>` and
  record the result line and exit status. This is the deterministic signal for
  the metadata-fileset half of REQ-001.
- **VER-002** — For each deliverable folder, execute
  `python3 tools/validation/scan_deliverable_consistency.py <deliverable folder>`
  and record the emitted report, reading its identity-mismatch and
  missing-core-file findings as the deterministic signal for REQ-002 and the
  remainder of REQ-001.

Where no deterministic surface exists, the matrix carries an explicit
`HUMAN_REVIEW` method rather than a fabricated command. That applies to OUT-002
and OUT-003. For OUT-003 this is not merely a gap: REQ-004 requires the
disposition to be human, so human review is the correct method rather than a
substitute for a missing tool.

- **CON-001** — Identifier-width disagreement between live checks. The
  repository's `tools/validation/validate_id_format.sh` enforces three-digit
  package and deliverable segments, and rejects this project's own accepted
  identifiers, including this deliverable's. The Scope-of-Work schema instead
  admits two-or-three-digit segments, and the governing standard states that
  exact widths come from the active decomposition rather than from a fixed
  pattern. That checker is therefore not cited as a verification method here.
  The disagreement bears directly on REQ-002 and is recorded for human ruling,
  not resolved in this document.
- **CON-002** — Verification gap. No deterministic check was found that
  validates lifecycle-state files across the execution instance against the
  canonical state set and transition rules, and none that records staleness
  triage. OUT-002 and OUT-003 therefore verify by human review.

## Governing Values and Decisions — Axiology

- **AX-001** — Grounding discipline. Every definition above traces to this
  deliverable's register row, its `_CONTEXT.md`, the scope-ledger statement of
  SOW-032, or the adopted PRD. Nothing is inferred, and unknowns stay marked.
- **AX-002** — Write-locus boundary. The register records this deliverable's
  `AnticipatedWriteLocus` as the execution tree only. Nothing in this document
  authorizes a change to the instruction surface; any such act, including
  amending or replacing the checker named in CON-001, requires an independently
  authorized M2 tranche, which this document does not grant.
- **AX-003** — Lifecycle neutrality. This contract asserts no lifecycle state
  and no acceptance. Lifecycle authority remains each deliverable's `_STATUS.md`,
  which this work reads and does not write, and acceptance remains a human
  judgment.
- **AX-004** — Human triage is a feature, not a cost. Where the obligation names
  a human disposition, automating it away would defeat the requirement rather
  than satisfy it more efficiently.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-032 OBJ-002 | REQ-001 REQ-002 CLM-001 | AC-001 | VER-001 VER-002 | Per-deliverable record of command, result line, and exit status, plus an enumeration showing instance-wide coverage and every failure named |
| OUT-002 | SOW-032 OBJ-002 | REQ-003 CLM-002 | AC-002 | HUMAN_REVIEW: reviewer checks each deliverable's lifecycle state file against the canonical format, the canonical state set, and the transition-authority rules, and confirms no other file asserts state | Per-deliverable note of the parsed state, the format check, and any competing state assertion found elsewhere |
| OUT-003 | SOW-032 OBJ-002 | REQ-004 CLM-003 | AC-003 | HUMAN_REVIEW: a human triages each staleness signal and records the disposition and its reason, this being the obligation itself rather than a fallback for a missing tool | Signal-by-signal record of source, affected work, named human disposition, reason, and date |
