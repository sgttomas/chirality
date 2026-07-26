---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-01
package_id: PKG-03
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-020, SOW-031]
package_objective_refs: [OBJ-004, OBJ-007]
---

# Scope of Work — DEL-03-01

## Purpose and Objective Traceability

This deliverable keeps the two-root path model, the ScopePath containment rule,
and the closed root-token registry enforced across the root product, so that
every scope path and write target resolves under the active checkout or the task
stops, and so that no machine-absolute path is embedded in an instruction,
coordination, or plan file.

It covers two project scope items and supports one package objective, exactly as
declared in `_CONTEXT.md` "Scope Traceability" and the companion deliverable
register:

- SOW-020 — "Every scope path and write target resolves under the active
  checkout or the task stops." SourceRef: PRD §5.1 N-5 (transcribed).
- SOW-031 — "The path model defines two roots, one containment rule, and a
  closed root-token registry, and instruction, coordination, and plan files must
  not embed machine-absolute paths." SourceRef: PRD §5.2 O-6 (transcribed).
- OBJ-007 — file-native continuity and recoverability. Containment and
  path-token discipline are what make the governed state recoverable from the
  checkout alone: a path that escapes the checkout, or a machine-absolute path
  baked into a live surface, is state that does not survive relocation.

This document is a production contract, not an acceptance record. Every
definition below is a candidate grounded in the accepted decomposition, this
deliverable's `_CONTEXT.md`, the scope-ledger statements of its covered items,
and the adopted PRD. Nothing here asserts a lifecycle state or an acceptance
judgment; both remain human acts recorded elsewhere.

## Deliverable Definition — Ontology

The deliverable is conformance work over an existing rule set, evidenced by
three anticipated artifacts transcribed from the register and `_CONTEXT.md`.

- **OUT-001** — Path-anchor validation runs. Recorded executions of the
  repository's path-anchor check over the live instruction, coordination, and
  plan surfaces, capturing the command, the surface count scanned, and the
  pass/fail result for each run.
- **OUT-002** — Containment test evidence. Evidence that a `ScopePath` or
  declared write target resolving outside the active checkout — including via
  symlink or `..` traversal — is rejected and the task stops rather than
  writing, covering the worktree case in which an agent could otherwise write
  back to the main checkout.
- **OUT-003** — Token-registry conformance note. A reconciliation of the closed
  `{*_ROOT}` token registry against live `{*_ROOT}` token use on the governed
  surfaces, recording each token's declared anchor, its observed use, and any
  token used without a registry entry.

- **CLM-001** — The path model in scope is two-rooted: an active-checkout root
  and an active-workspace root, with one containment rule binding both. This
  restates SOW-031 (PRD §5.2 O-6) and is descriptive of the accepted basis, not
  a new design proposal.
- **CLM-002** — Containment is architectural rather than advisory: the stop
  behaviour on an out-of-checkout path is the deterministic backstop, not a
  warning. This restates SOW-020 (PRD §5.1 N-5).

## Completion and Reliance Basis — Epistemology

- **REQ-001** — Every `ScopePath` and every declared write target shall
  normalize and resolve under the active checkout; one that resolves outside it
  shall be rejected and the task shall stop rather than write. Obligation
  restated from SOW-020, SourceRef PRD §5.1 N-5.
- **REQ-002** — The path model shall define exactly two roots, one containment
  rule, and a closed root-token registry, and any token in live use shall have a
  registry entry with a declared anchor. Obligation restated from SOW-031,
  SourceRef PRD §5.2 O-6.
- **REQ-003** — Instruction, coordination, and plan files shall not embed
  machine-absolute paths. Obligation restated from SOW-031, SourceRef PRD §5.2
  O-6.

- **AC-001** — The path-anchor check runs over the live surfaces and reports no
  machine-absolute path, with the run recorded under OUT-001.
- **AC-002** — For each of the out-of-checkout cases in scope — plain outside
  path, `..` traversal, and symlink escape — OUT-002 records the rejection and
  the stop, with no write performed.
