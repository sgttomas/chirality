# Scope-of-Work Stage-1 Handoff State

Status: `STAGE1_PASS_AWAITING_D-GOV-16_RULING`

## Accepted upstream basis

- Frozen root main: `2770fda4c63c98ee9f18cffbafd14c9aa59f497f`.
- D-GOV-15 published ruling:
  `58aa81d62f4a32e3c2d687e4356a1e4be8141674`, including its owner-authorized
  deterministic-checklist addendum.
- App pilot evidence branch/commit:
  `codex/sow-app-pilot@fb83ffca8a7f674db13c6cda775ca7b7d7c8ef26`.
- Piping pilot evidence branch/commit:
  `codex/sow-piping-pilot@31c35ea9798c29cd0af16b7089186f3942dcfcb1`.
- Stage-1 proposal/evidence snapshot:
  `31e5efd986b7c59fc709f4fe967575c59659aae0` on
  `codex/sow-stage1-execution`.

## Closure verdict

Stage 1 is `PASS`. All ten authorized candidates passed independent
preservation audit: 325/325 claim mappings are `PRESERVED`, 3,466/3,466 source
lines are covered, the 40 legacy sources and ten statuses are byte-identical
to the frozen basis, all pilot lifecycle states remain `IN_PROGRESS`, and no
fresh conversion or verifier rerun was required. Schema, project content, and
preservation pass; authorized serialized conversion fallback is separately
reported from native verifier PASS.

The owner-authorized governance correction replaced repeated agentic checklist
extraction with a deterministic `AC-*` compiler and a REVIEW exact-consumer
contract. Ten-pilot reproduction passes byte-for-byte. The full evidence is
derivative and does not replace deliverable, decomposition, lifecycle, or
human-decision truth.

## D-GOV-16 decision package

`docs/governance_harness/_DECISIONS/D-GOV-16_deliverable_scope_of_work_stage2.md`
is `PROPOSED — NO EFFECT WITHOUT OWNER RULING`, bound to the proposal snapshot
above. Its evidence index and exact inactive successor-standard/TYPES/SPEC
proposal artifacts reside under `docs/governance_harness/_PROPOSALS/D-GOV-16/`.
The proposal revision preserves the originally proposed target bytes and changes
only the two patch artifacts to a whitespace-clean zero-context representation;
they require `git apply --unidiff-zero --check` against the frozen base.

## Remaining blocker and stop

Only an explicit owner D-GOV-16 ruling can release the proposed canon,
conversion, ISSUED-handling, pilot-replacement, and legacy-transition lanes.
Until then, Stage 2 is not implemented; `docs/TYPES.md` and `docs/SPEC.md`
remain ratified unchanged; no remaining-corpus conversion starts; no candidate
pilot is merged into `main`; and no lifecycle change occurs.

## Rerun requirements

If a relied-on pilot candidate/source/status, frozen parser/catalog/checklist
contract, proposal text, or accepted basis changes before ruling or execution,
re-run the affected validator, claim map, parity, HTML, checklist, verifier,
and RECONCILIATION fan-in. Otherwise no Stage-1 rerun is required.
