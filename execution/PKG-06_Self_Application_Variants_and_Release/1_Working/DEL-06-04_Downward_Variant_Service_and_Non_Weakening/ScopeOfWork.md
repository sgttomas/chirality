---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-06-04
package_id: PKG-06
decomposition_basis: execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md@653fabc9b3e8abf369f5e776a7d3ee24bf235e7a
project_scope_refs: [SOW-067, SOW-068, SOW-069, SOW-075]
package_objective_refs: [OBJ-005]
---

# Scope of Work — DEL-06-04

## Purpose and Objective Traceability

DEL-06-04 (`REQ_SLICE`) serves project scope SOW-067, SOW-068, SOW-069, and
SOW-075, and package objective OBJ-005. Its purpose, transcribed from the
accepted deliverable register, is to keep one instruction root serving many
working roots without per-workspace drift, to keep working roots free to extend
the invariant catalog and specialize the agent suite but never to weaken
framework governance, and to keep the root working-root exception uninherited
by any variant.

OBJ-005 in `docs/PRD_ROOT.md` §3 is "situated specialization with governed
convergence". This deliverable covers the **downward** half of that relation —
root serving variants (`docs/PRD_ROOT.md` §7.1). The upward half, governed
promotion (§7.2), is a separate scope surface and is not defined here.

`_CONTEXT.md` sets the context envelope to `M` with the note "one relation
across an enumerated set of working roots". The unit of work is therefore one
relation checked across an enumerated variant set, not a per-variant
remediation programme.

Every definition below is grounded in the deliverable-register row for
DEL-06-04, this deliverable's `_CONTEXT.md`, the scope-ledger statements for
the four covered scope items, and the adopted `docs/PRD_ROOT.md`. Acceptance
criteria and verification methods are **candidates for owner review**; this
contract claims no acceptance and no lifecycle state.

## Deliverable Definition — Ontology

The three anticipated artifacts transcribed from the register
(`AnticipatedArtifacts`) and from `_CONTEXT.md ## Anticipated Artifacts` are:

- **OUT-001** — Variant conformance checklist: the enumerated working-root set
  with, per variant, whether it runs on the one instruction root without
  per-workspace instruction drift.
- **OUT-002** — Non-weakening check: per variant, the recorded extensions to the
  invariant catalog and the agent-suite overlays or specializations, each
  classified as an extension/specialization or as a candidate weakening of
  framework governance.
- **OUT-003** — Exception non-inheritance evidence: evidence that no variant
  inherits the root working-root exception and that the exception extends to no
  other working root or to desktop-selected folders.

- **CLM-001** — SOW-067 (SourceRef `PRD §7.1 [TRANSCRIBED]`) records that one
  instruction root serves many working roots without per-workspace instruction
  drift. `docs/PRD_ROOT.md` §7.1 enumerates the classes of working root as
  `projects/*`, `domains/*`, and desktop-harness user-selected folders.
- **CLM-002** — SOW-068 (SourceRef `PRD §7.1 [TRANSCRIBED]`) records that a
  working root may extend the invariant catalog and may overlay or specialize
  the agent suite, but must not weaken framework governance.
- **CLM-003** — SOW-069 (SourceRef `PRD §7.1 [TRANSCRIBED]`) records that no
  variant inherits the root working-root exception and that the exception
  extends to no other working root.
- **CLM-004** — SOW-075 is a boundary item recorded `OUT` of scope
  (SourceRef `PRD §8.1 [TRANSCRIBED non-goal]`, DecisionRef DEC-007): no
  extension of the root working-root exception to any other working root or to
  desktop-selected folders. It bounds this deliverable rather than assigning it
  production; OUT-003 evidences that the boundary held and proposes no
  extension.
- **CON-001** — The scope ledger maps SOW-069 to `ObjectiveIDs` OBJ-004, while
  this deliverable's `_CONTEXT.md ## Scope Traceability` declares OBJ-005 as the
  package objective. This contract uses the `_CONTEXT.md` value, as required,
  and records the divergence rather than reconciling it. Reconciliation is an
  owner act. SOW-075 carries no `ObjectiveIDs` value, consistent with its `OUT`
  boundary status.

## Completion and Reliance Basis — Epistemology

- **REQ-001** — Per SOW-067, the variant set shall be enumerated explicitly from
  the checkout before the relation is checked, and the enumeration basis shall be
  stated. A variant absent from the enumeration is a coverage gap to report, not
  an implicit pass.
- **REQ-002** — Per SOW-067, "without per-workspace instruction drift" shall be
  assessed against the one instruction root as the single basis; a
  workspace-local instruction copy that has diverged from that basis is recorded
  as drift with the diverging surface named.
- **REQ-003** — Per SOW-068, each recorded variant extension or overlay shall be
  classified as (a) an extension of the invariant catalog, (b) an overlay or
  specialization of the agent suite, or (c) a **candidate weakening** of
  framework governance. Class (c) is reported for owner ruling and is never
  resolved, waived, or repaired by this deliverable.