- **AC-003** — OUT-003 accounts for every `{*_ROOT}` token observed in live use
  against the closed registry, with each unregistered token listed rather than
  silently accepted.

Reliance basis: OUT-001 is deterministic tool output and may be relied on as
evidence of the machine-absolute-path obligation alone. OUT-002 and OUT-003 rest
on human review, because the repository holds no deterministic containment-
rejection check and no deterministic token-registry check at this basis; see
CON-002. No artifact here carries acceptance until a human accepts it.

## Production and Verification Method — Praxeology

Production is: run the existing check, record the result, construct the
containment cases, reconcile the token registry, and report gaps as gaps.

- **VER-001** — Execute `python3 tools/validation/validate_path_anchors.py .`
  and record the verbatim result line and exit status. Exit 0 with a pass line
  is the deterministic signal for REQ-003.
- **VER-002** — Execute
  `python3 -m pytest tools/validation/test_validate_path_anchors.py` and record
  the result, confirming the checker used for VER-001 is itself exercised by its
  registered regression surface rather than trusted unverified.

Where no deterministic surface exists, the matrix carries an explicit
`HUMAN_REVIEW` method instead of a fabricated command. That applies to OUT-002
and OUT-003.

- **CON-001** — Objective linkage disagreement across grounding sources. The
  scope-ledger row for SOW-020 records OBJ-004 in its own objective column,
  while this deliverable's `_CONTEXT.md` and register row declare OBJ-007. The
  frontmatter carries OBJ-007 per `_CONTEXT.md` as instructed. The disagreement
  is recorded, not resolved here; resolution is a human ruling. **Ruled
  (D-GOV-27, 2026-07-25): additive propagation** — the ledger mapping stands,
  the register and this frontmatter gained OBJ-004, and this divergence is
  closed.
- **CON-002** — Verification gap. No deterministic check for containment
  rejection or for token-registry closure was found in the repository at this
  basis. OUT-002 and OUT-003 therefore verify by human review. Whether to build
  such a check is a separate question and is not authorized by this document;
  see AX-002.

## Governing Values and Decisions — Axiology

- **AX-001** — Grounding discipline. Every definition above traces to this
  deliverable's register row, its `_CONTEXT.md`, the scope-ledger statements of
  SOW-020 and SOW-031, or the adopted PRD. Nothing is inferred from convenience,
  and unknowns stay marked rather than filled in.
- **AX-002** — Write-locus boundary. The register records this deliverable's
  `AnticipatedWriteLocus` as the execution tree plus `tools/` if a check must
  change. `tools/` is part of the instruction surface. Any act that modifies it
  requires an independently authorized M2 tranche. This document grants no such
  authorization, and nothing in CON-002 should be read as licence to add or
  amend a checker under this scope.
- **AX-003** — Lifecycle neutrality. This contract asserts no lifecycle state
  and no acceptance. Lifecycle authority remains the deliverable's `_STATUS.md`,
  which this document does not touch, and acceptance remains a human judgment.
- **AX-004** — Evidence over assertion. A conformance claim is worth what its
  recorded run is worth; a gap is reported as a gap rather than closed by
  narrative.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-031 OBJ-007 | REQ-003 CLM-001 | AC-001 | VER-001 VER-002 | Recorded command, scanned-surface count, verbatim result line, and exit status for each run |
| OUT-002 | SOW-020 OBJ-007 | REQ-001 CLM-002 | AC-002 | HUMAN_REVIEW: reviewer walks each constructed out-of-checkout case (plain outside path, `..` traversal, symlink escape) and confirms the recorded rejection and stop, with no write performed | Per-case record of the attempted path, the rejection, the stop, and the unchanged target |
| OUT-003 | SOW-031 OBJ-007 | REQ-002 CLM-001 | AC-003 | HUMAN_REVIEW: reviewer reconciles the note's token inventory against the closed root-token registry and confirms every live token is accounted for or listed as unregistered | Token-by-token table of declared anchor, observed use, and disposition, with unregistered tokens named |
