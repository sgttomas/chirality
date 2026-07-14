# Clean Scope-of-Work Production Handoff

Status: `COMPLETE — HOLD_FOR_HUMAN`
Closure verdict: `IMPLEMENTED_VALIDATED_COMMITTED`

## Accepted upstream basis

- Human direction recorded in `HUMAN_DIRECTION.md`.
- Root basis: `main@7fea3356b465633dbf4b30cb61d547bfc978ccec`.
- Active Stage-2 plan remains the standing workplan; amendment
  `CLEAN-SOW-PRODUCTION-001` governs every unintegrated candidate.

## Result

The workflow now distinguishes an evidence-rich migration candidate from the
clean production contract. A registered deterministic finalizer externalizes
migration-only metadata, preserves literal source content as quotations, and
binds evidence and production hashes. Mapping and parity can require exact
production finalization; checklist and HTML consumers operate on clean
production only. The existing 60 prepared candidates pass compatibility.

Implementation commit:
`8a8a3ee79aa8daa0a9909d7d624ad691530bfbc9`.

## Derivative status and rerun requirements

All migration candidates, finalization reports, maps, parity reports,
checklists, corpus checks, and this handoff are derivative evidence. They do
not accept project content or lifecycle state.

Before any prepared candidate is integrated, rerun finalization and all
downstream checks from its current evidence candidate and bind the clean
production hash in the replacement manifest. Do not reuse earlier target-hash,
checklist, render, or integration evidence as if it already covered the clean
artifact.

## Remaining gates

- Piping execution remains stopped pending a later human instruction.
- H1/H2, lifecycle acceptance, integration, and legacy retirement remain
  parked at their existing human gates.
