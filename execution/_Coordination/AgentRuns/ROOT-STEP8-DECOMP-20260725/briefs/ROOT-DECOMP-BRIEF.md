# Sealed Brief — N1: Candidate first root decomposition (ROOT-STEP8-DECOMP-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: Agent 1 instance in
the **SOFTWARE_DECOMP** role, `opus-5`. One objective; terminal return; no
further delegation (run the phases inline).

## Role and instruction stack

Load and conform to, in this precedence order:

1. `docs/DECOMPOSITION_STANDARD.md` (RATIFIED; PROTOCOL > SPEC > STRUCTURE >
   RATIONALE; conflicts surfaced, never silently reconciled)
2. `agents/AGENT_SOFTWARE_DECOMP.md` (your role file; its ID formats and
   Context Envelope discipline apply)
3. This brief (adapts the role to the root product; where the software-SOW
   framing strains against the root product's nature, conform to the
   standard and record the strain in Open Issues — do not silently adapt
   and do not invent a new method)

## Objective

Author the **CANDIDATE** first decomposition of the **Chirality Root
product** from the adopted PRD, per D-GOV-21 §6 step 8. The product is the
repository root product defined by `docs/PRD_ROOT.md` (adopted through
D-GOV-22): the canonical human-governed application environment and
generative operating form for governed professional knowledge work,
constituted by four functional categories (PRD §4.1): normative basis,
operative product, developmental machinery, evidence.

This is a candidate only. **All seven gates are human-gated (I1) and NONE is
accepted in this run.** Stage every gate's outputs; mark every Gate Log row
`PENDING_OWNER_RULING`. The owner will rule over the exact committed
candidate (K-AUTH-2 vehicle). Claim no acceptance anywhere.

## Source discipline (D-9 — binding)

- The **sole scope source** is `docs/PRD_ROOT.md` at the current basis: its
  objectives OBJ-1..OBJ-7 (§3), categories (§4), stable requirements §5
  (N-*, O-1..O-10, D-1..D-16, E-*), self-application direction (§6),
  variant/promotion direction (§7), non-goals and falsifiers (§8), ruled
  owner decisions (§9), and source-concordance obligations (§10, incl.
  D-14's "the check is not built" precondition).
- Documents the PRD incorporates by reference (`AGENTS.md`,
  `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`,
  D-GOV-21 §5) are **interpretive context** for understanding what a
  commitment requires — they generate no scope items of their own.
- Nothing from discussion, from this brief's framing, or from your own
  judgment about what the product "should" include may create scope. Where
  the PRD is silent or ambiguous: `TBD` + Open Issue (I2), never invention.
- Respect provenance labels: PROPOSED commitments (D-13, D-14, D-15, D-16)
  are lawful trace targets but their PROPOSED status must be visible in the
  ledger/mapping wherever relied on.

## Coverage obligations

- **D-15**: demonstrated coverage across all four §4.1 categories — each
  category has decomposition coverage or a recorded, reasoned deferral. The
  categories are non-exclusive functions, NOT four prescribed packages
  (§4.3); your partition is yours to propose under the standard.
- **F4 (falsifier — your candidate must not trip it)**: bidirectional
  traceability. Every proposed scope unit traces to at least one PRD
  requirement or objective; every PRD objective (OBJ-1..7) and every §5
  commitment has either coverage or a recorded, reasoned deferral. Provide
  this as an explicit machine-checkable mapping register, both directions.
- D-12: developmental machinery is product scope — decompose it, don't
  exempt it. E-* evidence commitments likewise.

## Output format and location

Write a conforming decomposition **package** (working surface + authoritative
companion registers, every artifact carrying its package-role label) under
root `execution/_Decomposition/` (new directory; control-plane, lawful —
no `PKG-*`/`DEL-*` folders are created by decomposition truth):

- Working surface: `execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md`
  with the full section set your role file and the standard require (Gate
  Log, References, Intake Summary, Vocabulary Map, SSOW/atomic units,
  Objectives, Packages, Deliverables, Scope Ledger, Coverage & Telemetry,
  Open Issues, Decision/Change Log, Downstream Execution Notes). Study
  `projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
  as the structural precedent (including its §10A-style control coverage);
  do not copy its content.
- Companion registers (CSV or structured md, your role's convention) for the
  heavy machine truth: scope ledger, objective/requirement mapping (both
  directions — the F4 register), coverage telemetry. Reference them from
  the working surface; do not duplicate full ledgers inline.
- References section: pin `docs/PRD_ROOT.md` by path + sha256 + the basis
  commit SHA; list interpretive-context documents separately, clearly
  labeled non-source.

Format constraints:

- IDs per `docs/SPEC.md` §1 and your role file: `PKG-XX_{PkgLabel}`,
  `DEL-XX-YY_{DelLabel}`; stable (I5); deterministic DEL↔PKG coupling (I6).
- **G2 readiness**: every PKG and DEL identifier string must appear verbatim
  in the working surface — they will later be used as literal
  `decomposition_ref` substrings by
  `tools/validation/validate_root_surface_ownership.py`. See
  `../evidence/GUARD_STATE_SPEC.md`.
- Each DEL carries: Type (your role's taxonomy), AnticipatedArtifacts,
  CoversScopeItems, SupportsObjectives, ContextEnvelope (S|M|L|XL sized for
  a bounded Agent 2 execution).
- For each DEL, note anticipated write-target locus (root `execution/`
  package tree vs instruction-surface targets needing M2 tranches) so the
  later G2/G3 state instantiation can be derived without reinterpretation.
  Anticipated targets are planning notes, not authorization.
- `UnassignedINUnits` must be 0 in telemetry; unknowns are `TBD` + Open
  Issue, not gaps.
- Machine-absolute paths prohibited everywhere.

## Sizing guidance (judgment, not quota)

Propose the partition you can defend under I3/I4 (flat, no overlap, no
gaps). The PRD carries 7 objectives and 42 commitments; the product is one
repository. Prefer the smallest package set that keeps ownership boundaries
clean and deliverables dispatchable within their Context Envelopes. Do not
pad; do not force four packages to mirror the four categories (§4.3
prohibits reading them as a partition).

## Hard scope limits

- Write ONLY: new files under `execution/_Decomposition/`, and your terminal
  return at
  `execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/returns/N1_RETURN_RAW.md`.
- Create NO `PKG-*`/`DEL-*` directories anywhere; touch NO instruction
  surface (`AGENTS.md`, `agents/`, `skills/`, `tools/`, root `docs/`,
  `init/`, `.github/`); write NOTHING under `execution/_harness/`; no
  `INIT.md`; no commits, no branches — leave the working tree for Agent 0
  fan-in.
- Read scope: unrestricted within the repo.

## Verification before returning

Run and report honestly:

- `python3 tools/validation/validate_path_anchors.py`
- `python3 tools/validation/validate_root_materialization_fence.py` (expect
  PASS idle — you created no PKG/DEL structure)
- `git status --porcelain` (confirm writes are exactly in scope)
- Your own F4 check: script or table proving both trace directions closed
  (every OBJ/N/O/D/E covered or deferred; every PKG/DEL tracing back).

## Terminal return (`N1_RETURN_RAW.md`, and return the same content)

Files created; partition summary (PKG list with one-line scope each; DEL
counts per PKG); the four-category coverage demonstration (D-15) with any
deferrals and reasons; F4 closure statement with the register location;
open issues (including every framing strain); verification results verbatim;
constraint confirmations.