- **REQ-004** — Per SOW-069 and the SOW-075 boundary, the non-inheritance
  evidence shall cover every enumerated variant and shall state, per variant,
  that the root working-root exception is not claimed, relied upon, or extended
  there. Silence in a variant is not evidence of non-inheritance; an absent
  record is reported as unevidenced.
- **REQ-005** — Per CLM-004, this deliverable shall propose no extension of the
  root working-root exception and shall recommend no change to any variant's
  governance posture; its outputs are observational and advisory to the owner.

- **AC-001** — The conformance checklist enumerates the working-root set from a
  stated checkout-derived basis and records, per variant, a determinate verdict
  on service by the one instruction root without per-workspace instruction
  drift, with any diverging surface named.
- **AC-002** — The non-weakening check classifies every recorded variant
  extension and agent-suite overlay into exactly one of the three REQ-003
  classes, and every class (c) item is reported unresolved for owner ruling with
  the governing clause it appears to weaken cited.
- **AC-003** — The non-inheritance evidence covers every enumerated variant,
  distinguishes "evidenced as not inherited" from "unevidenced", and records no
  extension of the exception to any working root or desktop-selected folder.

## Production and Verification Method — Praxeology

Production enumerates the working roots from the checkout, reads each variant's
instruction entrypoints and any invariant-catalog extension or agent-suite
overlay it declares, compares them against the one instruction root, and writes
the three artifacts inside this deliverable folder. Variant surfaces are
read-only inputs: this deliverable does not edit, normalize, or repair any
working root, and it does not touch the instruction root.

- **VER-001** — Enumerate the variant set deterministically and bind it to the
  checklist: list the working-root directories under `projects/` and `domains/`
  (`git ls-files 'projects/*' 'domains/*'` reduced to first-level directories)
  and confirm the checklist's variant set equals that enumeration, with
  desktop-harness user-selected folders recorded as an unenumerable class rather
  than omitted silently.
- **VER-002** — Execute `python3
  tools/validation/validate_instruction_entrypoints.py` (root instruction
  entrypoints and the import contract) and `python3
  tools/validation/validate_agent_instructions.py` (the mechanically observable
  `AGENT_*.md` instruction contract), and record each exit status and message as
  evidence for the single-instruction-root and drift findings. A guard result is
  evidence for a verdict; it is not the verdict, and it makes no judgment about
  whether an overlay weakens governance.

## Governing Values and Decisions — Axiology

- **AX-001** — Specialize downward, never weaken. Per SOW-068, extension and
  specialization are permitted and weakening is not; the check therefore
  separates the two rather than scoring variants for conformity in general.
- **AX-002** — Weakening is a judgment, not a scan. Whether an overlay weakens
  framework governance is a semantic question reserved for the owner. REQ-003
  class (c) exists so that candidates are surfaced with their evidence rather
  than silently absolved by a passing mechanical check.
- **AX-003** — The exception does not travel. Per SOW-069 and the SOW-075
  boundary item (DEC-007), the root working-root exception is uninherited and
  unextended. This contract records that state and grants no extension of it.
- **AX-004** — Unevidenced is not compliant. Per REQ-004, absence of a claim in
  a variant is reported as unevidenced rather than counted as non-inheritance.
- **AX-005** — This deliverable's `AnticipatedWriteLocus` is `execution-tree`
  and this contract grants no instruction-surface authority. Any act that would
  change `AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`, `init/`, or
  `.github/workflows/` — including any change to the one instruction root that a
  drift finding might suggest — requires an independently authorized M2 tranche,
  which this contract does not grant.
- **AX-006** — Nothing is inferred where the accepted decomposition is silent
  (K-INVENT-1). `_CONTEXT.md ## Acceptance Criteria` records `TBD`; AC-001
  through AC-003 are candidate criteria derived only from the authorized
  grounding sources and remain subject to owner review.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-067 OBJ-005 | CLM-001 REQ-001 REQ-002 | AC-001 | VER-001 VER-002 | Conformance checklist plus the variant enumeration output and the captured entrypoint and agent-instruction validator results |
| OUT-002 | SOW-068 OBJ-005 | CLM-002 REQ-003 REQ-005 | AC-002 | HUMAN_REVIEW: owner reads each recorded extension and overlay against PRD §7.1 and rules on every candidate-weakening item, which no mechanical check may absolve | Per-variant classification table, the cited governing clause for each candidate weakening, and the owner's recorded ruling |
| OUT-003 | SOW-069 SOW-075 OBJ-005 | CLM-003 CLM-004 CON-001 REQ-004 REQ-005 | AC-003 | HUMAN_REVIEW: owner confirms per variant that the root working-root exception is neither claimed nor extended, and that unevidenced cases are recorded as unevidenced rather than as compliant | Per-variant non-inheritance evidence with evidenced / unevidenced dispositions and the reviewer's recorded disposition |
