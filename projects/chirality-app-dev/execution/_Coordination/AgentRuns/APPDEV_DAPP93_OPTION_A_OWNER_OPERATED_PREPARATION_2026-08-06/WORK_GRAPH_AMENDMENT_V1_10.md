# Work-graph amendment v1.10 — R4.4 simplification

Authority: `R4_4_SIMPLIFICATION_AUTHORITY_ADOPTION.md`

Posture: `SINGLE_MANAGER_INTEGRATION — VERIFIER HELD`

Status: `ACTIVE`

## Nodes and ordering

1. `R44-CONTROL`: freeze and hash the authority adoption and this amendment.
2. `R44-INVENTORY`: enumerate the live command set and every in-runbook
   evidence parsing/manifest/range/crosscheck/verdict operation; classify each
   as preserve, replace, or remove.
3. `R44-INTEGRATE`: sole WORKING_ITEMS owner edits only the authorized affected
   prepared surfaces and necessary run-local cross-references. Preserve
   C196/C197, C1145→C1144→C1130, and unaffected bytes.
4. `R44-MATRICES`: create exhaustive branch/precondition and required raw-byte
   producer/return matrices over the final bytes. Any unsatisfied row blocks
   freeze.
5. `R44-BACKCHECK`: mechanically verify identities, command uniqueness/range,
   exact literal operations, prohibited-parser absence, cross-surface
   agreement, whitespace/diff/frontend/App-only containment, and no-effect
   boundaries.
6. `R44-FREEZE`: write one immutable successor freeze and report exact hashes
   to HELP_HUMAN.
7. `R44-VERIFY`: held. No Agent 2 verifier dispatch until HELP_HUMAN explicitly
   accepts the stable successor freeze.

## Ownership and permissions

WORKING_ITEMS is the sole integration writer. No Agent 2 or EVALUATION child
is required for this bounded simplification. Reads are confined to the D-APP-93
run, accepted EVALUATION records, App loop controls, and static repository
checks. Writes are confined to owner-listed affected prepared surfaces and
necessary run-local control/cross-reference records. No packet, runtime,
debugger, package, helper, GUI, signal, credential, product, release, reliance,
Git mutation, Task Management, foreign-loop, or other action is permitted.

## Fan-in gates

- Every retained runbook action has exact enumerated bytes and satisfiable
  prerequisites.
- Evidence steps use only enumerated raw-byte capture, whole-file
  `/usr/bin/shasum -a 256`, and `/bin/cp -p` return operations; forbidden
  parsing/logic constructs are absent from future evidence-command bytes.
- Later ingestion owns manifest/range/completeness/exit/PASS crosschecks and
  terminal verdict over immutable returned bytes.
- All named failure classes terminate without invoking an impossible command.
- Frozen prepared bytes and matrices pass before a successor freeze exists.
