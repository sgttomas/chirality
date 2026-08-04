# Sealed Agent 2 brief — AUTHOR remediation 1

- Applies to: new immutable `OWNER_SELECTION_V2` candidate package
- Predecessor V1: immutable; do not edit, move, delete, or overwrite
- Refuter return: SHA-256
  `a5340f2f7396aa3d08ff0bffe6b960abd4d15e93a70bd20d3638efa3e9408a49`
- Authority and selection: unchanged from the original AUTHOR brief

## Objective

Create a complete new six-file V2 package plus V2 application trace that
preserves every V1 selected semantic and closes exactly these two admitted
refuter findings:

1. `REFUTER-F01`: make the four-state transition relation deterministic by
   explicitly specifying the pre-scan failure transition from
   `RECOVERY_REQUIRED` to `RECOVERY_BLOCKED` when safe single-writer ownership
   or the exact corpus basis cannot be established. This is a direct
   completeness application of selected `TBD-016-A` and D4-A; do not add a new
   state or relax fail-closed behavior.
2. `REFUTER-F02`: require the one immutable compatibility binding manifest to
   bind the exact identities of all six accepted semantic-contract members
   and the exact V2 package manifest, in addition to source, release, clients,
   evidence, and disposition. This is a direct completeness application of
   selected `TBD-004-A`; do not narrow or alter selected package semantics.

## Outputs and writes

Write only:

- `candidate_v2/**` — exactly the six planned candidate files, with V2 headers;
- `application_trace_v2/SELECTION_APPLICATION_TRACE.md`;
- `remediation/AUTHOR_RETURN.md`.

Update the V2 trace to cite both findings and their exact resolved clauses.
Recompute all V2 hashes. Preserve 27/27 selection, the allowed tuple, all
unselected-option records, owner boundaries, N3 unexecuted posture, future
epoch placeholder, conditional compatibility delta, and every no-effect and
implementation gate. Agent 2 shall not delegate.

All original tools, exclusions, source identities, and no-implementation
limits remain sealed. Any new ambiguity or required semantic choice returns
to WORKING_ITEMS; do not repair V1 or any source/history file.
