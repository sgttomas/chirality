# Sealed Brief — V1: Adversarial verification of the candidate root decomposition (ROOT-STEP8-DECOMP-20260725)

Issued by: `HELP_HUMAN` (Agent 0), 2026-07-25. Executor: ephemeral bounded
Agent 2 generalist, `opus-5`. One objective; no delegation; read-only except
the terminal return.

## Objective

Adversarially verify the CANDIDATE first root decomposition staged under
root `execution/_Decomposition/` by run node N1. Your job is to find
defects that would embarrass the owner's ruling, not to confirm the work.
Default skeptical: attempt to falsify each claim below and report what
survives.

## Checks (all required; report each PASS/FAIL/FINDING with evidence)

1. **F4 traceability, both directions** (PRD §8.2 F4). Independently
   reconstruct — do not trust N1's own register without checking it —
   that (a) every proposed PKG/DEL traces to at least one real PRD
   requirement or objective (verify cited IDs exist in `docs/PRD_ROOT.md`
   and actually support the scope claimed), and (b) every OBJ-1..7 and
   every §5 commitment (N-*, O-1..O-10, D-1..D-16, E-*) has coverage or a
   recorded, reasoned deferral. Enumerate the §5 IDs yourself from the PRD;
   report any commitment silently missing from both coverage and deferral.
2. **D-15 category coverage**: all four §4.1 categories covered or
   reasoned-deferred; the partition is NOT a forced mirror of the four
   categories (§4.3).
3. **D-9 no-invention scan** (I2): sample every PKG and at least half the
   DELs; flag any scope unit whose substance is not grounded in the PRD
   (invented from context documents, from the brief, or from judgment).
   Flag any scope drawn from incorporated-by-reference documents alone.
4. **Standard conformance**: I3 flat partitions; I4 every IN unit in
   exactly one partition (check the ledger mechanically); I5/I6 ID
   stability and coupling; I9 telemetry present with UnassignedINUnits=0
   and counts that actually reconcile against the registers (recount,
   don't trust); I10 vocabulary map present; required sections present;
   package-role labels on every artifact; no acceptance claimed anywhere
   (every gate PENDING_OWNER_RULING).
5. **SPEC ID format**: `PKG-XX_{Label}` / `DEL-XX-YY_{Label}` per
   `docs/SPEC.md` §1; G2 literal-containment readiness (every identifier
   appears verbatim in the working surface).
6. **Scope hygiene**: `git status --porcelain` shows writes only under
   `execution/_Decomposition/` and the run record; no `PKG-*`/`DEL-*`
   directories exist anywhere under root `execution/`; no instruction
   surface touched; `python3 tools/validation/validate_root_materialization_fence.py`
   exits 0; `python3 tools/validation/validate_path_anchors.py` exits 0.
7. **Candidate-posture hygiene**: no machine-absolute paths; References pin
   `docs/PRD_ROOT.md` by sha256 (verify the hash yourself with
   `shasum -a 256`); interpretive-context documents labeled non-source.

## Constraints

- Read anything; write ONLY your terminal return at
  `execution/_Coordination/AgentRuns/ROOT-STEP8-DECOMP-20260725/returns/V1_RETURN_RAW.md`.
- Run shell commands for verification only; modify nothing.
- Report findings with severity: BLOCKER (would trip a falsifier, violate
  an invariant, or misstate a fact to the owner), MAJOR (defect the owner
  should see before ruling), MINOR (cosmetic). An empty findings list must
  mean you looked and found nothing — list what you checked.

## Terminal return (`V1_RETURN_RAW.md`, and return the same content)

Per-check verdicts with evidence; findings by severity with exact
locations; the commitment-coverage recount table (or its location if you
write it as part of the return); overall verdict: CLEAN /
FINDINGS-NONBLOCKING / BLOCKERS-FOUND.
